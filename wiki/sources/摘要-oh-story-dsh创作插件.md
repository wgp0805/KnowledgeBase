---
title: "摘要-oh-story-dsh创作插件"
type: source
tags: [来源, DeepSeekHarness, 插件, 创作工具, Agent]
sources: [raw/09-archive/一个神级DeepSeek插件，写小说做短剧改游戏，一个插件全包！.md]
last_updated: 2026-11-19
---

## 核心摘要
程序员追风 2026-11-18 文章，介绍 DeepSeek Harness 社区创作插件 [[oh-story-dsh]]（开源仓库 zenstory-ai/oh-story-dsh）：装完后 DSH 里多出四个创作工作台——小说、短剧、互动游戏、视频解说，各配固定版本技能包（小说 14 Skills + 7 角色、短剧 12 Skills、互动游戏 5 个、视频解说 2 个）与图形工作台。产物全部是本地 Markdown/JSON/媒体文件，Agent、会话、模型配置、权限审批沿用 DSH 原生机制，不露面于普通代码仓库，只有目录里存在创作工程才展开工作台。

## 关键要点
- **小说工作台**：三栏界面（文件树 + Markdown 编辑器 + DSH 对话），Agent 写设定/大纲/章节时编辑器实时跟随；功能覆盖选题、扫榜、拆文、长短篇连载、审稿、去 AI 味、番茄小说建书资料与封面提示词；「追踪/上下文.md」由 AI 持续维护章节进度、未回收伏笔与连贯性风险（如"F016：钟嘉嘉的军方家庭背景还没公开，第 7 章埋的，回收章未定"）
- **短剧工作台**：每集五份文档（剧本/视觉设定/分镜/图片提示词/视频提示词）；「连戏锁」把跨镜头不能变的造型钉死成锁定词（如 pine-green lapel service jacket）原样贴进每个相关镜头提示词；无限画布摆剧本场次/角色参考板/分镜关键帧/视频片段；「制作详情」自动查断链并报文件名行号
- **互动游戏工作台**：试玩/创作画布/文稿三视角，构建直接在左侧沙箱运行，试玩进度不因切视图或收起对话中断，新版由用户决定何时载入；入口 `/novel-to-game quick`，产物在 game-adaptations 目录
- **视频解说工作台**：拆剪现成视频 → 写分段解说词 → 配音 → 烧字幕；解说词逐段修改保存不重配已配音段落；原片 sources/中间产物 work/成片 outputs 目录分明；ffmpeg 带 libass 则烧字幕否则给外挂 SRT
- **依赖门槛**：Node.js 24.9+；纯文字任务只要模型 Key（拆文/导入旧稿/追踪需 Python 3）；短剧出图需 GPT Image 2 Key、视频需 Seedance（火山方舟）或 MiniMax H3 Key、配音需 MiniMax Key、合成需 Python 3.9+/ffmpeg；视频解说需 Python 3.10+/ffmpeg/MIMO_API_KEY（Fish Audio 配音再加 FISH_API_KEY）；缺什么「制作详情」会提示对应环境变量
- **Claude Code / Codex 用户**：可装同组织的四个独立技能包 oh-story-claudecode（小说）、drama-skills（短剧）、novel-to-game（游戏）、video-recap-skills（视频解说）
- **作者评价**：最值的是在熟悉的 DSH 里改出四个工作台、工具习惯零迁移；产物全本地文件，解决"聊几十轮就失忆、二十章后没法用"的痛点；但完整短剧/视频流水线依赖多，不算开箱即用

## 关联连接
- [[oh-story-dsh]] — 插件本体
- [[DeepSeekHarness]] — 宿主平台
- [[插件生态]] — DSH 插件生态
- [[ClaudeCode]] — 可装同源技能包的 Agent
- [[Codex]] — 可装同源技能包的 Agent
- [[程序员追风]] — 作者
