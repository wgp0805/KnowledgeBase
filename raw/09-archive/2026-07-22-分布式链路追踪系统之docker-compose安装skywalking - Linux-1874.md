---
title: "分布式链路追踪系统之docker-compose安装skywalking - Linux-1874"
source: "博客园"
url: "https://www.cnblogs.com/qiuhom-1874/p/21657975"
date: "2026-07-22T14:35:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 分布式链路追踪系统之docker-compose安装skywalking - Linux-1874

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/qiuhom-1874/p/21657975  
> **抓取日期**: 2026-07-22  
> **相关性评分**: 0.7

### 环境准备

#### 安装docker docker-compose

**更新 安装依赖**
    
    
    root@skywalking-docker-compose:~# apt update
    root@skywalking-docker-compose:~# apt install -y ca-certificates curl gnupg lsb-release
    

**添加Docker的GPG公钥**
    
    
    root@skywalking-docker-compose:~# install -m 0755 -d /etc/apt/keyrings
    root@skywalking-docker-compose:~# curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    root@skywalking-docker-compose:~# chmod a+r /etc/apt/keyrings/docker.gpg
    

**更新源**
    
    
    root@skywalking-docker-compose:~# echo \
    >   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
    >   "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    >   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    root@skywalking-docker-compose:~# cat /etc/apt/sources.list.d/docker.list 
    deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu   jammy stable
    

**安装docker docker-compose**
    
    
    apt install docker-ce  docker-compose -y
    

**验证docker 、docker-compose**
    
    
    root@skywalking-docker-compose:~# docker version
    Client: Docker Engine - Community
     Version:           29.6.2
     API version:       1.55
     Go version:        go1.26.5
     Git commit:        dfc4efb
     Built:             Thu Jul 16 16:12:23 2026
     OS/Arch:           linux/amd64
     Context:           default
    
    Server: Docker Engine - Community
     Engine:
      Version:          29.6.2
      API version:      1.55 (minimum version 1.40)
      Go version:       go1.26.5
      Git commit:       3d80467
      Built:            Thu Jul 16 16:12:23 2026
      OS/Arch:          linux/amd64
      Experimental:     false
     containerd:
      Version:          v2.2.6
      GitCommit:        11ce9d5f3c68c941867e82890e93e815c1304f1b
     runc:
      Version:          1.3.6
      GitCommit:        v1.3.6-0-g491b69ba
     docker-init:
      Version:          0.19.0
      GitCommit:        de40ad0
    root@skywalking-docker-compose:~# docker-compose version
    docker-compose version 1.29.2, build unknown
    docker-py version: 5.0.3
    CPython version: 3.10.6
    OpenSSL version: OpenSSL 3.0.2 15 Mar 2022
    root@skywalking-docker-compose:~# 
    

#### 创建项目目录
    
    
    root@skywalking-docker-compose:~# cd /usr/local/src/
    root@skywalking-docker-compose:/usr/local/src# mkdir skywalking-compose
    root@skywalking-docker-compose:/usr/local/src# cd skywalking-compose
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose#
    

### 编写部署清单
    
    
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# cat docker-compose.yml
    version: "3"
    
    services:
        elasticsearch:
            image: harbor-server.ilinux.io/skywalking/elasticsearch:8.4.2
            container_name: elasticsearch
            ports:
            - "9200:9200"
            healthcheck:
                test: ["CMD-SHELL", "curl -sf http://localhost:9200/_cluster/health || exit 1"] 
                interval: 60s 
                timeout: 10s
                retries: 3
                start_period: 60s 
            environment:
                discovery.type: single-node 
                ingest.geoip.downloader.enabled: "false"
                bootstrap.memory_lock: "true"
                ES_JAVA_OPTS: "-Xms512m -Xmx512m"
                TZ: "Asia/Shanghai"
                xpack.security.enabled: "false" 
            ulimits:
                memlock:
                    soft: -1
                    hard: -1
    
        skywalking-oap:
            image: harbor-server.ilinux.io/skywalking/apache/skywalking-oap-server:9.3.0
            container_name: skywalking-oap
            depends_on:
                elasticsearch:
                    condition: service_healthy
            links:
            - elasticsearch
            environment:
                SW_HEALTH_CHECKER: default
                SW_STORAGE: elasticsearch
                SW_STORAGE_ES_CLUSTER_NODES: elasticsearch:9200
                JAVA_OPTS: "-Xms2048m -Xmx2048m"
                TZ: Asia/Shanghai
                SW_TELEMETRY: prometheus
            healthcheck:
                test: ["CMD-SHELL", "/skywalking/bin/swctl ch"]
                interval: 30s
                timeout: 10s
                retries: 3
                start_period: 10s
            restart: on-failure
            ports:
                - "11800:11800"
                - "12800:12800"
    
        skywalking-ui:
            image: harbor-server.ilinux.io/skywalking/apache/skywalking-ui:9.3.0
            depends_on:
                skywalking-oap:
                    condition: service_healthy
            links:
            - skywalking-oap
            ports:
                - "8080:8080"
            environment:
                SW_OAP_ADDRESS: http://skywalking-oap:12800
                SW_HEALTH_CHECKER: default
                TZ: Asia/Shanghai
            healthcheck:
                test: ["CMD-SHELL", "curl -sf http://localhost:8080 || exit 1"] 
                interval: 60s 
                timeout: 10s
                retries: 3
                start_period: 60s 
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose#
    

> 由于现在docker官方仓库在国内基本无法访问，上面的镜像是使用本地自己搭建harbor仓库存放的镜像；有关harbor仓库的搭建可以参考本人博客<https://www.cnblogs.com/qiuhom-1874/p/13061984.html>

### 启动项目部署清单
    
    
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# docker-compose up -d  
    Creating network "skywalking-compose_default" with the default driver
    Pulling elasticsearch (harbor-server.ilinux.io/skywalking/elasticsearch:8.4.2)...
    ERROR: failed to resolve reference "harbor-server.ilinux.io/skywalking/elasticsearch:8.4.2": failed to do request: Head "https://harbor-server.ilinux.io/v2/skywalking/elasticsearch/manifests/8.4.2": dial tcp 192.168.112.111:443: connect: connection refused
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# 
    

> 启动出现上述错误是我使用的私有仓库，没有提供https，默认docker会认为我们使用的私有仓库是安全的，所以使用https访问，解决办法告诉docker 私有仓库是不安全的仓库，使用非https访问，如下

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260721231353294-1422314680.png)

> 在/etc/docker/daemon.json文件中用insecure-registries来配置非安全的仓库，后面是一个列表，可以跟多个仓库地址，用逗号隔开即可；

**加载docker配置文件，重启docker**
    
    
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# systemctl daemon-reload
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# systemctl restart docker
    

**启动docker-compose**
    
    
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# docker-compose up -d
    Pulling elasticsearch (harbor-server.ilinux.io/skywalking/elasticsearch:8.4.2)...
    8.4.2: Pulling from skywalking/elasticsearch
    713e6bb53405: Pull complete
    8e1d640ddcb9: Pull complete
    675920708c8b: Pull complete
    4ce1c159ba1b: Pull complete
    838df58225af: Pull complete
    20fe1ad733fe: Pull complete
    6dd4ae51eecd: Pull complete
    09e1c6584446: Pull complete
    355bd4dfc6f0: Pull complete
    Digest: sha256:44abebecec5c88e5cc9f40e720358903610b3835a8b4db501d69d1d2fcf94648
    Status: Downloaded newer image for harbor-server.ilinux.io/skywalking/elasticsearch:8.4.2
    Pulling skywalking-oap (harbor-server.ilinux.io/skywalking/apache/skywalking-oap-server:9.3.0)...
    9.3.0: Pulling from skywalking/apache/skywalking-oap-server
    7ffda9c68111: Pull complete
    8226a2ee5818: Pull complete
    4ced2591451d: Pull complete
    111b6c748642: Pull complete
    fa328ff46047: Pull complete
    5cb275601c3a: Pull complete
    df8f874ae8c0: Pull complete
    e7b94896debc: Pull complete
    e0f93d05989f: Pull complete
    e96e057aae67: Pull complete
    a373ef37d4c6: Pull complete
    Digest: sha256:d31390947d06f7fda7bf16a2fc3ea15992ad6ab39b9b902225464c7e036a998b
    Status: Downloaded newer image for harbor-server.ilinux.io/skywalking/apache/skywalking-oap-server:9.3.0
    Pulling skywalking-ui (harbor-server.ilinux.io/skywalking/apache/skywalking-ui:9.3.0)...
    9.3.0: Pulling from skywalking/apache/skywalking-ui
    3d5164883dbb: Pull complete
    223af88a0e24: Pull complete
    e41d53e5a442: Pull complete
    5784c2c8bf5f: Pull complete
    c99978fd3ba9: Pull complete
    Digest: sha256:069f8f4fda0a510bdca4922b356bcdfdb431b33d2c540eb64c54e6e413cc55b4
    Status: Downloaded newer image for harbor-server.ilinux.io/skywalking/apache/skywalking-ui:9.3.0
    Creating elasticsearch ... done
    Creating skywalking-oap ... done
    Creating skywalking-compose_skywalking-ui_1 ... done
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# ss -tnl
    State               Recv-Q              Send-Q                           Local Address:Port                            Peer Address:Port              Process              
    LISTEN              0                   4096                                   0.0.0.0:8080                                 0.0.0.0:*                                      
    LISTEN              0                   4096                                   0.0.0.0:9200                                 0.0.0.0:*                                      
    LISTEN              0                   4096                             127.0.0.53%lo:53                                   0.0.0.0:*                                      
    LISTEN              0                   128                                    0.0.0.0:22                                   0.0.0.0:*                                      
    LISTEN              0                   4096                                   0.0.0.0:11800                                0.0.0.0:*                                      
    LISTEN              0                   4096                                   0.0.0.0:12800                                0.0.0.0:*                                      
    LISTEN              0                   4096                                      [::]:8080                                    [::]:*                                      
    LISTEN              0                   4096                                      [::]:9200                                    [::]:*                                      
    LISTEN              0                   4096                                      [::]:11800                                   [::]:*                                      
    LISTEN              0                   4096                                      [::]:12800                                   [::]:*                                      
    root@skywalking-docker-compose:/usr/local/src/skywalking-compose# 
    

> 没有报错，对应服务的端口都处于正常监听状态，则表示服务启动成功；

### 验证elasticsearch 数据

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260721232100788-147662767.png)

> 能够正常用浏览器访问服务器的9200端口并打印出数据，表示elasticsearch部署成功；

### 验证skywalking web

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260721232147823-462391842.png)

> 能够正常用浏览器访问服务器的8080端口，说明skywalking部署成功；以上就是基于docker-compose部署skywalking的全部过程；


---
> 原文链接: https://www.cnblogs.com/qiuhom-1874/p/21657975