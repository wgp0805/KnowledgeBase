---
title: "ToolCalling"
type: concept
tags: [AI, LLM, 工具调用]
sources: ["raw/01-articles/用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅.md", "raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md"]
last_updated: 2026-11-27
---

## 定义

Tool Calling（工具调用）是 LLM 执行外部操作的核心机制——模型根据用户意图选择合适的工具（函数），生成调用参数，由框架执行后将结果回传给模型，完成"思考-行动-观察"循环。

## 关键信息

- **核心流程**：用户请求 → LLM 分析 → 选择工具 → 生成参数 → 框架执行 → 结果回传 → LLM 总结
- **与 Function Calling 关系**：Tool Calling 是 Function Calling 的演进，增加了工具选择、结果回传、多轮调用等能力
- **实现框架**：Spring AI `@Tool` 注解、LangChain4j `@Tool` 注解、Solon AI ToolCallingAdvisor
- **与 Agent 关系**：Tool Calling 是 Agent 的底层执行能力，Agent 在循环中多次调用工具完成复杂任务
- **与 HITL 结合**：通过拦截器在工具调用前插入人工审批节点

## 框架级确认机制（2026-11 进展）

上面「拦截器插审批节点」是**自己实现**的路子。到 [[SpringAI]] 2.1，这件事被提升为**框架能力**：`@Tool(requiresConfirmation = true)` 标记后，**整个工具调用循环在执行任何调用之前暂停**，应用逐条给出 `ToolCallDecision`（allow / deny+消息）再调 `ToolCallingManager.executeToolCalls(...)` 恢复。关键设计是暂停**不保留状态**（暂停=普通响应返回，恢复=普通请求发送），因此重启可恢复、多实例可接力——这正是自己写拦截器最容易写错的地方。详见 [[ToolCallConfirmation]]。

### 流式工具调用的参数增量

2.1 起，流式响应会把**参数增量**以带 partial 标记的 `ToolCallPart` 暴露出去，供 UI 实时展示「参数正在生成」。这些 partial Part 会被 `getToolCalls()` 和 `ToolCallingManager` **忽略**，随后同一个 index 的**完整调用**才到达——即「展示用增量、执行用完整」，两者不冲突。载体是 [[MessageParts]]。

### 调用上限

同一版本还加了**默认上限**：单工具每轮最多 40 次、总调用最多 150 次，可用 `spring.ai.tools.limits.*` 调整。这道闸门防的是「模型在循环里反复调同一个工具烧钱」这类失控，与确认机制互补——确认管「该不该执行」，上限管「能执行多少次」。

## 关联连接
- [[FunctionCalling]] — 工具调用的底层机制
- [[Agent]] — 工具调用的上层编排
- [[HITL]] — 工具调用前的人工审批
- [[ReActAgent]] — 思考-行动-观察循环
- [[摘要-SolonAI-ReActAgent智能客服]] — 来源
- [[ToolCallConfirmation]] — 框架级工具调用确认（2.1）
- [[MessageParts]] — 流式参数增量的消息载体
- [[SpringAI]] — 提供上述框架能力的框架
- [[摘要-spring-ai-2-1-苏三解读]] — 来源
