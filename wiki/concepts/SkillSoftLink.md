---
title: "SkillSoftLink"
type: concept
tags: [Skill管理, AgentBro, 软链接, 分发机制, 版本一致性]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

软链接分发是 AgentBro 实现"中心库唯一事实源"的技术手段。个人 Git 项目目录 → 软链接导入中心库 → 软链接分发给各 Agent。源码改动即时同步到中心库与所有已分发 Agent，无需手动复制。

## 核心原则

1. **单向流向**：源码 → 中心库 → Agent，不反向
2. **即时同步**：修改源码，中心库与 Agent 直接看到新内容
3. **可选快照**：需冻结版本时可复制导入，但开发中持续用软链接
4. **去重**：同一 Skill 在各 Agent 处不再有多份副本，全指向中心库同一实体

## 关键信息

**拓扑结构：**
```
个人 Git 项目本地目录 → 软链接导入 AgentBro 中心库 → 软链接分发 Codex / Claude Code / 其他 Agent
```

**解决的问题：**
- Case 1：自己开发的 Skill 改完还要到处复制，漏一次各 Agent 看到的内容就不一样
- Case 2：同一 Skill 在 Claude Code 和 Codex 里各有一份，先改这边再改那边，最后没人说得清哪份更新

**硬规则：** "AgentBro 中心库是治理上的唯一事实源。源码可以继续放在个人 Git 项目里，真正分发给 Agent 的关系只能从中心库出去。"

## 关联连接

- [[SkillCentralLibrary]] — 中心库唯一事实源
- [[SkillPackage]] — 技能包开关层
- [[AgentBro]] — 核心工具
- [[SkillScanTakeover]] — 存量扫描接管（将旧副本替换为指向中心库的软链接）