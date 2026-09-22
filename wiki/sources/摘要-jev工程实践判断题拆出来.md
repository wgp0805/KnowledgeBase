---
title: "摘要-jev工程实践判断题拆出来"
type: source
tags: [来源, Jev, Agent, 工程实践]
sources: [raw/01-articles/2026-09-21-一万字Jev 工程实践长文：把 Agent 的"判断题"从大模型里拆出来.md]
last_updated: 2026-09-22
---

## 核心摘要
Jev在工程实践中的定位：将Agent工作流中的「判断题」从大模型里拆出来，交给轻量决策模型快速处理。核心价值：一次请求多问题并行评估（延迟不变）、返回类型化结果+校准置信度（不是字符串需要解析）、输出Token永久免费。典型场景：工单分类路由、浏览器Agent动作选择、模型/工具路由、Agent执行轨迹监督。Java生态已有社区SDK（不依赖Spring AI ChatModel抽象，因为Jev没有消息/生成/流式）、Spring Boot Starter、MCP Server。

## 关联连接
- [[Jev]] — 判断模型
- [[Agent]] — 智能体
- [[工单分类]] — 客服路由
- [[浏览器Agent]] — 动作选择
- [[模型路由]] — 工具选择
- [[TypeSafeJavaSDK]] — Java社区SDK
- [[MCP]] — Model Context Protocol
- [[快慢分工]] — Agent架构共识
