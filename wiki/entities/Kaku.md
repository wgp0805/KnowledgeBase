---
title: "Kaku"
type: entity
tags: [终端工具, AI编程, 开源工具, Rust]
sources: [raw/01-articles/又一个神级终端诞生了！让 Claude Code和Codex 用得更爽！.md]
last_updated: 2026-07-14
---

## 定义
Kaku 是一款基于 WezTerm 深度定制的 AI 终端工具，用 Rust 编写，提供开箱即用的极客风终端体验，内置 Claude Code 和 Codex 支持。

## 关键信息
- **技术栈**：Rust 编写，基于 WezTerm 深度定制
- **安装方式**：支持 Homebrew (`brew install tw93/tap/kaku`) 和 DMG 下载安装
- **协议**：MIT 协议，完全免费
- **核心功能**：
  - AI 模式：通过 `command + L` 快捷键进入
  - 上下文附加：支持 `@cwd`（项目概况）、`@tab`（终端画面）、`@selection`（选中文本）
  - 模型切换：`shift + tab` 快速切换 AI 模型
  - 内置工具：Lazygit（Git 可视化）、Yazi 文件管理器、目录跳转、广播输入
  - 快捷键：`Cmd+T` 新建标签，`Cmd+D` 分屏，`Cmd+L` AI 面板等
- **适用场景**：终端报错分析、项目理解、代码审查、中小型 bug 修复
- **平台限制**：目前仅支持 macOS
- **GitHub 星标**：5.6k+ star

## 关联连接
- [[摘要-又一个神级终端诞生了让-codex-用得更爽]] — 来源
- [[ClaudeCode]] — 内置的 AI 编码助手
- [[Codex]] — 内置的 AI 编码助手
- [[WezTerm]] — 基于的终端模拟器
- [[Lazygit]] — 内置的 Git 可视化工具
- [[Yazi]] — 内置的文件管理器
- [[JetBrainsMono]] — 预设的编程字体
- [[AI终端]] — 相关概念