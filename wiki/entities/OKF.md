---
title: "OKF"
type: entity
tags: [实体, 标准, 知识库, Google]
sources:
  - raw/09-archive/2026-08-02-AI 时代的“HTML 时刻”：一个被严重低估的知识标准 OKF - 贾克斯的平行世界.md
last_updated: 2026-08-03
---

## 定义
OKF（Open Knowledge Format，开放知识格式）是 Google Cloud 2026 年 6 月发布的知识格式标准，把「LLM Wiki」模式正式定义为开放、厂商中立、可移植的知识格式，让 Agent 能以统一接口读取并维护一个组织「知道的东西」。

## 关键信息
- **版本**：2026 年 6 月发布，V0.2 加入来源、验证、时效性和可信度机制
- **核心形态**：一个 OKF Knowledge Bundle 就是一个 Markdown 文件目录：
  ```
  company-knowledge/
  ├── index.md
  ├── log.md
  ├── metrics/
  │   ├── revenue.md
  │   └── active-users.md
  └── policies/
      └── revenue-recognition.md
  ```
- **文件约定**：每个 Markdown 文件代表一个独立知识概念（数据库表/公司政策/业务流程均可）；文件路径就是概念身份；YAML 头部描述结构化信息（type/title/description/status/sources），正文为普通 Markdown
- **生产-消费分离**：任何人、Agent、知识平台可基于该格式生产 OKF；任何模型、搜索引擎、Agent 可消费 OKF；知识不再被锁在向量数据库/Agent 框架/模型 Memory 里
- **可信度机制**：随 Agent 生成的知识越来越多，OKF 开始描述「这是什么知识、谁产生的、可信程度如何、现在是否仍然有效」，从「让 Agent 能读文档」走向「让 Agent 判断知识是否值得相信」，接近组织知识治理协议
- **与 HTML 类比**：OKF 不替代 RAG、向量数据库、搜索引擎或 Agent Runtime，只定义这些系统共同操作的知识产物长什么样
- **分层定位**：模型=能不能思考；MCP=能连接什么；Skills=应该怎样做；OKF=应该知道什么+是否可信
- **生态现状**：Google 提供规范/示例知识库/工具；开源社区出现知识创建/校验/索引/可视化工具；OpenWiki 是快速采用 OKF 的上层应用
- **趋势意义**：Harness 会被 Agent 平台不断吸收，但企业知识层会变厚；模型是租来的、框架可替换、工具接口可迁移，只有结构化、可验证、持续更新的组织知识才是企业真正的资产

## 关联连接
- [[OpenWiki]] — OKF 上层应用
- [[MCP]] — 分层对比（连接）
- [[Skill]] — 分层对比（执行）
- [[自生长知识库]] — 相关知识组织模式
- [[Google]] — 发布方
- [[RAG]] — OKF 不替代它
- [[摘要-okf]] — 来源
