---
title: "摘要-spring-ai-alibaba停更分析"
type: source
tags: [来源, 原始文件, SpringAIAlibaba, Java, AI框架]
sources: ["raw/01-articles/2026-10-03 - Spring AI Alibaba已停更了，Java还有希望吗？.md"]
last_updated: 2026-10-08
---

## 核心摘要
针对"Spring AI Alibaba 停更"传闻（10.8k Star，最后一个正式版 v1.1.2.2 发布于 2026-03-10，半年无新版），苏三核查后判断：**不是弃坑，是在换心脏**——Release 停了但 main 分支没停（v1.1.2.2 后累计 137 个提交，以修复、JUnit 5 迁移等养护为主），最后一个正式版的最大特性是引入 AgentScope Java 集成（spring-ai-alibaba-starter-agentscope），官方公告明确 SAA 以 Graph 编排为核心、AgentScope 以 Agentic 为核心、两者独立发展不替代，但 AgentScope Java 四天一版 vs SAA 半年一版，资源倾斜肉眼可见。文章提出 Java AI 生态"三层台阶"：**接入层**（Spring AI 2.0、LangChain4j，活跃）、**编排层**（SAA 养护模式、Embabel 确定性规划）、**运行时层**（AgentScope 快速迭代，2026-06 发布 2.0，阿里内部十余条业务线生产使用）。选型建议：只需调模型/RAG/工具调用用 Spring AI 2.0（2026-06 GA，基于 Spring Boot 4.1 与 Spring Framework 7.0）；需要 Graph 工作流编排 SAA 仍可用但迭代慢；要 Agent 长期自主运行选 AgentScope。另有跨语言路径：旁边起 TS 运行时通过 gRPC/HTTP 调用主流 Harness。

## 关联连接
- [[SpringAI_Alibaba]] — 文章主角
- [[AgentScope_Java]] — 资源倾斜的接棒者
- [[JavaAI三层台阶]] — 文章提出的选型框架
- [[SpringAI]] — 接入层框架
- [[LangChain4j]] — 接入层框架
- [[Embabel]] — 编排层框架
- [[苏三]] — 作者
