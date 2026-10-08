---
title: "摘要-jev哑巴模型产业改变"
type: source
tags: [来源, 原始文件, Jev, 模型分化]
sources: [raw/01-articles/2026-09-30-“哑巴模型”Jev火了，会给AI产业带来什么改变.md]
last_updated: 2026-10-08
---

## 核心摘要
"哑巴模型"Jev 走红：它不聊天、不写文章代码，只在开发者给定一组选择和状态时输出判断（Choice/Score/Boolean + 概率）。前 OpenAI 研究员（参与 InstructGPT、ChatGPT、GPT-4）Diogo Almeida 反向造模型，反思 RLHF 让模型面对没把握的问题也倾向给出流畅笃定的回答，Jev 则把不确定性写进输出。实测：Browser Use 创始人用它搭浏览器 Agent 查 Google Flights 机票，全流程 7.1 秒、单次成本 0.0039 美元、中位延迟约 178 毫秒；Vercel AI Gateway 上输入约 0.04 美元/百万 Token、输出免费。Jev 是模型分化趋势的极端样本（同期 Gemini 3.5 Flash、DeepSeek V4 Flash、Qwen3.8-Flash-Next、GLM-5.3-Flash 等 flash 档位扎堆）——模型厂商按任务复杂度、频率、速度、成本重新切分能力档位。局限：正反问概率之和有时超过 1，校准尚未达标。行业影响：任务成为核心、按任务路由多个模型（腾讯 WorkBuddy Auto 模式、Cursor 2026-08 推出的 Cursor Router），能调用多模型的 Agent 入口将更重要；Jev 名字取自"杰文斯悖论"——判断更便宜后调用量反而上升。

## 关联连接
- [[Jev]] — 主角模型
- [[DiogoAlmeida]] — 创始人
- [[模型分化]] — 本文核心概念
- [[模型路由]] — Jev 走红推动的入口能力
- [[杰文斯悖论]] — Jev 命名来源
- [[WorkBuddy]] — Auto 模式按任务选模型的国内案例
- [[Cursor]] — Cursor Router 海外案例
