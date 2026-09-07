---
title: "diagnosing-bugs"
type: concept
tags: [调试, 质量保证, AI编程]
sources: [raw/01-articles/Matt-Pocock-Skills与OpenSpec配合开发完整教程.md]
last_updated: 2026-09-05
---

## 定义
`/diagnosing-bugs` 是 Matt Pocock Skills 中的系统化调试 skill，用于在测试失败或代码运行异常时，系统化定位根因而非让 AI 瞎改。

## 关键信息
### 核心原则
- **系统化定位**：不盲目修改代码，而是按步骤分析可能的原因
- **根因分析**：找到问题的根本原因，而非表面症状
- **避免瞎改**：防止 AI 随意修改代码引入新问题

### 使用场景
- 测试跑不过时
- 代码运行异常时
- 需要定位复杂 bug 时

### 在 OpenSpec + Matt Skills 流程中的位置
在 OpenSpec + Matt Skills 配合开发流程中，`/diagnosing-bugs` 通常在以下时机使用：
1. `/tdd` 实现过程中测试跑不过时
2. `/code-review` 后修复问题时遇到困难
3. 任何代码运行异常需要系统化调试时

### 典型用法
```
/diagnosing-bugs 测试跑不过，帮我系统化定位根因，不要瞎改
```

## 关联连接
- [[MattPocock]] — skill 作者
- [[TDD]] — 测试驱动开发（经常配合使用）
- [[摘要-matt-openspec配合开发教程]] — 使用场景来源
- [[openspec-matt-skills-execution-workflow]] — 配合执行流程详解
