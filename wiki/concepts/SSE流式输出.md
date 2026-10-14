---
title: "SSE流式输出"
type: concept
tags: [LLM, 流式, 前端, 交互体验]
sources: [raw/01-articles/2026-10-12-从 0 到 1：Electron41 + Vite8 + OpenAI SDK 接入 DeepSeek-V4.1-Flash 桌面端AI系统 - yxybox.md]
last_updated: 2026-10-13
---

## 定义
SSE（Server-Sent Events）流式输出是 LLM 对话产品的主流传输方式：服务端按生成进度逐段推送，客户端边收边渲染，用户看到"逐字打出"的效果而非等待完整响应。OpenAI SDK 中通过 `stream: true` 开启。

## 关键信息
- **体验指标**：首字延迟与逐字渲染延迟（案例中 < 100ms）；配打字机动画模拟接近官方客户端的输出质感
- **多轮上下文**：维护 `messages` 数组自动携带历史对话，需自己做上下文窗口管理
- **思维链同流**：解析 `reasoning_content` 字段，让推理过程与正文同步流式输出，用可折叠面板 + 脉冲动画区分"思考中/已思考"
- **渲染层才是主工作量**：Markdown 解析、代码块（highlight.js 按需加载语言包）、KaTeX 公式、Mermaid 图表、图片预览、链接跳转、Sticky 复制按钮
- **本地持久化**：会话列表落盘，重新打开可续接；这也是轻量版"记忆"
- **相关参数**：`temperature`（0.4 偏确定性）、`max_tokens`（未设时非思考模式默认 8K、思考模式 64K）、`thinking` 开关

## 关联连接
- [[Agent上下文管理]] — 上下文窗口管理
- [[短期记忆]] — 会话持久化的记忆属性
- [[摘要-electron41-vite8-deepseek桌面ai]] — 来源
- [[摘要-spring-ai-2-对话记忆实战]] — 服务端流式与记忆实现对照
