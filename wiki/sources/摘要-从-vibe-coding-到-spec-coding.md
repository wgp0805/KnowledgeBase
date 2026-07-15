---
title: "摘要-从-vibe-coding-到-spec-coding"
type: source
tags: [来源, AI编程, Trellis, 规范驱动开发]
sources: [raw/01-articles/从 vibe coding 到 spec coding：我一年多使用AI开发的实践总结.md]
last_updated: 2026-07-15
---

## 核心摘要

文章以作者使用 Trellis 的一年实践为线索，主张长期维护的 AI 编程项目应从临时对话式的 [[VibeCoding]] 转向以规格、任务和持续记忆为中心的规范化开发。作者认为 Prompt、规则文件和 Skill 分别能解决临时需求、静态约束与固定流程，却无法单独处理跨会话记忆、跨工具共享和项目级经验回流。

文中将 [[Trellis]] 定位为项目级工作流 Harness：以 `.trellis/` 集中保存 Spec、Task、Workflow 与 Workspace/Journal，并按需把当前任务所需的上下文交给 Agent。其闭环为：恢复上下文 → 注入当前状态 → 判断是否建任务 → planning → execute → check → update-spec → 业务代码提交后 finish-work 归档任务并记录 journal。

该方案适用于长期维护、多人协作、频繁切换 AI 工具或希望沉淀决策依据的项目；一次性脚本、短任务或无意维护规范的团队不宜强行采用。文章同时强调，Spec 只应收录可长期复用且经验证的规则，避免成为冗长、过期的材料堆。

## 关联连接

- [[Trellis]] — 文中介绍的项目级工作流框架
- [[项目级AI工作流]] — Spec、Task、状态与 Journal 的闭环方法
- [[规范驱动开发]] — 从 Vibe Coding 转向的上层方法论
- [[VibeCoding]] — 文中辨析的临时对话式开发模式
- [[AgentHarness]] — Trellis 所处的工程化支撑层
- [[Codex]] — 文中重点说明的接入平台
- [[OpenSpec]] — 规范管理取向的对照方案
- [[Superpowers]] — 流程强化取向的对照方案
