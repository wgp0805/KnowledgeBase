---
title: "SpringAI"
type: entity
tags: [AI框架, Spring, Java, LLM]
sources: [raw/09-archive/SpringAI.md, raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md, raw/01-articles/Spring AI 2.0真香！.md, raw/01-articles/Spring AI 2.0 和 Spring AI Alibaba，哪个更好？.md, raw/01-articles/2026-08-01-Spring之父再次出山，开发了新的AI框架！ - 苏三说技术.md]
last_updated: 2026-08-03
---

## 定义
Spring AI 是 Spring 官方推出的 AI 应用开发框架，提供统一的 API 抽象接入各类 AI 模型（OpenAI、通义千问、Ollama 等），遵循 Spring 模块化与可互换设计原则。

## 关键信息
- 版本要求：JDK 17+、Spring Boot 4.1+、Spring Framework 7.0+（Spring AI 2.0 GA 于 2026-06-12，GitHub 3.2 万+ Star）
- 核心接口：ChatClient（高级聊天客户端）、ChatModel（底层模型接口）
- 通过 OpenAI API 协议兼容模式接入 DeepSeek、通义千问等模型
- 函数调用（Function Calling）：声明 @Bean 定义 java.util.Function，注册到 ChatClient 后由模型自动调用
- 提示词模板：SystemPromptTemplate 支持占位符动态替换
- 图像模型：DashScopeImageModel 支持文生图
- 语音模型：DashScopeSpeechSynthesisModel 支持文本转语音
- RAG 支持：VectorStore + QuestionAnswerAdvisor 实现检索增强生成

### Spring AI 2.0 架构升级
- 定位：connecting enterprise Data and APIs with the AI Models，刻意不做 Agent Framework
- 构建：Spring Boot 4.1 + Spring Framework 7.0，全面采用 JSpecify 空值安全注解，升级 Jackson 3 序列化
- Tool Calling 成为一等公民：工具调用循环从各 ChatModel 剥离，统一由 ChatClient + ToolCallingAdvisor 外部处理；新增 ToolSearchToolCallingAdvisor 按需发现工具
- 结构化输出增强：自修正结构化输出（Self-Correcting Structured Output）+ EntityParamSpec
- MessageWindowChatMemory 支持按消息边界（turn-boundary）截断
- Chat Model 供应商精简：OpenAI、Anthropic、Amazon Bedrock、Google GenAI 等

### Spring AI Alibaba
- 阿里推出的独立项目（`alibaba/spring-ai-alibaba`），与 Spring Cloud Alibaba 无关
- 完整提供 Model、Prompt、RAG、Tools 等能力
- 集成通义系列模型，需申请阿里云百炼 API Key

### Skill 与 Agent 支持
Spring AI 无原生 Skill 抽象，其等价能力通过 Tool Calling 实现（@Tool 注解、FunctionToolCallback、ToolContext）。但 Tool 不具备渐进式披露能力，也没有标准化 SKILL.md 目录结构。Agent 能力相对基础，基于 ChatClient Advisors 链模式。

### Spring AI 2.0 Agent 最佳实践
Spring AI 2.0 将"工具调用循环"从各个 ChatModel 内部抽出来，统一交给 `ChatClient` + `ToolCallingAdvisor` 管理：

1. **ChatClient 是入口**：自带 Advisor 链、工具注册、流式封装，无需直接调 ChatModel
2. **@Tool 注解定义工具**：`@Tool(description = "工具描述")` 声明 Java 方法，框架自动生成 JSON Schema
3. **Advisor 链拆分职责**：MessageChatMemoryAdvisor（记忆）、QuestionAnswerAdvisor（RAG）、ToolCallingAdvisor（工具循环）、自定义 Advisor（审计/权限）
4. **ChatMemory 管理会话**：`MessageWindowChatMemory` 滑动窗口策略，配合 `MessageChatMemoryAdvisor` 自动注入
5. **System Prompt 优先**：写好角色/边界/工具规则比换模型更管用
6. **流式输出（SSE）**：`chatClient.prompt().stream().content()` 返回 Flux
7. **工具宁少勿滥**：单 Agent 控制在 5~8 个内，按场景分组注册
8. **可观测性前置**：实现 `CallAdvisor` 接口，集成 Micrometer + Prometheus + Grafana

### 模型与向量库支持
- 支持模型：OpenAI、Anthropic、DeepSeek、Google Gemini、Ollama、Amazon Bedrock、Azure OpenAI、阿里通义等 10+
- 支持向量库：PGVector、Chroma、Pinecone、Redis、Milvus、Weaviate、Elasticsearch、MongoDB Atlas、Cassandra、Qdrant、Oracle 等 15+

### 与 Embabel 的分层关系（Rod Johnson 观点）
- 比喻：**Spring AI ≈ Servlet API，Embabel ≈ Spring MVC**；「Spring AI 是零件箱，Embabel 是装配图纸+流水线」
- Spring AI 解决「怎么接入 AI 模型」（统一 ChatModel 接口、向量存储抽象、工具调用机制），但 Agent 逻辑组织、多步任务规划、流程可控需自己写代码
- Embabel 解决「怎么让 AI Agent 在企业系统里稳定工作」，提供 Action/Goal/Condition 等完整 Agent 编程模型
- 决策方式差异：Spring AI 命令式（开发者手动编排 ReAct 循环，每次决策都调 LLM）；Embabel 声明式（GOAP 引擎运行时动态计算最优路径，规划 0 Token，省 40-60% LLM 调用）

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
- [[摘要-spring-ai-2-agent-tips]] — 来源
- [[AdvisorChain]] — Advisor 链模式
- [[摘要-spring-ai-2-对话记忆实战]] — Spring AI 2.0 对话记忆实战
- [[摘要-spring-ai-2-vs-alibaba选型]] — Spring AI 2.0 vs Alibaba 选型
- [[Embabel]] — 上层 Agent 编程模型（Rod Johnson）
- [[摘要-embabel]] — 来源（Embabel 对比）
