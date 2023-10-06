import asyncio
import functools
import unittest

from agent.rpc_client import RpcClient

HOST, PORT = "127.0.0.1", 8688


def async_test(f):
    @functools.wraps(f)
    def _f(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f(self))

    return _f


class NodeTest(unittest.TestCase):
    @async_test
    async def setUp(self):
        host, port = HOST, PORT
        self.client = RpcClient(host=host, port=port)

    @async_test
    async def tearDown(self):
        pass

    @async_test
    async def test_ping(self):
        async def _worker():
            status, result = await self.client.ping(message="Hello World")
            self.assertEqual(status, 0)

        tasks = [asyncio.create_task(_worker()) for _ in range(10000)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    unittest.main()
