---
title: "OpenDots"
type: entity
tags: [开源, PersonalAgent, GitHub, Agent]
sources: [raw/01-articles/2026-10-09 - 3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。.md]
last_updated: 2026-10-12
---

## 定义
OpenDots 是 OpenAI [[Dots]] 的开源平替，用于搭建拥有多个专业助手（Dot）的 AI 工作台；基于 CopilotKit 和 AG-UI 构建，目前是早期的单用户模板。

## 关键信息
- **多专业助手**：每个 Dot 可设置自己的名字、职责、工作要求和工具权限（如研究助手、写作助手），并决定它们能访问哪些工作空间
- **独立执行环境**：接好电脑服务后，每个 Dot 可有自己的浏览器、工作文件和终端，浏览器环境和文件在电脑停止、重启后仍保留；操作记录、命令输出可查看，也可接管浏览器——这些能力按助手分别授权
- **Space/Page 工作空间**：成果可放进 Space（按项目组织文档的工作区），保存后的 Page 是可继续编辑的文档；可要求助手先交草稿、通过审核确认后再保存，文档可手动改或让助手继续修改
- **协作能力**：支持周期任务、语音通话和 Slack 接入；后台任务在原对话里运行，配置 Slack 后可在消息线程中继续交流
- **部署形态**：Alpha/早期单用户模板，聊天需连接 Intelligence 和模型服务，电脑、语音及 Slack 需分别配置
- **开源地址**：github.com/CopilotKit/OpenDots；文中另提到其他开发者开源的 open-dots（github.com/Anil-matcha/open-dots）

## 关联连接
- [[摘要-personal-agent-open-source-alternatives]] — 来源
- [[Dots]] — 被平替的 OpenAI 产品
- [[OpenMuse]] — 同门开源项目（CopilotKit 出品）
- [[Rakazo]] — 同文介绍的 Grok Bot 开源平替
- [[personal-ai-agent]] — 所属赛道
- [[WorkBuddy]] — 同类多助手工作台产品
