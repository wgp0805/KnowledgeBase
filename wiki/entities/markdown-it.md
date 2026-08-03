---
title: "markdown-it"
type: entity
tags: [实体, Markdown, 解析器]
sources: []
last_updated: 2026-08-03
---

## 定义
markdown-it 是 JavaScript 生态流行的 Markdown 解析/渲染器，性能好、可扩展（支持插件与自定义语法），被 marka.md 等工具用作 Markdown 渲染引擎。

## 关键信息
- **定位**：JavaScript 最快的 Markdown 解析器之一，npm 生态广泛使用
- **特性**：CommonMark 兼容、插件系统、支持自定义规则
- **关联工具**：marka.md（Rust+Tauri Markdown 编辑器）使用 markdown-it 渲染
- **与 Shiki 的关系**：Shiki 负责代码高亮，markdown-it 负责整体 Markdown 渲染，二者常搭配

## 关联连接
- [[Shiki]] — 代码高亮搭配
- [[marka]] — 使用方
- [[CodeMirror]] — 同类编辑组件
