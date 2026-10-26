---
title: "HuobaoDrama"
type: entity
tags: [实体, 开源项目, AI短剧, 多Agent]
sources: [raw/09-archive/开源项目｜Star16.3k一站式AI短剧生成平台.md]
last_updated: 2026-10-20
---

## 定义
火宝短剧（huobao-drama）是一款 16.3k Star 的一站式 AI 短剧生成开源平台，把剧本、角色、分镜串成一条从"小说"到"成片"的视频生产线。

## 关键信息
- **架构四块**：`frontend/`（Nuxt 3 + Vue 3 + TypeScript）、`backend/`（Hono + Drizzle + Mastra + SQLite）、`backend/workspace/skills/`（Agent 技能）、`desktop/`（Electron 桌面版），`data/` 存生成素材
- **四个 Mastra Agent 各管一段**：`script_rewriter`（小说改剧本）、`extractor`（角色/场景/道具提取去重）、`storyboard_breaker`（拆分镜）、`prompt_generator`（写图片/视频提示词）；无独立配音 Agent，声音由视频模型随画面产出
- **模型全部外接不自训**：文本走 OpenAI 兼容接口 / Gemini；图片用 OpenAI / Gemini / 火山引擎；视频用火山 Seedance 2.0、MiniMax H3、阿里云百炼 Wan 3.0
- **六步工作流**：创建项目（定宽高比与风格）→ 配 AI 服务 → 剧本改写 → 资产参考图 → 分镜视频 → FFmpeg 拼接导出整集
- **角色一致性靠"攒"**：AI 先生成角色形象与场景参考图，生视频时注入，支持批量生成与图片上传管理
- **部署**：Node.js 20+ / npm 9+ 源码部署（SQLite、FFmpeg 免装）；桌面版腾讯云 COS 镜像双击安装；Docker 镜像 `huobao/huobao-drama:4.0.5`（端口 5679）
- **许可**：CC BY-NC-SA 4.0，禁止商用，商用需作者授权；生成视频需另付第三方模型调用费
- 界面支持中英日韩四语
- GitHub：https://github.com/chatfire-AI/huobao-drama

## 关联连接
- [[摘要-huobao-drama-短剧平台]] — 来源
- [[Mastra]] — 后端 Agent 框架
- [[AI漫剧工作流]] — 所属工作流
- [[VideoGeneration]] — 底层生成技术
- [[IT码徒]] — 来源公众号
