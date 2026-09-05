---
title: "LoopEngineering"
type: concept
tags: [AI, Agent, 自动化循环, 方法论]
sources: [raw/01-articles/Loop Engineering 实战指南.md, raw/01-articles/Prompt 已死，Loop当立？先看完这5个生产级坑再决定.md]
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

### 生产环境五大坑（陶炳哲/阶跃星辰实践）
1. **生成和验证必须硬隔离**：不是靠提示词约束，而是工具可见性的硬隔离——builder 有 Write/Edit 权限，checker 只能有 Read/Grep/Glob/Bash
2. **编排器必须原样转发失败信息**：拿到 checker 报告后不能自己解读或过滤，必须完整转发给 builder，模糊报告会让 builder 瞎猜浪费循环
3. **必须有明确的停止规则**：最多几轮、什么情况下停止、什么情况下升级给人工，循环启动前就写死，没有刹车的 Loop 会在暗坑里疯狂燃烧
4. **状态必须落地**：所有进度不能只存在对话里，必须写进状态文件，AI 对话是"失忆"的，状态文件存在磁盘上下次从上次停下继续
5. **目标必须可验证**："把这个功能做好"不是合格目标，"所有单元测试通过、TS 编译无报错、Diff 不超过 500 行"才是

## 关联连接
- [[ClaudeCode]] — CLAUDE.md 平台
- [[Codex]] — AGENTS.md 平台
- [[Skill]] — 技能扩展机制
- [[CLAUDEmd]] — 项目指令文件规范
- [[渐进式披露]] — Skill 内容组织原则
- [[摘要-loop-engineering-guide]] — 方法论来源
- [[摘要-loop-engineering-pitfalls]] — 生产实践来源
- [[阶跃星辰]] — 生产级 Loop 实践公司
- [[可观测性]] — 系统状态监控与问题定位
