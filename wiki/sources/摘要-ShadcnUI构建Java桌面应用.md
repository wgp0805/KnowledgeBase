---
title: "摘要-ShadcnUI构建Java桌面应用"
type: source
tags: [来源, Java桌面, JxBrowser, shadcn]
sources: ["raw/01-articles/使用 Shadcn UI 构建 Java 桌面应用.md"]
last_updated: 2026-07-13
---

## 核心摘要

本文介绍如何使用 JxBrowser + React + shadcn/ui 构建跨平台 Java 桌面应用。解决三个核心问题：可靠的 Web 视图（JxBrowser Chromium 内核）、无服务器加载（jxb:// 协议从 classpath 加载）、Java ↔ Web 通信（JS-Java Bridge 或 Protobuf+gRPC）。

该方案借鉴了 Slack、Notion、Teams 等桌面应用的 Web UI 技术路线，让 Java 桌面应用能利用前端生态红利，同时保持原生应用的体验。

## 关联连接
- [[JxBrowser]] — Chromium 内核 Web 视图
- [[shadcn_ui]] — UI 组件库
- [[Protobuf]] — 序列化协议
- [[gRPC]] — RPC 框架
