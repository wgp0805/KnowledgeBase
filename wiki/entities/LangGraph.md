---
title: "LangGraph"
type: entity
tags: [AI框架, Agent, 工作流编排, Python]
sources: [raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md, raw/01-articles/2026-08-20-LangGraph+PostgreSQL 会话记忆持久化存储 - lyshark.md, raw/01-articles/2026-08-24-LangGraph Server Agent 框架本地部署指南 - lyshark.md, raw/01-articles/LangChain、LangGraph和LlamaIndex 傻傻分不清楚？.md]
last_updated: 2026-08-28
---

## 定义
LangChain 团队推出的 AI Agent 编排框架，支持有状态图执行（Graph-based State Machine），用于构建多步骤推理循环、多 Agent 协作和复杂工作流。核心抽象是 `StateGraph` + Node + Edge + Condition。

## 关键信息
- 基于 Python，是 LangChain 生态的核心 Agent 框架
- 核心原语：**2 个节点 + 1 条条件边**就能构建完整的 ReAct Agent
  - `agent` 节点：LLM 推理决策，判断是否需要工具
  - `tools` 节点：执行工具并返回 ToolMessage
  - 条件边：检查最后一条 AIMessage 是否包含 `tool_calls`
- `create_react_agent` 是对这套循环的一行封装，内部自动构建 StateGraph、绑定工具、添加条件边
- 支持流式输出（`agent.stream(...)`）、递归限制（`recursion_limit`）、Human-in-the-Loop
- 与 [[LangGraph4j]]（Java 移植版）不同，LangGraph 是 Python 原生版

### 与其他框架的关系
- **[[LangChain]]** — 上层框架，LangGraph 是 LangChain 生态的子项目
- **[[LangGraph4j]]** — Java 移植版，概念一致但版本和生态不同
- **[[LangChain4j]]** — Java LLM 应用框架，常与 LangGraph4j 配合使用

### 记忆持久化体系
LangGraph 将记忆存储划分为两套独立体系（详见 [[AgentMemory]]）：
- **[[Checkpointer]]**（短期会话记忆）：自动写入、thread_id 隔离，实现 [[PostgresSaver]] 持久化，支持中断恢复与历史回溯
- **Store**（长期用户记忆）：手动写入、namespace+key 隔离，实现 [[PostgresStore]] 跨会话共享，支持语义检索（依赖 [[pgvector]]）
- 两套机制相互独立、数据隔离、能力互补，共同构成企业级记忆体系

### 常见陷阱
1. **无限循环**：工具返回内容模糊或 prompt 未提醒停止，需设 `MAX_ITERATIONS` + `recursion_limit` 双保险
2. **工具选错**：工具 description 重叠导致 LLM 误选，需在 docstring 中明确适用/不适用场景
3. **ToolMessage 丢失**：工具结果必须写回 messages，否则 Agent "失忆"
4. **recursion_limit 误解**：限制的是 Graph 递归步数而非工具调用次数，需维护 `tool_call_count` 业务计数器

### LangGraph Server 本地部署（2026-08，详见 [[摘要-langgraph-server-本地部署]]）
- **目标**：纯本地离线运行 LangGraph Agent，无需公网调用
- **架构**：LangGraph Server + [[llama.cpp]]（本地 GGUF 模型推理）+ [[Qwen]] 量化模型
- **配置**：.env 设置 `OPENAI_BASE_URL=http://127.0.0.1:11433/v1` + `OPENAI_API_KEY=dummy`
- **模型**：qwen2.5-1.5b-instruct-q4_k_m.gguf（Q4 量化）
- **关键参数**：`--jinja` 开启模板解析保证消息格式正确，`-c 4096` 上下文长度
- **适用场景**：本地离线 AI Agent、私有化部署、功能调试

## 关联连接
- [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]] — 来源
- [[摘要-langgraph-postgresql-会话记忆持久化]] — 来源（记忆持久化）
- [[摘要-langgraph-server-本地部署]] — 来源（本地部署）
- [[摘要-langchain-langgraph-llamaindex对比]] — 三框架对比来源
- [[llama.cpp]] — 本地推理引擎
- [[PostgresSaver]] — Checkpointer 持久化实现
- [[PostgresStore]] — Store 长期记忆实现
- [[Checkpointer]] — 检查点存储概念
- [[AgentMemory]] — 记忆系统概念
- [[LangGraph4j]] — Java 移植版
- [[LangChain]] — 所属生态
- [[LlamaIndex]] — 互补框架（数据层）
- [[ReAct_Agent]] — 核心推理模式
- [[StateGraph]] — 核心抽象
- [[Agent工作流编排]] — 所属方法论
- [[苏三]] — 对比文章作者

