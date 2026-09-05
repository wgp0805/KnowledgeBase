---
title: "Tauri"
type: entity
tags: [桌面应用框架, Rust, Web前端, 跨平台]
sources: [raw/01-articles/仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计.md]
last_updated: 2026-07-16
---

## 定义

Tauri 是一个用于构建小型、快速且安全的桌面应用程序的框架，使用 Rust 作为后端，Web 技术（HTML/CSS/JS）作为前端界面。

## 关键信息

- **架构模式**：Rust 负责桌面壳和系统能力，Web 技术负责界面和编辑体验
- **核心优势**：
  - 体积小：使用系统 WebView 而非捆绑 Chromium
  - 性能高：Rust 后端提供原生性能
  - 安全：默认安全沙箱，权限控制精细
- **版本**：当前稳定版 Tauri 2.x
- **对比 Electron**：
  - Tauri 体积更小（几 MB vs 百 MB）
  - 内存占用更低
  - 安全性更好
- **典型应用**：marka.md、Potato（笔记应用）、CheatSheet 等
- **生态**：Tauri Plugin 系统支持文件系统、通知、全局快捷键等

## 关联连接

- [[Rust]] — 后端语言
- [[marka]] — 使用 Tauri 的应用案例
- [[Tauri]] — 官网：https://tauri.app
