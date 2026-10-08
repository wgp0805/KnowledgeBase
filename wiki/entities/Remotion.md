---
title: "Remotion"
type: entity
tags: [视频生成, React, 代码化, 开源框架]
sources:
  - wiki/syntheses/opencode-video-generation-paths.md
  - raw/01-articles/2026-10-02-用 Claude Opus 5.5 做视频堪称一绝，外网已经玩疯了。.md
last_updated: 2026-10-08
---

## 定义
Remotion 是用 React + TypeScript 以代码方式生成视频的开源框架。核心理念是"组件即帧"——视频的每一帧由 React 组件渲染，最终导出为 MP4/WebM。让视频可编程、可版本控制、可参数化。

## 关键信息
- **组件即帧**：用 `useCurrentFrame()` 驱动动画，时间轴即 React 状态
- **渲染管线**：headless Chromium 逐帧截图 → ffmpeg 合成
- **优势**：视频可代码化、可复用组件、可参数化批量生成
- **与 AI 结合**：可作为 AI Agent 的视频输出通道，用代码生成视频而非调用视频模型
- **在 [[opencode-video-generation-paths]] 中**：是 bash+Remotion 方案的核心
- **官方 Agent Skills（2026-10）**：github.com/remotion-dev/skills 是 GitHub 上让 AI 通过 Coding 方式做视频的高赞项目之一，教 Agent 用 React 代码制作、预览和导出视频；与 [[HyperFrames]] 并列为两个老牌方案（详见 [[摘要-opus55代码做视频]]、[[代码做视频]]）

## 关联连接
- [[opencode-video-generation-paths]] — 提及本框架的视频生成方案来源
- [[HyperFrames]] — 同类代码化视频框架
- [[代码做视频]] — 本框架所服务的视频生产路线
- [[摘要-opus55代码做视频]] — 来源（Opus 5.5 做视频热潮）
