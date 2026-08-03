---
title: "摘要-okf"
type: source
tags: [来源, OKF, 知识标准, 知识库]
sources:
  - raw/01-articles/2026-08-02-AI 时代的“HTML 时刻”：一个被严重低估的知识标准 OKF - 贾克斯的平行世界.md
last_updated: 2026-08-03
---

## 核心摘要
- 2026 年 6 月 Google Cloud 发布 **Open Knowledge Format（OKF）**，把「LLM Wiki」模式正式定义为一种开放、厂商中立、可移植的知识格式；2026-08 前后更新到 V0.2，加入来源、验证、时效性和可信度机制。
- 分层定位：模型负责「能不能思考」，MCP 负责「能连接什么」，Skills 负责「应该怎样做」，OKF 负责「**应该知道什么，以及这些知识是否可信**」。
- OKF Knowledge Bundle 本质上就是一个 Markdown 文件目录（index.md、log.md、metrics/、policies/ 等），每个文件代表一个独立知识概念，文件路径即身份，YAML 描述结构化信息，正文为普通 Markdown。
- 关键设计：**生产者和消费者被分开**——任何人/Agent/平台可生产 OKF，任何模型/搜索引擎/Agent 可消费 OKF，知识不再被锁在某个向量数据库/Agent 框架/模型 Memory 里。
- 与 HTML 类比：OKF 不会替代 RAG、向量数据库、搜索引擎或 Agent Runtime，它定义的是这些系统共同操作的那个「知识产物」长什么样，构建的是新时代的共识。
- 核心价值演进：从「让 Agent 能读文档」走向「让 Agent 在使用知识之前先判断这条知识是否值得相信」，逐渐接近一种**组织知识治理协议**。
- 生态：Google 提供规范/示例/工具；开源社区出现知识创建、校验、索引、可视化工具；OpenWiki 是快速采用 OKF 的上层应用（Agent 生成并持续维护相互链接的 Wiki）。
- 趋势判断：未来 Agent Harness 会被平台不断吸收，但**企业知识的定义不会**——模型是租来的、框架可替换、接口可迁移，而经过长期沉淀的、结构化、可验证、持续更新的组织知识才是企业真正属于自己的资产。

## 关联连接
- [[OKF]] — 本文介绍的标准
- [[OpenWiki]] — OKF 上层应用
- [[MCP]] — 分层对比
- [[Skill]] — 分层对比
- [[自生长知识库]] — 相关的知识组织模式
- [[LLMWiki]] — OKF 的前身模式
- [[Google]] — 标准发布方
