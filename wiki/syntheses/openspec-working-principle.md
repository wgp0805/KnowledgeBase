---
title: "openspec-working-principle"
type: synthesis
tags: [AI编程, 规范驱动, OpenSpec, 工作原理, 综合分析]
sources:
  - wiki/entities/OpenSpec.md
  - wiki/concepts/delta-spec.md
  - wiki/sources/摘要-OpenSpec规范驱动AI编程框架.md
  - wiki/sources/摘要-superpowers-openspec-speckit对比.md
  - wiki/sources/摘要-spec-superflow-融合工作流.md
  - wiki/sources/摘要-spec-superflow-融合工作流-源码级详解.md
last_updated: 2026-08-21
---

# OpenSpec 工作原理综合分析

## 一句话定位

[[OpenSpec]] 是 [[FissionAI]] 开源的**规范驱动 AI 编程框架**（MIT 协议，57k+ Star），核心理念：**先对齐需求，再写代码**。它把"规划"做到极致，有意不碰"从规划到落地"这段路，定位是**规划引擎**。

## 一、四阶段核心工作流

OpenSpec 通过四个斜杠命令驱动一次完整变更生命周期（见 [[摘要-OpenSpec规范驱动AI编程框架]]）：

| 阶段 | 命令 | 作用 |
|------|------|------|
| 探索 | `/opsx:explore` | 纯对话理清需求，不写代码 |
| 提案 | `/opsx:propose` | 生成四份规划工件 |
| 应用 | `/opsx:apply` | 按任务清单逐项实现，生成代码并更新 tasks 进度 |
| 归档 | `/opsx:archive` | 完成后将规划文档移入 `archive/` 目录 |

## 二、四份规划工件 + DAG 依赖图

`/opsx:propose` 阶段产出四份互相依赖的工件（见 [[OpenSpec]]）：

1. **proposal.md** — 变更提案：为什么做、做什么
2. **specs/spec.md** — 需求规格：用 `SHALL`/`MUST` 确定性词汇 + `Given/When/Then` 验收场景描述
3. **design.md** — 技术设计：怎么实现
4. **tasks.md** — 任务清单：可执行步骤

**工件依赖链**：`proposal → specs → design → tasks → implement`。每个工件都有 schema 定义，靠 YAML 引擎做**拓扑排序**。关键点是依赖关系是"使能"而非"卡死"——随时可回去修改前面的工件，不会强制线性推进。

## 三、Delta Spec 增量变更机制

这是 OpenSpec 对**棕地项目**最友好的设计（详见 [[delta-spec]]）：

- 用 `ADDED` / `MODIFIED` / `REMOVED` 三个标记描述变更差异
- **不动已有 spec，只描述差异**——改一处不必重写整份 spec
- 通过 `/opsx:sync` 把 delta spec 合并回主 spec

例如"认证边界从 A 移到 B"，只需写这个 delta，原有 spec 保持不变。

## 四、多平台分发机制

OpenSpec 支持 **31 个 AI 编码工具**（claude、cursor、codex、gemini、opencode、qoder、windsurf 等）。初始化时：

```bash
openspec-cn init --tools claude,cursor,codex   # 指定多个
openspec-cn init --tools all                     # 全部 31 个
```

每个工具按各自目录约定生成 Skills（`.../skills/openspec-*/SKILL.md`）和 Commands（`.../commands/opsx-<id>.md`），实现"一份规范，多平台执行"。

## 五、定位边界与生态组合

OpenSpec 只管"**改了什么**"（规划层），不管"怎么干"（执行纪律）。[[摘要-superpowers-openspec-speckit对比]] 给出三者理想组合：

- [[SpecKit]]（GitHub 官方）定项目宪法 → 解决"按什么规矩干"
- [[OpenSpec]] 管每次变更生命周期 → 解决"改了什么"
- [[Superpowers]] 强制执行纪律 → 解决"怎么干"

[[SpecSuperflow]]（spec-superflow 插件）已将 OpenSpec 与 Superpowers **源码级融合**：通过 contract-builder 桥接层，把 OpenSpec 的四份工件自动压缩成一份 `execution-contract.md`，作为规划到实现的唯一交接层（Guarded Handoff），由八状态机驱动，DP-3 为唯一人工审批点（见 [[摘要-spec-superflow-融合工作流-源码级详解]]）。

## 六、工作原理公式化总结

OpenSpec 的工作原理可概括为四个维度的乘积：

> **四阶段命令循环**（explore → propose → apply → archive）
> × **四份 DAG 依赖工件**（proposal / specs / design / tasks）
> × **Delta Spec 增量机制**（棕地友好，ADDED/MODIFIED/REMOVED）
> × **31 平台 Skills 分发**（一份规范多平台执行）

把"需求对齐"从口头约定变成可机器消费的结构化文档，是 OpenSpec 的本质贡献。

## 关联连接

- [[OpenSpec]] — 核心框架实体
- [[delta-spec]] — 增量变更机制
- [[FissionAI]] — 开源方
- [[SpecKit]] — 兄弟方案，让规范可执行
- [[Superpowers]] — 兄弟方案，管"怎么干"
- [[SpecSuperflow]] — 与 Superpowers 的融合插件
- [[规范驱动开发]] — 上层方法论
- [[AICoding]] — AI 辅助编程范式
- [[OpenCode]] — 支持 OpenSpec 的编程工具
- [[ClaudeCode]] — 主要承载平台
- [[摘要-OpenSpec规范驱动AI编程框架]] — 来源
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比来源
- [[摘要-spec-superflow-融合工作流]] — 融合方案来源
- [[摘要-spec-superflow-融合工作流-源码级详解]] — 源码级深度解读
