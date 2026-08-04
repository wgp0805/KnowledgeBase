---
title: "摘要-pi-agent-core-principles"
type: source
tags: [AI, Agent, pi-agent, 原理]
sources: [raw/01-articles/Pi-Agent 智能体核心原理实战文档.md]
last_updated: 2026-08-04
---

## 核心摘要
智能体本质公式：**Agent = 大模型 + 工具集 + 执行循环**。通过 200 行极简 Coding Agent 代码（read_file + write_file 两个工具 + while True 循环）直观展示 Agent 核心运行机制。关键思辨：模型不调用工具时循环必须终止，否则无限消耗 Token。pi-agent 是对极简循环的工程增强版本，在其基础上叠加了最大轮次限制、上下文截断压缩、参数校验、安全拦截、错误自愈、10 个生命周期钩子等生产级能力。

## 关联连接
- [[PiAgent]] — 核心实体，本文分析对象
- [[Agent]] — 核心概念，本文给出本质公式
- [[摘要-pi-agent-production-guide]] — 同一项目的落地实战篇
- [[ReActAgent]] — ReAct 推理循环，与本文 Agent 循环一脉相承