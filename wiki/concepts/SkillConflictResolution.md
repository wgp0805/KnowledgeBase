---
title: "SkillConflictResolution"
type: concept
tags: [Skill管理, AgentBro, 同名冲突, 冲突决策]
sources: [raw/01-articles/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

同名冲突处理是 AgentBro 在扫描接管存量技能时，针对同名但内容不同的 Skill 所做的决策机制。同名不代表内容相同，可能是旧副本或两套碰巧重名的 Skill，系统不能直接覆盖。

## 核心原则

1. **中心库版本优先**：默认原则，同名时以中心库版本为准
2. **例外处理**：
   - 确认两份内容确需并存 → 重命名
   - 确认 Agent 目录版本更新 → 反向覆盖中心库
3. **分类展示**：扫描结果单独标出"未管理项"与"同名冲突"
4. **人工介入**：名字撞车必须停下来看内容，不能塞进"一键覆盖"

## 关键信息

**实战数据：** 一次扫描发现 86 个可接管 Skill + 19 个同名冲突

**禁止行为：** 同名冲突不能自动覆盖 — 可能两套 Skill 用途不同。无冲突可批量收，有冲突必须人工审。

## 关联连接

- [[SkillScanTakeover]] — 发起扫描
- [[AgentBro]] — 核心工具
- [[SkillCentralLibrary]] — 中心库版本