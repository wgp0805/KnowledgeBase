---
title: "摘要-AI编码Agent从原理到可运行代码"
type: source
tags: [AI编码Agent, ReAct, 上下文工程, FunctionCalling, CodeAct, 安全沙箱, 架构分层]
sources: [raw/01-articles/2026-08-30-AI 编码 Agent 从原理到可运行代码 - 哥不是小萝莉.md]
last_updated: 2026-08-31
---

## 核心主旨

系统讲解 AI 编码 Agent 的完整原理与生产级架构：从 ReAct 推理循环、Agent 五件套、上下文工程、Function Calling 到 CodeAct 范式，最后给出生产级架构分层设计。

## 关键信息

### ReAct 推理循环
- 思考→行动→观察→再思考的迭代循环，是 Agent 的核心运转模式
- 详见 [[ReAct_Agent]] 和 [[ReActAgent]]

### Agent 五件套
1. **大模型** — 推理引擎
2. **工具集** — 文件读写、Shell、搜索、代码执行
3. **执行循环** — ReAct 或 Plan-and-Execute
4. **记忆系统** — 短期（会话）+ 长期（跨会话）+ 项目（规则文件）
5. **上下文管理** — 窗口管理、压缩、Token 预算

### 上下文工程
- 不是"检索增强"，而是"为模型构造最合适的上下文"
- 选取、排序、压缩、冲突处理四子问题
- 详见 [[ContextEngineering]]

### Function Calling
- 模型输出结构化工具调用 JSON，由 Harness 执行
- 比"让模型输出自然语言再解析"更可靠
- 支持并行调用多个工具

### CodeAct 范式
- 模型直接输出可执行代码（Python/TypeScript），由沙箱执行
- 比 Function Calling 更灵活：模型可以写循环、条件、组合多个工具
- 代价：需要安全沙箱隔离执行环境
- 代表：[[DeepSeekHarness]] 的 PTC 模式

### 生产级架构分层
1. **接入层** — CLI/Web UI/SDK 多入口
2. **编排层** — 任务分解、子 Agent 调度、Plan-Execute
3. **执行层** — ReAct 循环、工具调用、CodeAct 沙箱
4. **基础设施层** — 记忆、上下文管理、MCP、安全沙箱
5. **可观测层** — 日志、Trace、Token 统计、成本监控

### 安全沙箱
- CodeAct 必须在隔离环境执行（Docker/microVM/WASM）
- 文件系统隔离、网络隔离、资源限制
- 危险操作白名单/黑名单 + 人机协作审批（HITL）

## 关联连接
- [[ReAct_Agent]] — 推理循环核心概念
- [[ReActAgent]] — AgentScope 实现
- [[ContextEngineering]] — 上下文工程
- [[Harness]] — 运行时概念
- [[DeepSeekHarness]] — CodeAct/PTC 模式实践
- [[ClaudeCode]] — 生产级 Harness 实现
- [[Codex]] — 云端沙箱 + 并行子 Agent
- [[摘要-生产级Agent设计]] — 生产级 Agent 11 个核心工程问题
- [[摘要-pi-agent-core-principles]] — pi-agent 核心原理
- [[摘要-复杂agent的四大体系]] — 执行/反馈/协作/记忆四大体系
- [[摘要-agent-engineering]] — Agent 工程选型与架构
