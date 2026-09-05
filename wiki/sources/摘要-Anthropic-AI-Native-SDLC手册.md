---
title: "摘要-Anthropic-AI-Native-SDLC手册"
type: source
tags: [Anthropic, AI-Native, SDLC, intent.md, 审查前置, 开发手册]
sources: [raw/01-articles/2026-08-30-Anthropic 写给 AI Native 团队的完整开发手册.md]
last_updated: 2026-08-31
---

## 核心主旨

拆解 Anthropic 发布的《AI-Native SDLC Playbook》（AI 原生软件开发生命周期手册），核心机制是 **intent.md 产物链**和**审查前置**，重塑需求→设计→实现→测试→交付的全流程。

## 关键信息

### intent.md 产物链机制
- **intent.md** 是整个 SDLC 的"源头产物"，记录用户意图和需求边界
- 后续所有产物（设计文档、代码、测试、变更说明）都从 intent.md 派生
- 产物之间通过双向链接追溯：代码可回溯到设计，设计可回溯到 intent
- 类比：intent.md 是"宪法"，后续产物是"法律/细则/判例"

### 审查前置
- 传统 SDLC：审查在实现之后（代码审查）
- AI-Native SDLC：审查在实现之前（intent 审查、设计审查）
- 逻辑：AI 实现成本极低，错在 intent 比错在代码代价更大
- 实践：intent.md 必须经过人工审查后，才允许 Agent 开始实现

### SDLC 五阶段重塑
1. **意图捕获** — 写 intent.md，明确"要解决什么问题"
2. **设计对齐** — 基于 intent 产出设计文档，人工审查
3. **Agent 实现** — Agent 按设计文档生成代码
4. **自动验证** — 测试、lint、安全扫描自动执行
5. **交付复盘** — 回溯 intent，验证是否真正解决了问题

### 与现有工作流的关系
- intent.md 产物链与 [[OpenSpec]] 的 spec-driven 理念一致
- 审查前置与 [[Superpowers]] 的 grill-me（编码前需求澄清）呼应
- 与 [[Research-Plan-Execute-Review-Ship]] 五阶段范式同源

## 关联连接
- [[Anthropic]] — 手册发布方
- [[ClaudeCode]] — Anthropic 的 Agent 工具
- [[OpenSpec]] — 同类规范驱动理念
- [[Superpowers]] — grill-me 审查前置实践
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发范式
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比
- [[摘要-AGENTS.md只该管边界]] — 同期关于 Agent 协作规范的思考
