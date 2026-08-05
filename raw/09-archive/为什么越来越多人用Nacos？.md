---
title: "为什么越来越多人用Nacos？"
source: "https://mp.weixin.qq.com/s/Z9jOq0SK314wnLzSbRx7XQ"
---
苏三 苏三说技术 *2026年8月5日 09:31*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

> 从Eureka到Nacos，微服务注册中心的一次认知升级

不知道你有没有发现这样一种趋势：最近用的人Eureka越来越少了，而用Nacos的人越来越多了。

而且很多之前用Apollo的人，最近也默默转向Nacos了。

今天这篇文章，我就把Nacos为什么越来越多人用的原因，从底层原理到实战用法，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/120fc0032d790118e773ec1a67b88378_MD5.webp)

## 一、注册和配置中心为什么“合体”？

在聊Nacos之前，我们先理解一个根本问题—— **为什么注册中心和配置中心应该是一体的？**

微服务架构里有两个核心的“中心”：

- **注册中心** ：服务启动时告诉它“我在这里”，服务调用时问它“谁在那里”
- **配置中心** ：存着所有服务的配置参数，改了配置不用重启服务

在Nacos出现之前，这两个“中心”通常是分开的。

Eureka只管注册、Apollo只管配置，你得维护两套系统、两套控制台、两套权限体系。

**问题在哪里？**

想象一下这个场景：服务A调用服务B突然超时了。

你要排查原因——可能是服务B挂了（注册中心的问题），也可能是超时配置被改了（配置中心的问题）。

你需要在两个系统之间来回切换，翻两套日志，看两套监控。

更麻烦的是，Eureka [2.x已经停止维护，1.x版本发展缓慢。](http://2.xn--x,1-r00e343ddugupqwu0buja.xn--x-328ap5x1mfwlis2rd9u./)

你今天选Eureka，明天可能就得考虑迁移方案。

而Consul的配置能力相对较弱，ZooKeeper的配置基本得自己搞watch。

**Nacos的核心价值，就是把这两件事做成了一件事。**

Nacos = 服务注册与发现 + 动态配置管理 + 服务管理。

你只需要维护一套系统，注册中心和配置中心天然打通，服务发现和配置推送共享同一套基础设施。

## 二、一张图看懂Nacos的整体架构

在深入代码之前，我们先建立一个整体认知。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/a12c49713245ea0c9707e560309cb684_MD5.jpg)

Nacos的架构设计充分考虑了 **高可用、高并发和可扩展性** 。

核心模块包括服务发现模块（NameService）、配置管理模块（ConfigService）和AI Registry模块，一致性协议层使用自研的Distro协议和Raft协议保证数据一致性。

**但Nacos最精妙的设计，在于它内部其实干的是两件性质完全不同的活** 。

## 三、AP和CP双模：Nacos最核心的设计哲学

> 有些小伙伴可能会问：“Nacos到底是AP还是CP？”

答案是： **它既是AP，也是CP。按场景选。**

Nacos支持两种一致性模式：

- **AP模式** ：基于Distro协议（最终一致性），优先保证可用性—— **用于服务发现**
- **CP模式** ：基于Raft协议（强一致性）—— **用于配置管理**

### 3.1 为什么服务发现用AP？

服务发现的核心场景是：服务实例频繁上下线。

如果每次上线都要走Raft那种“多数派确认”，集群压力会非常大。

更重要的是，服务发现的容错点很特殊：

- **多一个实例** ：最多多一次失败重试，业务体感几乎没影响
- **少一个实例** ：最多少处理一段时间流量，影响有限

短时间不一致，对业务体感几乎没影响。所以服务发现没必要用强一致，AP就够了。

### 3.2 为什么配置管理用CP？

配置管理就不一样了。

想象一个场景：你在控制台里把一个核心限流值从1000改到100。

如果Nacos集群在这一刻不一致，部分节点收到了新值，部分节点还是老值——客户端从不同节点拉到的配置不一样，业务行为开始飘。

这种情况比“多一个老实例”严重得多。所以配置中心必须CP，写入要在多数派确认成功之后才算成功。

Nacos配置中心走的是 **JRaft** （Raft协议的工程化实现），几个工程细节必须注意：

- **必须≥3节点** ：Raft要选举，2节点没法选
- **写都走Leader** ：Follower收到写请求会转发或拒绝
- **Leader挂了会重新选** ：选举期间短暂不可写，是正常的
- **配置存到MySQL** ：Raft是协调一致性，不是存储

### 3.3 AP与CP模式下的数据流对比

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/4ec8e873ec42a7c6e3412cd6231cff98_MD5.jpg)

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/3b027ee450e4dd4717c2f22fb0aae6a6_MD5.jpg)

## 四、Distro协议深度

Distro是Nacos自研的一致性协议，专门为服务发现场景设计。

### 4.1 责任分片：每个节点管一摊

Distro的核心设计思路是 **责任分片** 。每个Nacos节点只负责一部分服务实例的“权威数据”。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/3ceb2f4afb227533905840ba2745054c_MD5.jpg)

### 4.2 读写分离：读本地、写异步

Distro协议的核心机制：

- **写操作** ：客户端注册到任意节点，节点先本地写再异步广播给其他节点
- **读操作** ：客户端从任意节点读取，读到的是该节点当前的本地数据
- **最终一致** ：一段时间内集群内同一服务实例视图会收敛
- **节点故障可恢复** ：某节点挂了，它负责的实例数据由其他节点接管，重启后可重新拉取

**这个设计的精妙之处在于：它承认了“服务发现是AP场景”这件事，没有为了强一致硬上Raft** 。

### 4.3 健康检查机制

Nacos的健康检查非常灵活：

| 健康检查类型 | 适用场景 | 工作机制 |
| --- | --- | --- |
| **客户端主动心跳** | 大多数场景 | 服务实例定期发送心跳，超时标记不健康 |
| **服务端主动探测** | 特殊场景 | 服务端主动探测实例端口是否可达 |
| **TCP/HTTP检测** | 定制化需求 | 通过TCP连接或HTTP请求检测服务可用性 |
| **自定义检测** | 特殊业务场景 | 支持用户自定义健康检查逻辑 |

### 4.4 CopyOnWrite：读写并发冲突的优雅解法

Nacos为防止读写并发冲突，在服务注册表的更新中大量运用了 **CopyOnWrite思想** ——把原内存结构复制一份，操作完再替换回真正的注册表。

**为什么不用锁？**

因为服务发现是典型的“读多写少”场景。读操作频繁（每次服务调用都要查），写操作相对较少（实例上下线）。

CopyOnWrite让读操作完全无锁，写操作复制一份再替换，读操作永远看到一致的数据。

## 五、配置推送

很多人以为Nacos推配置走的是WebSocket。

**不是** 。

它用的是 **长轮询（Long Polling）** 。

### 5.1 长轮询的工作流程

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/c4571905730bfa8be9efe94b561e53bf_MD5.jpg)

### 5.2 为什么用长轮询而不是WebSocket？

- **简单** ：HTTP协议，所有SDK都好实现，运维和网关压力小
- **兼容性好** ：不需要支持WebSocket的代理
- **可靠** ：HTTP请求天然支持超时和重试
- **防火墙友好** ：WebSocket在某些网络环境下可能被拦截

### 5.3 配置数据的变更通知机制

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/f23fb511f1f7495d352fe7aac54227f4_MD5.jpg)

## 六、Nacos 2.0：性能提升10倍的秘密

如果你还在用Nacos [1.x，这篇文章有一个非常重要的信息要告诉你：](http://1.x，这篇文章有一个非常重要的信息要告诉你：) **Nacos 2.0性能提升了10倍** 。

### 6.1 1.x时代的“三座大山”

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/cc7ed8d4f9e1a1144d1e561cfd3c6652_MD5.jpg)

### 6.2 2.0的四张王牌

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/67c6b9e3c3c38258373c4ea5dc30c0e3_MD5.jpg)

**效果有多明显？** 有团队把Nacos从1.4升级到2.1后，服务发现的延迟从 **800ms直接降到20ms** ，降了\*\*96%\*\*。

如果你还在跑Nacos [1.x，升级的理由已经够了——](http://1.xn--x,-81ta2650dv7fh3kjvjm63cppcr4efv7a8oa/) **延迟降96%，连接数降8倍，不需要改任何业务代码** 。

## 七、Nacos 3.0：从微服务到AI Agent

> 有些小伙伴可能会问：“Nacos不是做微服务的吗？跟AI有什么关系？”

2026年，Nacos发生了一次 **定位级别的巨变** 。

官方定义从“更易于构建云原生应用的动态服务发现、配置管理和服务管理平台”变成了 **“一个易于构建AI Agent应用的动态服务发现、配置管理和AI智能体管理平台”** 。

### 7.1 为什么Agent需要Nacos？

微服务时代，Nacos解决的是“服务A怎么找到服务B”。AI Agent时代，Agent需要调用各种工具——查天气、查订单、发邮件、操作数据库。

问题来了： **Agent怎么知道有哪些工具可以用？怎么知道每个工具的调用方式？怎么动态发现新上线的工具？**

用人话说：微服务时代，Nacos是 **人与服务之间的“电话簿”** 。AI Agent时代，Nacos要变成 **Agent与工具之间的“电话簿”** 。

### 7.2 AI Registry：三层架构

Nacos 3.0引入了全新的 **AI Registry模块** ，和传统的服务注册、配置管理并列，成为Nacos的三大核心能力之一。

AI Registry的架构分为三层：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Nacos%EF%BC%9F/8e3f007291ef00b8b68bdc95b4cbaa49_MD5.jpg)

**模型层** ：管理AI模型的动态参数——Prompt模板、学习率、连接配置等。这一层复用了Nacos配置管理的分发能力。典型场景：线上Prompt模板热更新、多模型切换、A/B测试不同Prompt版本。

**工具层** ：这是AI Registry最核心的一层—— **MCP Registry** 。它解决的问题是：让LLM模型和MCP工具之间实现自动发现、自动注册、智能检索。关键能力是通过智能过滤，减少传递给大模型的工具描述数量，从而 **降低Token消耗** 。

**智能体层** ：管理AI Agent的生命周期和元数据。

## 八、Nacos vs 主流注册中心对比

我把几个主流注册中心放在一起做了个深度对比：

| 对比维度 | Nacos | Eureka | Consul | ZooKeeper |
| --- | --- | --- | --- | --- |
| **一致性协议** | **AP+CP双模** | AP | CP | CP |
| **配置中心** | ✅ 原生支持 | ❌ 需额外组件 | ⚠️ 较弱 | ⚠️ 需自己搞watch |
| **控制台** | ✅ 功能丰富 | ❌ 简单 | ✅ 有 | ❌ 无 |
| **健康检查** | 心跳+多种方式 | 仅心跳 | HTTP/TCP/gRPC | 心跳 |
| **Spring Cloud集成** | ✅ 深度集成 | ✅ 原生 | ✅ 支持 | ⚠️ 需适配 |
| **多数据中心** | ⚠️ 有限 | ❌ 不支持 | ✅ 原生支持 | ❌ 不支持 |
| **服务管理** | ✅ 完善 | ❌ 无 | ✅ 有 | ❌ 无 |
| **AI原生支持** | ✅ 3.0 AI Registry | ❌ | ❌ | ❌ |

Eureka [2.x已经停止维护，1.x版本发展缓慢。Consul的配置能力相对较弱。ZooKeeper的配置基本得自己搞watch。](http://2.xn--x,1-r00e343ddugupqwu0buja.xn--x-328ap5x1mfwlis2rd9u.xn--consul-8d4j023d5tg656drbbu83dhuekx5devf.xn--zookeeperwatch-yh8yc21e7mgdywpinsy8ehexb4olmi0g./)

**Nacos最大的优势不是“某一个功能特别强”，而是“该有的都有，而且都做到了及格线以上”** 。

## 九、实战：3步跑通Nacos

光说理论不够，我们来看怎么快速上手。

### 9.1 第一步：启动Nacos Server

从GitHub下载最新版本：

```
# 下载后解压
unzip 
            nacos-server-2.3.2.zip
          
cd nacos/bin

# 单机模式启动（开发/测试环境）
sh 
            startup.sh
           -m standalone
```

控制台默认地址：http://127.0.0.1:8848/nacos。默认账号是nacos/nacos，首次登录强制改密码。

### 9.2 第二步：Spring Boot服务接入

在 [pom.xml中添加依赖：](http://pom.xml中添加依赖：)

```
<dependency>
    <groupId>
            com.alibaba.cloud
          </groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>

<dependency>
    <groupId>
            com.alibaba.cloud
          </groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
```

在 [application.yml中配置：](http://application.yml中配置：)

```
spring:
  application:
    name: user-service
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848
      config:
        server-addr: 127.0.0.1:8848
        file-extension: yaml
```

加上 `@EnableDiscoveryClient` 注解，服务启动后自动注册到Nacos。

### 9.3 第三步：动态配置刷新

```
@RestController
@RefreshScope  // 配置变更自动刷新
public class ConfigController {
    
    @Value("${
            app.timeout:30}"
          )
    private int timeout;
    
    @GetMapping("/timeout")
    public int getTimeout() {
        return timeout;
    }
}
```

在Nacos控制台修改 `              app.timeout            ` 的值，不需要重启服务，配置自动生效。

## 十、优缺点

### 优点

**1\. 注册中心+配置中心一体化** Nacos把两件事做成了一件事，少养一套系统。Eureka只做注册，Consul配置弱，ZooKeeper配置基本得自己搞watch。

**2\. AP/CP双模切换** 服务发现走Distro（AP），配置管理走Raft（CP）。你不用为了“配置写错全公司挂掉”再单独搭个强一致的存储。

**3\. 性能强悍** Nacos 2.0将通信从HTTP升级到gRPC，性能提升10倍。服务发现延迟从800ms降到20ms。

**4\. Spring Cloud Alibaba深度集成** 国内大多数团队用的是Spring Cloud Alibaba而不是Spring Cloud Netflix。Nacos是这套生态里的默认注册和配置中心，集成几乎零摩擦。

**5\. 生态成熟** 控制台、命名空间、灰度、推送、监听、SDK多语言，都已经磨过几年。线上踩过的坑，社区基本都讨论过。

**6\. AI时代持续进化** Nacos 3.0引入了AI Registry模块，支持MCP工具的自动发现和注册。

**7\. 开源协议友好** Apache 2.0协议，可自由使用、修改、商用。

### 缺点

**1\. 多语言SDK支持不均衡** Java最完整，Go和Node还在追。如果团队使用多种语言，需要评估各语言SDK的成熟度。

**2\. 文档更新跟不上版本** 3.0引入AI Registry/MCP管理后，能力扩展了，文档跟得有点吃力。

**3\. 大规模集群部署较复杂** 3节点+MySQL手动部署步骤繁琐，容器化部署更推荐。

**4\. gRPC端口需要额外放行** Nacos [2.x引入了gRPC通信端口（主端口+1000），防火墙必须放行，否则集群间通信失败。](http://2.xn--xgrpc\(+1000\),,-lx7vg0bxznka964elzdrwmca36m802dymdt16cl5d2q2cqz1ed65cda9869ajy3dzp8ajvvxa9356cb6bf3ijtu./)

## 十一、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **Spring Cloud Alibaba项目** | ✅✅✅ 强烈推荐 | 零摩擦集成，生态默认选择 |
| **需要注册+配置一体化** | ✅✅✅ 强烈推荐 | 少维护一套系统，降低运维成本 |
| **微服务规模中等偏大** | ✅✅✅ 强烈推荐 | 性能强悍，支撑大规模服务注册 |
| **需要AP/CP灵活切换** | ✅✅✅ 强烈推荐 | 服务发现用AP，配置管理用CP |
| **Kubernetes云原生环境** | ✅✅ 推荐 | 提供良好的Kubernetes支持 |
| **AI Agent/MCP工具管理** | ✅✅ 推荐 | Nacos 3.0原生支持AI Registry |
| **纯Dubbo项目** | ✅✅ 推荐 | 可替代ZooKeeper作为注册中心 |
| **多语言混合团队** | ⚠️ 需评估 | Go/Node SDK成熟度不如Java |

## 十二、写在最后

回到最初的问题： **为什么越来越多人用Nacos？**

答案其实很简单—— **因为它把注册中心和配置中心这两件微服务架构中最核心的事情，做成了“一件事”** 。

Eureka只做注册，Consul配置弱，ZooKeeper配置要自己搞watch。

每一个都有短板，每一个都让你不得不多维护一套系统。

**Nacos走了一条“第三条路”** ——注册中心和配置中心天然一体化，AP和CP按场景切换， [1.x到2.x性能提升10倍，3.0又拥抱了AI时代。它不是“某一个功能特别强”，而是](http://1.xn--x2-rh5c.xn--x10,3-i03ht6qm23a7jh879e.xn--0ai-1h9dtqm6vo81a4lat9u.xn--,-ohnd1018b2baxjz9yr0ae99c5piu1tia725cy98bot6b9ed/) **“该有的都有，而且都做到了及格线以上”** 。

从Eureka到Nacos，不是“谁取代谁”，而是 **在合适的场景选择更合适的工具** 。

开源地址

- **GitHub** ： [https://github.com/alibaba/nacos](https://github.com/alibaba/nacos)
- **官方文档** ： [https://nacos.io](https://nacos.io/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

我最近开发的企业智能知识库系统就用了Nacos的注册中心和配置中心功能，感兴趣的小伙伴，可以加入星球学习。