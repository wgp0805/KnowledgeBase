---
title: "SkillCentralLibrary"
type: concept
tags: [Skill管理, AgentBro, 治理核心, 单一事实源]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

Skill 中心库是 AgentBro 治理体系中的"唯一事实源"。所有 Skill 的真实来源、版本认定、分发关系均以中心库记录为准。源码可继续留在个人 Git 项目，但真正分发给各 Agent 的关系只能从中心库出去。

## 核心原则

1. **唯一事实源**：中心库是治理上的 Single Source of Truth
2. **软链接分发**：个人 Git 项目 → 中心库（软链接） → 各 Agent（软链接），修改源码即时同步
3. **快照冻结**：需冻结版本时可复制导入，但开发中的 Skill 持续用软链接
4. **去重**：同一 Skill 不再在多个 Agent 目录存在多份副本，全部指向中心库同一份

## 关键信息

**解决的问题：**
- Case 1：自己开发的 Skill 改完要手动复制到多个 Agent，易漏、易不一致
- Case 2：同一 Skill 在不同 Agent 目录各自修改，版本分叉无人知晓

**操作模式：**
```
个人 Git 项目本地目录 → 软链接导入 AgentBro 中心库 → 软链接分发 Codex / Claude Code / 其他 Agent
```

## 关联连接

- [[AgentBro]] — 核心工具
- [[SkillPackage]] — 技能包开关机制
- [[SkillSoftLink]] — 软链接分发机制
- [[SkillScanTakeover]] — 存量扫描接管
- [[ShirenChuang]] — 作者