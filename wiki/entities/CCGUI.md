---
title: "CCGUI"
type: entity
tags: [实体, 工具, JetBrains插件, 开源]
sources: [raw/01-articles/IDEA 里跑 Claude Code 和 Codex 的最佳搭子，5.4k Star 开源免费太爽了！.md]
last_updated: 2026-08-18
---

## 定义
CC GUI（原名 Claude Code GUI，后为规避商标风险改名）是开源 JetBrains 插件，把 Claude Code、Codex 等 CLI Agent 接入 IDEA 工具窗口，让文件引用、执行过程、权限确认、Diff 和历史会话回到同一处。项目地址 zhukunpenglinyutong/jetbrains-cc-gui，MIT 许可证，5.4k Star。

## 关键信息
- **不提供模型能力**：真正干活的仍是 Claude Code、Codex 或其他已配置的 CLI，插件负责补齐 IDE 侧体验
- **三层架构**：
  - `src/main/java/` — JetBrains 插件层（IDE API、原生 Diff、通知、生命周期）
  - `webview/` — React + TypeScript 交互界面（会话、权限弹窗、流式结果）
  - `ai-bridge/` — Node.js CLI 适配与事件转换（归一化不同 CLI 事件格式）
- **消息链路**：输入框 → Java Bridge → ai-bridge → Claude/Codex CLI → 流式事件与文件补丁 → Java 回调 → React 更新
- **核心能力**：
  - `@文件`/代码选区/图片/控制台输出组织上下文
  - 流式文本/思考/命令/工具调用/子 Agent 状态拆分显示
  - 文件修改整理成 Diff，支持跳转/保留/撤销
  - 历史会话管理、搜索、收藏、导出、Token 与配额
  - 界面管理 Provider、Skills 和 MCP
  - 从编辑器/项目树/Run-Debug 控制台/VCS 区域直接发起动作
- **兼容范围**：JetBrains Build 233 到 263.*（以插件市场页面为准）
- **凭证来源**：手动 Provider / 显式读取本地配置 / CLI Login / cc-switch 兼容
- **专项修复记录**：Windows CLI 解析、JCEF 中文输入法、密集流式输出、权限 watcher、后台子 Agent、Codex patch 恢复
- **定位**：社区插件，非 JetBrains/Anthropic/OpenAI 官方产品；适合已长期使用 Claude Code 或 Codex CLI 且希望保留原配置习惯的用户

## 关联连接
- [[摘要-cc-gui-jetbrains插件]] — 来源资料
- [[ClaudeCode]] — 接入的 CLI Agent
- [[Codex]] — 接入的 CLI Agent
- [[IntelliJIDEA]] — 宿主 IDE
- [[JetBrains]] — 插件运行平台
- [[ACP]] — 官方 Agent 接入层（对比项）
- [[MCP]] — 插件支持的协议
- [[Skills]] — 插件支持的能力封装
- [[React]] — WebView 前端框架
- [[NodeJS]] — ai-bridge 运行时
