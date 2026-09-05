---
title: "摘要-spec-superflow-融合工作流-源码级详解"
type: source
tags: [来源, spec-superflow, AI编程, 规范驱动, 工作流]
sources: [raw/01-articles/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md]
last_updated: 2026-07-14
---

## 核心摘要

程序员追风撰写的 spec-superflow 深度解读文章，揭示其"源码级融合，不是简单并列"的设计理念。核心创新是 contract-builder 桥接层：将 OpenSpec 的四份规划工件自动压缩成一份 execution-contract.md，作为规划到实现的唯一交接层（Guarded Handoff），没有契约或未被批准就不准进入实现。工作流由 8 状态路由引擎驱动（workflow-start 为入口技能，做内容级状态检测、阻止非法跳转），9 个核心技能各对应一个阶段。跨 17 个平台分发，零运行时依赖，MIT 协议。端到端流程为：workflow-start 路由 → need-explorer 探索 → spec-writer 出四份工件 → contract-builder 生成执行契约 → DP-3 人工批准 → build-executor 执行（TDD+SDD+Review Gate） → release-archivist 收口归档 → spec-merger delta 合并防规范腐烂。提供 hotfix（≤2 文件）和 tweak（≤4 文件纯配置）两条快速路径。

## 关联连接

- [[SpecSuperflow]] — 核心实体
- [[OpenSpec]] — 融合的规划层
- [[Superpowers]] — 融合的执行层
- [[execution-contract]] — 执行契约桥接层
- [[eight-state-machine]] — 八状态路由引擎
- [[DP-3]] — 人工审批检查点
- [[规范驱动开发]] — 上层方法论
- [[程序员追风]] — 文章作者
- [[MageByte-Zero]] — spec-superflow 开发者
- [[FissionAI]] — OpenSpec 开源方
