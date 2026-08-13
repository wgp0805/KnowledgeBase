---
title: "摘要-superpowers到底是什么"
type: source
tags: [Superpowers, AI编程, 工程纪律, Skill框架]
sources: [raw/09-archive/全网爆火的Superpowers到底是什么.md]
last_updated: 2026-06-26
---

## 核心摘要

苏三深度解读了 Anthropic 官方插件市场安装量超 68 万、GitHub 204K Star 的 Superpowers 框架。其核心理念是 **Process over Prompt（流程大于提示词）**：实现形态仅是一组 `SKILL.md` 文件，没有运行时、不锁定模型，跨 Claude Code / Cursor / Codex CLI / Gemini CLI / Copilot CLI 通用。框架内置 14 个 Skill，分为协作、测试、调试、元四类；强制执行五阶段开发流程（头脑风暴 → 方案设计 → 编写计划 → 执行开发 → 代码审查），任何代码产出都不能跳步骤。最具特色的是 **subagent-driven-development**：每个任务派发独立子代理隔离上下文，完成后经 F1（规格合规）+ F2（代码质量）两阶段审查。已知问题是子 Agent 上下文继承不完整，需手动触发 `using-superpowers` 拉回轨道，官方预计 v5.2.0 修复。

## 关联连接

- [[Superpowers]] — 主体实体
- [[VibeCoding]] — 它要消灭的现象
- [[Skill]] — 核心机制
- [[ClaudeCode]] — 首发载体
- [[子Agent编排]] — 子代理隔离机制
- [[TDD|test-driven-development]] — 强制 TDD
- [[code-review]] — 强制代码审查
- [[摘要-superpowers-openspec-speckit对比]] — 对比视角
