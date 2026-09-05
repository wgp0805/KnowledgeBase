---
title: "AgentSpecificSkillPackages"
type: concept
tags: [Skill管理, AgentBro, Agent隔离, 环境隔离, 个人与公司隔离]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

Agent 维度技能包隔离是指同一中心库下，不同 Agent 可以独立启用不同的技能包组合。Codex 可开启内容创作和 NiceTry，Claude Code 使用另一套组合，公司 Agent 只应用公司内部包。不追求所有 Agent 一模一样。

## 核心原则

1. **技能包生效状态按 Agent 独立管理**
2. **公司/个人完全隔离**：公司的内部 Agent 需公司技能包，个人的 Agent 无权限看到公司 Skill
3. **工作场景差异化**：不同 Agent 承担不同工作，能用的 Skill 本应不同

## 关联连接

- [[SkillPackage]] — 技能包机制
- [[AgentBro]] — 核心工具
- [[ClaudeCode]] — 差异化生效示例
- [[Codex]] — 差异化生效示例