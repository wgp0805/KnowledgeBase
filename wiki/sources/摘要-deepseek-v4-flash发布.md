---
title: "摘要-deepseek-v4-flash发布"
type: source
tags: [来源, DeepSeek, 模型]
sources:
  - raw/01-articles/2026-07-31-倒反天罡！DeepSeek V4-Flash 正式版悄然上线：130亿激活参数，把自家1.6万亿旗舰「以下克上」 - 小白跃升坊.md
last_updated: 2026-08-03
---

## 核心摘要
- 2026-07-31 DeepSeek 在 API 更新日志中悄然上线 DeepSeek-V4-Flash-0731 正式版：模型结构/尺寸与 4 月预览版完全一致，**仅重新进行了后训练**，开发者无需改代码，后台自动切换；仅限 API，App/网页端未变。
- 「以下克上」：V4-Flash（总参数 284B、激活参数 13B）在 Agent 能力多项基准上反超三个月前的 V4-Pro 预览版。Terminal Bench 2.1 达 82.7（预览仅 61.8）、DeepSWE 从 7.3 暴增至 54.4、Toolathlon Verified 70.3，逼近 Claude Opus 4.8。
- 技术底牌（V4 系列共通）：CSA+HCA 混合稀疏注意力（1M 上下文 KV Cache 压缩）、mHC 流形约束超连接（Birkhoff 双随机矩阵）、Muon 优化器（替代 AdamW）、FP4 QAT 量化。1M 上下文从 demo 变成日常工作负载。
- 定价「降维打击」：Flash 约为 Pro 价格的三分之一（输入未命中 1 元/百万 tokens，输出 2 元），并发上限 2500 vs Pro 的 500；预告峰谷定价（高峰 2 倍）。
- 生态攻势：原生支持 OpenAI Responses API（Flash 独占）、Codex CLI/桌面端/IDE 扩展可直接接入；预览版已适配 Claude Code、OpenClaw、OpenCode、CodeBuddy。
- 彩蛋：DeepSeek Harness 首次亮相（Agent 评测框架，团队负责人崔添翼）。
- 实测：爱范儿 5 个任务共 393 次请求、3422 万 token、总花费 2.85 元。
- 行业信号：AI 竞争进入「智价比」时代，后训练成为主战场；Kimi K3（2.8T MoE）走全能路线，V4-Flash 走轻量效率路线，国产模型差异化格局形成。
- 泼冷水：仅 API、权重未开源、基准均为官方自测、高推理强度依赖 token 消耗大、能力上限仍低于 Pro、缺原生多模态。

## 关联连接
- [[DeepSeek]] — 模型系列
- [[DeepSeekHarness]] — Agent 评测框架
- [[后训练]] — 核心概念
- [[Codex]] — 被适配的生态
- [[Kimi]] — 国产对手
- [[GLM]] — 国产对手
- [[ClaudeCode]] — 适配的 Agent
- [[OpenClaw]] — 适配的 Agent
- [[OpenCode]] — 适配的 Agent
