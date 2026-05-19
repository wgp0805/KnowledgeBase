---
title: Docker-window环境下部署RocketMq
tags:
  - RocketMQ
categories:
  - RocketMQ
date: 2025-11-20 10:00:07
---

## 一、环境要求

1. 系统版本：Windows 10/11（需启用WSL2及Hyper-V）
2. Docker Desktop：≥4.15.0（设置中勾选“Use WSL2”）（安装步骤可参考之前文章：https://blog.csdn.net/qq_17153885/article/details/141337873?spm=1011.2415.3001.5331）
3. 硬件配置：双核CPU/8GB内存/50GB磁盘空间
4. 端口开放：9876（NameServer）、10911（Broker）、8080（控制台）

## 二、部署步骤

### 1. 创建网络

RocketMQ 中有多个服务，需要创建多个容器，创建 docker 网络便于容器间相互通信。

```bash
docker network create rocketmq
```

![image-20251120100321850](image-20251120100321850.png)

由于我这里已经创建成功了，再次创同名网络配置报错了，提示已存在

### 2. 拉取RocketMQ镜像

打开cmd终端执行以下命令

#### 2.1、搜索RocketMQ镜像

```bash
docker search rocketmq
```

`docker search`docker搜索命令

`rocketmq`要搜索的中间件信息

![image-20251120100714388](image-20251120100714388.png)

```bash
docker pull apache/rocketmq:latest
```

`dockert pull` 拉取镜像命令

`apache/rocketmq:latest`拉取的镜像名称，其中`:latest`指定版本号，如果直接拉取最新的镜像可以不写，也可以写`:latest`

![image-20251120100901996](image-20251120100901996.png)

拉取成功后就会在Docker Desktop的镜像页面显示

![image-20251120100843827](image-20251120100843827.png)

#### 2.2、启动NameServer容器

Namesrv（Name Server）是 RocketMQ 的名称服务，用于管理 Broker 的元数据信息，如 Broker 的地址、状态等。每个 RocketMQ 集群至少需要一个 Namesrv 实例。

##### 2.2.1、创建数据目录

创建数据目录（可选，但推荐）：为了持久化存储 Namesrv 的配置和日志数据，建议在本地创建一个数据目录。例如，在 D 盘创建一个名为 “rocketmq_data” 的目录，并在其中创建 “namesrv” 子目录：

`mkdir -p D:\dockerDir\recketMQ\namesrv`

![image-20251120101110070](image-20251120101110070.png)

##### 2.2.2、运行Namesrv容器

运行 Namesrv 容器：执行以下命令创建并运行 Namesrv 容器：

`docker run -d --name rmqnamesrv -p 9876:9876 --network rocketmq -v D:\dockerDir\recketMQ\namesrv:/home/rocketmq/namesrv -e "MAX_POSSIBLE_HEAP=100000000" apache/rocketmq sh mqnamesrv`

命令参数说明：

- `-d`：以守护进程模式运行容器。
- `--name rmqnamesrv`：为容器指定名称为 “rmqnamesrv”。
- `-p 9876:9876`：将容器的 9876 端口映射到主机的 9876 端口，以便外部访问 Namesrv 服务。
- `--network rocketm`：指定使用之前创建的网络配置

- `-v D:\dockerDir\recketMQ\namesrv:/home/rocketmq/namesrv`：将主机的 “D:\dockerDir\recketMQ\namesrv” 目录挂载到容器的 “/home/rocketmq/namesrv” 目录，实现数据持久化。（==这里正常来说应该是这么配置的，但是我的没有实现，生成的日志啥的依旧在容器的目录中==）

- `-e "MAX_POSSIBLE_HEAP=100000000"`：设置容器中 Java 进程的最大堆内存为 100MB（根据实际需求调整，建议不要设置过大，以免占用过多系统资源）。

- `sh mqnamesrv`：在容器中执行启动 Namesrv 的命令。

```bash
docker run -d --name rmqnamesrv -p 9876:9876 --network rocketmq -v D:\dockerDir\recketMQ\namesrv:/home/rocketmq/namesrv -e "MAX_POSSIBLE_HEAP=100000000" apache/rocketmq sh mqnamesrv
```

![image-20251120101448837](image-20251120101448837.png)

容器中就出现了这个启动的容

![image-20251120101500431](image-20251120101500431.png)

#### 2.3、启动Broker容器

Broker 是 RocketMQ 的核心组件，负责存储和处理消息。每个 Broker 实例需要向 Namesrv 注册，以便客户端能够发现和连接到 Broker。

##### 2.3.1、创建数据目录

创建数据目录：同样，为了持久化存储 Broker 的配置、日志和消息数据，在本地创建 “broker” 子目录：
`mkdir -p D:\dockerDir\recketMQ\broker`

![image-20251120101629136](image-20251120101629136.png)

##### 2.3.2、创建 Broker 配置文件

创建 Broker 配置文件：在 “broker” 目录中创建一个名为 “broker.conf” 的配置文件，内容如下：

```pro
brokerClusterName=DefaultCluster # 集群名称
brokerName=broker-a   # Broker名称（同一集群内唯一）
brokerId=0     # Broker角色（0=主节点）
deleteWhen=04  # 文件删除时间（凌晨4点）
fileReservedTime=72  # 文件保留时间（72小时）
brokerRole=ASYNC_MASTER  #Broker角色（异步主节点）
flushDiskType=ASYNC_FLUSH   #刷盘策略（异步刷盘）
namesrvAddr=rmqnamesrv:9876 #NameServer地址（需可访问）
brokerIP1=172.26.144.1    # Broker对外IP（实际IP或域名）。指定 Broker 的公网 IP 地址或外部访问的 IP 地址
autoCreateTopicEnable = true   # 允许自动创建Topic
clusterTopicEnable = true      # 启用集群级Topic
brokerTopicEnable = true       # 启用Broker级Topic
```

![image-20251120101710303](image-20251120101710303.png)

##### 2.3.3、运行Broker容器

运行 Broker 容器：执行以下命令创建并运行 Broker 容器：

`docker run -d --name rmqbroker -p 10911:10911 -p 10909:10909 --network rocketmq -v D:\dockerDir\recketMQ\broker:/home/rocketmq/broker -v D:\dockerDir\recketMQ\broker\broker.conf:/home/rocketmq/conf/broker.conf -e "NAMESRV_ADDR=rmqnamesrv:9876" -e "MAX_POSSIBLE_HEAP=200000000" apache/rocketmq sh mqbroker -c /home/rocketmq/conf/broker.conf`

- `-p 10911:10911`：映射 Broker 的内部通信端口（用于 Broker 与 Namesrv、Broker 与 Broker 之间的通信）到主机的 10911 端口。

- `-p 10909:10909`：映射 Broker 的客户端通信端口（用于客户端发送和接收消息）到主机的 10909 端口。

- `-v D:\dockerDir\recketMQ\broker:/home/rocketmq/broker`：挂载 Broker 的数据目录。

- `-v D:\dockerDir\recketMQ\broker\broker.conf:/home/rocketmq/conf/broker.conf`：挂载 Broker 的配置文件。

- `-e "NAMESRV_ADDR=rmqnamesrv:9876"`：设置 Namesrv 的地址和端口，其中 “rmqnamesrv” 是之前创建的 Namesrv 容器的名称，Docker 会自动解析为容器的 IP 地址。

- `-e "MAX_POSSIBLE_HEAP=200000000"`：设置 Broker 进程的最大堆内存为 200MB（根据实际需求调整）。

- `sh mqbroker -c /home/rocketmq/conf/broker.conf`：在容器中执行启动 Broker 的命令，并指定配置文件路径。

```bash
docker run -d --name rmqbroker -p 10911:10911 -p 10909:10909 --network rocketmq -v D:\dockerDir\recketMQ\broker:/home/rocketmq/broker -v D:\dockerDir\recketMQ\broker\broker.conf:/home/rocketmq/conf/broker.conf -e "NAMESRV_ADDR=rmqnamesrv:9876" -e "MAX_POSSIBLE_HEAP=200000000" apache/rocketmq sh mqbroker -c /home/rocketmq/conf/broker.conf
```

![image-20251120102009805](image-20251120102009805.png)

![image-20251120102021071](image-20251120102021071.png)

#### 2.4、安装 RocketMQ 控制台（可选，用于可视化管理）

为了方便对 RocketMQ 集群进行可视化管理和监控，我们可以安装 RocketMQ 控制台。RocketMQ 控制台是一个基于 Web 的管理工具，提供了对 Topic、Consumer Group、Broker 等资源的管理和监控功能。

##### 2.4.1、拉取RocketMqConsole镜像

```bash
docker pull apacherocketmq/rocketmq-dashboard
```

备注：镜像背景说明

- **`apache/rocketmq-console-ng`**
  - **状态**：已废弃（2021年后停止维护）
  - **问题**：不支持RocketMQ 5.x+，存在兼容性风险
  - **来源**：非Apache官方维护，社区旧版项目镜像

**`apacherocketmq/rocketmq-dashboard`**

- **状态**：官方维护（持续更新，支持最新版本）
- **功能**：支持RocketMQ 4.x/5.x，集成监控告警、权限管理等新特性
- **来源**：Apache RocketMQ官方GitHub仓库

![image-20251120102128183](image-20251120102128183.png)

##### 2.4.2、运行Rocket-console容器

```bash
docker run -d --name rmq-console -p 8080:8082 --network rmq-net -e "JAVA_OPTS=-Drocketmq.config.namesrvAddr=rmqnamesrv:9876 -Drocketmq.config.isVIPChannel=false" -t apacherocketmq/rocketmq-dashboard
```

在上述命令中：

- `-d` 是以守护进程模式在后台运行容器。
- `--name rmq - dashboard` 是给容器指定名称为 `rmq - dashboard`。

- `-p 8080:8082` 是将容器的 8082 端口映射到宿主机的 8080 端口，这样就能通过浏览器访问控制台。至于这里为什么不直接使用8080端口，是我发现这个监控程序启动以后，在容器上不是在8080启动的所以使用8082，**这个监控程序启动的时候，不一定是哪个端口，根据实际情况配置就行**

‍![image-20251120102415472](image-20251120102415472.png)

![image-20251120102854949](image-20251120102854949.png)

## 三、浏览器访问

访问控制台：浏览器打开 http://localhost:8080，若显示Broker节点状态、Topic列表，则部署成功

![image-20251120102953209](image-20251120102953209.png)

### 1、主题

![image-20251120103115859](image-20251120103115859.png)

### 2、消费者

![image-20251120103139818](image-20251120103139818.png)
