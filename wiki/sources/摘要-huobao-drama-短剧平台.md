---
title: "摘要-huobao-drama-短剧平台"
type: source
tags: [来源, 原始文件, AI短剧, 多Agent, 开源项目]
sources: [raw/09-archive/开源项目｜Star16.3k一站式AI短剧生成平台.md]
last_updated: 2026-10-20
---

## 核心摘要
火宝短剧（huobao-drama，16.3k Star）是把剧本、角色、分镜串成一条视频生产线的一站式 AI 短剧生成平台。架构分四块：frontend/（Nuxt 3 + Vue 3）、backend/（Hono + Drizzle + Mastra + SQLite）、backend/workspace/skills/（Agent 技能）、desktop/（Electron）。内置四个 Mastra Agent 各管一段：script_rewriter（小说改剧本）、extractor（角色/场景/道具提取去重）、storyboard_breaker（拆分镜）、prompt_generator（写图片视频提示词），无独立配音 Agent（声音随视频模型产出）。模型全部外接不自训：文本走 OpenAI 兼容接口/Gemini，视频用火山 Seedance 2.0、MiniMax H3、阿里云百炼 Wan 3.0。从小说到成片六步工作流：建项目→配 AI 服务→剧本→资产参考图→分镜视频→FFmpeg 拼接导出。许可证 CC BY-NC-SA 4.0 禁止商用，生成需付第三方模型调用费。

## 关联连接
- [[HuobaoDrama]] — 火宝短剧平台实体
- [[Mastra]] — 后端 Agent 框架
- [[AI漫剧工作流]] — 相关工作流概念
- [[VideoGeneration]] — 视频生成技术
- [[IT码徒]] — 来源公众号
