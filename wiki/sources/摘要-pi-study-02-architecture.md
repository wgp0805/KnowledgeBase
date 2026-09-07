---
title: "摘要-pi-study-02-architecture"
type: source
tags: [来源, pi-agent, 学习笔记, 架构]
sources: [raw/01-articles/pi-study-02-architecture.md]
last_updated: 2026-08-09
---

## 核心摘要

本篇是 Pi (pi.dev) 系统学习的第二课笔记，详细讲解 Pi 的整体架构。Pi 采用"小内核 + 强扩展"的双层架构：核心层包含 LLM Loop（运行循环）、工具系统、Session 管理、TUI 界面四大组件；扩展层分为四个层次（Prompt Template / Skill / Extension / Package），从浅到深能力逐级递增。两层之间通过 ExtensionContext（扩展上下文）连接，扩展通过其提供的 API 和事件系统参与到核心运行中。

## 关键知识点

1. **核心层四件套**：LLM Loop（思考-工具调用-观察循环）、工具系统（注册/调度/安全）、Session管理（持久化/分支/压缩）、TUI界面（Ink组件化）
2. **扩展四层模型**：Prompt Template < Skill < Extension < Package，从声明式到代码级
3. **ExtensionContext**：扩展上下文是核心与扩展的桥梁，提供读取API、操作API、事件系统、UI API
4. **事件驱动**：扩展通过监听事件（tool_call、model_request等）参与运行，反向控制
5. **加载流程**：发现 → jiti加载 → 执行注册 → 就绪，支持 /reload 热重载
6. **Harness 的价值**：工程化细节（压缩、重试、死循环防护、中断）决定 Agent 实际表现

## 关联连接
- [[Pi (coding harness)]] — 学习对象，Pi Agent 基座
- [[AgentHarness]] — Harness 概念
- [[Agent扩展层级]] — 扩展四层模型
- [[LLM Loop]] — Agent 运行循环
- [[Agent]] — Agent 核心概念
- [[摘要-pi-agent-study-01-pi-overview]] — 前一课，Pi 定位与核心理念
