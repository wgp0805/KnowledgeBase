---
title: "ToolCalling"
type: concept
tags: [AI, LLM, 工具调用]
sources: ["raw/01-articles/用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅.md"]
last_updated: 2026-07-13
---

## 定义

Tool Calling（工具调用）是 LLM 执行外部操作的核心机制——模型根据用户意图选择合适的工具（函数），生成调用参数，由框架执行后将结果回传给模型，完成"思考-行动-观察"循环。

## 关键信息

- **核心流程**：用户请求 → LLM 分析 → 选择工具 → 生成参数 → 框架执行 → 结果回传 → LLM 总结
- **与 Function Calling 关系**：Tool Calling 是 Function Calling 的演进，增加了工具选择、结果回传、多轮调用等能力
- **实现框架**：Spring AI `@Tool` 注解、LangChain4j `@Tool` 注解、Solon AI ToolCallingAdvisor
- **与 Agent 关系**：Tool Calling 是 Agent 的底层执行能力，Agent 在循环中多次调用工具完成复杂任务
- **与 HITL 结合**：通过拦截器在工具调用前插入人工审批节点

## 关联连接
- [[FunctionCalling]] — 工具调用的底层机制
- [[Agent]] — 工具调用的上层编排
- [[HITL]] — 工具调用前的人工审批
- [[ReActAgent]] — 思考-行动-观察循环
- [[摘要-SolonAI-ReActAgent智能客服]] — 来源
