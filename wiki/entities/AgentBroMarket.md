---
title: "AgentBroMarket"
type: entity
tags: [AgentBro组件, 技能市场, Skill分发, 创作者技能包]
sources: [raw/01-articles/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

AgentBro Market 是 AgentBro 内置的技能市场功能，支持从市场安装 Skill 并按创作者直接组成技能包（如 `anthropics/skills`），实现来源与用途的分离管理。

## 关键信息

**核心能力：**
- 浏览并安装社区/官方发布的 Skill
- 安装时可直接指定归属技能包，自动按创作者组织（如 `anthropics/skills`）
- 新安装的 Skill 先进入试用区（`NiceTry-测试`），验证好用后再晋升到稳定包（`NiceTry`）
- 试用包非垃圾桶，而是给新 Skill 明确观察期，也让用户知道哪些还未进生产

**工作流：**
1. 看到好用的社区 Skill → 放入 `NiceTry-测试`
2. 确认好用 → 移入稳定的 `NiceTry`
3. 创作者批量 Skill → 市场安装时直接组成创作者技能包（如 `anthropics/skills`）
4. 来源、用途、稳定性三维度互不混淆

## 关联连接

- [[AgentBro]] — 核心产品
- [[SkillPackage]] — 技能包概念
- [[SkillTestPackage]] — 测试包观察期
- [[Anthropic]] — 官方技能包来源示例