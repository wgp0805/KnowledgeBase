---
title: "Agent 规范驱动框架对比与 Matt Pocock Skills 实战流程"
type: synthesis
tags: [AI编程, 规范驱动, OpenSpec, Superpowers, SpecKit, MattPocock, GSDCore, Trellis, SpecSuperflow, 框架选型, Java后端, 实战流程]
sources:
  - wiki/sources/摘要-superpowers-openspec-speckit对比.md
  - wiki/sources/摘要-OpenSpec规范驱动AI编程框架.md
  - wiki/sources/摘要-superpowers到底是什么.md
  - wiki/sources/摘要-gsd-core-ai工作流.md
  - wiki/sources/摘要-trellis使用手册.md
  - wiki/sources/摘要-spec-superflow-融合工作流.md
  - wiki/sources/摘要-从-vibe-coding-到-spec-coding.md
  - wiki/sources/摘要-loop-engineering-guide.md
  - wiki/sources/摘要-mattpocock-skills.md
  - wiki/sources/摘要-agent-skills-经济学-月增5万星.md
  - wiki/sources/摘要-强模型时代删掉Superpowers该怎么选.md
  - wiki/entities/OpenSpec.md
  - wiki/entities/Superpowers.md
  - wiki/entities/SpecKit.md
  - wiki/entities/GSDCore.md
  - wiki/entities/Trellis.md
  - wiki/entities/SpecSuperflow.md
  - wiki/entities/MattPocock.md
  - wiki/entities/mattpocock-skills.md
  - wiki/entities/GrillMe.md
  - wiki/syntheses/openspec-working-principle.md
  - wiki/syntheses/optimal-framework-combination-heavy-project.md
  - wiki/concepts/TDD.md
  - wiki/concepts/code-review.md
  - wiki/concepts/流程税.md
  - wiki/concepts/强模型时代工作流选型.md
last_updated: 2026-09-03
---

# Agent 规范驱动框架对比与 Matt Pocock Skills 实战流程

> **核心问题**：Agent 使用的类 OpenSpec 规范驱动框架都有哪些？分别适合什么项目？优缺点是什么？Matt Pocock 的 mattpocock/skills 是怎么回事？用它在现有 Java 后端项目开发中型功能，流程应该是什么样的？

## 一、规范驱动框架全景（按解决的核心问题分类）

主流"规范驱动 AI 编程"框架可按**解决的核心问题**分为三类（[[摘要-superpowers-openspec-speckit对比]]）：

| 框架 | 解决的问题 | 形态 | 适合项目 |
|------|-----------|------|---------|
| [[OpenSpec]] | "改了什么"（规划层） | 四阶段命令 + 四份 DAG 工件 + Delta Spec | **棕地项目**最友好，增量变更 |
| [[Superpowers]] | "怎么干"（执行纪律） | 14 个 SKILL.md + 五阶段强制流程 | 全新复杂项目、高风险模块、AI 编程新手 |
| [[SpecKit]] | "按什么规矩干"（项目宪法） | GitHub 官方，七阶段流水线 | **绿地项目**，规范可执行直接生成代码 |

### 1. OpenSpec（57k+ Star，FissionAI）

- **优点**：Delta Spec 增量机制对棕地最友好（只描述 ADDED/MODIFIED/REMOVED，不重写整份 spec）；31 平台分发；人工确认门保留主动权；产出人类可读 markdown 利于混合协作
- **缺点**：只管规划不管执行纪律；需自行搭配执行层
- **适合**：已有代码库的增量改动、需同事混合协作、要求绝对主动权
- 详见 [[openspec-working-principle]]

### 2. Superpowers（238K Star，Jesse Vincent）

- **优点**：Process over Prompt，强制 TDD/Review Gate/SDD 子代理隔离，token 消耗砍约 50%；纯 SKILL.md 无运行时跨平台
- **缺点**：强模型时代有"流程税"（重复规划）；简单任务杀鸡用牛刀；子 Agent 上下文继承偶有故障
- **适合**：全新复杂项目、核心业务重构、需完整可追溯工程留痕
- **不适合**：快速原型、小 bug、老代码局部改动
- 详见 [[Superpowers]]

### 3. Spec-Kit（115K+ Star，GitHub 官方）

- **优点**：GitHub 官方背书长期维护；规范可执行直接生成代码；项目宪法机制从顶层约束
- **缺点**：学习曲线陡；Python/uv 对 Java 开发者有门槛；棕地适配不如 OpenSpec
- **适合**：绿地项目、从零起步需强规范约束
- 详见 [[SpecKit]]

## 二、其他相关框架

| 框架 | 定位 | 适合场景 |
|------|------|---------|
| [[GSDCore]]（2.3k Star） | "项目管理大脑"，元提示+上下文工程 | 中型项目，但属"接管流程"型，控制权被拿走 |
| [[Trellis]] | 项目级工作流 Harness，`.trellis/` 集中存 Spec/Task/Journal | 长期维护、多人协作、跨 AI 工具切换 |
| [[SpecSuperflow]] | OpenSpec + Superpowers **源码级融合**，8 状态机自动驱动 | 大型功能开发、需 TDD+Review Gate 的棕地；但太重，不适合原型 |
| Loop Engineering | 三文件（AGENTS/STATE/SKILL.md）驱动 Agent 自动循环 | L1-L3 渐进式自动化循环 |

## 三、选型建议

### 理想组合（苏三的初始结论，[[摘要-superpowers-openspec-speckit对比]]）

> [[SpecKit]] 定项目宪法 → [[OpenSpec]] 管每次变更生命周期 → [[Superpowers]] 强制执行纪律

### 重型棕地项目最优组合（用户反馈 GSD Core 不满意后的修正版，[[optimal-framework-combination-heavy-project]]）

> **[[OpenSpec]]（规划）+ CodeGraph（影响分析）+ [[MattPocock]] Skills（纪律箱）**——三者都是工具按需调用，无框架接管流程，保留绝对主动权

### 核心认知

- "不知道怎么做"→ 用 OpenSpec `/opsx:explore` 结构化探索
- "方案试错成本高"→ OpenSpec design.md + CodeGraph impact 事前分析
- "绝对主动权"→ 选工具箱型（OpenSpec+Skills），拒绝接管流程型（GSD Core/SpecSuperflow）
- "同事混合协作"→ 必须产出人类可读 markdown，只有 OpenSpec 满足

## 四、Matt Pocock 的 mattpocock/skills

### 是什么

[[MattPocock]]（Total TypeScript 作者）开源的 `mattpocock/skills` 仓库，2026 年 8 月在 GitHub Agent Skills 集体爆发现象中**单月增星 50,486**，5 个月冲到 17 万 star（[[摘要-agent-skills-经济学-月增5万星]]、[[mattpocock-skills]]）。本质是把十几年生产环境踩过的坑，打包成 Claude/Gemini/Codex 通用的「代码自检技能包」。

### 为什么火

核心经济学判断（[[摘要-agent-skills-经济学-月增5万星]]）：
> **模型能力是租的（按 token 付费），技能是自己的（一次编写处处复用）**

2024 写提示词 → 2025 调模型 → 2026 沉淀技能。Skills 类项目正在吃掉原本属于"大模型新版本""Agent 框架"的榜单位置。

### 核心设计哲学

**"把 skill 当纪律，不当框架"**（[[摘要-mattpocock-skills]]）——与 GSD、BMAD、Spec-Kit 等"接管流程"的重量级框架形成根本分野：

1. **小**：每个 skill 职责单一
2. **可改**：允许用户修改定制
3. **可组合**：skill 之间自由组合
4. **跨模型**：不绑定特定 AI
5. **基于工程基础**：引用 The Pragmatic Programmer、DDD、XP、Ousterhout 软件设计哲学

Matt 公开批评 GSD/Spec-Kit："帮你接管整套流程，代价是控制权被拿走，流程本身出了 bug 你还很难修"（[[GSDCore]]、[[SpecKit]] 对比视角章节）。

### 四大失败模式 + 修复 Skill

| 失败模式 | 表现 | 修复 Skill | 工程经典 |
|---------|------|-----------|---------|
| 对不齐 | Agent 没做你想要的 | `/grill-with-docs`（盘问对齐） | The Pragmatic Programmer |
| 太啰嗦 | 命名冗长代码膨胀 | 共享语言 → CONTEXT.md | DDD（Eric Evans） |
| 跑不起来 | 看着对跑就崩 | `/tdd` + `/diagnosing-bugs` | The Pragmatic Programmer |
| 架构烂成泥 | 软件熵加速 | `/to-spec` + `/improve-codebase-architecture` | XP / Ousterhout |

### 两层调用架构

- **User-invoked（编排层）**：用户手打 `/xxx` 触发——`ask-matt`、`grill-with-docs`、`triage`、`implement`、`wayfinder`
- **Model-invoked（纪律层）**：模型自动调用——`prototype`、`diagnosing-bugs`、`tdd`、`domain-modeling`、`code-review`
- **铁律**：User-invoked 可调 Model-invoked，但 User-invoked 之间互不调用

### 一个有意思的细节

Matt 自己把最火的 `/grill-me` 从默认推荐位移除，转推 `/domain-model` 作为规划起点——但社区仍普遍把 grill-me 作为编码前需求澄清首选，两者不矛盾（[[GrillMe]] 知识冲突区块）。

### 强模型时代的定位

[[摘要-强模型时代删掉Superpowers该怎么选]] 指出，在 GPT-5.6/Kimi K3/Fable-5 时代，Matt Skills 的轻量可组合特性使其**优于 Superpowers** 作为日常默认配置：
- 避免流程税（不强制全套流程，[[流程税]]）
- 保留人的主导权
- 简单任务直接用模型原生能力，按需调用 skill

## 五、用 Matt Pocock Skills 在现有 Java 后端项目开发中型功能的流程

### 前提：先装三件套

```bash
npx skills@latest add mattpocock/skills
# 核心选：grill-with-docs, tdd, code-review
# 可选：to-spec, domain-modeling, diagnosing-bugs
```

### 完整流程（7 步）

#### 第 1 步：需求澄清 — `/grill-with-docs`

```
/grill-with-docs 我要在现有的 Spring Boot 项目里新增 XX 功能。
现有代码在 src/main/java/com/xxx/...，相关模块是 YY。
帮我盘问这个需求的边界和设计分支。
```

**做什么**：AI 像面试官逐层追问——触发条件？异常场景？要不要事务？并发量？权限控制？现有哪个模块该复用？

**为什么**：中型功能最容易"对不齐"（四大失败模式之首）。`grill-with-docs` 会读现有代码+文档，盘问到共识（[[GrillMe]]）。

**产出**：对齐后的需求描述 + 设计决策点清单。

#### 第 2 步：领域建模 — `/domain-model`（可选但推荐）

```
/domain-model 基于刚才对齐的需求，帮我梳理这个功能涉及的核心领域概念和它们的关系。
```

**做什么**：梳理实体、值对象、聚合根边界。对 Java 后端中型功能特别有用——避免一上来就写 CRUD，先想清楚领域模型。

**解决"太啰嗦"失败模式**：把长业务描述压成术语表放 `CONTEXT.md`，后续 AI 写代码命名一致（DDD 共享语言）。

#### 第 3 步：写规格 — `/to-spec`

```
/to-spec 把对齐后的需求和领域模型转成规格文档。
```

**做什么**：产出结构化 spec——技术方案、改哪些文件、接口契约、验收标准。

**为什么中型功能必须这步**：[[optimal-framework-combination-heavy-project]] 核心认知——"方案试错成本高"的根因是动手前没分析可行性。spec 阶段就能发现"注解拿不到某字段""这个表要加索引影响线上"等问题。

#### 第 4 步：人工审查 spec（你的绝对主动权）

这一步**不是 skill 命令**，是你自己做的事：

- 技术方案可行吗？（注解还是拦截器？AOP 还是监听？）
- 改现有代码的影响面你接受吗？
- 接口契约合理吗？
- 验收标准完整吗？

**不通过就改**，告诉 AI "spec 里 XX 方案不行，改成 YY"。**通过后才进入下一步**。

> 对应 Matt 哲学核心：**控制权在你手里，skill 是工具不是框架**（[[MattPocock]]）。

#### 第 5 步：实现 — `/tdd` + `/implement`

```
/tdd 按规格实现 XX 功能，先写失败测试再写实现。
```

**做什么**：Matt 的 TDD 铁律——没有失败测试就不准写生产代码（[[TDD]]）。AI 先写跑不过的测试，再写实现让它通过，红-绿-重构循环。

**为什么中型功能用 TDD**：
- Java 后端有现成测试框架（JUnit 5 + AssertJ + Spring Boot Test），TDD 落地成本低
- 中型功能涉及多模块，测试是防止"改 A 坏 B"的护栏
- Matt 引用 The Pragmatic Programmer："反馈的速度就是你的速度上限"——先写失败测试再修，比让 AI 直接写代码然后反复调试快得多

**如果跑不起来**：用 `/diagnosing-bugs` 系统化定位根因，别让 AI 瞎改。

#### 第 6 步：代码审查 — `/code-review`

```
/code-review 审查刚才实现的 XX 功能代码。
```

**做什么**：Matt 的两轴并行审查（[[code-review]]）：
- **正确性轴**：逻辑对不对、边界条件覆盖没、异常处理合理不
- **质量轴**：命名、结构、可维护性、有没有重复

按 Critical / Important / Minor 三级严重度输出问题清单。

#### 第 7 步：修复 + 提交

根据 code-review 结果修复 Critical 和 Important 问题，然后正常 git 提交。

### 流程一览

```
现有 Java 项目 + 中型功能需求
    │
    ├─ /grill-with-docs      # 1. 盘问对齐需求（解决"对不齐"）
    │    → 需求描述 + 设计决策点
    │
    ├─ /domain-model         # 2. 梳理领域概念（解决"太啰嗦"）
    │    → 术语表 → CONTEXT.md
    │
    ├─ /to-spec              # 3. 写规格文档（解决"架构烂成泥"）
    │    → 技术方案 + 接口契约 + 验收标准
    │
    ├─ 【人工审查 spec】      # 4. 你的绝对主动权
    │    → 不通过就改，通过才推进
    │
    ├─ /tdd                  # 5. 先写失败测试再实现（解决"跑不起来"）
    │    → 红-绿-重构循环
    │    → 跑不起来用 /diagnosing-bugs
    │
    ├─ /code-review          # 6. 两轴审查（Critical/Important/Minor）
    │
    └─ 修复 + git 提交       # 7. 收尾
```

### 什么时候可以跳步

Matt 哲学的关键是**按需调用，不强制全套**（[[MattPocock]]、[[流程税]]）：

| 场景 | 流程 |
|------|------|
| 中型功能（本文） | 完整 7 步 |
| 加一个简单接口 | `/implement` 直接写 + `/code-review` |
| 修 bug | `/diagnosing-bugs` 定位 + `/tdd` 修 |
| 需求模糊但改动小 | `/grill-with-docs` + `/implement` |

### 与 OpenSpec 的区别

用 [[OpenSpec]] 流程会是 `/opsx:explore` → `/opsx:propose`（产出 4 份工件）→ 人工确认 → `/opsx:apply` → `/opsx:archive`，更重但产出人类可读 markdown 利于同事协作。Matt Skills 更轻——**你主导流程，skill 是按需调用的纪律箱**，适合个人快速推进（[[optimal-framework-combination-heavy-project]] 对比）。

## 关联连接

- [[OpenSpec]] — 规划层框架
- [[Superpowers]] — 执行纪律框架
- [[SpecKit]] — GitHub 官方规范可执行框架
- [[GSDCore]] — 接管流程型框架（对比对象）
- [[Trellis]] — 项目级工作流 Harness
- [[SpecSuperflow]] — OpenSpec+Superpowers 融合
- [[MattPocock]] — mattpocock/skills 创建者
- [[mattpocock-skills]] — 仓库实体
- [[GrillMe]] — 需求澄清 skill
- [[TDD]] — 测试驱动开发
- [[code-review]] — 代码审查
- [[流程税]] — 强模型时代成本概念
- [[强模型时代工作流选型]] — 选型方法论
- [[openspec-working-principle]] — OpenSpec 工作原理
- [[optimal-framework-combination-heavy-project]] — 重型项目最优组合
- [[openspec-matt-skills-execution-workflow]] — 姊妹篇：OpenSpec + Matt Skills 配合执行详解（apply 与 tdd 三种配合方式 / 叫停机制 / 棕地补录）
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比来源
- [[摘要-mattpocock-skills]] — Matt Skills 来源
- [[摘要-agent-skills-经济学-月增5万星]] — Agent Skills 经济学来源
- [[摘要-强模型时代删掉Superpowers该怎么选]] — 强模型时代定位来源
- [[规范驱动开发]] — 上层方法论
- [[AICoding]] — AI 辅助编程范式
