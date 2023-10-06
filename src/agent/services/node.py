from agent.decorators import rpc_log
from agent.proto import node_pb2, node_pb2_grpc
from rook.error_code import StatusCode

HOSTNAMECTL = "/usr/bin/hostnamectl"
TIMEDATECTL = "/usr/bin/timedatectl"
DATE = "/usr/bin/date"


class NodeService(node_pb2_grpc.NodeServiceServicer):
    def __init__(self, app):
        self.app = app

    @rpc_log
    async def ping(self, request, context) -> node_pb2.PingReply:
        """检测主机是否正常在线"""
        message = request.message
        if not message:
            message = "pong"
        reply = node_pb2.PingReply(status=StatusCode.STATUS_SUCCESS, message=message)
        return reply

    @rpc_log
    async def node_add(self, request, context) -> node_pb2.AddNodeReply:
        """添加节点"""
        etcd_endpoints = request.etcd_endpoints
        print(etcd_endpoints)
        status = StatusCode.STATUS_SUCCESS

        reply = node_pb2.AddNodeReply(
            status=status,
        )
        return reply
