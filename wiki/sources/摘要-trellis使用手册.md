---
title: "摘要-trellis使用手册"
type: source
tags: [来源, Trellis, Codex, 工作流, 规范驱动开发]
sources: [raw/01-articles/Trellis使用手册.md]
last_updated: 2026-07-15
---

## 核心摘要

本文按官方中文资料整理 [[Trellis]] 的定位、安装和日常工作流。Trellis 不替代模型或 AI 编码工具，而是为 Codex、Claude Code、Cursor 等平台提供共享的项目规范、任务文档、会话记忆与阶段控制；其跨平台事实源位于 `.trellis/`，不同工具仅保留各自的适配层。

完整任务按“分类请求 → 经许可创建任务 → planning 产出 PRD/设计/实施计划 → execute 按需读取 Spec 与任务上下文 → check 验证和修复 → 先提交业务代码 → finish-work 归档并写 journal”推进。Spec 用于长期且可复用的项目契约，Task 保存当前变更的临时决策，Workspace/Journal 则记录按开发者隔离的会话轨迹。

文中提醒：不应为了小型改动强行建任务；规范必须从真实代码和已验证的经验中提炼，并保持精简、可追溯。Codex 接入需要让基础项目指引可被读取；若依赖 Hook 自动注入工作流状态，则还需完成相应的平台配置与审批。

## 关联连接

- [[Trellis]] — 本文说明的工作流框架
- [[项目级AI工作流]] — Spec、Task、Journal 构成的闭环
- [[Codex]] — 重点说明的接入平台
- [[规范驱动开发]] — 上层方法论
- [[AgentHarness]] — 项目级工程支撑层
- [[计划模式]] — planning 阶段的协作方式
