---
title: "重型项目最优框架组合：OpenSpec + CodeGraph + Matt Pocock Skills"
type: synthesis
tags: [OpenSpec, CodeGraph, MattPocock, 框架选型, 重型项目, 绝对主动权, 棕地项目, 日志收集, 实操指南]
sources:
  - wiki/entities/OpenSpec.md
  - wiki/entities/CodeGraph.md
  - wiki/entities/MattPocock.md
  - wiki/entities/mattpocock-skills.md
  - wiki/entities/GrillMe.md
  - wiki/entities/GSDCore.md
  - wiki/entities/SpecSuperflow.md
  - wiki/syntheses/openspec-brownfield-usage-guide.md
  - wiki/syntheses/openspec-working-principle.md
  - wiki/syntheses/heavy-project-impact-analysis-and-planning.md
  - wiki/concepts/流程税.md
  - wiki/concepts/强模型时代工作流选型.md
  - wiki/sources/摘要-mattpocock-skills.md
last_updated: 2026-08-28
---

# 重型项目最优框架组合：OpenSpec + CodeGraph + Matt Pocock Skills

> **核心问题**：重型棕地项目，需求来了不知道怎么做，方案试错成本高（写到一半发现走不通），改代码发现影响其他代码要重构，同事有的用 AI 有的不用需要混合协作，要求对 AI 产出有绝对主动权。GSD Core 等"接管流程"型框架不满意。什么是最优框架组合？

## 一、用户真实需求的 4 个硬约束

以"集团下发日志收集需求（4 种日志：登录/权限/前端操作/前端数据流转）"为典型场景，提炼出 4 个硬约束：

| 约束 | 典型表现 | 本质需求 |
|------|---------|---------|
| ① 需求来了不知道怎么做 | "集团给了采集文档，我看了项目不知道该咋做" | 需要**需求拆解+技术方案探索**引导 |
| ② 方案试错成本高 | "用注解→发现字段拿不到→放弃→改拦截器" | 需要**动手前先分析可行性**，而不是写一半发现走不通 |
| ③ 绝对主动权 | "AI 写的代码我也要足够了解，有绝对主动权" | 拒绝"框架接管流程"，要**人主导+AI 辅助** |
| ④ 同事混合协作 | "有的用 AI 有的不用，相互配合" | 产出物必须是**人类可读的规范文档**，不能是只有 AI 懂的内部状态 |

## 二、为什么 GSD Core / SpecSuperflow 不满意

根据 [[GSDCore]] 和 [[MattPocock]] 的批评：

- **GSD Core**：属于"接管流程"型框架（[[MattPocock]] 批评"帮你接管整套流程，代价是控制权被拿走，流程本身出了 bug 你还很难修"），违背约束③
- **SpecSuperflow**：八状态机自动驱动，太重，用户反馈"plan mode 直接实现代码还是不全面"——问题不在流程不够重，而在**没有事前分析影响面**（约束②未解决）
- **Matt Pocock 单独用**：`/grill-with-docs` 能澄清需求，但没有**规划文档存档**，同事看不到你为什么这么决策（约束④未解决）

## 三、最优组合：OpenSpec + CodeGraph + Matt Pocock Skills

### 组合构成

| 工具 | 定位 | 解决的约束 | 核心命令 |
|------|------|-----------|---------|
| [[OpenSpec]] | 规划引擎（想清楚再动手+存档） | ①②③④ | `/opsx:explore` `/opsx:propose` `/opsx:apply` `/opsx:archive` |
| [[CodeGraph]] | 变更影响分析（动手前知道影响面） | ② | `codegraph impact <符号> --depth 2` |
| [[MattPocock]] Skills | 执行纪律箱（按需调用） | ③ | `/tdd` `/code-review` `/grill-with-docs` |

### 为什么是这个组合

| 约束 | 对应工具 | 解决方式 |
|------|---------|---------|
| ① 不知道怎么做 | OpenSpec `/opsx:explore` | 纯对话探索需求，AI 帮你理清"集团要什么→项目现状→该怎么落地" |
| ② 方案试错成本高 | OpenSpec `/opsx:propose` | 动手前先产出 design.md 技术方案，审查通过才写代码 |
| ② 改了怕影响其他代码 | CodeGraph `codegraph impact` | 事前分析变更影响面，不写一半才发现要重构 |
| ③ 绝对主动权 | OpenSpec 人工确认门 + Matt Pocock 纪律箱 | 每阶段你审批才推进，skill 是工具不是框架 |
| ④ 同事混合协作 | OpenSpec 的 spec 文档 | 产出的是人类可读的 markdown 规范，不用 AI 的同事也能看 |

### 组合的本质

> **OpenSpec 管"想清楚再动手"（规划+存档），CodeGraph 管"动手前知道影响面"（影响分析），Matt Pocock Skills 管"动手时的代码质量"（纪律箱）。三者都是工具，你按需调用，没有任何框架接管你的流程。**

### 设计哲学依据

根据 [[强模型时代工作流选型]] 和 [[流程税]]，强模型时代应采用**分层工作流按需加载**，而非无脑常驻全套重流程。本组合遵循这一原则：
- 简单修改 → 直接用模型原生能力
- 需求模糊 → OpenSpec explore + Matt Pocock grill-with-docs
- 高风险改动 → OpenSpec 完整规划 + CodeGraph 影响分析 + Matt Pocock tdd/code-review

## 四、具体使用方法（以日志收集需求为例）

### 第 0 步：安装三个工具

```bash
# 1. 安装 OpenSpec 中文版
npm install -g @studyzy/openspec-cn@latest
cd /your-project
openspec-cn init --tools claude    # 你用的 AI 工具

# 2. 安装 CodeGraph
npm install -g @colbymchenry/codegraph
codegraph init -i                   # 初始化项目索引

# 3. 安装 Matt Pocock Skills（选装，执行时用）
npx skills@latest add mattpocock/skills
# 选择：grill-with-docs, tdd, code-review
```

### 第 1 步：探索需求 — `/opsx:explore`

```
/opsx:explore 集团要求收集4种日志：登录日志、权限管理日志、前端操作日志、前端数据流转日志。
集团只给了采集文档，我看了项目不知道该怎么落地。
帮我分析：这4种日志各自的采集点在哪，用什么技术方案最合适。
```

AI 会帮你理清：
- 4 种日志的采集点分别在哪（登录=认证模块、权限=鉴权模块、操作=Controller 层、流转=跨系统调用）
- 每种日志的技术方案选项（注解 vs 拦截器 vs AOP vs 异步监听）
- AI 会探索你的代码库，告诉你现有项目结构适合作哪种方案

> 这一步解决约束①"不知道该咋做"。纯对话，不写代码。

### 第 2 步：生成规划工件 — `/opsx:propose`

```
/opsx:propose 实现日志收集系统：4种日志分别采用不同采集策略
```

AI 产出四份文档（在 `opsx/changes/log-collection/` 下）：

| 文件 | 内容 | 审查重点 |
|------|------|---------|
| `proposal.md` | 为什么做（集团要求）+ 做什么（4 种日志） | 动机对不对 |
| `specs/spec.md` | 具体需求，用 SHALL/MUST + Given/When/Then | **4 种日志的采集场景有没有漏** |
| `design.md` | 技术方案 | **注解 vs 拦截器的选择理由，字段能不能拿到** |
| `tasks.md` | 任务清单 | 步骤是否可执行 |

> 这一步解决约束②"方案试错成本高"。在写代码前，design.md 里就会写清楚"操作日志用注解（字段够）、流转日志用拦截器（需要请求上下文）、登录/权限用异步保存（接口少）"。**你审查 design.md 时就能发现"注解拿不到某些字段"的问题，而不用写到一半才放弃**。

### 第 3 步：变更影响分析 — `codegraph impact`

在审查 design.md 时，如果方案要改现有的登录接口或权限拦截器：

```bash
# 分析改这个函数会影响哪些代码
codegraph impact LoginController.login --depth 2

# 分析改权限拦截器的影响面
codegraph impact PermissionInterceptor.check --depth 2

# 看谁调用了你要改的方法
codegraph callers UserService.getUserInfo
```

> 这一步解决约束②"改了发现影响其他代码要重构"。在动手前就知道影响面，design.md 里就能写清楚"改 LoginController 会影响 XX、XX、XX 三处调用方"。

### 第 4 步：人工确认（绝对主动权）

审查四份文档 + 影响分析结果：
- spec.md：4 种日志场景有没有遗漏？
- design.md：技术方案是否可行？（注解能不能拿到字段？）
- codegraph impact：影响面你能不能接受？
- tasks.md：步骤你认同吗？

**不通过就改**，告诉 AI "design.md 里操作日志的注解方案拿不到响应时间字段，改成拦截器方案"。

**通过后才说**："通过，开始实现"。

> 这一步解决约束③"绝对主动权"。每阶段你审批才推进。

### 第 5 步：按清单实现 — `/opsx:apply`

```
/opsx:apply
```

AI 按 tasks.md 逐项实现，每完成一项更新进度。你随时可以叫停，因为任务清单是你审过的。

如果执行中想要代码质量纪律，按需调用 Matt Pocock 的 skill：
- `/tdd` — 先写测试再实现（流转日志拦截器的测试）
- `/code-review` — 实现完审查代码质量

### 第 6 步：归档 — `/opsx:archive`

```
/opsx:archive
```

把整个 `opsx/changes/log-collection/` 移入 `opsx/archive/`。

> 这一步解决约束④"同事混合协作"。不用 AI 的同事也能打开 `opsx/archive/log-collection/design.md` 看懂"为什么流转日志用拦截器而不用注解"。这是人类可读的规范文档，不是 AI 的内部状态。

## 五、完整工作流一览

```
集团下发日志收集需求
    │
    ├─ /opsx:explore                    # OpenSpec：探索4种日志怎么落地
    │    → AI 分析你项目现状，给出方案选项
    │
    ├─ /opsx:propose                    # OpenSpec：生成规划工件
    │    → proposal.md / spec.md / design.md / tasks.md
    │    → design.md 里写清：操作日志=注解、流转日志=拦截器、登录/权限=异步
    │
    ├─ codegraph impact <符号>          # CodeGraph：分析改现有代码的影响面
    │    → 改 LoginController 会影响哪些调用方
    │
    ├─ 【人工确认】                      # 你的绝对主动权
    │    → 审查 spec + design + 影响分析
    │    → 不通过就改，通过才推进
    │
    ├─ /opsx:apply                      # OpenSpec：按 tasks.md 逐项实现
    │    → 可选：/tdd 先写测试、/code-review 审查质量
    │
    └─ /opsx:archive                    # OpenSpec：归档
         → 同事打开 design.md 就能看懂决策原因
```

## 六、对比：为什么这个组合优于 GSD Core

| 维度 | GSD Core | OpenSpec + CodeGraph + Matt Pocock |
|------|---------|-----------------------------------|
| 控制权 | 框架接管流程，你跟着走 | **你主导**，每步你审批才推进 |
| 需求探索 | `/gsd-discuss-phase`（较重） | `/opsx:explore`（纯对话，轻量） |
| 影响分析 | ❌ 没有 | ✅ `codegraph impact` 事前分析 |
| 方案试错 | 边写边发现走不通 | **design.md 先审查再动手** |
| 同事协作 | 产出是 AI 内部状态 | **产出是人类可读的 markdown** |
| 代码纪律 | 不专注 | `/tdd` `/code-review` 按需调用 |
| 重量 | 重（接管流程） | **轻**（工具箱，按需用） |

## 七、与已有 synthesis 的关系

- [[heavy-project-impact-analysis-and-planning]] — 之前推荐的 CodeGraph + GSD Core 组合，本文用 OpenSpec 替代 GSD Core（用户反馈不满意接管流程型框架）
- [[openspec-brownfield-usage-guide]] — OpenSpec 棕地项目使用方案，本文在此基础上加入 CodeGraph 影响分析和 Matt Pocock 纪律箱
- [[openspec-working-principle]] — OpenSpec 工作原理，本文是其落地应用
- [[project-analysis-planning-tool-selection]] — 结合项目分析的工具选型，本文是其修正版（用户反馈后的最终结论）

## 八、核心认知

1. **"不知道怎么做"的根因是缺乏结构化探索**，不是缺乏流程管控。OpenSpec 的 explore 模式解决这个。
2. **"方案试错成本高"的根因是动手前没分析可行性**，不是流程不够重。OpenSpec 的 design.md + CodeGraph 的 impact 解决这个。
3. **"绝对主动权"的对立面是"框架接管流程"**，所以必须选工具箱型而非流水线型。OpenSpec 的人工确认门 + Matt Pocock 的纪律箱解决这个。
4. **"同事混合协作"要求产出人类可读文档**，只有 OpenSpec 的 spec 文档满足，GSD Core 的内部状态不满足。

## 关联连接

- [[OpenSpec]] - 规划引擎（组合核心）
- [[CodeGraph]] - 变更影响分析
- [[MattPocock]] - 执行纪律箱作者
- [[mattpocock-skills]] - 执行纪律箱仓库
- [[GrillMe]] - 需求澄清 skill（可选）
- [[GSDCore]] - 被否决的方案（接管流程型）
- [[SpecSuperflow]] - 被否决的方案（太重）
- [[openspec-brownfield-usage-guide]] - OpenSpec 棕地使用方案
- [[openspec-working-principle]] - OpenSpec 工作原理
- [[heavy-project-impact-analysis-and-planning]] - 前一版推荐（已修正）
- [[project-analysis-planning-tool-selection]] - 前一版选型（已修正）
- [[流程税]] - 避免重流程的理论依据
- [[强模型时代工作流选型]] - 分层加载方法论
- [[delta-spec]] - OpenSpec 增量变更机制
- [[规范驱动开发]] - 上层方法论
- [[ClaudeCode]] - 承载平台
