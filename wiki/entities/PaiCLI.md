---
title: "PaiCLI"
type: entity
tags: [AI, CLI工具, Agent, 开源项目]
sources: [raw/01-articles/AI agent工具应该怎么使用.md, raw/01-articles/面试官皱眉："让你负责一个生产级 Agent，你会怎么设计？"，我上来就开始背 ReAct、Function Calling、Skills。面试官听完摇头。.md]
last_updated: 2026-07-24
---

## 定义
PaiCLI 是开发者"二哥"（沉默王二）开源的终端 Agent 项目，类 Claude Code 的 AI 命令行工具，使用 Python 编写，GitHub 地址：https://github.com/itwanger/PaiCLI-Python。作为生产级 Agent 的典型案例，深度覆盖了 Agent 工程化的核心挑战。

## 关键信息
- 开发方式：全程使用 Codex 进行 AI 辅助编程
- 集成了阿里云 OCR 服务（通过 .env 中 ALIYUN_OCR_ENABLED 全局开关控制）
- 使用 JLine 交互库实现命令行交互界面
- 多模型协作开发流程：Claude Code 做需求拆解和审查，Codex 负责执行实现
- 每个功能均让 Codex 生成测试用例

### 三种运行模式
1. **ReAct 主循环**：经典的推理-行动循环模式
2. **Plan-and-Execute**：先规划后执行，适合复杂任务
3. **Multi-Agent**：多角色协作模式

三种模式共用一套工具注册表、记忆系统、安全审批、审计日志，是 Agent Harness 的核心设计挑战。

### 上下文压缩策略
- Map-Reduce 分片摘要：旧消息每 5 条一组切片 → 独立生成摘要 → 合并为整体摘要
- 压缩后保留"摘要 + 最近 3 轮完整对话"
- 压缩前进行事实提取，将跨会话稳定事实写入长期记忆

### 记忆系统设计
- 不使用向量数据库，而是关键词匹配检索（规模小，毫秒级响应）
- 时间衰减加权：24 小时从满分衰减到半分
- 重要信息三层过滤：排除临时任务 → 排除推测 → 保留持久信号

### 指数退避重试
- 默认最多 3 次，间隔 500ms → 1s → 2s，上限 30s
- 加 20% 随机抖动，支持 Retry-After 头
- 区分可重试和不可重试错误类型

## 关联连接
- [[Codex]] — 核心开发工具
- [[ClaudeCode]] — 代码审查工具
- [[PaiAgent]] — 同作者的 AI Agent 平台项目
- [[摘要-AI-agent工具应该怎么使用]] — 来源
- [[摘要-生产级Agent设计]] — 来源（面试题详解）
- [[context-compression]] — 上下文压缩策略
- [[指数退避重试]] — API 重试机制
- [[渐进式披露]] — Skill 按需加载机制
- [[沉默王二]] — 项目作者
