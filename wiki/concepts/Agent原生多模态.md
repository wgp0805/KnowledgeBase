---
title: "Agent原生多模态"
type: concept
tags: [概念, Agent, 多模态, AI架构]
sources: [raw/01-articles/阿里又开源了一个神级Skill项目！.md]
last_updated: 2026-08-14
---

## 定义

Agent 原生多模态是一种 AI 技能设计理念：将多模态能力（文本、图像、视频、语音、视觉理解）打包成标准 Agent Skills，由 Agent 自身负责选模型、调参数、处理报错，用户只需用自然语言提需求，无需关心 API 调用细节和 SDK 对接。

## 关键信息

### 与传统多模态 API 调用的区别
- **传统方式**：开发者需手动选择模型、拼接 API 参数、处理报错和重试，体验割裂（需切出 Agent 手动操作）
- **Agent 原生方式**：Agent 自动完成模型选择、参数配置、错误处理，用户在对话框里说一句需求即可

### 核心特征
1. **模型路由自动化**：Agent 根据任务类型自动选择合适模型（如图片生成选 wan2.6-t2i，语音选 qwen3-tts-instruct-flash）
2. **零 SDK 对接**：一行命令安装即用，无需编写 API 调用代码
3. **能力补齐**：可为不支持某模态的模型补齐短板（如通过 /qianwen-vision 让纯文本模型识别图片）
4. **技能标准化**：每个能力封装为标准 Agent Skill，适配多种支持 Agent Skills 的智能体

### 代表项目
- [[QianWen-AI]]：阿里开源的 8 技能多模态包，是这一理念的典型实践

## 关联连接
- [[QianWen-AI]] — 代表实践项目
- [[摘要-阿里开源qianwen-ai-skill项目]] — 来源
- [[Skill]] — Agent Skills 概念
- [[多模态大模型]] — 多模态模型类别
- [[Agent]] — Agent 核心概念
