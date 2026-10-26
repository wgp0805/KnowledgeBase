---
title: "摘要-claude-code-mods机制"
type: source
tags: [来源, 原始文件, ClaudeCode, Mods, DeepSeekHarness, Agent扩展]
sources: [raw/09-archive/2026-10-04-Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？.md]
last_updated: 2026-10-08
---

## 核心摘要
Anthropic 在 Claude Code v2.1.287 推出 Claude Mods：开发者编写小型 TypeScript/JavaScript 函数挂到 Claude Code 进程内事件流上，执行三类操作——观察（Observe，只读放行）、改写（Rewrite，发送/执行前动态修改）、接管（Answer，直接返回结果跳过默认逻辑），形成类似中间件管道（Middleware Chain）的介入方式，并可在终端/桌面绘制自定义界面。官方四个扩展机制互补协同：Skills（Markdown 教模型理解任务）、MCP（外部工具）、Settings Hooks（生命周期外部脚本）、Mods（进程内事件函数），且部分内置能力已以 Mod 形式交付（/diff 对应 cc-plugin-diff、AGENTS.md 加载对应 cc-plugin-agents-md），未来计划把宿主缩减为小 Core 按需装配——与 DeepSeek Harness"一切皆插件"（Cordis 插件树装配整套 Harness、服务契约级组件插拔）演化方向相似：都把定制单元推进到 Agent 运行时内部、都用类似中间件的 next/提前返回流水线，但两套 API 与上下文模型完全不兼容，无协议继承关系。安全边界：Mods 无沙箱、以当前用户 OS 权限运行（Mod 自启进程在 Bash 沙箱之外）、不能改绘权限提示框，企业可经 Managed Settings/Team·Enterprise 登录触发 cc-plugin-sec-default 抢先加载并以 allowManagedModsOnly 拦截用户自带 Mods。

## 关联连接
- [[ClaudeCode]] — Mods 的宿主产品
- [[Mods]] — 本文核心概念
- [[DeepSeekHarness]] — 对比对象（一切皆插件）
- [[Cordis]] — DSH 的插件框架底座
- [[AgentHarness]] — 上位概念
- [[Anthropic]] — 发布方
