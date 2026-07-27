---
title: "推荐5个牛逼的AI Agent项目"
source: "https://mp.weixin.qq.com/s/yMjYj-WX6qIDKjT4srQAVg"
---
苏三说技术 *2026年7月27日 09:00*

## 大家好，我是苏三，又跟大家见面了。

## 前言

最近我一口气肝了13个SpringBoot项目。

包括：5个AI Agent实战项目。

从0~1项目开发实战、系统架构、系统设计、表设计、高并发、微服务、分布式、集群、SaaS、多租户、Vue、小程序、AI Agent、LangChain、Spring AI、Spring AI Alibaba、RAG、KAG、Fucation Calling、MCP、向量检索、向量库什么都有。

今天给大家介绍一下这些项目，感兴趣的小伙伴，可以加入星球学习，嘎嘎香。

## 1.企业智能知识库系统

企业级智能知识库系统，基于 **Spring Cloud 微服务架构** ，将大语言模型（LLM）、检索增强生成（RAG）与知识图谱（KAG）深度结合，为企业提供从知识沉淀、智能检索到 AI 问答的全链路知识管理能力。

### 项目介绍

基于 Spring Cloud 微服务 + Nacos 注册中心，包含 **10 个独立服务模块** ，通过 API Gateway 统一入口、RabbitMQ 异步事件总线实现服务间解耦。

- **kb-gateway（8080）** ：API 网关卡，JWT 鉴权过滤、CORS、请求日志、统一响应格式化
- **kb-user-auth（8081）** ：用户认证与权限管理，JWT 签发/校验、RBAC 权限模型、团队管理、邮箱验证
- **kb-document（8082）** ：文档核心服务，文档 CRUD、分类树、标签、评论、收藏、审阅流程、版本历史与 Diff 对比、访问控制与分享、Markdown 编辑、自动保存、MongoDB 文档内容存储
- **kb-search（8083）** ：全文检索引擎，ElasticSearch 搜索引擎、搜索建议与自动补全、搜索历史管理、RAG 混合检索对接
- **kb-file（8084）** ：文件存储与处理，RustFS 分布式文件存储、Apache Tika 格式转换（25+ 文件类型）、FFmpeg 媒体转码、RabbitMQ 异步转码消费
- **kb-statistics（8085）** ：数据统计与分析，仪表盘总览、文档/用户/评论统计、趋势分析、热点文档、分类分布、定时聚合任务
- **kb-ai（8086）** ：AI 智能问答引擎，AI Chat 对话（Qwen/DeepSeek 多模型）、RAG 检索增强生成（文档切块 → Embedding → 向量索引 → 语义检索）、KAG 知识增强生成（LLM 实体关系抽取 → 图谱构建 → 图检索 → RAG+Graph 融合）、AI 辅助写作、对话历史管理、用户反馈收集
- **kb-graph（8088）** ：知识图谱服务，Neo4j 图数据库存储、实体/文档节点与关系建模、图遍历与路径检索、子图查询、社区发现、实体合并
- **kb-foundation（8089）** ：系统基础服务，系统配置管理、数据字典、通知管理（WebSocket STOMP 实时推送）、通知模板、操作日志（AOP 自动采集 + MQ 异步写入）
- **kb-common** ：公共模块，全局异常处理、统一响应体（Result）、AOP 操作日志注解与切面、JWT 工具、分布式雪花 ID、自定义业务异常、MyBatis Plus 自动填充

### 核心能力

- **文档全生命周期管理** ：草稿 → 提交审阅 → 审批通过/驳回 → 发布 → 归档，完整状态流转。Markdown 编辑器 + 实时自动保存至 MongoDB，支持批量导入导出。
- **版本历史与回溯** ：每次编辑生成版本快照，版本 Diff 对比，一键回滚到任意历史版本。
- **审阅流与协作** ：多级审阅流程，批量审批，嵌套评论线程，点赞收藏，访问控制与链接分享。
- **文件处理引擎** ：支持 PDF、Word、Markdown、HTML 等 25+ 文件格式上传，Apache Tika 驱动格式转换，FFmpeg 媒体转码，RustFS 分布式存储。
- **ElasticSearch 全文检索** ：关键词搜索、自动补全与搜索建议、搜索历史记录，与 RAG 语义检索互补形成双路召回。
- **RAG 检索增强生成** ：文档自动切块 → text-embedding-v3 向量化 → ElasticSearch 向量索引 → 向量 + 关键词双路混合检索（RRF 融合排序）→ LLM 上下文注入，回答附带来源引用。
- **KAG 知识增强生成** ：LLM 从文档切片中自动抽取实体与关系 → Neo4j 图谱构建 → 图遍历检索实体关联知识 → RAG + Graph 结果融合，将离散文档编织为结构化知识网络，回答不仅是片段匹配，更是关系推理。
- **知识图谱** ：Neo4j 存储文档实体、知识实体、文档切片节点与关系边，支持图遍历、路径查询、子图展开、社区发现、实体合并，让隐性知识关系显性化。
- **AI 对话与写作** ：多轮对话历史管理，流式响应，AI 辅助写作与文档问答，用户反馈闭环。
- **实时通知推送** ：WebSocket STOMP 协议实时推送审阅通知、系统公告，通知模板可配置。
- **数据统计与看板** ：仪表盘总览、文档/用户/评论多维统计、趋势分析、热点文档排行、分类分布、活跃用户排行，定时任务自动聚合。
- **操作审计** ：AOP 注解自动采集操作日志，RabbitMQ 异步写入，操作人员、操作类型、请求参数、执行结果全链路可审计。

### 技术栈

| 类别 | 技术选型 |
| --- | --- |
| 语言与框架 | Java 21、Spring Boot 3.2.0、Spring Cloud 2023.0.0 + Alibaba Nacos |
| 微服务组件 | Nacos（注册中心 + 配置中心）、Spring Cloud Gateway、OpenFeign |
| ORM | MyBatis Plus + Druid 连接池 |
| 数据库 | MySQL 8.0（业务数据）、MongoDB（文档内容/自动保存）、Neo4j（知识图谱） |
| 搜索引擎 | ElasticSearch（全文索引 + 向量索引） |
| 缓存 | Redis（Caffeine 本地缓存 + Redis 二级缓存） |
| 对象存储 | RustFS（分布式文件存储） |
| 消息队列 | RabbitMQ（异步事件：统计聚合、通知推送、操作日志、索引重建） |
| AI 模型 | Qwen / DeepSeek（LLM 对话）、text-embedding-v3（向量化） |
| 文档处理 | Apache Tika（格式转换）、FFmpeg（媒体转码） |
| 实时推送 | WebSocket STOMP |
| 构建与部署 | Maven 多模块、Docker 容器化 |
| API 文档 | Knife4j（Swagger 增强） |
| 前端 | React 18 + TypeScript + Vite + Ant Design 5 + Zustand + React Router 6 |

### 技术亮点

- **微服务 + 事件驱动架构** ：10 个独立服务模块，Nacos 注册发现，Feign 声明式服务调用，RabbitMQ 异步事件总线串联「统计聚合、通知推送、操作日志、全文索引重建、KAG 图谱重建」等关键管线，模块边界清晰，可独立扩展。
- **RAG + KAG 双引擎融合** ：不是简单的文档片段检索——RAG 提供语义级别的模糊匹配，KAG 在此基础上通过 LLM 抽取实体关系构建知识图谱，将散落的文档内容编织为结构化知识网络。查询时 RAG 与 Graph 双路并行检索、结果融合排序，兼顾语义广度与逻辑深度。
- **混合检索 + RRF 融合** ：ElasticSearch 向量语义检索 + 关键词检索双路召回，RRF（Reciprocal Rank Fusion）融合排序，比单一检索方式命中率显著提升。
- **全链路异步解耦** ：RabbitMQ 驱动统计聚合、通知推送、操作日志写入、搜索引擎索引重建、KAG 图谱重建等关键流程，核心业务操作低延迟，非关键计算异步消化。

架构图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/8ea140ffde0d5eb2f24a9ffc1058ac8d_MD5.png)

部分页面截图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/a1d38a957ee6f8dfc0c97231e8354e3f_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9176dd90ed6d44d502ce80ead1dc5ea3_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7ec56fa4f7f976931525b129356d988f_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/e8ddc7fdd1e66c9ab1a80d9ab16e6ef5_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/4f49b4e3a9618869b920ee246a742e29_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9e4eb742cc6d687e34fc6fd0c1004caa_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/f9fbc516e86bb8de740d11df29bc9f89_MD5.png)

2.智能代码审查AI Agent

## 项目描述

代码审查AI Agent(CodeGuardian AI) 是面向企业与团队的智能代码审查 Agent。

它将传统静态分析与大语言模型（LLM）深度结合，提供多语言、多维度、高上下文感知的代码问题识别与修复建议。

通过与 Git 仓库、CI/CD 流水线的无缝集成，项目在开发、提交、发布前审计等关键环节提供可审计、可落地的审查能力与专业报告。

## 核心功能

- 多范围审查：支持项目/目录/文件/代码片段/Git 项目审查，适配不同开发阶段与场景。
- 深度分析（AI+规则）：LLM 结合规则引擎（PMD/Checkstyle/SpotBugs/Semgrep），既有上下文推理又有规范落地。
- RAG 增强：基于代码库与知识库的检索增强生成（Hybrid：BM25 + 向量检索 + Rerank），提供相似问题与修复示例。
- Function Calling：以结构化工具调用驱动本地分析器与解析器（JavaParser/Semgrep），强制输出严格 JSON 结果（Finding/Report）。
- 专业报告：生成 HTML/Markdown/PDF 报告，包含问题分布、严重级别统计、位置与 Diff、可执行建议。
- 历史与检索：审查记录留存、分页与查询（名称/范围/时间）、二次检索与复盘。
- 规范与规则：内置阿里/Google/Airbnb/PEP8 规范模板，支持自定义规范（名称+要点）、权重调优。
- Git 集成：支持 Git 地址配置（账户与令牌），拉取并增量分析模块级问题。
- CI/CD 集成：REST API 与 Webhook，在 PR/MR、构建、发布前自动触发审查与阻断策略。
- 安全与合规：敏感信息脱敏、凭据仅会话态、审计日志与链路追踪。
- 基于Redis缓存的语义指纹功能，显著降低重复代码/相似代码的模型调用成本与耗时。

## 技术栈

- 语言与框架：Java 21、Spring Boot [3.x、Spring](http://3.xn--xspring-yo3f/) Web（REST）
- 解析与规则：JavaParser、Semgrep、PMD、Checkstyle、SpotBugs、Tree-sitter（可选）
- AI 接入：Spring AI；RAG（Embedding + 向量库 + BM25）
- 数据与存储：PostgreSQL（任务/结果）、Redis（缓存）、MinIO（对象存储/大报告）
- 检索与向量：ElasticSearch/pgvector/VectorDB（可选，混合检索）
- 并发与事件：Java 21 虚拟线程（Loom）、Redis Streams（事件总线，可选）
- 构建与部署：Maven、Docker
- 观测与日志：Grafana/ELK、SLF4J + Logback
- 测试：JUnit 5

## 技术亮点

- 可演进单体 + 事件驱动：以模块化单体起步，内部事件总线组织审查管线，平滑演进为微服务。
- 虚拟线程并发：利用 Java 21 Loom 显著提升多文件/多模块并行分析吞吐。
- 混合检索与重排：BM25 + 向量检索 + Rerank，让上下文更精准、建议更可靠。
- 工具函数调用：LLM 与本地分析器协作，既智能又可落地，输出严格结构化结果。

系统架构图：

![智能审查系统架构图](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/c1a1e28c30e7aeb28466231b1f64e734_MD5.webp)

部分页面截图：

![image.png](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7e19c612d54bc8af1378ebe48c8ba204_MD5.png)

![image.png](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/a3168337d756eac5455f1cabc86cd942_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/c29a5bdc6fe084fe2a0ecdbde87e830c_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/204819be26cb21ef0c89a05bcfb06371_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9f77676ab1b4132827c12563ff891b57_MD5.webp)

扫描下方二维码即可加入星球（今天前10名有优惠）：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价159，今天券后仅需129，后面会逐步涨到299。

只有10 张优惠券，数量有限，先到先得。

如果不满意3天内包退。

## 3 100万QPS短链系统

使用技术：JDK21、 [SpringBoot3.5.3、JPA、Redis、布隆过滤器、Sentinel、Nacos、Redisson、shardingsphere、HikariCP、guava、Prometheus、AlertManager、Grafana、ELK等。](http://springboot3.5.xn--3jparedissentinelnacosredissonshardingspherehikaricpguavaprometheusalertmanagergrafanaelk-gq70gdafaifioifkmh02632hmkff9m8ojwnjefkq9i6e./)

这个系统拥有超高的并发，面包含的东西很复杂。

目前设计了32个数据库，每个数据库包含256张表。

每天可支持2.6亿以上的数据写入。

简历中加上短链系统面试机会一下子多了很多：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/1a0d33347a9c3bed8477b47ceef670b0_MD5.webp)

一周拿了3个offer：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/94e6c1ba6228a5e8fd828252cbc15e3a_MD5.webp)

该系统的亮点是：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/51213318e2631c3e2d873a9df039333a_MD5.webp)

1. 使用了最新的JDK21和 [SpringBoot3.5.3](http://SpringBoot3.5.3)
2. 100万QPS的超高并发请求
3. 数据库分库分表设计
4. 多级布隆过滤器设计
5. 限流和熔断的使用
6. Redis分片集群
7. 改进后的雪花算法
8. Redis分布式锁的使用
9. Redis Stream的使用
10. 多级缓存设计
11. 多线程的处理
12. 完整的单元测试覆盖
13. 使用Prometheus对项目实时监控
14. 使用Grafana创建监控仪表盘
15. 使用AlertManager实现自动报警功能
16. 接入钉钉报警
17. 基于时间片的布隆过滤器
18. 系统平滑8倍扩容
19. 基于Docker容器化部署
20. 支持多种短链生成算法
21. 接口幂等性设计
22. 数据双写机制
23. 历史数据迁移程序
24. 数据一致性校验程序
25. 过期数据自动迁移程序
26. 多个服务节点数据同步机制

等等。。。

基于时间片的布隆过滤器流程图如下：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/779ecf0e361a50249ee3e80390d3ede1_MD5.webp)

短链系统平滑扩容方案如下：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/3bff8b0a217eef19a24b22e0f259f06a_MD5.webp)

通过这个项目，可以学到很多高并发、流量评估、分库分表、多级缓存、多级布隆过滤器、限流、熔断、多线程、监控、报警、数据扩容、集群、广播消息、单元测试编写等多方面的知识。

目前这个项目包含两端代码：

1. 后端服务
2. 前端服务

想进大厂的小伙伴们，一定不要错过这个项目，里面有很多加分项。

扫描下方二维码即可加入星球（今天前10名有优惠）：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价159，今天券后仅需129，后面会逐步涨到299。

只有 10 张优惠券，数量有限，先到先得。

如果不满意3天内包退。

4.智能天气播报AI Agent

### 核心功能

- **天气数据获取** ：实时获取天气信息
- **智能播报** ：用自然语言播报天气
- **穿衣建议** ：根据天气推荐穿衣搭配
- **出行建议** ：基于天气条件的出行建议
- **语音播报** ：支持语音播报功能

### 技术栈

核心框架：

- Spring Boot [3.x](http://3.x/)
- Spring AI Alibaba Starter

AI服务：

- 通义千问 (天气解读)
- 阿里云语音合成

第三方API：

- 聚合数据API

数据存储：

- Redis (天气数据缓存)
![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/b474be126bdfee2e01183bbd8e6bee12_MD5.webp)

5.智能翻译助手AI Agent

### 核心功能

- **文本翻译**
	支持中英日韩等多语言互译
- **文档翻译**
	PDF、Word、Excel文档智能翻译
- **实时对话翻译**
	聊天场景的实时翻译
- **术语库管理**
	专业术语的定制化翻译
- **翻译质量评估**
	自动评估翻译准确性
- 会员点数付费功能

### 技术栈

核心框架：

- Spring Boot [3.x](http://3.x/)
- Spring AI Starter
- Elasticsearch
- MinIO

AI服务：

- 通义千问 (文本理解和优化)
- RAG

数据存储：

- MySQL (翻译记录)
- Redis (缓存)

前端：

- Thymeleaf
- Bootstrap (UI框架)
- JavaScript ES6+
- WebSocket

系统架构图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/95aecc082389c817833cfb1f685ec5a5_MD5.webp)

部分页面截图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/ccffdf78ab2f58249145bb235b24807b_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/5aec76b2465041fcd8bd316eb5f1cd86_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/cbc2b808bd8c3dff00223701ff1a0c5d_MD5.webp)

这个项目是一个完整的AI商业应用，包含了完整的会员开通、下单、支付、获取点数、消费点数、续费等功能。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/20f7aee37e1e8bf11ab2bb26e98dcc1f_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/4a16252b389ac84ddf99dcaeca55d9f6_MD5.webp)

## 6 SaaS点餐系统

使用技术：JDK21、 [SpringBoot3.4.3、SpringCloud、SpringCloud](http://springboot3.4.xn--3springcloudspringcloud-9i2vla/) Alibaba、Gateway、Mybatis、PostgesSQL、Redis、RocketMQ、ElasticSearch、Knife4j、Prometheus、Grafana、Minio、数据隔离等。

SaaS点餐系统是一套：DDD开发模式 + 多租户 + PostgesSQL 的复杂微服务系统。

包含了9个微服务。

系统整体架构如下：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/ed3db66c0d8b4da9f6df292b23cb6cb6_MD5.webp)

数据隔离方案如下：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/d126106871f2eae1087321cf687e32d8_MD5.webp)

DDD开发模式的代码示例：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/e0115fb3fd6b0ee81e02ca46125c92eb_MD5.webp)

通过这个项目可以掌握DDD开发模型、多租户数据隔离的方案实现、PostgresSQL数据库的使用，还有微服务之间的数据交换，网关服务的统一处理，以及复杂系统的职责领域的划分。

页面效果：

![image.png](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/155c93a22d140d983a5694e48c9da8cf_MD5.webp)

## 7 商城微服务系统

susan\_mall\_cloud是微服务项目。

使用了目前业界比较新的技术：JDK17、Spring6、 [SpringBoot3.3.5、SpringCloud2024、SpringCloud](http://springboot3.3.xn--5springcloud2024springcloud-371zpa/) [Alibaba2023.0.1.0。](http://Alibaba2023.0.1.0。)

微服务后端包含了：

- susan-mall-common （公共文件）
- susan-mall-gateway （网关服务）
- susan-mall-basic (基础服务)
- susan-mall-auth （权限服务，包含用户和权限相关的）
- susan-mall-product （商品服务）
- susan-mall-order （订单服务）
- susan-mall-pay （支付服务）
- susan-mall-member （会员服务）
- susan-mall-marketing （营销服务）
- susan-mall-admin（后台管理系统API）
- susan-mall-mobile（移动端API）

这个版本在商城已有技术基础之上，又增加了：SpringCloud Gateway、WebFlux、Seata、Skywaking、OpenFeign、Loadbalancer、Sentinel、Nacos、Canal、xxl-job、Prometheus、K8S等。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/b57537701ad5624972324df148db2b65_MD5.webp)

项目架构图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/164c5f605e51141d9939cb3d84682ce1_MD5.webp)

目前包含了多端代码：

1. 服务端的网关服务和6个微服务。
2. 后台管理系统。
3. uniapp小程序。

下面是商城小程序真实的截图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/921c8a716c6c8fca513db84c7101682e_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/c1f1a68d925327b2f9a41c96aae9e652_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/a36714272d430ecb6f9c3ba3ab2d9eef_MD5.webp)

看起来是不是非常专业？

商城微服务项目很复杂，包含了目前业界微服务分布式系统中使用最主流的技术，强烈推荐一下。

无论在工作中，还是面试中，都可以作为加分项。

特别是SpringCloud Gateway中WebFlux的使用，微服务之间的异常处理，以及微服务之间的通信，都很值得一看。

扫描下方二维码即可加入星球（今天前10名有优惠）：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价159，今天券后仅需129，后面会逐步涨到299。

只有 10 张优惠券，数量有限，先到先得。

如果不满意3天内包退。

## 8 商城系统

商城系统目前包含了：SpringBoot后端 + Vue管理后台 + uniapp小程序 ，三个端的完整代码。

商城项目中包含了：基于Docker部署教程、域名解析教程、按环境隔离、网络爬虫、推荐算法、支付宝支付、分库分表、分片算法优化、手写动态定时任务、手写通用分页组件、JWT登录验证、数据脱敏、动态workId、hanlp敏感词校验，手写分布式ID生成器、分布式限流、手写Mybatis插件、两级缓存提升性能、MQ消息通信、ES商品搜索、OSS服务对接、失败自动重试机制、接口幂等性处理、百万数据excel导出、WebSocket消息推送、用户异地登录检测、freemarker模版邮件发送、代码生成工具、重复请求自动拦截、自定义金额校验注解等等一系列功能。

使用的技术：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7b0fcfa217406d599f0b7e26c93c649c_MD5.webp)

功能亮点：

商城项目无论是毕业设计，还是面试，还是实际工作中，都非常值得一看。

商城项目使用了目前非常主流的技术，手写了很多底层的代码，设计模式、自定义了很多拦截器、过滤器、转换器、监听器等，很多代码可以搬到实际的工作中。

目前星球中包含了商城项目从0~1的完整开发教程，小白也可以直接上手。

星球中有些小伙伴，通过这个项目拿到了非常不错的offer。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7cf0dad97c6aa8ecc58b3f2014646838_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/028b14981c46f0790d0128c211e40b82_MD5.webp)

扫描下方二维码即可加入星球（今天前10名有优惠）：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价159，今天券后仅需129，后面会逐步涨到299。

只有 10 张优惠券，数量有限，先到先得。

如果不满意3天内包退。

## 9 秒杀系统

苏三的秒杀系统是专门为高并发而生的。

目前使用的技术有：SpringBoot、Redis、Redission、lua、RocketMQ、ElasticSearch、JWT、freemarker、themelaf、html、vue、element-ui等。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/a69c22c6f5099cd1a7991c25fa512794_MD5.webp)

涉及到了高并发的多种技术，特别是对页面静态化，倒计时、秒杀按钮控制、预扣库存、分布式锁、MQ处理、数据一致性等，会有比较大的收获。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/96b387674c8ee0542b70d62be43ef4e8_MD5.webp)

可以帮你增加高并发的工作经验，也可以写到你的简历中。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9a638699c23a4c7dbf8764719495eb8f_MD5.webp)

秒杀系统在面试或者工作中，会经常遇到，非常有参考价值。

## 10 苏三的demo项目

这个项目包含了一些工作中常用的技术点，有很多非常有参考价值的示例。

涵盖：Spring、Mybatis、多线程、事务、常用工具、设计模式、http请求、lamda、io、excel、泛型、注解等多个方面。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/f276921ae8430666e3d1c53130c2ba49_MD5.webp)

本项目的宗旨是分享实际工作中，非常实用的代码技巧，能够让你写出更优雅高效的代码。

此外，后面会收录一下面试中，尤其是笔试中经常会被问题到的代码片段和算法。

## 11 代码生成器项目

这是一个基于Spring Boot的智能代码生成器，能够根据数据库表结构自动生成完整的Java Web项目代码，极大提升开发效率，让开发者专注于业务逻辑而非重复的CRUD代码编写。

我们用这个代码生成器，可以通过数据库表，一键直接生成controller、service、mapper、entity、菜单sql、vue页面等。

使用的技术：SpringBoot、MyBatis、Apache Velocity、Swagger2、Lombok、Druid、Maven等。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/b9288213a14592de6b6795dbf6a1fb1d_MD5.webp)

![image.png](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/03234b47f31fd43b248d8cb73df18009_MD5.webp)

### 代码生成器的优势：

**1.极速开发**

- 10倍效率提升 ：原本需要几小时的CRUD代码编写，现在只需几分钟
- 零错误率 ：模板化生成，避免手工编码错误
- 标准化输出 ：确保代码风格统一，便于团队协作

**2.高度可定制**

- 灵活的模板系统 ：基于Velocity模板引擎，可自定义生成规则
- 可配置参数 ：支持作者信息、包名、表前缀等个性化配置
- 扩展性强 ：可轻松添加新的代码模板

**3.企业级特性**

- 完整的分层架构 ：严格按照MVC模式生成代码
- 统一异常处理 ：内置错误处理机制
- API文档自动化 ：集成Swagger，自动生成接口文档
- 数据验证 ：支持参数校验和业务规则验证

**4.现代化开发体验**

- RESTful设计 ：生成符合REST规范的API接口
- JSON数据交互 ：现代化的数据交换格式
- 分页查询内置 ：开箱即用的分页功能
- 响应式设计 ：支持前后端分离架构

在实际工作中，非常有价值。

## 12 刷题吧小程序

IT刷题吧是我用AI花了几天时间，设计和开发了一款小程序。

使用技术：JDK17、SpringBoot、MyBatis、MySQL、Redis、MongoDB、MinIO、JWT、Spring Security、Knife4j、HuTool、阿里云短信服务、邮件服务等。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7da17f9ea8cdd113390c8f1159350498_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/5fcf40d1afd1061aa303c38720c12f34_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/661ecd056985fc356785340fb99bd1de_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/64a2dc1568095cf22acd659ab33f593d_MD5.webp)

为了帮助大家能够快速的掌握使用AI开发项目的技巧，提升开发效率，能够先人一步，变成全栈工程师。

你可以是产品经理，可以是UI设计师，可以是运营，可以是前端工程师，可以是后端工程师，可以是运维，也可以是DBA。

无论是自己接私活，还是开发公司的项目，都能够用更少的时间，写出更多，更有价值的代码。

苏三在知识星球中给小伙伴们，通过IT刷题吧项目，专门开设了一个AI开发课程。

你看完之后，会发现打开了一扇通向新世界的大门。（有很多惊喜）

这个课程会包含如下内容：

- 如何用AI设计产品原型的？
- 如何用AI生成小程序端和后端的代码结构的？
- 如何用AI生成后端的表结构？
- 如何用AI生成小程序和后端代码？
- 如何生成一套完整的可运行的代码？
- 如何基于图片生成想要的代码？
- 如何搞定小程序页面中的图片问题？
- 如何让小程序端和后端代码调通？
- 生成的代码不理想怎么办？
- 如果在开发过程中遇到了一些问题，用AI如何解决问题？
- 如何生成测试数据？
- 如何制定代码开发规范？
- AI开发工具的使用方法
- AI开发工具卡顿怎么办？
- 如何运行项目？
- 如何上线部署项目？ 等等。。。

星球中会交付如下内容：

1. IT刷题吧小程序
2. SpringBoot后端代码
3. 用AI开发项目的完整教程
4. 技术答疑

目前这个项目已经全部开发完。

使用AI开发这个项目，从0~1的开发和部署教程。

通过这个项目，你可以学到使用AI开发项目的具体方法。

如果你掌握了这些方法，开发其他的小程序绰绰有余。

这个项目有极大的价值。

授人予鱼，不如授人以渔。

光是学会这个项目，就值回门票了。

## 13.智能商品推荐AI Agent系统

### 项目描述

**智能推荐与交易助手（Smart Recommendation Assistant）** 是一个面向电商/零售场景的对话式导购与交易协同系统。

项目以“一个对话入口”串联完整交易链路：从 **商品咨询、智能推荐、购物车操作、订单确认、下单、订单查询、取消订单、确认收货、评价查看与提交** ，实现“推荐可解释、操作可执行、结果可追踪”的闭环体验。

系统采用 **RAG（检索增强生成）+ Function Calling（工具调用）+ MCP** 的组合架构：

- 对“需要理解和推荐”的问题使用 RAG 提升回答相关性与解释性；
- 对“需要真实数据与业务动作”的问题走工具调用与后端服务，确保结果可落地、可回写。

同时，项目支持通过 **Feign + 网关** 无缝接入现有商品/购物车/订单服务，并提供会话历史与关键 UI 快照能力（订单卡片、购物车卡片、确认单卡片等），适配真实生产场景中的复杂交互与服务波动。

### 核心功能

- **智能推荐（RAG）** ：结合向量检索补全上下文，输出可解释的推荐理由、对比建议与场景化方案。
- **对话式购物车操作（Function Calling）** ：支持加购、改数量、删商品、查购物车，兼容“第几个/商品ID/条目ID”等输入方式。
- **对话式下单闭环** ：支持从“购物车已选商品”发起订单确认与下单，并在对话中回显结果。
- **对话式订单查询（多关键字）** ：支持按订单号/商品名/状态等组合筛选，适配真实用户自然表达。
- **订单全链路操作** ：支持取消订单、确认收货、提交评价、查看评价（含聊天入口与详情页入口双通道）。
- **订单列表与详情页** ：可视化展示状态、金额、时间、商品明细，支持一键操作与状态联动刷新。
- 支付能力接入：支持订单详情/聊天入口发起支付，提供支付页跳转与支付结果回写（已支付状态更新）
- **会话历史与快照恢复** ：保存聊天记录及关键卡片快照，刷新或服务波动后仍能恢复主要上下文与展示内容。

### 技术栈

- **语言与框架** ：Java 21、Spring Boot [3.x、Spring](http://3.xn--xspring-yo3f/) Web、Thymeleaf
- **AI 能力** ：Spring AI（Chat + Tools/Function Calling）、Embedding
- **检索与向量库** ：PostgreSQL + pgvector
- **服务集成** ：Spring Cloud OpenFeign、网关透传
- **数据与存储** ：PostgreSQL、Redis、MongoDB（聊天历史与快照）
- **构建测试** ：Maven、JUnit 5
- **日志观测** ：SLF4J + Logback（可扩展链路追踪与指标）

### 技术亮点

- **RAG + 工具调用双通道架构** ：将“智能回答”与“业务执行”解耦，显著降低幻觉并提升结果可信度。
- **对话即工作流** ：将购物车、确认单、订单详情等中间态卡片化嵌入对话，减少页面跳转和流程中断。
- **多关键字稳健查询** ：兼容空格/逗号等分隔输入，贴合真实用户习惯。
- **外部接口兼容策略** ：对订单相关接口提供多参数形态与请求方式兼容（路径/query/body），提升对接成功率。
- **快照与降级兜底机制** ：服务抖动时尽量保证“用户已看到的数据不丢失”，提升体验稳定性。
- **状态一致性治理** ：通过状态映射与前后端联动修正，避免订单状态误判（如“待评价/已评价”混淆）。

部分功能截图：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/67f16ff316a919f5ce4776cef0814aeb_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/bdd7a46816762b1bc783cd7a21efe2fb_MD5.jpg)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/026d2ef4afb7146ad539c051b0e3a1ac_MD5.jpg)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/027b3d696e71ecbe190c6a84e0466239_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/251119142ff6ad15820e4f57a9c8e4cf_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/6bf0f6e087923d0f53800675088c743c_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/e8b8a9baabd484b40998af4f7b3e6351_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9406e0700948de378d4f76167678f43f_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/30ab87c673c63345f3691c242492405f_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/3b29c1897ed276dcf61b1a3dd00eff06_MD5.png)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/bbf2763171f91f6299d1b5b338468c3a_MD5.png)

## 如何加入星球？

扫描下方二维码即可加入星球：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价159，今天券后仅需129，后面会逐步涨到299。

加入星球可以获取这13个项目的代码，和非常详细的教程，还能获得技术答疑。

如果不满意3天内包退。

说句实话，我光是卖代码，一个项目就可以卖100，13个项目可以卖1300了。

今天的129，简直是白菜价。

后面会逐步涨到299。

加入星球后，你可以跟着文档，从0~1开发项目。

也可以直接运行这些项目。

其实，星球中不光有这13个实战项目，还有很多其他的干货内容。

最近两年多的时间，我将这些年开发和架构道路上，总结的一些经验、问题定位和教训，沉淀到了知识星球：Java突击队 中，可以说干货满满。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/b0ee7e0d953846591b20d1e3f334f2e8_MD5.webp)

还有1V1答疑、修改简历、职业规划、送书活动、技术交流。

最近星球得到了许多小伙伴的好评：

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/73e04f5b1ac34e938c9246201fd5f12e_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/79fdaf5fb5d065c159ae936afd3d2be1_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/df0615567da5b7f456941384e58cc571_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/0a2f2d208fe81d8b0b83e380e9f16835_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/4ab78386aa3cae855a54d4f9d946dbba_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/3cf0be3f1c2e2abd86737e9aef40a9f0_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/2d2bf9da2071f18acafbf32bf2d8211e_MD5.webp)

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9f77676ab1b4132827c12563ff891b57_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/c4f6b0330d8b264a9b7eb1afd262b46d_MD5.webp)

星球中你可以开阔一下视野，跟一群优秀的人一起交流和学习，如果工作中有些难题也有人给你出谋划策，这个价格超值！

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/59fab5708285ad415872bdf248d19ffd_MD5.webp)

说实话129元这个价格已经非常便宜了，可能就是一顿饭钱。

这100多块钱可能是2026年你花的最值的一次钱。

我相信知识星球回馈给你的，将来是十倍或者百倍的价值。

最近苏三星球的口碑越来越好了，我听到最多的反馈是：项目很棒、项目含金量高、良心价格、性价比很高、干货满满、学到很多东西、后悔没有早点加入。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/15ff2718c0e95a4d0544bc2804ef3ed4_MD5.png)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/c444ae8076ab0d44967dc641824d251e_MD5.png)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/255dd31effff5d795d2b659a5a8595fe_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/19ae266d07a14ce11314d9424d5f4e1f_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/719948d60e67b072ca3ccbaab0278f0e_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/9e0ccd8b8cdf3acf30b6e71bd5a17bef_MD5.webp)![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/7b4fbbf8a6baadf5f5fa4f391122a269_MD5.webp)

很多在观望的小伙伴，不妨抱着试看3天，然后申请全额退款的心态，加入星球看看。

里面的干货内容也许会远超出你的预期。

今天扫描下方二维码加入星球，能够立减30元（前10名有效）。

![图片](assets/%E6%8E%A8%E8%8D%905%E4%B8%AA%E7%89%9B%E9%80%BC%E7%9A%84AI%20Agent%E9%A1%B9%E7%9B%AE/740a9a38ccfeaf055d63af6b0f068d7c_MD5.png)

原价：159，今天券后仅需：129。

只有 10 张优惠券，数量有限先到先得。

我相信这100多块钱，是你2026年花的最值的一次。

随着星球里面干货越来越多，后面会逐步涨价到299，现在加入是非常合适的。

加入星球如果不满意3天内包退。