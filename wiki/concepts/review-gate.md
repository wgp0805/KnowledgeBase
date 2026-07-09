---
title: "review-gate"
type: concept
tags: [AI编程, 工程纪律, 代码审查]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

Review Gate（审查门禁）是 [[Superpowers]] 的质量管控机制，在开发流程中层层设卡，任何一层未通过都不能往下走。它将代码审查从"事后补救"变为"过程中拦截"。

## 关键信息

### 四层门禁

1. spec 写完后自审
2. 每个任务完成后审查
3. 整个分支完成后审查
4. 交付前最终验证

### 在执行契约中的体现

[[execution-contract|执行契约]] 的 Review Gates 约束定义了执行到哪一步需暂停等人 review（如"DTO/Service 层完成后 review 分页逻辑"）。execution-governor 据此在对应节点暂停。

### Red Flags 表

Superpowers 还有一张 Red Flags 表，列出 AI 可能用来跳过流程的借口（如"改动太小不需要测试""用户赶时间先跳过 review"），逐条说明为何这些借口不成立。

## 关联连接

- [[Superpowers]] - 所属框架
- [[SpecSuperflow]] - 融合后保留
- [[execution-contract]] - 契约中的审查约束
- [[code-review]] - 代码审查实践
- [[TDD]] - 同属质量门禁体系
- [[摘要-spec-superflow-融合工作流]] - 来源
