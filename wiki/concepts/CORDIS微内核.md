---
title: "CORDIS微内核"
type: concept
tags: [微内核, Agent, 插件架构, DeepSeek]
sources: [raw/01-articles/2026-10-31 - 推荐 10 个 DeepSeek 顶级开源项目.md]
last_updated: 2026-11-02
---

## 定义

CORDIS 是一种微内核（Microkernel）架构模式，将系统的核心功能（进程管理、内存管理、基础服务）精简到内核层，其余功能（文件系统、设备驱动、网络协议、Agent 工具等）以插件形式运行在用户态。DeepSeek Harness 即基于 CORDIS 微内核构建。

## 关键信息

- **微内核 vs 宏内核**：微内核只保留最核心的机制，其余全部外移到用户态插件；宏内核（如 Linux 传统内核）将大量服务编译进内核
- **在 Agent 领域的应用**：DeepSeek Harness 基于 CORDIS 微内核构建，全面拥抱「一切皆插件」与驾驭工程（Harness Engineering），把 Agent 的工具、技能、MCP 服务等全部做成可插拔插件
- **优势**：插件可独立开发/部署/升级，内核稳定性不受插件影响，系统可裁剪（按需加载插件）
- **工程文化**：DeepSeek Harness 仓库 `.agents/notes/` 目录将系统演进的真实思考全景留痕——方案选型日期、Trade-off、被放弃的技术路线，这种开源态度本身也是该项目的一大看点

## 关联连接
- [[DeepSeekHarness]] — 基于 CORDIS 构建的 Agent 底座
- [[DeepSeek]] — 主体公司
- [[插件架构]] — 微内核是插件化的一种实现（待建）
- [[苏三]] — 文章作者
