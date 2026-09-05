---
title: "OpenSpec 归档需求修改流程与 Token 成本权衡"
type: synthesis
tags: [OpenSpec, 规范驱动, Token消耗, 成本权衡, 决策指南, SpecRot]
sources:
  - raw/09-archive/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/09-archive/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
  - raw/09-archive/开源了！Claude Code 最佳实践 60 天斩获 54k Star，前后端开发直接起飞了！.md
  - raw/09-archive/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md
last_updated: 2026-07-29
---

# OpenSpec 归档需求修改流程与 Token 成本权衡

> **核心问题**：[[OpenSpec]] 走完一轮 `/opsx:archive` 后，需求又要改怎么办？这套规范驱动流程会增加多少 token 消耗？相比直接问智能体干活，多出来的 token 开销到底值不值？

## 一、已归档需求的修改流程

### 核心原则：不要直接手改 archive 目录中的归档文档

[[OpenSpec]] 的工件依赖关系是"使能"而非"卡死"--随时可回去修改前面工件。但归档后的需求如需变更，**标准做法是用 [[delta-spec]] 增量变更机制**，而非直接编辑归档文件。直接改归档文档会丢失"为什么改"的上下文，delta spec 才能显式记录差异和理由。

### 使用者操作流程

**前提**：项目已用 OpenSpec 走过一轮 `propose -> apply -> archive`，`opsx/archive/` 目录里已有归档基线。现在需求要改。

#### 步骤 1：探索变更意图 `/opsx:explore`

用对话方式理清"这次要改什么、为什么改"。明确是新增功能、修改既有行为、还是删除某块需求。此步产物为纯对话，不生成文件。

#### 步骤 2：生成 Delta Spec 提案 `/opsx:propose`

此时 OpenSpec 不会让你重写整份 spec，而是产出 **delta spec**--用三个标记描述差异（见 [[delta-spec]]）：

- `ADDED`：新增的需求条目
- `MODIFIED`：要修改的既有条目
- `REMOVED`：要删除的条目

生成的制品仍是四件套（proposal.md / specs/spec.md / design.md / tasks.md），但内容是"相对于已归档基线改了什么"。

#### 步骤 3：人工确认（关键检查点）

审阅 delta 提案，确认变更范围和理由无误。这是规划阶段唯一的人工介入点（[[DP-3]]）。

#### 步骤 4：按清单实现 `/opsx:apply`

按 tasks.md 逐项执行，生成/修改实际代码，同时更新 tasks 进度。

#### 步骤 5：同步 delta 到主 spec `/opsx:sync`

将 delta spec 合并回主 spec，让主规范保持最新，避免规范腐烂。[[SpecSuperflow]] 中的 spec-merger 组件正是负责这一步。

#### 步骤 6：重新归档 `/opsx:archive`

将本次变更的规划文档移入 archive 目录，形成新的基线版本。

### 流程速记

> explore（理清改什么）-> propose（生成 delta）-> 人工确认 -> apply（改代码）-> sync（合并规范）-> archive（新基线）

### 小改动走快速路径

如果用的是 [[SpecSuperflow]]，hotfix（≤2 文件）和 tweak（≤4 文件纯配置）可跳过完整流程，直接快速处理，避免小改动也走完整规划工件。

## 二、Token 成本权衡：相比直接问智能体干活的得失

### 确实会增加 token 消耗

使用 OpenSpec，每次变更会额外产生四份规划文档（proposal.md / specs/spec.md / design.md / tasks.md），AI 需要读取、生成、维护这些文档。归档后修改还要走 delta spec 流程。这些都是额外 token 开销。

### 但直接问智能体干活的隐性成本更高

根据 [[摘要-claude-code-best-practice-苏三视角]]，关键数据是：

> Context rot 在 300-400k token 处显现，维持总 context 利用率 < 40%，超过 300k 立即 `/compact`

直接问智能体干活有三大隐性成本：

#### 1. 返工才是最大的 token 黑洞

直接问智能体，它容易"跳步骤、乱改架构、质量靠运气"（见 [[规范驱动开发]] 对 [[VibeCoding]] 的批判）。一次返工重写的 token，往往比前期做规划花的多得多。OpenSpec 的"未对齐需求禁止动手"原则，本质是用少量规划 token 换大量返工 token。

#### 2. 上下文腐烂导致质量螺旋下降

长会话里直接干活，上下文越堆越长，智能体开始遗忘前面的约定、重复犯已纠正的错。OpenSpec 的规划文档是**结构化、可复用**的--新开会话只注入相关 spec 片段，而不是把整个混乱的对话历史塞进去。这正是"Plan 与 Execute 分 Session"理念的系统化实现（见 [[摘要-claude-code-best-practice-苏三视角]]）。

#### 3. 变更可追溯 = 后续维护省 token

没有 spec 归档，下次改需求时智能体得重新"理解"整个项目。有了 [[delta-spec]]，智能体只需读 delta，明确"改了什么"，不必重新加载全部上下文。

### 对比表

| 维度 | 直接问智能体 | OpenSpec 规范驱动 |
|------|------------|----------------|
| 前期 token | 少 | 多（生成四件套） |
| 返工概率 | 高（需求未对齐就动手） | 低（先对齐再写） |
| 上下文腐烂 | 快（长会话堆叠） | 慢（分 Session + 精确注入） |
| 变更可追溯 | 无 | 有（delta spec 闭环） |
| 适合场景 | 一次性小脚本 | 中大型项目、多次迭代 |

### 结论

**小活儿别用 OpenSpec**--改个配置、写个脚本，直接问智能体更快，规划开销不划算。

**中大型项目、需求会反复变更的场景，OpenSpec 的额外 token 是"保险费"**--它买的不是文档，是"减少返工"和"上下文质量可控"。一次返工省下来的 token，够做好几轮规划。

用 [[SpecSuperflow]] 的话还有 hotfix/tweak 快速路径，让小改动不必走完整流程，进一步降低不必要的 token 开销。

## 三、跳过流程的代价：未记录小改动与 spec rot

上面的结论"小活儿别用 OpenSpec"有一个重要前提必须说清--**跳过流程的改动，OpenSpec 不会自动知道**。

### spec rot（规范腐烂）风险

OpenSpec 的 spec 是**静态文档**，不会自动扫描代码变更。小改动绕过 OpenSpec 直接改了代码，spec 和实际代码就会脱节，这就是规范腐烂。[[摘要-spec-superflow-融合工作流]] 中提到 spec-merger 组件正是为了"防规范腐烂"，但它的前提是改动走了 delta spec 流程；**绕过流程的改动，spec-merger 也救不了**。

### 后续大改动时的补救：靠手动引导 + delta 补录

虽然不能自动感知，但有手动对齐机制（见 [[openspec-brownfield-usage-guide]] 的补录策略）。

**重要前提**：`/opsx:explore` 本身是**纯对话式探索工具**（见 [[OpenSpec]] 的定义），它**不会自动扫描代码**去对比 spec 和实际实现的差异。OpenSpec 没有内置"代码-spec 一致性校验"能力。以下补录流程需要你主动引导：

1. **explore 阶段手动要求差异核对**：大改动开始走 `/opsx:explore` 时，**你主动在对话中要求** AI 对比当前代码和 `opsx/specs/` 主规范，找出"代码已改但 spec 没记录"的差异。例如："先读 `opsx/specs/order/spec.md`，再扫 `src/order/` 实际代码，告诉我哪里不一致。"是**你发起的指令**让 AI 去比对，不是 explore 命令自带的功能。
2. **用 delta spec 的 MODIFIED 补录**：把这些未记录的小改动作为 delta 的 MODIFIED 条目写进去，相当于"补作业"。
3. **sync 合并回主 spec**：`/opsx:sync` 把补录内容合并回主规范，消除脱节。

> 本质上，OpenSpec 依赖"人工诚实"--你跳过了流程，就得在大改动时主动引导 AI 补录，否则 spec 就是假的。

### 跳过 vs 走流程的真实权衡

| 做法 | 风险 |
|------|------|
| 小改动绕过 OpenSpec | 省了当下 token，但积累 spec rot，大改动时 AI 读到的是过期规范，可能基于错误前提实现 |
| 小改动也走流程 | token 开销大，但 spec 始终可信 |

### 实践建议

- **真正琐碎的改动**（改个文案、调个常量）：绕过无妨，影响极小。
- **改变了行为的改动**（哪怕只改一行逻辑）：建议至少在 `opsx/specs/` 里留个 MODIFIED 痕迹，或用 [[SpecSuperflow]] 的 tweak 快速路径（≤4 文件纯配置），轻量记录而非完全跳过。
- **定期对齐**：大改动前在 explore 中**主动要求** AI 做差异核对，把积累的脱节一次性补录。

⚠️ OpenSpec 本身没有"代码 spec 一致性自动校验"功能，这依赖人工纪律。知识库中关于自动检测 spec rot 的能力记录有限，以上补录流程是基于 [[delta-spec]] 和 [[openspec-brownfield-usage-guide]] 补录策略的推导。

## 关联连接

- [[OpenSpec]] - 核心框架
- [[delta-spec]] - 增量变更机制（归档修改的关键）
- [[规范驱动开发]] - 上层方法论
- [[摘要-claude-code-best-practice-苏三视角]] - Context rot 数据与 Plan/Execute 分离理念
- [[ContextEngineering]] - 上下文工程认知
- [[VibeCoding]] - 直接问智能体的对立面
- [[SpecSuperflow]] - hotfix/tweak 快速路径
- [[openspec-brownfield-usage-guide]] - 配套：棕地项目完整使用方案
- [[摘要-OpenSpec规范驱动AI编程框架]] - OpenSpec 来源
- [[摘要-spec-superflow-融合工作流]] - SpecSuperflow 来源
- [[摘要-superpowers-openspec-speckit对比]] - 三方对比
- [[ClaudeCode]] - 承载平台
- [[ContextManagement]] - 上下文管理（互补方案）
