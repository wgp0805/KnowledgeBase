---
title: "SpecKit 使用教程（以 OpenSpec 为对照）"
type: synthesis
tags: [AI编程, 规范驱动, SpecKit, OpenSpec, 七阶段流水线, 项目宪法, 教程]
sources:
  - raw/01-articles/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md
last_updated: 2026-10-16
---

# SpecKit 使用教程（以 OpenSpec 为对照）

> **阅读提示**：本页面向用过 [[OpenSpec]] 的读者，用命令对照的方式讲清 [[SpecKit]] 的用法。教程骨架（阶段/命令/定位）来自知识库，标注「通用知识补充」处为 wiki 未记录、按官方惯例补全的细节。

## 一、心智模型：它和 OpenSpec 是什么关系

一句话定位（[[摘要-superpowers-openspec-speckit对比]]）：

> **OpenSpec 管"改了什么"，Spec-Kit 管"按什么规矩干"。**

| 维度 | [[OpenSpec]] | [[SpecKit]] |
| --- | --- | --- |
| 出品方 | FissionAI，57k Star | **GitHub 官方**，115k+ Star |
| 核心主张 | 先对齐需求再写代码（规划引擎） | **规范是可执行的**，直接生成工作代码 |
| 强项 | 棕地项目、增量变更（[[delta-spec]]） | 绿地项目、标准化流水线 |
| 产物 | proposal/spec/design/tasks 四件套 | 宪法 → spec → plan → tasks 产物链 |
| 门槛 | npm 一键 init | Python/uv 技术栈，学习曲线陡峭 |

用过 OpenSpec 的人可以这样理解 SpecKit：**把 `/opsx:propose` 拆成了更细的流水线，并在最前面加了一个 OpenSpec 没有的"项目宪法"阶段。**

## 二、命令对照表（OpenSpec → SpecKit）

| 你想做的事 | OpenSpec 命令 | SpecKit 命令 | 产物 |
| --- | --- | --- | --- |
| 初始化项目 | `openspec-cn init` | `specify-cli init` | 各自的命令/Skill 文件 |
| （OpenSpec 无对应） | — | `/speckit.constitution` | 项目宪法：代码质量/测试/UX/性能治理原则 |
| 探讨需求 | `/opsx:explore` | 直接对话（无独立命令） | — |
| 描述需求 What/Why | `/opsx:propose`（spec 部分） | `/speckit.specify` | `specs/<feature>/spec.md` |
| 技术方案设计 | `/opsx:propose`（design 部分） | `/speckit.plan` | `plan.md`：技术栈/架构/API 契约 |
| 拆任务清单 | `/opsx:propose`（tasks 部分） | `/speckit.tasks` | `tasks.md` |
| 一致性检查 | （无独立命令） | `/speckit.analyze` | 冲突/遗漏报告 |
| 执行实现 | `/opsx:apply` | `/speckit.implement` | 实际代码 |
| 归档 | `/opsx:archive` | `/speckit.archive`（通用知识补充，wiki 未记录） | 归档目录 |

关键理解：OpenSpec 的 `/opsx:propose` 一口气生成 proposal + spec + design + tasks；SpecKit 把它**拆成 specify → plan → tasks 三步强制逐阶段确认**，中间还塞了 analyze 做一致性检查——这就是 [[SpecKit]] 页说的"像工厂流水线，每阶段输入输出明确"。

## 三、安装

来自 [[SpecKit]] 页（wiki 中命令记录到 `--from` 处截断，完整命令为通用知识补充）：

```bash
# 1. 安装 uv（Python 包管理器）
curl -LsSf https://astral.sh/uv/install.sh | sh        # Windows: pip install uv

# 2. 安装 Specify CLI（通用知识补充）
uv tool install specify-cli --from git+https://github.com/github/spec-kit

# 3. 在项目里初始化（对照 openspec-cn init）
cd your-project
specify-cli init        # 交互式，会提示选择 AI 编码工具
```

初始化后会在 AI 工具目录下生成 `/speckit.*` 命令（类似 OpenSpec 生成 `/opsx:*`），支持 Claude Code、Copilot、Cursor 等 25+ 种代理（[[SpecKit]]）。

## 四、实战流程：以"订单导出功能"为例

假设给现有 Java 项目加"订单导出 Excel"功能：

**第 0 步（仅 SpecKit）——立宪法**

```
/speckit.constitution
```

生成或手写项目治理原则，例如"所有接口必须有单测"、"Service 层禁止直接返回 DTO"、"分页查询必须走索引"。这是 OpenSpec 没有的一步——对应 [[claude-code-增强框架对比]] 所述的"项目宪法机制从顶层约束 AI 行为"。**一次性做，之后所有阶段都被它约束。**

**第 1 步——写规范（What/Why，不谈技术）**

```
/speckit.specify 订单导出功能：支持按时间范围和状态筛选，
导出 Excel，单次最多 5 万行，后台异步生成并邮件通知
```

→ 生成 `spec.md`，只有需求和验收标准，**不涉及用 EasyExcel 还是 POI**（对应 OpenSpec 的 `specs/spec.md`，同样是 SHALL/MUST + Given/When/Then 风格）。

**第 2 步——做计划（技术方案）**

```
/speckit.plan
```

→ 生成 `plan.md`：技术栈（EasyExcel + ThreadPoolTaskExecutor + Redis 任务状态）、API 契约、表设计（对应 OpenSpec 的 `design.md`）。

**第 3 步——拆任务**

```
/speckit.tasks
```

→ 生成带编号、可勾选的 `tasks.md`（对应 OpenSpec 的 `tasks.md`）。

**第 4 步——一致性检查（SpecKit 独有）**

```
/speckit.analyze
```

→ 检查 spec/plan/tasks 三者是否互相矛盾、有无遗漏和歧义。OpenSpec 把这一步隐含在人工审阅 proposal 里。

**第 5 步——实现**

```
/speckit.implement
```

→ 按 tasks 逐项写代码（对应 `/opsx:apply`）。

之后每个新功能重复 1~5；变更旧功能时，OpenSpec 的 Delta Spec（`ADDED/MODIFIED/REMOVED` 增量标记，[[delta-spec]]）对棕地项目更省事，SpecKit 倾向重新走一遍完整规范。

## 五、选型与组合建议

（[[agent-spec-framework-comparison-and-matt-skills-workflow]]、[[摘要-superpowers-openspec-speckit对比]]）

- **绿地新项目 / 要标准化流水线** → SpecKit
- **棕地老项目 / 小步快跑改需求** → OpenSpec 更合适
- **理想组合**：`/speckit.constitution` 定一次项目宪法 → 日常变更走 `/opsx:*` 流程 → 需要执行纪律时叠加 Superpowers/Matt Skills
- **反方观点**（[[SpecKit]] 页记录）：[[MattPocock]] 批评 Spec-Kit 属于"接管流程"的重量级框架——控制权被拿走、流程本身出 bug 难排查；主张用小而可组合的 skill 替代

## 关联连接

- [[SpecKit]] — 主角实体页（七阶段流水线、优缺点、Matt 批评视角）
- [[OpenSpec]] — 对照对象，规划引擎
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比来源
- [[claude-code-增强框架对比]] — ECC/Superpowers/OpenSpec/Spec-Kit 横向选型
- [[agent-spec-framework-comparison-and-matt-skills-workflow]] — 全景对比 + 实战流程
- [[规范驱动开发]] — 上层方法论
- [[delta-spec]] — OpenSpec 增量变更机制
- [[project-analysis-planning-tool-selection]] — 需求规划工具选型
- [[Superpowers]] — 管"怎么干"的兄弟方案
