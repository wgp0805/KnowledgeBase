---
title: "JavaAI三层台阶"
type: concept
tags: [Java, AI框架, 选型, 架构分层]
sources: ["raw/09-archive/2026-10-03 - Spring AI Alibaba已停更了，Java还有希望吗？.md"]
last_updated: 2026-10-08
---

## 定义
Java AI 框架选型的三层能力模型：**接入层**（怎么连上模型）、**编排层**（怎么编排多个步骤）、**运行时层**（怎么让 Agent 长期稳定运行）。文章用它解释"Spring AI Alibaba 停更"风波——选框架前先搞清楚自己需要哪一层，而不是被"某个框架停更"的焦虑带偏。

## 关键信息
- **接入层**：模型接入、工具调用、向量库——[[SpringAI]] 2.0（2026-06 GA，基于 Spring Boot 4.1/Spring Framework 7.0，ChatClient API 干净、工具调用提升为 Advisor 链一等公民）与 [[LangChain4j]]（30+ 模型开箱即用），两家都活跃，无停更风险
- **编排层**：Graph 工作流、条件路由、状态持久化——[[SpringAI_Alibaba]]（进入养护模式，可用但半年一更）与 [[Embabel]]（确定性规划）
- **运行时层**：会话持久化、多租户隔离、沙箱执行、断点恢复——[[AgentScope_Java]]（2026-06 发 2.0，四天一版快速迭代，阿里十余条业务线生产使用）
- **选型口诀**：只调大模型/RAG/工具调用 → Spring AI 2.0；要 Graph 工作流编排 → SAA 仍可用但接受养护模式；要 Agent 长期自主跑 → AgentScope
- **补充路径**：主流开源 Harness 多为 TypeScript，Java 应用可旁边起 TS 运行时经 gRPC/HTTP 调用——"没必要因为业务是 Java 写的就要求 Agent 引擎也必须是 Java"

## 关联连接
- [[摘要-spring-ai-alibaba停更分析]] — 来源
- [[SpringAI_Alibaba]] — 编排层代表（养护模式）
- [[AgentScope_Java]] — 运行时层代表
- [[SpringAI]] — 接入层代表
- [[LangChain4j]] — 接入层代表
- [[Embabel]] — 编排层另一选择
