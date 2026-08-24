---
title: "PromptInjection"
type: concept
tags: [AI安全, 提示词注入, Agent, Anthropic]
sources: [raw/01-articles/2026-08-23-对话 Claude Code 之父：当模型越来越聪明，还在设计复杂工作流的人只是在假装做产品.md]
last_updated: 2026-08-24
---

# Prompt Injection（提示词注入）

## 核心定义
攻击者通过在模型读取的内容中嵌入恶意指令，诱导模型执行非预期操作。当 Agent 同时具备访问不可信内容、访问敏感数据、执行外部操作（lethal trifecta，致命三要素）时，风险尤为严重。

## Opus 5 的突破
Boris Cherny 表示，Opus 5 已很难再被有效注入攻击。通过三层防护实现：

1. **模型对齐**：三年左右的 alignment 研究，模型本身具备抵抗能力
2. **注入检测器**：基于 Crysola 的机制可解释性研究，观察模型"大脑"中的神经元激活——当 prompt injection 发生时特定神经元会被激活，即使模型不报告也能检测到
3. **Auto Mode classifier**：对所有流量运行的分类器

## 影响
Prompt Injection 从根本性障碍变为可控问题，这对 harness design、Agent design 和 product design 产生重大影响——Agent 可以更安全地访问互联网内容并执行操作。

## 关联连接
- [[BorisCherny]]
- [[ClaudeCode]]
- [[Anthropic]]
- [[auto-mode]]
- [[沙箱]]
- [[Agent]]
