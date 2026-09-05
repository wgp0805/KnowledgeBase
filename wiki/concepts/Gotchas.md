---
title: "Gotchas"
type: concept
tags: [Skill设计, 经验总结, 最佳实践]
sources: [raw/01-articles/Anthropic 工程师总结的 9 条血泪经验.md]
last_updated: 2026-05-28
---

## 定义
指 Claude 在使用 Skill 时真正踩过的坑和失败模式，是 Skill 中含金量最高的部分。

## 关键信息
- 核心价值：记录 Claude 的默认行为与实际需求之间的差距
- 来源：每次遇到新的失败模式就更新进去
- 设计原则：把 Claude 的默认行为推到特定方向（设计品味、组织规范、边界情况）
- 示例：Anthropic 内部的"设计品味 Skill"通过反复迭代，让 Claude 避免常见的设计陋习

## 关联连接
- [[Skill]] — Gotchas 是 Skill 的核心组成部分
- [[ClaudeCode]] — Gotchas 的积累平台
- [[Thariq]] — 提出 Gotchas 重要性的工程师
- [[摘要-anthropic-engineer-skills]] — 来源