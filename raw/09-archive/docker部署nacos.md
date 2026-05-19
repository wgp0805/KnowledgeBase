---
title: docker部署nacos
tags:
  - nacos
categories:
  - nacos
date: 2026-03-31 10:49:46
---

# docker部署nacos

查看nacos官网

https://nacos.io/zh-cn/docs/1.X/v2/quickstart/quick-start-docker

进行操作

```shell
docker run -d -p 8848:8848 -p 9848:9848 --name nacos --network docker-net -e MODE=standalone -e TIME_ZONE='Asia/Shanghai' -e MYSQL_SERVICE_HOST='192.168.0.254' -e MYSQL_SERVICE_DB_NAME='pmhub-nacos' -e MYSQL_SERVICE_PORT='3306' -e MYSQL_SERVICE_USER='root' -e MYSQL_SERVICE_PASSWORD='123456' -e SPRING_DATASOURCE_PLATFORM='mysql' nacos/nacos-server:v2.2.3
//nacos在docker的配置文件会从启动命令上取参数,但是加上mysql后就报错了。起不来，所以决定使用原来的命令部署


```

## 命令解释

表格



| 参数                                              | 含义说明                                                     |
| :------------------------------------------------ | :----------------------------------------------------------- |
| **`-d`**                                          | 后台运行容器，并返回容器 ID。                                |
| **`--name nacos`**                                | 为容器指定一个名称，这里是 `nacos`，方便后续管理。           |
| **`--network docker-net`**                        | 将容器连接到名为 `docker-nacos` 的自定义网络，这样它才能通过容器名访问同网络的 MySQL。 |
| **`-p 8848:8848`**                                | 将容器的 8848 端口映射到宿主机。这是 Nacos 的 HTTP API 和控制台访问端口。 |
| **`-p 9848:9848`**                                | 将容器的 9848 端口映射到宿主机。这是 Nacos 2.x 版本新增的 gRPC 通信端口。 |
| **`-p 9849:9849`**                                | 将容器的 9849 端口映射到宿主机。这也是 Nacos 2.x 版本新增的 gRPC 通信端口。 |
| **`-e MODE=standalone`**                          | 设置 Nacos 的运行模式为单机模式（standalone），不组建集群。  |
| **`-e SPRING_DATASOURCE_PLATFORM=mysql`**         | 指定数据源平台为 MySQL，启用外部数据库存储配置信息。         |
| **`-e MYSQL_SERVICE_HOST=mysql`**                 | 指定 MySQL 数据库的主机地址。因为在同一 Docker 网络下，这里直接填写 MySQL 容器的名称 `mysql`。 |
| **`-e MYSQL_SERVICE_PORT=3306`**                  | 指定 MySQL 数据库的服务端口，默认为 3306。                   |
| **`-e MYSQL_SERVICE_DB_NAME=nacos_config`**       | 指定 Nacos 使用的数据库名称，需与你预先在 MySQL 中创建的数据库名一致。 |
| **`-e MYSQL_SERVICE_USER=root`**                  | 指定连接 MySQL 的用户名。                                    |
| **`-e MYSQL_SERVICE_PASSWORD=...`**               | 指定连接 MySQL 的密码。                                      |
| **`-v D:\dockerDir\nacos\logs:/home/nacos/logs`** | 将宿主机的 `D:\dockerDir\nacos\logs` 目录挂载到容器内的 `/home/nacos/logs`，实现日志持久化。 |
| **`-v D:\dockerDir\nacos\conf:/home/nacos/conf`** | 将宿主机的 `D:\dockerDir\nacos\conf` 目录挂载到容器内的 `/home/nacos/conf`，实现配置文件持久化。 |
| **`nacos/nacos-server`**                          | 指定要运行的 Docker 镜像名称。                               |



## Nacos的docker启动可以配置的参数

| 属性名称                                | 描述                                               | 选项                                                         |
| --------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| MODE                                    | 系统启动方式: 集群/单机                            | cluster/standalone默认 **cluster**                           |
| NACOS_SERVERS                           | 集群地址                                           | p1空格ip2空格ip3                                             |
| PREFER_HOST_MODE                        | 支持IP还是域名模式                                 | hostname/ip 默认 **ip**                                      |
| NACOS_SERVER_PORT                       | Nacos 运行端口                                     | 默认 **8848**                                                |
| NACOS_SERVER_IP                         | 多网卡模式下可以指定IP                             |                                                              |
| SPRING_DATASOURCE_PLATFORM              | 单机模式下支持MYSQL数据库                          | mysql / 空 默认:空                                           |
| MYSQL_SERVICE_HOST                      | 数据库 连接地址                                    |                                                              |
| MYSQL_SERVICE_PORT                      | 数据库端口                                         | 默认 : **3306**                                              |
| MYSQL_SERVICE_DB_NAME                   | 数据库库名                                         |                                                              |
| MYSQL_SERVICE_USER                      | 数据库用户名                                       |                                                              |
| MYSQL_SERVICE_PASSWORD                  | 数据库用户密码                                     |                                                              |
| MYSQL_SERVICE_DB_PARAM                  | 数据库连接参数                                     | default : **characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true&useSSL=false** |
| MYSQL_DATABASE_NUM                      | 数据库编号                                         | 默认 :**1**                                                  |
| JVM_XMS                                 | -Xms                                               | 默认 :1g                                                     |
| JVM_XMX                                 | -Xmx                                               | 默认 :1g                                                     |
| JVM_XMN                                 | -Xmn                                               | 默认 :512m                                                   |
| JVM_MS                                  | -XX                                                | 默认 :128m                                                   |
| JVM_MMS                                 | -XX                                                | 默认 :320m                                                   |
| NACOS_DEBUG                             | 是否开启远程DEBUG                                  | y/n 默认                                                     |
| TOMCAT_ACCESSLOG_ENABLED                | server.tomcat.accesslog.enabled                    | 默认                                                         |
| NACOS_AUTH_SYSTEM_TYPE                  | 权限系统类型选择,目前只支持nacos类型               | 默认                                                         |
| NACOS_AUTH_ENABLE                       | 是否开启权限系统                                   | 默认                                                         |
| NACOS_AUTH_TOKEN_EXPIRE_SECONDS         | token 失效时间                                     | 默认 :18000                                                  |
| NACOS_AUTH_TOKEN                        | token                                              | 默认                                                         |
| NACOS_AUTH_CACHE_ENABLE                 | 权限缓存开关 ,开启后权限缓存的更新默认有15秒的延迟 | 默认 : false                                                 |
| MEMBER_LIST                             | 通过环境变量的方式设置集群地址                     | 例子:192.168.16.101:8847?raft_port=8807,192.168.16.101?raft_port=8808,192.168.16.101:8849?raft_port=8809 |
| EMBEDDED_STORAGE                        | 是否开启集群嵌入式存储模式                         | `embedded` 默认 : none                                       |
| NACOS_AUTH_CACHE_ENABLE                 | nacos.core.auth.caching.enabled                    | default : false                                              |
| NACOS_AUTH_USER_AGENT_AUTH_WHITE_ENABLE | nacos.core.auth.enable.userAgentAuthWhite          | default : false                                              |
| NACOS_AUTH_IDENTITY_KEY                 | nacos.core.auth.server.identity.key                | default : serverIdentity                                     |
| NACOS_AUTH_IDENTITY_VALUE               | nacos.core.auth.server.identity.value              | default : security                                           |
| NACOS_SECURITY_IGNORE_URLS              | nacos.security.ignore.urls                         |                                                              |

## 如果上述操作起不来，就要自行处理配置文件了

```shell

docker run -d -p 8848:8848 -p 9848:9848 --name nacos2 -e MODE=standalone -e TIME_ZONE='Asia/Shanghai' nacos/nacos-server:v2.2.3

然后切入nacos容器中修改配置文件
docker exec -it nacos2 /bin/bash
//进入目录
cd /home/nacos/conf
```

拉取镜像

```
docker pull nacos/nacos-server:v2.2.3
```

拷贝文件

```
mkdir -p /data/nacos/{conf,logs,data}

docker run -p 8848:8848 --name nacos -d nacos/nacos-server:v2.2.3

docker cp nacos:/home/nacos/conf /data/nacos  # 如果是windows上的docker需要指定盘符下的绝对路径
docker cp nacos:/home/nacos/data /data/nacos
docker cp nacos:/home/nacos/logs /data/nacos

chmod 777 /data/nacos/{conf,logs,data}

docker rm -f nacos
```

修改配置文件 [application.properties](..\..\..\IDEA\project\pmhub\nacos\conf\application.properties) 新版本Nacos默认不开启鉴权

直接复制就可，然后修改最上边的mysql链接然后换成自己的数据库链接和密码即可

```
spring.datasource.platform=mysql
db.num=1
db.url.0=jdbc:mysql://192.168.100.100:3306/pmhub-nacos?characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true&useUnicode=true&useSSL=false&serverTimezone=UTC
db.user=root
db.password=123456

# 当服务为空时，是否自动清理
nacos.naming.empty-service.auto-clean=true
# 空服务清理的初始延迟时间（毫秒）
nacos.naming.empty-service.clean.initial-delay-ms=50000
# 空服务清理的周期时间（毫秒）
nacos.naming.empty-service.clean.period-time-ms=30000

# 允许暴露的 Web 端点（用于监控和管理）
management.endpoints.web.exposure.include=*

# 禁用 Elastic 的指标导出
management.metrics.export.elastic.enabled=false
# 禁用 Influx 的指标导出
management.metrics.export.influx.enabled=false

# 启用 Tomcat 的访问日志
server.tomcat.accesslog.enabled=true
# Tomcat 访问日志的格式
server.tomcat.accesslog.pattern=%h %l %u %t "%r" %s %b %D %{User-Agent}i %{Request-Source}i
# 设置 Tomcat 的基目录
server.tomcat.basedir=file:.

# 定义忽略安全验证的 URL 列表
nacos.security.ignore.urls=/,/error,/**/*.css,/**/*.js,/**/*.html,/**/*.map,/**/*.svg,/**/*.png,/**/*.ico,/console-ui/public/**,/v1/auth/**,/v1/console/health/**,/actuator/**,/v1/console/server/**
# 禁用 Istio MCP 服务器功能
nacos.istio.mcp.server.enabled=false
# 是否开启鉴权功能
nacos.core.auth.enabled=true
# 鉴权类型
nacos.core.auth.system.type=nacos
# 默认鉴权插件用于生成用户登陆临时accessToken所使用的密钥，使用默认值有安全风险
nacos.core.auth.plugin.nacos.token.secret.key=SecretKey01234567890123456789012112345678901234567890123456789012345678
# 用户登陆临时accessToken的过期时间，2.1.0及以上版本使用
nacos.core.auth.plugin.nacos.token.expire.seconds=18000
# 是否使用useragent白名单，主要用于适配老版本升级，置为true时有安全风险
nacos.core.auth.enable.userAgentAuthWhite=false
# 用于替换useragent白名单的身份识别key，使用默认值有安全风险（2.2.1后无默认值）
nacos.core.auth.server.identity.key=serverIdentity-laigeoffer-pmhub
# 用于替换useragent白名单的身份识别value，使用默认值有安全风险
nacos.core.auth.server.identity.value=security-laigeoffer-pmhub-666
# 启用 Nacos 的核心认证缓存机制
nacos.core.auth.caching.enabled=true
```

创建容器

MYSQL_SERVICE_HOST=192.168.100.100 修改为自己的ip

MYSQL_SERVICE_PASSWORD=ovo@Knight修改为自己的密码

**liunx使用**

```
docker run -d \
-e MODE=standalone \
--privileged=true \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.100.100 \ # 换成自己的服务器IP地址
-e MYSQL_SERVICE_PORT=3306 \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=ovo@Knight \   # 换成自己MYSQL的密码
-e MYSQL_SERVICE_DB_NAME=pmhub-nacos \
-e TIME_ZONE='Asia/Shanghai' \
-v /data/nacos/logs:/home/nacos/logs \
-v /data/nacos/data:/home/nacos/data \
-v /data/nacos/conf:/home/nacos/conf \
-p 8848:8848 -p 9848:9848 -p 9849:9849 \
--name nacos --restart=always nacos/nacos-server:v2.2.3
```

**windows使用**

```
docker run -d \
-e MODE=standalone \
--privileged=true \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.100.100 \ # 换成自己的服务器IP地址
-e MYSQL_SERVICE_PORT=3306 \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=ovo@Knight \   # 换成自己MYSQL的密码
-e MYSQL_SERVICE_DB_NAME=pmhub-nacos \
-e TIME_ZONE='Asia/Shanghai' \
-v D:\dockerDir\dockerData\nacos/logs:/home/nacos/logs \
-v D:\dockerDir\dockerData\nacos/data:/home/nacos/data \
-v D:\dockerDir\dockerData\nacos/conf:/home/nacos/conf \
-p 8848:8848 -p 9848:9848 -p 9849:9849 \
--name nacos --restart=always nacos/nacos-server:v2.2.3
```

