---
title: "Electron"
type: entity
tags: [桌面框架, 开源, 跨平台]
sources: [raw/09-archive/DeepSeek桌面版真不错，再见了WebUI。.md, raw/01-articles/2026-10-12-从 0 到 1：Electron41 + Vite8 + OpenAI SDK 接入 DeepSeek-V4.1-Flash 桌面端AI系统 - yxybox.md]
last_updated: 2026-10-13
---

## 定义
跨平台桌面应用框架，用 Web 技术（Chromium + Node.js）构建桌面程序。本知识库中它是 [[DeepSeekHarness]] 桌面版与社区版 deepseek-harness-desktop 的打包载体，也是 DSH 桌面版"页面与服务同进程运行、插件无沙箱"特性的技术根源。

## 关键信息
- **DSH 桌面版用法**：Electron 打包，主窗口加载完整 WebUI 页面，子进程跑 `dsh web` 同一套本地服务（端口 3080→19387），不重写界面，只补"Agent 常驻本机"能力（自动更新、关窗任务继续、自带运行时与 Office Skills、内置浏览器）
- **插件运行环境**：桌面版上 Agent 宿主与所有插件共用同一 Electron Node 进程，页面部分同页运行无 iframe 隔离——插件无沙箱的风险被 Electron 架构放大（DSH 官方 SAFETY.md 提醒勿装来路不明插件）
- **同类应用**：社区插件 deepseek-harness-desktop（anywhere-labs）也基于 Electron
- **桌面 AI 客户端模板（2026-10-12，详见 [[摘要-electron41-vite8-deepseek桌面ai]]）**：Electron 41 + Vue 3 + Vite 8 也是"接一个国产模型做桌面 AI 对话客户端"的主流组合。关键工作量不在接模型（OpenAI SDK + base_url 切换即可），而在渲染层：SSE 逐字渲染、`reasoning_content` 思维链折叠面板、highlight.js 按需加载、KaTeX、Mermaid 渲染、本地会话持久化；中文内容排版与深浅主题切换是此类模板的常见卖点

## 关联连接
- [[摘要-dsh桌面版-electron源码解析]] — 来源
- [[摘要-electron41-vite8-deepseek桌面ai]] — 来源（Electron 41 桌面 AI 客户端模板）
- [[DeepSeekHarness]] — 主要应用案例
- [[everything-is-a-plugin]] — 与该架构的交互关系
- [[Cordis]] — 与 Electron 同为 DSH 桌面版的两层技术基础
