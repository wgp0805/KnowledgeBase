---
title: "摘要-dsh官方点名4个神级插件"
type: source
tags: [来源, DeepSeekHarness, 插件, 沉默王二]
sources: [raw/09-archive/官方点名，DeepSeek Harness 的 4 个神级插件。.md]
last_updated: 2026-11-16
---

## 核心摘要
沉默王二 2026-11-12 盘点 DeepSeek Harness 官方点名的 4 个插件（当时官方 API 日活 154 万、第三方插件 3.5 万个），外加作者自研一个，共五个：①**dsh-media-desk 自媒体工作台**（科技博主"蜗牛的科技笔记"）——侧边栏独立工作台，灵感墙/内容四态管理（灵感/成稿/待发布/已发布）/发布排期日历/数据复盘导出 Skill/15 种预设风格卡，一键成稿出标题+口播正文+分镜脚本，生图需自配 OpenAI 兼容 API Key；②**dsh-guizang-design 归藏设计**——五个内容生成 Skill（`/guizang-ppt-skill` 网页 PPT、`/guizang-page-skill` 杂志/瑞士风网页排版、`/humanizer-zh` 去 AI 味、`/guizang-voice` 语气档案）+ 统一配色排版规范打包，6 套杂志风 + 4 套瑞士风主题；③**dsh-context 上下文洞察**（Bowen）——把 Token 花在哪逐项列出：全局洞察页（7 天计费 Token/8 周热力图）、单会话 Context 标签页（Token 构成/请求变化/读写文件与命令）、Fleet 标签页（主/子 Agent 分工与各自消耗）、`/context` 命令弹窗速查；④**agentero-dsh 论文阅读**（Phil-Fan 团队）——把本地存储的科研工具 Agentero 接进 DSH，四模块（客户端通信/文献库/笔记/PDF 阅读器），需 Node ≥ 24.9.0 + Agentero CLI + 绑定本地知识库目录；⑤**paiwarp-dsh 自动化终端**（沉默王二自研，github.com/itwanger/paiwarp-dsh）——自然语言驱动 DSH 打开本机真实终端逐步输入命令/读屏幕输出/查退出码，自动存 PNG 截图与 MP4 录屏到 `.paiwarp/runs/`，支持"接管键盘"人机切换（Codex/Claude Code/DSH 原生都没有 terminal use）。总结判断：DeepSeek Harness 可被定制成任何想要的样子，"Agent 时代的操作系统"。内容已并入 [[DeepSeekHarness]] 与 [[插件生态]]。

## 关联连接
- [[DeepSeekHarness]] — 宿主框架（增量更新官方点名章节）
- [[插件生态]] — 生态概念页（增量更新规模数据）
- [[everything-is-a-plugin]] — 架构理念
- [[沉默王二]] — 来源作者 + paiwarp-dsh 作者
- [[ModLens]] — 早期必装插件对照
- Playwright / FFmpeg — paiwarp-dsh 依赖的自动化与录屏底座（无独立页，纯文本标注）
