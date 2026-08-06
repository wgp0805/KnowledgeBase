---
title: "Harness"
type: concept
tags: [概念, Agent, 架构, 框架]
sources:
  - raw/01-articles/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
last_updated: 2026-08-06
---

## 定义
Harness 是指 AI Agent 中模型之外的一切基础设施层，包括工具调用、记忆管理、上下文控制、桌面集成、MCP 协议、Skills 体系等。核心公式为 **Model + Harness = Agent**：模型负责推理，Harness 负责将模型的推理能力转化为可执行的工程化操作。

## 关键信息
- Harness 是未来五年 AI 工程化的核心主题，各大模型厂商都在争先恐后构建自己的 Harness
- 国内主要 Harness 产品：DeepSeek Harness（DSH）、阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode
- 所有 Agent 本质上都是在做 Harness——让模型更好用、更匹配业务
- **Harness 最关键的能力**：上下文管理、Memory 管理、多 Agent 协作、提示词优化

### 核心组件
1. **工具调用系统**：工具注册表、Schema 校验、HITL 审批
2. **记忆管理系统**：短期记忆（会话级）、长期记忆（跨会话持久化）、项目记忆（规则文件）
3. **上下文控制**：窗口管理、摘要压缩、Token 预算控制
4. **MCP 协议**：外部服务集成
5. **Skills 体系**：可复用的行为模块
6. **多 Agent 协作**：Sub-agent 编排、任务分解

## 关联连接
- [[DeepSeekHarness]] — DeepSeek 原生 Harness 实现
- [[PaiCLI]] — 开源终端 Agent Harness 实现
- [[ReAct_Agent]] — ReAct 推理循环是 Harness 的核心模式
- [[摘要-deepseek-harness内测]] — 来源
- [[ClaudeCode]] — Claude 的 Harness 实现
- [[Codex]] — Codex 的 Harness 实现
- [[HITL]] — 人机协作审批机制
- [[context-compression]] — 上下文压缩策略