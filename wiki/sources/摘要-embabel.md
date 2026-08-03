---
title: "摘要-embabel"
type: source
tags: [来源, AI框架, Agent, Java]
sources:
  - raw/01-articles/2026-08-01-Spring之父再次出山，开发了新的AI框架！ - 苏三说技术.md
last_updated: 2026-08-03
---

## 核心摘要
- Rod Johnson（Spring 之父）在 2026 年 4 月 Microsoft JDConf 上发布 **Embabel**——面向企业 AI Agent 的 JVM 开源框架（Kotlin 编写，Java 完全兼容），2026-07-20 发布 1.0.0 GA，Apache 2.0 协议。
- 核心问题：「怎么让非确定性的 AI 在确定性的企业系统里稳定工作」。企业业务系统容不得个人助手场景下可接受的 10% 错误率，生成式 AI 的不可预测性在金融交易、订单处理、合规审计场景=不可用。
- 与 Spring AI 的分层：Spring AI ≈ Servlet API（解决"怎么接入 AI 模型"），Embabel ≈ Spring MVC（解决"怎么让 Agent 在企业系统稳定工作"）。「Spring AI 是零件箱，Embabel 是装配图纸+流水线」。
- 核心武器 GOAP（Goal-Oriented Action Planning）：从游戏 AI 借来的确定性规划算法，规划器完全不用 LLM，直接砍掉 40-60% 的 LLM 调用。另有 Utility AI 模式。
- 强类型、面向对象的 Agent 编程：Agent/Action/Goal 三大核心抽象，@Action/@Goal 注解，输入输出都是强类型领域对象，告别 Python 生态的字符串/dict 地狱。
- 成本数据：GOAP 不用 LLM 规划省 40-60% 调用；强类型 Domain Model 精确契约省 20-40% Token；整体降本空间 50-70%。
- 适用场景：企业级 AI Agent、金融/合规/审计、多步复杂任务自动化、已有 Spring Boot 技术栈；快速原型验证可能偏重（Spring AI 更轻量）。

## 关联连接
- [[Embabel]] — 本文介绍的框架
- [[RodJohnson]] — Spring 之父
- [[GOAP]] — 核心算法
- [[UtilityAI]] — 备选规划模式
- [[SpringAI]] — 对比框架
- [[Agent]] — 编程模型
- [[苏三]] — 文章作者
