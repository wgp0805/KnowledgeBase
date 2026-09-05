---
title: "Drools"
type: entity
tags: [Java, 规则引擎, BRMS, KIE]
sources: []
last_updated: 2026-08-13
---

## 定义
Drools 是开源业务规则引擎（BRMS），基于 Rete 系列算法，将业务规则从代码外部化为独立管理的规则文件（DRL），实现规则与业务逻辑解耦。与 [[jBPM]] 同属 KIE（Knowledge Is Everything）项目组。

## 关键信息
- **算法**：ReteOO（面向对象版 Rete）/ PHREAK（异步增量推理，提升性能）
- **规则文件**：DRL（Drools Rule Language），用 `rule "名称" when ... then ... end` 描述
- **核心组件**：KieSession（规则会话）、Working Memory（事实 Fact 容器）、Agenda（冲突消解）
- **KIE 工作台**：规则编写/测试/部署的 Web 工具
- **典型场景**：风控规则、计费策略、促销规则、复杂决策逻辑

## 关联连接
- [[jBPM]] — 同属 KIE，常与 Drools 协同（规则 + 工作流）
- [[Camunda]] — 另一流程/规则引擎对标
- [[Zeebe]] — Camunda 8 的分布式引擎
