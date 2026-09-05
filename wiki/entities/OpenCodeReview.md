---
title: "OpenCodeReview"
type: entity
tags: [阿里, 代码审查, Agent, 开源项目]
sources: [raw/01-articles/2026-09-05 - 阿里开源了一个神级Agent项目.md]
last_updated: 2026-09-05
---

## 定义
Open Code Review 是阿里巴巴开源的 AI 代码审查 Agent，源自内部官方 AI 代码审查助手，采用"确定性工程 + LLM Agent"混合架构。

## 关键信息
- 来源：阿里巴巴集团内部，服务数万开发者，识别数百万代码缺陷
- 架构：确定性工程（文件选择/分束/规则匹配/位置定位）+ LLM Agent（动态决策/上下文检索/深度审查）
- 性能：相同模型下精度反超 Claude Code，token 消耗约1/9
- 速度：中等规模 PR 1-3 分钟
- 内置规则：NPE、SQL注入、XSS、线程安全、参数校验、Mapper SQL
- 协议：Apache-2.0
- 安装：`npm install -g @alibaba-group/open-code-review`

## 关联连接
- [[摘要-阿里开源open-code-review]] — 来源
- [[阿里巴巴]] — 开源公司
- [[代码审查]] — Code Review
- [[确定性工程]] — 工程保证确定性
- [[ClaudeCode]] — 对比基准
- [[Apache-2.0协议]] — 开源协议
