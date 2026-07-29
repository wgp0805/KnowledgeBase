---
title: "棕地项目 OpenSpec 详细使用方案"
type: synthesis
tags: [OpenSpec, 棕地项目, AI编程, 规范驱动, AI遗忘, 实操指南]
sources:
  - raw/09-archive/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/09-archive/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
  - raw/09-archive/Claude Code 最佳实践（最新版）.md
last_updated: 2026-07-29
---

# 棕地项目 OpenSpec 详细使用方案

> **核心问题**：[[OpenSpec]] 明确为棕地项目而设计（built for brownfield），但如何在已有代码库的项目中落地？如何用它解决"AI 随时间推移遗忘原始决策"的问题？

## 一、安装与初始化

```bash
# 1. 安装中文版（原版英文：npm install -g @fission-ai/openspec@latest）
npm install -g @studyzy/openspec-cn@latest

# 2. 进入你的已有项目
cd /your-existing-project

# 3. 初始化（--tools 指定你用的 AI 工具）
openspec-cn init --tools opencode      # 或 claude-code / cursor / codex

# 4. 查看仪表盘
openspec-cn view
```

初始化后项目根目录会出现 `opsx/` 工作区，这是 OpenSpec 的所有规划文档存放地。[[OpenSpec#安装与初始化]]

## 二、棕地项目首次补录（关键步骤）

已有项目最大的问题是"历史决策无文档"。OpenSpec 不要求你一次性补全所有，**用 [[delta-spec|Delta Spec]] 增量补录**即可。

### 补录策略：从最近要改的模块开始

不要试图一次性为整个项目写 spec。按需补录：

```
opsx/
├── archive/                    # 已完成的变更归档（AI 的"记忆库"）
├── specs/                      # 当前生效的需求规格
│   ├── auth/                   # 认证模块 spec
│   │   └── spec.md
│   ├── order/                  # 订单模块 spec
│   │   └── spec.md
│   └── ...
├── changes/                    # 进行中的变更
│   └── add-user-avatar/
│       ├── proposal.md
│       ├── specs/
│       │   └── delta.md        # 增量描述：只写差异
│       ├── design.md
│       └── tasks.md
└── ...
```

### 补录已有模块的写法（Delta Spec）

比如你的项目已有"认证模块"，现在要加"手机号验证码登录"功能，delta.md 只写差异：

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

核心原则：**不动已有 spec，只描述差异**。通过 `/opsx:sync` 将 delta 合并回主 spec。[[OpenSpec#Delta Spec 增量变更]]

## 三、日常开发完整工作流（每次新功能）

这是最常用的循环。每个功能按四步走：

### 步骤 1：探索需求 `/opsx:explore`

```
你在 Claude Code / OpenCode 里输入：
/opsx:explore 我想给订单模块加一个"批量导出 Excel"功能
```

AI 会通过对话帮你理清：
- 为什么要做（业务背景）
- 谁来用（角色）
- 边界在哪（哪些不做）
- 有什么风险

**这步产物**：纯对话，不生成文件。目的是"先想清楚再动手"。

### 步骤 2：生成规划工件 `/opsx:propose`

```
/opsx:propose 批量导出订单为 Excel
```

AI 自动生成四份文档，放在 `opsx/changes/export-order-excel/` 下：

| 文件 | 内容 | 校验规则 |
|------|------|----------|
| `proposal.md` | 为什么改 + 改什么 | `## Why` 不能少于 50 字符 |
| `specs/spec.md` | 具体需求，用 SHALL/MUST + Given/When/Then | 每个 Requirement 必须含 SHALL 或 MUST，至少一个 Scenario 块 |
| `design.md` | 技术方案（用什么库、改哪些类、数据流） | - |
| `tasks.md` | 可执行步骤清单 | - |

**工件依赖链**：proposal（意图）-> specs（需求）-> design（方案）-> tasks（步骤）-> implement。靠 YAML 引擎做拓扑排序，依赖关系是"使能"而非"卡死"--随时可回去改前面的工件。[[OpenSpec#工件依赖图]]

### 步骤 3：人工确认

**这是关键一步，不要跳**。审查四份文档：
- proposal.md：动机对不对
- spec.md：需求有没有漏掉边界场景
- design.md：技术方案是否合理
- tasks.md：步骤是否可执行

确认后告诉 AI："通过，开始实现"。

### 步骤 4：按清单实现 `/opsx:apply`

```
/opsx:apply
```

AI 按 `tasks.md` 逐项实现：
- 每完成一项，更新 tasks.md 进度（`[x]`）
- 生成实际代码 + 测试
- 如果中途发现 design 有问题，可以回去改 design.md 再继续

### 步骤 5：归档 `/opsx:archive`

```
/opsx:archive
```

完成后，把整个 `opsx/changes/export-order-excel/` 移入 `opsx/archive/`。**这就是对抗 AI 遗忘的核心**--所有历史决策永久存档，将来任何新会话都能回溯。

## 四、AI 遗忘问题的三层防护

| 层级 | 机制 | 作用 |
|------|------|------|
| **L1 规格层** | `opsx/specs/` 主规范 | 当前生效的需求规格，AI 每次会话加载 |
| **L2 归档层** | `opsx/archive/` 变更历史 | 所有历史决策的"为什么"，AI 按需检索 |
| **L3 增量层** | [[delta-spec]] `/opsx:sync` | 只描述差异，不重写整份 spec，防止文档腐烂 |

将来 AI 新会话问你"订单模块为什么用状态机而不是枚举"--你让它读 `opsx/archive/redesign-order-status/` 下的 proposal.md 和 design.md 即可。[[OpenSpec#核心工作流]]

## 五、项目目录最终结构

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

## 六、可选升级：SpecSuperflow（OpenSpec + Superpowers 融合）

如果你觉得 OpenSpec 只管"改了什么"还不够，还想要 AI 强制按纪律执行（先 TDD 再写实现），可以升级到 [[SpecSuperflow]]。它把 OpenSpec 的规划引擎和 [[Superpowers]] 的执行纪律**源码级融合**为一个插件。

```bash
# Claude Code 安装
/plugin marketplace add MageByte-Zero/spec-superflow
/plugin install spec-superflow@spec-superflow
```

它的完整流程是八状态机：`workflow-start -> need-explorer -> spec-writer -> contract-builder -> DP-3（人工审批）-> build-executor（TDD+SDD）-> release-archivist -> spec-merger`。核心创新是 `contract-builder` 把四份规划工件自动压缩成一份 execution-contract.md，没有契约或没被批准就不准进入实现。[[SpecSuperflow#八状态机]]

**但注意**：SpecSuperflow 适合"大型功能开发、多人协作、长期维护"的棕地项目。如果是快速原型或一次性脚本，太重了。经验法则--不需要写 proposal 和 design doc 就能想清楚的事，不要用。[[SpecSuperflow#适用边界]]

## 七、选型建议

| 你的情况 | 推荐方案 |
|----------|----------|
| 只想解决"AI 遗忘历史决策" | **OpenSpec 单独使用**，每次功能走 explore -> propose -> apply -> archive |
| 还想要 AI 强制按 TDD 纪律执行 | **OpenSpec + Superpowers**，或直接用 SpecSuperflow 融合插件 |
| 还想要 47+ Agent 池和安全扫描 | **ECC 全家桶**，OpenSpec 作为规划层嵌入 |
| 只改一两个文件的小修复 | 用 OpenSpec 的 hotfix 快速路径（≤2 文件）或 tweak 路径（≤4 文件纯配置），跳过完整规划工件 |

> 理想三重栈组合：OpenSpec 管"WHAT"（改了什么），Superpowers 管"HOW"（怎么干），[[ClaudeCode]] 负责"执行"。[[摘要-claude-code-best-practice-最新版]]

## 关联连接

- [[OpenSpec]] - 核心框架
- [[delta-spec]] - 增量变更机制
- [[SpecSuperflow]] - OpenSpec + Superpowers 融合插件
- [[规范驱动开发]] - 上层方法论
- [[claude-code-增强框架对比]] - 四大框架横向对比
- [[摘要-OpenSpec规范驱动AI编程框架]] - OpenSpec 来源
- [[摘要-spec-superflow-融合工作流-源码级详解]] - SpecSuperflow 深度解读
- [[摘要-claude-code-best-practice-最新版]] - 三重栈组合建议
- [[ClaudeCode]] - 承载平台
- [[Superpowers]] - 执行纪律框架
- [[ECC]] - 全家桶增强框架
- [[ContextManagement]] - 上下文管理（互补方案）
- [[persistent-memory]] - 持久记忆（互补方案）
- [[openspec-archive-modify-and-token-tradeoff]] - 配套：归档后修改流程与 Token 成本权衡分析