---
title: "Workspace"
type: concept
tags: [AI概念, 文件驱动, 架构设计]
sources: [raw/09-archive/AgentScopeJava2.0正式发布了！.md, raw/09-archive/AgentScope入门指南.md]
last_updated: 2026-07-22
---

## 定义
Workspace 是 AgentScope Java 2.0 的核心设计哲学：所有需要持久化的内容都表达为磁盘上的 Markdown/JSON 文件，而不是散落在代码或数据库表中。这种"配置即代码"的设计让 Agent 的运行时状态变成可读的普通文件。

## 关键信息
- **核心文件**：
  - workspace/AGENTS.md — 智能体的人格定义
  - workspace/MEMORY.md — 长期沉淀的"事实记忆"
  - workspace/subagents/<id>.md — 子 Agent 的声明
- **设计优势**：
  - 可审计 — 可以用 git diff 查看智能体的人格变化，整个演进轨迹清清楚楚
  - 可编辑 — 直接改 AGENTS.md 里的提示词，下一句话就生效，无需重启 JVM
  - 可迁移 — 把整个 workspace/ 目录打包，放到另一台机器上，智能体的记忆、技能、计划全部都在
  - 可组合 — 人格写在文件里，长期事实沉淀在文件中，子 Agent 也声明在文件中，一切皆文件
- **运维友好** — 运维和开发人员随时可以用自己最熟悉的工具（Vim、cat、grep）查看和修改 Agent 状态

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[HarnessAgent]] — 使用 Workspace 的 Agent
- [[多租户隔离]] — 配套安全能力
- [[摘要-AgentScopeJava2.0发布]] — 来源
- [[摘要-AgentScope入门指南]] — 来源（苏三入门实战指南）
