---
title: "Scouting-First"
type: concept
tags: [策略, 代码库理解, FastCode]
sources: ["raw/01-articles/比 Claude Code 快4倍、消耗节省接近一半！港大开源的代码库理解神器.md"]
last_updated: 2026-07-20
---

## 定义

侦察优先（Scouting-First）是 FastCode 代码库理解框架的核心策略——先摸清代码库的地形（构建语义地图和结构关系图），再精准出击加载目标代码，而非像传统做法满仓库翻文件。

## 关键信息

与传统的"提问→加载文件→搜索→再加载→回答"循环不同，Scouting-First 的流程是"提问→构建语义地图→结构导航→精准加载目标代码→回答"。核心在于通过分层 AST 解析建立索引、混合检索（语义向量+BM25）定位相关文件、关系图谱（调用/依赖/继承）辅助导航，以及预算感知决策动态控制挖掘深度。

## 关联连接
- [[FastCode]] — 实现该策略的框架
- [[摘要-fastcode-hkuds-codebase-understanding]] — 来源
- [[AgenticSearch]] — 同类搜索策略
