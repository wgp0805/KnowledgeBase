---
title: "HarnessAgent"
type: concept
tags: [AI概念, Agent模式, 工程化]
sources: [raw/01-articles/AgentScopeJava2.0正式发布了！.md]
last_updated: 2026-06-23
---

## 定义
HarnessAgent 是 AgentScope Java 2.0 推荐的 Agent 入口，在 ReActAgent 之上的"薄包装"，把长期运行 Agent 必备的工程能力——工作区、Session、记忆、压缩、子 Agent、沙箱、技能、Plan Mode——用一个 Builder 串起来。

## 关键信息
- **推荐入口** — AgentScope 2.0 官方推荐的 Agent 创建方式
- **设计哲学** — 不重写推理循环，只是在外面包一层"壳"
- **核心职责** — 每次调用开始时绑定 RuntimeContext（告诉系统"你是谁"），并在模型报告上下文溢出时强制压缩并重试
- **扩展机制** — 所有能力都是通过 ReActAgent 已有的 Hook 扩展点注入的
- **3D 类比** — Harness 就是 ReActAgent 的"手机壳"——壳上加卡槽、支架等功能，但手机本身完全没动

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[ReActAgent]] — 底层推理 Agent
- [[Workspace]] — 工作区抽象
- [[Middleware]] — 中间件扩展机制
- [[摘要-AgentScopeJava2.0发布]] — 来源
