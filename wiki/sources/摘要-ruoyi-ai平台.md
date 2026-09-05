---
title: "摘要-ruoyi-ai平台"
type: source
tags: [Java, AI, RuoYi, SpringAI, Langchain4j, RAG, 开源, 简历项目]
sources: [raw/01-articles/RuoYi 全栈 AI 平台开源了（若依）。.md]
last_updated: 2026-08-13
---

## 核心摘要
[[RuoYiAI]] 是基于 [[RuoYi-Vue-Plus]] 扩展的开源全栈 AI 平台，技术栈 Spring Boot 3.4 + [[SpringAI]] + [[LangChain4j]]，深度集成 FastGPT / 扣子 / DIFY 三大平台。本地可跑 [[RAG]]、知识图谱、数字人、AI 流程编排、Agent Skills、自然语言生成图表。作者 [[沉默王二]]，v3.0.0 分支新增 AI 流程编排与 Agent Skills。

## 关键信息
- **RAG 方案**：Langchain4j + BGE-large-zh-v1.5 中文向量模型，纯 Java 实现；对比派聪明 RAG（用 ElasticSearch 向量）体感更粗，因若依涉及面广难专精
- **统一聊天服务**：FastGPT/扣子/DIFY 三平台无缝切换 + 负载均衡
- **MCP 协议**：集成 Spring AI MCP，动态接入 OpenAI/通义千问/智谱 AI
- **Agent Skills**：工具注册/参数解析/结果回调完整链路；本质是提示词 + [[渐进式披露]]，按需加载
- **简历价值**：Java 开发者 AI 应用落地参考，可作为企业级 AI 智能助手平台项目经验
- **作者观点**：Java 在 AI 时代是参与者非旁观者；开源意义在降低门槛而非造完美轮子

## 关联连接
- [[RuoYiAI]] — 若依 AI 平台实体
- [[沉默王二]] — 来源作者
- [[SpringAI]] — 核心框架
- [[LangChain4j]] — RAG 实现框架
- [[RAG]] — 检索增强生成
- [[Skill]] — Agent Skills 机制
- [[渐进式披露]] — Skills 按需加载原则
- [[PaiCLI]] — 文中提及的 Agent 项目
- [[spring-ai-vs-langchain4j]] — 框架选型对比
