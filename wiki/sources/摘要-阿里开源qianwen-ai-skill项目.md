---
title: "摘要-阿里开源qianwen-ai-skill项目"
type: source
tags: [来源, Agent Skill, 多模态, 阿里, 通义千问]
sources: [raw/01-articles/阿里又开源了一个神级Skill项目！.md]
last_updated: 2026-08-14
---

## 核心摘要

阿里开源的 qianwen-ai 是一套 Agent 原生多模态 AI 技能包，将通义千问的文本、图像、视频、语音、视觉理解等 8 个能力打包成标准 Agent Skills，可一行命令接入 Claude Code 等支持 Agent Skills 的 AI 编程智能体。核心亮点是"Agent 原生"——由 Agent 自动选模型、调参数、处理报错，用户只管提需求，无需对接 SDK。安装命令为 `npx skills add QianWen-AI/qianwen-ai`，使用前需通过 `/qianwen-ops-auth` 配置 `DASHSCOPE_API_KEY`（sk- 开头）。实测覆盖图片生成（wan2.6-t2i）、图片识别（/qianwen-vision，补齐模型不支持图片识别的短板）、语音合成（qwen3-tts-instruct-flash）、视频生成（wan2.6-t2v）等场景。

## 8 个内置技能

| 技能 | 命令 | 说明 |
|------|------|------|
| 认证配置 | `/qianwen-ops-auth` | 创建 .env 配置 DASHSCOPE_API_KEY |
| 图片生成 | `/qianwen-image-generation` | 自动选模型（如 wan2.6-t2i） |
| 视觉理解 | `/qianwen-vision` | 图片识别，补齐模型短板 |
| 语音合成 | `/qianwen-audio-tts` | 自动调用 qwen3-tts-instruct-flash |
| 视频生成 | `/qianwen-video-generation` | 自动调用 wan2.6-t2v |
| 文本生成 | `/qianwen-text` | 文本能力 |
| 模型选择 | `/qianwen-model-select` | 模型路由 |
| 用量查询 | `/qianwen-ops-usage` | 查询 API 用量 |

## 关联连接
- [[QianWen-AI]] — 本文介绍的开源 Skill 项目
- [[程序汪]] — 文章作者
- [[ClaudeCode]] — 实测接入的 AI 编程智能体
- [[Qwen]] — 通义千问模型系列
- [[DashScope]] — API Key 所在平台
- [[Skill]] — Agent Skills 概念
- [[Agent原生多模态]] — 核心设计理念
