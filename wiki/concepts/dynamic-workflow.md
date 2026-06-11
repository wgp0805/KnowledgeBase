---
title: "dynamic-workflow"
type: concept
tags: [AI Agent, 工作流编排, 代码即配置, MiMo Code]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 定义
Dynamic Workflow 是用代码替代自然语言编排复杂 AI Agent 工作流的方案。主 Agent 生成 JavaScript 脚本，在隔离沙箱中确定性执行，通过 `agent()` 派出 Sub-agent，通过 `parallel()` 和 `pipeline()` 控制并发。

## 关键信息
- **问题本质**：传统 Skill 用自然语言写编排逻辑 → 自然语言模糊、可遗忘、不可验证 → 复杂流程中系统性失效（上下文压缩吞掉步骤、模型跳过环节、分支重试靠模型判断而非代码保证）
- **解决思路**：编排逻辑从自然语言变为代码（JavaScript），在隔离沙箱中确定性执行
- **兼容性**：兼容 Anthropic Dynamic Workflow 核心语义
- **扩展能力**：
  - `workflow()` 允许脚本调用其他脚本，编排逻辑可复用和组合
  - 每个 `agent()` 调用的结果同步落盘，进程中断后可恢复
  - 沙箱内可直接读写文件
- **Skill vs Workflow**：Skill 是用自然语言写的 SOP，Workflow 是用代码写的 SOP

## 关联连接
- [[MiMoCode]] — 所属产品
- [[max-mode]] — 计算主题的并行机制
- [[goals]] — 计算主题的串行机制
- [[AgentHarness]] — Harness 计算主题
- [[Skill]] — 自然语言 SOP 对比
- [[摘要-mimo-code发布]] — 来源
