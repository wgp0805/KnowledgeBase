---
title: "EMQX"
type: entity
tags: [物联网, MQTT Broker, 开源, 分布式]
sources: ["raw/09-archive/2026-10-13-MQTT 生产实战 - 用了 8 年 MQTT，我为什么还要重新系统啃一遍（一） - IT规划师.md"]
last_updated: 2026-10-14
---

## 定义
EMQX 是大规模分布式 MQTT Broker，IT规划师 MQTT 系列阶段 3（Broker 选型）的三大对比候选之一（与 [[Mosquitto]]、HiveMQ），也是推荐本地实验环境 Broker 首选（"本地 Mosquitto 或 EMQX"）。

## 关键信息
- **选型对比范围**：系列将对比 EMQX/Mosquitto/HiveMQ 的功能、单机部署 vs 集群、认证与权限、监控告警、桥接与边缘部署
- **学习资料**：作者 8 年前入门 MQTT 的路径之一就是看 HiveMQ 博客入门文章 + EMQX 博客协议基础（阶段 1 计划重读官方文档与 EMQX 博客）
- **生产定位**：阶段 4 生产可靠性篇章面向万级设备接入的后端设计，EMQX 集群是该量级的候选方案
- 中文文档与博客生态是 .NET 物联网开发者主要学习来源

## 关联连接
- [[摘要-mqtt生产实战开篇]] — 来源
- [[MQTT协议]] — 实现的协议
- [[Mosquitto]] — 对比候选 Broker
- [[MQTTnet]] — 配套 .NET 客户端
- [[IT规划师]] — 系列作者
