---
title: "Step3Flash"
type: entity
tags: [AI模型, Flash模型, Agent, 多模态]
sources: [raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md, raw/01-articles/测评国内多模态大模型，到底哪个更省事？.md]
last_updated: 2026-07-02
---

## 定义
Step3Flash 是阶跃星辰 Step 系列中的 Flash 档模型，文章将 Step 3.7 Flash 定位为面向高频、多轮、低延迟 Agent 执行场景的效率型模型；在 2026-07 苏三多模态横评中被评为"生产可用"综合胜出者。

## 关键信息
- 在 Coding Agent 横评（[[摘要-step-3-7-flash-agent横评]]）中，Step 3.7 Flash 被用于 Claude Code 中执行开发者日志站、GitHub 项目雷达、源码架构报告生成等 Coding Agent 任务。
- 优势集中在工具调用稳定性、错误率较低、前端页面视觉层级较好和最终交付物完成度较高。
- 成本不是最低，DeepSeek V4 Flash 的单次 Token 成本更低；但文章认为真实 Agent 成本还应计算失败重试成本和人工介入成本。
- 适合高频、多轮、低延迟任务、生产级 Coding Agent 工作流、多模态理解和预算敏感但又不想牺牲稳定性的场景。
- 明显短板是上下文窗口约 256K，不适合一次性塞入大量代码库或超长文档。

### 多模态实战表现（苏三 2026-07 横评，详见 [[摘要-多模态大模型横评-苏三]]）

| 场景 | 表现 |
|------|------|
| **流程图→业务逻辑还原**（Claude Code `@图片`） | 10 步流程完全吻合原图；15s 完成；Token 换算 ¥0.0246，三者最便宜也最快 |
| **电子发票→结构化 JSON 提取**（业务 API） | 12 字段完全正确；5.6s 完成；一张成本 ¥0.0060，三者最优 |

**综合结论**：在两个真实生产场景（Agent 内 + 业务 API）都保持了较好的输出质量，同时速度更快、Token 消耗更低——最符合"生产可用"的要求。苏三个人推荐作为 Agent 或业务 API 的首选测试对象。

## 关联连接
- [[摘要-step-3-7-flash-agent横评]] — Coding Agent 横评来源
- [[摘要-多模态大模型横评-苏三]] — 多模态横评来源（综合胜出）
- [[多模态大模型]] — 归属类别
- [[DeepSeek]] — 横评对比模型
- [[Gemini]] — 横评对比模型
- [[Qwen]] — 横评对比模型
- [[MiniMax]] — 多模态横评对手（M3）
- [[AICoding]] — 主要应用场景
- [[Agent]] — 执行层使用语境
