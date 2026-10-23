---
title: "Flutter"
type: entity
tags: [前端框架, 跨平台, Google, 移动开发]
sources: [raw/09-archive/2026-10-22-纯原生Flutter3 + Dio 实战 DeepSeek V4.1 SSE流式对话 - yxybox.md]
last_updated: 2026-10-23
---

## 定义
Flutter 是 Google 开源的跨平台 UI 框架（Dart 语言），一套代码运行 Android / iOS / Web / Windows / macOS / Linux。

## 关键信息
- **版本**：2026-10 实践常用 Flutter 3.41.5 + Dart 3.11
- **生态**：60000+ 内置 Material / Cupertino 组件，Widget 一切皆组件的声明式 UI
- **AI 应用场景（2026-10-22，详见 [[摘要-flutter-dio-deepseek-sse]]）**：
  - 以 [[Dio]] 处理 [[SSE]] 流式请求，配合 GetX 状态管理实现打字机式对话
  - 渲染层组合：flutter_markdown_plus（Markdown）+ flutter_highlight（代码高亮）+ flutter_markdown_plus_latex（LaTeX 公式）+ flutter_mermaid（流程图/时序图）
  - get_storage 做本地会话持久化， flutter_dotenv 管理 API Key
  - 多端自适应：窄屏单栏，≥750px 自动切桌面/宽屏布局
  - Flutter 3.32+ 需手动设置 `systemNavigationBarColor: Colors.transparent` 修复底部导航栏黑色问题
- **适用判断**：适合个人开发者构建跨端 AI 对话客户端；理解流式状态管理（Obx 监听消息列表）是核心难点

## 关联连接
- [[Dio]] — 标配 HTTP 客户端，承担 SSE 流式请求
- [[SSE流式输出]] — 流式对话的传输机制
- [[DeepSeek-V4.1-Flash]] — 实测接入的大模型
- [[摘要-flutter-dio-deepseek-sse]] — 来源（流式对话 App 实战）
- [[Google]] — 出品公司
