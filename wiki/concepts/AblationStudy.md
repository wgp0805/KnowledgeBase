---
title: "AblationStudy"
type: concept
tags: [AI工程, 模型评估, 消融实验, 产品设计]
sources: [raw/01-articles/2026-08-23-对话 Claude Code 之父：当模型越来越聪明，还在设计复杂工作流的人只是在假装做产品.md]
last_updated: 2026-08-24
---

# Ablation Study（消融实验）

## 核心定义
通过逐个删除系统组件来评估每个组件单独产生的影响。在 AI 产品工程中，指删除 system prompt、工具、hooks 等组件后观察模型表现，判断哪些组件真正有用。

## Claude Code 的实践
1. **每次新模型发布都做 ablation**：删除整个 system prompt，再逐行加回，判断每行的影响
2. **工具也做 ablation**：不断 unship 工具，删除 harness 里的代码
3. **结果**：Claude Code harness 里剩下的代码几乎全是围绕安全性、权限和静态分析的，加上 UI 代码
4. **隐藏功能**：设置 `CLAUDE_CODE_SIMPLE=1` 环境变量可删除所有 system prompt（包括工具中的），用作 ablation 实验

## 关键发现
- Opus 5 删除 80% system prompt 后表现更好
- 在没有 prompt 的情况下，模型实际上反而稍微更聪明一点
- 三个月前针对某模型做的优化，到下一个模型可能完全无法迁移

## 与 Eval 的关系
Ablation 本质上是一种 eval——通过删除东西来判断其影响。Eval 的生命周期比 harness 稍长，但在指数增长阶段，eval 很快会饱和，需要重新设计。

## 关联连接
- [[Unhobbling]]
- [[ProductOverhang]]
- [[BorisCherny]]
- [[ClaudeCode]]
- [[ContextEngineering]]
