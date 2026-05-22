---
title: "FunctionCalling"
type: concept
tags: [AI, 工具调用, LLM]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/SpringAI.md]
last_updated: 2026-05-19
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

### LangChain4j 实现
- 用 `@Tool` 注解声明 Java 方法
- 框架自动完成：解析方法签名→生成 JSON Schema→交给模型→拿到 function call→反射调用→结果回传→模型给最终答复
- 这是一个自动循环过程，对业务完全透明

### 与 Agent 工具的关系
Function Calling 是 Agent 工具调用的底层机制，LangChain4j 的 Tools、Claude Code 的 Skill、Codex 的插件系统都基于此模式。

## 关联连接
- [[LangChain4j]] — Function Calling 框架
- [[SpringAI]] — Spring AI 函数调用
- [[Agent]] — Agent 工具调用
- [[Skill]] — 上层技能封装
