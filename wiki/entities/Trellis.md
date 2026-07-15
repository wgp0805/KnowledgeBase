---
title: "Trellis"
type: entity
tags: [AI编程, 工作流, 规范驱动开发, 跨平台]
sources: [raw/01-articles/Trellis使用手册.md, raw/01-articles/从 vibe coding 到 spec coding：我一年多使用AI开发的实践总结.md]
last_updated: 2026-07-15
---

## 定义

**Trellis** 是面向 AI 编码的项目级工作流框架。它不替代 [[Codex]]、[[ClaudeCode]] 等 Agent，而是将项目规范、任务材料、阶段状态与会话记录组织为可提交、可追溯的文件资产，帮助团队在不同 AI 工具之间共享同一套项目事实源。

## 关键信息

### 核心结构

- `.trellis/spec/`：长期可复用的项目契约；应从真实代码和已验证经验中提炼。
- `.trellis/tasks/`：任务的 PRD、设计、实施清单与调研结论；用于保存当前变更的决策依据。
- `.trellis/workspace/`：按开发者隔离的工作记录与 Journal。
- `workflow.md`、`config.yaml` 与脚本：定义阶段规则、共享配置和任务辅助操作；`.runtime/`、`.developer` 等会话级状态不应作为团队共享事实。

### 任务闭环

Trellis 先区分普通对话、小型改动和完整任务；完整任务必须在得到创建任务许可后进入 planning。规划经确认后，执行阶段只按需加载相关 Spec 和任务材料；check 阶段对照验收标准、规范和本地验证结果修复问题。业务代码提交后，`finish-work` 才归档任务并追加 Journal，从中筛选稳定经验回写 Spec。

### 适用边界

它更适合长期维护、多人协作、需要跨会话接续或允许团队成员使用不同 AI 工具的项目。一次性脚本、单轮可验证的小改动，以及无法维护规范的团队，应保持轻量流程，避免空模板和过期规则造成额外负担。

## 关联连接

- [[摘要-trellis使用手册]] — 安装、结构与命令说明
- [[摘要-从-vibe-coding-到-spec-coding]] — 从实践视角解释其价值与边界
- [[项目级AI工作流]] — Trellis 落地的方法论
- [[规范驱动开发]] — 上层工程方法论
- [[AgentHarness]] — Trellis 所提供的项目工程支撑
- [[Codex]] — 可接入的 AI 编码平台
- [[OpenSpec]] — 规范管理取向的对照方案
- [[Superpowers]] — 流程强化取向的对照方案
