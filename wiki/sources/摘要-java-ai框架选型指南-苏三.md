---
title: "摘要-java-ai框架选型指南-苏三"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/Java AI框架选型指南.md]
last_updated: 2026-09-18
---

## 核心摘要
苏三撰写的 Java AI 框架选型指南，将 Java 生态 AI 框架分为两层：底层基础设施层（Spring AI、LangChain4j、Solon AI）解决"怎么接入 AI"，高级应用框架层（Spring AI Alibaba、AgentScope、Embabel）解决"怎么组织 AI 干活"。Spring AI 2.0 基于 Spring Boot 4.1，明确 ChatClient/ChatModel 边界，工具执行循环提升到 Advisor 链统一处理；LangChain4j 1.19 支持 30+ 模型，MCP 协议进入稳定期；Solon AI 是唯一支持 Java 8-26 的框架；Embabel 引入 GOAP 确定性规划算法替代 LLM 驱动规划。

## 关联连接
- [[SpringAI]] — 底层基础设施框架
- [[LangChain4j]] — 底层基础设施框架
- [[SolonAI]] — 全场景框架
- [[SpringAI_Alibaba]] — Agent 编排框架
- [[AgentScope_Java]] — 企业级 Agent 框架
- [[Embabel]] — GOAP 确定性编排框架
- [[GOAP]] — 目标导向规划算法
- [[spring-ai-vs-langchain4j]] — Spring AI 与 LangChain4j 对比分析
- [[SuSan]] — 文章作者
