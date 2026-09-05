---
title: "Camunda"
type: entity
tags: [工作流引擎, BPMN, 云原生]
sources: [raw/01-articles/为什么越来越多人使用 Flowable  ？.md]
last_updated: 2026-08-06
---

## 定义
Camunda 是一个开源的工作流引擎，分为 Camunda 7（经典嵌入式）和 Camunda 8（云原生事件流）。

## 关键信息
- **架构风格**：
  - Camunda 7：类似 Flowable 的经典嵌入式引擎 + 关系型数据库
  - Camunda 8：云原生事件流架构（基于 Zeebe）
- **运维工具**：Cockpit / Operate 等工具更完善
- **超高并发**：Camunda 8 + Zeebe 性能更强
- **学习曲线**：Camunda 8 学习曲线更陡
- **适合场景**：大规模分布式、云原生场景
- **对比**：Camunda 在监控和超大规模场景更猛，Flowable 在嵌入现有 Java 系统、快速落地更省心

## 关联连接
- [[摘要-为什么越来越多人使用Flowable]] — 来源
- [[Flowable]] — 竞品工作流引擎
- [[Activiti]] — Flowable 前身
- [[工作流引擎]] — 核心概念
- [[BPMN 2.0]] — 流程建模标准
- [[Zeebe]] — Camunda 8 的核心引擎
