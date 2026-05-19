---
title: "LangChain4j"
type: entity
tags: [AI框架, Java, LLM]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md]
last_updated: 2026-05-19
---

## 定义
Java 世界首款成熟的 LLM 应用框架，灵感来自 Python LangChain 但非简单翻译，充分尊重 Java 工程习惯（强类型、注解驱动、依赖注入），提供统一的、面向对象的、Java 味十足的 API。

## 关键信息

### 核心抽象七大件
1. **ChatLanguageModel**：所有对话的起点，统一接口抹平模型差异
2. **AI Services**：声明式"魔法"，接口描述需求，框架生成实现
3. **ChatMemory**：让模型拥有上下文，滑动窗口/Token 窗口策略
4. **Tools / Function Calling**：用 @Tool 注解声明方法，框架自动完成 JSON Schema 生成→模型调用→反射执行→结果回传
5. **RAG**：DocumentLoader→DocumentSplitter→EmbeddingModel→EmbeddingStore→ContentRetriever
6. **Streaming**：StreamingChatLanguageModel + StreamingResponseHandler
7. **结构化输出**：根据返回类型自动生成 JSON Schema 并反序列化

### 分层架构
- **应用层**：聊天机器人、RAG 问答、Agent、文档总结、代码助手
- **高级 API 层**：AI Services 声明式描述
- **核心抽象层**：ChatLanguageModel、EmbeddingModel、ChatMemory、ContentRetriever 等
- **集成层**：LLM 适配器、向量库适配器、工具适配器
- **基础设施层**：HTTP Client、JSON、重试熔断、可观测性、Spring/Quarkus Starter

### 适合场景
1. 企业内部智能问答/知识库
2. 客服/营销对话机器人
3. 业务系统 AI 小能手
4. Agent/Copilot 类应用

### 工程化建议
- Prompt 与代码分离
- 对 LLM 调用做幂等与重试
- 可观测性（Micrometer + OpenTelemetry）
- 内容审查与越狱防御
- 模型选型做成配置
- RAG 关键在切分策略

## 关联连接
- [[摘要-LangChain4j-Java-AI智能体开发]] — 来源
- [[SpringBoot]] — 集成框架
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 工具调用
- [[ChatMemory]] — 对话记忆
- [[AIService]] — 声明式 AI 接口
