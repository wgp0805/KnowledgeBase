---
title: "OpenSpec 个人使用时同事代码更新后的 Spec 同步策略"
type: synthesis
tags: [OpenSpec, 个人使用, 团队协作, spec-rot, delta-spec, 实操指南]
sources:
  - wiki/syntheses/openspec-brownfield-usage-guide.md
  - wiki/syntheses/openspec-bugfix-workflow.md
  - wiki/syntheses/openspec-archive-modify-and-token-tradeoff.md
  - wiki/entities/OpenSpec.md
  - wiki/concepts/delta-spec.md
  - wiki/sources/摘要-spec-superflow-融合工作流-源码级详解.md
last_updated: 2026-08-28
---

# OpenSpec 个人使用时同事代码更新后的 Spec 同步策略

> **核心问题**：[[OpenSpec]] 是个人使用，团队其他同事不参与 OpenSpec 流程。同事开发完代码后你 `git pull` 下来，OpenSpec 没有记录这些更新，spec 与实际代码脱节。如何保证 OpenSpec 的准确性？

## 一、问题本质：OpenSpec 不会自动感知代码变更

根据 [[openspec-archive-modify-and-token-tradeoff]] 的明确结论：

> [[OpenSpec]] 的 spec 是**静态文档**，不会自动扫描代码变更。同事改了代码但没走 OpenSpec 流程，spec 和实际代码就会脱节，这就是 **spec rot（规范腐烂）**。OpenSpec 没有内置"代码-spec 一致性自动校验"能力，依赖**人工诚实**和**手动补录**。

`/opsx:explore` 本身是**纯对话式探索工具**（见 [[OpenSpec]] 定义），它**不会自动扫描代码**去对比 spec 和实际实现的差异。所有补录流程需要你主动引导。

## 二、核心机制：Delta Spec 补录 + /opsx:sync

根据 [[delta-spec]] 和 [[openspec-bugfix-workflow]]：

- **Delta Spec**：用 `ADDED` / `MODIFIED` / `REMOVED` 三标记描述差异，不动已有 spec，只描述差异
- **`/opsx:sync`**：把 delta spec 合并回 `opsx/specs/` 主规范，让主规范保持最新
- **关键**：没有 `/opsx:sync` 这一步，OpenSpec 永远不知道改了什么

## 三、三种应对策略

### 策略一：拉取同事代码后，主动做差异核对（推荐）

每次 `git pull` 同事代码后，在开始你自己的 OpenSpec 工作流前，**在 `/opsx:explore` 阶段主动要求 AI 做差异核对**：

```
/opsx:explore 我要开始改 XX 功能。先帮我读 opsx/specs/order/spec.md，
再扫 src/order/ 实际代码，告诉我哪里不一致——哪些代码已改但 spec 没记录。
```

关键点：是**你发起的指令**让 AI 去比对，不是 explore 命令自带的功能。

### 策略二：用 Delta Spec 补录未记录的变更

发现差异后，用 [[delta-spec]] 的 `MODIFIED` 标记补录同事的改动：

```markdown
# Delta Spec: 补录同事变更

## MODIFIED
- Requirement: 订单状态 SHALL 支持已退款状态
  （同事已实现但 spec 未记录，现补录对齐）
  #### Scenario: 订单退款
    Given 订单状态为"已发货"
    When 用户申请退款且管理员批准
    Then 订单状态变为"已退款"

## ADDED
- Requirement: 系统 SHALL 支持订单导出为 PDF
  （同事新增功能，spec 未记录）
```

然后执行 `/opsx:sync` 把补录合并回主 spec，消除脱节。

### 策略三：按改动影响分级处理

根据 [[openspec-archive-modify-and-token-tradeoff]] 的实践建议：

| 同事改动类型 | 处理方式 | 理由 |
|------------|---------|------|
| **琐碎改动**（文案、常量） | 绕过无妨 | 影响极小，不值得补录开销 |
| **改变了行为的改动**（哪怕一行逻辑） | 至少在 `opsx/specs/` 留 `MODIFIED` 痕迹 | 或用 [[SpecSuperflow]] 的 tweak 快速路径（≤4 文件纯配置）轻量记录 |
| **结构性改动**（新增模块、改接口） | 必须走完整 delta spec 补录流程 | 影响后续所有开发的前提认知 |

## 四、实操建议：建立"拉取即核对"纪律

根据 [[openspec-archive-modify-and-token-tradeoff]] 和 [[openspec-brownfield-usage-guide]]：

1. **每次 `git pull` 后**：在开始新功能前，先在 explore 中主动要求 AI 对比 spec 和代码
2. **把积累的脱节一次性补录**：用 delta spec 的 `MODIFIED` 条目"补作业"，再 `/opsx:sync`
3. **大改动前必做**：避免基于过期 spec 实现新功能，否则 AI 会基于错误前提工作

### 完整工作流

```
git pull（拉取同事代码）
    │
    ├─ 检查是否有结构性改动（看 commit log / diff）
    │
    ├─ 有改动 → /opsx:explore 主动要求 AI 差异核对
    │           （"读 spec，扫代码，告诉我哪里不一致"）
    │
    ├─ 发现差异 → /opsx:propose 生成 delta spec（补录同事变更）
    │
    ├─ 人工确认 → 审阅补录是否准确
    │
    ├─ /opsx:sync → 合并回主 spec
    │
    └─ 继续你自己的 OpenSpec 工作流（explore → propose → apply → archive）
```

## 五、本质认知

> **OpenSpec 依赖"人工诚实"——你跳过了流程，就得在大改动时主动引导 AI 补录，否则 spec 就是假的。**（[[openspec-archive-modify-and-token-tradeoff]]）

这是 OpenSpec 作为"规划引擎"的定位决定的——它只管"改了什么"，不自动感知代码变化。作为个人用户，你需要在**每次拉取同事代码后、开始自己的 OpenSpec 工作流前**，主动做一次差异核对和补录。

## 六、与已有 synthesis 的关系

本页是已有三个 synthesis 的场景特化：
- [[openspec-brownfield-usage-guide]] — 棕地项目完整使用方案（首次补录策略）
- [[openspec-bugfix-workflow]] — apply 后发现 bug 的修复流程（delta spec + sync 机制）
- [[openspec-archive-modify-and-token-tradeoff]] — 归档后修改流程与 spec rot 风险分析

本页聚焦"**个人使用 + 同事不参与 OpenSpec + 定期拉取代码**"这一特定协作场景，提供可落地的"拉取即核对"纪律。

## 关联连接

- [[OpenSpec]] - 核心框架
- [[delta-spec]] - 增量变更机制（补录同事变更的关键）
- [[openspec-brownfield-usage-guide]] - 配套：棕地项目完整使用方案
- [[openspec-bugfix-workflow]] - 配套：apply 后 bug 修复流程
- [[openspec-archive-modify-and-token-tradeoff]] - 配套：归档修改与 spec rot 风险
- [[SpecSuperflow]] - tweak 快速路径（轻量记录小改动）
- [[规范驱动开发]] - 上层方法论
- [[摘要-spec-superflow-融合工作流-源码级详解]] - spec-merger 防规范腐烂
- [[ClaudeCode]] - 承载平台
