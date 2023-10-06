import atexit
import logging
import os
import signal
import sys
import time

logger = logging.getLogger()


class Daemon:
    def __init__(self, pidfile, stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
        self.pidfile = pidfile
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.force_ground = False

    def sigterm_handler(self, signo, frame):
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)
        raise SystemExit(1)

    def _daemon(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as err:
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (err.errno, err.strerror))
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

        # Flush I/O buffers
        sys.stdout.flush()
        sys.stderr.flush()

        # Replace file descriptors for stdin, stdout, and stderr
        with open(self.stdin, "rb", 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open(self.stdout, "ab", 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open(self.stderr, "ab", 0) as f:
            os.dup2(f.fileno(), sys.stderr.fileno())

        # 注册退出函数，根据文件pid判断是否存在进程
        atexit.register(self.delete_pidfile)

    def set_force_ground(self, force_ground):
        self.force_ground = force_ground

    def delete_pidfile(self):
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)

    def start(self, *args, **kwargs):
        if os.path.exists(self.pidfile):
            raise RuntimeError("process already is running\n")

        self.not_force_ground()

        self.write_pid_file()

        signal.signal(signal.SIGTERM, self.sigterm_handler)
        signal.signal(signal.SIGINT, self.sigterm_handler)
        self.run(*args, **kwargs)

    def stop(self):
        if os.path.exists(self.pidfile):
            with open(self.pidfile) as f:
                pid = int(f.read())
                os.kill(pid, signal.SIGTERM)
            # wait 1s for other daemon cleanup
            time.sleep(1)
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)
        else:
            sys.stdout.write("process is not running\n")
            raise SystemExit(1)

    def restart(self, *args, **kwargs):
        if os.path.exists(self.pidfile):
            with open(self.pidfile) as f:
                pid = int(f.read())
                os.kill(pid, signal.SIGTERM)
            # wait 1s for other daemon cleanup
            time.sleep(1)
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)

        self.not_force_ground()

        self.write_pid_file()

        signal.signal(signal.SIGTERM, self.sigterm_handler)
        signal.signal(signal.SIGINT, self.sigterm_handler)
        self.run(*args, **kwargs)

    def not_force_ground(self):
        if not self.force_ground:
            self._daemon()

    def write_pid_file(self):
        # Write the PID file
        with open(self.pidfile, "w") as f:
            f.write("%s" % os.getpid())
            f.flush()

    def run(self, *args, **kwargs):
        raise NotImplementedError()
