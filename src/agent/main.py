#  Copyright (C) 2023 - FuuKa Co.,Ltd. <https://github.com/Igarashi-G>
#  Copyright (C) 2023 - Igarashi <igarashifk@gmail.com>

import argparse
import asyncio
import logging
import os
import signal
import sys
from pathlib import Path

# src, src/agent, src/agent/proto
sys.path.insert(0, str(Path(__file__).parent.parent.absolute()))
sys.path.insert(0, str(Path(__file__).parent.absolute()))
sys.path.insert(0, str(Path(__file__).parent.absolute().joinpath("proto")))

from agent import settings
from agent.rpc_server import RpcServer
from rook import osc, daemon
from agent import log

logger = logging.getLogger()


class Application(daemon.Daemon):

    def __init__(self, pidfile, stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
        super(Application, self).__init__(pidfile=pidfile, stdin=stdin, stdout=stdout, stderr=stderr)
        self.task_list = []
        self._terminate_task = None

    def run(self):
        # step 1. init all signal handlers
        if not osc.IS_WINDOWS:
            loop.add_signal_handler(signal.SIGINT, self.stop)
            loop.add_signal_handler(signal.SIGTERM, self.stop)
            loop.add_signal_handler(signal.SIGHUP, self.reload_handler)
            loop.add_signal_handler(signal.SIGUSR1, self.info_handler)

        # step 2. register my tasks
        rpc_server = RpcServer(loop, args.host, args.port, args.workers)
        self.task_list.append(loop.create_task(rpc_server.run(), name="rpc_server"))

        # step 3. run asyncio
        try:
            loop.run_forever()
        except RuntimeError as e:
            if e.args[0] != "Event loop is closed":
                raise
        except KeyboardInterrupt:
            pass

        # step 4. exit
        if not osc.IS_WINDOWS:
            os.killpg(os.getpgid(os.getpid()), signal.SIGTERM)
            os._exit(0)  # noqa:

    def reload_handler(self):  # noqa:
        # TODO:
        logger.info("got signal: SIGHUP")

    def info_handler(self):  # noqa:
        # TODO:
        logger.info("got signal: SIGUSR1")

    def stop(self):
        logger.info("stopping...")
        self._terminate_task = loop.create_task(self._terminate())
        super(Application, self).stop()

    async def _terminate(self):
        for task in asyncio.all_tasks(loop):
            if task != self._terminate_task:
                logger.info("canceling %r", task)
                task.cancel()
        loop.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RPC server")
    parser.add_argument(
        "--host", type=str, default=settings.SERVER_HOST, nargs="?",
        help="Bind socket to this host."
    )
    parser.add_argument(
        "--port", type=int, default=settings.SERVER_PORT, nargs="?",
        help="Bind to a socket with this port."
    )
    parser.add_argument(
        "--workers", type=int, default=settings.SERVER_WORKERS, nargs="?",
        help="Max size of multiple worker processes"
    )
    parser.add_argument(
        "--log_to_stderr", type=str, default=settings.LOG_TO_STDERR, nargs="?",
        help="Output log to stderr"
    )
    parser.add_argument(
        "--log_level", type=str, default=settings.LOG_LEVEL, nargs="?",
        help="Log level"
    )
    # parse args
    args = parser.parse_args()

    # init components
    log.log_init(args.log_to_stderr, args.log_level)

    if osc.IS_WINDOWS:
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()

    # start server
    logger.info("Starting application...")
    if osc.IS_LINUX:
        program = Application(pidfile=settings.PID_FILE)
        force_ground = args.log_to_stderr.lower() in ("true", "1", "yes")
        program.set_force_ground(force_ground)
        program.start()
    elif osc.IS_WINDOWS or osc.IS_DARWIN:
        program = Application(pidfile=settings.PID_FILE)
        program.run()
    logger.info("exit...OK")
