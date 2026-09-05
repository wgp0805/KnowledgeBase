---
title: "ReActAgent"
type: concept
tags: [AI概念, Agent模式, 推理循环]
sources: [raw/09-archive/AgentScopeJava2.0正式发布了！.md, raw/09-archive/AgentScope入门指南.md]
last_updated: 2026-07-22
---

## 定义
ReActAgent 是 AgentScope Java 2.0 中的核心推理循环 Agent，实现"思考→调用工具→观察结果→继续思考"的 ReAct 范式。它是框架真正的"发动机"，负责解决"一次请求→推理→工具→回复"这个最基础的智能体能力。

## 关键信息
- **ReAct 范式** — 让智能体交替进行推理和行动，通过"思考-行动-观察"循环完成任务
- **核心定位** — AgentScope 1.x 核心类的完整保留，是 2.0 架构的基础
- **特点** — 轻量级、专注于推理循环，不包含长期运行的工程能力
- **与 HarnessAgent 的关系** — HarnessAgent 是 ReActAgent 的"薄包装"，在 ReActAgent 之上添加工作区、Session、记忆、压缩、子 Agent、沙箱、技能、Plan Mode 等能力
- **类比** — ReActAgent 是发动机，HarnessAgent 是给这台发动机配了油箱、轮胎、刹车片和仪表盘的整车
- **适用场景** — 轻量级、单次对话、不需要持久化状态的场景
- **实践建议** — 大部分场景直接用 HarnessAgent，虽然多了一些配置但这些工程能力在生产环境中几乎是必需的

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[HarnessAgent]] — 上层封装 Agent
- [[Agent]] — AI Agent 核心概念
- [[摘要-AgentScopeJava2.0发布]] — 来源
- [[摘要-AgentScope入门指南]] — 来源（苏三入门实战指南）
