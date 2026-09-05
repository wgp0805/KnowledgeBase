---
title: "marka.md"
type: entity
tags: [Markdown编辑器, AI工具, Rust, Tauri, 本地优先]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

marka.md 是一款基于 Rust + Tauri 构建的轻量级本地 Markdown 编辑器，专为 AI 场景设计，能够将多个 Markdown 文件打包成 AI 可直接读取的上下文包。

## 关键信息

- **定位**：安静、轻量的本地 Markdown 编辑器，专注「整理笔记 → 编辑 → 打包发给 AI」链路
- **体积**：安装包仅几 MB，远小于 Electron 应用
- **技术栈**：Tauri 2.11 + React 19 + Vite 7 + TypeScript + CodeMirror 6
- **核心功能**：
  - Context Tray（上下文托盘）：暂存多文件，实时 Token 估算，一键复制 AI 就绪上下文包
  - 相对路径：保留项目结构但不暴露本机绝对路径
  - 未保存编辑：复制时使用编辑器最新内容
  - 兼容所有 AI：Claude/ChatGPT/Gemini/Cursor 等
- **写作体验**：左右分屏预览、Shiki 代码高亮、Mermaid 图表、任务列表、阅读模式、可选 Vim 模式
- **导出**：PDF 导出、代码块一键复制
- **个性化**：14 套主题（含 Claude/Cursor/Gemini 品牌色）、透明度调节
- **隐私**：本地优先，无账号、无云同步、无遥测
- **项目地址**：https://github.com/mattenarle10/markamd

## 关联连接

- [[Tauri]] — 桌面应用框架
- [[Rust]] — 系统编程语言
- [[CodeMirror]] — 代码编辑器组件
- [[Shiki]] — 代码高亮库
- [[Mermaid]] — 图表渲染
- [[Obsidian]] — 同类知识管理工具
- [[小锋]] — 文章作者
- [[摘要-markamd-rust-markdown-ai]] — 来源
