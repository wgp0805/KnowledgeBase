---
title: "Activiti"
type: entity
tags: [工作流引擎, BPMN, Java]
sources: [raw/01-articles/为什么越来越多人使用 Flowable  ？.md]
last_updated: 2026-08-06
---

## 定义
Activiti 是一个开源的 Java 工作流引擎，Flowable 的前身，由 Alfresco 公司开发。

## 关键信息
- **历史**：Flowable 核心开发团队从 Activiti 分叉创建 Flowable
- **现状**：维护活跃度相对较低，性能基础能力够用
- **对比**：
  - 维护活跃度：Flowable > Activiti
  - 性能：Flowable 有更好的异步优化
  - DMN/CMMN：Flowable 支持更全面
  - 适合场景：Activiti 适合老项目维护，Flowable 适合新项目首选
- **迁移建议**：老系统已跑在 Activiti 上，不必为了追新而强行换，需评估数据库脚本和业务兼容

## 关联连接
- [[摘要-为什么越来越多人使用Flowable]] — 来源
- [[Flowable]] — 分叉项目
- [[Camunda]] — 竞品工作流引擎
- [[工作流引擎]] — 核心概念
- [[BPMN 2.0]] — 流程建模标准
