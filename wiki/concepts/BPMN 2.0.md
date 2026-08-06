---
title: "BPMN 2.0"
type: concept
tags: [工作流, 流程建模, 标准]
sources: [raw/01-articles/为什么越来越多人使用 Flowable  ？.md]
last_updated: 2026-08-06
---

## 定义
BPMN 2.0（Business Process Model and Notation）是业界通用的业务流程建模规范，用于定义业务流程的可视化表示。

## 关键信息
- **核心元素**：
  - 事件（Events）：开始、结束、中间事件
  - 活动（Activities）：任务、子流程
  - 网关（Gateways）：条件分支、并行分支
  - 流向（Sequence Flows）：连接各元素
- **文件格式**：.bpmn20.xml
- **部署方式**：放在 resources/processes/ 目录，应用启动时自动部署
- **支持引擎**：Flowable、Activiti、Camunda 等主流工作流引擎
- **优势**：可视化流程设计，业务人员和技术人员都能理解

## 关联连接
- [[摘要-为什么越来越多人使用Flowable]] — 来源
- [[Flowable]] — 工作流引擎
- [[Activiti]] — Flowable 前身
- [[Camunda]] — 竞品工作流引擎
- [[工作流引擎]] — 核心概念
- [[CMMN]] — 案例管理标准
- [[DMN]] — 决策表标准
