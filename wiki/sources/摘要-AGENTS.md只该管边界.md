---
title: "摘要-AGENTS.md只该管边界"
type: source
tags: [AGENTS.md, Codex, 边界管理, AI编程, 协作规范]
sources: [raw/01-articles/2026-08-30-经常用 Codex 后，我发现 AGENTS.md 只该管一件事 - 程序员徐公.md]
last_updated: 2026-08-31
---

## 核心主旨

基于长期使用 Codex 的实战经验，提出 AGENTS.md 应只管"边界"一件事，而非堆砌所有项目信息。保留四类内容：协作习惯、目标驱动、真实性验证、安全边界。

## 关键信息

### 核心论点
- AGENTS.md 不是"项目说明书"，而是"边界声明"
- 写得越多越像噪音，Agent 抓不住重点反而忽略关键约束
- 类比：给新人的不是一本手册，而是"这几条红线别碰"

### 四类保留内容
1. **协作习惯** — 你希望 Agent 怎么跟你配合（先计划再执行、小步验证、不开新会话不假设）
2. **目标驱动** — 当前任务的目标和验收标准，让 Agent 知道"完成"长什么样
3. **真实性验证** — 要求 Agent 验证而非假设（跑测试、看 diff、不编造 API）
4. **安全边界** — 红线规则（禁止 push --force、禁止降级依赖、禁止动生产配置）

### 应删除的内容
- 能从代码推断的信息（技术栈、目录结构、构建命令）
- 一次性任务描述（应放对话上下文而非 AGENTS.md）
- 过时的踩坑记录（已修复的坑不必长期保留）

### 与现有知识的呼应
- 与 [[Codex]] 的 AGENTS.md 三原则一致：只放硬约定、不是越全越好、踩坑后更新
- 与 [[ClaudeCode]] 的 CLAUDE.md 最佳实践一致：≤200 行、能从代码推断的不写

## 关联连接
- [[Codex]] — 文章基于的实战工具
- [[ClaudeCode]] — CLAUDE.md 同类理念
- [[CLAUDEmd]] — Claude Code 指令系统
- [[摘要-再见吧-codex]] — Codex 七步工作流含 AGENTS.md 原则
- [[摘要-codex-97percent-技巧]] — 苏三的 AGENTS.md 四块内容
- [[摘要-AI-agent工具应该怎么使用]] — 二师兄的 AGENTS.md 实践
- [[摘要-claude-code-best-practice-最新版]] — CLAUDE.md 最佳实践
