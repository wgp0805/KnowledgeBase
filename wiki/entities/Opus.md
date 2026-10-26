---
title: "Opus"
type: entity
tags: ["Anthropic", "模型"]
sources: [raw/09-archive/2026-09-24-A社O社，坐不住了.md, raw/01-articles/2026-10-02-用 Claude Opus 5.5 做视频堪称一绝，外网已经玩疯了。.md]
last_updated: 2026-10-08
---

# Opus

Opus 是 Anthropic 的旗舰模型系列，Opus 4.7 曾是 2026 年的最新版本；2026-09-22 发布 **Opus 5.5**，位于 Claude 架构的模型层，是 Agent 的推理引擎。

## Opus 5.5（2026-09-22）
- **定价**：输入/输出每百万 token 4/20 美元，比 Opus 5 低 20%；完成任务用的 token 更少，典型任务整体成本比 Opus 5 低约 40%
- **性能**：Anthropic 公布的 9 项基准测试中超过三周前发布的 [[Fable 5.1]]，标价仅其四成（官方提醒实际使用差距比跑分小）；提升集中在编程、智能体、计算机使用、数学与科学推理
- **发布背景**：约一个半小时后 OpenAI 推出 GPT-6 Sol/Luna 应战，构成 [[大模型价格战]]（详见 [[摘要-a社o社价格战]]）

## Opus 5.5 做视频走红（2026-10-02，详见 [[摘要-opus55代码做视频]]）
- 外网爆火玩法**不是**调视频生成模型，而是让 [[ClaudeCode]]、[[Codex]] 用 Opus 5.5 编写 HTML/Canvas/WebGL/[[Remotion]] 动画，Playwright 截帧 + FFmpeg 导出 MP4，字幕/镜头/转场全在代码里调
- 成品覆盖 28 秒手绘短片、一镜到底钻进 Blackwell 芯片的三维场景、250 年美国沙画、五分钟奥斯特里茨战役电影、剪纸风相对论科普等 10 支
- 开源生态：Lemo-Opuscar（39 种影片风格 Skill）、Awesome-Opus5-5-Videos（301 个视频、作者花费 3000 美元、全套 Prompt 开源）、opus-video-prompts、OneTake、[[Remotion]] 官方 Agent Skills——见 [[代码做视频]]

## 关联连接
[[Anthropic]], [[Claude]], [[Claude-Code]], [[沉默王二]], [[Fable 5.1]], [[GPT-6]], [[大模型价格战]], [[摘要-a社o社价格战]], [[ClaudeCode]], [[代码做视频]], [[摘要-opus55代码做视频]]
