---
title: "PaiCLI"
type: entity
tags: [AI, CLI工具, 项目]
sources: [raw/01-articles/AI agent工具应该怎么使用.md]
last_updated: 2026-06-08
---

## 定义
PaiCLI 是开发者"二哥"（二师兄）基于 Codex 开发的 CLI 命令行项目，集成了阿里云 OCR 等 AI 能力，作为 Codex 实战开发的典型案例。

## 关键信息
- 开发方式：全程使用 Codex 进行 AI 辅助编程
- 集成了阿里云 OCR 服务（通过 .env 中 ALIYUN_OCR_ENABLED 全局开关控制）
- 使用 JLine 交互库实现命令行交互界面
- 多模型协作开发流程：Claude Code 做需求拆解和审查，Codex 负责执行实现
- 每个功能均让 Codex 生成测试用例

## 关联连接
- [[Codex]] — 核心开发工具
- [[ClaudeCode]] — 代码审查工具
- [[PaiAgent]] — 同作者的 AI Agent 平台项目
- [[摘要-AI-agent工具应该怎么使用]] — 来源
