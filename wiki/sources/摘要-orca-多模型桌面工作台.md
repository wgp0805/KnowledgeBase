---
title: "摘要-orca-多模型桌面工作台"
type: source
tags: [来源, Orca, 多模型, 桌面端, AI编程]
sources: [raw/01-articles/2026-11-01 - 终于有桌面版了！112k Star，Claude Codex Cursor一个窗口全搞定.md]
last_updated: 2026-11-02
---

## 核心摘要

「我是程序汪」介绍桌面端代码 Agent 工作台 **Orca**（GitHub `stablyai/orca`，112k Star）。定位是代码专用的多模型调度桌面客户端：把 Claude、OpenAI Codex、Cursor 配套模型以及本地 Ollama 模型塞进同一个客户端，统一会话、统一文件上传、统一 API 管理。**Orca 不自带模型权重**，是客户端调度层，所有推理走用户自己的 API Key，流量不经过第三方中转服务器。

解决的痛点：每个代码工具独立入口、上下文隔离（Claude 里喂过架构说明，换 Codex 要重贴）、多 Key 管理麻烦、缺少面向代码的会话管理。

核心能力：

- **多模型一键切换**：同一会话内上一句用 Claude 读大仓库架构、下一句切 Codex 做函数补全、再切别的模型做 review，对话历史、粘贴的代码、上传的文件全部保留。原生针对代码场景优化，支持批量上传多个源码文件/文件夹，自动识别代码语言
- **原生代码库导入**：选择本地项目文件夹导入，自动跳过 `.git`、`node_modules`、`dist`、编译产物；可手动勾选参与对话的文件（如只选 controller、service 层），精准控制上下文
- **代码会话管理**：workspace 工作区概念，按项目分组保存对话、文件、模型配置，换项目直接切工作区
- **输出侧代码块优化**：支持一键复制单块/全部代码；可单独选中某段代码追问（优化、加注释、找 bug、改成异步版本）

安装：Releases 提供 dmg（Mac）、exe（Windows）、AppImage（Linux）；也可源码运行（Tauri + 前端栈，`pnpm install` + `pnpm dev`）。Key 保存在本地配置文件，不上传 Orca 服务器。

适用场景：一次性读整个仓库梳理架构、批量重构一批文件、对比不同模型对同一代码问题的输出、接入本地 Ollama 离线跑代码任务。

不适合：替代 IDE 内实时补全（Cursor、Copilot 更顺手）、实时联动 IDE 自动改本地文件（Orca 没有自动写回能力，代码要手动复制）、追求完全免费（模型调用费用仍是各服务商账单）。

短板：没有自动写入本地文件能力、没有内置 diff 预览、超大仓库导入后手动筛选文件耗时、社区更新节奏偏慢。

## 关联连接
- [[Orca]] — 被介绍的实体
- [[摘要-orca-ade多agent协作]] — 更早的 Orca 来源（另一视角）
- [[Cursor]] — IDE 内嵌的对照工具
- [[ClaudeCode]] / [[Codex]] / [[Ollama]] — 可接入的模型与本地运行时
- [[我是程序汪]] — 文章作者
