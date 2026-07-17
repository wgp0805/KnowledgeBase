---
title: "CodeMirror"
type: entity
tags: [代码编辑器, Web组件, 可扩展, 模态编辑]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

CodeMirror 是一个用于浏览器的代码编辑器组件，提供丰富的 API 用于展示和操作文本代码，支持语法高亮、自动补全、括号匹配等功能。

## 关键信息

- **当前版本**：CodeMirror 6（CM6），完全重写，模块化架构
- **核心特性**：
  - 语法高亮：支持 100+ 语言
  - 可扩展：通过 Extension 系统添加功能
  - 模态编辑：可选 Vim/Emacs 键绑定
  - 协作编辑：支持多人实时协作
- **技术架构**：
  - 基于 DOM 的视图层
  - 状态树（State Tree）管理编辑器状态
  - 命令（Command）系统处理用户操作
- **应用场景**：VS Code（内部使用 Monaco，类似理念）、GitHub、GitLab 等
- **marka.md 使用**：作为核心编辑器组件，支持可选 Vim 模式

## 关联连接

- [[marka.md]] — 使用 CodeMirror 的应用
- [[Shiki]] — 常配合使用的代码高亮库
- [[Vim]] — CodeMirror 支持的键绑定模式
