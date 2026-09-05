---
title: "QianWen-AI"
type: entity
tags: [阿里, 开源, Agent Skill, 多模态, 通义千问]
sources: [raw/01-articles/阿里又开源了一个神级Skill项目！.md]
last_updated: 2026-08-14
---

## 定义

阿里开源的 Agent 原生多模态 AI 技能包（GitHub: QianWen-AI/qianwen-ai），将通义千问的文本、图像、视频、语音、视觉理解等 8 个能力打包成标准 Agent Skills，可一行命令接入 Claude Code 等支持 Agent Skills 的 AI 编程智能体。

## 关键信息

### 核心亮点
- **Agent 原生**：Agent 帮你选模型、调参数、处理报错，用户只管提需求
- **一行安装**：`npx skills add QianWen-AI/qianwen-ai`，零配置，无需对接 SDK
- **技能齐全**：文本、图像、视频、语音、视觉、模型选择、认证、用量查询，8 个技能全部内置
- **适配广泛**：可接入多种支持 Agent Skills 的 Agent，即装即用

### 安装前提
- 需安装 Node.js 18 以上版本
- 安装时可选目标 AI 编程智能体（如 Claude Code）
- 使用前需通过 `/qianwen-ops-auth` 配置 `DASHSCOPE_API_KEY`（sk- 开头，在千问 AI 平台创建获取）

### 8 个内置技能
| 技能 | 命令 | 说明 |
|------|------|------|
| 认证配置 | `/qianwen-ops-auth` | 创建 .env 配置 API KEY |
| 图片生成 | `/qianwen-image-generation` | 自动选模型（如 wan2.6-t2i） |
| 视觉理解 | `/qianwen-vision` | 图片识别，补齐模型短板 |
| 语音合成 | `/qianwen-audio-tts` | 自动调用 qwen3-tts-instruct-flash |
| 视频生成 | `/qianwen-video-generation` | 自动调用 wan2.6-t2v |
| 文本生成 | `/qianwen-text` | 文本能力 |
| 模型选择 | `/qianwen-model-select` | 模型路由 |
| 用量查询 | `/qianwen-ops-usage` | 查询 API 用量 |

### 实测场景（程序汪 2026-08）
- 图片生成：提示词"画一条青色的龙做吉祥物" → 自动选 wan2.6-t2i 生成
- 图片识别：通过 /qianwen-vision 让不支持图片识别的 Claude Code 模型识别图片
- 语音合成：温暖女声朗读《上学歌》→ 自动调用 qwen3-tts-instruct-flash
- 视频生成：5 秒孙悟空三打白骨精动画 → 自动调用 wan2.6-t2v

## 关联连接
- [[摘要-阿里开源qianwen-ai-skill项目]] — 来源
- [[程序汪]] — 介绍文章作者
- [[ClaudeCode]] — 实测接入的 AI 编程智能体
- [[Qwen]] — 通义千问模型系列
- [[DashScope]] — API Key 所在平台
- [[Skill]] — Agent Skills 概念
- [[Agent原生多模态]] — 核心设计理念
