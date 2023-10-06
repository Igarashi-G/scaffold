from agent.decorators import RpcStubMixin
from agent.decorators import call_rpc
from agent.proto import node_pb2, node_pb2_grpc


class Node(RpcStubMixin):
    def __init__(self, channel):
        super().__init__(channel)
        self.node_stub = node_pb2_grpc.NodeServiceStub(channel=channel)

    @call_rpc(lambda message: node_pb2.PingRequest(message=message),
              lambda status, resp: (status, resp),
              lambda stub: stub.node_stub.ping)
    async def ping(self, message: str = None, *args, **kwargs):
        pass

    @call_rpc(lambda etcd_endpoints: node_pb2.AddNodeRequest(etcd_endpoints=etcd_endpoints),
              lambda status, resp: (status, resp),
              lambda stub: stub.node_stub.node_add)
    async def node_add(self, etcd_endpoints: str, *args, **kwargs):
        pass
