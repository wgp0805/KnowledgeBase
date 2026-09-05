---
title: "摘要-deepseek-v4-pro-正式版实测"
type: source
tags: [来源, AI, 模型, DeepSeek, 实测]
sources: [raw/01-articles/DeepSeek V4 Pro 正式版是夯还是拉？深度实测来了！.md]
last_updated: 2026-08-17
---

## 核心摘要
小哈（犬小哈）对 DeepSeek V4 Pro 0813 正式版进行深度实测。结论：相比 Preview 版本，正式版在跑分上有明显提升，但实际编程体验提升有限。**跑分对比**：Aider Polyglot 78.5%（Preview 74.0%）、SWE-bench Verified 68.0%（Preview 65.5%）、HumanEval 98.5%、MBPP 95.0%、LiveCodeBench 76.5%。**实测任务**：(1) Spring Boot 3 + 虚拟线程高并发示例代码一次生成可用；(2) Spring Boot + MyBatis Plus + MySQL + Vue 3 后台管理系统，CRUD 生成完整但分页插件配置需手动调整；(3) Spring Cloud Gateway + Nacos 服务发现微服务，配置基本正确但路由规则需补充。**API 峰谷定价**：高峰时段（10:00-24:00）输入 2 元/百万 tokens、输出 8 元；低谷时段（00:00-10:00）输入 0.5 元、输出 2 元，缓存命中再减半。建议：日常编程用 Flash 性价比更高，复杂推理任务用 Pro。

## 关键信息
- **版本**：deepseek-v4-pro-0813（正式版），2026-08-13 上线
- **结构**：总参数 1.6T / 激活参数 49B（MoE），100 万上下文
- **跑分提升**：Aider Polyglot +4.5pp、SWE-bench +2.5pp、HumanEval 98.5%
- **实测表现**：基础代码生成能力强，复杂项目需人工微调（分页配置、路由规则等细节）
- **峰谷定价**：高峰 10:00-24:00（输入 2 元/输出 8 元），低谷 00:00-10:00（输入 0.5 元/输出 2 元），缓存命中减半
- **选型建议**：日常编程用 Flash，复杂推理用 Pro；锁定版本号保证可复现

## 关联连接
- [[DeepSeek]] — 核心实体
- [[小哈]] — 来源作者
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — 相关发布信息
- [[摘要-deepseek-v4-flash发布]] — Flash 版本对比
- [[DeepSeekHarness]] — 评测框架
- [[虚拟线程]] — 实测任务涉及技术
- [[SpringCloudGateway]] — 实测任务涉及技术
- [[Nacos]] — 实测任务涉及技术
