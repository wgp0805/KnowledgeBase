---
title: "Octop"
type: entity
tags: [开源项目, 腾讯, AI助手, 自部署, WorkBuddy]
sources: [raw/09-archive/2026-11-12 - 夯爆了！腾讯甩出 "开源版 WorkBuddy".md]
last_updated: 2026-11-16
---

## 定义
Octop 是腾讯云开源的自部署 AI 助手（GitHub 11.9K Star，github.com/TencentCloud/Octop），可装在个人电脑、NAS 或云服务器上，社区俗称"开源版 [[WorkBuddy]]"。软件免费，模型自接（腾讯云、OpenAI、[[DeepSeek]]、[[Ollama]] 预设，费用由模型服务商结算）。

## 关键信息
- **与 WorkBuddy 的关系**：两者都是腾讯云 AI Agent——WorkBuddy 是登录即用的闭源成品（模型算力在云上）；Octop 面向个人、家庭和小团队，强调开源、自己部署、数据留在本机。两类人群：不想折腾安装和密钥的用 WorkBuddy；希望对话/文件/密钥都留在自己机器上的选 Octop
- **多端对话**：网页 + 飞书、微信、钉钉、企业微信、QQ、Telegram 均可聊；一套部署开多账号（家里一人一个/小团队一人一个）
- **专家体系**：每账号下养多位专家（写周报的、看服务器的、陪孩子记疫苗的），各干各的、记忆和文件分开；内置专家模板一键安装，16 种 MBTI 人格模板可换说话风格
- **连接器与知识库**：连接器是授权过一次的应用（腾讯文档、腾讯会议、邮箱、Notion），用大白话吩咐；知识库接收 PDF/Word/表格，回答标注引用段落。飞书只负责传话，查会议/翻方案是专家自己去干
- **双向 ACP**：`octop acp --agent main` 让 Zed、[[OpenCode]] 等 ACP 工具调用本机专家；反向在 Octop 网页 ACP 里接 [[OpenCode]]、[[ClaudeCode]]、[[CodeBuddy]] 把编码活交出去，危险操作先停下等用户点头
- **定时任务**：白话创建（"每天早上发一条待办"），到点自动开口执行
- **数据本机化**：对话、专家工作区、密钥默认在 `~/.octop/`（config.json 端口配置 / octop.db 用户专家通道任务 / secrets 密钥 / agents 各专家文件记忆）；默认 SQLite，人多可换 PostgreSQL；中间无 Redis 无额外服务；迁移先跑 `octop backup`
- **安装**：Windows PowerShell `irm ...install.ps1 | iex` 或 macOS/Linux `curl -fsSL ...install.sh | bash`，随后 `octop init`（设管理员，密码至少 8 位含字母数字）+ `octop run`，浏览器开 127.0.0.1:8088；服务器场景走 Docker（ghcr.nju.edu.cn/tencentcloud/octop 镜像），数据卷挂出容器删了数据还在；安装器自带 Python 3.12 放 `~/.octop/` 不动系统 Python；密钥可写 `~/.octop/env`

## 关联连接
- [[WorkBuddy]] — 同门闭源成品对照
- [[腾讯]] — 出品方（腾讯云）
- [[ACP]] — 双向接入协议
- [[ClaudeCode]] / [[OpenCode]] / [[CodeBuddy]] — 可反向接入的编码工具
- [[Ollama]] / [[DeepSeek]] / [[OpenAI]] — 可自接的模型
- [[PostgreSQL]] — 可升级的数据存储
- [[锋哥]] — 来源作者
- [[摘要-octop开源版workbuddy]] — 来源
