---
title: "ECC"
type: entity
tags: [AI, Claude-Code, OpenCode, Agent, 增强框架]
sources: [raw/09-archive/ECC使用教程.md]
last_updated: 2026-06-02
---

## 定义
ECC（Everything Claude Code）是安装在 Claude Code 和 OpenCode 之上的增强框架，提供预定义工作流、专业化子代理、自动化钩子、持续学习系统和安全扫描器。版本基准：v1.10.0+，仓库：https://github.com/affaan-m/ECC

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
- **插件安装（推荐）**：`/plugin marketplace add` + `/plugin install ecc@ecc`
- **手动安装**：`./install.sh --profile core`（minimal/core/full 三种 profile）
- **OpenCode**：`npm install -g opencode-ecc`

### 主要命令
- `/plan` — 制定实施计划（最重要的命令）
- `/tdd` — 测试驱动开发（Red-Green-Refactor）
- `/code-review` — 代码审查（80% 置信度过滤）
- `/verify` — 验证循环（编译→Lint→测试→类型检查）
- `/orchestrate` — 多代理编排（feature/bugfix/refactor/security）
- `/learn-eval` — 持续学习模式提取

### 安全扫描（AgentShield）
三阶段流水线：红队（对抗性攻击）→ 蓝队（验证防御）→ 审计（生成报告）

## 关联连接
- [[ClaudeCode]] — 主要支持平台
- [[OpenCode]] — 同样支持的平台
- [[Agent]] — Agent 核心概念
- [[Skill]] — Skill 技能扩展机制
- [[Hooks]] — 钩子系统
- [[AutoMemory]] — 持续学习相关
- [[ContextManagement]] — 上下文管理优化
- [[摘要-ECC使用教程]] — 来源
