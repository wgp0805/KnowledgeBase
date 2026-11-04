---
title: "Orca"
type: entity
tags: [开源项目, ADE, 多Agent, 开发环境, 多模型]
sources: [raw/09-archive/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md, raw/09-archive/2026-11-01 - 终于有桌面版了！112k Star，Claude Codex Cursor一个窗口全搞定.md]
last_updated: 2026-11-02
---

## 定义

Orca 是 Stably AI（YC 孵化）开源的 ADE（Agent Development Environment，智能体开发环境）与多模型代码工作台（GitHub `stablyai/orca`，2026-11 达 112k Star）。定位与传统 IDE 相反：AI 不是插件，干活的主力是 Agent，人负责派任务、看进度、跑完挑结果。同时它也是**代码专用的多模型调度桌面客户端**：把 Claude、OpenAI Codex、Cursor 配套模型、本地 Ollama 代码模型塞进同一个窗口，统一会话、统一文件上传、统一 API 管理。**不自带模型权重**，所有推理走用户自己的 API Key，流量不经过第三方中转服务器。

## 关键信息

### 不含模型，复用已有 Agent

无需注册 Orca 账号，直接复用本地已登录的命令行 Agent；官方具名近 30 种（Claude Code、Codex、OpenCode、Grok、Cursor CLI、GitHub Copilot CLI、Kimi、Qwen Code、MiMo Code 等）——只要能在终端跑，就能放进 Orca。

### 多模型一键切换

同一对话窗口，上一句用 Claude 读大仓库架构，下一句直接切 Codex 做函数补全，再切别的模型做 review。对话历史、粘贴的代码、上传的文件全部保留。原生针对代码场景优化：支持一次性批量上传多个源码文件/文件夹，自动识别代码语言，不会把代码当成普通文本乱压缩。

### 原生代码库导入

直接选择本地项目文件夹导入，自动过滤 `.git`、`node_modules`、`dist`、编译产物；可手动勾选参与对话的文件（如只选 controller、service 层），精准控制上下文。

### 代码会话管理（workspace 工作区）

按项目分组保存对话、上传文件、模型配置，换项目直接切工作区，不用手动清理历史。

### 输出侧代码块优化

支持一键复制单块代码、一键复制全部代码；可单独选中某段代码追问（优化、加注释、找 bug、改成异步版本）。

### 并行 Worktree（ADE 核心特性）

同一需求派给多个 Agent，各自独立目录 + 独立分支，跑完并排看 diff 挑一份合并，其余丢弃。

### 其他功能

- WebGL 无限分屏终端（重启保留回滚记录、完成通知）
- Design Mode（内置 Chromium，点选页面元素把 HTML/CSS/截图一起发给 Agent）
- Diff 行级批注
- GitHub 与 Linear 集成（从任务一键开 worktree）
- SSH 远程 Worktree（断线重连 + 端口转发）
- 多账号用量与限流重置时间管理
- 手机端：iOS/Android App 与桌面配对，Agent 完成后推送通知

### Orca CLI

建 worktree、打快照、点界面均可脚本化，Agent 可反向驱动 Orca 接入自动化。

### 成本提示

Orca 本身免费，但 token 消耗按 Agent 数量算，5 个 Agent 并行就是 5 份消耗；模型调用费用仍是各服务商账单。

### 短板

- 没有自动写入本地文件的能力，所有代码输出都要手动复制
- 没有内置 diff 预览，改完代码只能自己对比
- 对超大仓库（几十万行）导入后手动筛选文件仍耗时，没有智能自动摘要筛选
- 社区更新节奏不算爆炸，新功能迭代偏慢

### 与 Cursor 的关系

互补而非替代——Cursor 深度嵌入 IDE、自动读取当前打开文件；Orca 是独立桌面工作台，适合批量喂文件做架构分析与大规模重构。

### 安装

```bash
brew install --cask stablyai/orca/orca   # Mac
# Windows/Linux 走 onorca.dev 或 GitHub Releases
# 或源码：git clone + pnpm install + pnpm dev，打包 pnpm build
```

技术栈：Tauri + 前端，内存占用低于开一堆浏览器标签。Key 保存在本地配置文件，不上传 Orca 服务器。

### 适用场景

✅ 一次性读整个仓库梳理架构 / 批量重构一批文件 / 对比不同模型输出 / 接入本地 Ollama 离线跑代码任务

❌ 替代 IDE 内实时补全 / 实时联动 IDE 自动改文件 / 追求完全免费

## 关联连接
- [[agent-development-environment]] — 所属品类概念
- [[Worktree]] — 并行协作的隔离机制
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ClaudeCode]] — 可接入的 Agent
- [[Codex]] — 可接入的 Agent
- [[Cursor]] — 互补的 IDE 内嵌工具
- [[Ollama]] — 本地模型接入
- [[Tauri]] — 桌面端技术栈（待建）
- [[摘要-orca-ade多agent协作]] — 早期来源
- [[摘要-orca-多模型桌面工作台]] — 最新来源
- [[程序员追风]] — 早期来源作者
- [[我是程序汪]] — 最新来源作者
