---
title: "LLMWiki"
type: concept
tags: [概念, 知识库, Wiki, Agent]
sources:
  - raw/01-articles/2026-08-02-AI 时代的“HTML 时刻”：一个被严重低估的知识标准 OKF - 贾克斯的平行世界.md
last_updated: 2026-08-03
---

## 定义
LLM Wiki 是 Andrej Karpathy 提出的一种知识库组织模式：把碎片化信息编译成结构化、高度相互链接的 Wiki 式知识库，使知识既可供人类阅读，也可供 LLM/Agent 高效读取、维护与交换。

## 关键信息
- **核心思想**：知识以「人能打开、能审查、能版本管理、能迁移的文件」形式存在，而不是锁在某个向量数据库/Agent 框架/模型 Memory 里
- **与 OKF 的关系**：OKF 把 LLM Wiki 模式正式定义成开放、厂商中立、可移植的知识格式标准；LLM Wiki 是 OKF 的前身模式
- **实践形态**：本仓库（wiki/ 编译输出层 + raw/ 不可变层）即 LLM Wiki 的具体实践
- **双向链接**：页面之间通过 [[wikilink]] 强制相互连接，杜绝孤岛页面
- **可验证性**：知识附带来源、状态、时效性，使 Agent 在使用知识前能判断是否值得相信

## 关联连接
- [[OKF]] — LLM Wiki 的正式化标准
- [[AndrejKarpathy]] — 理念提出者
- [[自生长知识库]] — 相关的知识组织模式
- [[Obsidian]] — 承载工具
- [[摘要-okf]] — 来源
