---
title: "execution-contract"
type: concept
tags: [AI编程, 规范驱动, 执行验证, 契约]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/01-articles/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
last_updated: 2026-07-14
---

## 定义

执行契约（Execution Contract）是 [[SpecSuperflow]] 的核心创新，由 bridge-contract 组件自动从 [[OpenSpec]] 的四个规划工件（proposal、specs、design、tasks）中提取关键约束，生成一份 `execution-contract.md`。它不是第五个规划文档，而是规划与执行之间的「锚点」——一份执行必须对标的可验证契约，解决"规划是参考材料、执行可能不看"的脱节问题。

## 关键信息

### 提取的六类约束

| 约束 | 作用 |
| --- | --- |
| Intent Lock | 锁定变更意图，防止执行过程中目标漂移 |
| Scope Fence | 圈定变更范围（In Scope / Out of Scope），明确什么该改什么不该改 |
| Non-Goals | 列出明确不做的事，防止 AI 顺手做 spec 之外的事 |
| Test Obligations | 测试义务，哪些场景必须有测试覆盖 |
| Review Gates | 审查节点，执行到哪一步需暂停等人 review |
| Rewind Triggers | 回滚触发条件，出现什么情况必须停下重新评估 |

### 覆盖检查

每个 spec 里的 SHALL 和 MUST 需求，都必须在契约中有对应条目。若某条需求在契约里找不到映射，说明规划层与执行层有缝隙——要么补契约，要么回头补规划。

### 人工门禁

契约生成后，唯一的人工门禁是用户审批。审批通过后 execution-governor 才启动执行。设计意图：机器可生成规划、可执行代码，但"确认这个规划值得执行"的判断必须由人来做。

### 执行期管控

execution-governor 拿契约逐条比对：Scope Fence 之外的文件不许碰；Non-Goals 的事不准顺手做；Rewind Trigger 触发则暂停等人决定。

## 关联连接

- [[SpecSuperflow]] - 所属框架
- [[OpenSpec]] - 规划工件来源
- [[Superpowers]] - 执行层框架
- [[review-gate]] - 审查门禁机制
- [[eight-state-machine]] - 契约所处的 bridging 状态
- [[规范驱动开发]] - 上层方法论
- [[摘要-spec-superflow-融合工作流]] - 来源
- [[摘要-spec-superflow-融合工作流-源码级详解]] - 来源
