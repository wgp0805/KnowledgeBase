---
title: "子Agent编排"
type: concept
tags: [AI概念, 多智能体, 任务委派]
sources: [raw/01-articles/AgentScopeJava2.0正式发布了！.md]
last_updated: 2026-06-23
---

## 定义
子Agent编排是 AgentScope Java 2.0 的多智能体协作机制，一个智能体（主 Agent）可以"委派"任务给另一个智能体（子 Agent），并在子 Agent 完成任务后接收结果。这种模式比静态的 Pipeline 更灵活，因为子 Agent 可以在运行时动态创建和销毁，任务的委派链也是动态决定的。

## 关键信息
- **声明式子Agent配置** — 在 workspace/subagents/<id>.md 中定义子 Agent 的名称、描述和提示词
- **动态创建** — 主 Agent 通过内置的 agent_spawn 工具动态创建子 Agent
- **两种委派模式**：
  - 同步委派 — 设置 timeout_seconds > 0，主 Agent 等待子 Agent 完成后再继续
  - 后台委派 — 设置 timeout_seconds = 0，子 Agent 异步执行，完成后自动反向通知
- **历史演进** — 1.x 中的 Pipeline 和 MsgHub 模块已在 2.0 中移除，取而代之的是更强大的子 Agent 系统

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[HarnessAgent]] — 支持子 Agent 的 Agent
- [[Workspace]] — 子 Agent 声明位置
- [[摘要-AgentScopeJava2.0发布]] — 来源
