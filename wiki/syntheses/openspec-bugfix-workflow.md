---
title: "OpenSpec apply 后发现 bug 的修复流程"
type: synthesis
tags: [OpenSpec, bug修复, delta-spec, spec-rot, 决策指南]
sources:
  - raw/09-archive/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/09-archive/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
  - raw/09-archive/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md
last_updated: 2026-08-19
---

# OpenSpec apply 后发现 bug 的修复流程

> **核心问题**：[[OpenSpec]] 走完 `/opsx:explore` → `/opsx:propose` → `/opsx:apply` 写完代码后，验证发现有问题。此时该用哪个 skill 改，还是直接让 AI 改？改完用哪个技能让 OpenSpec "知道"这次修改？

## 一、先判断 bug 的性质（关键分叉）

| bug 性质 | 判断标准 | 处理方式 |
|---------|---------|---------|
| **实现 bug**（代码写错了，但 spec 没问题） | 需求规格本身是对的，是 AI 没按 spec 实现 | **直接让 AI 改代码**，不必动 spec |
| **需求 bug**（spec 本身有遗漏或错误） | 验收场景没覆盖到、需求理解偏差、边界没想清楚 | **必须走 delta spec 流程**，先改 spec 再改代码 |

**spec 对不对**决定了要不要动 OpenSpec 的工件。这是整个修复流程的核心分叉点。

## 二、情况 A：实现 bug（spec 没问题）

**直接让 AI 改代码即可，不需要调用任何 OpenSpec skill。**

理由：`/opsx:apply` 已经把 tasks.md 跑完，规划文档是正确的，只是 AI 实现时手抖了。此时：

1. 直接在对话里告诉 AI 哪里有问题、期望行为是什么
2. AI 修复代码
3. 重新验证

**注意**：
- 如果还没 `/opsx:archive`，这次修复属于 apply 阶段的延续，tasks.md 可以补一条修复记录。
- 如果已经 archive 了，小修复绕过流程无妨（见 [[openspec-archive-modify-and-token-tradeoff]] 的"小改动走快速路径"）。

## 三、情况 B：需求 bug（spec 有问题）

**必须走 delta spec 流程，不能直接改代码。** 否则代码和 spec 会脱节，产生 **spec rot（规范腐烂）**——OpenSpec 不会自动扫描代码感知你的改动，下次 AI 读到的是过期规范，可能基于错误前提实现。

### 完整流程

```
/opsx:explore   → 理清改什么、为什么改
/opsx:propose   → 生成 delta spec（ADDED/MODIFIED/REMOVED 三标记，只写差异）
人工确认         → 审阅 delta 提案（关键检查点，别跳）
/opsx:apply     → 按 tasks.md 改代码
/opsx:sync      → 把 delta 合并回主 spec（让 OpenSpec "知道"这次修改）
/opsx:archive   → 归档本次变更，形成新基线
```

### 关键点：`/opsx:sync` 才是让 OpenSpec "知道"的命令

改完代码后，**`/opsx:sync`** 把 delta spec 合并回 `opsx/specs/` 主规范，让主规范保持最新。**没有这一步，OpenSpec 永远不知道你改了什么**。

### Delta Spec 写法（只写差异，不重写整份 spec）

```markdown
# Delta Spec: 修复订单导出金额计算错误

## MODIFIED
- Requirement: 系统 SHALL 按含税价格导出订单金额
  （原 spec 写的是"按不含税价格"，验证时发现业务需要含税）
  #### Scenario: 导出含税金额
    Given 订单金额 100 元，税率 13%
    When 点击"导出 Excel"
    Then 导出金额列显示 113 元

## ADDED
- 无

## REMOVED
- 无
```

## 四、速记决策树

```
验证发现 bug
    │
    ├─ spec 是对的，只是代码写错 → 直接让 AI 改代码（不必动 OpenSpec）
    │
    └─ spec 本身有问题
         │
         ├─ 还没 archive → 回去改 specs/spec.md 和 design.md，再 /opsx:apply
         │
         └─ 已经 archive → /opsx:explore → /opsx:propose（生成 delta）
                           → 人工确认 → /opsx:apply → /opsx:sync → /opsx:archive
```

## 五、一个容易踩的坑

**不要直接手改 `opsx/archive/` 里的归档文档**。归档是历史基线，直接改会丢失"为什么改"的上下文。标准做法是用 [[delta-spec]] 描述差异，再 `/opsx:sync` 合并。这是 [[OpenSpec]] 工件依赖关系"使能而非卡死"的设计——随时可回改，但要留下变更痕迹。

## 六、与归档修改流程的关系

本页是 [[openspec-archive-modify-and-token-tradeoff]] 的前置场景特化：
- [[openspec-archive-modify-and-token-tradeoff]] 解决"已经 archive 后又要改"的完整流程与 token 权衡
- 本页解决"apply 完还没 archive（或刚 archive）发现 bug"的即时决策
- 两者共享 delta spec + `/opsx:sync` 的核心机制

## 关联连接

- [[OpenSpec]] - 核心框架
- [[delta-spec]] - 增量变更机制（修复需求 bug 的关键）
- [[openspec-archive-modify-and-token-tradeoff]] - 配套：归档后修改流程与 token 成本权衡
- [[openspec-brownfield-usage-guide]] - 配套：棕地项目完整使用方案
- [[SpecSuperflow]] - hotfix/tweak 快速路径（小改动可跳过完整流程）
- [[规范驱动开发]] - 上层方法论
- [[摘要-OpenSpec规范驱动AI编程框架]] - OpenSpec 来源
- [[摘要-spec-superflow-融合工作流]] - SpecSuperflow 来源
- [[摘要-superpowers-openspec-speckit对比]] - 三方对比
- [[ClaudeCode]] - 承载平台
