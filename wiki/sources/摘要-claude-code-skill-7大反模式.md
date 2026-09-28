---
title: "摘要-claude-code-skill-7大反模式"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/2026-09-26-我写了 50 个 Claude Code Skill 才发现，前 30 个都白写了 - 码哥字节.md]
last_updated: 2026-09-28
---

# 摘要-claude-code-skill-7大反模式

## 核心摘要

作者写了 50 多个 Claude Code Skill 后总结：前 30 个作废的原因不是技术，而是把 Skill 当成了 prompt 模板升级版——正确哲学是 Skill 决定「什么时候轮到我做」而非「我能做什么」。文章给出 7 个反模式：SKILL.md 写成长篇 prompt（建议主文件 ≤200 行，超出拆到 references/）、description 写成功能介绍而非触发条件、把工具调用写进 Skill（工具该走 MCP）、多个 Skill 边界重叠、不写 Gotchas 章节、示例用伪代码（模型是镜子）、不分项目级与用户级。正面案例是 Anthropic 官方 frontend-design（27 万安装）：「Use this skill when」触发条件 + 渐进式披露 + 完整 Anti-patterns 章节。Skill 正在成为跨工具事实标准：OpenAI Codex 的 SKILL.md frontmatter 与 Anthropic 几乎一致，实测纯指令型 Skill 软链复用约 90% 兼容，涉及工具调用与路径的 10% 会翻车；Skill vs MCP 用 Spring 类比——MCP 像 SPI（能力发现），Skill 像 Starter（场景编排）。

## 关联连接
- [[Skill]] — 该文的反模式与设计哲学归入此概念
- [[Skills]] — Skills 系统
- [[Skill命中率]] — description 触发条件写法决定命中
- [[SkillSoftLink]] — 软链跨工具复用实验
- [[SkillCreator]] — 官方生成 Skill 的元工具
- [[Codex]] — SKILL.md 格式趋同的另一方
- [[ClaudeCode]] — Skill 机制的发源工具
- [[MCP]] — 与 Skill 的职责分界
- [[码哥字节]] — 文章作者
