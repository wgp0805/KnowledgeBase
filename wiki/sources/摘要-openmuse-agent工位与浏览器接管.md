---
title: "摘要-openmuse-agent工位与浏览器接管"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/为什么越来越多人用OpenMuse？.md]
last_updated: 2026-10-08
---

## 核心摘要
苏三介绍 CopilotKit 团队 2026 年 9 月开源的个人 AI Agent「OpenMuse」（MIT 协议，上线不到一月 4.2K Star）。它不解决"多 Agent 怎么协作"（AutoGen/CrewAI 的问题），而是给单个 Agent 一个完整执行环境：持久 Playwright 浏览器（保留 cookies/登录态）、隔离 Linux 终端与文件系统，定位是"Agent 的工位"而非对话框架。核心差异化是 **可接管（Take control）**：Agent 遇到验证码、双因素认证或复杂页面时，人可打开同一个实时浏览器会话完成操作再交还，不重启任务、不重新登录。任务引擎支持暂停/恢复/取消/重试，跨 iOS/Android/Web，暴露 REST + WebSocket API 供 Java 等无官方 SDK 的语言集成。缺点：Alpha 阶段接口不稳、真实模式配置复杂、Chromium 占 0.25-0.48GB 内存、单所有者无多租户认证。适用自动化网页调研、价格监控、PDF 表单自动化与需人工介入的长任务。

## 关联连接
- [[OpenMuse]] — 核心实体
- [[MetaMuse]] — 同名"系"个人 Agent 产品对照
- [[personal-ai-agent]] — 个人 Agent 赛道
- [[WorkBuddy]] — 同类可接管/本地执行 Agent 对照
