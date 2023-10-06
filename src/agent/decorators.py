import functools
import json
import logging
import time
import uuid
from inspect import signature

import grpc
from google.protobuf import json_format  # noqa:

from rook.error_code import StatusCode

# logger for rpc client
logger = logging.getLogger("rpc_log")

DEFAULT_RPC_TIMEOUT = 30


def convert_grpc_error(err: grpc.RpcError) -> StatusCode:
    if err.code() == grpc.StatusCode.OK:
        return StatusCode.STATUS_SUCCESS
    elif err.code() == grpc.StatusCode.CANCELLED:
        return StatusCode.STATUS_RPC_CANCELLED
    elif err.code() == grpc.StatusCode.INVALID_ARGUMENT:
        return StatusCode.STATUS_RPC_INVALID_PARAMETER
    elif err.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
        return StatusCode.STATUS_RPC_DEADLINE_EXCEEDED
    elif err.code() == grpc.StatusCode.UNAVAILABLE:
        return StatusCode.STATUS_RPC_UNAVAILABLE
    elif err.code() == grpc.StatusCode.UNIMPLEMENTED:
        return StatusCode.STATUS_RPC_UNIMPLEMENTED
    else:
        return StatusCode.STATUS_RPC_UNKNOWN


def rpc_log(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        response = await func(*args, **kwargs)
        process_time = time.time() - start_time
        func_name = "{}.{}".format(func.__module__, func.__name__)
        sig = signature(func)
        bind = sig.bind(*args, **kwargs).arguments
        request = bind.get("request")
        json_data = json_format.MessageToJson(response, preserving_proto_field_name=True)
        if len(json_data) > 1024 * 4:
            logger.debug("{}".format({
                "type": "rpc_log",
                "request_id": request.request_id,
                "function": func_name,
                "status": response.status,
                "process_time": "{:.6f}s".format(process_time),
                "response": json_data[:1024 * 4] + "...",
            }))
        else:
            logger.debug("{}".format({
                "type": "rpc_log",
                "request_id": request.request_id,
                "function": func_name,
                "status": response.status,
                "process_time": "{:.6f}s".format(process_time),
                "response": json.loads(json_data),
            }))
        return response

    return wrapper


class RpcStubMixin(object):
    def __init__(self, channel):
        self.channel = channel

    @staticmethod
    async def remote_call(target, f, stub_func, request, timeout=None):
        has_error = False
        start_time = time.time()
        request.request_id = uuid.uuid4().hex
        error_msg = ""
        if timeout is None:
            timeout = DEFAULT_RPC_TIMEOUT
        try:
            response = await stub_func(request, timeout=timeout)
            status = response.status
        except grpc.RpcError as exc:
            # logger.info("remote_call error: {}".format(exc))
            # raise exc
            has_error = True
            error_msg = "{}".format(exc)
            status, response = convert_grpc_error(exc), None
        process_time = time.time() - start_time
        json_data = json_format.MessageToJson(response, preserving_proto_field_name=True) if not has_error else "{}"
        log_message = "{}".format({
            "type": "remote_call",
            "target": target,
            "request_id": request.request_id,
            "function": f,
            "process_time": "{:.6f}s".format(process_time),
            "status": status,
            "request": json.loads(json_format.MessageToJson(request, preserving_proto_field_name=True)),
            "response": json_data[:1024 * 4] + "..." if len(json_data) > 1024 * 4 else json.loads(json_data),
        })
        if has_error:
            logger.info("{}\n{}".format(log_message, error_msg))
        else:
            logger.debug(log_message)
        return status, response


def call_rpc(request, response_func, method):
    def _f(f):
        @functools.wraps(f)
        async def call(self, *args, **kwargs):
            if "timeout" in kwargs:
                timeout = kwargs.pop("timeout")
            else:
                timeout = DEFAULT_RPC_TIMEOUT
            status, response = await self.remote_call(self.target, f, method(self), request(*args, **kwargs), timeout)
            return response_func(status, response)

        return call

    return _f
