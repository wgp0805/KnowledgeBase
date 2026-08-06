---
title: "ReAct Agent"
type: concept
tags: [AI, Agent, 推理, 行动循环]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/2026-07-05-AI Agent 30天速成｜Day10 笔记 - 云淡风轻YangG.md, raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md]
last_updated: 2026-07-06
---

## 定义
推理+行动循环（Reasoning + Acting）的 Agent 模式，模型自主进行"思考→行动→观察结果→再思考"的迭代循环，直到完成任务。

## 关键信息
- 多个 Java AI 框架实现了 ReAct Agent：Spring AI Alibaba（ReactAgent）、Solon AI（ReActAgent）、AgentScope-Java（HarnessAgent）
- ReAct 范式是 Agent 工程中最基础的自主推理模式
- 与 Pure Agent（模型完全自主决策）和 Workflow（预定义编排流程）并列为主流 Agent 模式

### 完整 ReAct 流程（以 PaiCLI 为例）
1. **输入预处理**：展开本地路径、解析图片引用等
2. **长期记忆检索**：找出与当前输入相关的记忆并注入系统提示词
3. **Prompt 组装**：分层拼接，静态层（身份、人格、模式指令、审批策略）放在动态层前面，利用 Prompt Caching 按最长公共前缀命中降低 API 成本
4. **ReAct 循环主体**：
   - 检查退出条件：Token 预算是否耗尽、是否连续多次调用同样的工具、是否超过迭代上限
   - 调用 LLM 获取决策
   - 若返回 Function Calling → 执行工具（可并行多个工具）→ 执行结果作为新消息追加到对话历史 → 继续循环
   - 若未返回工具调用 → 任务完成，格式化输出并返回
5. **输出格式化**：将最终结果格式化为 HTML 返回给用户

### ReAct 的局限性
- 单次只能调用一个工具（或一轮并行），多步骤需多轮 LLM 思考，Token 消耗大
- 不适合需要全局规划的多文件重构任务。例如改 A 文件后跑测试挂了，但"挂"不是因为 A 改错了，而是 B、C、D 还没改——ReAct 看到报错可能尝试修复不该修的问题，越改越乱
- 此类场景应切换到 Plan-and-Execute 模式，先规划 DAG 任务图再按拓扑排序执行

### 与 ToolPipeline 对比
- ReAct 单次只能调用一个工具，多步骤需多轮 LLM 思考，Token 消耗大
- ToolPipeline 一次性定义串行/并行多工具步骤，模型仅一次规划，网关批量调度
- **选型建议**：无固定流程开放问题 → ReAct；流程固定标准化任务 → ToolPipeline

### 实现结构（LangGraph 视角）
在 [[LangGraph]] 中，最小 ReAct Agent 只需 **2 个节点 + 1 条条件边**：

1. **agent 节点** — LLM 推理决策，读取当前 `messages` 判断下一步
2. **tools 节点** — 执行工具，结果包装成 `ToolMessage` 写回消息链
3. **条件边** — 检查最后一条 `AIMessage` 是否包含 `tool_calls`，有则走 tools，无则结束

**消息链状态**：`messages: Annotated[list[BaseMessage], add_messages]` 使用 `add_messages` reducer 保证新消息追加而非覆盖，这是 ReAct 循环能持续转动的关键。

**双重安全阀**：
- 业务层：`tool_call_count` + `MAX_ITERATIONS` 限制工具调用次数
- 框架层：`recursion_limit` 防止 Graph 无限递归

**典型 Bug**：工具结果未以 `ToolMessage` 形式写回 `messages`，导致 Agent "失忆"——工具明明执行了，但最终回答完全没用上工具结果。

## 关联连接
- [[Agent]] — 所属核心概念
- [[SpringAI_Alibaba]] — ReactAgent 实现
- [[SolonAI]] — ReActAgent 实现
- [[AgentScope_Java]] — HarnessAgent 实现
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-ai-agent-day10-tool-pipeline]] — 来源
- [[ToolPipeline]] — 工具流水线编排对比
- [[LangGraph]] — ReAct Agent 的 Python 框架实现
- [[StateGraph]] — LangGraph 的核心状态图抽象
