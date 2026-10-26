---
title: "Cordis"
type: entity
tags: ["Cordis", "DeepSeek", "Harness", "插件框架"]
sources: [raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md, raw/09-archive/DeepSeek桌面版真不错，再见了WebUI。.md]
last_updated: 2026-09-29
---

# Cordis

Cordis 是 [[DeepSeekHarness]] 的插件系统底座（Koishi 同源技术，4 年 4000+ 社区插件验证），提供插件机制扩展 Agent 能力，与 Claude Code Skills 的设计理念可对比。DSH 中插件以 `apply(ctx)` 导出 + `inject` 声明服务依赖接入 Cordis。

## 关键信息（2026-09-29 源码级补充）
- **补丁分层**：插件打成 npm 包，`package.json` 的 `dsh` 字段指向 `cordis.patch.yml` 增量补丁；启动时基础 bundle → 各 bundle patch → profile patch → 用户 patch 逐层叠加
- **profile 隔离**：WebUI 用 `~/.dsh/profiles/web`，桌面版用 `~/.dsh/profiles/desktop`，会话/设置/凭证共享但插件不共享
- **插件无沙箱**：服务端插件直接跑在 Agent 宿主进程（桌面版即 Electron Node 进程）里，官方 SAFETY.md 提醒勿装来路不明插件
- **地位**：Cordis 是 [[everything-is-a-plugin]] 架构理念的实现载体，详见 [[摘要-dsh桌面版-electron源码解析]]

## 关联连接
[[DeepSeek]], [[DeepSeekHarness]], [[HarnessEngineering]], [[Skills]], [[沉默王二]], [[everything-is-a-plugin]], [[Electron]], [[摘要-dsh桌面版-electron源码解析]], [[摘要-cordis-deepseek-harness]]
