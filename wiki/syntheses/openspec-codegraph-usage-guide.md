---
title: "OpenSpec 和 CodeGraph 完整使用指南"
type: synthesis
tags: [OpenSpec, CodeGraph, 使用指南, 实操手册, 棕地项目, MCP, delta-spec]
sources:
  - wiki/entities/OpenSpec.md
  - wiki/entities/CodeGraph.md
  - wiki/concepts/delta-spec.md
  - wiki/syntheses/openspec-brownfield-usage-guide.md
  - wiki/syntheses/openspec-bugfix-workflow.md
  - wiki/syntheses/openspec-archive-modify-and-token-tradeoff.md
  - wiki/sources/摘要-codegraph-deep-dive.md
  - wiki/sources/摘要-codegraph-mcp-gateway.md
  - wiki/sources/摘要-OpenSpec规范驱动AI编程框架.md
last_updated: 2026-08-28
---

# OpenSpec 和 CodeGraph 完整使用指南

> **定位**：[[OpenSpec]] 管"想清楚再动手"（规划+存档），[[CodeGraph]] 管"动手前知道影响面"（影响分析）。本文是两个工具的完整实操手册，配合 [[optimal-framework-combination-heavy-project]] 使用。

## 第一部分：OpenSpec 使用方法

### 1. 安装与初始化

```bash
# 安装中文版（原版英文：npm install -g @fission-ai/openspec@latest）
npm install -g @studyzy/openspec-cn@latest

# 进入你的已有项目
cd /your-existing-project

# 初始化（--tools 指定你用的 AI 工具）
openspec-cn init --tools claude          # 单个工具
openspec-cn init --tools claude,cursor   # 多个工具
openspec-cn init --tools all             # 全部 31 个工具

# 查看仪表盘
openspec-cn view
```

**支持的 31 个工具 ID**：`claude` `cursor` `codex` `gemini` `opencode` `kimi` `qwen` `qoder` `windsurf` `github-copilot` 等。

初始化后项目根目录出现 `opsx/` 工作区：

```
opsx/
├── archive/          # 已完成的变更归档（AI 的"记忆库"）
├── specs/            # 当前生效的需求规格
├── changes/          # 进行中的变更
└── openspec.config.json
```

### 2. 四个核心命令（完整生命周期）

#### 命令 1：`/opsx:explore` — 探索需求（纯对话，不写代码）

```
/opsx:explore 我想给系统加日志收集功能，集团要求收集4种日志...
```

AI 通过对话帮你理清：
- 为什么要做（业务背景）
- 谁来用（角色）
- 边界在哪（哪些不做）
- 有什么风险

**产物**：纯对话，不生成文件。目的是"先想清楚再动手"。

#### 命令 2：`/opsx:propose` — 生成规划工件

```
/opsx:propose 实现日志收集系统：4种日志分别采用不同采集策略
```

AI 自动生成四份文档，放在 `opsx/changes/<变更名>/` 下：

| 文件 | 内容 | 校验规则 |
|------|------|---------|
| `proposal.md` | 为什么改 + 改什么 | `## Why` 不能少于 50 字符 |
| `specs/spec.md` | 具体需求，用 SHALL/MUST + Given/When/Then | 每个 Requirement 必须含 SHALL 或 MUST，至少一个 Scenario 块 |
| `design.md` | 技术方案（用什么库、改哪些类、数据流） | - |
| `tasks.md` | 可执行步骤清单 | - |

**工件依赖链**：`proposal → specs → design → tasks → implement`。依赖关系是"使能"而非"卡死"——随时可回去改前面的工件。

#### 命令 3：`/opsx:apply` — 按清单实现

```
/opsx:apply
```

AI 按 `tasks.md` 逐项实现：
- 每完成一项，更新 tasks.md 进度（`[x]`）
- 生成实际代码 + 测试
- 中途发现 design 有问题，可以回去改 design.md 再继续

#### 命令 4：`/opsx:archive` — 归档

```
/opsx:archive
```

把整个 `opsx/changes/<变更名>/` 移入 `opsx/archive/`。**这是对抗 AI 遗忘的核心**——所有历史决策永久存档，将来任何新会话都能回溯。

### 3. 棕地项目首次补录（关键步骤）

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
  （原来是仅密码登录）

## REMOVED
- 无
```

**核心原则**：不动已有 spec，只描述差异。通过 `/opsx:sync` 将 delta 合并回主 spec。

### 4. 归档后需求变更的流程

根据 [[openspec-archive-modify-and-token-tradeoff]]，**不要直接手改 archive 目录中的归档文档**。标准流程：

```
/opsx:explore   → 理清改什么、为什么改
/opsx:propose   → 生成 delta spec（ADDED/MODIFIED/REMOVED 三标记，只写差异）
人工确认         → 审阅 delta 提案（关键检查点，别跳）
/opsx:apply     → 按 tasks.md 改代码
/opsx:sync      → 把 delta 合并回主 spec（让 OpenSpec "知道"这次修改）
/opsx:archive   → 归档本次变更，形成新基线
```

**`/opsx:sync` 是关键**——没有这一步，OpenSpec 永远不知道你改了什么。

### 5. apply 后发现 bug 的修复流程

根据 [[openspec-bugfix-workflow]]，先判断 bug 性质：

```
验证发现 bug
    │
    ├─ spec 是对的，只是代码写错 → 直接让 AI 改代码（不必动 OpenSpec）
    │
    └─ spec 本身有问题
         │
         ├─ 还没 archive → 回去改 specs/spec.md 和 design.md，再 /opsx:apply
         │
         └─ 已经 archive → /opsx:explore → /opsx:propose（生成 delta）
                           → 人工确认 → /opsx:apply → /opsx:sync → /opsx:archive
```

### 6. 重要注意事项

- **OpenSpec 的 spec 是静态文档，不会自动扫描代码变更**。小改动绕过流程直接改代码，spec 和实际代码会脱节（spec rot）
- **`/opsx:explore` 不会自动扫描代码**对比 spec 和实际实现的差异。需要你主动在对话中要求 AI 对比
- **定期对齐**：大改动前在 explore 中主动要求 AI 做差异核对，把积累的脱节一次性补录

### 7. 项目目录最终结构

```
your-existing-project/
├── src/                          # 你的源码
├── opsx/                         # OpenSpec 工作区
│   ├── archive/                  # 历史变更归档（AI 的长期记忆）
│   │   ├── add-user-avatar/
│   │   │   ├── proposal.md       # 当时为什么加这个功能
│   │   │   ├── specs/spec.md     # 具体需求 + 验收场景
│   │   │   ├── design.md         # 技术决策（为什么用 Redis 存验证码）
│   │   │   └── tasks.md          # 最终任务清单
│   │   ├── export-order-excel/
│   │   └── ...
│   ├── specs/                    # 当前生效的主规格
│   │   ├── auth/spec.md
│   │   ├── order/spec.md
│   │   └── ...
│   ├── changes/                  # 进行中的变更
│   │   └── refactor-payment/
│   │       ├── proposal.md
│   │       ├── specs/delta.md    # Delta Spec：只写差异
│   │       ├── design.md
│   │       └── tasks.md
│   └── openspec.config.json      # 配置文件
├── CLAUDE.md                     # Claude Code 指令文件
└── ...
```

## 第二部分：CodeGraph 使用方法

### 1. 安装

三种方式任选：

```bash
# 方式 1：一键安装脚本（自带运行时，无需 Node.js）
# 从 GitHub releases 下载对应平台的安装脚本

# 方式 2：npm 全局安装
npm install -g @colbymchenry/codegraph

# 方式 3：交互式安装器（自动检测已装 AI 代理并配置 MCP）
codegraph install --yes
```

### 2. 初始化项目索引

```bash
# 交互式初始化（创建 .codegraph/ 目录）
codegraph init -i

# 强制重建索引
codegraph index --force

# 增量更新索引（代码改了后同步）
codegraph sync

# 查看索引统计信息
codegraph status
```

初始化后，CodeGraph 会：
- 用 tree-sitter 解析你的源码（支持 Java 等多语言）
- 提取节点（函数/类/方法/接口/路由/组件）
- 提取边（调用/导入/继承/引用/路由绑定）
- 存入本地 SQLite 数据库 + FTS5 全文检索
- **纯本地运行，代码不上传第三方服务器**

### 3. 核心命令（命令行直接使用）

#### 命令 1：`codegraph query` — 按名称搜索符号

```bash
codegraph query LoginController
```

找到项目中所有名为 LoginController 的符号及其位置。

#### 命令 2：`codegraph callers` — 查找谁调用了某函数

```bash
codegraph callers UserService.getUserInfo
```

**用途**：改函数签名前，先看谁在用这个函数，避免改完一堆地方报错。

#### 命令 3：`codegraph callees` — 查找某函数调用了谁

```bash
codegraph callees OrderService.createOrder
```

**用途**：了解一个函数的依赖范围，判断改动是否会波及外部系统。

#### 命令 4：`codegraph impact` — 变更影响分析（核心命令）

```bash
# 分析改这个符号会影响哪些代码，深度2层调用链
codegraph impact LoginController.login --depth 2

# 分析改权限拦截器的影响面
codegraph impact PermissionInterceptor.check --depth 2
```

**这是防遗漏的核心命令**——在改代码前就知道影响面，而不是改完才发现要重构。

#### 命令 5：`codegraph trace` — 追踪两个符号间完整调用路径

```bash
codegraph trace Controller.handleRequest Service.executeQuery
```

**用途**：理解一次请求从入口到数据库的完整调用链路。

#### 命令 6：`codegraph affected` — 查找受改动影响的测试文件

```bash
codegraph affected
```

**用途**：改完代码后，知道哪些测试文件需要跑一遍验证。

#### 命令 7：`codegraph uninit` — 从项目中移除 CodeGraph

```bash
codegraph uninit
```

### 4. 通过 MCP 接入 AI 工具（推荐方式）

启动 MCP 服务器，让 AI 直接查图分析，不用你手动复制结果：

```bash
# 启动 MCP 服务器
codegraph serve --mcp
```

**10 个 MCP 工具**（AI 可自动调用）：

| MCP 工具 | 作用 |
|---------|------|
| `codegraph_context` | 一次获取入口点、相关符号和代码片段 |
| `codegraph_trace` | 追踪两个符号间完整调用路径 |
| `codegraph_search` | 按名称搜索符号 |
| `codegraph_callers` | 找出函数调用方 |
| `codegraph_callees` | 找出函数调用依赖 |
| `codegraph_impact` | 分析修改影响范围 |

**配置方式**：`codegraph install --yes` 会自动检测已装的 AI 代理（Claude Code/Cursor/Codex CLI/opencode/Hermes Agent）并配置 MCP。

### 5. 多项目统一 MCP 网关（企业级方案）

根据 [[摘要-codegraph-mcp-gateway]]，如果有多个项目需要访问：

```bash
# 使用 Docker 部署多项目统一网关
# 项目地址：https://github.com/dora-wang-x/codegraph-mcp-gateway

# .env 配置
HOST_PROJECTS_PATH=/path/to/projects
HOST_PORT=8000

# 访问方式
http://远程机器:8000/project-a/mcp
http://远程机器:8000/project-b/mcp
```

一个容器一个端口访问多个代码仓库，解决多项目切换时端口管理混乱的问题。

### 6. 性能数据

根据 [[摘要-codegraph-deep-dive]]，官方测试（7 个真实代码库）：
- 工具调用减少 71%
- Token 消耗降低 57%
- 任务执行速度提升 46%
- 综合成本降低 35%

### 7. 自动增量同步

CodeGraph 有文件监听器，自动检测代码变化并增量更新索引。如果发现索引没更新，手动跑 `codegraph sync`。

## 第三部分：两个工具配合使用的完整工作流

以日志收集需求为例：

```
集团下发日志收集需求
    │
    ├─ 1. /opsx:explore                    # OpenSpec：探索4种日志怎么落地
    │      → AI 分析你项目现状，给出方案选项
    │
    ├─ 2. /opsx:propose                    # OpenSpec：生成规划工件
    │      → proposal.md / spec.md / design.md / tasks.md
    │
    ├─ 3. codegraph impact <符号>          # CodeGraph：分析改现有代码的影响面
    │      codegraph callers <函数名>       #   看谁调用了你要改的方法
    │      codegraph trace <A> <B>         #   追踪调用链路
    │
    ├─ 4. 【人工确认】                      # 审查 spec + design + 影响分析
    │      → 不通过就改，通过才推进
    │
    ├─ 5. /opsx:apply                      # OpenSpec：按 tasks.md 逐项实现
    │
    └─ 6. /opsx:archive                    # OpenSpec：归档
         → 同事打开 design.md 就能看懂决策原因
```

### 日常维护

- **代码改了**：`codegraph sync` 更新索引
- **需求又变了**：走 OpenSpec 的 delta spec 流程（explore → propose → apply → sync → archive）
- **apply 后发现 bug**：判断是代码 bug 还是 spec bug，按 [[openspec-bugfix-workflow]] 的决策树处理
- **定期对齐**：大改动前在 explore 中主动要求 AI 对比 spec 和代码差异

## 关联连接

- [[OpenSpec]] - 规划引擎
- [[CodeGraph]] - 变更影响分析
- [[delta-spec]] - 增量变更机制
- [[openspec-brownfield-usage-guide]] - 棕地项目完整使用方案
- [[openspec-bugfix-workflow]] - apply 后发现 bug 的修复流程
- [[openspec-archive-modify-and-token-tradeoff]] - 归档后修改流程与 token 权衡
- [[optimal-framework-combination-heavy-project]] - 最优框架组合（本文是其配套实操手册）
- [[摘要-codegraph-deep-dive]] - CodeGraph 深度解析来源
- [[摘要-codegraph-mcp-gateway]] - CodeGraph 多项目网关方案
- [[摘要-OpenSpec规范驱动AI编程框架]] - OpenSpec 来源
- [[MCP]] - CodeGraph 接入协议
- [[TreeSitter]] - CodeGraph 底层解析引擎
- [[ClaudeCode]] - 承载平台
