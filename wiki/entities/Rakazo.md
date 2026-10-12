---
title: "Rakazo"
type: entity
tags: [开源, PersonalAgent, GitHub, Agent]
sources: [raw/01-articles/2026-10-09 - 3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。.md]
last_updated: 2026-10-12
---

## 定义
Rakazo 是 [[GrokBot]]（Grok Bot）的开源平替，可搭建持续运行的 AI Bot：每个 Bot 都有自己的对话、记忆、例行任务和工作历史，连接模型后再配置一套执行任务用的电脑环境即可工作。

## 关键信息
- **执行环境**：Bot 可使用浏览器、终端、文件和图形桌面，能在网页查资料、保存文件、运行命令处理工作；实际能用哪些工具取决于连接的服务与授予的权限
- **多 Bot 分工**：支持创建多个 Bot 分工协作，一个 Bot 可把任务交给其他 Bot，或临时创建子 Agent 处理其中一部分（如一个查资料、另一个接着写作）
- **电脑隔离策略**：多个 Bot 可共用团队电脑，也可各自使用隔离的私有电脑
- **入口与交互**：提供网页、桌面和移动端入口，支持语音交互；模型和电脑服务可自行选择，整套服务可本地运行也可连接外部电脑服务
- **常驻运行**：后端放在持续运行的服务器上，Bot 可继续工作，用户从手机或电脑连接查看
- **开源地址**：github.com/elie222/rakazo；文中同时提到另一 Grok Bot 开源平替 OpenMausBot（github.com/milind-soni/OpenMausBot）

## 关联连接
- [[摘要-personal-agent-open-source-alternatives]] — 来源
- [[GrokBot]] — 被平替的闭源产品
- [[OpenMuse]] — 同文介绍的 Muse 开源平替
- [[OpenDots]] — 同文介绍的 Dots 开源平替
- [[personal-ai-agent]] — 所属赛道
- [[Subagent]] — 多 Bot 分工中的子 Agent 机制
