---
title: "Codex"
type: entity
tags: [AI工具, Agent, OpenAI]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md]
last_updated: 2026-05-19
---

## 定义
OpenAI 推出的桌面端 AI Agent 程序，从编程 Agent 起家逐步走向通用 Agent，需要 ChatGPT 账号使用。

## 关键信息

### 核心能力
1. **本地文件操作**：可自主读写操作本地文件，不限数量，项目对应本地文件夹
2. **命令行工具使用**：授权后可执行终端命令，安装软件、部署环境
3. **持久记忆**：全局/项目级 agents.md + 自动记忆（实验性）
4. **图片生成**：内置 image2 模型生图能力
5. **插件系统**：Browser Use、Computer Use、Chrome 等操控类插件；Vercel/Netlify 部署插件
6. **Skill 流程沉淀**：可复用的方法、流程和工具组合
7. **MCP 外部服务连接**：对接 NotebookLM 等外部服务
8. **自动化定时任务**：结合 Skill 实现定点执行

### 与 Claude Code 对比
- Claude Code 先发了 Skill、MCP、Hook、远程操控等功能
- Codex 后来居上，新增浏览器操控、Computer Use、image2 生图、手机端操控
- Codex 额度更友好，产品体验更直观（上下文余量可视、额度状态显示）
- Claude Code 写作和规划能力更强（Opus 模型）

### 权限模式
- 自动审查模式（默认）
- 建议模式
- 手动确认模式

### 独有特性
- 手机远程操控（ChatGPT 手机端→电脑端 Codex）
- 内置预览浏览器（可批注元素给修改意见）
- Fork 分叉（从历史节点重新开对话）
- 桌面宠物

## 关联连接
- [[摘要-40分钟学会Codex零基础教程]] — 来源
- [[ClaudeCode]] — 对标产品
- [[OpenAI]] — 所属公司
- [[Agent]] — 核心概念
- [[Skill]] — 技能扩展
- [[MCP]] — 外部服务协议
