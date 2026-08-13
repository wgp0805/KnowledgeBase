---
title: "Zeebe"
type: entity
tags: [流程引擎, 工作流, 分布式, Camunda, 云原生]
sources: []
last_updated: 2026-08-13
---

## 定义
Zeebe 是 [[Camunda]] 开源的分布式流程引擎，为云原生、高吞吐工作流场景设计，是 Camunda 8 的引擎核心。采用事件溯源 + 日志复制实现水平扩展与容错，区别于 Camunda 7 的关系型存储单体架构。

## 关键信息
- **架构**：分区（Partition）+ 副本（Replica）实现水平扩展，Raft 协议选主
- **事件日志**：所有流程事件以 append-only 日志记录，事件溯源可重放
- **BPMN 2.0**：标准流程建模语言
- **三大组件**：Gateway（API 网关）、Broker（流程引擎节点）、Operate（可视化监控）
- **对比 [[Camunda]] 7**：7 是单体关系型、8(Zeebe) 是分布式日志型，适合微服务高并发
- **对比 [[jBPM]]**：jBPM 偏 Java 嵌入式，Zeebe 偏独立分布式服务

## 关联连接
- [[Camunda]] — 所属流程引擎家族
- [[jBPM]] — 另一流程引擎对标
- [[Drools]] — 规则引擎，常与流程引擎协同
