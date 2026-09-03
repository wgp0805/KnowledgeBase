---
title: "OpenSpec + Matt Pocock Skills 配合执行流程详解"
type: synthesis
tags: [OpenSpec, MattPocock, TDD, code-review, 执行纪律, 配合工作流, apply与tdd, Java后端, 实操指南]
sources:
  - wiki/entities/OpenSpec.md
  - wiki/entities/MattPocock.md
  - wiki/entities/mattpocock-skills.md
  - wiki/entities/GrillMe.md
  - wiki/entities/SpecSuperflow.md
  - wiki/syntheses/openspec-brownfield-usage-guide.md
  - wiki/syntheses/openspec-codegraph-usage-guide.md
  - wiki/syntheses/optimal-framework-combination-heavy-project.md
  - wiki/syntheses/agent-spec-framework-comparison-and-matt-skills-workflow.md
  - wiki/sources/摘要-mattpocock-skills.md
  - wiki/concepts/TDD.md
  - wiki/concepts/code-review.md
  - wiki/concepts/delta-spec.md
last_updated: 2026-09-03
---

# OpenSpec + Matt Pocock Skills 配合执行流程详解

> **核心问题**：OpenSpec 的"不管执行纪律"到底指什么？用 OpenSpec + Matt Skills 在现有 Java 项目开发中型功能，完整安装和执行流程是什么？`/opsx:apply` 和 `/tdd` 怎么配合——要不要叫停？Matt Skills 是项目级安装还是全局安装？

## 一、先厘清：OpenSpec"不管执行纪律"是什么意思

OpenSpec **有执行阶段**（`/opsx:apply` 按任务清单逐项写代码），不是"不管执行"。区别在于 **"执行"和"执行纪律"是两件事**：

| | OpenSpec `/opsx:apply` | Superpowers 强制流程 |
|---|---|---|
| 按任务清单写代码 | ✅ 做 | ✅ 做 |
| **强制 TDD**（没失败测试不准写生产代码） | ❌ 不管 | ✅ 铁律，违反要删掉重来 |
| **强制代码审查门禁**（每任务/每分支/交付前三层审查） | ❌ 不管 | ✅ Review Gate 四层设卡 |
| **子代理上下文隔离**（防上下文污染） | ❌ 不管 | ✅ SDD 隔离 + F1/F2 双裁决 |
| **完成前验证**（强制跑测试+验证才准说完成） | ❌ 不管 | ✅ verification-before-completion |
| **Red Flags 表**（堵住"改动小不用测试"等借口） | ❌ 不管 | ✅ 逐条封堵 |

**比喻**：
- OpenSpec 像**项目经理**——把任务拆清楚、排好序、盯着你按清单干完，但**你怎么干、干的时候守不守规矩它不管**
- Superpowers 像**质检员+纪律委员**——不光让你干完，还强制你先写测试、写完必须过审查、不许跳步骤

**OpenSpec 实体页明确写**："定位边界：规划引擎，有意不碰从规划到落地这段路"——这里的"落地"指的就是执行过程中的纪律保障。

**准确表述**（修正之前容易误解的"只管规划不管执行纪律"）：
> **OpenSpec 管规划 + 按清单执行，但不管执行过程中的纪律**（不强制 TDD、不设审查门禁、不做子代理隔离、不强制完成前验证）。如果要执行纪律保障，需搭配 Superpowers 或 Matt Pocock Skills。

## 二、核心分工

| 工具 | 管什么 | 阶段 |
|------|--------|------|
| [[OpenSpec]] | **规划 + 存档**（想清楚再动手 + 历史决策留痕） | 编码前 |
| [[MattPocock]] Skills | **执行纪律**（TDD / 代码审查 / 调试） | 编码中 |

> OpenSpec 的 `/opsx:apply` 会按 tasks.md 写代码，但**不强制 TDD、不设审查门禁**。Matt Skills 补这块——执行时手动调 `/tdd` `/code-review`，把纪律焊在执行环节。

## 三、安装两个工具

### 安装 OpenSpec（中文版）

```bash
# 1. 安装
npm install -g @studyzy/openspec-cn@latest

# 2. 进入你的已有 Java 项目
cd /your-java-project

# 3. 初始化（--tools 指定你用的 AI 工具）
openspec-cn init --tools claude          # 单个工具
openspec-cn init --tools claude,cursor   # 多个工具
openspec-cn init --tools all             # 全部 31 个工具

# 4. 查看仪表盘
openspec-cn view
```

初始化后项目根目录出现 `opsx/` 工作区：
```
opsx/
├── archive/          # 已完成的变更归档（AI 的"记忆库"）
├── specs/            # 当前生效的需求规格
├── changes/          # 进行中的变更
└── openspec.config.json
```

**支持的 31 个工具 ID**：`claude` `cursor` `codex` `gemini` `opencode` `kimi` `qwen` `qoder` `windsurf` `github-copilot` 等。

### 安装 Matt Pocock Skills

Matt Skills **不是** OpenSpec 那种"全局装 CLI + 项目 init"模式，没有 init 步骤。有**两种安装方式**，对应两种哲学：

#### 方式一：`skills.sh` 安装器（可编辑副本，拷进项目）— 推荐

```bash
npx skills@latest add mattpocock/skills
# 核心选这三个：
#   tdd              — 测试驱动开发（执行阶段用）
#   code-review      — 代码审查（实现后用）
#   grill-with-docs  — 需求澄清（可选，OpenSpec 的 explore 已覆盖部分）
# 可选：
#   diagnosing-bugs  — 系统化调试（跑不起来时用）
#   domain-modeling  — 领域建模（复杂业务用）
```

- **本质**：把 SKILL.md 文件**拷贝到你的项目目录里**（通常是 `.claude/skills/`）
- **可修改**：拷进来就是你的了，可以改造成团队自己的规范
- **不会自动更新**：作者更新了上游，你这边不动，要手动重新拉
- **适合**：团队使用、想定制化、issue 流程和标签体系要适配
- **Codex 支持**：skills.sh 安装器已支持 Codex 及其他遵循 Agent-Skills 标准的 agent

> 原文："skills.sh copies the skills into your project so you can hack on them and make them your own"

#### 方式二：Claude Code Plugin（只读订阅，跟着作者更新）

```bash
# Claude Code 里
/plugin marketplace add mattpocock/skills
/plugin install mattpocock/skills

# 或命令行
claude plugin marketplace add mattpocock/skills
```

- **本质**：作为插件订阅，**只读、永远最新**，作者更新你自动跟着更新
- **不可修改**：你别动，动了也被下次更新覆盖
- **适合**：个人使用、只想蹭一套靠谱默认、不想维护
- **安装后**：每仓库跑一次 `/setup-matt-pocock-skills`

> 原文："The plugin keeps them as a read-only, always-current bundle you don't edit"

#### 两种方式对比

| | skills.sh（可编辑副本） | Claude Code Plugin（只读订阅） |
|---|---|---|
| 位置 | 拷进**项目目录** | 作为插件订阅 |
| 可修改 | ✅ 随便改 | ❌ 只读 |
| 更新 | 手动重新拉 | 自动跟着上游 |
| 适合 | 团队定制、要适配自己的流程 | 个人用、想省心 |
| Codex 支持 | ✅ | ❌（原生插件还在路线图） |

#### 关键提醒

- **两种方式不要混用**——会导致同一 skill 两份来源、版本对不上。选一个跟到底
- **团队刚上手先用 skills.sh 更稳**，因为你迟早要改一两个 skill 去适配自己的 issue 流程和标签体系；等全组跑顺了，再切成 plugin 跟着上游走，反而省维护

#### 与 OpenSpec 安装模式的区别

| | OpenSpec | Matt Skills |
|---|---|---|
| 安装模式 | **全局装 CLI** + **项目 init** 生成 `opsx/` 工作区 | **直接拷进项目**（skills.sh）或**插件订阅**（plugin） |
| 项目级初始化 | ✅ `openspec-cn init` 生成目录结构 | ❌ 没有 init 步骤，拷进来就用 |
| 产出物 | `opsx/` 规划文档工作区 | `.claude/skills/` 下的 SKILL.md 文件 |

## 四、完整执行流程（以"现有 Java 项目新增日志收集功能"为例）

### 第 1 步：探索需求 — `/opsx:explore`

```
/opsx:explore 我想给系统加日志收集功能，集团要求收集4种日志：
登录日志、权限管理日志、前端操作日志、前端数据流转日志。
集团只给了采集文档，我看了项目不知道该怎么落地。
帮我分析：这4种日志各自的采集点在哪，用什么技术方案最合适。
```

**做什么**：AI 通过纯对话帮你理清——为什么要做、谁用、边界在哪、有什么风险、现有项目结构适合哪种方案。

**产物**：纯对话，不生成文件。目的是"先想清楚再动手"。

> 如果需求特别模糊，可以先调 Matt 的 `/grill-with-docs` 盘问对齐，再回来走 OpenSpec 流程。

### 第 2 步：生成规划工件 — `/opsx:propose`

```
/opsx:propose 实现日志收集系统：4种日志分别采用不同采集策略
```

AI 自动生成四份文档，放在 `opsx/changes/log-collection/` 下：

| 文件 | 内容 | 校验规则 | 你审查的重点 |
|------|------|---------|------------|
| `proposal.md` | 为什么改 + 改什么 | `## Why` 不能少于 50 字符 | 动机对不对 |
| `specs/spec.md` | 具体需求，用 SHALL/MUST + Given/When/Then | 每个 Requirement 必须含 SHALL 或 MUST，至少一个 Scenario 块 | **4 种日志场景有没有漏** |
| `design.md` | 技术方案（用什么库、改哪些类、数据流） | - | **注解 vs 拦截器的选择理由，字段能不能拿到** |
| `tasks.md` | 可执行步骤清单 | - | 步骤是否可执行 |

**工件依赖链**：`proposal → specs → design → tasks → implement`。依赖关系是"使能"而非"卡死"——随时可回去改前面的工件。

### 第 3 步：人工审查（你的绝对主动权）

**这是关键一步，不要跳**。审查四份文档：

- `proposal.md`：动机对不对
- `specs/spec.md`：需求有没有漏掉边界场景
- `design.md`：技术方案是否合理（注解能不能拿到字段？拦截器性能可接受？）
- `tasks.md`：步骤你认同吗

**不通过就改**，**通过后才说**："通过，开始实现"。

### 第 4 步：按清单实现 — `/opsx:apply` + `/tdd` 配合

**这是 OpenSpec 和 Matt Skills 配合的关键点**，也是最容易混淆的地方。

#### 核心结论：先 `/opsx:apply`，再 `/tdd`，不是二选一

```
/opsx:apply          ← OpenSpec：按 tasks.md 清单逐项实现
   ↓
/tdd                 ← Matt：对当前这一项强制 TDD 纪律
```

**`/opsx:apply` 管"按清单推进 + 更新进度"，`/tdd` 管"每一项怎么写代码（先测试后实现）"。两个命令不冲突——apply 是骨架，tdd 是肌肉。**

#### 三种配合方式

**方式一：执行前约定（推荐，最省心）**

在调 `/opsx:apply` 之前，先告诉 AI 你的要求：

```
/opsx:apply 
注意：每一项任务都必须用 TDD 方式实现——先写失败测试，跑红，再写实现让它通过。
不要一口气写完所有代码，每完成一项停下来等我确认再继续下一项。
```

这样 AI 在 apply 过程中就会自带 TDD 纪律，不用你每项手动叫停。**本质是把 Matt 的 `/tdd` 纪律"内联"到 OpenSpec 的 apply 执行里**。

**方式二：手动叫停，逐项切换**

如果你已经直接跑了 `/opsx:apply`，AI 开始连贯写代码了：

1. **随时打断**：直接发消息"停，先别写第 2 项"
2. **切换到 TDD**：`/tdd 重新实现第 1 项，先写失败测试再写实现`
3. **确认通过后**：`继续 apply 第 2 项，同样用 TDD 方式`

这种方式累，但控制最细。

**方式三：跳过 `/opsx:apply`，直接 `/tdd` 逐项干**

```
/tdd 按 opsx/changes/log-collection/tasks.md 第 1 项实现，先写失败测试再写实现
```

完成确认后：
```
/tdd 按 tasks.md 第 2 项实现，先写失败测试再写实现
```

**完全跳过 apply**，OpenSpec 只当规划文档用，执行全交给 Matt。最后手动把 tasks.md 的 `[ ]` 改成 `[x]`，再 `/opsx:archive` 归档。

#### 三种方式对比

| | 方式一：执行前约定 | 方式二：手动叫停 | 方式三：跳过 apply |
|---|---|---|---|
| 省心程度 | ✅ 最省心 | ❌ 最累 | ⚠️ 中等 |
| TDD 纪律强度 | ⚠️ 靠 AI 自觉 | ✅ 你强制 | ✅ 你强制 |
| tasks.md 进度 | ✅ 自动更新 | ⚠️ 可能乱 | ❌ 手动维护 |
| 适合 | **中型功能（推荐）** | 控制狂 | 简单功能 |

#### 关于"叫停"的关键认知

**`/opsx:apply` 默认是连贯执行的**——AI 会一口气按 tasks.md 写完所有代码，不会自动停下来等你调 `/tdd`。所以：

- 用方式一：执行前就约定好，不用叫停
- 用方式二：必须主动叫停，AI 不会自己停
- 用方式三：根本不启动 apply，没有叫停问题

#### TDD 执行细节

Matt 的 TDD 铁律（[[TDD]]）：
- 没有失败测试就不准写生产代码
- AI 先写一个跑不过的测试，再写实现让它通过
- 红-绿-重构循环
- 引用 The Pragmatic Programmer："反馈的速度就是你的速度上限"

**如果跑不起来**：用 Matt 的 `/diagnosing-bugs` 系统化定位根因，别让 AI 瞎改：

```
/diagnosing-bugs 测试跑不过，帮我系统化定位根因，不要瞎改
```

### 第 5 步：代码审查 — `/code-review`

所有 tasks 实现完后，调 Matt 的代码审查：

```
/code-review 审查刚才实现的日志收集功能全部代码
```

**Matt 的两轴并行审查**（[[code-review]]）：
- **正确性轴**：逻辑对不对、边界条件覆盖没、异常处理合理不
- **质量轴**：命名、结构、可维护性、有没有重复

按 **Critical / Important / Minor** 三级严重度输出问题清单。

> OpenSpec 的 `/opsx:apply` 不会强制审查，Matt 的 `/code-review` 补上这块纪律。

### 第 6 步：修复 + 验证

根据 code-review 结果修复 Critical 和 Important 问题，修复后重新跑测试确认没引入新问题。

### 第 7 步：归档 — `/opsx:archive`

```
/opsx:archive
```

把整个 `opsx/changes/log-collection/` 移入 `opsx/archive/`。**这是对抗 AI 遗忘的核心**——所有历史决策永久存档，同事打开归档的 markdown 就能看懂决策原因。

## 五、完整流程一览

```
现有 Java 项目 + 中型功能需求
    │
    ├─ /opsx:explore              # OpenSpec：探索需求（纯对话）
    │    → AI 分析项目现状，给出方案选项
    │
    ├─ /opsx:propose              # OpenSpec：生成四份规划工件
    │    → proposal.md / spec.md / design.md / tasks.md
    │
    ├─ 【人工审查】                # 你的绝对主动权
    │    → 不通过就改，通过才推进
    │
    ├─ /opsx:apply + /tdd         # OpenSpec 按清单 + Matt 强制 TDD
    │    → 推荐方式一：执行前约定 TDD 纪律
    │    → 逐项实现，先写失败测试再写实现
    │    → 跑不起来用 /diagnosing-bugs
    │
    ├─ /code-review               # Matt：两轴审查（Critical/Important/Minor）
    │
    ├─ 修复 + 验证                # 修复审查问题，重跑测试
    │
    └─ /opsx:archive              # OpenSpec：归档
         → 同事打开 design.md 就能看懂决策原因
```

## 六、什么时候可以跳步

| 场景 | 流程 |
|------|------|
| 中型功能（本文） | 完整 7 步 |
| 加一个简单接口 | `/opsx:propose`（轻量）→ `/opsx:apply` 直接写 → `/code-review` |
| 修 bug | `/diagnosing-bugs` 定位 → `/tdd` 修 |
| 需求模糊但改动小 | `/grill-with-docs` 对齐 → `/opsx:apply` |

## 七、棕地项目首次补录（第一次用 OpenSpec）

已有项目最大的问题是"历史决策无文档"。**不要一次性补全所有**，用 [[delta-spec]] 增量补录，从最近要改的模块开始：

```markdown
# Delta Spec: 手机号验证码登录

## ADDED
- Requirement: 系统 SHALL 支持手机号 + 短信验证码登录
  #### Scenario: 用户输入有效手机号
    Given 用户在登录页输入手机号 138xxxx
    When 点击"获取验证码"
    Then 系统发送 6 位验证码，5 分钟内有效

## MODIFIED
- Requirement: 认证流程 MUST 支持原密码登录 + 验证码登录两种模式

## REMOVED
- 无
```

**核心原则**：不动已有 spec，只描述差异。通过 `/opsx:sync` 将 delta 合并回主 spec。

## 八、归档后需求又变了怎么办

**不要直接手改 archive 目录中的归档文档**。标准流程：

```
/opsx:explore   → 理清改什么、为什么改
/opsx:propose   → 生成 delta spec（ADDED/MODIFIED/REMOVED 三标记，只写差异）
人工确认         → 审阅 delta 提案
/opsx:apply     → 按 tasks.md 改代码（配合 /tdd）
/opsx:sync      → 把 delta 合并回主 spec（关键！没这步 OpenSpec 不知道你改了什么）
/opsx:archive   → 归档本次变更，形成新基线
```

## 九、为什么是这个组合（而非 SpecSuperflow）

[[SpecSuperflow]] 也把 OpenSpec + Superpowers 融合了，但它是**八状态机自动驱动**，太重。OpenSpec + Matt Skills 的优势：

| 维度 | SpecSuperflow | OpenSpec + Matt Skills |
|------|--------------|----------------------|
| 控制权 | 状态机自动驱动 | **你主导**，手动调 skill |
| 重量 | 重（8 状态机 + contract-builder） | **轻**（按需调用） |
| 灵活性 | 固定流程 | 简单任务可跳步 |
| 适合 | 大型功能、多人协作 | 中型功能、个人快速推进 |

> 经验法则：不需要写 proposal 和 design doc 就能想清楚的事，SpecSuperflow 太重；OpenSpec + Matt Skills 按需调用更合适。

## 关联连接

- [[OpenSpec]] — 规划引擎（组合核心）
- [[MattPocock]] — 执行纪律箱作者
- [[mattpocock-skills]] — 执行纪律箱仓库
- [[GrillMe]] — 需求澄清 skill（可选）
- [[TDD]] — 测试驱动开发（执行阶段核心纪律）
- [[code-review]] — 代码审查（实现后纪律）
- [[delta-spec]] — 增量变更机制（棕地补录）
- [[SpecSuperflow]] — 被对比的融合方案（太重）
- [[openspec-brownfield-usage-guide]] — OpenSpec 棕地完整使用方案
- [[openspec-codegraph-usage-guide]] — OpenSpec + CodeGraph 使用指南
- [[optimal-framework-combination-heavy-project]] — 重型项目最优框架组合
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] — 姊妹篇：框架全景对比 + Matt Skills 介绍 + 7 步流程
- [[摘要-mattpocock-skills]] — Matt Skills 来源
- [[规范驱动开发]] — 上层方法论
- [[AICoding]] — AI 辅助编程范式
- [[ClaudeCode]] — 承载平台
