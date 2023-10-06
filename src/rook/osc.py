import asyncio
import logging
import os
import platform
import subprocess
from pathlib import PurePath
from typing import List, Union

import setproctitle

SYSTEM = platform.system().upper()
try:
    DIST = platform.dist()[0].upper()
except:  # noqa
    DIST = None
    sysctl = None

IS_FREEBSD = SYSTEM == "FREEBSD"
IS_LINUX = SYSTEM == "LINUX"
IS_WINDOWS = SYSTEM == "WINDOWS"
IS_DARWIN = SYSTEM == "DARWIN"

IS_UBUNTU = DIST == "UBUNTU"
IS_CENTOS = DIST == "CENTOS"

logger = logging.getLogger()


async def run_command(cmd: Union[str, List[str]], shell=False, stdin=asyncio.subprocess.PIPE,
                      stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, throw=False,
                      log=False, input=None, encoding="utf-8"):
    """Usage:

        WARNING!!! shell injection
        shell:
            run_command("ls -l", shell=True)
            run_command("/usr/bin/ls -l", shell=True)

        program:
            run_command("/usr/local/bin/your_program", shell=False)
            run_command(["/usr/local/bin/your_program"], shell=False)
            run_command(["/usr/bin/ls", "-l", "-a"], shell=False)
    """
    try:
        # We force run_command to always use en_US
        # to avoid issues on date and number formats
        # on not Anglo-Saxon systems (ex. it, es, fr, de, etc)
        fake_env = dict(os.environ)
        fake_env["LANG"] = "en_US.UTF-8"
        if shell:
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr,
                env=fake_env,
            )
        else:
            if isinstance(cmd, List):
                program = cmd[0]
                args = cmd[1:]
            else:
                program = cmd
                args = []
            proc = await asyncio.create_subprocess_exec(
                program,
                *args,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr,
                env=fake_env,
            )
        out, err = await proc.communicate(input=input)
        rc = proc.returncode
    except Exception as why:
        err, rc = "Exception while running command({}): {}".format(cmd, str(why)), -1
        logger.info(err)
        if throw:
            raise why
        return [], err, rc
    if log:
        logger.info("run command: {} => out, err, rc = {}, {}, {} ======="
                    .format(cmd, out, err, rc))
    return out.decode(encoding=encoding), err.decode(encoding=encoding), rc


def run_command_sync(cmd, shell=False, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
                     stderr=asyncio.subprocess.PIPE, log=False, input=None, throw=False, encoding="utf-8"):
    """Usage:

        WARNING!!! shell injection
        shell:
            run_command_sync("ls -l", shell=True)
            run_command_sync("/usr/bin/ls -l", shell=True)

        program:
            run_command_sync("/usr/local/bin/your_program", shell=False)
            run_command_sync(["/usr/local/bin/your_program"], shell=False)
            run_command_sync(["/usr/bin/ls", "-l", "-a"], shell=False)
    """
    try:
        # We force run_command to always use en_US
        # to avoid issues on date and number formats
        # on not Anglo-Saxon systems (ex. it, es, fr, de, etc)
        fake_env = dict(os.environ)
        fake_env["LANG"] = "en_US.UTF-8"
        if not shell:
            cmd = map(str, cmd)
        proc = subprocess.Popen(
            cmd,
            shell=shell,
            stdout=stdout,
            stderr=stderr,
            stdin=stdin,
            env=fake_env,
        )
        out, err = proc.communicate(input=input)
        rc = proc.returncode
    except Exception as why:
        err, rc = "Exception while running command({}): {}".format(cmd, str(why)), -1
        logger.info(err)
        if throw:
            raise why
        return [], err, rc
    if log:
        logger.info("Run command: {} => out, err, rc = {}, {}, {} ======="
                    .format(cmd, out, err, rc))
    return out.decode(encoding=encoding), err.decode(encoding=encoding), rc


def set_thread_title(title):
    setproctitle.setthreadtitle(title=title)


def get_thread_title():
    return setproctitle.getthreadtitle()


def set_proc_title(title):
    setproctitle.setproctitle(title=title)


def get_proc_title():
    return setproctitle.getproctitle()


def splice_path(*args):
    """
    *args 所有需要拼接的路径
    return 返回拼接后的路径
    """
    root = args[0]
    if root.startswith("/"):
        root = "/" + root.strip("/")
    paths = [p.strip("/") for p in args[1:]]
    return PurePath(root, *paths).as_posix()
