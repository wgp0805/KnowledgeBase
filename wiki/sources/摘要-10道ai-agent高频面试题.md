---
title: "摘要-10道ai-agent高频面试题"
type: source
tags: [来源, 原始文件, AI Agent, 面试题, 技术]
sources: [raw/09-archive/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md]
last_updated: 2026-09-20
---

## 核心摘要
万字详解 10 道 AI Agent 高频面试题，每题配图解、代码示例和总结。Q1 AI Agent 与普通 LLM 应用本质区别（自主决策/目标驱动/循环闭环，循环是被自回归生成机制逼出来的）；Q2 什么时候用 Workflow/单 Agent/多 Agent（路径写得死用 Workflow，写不死上单 Agent，拆多 Agent 看能不能多出新信息）；Q3 ReAct/CoT/Plan-and-Execute/Self-Refine 怎么选（CoT 管想、ReAct 加做、Plan 先想全局、Refine 做完再审，生产混着用）；Q4 Function Calling 完整流程（模型只做决策不执行，Pydantic 参数校验）；Q5 MCP 与 Function Calling 关系（正交，工具形态/接入协议/路由策略三个独立维度）；Q6 工具调用失败容错与防无限循环（解析失败/超时/数据太大，四道防线）；Q7 短期/长期记忆、知识库、日志区分（判断是不是记忆就看会不会被语义检索影响决策）；Q8 上下文满了怎么办（溢出 vs 腐化，隔离优于压缩，KV Cache 三铁律）；Q9 RAG 完整链路与检索优化（混合检索+RRF+Rerank+Agentic RAG）；Q10 怎么评估 Agent（Pass@k vs Pass^k，失败归因归首个错误且归对层）。

## 关联连接
- [[Agent]] — 核心概念
- [[Workflow]] — 概念
- [[单Agent]] — 概念
- [[多Agent]] — 概念
- [[ReAct]] — 范式
- [[CoT]] — 范式
- [[Plan-and-Execute]] — 范式
- [[Self-Refine]] — 范式
- [[FunctionCalling]] — 工具调用
- [[MCP]] — 协议
- [[工具路由]] — 概念
- [[KV Cache]] — 成本优化
- [[上下文溢出]] — 概念
- [[ContextRot]] — 概念
- [[RAG]] — 检索增强生成
- [[混合检索]] — 检索优化
- [[RRF]] — 融合算法
- [[Rerank]] — 重排
- [[AgenticRAG]] — 智能体化 RAG
- [[Pass@k]] — 评估指标
- [[Pass^k]] — 评估指标
- [[楼仔]] — 作者