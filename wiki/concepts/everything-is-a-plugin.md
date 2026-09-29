---
title: "everything-is-a-plugin"
type: concept
tags: [概念, 架构, 插件, Agent]
sources: [raw/01-articles/DeepSeek桌面版真不错，再见了WebUI。.md]
last_updated: 2026-09-29
---

## 定义
"一切皆插件"：[[DeepSeekHarness]] 的核心架构理念——Agent 的每个组成部分（Agent loop、工具注册表、会话日志、上下文压缩、Sub-agent、Skills 加载、MCP 客户端）都不是硬编码，而是建立在 [[Cordis]] 框架上的普通插件，通过 `apply(ctx)` 导出 + `inject` 声明服务依赖。

## 关键信息
- **补丁分层**：插件打成 npm 包，`package.json` 的 `dsh` 字段指向 `cordis.patch.yml` 增量补丁；启动时基础 bundle → 各 bundle patch → profile patch → 用户 patch 逐层叠加
- **profile 隔离**：WebUI 用 `~/.dsh/profiles/web`，桌面版用 `~/.dsh/profiles/desktop`，会话/设置/凭证共享但**插件不共享**；desktop profile 只归 Electron 应用管，命令行拒绝访问
- **代价——插件无沙箱**：服务端插件直接跑在 Agent 宿主进程里；桌面版上宿主与全部插件共用同一 Electron Node 进程，页面部分同页运行无 iframe 隔离——官方 SAFETY.md 提醒不要安装来路不明的插件
- **架构含义**：模型负责推理，Harness 之外的一切（工具、记忆、上下文、协议）皆可被插件替换/热更——这既是生态爆发（5 天 1400+ 社区插件）的原因，也是安全边界的来源

## 关联连接
- [[摘要-dsh桌面版-electron源码解析]] — 来源（源码级拆解）
- [[DeepSeekHarness]] — 该理念的载体
- [[Cordis]] — 插件框架底座
- [[Electron]] — 桌面版宿主（插件无沙箱的放大器）
- [[Harness]] — 上位概念（Model + Harness = Agent）
- [[MCP]] — 被插件化的协议能力之一
