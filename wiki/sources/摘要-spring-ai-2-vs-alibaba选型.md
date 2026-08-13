---
title: "摘要-spring-ai-2-vs-alibaba选型"
type: source
tags: [来源, Spring AI, 框架对比, 选型]
sources:
  - raw/09-archive/Spring AI 2.0 和 Spring AI Alibaba，哪个更好？.md
last_updated: 2026-07-09
---

## 核心摘要

苏三对 [[SpringAI]] 2.0 与 [[SpringAI_Alibaba]] 的全面选型对比。核心观点：两者非替代关系，而是「基础原子抽象」与「企业级编排运行时」的互补关系。Spring AI 2.0（2026-06-12 GA，基于 Spring Boot 4.1 + Spring Framework 7.0，3.2 万+ Star）定位是「接入 AI」，类比 JDBC，刻意不做 Agent Framework；Spring AI Alibaba（1.0 GA 于 2026-05-13，10k+ Star）定位是「编排多个 AI」，类比 [[LangGraph]]，核心武器是 Graph 工作流引擎。两者 API 兼容，可组合使用：Spring AI 提供标准化 ChatClient 抽象，Alibaba 提供 Graph 引擎做多 Agent 编排 + A2A + Nacos 分布式协调。

## 关键信息

### Spring AI 2.0 核心升级
- 构建：Spring Boot 4.1 + Spring Framework 7.0，JSpecify 空值安全注解，Jackson 3 序列化
- Tool Calling 成为一等公民，由 ChatClient + ToolCallingAdvisor 外部处理
- 全新 ToolCallback API + ToolSearchToolCallingAdvisor 按需发现工具
- 自修正结构化输出（Self-Correcting Structured Output）+ EntityParamSpec
- MessageWindowChatMemory 按消息边界（turn-boundary）截断
- Chat Model 供应商精简：OpenAI、Anthropic、Amazon Bedrock、Google GenAI 等

### Spring AI Alibaba Graph 引擎
- 多智能体协作：ReAct Agent、Supervisor 模式
- 可视化工作流编排：20+ 种标准组件（条件分支、并行处理、异常捕获）
- 状态管理：流程快照（故障恢复）、记忆持久化（跨会话）、人工干预节点
- 1.1.2.0（2026-02）：Agent Skills、多智能体并行执行（AllOf/AnyOf 聚合）、异步工具执行

### 选型决策
- 选 Spring AI：只需接入 AI、避免供应商锁定、追求简洁标准化、团队熟 Spring、不需复杂多 Agent
- 选 Alibaba：需多 Agent 协作、复杂工作流编排、用国产大模型、国内部署合规、需可视化开发、需 Agent 间通信
- 最佳实践：组合使用（Spring AI 底层抽象 + Alibaba Graph 编排）

## 关联连接

- [[SpringAI]] - 对比对象一
- [[SpringAI_Alibaba]] - 对比对象二
- [[苏三]] - 文章作者
- [[LangGraph]] - Alibaba 的类比
- [[LangChain]] - Spring AI 的类比
- [[DashScope]] - Alibaba 底层模型 API
- [[Qwen]] - 通义千问模型
- [[Nacos]] - A2A 分布式协调
- [[multi-agent-collaboration]] - 多 Agent 协作
- [[A2A]] - Agent 间通信
- [[FunctionCalling]] - Tool Calling
- [[ChatClient]] - 聊天客户端
- [[AdvisorChain]] - Advisor 链
- [[spring-ai-vs-langchain4j]] - 相关框架对比
- [[摘要-java-ai框架选型指南-2026]] - 相关选型指南
