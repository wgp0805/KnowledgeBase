# Everything Claude Code (ECC) 完整使用教程（超详细版）

> 专注于 **Claude Code** 和 **OpenCode** 两个工具，手把手教你从零到精通。
> 版本基准：ECC v1.10.0+ | 仓库：https://github.com/affaan-m/ECC

---

## 目录

- [第 1 章 ECC 到底是什么](#第-1-章-ecc-到底是什么)
- [第 2 章 核心概念详解（必须理解）](#第-2-章-核心概念详解必须理解)
- [第 3 章 在 Claude Code 中使用 ECC](#第-3-章-在-claude-code-中使用-ecc)
- [第 4 章 在 OpenCode 中使用 ECC](#第-4-章-在-opencode-中使用-ecc)
- [第 5 章 命令详解与实战场景](#第-5-章-命令详解与实战场景)
- [第 6 章 Agents 代理详解](#第-6-章-agents-代理详解)
- [第 7 章 Skills 技能详解](#第-7-章-skills-技能详解)
- [第 8 章 Hooks 钩子系统](#第-8-章-hooks-钩子系统)
- [第 9 章 Continuous Learning（持续学习）](#第-9-章-continuous-learning持续学习)
- [第 10 章 AgentShield 安全扫描](#第-10-章-agentshield-安全扫描)
- [第 11 章 完整工作流实战](#第-11-章-完整工作流实战)
- [第 12 章 性能与上下文优化](#第-12-章-性能与上下文优化)
- [第 13 章 常见问题排查](#第-13-章-常见问题排查)

---

## 第 1 章 ECC 到底是什么

### 1.1 一句话解释

**ECC = 给 AI 编码助手装的"外挂系统"**。它不是取代 Claude Code 或 OpenCode 的新工具，而是安装在这两者之上的 **增强层**，提供：

- 预定义的工作流（TDD、代码审查、安全扫描等）
- 专业化的子代理（规划者、架构师、代码审查员等）
- 自动化钩子（保存时自动格式化、提交前检查等）
- 持续学习系统（记住你过去是怎么写代码的）
- 安全扫描器（检测配置漏洞和提示注入）

### 1.2 为什么你需要 ECC

**没有 ECC 的 Claude Code：**
```
你："帮我写个用户登录功能"
Claude：好的，马上开始写...
        （没有计划、没有测试、没有安全审查）
你：（写完发现没考虑边界情况）
```

**有 ECC 的 Claude Code：**
```
你："帮我写个用户登录功能"
ECC 拦截并启动 planner agent
  → 生成实施计划（含风险评估、依赖分析、阶段划分）
  → 你审核批准
  → tdd-guide agent 介入，先写测试
  → 实现代码
  → code-reviewer agent 自动审查
  → security-reviewer agent 安全检查
  → 完成
```

### 1.3 ECC 的六层架构

```
┌─────────────────────────────────────────────────────┐
│  Rules（规则）  ──  必须遵守的约束                     │
│  ~/.claude/rules/*.md                                │
│  例如：测试覆盖率必须 ≥80%、禁止 console.log 提交       │
├─────────────────────────────────────────────────────┤
│  Skills（技能）  ──  如何完成特定任务的工作流           │
│  ~/.claude/skills/*/SKILL.md                         │
│  例如：TDD 工作流、安全审查检查清单、API 设计模式       │
├─────────────────────────────────────────────────────┤
│  Agents（代理）  ──  能完成特定任务的"专家"             │
│  ~/.claude/agents/*.md                               │
│  例如：planner（规划者）、tdd-guide（TDD 专家）        │
├─────────────────────────────────────────────────────┤
│  Hooks（钩子）  ──  自动触发的检查/动作                │
│  ~/.claude/settings.json 中配置                       │
│  例如：编辑 .ts 文件后自动 tsc、提交前检查密钥泄露      │
├─────────────────────────────────────────────────────┤
│  MCPs（外部服务） ──  连接外部工具                     │
│  例如：GitHub、数据库、Context7 实时文档                │
├─────────────────────────────────────────────────────┤
│  Continuous Learning  ──  从历史中学习                  │
│  例如：记住你喜欢用 pnpm 而非 npm，记住测试习惯         │
└─────────────────────────────────────────────────────┘
```

---

## 第 2 章 核心概念详解（必须理解）

### 2.1 Skills vs Commands vs Agents 的关系

这是新手最容易混淆的概念。用餐厅做比喻：

| 概念 | 比喻 | 说明 |
|------|------|------|
| **Agent（代理）** | **厨师长** | 负责统筹某个任务的人。planner 负责规划、tdd-guide 负责测试 |
| **Skill（技能）** | **菜谱** | 告诉"人"怎么做事的详细步骤文档，约 200-550 行 |
| **Command（命令）** | **按铃** | 快捷入口，你按一下（输命令）就触发一个工作流 |

**执行流程：**
```
你输入 /plan "添加登录功能"
    → Command /plan（按铃）
        → 调用 planner agent（叫厨师长）
            → 读取 tdd-workflow skill（看菜谱）
                → 开始工作
```

**核心要点：**
- **Skill 是最重要的**：它包含了真正的详细工作流。ECC 官方说"skills-first"。
- **Command 已经过时**：ECC 官方明确说 commands 是"legacy shims"（遗留兼容层），新功能都做成 skill。
- **Agent 是执行者**：它读取 skill 的内容并执行。

### 2.2 Skill 的文件结构

每条 skill 是一个文件夹，里面必须包含 `SKILL.md`：

```
~/.claude/skills/tdd-workflow/       ← 文件夹名 = skill 名
├── SKILL.md                         ← 主文件（必须）
├── examples/                        ← 可选：示例代码
├── templates/                       ← 可选：模板文件
└── codemap.md                       ← 可选：代码库导航
```

`SKILL.md` 的格式：
```markdown
---
name: tdd-workflow                    # 技能名（必须 = 文件夹名）
description: >                        # 描述（必须）
  测试驱动开发工作流。当需要实现新功能、修复 bug 或重构时激活。
  强制先写测试、再实现、再重构，保持 80%+ 覆盖率。
origin: ECC                           # 可选：来源
version: "1.0"                        # 可选：版本
---

# TDD 工作流

## 何时激活
- 用户说"写一个新功能"时
- 用户说"修复这个 bug"时
- 任何需要编写代码的场景

## 详细步骤
1. RED：先写测试，测试**必须失败**
2. GREEN：写最少代码让测试通过
3. IMPROVE：重构，保持 80%+ 覆盖率

## 反模式（禁止）
- ❌ 先写实现再补测试
- ❌ 覆盖率不足 80%
- ❌ 测试依赖共享状态
...
```

### 2.3 Agent 的定义格式

每个 agent 也是一个 `.md` 文件：

```markdown
---
name: tdd-guide
description: 测试驱动开发专家，强制先写测试后写代码
tools: ["Read", "Write", "Edit", "Bash", "Grep"]
model: sonnet
---

# TDD Guide Agent

你是 TDD 专家，确保所有代码都测试先行...

## 工作流程
1. 分析需求 → 确定接口
2. 编写失败测试（RED）
3. ...
```

### 2.4 Rules vs Skills 的本质区别

很多用户分不清，这里用一句话说清楚：

- **Rules**：告诉 AI **"不许做什么"**（约束）—— 比如"不要提交未测试的代码"
- **Skills**：告诉 AI **"应该怎么做"**（方法）—— 比如"先写测试，然后这样实现..."

Rules 永远生效，Skills 只在被激活时加载。

---

## 第 3 章 在 Claude Code 中使用 ECC

### 3.1 安装前必读

**最重要的规则：只选一条安装路径，不要堆叠！**

```
❌ 错误做法：
  /plugin install ecc@ecc     ← 先装插件
  ./install.sh --profile full  ← 再手动安装
  → 重复的技能和钩子导致行为异常

✅ 正确做法：选其一
  路径 A：插件安装（推荐给大多数用户）
  路径 B：手动安装（需要精细控制）
```

### 3.2 路径 A：插件安装（推荐）

#### 步骤 1：确认环境
```bash
# 检查 Claude Code 版本（需要 ≥2.1.0）
claude --version
```

#### 步骤 2：添加市场源并安装
```bash
# 在 Claude Code 会话中执行
/plugin marketplace add https://github.com/affaan-m/ECC
```
这条命令的作用是告诉 Claude Code："这个 GitHub 仓库是一个插件市场，我可以从这里安装插件"。它会在 `~/.claude/settings.json` 中添加市场配置。

```bash
/plugin install ecc@ecc
```
`ecc@ecc` 的格式是 `插件名@市场标识`。安装后，ECC 的 skills、commands、hooks、agents 立即可用。

#### 步骤 3：手动复制 Rules（必须做）

> ⚠️ **为什么不能通过插件自动安装 Rules？**
> Claude Code 的插件系统有一个上游限制：插件不能自动分发 `rules/` 目录下的文件。这不是 ECC 的问题，是所有 Claude Code 插件都有的限制。所以 rules 必须手动复制。

```bash
# 先克隆仓库（如果本地还没有）
git clone https://github.com/affaan-m/ECC.git
cd ECC

# 安装 npm 依赖
npm install

# 创建 ECC 专用的 rules 命名空间目录
mkdir -p ~/.claude/rules/ecc

# 复制通用规则（必装）
cp -r rules/common ~/.claude/rules/ecc/

# 按需复制语言规则（选你用的技术栈即可，不要全装）
cp -r rules/typescript ~/.claude/rules/ecc/
cp -r rules/python ~/.claude/rules/ecc/
```

**为什么不直接把 rules 文件复制到 `~/.claude/rules/` 根目录？**
- 因为 ECC 的 rules 中有相对引用（如 `common/testing.md` 引用了同级的其他文件）
- 复制到 `ecc/` 子目录下保持目录结构完整，引用不受影响
- 也方便日后卸载——删掉 `ecc/` 文件夹即可

#### 步骤 4：验证安装
```bash
/plugin list ecc@ecc              # 列出所有命令
/ecc:plan "测试插件是否可用"        # 测试一个命令
```

#### 步骤 5：安装额外技能（选择性）
插件只安装了 core skills，其他专业 skills 需要手动复制：
```bash
# 从克隆的 ECC 仓库执行
mkdir -p ~/.claude/skills/ecc
cp -r skills/security-review ~/.claude/skills/ecc/
cp -r skills/api-design ~/.claude/skills/ecc/
cp -r skills/backend-patterns ~/.claude/skills/ecc/
```

### 3.3 路径 B：手动安装（精细控制）

适用于以下情况：
- 不想用插件系统
- 想精确控制安装了哪些内容
- 使用 OpenCode、Cursor 等其他编码助手

```bash
# 克隆
git clone https://github.com/affaan-m/ECC.git
cd ECC
npm install

# 安装脚本提供了 3 种 profile
./install.sh --profile minimal   # 仅 rules + agents + core skills，无 hooks
./install.sh --profile core      # minimal + all skills + hooks（推荐）
./install.sh --profile full      # 全部内容（可能太多）

# Windows PowerShell
.\install.ps1 --profile core
```

**三种 Profile 的选择建议：**

| Profile | 包含内容 | 推荐场景 |
|---------|---------|---------|
| `minimal` | rules + agents + commands + 核心 skills | 新手起步、只想用规则 |
| `core` | minimal + 所有 skills + hooks | **大多数用户的选择** |
| `full` | core + 所有 MCP 配置 + 示例 | 资深用户、想探索全部功能 |

### 3.4 验证安装是否成功

```bash
# 检查规则是否安装
ls ~/.claude/rules/ecc/
# 应该看到 common/ typescript/ 等目录

# 检查技能
ls ~/.claude/skills/
# 应该看到 tdd-workflow/ security-review/ 等

# 检查代理
ls ~/.claude/agents/
# 应该看到 planner.md tdd-guide.md 等

# 测试命令
/plan "验证 ECC 是否正常工作"
```

### 3.5 插件安装后使用命令的注意事项

- **插件安装**：命令使用命名空间形式 `/ecc:plan`、`/ecc:tdd`
- **手动安装**：命令使用短形式 `/plan`、`/tdd`

---

## 第 4 章 在 OpenCode 中使用 ECC

### 4.1 OpenCode 的优势

OpenCode 相比 Claude Code 在插件系统上更强大：

| 特性 | Claude Code | OpenCode |
|------|------------|----------|
| 钩子事件类型 | 8 种 | **20+ 种** |
| 自定义工具 | 通过 hooks 模拟 | **6 个原生工具** |
| Skill 格式 | SKILL.md | SKILL.md（**兼容**） |
| 插件 API | 有限 | **更丰富的插件 API** |

**最重要的差异**：OpenCode 的 `file.edited`（文件编辑后触发）和 `lsp.client.diagnostics`（LSP 诊断后触发）等事件是 Claude Code 没有的，可以实现更精细的自动化。

### 4.2 方法一：npm 包安装（推荐）

```bash
npm install -g opencode-ecc
# 或
npm install -g ecc-universal    # 通用包，同时支持 Claude Code 和 OpenCode
```

在项目根目录的 `opencode.json` 中添加：
```json
{
  "plugin": ["opencode-ecc"]
}
```

或者全局配置 `~/.config/opencode/opencode.json`：
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-ecc"]
}
```

### 4.3 方法二：直接克隆运行

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
opencode
```

这会在 ECC 仓库内部直接启动 OpenCode，自动加载所有配置。但这样只能在 ECC 目录下使用，不实用。

### 4.4 方法三：复制配置到你的项目（推荐）

这是大多数用户的最佳选择。从 ECC 仓库复制相关文件到你的项目：

```bash
# 克隆 ECC 仓库
git clone https://github.com/affaan-m/ECC.git
cd ECC

# 在项目根目录创建 .opencode 目录
mkdir -p /你的项目/.opencode/agents
mkdir -p /你的项目/.opencode/commands
mkdir -p /你的项目/.opencode/skills

# 复制 agents
cp -r .opencode/agents/* /你的项目/.opencode/agents/

# 复制 commands
cp -r .opencode/commands/* /你的项目/.opencode/commands/

# 复制 skills（只复制你需要的，不要全装）
cp -r skills/tdd-workflow /你的项目/.opencode/skills/
cp -r skills/security-review /你的项目/.opencode/skills/
cp -r skills/coding-standards /你的项目/.opencode/skills/
```

### 4.5 OpenCode 配置文件详解

创建/修改项目根目录的 `opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-20250514",
  "small_model": "anthropic/claude-haiku-4-20250514",

  "instructions": [
    ".opencode/skills/tdd-workflow/SKILL.md",
    ".opencode/skills/security-review/SKILL.md",
    ".opencode/skills/coding-standards/SKILL.md"
  ],

  "agent": {
    "planner": {
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:.opencode/agents/planner.md}",
      "permission": {
        "read": "allow",
        "glob": "allow",
        "grep": "allow",
        "edit": "deny",
        "bash": "deny"
      }
    },
    "code-reviewer": {
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:.opencode/agents/code-reviewer.md}",
      "permission": {
        "read": "allow",
        "edit": "deny",
        "bash": {
          "*": "ask",
          "git diff": "allow",
          "git log*": "allow"
        }
      }
    },
    "tdd-guide": {
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:.opencode/agents/tdd-guide.md}",
      "permission": {
        "read": "allow",
        "edit": "allow",
        "bash": "allow"
      }
    }
  },

  "command": {
    "plan": {
      "description": "创建实施计划",
      "prompt": "运行 planner agent，创建详细的实施计划"
    },
    "tdd": {
      "description": "TDD 工作流",
      "prompt": "运行 tdd-guide agent，强制执行测试先行"
    },
    "code-review": {
      "description": "代码审查",
      "prompt": "运行 code-reviewer agent，审查代码质量"
    }
  },

  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

**关键配置项解释：**

- `model` 和 `small_model`：主模型和轻量模型。主模型用于主要工作，小模型用于搜索/分析等轻量任务
- `instructions`：告诉 OpenCode 始终加载哪些 skill 文件（类似 AGENTS.md 的补充）
- `agent`：定义子代理。`mode: subagent` 表示这是可以被主 agent 调用的子代理
- `command`：定义斜杠命令
- `permission.skill`：控制哪些 skill 可以被哪些 agent 访问。`*: allow` 表示默认允许所有

**Agent 权限设计的哲学：**

```json
"code-reviewer": {
  "permission": {
    "edit": "deny",          // 审查者不能改代码
    "bash": {
      "*": "ask",            // 大多数命令需要询问
      "git diff": "allow",   // 但 git diff 可以直接运行
      "git log*": "allow"    // git log 也可以
    }
  }
}
```

这种精细权限控制的目的是安全：
- **planner** 只需要读权限（Read、Glob、Grep），不能改代码
- **code-reviewer** 可以读代码、运行 git 命令，但不能编辑文件
- **tdd-guide** 需要完全权限（要写测试和代码）

### 4.6 OpenCode 的 AGENTS.md 配置

在项目根目录创建/修改 `AGENTS.md`，添加 ECC 相关指令：

```markdown
# AGENTS.md - 项目规则

## 开发工作流

1. 在写任何代码之前，先使用 planner agent 制定计划
2. 所有新功能必须使用 tdd-guide agent（测试先行）
3. 代码写完后必须运行 code-reviewer agent 审查
4. 安全敏感的代码必须运行 security-reviewer agent

## ECC Agents

本项目安装了以下 ECC 代理：
- @planner - 实施规划
- @code-reviewer - 代码审查
- @tdd-guide - 测试驱动开发

## 测试要求
- 测试覆盖率必须 ≥ 80%
- 必须测试边界情况（null、空值、错误路径）
```

然后在需要使用 agent 时，在对话中用 `@` 引用：
```
@planner 请为"用户认证系统"创建一个实施计划
@code-reviewer 请审查刚刚修改的 auth.ts
```

### 4.7 OpenCode 钩子事件映射

ECC 的钩子系统在 OpenCode 中的事件映射：

| Claude Code 事件 | OpenCode 事件 | 触发时机 |
|-----------------|---------------|---------|
| PreToolUse | `tool.execute.before` | 工具执行前 |
| PostToolUse | `tool.execute.after` | 工具执行后 |
| Stop | `session.idle` | Claude 回复完成 |
| SessionStart | `session.created` | 会话开始 |
| SessionEnd | `session.deleted` | 会话结束 |
| — | `file.edited` | **文件被编辑后**（Claude Code 无此事件） |
| — | `file.watcher.updated` | **文件监视器更新** |
| — | `message.updated` | **消息更新** |
| — | `lsp.client.diagnostics` | **LSP 诊断结果** |

### 4.8 OpenCode 原生自定义工具

ECC 为 OpenCode 提供了 3 个原生自定义工具（Claude Code 中只能通过 hooks 模拟）：

| 工具名 | 功能 | 使用方法 |
|--------|------|---------|
| `run-tests` | 运行测试套件 | 带选项（指定文件、watch 模式等） |
| `check-coverage` | 分析测试覆盖率 | 返回覆盖率报告 |
| `security-audit` | 安全漏洞扫描 | 扫描代码库安全漏洞 |

### 4.9 在 OpenCode 中使用 Skill 权限控制

OpenCode 的 skill 权限系统非常灵活：

```json
{
  "permission": {
    "skill": {
      "*": "allow",           // 默认允许所有 skill
      "internal-*": "deny",   // 但 internal- 开头的禁止
      "experimental-*": "ask" // experimental- 开头的需要询问
    }
  }
}
```

也可以针对特定 agent 设置不同的 skill 权限：
```json
{
  "agent": {
    "plan": {
      "permission": {
        "skill": {
          "internal-*": "allow"    // planner agent 可以访问 internal 技能
        }
      }
    },
    "code-reviewer": {
      "permission": {
        "skill": {
          "internal-*": "deny"     // code-reviewer 不能访问 internal 技能
        }
      }
    }
  }
}
```

---

## 第 5 章 命令详解与实战场景

### 5.1 /plan — 实施计划（最重要的命令）

**用途**：在写任何代码之前先制定计划。

**为什么必须先 /plan？**
- 没有 plan 的 AI 编码：直接开始写，可能偏离方向
- 有 plan 的 AI 编码：先分析需求、评估风险、划分阶段，**等你批准后才开始写**

**实战示例**：

```
你：/plan "为我的博客添加评论功能，支持 Markdown 渲染"

AI（planner agent 启动）：
┌─────────────────────────────────────────────────────┐
│  📋 实施计划：博客评论功能                            │
│                                                     │
│  阶段 1：数据库设计                                   │
│  - 创建 comments 表（id, post_id, author, body,     │
│    created_at, updated_at）                          │
│  - 添加外键约束到 posts 表                            │
│  - 创建迁移文件                                      │
│                                                     │
│  阶段 2：API 开发                                    │
│  - POST /api/posts/:id/comments  — 创建评论          │
│  - GET  /api/posts/:id/comments  — 获取评论列表       │
│  - DELETE /api/comments/:id     — 删除评论            │
│                                                     │
│  阶段 3：前端实现                                    │
│  - CommentForm 组件（作者、内容输入）                  │
│  - CommentList 组件（渲染评论列表）                    │
│  - Markdown 渲染集成（react-markdown）                │
│                                                     │
│  阶段 4：安全与验证                                   │
│  - XSS 防护（Markdown 过滤）                          │
│  - 速率限制（每个用户每分钟最多 5 条评论）              │
│  - 输入验证（作者名 ≤50 字符、内容 ≤10000 字符）       │
│                                                     │
│  风险评估：                                          │
│  - Markdown 渲染可能引入 XSS 风险                     │
│  - 大量评论可能影响查询性能，需要分页                   │
│                                                     │
│  ⚠️ 请审查此计划。输入 "approve" 继续，或提供修改意见。 │
└─────────────────────────────────────────────────────┘

你：approve

AI：开始执行阶段 1...
```

**为什么 plan 如此有效？**
- 让 AI 在花钱之前先想清楚
- 你可以在执行前纠正错误方向
- 阶段划分让长任务可管理
- 风险评估提前暴露问题

### 5.2 /tdd — 测试驱动开发

**用途**：强制测试先行的开发流程。

**工作流程（Red-Green-Refactor）：**

```
RED   阶段：先写一个会失败的测试
         ↓
GREEN 阶段：写最少的代码让测试通过
         ↓
IMPROVE 阶段：重构，保持所有测试通过
         ↓
覆盖率检查：必须 ≥ 80%
```

**实战示例**：

```
你：/tdd "实现一个 URL 验证函数"

AI（tdd-guide agent 启动）：
┌─────────────────────────────────────────────────────┐
│  📋 TDD 工作流启动                                   │
│                                                     │
│  STEP 1 (RED)：先写测试                              │
│  ─────────────────────────────────────              │
│  describe('validateUrl', () => {                     │
│    it('should validate https://example.com', () => { │
│      expect(validateUrl('https://example.com'))      │
│        .toBe(true)                                   │
│    })                                                │
│    it('should reject invalid urls', () => {          │
│      expect(validateUrl('not-a-url')).toBe(false)     │
│    })                                                │
│    it('should handle empty string', () => {          │
│      expect(validateUrl('')).toBe(false)              │
│    })                                                │
│    it('should handle null/undefined', () => {        │
│      expect(validateUrl(null)).toBe(false)            │
│      expect(validateUrl(undefined)).toBe(false)       │
│    })                                                │
│  })                                                  │
│                                                     │
│  运行测试... ❌ 全部失败（预期中的 RED）               │
│                                                     │
│  STEP 2 (GREEN)：写最少实现                           │
│  ─────────────────────────────────────              │
│  function validateUrl(url) {                         │
│    if (!url) return false                            │
│    try {                                             │
│      new URL(url)                                    │
│      return true                                     │
│    } catch {                                         │
│      return false                                    │
│    }                                                 │
│  }                                                   │
│                                                     │
│  运行测试... ✅ 全部通过                              │
│                                                     │
│  STEP 3 (IMPROVE)：检查覆盖率                        │
│  ─────────────────────────────────────              │
│  覆盖率报告: 100% ✅                                 │
└─────────────────────────────────────────────────────┘
```

**为什么 TDD 比先写实现再补测试好？**
1. **设计驱动**：先写测试迫使你思考接口设计（"这个函数应该怎么被调用？"），而不是实现细节
2. **防止过度工程**：只写让测试通过的最小代码，不会写出不需要的功能
3. **测试必然通过**：如果你先写实现再补测试，可能写出"永远通过的测试"（测试太弱），TDD 中你的测试先失败过了，证明测试有效
4. **边界情况不漏**：TDD 要求你在写实现之前就想好各种边界情况（null、空值、异常）

### 5.3 /code-review — 代码审查

**用途**：对已修改的代码进行全面审查。

**为什么 ECC 的 code-review 比普通 AI 代码审查好？**

普通 AI 代码审查的问题：
```
你：审查这段代码
AI：建议 1：把 `let` 改为 `const`（噪声）
    建议 2：加一个空行（噪声）
    建议 3：这个函数有安全漏洞！（重要）
    ... 30 条建议，重要信息被淹没
```

ECC code-review 的 **80% 置信度过滤**：
```
你：/code-review
AI：CRITICAL: SQL 注入漏洞在第 42 行（置信度 95%）
    HIGH: 缺少输入验证在第 15 行（置信度 88%）
    LOW: 建议 let→const 在第 7 行（噪声，已过滤）
    → 只报告置信度 ≥ 80% 的问题
```

**实战示例**：
```
你：/code-review

AI（code-reviewer agent 启动）：
┌─────────────────────────────────────────────────────┐
│  📋 代码审查报告                                     │
│                                                     │
│  审查文件：src/auth/login.ts                         │
│                                                     │
│  🔴 CRITICAL (2):                                   │
│  1. SQL 注入风险 - 第 42 行                          │
│     `const query = SELECT * FROM users WHERE         │
│      id = ${userId}` ← 直接拼接字符串！               │
│     修复：使用参数化查询                              │
│                                                     │
│  2. 密码明文存储 - 第 55 行                          │
│     `db.save(password)` ← 未哈希！                    │
│     修复：使用 bcrypt.hash()                         │
│                                                     │
│  🟡 HIGH (3):                                       │
│  3. 缺少速率限制 - 第 30 行                          │
│     登录接口没有限制尝试次数                          │
│                                                     │
│  4. 错误信息过多 - 第 48 行                          │
│     "用户不存在" ← 暴露了用户是否存在                │
│     修复：统一返回"用户名或密码错误"                  │
│                                                     │
│  🟢 PASS (12):                                      │
│  类型安全、代码格式、命名规范等全部通过                │
└─────────────────────────────────────────────────────┘
```

### 5.4 /verify — 验证循环

**用途**：运行完整的验证链：编译 → Lint → 测试 → 类型检查。

```bash
/verify
```

它会依次执行（根据项目类型自动检测）：
1. TypeScript 项目：`tsc --noEmit`
2. 测试：`npm test` 或 `pytest` 等
3. Lint：`eslint` 或 `ruff` 等
4. 类型：`tsc` 或 `mypy` 等

**为什么需要 /verify？**
- 人经常会忘记运行测试就提交
- 一个 /verify 触发所有检查，省去多次手动运行

### 5.5 /orchestrate — 多代理编排

**用途**：自动串联多个 agent 完成复杂工作流。

**4 种工作流模式：**

| 模式 | 用途 | 执行序列 |
|------|------|---------|
| `feature` | 新功能开发 | planner → tdd-guide → code-reviewer → security-reviewer |
| `bugfix` | Bug 修复 | tdd-guide → code-reviewer |
| `refactor` | 重构 | planner → code-reviewer |
| `security` | 安全审计 | security-reviewer |

**示例**：
```
你：/orchestrate feature "添加用户资料页面"

AI 自动执行：
  1. planner agent → 制定计划 → 你审核
  2. tdd-guide agent → 先写测试 → 实现 → 验证
  3. code-reviewer agent → 审查代码质量
  4. security-reviewer agent → 安全检查（XSS、CSRF 等）
```

### 5.6 /build-fix — 修复编译错误

**用途**：自动检测和修复编译/构建错误。

**工作原理**：
1. 运行构建命令，捕获错误输出
2. 分析错误类型（语法错误、类型错误、依赖缺失、配置错误）
3. 自动委派给正确的 build-resolver agent
4. 修复后重新构建验证

**示例**：
```
你：/build-fix

AI（build-error-resolver agent）：
发现 3 个构建错误：
1. src/app.ts:42 - 类型 'string | undefined' 不能赋值给 'string'
   → 修复：添加空值检查
2. tsconfig.json - 未开启 strict mode
   → 修复：启用 strict: true
3. package.json - 缺少依赖 @types/express
   → 修复：npm install @types/express --save-dev
```

### 5.7 /refactor-clean — 清理死代码

**用途**：检测并清理项目中的死代码、未使用文件、冗余代码。

**扫描项**：
- 未使用的变量、函数、导入
- 未引用的文件
- 重复的代码块
- 多余的注释
- 孤立的 .md 文件

**为什么需要它？**
经过长期开发，仓库里会有大量"遗物"——测试过的老函数、被替换的工具函数、不再引用的组件。手动清理很费时，AI 最适合做这种模式识别工作。

### 5.8 快速决策指南

```
开始新功能？          → /plan 先，然后 /tdd
刚写完代码？          → /code-review
编译失败？            → /build-fix
准备提交？            → /verify 然后 /code-review
会话要结束了？        → /learn 或 /save-session
第二天继续？          → /resume-session
上下文太重了？        → /compact 然后 /checkpoint
想记住工作模式？      → /learn → /evolve
运行重复任务？        → /loop-start
```

---

## 第 6 章 Agents 代理详解

### 6.1 Agent 概览

ECC 提供 47+ 个 agent，每个 agent 是特定领域的"专家"。

| Agent | 角色 | 用途 | 使用方式 |
|-------|------|------|---------|
| planner | 规划者 | 制定实施计划 | `/plan` 或 `@planner` |
| architect | 架构师 | 系统设计决策 | `/plan` + architect 或 `@architect` |
| code-reviewer | 代码审查员 | 质量/安全审查 | `/code-review` 或 `@code-reviewer` |
| security-reviewer | 安全专家 | OWASP 扫描 | `/security-scan` 或 `@security-reviewer` |
| tdd-guide | TDD 专家 | 测试先行 | `/tdd` 或 `@tdd-guide` |
| build-error-resolver | 构建修复师 | 修复编译错误 | `/build-fix` |
| e2e-runner | E2E 测试员 | Playwright 测试 | `/e2e` |
| refactor-cleaner | 重构清理师 | 死代码清理 | `/refactor-clean` |
| doc-updater | 文档更新员 | 更新文档/代码映射 | `/update-docs` |
| loop-operator | 循环操作员 | 安全运行循环任务 | `/loop-start` |
| database-reviewer | 数据库专家 | Schema/查询优化 | 自动委派 |
| harness-optimizer | 优化师 | 配置调优 | `/harness-audit` |

### 6.2 Agent 的权限设计哲学

每个 agent 的权限遵循**最小权限原则**：

- **planner**：只有 Read、Glob、Grep（只能读，不能写）
- **code-reviewer**：Read + 有限的 Bash（git diff/git log 允许，其他需要询问）
- **tdd-guide**：Read + Write + Edit + Bash（需要完整权限来写测试和代码）
- **security-reviewer**：Read + Glog + Grep（只需要读代码来发现漏洞）

**为什么 planner 不允许写文件？**
如果 planner 可以直接写文件，它可能会跳过"等待审核"的步骤直接开始编码。"写计划但不执行"是刻意设计的工作流控制。

### 6.3 如何调用 Agent

**方法 1：通过命令隐式调用**
```
/plan "功能"      → 自动调用 planner
/tdd "功能"       → 自动调用 tdd-guide
/code-review      → 自动调用 code-reviewer
```

**方法 2：通过 @ 显式调用（OpenCode）**
```
@planner 请为支付模块设计实施计划
@code-reviewer 请审查 src/payment/services.ts
```

**方法 3：在对话中让 AI 自动判断**
```
"我想给博客添加评论功能，需要先做个计划"
→ AI 根据上下文自动决定是否调用 planner agent
```

---

## 第 7 章 Skills 技能详解

### 7.1 应该安装哪些 Skills

**不要全装！** 装太多没用的 skill 会占用上下文窗口。按你的技术栈选择性安装：

**基础技能（所有人都应该装）：**

| Skill | 用途 | 文件 |
|-------|------|------|
| `coding-standards` | 编码规范 | 适用于所有语言 |
| `tdd-workflow` | TDD 工作流 | 测试先行方法论 |
| `verification-loop` | 验证循环 | 编译→lint→测试→类型检查 |
| `search-first` | 搜索优先 | 写代码前先搜索现有方案 |
| `strategic-compact` | 上下文压缩 | 优化上下文使用 |

**前端/TypeScript 用户：**
| Skill | 用途 |
|-------|------|
| `frontend-patterns` | React/Next.js 模式 |
| `frontend-ui-ux` | UI/UX 设计原则 |
| `e2e-testing` | Playwright 端到端测试 |
| `api-design` | API 设计模式 |

**Python 用户：**
| Skill | 用途 |
|-------|------|
| `python-patterns` | Python 最佳实践 |
| `python-testing` | pytest 模式 |
| `django-patterns` | Django 模式 |
| `django-tdd` | Django TDD |

**Java/Spring Boot 用户：**
| Skill | 用途 |
|-------|------|
| `java-coding-standards` | Java 编码规范 |
| `springboot-patterns` | Spring Boot 模式 |
| `springboot-tdd` | Spring Boot TDD |
| `jpa-patterns` | JPA 模式 |

### 7.2 Skill 的激活机制

Skill 有两种激活方式：

**自动激活**（推荐）：
```
你：用 TDD 方式实现一个用户注册功能
AI 读取 tdd-workflow SKILL.md → 按照步骤执行
```

**手动激活**：
```
你：/tdd "实现用户注册功能"
→ 等价于触发 tdd-workflow skill
```

AI 是怎么知道该激活哪个 skill 的？
- 每个 skill 的 `description` 字段包含了触发条件（"当用户提到测试时"、"当用户需要安全审查时"）
- 启动时 AI 只加载所有 skill 的 name 和 description（约 100 tokens/个）
- AI 根据你的对话内容判断哪个 skill 相关，然后才加载完整的 SKILL.md 内容

### 7.3 Skill 内容示例（部分）

查看 `skills/tdd-workflow/SKILL.md` 的实际内容（截取）：

```markdown
## Edge Cases You MUST Test

1. **Null/Undefined** input
2. **Empty** arrays/strings
3. **Invalid types** passed
4. **Boundary values** (min/max)
5. **Error paths** (network failures, DB errors)
6. **Race conditions** (concurrent operations)
7. **Large data** (performance with 10k+ items)
8. **Special characters** (Unicode, emojis, SQL chars)
```

为什么这些在 Skill 中而不是在 Rules 中？因为这是"怎么做"而非"必须做"——Rules 只说"覆盖率 ≥80%"，Skills 说"具体怎么测试这些边界情况"。

---

## 第 8 章 Hooks 钩子系统

### 8.1 Hook 类型与触发时机

| Hook 类型 | 触发时机 | 典型用途 |
|-----------|---------|---------|
| PreToolUse | 工具执行之前 | 验证输入、阻止危险操作 |
| PostToolUse | 工具执行之后 | 格式化代码、类型检查 |
| UserPromptSubmit | 你发送消息时 | 检查包含敏感信息 |
| Stop | AI 回复完成时 | 检查修改过的文件 |
| PreCompact | 上下文压缩前 | 保存关键状态 |
| Notification | 权限请求时 | 长时间运行任务通知 |

### 8.2 在 Claude Code 中配置 Hooks

在 `~/.claude/settings.json` 中配置：
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "npm|pnpm|yarn|cargo|pip|pip3",
        "hooks": ["tmux-reminder"]
      },
      {
        "matcher": "Write$",
        "hooks": ["block-readme-only"]
      },
      {
        "matcher": "git push",
        "hooks": ["open-editor-review"]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit$ && .*\\.ts$|.*\\.tsx$",
        "hooks": ["typescript-check"]
      },
      {
        "matcher": "Edit$ && .*\\.ts$|.*\\.tsx$|.*\\.js$|.*\\.jsx$",
        "hooks": ["prettier-format"]
      },
      {
        "matcher": "Edit$",
        "hooks": ["check-console-log"]
      }
    ],
    "Stop": [
      {
        "matcher": "*",
        "hooks": ["check-modified-files"]
      }
    ]
  }
}
```

**关键概念解释：**

- **matcher**：正则表达式，匹配要拦截的工具调用
- **hooks**：钩子名数组，对应 `~/.claude/hooks/` 下的脚本

**每条配置的目的是什么：**

```json
{
  "matcher": "npm|pnpm|yarn|cargo|pip|pip3",
  "hooks": ["tmux-reminder"]
}
```
- npm install 可能需要几分钟，放在 tmux 中运行可以避免阻塞当前会话
- 所以检测到这些命令时，提醒用户用 tmux 运行

```json
{
  "matcher": "Edit$ && .*\\.ts$|.*\\.tsx$",
  "hooks": ["typescript-check"]
}
```
- 每次编辑 TypeScript 文件后自动运行 `tsc --noEmit`
- 因为 TypeScript 的类型错误如果不及时修复，会越积越多
- 立即发现立即修复，而不是等到最后一起修

```json
{
  "matcher": "Edit$",
  "hooks": ["check-console-log"]
}
```
- 每次编辑后检查是否添加了 `console.log`
- 因为 debug 时加的 log 很容易忘记删除，提交到生产环境

### 8.3 在 OpenCode 中配置 Hook 事件

OpenCode 使用插件系统实现钩子：

```typescript
// .opencode/plugins/ecc-hooks.ts
export const hooks = {
  "tool.execute.before": [
    {
      matcher: /npm|pnpm|yarn/,
      handler: (ctx) => {
        console.log("长时间运行命令，建议 tmux")
      }
    }
  ],
  "file.edited": [
    {
      matcher: /\.ts$/,
      handler: (ctx) => {
        // 自动运行 tsc
      }
    }
  ],
  "session.idle": [
    {
      handler: (ctx) => {
        // 检查修改的文件
      }
    }
  ]
}
```

### 8.4 使用 hookify 插件创建 Hook

如果你不想手写 JSON，可以使用 `hookify` 插件通过对话创建 hooks：

```
/hookify "创建一个钩子，每次我编辑 TypeScript 文件后自动运行 tsc"
→ hookify 自动生成对应的 hooks JSON
```

---

## 第 9 章 Continuous Learning（持续学习）

### 9.1 什么是持续学习

ECC 的持续学习系统 v2 是一个"本能"系统——它观察你在会话中的行为，记录模式，并随着时间推移提升准确度。

**工作原理：**

```
会话 1：你用了 pnpm install 而不是 npm install
        → 系统记录："用户偏好 pnpm（置信度 30%）"

会话 2：你又用了 pnpm install
        → 置信度提升到 55%

会话 5：你 5 次都用 pnpm
        → 置信度 85%，固化为本能
        → 以后 AI 自动用 pnpm 而不是 npm
```

### 9.2 使用命令

```bash
/learn                  # 从当前会话提取模式
/learn-eval            # 提取模式 + 自我评估质量
/instinct-status       # 查看所有已学习的本能（含置信度）
/instinct-export       # 导出本能到文件
/instinct-import       # 从文件导入本能
/evolve                # 分析本能，建议进化技能结构
/promote               # 将项目级本能提升为全局本能
/prune                 # 删除低置信度或过时的本能
```

### 9.3 实战场景

```
你完成了支付模块的开发，会话要结束了：

/learn-eval
→ AI 提取本次会话中发现的模式：
   - 你喜欢用 `@nestjs/config` 管理配置（置信度 85%）
   - 你习惯用 `class-validator` + `class-transformer` 做 DTO 验证（置信度 90%）
   - 你倾向用 `Repository` 模式而不是 ActiveRecord（置信度 75%）

→ 询问你是否保存这些模式

你：保存

→ 下次开发新模块时，AI 自动使用这些模式
```

---

## 第 10 章 AgentShield 安全扫描

### 10.1 什么是 AgentShield

AgentShield 是 ECC 生态中的安全审计工具，专门扫描 AI Agent 配置文件（CLAUDE.md、.cursorrules、settings.json 等）。

### 10.2 三阶段流水线

```
                ┌─────────────┐
                │  CLAUDE.md   │
                │  settings   │
                │  agents.json│
                └──────┬──────┘
                       ▼
         ┌─────────────────────────┐
         │  Phase 1: 红队 (Red)     │
         │  构造对抗性提示          │
         │  测试提示注入漏洞        │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │  Phase 2: 蓝队 (Blue)    │
         │  验证安全边界            │
         │  检查权限范围            │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │  Phase 3: 审计 (Auditor) │
         │  生成结构化报告          │
         │  给出修复建议            │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │  安全评分 + 修复方案     │
         └─────────────────────────┘
```

**为什么需要三阶段？**
- **红队**：主动攻击，发现你自己意识不到的漏洞
- **蓝队**：验证防御措施是否真的有效
- **审计**：把发现的问题组织成可操作的报告

### 10.3 安装和使用

```bash
# 安装
npm install -g ecc-agentshield

# 扫描配置文件
npx ecc-agentshield scan ./CLAUDE.md
npx ecc-agentshield scan ./.claude/settings.json
npx ecc-agentshield scan ./.cursorrules

# 扫描目录
npx ecc-agentshield scan ./config/

# 输出报告
npx ecc-agentshield scan ./CLAUDE.md --output report.json
```

### 10.4 输出示例

```
$ npx ecc-agentshield scan ./CLAUDE.md

AgentShield CLI — AI Agent Config Security Auditor
Powered by Opus 4.6 red-team / blue-team / auditor pipeline

Scanning: CLAUDE.md (2,847 tokens)

🔴 CRITICAL (1):
  1. Unrestricted file system access via Bash tool
     → 限制：只允许在项目目录内操作文件

🟡 WARNING (2):
  1. No rate limiting on external API calls
     → 建议：添加速率限制规则
  2. Missing secret detection guardrail
     → 建议：添加密钥泄露检测

🟢 PASS (3):
  1. Tool permissions properly scoped
  2. Destructive action confirmation required
  3. No prompt injection vectors detected

Security Score: 72/100 — 1 critical, 2 warnings, 3 passed
Full report saved to ./agentshield-report.json
```

---

## 第 11 章 完整工作流实战

### 11.1 场景：开发一个用户认证系统

**场景说明**：为一个 Express.js + TypeScript + PostgreSQL 项目添加 JWT 用户认证。

**完整工作流：**

```
Step 1: /plan "实现 JWT 用户认证系统"
  → planner agent 分析需求
  → 输出实施计划（4 个阶段、风险分析）
  → 你审核并批准

Step 2: 批量实现阶段 1（数据库）
  AI 自动加载 backend-patterns skill
  学习 postgres-patterns skill
  → 创建 users 表迁移
  → 创建 User 实体/类型

Step 3: /tdd "实现注册 API"
  → tdd-guide agent 启动
  → RED：写注册接口测试
  → GREEN：实现注册逻辑（密码加密、验证）
  → IMPROVE：重构、验证覆盖率

Step 4: /tdd "实现登录 API"
  → 同上流程，添加 JWT token 生成

Step 5: /tdd "实现 JWT 中间件"
  → 测试 token 验证、过期处理、刷新

Step 6: /code-review
  → code-reviewer agent 审查全部修改
  → 发现：密码重置接口缺少速率限制
  → 发现：JWT secret 硬编码在代码中
  → 修复这两个问题

Step 7: /security-scan
  → security-reviewer agent 扫描
  → 检查：OWASP Top 10
  → 全部通过 ✅

Step 8: /verify
  → tsc --noEmit ✅
  → npm test ✅
  → lint ✅

Step 9: /learn-eval
  → 提取本项目的认证模式
  → 保存以备将来参考
```

### 11.2 场景：修复生产环境 Bug

```
Step 1: /tdd "修复订单状态显示错误"
  → tdd-guide agent 启动
  → RED：写一个重现 bug 的测试
  → GREEN：修复 bug
  → IMPROVE：添加回归测试

Step 2: /code-review
  → code-reviewer 确认修复方案无副作用

Step 3: /verify
  → 全部验证通过
```

### 11.3 场景：重构旧代码

```
Step 1: /plan "将 Express 路由重构为 NestJS 控制器"
  → planner 分析现有代码
  → 制定分阶段迁移计划

Step 2: 按阶段迁移（每阶段后运行 /verify）
  → /tdd "将 users 路由迁移为 UsersController"

Step 3: /code-review
  → 确认重构未引入新问题

Step 4: /refactor-clean
  → 删除旧的 users.ts 路由文件
  → 更新 import 引用
```

---

## 第 12 章 性能与上下文优化

### 12.1 为什么上下文管理如此重要

每个 MCP 连接、每个规则文件、每个 skill 都占用上下文窗口：

```
┌─────────────────────────────────────────────┐
│           200K tokens 上下文窗口              │
├─────────────────────────────────────────────┤
│  系统提示         5K                         │
│  AGENTS.md        3K                         │
│  Rules            10K                        │
│  Skills（已激活）  15K                        │
│  MCP 连接         20K                        │
│  对话历史         100K                        │
│  剩余可用          47K ← 可用太少会影响推理质量 │
└─────────────────────────────────────────────┘
```

### 12.2 优化原则

**原则 1：只装你需要的 skills**
- 不要 cp -r skills/* 全装
- 只装你的技术栈相关的
- TypeScript 开发者不需要装 django-patterns

**原则 2：保持 MCP 在 10 个以下**
- 配置 20-30 个 MCP 备份，但只启用不到 10 个
- 当前项目不需要的 MCP 禁用

**原则 3：用 /compact 手动压缩**
```
/compact
```
手动触发上下文压缩，删除最旧的不相关对话历史。

### 12.3 使用 /checkpoint 保存状态

```
/checkpoint "认证模块开发完成，准备开始支付模块"
```
保存当前状态，即使之后需要回滚，也能回到这个检查点。

---

## 第 13 章 常见问题排查

### 13.1 命令不工作

```bash
# 如果安装后命令没出现
/plugin list ecc@ecc              # 检查插件是否启用

# 如果插件已安装但命令无效
node scripts/ecc.js doctor        # 诊断问题
node scripts/ecc.js repair        # 修复

# 检查 settings.json
cat ~/.claude/settings.json       # 确认插件在 enabledPlugins 中
```

### 13.2 Skills 不被 AI 加载

```
检查项 1：SKILL.md 文件名是否大写 S
  ✅ skills/tdd-workflow/SKILL.md
  ❌ skills/tdd-workflow/skill.md

检查项 2：frontmatter 是否完整
  ✅ 包含 name 和 description
  ❌ 缺少其中一个

检查项 3：文件夹名是否 = name 字段
  ✅ 文件夹 tdd-workflow，name: tdd-workflow
  ❌ 不一致

检查项 4：权限是否 deny
  在 opencode.json 中检查 permission.skill 设置
```

### 13.3 如何卸载 ECC

```bash
# 预览要删除的内容
node scripts/uninstall.js --dry-run

# 执行卸载
node scripts/uninstall.js

# 如果是插件安装
/plugin remove ecc@ecc
# 然后手动删除 rules
rm -rf ~/.claude/rules/ecc
```

### 13.4 安装后感觉重复/冲突

```
症状：命令出两次、skill 重复加载
原因：同时用了插件安装和手动安装

解决方案：
1. 卸载插件或删除手动安装的文件
2. 只保留一种安装方式
3. node scripts/ecc.js repair
```

### 13.5 OpenCode 中 skill 不显示

```
1. 检查 SKILL.md 是否在正确位置
   .opencode/skills/<skill-name>/SKILL.md

2. 检查 opencode.json 的 permission.skill 配置
   "internal-*": "deny"  →  internal- 开头的 skill 被隐藏

3. 检查 skill 名是否唯一
   不能有同名的 skill 在不同目录中

4. 运行 opencode 时查看启动输出
   是否有 skill loading 相关的错误信息
```

---

## 附录 A：快速参考卡

### A.1 最常用命令速查

| 场景 | 命令 |
|------|------|
| 开始新功能 | `/plan "功能描述"` → 审核 → `/tdd` |
| 写代码 | 直接描述需求，AI 自动执行 |
| 审查代码 | `/code-review` |
| 修复编译 | `/build-fix` |
| 验证 | `/verify` |
| 安全检查 | `/security-scan` |
| 清理死代码 | `/refactor-clean` |
| 保存模式 | `/learn-eval` |
| 管理上下文 | `/compact` → `/checkpoint "备注"` |

### A.2 Skill 选择速查

| 你的技术栈 | 需要安装的 Skills |
|-----------|------------------|
| TypeScript + React | coding-standards, tdd-workflow, frontend-patterns, api-design, e2e-testing |
| Python + Django | coding-standards, tdd-workflow, python-patterns, django-patterns, django-tdd |
| Java + Spring Boot | coding-standards, tdd-workflow, java-coding-standards, springboot-patterns, jpa-patterns |
| Go | coding-standards, tdd-workflow, golang-patterns, golang-testing |
| 前端 + 后端全栈 | 以上 TypeScript 全部 + backend-patterns, postgres-patterns |

### A.3 快捷键速查

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+U` | 删除整行 |
| `!` | 执行 shell 命令 |
| `@` | 搜索文件（OpenCode） |
| `/` | 斜杠命令 |
| `Shift+Enter` | 多行输入 |
| `Tab` | 切换思维链显示 |
| `Esc Esc` | 中断 AI 回复 |

---

*本教程基于 ECC v1.10.0+，覆盖 Claude Code 和 OpenCode 两大平台。*
*仓库地址：https://github.com/affaan-m/ECC*
*官方网站：https://ecc.tools*
