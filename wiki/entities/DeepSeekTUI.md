---
title: "DeepSeekTUI"
type: entity
tags: [AI工具, Agent, DeepSeek, 开源]
sources: [raw/01-articles/推荐一款DeepSeek V4 编程神器！.md]
last_updated: 2026-05-19
---

## 定义
基于 DeepSeek V4 的开源终端编程智能体（类似 Claude Code），原生支持 100 万 token 上下文和思考模式流式输出，由社区开发者 Hmbown 在 GitHub 上开源。

## 关键信息

### 核心特性
- **100 万 token 上下文**：支持上下文跟踪、手动或配置压缩
- **思考模式流式输出**：实时观察模型解决问题的思维链
- **完整工具集**：文件操作、Shell 执行、Git、网页搜索/浏览、子智能体、MCP 服务器
- **Auto 模式**：根据任务复杂度自动选择模型和推理强度

### 三种交互模式
1. **Plan（计划模式）**：只读分析，先生成计划再执行
2. **Agent（代理模式）**：任务执行需审批的默认模式
3. **YOLO（自动模式）**：工作区任务自动执行，无需审批

### 推理强度
- 提供 `off → high → max` 三种推理强度档位

### 配置与主题
- 通过 `/config` 命令配置语言（locale）和模型
- 通过 `/theme` 命令切换主题，内置 8 种主题可实时预览
- 支持中文界面和亮/暗色主题

### 安装使用
```
npm install -g deepseek-tui@0.8.37
deepseek --model auto
```
- 首次启动弹出设置引导
- API 密钥从 Deepseek 官网获取

### 性价比
- 使用 `deepseek-v4-pro` 模型处理 200 万+ token 花费不到 2 元
- 配合 DeepSeek 使用性价比高

## 关联连接
- [[DeepSeek]] — 模型提供方
- [[摘要-推荐deepseek-v4-编程神器]] — 来源
- [[ClaudeCode]] — 对标产品
- [[Agent]] — Agent 核心概念
- [[MCP]] — 外部服务协议
- [[AICoding]] — AI 编程范式
