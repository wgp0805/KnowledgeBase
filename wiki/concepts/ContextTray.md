---
title: "Context Tray"
type: concept
tags: [AI工具, 上下文管理, Markdown, 工作流]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

Context Tray（上下文托盘）是 marka.md 的核心功能，允许用户将多个 Markdown 文件「暂存」到侧边栏，实时显示文件数量和 Token 估算，一键复制成 AI 就绪的上下文包。

## 关键信息

- **工作流程**：
  1. 将多个 .md 文件拖入 Context Tray
  2. 实时显示文件数量和 Token 估算
  3. 一键复制为 Bundle（上下文包）
  4. 粘贴到任意 AI 对话窗口
- **设计优势**：
  - 相对路径：保留项目结构，不暴露本机绝对路径
  - 未保存内容：复制时使用编辑器最新内容
  - Token 估算：帮助用户控制上下文长度
- **解决的痛点**：
  - 传统方式需逐个打开、复制、粘贴
  - 文件名和路径管理混乱
  - 容易遗漏未保存的编辑

## 关联连接

- [[marka.md]] — 实现 Context Tray 的应用
- [[AI就绪上下文包]] — Context Tray 的输出格式
- [[Token估算]] — Context Tray 的辅助功能
