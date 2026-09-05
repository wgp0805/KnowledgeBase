---
title: "FunctionCalling"
type: concept
tags: [AI, 工具调用, LLM]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/09-archive/SpringAI.md, raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md, raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md, raw/01-articles/美团二面：Agent、Tools、Workflow 这三个的概念和区别介绍一下？我：没接触过.md]
last_updated: 2026-07-08
---

## 定义
让 LLM 不仅回答问题还能执行操作的能力——查天气、查订单、发邮件等，通过 JSON Schema 描述可用工具，模型决定何时调用。

## 关键信息

### Spring AI 实现
Spring AI 的 Function Calling 通过 @Bean 定义 java.util.Function 实现：
- 定义一个 record 作为输入参数类型，@Description 注解描述函数用途
- 将函数作为 @Bean 注册到 Spring 容器
- 在 ChatClient 调用时通过 functions("funcName") 注册
- 模型决定调用函数时，Spring AI 自动执行并将结果回传给模型
- 核心流程：定义函数→模型交互→执行函数→返回结果

### Spring AI 2.0 增强
Spring AI 2.0 引入 `@Tool` 注解定义工具：
- `@Tool(description = "...")` 注解 Java 方法，框架自动解析方法签名生成 JSON Schema
- `@ToolParam(description = "...")` 补充参数说明，减少模型传错值
- 通过 `chatClient.prompt().tools(toolObject)` 注册
- `ToolCallingAdvisor` 统一管理工具调用循环，不再散落在各个 Model 实现中

### LangChain4j 实现
- 用 `@Tool` 注解声明 Java 方法
- 框架自动完成：解析方法签名→生成 JSON Schema→交给模型→拿到 function call→反射调用→结果回传→模型给最终答复
- 这是一个自动循环过程，对业务完全透明

### 与 Agent 工具的关系
Function Calling 是 Agent 工具调用的底层机制，LangChain4j 的 Tools、Claude Code 的 Skill、Codex 的插件系统都基于此模式。

### Tools 概念：LLM 可调用的离散函数
Tool 是 LLM 可调用的离散函数，是构建 Workflow 和 Agent 的最小能力单元。它本身没有"智能"，就是一个被动的能力插件——查数据库、调 API、读文件。至于"什么时候调、调几次、调用结果怎么处理"，那是上层 Workflow 或 Agent 的事。

**description 字段决定 LLM 能否选对工具**：Spring AI 中用 `@Tool(description = "...")` 注解描述工具用途，这个字段直接决定 LLM 能不能选对工具。写得模糊或重复，模型就会乱调。

Tool 既不是 Agent 也不是 Workflow。只有"LLM 自主决策 + 循环执行"同时成立时才叫 Agent；路径是开发者写死的 Function Calling 仍然只是 Workflow 的一部分。

## 关联连接
- [[LangChain4j]] — Function Calling 框架
- [[SpringAI]] — Spring AI 函数调用
- [[Agent]] — Agent 工具调用
- [[Skill]] — 上层技能封装
- [[摘要-langchain4j-langgraph4j-comparison]] — LangChain4j Tool Calling 对比来源
- [[摘要-spring-ai-2-agent-tips]] — 来源
- [[AI工作流]] — Tools 是 Workflow 和 Agent 的构建基础
- [[摘要-agent-tools-workflow区别]] — Tools 概念与三者关系来源
