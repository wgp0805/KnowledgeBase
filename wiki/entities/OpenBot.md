---
title: "OpenBot"
type: entity
tags: [开源项目, 多Agent, 桌面应用, AI编程, CLI调度]
sources: [raw/09-archive/一个窗口同时跑 Codex、Claude、Cursor ，还能互相派活，这个 GitHub 项目火了！！.md]
last_updated: 2026-11-03
---

## 定义

OpenBot 是 nightly-labs 开源的**多 AI CLI 调度桌面应用**（GitHub `nightly-labs/openbot`），解决同时开多个 AI 编程工具时的窗口割裂：Codex 开一个终端、Claude Code 开另一个、Cursor CLI 再开一个，彼此不通气、会话一关记录就散。它**不提供模型，只负责调度本机已有的 CLI**，让 agent 之间能互相派活。

## 关键信息

### 接入与角色配置

- 原生支持：**Codex**、**Claude Code**；通过 **ACP 协议**接入：Grok CLI、OpenCode、Gemini、Cursor CLI、Cline CLI
- 本机跑 Ollama / LM Studio 时启动自动识别，本地模型可直接用
- 每个 agent 独立配置：名字、头像、指令、工作目录、对话记录分开保存，应用重开仍在
- 模型按 agent 单独设置，推理档位/供应商可不同；中途换供应商（如 Codex→Claude Code）工作区与对话保留

### 工作区与持久化

- agent 文件：`~/OpenBot/Agents/<agent-id>`；共享文件：`~/OpenBot/Shared`（传输带清单与校验值）
- 对话与任务队列存本地 SQLite，agent 有记忆载体，重开可继续
- 任务队列 FIFO，可暂停/恢复/取消，应用崩溃重开队列不丢

### agent 间协作（核心差异点）

- 两个 agent 可直接发消息、回表情、传文件——查完资料的 agent 直接把结果发给写代码的 agent，不需要人在中间转手
- **频道（Channel）**：多 agent 公共聊天区；一个任务同一时间只有一个负责人，可指定交给谁，有 Stop/Resume/Reassign/Archive 操作

### 附加能力

- 内置浏览器：agent 可开网页、看内容、操作页面
- 可选 Computer Use：macOS/Windows/Linux 都支持（macOS 需屏幕录制 + 辅助功能权限）
- 对话接近上下文上限自动压缩，无需手动清理
- 常用流程可存 skill 进本地技能库，其他 agent 也能安装使用

### 手机端与服务器模式

- iPhone/Android 客户端连自己电脑（电脑需开着）；装到常开服务器（一键脚本 + Docker 镜像）后用手机/网页端连接，实现常在线

### 三件注意事项

1. **权限放得很大**：开发预览版 agent 跑在 `danger-full-access` 模式，首次同意后读写文件/执行命令/上网/操作浏览器不再逐项询问——建议先备用机/虚拟机/Docker 试用，别直接上主力机
2. **许可证有边界**：PolyForm Noncommercial 1.0.0——个人/非商用免费，商用需购买授权；0.1.11 之前旧版为 Apache-2.0，公司使用需先确认
3. **本地优先 ≠ 完全离线**：数据在本地，但用云端模型时对话仍发给 OpenAI/Anthropic/xAI；想彻底不联网须接 Ollama 等本地模型

## 关联连接
- [[摘要-openbot多agent窗口]] — 来源
- [[ACP]] — 接入协议（Grok/OpenCode/Gemini/Cursor/Cline）
- [[multi-agent-collaboration]] — 多 Agent 协作上位概念
- [[Codex]] — 原生支持之一
- [[ClaudeCode]] — 原生支持之一
- [[Cursor]] — 通过 ACP 接入
- [[冰河]] — 介绍作者
- [[Ollama]] — 本地模型自动识别
- [[权限模式]] — danger-full-access 对照
- [[ComputerUse]] — 附加能力之一
- [[上下文压缩]] — 自动压缩机制
- [[Skill]] — 本地技能库
- [[Paperclip]] — 同类多 Agent 编排工具（公司模式对照）
