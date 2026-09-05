---
title: "HarnessAgent"
type: concept
tags: [AI概念, Agent模式, 工程化]
sources: [raw/09-archive/AgentScopeJava2.0正式发布了！.md, raw/09-archive/AgentScope入门指南.md]
last_updated: 2026-07-22
---

## 定义
HarnessAgent 是 AgentScope Java 2.0 推荐的 Agent 入口，在 ReActAgent 之上的"薄包装"，把长期运行 Agent 必备的工程能力——工作区、Session、记忆、压缩、子 Agent、沙箱、技能、Plan Mode——用一个 Builder 串起来。

## 关键信息
- **推荐入口** — AgentScope 2.0 官方推荐的 Agent 创建方式
- **设计哲学** — 不重写推理循环，只是在外面包一层"壳"
- **核心职责** — 每次调用开始时绑定 RuntimeContext（告诉系统"你是谁"），并在模型报告上下文溢出时强制压缩并重试
- **扩展机制** — 所有能力都是通过 ReActAgent 已有的 Hook 扩展点注入的
- **3D 类比** — Harness 就是 ReActAgent 的"手机壳"——壳上加卡槽、支架等功能，但手机本身完全没动

### 工程能力一览
| 工程能力 | 说明 |
| --- | --- |
| **工作区（Workspace）** | Agent 人格、知识、技能、记忆统一沉淀在结构化工区 |
| **长期记忆（Memory）** | 跨会话记忆持久化和语义检索 |
| **会话持久化（Session）** | 对话状态自动保存，重启后无缝恢复 |
| **子 Agent 编排** | 主 Agent 委派任务给子 Agent |
| **沙箱隔离（Sandbox）** | 工具执行在隔离环境运行，保证安全 |
| **上下文压缩（Compaction）** | 长对话自动压缩，防止上下文溢出 |

### MCP 自动集成
HarnessAgent 启动时自动扫描 `workspace/tools.json` 的 `mcpServers` 段，连接每个 MCP Server，自动将 Server 暴露的工具注册到 Agent。支持 stdio（本地进程）、sse（远程 HTTP）、ws（双向 WebSocket）三种传输协议。

### 子 Agent 两种定义方式
1. **文件驱动**：在 `workspace/subagents/*.md` 中声明 `id`/`description`/`sysPrompt`
2. **Java API**：用 `SubagentDeclaration.builder()` 在代码中定义，可注入 toolkit

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[ReActAgent]] — 底层推理 Agent
- [[Workspace]] — 工作区抽象
- [[Middleware]] — 中间件扩展机制
- [[摘要-AgentScopeJava2.0发布]] — 来源
- [[摘要-AgentScope入门指南]] — 来源（苏三入门实战指南）
