---
title: "Astra"
type: entity
tags: [大模型, GPT-6, OpenAI, 模型版本]
sources: [raw/01-articles/2026-10-10-Claude、GPT“跨界”做视频，Seedance们的护城河还牢吗？.md]
last_updated: 2026-10-12
---

Astra 是 [[GPT-6]] 的旗舰版本代号，在本知识库多篇 GPT-6 相关资料中作为核心模型被讨论（[[摘要-OpenAI总裁Brockman最新采访]] 中称其为「GPT-6 Astra」）。[[摘要-gpt6-自训练信号]] 记载其网络安全能力评测触及 Critical 阈值。

## AI 导演角色（2026-09-10 跨界做视频）
- 9 月 3 日发布，官方定位新一代通用智能体模型，对 [[Blender]]、Unreal Engine 等三维创作软件的操作能力成为其切入视频创作的关键支点
- **"导演+制片"路线**：不直接生成画面，先完成创意规划、空间设计与镜头调度，再交 [[Seedance]] 2.5 等专业视频模型渲染——Higgsfield AI 一镜到底测试中先在 Blender 用几何体搭白模、规划走位与运镜路线，缓解了 AI 视频的空间错乱与穿模问题（详见 [[3D运镜预演]]）
- **世界模型与 3D 空间理解**：能理解相连空间的拓扑关系、人物走位逻辑与摄像机运动路径；空间布局、人物调度、摄像机路线可留存复用，创意变成可修改、可复用的资产
- **专业软件接入**：DaVinci Resolve 21.1（9-8）上线原生 MCP 服务器后，Astra 可直接操作剪辑软件，将 75 分钟素材输出含 96 个剪辑片段、字幕、调色与音量校准的 22 分钟粗剪；创作者工作流如仙侠剧本→Astra 拆分镜→Seedance 2.5 生成 90 秒成片
- 与 [[Claude]] Opus 5.5 的 [[代码做视频]]（Vibe Video）路线构成交错竞争的两条跨界路线，详见 [[摘要-claude-gpt-video-seedance-moat]]

## 关联连接
- [[AGI]] — 来源（死链修复）
- [[ComputerUse]] — 来源（死链修复）
- [[GregBrockman]] — 来源（死链修复）
- [[NavierStokes]] — 来源（死链修复）
- [[OpenAI]] — 来源（死链修复）
- [[摘要-gpt6-自训练信号]] — 来源（死链修复）
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源（死链修复）
- [[GPT-6]] — 所属模型
- [[摘要-claude-gpt-video-seedance-moat]] — AI 导演跨界做视频来源
- [[Seedance]] — 被其调度的下游渲染模型
- [[Blender]] — 白模预演工具
- [[3D运镜预演]] — 其视频规划工作流所属概念
