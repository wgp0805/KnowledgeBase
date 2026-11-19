---
title: "摘要-octop开源版workbuddy"
type: source
tags: [来源, Octop, 腾讯, AI助手, 开源项目]
sources: [raw/09-archive/2026-11-12 - 夯爆了！腾讯甩出 “开源版 WorkBuddy”.md]
last_updated: 2026-11-16
---

## 核心摘要
锋哥（java1234）2026-11-12 介绍腾讯开源 AI 助手 Octop（GitHub 11.9K Star，github.com/TencentCloud/Octop）：可装在自己电脑、NAS 或云服务器的自部署 AI 助手，网页 + 飞书/微信/钉钉/企业微信/QQ/Telegram 均可对话，一套部署可开多账号，每账号下再养多位"专家"（写周报的/看服务器的/记疫苗的），各专家的记忆与文件相互隔离。与 [[WorkBuddy]] 的关系：两者都是腾讯云 AI Agent——WorkBuddy 是开箱即用的闭源成品（模型算力在云上），Octop 面向个人/家庭/小团队强调开源自部署、数据留在本机（对话/专家工作区/密钥默认在 `~/.octop/`，默认 SQLite 可换 PostgreSQL，无需 Redis）。功能对齐 WorkBuddy：专家/技能/连接器（腾讯文档、腾讯会议、邮箱、Notion 授权接入）/知识库（回答标注引用段落）/定时任务（白话创建到点自动执行）/16 种 MBTI 人格模板。双向 ACP 能力：`octop acp --agent main` 让 Zed/OpenCode 等 ACP 工具调用本机专家；也可在 Octop 里反向接 OpenCode/Claude Code/CodeBuddy 把编码活交出去，危险操作先停下等确认。安装：PowerShell/curl 脚本或 Docker（ghcr 镜像），`octop init` 设管理员，模型自接（腾讯云/OpenAI/DeepSeek/Ollama 预设，密钥可写 `~/.octop/env`）。内容已并入 [[Octop]]。

## 关联连接
- [[Octop]] — 本篇主角（新建实体页）
- [[WorkBuddy]] — 同门闭源成品对照（增量更新）
- [[腾讯]] — 出品方
- [[ACP]] — 双向接入协议
- [[ClaudeCode]] / [[OpenCode]] / [[CodeBuddy]] — 可被反向接入的编码工具
- [[Ollama]] / [[DeepSeek]] / [[OpenAI]] — 可自接的模型
- [[锋哥]] — 来源作者
