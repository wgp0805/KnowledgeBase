---
title: "Apdex"
type: concept
tags: [APM, 性能监控, 用户体验, 度量标准]
sources: [raw/01-articles/2026-07-26-分布式链路追踪系统之skywalking java agent 的使用、skywalking web界面简介 - Linux-1874.md]
last_updated: 2026-07-27
---

## 定义
Apdex（Application Performance Index，应用性能指数）是由 Apdex 联盟于 2004 年开放的应用性能评估标准。它从用户角度出发，将应用响应时间量化为 0-1 的满意度评价，统一测量和报告用户体验。

## 关键信息
- **核心原理**：定义应用响应时间的最优门槛 T，根据实际响应时间与 T 的比较，将用户体验分为三个等级：
  - **Satisfied（满意）**：响应时间 ≤ T（如 T=1s，耗时 0.6s 或 1s 为满意）
  - **Tolerating（可容忍）**：T < 响应时间 ≤ 4×T（如 T=1s，1s~4s 为可容忍）
  - **Frustrated（烦躁期）**：响应时间 > 4×T
- **计算公式**：Apdex = (Satisfied 请求数 + Tolerating 请求数 × 0.5) / 总请求数
- **应用场景**：SkyWalking 等 APM 工具使用 Apdex 作为服务性能的核心评分指标

## 关联连接
- [[SkyWalking]] — 在 SkyWalking 仪表盘中作为关键性能指标展示
- [[distributed-tracing]] — 分布式链路追踪
- [[摘要-skywalking-java-agent-使用]] — 来源