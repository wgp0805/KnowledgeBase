---
title: "摘要-openbot多agent窗口"
type: source
tags: [来源, 原始文件, OpenBot, 多Agent, 桌面应用]
sources: [raw/09-archive/一个窗口同时跑 Codex、Claude、Cursor ，还能互相派活，这个 GitHub 项目火了！！.md]
last_updated: 2026-11-03
---

## 核心摘要

冰河（冰v河，2026-11-03）介绍 **OpenBot**（nightly-labs/openbot）——同时跑多个 AI 编程 CLI 的桌面应用，解决"Codex 开一个终端、Claude Code 开另一个、Cursor CLI 再开一个，彼此不通气、会话一关记录就散"的割裂状态。

**核心定位**：不提供模型，只负责调度本机已有的 CLI。原生支持 Codex 和 Claude Code；Grok CLI、OpenCode、Gemini、Cursor CLI、Cline CLI 通过 **ACP 协议**接入；本机 Ollama/LM Studio 自动识别可用本地模型。每个 agent 独立配置：名字、头像、指令、工作目录、对话记录分开保存，应用重开仍在；模型按 agent 单独设置，推理档位/供应商可不同，中途换供应商工作区与对话保留。

**工作区与持久化**：agent 文件在 `~/OpenBot/Agents/<agent-id>`，共享文件走 `~/OpenBot/Shared`（带清单与校验值）；对话与任务队列存本地 SQLite；任务队列 FIFO，可暂停/恢复/取消，崩溃重开不丢。

**agent 间协作**：两个 agent 能直接发消息、回表情、传文件（查完资料直接发给写代码的 agent，不需人转手）；**频道（Channel）**= 多 agent 公共聊天区，一个任务同一时间只有一个负责人，可指定交给谁，有 Stop/Resume/Reassign/Archive 操作。

**附加能力**：内置浏览器（agent 开网页看内容操作页面）；可选 Computer Use（macOS/Win/Linux，macOS 需屏幕录制+辅助功能权限）；对话接近上下文上限自动压缩；常用流程可存 skill 进本地技能库供其他 agent 安装。

**手机端与服务器模式**：iPhone/Android 客户端连自己电脑（电脑得开着），或装到常开服务器（一键脚本 + Docker 镜像）用手机/网页端连接。

**三件注意事项**：① 权限放很大——开发预览版 agent 跑在 `danger-full-access` 模式，同意后不再逐项询问，建议先备用机/虚拟机/Docker 试用；② 许可证有边界——PolyForm Noncommercial 1.0.0，个人/非商用免费，商用需购买授权，0.1.11 之前旧版是 Apache-2.0；③ 本地优先≠完全离线——用云端模型时对话仍发往 OpenAI/Anthropic/xAI，想彻底离线接 Ollama 本地模型。

## 关联连接
- [[OpenBot]] — 本文主角实体
- [[ACP]] — 接入协议（Grok/OpenCode/Gemini/Cursor/Cline 走 ACP）
- [[multi-agent-collaboration]] — 多 Agent 协作上位概念
- [[Codex]] — 原生支持之一
- [[ClaudeCode]] — 原生支持之一
- [[Cursor]] — 通过 ACP 接入
- [[冰河]] — 作者
- [[Ollama]] — 本地模型自动识别
- LM Studio — 本地模型自动识别（无独立页，纯文本标注）
- [[权限模式]] — danger-full-access 对比
- [[ComputerUse]] — 附加能力之一
- [[上下文压缩]] — 自动压缩机制
- [[Skill]] — 本地技能库
