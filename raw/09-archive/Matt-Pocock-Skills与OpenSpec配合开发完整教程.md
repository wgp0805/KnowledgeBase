# Matt Pocock Skills 与 OpenSpec 配合开发完整教程

## 问题一：使用 Matt 开发一个功能的完整流程是什么样的？给我一个详细的教程

### 完整流程（7 步）

#### 第 1 步：需求澄清 — `/grill-with-docs`
```
/grill-with-docs 我要在现有的 Spring Boot 项目里新增 XX 功能。
现有代码在 src/main/java/com/xxx/...，相关模块是 YY。
帮我盘问这个需求的边界和设计分支。
```
**做什么**：AI 像面试官逐层追问——触发条件？异常场景？要不要事务？并发量？权限控制？现有哪个模块该复用？解决"对不齐"失败模式。

#### 第 2 步：领域建模 — `/domain-model`（可选但推荐）
```
/domain-model 基于刚才对齐的需求，帮我梳理这个功能涉及的核心领域概念和它们的关系。
```
**做什么**：梳理实体、值对象、聚合根边界。把长业务描述压成术语表放 `CONTEXT.md`，解决"太啰嗦"失败模式。

#### 第 3 步：写规格 — `/to-spec`
```
/to-spec 把对齐后的需求和领域模型转成规格文档。
```
**做什么**：产出结构化 spec——技术方案、改哪些文件、接口契约、验收标准。解决"架构烂成泥"失败模式。

#### 第 4 步：人工审查 spec（你的绝对主动权）
这不是 skill 命令，是你自己做的事：技术方案可行吗？改现有代码的影响面你接受吗？接口契约合理吗？验收标准完整吗？不通过就改，通过才推进。

> 对应 Matt 哲学核心：**控制权在你手里，skill 是工具不是框架**。

#### 第 5 步：实现 — `/tdd` + `/implement`
```
/tdd 按规格实现 XX 功能，先写失败测试再写实现。
```
**做什么**：Matt 的 TDD 铁律——没有失败测试就不准写生产代码。AI 先写跑不过的测试，再写实现让它通过，红-绿-重构循环。如果跑不起来，用 `/diagnosing-bugs` 系统化定位根因。

#### 第 6 步：代码审查 — `/code-review`
```
/code-review 审查刚才实现的 XX 功能代码。
```
**做什么**：Matt 的两轴并行审查：
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
Matt 哲学的关键是**按需调用，不强制全套**：
| 场景 | 流程 |
|------|------|
| 中型功能（本文） | 完整 7 步 |
| 加一个简单接口 | `/implement` 直接写 + `/code-review` |
| 修 bug | `/diagnosing-bugs` 定位 + `/tdd` 修 |
| 需求模糊但改动小 | `/grill-with-docs` + `/implement` |

---

## 问题二：Matt 的规划能力和 OpenSpec 相比怎么样？可以替代 OpenSpec 吗？

### 定位差异

| 框架 | 解决的问题 | 规划能力 | 执行能力 |
|------|-----------|---------|---------|
| OpenSpec | "改了什么"（规划层） | **强**：四阶段命令 + 四份 DAG 工件 + Delta Spec 增量机制 | 弱：只管规划不管执行纪律 |
| Matt Pocock | "怎么干"（执行纪律） | 弱：`/grill-with-docs` 需求澄清 + `/domain-model` 领域建模 | **强**：`/tdd` `/code-review` 按需调用 |

### 规划能力具体对比

**OpenSpec 的规划能力**：
- `/opsx:explore`：纯对话探索需求，不写代码
- `/opsx:propose`：生成四份结构化工件（proposal.md / specs/spec.md / design.md / tasks.md）
- Delta Spec 增量机制：对棕地项目友好，只描述 ADDED/MODIFIED/REMOVED
- 31 平台分发：一份规范多平台执行

**Matt Pocock 的规划能力**：
- `/grill-with-docs`：像面试官逐层追问需求边界
- `/domain-model`：梳理实体、值对象、聚合根边界
- **缺少**：结构化的技术方案文档、任务清单、变更存档机制

### 能否替代？

**不能替代**，但可以**组合使用**：

> **OpenSpec 管"想清楚再动手"（规划+存档），Matt Pocock Skills 管"动手时的代码质量"（纪律箱）。**

#### 为什么不能替代

1. **规划深度不同**：OpenSpec 产出 `design.md` 技术方案，Matt 只有需求澄清
2. **存档机制不同**：OpenSpec 有 `archive/` 目录归档决策原因，Matt 无存档
3. **同事协作不同**：OpenSpec 产出人类可读 markdown，Matt 的产出是对话上下文

#### 最佳组合方式

```
OpenSpec /opsx:explore      # 1. 探索需求（Matt 的 /grill-with-docs 可补充）
OpenSpec /opsx:propose      # 2. 生成规划工件（proposal/specs/design/tasks）
CodeGraph impact            # 3. 分析变更影响面
【人工确认】                 # 4. 你的绝对主动权
OpenSpec /opsx:apply        # 5. 按清单实现
Matt Pocock /tdd            # 5a. 实现时：先写测试再写代码
Matt Pocock /code-review    # 6. 实现后：代码审查
OpenSpec /opsx:archive      # 7. 归档决策文档
```

### 核心认知

- **"不知道怎么做"** → 用 OpenSpec `/opsx:explore` 结构化探索
- **"方案试错成本高"** → OpenSpec `design.md` + CodeGraph `impact` 事前分析
- **"代码质量纪律"** → Matt Pocock `/tdd` `/code-review` 按需调用

**结论**：Matt Pocock 是**执行纪律箱**，OpenSpec 是**规划引擎**，两者互补而非替代。重型棕地项目推荐 OpenSpec + CodeGraph + Matt Pocock Skills 三件套组合。

---

## 问题三：按照以上的组合方式，给我一个开发需求的流程整理，重点说明 OpenSpec 中怎么穿插 Matt 的 skill

### 核心分工
- **OpenSpec**：规划引擎（想清楚再动手 + 历史决策留痕）
- **Matt Pocock Skills**：执行纪律箱（TDD / 代码审查 / 调试）

### 完整流程（7 步）

#### 第 1 步：探索需求 — `/opsx:explore`
```
/opsx:explore 我想给系统加 XX 功能，集团要求...
帮我分析：各自的采集点在哪，用什么技术方案最合适。
```
**Matt skill 穿插点**：如果需求特别模糊，可先调 `/grill-with-docs` 盘问对齐，再回来走 OpenSpec 流程。

#### 第 2 步：生成规划工件 — `/opsx:propose`
```
/opsx:propose 实现 XX 功能：...
```
**产出**：四份文档（proposal.md / specs/spec.md / design.md / tasks.md）
**Matt skill 穿插点**：无，这是 OpenSpec 的纯规划阶段。

#### 第 3 步：人工审查（你的绝对主动权）
审查四份文档，不通过就改，通过才推进。**这是关键一步，不要跳**。

#### 第 4 步：按清单实现 — `/opsx:apply` + `/tdd` 配合（核心穿插点）

**这是 OpenSpec 和 Matt Skills 配合的关键点**，有三种配合方式：

**方式一：执行前约定（推荐，最省心）**
```
/opsx:apply 
注意：每一项任务都必须用 TDD 方式实现——先写失败测试，跑红，再写实现让它通过。
不要一口气写完所有代码，每完成一项停下来等我确认再继续下一项。
```
**本质**：把 Matt 的 `/tdd` 纪律"内联"到 OpenSpec 的 apply 执行里。

**方式二：手动叫停，逐项切换**
1. 随时打断："停，先别写第 2 项"
2. 切换到 TDD：`/tdd 重新实现第 1 项，先写失败测试再写实现`
3. 确认通过后：`继续 apply 第 2 项，同样用 TDD 方式`

**方式三：跳过 `/opsx:apply`，直接 `/tdd` 逐项干**
```
/tdd 按 opsx/changes/XX/tasks.md 第 1 项实现，先写失败测试再写实现
```
完成确认后继续下一项。最后手动把 tasks.md 的 `[ ]` 改成 `[x]`，再 `/opsx:archive` 归档。

**三种方式对比**：
| | 方式一：执行前约定 | 方式二：手动叫停 | 方式三：跳过 apply |
|---|---|---|---|
| 省心程度 | ✅ 最省心 | ❌ 最累 | ⚠️ 中等 |
| TDD 纪律强度 | ⚠️ 靠 AI 自觉 | ✅ 你强制 | ✅ 你强制 |
| tasks.md 进度 | ✅ 自动更新 | ⚠️ 可能乱 | ❌ 手动维护 |
| 适合 | **中型功能（推荐）** | 控制狂 | 简单功能 |

**关键认知**：`/opsx:apply` 默认是连贯执行的，AI 会一口气写完所有代码，不会自动停下来等你调 `/tdd`。

#### 第 5 步：代码审查 — `/code-review`
```
/code-review 审查刚才实现的 XX 功能全部代码
```
**Matt skill 穿插点**：OpenSpec 的 `/opsx:apply` 不会强制审查，Matt 的 `/code-review` 补上这块纪律。按 **Critical / Important / Minor** 三级输出问题清单。

#### 第 6 步：修复 + 验证
根据 code-review 结果修复 Critical 和 Important 问题，修复后重新跑测试确认没引入新问题。

**Matt skill 穿插点**：如果跑不起来，用 `/diagnosing-bugs` 系统化定位根因，别让 AI 瞎改：
```
/diagnosing-bugs 测试跑不过，帮我系统化定位根因，不要瞎改
```

#### 第 7 步：归档 — `/opsx:archive`
```
/opsx:archive
```
把整个 `opsx/changes/XX/` 移入 `opsx/archive/`。**这是对抗 AI 遗忘的核心**——所有历史决策永久存档。

### 完整流程一览
```
现有 Java 项目 + 中型功能需求
    │
    ├─ /opsx:explore              # OpenSpec：探索需求（纯对话）
    │    → AI 分析项目现状，给出方案选项
    │    （可选：/grill-with-docs 盘问对齐）
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

### 什么时候可以跳步
| 场景 | 流程 |
|------|------|
| 中型功能（本文） | 完整 7 步 |
| 加一个简单接口 | `/opsx:propose`（轻量）→ `/opsx:apply` 直接写 → `/code-review` |
| 修 bug | `/diagnosing-bugs` 定位 → `/tdd` 修 |
| 需求模糊但改动小 | `/grill-with-docs` 对齐 → `/opsx:apply` |
