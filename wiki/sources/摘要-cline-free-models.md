---
title: "摘要-cline-free-models"
type: source
tags: [来源, Agent, 免费模型, token, 反代]
sources: [raw/01-articles/2026-10-07-Cline免费模型接入各种Agent，多账号免费token管够.md]
last_updated: 2026-10-08
---

## 核心摘要
编程 Agent Cline 会随新模型上线推出轮换的免费模型（如 DeepSeek V4.1 Flash、Space-Bunny、Meta Muse Spark 1.3、小米 Mimo V2.6 Flash，新用户另有 0.5 美元额度），但官方只支持在客户端或 VSCode 插件里用，接不进 WorkBuddy、OpenClaw、Hermes、Cherry Studio 等第三方 Agent。作者马佳彬参考 cline-free、cline2api-workers、cline2api 三个开源项目，以 cline-free 为基础改进出 ClineFreePool（MIT 协议，github.com/mijiabin2020/ClineFreePool）：剔除会耗尽赠送额度的付费模型与需订阅的模型、免费模型列表随 Cline 实时更新、优化部署体验（WorkBuddy 一句话安装）。流程为：部署本地控制台 → 刷新获取最新免费模型 → 用 Microsoft 账号批量注册登录 Cline 账号 → 多账号池轮询（免费模型可能 429 限流，官方未公开限流规则，被限流自动切下个账号）→ 从"接入配置"复制 Base URL 与 API Key 接入任意第三方 Agent。

## 关联连接
- [[Cline]] — 免费模型的提供方
- [[多账号池轮询]] — 核心机制
- [[WorkBuddy]] — 实测接入的 Agent
- [[Agent]] — 接入目标
