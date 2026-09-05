---
title: "Flowable"
type: entity
tags: [工作流引擎, BPMN, Java, 开源]
sources: [raw/01-articles/为什么越来越多人使用 Flowable  ？.md]
last_updated: 2026-08-06
---

## 定义
Flowable 是一个开源的 Java 工作流引擎，基于 BPMN 2.0 标准，用于管理业务流程、审批流程和任务流转。

## 关键信息
- **起源**：从 Activiti 分叉而来，由 Activiti 核心开发团队创建
- **标准支持**：BPMN 2.0（流程建模）、CMMN（案例管理）、DMN（决策表）
- **核心优势**：
  - 与 Java/Spring 生态深度集成（flowable-spring-boot-starter）
  - 性能优于 Activiti（异步执行器优化、锁粒度、批处理）
  - 支持嵌入式部署和独立部署
  - 中文资料逐渐丰富
- **典型架构**：流程文件（.bpmn20.xml）放在 resources/processes/ 目录，应用启动时自动部署
- **核心 API**：RuntimeService（流程驱动）、TaskService（任务管理）
- **适用场景**：OA 审批、订单流转、工单系统、银行/政务/制造行业内网部署

## 关联连接
- [[摘要-为什么越来越多人使用Flowable]] — 来源
- [[Activiti]] — 前身项目
- [[Camunda]] — 竞品工作流引擎
- [[BPMN 2.0]] — 流程建模标准
- [[CMMN]] — 案例管理标准
- [[DMN]] — 决策表标准
- [[SpringBoot]] — Java 框架
- [[工作流引擎]] — 核心概念
- [[流程实例]] — 工作流执行单元
- [[任务服务]] — 任务管理服务
- [[运行时服务]] — 流程驱动服务
- [[嵌入式设计]] — 部署模式
