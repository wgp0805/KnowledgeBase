---
title: "摘要-codex-mcp额度优化邪修方法"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/2026-09-17-分享一个大幅节省Codex额度的邪修方法，不要浪费了你的ChatGPT Pro会员.md]
last_updated: 2026-09-18
---

## 核心摘要
数字生命卡兹克分享的 Codex 额度节省工作流：将服务器封装为只读 MCP Server 插件，接入飞书 OAuth 认证，让 ChatGPT 网页版 GPT-6 Pro 直接读取真实生产数据进行分析规划，再将分析结果"添加到 Codex"由 GPT-6 Astra High 执行开发。该方案利用 GPT-6 Pro 的 200 次/周独立额度（不消耗 Codex 额度），将周额度消耗从 10% 降至 4%，完全合规。核心思路是让 GPT-6 Pro 通过 MCP 协议读取服务器日志和数据库进行数据驱动的架构规划。

## 关联连接
- [[Codex]] — 执行层
- [[GPT-6]] — 规划层模型
- [[MCP]] — 协议连接
- [[AIHOT]] — 作者的 AI 热点资讯产品
