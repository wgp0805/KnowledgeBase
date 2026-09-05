---
title: "摘要-mimo-code发布"
type: source
tags: [来源, 原始文件, MiMo Code, 小米]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 核心摘要
小米基于 OpenCode 发布了 MiMo Code 0.1（MIT 开源），是一款 AI 编程 Agent 工具。文章详细解析了其 Harness 架构——围绕计算（Max Mode、Goal、Dynamic Workflow）、记忆（四层记忆体系）展开。Max Mode 通过并行生成 N 个候选方案由 judge 选出最优来提升可靠性；Goal 通过独立验证器防止 Agent 提前宣称完成；Dynamic Workflow 用 JavaScript 脚本替代自然语言编排复杂任务。上下文管理采用 Checkpoint/Rebuild 机制和分层记忆（Session/Project/Global/History）实现无限延伸。

## 关联连接
- [[MiMoCode]] — 本文介绍的核心实体
- [[Xiaomi]] — 发布公司
- [[OpenCode]] — MiMoCode 的底层框架
- [[max-mode]] — 并行候选评估机制
- [[goals]] — 带验证器的任务完成机制
- [[dynamic-workflow]] — 代码化的工作流编排
- [[checkpoint-rebuild]] — 上下文窗口管理机制
- [[AgentHarness]] — Harness 架构总称
