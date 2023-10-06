# Scaffold

### 1. 安装部署

#### 安装Python 3.9

```shell
# 下载Python
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh

# 安装Python
bash ./Miniconda3-py39_4.9.2-Linux-x86_64.sh -b -f -p /opt/miniconda3

# 初始化Python
/opt/miniconda3/bin/conda init

# 激活Python环境
source ~/.bashrc
```

#### 配置Python软件源

```.shell
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple

# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 安装依赖包

```shell
mkdir ./wheels

# 下载wheels
pip wheel -w wheels -r ./requirements.txt

# 安装wheels
pip install --no-index --find-links=./wheels -r ./requirements.txt
```

#### 卸载依赖包
```shell
pip uninstall -r ./requirements.txt --yes
```

### 2. 启动 Agent

`cp` 项目，`or rpm install scaffold `

参考 [python 打 rpm 包]()

```shell
# 拷贝到默认的执行路径
cp ./scaffold /opt/
```

#### 2.1 使用 systemd

```shell
# 使用systemd, 将agent.service 注册到宿主机
$ systemctl enable agent.service
$ systemctl restart agent.service
```

#### 2.2 Linux 下运行

```shell
# 运行grpc agent server 
$ /opt/miniconda3/bin/python /opt/scaffold/src/agent/main.py --log_to_stderr=false --log_level=info
```

#### 2.3 Windows下运行

```shell
# cd 到 agent目录，执行
$ cd `target path`
$ python main.py

# or ide run main.py
```

#### 2.4 测试

```shell
# python -m unittest test_node.NodeTest.test_ping in scaffold\src\agent\tests
$ python src/agent/tests/test_node.py
```

