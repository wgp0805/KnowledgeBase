---
title: "Research-Plan-Execute-Review-Ship"
type: concept
tags: [ClaudeCode, 工作流, 开发范式, AICoding]
sources: ["raw/01-articles/夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！.md"]
last_updated: 2026-06-24
---

## 定义
**Research → Plan → Execute → Review → Ship** 是 [[ClaudeCode]] 主流开发工作流项目（Superpowers、Spec Kit、gstack、Get Shit Done、[[OpenSpec]] 等）共同采用的五阶段范式：**先研究，再计划，再执行，再审查，最后交付**。其本质是要求用户**拆阶段使用 Agent**，而不是一上来就让它写代码。

## 关键信息

### 五阶段含义
| 阶段 | 任务 | 产出 |
|---|---|---|
| Research | 让 Agent 读项目、需求、相关代码 | 上下文清单 |
| Plan | 输出实现方案 | 设计文档/任务清单 |
| Execute | 在方案确认后写代码 | 代码改动 |
| Review | 自审、子 Agent 审查、测试 | 评审报告/测试结果 |
| Ship | 提交/PR/发布 | 最终交付物 |

### 为什么必须拆阶段
许多人用 Claude Code 没有提效，原因是**直接让它写代码**，Agent 不知道目标和约束，结果产出偏离预期。拆阶段执行让每一步都可校验、可纠偏，符合 [[steering]] 机制。

### 推荐做法
> **先让 Claude 读项目和需求，输出方案；方案确认后，再开新阶段执行；执行完成后，再进入 Review 和测试阶段。**

### 与 [[VibeEngineering]] 的呼应
该范式实际就是 Vibe Engineering 在 Claude Code 上的工程化落地——对代码负责、重度调度 Agent、明确每阶段的人机协作边界。

### 主流工作流项目（共用此架构）
- **Superpowers**
- **Everything Claude Code**
- **Matt Pocock Skills**
- **Spec Kit**
- **gstack**
- **Get Shit Done**
- [[OpenSpec]]

## 关联连接
- [[摘要-claude-code-best-practice]] — 来源
- [[claude-code-best-practice]] — 提出仓库
- [[ClaudeCode]] — 落地平台
- [[Command-Agent-Skill编排]] — 阶段内的编排架构
- [[VibeEngineering]] — 理念呼应
- [[OpenSpec]] — 采用该范式的工作流项目
- [[steering]] — 阶段纠偏机制
- [[AICoding]] — 编程范式
- [[goals]] — 与"带验证器的长跑任务"思路一致
