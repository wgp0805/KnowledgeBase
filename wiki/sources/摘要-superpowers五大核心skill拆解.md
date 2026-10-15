---
title: "摘要-superpowers五大核心skill拆解"
type: source
tags: [AI编程, Skill, Superpowers, ClaudeCode, 工程纪律]
sources: ["raw/01-articles/2026-10-14-185,000 星的 Superpowers 插件，90% 的人只用了它 10% 的功能 - 码哥字节.md"]
last_updated: 2026-10-15
---

## 核心摘要

码哥字节从 Superpowers 的 SKILL.md 源文件出发，拆解大多数人只用了 10% 功能的五大核心 skill。核心论点：Superpowers 里的每个 skill 本质是纯文本行为约束（Markdown），AI 编程 Agent 缺的不是能力而是纪律，纪律可以用纯文本分发。①**brainstorming**：`<HARD-GATE>` 硬门——设计未获批准前一行代码不许写；完整 9 步流程，最易跳过的是步骤 6-8（把设计写入 docs/superpowers/specs/ 并 commit、自检 spec、用户审阅）；终态只能移交 writing-plans；反直觉设计是"越觉得项目简单越要走流程"。②**systematic-debugging**：铁律"NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"，四阶段（根因调查→模式分析→单假设验证→实现修复），数据称系统调试平均 2-3 小时可降至 15-30 分钟；Phase 4 有"三次失败规则"——连续 3 次修复失败必须停下来讨论是否架构问题。③**writing-plans**：每步骤粒度 2-5 分钟（"写失败测试"和"跑一下确认失败"是两步），零占位符规则——TBD/TODO/"添加适当的错误处理"/"类似 Task N"均视为计划失败。④**执行二选一**：subagent-driven-development（每任务全新 subagent + 两轮审查，防上下文串扰，环境支持就选它）vs executing-plans（当前会话串行，适合 Cursor 等无 subagent 环境）。⑤**finishing-a-development-branch**：验证测试→定 base branch→四选项（本地 merge/PR/保留/丢弃），丢弃需手动输入 "discard" 防误删。两个常见坑：上下文漂移（显式喊 `/using-superpowers` 重置）、把 brainstorming 当问答机（价值在产出 committed spec）。

## 关联连接
- [[Superpowers]] — 被拆解的 Skill 框架
- [[码哥字节]] — 作者
- [[brainstorming]] — 核心 skill 之一
- [[systematic-debugging]] — 调试纪律 skill
- [[writing-plans]] — 计划拆解 skill
- [[subagent-driven-development]] — 子代理驱动开发
- [[executing-plans]] — 串行执行方案
- [[TDD]] — 贯穿实现阶段的测试纪律
- [[AgentSkills]] — skill 的承载机制
