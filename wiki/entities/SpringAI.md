---
title: "SpringAI"
type: entity
tags: [AI框架, Spring, Java, LLM]
sources: [raw/01-articles/SpringAI.md, raw/01-articles/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
Spring AI 是 Spring 官方推出的 AI 应用开发框架，提供统一的 API 抽象接入各类 AI 模型（OpenAI、通义千问、Ollama 等），遵循 Spring 模块化与可互换设计原则。

## 关键信息
- 版本要求：JDK 17+、Spring Boot 3.x（最新版 2.0.0-M8，2026-05）
- 核心接口：ChatClient（高级聊天客户端）、ChatModel（底层模型接口）
- 通过 OpenAI API 协议兼容模式接入 DeepSeek、通义千问等模型
- 函数调用（Function Calling）：声明 @Bean 定义 java.util.Function，注册到 ChatClient 后由模型自动调用
- 提示词模板：SystemPromptTemplate 支持占位符动态替换
- 图像模型：DashScopeImageModel 支持文生图
- 语音模型：DashScopeSpeechSynthesisModel 支持文本转语音
- RAG 支持：VectorStore + QuestionAnswerAdvisor 实现检索增强生成

### Spring AI Alibaba
- 阿里推出的独立项目（`alibaba/spring-ai-alibaba`），与 Spring Cloud Alibaba 无关
- 完整提供 Model、Prompt、RAG、Tools 等能力
- 集成通义系列模型，需申请阿里云百炼 API Key

### Skill 与 Agent 支持
Spring AI 无原生 Skill 抽象，其等价能力通过 Tool Calling 实现（@Tool 注解、FunctionToolCallback、ToolContext）。但 Tool 不具备渐进式披露能力，也没有标准化 SKILL.md 目录结构。Agent 能力相对基础，基于 ChatClient Advisors 链模式。

### 模型与向量库支持
- 支持模型：OpenAI、Anthropic、DeepSeek、Google Gemini、Ollama、Amazon Bedrock、Azure OpenAI、阿里通义等 10+
- 支持向量库：PGVector、Chroma、Pinecone、Redis、Milvus、Weaviate、Elasticsearch、MongoDB Atlas、Cassandra、Qdrant、Oracle 等 15+

## 关联连接
- [[SpringBoot]] — 基础框架
- [[Ollama]] — 本地 LLM 部署
- [[ChatClient]] — 聊天客户端
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 函数调用
- [[LangChain4j]] — 同类框架对比
- [[SpringAI_Alibaba]] — 阿里多智能体编排框架
- [[摘要-spring-ai]] — 来源
- [[摘要-java-ai框架选型指南-2026]] — 来源
