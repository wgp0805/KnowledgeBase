---
title: "Cline"
type: entity
tags: [实体, 编程Agent, 免费模型, VSCode]
sources: [raw/09-archive/2026-10-07-Cline免费模型接入各种Agent，多账号免费token管够.md]
last_updated: 2026-10-08
---

## 定义
Cline 是一款编程 Agent，最早以 VSCode 插件形式推出，在开发者社区（Vibe Coding 圈）享有知名度。它提供轮换更新的免费模型额度服务，是"薅 token"生态的重要入口。

## 关键信息
- **免费模型机制**：注册即用，新用户另有 0.5 美元额度；免费模型列表非固定，随最新模型上线定期更换（如 DeepSeek V4.1 Flash、Space-Bunny 太空兔、Meta Muse Spark 1.3、小米 Mimo V2.6 Flash），模型上下架都属正常
- **官方接入限制**：只能在 Cline 客户端或 VSCode 插件里用，无法直接接入 WorkBuddy、OpenClaw、Hermes、Cherry Studio 等第三方工具，除非做成本地 API 反代
- **第三方反代生态**：cline-free、cline2api-workers、cline2api 等开源项目；作者基于 cline-free 改进的 ClineFreePool（github.com/mijiabin2020/ClineFreePool，MIT 协议）剔除会耗光 0.5 美元赠送额度的付费模型、免费列表实时更新、支持 WorkBuddy 一键部署
- **账号与限流**：免费模型仍可能 429 限流且官方未公开限流规则，需多账号池轮询兜底；Cline 账号可用 Microsoft 账号注册（国内门槛低），设备码激活超时可重新登录重试
- **风险提示**：免费福利何时收紧或加强限流不确定，"该薅抓紧薅"；实测调用速度尚可，适合日常平替和补充

## 关联连接
- [[摘要-cline-free-models]] — 来源
- [[多账号池轮询]] — 配套使用机制
- [[WorkBuddy]] — 实测接入的 Agent
- [[Agent]] — 所属软件类别
