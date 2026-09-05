---
title: "摘要-casebook-ai-native-testcase-workflow"
type: source
tags: [来源, AI, 测试, Agent]
sources: [raw/01-articles/2026-06-29-AI native Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师.md]
last_updated: 2026-06-30
---

## 核心摘要
Casebook 是面向 AI Agent 时代的测试用例工程化工作流，它不把 AI 当成测试平台里的“生成按钮”，而是把 AI Agent 作为测试用例资产的主要生产者。其核心做法是把需求文档、测试设计技能包、JSON Schema 和 YAML 用例放进 Git 仓库，使测试用例可以被 AI 生成和重构，也可以被 Git 审查、回滚与追踪。Casebook 本身提供本地 Web 工作台，用于浏览、评审、标记、轻量编辑、执行测试计划和生成 HTML 报告，形成“需求 → AI 生成 YAML 用例 → 本地评审执行 → 报告”的闭环。

## 关联连接
- [[Casebook]] — 面向 AI Agent 的测试用例工作台
- [[AI原生测试用例工程化]] — 该资料提出的核心方法论
- [[Agent]] — 用例生成与维护的主要执行者
- [[Skill]] — 测试设计方法以技能包形式注入 Agent
- [[Git]] — 用例资产协作、审查和回滚的底座
