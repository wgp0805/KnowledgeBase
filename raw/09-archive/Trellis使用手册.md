# Trellis 使用手册

> 适用对象：希望在 AI 编码工作流中持续使用项目规范、任务规划和会话记忆的个人开发者或团队。本文按 Trellis 官方中文文档整理，重点覆盖 Codex，也标出通用用法。

## 1. Trellis 是什么

Trellis 是 AI 编码助手的项目级工作流框架：把编码规范（Spec）、任务文档（Task）、会话日志（Workspace）和自动触发的 Skills 结合起来，让 AI 在每个会话中按同一套约定完成规划、开发、检查和收尾。

它并不是替代 Codex、Claude Code 或 Cursor 的模型，而是为这些平台提供共同的项目上下文与开发流程。当前支持 Codex、Claude Code、Cursor、OpenCode、Kiro、Gemini CLI、Copilot 等平台；核心 `.trellis/` 目录在各平台之间通用。

## 2. 开始前准备

### 2.1 环境要求

- 操作系统：Windows、macOS、Linux。
- Node.js 18 或更高版本。
- Python 3.9 或更高版本。
- 已安装至少一个 AI 编码平台；以下示例以 Codex 为主。

### 2.2 安装与初始化

在终端执行：

```bash
# 安装 Trellis CLI
npm install -g @mindfoldhq/trellis@latest

# 进入需要接入的仓库
cd your-project

# 初始化 Codex 配置，并设置本机开发者身份
trellis init -u your-name --codex
```

`your-name` 会写入本机的 `.trellis/.developer`，并建立 `.trellis/workspace/your-name/`。这个身份文件会被 Git 忽略；而项目规范、任务和工作日志通常随仓库共享。

如需同时使用多个 AI 工具，可在同一仓库追加平台：

```bash
trellis init --cursor
trellis init --claude --opencode
```

不要为了新增平台重新完整初始化已有项目；直接运行 `trellis init`，在交互菜单中选择 **Add AI platform(s)**。新成员只应选择 **Set up developer identity on this device**。

### 2.3 Codex 必做配置

在 `~/.codex/config.toml` 中启用 Hook：

```toml
[features]
hooks = true
```

对于 Codex 0.129+，还需要在 TUI 中运行一次 `/hooks`，审批 Trellis 安装的 `UserPromptSubmit` Hook。这样工作流状态会在每次提交消息时注入，`/start`、`/continue`、`/finish-work` 等入口也能在命令菜单出现。

未启用 Hook 时，Codex 仍会通过仓库根目录的 `AGENTS.md` 读取基础上下文，但命令入口和自动状态提示会受限。

## 3. 初始化后会得到什么

```text
.trellis/
├── workflow.md              # 开发阶段与状态规则
├── config.yaml              # 共享项目配置
├── spec/                    # 可复用的编码规范库
├── tasks/                   # 活跃任务与归档任务
├── workspace/               # 开发者索引与会话日志
├── .runtime/                # 会话当前任务指针（忽略 Git）
└── scripts/                 # task.py、get_context.py 等工具

.codex/
├── prompts/                 # start / continue / finish-work 入口
├── skills/                  # Trellis 自动工作流模块
├── agents/                  # 可选的 implement/check/research 子代理
└── hooks/                   # 每回合工作流状态注入

AGENTS.md                    # Codex 自动读取的项目入口
```

第一次初始化还会创建 `00-bootstrap-guidelines` 引导任务，以及一组待填写的 Spec 模板。新项目先补齐当前真正需要的规则；存量项目则应从现有代码提取真实做法，不能把“理想状态”伪装成既有规范。

## 4. 日常使用：把一次开发任务跑完

### 4.1 从自然语言需求开始

通常直接告诉 AI 要做什么即可，例如：

```text
新增用户登录功能。请先判断是否应该创建 Trellis task；如果需要，先和我确认范围、验收标准和风险，再进入实现。
```

Trellis 会先分类请求：

| 类型 | 典型情况 | 处理方式 |
|---|---|---|
| 简单对话 | 解释、查询、讨论 | 默认不创建任务 |
| 小型 inline 改动 | 一轮可理解、可验证的局部修改 | 询问是否需要任务；拒绝后直接改 |
| 完整任务 | 多文件、跨层、需调研或长期规划的工作 | 先征得创建任务许可，再进入规划 |

同意“创建任务”只表示可以开始规划，不表示已经同意实现。规划产物经检查并由你确认后，才应进入开发。

### 4.2 Plan：先把任务讲清楚

AI 创建任务后，任务状态为 `planning`。常见目录是 `.trellis/tasks/MM-DD-task-name/`，其中包含：

- `task.json`：状态、负责人、优先级、分支等元数据。
- `prd.md`：每个任务都必须有；写明目标、约束、验收标准与不做什么。
- `design.md`：复杂任务的边界、数据流、兼容性、取舍与回滚方案。
- `implement.md`：有序实施清单、验证命令、审查关口与回滚点。
- `research/`：调研结论。
- `implement.jsonl`、`check.jsonl`：给实现和检查阶段加载的稳定上下文清单。

这一阶段通常由 `trellis-brainstorm` 处理。建议在 PRD 中明确：用户行为、接口与数据变化、权限、错误处理、测试、发布或回滚，以及 out-of-scope。

### 4.3 Execute：实现前先读取相关规范

规划确认后，任务转为 `in_progress`。实现时，Trellis 会按照以下顺序加载上下文：

```text
implement.jsonl / check.jsonl 的条目
→ prd.md
→ design.md（如果存在）
→ implement.md（如果存在）
```

`implement.jsonl` 和 `check.jsonl` 只放**规范文件**和**任务调研文件**，不要预先登记即将修改的源码；源码会在实际实现时读取。例如：

```jsonl
{"file": ".trellis/spec/backend/index.md", "reason": "后端开发规范"}
{"file": ".trellis/tasks/07-15-user-login/research/auth.md", "reason": "认证方案结论"}
```

`trellis-before-dev` 会在动手前匹配并读取规范。Codex 默认用 `inline` 模式，即由主会话实现和检查；如果确实要使用旧式子代理拆分，可在 `.trellis/config.yaml` 中设为 `sub-agent`。

### 4.4 Check：验证、修复、再验证

实现后 `trellis-check` 会核对 PRD、设计与实施计划、关联 Spec、改动文件和本地的 lint、类型检查、测试或格式化命令。它不应只报告问题；可修复的问题应修复后重新检查。

遇到难以复现、同类问题反复出现的 Bug，可要求 AI 运行 `trellis-break-loop`：先找根因，再补测试、环境检测或 Spec 规则，避免只修症状。

### 4.5 Finish：提交、归档、记录会话

完成代码验证并先提交工作代码后，使用：

```text
/finish-work
```

Trellis 会归档完成的任务，并向 `.trellis/workspace/<your-name>/journal-N.md` 追加会话记录。该命令会拒绝在工作代码仍未提交时收尾，以保证提交顺序是：工作提交 → 任务归档提交 → journal 提交。

如果 AI 停在某个阶段或你不知道下一步，使用：

```text
/continue
```

它会读取当前任务状态、已有产物和 `workflow.md`，继续推进当前任务，而不是开始一个新任务。

## 5. 你真正需要记住的命令

### 会话命令（Codex）

| 命令 | 什么时候用 |
|---|---|
| `/start` | 重新加载/查看项目上下文；已启用 Hook 时通常自动完成 |
| `/continue` | 当前任务在计划、实现、检查或收尾之间推进 |
| `/finish-work` | 工作代码已提交且验收完成后，归档任务并记 journal |

### CLI 升级命令

```bash
# 升级全局 CLI
trellis upgrade

# 再把当前仓库的模板、Skill、Hook 同步到本机 CLI 版本
trellis update

# 文档提示存在破坏性迁移时使用；建议先加 --dry-run 预览
trellis update --migrate
```

升级是两步：`upgrade` 更新全局 CLI，`update` 更新当前项目。只运行 `update` 不会把项目升到比本机 CLI 更高的版本。

### 可选：手动管理任务

日常可交给 AI，但需要排查或脚本化时可使用：

```bash
# 创建任务
./.trellis/scripts/task.py create "新增用户登录" --slug user-login

# 将任务设为当前会话任务
./.trellis/scripts/task.py start .trellis/tasks/07-15-user-login

# 检查 JSONL 上下文引用是否存在
./.trellis/scripts/task.py validate .trellis/tasks/07-15-user-login

# 清除当前会话的 active task 指针
./.trellis/scripts/task.py finish
```

## 6. 如何写出有效的 Spec

Spec 是 AI 写代码前要遵守的项目契约，推荐放在 `.trellis/spec/`。一个层级目录只要带有 `index.md`，就会被 Trellis 识别为一个 Spec 层；目录名可按前后端、包、运行时或职责自行组织。

写法原则：

- 写真实路径、真实类型和真实代码例子，不写“代码应整洁”一类空泛要求。
- 每条规则都说明原因或风险。
- 一个文件聚焦一个主题，例如 API 输入校验、错误模型、组件结构或测试约定。
- `index.md` 保持短小：每行只列一个 Spec 文件和用途；正文放在具体文件中。
- 可将每份 Spec 控制在约 200–500 行，每小节约 20–50 行；发现过时内容应立即更新。

任务结束时，`trellis-update-spec` 会判断哪些结论可长期复用：稳定的团队规则提升到 `.trellis/spec/`；仅对当前任务成立的事实保留在任务目录中。

## 7. 常用配置

`.trellis/config.yaml` 是需要提交的团队配置，不能放 token、API Key 或个人机器绝对路径。常用项：

```yaml
# 会话日志的提交信息与单个日志文件最大行数
session_commit_message: 'chore: record journal'
max_journal_lines: 2000

# 若团队希望手动审查归档/journal 变更，可关闭自动提交
session_auto_commit: false

# Codex 默认 inline；只有确有需要才使用 sub-agent
codex:
  dispatch_mode: inline

# 可选：任务生命周期自动化，例如同步项目管理工具或触发 CI
hooks:
  after_create:
    - "echo 'Task created'"
  after_archive:
    - "echo 'Task archived'"
```

可用的生命周期事件为 `after_create`、`after_start`、`after_finish`、`after_archive`。Hook 失败只会发出警告，不会阻塞任务操作。

对于 monorepo，可在 `packages` 中声明前端、后端和文档等包，并用 `default_package` 指定默认包；让不同任务只引入相关包的 Spec。

## 8. 推荐落地方式

### 新项目

1. 执行 `trellis init`，完成 bootstrap 任务。
2. 与 AI 先确定技术栈、目录结构、API 形状、错误处理和测试策略。
3. 只填当前需要的最小 Spec，并人工审查。
4. 选一个可端到端交付的小功能，完整跑一遍 Plan → Execute → Check → Finish。

### 存量项目

1. 初始化后让 AI 扫描现有代码，从真实 API、鉴权、日志、测试、表单等模式提取 Spec。
2. 每条规则都要求能指向仓库中的实际文件；删掉不能追溯的“想当然”规则。
3. 先选择一个 feature 或 bugfix 作为试点。
4. 观察 AI 是否显著减少了对同类本地约定的重复询问，再逐步扩大覆盖范围。

## 9. 易错点与排查

- **AI 跳过流程直接改代码**：明确说“先按 Trellis 分类请求；未经我同意不要创建 task；未经 planning review 不要实现”。反复发生时，应加强 `.trellis/workflow.md` 中对应状态的提示。
- **`finish-work` 无法执行**：先提交工作代码；它只负责归档和 journal，不负责替你提交未提交的实现。
- **`trellis update` 版本没有变化**：先运行 `trellis upgrade` 更新全局 CLI，再运行 `trellis update`；遇到 `MIGRATION REQUIRED` 使用 `trellis update --migrate`。
- **Spec 让上下文太大**：规划阶段只读各层 `index.md`，把真正相关的具体 Spec 精确列入 JSONL；不要全量加载规范库。
- **新同事或换机器**：运行 `trellis init -u <name>` 建立本机身份，不要对共享项目执行 Full re-initialize。

## 官方资料

- [Trellis 概览](https://docs.trytrellis.app/zh)
- [安装与第一项任务](https://docs.trytrellis.app/zh/start/install-and-first-task)
- [工作流原理](https://docs.trytrellis.app/zh/start/how-it-works)
- [命令、任务与 Spec](https://docs.trytrellis.app/zh/start/everyday-use)
- [Codex 与多平台配置](https://docs.trytrellis.app/zh/advanced/multi-platform)
- [config.yaml 配置参考](https://docs.trytrellis.app/zh/advanced/configuration)
- [FAQ](https://docs.trytrellis.app/zh/advanced/appendix-f)

