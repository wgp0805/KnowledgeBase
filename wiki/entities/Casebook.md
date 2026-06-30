---
title: "Casebook"
type: entity
tags: [测试, AI, Agent, 工具]
sources: [raw/01-articles/2026-06-29-AI native Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师.md]
last_updated: 2026-06-30
---

## 定义
Casebook 是面向 AI Agent 时代的测试用例工程化工作台，用于把 AI 生成和维护的 YAML 测试用例转化为可本地浏览、评审、标记、执行和生成报告的工程资产。

## 关键信息
- Casebook 不定位为传统测试用例管理平台，而是围绕 Git 仓库和 AI Agent 组织测试用例资产。
- 推荐目录结构包括 `docs/requirements/`、`.agents/skills/`、`schema/test-case-schema.json`、`releases/`、`.casebook/marks.json`、`test-runs/`。
- AI Agent 负责读取需求、技能包、schema 和已有 YAML，生成、补充、删除或重构测试用例。
- Schema 负责约束 YAML 结构，降低 AI 输出漂移。
- Git 负责协作、Code Review、回滚和追踪。
- Casebook CLI 支持 `serve`、`init`、`export`、`report`、`renumber` 等命令。
- 执行结果独立保存为 `test-runs/<run-id>.json`，不会污染 YAML 用例定义。

## 关联连接
- [[摘要-casebook-ai-native-testcase-workflow]] — 来源
- [[AI原生测试用例工程化]] — Casebook 背后的方法论
- [[Agent]] — 测试用例生产者
- [[Skill]] — 测试设计技能包
- [[Git]] — 测试用例资产协作底座
