---
title: "OpenSpec + Matt 轻量执行：init 与 setup 配置 FAQ"
type: synthesis
tags: [OpenSpec, MattPocock, setup-matt-pocock-skills, tdd, code-review, 轻量执行, FAQ, 实操问答]
sources:
  - wiki/syntheses/openspec-matt-skills-execution-workflow.md
  - wiki/syntheses/agent-spec-framework-comparison-and-matt-skills-workflow.md
  - wiki/syntheses/optimal-framework-combination-heavy-project.md
  - wiki/sources/摘要-matt-openspec配合开发教程.md
  - C:\Users\w1217\.agents\skills\setup-matt-pocock-skills\SKILL.md
  - C:\Users\w1217\.agents\skills\to-tickets\SKILL.md
  - C:\Users\w1217\.agents\skills\code-review\SKILL.md
  - C:\Users\w1217\.agents\skills\wayfinder\SKILL.md
  - C:\Users\w1217\.agents\skills\triage\SKILL.md
last_updated: 2026-09-07
---

# OpenSpec + Matt 轻量执行：init 与 setup 配置 FAQ

> **核心问题**：当工作流是"OpenSpec 管需求规划 + Matt 只用 tdd/code-review 做执行纪律"时，两个工具的安装配置怎么搞？OpenSpec 要不要 init？Matt 要不要跑 `/setup-matt-pocock-skills`？setup 生成的 `domain.md` / `issue-tracker.md` / `triage-labels.md` 还有用吗？

## 一、场景定位

本文针对的是**轻量组合**工作流：

```
OpenSpec:  explore → propose → 人工审查 → apply → archive   （管规划全流程）
Matt:      tdd（执行时）→ code-review（实现后）              （只做执行纪律）
```

**不使用** Matt 的工程类 skill：`to-tickets`、`to-spec`、`triage`、`wayfinder`、`domain-modeling`（规划走 OpenSpec，不用 Matt 的规划能力）。

这是 [[optimal-framework-combination-heavy-project]] 推荐组合的常见落地形态，也是 [[openspec-matt-skills-execution-workflow]] 三种配合方式中"方式一：执行前约定"的典型用法。

## 二、FAQ-1：OpenSpec 和 Matt 的 init 要不要做？

### 结论：OpenSpec 必须 init，Matt 没有 init

| 工具 | 安装模式 | 是否需要项目初始化 | 命令 |
|------|---------|------------------|------|
| **OpenSpec** | 全局装 CLI + **项目 init** 生成 `opsx/` 工作区 | ✅ **必须** | `openspec-cn init --tools claude` |
| **Matt Skills** | **直接拷进项目**（skills.sh）或插件订阅 | ❌ **没有 init 步骤** | `npx skills@latest add mattpocock/skills` |

### 为什么不同

根据 [[openspec-matt-skills-execution-workflow]] 的对比：

> Matt Skills **不是** OpenSpec 那种"全局装 CLI + 项目 init"模式，没有 init 步骤。

- **OpenSpec** 是**规划引擎**，需要 `opsx/` 工作区目录来存放 `specs/`、`changes/`、`archive/` 等规划工件，所以必须 init 生成目录结构
- **Matt Skills** 是**纪律箱**，设计哲学是"把 skill 当纪律，不当框架"（[[mattpocock-skills]]），按需调用，不接管流程，所以不需要初始化工作区

### 具体操作

```bash
# 1. OpenSpec（需要 init）
npm install -g @studyzy/openspec-cn@latest
cd /your-java-project
openspec-cn init --tools claude   # 生成 opsx/ 目录

# 2. Matt Skills（不需要 init，拷进来就用）
npx skills@latest add mattpocock/skills
# 选：tdd, code-review（你用到的执行纪律）
# 可选：grill-with-docs, diagnosing-bugs
```

Matt 的 SKILL.md 文件会被拷到项目的 `.claude/skills/` 下，拷进来就能用。

### 完整工作流

```
/opsx:explore          # OpenSpec：探索需求
/opsx:propose          # OpenSpec：生成规划工件
【人工审查】
/opsx:apply + /tdd     # OpenSpec 按清单 + Matt 强制 TDD
/code-review           # Matt：代码审查
/opsx:archive          # OpenSpec：归档
```

**一句话**：OpenSpec 要 init，Matt Skills 只要装不要 init，两者各司其职。

## 三、FAQ-2：setup-matt-pocock-skills 生成的三个文件有用吗？

### 背景

用户跑了 `/setup-matt-pocock-skills`，在项目下生成了三个文件：
- `docs/agents/domain.md`
- `docs/agents/issue-tracker.md`
- `docs/agents/triage-labels.md`

### 结论：轻量组合下这三个文件没用，可以删掉

| 文件 | 服务的 skill | 轻量组合下是否用到 |
|------|------------|------------------|
| `issue-tracker.md` | `to-tickets`、`to-spec`、`triage`、`wayfinder`、`code-review`（读 commit issue 引用） | ❌ 规划走 OpenSpec，不用 Matt 的 to-tickets/to-spec；code-review 只在用 issue 关联 commit 时才读 |
| `triage-labels.md` | `triage`（issue 分诊） | ❌ 不用 triage |
| `domain.md` | `domain-modeling`（CONTEXT.md/ADR 布局规则） | ⚠️ 只有跑 `/domain-model` 时才读，轻量组合不用 |

### 这三个文件是给谁准备的

根据 `setup-matt-pocock-skills/SKILL.md` 源码（`C:\Users\w1217\.agents\skills\setup-matt-pocock-skills\SKILL.md`），这个 setup skill 是给**全套 Matt 工程流**准备的配套配置：

```
setup-matt-pocock-skills 配置的文件  →  服务的 skill
├─ issue-tracker.md                  →  to-tickets / to-spec / triage / wayfinder / code-review
├─ triage-labels.md                  →  triage（issue 分诊标签）
└─ domain.md                         →  domain-modeling（CONTEXT.md/ADR 布局）
```

各 skill 对这三个文件的依赖（源码验证）：

- **`to-tickets`**（`SKILL.md:11`）："The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`."
- **`to-spec`**（`SKILL.md:9`）：同上
- **`wayfinder`**（`SKILL.md:25`）："The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`."
- **`triage`**（`SKILL.md:43`）："The mapping should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`."
- **`code-review`**（`SKILL.md:13`）："If `docs/agents/issue-tracker.md` is missing, tell the user to run `/setup-matt-pocock-skills`."——但这里只是用来从 commit message 里提取 `#123` issue 引用，不用 issue tracker 的话这块是空的

### 对照轻量组合：为什么没用

你的流程：
```
OpenSpec: explore → propose → 人工审查 → apply → archive
Matt:     tdd（执行时）→ code-review（实现后）
```

逐个 skill 核对：

| 你用到的 Matt skill | 是否读这三个文件 | 说明 |
|--------------------|----------------|------|
| `tdd` | ❌ 不读 | 只管"先写失败测试再写实现"，不依赖配置文件 |
| `code-review` | ⚠️ 只读 `issue-tracker.md` | 用于从 commit message 提取 issue 引用；不用 issue 关联 commit 则为空 |
| `grill-with-docs`（可选） | ❌ 不读 | 只做需求盘问对齐 |
| `diagnosing-bugs`（可选） | ❌ 不读 | 只做系统化调试 |

**你根本没装也没用的 skill**（这三个文件真正服务的）：
- `to-tickets` —— 你用 OpenSpec 的 propose 生成 tasks.md，不用 to-tickets
- `to-spec` —— 你用 OpenSpec 的 propose 生成 spec.md，不用 to-spec
- `triage` —— 你不做 issue 分诊
- `wayfinder` —— 你不做大型决策地图
- `domain-modeling` —— 轻量组合不用（如需领域建模可直接告诉 AI，不一定要 domain.md）

### 建议

**直接删掉 `docs/agents/` 整个目录**，理由：
1. 规划走 OpenSpec（`opsx/` 工作区），不走 Matt 的 to-tickets/to-spec/wayfinder
2. 不用 triage 分诊
3. `tdd` 不依赖这些文件
4. `code-review` 唯一用到的是 issue-tracker（读 commit 里的 issue 引用），不用这块则为空

**唯一例外**：如果后续想用 `/domain-model` 梳理领域概念，它会读 `domain.md` 来知道 `CONTEXT.md` 放哪。但这个也可以直接告诉它，不一定要文件。

### 顺便：setup-matt-pocock-skills 本身的定位

`setup-matt-pocock-skills` 是给**全套 Matt 工程流**（to-tickets → triage → wayfinder → to-spec）准备的配套配置。只用 `tdd` + `code-review` 两个执行纪律箱属于"轻量使用"，跑这个 setup 是**过度配置**。

> `ask-matt/SKILL.md:90` 原文："`/setup-matt-pocock-skills`: run before your first engineering flow to configure the issue tracker, triage labels, and doc layout the other skills assume."

关键词是 "the other skills"——指的是工程类 skill（to-tickets/triage/wayfinder/to-spec），不是 tdd/code-review。

## 四、决策速查表

| 你的情况 | OpenSpec init | Matt setup | 保留 docs/agents/ |
|---------|--------------|-----------|------------------|
| OpenSpec 管规划 + Matt 只用 tdd/code-review | ✅ 必须 | ❌ 不需要 | ❌ 删掉 |
| OpenSpec 管规划 + Matt 用 tdd/code-review/domain-model | ✅ 必须 | ⚠️ 可选 | ⚠️ 只留 domain.md |
| 全套 Matt 工程流（to-tickets/triage/wayfinder/to-spec） | ❌ 不用 OpenSpec | ✅ 必须 | ✅ 全保留 |
| OpenSpec + 全套 Matt 工程流 | ✅ 必须 | ✅ 必须 | ✅ 全保留 |

## 五、与已有 synthesis 的关系

- [[openspec-matt-skills-execution-workflow]] —— 姊妹篇，讲 OpenSpec + Matt 的三种配合方式（apply 与 tdd 怎么穿插），本文是其安装配置环节的 FAQ 补充
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] —— 框架全景对比 + Matt 7 步流程，本文是其"轻量组合"场景的配置细化
- [[optimal-framework-combination-heavy-project]] —— 重型项目最优组合（OpenSpec + CodeGraph + Matt），本文是其"只用 OpenSpec + Matt 两件套"的轻量变体

## 关联连接

- [[OpenSpec]] — 规划引擎（需要 init）
- [[MattPocock]] — 执行纪律箱作者
- [[mattpocock-skills]] — 执行纪律箱仓库
- [[TDD]] — 测试驱动开发（执行阶段核心纪律）
- [[code-review]] — 代码审查（实现后纪律）
- [[openspec-matt-skills-execution-workflow]] — 姊妹篇：配合执行详解
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] — 框架全景对比
- [[optimal-framework-combination-heavy-project]] — 重型项目最优组合
- [[摘要-matt-openspec配合开发教程]] — 配合开发教程来源
- [[规范驱动开发]] — 上层方法论
- [[AICoding]] — AI 辅助编程范式
