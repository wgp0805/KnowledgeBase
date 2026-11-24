---
title: "SpringBoot4.2正式发布，人麻了！"
source: "https://mp.weixin.qq.com/s/chth56FnKuaBCPf6WLuB-Q"
author:
  - "[[苏三]]"
published:
created: 2026-11-24
description:
tags:
  - "clippings"
---
苏三 苏三说技术 *2026年11月24日 08:20*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

2026年11月19日，Spring Boot 4.2.0 正式发布了。  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/HUV4yMdu0rdaALF8IDG6QOovC6u0bWee1sgnYqEDxLVakySPwp46kjs5Q9nS07d3J6RhTA5yJ88YG21x78nqk3lL1qtJgJicml0qHHiav82NE/640?wx_fmt=png&from=appmsg#imgIndex=0)

说实话，看到 Release 的第一眼，我脑子里就一个念头：该来的还是来了。

不是新功能多到学不过来，是那些你用了好几年、早就习惯成自然的东西，突然被官方打上了“弃用”的标签。

`RestTemplate` 被弃用了，`TestRestTemplate` 被弃用了，Apache Pulsar 的支持也被弃用了。

更让人后背发凉的是，有一批配置项的 **默认值被悄悄改了** 。

不报错，不警告，但行为变了。

有些小伙伴可能会说：“那我先不升，赖在 4.1 上总行了吧？”

Spring Boot 4. [1.x](http://1.x/) 的开源支持到 2027 年 7 月 31 日就结束了。

“先不升”这个选项，是有保质期的。

今天这篇文章，我就是专门跟大家一起聊聊Spring Boot 4.2，希望对你会有所帮助。

## 一、弃用清单：这些东西以后不能用了

### 1.1 RestTemplate 和 TestRestTemplate：最疼的一刀

Spring Framework 7.1 把 `RestTemplate` 标记为“即将移除”，Spring Boot 4.2 跟着把整套支持基础设施全部弃用了。

具体包括：`RestTemplateAutoConfiguration`、`RestTemplateObservationAutoConfiguration`、`RestTemplateBuilder`、`RestTemplateBuilderConfigurer`、`RestTemplateCustomizer`，以及测试用的 `TestRestTemplate`。

**注意措辞：不是移除，是弃用。**

你的代码还能编译、还能跑，但编译时会看到 warning。官方给出的替代方案很明确：用 `RestClient` 替代 `RestTemplate`，用 `RestTestClient` 替代 `TestRestTemplate`。

**为什么这件事让人麻？**

因为 `RestTemplate` 在项目里的渗透率太高了。一个跑了三年的老项目，HTTP 调用散落在十几个 Service 里，全是 `RestTemplate`。改一个两个不难，改五十个就是体力活。

为什么 Spring 要下这个狠手？

`RestTemplate` 是 2009 年出来的，基于 **阻塞式 I/O** ，线程调一个远程接口就卡在那里等。

在虚拟线程和 WebFlux 越来越普及的今天，这种模型在资源利用率上是吃亏的。

`RestClient` 提供了流式 API，请求构建、拦截器、错误处理都可以链式组合。

### 1.2 Apache Pulsar：2.0.8 是最终版

Pulsar 项目已经捐给了 Apache 软件基金会，所以 Spring Boot 的 Pulsar 支持也被弃用了。

**关键信息** ：Spring for Apache Pulsar 的 **最终版本是 2.0.8** ，Spring 团队不再发布任何更新、维护补丁或 bug 修复。后续的维护和发布全部由 Apache Pulsar 项目接管，新项目名为 **Apache Pulsar support for Spring** 。

**对你意味着什么？**

如果你在用 Pulsar，升级 4.2 不会直接炸，`2.0.8` 这个 starter 在 4.2.0 里仍然可用。

但要获取未来的更新，必须迁移到 Apache Pulsar 官方提供的 starter。

### 1.3 KafkaProperties 的 Client 构建方法

`KafkaProperties` 里的 `buildConsumerProperties()`、`buildProducerProperties()`、`buildAdminProperties()` 被标记为弃用，替代方案是 `KafkaConfigBuilder`。

如果你在代码里手动调用了这些方法，现在就得开始改。如果只是用 Spring Boot 的自动配置，不受影响。

## 二、静默变更：不报错，但行为变了

这一类比弃用更危险。

**弃用至少会给你一个 warning，静默变更连 warning 都没有。**

### 2.1 use-relative-redirects：默认值从 false 变成 true

            **`              server.tomcat.servlet.use-relative-redirects            `（以及它的前身 `              server.tomcat.use-relative-redirects            `）的默认值从 `false` 变成了 `true`** 。

**以前** ：Tomcat 生成重定向响应时，默认返回 **绝对 URL** （比如 `              http://example.com/new-path            `）。  
**现在** ：默认返回 **相对路径** （比如 `/new-path`）。

Spring 团队的理由是“让这个属性的默认值与 Tomcat 自身的默认值保持一致”。

但这对你的项目来说，就是行为变更。

如果你的前端或网关依赖绝对 URL 做解析，升级后拿到的 Location 头会变， **但不会报任何错** 。

**怎么恢复旧行为** ：显式设置 `              server.tomcat.servlet.use-relative-redirects=false            `。

### 2.2 X-Forwarded-Prefix：默认被忽略了

如果你的服务部署在多层代理后面，代理可能会发送 `X-Forwarded-Prefix` 头，告诉后端“我前面挂了一个 `/api` 前缀”。

**4.1 的行为** ：`native` 策略下，`contextPath` 是 `/api`。  
**4.2 的行为** ： **默认忽略了** ，`contextPath` 变成空。

**这意味着什么？** 你的应用在生成链接或重定向时，前缀会丢失。前端访问 `/api/foo`，后端生成的链接可能是 `/foo`，少了 `/api`。

**怎么恢复** ：如果你用的是 `framework` 策略，设置 `              spring.webflux.forwarded-headers.use-forwarded-prefix=true            `。如果你用的是 `native` 策略（Reactor Netty）， **没有直接的配置项** ，只能切换策略或写 `NettyServerCustomizer`。另外，通用开关是 `              server.request.header.forwarded.use-prefix=true            `。

### 2.3 WebFlux multipart：限制更明确了

WebFlux 的 multipart 配置在 [4.x](http://4.x/) 系列中已有相关属性，4.2 进一步明确了 **大小和数量限制** 的行为。

如果你有文件上传接口，且文件大小或数量接近限制值，升级后可能会被拒绝。

**但不会报编译错误，只会在运行时返回错误。**

### 2.4 Tomcat servlet 属性：挪了位置

`              server.tomcat.use-relative-redirects            ` 被挪到了 `              server.tomcat.servlet.use-relative-redirects            `。

**旧配置在新版本里还能用吗？**

能，但会看到弃用警告。

建议直接改成新位置。

## 三、移除清单：这些东西没了

### 3.1 Janino 依赖管理被移除

Logback 移除了对 Janino 的支持，Janino 项目本身也已经归档。

Spring Boot 跟着把 Janino 的依赖管理删了。

**对你意味着什么？**

如果你在 `              pom.xml            ` 里用了 Janino 但没写版本号，以前 Spring Boot 帮你管，现在你得自己写。不写就编译不过。

你说得对，这是文章结构上的一个明显漏洞。适用场景表里把“AMQP 1.0”和“启动更快”列为推荐升级的理由，但正文的优缺点部分只是一笔带过，没有展开讲清楚，读者看到表格会一头雾水。

我补两个小节，放在“静默变更”和“移除清单”之后，把这两点讲透。

## 四、值得关注的新能力

### 4.1 AMQP 1.0 支持：RabbitMQ 的通信协议升级

Spring Boot 4.2 引入了对 **AMQP 1.0** 的支持。

这是这一版最实在的新功能。

AMQP 1.0 和 RabbitMQ 长期使用的 AMQP 0-9-1 是两套不同的协议。

0-9-1 是 RabbitMQ 的“原生协议”，灵活但偏私有；AMQP 1.0 是 OASIS 标准化协议，跨厂商、跨语言的一致性更好。

**对你意味着什么？**

如果你的系统里不只有 Java，还有.NET、Go、Python 的服务，AMQP 1.0 能让它们用同一套标准协议跟 RabbitMQ 通信，减少协议适配层的维护成本。

Spring Boot 4.2 把这套协议的支持收进了官方 starter，不需要再自己拼装第三方库。

**注意** ：AMQP 1.0 不是 0-9-1 的替代品，两者在 RabbitMQ 里可以共存。

如果你的现有系统全是 Java、全用 0-9-1，升级 4.2 不会强制你迁移。但如果你正在做多语言架构，或者计划对接标准化的消息中间件，这个能力值得评估。

### 4.2 可执行 jar 启动更快：启动时间的实打实收益

Spring Boot 4.2 官方 Release Notes 里明确写了 **faster startup of executable jars** 。

**这个优化针对的是“可执行 jar”的启动过程** ，也就是你用 `java -jar              app.jar           ` 启动的那种打包方式。Spring Boot 在 4.2 里优化了可执行 jar 的类加载和资源定位逻辑，减少了启动阶段的开销。

**收益有多大？**

官方没有给出具体的百分比数字，但“faster startup”是作为一个独立条目列在 Release Notes 里的，说明优化幅度是可感知的。

对于 **启动时间敏感** 的场景——比如 Serverless、FaaS、Kubernetes 频繁扩缩容、CI 流水线里频繁启动测试容器——这个优化是实打实的。

**注意** ：这个优化只针对可执行 jar。如果你用的是传统 war 包部署到外部 Tomcat，或者用的是 Native Image，不受这个优化的直接影响。

## 五、一张表看懂 4.2 的完整变更

| 类别 | 变更项 | 具体变化 | 影响 | 应对方式 |
| --- | --- | --- | --- | --- |
| **弃用** | RestTemplate | 整套支持基础设施被弃用，编译时出现 warning | HTTP 调用代码需要迁移 | 用 `RestClient` 替代 |
| **弃用** | TestRestTemplate | 被弃用，编译时出现 warning | 集成测试代码需要迁移 | 用 `RestTestClient` 替代 |
| **弃用** | Apache Pulsar | 2.0.8 是最终版本，后续由 Apache 接管 | 无法获取未来更新 | 迁移到 Apache Pulsar 官方 starter |
| **弃用** | KafkaProperties 构建方法 | `buildConsumerProperties()`<br>等方法被弃用 | 手动调用这些方法的代码需改 | 用 `KafkaConfigBuilder` 替代 |
| **静默变更** | use-relative-redirects | 默认值从 `false` 变成 `true` | 重定向 URL 从绝对变相对，不报错但行为变了 | 显式设 `              server.tomcat.servlet.use-relative-redirects=false            ` |
| **静默变更** | X-Forwarded-Prefix | 默认被忽略 | `contextPath`<br>前缀丢失，生成的链接可能少一段 | `framework`<br>策略设 `use-forwarded-prefix=true`；通用开关设 `              server.request.header.forwarded.use-prefix=true            ` |
| **静默变更** | WebFlux multipart | 大小/数量限制更明确 | 文件上传接口可能被拒绝，运行时才报错 | 检查 `              spring.webflux.multipart.*            ` 配置，按需调整 |
| **静默变更** | Tomcat servlet 属性 | 从 `              server.tomcat.*            ` 挪到 `              server.tomcat.servlet.*            ` | 旧配置还能用，但有弃用警告 | 直接改成新位置 |
| **新能力** | AMQP 1.0 支持 | 引入对 AMQP 1.0 标准化协议的支持 | 多语言架构的消息通信更标准，可与 0-9-1 共存 | 多语言/标准化消息中间件场景可评估 |
| **新能力** | 可执行 jar 启动更快 | 优化可执行 jar 的类加载和资源定位逻辑 | 启动时间缩短，对 Serverless/FaaS/频繁扩缩容场景有收益 | 用 `java -jar` 启动的场景直接受益 |
| **移除** | Janino 依赖管理 | 不再管理 Janino 版本 | `              pom.xml            `<br>里不写版本号就编译不过 | 手动声明 Janino 版本号 |

## 六、RestTemplate 迁到 RestClient

### 5.1 GET 请求

```
// RestTemplate
User user = 
            restTemplate.getForObject(
          "/users/{id}", 
            User.class,
           id);

// RestClient
User user = 
            restClient.get()
          
    .uri("/users/{id}", id)
    .retrieve()
    .body(
            User.class);
```

### 5.2 POST 请求

```
// RestClient
User created = 
            restClient.post()
          
    .uri("/users")
    .body(user)
    .retrieve()
    .body(
            User.class);
```

### 5.3 错误处理

```
User user = 
            restClient.get()
          
    .uri("/users/{id}", id)
    .retrieve()
    .onStatus(HttpStatusCode::is4xxClientError, (request, response) -> {
        throw new UserNotFoundException(id);
    })
    .body(
            User.class);
```

### 5.4 测试：TestRestTemplate → RestTestClient

```
@Autowired
private RestTestClient restTestClient;

            restTestClient.get().uri(
          "/users/1")
    .exchange()
    .expectStatus().isOk()
    .expectBody(
            User.class);
```

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **正在用 4.1，想跟进** | ✅✅✅ 推荐 | 增量升级，收益明确，风险可控 |
| **需要 AMQP 1.0** | ✅✅✅ 推荐 | 4.2 原生支持 |
| **对启动速度敏感** | ✅✅ 推荐 | 可执行 jar 启动更快 |
| **RestTemplate 用量巨大** | ⚠️ 需评估 | 弃用不是移除，可以先不迁，但要规划 |
| **用 Pulsar 做消息** | ⚠️ 需评估 | 2.0.8 是最终版，需要迁移到官方 starter |
| **还在 3.5 或更早** | ❌ 不推荐直接跳 | 先升到 4.0/4.1，再考虑 4.2 |

## 八、写在最后

Spring Boot 4.2 正式发布，人麻了，怎么办？

我的判断是： **麻归麻，但不用慌。**

4.2 的核心变化，不是“新东西学不会”，是“**老东西要换，老配置要查**”。

`RestTemplate` 弃用、Pulsar 弃用、Janino 要自己管版本——这些事不会让你当天就炸，因为弃用不是移除。但它们会一直提醒你，编译时的 warning、启动时的日志，都在说“该改了”。

**具体操作** ：

1. 对照弃用清单，标出需要改的地方
2. `RestTemplate`

	可以分批迁，先迁新代码，老代码排期
3. 检查 `              application.yml            ` 里有没有配 `use-relative-redirects` 和 `X-Forwarded-Prefix`，确认行为变化是否影响你
4. 如果用了 Janino，补上版本号
5. 升级后跑一遍集成测试，重点关注重定向和转发头相关的用例

**Spring Boot 的升级，从来不是“等它稳定了再升”，是“在支持周期内，把该还的债还了”。** 4.2 给了你这个窗口。

## 九、参考资源

Spring Boot 4.2.0 官方发布公告： [https://spring.io/blog/2026/11/19/spring-boot-4-2-0-available-now](https://spring.io/blog/2026/11/19/spring-boot-4-2-0-available-now)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)