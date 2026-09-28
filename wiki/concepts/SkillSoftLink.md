---
title: "SkillSoftLink"
type: concept
tags: [Skill管理, AgentBro, 软链接, 分发机制, 版本一致性]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md, raw/01-articles/2026-09-26-我写了 50 个 Claude Code Skill 才发现，前 30 个都白写了 - 码哥字节.md]
last_updated: 2026-09-28
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

## 跨工具复用实验（Claude Code ↔ Codex，2026-09）
来自 [[摘要-claude-code-skill-7大反模式]]。由于两边 SKILL.md frontmatter 几乎一致，把同一 Skill 软链到两个目录即可一鱼两吃：
```
ln -s ~/skills-shared/commit-msg-zh ~/.claude/skills/commit-msg-zh
ln -s ~/skills-shared/commit-msg-zh ~/.codex/skills/commit-msg-zh   # 或 ~/.agents/skills/
```
- **约 90% 兼容**：纯文本指令、规则、checklist 类 Skill 两边表现几乎一样（如 commit-msg-zh、redis-key-naming）
- **10% 翻车**：涉及工具调用与文件路径的不可直接复用——Codex 是 `read_file`，Claude 是 `Read`，工具命名、路径解析、子进程隔离机制完全不同
- **实操**：Skill 库拆成「pure 指令型」（通用，软链即可）与「带工具调用型」（各写一份）；典型比例约 60% 为 pure 型

## 关联连接

- [[SkillCentralLibrary]] — 中心库唯一事实源
- [[SkillPackage]] — 技能包开关层
- [[AgentBro]] — 核心工具
- [[SkillScanTakeover]] — 存量扫描接管（将旧副本替换为指向中心库的软链接）
- [[Skill]] — 被分发的技能本体
- [[Codex]] — 跨工具复用的另一端
- [[摘要-claude-code-skill-7大反模式]] — 来源（复用兼容性实验）