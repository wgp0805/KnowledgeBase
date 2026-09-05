---
title: "DP-3"
type: concept
tags: [AI编程, 人工审批, 工作流, 规范驱动]
sources: [raw/01-articles/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md]
last_updated: 2026-07-14
---

## 定义

**DP-3**（Design-Phase-3）是 [[SpecSuperflow]] 工作流中唯一一次人工审批检查点。在 contract-builder 生成 execution-contract.md 之后，系统暂停并要求用户批准契约内容，不批准就不允许进入 executing 阶段写任何业务代码。

## 关键信息

- DP-3 是整个流程里**唯一一次人工介入**，是规划到实现的硬墙
- 审批通过后，build-executor 按 TDD → SDD → Review Gate 顺序推进
- 哪怕是 hotfix 快速路径，也必须完成 DP-3
- 设计意图：机器可以生成规划、执行代码，但"确认这个规划值得执行"的判断必须由人来

## 关联连接

- [[execution-contract]] — DP-3 审批的契约对象
- [[eight-state-machine]] — 状态机中的 DP-3 节点
- [[review-gate]] — 执行阶段的质量门禁
- [[规范驱动开发]] — 相关方法论
- [[摘要-spec-superflow-融合工作流-源码级详解]] — 来源
