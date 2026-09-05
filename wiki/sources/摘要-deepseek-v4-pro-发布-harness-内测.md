---
title: "摘要-deepseek-v4-pro-发布-harness-内测"
type: source
tags: [来源, DeepSeek, V4 Pro, Harness, Responses API, Agent, 面试]
sources: [raw/01-articles/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md]
last_updated: 2026-08-13
---

## 核心摘要

本文是 [[沉默王二]] 于 2026-08-13 发布的 Agent 工程面试题系列第二篇。以 **DeepSeek V4 Pro 正式版发布** 和 **DeepSeek Harness 进入最后一个内测版本** 为引子，通过 12 道面试问答系统讲解 Agent 工程化的进阶议题。

核心论点：**模型决定 Agent 的能力上限，Harness 决定这个上限能不能稳定兑现**。V4 Pro 正式版（总参数 1.6T / 激活 49B）与 Flash（284B / 13B）虽都支持 100 万上下文，但激活参数差近 4 倍，直接影响推理深度与 Agent 工具调用准确率。

文章关键议题：
- **Pro/Flash 模型路由**：规划/审查/复杂推理走 Pro，文件读写/格式化/简单补全走 Flash；PaiCLI 支持 7 供应商动态切换 + 降级兜底
- **上下文布局与 Prompt Caching**：不变内容（System Prompt/工具定义/长期记忆/Few-shot）放前面，变化内容（用户输入/工具结果）放后面，以命中前缀缓存降低成本
- **Responses API vs Chat Completions**：有状态、可引用前一轮 response ID、tool_calls 结构化返回，更适合 Agent 且能显著降低 Token 成本
- **后训练的价值**：架构/参数不变仅重做后训练（SFT + RL）也能显著提升 Agent 能力，V4 Flash 正式版即典型例证
- **版本管理与可复现**：锁定具体版本号（如 deepseek-v4-pro-0813）+ 离线回归测试集 + 上线后持续监控失败率/任务放弃率/平均完成步数
- **Harness 定义**：模型之外的一切工程设施（循环控制/上下文管理/工具调度/记忆/安全审批），Claude Code/Codex/PaiCLI 都是 Harness
- **上下文压缩必要性**：长程任务会撑爆窗口、中间位置信息易被忽略、延迟随长度增加
- **Better Harness 审计工具**：PaiCLI 的 Better Harness 并非 Agent 产品，而是通过会话证据/项目配置/配置三通道并行取证，按五维度打分评估 Agent 干活质量

## 关联连接
- [[DeepSeek]] — V4 Pro 正式版发布方
- [[Harness]] — Model + Harness = Agent 核心概念
- [[PaiCLI]] — 文章案例项目，含 Better Harness 审计工具
- [[ResponsesApi]] — Pro/Flash 正式版支持的有状态 API
- [[BetterHarness]] — PaiCLI 的 Agent 质量审计工具
- [[沉默王二]] — 文章作者
- [[摘要-deepseek-harness内测]] — 同系列前篇（2026-08-06 Harness 内测消息）
- [[摘要-deepseek-v4-flash发布]] — V4-Flash 正式版发布（0731）
- [[Codex]] — 被 V4 Pro 适配的 Agent 工具
- [[ClaudeCode]] — DeepSeek Harness 对标产品
