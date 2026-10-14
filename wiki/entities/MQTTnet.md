---
title: "MQTTnet"
type: entity
tags: [物联网, .NET, MQTT客户端, 开源库]
sources: ["raw/01-articles/2026-10-13-MQTT 生产实战 - 用了 8 年 MQTT，我为什么还要重新系统啃一遍（一） - IT规划师.md"]
last_updated: 2026-10-14
---

## 定义
MQTTnet 是 .NET 生态最主流的 MQTT 客户端/服务器开源库，IT规划师 8 年 MQTT 生涯的入门入口（当年通过 GitHub 搜索 "MQTT .NET" 找到，看 README 和 Demo 上手），也是其 MQTT 生产实战系列阶段 2（.NET 实战）的指定客户端。

## 关键信息
- **系列实战范围**：基于 MQTTnet 跑通发布订阅，实现生产级客户端——连接验证器、ClientId 管理、自动重连、心跳配置、QoS 1 幂等处理
- **配套实验环境**：.NET 10 + MQTTnet + 本地 Mosquitto 或 EMQX Broker
- **丢包排查**：系列第 6 篇专门讲 MQTTnet 场景下的丢包排查方法论
- **历史背景**：2016 年前后 .NET 生态几乎没有 MQTT 资料，NuGet 上连像样的客户端库都找不到，MQTTnet 是少数选择

## 关联连接
- [[摘要-mqtt生产实战开篇]] — 来源
- [[MQTT协议]] — 实现的协议
- [[IT规划师]] — 系列作者
- [[EMQX]] — 配套 Broker
- [[Mosquitto]] — 配套 Broker
- [[QoS]] — 客户端需处理的等级
- [[CleanSession]] — 生产级客户端关键配置
