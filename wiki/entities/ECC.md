---
title: "ECC"
type: entity
tags: [AI, Claude-Code, OpenCode, Agent, 增强框架]
sources: [raw/09-archive/ECC使用教程.md, raw/01-articles/ECC-OpenCode-使用指南.md]
last_updated: 2026-06-26
---

## 定义
ECC（Everything Claude Code）是一个开源的 AI 编码智能体编排系统，由 affaan-m 在 GitHub 上维护（222K+ Stars），MIT 协议，完全免费。它原生支持 OpenCode、Claude Code、Cursor、Codex、Gemini 等多个 AI 编码工具，提供 agents、commands、hooks、skills、rules、custom tools 等一套完整的配置增强体系。版本基准：v1.10.0+，仓库：https://github.com/affaan-m/ECC

## 关键信息

### 六层架构
1. **Rules（规则）**：必须遵守的约束（如测试覆盖率 ≥80%）
2. **Skills（技能）**：如何完成特定任务的工作流（如 TDD 工作流）
3. **Agents（代理）**：能完成特定任务的"专家"（如 planner、tdd-guide）
4. **Hooks（钩子）**：自动触发的检查/动作（如编辑后自动 tsc）
5. **MCPs（外部服务）**：连接外部工具（GitHub、数据库等）
6. **Continuous Learning**：从历史中学习用户偏好和编码习惯

### 核心概念
- **Skills vs Commands vs Agents**：Skill 是菜谱（最重要），Command 是按铃（已过时），Agent 是厨师长
- **Rules vs Skills**：Rules 告诉 AI"不许做什么"（约束），Skills 告诉 AI"应该怎么做"（方法）
- **47+ Agents**：planner、architect、code-reviewer、security-reviewer、tdd-guide 等

### 安装方式
#### 三种安装方式对比（不要混用）
| 方式 | 是否依赖 ECC 目录 | 功能完整度 | 适用场景 |
|------|-----------------|-----------|---------|
| npm 包 | ❌ 不需要 | ⚠️ 仅 plugin hooks + tools | 只想用安全审计、格式化等 hooks |
| 完整克隆 | ✅ 必须在 ECC 目录内运行 opencode | ✅ 全部功能 | 学习/调试 ECC 本身 |
| 选择性复制 | ❌ 不需要 | ✅ 可自选组合 | **日常多项目开发（推荐）** |

#### 具体安装命令
- **方式一：npm 包安装（功能有限）**
  ```bash
  npm install ecc-universal -g
  ```
  在项目的 `opencode.json` 中加入：`"plugin": ["ecc-universal"]`

- **方式二：完整克隆仓库（功能全但受限）**
  ```bash
  git clone https://github.com/affaan-m/ECC.git
  cd ECC && npm install && npm run build:opencode && opencode
  ```

- **方式三：选择性复制到项目（推荐）**
  ```bash
  git clone https://github.com/affaan-m/ECC.git
  mkdir 你的项目/.opencode
  cp -Recurse ECC/.opencode/commands 你的项目/.opencode/commands/
  cp -Recurse ECC/.opencode/prompts 你的项目/.opencode/prompts/
  cp -Recurse ECC/.opencode/instructions 你的项目/.opencode/instructions/
  cp -Recurse ECC/skills 你的项目/.opencode/skills/
  cp -Recurse ECC/.opencode/tools 你的项目/.opencode/tools/
  ```

#### 传统安装方式（Claude Code）
- **插件安装（推荐）**：`/plugin marketplace add` + `/plugin install ecc@ecc`
- **手动安装**：`./install.sh --profile core`（minimal/core/full 三种 profile）

### 主要命令
| 命令 | 用途 |
|------|------|
| `/plan "添加用户认证"` | 生成实现计划（最重要的命令） |
| `/tdd` | TDD 工作流驱动（Red-Green-Refactor） |
| `/code-review` | 代码审查（80% 置信度过滤） |
| `/security` | 安全审查 |
| `/build-fix` | 修复编译错误 |
| `/orchestrate` | 多 agent 协同工作（feature/bugfix/refactor/security） |
| `/learn` | 从当前会话提取模式 |
| `/verify` | 验证循环（编译→Lint→测试→类型检查） |
| `/eval` | 评估指标 |

### 安全扫描（AgentShield）
三阶段流水线：红队（对抗性攻击）→ 蓝队（验证防御）→ 审计（生成报告）

## 关联连接
- [[ClaudeCode]] — 主要支持平台
- [[OpenCode]] — 同样支持的平台
- [[Cursor]] — AI 代码编辑器
- [[Codex]] — OpenAI 桌面端 AI Agent
- [[Gemini]] — Google 大模型系列
- [[Agent]] — Agent 核心概念
- [[Skill]] — Skill 技能扩展机制
- [[Hooks]] — 钩子系统
- [[AutoMemory]] — 持续学习相关
- [[ContextManagement]] — 上下文管理优化
- [[摘要-ECC使用教程]] — 来源（v1.10.0+ 完整教程）
- [[摘要-ECC-OpenCode-使用指南]] — 来源（安装方式对比）
