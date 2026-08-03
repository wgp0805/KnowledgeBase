---
title: "手搓 Agent 完整指南"
type: synthesis
tags: [agent, react-loop, tutorial]
sources:
  - wiki/concepts/Agent.md
  - wiki/concepts/ReAct_Agent.md
  - wiki/sources/摘要-构建你的第一个Tool-Agent-从零理解ReAct循环.md
  - wiki/sources/摘要-agent-tools-workflow区别.md
last_updated: 2026-07-22
---

# 手搓 Agent 完整指南

## 核心本质：ReAct 循环

手搓 Agent 的本质是实现 **ReAct（Reasoning + Acting）循环**——一个让 LLM 自主驱动的闭环：**指令 → 思考（Think）→ 行动（Act）→ 观察（Observe）→ 再思考...直到任务完成**。[Agent] 与 [Workflow] 的关键区别在于：Workflow 是"直线"（人预编排），Agent 是"圆环"（LLM 自主决策）。[[Agent]]

## 最小实现结构

使用 [LangGraph] 框架只需 **2 个节点 + 1 条条件边**：

```
agent_node → tools_node → (条件边)
                              ├─ 有 tool_calls → 回 agent_node（继续循环）
                              └─ 无 tool_calls → 结束（返回最终答案）
```

核心伪代码：

```python
messages = [user_query]
while True:
    response = llm.invoke(messages, tools=tool_list)
    if not response.tool_calls:
        return response.content  # ✅ 任务完成，结束循环
    for tc in response.tool_calls:
        result = execute_tool(tc)
        messages.append(ToolMessage(result, tool_call_id=tc.id))
    #   ↑ ⚠️ 这行最关键：ToolMessage 必须写回 messages
```

[[ReAct_Agent]]

## 两个必踩的坑

1. **Agent "失忆"**：`ToolMessage` 未追加到 `messages` → LLM 不知道工具执行结果 → 无限次重复调用同一工具。[[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]]
2. **无限循环**：缺少安全阀。必须设置：
   - 业务层：`MAX_ITERATIONS`（如 10 次）
   - 框架层：`recursion_limit`（LangGraph 内置）

## 何时应该手搓

[Anthropic] 的《Building Effective Agents》选型原则：**能用 Workflow 就别上 Agent**。[Workflow] 是开发者预编排的固定路径，LLM 只执行单步不决定走向；[Agent] 是 LLM 自主决策的循环系统，只有"LLM 自主决策 + 循环执行"同时成立才叫 Agent。[[摘要-agent-tools-workflow区别]]

适用场景判断：
- 简单工具调用 → 用 [FunctionCalling] 就够了
- 固定多步流程 → 用 [ToolPipeline]（串行/并行批量编排，比 ReAct 省 Token）
- 需要 LLM 自主决策何时调什么工具 → 手搓 ReAct Agent

## 关联连接

- [[Agent]] — AI Agent 核心概念
- [[ReAct_Agent]] — ReAct 循环详解
- [[ToolPipeline]] — ReAct 的批量替代方案
- [[LangGraph]] — 图式 Agent 编排框架
- [[LangGraph4j]] — Java 版 LangGraph
- [[FunctionCalling]] — LLM 工具调用能力
- [[AgentHarness]] — Agent 运行与测试框架
- [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]] — LangGraph 手写教程来源
- [[摘要-agent-tools-workflow区别]] — Tools/Workflow/Agent 选型来源
