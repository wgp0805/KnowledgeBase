---
title: "oh-story-dsh"
type: entity
tags: [开源项目, DeepSeekHarness, 插件, 创作工具, 小说, 短剧]
sources: [raw/09-archive/一个神级DeepSeek插件，写小说做短剧改游戏，一个插件全包！.md]
last_updated: 2026-11-19
---

## 定义
oh-story-dsh 是 [[DeepSeekHarness]] 的社区创作插件（开源仓库 zenstory-ai/oh-story-dsh），内置四套固定版本创作技能包与配套图形工作台：**小说**（14 Skills + 7 专业角色）、**短剧**（12 Skills）、**互动游戏**（5 Skills）、**视频解说**（2 Skills）。装完后 DSH 中新增小说、短剧、互动游戏、视频解说四个创作工作台；Agent、会话、模型配置、权限审批全部沿用 DSH 原生机制。

## 关键信息

### 工程化特性
- 产物全是本地文件：普通 Markdown、JSON 和媒体文件，AI 每改一笔都落在本地目录
- **按需显形**：平时打开写代码的仓库不露面，目录里存在创作工程时工作台才展开
- 不越界：番茄小说建书资料只整理用户确认过的内容存成文件，不替用户登录后台发布

### 四个工作台
| 工作台 | 核心机制 | 亮点 |
| --- | --- | --- |
| 小说 | 三栏界面（文件树 + Markdown 编辑器 + DSH 对话），Agent 写稿编辑器实时跟随 | 「追踪/上下文.md」持续维护章节进度、未回收伏笔与连贯性风险（如 F016 伏笔记录）；功能覆盖选题/扫榜/拆文/长短篇连载/审稿/去 AI 味/封面提示词 |
| 短剧 | 每集五份文档：剧本/视觉设定/分镜/图片提示词/视频提示词 | 「连戏锁」把跨镜头不能变的造型钉死成锁定词原样贴进每个镜头提示词；无限画布管理场次/参考板/关键帧/片段；「制作详情」自动查断链并报文件名行号 |
| 互动游戏 | 试玩/创作画布/文稿三视角，构建直接在沙箱运行 | 试玩进度不因切视图/收起对话中断，新版由用户决定何时载入；入口 `/novel-to-game quick`，产物在 game-adaptations 目录 |
| 视频解说 | 拆剪现成视频 → 分段解说词 → 配音 → 烧字幕 | 解说词逐段修改不重配已配音段落；sources/work/outputs 目录分明；ffmpeg 带 libass 烧字幕否则给外挂 SRT |

### 安装与依赖
```bash
npx -y --package pnpm@11.7.0 --package @deepseek-ai/dsh@0.2.2-rc.1 dsh plugin --profile web add @oh-story/dsh@0.1.26 && npx -y @deepseek-ai/dsh@0.2.2-rc.1 web
```
- 基础要求：Node.js 24.9+；纯文字任务（小说/互动游戏设计）只需模型 Key（拆文/导入旧稿/追踪需 Python 3）
- 媒体流水线按需配置：短剧出图 GPT Image 2 Key；短剧视频 Seedance（火山方舟）或 MiniMax H3 Key；配音 MiniMax Key；成片合成 Python 3.9+/ffmpeg；视频解说 Python 3.10+/ffmpeg/MIMO_API_KEY（Fish Audio 配音加 FISH_API_KEY）；缺哪个「制作详情」直接提示对应环境变量
- **Claude Code / Codex 用户替代方案**：同 GitHub 组织的四个独立技能包——oh-story-claudecode（小说）、drama-skills（短剧）、novel-to-game（游戏）、video-recap-skills（视频解说）

### 评价
- 核心价值：在熟悉的 DSH 里直接获得四个创作工作台，工具与习惯零迁移；产物全本地文件解决"聊天窗口写连载，聊几十轮失忆、二十章后没法用"的痛点
- 局限：完整短剧/视频流水线依赖项多（Python/ffmpeg/多家媒体 Key），对纯小白有门槛，不算开箱即用

## 关联连接
- [[摘要-oh-story-dsh创作插件]] — 来源
- [[DeepSeekHarness]] — 宿主平台
- [[插件生态]] — DSH 插件生态
- [[ClaudeCode]] — 同源技能包适配的 Agent
- [[Codex]] — 同源技能包适配的 Agent
