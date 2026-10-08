---
title: "OpenMuse"
type: entity
tags: [AI-Agent, 个人Agent, 浏览器自动化, 开源]
sources: [raw/01-articles/为什么越来越多人用OpenMuse？.md]
last_updated: 2026-10-08
---

## 定义
OpenMuse 是 CopilotKit 团队于 2026 年 9 月开源的个人 AI Agent（MIT 协议），定位"Agent 的工位"：为单个 Agent 提供持久浏览器、隔离终端与文件系统的完整执行环境，并支持人工随时接管实时浏览器会话。

## 关键信息
- 与 AutoGen/CrewAI 的区别：那些解决"多 Agent 怎么协作"，OpenMuse 解决"一个 Agent 怎么真正动手完成任务"
- 执行环境：Playwright Chromium 持久化 profile（cookies/登录态/历史保留）+ 隔离 Linux 终端 + 文件系统
- 核心差异化"Take control"：Agent 卡在验证码/双因素认证/复杂页面时，人接管的是**同一个实时浏览器会话**，交还后 Agent 从当前状态继续，不重启不重登
- 持久化任务引擎：任务支持暂停、恢复、取消、重试，关闭浏览器后继续执行；每次外部写入需审批
- 技术栈 TypeScript（Node.js 24 LTS + pnpm 11.19.0），暴露 REST + WebSocket API，Java 侧可经 HTTP 任务导向调用（无官方 SDK）
- 内置零配置演示模式（pnpm dev，8081 端口），跨 iOS/Android/Web
- 缺点：Alpha 阶段接口不稳、配置较复杂、Chromium 约 0.25-0.48GB 内存、单所有者无多租户认证
- 上线不到一个月 GitHub 4.2K Star；适用网页调研、价格监控、PDF 表单自动化

## 关联连接
- [[摘要-openmuse-agent工位与浏览器接管]] — 来源
- [[MetaMuse]] — 同名系个人 Agent 产品对照
- [[personal-ai-agent]] — 所属赛道
- [[WorkBuddy]] — 同类可接管/本地执行 Agent
