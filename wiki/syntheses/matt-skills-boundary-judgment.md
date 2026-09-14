---
title: "Matt Skills 边界判断：什么时候用哪个 skill，什么时候跳过"
type: synthesis
tags: [MattPocock, TDD, implement, 测试seam, 边界判断, 实操经验, 跳步规则]
sources:
  - wiki/concepts/TDD.md
  - wiki/sources/摘要-mattpocock-skills.md
  - wiki/syntheses/openspec-matt-skills-execution-workflow.md
  - wiki/syntheses/agent-spec-framework-comparison-and-matt-skills-workflow.md
  - wiki/syntheses/openspec-matt-lightweight-setup-faq.md
  - C:\Users\w1217\.agents\skills\tdd\SKILL.md
  - C:\Users\w1217\.agents\skills\tdd\tests.md
  - C:\Users\w1217\.agents\skills\implement\SKILL.md
last_updated: 2026-09-14
---

# Matt Skills 边界判断：什么时候用哪个 skill，什么时候跳过

> **核心问题**：TDD skill 要求"先确认测试 seam"但项目无测试基础设施且改动是纯声明式 UI 代码时怎么办？`/implement` 和 `/tdd` 有什么区别？`/implement` 和直接让 AI 干活有什么区别？——三个问题同属一个主题：**Matt Skills 的适用边界与跳步判断**。

## 一、TDD 无 seam 场景：什么时候应该跳过 TDD

### 问题场景

TDD skill（[[TDD]]）要求"先确认测试 seam（公共接口边界），没有确认的 seam 不写测试"。但实际开发中会遇到：

- 项目无前端测试框架（无 vitest/jest/@vue/test-utils）
- 改动是 Vue 模板中 `v-if`/`:disabled` 表达式条件调整——纯声明式 UI 代码
- AGENTS.md 明确声明"无单元测试工程，验证依赖人工与集成环境"

### TDD skill 原文对 seam 的定义

[[TDD]] skill 的 `SKILL.md:18-22` 原文：

> A **seam** is the public boundary you test at: the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.
> **Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. **No test is written at an unconfirmed seam.**

**seam = 公共接口边界**。纯声明式 UI 渲染逻辑（`v-if` 表达式）没有独立可调用的函数/模块/接口，它的 seam 是"浏览器渲染后的 DOM"，要测那个需要整套前端测试基础设施。

**关键认知**：TDD skill 自己就说了"No test is written at an unconfirmed seam"——没有确认的 seam 不写测试。**当它说"找不到 seam"时，就是在告诉你"这个改动不是 TDD 的菜"**。这不是 bug，是 TDD 的保护机制。

### 处理策略

| 步骤 | 做什么 | 为什么 |
|------|--------|--------|
| 1 | **跳过 TDD**，直接改模板表达式 | 无 seam，TDD skill 自己规定"无确认 seam 不写测试" |
| 2 | **人工验证**：启动前端，覆盖几种状态组合看 UI 表现对不对 | AGENTS.md 已声明验证依赖人工与集成环境 |
| 3 | 改完后跑 `/code-review`（如果改动涉及逻辑判断） | [[code-review]] 不依赖测试基础设施，纯静态审查 |
| 4 | 如果改动有业务逻辑判断，考虑**把条件逻辑抽成纯函数**再 TDD | 见下方"进阶方案" |

### 进阶方案：把声明式逻辑抽成纯函数再 TDD

如果 `v-if` 里的条件表达式有业务复杂度（如 `A && (B || C) && !D`），值得测：

1. **把条件表达式抽成一个纯函数**（computed 或 utils 函数），如 `shouldShowErrorMsg(state)`
2. **这个纯函数就是 seam**——明确的输入（state）和输出（boolean），可独立测试
3. **对这个纯函数做 TDD**：先写失败测试（各种 state 组合），再写实现
4. 模板里 `v-if="shouldShowErrorMsg(state)"` 只是调用这个函数

这样既遵守了 TDD 的"先确认 seam"规则，又不用装整套前端测试框架——纯函数用 Node 自带的 `assert` 或轻量测试就能跑。**但这属于重构，不是本次变更的强制要求**。

### 通用判断规则

```
改动是否有可独立测试的公共接口（函数/模块/API）？
├─ 有 → TDD 适用，先确认 seam 再 red-green
└─ 没有（纯声明式 UI / 纯配置 / 纯 SQL 字符串）
    ├─ 项目有测试基础设施 → 考虑抽函数再测（进阶方案）
    └─ 项目无测试基础设施 → 跳过 TDD，人工验证 + code-review
```

### 后端同类问题

后端如果某个模块也没有测试基础设施、或改动是纯配置/纯声明式代码（如改 `application.yml` 条件、改 SQL where 子句），也是**没有 seam** 的场景，同理跳过 TDD。

## 二、`/implement` vs `/tdd`：编排层 vs 纪律层

### 核心区别

[[摘要-mattpocock-skills]] 的两层调用架构：

| | `/implement` | `/tdd` |
|---|---|---|
| **层级** | User-invoked（编排层） | Model-invoked（纪律层） |
| **职责** | 按 spec/ticket 把代码写出来 | 强制 red→green→refactor 循环 |
| **是否强制测试** | ❌ 不强制 | ✅ 铁律：没有失败测试不准写生产代码 |
| **调用关系** | User-invoked **可以调用** Model-invoked | Model-invoked 可被调用 |
| **产出** | 实现代码 | 测试 + 实现代码 |

### `/implement` — "把活干完"

[[agent-spec-framework-comparison-and-matt-skills-workflow]] 跳步表里，`/implement` 出现在**轻量场景**：

| 场景 | 流程 |
|------|------|
| 加一个简单接口 | `/implement` 直接写 + `/code-review` |
| 需求模糊但改动小 | `/grill-with-docs` + `/implement` |

它就是"按规格/任务把代码写出来"，不强制先写测试。**适合改动小、逻辑简单、不值得写测试的场景**。

### `/tdd` — "先写失败测试，再写实现"

[[TDD]] skill 的 `SKILL.md:36-38` 三条铁律：

> - **Red before green.** Write the failing test first, then only enough code to pass it.
> - **One slice at a time.** One seam, one test, one minimal implementation per cycle.
> - **Refactoring is not part of the loop.**

强制 red→green 循环：先写跑不过的测试，再写最小实现让它通过，一次一个切片。**适合有明确 seam、逻辑有复杂度、值得写测试的场景**。

### 两者关系：`/implement` 可以内联 `/tdd` 纪律

[[openspec-matt-skills-execution-workflow]] 的"方式一：执行前约定"：

```
/implement 
注意：每一项任务都必须用 TDD 方式实现——先写失败测试，跑红，再写实现让它通过。
```

**本质是把 `/tdd` 的纪律"内联"到 `/implement` 的执行里**。`/implement` 是骨架（按清单推进），`/tdd` 是肌肉（每一项怎么写代码）。

### 什么时候用哪个

| 你的情况 | 用哪个 |
|---------|--------|
| 改动小、逻辑简单、无 seam | `/implement` 直接写 |
| 中型功能、有公共接口、逻辑有复杂度 | `/implement` + 内联 TDD 纪律，或直接 `/tdd` |
| 修 bug | `/diagnosing-bugs` 定位 → `/tdd` 修（先写重现测试） |
| 全新模块、多接口 | `/tdd` 逐个 seam 走 red-green |

## 三、`/implement` vs 直接让 AI 干活：有没有前置规格约束

### 核心区别

表面上看两者都是"让 AI 写代码"，但本质差异在**有没有前置规格约束**和**控制权在哪**。

| | `/implement` | 直接让 AI 干活 |
|---|---|---|
| **前置** | 有 spec/ticket（已对齐、已审查） | 无，只有口头需求 |
| **AI 理解偏差风险** | 低（规格已盘问对齐） | 高（AI 自己猜你想要什么） |
| **控制权** | 你在 spec 阶段已确认方案 | AI 边写边猜，你事后才发现不对 |
| **返工成本** | 低（方案提前验证过） | 高（写完才发现方向错了） |
| **可追溯性** | 有 spec 文档留痕 | 无，只有对话记录 |

### `/implement` 的前提是有 spec/ticket

`/implement` 的 SKILL.md 原文第一句：

> Implement a piece of work based on a spec or set of tickets.

**关键词："based on a spec or set of tickets"**。它不是凭空写，是**按已经对齐过的规格/工单写**。规格阶段已经把"改哪些文件、接口契约、验收标准"想清楚了，`/implement` 只是执行。

### 直接让 AI 干活 = 跳过规格，从需求直接到代码

直接跟 AI 说"帮我加个登录功能"、"改一下这个 bug"——这是**没有前置规格**的路径，承担"对不齐"的风险。

### 本质差异：解决的是 Matt 四大失败模式里的"对不齐"

[[摘要-mattpocock-skills]] 的四大失败模式：

| 失败模式 | 表现 | 修复 Skill |
|---------|------|-----------|
| **对不齐** | Agent 没做你想要的 | `/grill-with-docs`（盘问对齐） |
| 太啰嗦 | 命名冗长代码膨胀 | 共享语言 → CONTEXT.md |
| 跑不起来 | 看着对跑就崩 | `/tdd` + `/diagnosing-bugs` |
| 架构烂成泥 | 软件熵加速 | `/to-spec` + `/improve-codebase-architecture` |

**直接让 AI 干活最大的风险就是"对不齐"**。`/implement` 之所以比直接干活靠谱，是因为它**隐含了前面 grill-with-docs + to-spec 的对齐过程**，到实现阶段时"做什么"已经没有歧义了。

### 但 `/implement` 本身不强制对齐——它只是"按规格执行"

**澄清一个容易误解的点**：`/implement` 这个 skill 本身不做对齐，它假设规格已经准备好了。如果跳过 grill/to-spec 直接 `/implement`，那它和"直接让 AI 干活"的差距就很小了——都是凭口头需求写代码。

[[agent-spec-framework-comparison-and-matt-skills-workflow]] 跳步表能看出这个层级：

| 场景 | 流程 |
|------|------|
| 中型功能 | grill → domain-model → to-spec → 审查 → tdd/implement → code-review |
| 加一个简单接口 | `/implement` 直接写 + `/code-review` |
| 修 bug | `/diagnosing-bugs` → `/tdd` |

**简单接口可以直接 `/implement`**——因为简单到不需要规格对齐，AI 不会猜错。但中型功能必须走完对齐流程，`/implement` 才有意义。

### 什么时候直接干活就行，什么时候该走 `/implement`

| 你的情况 | 建议 |
|---------|------|
| 改一行代码、改个文案、调个样式 | 直接让 AI 干，不用任何 skill |
| 加个简单 CRUD 接口、改个简单 bug | 直接 `/implement` 或直接干活都行，差别不大 |
| 中型功能（多模块、有业务逻辑、有接口契约） | 必须先 grill/to-spec 对齐，再 `/implement` |
| 需求模糊、你自己都没想清楚 | 先 `/grill-with-docs` 盘问，别急着 implement |
| 全新模块、架构决策多 | grill → domain-model → to-spec → 审查 → implement + tdd |

## 四、总结：Matt Skills 的边界判断速查表

| 改动类型 | 有无 seam | 项目测试基础设施 | 推荐路径 |
|---------|----------|----------------|---------|
| 纯声明式 UI（v-if/样式/文案） | 无 | 无 | 直接改 + 人工验证 |
| 纯配置（yml/properties） | 无 | 无 | 直接改 + 人工验证 |
| 简单 CRUD 接口 | 有 | 有 | `/implement` + `/code-review` |
| 简单 CRUD 接口 | 有 | 无 | `/implement` + 人工验证 + `/code-review` |
| 中型功能（多模块） | 有 | 有 | grill → to-spec → 审查 → `/tdd` → `/code-review` |
| 中型功能（多模块） | 有 | 无 | grill → to-spec → 审查 → `/implement` + 人工验证 → `/code-review` |
| 复杂业务逻辑（无 seam 但值得测） | 可造 seam | 无 | 抽纯函数 → 对纯函数 `/tdd` |
| 修 bug | 有 | 有 | `/diagnosing-bugs` → `/tdd`（先写重现测试） |
| 修 bug | 无 | 无 | `/diagnosing-bugs` → 直接改 + 人工验证 |

**核心原则**（来自 [[mattpocock-skills]] 设计哲学）：
> **"把 skill 当纪律，不当框架"**——skill 不该被供着，而是随时可替换、可组合、可 hack 的一次性纪律。按需调用，不硬套，不强制全套。

## 关联连接

- [[TDD]] — 测试驱动开发（seam 定义与 red-green 循环）
- [[mattpocock-skills]] — 执行纪律箱仓库（设计哲学来源）
- [[摘要-mattpocock-skills]] — Matt Skills 来源（四大失败模式 + 两层架构）
- [[openspec-matt-skills-execution-workflow]] — OpenSpec + Matt 配合执行详解（apply 与 tdd 三种配合方式）
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] — 框架全景对比 + Matt 7 步流程 + 跳步表
- [[openspec-matt-lightweight-setup-faq]] — 轻量组合配置 FAQ（只装用得到的 skill）
- [[code-review]] — 代码审查（不依赖测试基础设施的静态审查）
- [[MattPocock]] — 执行纪律箱作者
- [[AICoding]] — AI 辅助编程范式
