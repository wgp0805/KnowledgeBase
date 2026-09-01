---
title: "Spring AI 应用分布：RAG 是主流，但重心正迁移到 Agent"
type: synthesis
tags: [Spring AI, RAG, Agent, 框架选型, 应用分布]
sources:
  - raw/09-archive/SpringAI.md
  - raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md
  - raw/09-archive/Spring AI 2.0 和 Spring AI Alibaba，哪个更好？.md
  - raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md
  - raw/01-articles/推荐5个牛逼的AI Agent项目.md
  - raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md
  - raw/09-archive/推荐一个牛逼的RAG+KAG双引擎系统.md
  - raw/01-articles/2026-08-23-从一次危重猫接诊，看动物医院该怎么做 RAG.md
  - raw/01-articles/2026-08-22-我花1小时劝退客户别做知识库，他反而谢我.md
  - raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md
last_updated: 2026-08-31
---

# Spring AI 应用分布：RAG 是主流，但重心正迁移到 Agent

## 核心结论

RAG 是 Spring AI **最常见、最易上手**的落地场景，但并非"唯一"或"最前沿"的应用方向。当前 Spring AI 生态的应用分布大致是：

**RAG 知识库 > ChatClient 对话 > Function Calling/Tool > Agent 编排**

且重心正在从 RAG 向 Agent 迁移。

## 一、为什么 RAG 看起来"应用最多"

1. **门槛低、价值直接**：RAG 解决的是大模型四大硬伤（幻觉、知识截止、私有知识缺失、无法溯源），企业最容易感知到痛点，也是 Spring AI 官方教程里的"综合案例"标配（见 [[摘要-spring-ai]] 的智能简历筛选助手）。
2. **Spring AI 原生支持**：`AdvisorChain` 里专门有 RAG Advisor，`VectorStore` 抽象统一了 Chroma/Neo4j/Redis 等后端，五件套（Loader/Splitter/Embeddings/VectorStore/Retriever）在 Java 侧落地成熟（[[摘要-langchain-rag构建知识库-理论]]）。
3. **项目案例集中**：苏三推荐的 5 个 Java AI Agent 项目里，有 4 个用到 RAG——企业知识库、智能代码审查、智能翻译、商品推荐（[[摘要-推荐5个AI-Agent项目]]）；RAG+KAG 双引擎系统更是典型样板（[[摘要-RAG-KAG双引擎知识库系统]]）。
4. **垂直场景持续渗透**：动物医院接诊、企业文档问答等场景都在用 RAG 落地（[[摘要-动物医院的rag落地路径]]）。

## 二、但 RAG 并非"最前沿"，重心正在迁移

1. **Spring AI 2.0 的核心升级是 Agent，不是 RAG**：Tool Calling 成为一等公民，`ToolCallingAdvisor` 统一管理工具调用循环，`ToolSearchToolCallingAdvisor` 按需发现工具——这些都不是 RAG，而是 Agent 能力（[[摘要-spring-ai-2-vs-alibaba选型]]）。苏三的九条 Agent 经验里，RAG 只是 Advisor 链的一环，更强调工具治理、记忆、可观测性（[[摘要-spring-ai-2-agent-tips]]）。
2. **多 Agent 编排才是新焦点**：Spring AI Alibaba 的 Graph 引擎、ReAct Agent、Supervisor 模式、A2A 协议，瞄准的是"编排多个 AI"，类比 LangGraph，而非 RAG（[[摘要-spring-ai-2-vs-alibaba选型]]）。
3. **RAG 本身在进化**：前沿已走向 Agentic RAG（智能体化决策）、Graph-RAG（知识图谱增强）、上下文工程，朴素 RAG 的天花板很明显（[[摘要-字节面试官什么是RAG为什么需要RAG]]）。
4. **RAG 不是银弹**：代码场景下 Claude Code 用 Agentic Search（grep+read）碾压 RAG（[[摘要-为什么Claude-Code不用RAG检索代码]]）；20 万份文档的"伪需求"知识库项目被 FDE 劝退（[[摘要-劝退客户做知识库的案例]]）。

## 三、更准确的应用分布（2026-08）

| 应用方向 | 在 Spring AI 生态的成熟度 | 典型场景 |
|---------|------------------------|---------|
| **RAG 知识库** | 最高，案例最多 | 企业文档问答、垂直领域助手 |
| **ChatClient 对话** | 高，入门首选 | 客服、对话记忆（[[摘要-spring-ai-2-对话记忆实战]]） |
| **Function Calling / Tool** | 中高，2.0 重点 | 天气播报、商品推荐、外部系统对接 |
| **Agent 编排** | 中，快速演进 | 多 Agent 协作、复杂工作流（Alibaba Graph） |

## 四、选型建议

- **只想快速接入 AI、做问答助手** → RAG 仍是首选，Spring AI 原生支持完善
- **需要调用外部系统、组合多个工具** → Function Calling / Tool，Spring AI 2.0 的重点
- **需要多 Agent 协作、复杂工作流** → Spring AI Alibaba Graph 引擎
- **代码场景的知识检索** → 慎用 RAG，Agentic Search（grep+read）可能更合适
- **海量非结构化文档** → 先做需求诊断，避免"伪需求"陷阱

## 关联连接
- [[SpringAI]] — Spring 官方 AI 应用开发框架
- [[SpringAI_Alibaba]] — 阿里多智能体编排框架
- [[RAG]] — 检索增强生成
- [[AgenticRAG]] — 智能体化 RAG 前沿趋势
- [[FunctionCalling]] — 函数调用
- [[ChatClient]] — 聊天客户端抽象
- [[AdvisorChain]] — Advisor 链模式
- [[摘要-spring-ai]] — Spring AI 框架完整教程
- [[摘要-spring-ai-2-agent-tips]] — Spring AI 2.0 开发 Agent 九条经验
- [[摘要-spring-ai-2-vs-alibaba选型]] — Spring AI 2.0 vs Alibaba 选型
- [[摘要-spring-ai-2-对话记忆实战]] — Spring AI 2.0 对话记忆实战
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — RAG 深度解析
- [[摘要-推荐5个AI-Agent项目]] — 5 个 Java AI Agent 项目推荐
- [[摘要-为什么Claude-Code不用RAG检索代码]] — Agentic Search 替代 RAG
- [[摘要-RAG-KAG双引擎知识库系统]] — RAG+KAG 双引擎系统
- [[摘要-动物医院的rag落地路径]] — RAG 垂直场景落地
- [[摘要-劝退客户做知识库的案例]] — RAG 伪需求识别
- [[摘要-langchain-rag构建知识库-理论]] — LangChain RAG 构建理论
