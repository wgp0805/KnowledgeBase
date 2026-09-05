---
title: "Remotion"
type: entity
tags: [视频生成, React, 代码化, 开源框架]
sources:
  - wiki/syntheses/opencode-video-generation-paths.md
last_updated: 2026-08-13
---

## 定义
Remotion 是用 React + TypeScript 以代码方式生成视频的开源框架。核心理念是"组件即帧"——视频的每一帧由 React 组件渲染，最终导出为 MP4/WebM。让视频可编程、可版本控制、可参数化。

## 关键信息
- **组件即帧**：用 `useCurrentFrame()` 驱动动画，时间轴即 React 状态
- **渲染管线**：headless Chromium 逐帧截图 → ffmpeg 合成
- **优势**：视频可代码化、可复用组件、可参数化批量生成
- **与 AI 结合**：可作为 AI Agent 的视频输出通道，用代码生成视频而非调用视频模型
- **在 [[opencode-video-generation-paths]] 中**：是 bash+Remotion 方案的核心

## 关联连接
- [[opencode-video-generation-paths]] — 提及本框架的视频生成方案来源
- [[HyperFrames]] — 同类代码化视频框架
