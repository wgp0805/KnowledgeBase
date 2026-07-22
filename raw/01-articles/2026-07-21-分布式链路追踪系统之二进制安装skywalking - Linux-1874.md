---
title: "分布式链路追踪系统之二进制安装skywalking - Linux-1874"
source: "博客园"
url: "https://www.cnblogs.com/qiuhom-1874/p/21657915"
date: "2026-07-21T13:35:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 分布式链路追踪系统之二进制安装skywalking - Linux-1874

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/qiuhom-1874/p/21657915  
> **抓取日期**: 2026-07-21  
> **相关性评分**: 0.7

### skywalking架构

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260719235804451-884506436.png)

> skywalking服务端主要由前端的skywalking-ui、和后端的skywalking-oap两大组件组成；其工作流程大致是各agent通过grpc或http协议将指标数据发送给skywalking服务端即skywalking-oap；服务端将收到的指标数据存储第三方存储系统，如es，mysql等；通过前端skywalking-ui来展示对应的监控指标数据；

  * skywalking-ui: 前端服务,端口号8080。
  * skywalking-oap(Observability Analysis Platform)：可观测性分析平台,11800为gRPC数据端口，12800为http数据端口。
  * es：9200为elasticsearch的数据读写端口，目前skywalking支持的存储有elasticsearch、h2、mysql、tidb、influxdb、postgresql等。
  * agent: app服务器部署skywalking agent，用于收集app中的访问请求。



### 部署elasticsearch

#### 调整内核参数
    
    
    root@skywalking-es-server:~# tail -2 /etc/sysctl.conf
    net.ipv4.ip_forward = 1
    vm.max_map_count=262144
    root@skywalking-es-server:~# sysctl -p
    net.ipv4.ip_forward = 1
    vm.max_map_count = 262144
    root@skywalking-es-server:~# cat /proc/sys/vm/max_map_count
    262144
    root@skywalking-es-server:~# cat /proc/sys/net/ipv4/ip_forward
    1
    root@skywalking-es-server:~# 
    

> net.ipv4.ip_forward = 1表示开启ipv4转发；vm.max_map_count参数用来定义每个进程可拥有的虚拟内存区域（Virtual Memory Area, VMA）的最大数量。这个内核参数默认是65530，一般大型java应用推荐设置为>=262144；Kafka/Cassandra >= 131072;ClickHouse >= 131072;Elasticsearch = 262144;

#### 上传elasticsearch deb包到服务器
    
    
    root@skywalking-es-server:~# rz
    rz waiting to receive.
     zmodem trl+C ȡ
    
      100%  567155 KB 25779 KB/s 00:00:22       0 Errors64.deb...
    
    root@skywalking-es-server:~# ls
    elasticsearch-8.5.1-amd64.deb
    root@skywalking-es-server:~# mv elasticsearch-8.5.1-amd64.deb /usr/local/src/
    root@skywalking-es-server:~# cd /usr/local/src/
    root@skywalking-es-server:/usr/local/src# ls
    elasticsearch-8.5.1-amd64.deb
    

#### 安装elasticsearch
    
    
    root@skywalking-es-server:/usr/local/src# ls
    elasticsearch-8.5.1-amd64.deb
    root@skywalking-es-server:/usr/local/src# dpkg -i elasticsearch-8.5.1-amd64.deb 
    Selecting previously unselected package elasticsearch.
    (Reading database ... 65695 files and directories currently installed.)
    Preparing to unpack elasticsearch-8.5.1-amd64.deb ...
    Creating elasticsearch group... OK
    Creating elasticsearch user... OK
    Unpacking elasticsearch (8.5.1) ...
    Setting up elasticsearch (8.5.1) ...
    --------------------------- Security autoconfiguration information ------------------------------
    
    Authentication and authorization are enabled.
    TLS for the transport and HTTP layers is enabled and configured.
    
    The generated password for the elastic built-in superuser is : XXtjREgVek*MIN9mFNKB
    
    If this node should join an existing cluster, you can reconfigure this with
    '/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token-here>'
    after creating an enrollment token on your existing cluster.
    
    You can complete the following actions at any time:
    
    Reset the password of the elastic built-in superuser with 
    '/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic'.
    
    Generate an enrollment token for Kibana instances with 
     '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana'.
    
    Generate an enrollment token for Elasticsearch nodes with 
    '/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node'.
    
    -------------------------------------------------------------------------------------------------
    ### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using systemd
     sudo systemctl daemon-reload
     sudo systemctl enable elasticsearch.service
    ### You can start elasticsearch service by executing
     sudo systemctl start elasticsearch.service
    root@skywalking-es-server:/usr/local/src# 
    

#### 配置elasticsearch
    
    
    root@skywalking-es-server:/usr/local/src# grep -v "#" /etc/elasticsearch/elasticsearch.yml | grep -v "^$"
    cluster.name: es1
    node.name: node1
    path.data: /var/lib/elasticsearch
    path.logs: /var/log/elasticsearch
    network.host: 192.168.112.71
    http.port: 9200
    discovery.seed_hosts: ["192.168.112.71", ]
    cluster.initial_master_nodes: ["192.168.112.71", ]
    xpack.security.enabled: false
    xpack.security.enrollment.enabled: false
    xpack.security.http.ssl:
      enabled: false
      keystore.path: certs/http.p12
    xpack.security.transport.ssl:
      enabled: false
      verification_mode: certificate
      keystore.path: certs/transport.p12
      truststore.path: certs/transport.p12
    http.host: 0.0.0.0
    root@skywalking-es-server:/usr/local/src# 
    

> 如果是单机模式按照上述配置即可，对应IP地址就是服务器IP地址；集群部署和配置请参考本人博客<https://www.cnblogs.com/qiuhom-1874/p/13758006.html>；

#### 启动elasticsearch
    
    
    root@skywalking-es-server:/usr/local/src# systemctl daemon-reload
    root@skywalking-es-server:/usr/local/src# systemctl start elasticsearch
    root@skywalking-es-server:/usr/local/src# systemctl enable elasticsearch
    Created symlink /etc/systemd/system/multi-user.target.wants/elasticsearch.service → /lib/systemd/system/elasticsearch.service
    root@skywalking-es-server:/usr/local/src# systemctl status elasticsearch
    ● elasticsearch.service - Elasticsearch
         Loaded: loaded (/lib/systemd/system/elasticsearch.service; enabled; vendor preset: enabled)
         Active: active (running) since Mon 2026-07-20 14:17:02 UTC; 5min ago
           Docs: https://www.elastic.co
       Main PID: 103849 (java)
          Tasks: 87 (limit: 4534)
         Memory: 2.4G
            CPU: 40.076s
         CGroup: /system.slice/elasticsearch.service
                 ├─103849 /usr/share/elasticsearch/jdk/bin/java -Xms4m -Xmx64m -XX:+UseSerialGC -Dcli.name=server -Dcli.script=/usr/share/elasticsearch/bin/elasticsearch -Dcli
    .libs=lib/tools/server-cli -Des.path.home=/usr/share/elasticsearch -Des.path.conf=/etc/elasticsearch -Des.distribution.type=deb -cp "/usr/share/elasticsearch/lib/*:/usr/sh
    are/elasticsearch/lib/cli-launcher/*" org.elasticsearch.launcher.CliToolLauncher -p /var/run/elasticsearch/elasticsearch.pid --quiet
                 ├─103917 /usr/share/elasticsearch/jdk/bin/java -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=10 -Djava.security.manager=allow -XX:+A
    lwaysPreTouch -Xss1m -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djna.nosys=true -XX:-OmitStackTraceInFastThrow -Dio.netty.noUnsafe=true -Dio.netty.noKeySetOptimizatio
    n=true -Dio.netty.recycler.maxCapacityPerThread=0 -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true -Dlog4j2.formatMsgNoLookups=true -Djava.locale.providers=SPI,
    COMPAT --add-opens=java.base/java.io=ALL-UNNAMED -XX:+UseG1GC -Djava.io.tmpdir=/tmp/elasticsearch-6403631656827745021 -XX:+HeapDumpOnOutOfMemoryError -XX:+ExitOnOutOfMemor
    yError -XX:HeapDumpPath=/var/lib/elasticsearch -XX:ErrorFile=/var/log/elasticsearch/hs_err_pid%p.log "-Xlog:gc*,gc+age=trace,safepoint:file=/var/log/elasticsearch/gc.log:u
    tctime,pid,tags:filecount=32,filesize=64m" -Xms1944m -Xmx1944m -XX:MaxDirectMemorySize=1019215872 -XX:G1HeapRegionSize=4m -XX:InitiatingHeapOccupancyPercent=30 -XX:G1Reser
    vePercent=15 -Des.distribution.type=deb --module-path /usr/share/elasticsearch/lib --add-modules=jdk.net -m org.elasticsearch.server/org.elasticsearch.bootstrap.Elasticsea
    rch
                 └─103950 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
    
    Jul 20 14:16:49 skywalking-es-server.ilinux.io systemd[1]: Starting Elasticsearch...
    Jul 20 14:17:02 skywalking-es-server.ilinux.io systemd[1]: Started Elasticsearch.
    root@skywalking-es-server:/usr/local/src# ss -tnl
    State              Recv-Q             Send-Q                                   Local Address:Port                         Peer Address:Port            Process             
    LISTEN             0                  4096                                     127.0.0.53%lo:53                                0.0.0.0:*                                   
    LISTEN             0                  128                                            0.0.0.0:22                                0.0.0.0:*                                   
    LISTEN             0                  4096                                                 *:9200                                    *:*                                   
    LISTEN             0                  4096                           [::ffff:192.168.112.71]:9300                                    *:*                                   
    root@skywalking-es-server:/usr/local/src# 
    

> 能够看到9200端口正常监听说明es启动成功；

### 部署skywalking

#### 准备java环境
    
    
    root@skywalking-server:~# apt install openjdk-11-jdk -y
    

**验证java版本信息**
    
    
    root@skywalking-server:~# java --version
    openjdk 11.0.31 2026-04-21
    OpenJDK Runtime Environment (build 11.0.31+11-post-1ubuntu1-22.04.2-Ubuntu)
    OpenJDK 64-Bit Server VM (build 11.0.31+11-post-1ubuntu1-22.04.2-Ubuntu, mixed mode, sharing)
    root@skywalking-server:~# 
    

> 能够使用java --version命令能够正常看到jdk对应版本信息即表示对应版本的javajdk安装成功；

#### 上传skywalking 二进制包到服务器
    
    
    root@skywalking-server:~# cd /usr/local/src/
    root@skywalking-server:/usr/local/src# rz
    rz waiting to receive.
     zmodem trl+C ȡ
    
      100%  136193 KB 17024 KB/s 00:00:08       0 Errors.3.0.tar.gz...
    
    root@skywalking-server:/usr/local/src# ls
    apache-skywalking-apm-9.3.0.tar.gz
    root@skywalking-server:/usr/local/src# 
    

#### 解压skywalking二进制包
    
    
    root@skywalking-server:/usr/local/src# tar xf apache-skywalking-apm-9.3.0.tar.gz 
    root@skywalking-server:/usr/local/src# ls
    apache-skywalking-apm-9.3.0.tar.gz  apache-skywalking-apm-bin
    root@skywalking-server:/usr/local/src# 
    

#### 软连接skywalking
    
    
    root@skywalking-server:/usr/local/src# ls
    apache-skywalking-apm-9.3.0.tar.gz  apache-skywalking-apm-bin
    root@skywalking-server:/usr/local/src# ln -s apache-skywalking-apm-bin skywalking
    root@skywalking-server:/usr/local/src# ll
    total 136208
    drwxr-xr-x  3 root root      4096 Jul 20 14:37 ./
    drwxr-xr-x 10 root root      4096 Feb 17  2023 ../
    -rw-r--r--  1 root root 139461881 Aug 31  2023 apache-skywalking-apm-9.3.0.tar.gz
    drwxr-xr-x  9 root root      4096 Feb 17  2022 apache-skywalking-apm-bin/
    lrwxrwxrwx  1 root root        25 Jul 20 14:37 skywalking -> apache-skywalking-apm-bin/
    root@skywalking-server:/usr/local/src# 
    

#### 配置skywalking
    
    
    root@skywalking-server:/usr/local/src/skywalking/config# pwd
    /usr/local/src/skywalking/config
    root@skywalking-server:/usr/local/src/skywalking/config# vim application.yml
    storage:
      selector: ${SW_STORAGE:elasticsearch}
      elasticsearch:
        namespace: ${SW_NAMESPACE:""}
        clusterNodes: ${SW_STORAGE_ES_CLUSTER_NODES:192.168.112.71:9200}
    

> 打开skywalking/config目录下application.yml配置文件，找到storage配置段，配置使用es作为存储，并在es段里配置对应es集群的地址（单个es就填写对应服务器的地址即可）；

#### 编写skywalking.service文件
    
    
    root@skywalking-server:/usr/local/src/skywalking/config# cat /etc/systemd/system/skywalking.service
    [Unit]
    Description=ApacheSkywalking
    After=network.target
    
    [Service]
    Type=oneshot
    User=root
    WorkingDirectory=/usr/local/src/skywalking/bin/
    ExecStart=/bin/bash  /usr/local/src/skywalking/bin/startup.sh
    RemainAfterExit=yes
    RestartSec=5
    
    [Install]
    WantedBy=multi-user.target
    root@skywalking-server:/usr/local/src/skywalking/config#
    

> 使用上述service文件需要注意修改自己环境程序对应pash路径

#### 启动skywalking
    
    
    root@skywalking-server:/usr/local/src/skywalking/config# systemctl daemon-reload
    root@skywalking-server:/usr/local/src/skywalking/config# systemctl start skywalking  
    root@skywalking-server:/usr/local/src/skywalking/config# systemctl enable skywalking
    Created symlink /etc/systemd/system/multi-user.target.wants/skywalking.service → /etc/systemd/system/skywalking.service.
    root@skywalking-server:/usr/local/src/skywalking/config# ss -tnl
    State               Recv-Q              Send-Q                           Local Address:Port                            Peer Address:Port              Process              
    LISTEN              0                   4096                             127.0.0.53%lo:53                                   0.0.0.0:*                                      
    LISTEN              0                   128                                    0.0.0.0:22                                   0.0.0.0:*                                      
    LISTEN              0                   4096                                         *:8080                                       *:*                                      
    LISTEN              0                   4096                                         *:11800                                      *:*                                      
    LISTEN              0                   4096                                         *:12800                                      *:*                                      
    root@skywalking-server:/usr/local/src/skywalking/config# 
    

> 能够看到8080、11800和12800这三个端口处监听状态，说明skywalking服务端部署成功；

### 验证skywalking web界面

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260720231339402-129976131.png)

> 用浏览器访问skywalking服务器的8080端口，如果能够正常访问，说明skywalking服务器部署成功；

### 验证elasticsearch 数据

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260720231847755-634839731.png)

> 用浏览器访问es服务器的9200端口，如果能够正常访问并返回相应信息，说明es服务器部署成功；到此二进制部署skywalking服务就完成了；


---
> 原文链接: https://www.cnblogs.com/qiuhom-1874/p/21657915