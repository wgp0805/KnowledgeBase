---
title: "AI原生测试用例工程化"
type: concept
tags: [测试, AI, Agent, 工程化]
sources: [raw/01-articles/2026-06-29-AI native Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师.md]
last_updated: 2026-06-30
---

## 定义
AI 原生测试用例工程化是一种把测试用例视为 Git 仓库中的工程资产，并让 AI Agent 负责生成、维护和重构用例，人类负责评审、判断和执行验收的方法论。

## 关键信息
- 需求文档放入 `docs/requirements/`，作为 AI 理解业务的输入。
- 测试设计方法沉淀到 `.agents/skills/`，让 AI 按测试人员思路设计用例。
- `schema/test-case-schema.json` 约束 YAML 用例结构，降低 AI 输出格式漂移。
- `releases/` 存放 YAML 用例，使其可被 Git 管理、Code Review、回滚和追踪。
- 评审标记、执行结果和报告数据独立保存，不污染用例定义。
- 人机分工是：AI Agent 负责生产，Schema 负责约束，Git 负责协作，Casebook 负责工作台，人负责质量判断。

## 关联连接
- [[摘要-casebook-ai-native-testcase-workflow]] — 来源
- [[Casebook]] — 该方法论的工具实现
- [[Agent]] — 用例生产者
- [[Skill]] — 测试设计方法载体
- [[Git]] — 工程资产协作底座
