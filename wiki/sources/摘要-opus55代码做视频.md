---
title: "摘要-opus55代码做视频"
type: source
tags: [来源, 原始文件, 视频, Claude, 代码生成]
sources: [raw/01-articles/2026-10-02-用 Claude Opus 5.5 做视频堪称一绝，外网已经玩疯了。.md]
last_updated: 2026-10-08
---

## 核心摘要
外网爆火的"用 Claude Opus 5.5 做视频"并非 Seedance 式视频生成模型，而是让 Claude Code、Codex 等 Agent 工具**编写 HTML、Canvas、WebGL 或 Remotion 动画，再逐帧导出 MP4**——字幕、镜头路径、转场全部在代码里调。典型玩法：单个 HTML 页面用时间参数计算每帧元素位置，Playwright 截屏 + FFmpeg 合成；Three.js 实时渲染三维场景做一镜到底（如镜头钻进 Blackwell 芯片）；Canvas 逐帧手绘短片、剪纸风科普片、五分钟 WebGL 历史电影。文章整理 10 支成品（28 秒手绘短片、按钮变形界面片、鸡尾酒调制动画、250 年美国沙画、推理公司介绍片、Replit 产品歌、奥斯特里茨战役电影、相对论科普、浏览器工作原理图解等）与 5 个开源项目：Lemo-Opuscar（39 种影片风格 Skill）、Awesome-Opus5-5-Videos（301 个视频、作者花费 3000 美元、全套 Prompt 开源）、opus-video-prompts 提示词合集、OneTake（一镜到底动作拆解 + Skill）、以及老牌的 HyperFrames 与 Remotion 官方 Agent Skills。

## 关联连接
- [[Opus]] — 所用模型（Opus 5.5）
- [[代码做视频]] — 该文提炼的核心概念
- [[ClaudeCode]] — 主要用到的 Agent 工具
- [[Codex]] — 同类 Agent 工具
- [[Remotion]] — React 代码视频框架（官方 Agent Skills）
- [[HyperFrames]] — HTML 动画渲染成视频的框架
- [[AI视频生成]] — 对照的另一条技术路线（视频生成模型）
