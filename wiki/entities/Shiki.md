---
title: "Shiki"
type: entity
tags: [代码高亮, 语法高亮, VSCode, TextMate]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

Shiki 是一个基于 TextMate 语法的代码高亮库，使用 VS Code 的语法和主题，生成精确的语法高亮 HTML。

## 关键信息

- **核心原理**：使用 TextMate 语法文件（与 VS Code 相同）进行词法分析
- **技术特点**：
  - 精确：与 VS Code 完全一致的高亮效果
  - 快速：异步高亮，支持 Worker 线程
  - 轻量：按需加载语言包和主题
- **对比其他方案**：
  - vs Prism.js：Shiki 更精确（TextMate vs 自定义词法）
  - vs highlight.js：Shiki 主题更丰富
- **marka.md 使用**：懒加载策略，主题和语言包仅在用到时加载，启动快、内存可控

## 关联连接

- [[marka]] — 使用 Shiki 的应用
- [[CodeMirror]] — 常配合使用的编辑器组件
- [[markdown-it]] — marka.md 使用的 Markdown 渲染器
