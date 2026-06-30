---
title: "Step3Flash"
type: entity
tags: [AI模型, Flash模型, Agent]
sources: [raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md]
last_updated: 2026-06-30
---

## 定义
Step3Flash 是阶跃星辰 Step 系列中的 Flash 档模型，文章将 Step 3.7 Flash 定位为面向高频、多轮、低延迟 Agent 执行场景的效率型模型。

## 关键信息
- 在文章实测中，Step 3.7 Flash 被用于 Claude Code 中执行开发者日志站、GitHub 项目雷达、源码架构报告生成等 Coding Agent 任务。
- 优势集中在工具调用稳定性、错误率较低、前端页面视觉层级较好和最终交付物完成度较高。
- 成本不是最低，DeepSeek V4 Flash 的单次 Token 成本更低；但文章认为真实 Agent 成本还应计算失败重试成本和人工介入成本。
- 适合高频、多轮、低延迟任务、生产级 Coding Agent 工作流、多模态理解和预算敏感但又不想牺牲稳定性的场景。
- 明显短板是上下文窗口约 256K，不适合一次性塞入大量代码库或超长文档。

## 关联连接
- [[摘要-step-3-7-flash-agent横评]] — 来源
- [[DeepSeek]] — 横评对比模型
- [[Gemini]] — 横评对比模型
- [[Qwen]] — 横评对比模型
- [[AICoding]] — 主要应用场景
- [[Agent]] — 执行层使用语境
