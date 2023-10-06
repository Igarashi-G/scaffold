import asyncio
import logging
import multiprocessing
from concurrent import futures

import grpc  # noqa:
import grpc.aio  # noqa:

from agent.proto import node_pb2_grpc
from agent.services.node import NodeService
from rook.run_in_thread import RunInThreadMixin

logger = logging.getLogger()

# For more channel options, please see https://grpc.io/grpc/core/group__grpc__arg__keys.html
DEFAULT_GRPC_OPTIONS = (
    ("grpc.enable_retries", 0),
    ("grpc.keepalive_timeout_ms", 1000),
    ("grpc.grpclb_call_timeout_ms", 500),
    ("grpc.grpclb_fallback_timeout_ms", 1000),
    ("grpc.priority_failover_timeout_ms", 1000),
    ("grpc.server_handshake_timeout_ms", 1000),
    ("grpc.client_idle_timeout_ms", 1000),
    ("grpc.max_send_message_length", 256 * 1024 * 1024),
    ("grpc.max_receive_message_length", 256 * 1024 * 1024),
)


class RpcServer(RunInThreadMixin):
    def __init__(self, event_loop, host: str = "[::]", port: int = 8688, worker: int = 24):
        self._listen_address = "{}:{}".format(host, port)
        self._server = None
        self.loop = event_loop
        self.run_in_thread_executor = futures.ThreadPoolExecutor(max_workers=worker, thread_name_prefix="job_worker")

        self.init_grpc_aio_server()
        self.register_services()

    def init_grpc_aio_server(self):
        self._server = grpc.aio.server(
            migration_thread_pool=futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()),
            options=DEFAULT_GRPC_OPTIONS,
            maximum_concurrent_rpcs=40)

    def register_services(self):
        node_pb2_grpc.add_NodeServiceServicer_to_server(NodeService(app=self), self._server)

    async def run(self) -> None:
        self._server.add_insecure_port(self._listen_address)
        logger.info("Run rpc server on {}".format(self._listen_address))
        await self._server.start()
        try:
            await self._server.wait_for_termination()
        except asyncio.CancelledError:
            # await self._server.stop(0)
            await self.stop()
        # try:
        #     while True:
        #         await asyncio.sleep(1)
        # except asyncio.CancelledError:
        #     await self._server.stop(0)

    async def stop(self):
        await self._server.stop(0)
