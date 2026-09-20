---
title: "Claude"
type: entity
tags: ["Anthropic", "AI-Agent"]
sources: [raw/01-articles/2026-09-19-Kimi向左，Claude、GPT向右.md, raw/01-articles/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md]
last_updated: 2026-09-20
---

# Claude

Claude 是 Anthropic 的 AI 产品线，包含模型层（Opus/Sonnet）、CLI 层、Harness 层（Claude Code）、Agent 层。不同形态体验差距大：网页版、APP、CLI、Agent 各有定位。

## 封号风波与地区识别争议（2026-06 至 2026-08）

来自 [[摘要-codex重置的真正原因]]。2026-06-24 [[Anthropic]] 指控与阿里有关的操作者使用约 2.5 万个欺诈账户与 Claude 进行 2880 万次交互以蒸馏模型能力，6 月底中国开发者社区集中出现 Claude 账号被停用的反馈。之后 Claude Code 又被发现加入了未充分披露的地区识别与请求标记代码（涉及时区、代理设置等信息），Anthropic 工程师称是防止账号转售与模型蒸馏的反滥用实验，并在争议出现后回滚。此事件构成一个[[竞品迁移窗口]]，详见 [[Anthropic]] 与 [[竞品迁移窗口]]。

## 产品合并路线（2026-09-16）

Claude 把独立 Chat 和 Cowork 合并成一个 Claude，在做减法。与 [[ChatGPT]]（OpenAI 7 月把 Codex App 并入新版 ChatGPT 桌面应用）形成对比，而 [[KimiCode]] 还在做加法。详见 [[摘要-kimi向左claude-gpt向右]]。

## 优化生物模型（2026-09-19）

Anthropic 让 Claude 用不到四周优化 30 多个生物研究开源模型，开发 FlashPairformer 自定义 kernel 加速 triangle attention，蛋白设计成本最高降 98%。详见 [[摘要-anthropic优化生物模型]]。

## 关联连接
[[Anthropic]], [[Opus]], [[Claude-Code]], [[CLI]], [[沉默王二]], [[竞品迁移窗口]], [[摘要-codex重置的真正原因]], [[摘要-kimi向左claude-gpt向右]], [[摘要-anthropic优化生物模型]], [[ChatGPT]], [[KimiCode]], [[FlashPairformer]]
