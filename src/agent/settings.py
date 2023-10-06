import platform
from pathlib import Path

SYSTEM = platform.system().upper()
IS_FREEBSD = SYSTEM == "FREEBSD"
IS_LINUX = SYSTEM == "LINUX"
IS_WINDOWS = SYSTEM == "WINDOWS"
IS_DARWIN = SYSTEM == "DARWIN"

#####################################################################################
#                                    全局配置 　　                                    ＃
#####################################################################################
# 根目录
ROOT_PATH = Path(__file__).parent.absolute()

SERVER_HOST = "[::]"
SERVER_PORT = 8688
SERVER_WORKERS = 24

####################################################################################


#####################################################################################
#                                    平台配置 　　                                    ＃
#####################################################################################
if IS_WINDOWS or IS_DARWIN:
    # Just for developer
    # CLUSTER_CONFIG = os.path.join(ROOT_PATH, "conf/cluster.json")
    # PLATFORM_CONFIG = os.path.join(ROOT_PATH, "conf/config.json")
    # PID_FILE = "../log/uxsagent.pid"
    PID_FILE = ROOT_PATH.parent.joinpath("log/agent.pid")
    APP_LOG_PATH = ROOT_PATH.parent.joinpath("log/agent.log")
    LOG_TO_STDERR = "true"
    LOG_LEVEL = "debug"
else:
    # config files
    # CLUSTER_CONFIG = "/etc/uxs/cluster.json"
    # PLATFORM_CONFIG = "/etc/uxs/config.json"
    # PID_FILE = "../log/agent.pid"
    PID_FILE = ROOT_PATH.parent.joinpath("log/agent.pid")
    APP_LOG_PATH = ROOT_PATH.parent.joinpath("log/agent.log")
    LOG_TO_STDERR = "true"
    LOG_LEVEL = "debug"

####################################################################################
