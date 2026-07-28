---
title: "TDD"
type: concept
tags: [测试, 开发方法论, 质量保证]
sources: [raw/01-articles/ECC-OpenCode-使用指南.md, raw/01-articles/Matt Pocock 那个 5 个月冲到 17 万 star 的 grill-me，作者自己却不用了，原因是这几个.md]
last_updated: 2026-07-27
---

## 定义
TDD（Test-Driven Development，测试驱动开发）是一种软件开发方法，要求在编写功能代码之前先编写测试用例。核心循环是 Red-Green-Refactor：先写一个失败的测试（Red），再写最少的代码让测试通过（Green），最后重构代码保持简洁（Refactor）。

## 关键信息
### 核心原则
- **测试先行**：先写测试，再写实现代码
- **小步快跑**：每次只添加一个测试，快速迭代
- **持续重构**：保持代码整洁，避免技术债务
- **快速反馈**：测试套件提供即时反馈，确保代码正确性

### 在 ECC 中的应用
- ECC 提供 `/tdd` 命令，自动执行 TDD 工作流
- 支持 Red-Green-Refactor 循环
- 与其他命令（如 `/plan`、`/code-review`）协同工作
- 帮助开发者养成良好的测试习惯

### 在 AI 编码中的定位（Matt Pocock 视角）
在 [[MattPocock]] 的 `mattpocock/skills` 两层架构中，`/tdd` 被归类为 **Model-invoked（纪律层）** skill——模型可自动调用，承载可复用的纪律。它作为"反馈回路"的核心组件，与 `/diagnosing-bugs` 配合解决 AI 编码的"跑不起来"失败模式。Matt 引用 The Pragmatic Programmer 的名言——"反馈的速度就是你的速度上限"——来强调 TDD 在 AI 编码中的价值：先写失败测试再修，比让 AI 直接写代码然后反复调试效率高得多。

### 优势
1. **代码质量**：测试覆盖确保代码正确性
2. **设计改善**：测试先行迫使思考接口设计
3. **重构安全**：测试套件保护重构过程
4. **文档作用**：测试即文档，说明代码行为
5. **调试简化**：快速定位问题所在

## 关联连接
- [[ECC]] — 提供 TDD 工作流支持
- [[code-review]] — 代码审查实践
- [[AICoding]] — AI 辅助编程中的 TDD 应用
- [[MattPocock]] — 将 TDD 作为纪律层 skill 的实践者
- [[摘要-mattpocock-skills]] — 来源（TDD 作为 AI 编码反馈回路）
