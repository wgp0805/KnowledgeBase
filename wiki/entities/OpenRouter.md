---
title: "OpenRouter"
type: entity
tags: [AI, 模型聚合, API网关, 路由]
sources:
  - raw/01-articles/"牛来"员工：你们可以在 OpenCode 爽用 Ox Alpha 模型了，1M上下文并支持视频输入（附Agent面试题）.md
  - raw/01-articles/2026-09-07-对话OpenRouter CEO：Harness 正在取代超级 App，未来所有软件都只是 Agent 的后台工具.md
last_updated: 2026-09-08
---

## 定义
OpenRouter 是大模型聚合路由平台，通过统一 API 聚合多家厂商模型，用户配一个 Key 即可访问和切换数百个模型。由 [[AlexAtallah]]（[[OpenSea]] 联合创始人）创办，在快速分裂的模型生态中扮演"总路由器"：连接不同模型与推理服务商，实时比较价格、速度和质量，并把流量导向更合适的供给方。

## 关键信息
- [[OxAlpha]] 在 OpenRouter 上以模型 ID `ox-alpha` 提供（2026-08）
- 知识库中多个工具将其作为 BYOK 中转渠道：[[Junie]] 的 BYOK 明确支持 OpenRouter，可曲线使用 DeepSeek/Qwen/GLM 等国产模型；AionUi、pi-agent、Hermes Agent 等亦内置其路由支持
- 同一模型经不同 Provider（如 OpenRouter vs OpenCode Zen）调用时，Agent 效果可能不同——Provider 会在 API 层做 system prompt 注入、参数覆盖、工具调用格式转换、限流超时策略等"加工"

### CEO Alex Atallah 的核心判断（2026-09-07 20VC 对谈）
- **路由出售的是选择权**而非技术：让开发者随时接入最新模型，降低对单一实验室和云厂商的依赖
- **多模型并用是长期常态**：AI 不会只剩一个赢家，训练数据/方法/模型"性格"差异本身就是价值（详见 [[多模型并用]]）
- **杰文斯悖论实证**：GPT-5.6 Luna 价格降 10 倍，使用量增 13 倍（详见 [[杰文斯悖论]]）
- **推理服务不是无差异商品**：同一模型不同服务商部署，速度/成本/输出质量都可能不同（"一个 Token 并不等于另一个 Token"）
- **7 月单月上线 70 个模型**，平均约每 10 小时一个
- **收费模式**：按量付费计划收 5.5% 抽成；基于承诺消费的企业计划承诺消费部分不收此项费用；自带推理服务或自带密钥相关费用取消
- **Stripe 收购传闻**（100 亿美元）：不能置评，但无论发生什么都会继续执行原有愿景

### OpenSea 经验迁移
- 2020-10 NFT 爆发让 Alex 提前经历了今天 AI 公司面对的扩容问题
- 教训：在真实流量到来前就做压测，确保系统能承受 10 倍负载
- 这套扩容和可靠性执念带到了 OpenRouter

## 关联连接
- [[摘要-ox-alpha模型与agent面试题]] — 早期来源
- [[摘要-对话OpenRouter-CEO-Harness取代超级App]] — CEO 对谈来源
- [[AlexAtallah]] — 创始人兼 CEO
- [[OpenSea]] — Alex 前序创业公司
- [[OxAlpha]] — 托管的免费预览模型
- [[LLM网关]] — 同类概念（企业级自建网关）
- [[Junie]] — 通过 OpenRouter 中转国产模型的典型场景
- [[模型路由]] — 核心业务概念
- [[多模型并用]] — 核心理念
- [[杰文斯悖论]] — 降价刺激需求实证
- [[Harness]] — Alex 判断 Harness 不会消失
- [[蒸馏]] — 开放权重生态关键方法
