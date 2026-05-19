---
title: pmhub微服务学习
tags:
  - 标签
categories:
  - 分类
date: 2026-03-31 09:01:44
---

# pmhub微服务项目的学习路线

今天再给大家分享一下[微服务 PmHub](https://javabetter.cn/zhishixingqiu/pmhub.html)的学习路线。你可以套用到任何一个开源的项目上去。

https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/xicrzm3xe48fnynz 最全的文档

## 第一阶段，让项目跑起来 

第一步别想太多，先让系统跑起来。你要做的就是让它能启动、能登录、能点几下不报错。

先准备好环境：JDK、Maven、Docker，一个都不能少。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe1479-image3104.png)

macOS 用户可以看这部分教程。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe2347-image4032.png)

你可以按照传统的方式，一个一个安装前置环境，最好版本保持一致，微服务的很多坑就版本上。

当然你也可以执行 docker-compose，把 Nacos、Redis、MySQL、Seata 一键拉起来。Windows 用户看这部分教程。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe2478-image7592.png)

数据库表也别忘了建，sql 目录里有初始化脚本，顺序执行就行。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe8980-image7271.png)

然后去 Nacos 看配置，确认数据库和 Redis 的连接没问题。启动顺序建议是 Auth → System → Gateway → Project → Workflow。

前端进 pmhub-ui 执行 npm install && npm run dev，再打开浏览器试登录。能进系统，说明你已经跨过第一道门。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe7140-image2839.png)

## 第二阶段，理解项目骨架

这一步重点是“看懂它怎么前后端通信的”，别钻细节。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe1148-image3886.png)

这个阶段，重点看开篇词部分。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe1186-image7568.png)

从 pmhub-gateway 开始，它是流量入口，也是权限、限流、跨域的防线。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe1108-image9598.png)

配合实战篇去看，看完后要明白：为什么需要网关？它除了路由还能做什么？（提示：统一认证、限流、跨域）

然后看认证中心（pmhub-auth），理解登录、Token 生成和网关校验的全流程。

搞清楚请求是如何被 pmhub-auth 处理的？它是如何生成 Token 的？Token 生成后，后续请求是如何携带 Token，网关又是如何校验 Token 的？

接着看看服务间调用怎么搞的（pmhub-api），Feign 是如何跨服务调用的，为什么需要 FeignRequestInterceptor 来解决 Token 丢失。

可以先从系统模块（pmhub-system）下手，比如用户管理。顺着 Controller → Service → Mapper 看一遍调用链，理解一条请求是怎么落到数据库的。

接着研究项目管理模块（pmhub-project），这是 PmHub 的灵魂。挑一个功能，比如“创建项目”，看看它牵扯了哪些表、走了哪些逻辑。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe1712-image2653.png)

再去看工作流模块（pmhub-workflow），打开 Flowable 的流程定义 XML，对照前端的流程图，搞清楚“发起审批”和“任务审批”的背后是怎么跑的。

## 第三阶段，准备面试

大概搞清楚 PmHub 的业务和架构后，就可以着手去写简历了，可以参考这个例子。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe2217-image6466.png)

完整版我放在了这个帖子里 `https://t.zsxq.com/C98g5` 可以挑自己感兴趣的写到简历上。

然后对照面试篇的内容去看，重点掌握 Gateway、TTL、Docker compose、Redis 分布式锁、SkyWalking、lua 脚本+AOP、Sentinel+OpenFeign、Seata 事务一致性、RocketMQ 消息队列、缓存和数据库一致性等微服务着重考察的点。

![img](https://cdn.tobebetterjavaer.com/stutymore/yingshizhexinzizhuoshilingrenzeshe4516-image4768.png)

## 第四阶段，为期一个月冲刺

接下来，我再给大家制定一个为期一个月的冲刺计划，当然你可以根据自身的能力做调整，压缩到一周或者扩展到两个月。

### 第 1 周：环境搭建 & 架构认知（从 0 到跑起来）

**学习目标**：熟悉项目整体架构，完成本地启动，理解模块划分和技术栈选型。

| 模块     | 教程                                                         | 学习重点                                        |
| -------- | ------------------------------------------------------------ | ----------------------------------------------- |
| 新人入门 | [✅小白如何学习 PmHub（🌟新人必看）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/rgmpz6p0nk422wbw) [✅PmHub 架构及功能概览](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/olwhnsmirmhzhhwx) [✅PmHub 技术选型与设计](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/zxhphttl8xl2gip6) [✅PmHub 架构方案设计](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/ah8kok7o5iuvbwn1) | 理解单体与微服务架构、模块职责、组件间关系      |
| 环境搭建 | [✅PmHub环境搭建和本地启动说明](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/ei61n5k3o9gcqfxq) [PmHub搭建 MySQL 环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/cl8luh6bz5ql87nk) [✅PmHub搭建Redis环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wt31t5h51l9zhytx) [✅PmHub 搭建 Nacos 环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wbnm3ysyixv80dsc) [✅PmHub搭建Sentinel环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/xkft36y6nqwm8f85) | 搭建数据库、Redis、Nacos、Sentinel 本地运行环境 |
| 编码规范 | [✅PmHub架构师必备编码规范](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/ys3ze4l21urawk6i) | 学习代码规范、统一风格和异常处理模式            |

**✅ 周目标产出**

- 本地启动成功，服务能正常注册到 Nacos
- 理解核心模块关系与依赖（gateway、auth、biz、common 等）
- 熟悉项目配置文件、日志输出与运行日志定位

### 第 2 周：微服务核心机制（从会跑到能改）

**学习目标**：深入理解 Spring Cloud 体系，掌握服务注册、熔断、配置中心与接口调用。

| 模块           | 教程                                                         | 学习重点                                |
| -------------- | ------------------------------------------------------------ | --------------------------------------- |
| 服务注册与发现 | [✅PmHub 搭建 Nacos 环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wbnm3ysyixv80dsc) | 理解服务注册与动态配置刷新              |
| 熔断限流       | [✅PmHub搭建Sentinel环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/xkft36y6nqwm8f85) | 掌握流控规则、熔断策略与监控面板使用    |
| 消息驱动       | [✅PmHub搭建RocketMQ环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/kqmnatuixpoa4d8p) | 理解消息队列在异步与解耦中的作用        |
| 动态刷新配置   | [✅PmHub自定义配置注入&动态刷新](https://www.yuque.com/itwanger/az7yww/oobmcdkym1232f6k) | 实现 Nacos 配置热更新与灰度配置         |
| 日志与事件     | [✅PmHub日志链路追踪 & SkyWalking](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/bxpms6wo9qf07gt5) | 搭建 SkyWalking，实现链路追踪与性能分析 |

**✅ 周目标产出**

- 能在本地启动多个服务并通过 Nacos 注册发现
- 实现接口限流与熔断保护
- 能理解异步解耦在系统稳定性中的作用
- 通过 SkyWalking 观察服务调用链

### 第 3 周：部署运维与中间件（从能改到能上线）

**学习目标**：掌握容器化、部署流程、CI/CD 流程和监控预警。

| 模块          | 教程                                                         | 学习重点                                  |
| ------------- | ------------------------------------------------------------ | ----------------------------------------- |
| Docker 容器化 | [✅PmHub搭建Docker环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/sxftnr6xqk09v07m) | 学习 Dockerfile 构建、Compose 启动        |
| 持续集成      | ✅PmHub CI/CD 流程配置（未完成）                              | 了解 GitHub Actions 或 Jenkins 自动化部署 |
| 应用监控      | [✅PmHub搭建SkyWalking环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/bxpms6wo9qf07gt5) [✅整合 Prometheus & Grafana 实现应用监控](https://www.yuque.com/itwanger/az7yww/vayxxydapbpgdgg2) | 掌握链路追踪与监控指标配置                |
| 性能压测      | [✅PmHub JMeter 接口压测实操](https://www.yuque.com/itwanger/az7yww/gnku2zsr9eeexihs) | 使用 JMeter 模拟高并发，评估系统瓶颈      |
| 部署实战      | 结合 `docker-compose.yml` 模板部署全链路                     | 在本地或云服务器模拟生产环境              |

**✅ 周目标产出**

- 完成 Docker 容器部署
- 了解日志收集、性能监控、服务监控指标
- 能执行一次完整的压测并分析结果

### 第 4 周：实战开发与项目总结（从能跑到能复刻）

**学习目标**：掌握业务模块设计，能独立开发功能、优化架构并写入简历。

| 模块           | 教程                                                         | 学习重点                                       |
| -------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| 架构扩展与实战 | [✅PmHub 架构方案设计](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/ah8kok7o5iuvbwn1) [✅PmHub 技术选型与设计](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/zxhphttl8xl2gip6) | 分析架构优势、瓶颈与扩展方向                   |
| 项目优化       | 实现缓存、限流、异步消息等增强功能                           | 综合应用 Redis、Sentinel、MQ、线程池           |
| 简历优化       | [✅如何将 PmHub 写入简历（🌟新人必看）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/lgalyd4oo1ekkgn6) | 学会提炼项目亮点与量化成果                     |
| 常见问题       | [📚PmHub常见问题 Q&A](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/gnis2du7cehzz21x) | 熟悉常见坑点与调试技巧                         |
| 项目复盘       | 结合架构、部署、业务逻辑进行总结                             | 输出完整复盘文档（架构图 + 流程图 + 学习心得） |

**✅ 周目标产出**

- 能独立开发一个模块并上线运行
- 输出一份《PmHub 项目技术总结文档》
- 更新简历项目描述，准备面试讲解稿

### 学习节奏建议

| 周次    | 时间投入      | 学习重点             | 实践建议           |
| ------- | ------------- | -------------------- | ------------------ |
| 第 1 周 | 每天 2~3 小时 | 环境搭建、架构认知   | 本地运行、查看日志 |
| 第 2 周 | 每天 3 小时   | 微服务通信、限流熔断 | 多模块联调         |
| 第 3 周 | 每天 3~4 小时 | 部署运维、监控压测   | 容器部署实战       |
| 第 4 周 | 每天 4 小时   | 实战开发、总结汇报   | 输出文档与项目复盘 |

### 最终收获

- 能完整从零搭建并部署 PmHub 全链路系统
- 掌握企业级 Spring Cloud 架构思想
- 理解服务注册、熔断、配置、限流、追踪、监控等关键机制
- 有可展示、可讲解的项目经验可写入简历

贴个喜报鼓励一下大家吧，也希望更多的球友能来给二哥报喜（项目用的就是 PmHub+派聪明），缘分一场，让二哥也沾沾大家的光，😄

![img](https://cdn.tobebetterjavaer.com/stutymore/biaoti2025nian11yue9ri1313-image5917.png)

冲！

# Nacos的安装

手把手教你安装 PmHub 的前置环境 Nacos，一定要注意版本！！！！

Color1

星球里有球友反馈项目启动不起来，很大一部分是因为 Nacos 没有正常启动，因为 Nacos 有很多配置信息，而 PmHub 的各个服务启动又依赖于配置，所以必须要先启动 Nacos。

:::

Nacos 是微服务场景下的配置中心和注册中心，对 Nacos 还不太清楚的可以去官网了解一下：[Nacos 配置中心简介, Nacos 是什么](https://nacos.io/docs/v2.3/what-is-nacos/)

我简单解释一下：比如说现在有两个微服务 service-consumer 和 service-provider，它们两个服务之间如果需要通信的话，就需要先把 service-provider 注册到 Nacos，然后 service-consumer 才能通过 svcID 调用 service-provider 提供的服务。

![img](https://cdn.tobebetterjavaer.com/paicoding/f75492ea1f4127ecc59382972dcbb6af.png)

在 PmHub 中，我们也会把对应的服务比如说 pmhub-gateway、pmhub-auth、pmhub-project、pmhub-workflow 等等注册到 Nacos 中。

除此之外，我们也会把 PmHub 的配置信息移交给 Nacos 并且持久到 MySQL 中。

![img](https://cdn.tobebetterjavaer.com/stutymore/environment-20240819185338.png)

Nacos 的前置条件需要先安装 JDK，一般都是 8 以上，这个不需要担心，大家既然学到了微服务，JDK 肯定是已经安装过了。CPU、内存一般电脑应该都能满足，1 核 2G，改版的云服务器都能满足，就更别提大家现在手头上配置很高的电脑了。

![img](https://cdn.tobebetterjavaer.com/paicoding/df332670b53196167d9360b4dea3638e.png)

## Nacos Server 下载和安装

官网下载地址：[Nacos Server 下载](https://nacos.io/download/nacos-server/)

最新的版本做了一些鉴权方面的优化，大家也可以下载尝试，但 PmHub 这里用的[是 2.2.3 的版本](https://nacos.io/download/release-history/?spm=5238cd80.6a33be36.0.0.10651e5duugP37)，建议大家保持同步，防止意想不到的 bug。二哥本地就亲身体验过，一开始由于 MySQL 的密码为空，导致 Nacos 2.2.3 启动不了，就切换到了 2.3.2，结果和 Sentinel 无法通信，最后给 MySQL 加了密码，然后 Nacos 切换到了 2.2.3，和 Sentinel 之间的通信算是搞定了。

这个 bug 非常特么坑爹，因为谁能想到 2.2.3 不允许 MySQL 的密码为空，当时没有细看安装后的日志，就切换到了 2.3.2，然后 Nacos 也正常启动了，结果卡到了和 Sentinel 之间的通信。超级坑爹。

![img](https://cdn.tobebetterjavaer.com/paicoding/554a9999843d92fdaa42027aefe98bc4.png)

我下载后的解压目录如下所示（二哥这里是 macOS，但思路是一样的。Windows 可以看球友的部署教程：[🍍1. Windows 本地启动 PmHub](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/lb341rb4ygqvybo9)）：

![img](https://cdn.tobebetterjavaer.com/paicoding/5b47d230384510eb92e21d87f6d2cbe0.png)

**当然也可以直接通过 docker 安装**：

```bash
docker run -d -p 8848:8848 -p 9848:9848 --name nacos2 -e MODE=standalone -e TIME_ZONE='Asia/Shanghai' -e MYSQL_SERVICE_HOST='192.168.0.254' -e MYSQL_SERVICE_DB_NAME='pmhub-nacos' -e MYSQL_SERVICE_PORT='3306' -e MYSQL_SERVICE_USER='root' -e MYSQL_SERVICE_PASSWORD='123456' -e SPRING_DATASOURCE_PLATFORM='mysql' nacos/nacos-server:v2.2.3
//nacos在docker的配置文件会从启动命令上取参数,但是加上mysql后就报错了。起不来，所以决定使用原来的命令部署

docker run -d -p 8848:8848 -p 9848:9848 --name nacos2 -e MODE=standalone -e TIME_ZONE='Asia/Shanghai' nacos/nacos-server:v2.2.3

然后切入nacos容器中修改配置文件
docker exec -it nacos2 /bin/bash
//进入目录
cd /home/nacos/conf

```

Nacos的docker启动可以配置的参数

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



## Nacos 的持久化配置

PmHub 将 Nacos 中的配置信息都持久化到 MySQL 中了，这样就可以避免每次 Nacos 重启后配置信息丢失。

Nacos 的默认配置文件在 `/conf/application.properties` 中。

![img](https://cdn.tobebetterjavaer.com/stutymore/environment-20240819190624.png)

这里，我们需要对 Nacos 默认配置中的 MySQL 链接信息配置下，就像我们在单体项目中配置 MySQL 的链接信息一样。

你也可以直接复制 `pmhub/docker/nacos/conf/application.properties` 覆盖 Nacos 的配置文件（最好提前做一次备份，养成好习惯）。

![img](https://cdn.tobebetterjavaer.com/stutymore/environment-20240819191117.png)

我对 Nacos 的配置信息做一些简单的介绍和说明，方便大家理解。

首先是 Nacos 中 DB（也就是 MySQL）的配置信息，主要是做 Nacos 的持久化：

```properties
spring.datasource.platform=mysql
db.num=1
db.url.0=jdbc:mysql://pmhub-mysql:3306/pmhub-nacos?characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true&useUnicode=true&useSSL=false&serverTimezone=UTC
db.user=root
db.password=laigeoffer-pmhub
```

1. 如果你的 Nacos 配置信息数据库名也是 pmhub-nacos，那么只需要修改 url（本地一般是 127.0.0.1）、用户名和密码即可。
2. 如果用户名也是 root，那么只需要修改密码即可。
3. 如果密码也一样，那么就不需要修改了（不可能，绝对不可能这么巧😂）。

然后是 Nacos 的一些常规配置，直接看注释吧，我就不废话了。

```properties
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
```

最后是鉴权部分的配置：

```properties
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

配置完成后，我们来启动 Nacos。

## Nacos 的启动

### macOS 用户启动 Nacos

①、如果你是 macOS 用户，可以直接在终端输入`sh startup.sh -m standalone`启动 Nacos。Windows 就是用 cmd 的启动。

![img](https://cdn.tobebetterjavaer.com/stutymore/environment-20240819193412.png)

注意看，我这里 Nacos 加载了 JDK 16 版本，但其实 PmHub 要求的是 JDK 8，主要是很多球友的版本还停留在 JDK8，为了做向下兼容，我们就没有使用最新的版本。

如果你的机器上装了多个 JDK 版本，可以在 starup.sh 中指定具体的 JDK 版本，比如说 JDK 8

![img](https://cdn.tobebetterjavaer.com/paicoding/bed16621ee9d1e821710a8e4f8fb2b0a.png)

这样启动的时候就会用对应的版本。

![img](https://cdn.tobebetterjavaer.com/paicoding/56874ccd0f03e75a773c34a58e64fefc.png)

也可以直接在 `~/.zshrc`中配置 JAVA_HOME。

![img](https://cdn.tobebetterjavaer.com/paicoding/02c50ee9a36066e1e89cde88d5542ab3.png)

或者[使用 jenv 进行管理](https://javabetter.cn/overview/jdk-install-config.html#_03、macos-安装-jdk)，确保 JDK 的版本是符合我们要求的（要求 `java -version`和 `echo $JAVA_HOME` 这两个结果都是 JDK 1.8），以免后续出现环境问题。

![img](https://cdn.tobebetterjavaer.com/paicoding/5bc6c814203fd6ac16ef87ba9f8aa027.png)

### Windows 用户启动 Nacos

如果你是 Windows 用户，可以直接双击 startup.cmd 启动 Nacos。参考：[🍍1. Windows 本地启动 PmHub](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/lb341rb4ygqvybo9)

## Nacos 的配置管理后台

启动成功后访问 http://localhost:8848/nacos 即可看到 Nacos 控制台（需要一定的反应时间，稍微等几秒，启动完直接访问会报错）。默认用户名密码都是 nacos。

也可以在 Nacos 的 logs 目录下查看 start.out（**一定注意，有错误，都在这里面**），看看版本、端口、后台管理是否 ok。

![img](https://cdn.tobebetterjavaer.com/paicoding/65bceb4ccaf909cd4ffa104643d84f50.png)

当出现两个红色框中的内容时，表明 Nacos 已经启动成功并且 MySQL 持久化是有效的。

![img](https://cdn.tobebetterjavaer.com/paicoding/45bc6dd34ffe00ee682067bbec802729.png)

点击详情，可以看到对应配置的详细信息。

![img](https://cdn.tobebetterjavaer.com/stutymore/environment-20240819193750.png)

如果启动失败，可以在 logs/start.out 查看启动日志。

![img](https://cdn.tobebetterjavaer.com/paicoding/9ebba50dfae36ba97a1cd666319778f5.png)

在启动项目前，请一定要保证 nacos 正常启动。

在启动项目前，请一定要保证 nacos 正常启动。

在启动项目前，请一定要保证 nacos 正常启动。

重要的事情说 3 遍！！😂

# PmHub 整合 Nacos 实现服务微服务注册及配置，全文 6000+字

PmHub 整合 Nacos 实现服务微服务注册及配置，全文 6000+字

球友好，欢迎来到 Nacos 这一篇。如果要考试划重点的话，我觉得此篇是重中之重。目前来说，在国内，注册中心和配置中心都是通过 Nacos 来完成的。

所以，学习本篇对实际上手工作（即便不是微服务）有很大的帮助。

## 前言

我们先来看一个问题，在单体应用中，所有的接口都打包成了一个 jar 包，然后放到服务器上去部署。这个时候，接口都是放在 controller 里面，一个接口要调另外一个接口，需要引入 service，然后通过 service 来调用。（不会AxxController 直接调用BxxController）。



![画板](https://cdn.tobebetterjavaer.com/paicoding/4e9b6d11c20a91a64bf36e486f2f974b.jpeg)画板



很好理解，对吧？也就是说单体内部如果需要调来调去就需要注入 service。

如果 service 需要调用外部服务呢？

我想有经验的你肯定会说，那还不简单，直接 http 调用呗，写上对方服务的 url，然后发起 post 请求或者 get 请求，等待响应结果就好了呀。比如下面这串代码：

```java
public class BaiduTranslateExample {
    public static void main(String[] args) throws Exception {
        // 请替换为您的AppID和密钥
        String appId = "YOUR_APP_ID";
        String secretKey = "YOUR_SECRET_KEY";

        // 待翻译的文本
        String query = "Hello world";
        // 翻译源语言和目标语言
        String from = "en";
        String to = "zh";

        // 随机数salt
        String salt = String.valueOf(new Random().nextInt(10000));
        // 签名计算: sign = MD5(appid+q+salt+密钥)
        String sign = md5(appId + query + salt + secretKey);

        // 构造参数
        String params = "q=" + URLEncoder.encode(query, StandardCharsets.UTF_8)
                + "&from=" + from
                + "&to=" + to
                + "&appid=" + appId
                + "&salt=" + salt
                + "&sign=" + sign;

        // Baidu翻译API地址
        String url = "https://fanyi-api.baidu.com/api/trans/vip/translate";

        // 使用HttpClient发送POST请求
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(params))
                .build();

        // 发送请求并获取响应
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        // 解析返回的JSON数据
        if (response.statusCode() == 200) {
            JSONObject json = new JSONObject(response.body());
            if (json.has("trans_result")) {
                // 提取翻译结果
                String result = json.getJSONArray("trans_result").getJSONObject(0).getString("dst");
                System.out.println("翻译结果: " + result);
            } else {
                System.out.println("翻译失败: " + response.body());
            }
        } else {
            System.out.println("请求失败，HTTP状态码: " + response.statusCode());
        }
    }
复制代码
```

注意，这里的 URL 需要写死。

那假设哪天百度翻译改了 URL 地址（虽然不大可能），我们是不是还得修改代码？那你可能要说，做成配置呀。

大哥，改个配置相当麻烦。（尤其是大厂，改线上配置的流程贼繁琐）

这是调用外部服务的例子， 假设调用的服务就是我们系统内部的，是个微服务，服务名变了，服务的 URL 也变了，有没有不用改代码和配置的办法呢？

当然有，那就是通过注册中心来完成。

什么是注册中心呢？

你可以这样理解，**注册中心就好比是整个微服务体系中服务的通讯录，\**\**它记录了服务和服务地址的映射关系**。



Nacos 的核心功能之一就是可以用来充当注册中心。



Nacos 的第二核心能力呢？



就是起到分布式配置中心的作用。很好理解，原先在本地 application.yml 中的配置，通通都可以放到 Nacos 配置中心去，改个配置，不用重启服务，妈妈再也不用担心我服务重启了，多省事呀。



好了，我花了大量篇幅来给你说明白两个事：

1、在分布式系统中，注册中心很有必要，而 Nacos 就是系统中服务的通讯录

2、Nacos 还可以充当微服务的配置中心。



那下面进入正篇。

## 什么是 Nacos？

不知道你有没有和我一样的癖好，看到一个名字，总喜欢去思考名字背后的故事和意义。

> 就好比 PmHub，我们就赋予了他不一样的寓意和故事，感兴趣的可以自行在[之前的文章中](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/osxtrri59x9zaf7g)了解哈。

Nacos 有什么寓意呢？

Nacos: Dynamic Naming and Configuration Service

翻译过来就是：**动态命名和配置服务**

前四个字母分别为 **Na**ming 和 **Co**nfiguration 的前两个字母，最后的 s 为 Service

不难理解，对应的其两大核心功能：**服务注册和配置**。

Nacos 是阿里巴巴开源的一个更易于构建云原生应用的动态服务发现、配置管理和服务管理平台。这是他的官网：https://nacos.io/

![img](https://cdn.tobebetterjavaer.com/paicoding/ab7dffdf2afcbe50a98bb844a33e3580.png)

很有科技感的背景，可以说是国产之光了。

用一句话总结下：Nacos 就是**注册中心**+**配置中心**的组合。



额外补充一点知识，不同注册中心的比较，这里苍何做了下总结：



| 服务注册与发现框架 | CAP模型 | 控制台管理 | 社区活跃度       |
| ------------------ | ------- | ---------- | ---------------- |
| Eureka             | AP      | 支持       | 低 (2.x版本闭源) |
| Zookeeper          | CP      | 不支持     | 中               |
| Consul             | CP      | 支持       | 高               |
| Nacos              | AP      | 支持       | 高               |

因为是阿里开源的，所以 Nacos 性能还是非常顶的，顶住了多个双十一的压力，在高并发场景下，Nacos 是相当给力。

其实，Nacos 默认是 AP 模式（最终一致性：数据可能暂时不一致），但也可以切换为 CP（强一致性：确保所有节点数据一致），我们一般就用默认的 AP。

下面是 Nacos 的设计理念，不难看出，其特性有：**易于使用、面向标准、高可用和方便扩展。**

------



![来自官网](https://cdn.tobebetterjavaer.com/paicoding/c3cd248e491f514932383245512b84b5.svg)来自官网



------

## Nacos 下载和安装

> 这部分在部署篇已经做了介绍，[✅PmHub 搭建 Nacos 本地环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wbnm3ysyixv80dsc)

## Nacos 做服务注册中心

服务注册中心不难理解，他是所有服务的「大管家」，在微服务架构中扮演中极其重要的角色。

我们知道，架构的重要性在于它影响了应用的**非功能性需求**，也成为**质量属性**或者**其他的能力**。

在微服务架构中，系统被拆分成了多个微服务，为了避免单点故障，微服务都会采用集群方式进行部署，集群的规模越大，性能也会越好。

比如现在 A 微服务想要调用 B 微服务，但是 B 微服务是集群部署，你不可能写死所有的集群中节点的地址，然后代码去控制他的调用吧？

所以就需要在 A 的配置文件中去维护 B 微服务的每个节点的请求地址，如果 B 集群中有个别几点宕机或者下线了，A 的配置文件中需要同步删除这些请求地址，防止请求发过去，人都已经不在了，白白找了个空。

那么，为了解决这些问题，就需要引入服务注册中心。



![wenxuehai：Nacos 注册中心](https://cdn.tobebetterjavaer.com/paicoding/677cc9d633a226610f07b1f8dfb12610.png)wenxuehai：Nacos 注册中心



服务注册中心主要解决以下问题：

- **服务地址的管理**
- **服务注册**
- **服务动态感知**

能够实现这些功能的有很多组件，像什么 Zookeeper 啊、Eureka 啊（这货前些年还很火，后面不行了），Consul 啊，但国内目前用的最多哦的还是国产之光 **Nacos**。

那也给大家给常用的服务注册中心组件做个总结，好给大家以后出去面试吹吹水：

| 特性                  | Zookeeper                                                  | Eureka                                               | Consul                                                     | Nacos                                                  |
| --------------------- | ---------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| **CAP 理论取舍**      | CP：保证一致性和分区容忍性，但在网络分区时可能导致不可用。 | AP：保证可用性和分区容忍性，但可能存在短暂的不一致。 | CP：保证一致性和分区容忍性，但在网络分区时可能导致不可用。 | CP/AP 可切换：用户可根据需求在一致性和可用性之间选择。 |
| **健康检查机制**      | 基于会话的心跳机制，失去连接即认为服务不健康。             | 需要显式配置健康检查支持。                           | 提供详细的健康检查，包括内存、文件系统等指标。             | 支持多种健康检查方式，包括传输层和应用层。             |
| **多数据中心支持**    | 需额外开发实现。                                           | 需额外开发实现。                                     | 原生支持多数据中心。                                       | 原生支持多数据中心。                                   |
| **KV 存储服务**       | 支持。                                                     | 不支持。                                             | 支持。                                                     | 支持。                                                 |
| **Watch 机制**        | 支持服务器端推送变化。                                     | 通过长轮询实现变化感知。                             | 通过长轮询实现变化感知。                                   | 通过长轮询实现变化感知。                               |
| **集群监控**          | 默认不支持 metrics。                                       | 默认不支持 metrics。                                 | 默认支持 metrics，便于监控和报警。                         | 默认不支持 metrics。                                   |
| **Spring Cloud 集成** | 提供相应的 starter，支持集成。                             | 提供相应的 starter，支持集成。                       | 提供相应的 starter，支持集成。                             | 提供相应的 starter，支持集成。                         |

------

**选择建议：**

- **Zookeeper**：适用于对一致性要求高的场景，但在网络分区时可能影响可用性。
- **Eureka**：适用于对可用性要求高的场景，容忍短暂的不一致，已停止维护，需谨慎选择。
- **Consul**：提供强一致性和丰富功能，适用于需要多数据中心部署的场景。
- **Nacos**：支持 CP/AP 模式切换，功能全面，适用于需要灵活性和多功能支持的场景。（目前国内应用首选）

### PmHub 如何使用 Nacos 注册服务？

在 PmHub 中如何使用 Nacos 注册服务呢？我们一起来看看吧。

1、在父工程的 pom.xml 中引入 alibaba.cloud 定义（统一约定版本，防止版本不兼容导致的问题）

![img](https://cdn.tobebetterjavaer.com/paicoding/3c91629bda41834a200370566a7af239.png)

2、在需要放入 Nacos 注册中心的微服务中添加以下依赖：

```xml
<!-- SpringCloud Alibaba Nacos -->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
复制代码
```

因为所有微服务都需要将自己注册进 Nacos，所以 PmHub 所有的服务模块都加了此依赖：

![img](https://cdn.tobebetterjavaer.com/paicoding/4d778f457f6ceef264107b16fd46c281.png)

3、在各自服务的 resource/bootstrap.yml 中添加 Nacos 作为注册中心的配置

```yaml
# Spring
spring: 
  application:
    # 应用名称
    name: pmhub-auth
  cloud:
    nacos:
      discovery:
        # 服务注册地址
        server-addr: 127.0.0.1:8848
        username: nacos
        password: nacos
复制代码
```

你可以发现 PmHub 的每个微服务都是这么配置的：

![img](https://cdn.tobebetterjavaer.com/paicoding/275d2a84c29976e44d3395297cc8bf9e.png)

4、在启动类中启动服务，然后去 Nacos 查看注册进来的服务。

Warning

重要：前提 Nacos 本身已经独立启动！

参考 1：[✅PmHub 搭建 Nacos 本地环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wbnm3ysyixv80dsc)

参考 2：[✅PmHub 在 MacOS 环境下的部署](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/ogytumlfziwre3vg)

参考 3：[✅PmHub在 Windows 环境下的部署（球友YaeMivo提供）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/xicrzm3xe48fnynz)

:::

完事就可以看到 PmHub 的所有服务都注册进来啦：

![img](https://cdn.tobebetterjavaer.com/paicoding/9c8affb1b78ac81edcc428df124a1cc3.png)

也就是说，从此以后，每个服务在注册中心都有一个唯一的名字了，以后大家看到这名字就知道对方是干嘛的了，比如说 pmhub-project 就是做项目管理的服务，pmhub-gateway 就是做网关的服务，pmhub-auth 就是做权限验证的服务。

是不是特别方便。

## Nacos 做服务配置中心

### 什么是配置中心？

在传统的单体应用中，配置通常直接写在应用的配置文件中，比如 application.properties 或 application.yml。



但在分布式架构中，每个服务都有自己的配置，并且这些配置可能会频繁变化（如数据库连接信息、服务调用地址、功能开关等）。如果每个服务独立管理配置，会导致以下问题：

1. **配置分散**：每个服务的配置都存储在自己的文件中，难以统一管理。
2. **更新繁琐**：如果需要修改某个配置（比如数据库密码），需要手动修改多个服务的配置文件并重启服务。
3. **一致性难保证**：配置的同步更新可能出现遗漏或版本不一致的情况。
4. **动态更新难**：部分配置需要支持实时更新，但传统方式需要重启服务才能生效。

配置中心正是为了解决这些问题而出现的。





![程序员小富：配置中心](https://cdn.tobebetterjavaer.com/paicoding/94ce32c46367e93c160c4796505839ac.png)程序员小富：配置中心





所有服务的配置统一存储在 Nacos 配置中心，开发者可以通过界面或 API 方便地查看和修改配置。



配置变更后会自动生效，无需重启服务。这通常依赖于配置中心的推送机制（如 Nacos 的实时推送）。





![程序员小富：Nacos 长轮询](https://cdn.tobebetterjavaer.com/paicoding/d426d1e3dbd1c221b09572175b636d9f.png)程序员小富：Nacos 长轮询



前面我们已经将 PmHub 的服务注册到 Nacos 中了，接下来我还需要将 PmHub 的一些配置信息通过 Nacos 持久化到 MySQL 中，以保证配置信息在服务重启后不丢失。

同时，Nacos 提供了一个易用的 web 管理界面，我们可以通过控制台发布、修改和删除配置。

客户端会通过长轮询方式定期向 Nacos 服务端发送请求，询问某个配置是否发生变化。如果服务端检测到配置有更新，会在长轮询请求的响应中返回最新的配置内容。



为了提升服务的高可用性，客户端会将从服务端获取的配置保存在本地文件中（例如 nacos-config.properties）。即使 Nacos 服务端暂时不可用，客户端也可以使用本地缓存的配置。



在复杂的微服务系统中，配置可能涉及到不同的环境（开发、测试、生产）和多个实例。配置中心可以根据环境存储多套配置（如开发环境用 dev 配置，生产环境用 prod 配置）。

### PmHub 如何使用 Nacos 配置服务？

1、在每个服务中添加 Nacos 配置依赖

```xml
<!-- springcloud alibaba nacos config -->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
复制代码
```

2、在各自服务的 bootstrap.yml添加Nacos配置

```yaml
# Spring
spring: 
  application:
    # 应用名称
    name: pmhub-auth
  profiles:
    # 环境配置
    active: dev
  cloud:
    nacos:
      config:
        # 配置中心地址
        server-addr: 127.0.0.1:8848
        # 配置文件格式
        file-extension: yml
        # 共享配置
        shared-configs:
          - application-${spring.profiles.active}.${spring.cloud.nacos.config.file-extension}
复制代码
```

特别说明，这里的共享配置，就是每个服务都共享的配置，有点类似于单体应用中的 application.yml。

![img](https://cdn.tobebetterjavaer.com/paicoding/d207eba52294df0b672f18ff3359fd42.png)

比如说在[技术派项目](https://javabetter.cn/zhishixingqiu/paicoding.html)中，dev 开发环境和 prod 生产环境中的配置都可以共享 application.yml 中的配置。

![img](https://cdn.tobebetterjavaer.com/paicoding/f81fb15e0e6cdf7c9b744fc7cd4d3cc4.png)

在 Nacos 中同样如此，各个服务的配置文件都可以共享 application-dev.yml 中的配置。

![img](https://cdn.tobebetterjavaer.com/paicoding/b653dd87ec1583ff06c69d4dae70ef7a.png)

配置文件加载的优先级（由高到低）

bootstrap.properties ->bootstrap.yml -> application.properties -> application.yml

3、在 Nacos 后台给每个微服务添加自己的配置

拿 pmhub-auth 这个服务为例，具体怎么添加呢？

点击+号：

![img](https://cdn.tobebetterjavaer.com/paicoding/35abf9795b2c9059a1c31f5f4a3626d2.png)

新建配置：

![img](https://cdn.tobebetterjavaer.com/paicoding/198d4c6806d7d21dc4f37bde4b809618.png)

在 Nacos Spring Cloud 中，数据集(Data Id) 的配置完整格式如下：

```
${spring.cloud.nacos.config.prefix}-${spring.profiles.active}.${spring.cloud.nacos.config.file-extension}
```

通俗一点，就是前缀-环境-扩展名

Group 就用默认的先（后面会说）

配置内容简单写上服务独有的配置：

```yaml
spring:
  redis:
    host: pmhub-redis
    port: 6379
    password:

复制代码
```

然后就大功告成啦：

![img](https://cdn.tobebetterjavaer.com/paicoding/f927990219e426674311b091a4cb47da.png)

### 如何实现配置的动态刷新？

在单体应用中，我们通常会在 Controller 里边用 @Value 取出配置信息。



![技术派使用@Value 取出配置信息](https://cdn.tobebetterjavaer.com/paicoding/9c460b16532be618d82a2b5a2df1a5ae.png)技术派使用@Value 取出配置信息



如果要改变某个具体的配置，就需要重新打包、部署，非常麻烦。当然了，也可以通过一些技术手段达到动态配置的目的，比如说使用定时任务从 MySQL 中取出配置再动态刷新到 Environment 中。技术派就是这么做的，算是一个轻量级的配置中心，参考：[✅技术派自定义配置注入&动态刷新](https://www.yuque.com/itwanger/az7yww/oobmcdkym1232f6k)

![img](https://cdn.tobebetterjavaer.com/paicoding/a2ae58d45adb42164eb00003a9960586.png)

那在 PmHub 中，如何让配置文件的值也动起来呢？Nacos 采用了 Spring Cloud 原生注解 @RefreshScope 来实现配置的自动更新。

使用方式很简单，直接在需要加载配置文件的类上一个注解 @RefreshScope。比如验证码配置类：

```java
/**
 * 验证码配置
 * 
 * @author canghe
 */
@Configuration
@RefreshScope
@ConfigurationProperties(prefix = "security.captcha")
public class CaptchaProperties
{
    /**
     * 验证码开关
     */
    private Boolean enabled;

    /**
     * 验证码类型（math 数组计算 char 字符）
     */
    private String type;

    public Boolean getEnabled()
    {
        return enabled;
    }

    public void setEnabled(Boolean enabled)
    {
        this.enabled = enabled;
    }

    public String getType()
    {
        return type;
    }

    public void setType(String type)
    {
        this.type = type;
    }
}

复制代码
```

注意看对应的代码位置。

![img](https://cdn.tobebetterjavaer.com/paicoding/966e0fcb03219788264597673f8d21ef.png)

### 如何实现配置的持久化？

为什么要持久化？

默认情况下 Nacos 配置是保存在内存中的，Nacos 挂了或者宕机了，我们辛辛苦苦配置的数据就丢失了。

做持久化的目的是为了将数据持久化到磁盘。

Nacos 持久化的方式还蛮多的，PmHub 主要是通过 MySQL 实现的。



![PmHub 将 Nacos 配置持久化到 MySQL](https://cdn.tobebetterjavaer.com/paicoding/6bde8b2db04d52f3ea2130700c9db057.png)PmHub 将 Nacos 配置持久化到 MySQL



使用方式也很简单，前面我们搭建 Nacos 本地环境的时候已经讲过了，参考：[✅PmHub 搭建 Nacos 本地环境](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wbnm3ysyixv80dsc)

有需要变更配置的话，就可以通过 Nacos 管理中心进行更新（本地为：http://localhost:8848/nacos/）。

![img](https://cdn.tobebetterjavaer.com/paicoding/1eb9a52f53e569c4a3814246d418d84f.png)

## Nacos 如何做多环境多项目管理

在公司开发项目时，通常会有多套环境，比如开发环境、测试环境、预发环境、线上环境，那如何保证服务在不同环境下读取到 Nacos 对应的配置呢？

你可能会说，不同环境一般会部署在不同平台，每个平台维护一个 Nacos 不就 OK 啦？



![画板](https://cdn.tobebetterjavaer.com/paicoding/d71cc0c68b6bb4462470d7dfcb82f535.jpeg)画板



如果这样搞，维护的成本巨高，像 PmHub 就有 8 个微服务，4 套环境可能就要维护 32 套 Nacos 了，这谁受得了。

实际上 Nacos 已经帮我们考虑的很周全了，Nacos 只需要部署一个，一个就可以应对多个环境。



![画板](https://cdn.tobebetterjavaer.com/paicoding/84286abefc95df7f83905cf00830b380.jpeg)画板



那在 Nacos 内部，怎么区分这么多环境呢？

通过三大隔离措施，分别是：Namespace、Group 和 Datald



### Namespace（命名空间）

命名空间是外层最大的隔离，是多环境隔离的首选方案。

**功能：**

- 提供配置和服务的隔离环境。
- 通常用于多租户场景、开发/测试/生产环境隔离，或者不同业务模块的隔离。

**特点：**

- 每个 Namespace 都是独立的配置和服务空间，彼此之间完全隔离。
- 一个配置或服务只能属于一个 Namespace。
- 默认存在一个 Namespace，ID 为 `public`，即默认命名空间。

**场景：**

- **多环境隔离**：将开发、测试、生产配置分别放到不同的 Namespace 中。
- **多租户管理**：为不同的用户或项目分配独立的配置空间。

默认有一个 public 命名空间：

![img](https://cdn.tobebetterjavaer.com/paicoding/498920325073802acd219f1fd6d35c80.png)

也可以新建命名空间：

![img](https://cdn.tobebetterjavaer.com/paicoding/9ec7afc7b05d0d472093f589a0b2e9a6.png)

比如生产环境，就可以新建一个 prod 的命名空间，测试环境新建一个 test 的命名空间，研发环境新建一个 dev 的命名空间。

比如我这里已经建好了三个环境的命名空间：

![img](https://cdn.tobebetterjavaer.com/paicoding/7cdf6c533c3e2941aedf81e5694644e0.png)

在 Nacos 的【配置管理-配置列表】菜单中，就会出现对应的命名空间。

![img](https://cdn.tobebetterjavaer.com/paicoding/fc4cd448ac9ebe3d01da3df0e0d6517a.png)

然后在每个微服务的 nacos 配置中，添加对应的命名空间：

![img](https://cdn.tobebetterjavaer.com/paicoding/3f4cede3d88b76898015504a58ebdc44.png)

### **Group（分组）**

功能：

- 用于对同一个 Namespace 内的配置进行逻辑分组管理。
- 配置属于同一个 Namespace 后，可以再通过 Group 进一步分类。

特点：

- 默认分组名称为 `DEFAULT_GROUP`。
- 一个配置可以同时指定 Namespace 和 Group。
- Group 可以帮助在 Namespace 内对配置文件按业务模块、功能划分进行更细致的管理。

场景：

- **按业务分组**：不同模块（如订单系统、库存系统）使用不同的 Group 名称。
- **细化管理**：在同一个 Namespace 中实现业务功能的进一步隔离和管理。

在新建配置的时候，默认有个 DEFAULT_GROUP。

![img](https://cdn.tobebetterjavaer.com/paicoding/e04eae18653f92dca99773f2dc699da2.png)

可以在输入框中输入自定义的分组。

![img](https://cdn.tobebetterjavaer.com/paicoding/cac7ac49429b132b5daeed4d9ffc71c6.png)

然后在前台就可以显示分组信息了，可以按照条件进行筛选。分组可以作为命名空间的细粒度操作。

![img](https://cdn.tobebetterjavaer.com/paicoding/28bb4b4faf0d88e5f327d313a33308c9.png)

### **DataId（配置文件标识）**

功能：

- 配置的唯一标识符，用来区分具体的配置文件。
- 一个配置文件可以看作是一条完整的配置信息（Key-Value），通过 DataId 可以获取。

特点：

- 每个配置都通过 `DataId` 进行唯一标识。
- 通常使用具有描述意义的名字，如 `app-config.yml` 或 `database.properties`。
- 同一个 DataId 可以在不同的 Namespace 和 Group 下共存。

场景：

- **配置管理**：用不同的 DataId 来存储应用的不同配置文件，如 `application.properties`、`logback.xml`。
- **服务动态调整**：动态修改或更新某个配置文件。

不同的服务用不同的 **DataId，**很好理解，比如 PmHub 中有 auth、project 服务，那 **DataId** 就可以如下图这样设置，当然规则也是可以自定义的。

![img](https://cdn.tobebetterjavaer.com/paicoding/ba896b593c667f2b3bdf0af0ca204dc8.png)

参考链接：https://learnku.com/articles/58731



# PmHub 整合 Gateway 实现微服务网关配置和限流，6000 字+20 张手绘图

原创

PmHub 整合 Gateway 实现微服务网关配置和限流，6000 字+20 张手绘图

球友好，这一节我们来更细粒度地聊一聊微服务网关 Gateway。

在面试系列中，我们已经讲过一些关于 Gateway 的基础知识，以及一些 Gateway 在 PmHub 中的实操。这一节， 我们将进行更深入地学习，来帮你打通任督二脉：

* **Gateway 工作流程机理**
* **网关如何做路由映射**
* **如何动态获取服务 URI**
* **自定义断言**
* **自定义过滤器**
* **PmHub 中的高级实践**

书读百遍不如跟着我实操一遍，涉及到代码的地方，希望你可以拿起高贵的笔记本和我一起敲击哦。

## 概述

> 这部分和面试系列稍微会有一些交叉，但会有一些意想不到的惊喜。

由于苍何最近在公司整的大数据及 K8s 应用，还发现了一种更高性能的网关，它的名字叫 APISIX，你可能没听过他，但工作中有可能用到哦，这里我们来看看他和 SpringCloud Gateway 有啥区别：

| **对比维度** | **Spring Cloud Gateway**                                     | **APISIX**                                               |
| ------------ | ------------------------------------------------------------ | -------------------------------------------------------- |
| **项目定位** | 基于 Spring Cloud 的微服务网关解决方案，专为 Java 生态设计。 | 一个高性能的开源 API 网关，面向多语言生态和高并发场景。  |
| **技术栈**   | 基于 Java 和 Spring Reactor。                                | 基于 Nginx 和 OpenResty，采用 Lua 语言扩展插件体系。     |
| **性能**     | 性能较高，但受限于 JVM 性能瓶颈。                            | 高性能，轻量级，基于 Nginx 的高并发优势。                |
| **生态支持** | 强大的 Spring 生态系统，集成 Spring Cloud 全家桶。           | 支持多语言客户端，广泛适配云原生生态，如 Kubernetes。    |
| **扩展性**   | 支持自定义 Filter 和 Predicate，但需掌握 Java 编程。         | 提供丰富的 Lua 插件，可动态加载，支持实时扩展。          |
| **动态性**   | 配置较为静态，需重启应用加载新配置。                         | 支持动态配置，无需重启，配置变更实时生效。               |
| **管理方式** | 依赖代码配置（通过 Java 配置类或 yml 文件）。                | 提供友好的 Dashboard 界面，支持 REST API 和 CLI 管理。   |
| **插件体系** | 插件功能有限，主要通过 Filter 实现。                         | 插件丰富，涵盖鉴权、限流、日志监控、数据转换等功能。     |
| **服务发现** | 原生支持 Spring Cloud 服务发现机制（Eureka、Consul 等）。    | 支持多种服务发现方式，包括 Nacos、Eureka、Consul 等。    |
| **协议支持** | HTTP 和 WebSocket。                                          | 支持 HTTP、HTTPS、gRPC、WebSocket、TCP 等多种协议。      |
| **社区支持** | 依赖 Spring 官方社区，更新周期较长。                         | Apache 基金会项目，社区活跃，更新频率较高。              |
| **适用场景** | 适用于 Java 微服务体系，特别是基于 Spring Cloud 的项目。     | 适用于多语言、多协议的高并发场景，如跨语言服务集成场景。 |
| **学习成本** | 对熟悉 Spring 生态的开发者成本较低。                         | 需要了解 Nginx 和 Lua，较高的学习曲线。                  |
| **性能瓶颈** | JVM 和线程模型可能成为高并发场景的瓶颈。                     | 更接近于原生 Nginx 性能，适合大规模高并发流量处理。      |
| **典型用户** | Java 开发团队，特别是 Spring Cloud 使用者。                  | 面向对性能和多语言支持要求较高的团队，如互联网公司。     |

由于我们的项目属于大数据平台，故不像 PmHub 这样单纯的美好，涉及到的开发语言也不只有 Java，还包括云原生和 k8s 等，所以 APISIX 更适合。但 APISIX 不是我们今天的主角，就不过多展示。

## 三大法宝

如果你有认真看面试系列的话，就应该清楚，说起 SpringCloud Gateway，就不得不提三大法宝，来，跟我一起回忆一遍吧。

### 法宝之一：路由

给你举个例子，我们在浏览器输入一串地址，就能跳转到对应的网站，这一串地址包含了域名，网站 URI 等信息。对于微服务系统而言，虽然只有一个页面，但不同的地方会有不同的 URL，比如说：

```bash
/a/**：跳转到 A 服务，

/b/**：跳转到 B 服务，

/c/**：跳转到 C 服务
复制代码
```

那在微服务系统中，就可以通过网关来实现，而这，用个牛逼点的名词来解释就是：**路由**。

啥是路由呢？

路由是由一组信息组合而成的，包含 ID、目标 URI、一组断言和一组过滤器，断言路由如果是真的，那请求的 URI 就是配置的路径，也就是请求了`/a/**`，就会跳转到路由配置的服务上来。

不大明白？哈哈，没关系，我们看看 PmHub 中是怎么做的。

```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          lowerCaseServiceId: true
          enabled: true
      routes:
        # 认证中心
        - id: pmhub-auth
          uri: lb://pmhub-auth
          predicates:
            - Path=/auth/**
          filters:
            # 验证码处理
            - CacheRequestFilter
           # - ValidateCodeFilter
            - StripPrefix=1
        # 代码生成
        - id: pmhub-gen
          uri: lb://pmhub-gen
          predicates:
            - Path=/gen/**
          filters:
            - StripPrefix=0

复制代码
```

比如你访问 `/auth/**`，那根据配置，predicates 断言为真，会跳转到 uri 对应的服务 id，也就是会跳转到 pmhub-auth 这个微服务。

是不是一下子就理解啦？

在路由配置中，有一个 predicates 配置，这个有人说是路由规则，其实就是我们下面要说的法宝二：断言。

### 法宝之二：断言

断言可以理解为**匹配规则**，比如在 PmHub 中配置的「 `- Path=/auth/**`」，就代表所有符合这个路径规则的请求都会被转发到对应的服务上。参考面试系列：[✅PmHub Gateway全局过滤器统计接口调用耗时（👍必看）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wxk1lvm5ffaen0dg)

### 法宝之三：过滤

在路由配置中，你会看到有 filters 这个配置，这个其实就是过滤器的配置。

网关中的过滤器，有点类似 SpringMVC 里面的拦截器 Interceptor，以及 Servlet 过滤器，其中「pre」 和「post」分别会在请求被执行栈调用前和被执行后调用，用来修改请求和响应信息。

参考面试系列：[✅PmHub Gateway全局过滤器统计接口调用耗时（👍必看）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wxk1lvm5ffaen0dg)

## SpringCloud Gateway 工作流

知其然，而后知其所以然，方可修炼成佛，哈哈，了解工作流后，你就可以和面试官吹逼。

我们先来祭出一张官网截图：

![](https://cdn.tobebetterjavaer.com/paicoding/7efbb8ae0e16e6dca0f95b2e40d1556d.png)

这是官网截图附带描述：

![](https://cdn.tobebetterjavaer.com/paicoding/143558be6f7d48989fed42b925fc39eb.png)

我让 ChatGPT 翻译一下：

> 客户端向 Spring Cloud Gateway 发出请求。如果 Gateway Handler Mapping 确定某个请求匹配一个路由 (Route)，则该请求会被发送到 Gateway Web Handler。此处理器通过特定于该请求的过滤器链来运行请求。过滤器被分为虚线前后两部分的原因是，过滤器可以在代理请求发送之前或之后执行逻辑。所有 "pre" 过滤器逻辑会先被执行，然后代理请求会被发送。代理请求完成后，会执行 "post" 过滤器逻辑。

苍何用人话来描述一下这个过程：

首先啊，客户端向 Spring Cloud Gateway 发出请求。然后在 Gateway Handler Mapping 中找到与请求相匹配的路由，将其发送到 Gateway Web Handler。Handler 再通过指定的过滤器链来将请求发送到我们实际的服务执行业务逻辑，然后返回。

过滤器之间用虚线分开是因为过滤器可能会在发送代理请求之前(Pre)或之后(Post)执行业务逻辑。

在“pre”类型的过滤器可以做参数校验、权限校验、流量监控、日志输出、协议转换等;

在“post”类型的过滤器中可以做响应内容、响应头的修改，日志的输出，流量监控等有着非常重要的作用。

其实你会发现，核心逻辑就是：路由转发+断言判断+执行过滤器链

## PmHub 中集成 SpringCloud Gateway

在 PmHub 中，将 SpringCloud Gateway 作为一个单独的微服务提供了，这也是解耦的关键，通常，我们的网关服务会单独部署，而且由于网关作为核心组件，会集群部署，至少 2 个节点吧。

那么但凡是单独的微服务，那就离不开五部曲：

* 1、建 module
* 2、改 pom
* 3、写 YML
* 4、修改主启动类
* 5、编写业务类

首先新建一个模块 module，pmhub-gateway：

![](https://cdn.tobebetterjavaer.com/paicoding/e27e2b2d40879569d0c50a92cba6704b.png)

然后再 pom 中引入依赖：

```xml
<!-- SpringCloud Gateway -->
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>

复制代码
```

然后写 YML：

```yaml
# Tomcat
server:
  port: 6880

# Spring
spring: 
  application:
    # 应用名称
    name: pmhub-gateway
  profiles:
    # 环境配置
    active: dev
  cloud:
    nacos:
      discovery:
        # 服务注册地址
        server-addr: 127.0.0.1:8848
        username: nacos
        password: nacos
      config:
        # 配置中心地址
        server-addr: 127.0.0.1:8848
        username: nacos
        password: nacos
        # 配置文件格式
        file-extension: yml
        # 共享配置
        shared-configs:
          - application-${spring.profiles.active}.${spring.cloud.nacos.config.file-extension}
    sentinel:
      # 取消控制台懒加载
      eager: true
      transport:
        # 配置控制台服务地址
        dashboard: 127.0.0.1:8080
        # 默认 8719 端口，假如被占用会自动从 8719 开始依次 +1 扫描,直至找到未被占用的端口
        port: 8719
      # nacos配置持久化
      datasource:
        ds1:
          nacos:
            server-addr: 127.0.0.1:8848
            dataId: sentinel-pmhub-gateway
            groupId: DEFAULT_GROUP
            data-type: json
            rule-type: gw-flow

# 实时log配置，可在http://localhost:6888/ 监控中心查看实时日志
logging:
  file:
    name: logs/${spring.application.name}/info.log

复制代码
```

还需要在 nacos 中进行**路由配置**：

![](https://cdn.tobebetterjavaer.com/paicoding/e5edf1a10cf4b23e6e84cf6bdcbc11a4.png)

```yaml
spring:
  redis:
    host: pmhub-redis
    port: 6379
    password:
  cloud:
    gateway:
      discovery:
        locator:
          lowerCaseServiceId: true
          enabled: true
      routes:
        # 认证中心
        - id: pmhub-auth
          uri: lb://pmhub-auth
          predicates:
            - Path=/auth/**
          filters:
            # 验证码处理
            - CacheRequestFilter
           # - ValidateCodeFilter
            - StripPrefix=1
        # 代码生成
        - id: pmhub-gen
          uri: lb://pmhub-gen
          predicates:
            - Path=/gen/**
          filters:
            - StripPrefix=0
        # 定时任务
        - id: pmhub-job
          uri: lb://pmhub-job
          predicates:
            - Path=/schedule/**
          filters:
            - StripPrefix=0
        # 系统模块
        - id: pmhub-system
          uri: lb://pmhub-system
          predicates:
            - Path=/system/**
          filters:
            - StripPrefix=0
        # 项目模块
        - id: pmhub-project
          uri: lb://pmhub-project
          predicates:
            - Path=/project/**
          filters:
            - StripPrefix=0
        # 流程模块
        - id: pmhub-workflow
          uri: lb://pmhub-workflow
          predicates:
            - Path=/workflow/**
          filters:
            - StripPrefix=0





复制代码
```

最后添加过滤器逻辑，核心就 AuthFilter 和 BlackListUrlFilter（黑名单过滤器）

其中 AuthFilter 和网关鉴权相关，具体代码和逻辑如下，大家对着代码看，更有感觉哦。

```java
@Component
public class AuthFilter implements GlobalFilter, Ordered {
    private static final Logger log = LoggerFactory.getLogger(AuthFilter.class);

    private static final String BEGIN_VISIT_TIME = "begin_visit_time";//开始访问时间

    // 排除过滤的 uri 地址，nacos自行添加
    @Autowired
    private IgnoreWhiteProperties ignoreWhite;

    @Autowired
    private RedisService redisService;


    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        ServerHttpRequest request = exchange.getRequest();
        ServerHttpRequest.Builder mutate = request.mutate();

        String url = request.getURI().getPath();
        // 跳过不需要验证的路径
        if (StringUtils.matches(url, ignoreWhite.getWhites())) {
            return chain.filter(exchange);
        }
        String token = getToken(request);
        if (StringUtils.isEmpty(token)) {
            return unauthorizedResponse(exchange, "令牌不能为空");
        }
        Claims claims = JwtUtils.parseToken(token);
        if (claims == null) {
            return unauthorizedResponse(exchange, "令牌已过期或验证不正确！");
        }
        String userkey = JwtUtils.getUserKey(claims);
        boolean islogin = redisService.hasKey(getTokenKey(userkey));
        if (!islogin) {
            return unauthorizedResponse(exchange, "登录状态已过期");
        }
        String userid = JwtUtils.getUserId(claims);
        String username = JwtUtils.getUserName(claims);
        if (StringUtils.isEmpty(userid) || StringUtils.isEmpty(username)) {
            return unauthorizedResponse(exchange, "令牌验证失败");
        }

        // 设置用户信息到请求
        addHeader(mutate, SecurityConstants.USER_KEY, userkey);
        addHeader(mutate, SecurityConstants.DETAILS_USER_ID, userid);
        addHeader(mutate, SecurityConstants.DETAILS_USERNAME, username);
        // 内部请求来源参数清除（防止网关携带内部请求标识，造成系统安全风险）
        removeHeader(mutate, SecurityConstants.FROM_SOURCE);

        //先记录下访问接口的开始时间
        exchange.getAttributes().put(BEGIN_VISIT_TIME, System.currentTimeMillis());

        return chain.filter(exchange.mutate().request(mutate.build()).build());
    }

    private void addHeader(ServerHttpRequest.Builder mutate, String name, Object value) {
        if (value == null) {
            return;
        }
        String valueStr = value.toString();
        String valueEncode = ServletUtils.urlEncode(valueStr);
        mutate.header(name, valueEncode);
    }

    private void removeHeader(ServerHttpRequest.Builder mutate, String name) {
        mutate.headers(httpHeaders -> httpHeaders.remove(name)).build();
    }

    private Mono<Void> unauthorizedResponse(ServerWebExchange exchange, String msg) {
        log.error("[鉴权异常处理]请求路径:{}", exchange.getRequest().getPath());
        return ServletUtils.webFluxResponseWriter(exchange.getResponse(), msg, HttpStatus.UNAUTHORIZED);
    }

    /**
     * 获取缓存key
     */
    private String getTokenKey(String token) {
        return CacheConstants.LOGIN_TOKEN_KEY + token;
    }

    /**
     * 获取请求token
     */
    private String getToken(ServerHttpRequest request) {
        String token = request.getHeaders().getFirst(TokenConstants.AUTHENTICATION);
        // 如果前端设置了令牌前缀，则裁剪掉前缀
        if (StringUtils.isNotEmpty(token) && token.startsWith(TokenConstants.PREFIX)) {
            token = token.replaceFirst(TokenConstants.PREFIX, StringUtils.EMPTY);
        }
        return token;
    }

    @Override
    public int getOrder() {
        return -200;
    }


}
复制代码
```

## 动态获取服务 URI

实际工作中，还有一种场景是，作为微服务，可能其对应的端口会改变，这个时候如果配置的路由是根据 http 写死的，那就完了，还得去大动干戈的调整网关的路由配置，特别麻烦。

很玄乎，是吧？

其实很简单，为了能动态的获取到服务的 URI，需要在路由配置的时候，按照注册中心的形式进行配置，如下：

```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          lowerCaseServiceId: true
          enabled: true
      routes:
        # 认证中心
        - id: pmhub-auth
          uri: lb://pmhub-auth
          predicates:
            - Path=/auth/**
          filters:
            # 验证码处理
            - CacheRequestFilter
           # - ValidateCodeFilter
            - StripPrefix=1

复制代码
```

## 自定义断言

上文中有提到常用的断言，基本上能满足绝大部分的需求，但聪明的你可能会问：那如果预制的断言不够用咋办？

好家伙，你可太聪明了，不过 SpringCloud Gateway 肯定也想到了，所以，他支持自定义断言。

先来看一波 AfterRoutePredicateFactory 源码：

![](https://cdn.tobebetterjavaer.com/paicoding/d2c9e4839841dede2770f2ba51acff35.png)

梳理一波源码架构：

![](https://cdn.tobebetterjavaer.com/paicoding/b9608cfe6cfe73b83d1ce9ce3efb7ab4.png)

不难看出，要想实现自定义断言：

* 要么继承 AbstractRoutePredicateFactory 抽象类
* 要么实现 lRoutePredicateFactory 接口
* 类可以取任意名，但是必须以 RoutePredicateFactory 后缀结尾

下面给一些具体的实操例子，大家可以动手试一试哦。

```java
@Component
public class MyCustomPredicateFactory extends AbstractRoutePredicateFactory<MyCustomPredicateFactory.Config> {

    public MyCustomPredicateFactory() {
        super(Config.class);
    }

    @Override
    public Predicate<ServerWebExchange> apply(Config config) {
        return exchange -> {
            // 在这里实现自定义逻辑
            String headerValue = exchange.getRequest().getHeaders().getFirst(config.getHeaderName());
            return headerValue != null && headerValue.equalsIgnoreCase(config.getExpectedValue());
        };
    }

    public static class Config {
        private String headerName;
        private String expectedValue;

        public String getHeaderName() {
            return headerName;
        }

        public void setHeaderName(String headerName) {
            this.headerName = headerName;
        }

        public String getExpectedValue() {
            return expectedValue;
        }

        public void setExpectedValue(String expectedValue) {
            this.expectedValue = expectedValue;
        }
    }
}

复制代码
```

```java
@Component
public class HeaderRoutePredicateFactory implements RoutePredicateFactory<HeaderRoutePredicateFactory.Config> {

    @Override
    public Class<Config> getConfigClass() {
        return Config.class;
    }

    @Override
    public Predicate<ServerWebExchange> apply(Config config) {
        return exchange -> {
            // 自定义断言逻辑：检查请求头是否匹配预期值
            String headerValue = exchange.getRequest().getHeaders().getFirst(config.getHeaderName());
            return headerValue != null && headerValue.equalsIgnoreCase(config.getExpectedValue());
        };
    }

    @Override
    public void init(Config config) {
        // 可以在此进行配置类的初始化操作
    }

    @Override
    public Map<String, Object> shortcutFieldOrder() {
        return Map.of("headerName", config.getHeaderName(), "expectedValue", config.getExpectedValue());
    }

    public static class Config {
        private String headerName;
        private String expectedValue;

        public String getHeaderName() {
            return headerName;
        }

        public void setHeaderName(String headerName) {
            this.headerName = headerName;
        }

        public String getExpectedValue() {
            return expectedValue;
        }

        public void setExpectedValue(String expectedValue) {
            this.expectedValue = expectedValue;
        }
    }
}

复制代码
```

然后在路由配置中，指定我们自定义的断言就好啦。

## 自定义过滤器

这部分其实在面试系列有一些说明，这里再描述下：

经典面试题：**如何统计接口的调用耗时情况，说说你的设计思路？**

参考：[✅PmHub Gateway全局过滤器统计接口调用耗时（👍必看）](https://www.yuque.com/canghe-u0ocv/laigeoffer-pmhub/wxk1lvm5ffaen0dg)

当然了，面试系列中讲的是全局过滤器，也就是全局通用，那如何自定义单一内置过滤器呢？

在 **Spring Cloud Gateway** 中，自定义单一的内置过滤器就像给蛋糕加上自己的创意配方：有规则，但你可以自由发挥！

过滤器是网关中的“守门员”，可以在请求进入目标服务之前（`pre`）或响应返回客户端之后（`post`）干点“小动作”。比如：

* 添加请求头（“你得戴口罩才能进来”）。
* 修改响应内容（“你得加点糖才能走”）。
* 日志记录（“我记下你啥时候来的”）。

假设我们想实现一个过滤器，往请求里偷偷加个头信息，告诉目标服务：“这个请求是 VIP 客户发的哦！”

### 第一步：实现一个过滤器类

创建一个类，继承 `AbstractGatewayFilterFactory`。以下是代码示例：

```java
import org.springframework.cloud.gateway.filter.GatewayFilter;
import org.springframework.cloud.gateway.filter.factory.AbstractGatewayFilterFactory;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.stereotype.Component;

@Component
public class AddVipHeaderFilter extends AbstractGatewayFilterFactory<AddVipHeaderFilter.Config> {

    public AddVipHeaderFilter() {
        super(Config.class); // 指定配置类
    }

    @Override
    public GatewayFilter apply(Config config) {
        // 返回过滤器逻辑
        return (exchange, chain) -> {
            // 在这里修改请求
            ServerHttpRequest request = exchange.getRequest()
                .mutate()
                .header("X-VIP-Customer", config.getVipLevel()) // 添加一个头信息
                .build();

            // 打印日志，幽默一下
            System.out.println("👑 哇哦！这个请求被标记为 VIP：" + config.getVipLevel());

            // 将修改后的请求继续传递下去
            return chain.filter(exchange.mutate().request(request).build());
        };
    }

    // 配置类，用于传递自定义参数
    public static class Config {
        private String vipLevel = "Gold"; // 默认是金牌VIP

        public String getVipLevel() {
            return vipLevel;
        }

        public void setVipLevel(String vipLevel) {
            this.vipLevel = vipLevel;
        }
    }
}
复制代码
```

### 第二步：在配置文件中启用过滤器

我们需要在 `application.yml` 中为路由指定这个过滤器，并传递参数。

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: vip_route
          uri: http://example.com # 目标服务地址
          filters:
            - name: AddVipHeaderFilter # 指定我们自定义的过滤器
              args:
                vipLevel: Platinum # 给过滤器传递参数，设置 VIP 等级
          predicates:
            - Path=/vip/** # 路由规则

复制代码
```

启动网关服务，然后访问类似 `/vip/123` 的 URL，请求会被加上一个 `X-VIP-Customer` 的头，值为 `Platinum`。目标服务收到请求时，会知道这是一位**白金 VIP 客户**。

想象网关是个“电梯小哥”，请求就是乘客：

* 小哥看乘客没戴 VIP 徽章（没头信息），直接帮他贴上“我是 VIP”。
* 乘客下电梯后（发送到目标服务），告诉服务端：“放心，这位乘客身份 VIP 认证过了！”
* 如果设置 `vipLevel` 为 `Gold` 或 `Platinum`，小哥会感慨：“哇哦，这可是稀客！”

总结下自定义单一内置过滤器：

* **继承** `AbstractGatewayFilterFactory` 实现自定义逻辑。
* **配置类** 用于传递参数，比如设置 VIP 等级。
* **在 YAML 配置中绑定过滤器**，用 `filters` 指定过滤器名称。
* **运行时日志调试**，幽默输出让日志不再单调。

## PmHub 中 SpringCloud Gateway 和 Sentinel 的整合

Sentinel 支持对 Spring Cloud Gateway、Zuul 等主流的 API Gateway 进行限流。

![Sentinel集成网关架构图（官网）](https://cdn.tobebetterjavaer.com/paicoding/3c597ede2ba0a4cff142128c84178fa9.png)

Sentinel集成网关架构图（官网）

从 1.6.0 版本开始，Sentinel 就提供了 Spring Cloud Gateway 的适配模块，可以提供两种资源维度的限流：

* route 维度：即在 Spring 配置文件中配置路由的条目，资源名为对应的 routeId
* 自定义 API 维度：用户可以利用 Sentinel 提供的 API 来自定义一些 API 分组

我们从 route 维度来讲一下具体的步骤。

### 引入依赖

```xml
<!-- SpringCloud Alibaba Sentinel 核心依赖-->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>

<!-- SpringCloud Alibaba Sentinel Gateway，如果不是gateway可以不用引入 -->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-alibaba-sentinel-gateway</artifactId>
</dependency>

<!-- Sentinel Datasource Nacos 用来做持久化存储-->
<dependency>
  <groupId>com.alibaba.csp</groupId>
  <artifactId>sentinel-datasource-nacos</artifactId>
</dependency>

复制代码
```

### 修改 yml

```yaml
spring: 
 cloud: 
   sentinel:
      # 取消控制台懒加载
      eager: true
      transport:
        # 配置控制台服务地址
        dashboard: 127.0.0.1:8080
        # 默认 8719 端口，假如被占用会自动从 8719 开始依次 +1 扫描,直至找到未被占用的端口
        port: 8719
      # nacos配置持久化
      datasource:
        ds1:
          nacos:
            server-addr: 127.0.0.1:8848
            dataId: sentinel-pmhub-gateway
            groupId: DEFAULT_GROUP
            data-type: json
            rule-type: gw-flow

复制代码
```

### nacos 持久化配置

Sentinel 的配置默认是放在内存中，如果服务一旦重启，原先配置好的规则就都不见了，为了避免这种情况发生，我们需要数据持久化，在 PmHub 中，nacos 的数据都会最终持久化到 MySQL 数据库。

所以我们只需要将 Sentinel 的配置放到 nacos 配置统一管理起来就好了。

通过 Nacos 的配置管理中心，可以找到 sentinel-pmhub-gateway。

![Sentinel的配置](https://cdn.tobebetterjavaer.com/paicoding/ad7dc0a8406ff422b91f15abeabc857b.png)

Sentinel的配置

这里主要是流控规则的配置，主要做限流控制。

### 查看 Sentinel 控制台

启动 gateway 服务，打开控制台。

![Sentinel 控制台](https://cdn.tobebetterjavaer.com/paicoding/00f1920907c1eea7fb7950c0533dea45.png)

Sentinel 控制台

### 流控规则介绍

Sentinel能够对流量进行控制，主要是监**控应用的 QPS 流量或者并发线程数**等指标，如果达到指定的阈值时，就会被流量进行控制，以避免服务被瞬时的高并发流量击垮，保证服务的高可靠性。这里以 pmhub-gateway 网关流控规则为例，参数见最下方：

![网关流控规则](https://cdn.tobebetterjavaer.com/paicoding/fb3be26345f4bab55df0f2bc3ecc1bd2.png)

网关流控规则

| **参数名称** | **参数值示例**      | **解释**                                                     |
| ------------ | ------------------- | ------------------------------------------------------------ |
| API 类型     | Route ID / API 分组 | 指定限流规则应用的API类型，可以是路由ID或API分组。           |
| API 名称     | pmhub-system        | 被限流的具体API的名称。                                      |
| 针对请求属性 | 复选框              | 是否根据请求属性（如IP地址、用户身份等）进行限流。           |
| 阈值类型     | QPS / 线程数        | 限流的依据类型，可以是每秒查询数（QPS）或并发线程数。        |
| QPS 阈值     | 1000                | 指定每秒允许通过的最大请求数，当超过此值时，将触发限流。     |
| 间隔         | 1                   | 配合QPS阈值使用，指定限流的时间窗口大小，如1秒、1分钟等。    |
| 流控方式     | 快速失败 / 匀速排队 | 当达到限流阈值时，采取的策略。快速失败表示直接拒绝请求，匀速排队表示排队等待处理。 |
| Burst size   | 0                   | 突发请求数，表示允许瞬间通过的请求数，0表示不允许突发流量。  |

如果阈值类型选择的是 QPS，则表示调用接口的QPS达到阈值时，会进行限流操作。如果阈值类型选择的是线程数，则表示当调用接口的并发线程数达到阈值时，进行限流操作。

pmhub-system 配置的是 QPS 1000，代表每秒最多可以处理 1000 个请求。

## 总结

你可以结合 Gateway 的面试篇，以及 PmHub 的源码，综合一起来看，基本上就能完全掌握 Gateway 了。

其实最重要的就是理解 Gateway 是用来干嘛的，他能够做过滤器、限流，是微服务架构中的一个重要的前置组件。

理解了这个，再结合实操和场景，就能够轻松应对面试中 Gateway 的相关内容了。

最后，希望球友能拿到一个好的面试结果，或者在 Gateway 上有一个清晰的认知，工作中用得上用得好。

# OpenAI如何用来辅助编程？PmHub 付费教程的 AI 付费篇

作为一名程序员，我们经常面临着需要编写大量代码的挑战，有时候我们需要学习新的编程概念，或者解决一些特定的 bug，在没有 OpenAI 之前，我们往往是通过 Google 搜索引擎来完成这项工作，有了 OpenAI 之后，很多棘手的问题，或者超出我们以前的编程能力之外的问题，就可以直接丢给 OpenAI 来辅助我们完成。

或者可以换句话说，如果你在提问编程问题之前，没有问一手 OpenAI，那我觉得你对自己是极不负责的。

OpenAI 不仅可以为我们提供编程示例，解释源码，还可以为 bug 提供解决方案。

我自己的 OpenAI 是每天都在用的，大大小小的编程问题，基本上都能找到想要的答案。

![](https://cdn.tobebetterjavaer.com/paicoding/c86d3ebb1ef058adf42cee8d2bb91e60.png)

这里我解释一下为什么我会选择 OpenAI 而不是 ChatGPT 来讲这篇内容，是因为我觉得 ChatGPT 已经进化得足够强大了，甚至已经超出了 ChatGPT 的定义。

ChatGPT，全称是聊天生成预训练转换器（Chat Generative Pre-trained Transformer），是 OpenAI 在 2022 年 11 月发布的大语言模型，它以人机自然语言对话的方式进行交互，可以说以一己之力彻底改变了 AI 的发展轨迹。

我个人对提示词还不是特别擅长，但我觉得即便如此，OpenAI 也足够强大了。

你比如说我在配置技术派的 SSL 证书时，遇到了一个问题，我就可以直接扔给 OpenAI。

![](https://cdn.tobebetterjavaer.com/paicoding/39f7753871f93d9324295ee3c55a80e6.png)

它不仅能对错误的原因进行详细的分析，还能够提供解决方法，我接下来要做的，就是依据它提供的解决方案去尝试和验证，确保它提供的方案时可行的。

我这里也总结了一些使用心得，顺带分享给大家。

**1、问题的描述一定要尽可能的详细**，尽量给 OpenAI 足够多的上下文信息，比如说你遇到 bug 的堆栈信息，可以把重要的信息全部复制过来扔给 OpenAI，不要嫌多。

![](https://cdn.tobebetterjavaer.com/paicoding/febb7a59078e5a17d09857972f433da1.png)

**2、限定语言和平台**，比如说大多数球友都是 Java 程序员，那么你在向 OpenAI 提问的时候，尤其是对话的第一次，一定要告诉他这一点信息。不然他可能会往 Python 方向去找问题。

**3、添加关键信息**，直接告诉他你想要的结果，或者一些证据，比如说在技术派安装 Redis 的 shell 命令中，我想让 OpenAI 帮我增加一下 Redis 运行状态的输出记录，就可以把原有的 shell 内容扔给 OpenAI。

![](https://cdn.tobebetterjavaer.com/paicoding/a043ade1d53b673b27f05b473d498067.png)

**4、在生成代码的时候，尽量不要求一次性生成完整，而是要分批分次**；生成完成后一定要加以验证，虽然 OpenAI 的代码能力真的非常强大，但毕竟是生成式 AI，还是有可能出错的，所以一定要验证，告诉它哪里有问题。

比如说，我们想学习一下 lua 脚本，那第一步，可以先让 OpenAI 帮我们大致介绍一下。

![](https://cdn.tobebetterjavaer.com/paicoding/ee7f9de39444e65d294054b2b19856ee.png)

然后让 OpenAI 帮我们写一段 lua 程序。

![](https://cdn.tobebetterjavaer.com/paicoding/f4a6e6e27250b6cdfe690d2489e6cc6c.png)

然后再限定一下我的编程环境，比如说是不是 macOS。

![](https://cdn.tobebetterjavaer.com/paicoding/08a71e94340d6fa003201ffc59c7091d.png)

明白了 lua 脚本的基本用法，我们就可以增加难度了，比如说在 PmHub 项目中，我们打算用 lua 脚本+Redis 来实现一个基于计数器算法的限流，那就可以让 OpenAI 给我们提供一个简单的示例。

![](https://cdn.tobebetterjavaer.com/paicoding/5585ebc81bf2758636fb9750f8911872.png)

然后我们可以继续限定编程环境，比如说是用 Java 来实现，并且要在 RedisConfig 中注入Redis 的限流，那 OpenAI 就可以继续帮我们生成对应的代码。

![](https://cdn.tobebetterjavaer.com/paicoding/c9c1f496aac097c124e643e16acf5b16.png)

所以说，如果能够正确利用 OpenAI，代码的编写效率就会提升一大截，当然了，别忘记验证。

**5、在定位代码问题的时候，OpenAI 更是杀手锏**，以前我们在搜索引擎时代，我们只能扔给搜索引擎一个很简单的问题，没办法给太多信息，因为搜索引擎不支持，但有了 OpenAI 后，我们可以把整个堆栈信息都扔给它，当然了，也不要太多啦。

比如说，第一次我导入 PmHub 的配置文件时，出现了乱码问题，直接扔给 OpenAI。

![](https://cdn.tobebetterjavaer.com/paicoding/78987077d354819f07771819274fcf6f.png)

比如说安装 Nacos 的时候，出现了 user not found 的错误，扔给 OpenAI。

![](https://cdn.tobebetterjavaer.com/paicoding/79868d7e69f73a8bad292acc631e95fd.png)

他能一步步提供思路给我，比如说先检查 Nacos 用户的权限。

![](https://cdn.tobebetterjavaer.com/paicoding/53b5d8eac83650178c788df04dd18abf.png)

如果 OpenAI 最终提供的思路无能为力的话，请不要慌乱，因为 PmHub 的教程中，已经帮大家想到了。比如说，如果你是 Windows 用户，就可以看筱筱的 PmHub 学习笔记，他已经遇到过 user not found 的错误，并且提供了解决方案。

![](https://cdn.tobebetterjavaer.com/paicoding/4d3bf974e9cee1a95d2625368bf0688b.png)

其实很多时候，你出现的问题，很多人之前已经碰到了，请一定保持耐心，多看看教程。

**6、在阅读理解源码方面，OpenAI 基本上处于无敌的存在**。在没有 OpenAI 之前，阅读别人的源码，尤其是一些没有注释的源码，简直就是遭罪，哪怕是代码写的再优雅，对初学者都是一种折磨，但现在完全不同了。

有任何不懂不清楚的源码，都可以扔给 OpenAI，他能读得非常明白。

比如说你阅读 Gateway 全局拦截器的时候，对 `Mono.fromRunnable(()`不明所以，那就可以问 OpenAI，他能给你解释得非常清楚。

![](https://cdn.tobebetterjavaer.com/paicoding/9324504ccf83719c82fe253f731e4baa.png)

来看一下 OpenAI 是怎么说的：

![](https://cdn.tobebetterjavaer.com/paicoding/57c222ad6b78640301b3631b55681fb7.png)

甚至还会给出一些建设性的意见，比如说追加更多上下文信息，比如说使用 slf4j 的键值对日志。

![](https://cdn.tobebetterjavaer.com/paicoding/408a25e86cfb8ac068dfc461388fb876.png)

最后，我想说得是，虽然 OpenAI 非常的强大，但我们必须合理使用他，避免滥用和过度依赖。我们要理解，模型是有一定局限性的，不管是 OpenAI 还是国内的大模型，都是基于训练数据生成的模型，他生成的代码和建议只能作为参考，而不是标准答案。

我们应该意识到，自己才是主人，我们要具备创造性的思维、专业知识，以及经验，要能够在复杂问题上做出更全面和创新的决策，OpenAI 只是工具，并不能替代我们程序员本身。

# 学习笔记

## Nacos部署

Nacos部署参考同目录下的笔记，上边的方法不咋地

## RocketMq部署

使用docker-compose进行部署

新建相应目录rocketmq，然后再里边新建broker，放入broker.conf

```
brokerClusterName = DefaultCluster
brokerName = broker
brokerId = 0
deleteWhen = 04
fileReservedTime = 48
brokerRole = ASYNC_MASTER
flushDiskType = ASYNC_FLUSH
# 你的本机ip, 注意不要写localhost,127.0.0.1等，因为这是放到docker容器中的，我们需要指向mac本机
brokerIP1 = 192.168.200.47
# 禁用 tsl
tlsTestModeEnable = false
```

然后在rocketmq下新建data,用来存放持久化数据，防止容器重启数据丢失

新建docker-compose文件夹然后存放docker-compose.yml文件,

**文件挂载地址改成自己的**

volumes:

   \- D:/dockerDir/recketmq/broker/broker.conf:/home/rocketmq/rocketmq-5.1.0/conf/broker.conf

   \- D:/dockerDir/recketmq/data:/home/rocketmq/store

```yml
version: '3.8'
services:
  namesrv:
    image: apache/rocketmq:5.1.0
    container_name: rocketmq-pmnamesrv
    command: sh mqnamesrv
    networks:
      - rocketmq
    ports:
      - "9876:9876"

  broker:
    image: apache/rocketmq:5.1.0
    container_name: rocketmq-pmbroker
    command: sh mqbroker -n namesrv:9876 -c /home/rocketmq/rocketmq-5.1.0/conf/broker.conf
    ports:
      - "10911:10911"
      - "10909:10909"
      - "10912:10912"
    depends_on:
      - namesrv
    networks:
      - rocketmq
    volumes:
      - D:/rocketmq/broker/broker.conf:/home/rocketmq/rocketmq-5.1.0/conf/broker.conf
      - D:/rocketmq/data:/home/rocketmq/store

  proxy:
    image: apache/rocketmq:5.1.0
    container_name: rocketmq-pmproxy
    networks:
      - rocketmq
    depends_on:
      - broker
      - namesrv
    ports:
      - 8080:8080
      - 8081:8081
    restart: on-failure
    environment:
      - NAMESRV_ADDR=rocketmq-pmnamesrv:9876
    command: sh mqproxy


  dashboard:
    image: apacherocketmq/rocketmq-dashboard:latest
    container_name: rocketmq-dashboard
    environment:
      - JAVA_OPTS=-Drocketmq.namesrv.addr=rocketmq-pmnamesrv:9876
    ports:
      - "8082:8080"
    networks:
      - rocketmq
    depends_on:
      - namesrv
      - broker
      - proxy

networks:
  rocketmq:
    driver: bridge
```

最终目录结构如下

![image-20260331161008366](image-20260331161008366.png)

然后再docker-compose目录下执行cmd，然后再cmd中执行命令 docker-compose up -d

**docker-compose相关命令**

```
# 一键启动
docker-compose up -d

# 一键停止所有容器
docker-compose stop

# 一键删除所有容器
docker-compose rm

# 一键查看所有启动的容器
docker-compose ps
```

**然后再nacos中的application.yml**中添加如下配置

```
# 企微消息相关
  workWx:
    host: https://laigeoffer.cn:7880
    corpid: ww212312313
    corpsecret: DIPuyCcN7C1231231
    addressSecret: eFTxBtSvzUyBO1JCNTT1jfzzRq1OG123123
    agentid: 1000008
    aeskey: txwiJmdUJlC8T5c8oaXm4G3OiM12312
    path:

 # rocketMQ 配置
  rocketMQ:
   # 配置nameserver代理地址
    addr: 127.0.0.1:8081
    topic:
     # 企微消息topic
      wxMessage: pmhub_local
    # 消费者组  
    group:
      wxMessage: PMHUB_GROUP
```

## sentinel部署

文章中指定sentinel是1.8.7版本这是使用docker部署这个版本，拉取命令

```
//拉取镜像
docker pull bladex/sentinel-dashboard:1.8.7
//启动命令
docker run --name sentinel --network docker-net -d -p 8858:8858 -d bladex/sentinel-dashboard
```

sentinel持久化到nacos只需直接配置即可，

##  RocketMQ部署（不使用docker-compose）

在 Windows 环境下（路径为 `D:\dockerDir\rocketMQ`），部署 RocketMQ 需要注意**路径分隔符**和**配置文件**的处理。

以下是针对 Windows 系统的完整部署步骤：

### **📂 第一步：准备目录和配置文件**

在部署之前，必须先在 Windows 本地创建好目录和配置文件，否则容器可能无法启动或无法持久化数据。

1. **创建文件夹结构**
   请在 `D` 盘创建以下文件夹（用于存储日志和数据）：

   - `D:\dockerDir\rocketMQ\namesrv\logs`
   - `D:\dockerDir\rocketMQ\namesrv\store`
   - `D:\dockerDir\rocketMQ\broker\logs`
   - `D:\dockerDir\rocketMQ\broker\store`
   - `D:\dockerDir\rocketMQ\broker\conf`

2. **创建配置文件**
   在 `D:\dockerDir\rocketMQ\broker\conf` 目录下，新建一个文本文件，命名为 `broker.conf`。
   **重要**：请用记事本打开它，将 `brokerIP1` 修改为你**本机的局域网 IP 地址**（例如 `192.168.1.5`），否则客户端无法连接 Broker。

   **`broker.conf` 内容示例：**

   ```
   # 集群名称
   brokerClusterName = RocketMQ-Cluster
   # Broker名称
   brokerName = broker-a
   # 0表示Master
   brokerId = 0
   # 指定NameServer地址（Docker内部通信使用容器名）
   namesrvAddr = rmqnamesrv:9876
   # 【关键】指定Broker对外服务的IP，请修改为你电脑的IP
   brokerIP1 = 192.168.x.x
   # 开启自动创建Topic
   autoCreateTopicEnable = true
   # 开启自动创建订阅组
   autoCreateSubscriptionGroup = true
   # 监听端口
   listenPort = 10911
   ```

------

### **🚀 第二步：执行 Docker 命令**

打开 PowerShell 或 CMD，依次执行以下命令。

#### **1. 创建网络**

powershell



```
docker network create docker-net
```

*(如果提示已存在，可以忽略)*

#### **2. 启动 NameServer**

注意 Windows 下路径使用反斜杠 `\`。

```
docker run -d `
  --name rmqnamesrv `
  --network docker-net `
  --restart=always `
  -p 9876:9876 `
  -v D:\dockerDir\rocketMQ\namesrv\logs:/root/logs `
  -v D:\dockerDir\rocketMQ\namesrv\store:/root/store `
  -e "MAX_POSSIBLE_HEAP=512m" `
  apache/rocketmq:5.1.4 `
  sh mqnamesrv
```

#### **3. 启动 Broker**

这里我们将刚才创建的 `broker.conf` 挂载进去。

```
docker run -d `
  --name rmqbroker `
  --network docker-net `
  --restart=always `
  -p 10911:10911 `
  -p 10909:10909 `
  -v D:\dockerDir\rocketMQ\broker\logs:/root/logs `
  -v D:\dockerDir\rocketMQ\broker\store:/root/store `
  -v D:\dockerDir\rocketMQ\broker\conf\broker.conf:/opt/rocketmq/conf/broker.conf `
  -e "NAMESRV_ADDR=rmqnamesrv:9876" `
  -e "MAX_POSSIBLE_HEAP=1g" `
  apache/rocketmq:5.1.4 `
  sh mqbroker -c /opt/rocketmq/conf/broker.conf
```

------

### **⚠️ 常见问题与注意事项**

1. **连接失败 (RemotingConnectException)**
   - **原因**：这是最常见的问题。RocketMQ Broker 默认会绑定网卡 IP。如果你在配置文件中不指定 `brokerIP1`，或者指定为 `127.0.0.1`，客户端（Java代码或其他工具）在连接时，会先连上 9876 端口，然后 NameServer 会告诉客户端：“请去连接 IP `x.x.x.x` 的 Broker”。如果这个 IP 是容器内部 IP 或 `localhost`，客户端就无法访问。
   - **解决**：务必在 `broker.conf` 中填写你电脑在局域网中的真实 IP（可以通过在 CMD 输入 `ipconfig` 查看 IPv4 地址）。
2. **文件权限问题**
   - 如果遇到 `Permission denied` 错误，请确保 Docker Desktop 有权限访问 `D:\dockerDir` 目录（通常在 Docker Desktop 设置 -> Resources -> File Sharing 中查看）。
3. **防火墙**
   - 如果外部机器（非本机）需要访问 RocketMQ，请确保 Windows 防火墙放行了 `9876`、`10911` 和 `10909` 端口。

### **📊 可选：部署 Dashboard (控制台)**

如果需要可视化管理界面，可以运行以下命令：

```
docker run -d `
  --name rmqdashboard `
  --network docker-net `
  --restart=always `
  -p 8080:8080 `
  -e "JAVA_OPTS=-Drocketmq.namesrv.addr=rmqnamesrv:9876" `
  apacherocketmq/rocketmq-dashboard:1.0.0
```

部署完成后，浏览器访问 `http://localhost:8080` 即可查看。

## 启动前端

文档上说使用node版本可以包括17，实际上只能用17以下，

然后执行命令

```
npm install
启动执行 文档上说执行dev 根本起不来！！！！
npm run serve   
```

## 项目访问账号密码

他本身的前端访问还需要密码

```
admin
123456
```

## 新建流程的时候报错

通过`system`请求到`/workflow/model`,然后代码就报错了。

通过AI进行修复，好了然后项目崩溃了，具体咋回事不知道了，明天早说

## 定时任务

他的定时任务实现的方式是使用的若依的框架，定时任务方式也和若依实现的一致

[若依定时任务实现方式](https://doc.ruoyi.vip/ruoyi/document/htsc.html#%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1)

在使用过程中呢，有参的方式

![image-20260403103317151](image-20260403103317151.png)

修改这里的参数到时候，然后再点击，任务后边的执行一次，就可以将写好的参数传递给定时任务

### 新增定时任务

需要先创建对应的类，然后才能新增任务要不新增时会报错没有这个bean，任务调用目标字符串，

创建有参的定时任务，构造方法中要字符串使用**单引号**，负责会报错

现在看后台定时任务管理的面板里，不能管理其他项目的定时任务

这里页面展示的定时任务有问题，页面上展示的定时任务，只是展示，实际上根本管理不了，其他项目的定时任务都是使用的springboot自带的定时任务注解实现的，如果想要管理定时任务的化，按照这个写法，就必须要再job项目中写才行，否则根本调用不到，而且后台中写的通过`class`调用的类也根本找不到，这要是初学者自学这个可能要走不少弯路，但是如果所有的定时任务都写在job里，那就不是微服务的思想了，这里如果是springcloud微服务，还是看看分布式定时任务吧
