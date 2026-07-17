---
title: "AI 就绪上下文包"
type: concept
tags: [AI工具, 上下文管理, 工作流, Markdown]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

AI 就绪上下文包（AI-ready Context Bundle）是将多个相关文件打包成一个结构化文本块，供 AI 模型直接读取和理解的格式。

## 关键信息

- **组成结构**：
  - 文件内容：多个 Markdown 文件的完整内容
  - 文件路径：使用相对路径，保留项目结构
  - 分隔符：清晰的文件分隔标记
- **设计要求**：
  - 相对路径：不暴露本机绝对路径
  - Token 友好：控制总长度，适配 AI 上下文窗口
  - 未保存内容：包含编辑器最新状态
- **使用场景**：
  - 代码审查：将多个源文件打包给 AI 审查
  - 文档编写：将笔记打包给 AI 参考
  - 项目理解：将项目文档打包给 AI 分析
- **兼容性**：Claude/ChatGPT/Gemini/Cursor/本地 Agent 等所有接受纯文本的 AI

## 关联连接

- [[marka.md]] — 生成 AI 就绪上下文包的工具
- [[Context Tray]] — 生成上下文包的功能组件
- [[Token估算]] — 控制上下文长度的辅助功能
- [[AICoding]] — AI 辅助编程的工作流
