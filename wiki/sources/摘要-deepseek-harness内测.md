---
title: "摘要-deepseek-harness内测"
type: source
tags: [来源, DeepSeek, Harness, Agent, 面试]
sources: [raw/01-articles/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md]
last_updated: 2026-08-06
---

## 核心摘要

本文以"DeepSeek Harness 开始内测"为引子，通过虚构的面试问答形式，系统性讲解了 Agent 工程化的核心技术点。文章核心论点是 **Model + Harness = Agent**，Harness 负责模型之外的一切：工具调用、记忆管理、上下文控制、MCP 协议、Skills 体系等。文章以 PaiCLI 终端 Agent 为案例，深入探讨了 ReAct 循环、Plan-and-Execute 多文件重构、混合检索（KNN + BM25）、记忆三层架构（短期/长期/项目）、审批机制（HITL）、上下文压缩策略、容错与异常处理等 Agent 工程化核心议题。

## 关联连接
- [[DeepSeekHarness]] — DeepSeek 原生 Agent 框架
- [[PaiCLI]] — 案例项目的终端 Agent
- [[ReAct_Agent]] — ReAct 推理循环模式
- [[Harness]] — Model + Harness = Agent 核心概念
- [[HITL]] — 人机协作审批机制
- [[context-compression]] — 上下文压缩策略
- [[混合检索]] — KNN + BM25 混合检索技术
- [[沉默王二]] — 文章作者