---
title: "LoopEngineering"
type: concept
tags: [AI, Agent, 自动化循环, 方法论]
sources: [raw/01-articles/Loop Engineering 实战指南.md]
last_updated: 2026-07-06
---

## 定义
循环工程（Loop Engineering）是一套用 Markdown 文件驱动 AI Agent 自动化循环的方法论，通过 AGENTS.md/CLAUDE.md（宪法）、STATE.md（记忆）、SKILL.md（技能）三份文件定义循环的边界、能力和进度。

## 关键信息

### 三文件体系
| 文件 | 职责 | 维护者 |
|------|------|--------|
| AGENTS.md / CLAUDE.md | 循环的"宪法"——项目规则、安全边界、运行命令 | 开发者写完即稳定 |
| STATE.md | 循环的"记忆"——记录进度、发现、下一步 | 循环自动更新 |
| SKILL.md | 循环的"技能卡"——封装具体能力（分诊/修复/验证） | 开发者编写，循环复用 |

### 三级循环模式
- **L1 报告模式**：只汇报不修代码，适合初始阶段建立信任
- **L2 分诊+小修**：自动修复简单问题，中高风险升级给人
- **L3 无人值守**：近乎全自动，需充分信任循环判断力

### 提示词设计
- `/loop` — 启动循环，指定时间范围、调用 Skill、产出写入 STATE.md
- `/goal` — 设定目标，循环持续跑直到条件满足，由独立验证模型判断完成

### 核心 Skill
- **loop-triage**（分诊）：扫描 CI 失败/Issue/提交，产出优先级报告
- **minimal-fix**（最小修复）：对指定问题产出最小代码改动
- **loop-verifier**（独立验证）：拒绝而非接受的检查者角色，全部通过才审批
- **loop-budget**（费用控制）：Token 预算管理

## 关联连接
- [[ClaudeCode]] — CLAUDE.md 平台
- [[Codex]] — AGENTS.md 平台
- [[Skill]] — 技能扩展机制
- [[CLAUDEmd]] — 项目指令文件规范
- [[渐进式披露]] — Skill 内容组织原则
- [[摘要-loop-engineering-guide]] — 来源
