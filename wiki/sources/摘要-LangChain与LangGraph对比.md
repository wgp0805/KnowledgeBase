---
title: "摘要-LangChain与LangGraph对比"
type: source
tags: [来源, AI框架, LangChain, LangGraph]
sources: ["raw/01-articles/2026-07-10-从链式调用到图式自治：LangChain与LangGraph核心差异与落地选型全解析 - 一天不进步，就是退步.md"]
last_updated: 2026-07-13
---

## 核心摘要

本文深度对比 LangChain 和 LangGraph 两大框架的核心差异。LangChain 是 LLM 应用组件工具库，适合简单线性流程；LangGraph 是面向生产环境的智能体工作流编排引擎，基于状态机、Pregel 图计算和 BSP 并行计算，支持循环迭代、动态分支、全局状态持久化。

关键差异在于：LangChain 是静态无状态的组件串联，适合固定简单流程；LangGraph 是动态有状态的图式自治编排，专为复杂自治智能体场景而生。两者是互补关系而非替代关系。

## 关联连接
- [[LangChain]] — 链式调用框架
- [[LangGraph]] — 图式编排框架
- [[StateGraph]] — 状态图概念
- [[Checkpoint]] — 检查点机制
