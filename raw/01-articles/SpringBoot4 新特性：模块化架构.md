---
title: "SpringBoot4 新特性：模块化架构"
source: "https://mp.weixin.qq.com/s/ugbPFPIW0YpLSZ6QoXkyHg"
---
点击关注 👉 IT码徒 *2026年7月30日 23:08*

点击“IT码徒”，关注，置顶公众号

每日技术干货，第一时间送达！

2014 年，Spring Boot 1.0 横空出世，凭借“开箱即用”的理念彻底改变了 Java 开发方式。当时，它的核心自动配置包 spring-boot-autoconfigure 仅 182 KB。到了 Spring Boot 3.5，这个包已经膨胀至 2 MB，支持的功能越来越多，但复杂度和体积也随之增长。

在即将到来的 Spring Boot 4 中，Spring 官方团队对这一现状进行了彻底重构，正式引入 模块化（Modularization） 架构。这一改变不仅影响了项目结构和依赖关系，更为开发者带来了更轻量、更清晰、更高效的使用体验。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

01

模块化改造的背景

Spring Boot 的最大优点之一，是它能自动配置大量技术组件，如 Web、JPA、Redis、Kafka 等。但随着支持范围的扩大，也带来了几个问题：

- 臃肿的自动配置包 ：无论是否使用，所有自动配置类都会被打包进应用；
- IDE 提示噪音多 ：会出现许多无关的类和配置建议；
- 启动扫描开销大 ：类路径越大，启动速度越慢。

Spring 团队意识到：要保持 Spring Boot 的“轻量”和“易用”，就必须重新设计其架构边界，这正是 Spring Boot 4 模块化的出发点。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

02

Spring Boot 4 模块化架构设计

Spring Boot 4 将原先的单体式自动配置包 拆分为多个独立模块 。每个模块仅负责一种特定技术的自动配置，例如：

| 模块名称 | 功能描述 |
| --- | --- |
| `spring-boot-webmvc` | 传统 Servlet Web 应用 |
| `spring-boot-webflux` | 响应式 Web 应用 |
| `spring-boot-data-jdbc` | JDBC 数据访问 |
| `spring-boot-flyway` | 数据库迁移管理 |
| `spring-boot-webclient` | 独立 WebClient 支持 |

每个模块都有清晰的边界，职责单一、依赖明确，从而让整个框架可维护性更高。

模块化带来的好处

模块化带来的核心优势包括：

1. 可维护性更高：模块边界清晰，开发者和贡献者可以更专注于特定技术领域，IDE 也能提供更精准的代码提示。
2. 启动更快、内存占用更小：应用只引入所需模块，不再加载冗余功能，减少类路径扫描，优化启动时间与内存占用。
3. 配置更精准：Spring Boot 4 能更准确地识别依赖意图。例如，只想使用 WebClient 时，引入 spring-boot-webclient 模块即可，无需再关闭 Web 服务器自动配置。
4. 支持更多灵活用例：例如，Micrometer 监控模块可以独立使用，无需引入完整的 Actuator 依赖链。
![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=4)

03

测试支持的模块化改造

模块化不仅体现在主功能上，测试支持也随之重构。 Spring Boot 4 新增了测试专用模块，如：

- spring-boot-data-jdbc-test
- spring-boot-starter-webmvc-test
- spring-boot-starter-security-test
- spring-boot-starter-flyway-test

每个功能模块都有对应的测试 Starter，确保测试依赖和生产依赖保持一致且精简。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=6)

04

从 Spring Boot 3 迁移指南

如果你想从 Spring Boot 3 迁移到 Spring Boot 4，大多数项目只需要：

- 更新 Starter 依赖
- 添加测试 Starter
- 更新包路径与自定义配置

模块化后，包路径调整为 \` [org.springframework.boot.](http://org.springframework.boot./) \`。 如果项目中有手动导入的自动配置类或自定义 Starter，需要同步修改。

为方便老项目平滑迁移，Spring Boot 4 提供了 “Classic Starters” ：

```
<dependency>
  <groupId>
            org.springframework.boot
          </groupId>
  <artifactId>spring-boot-starter-classic</artifactId>
</dependency>
```

该模式会自动引入所有模块的自动配置，但不包含新的依赖结构，适合过渡阶段。 开发者可先迁移到 Spring Boot 4 的 Classic 模式，再逐步精简为独立模块。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=8)

05

总结

Spring Boot 4 的模块化不仅让框架变得更清晰、更轻量，也让开发体验更自然、更高效。对于想要构建更轻、更快、更可控的企业级应用而言，Spring Boot 4 的模块化，是一场值得投入的升级。

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[IDEA 2026.2 正式发布，新特性真香！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514363&idx=1&sn=273d08907ef18dde4838c616e98f699f&scene=21#wechat_redirect)[SpringBoot + FFmpeg + ZLMediaKit 实现本地视频推流](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514363&idx=2&sn=491eacef61fb14000301127819d40f18&scene=21#wechat_redirect)[Redis官方发布高颜值可视化工具，功能更是强的离谱！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514355&idx=1&sn=47671f3b2d26c79e3e2f44eb767196d7&scene=21#wechat_redirect)[SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514355&idx=3&sn=7a817b3586c4a01bf59844e100363df1&scene=21#wechat_redirect)[Qoder王炸更新，比"写得快"更重要的是"写得安全"！！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514319&idx=1&sn=07180a3fa68b5c5d4e9d142e7a058253&scene=21#wechat_redirect)[让SpringBoot不需要Controller、Service、DAO、Mapper，卧槽！这款工具绝了！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514317&idx=1&sn=7b7f0673065c8ad58dca717809932f9d&scene=21#wechat_redirect)

Springboot · 目录

阅读原文