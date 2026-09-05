---
title: "摘要-spring-ai-2-agent-tips"
type: source
tags: [Spring AI, Agent, 最佳实践]
sources: [raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md]
last_updated: 2026-07-06
---

## 核心摘要
Spring AI 2.0 开发 Agent 的九条实践经验：ChatClient 是统一入口，自带 Advisor 链和工具注册；ToolCallingAdvisor 统一管理工具调用循环；@Tool 注解定义工具减少样板代码；System Prompt 比换模型更管用且省钱；Advisor 链拆分职责（记忆/RAG/日志）；流式输出（SSE）尽早接上改善体验；ChatMemory + MessageChatMemoryAdvisor 管理会话记忆；工具宁少勿滥（单 Agent 5~8 个）；可观测性提前接入（Micrometer + Prometheus + Grafana）。

## 关联连接
- [[SpringAI]] — 所属框架
- [[ChatClient]] — 聊天客户端
- [[AdvisorChain]] — Advisor 链模式
- [[ChatMemory]] — 对话记忆管理
- [[RAG]] — 检索增强生成
- [[Prometheus]] — 监控系统
- [[Grafana]] — 可视化平台
