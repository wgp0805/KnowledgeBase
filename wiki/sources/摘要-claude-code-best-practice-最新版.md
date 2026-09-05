---
title: "摘要-claude-code-best-practice-最新版"
type: source
tags: [来源, Claude Code, 最佳实践, 工作流]
sources: [raw/01-articles/Claude Code 最佳实践（最新版）.md]
last_updated: 2026-07-14
---

## 核心摘要

这是一篇系统性的 Claude Code 最佳实践指南，覆盖 CLAUDE.md 配置原则、工作流最佳实践、调试与纠错、上下文管理、Subagents、Skills 管理、Superpowers/OpenSpec 使用详解、权限与安全、规格与实现分离、常见陷阱、工具组合策略等 13 个模块。核心原则包括：保持 CLAUDE.md 简短（60-300 行）、分而治之（子智能体/分阶段/规格实现分离）、50% 时手动 /compact、三次失败 /clear 重启、系统约束（Hooks/权限）优于提示词约束。推荐 Claude Code + OpenSpec + Superpowers 三重栈组合：OpenSpec 管"WHAT"，Superpowers 管"HOW"，Claude Code 负责"执行"。

## 关联连接

- [[ClaudeCode]] — 核心实体
- [[CLAUDEmd]] — CLAUDE.md 配置
- [[计划模式]] — Plan Mode 工作流
- [[Superpowers]] — 工程纪律框架
- [[OpenSpec]] — 规范驱动框架
- [[Skill]] — 技能扩展
- [[Gotchas]] — 踩坑经验记录
- [[ContextManagement]] — 上下文管理
- [[子Agent编排]] — 子智能体机制
- [[claude-code-best-practice]] — 社区最佳实践仓库
