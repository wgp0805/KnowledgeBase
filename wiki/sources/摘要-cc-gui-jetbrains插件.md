---
title: "摘要-cc-gui-jetbrains插件"
type: source
tags: [来源, 原始文件, JetBrains插件, ClaudeCode, Codex]
sources: [raw/01-articles/IDEA 里跑 Claude Code 和 Codex 的最佳搭子，5.4k Star 开源免费太爽了！.md]
last_updated: 2026-08-18
---

## 核心摘要
CC GUI（原名 Claude Code GUI）是 JetBrains 插件，把 Claude Code、Codex 等 CLI Agent 接入 IDEA 工具窗口，让文件引用、执行过程、权限确认、Diff 和历史会话回到同一处。项目 MIT 许可证，5.4k Star，采用 Java + React + Node 三层架构（JetBrains 插件层 / React WebView / ai-bridge CLI 适配层）。文章对比了 JetBrains 官方 Agent/ACP、CC GUI、纯终端三条路线的取舍，并给出安装注意事项与"先只读规划、再人工复核、最后才让 Agent 修改测试"的实战工作流（以 Spring Boot 退款回调补幂等为示例）。

## 关键信息
- **项目地址**：zhukunpenglinyutong/jetbrains-cc-gui
- **三层架构**：
  - `src/main/java/` — JetBrains 插件层（IDE API、Diff、通知、生命周期）
  - `webview/` — React + TypeScript 交互界面（会话、权限弹窗、流式结果）
  - `ai-bridge/` — Node.js CLI 适配与事件转换（归一化 Claude/Codex 事件）
- **核心能力**：`@文件`/选区/图片/控制台输出组织上下文；流式文本/思考/命令/工具调用/子 Agent 状态拆分显示；Diff 跳转/保留/撤销；历史会话搜索收藏导出；Provider/Skills/MCP 界面管理
- **兼容范围**：JetBrains Build 233 到 263.*（以插件市场页面为准）
- **凭证来源**：手动 Provider / 本地配置 / CLI Login / cc-switch 兼容
- **三条路线对比**：
  | 路线 | 优势 | 代价 |
  | --- | --- | --- |
  | JetBrains 官方 Agent/ACP | 官方维护、IDE 集成统一、团队治理顺 | 受 JetBrains 版本与 Provider 范围影响 |
  | CC GUI | MIT 开源、CLI 会话管理细、历史配额界面丰富 | 多一层 bridge，升级兼容需社区处理 |
  | 纯终端 | 链路最短、脚本化方便、新能力最先可用 | 文件/Diff/报错/权限分散多窗口 |
- **长期使用五项关注**：上下文入口、权限可见性、Diff 与回退、会话恢复、进程稳定性
- **实战工作流**：`/plan` 只读规划 → 人工复核方案 → 执行模式限定修改范围 → 运行测试展示 Diff

## 关联连接
- [[CCGUI]] — 文章介绍的开源 JetBrains 插件实体
- [[ClaudeCode]] — 接入的 CLI Agent 之一
- [[Codex]] — 接入的 CLI Agent 之一
- [[IntelliJIDEA]] — 插件宿主 IDE
- [[JetBrains]] — 插件运行平台与官方 AI Assistant 对比方
- [[程序汪]] — 文章作者
- [[ACP]] — JetBrains 官方 Agent 接入层协议
- [[MCP]] — 插件支持的协议
- [[Skills]] — 插件支持的能力封装
