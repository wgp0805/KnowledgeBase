---
title: "StrongConsistency"
type: concept
tags: [概念, 分布式系统, 一致性, 架构]
sources: [raw/01-articles/SpringEvent别瞎用！被它坑的绩效都没了！.md]
last_updated: 2026-08-27
---

## 定义
强一致性（Strong Consistency）要求操作完全一致，失败必须回滚。例如提单场景库存扣减与订单提单必须完全一致，不能出现扣了库存但订单没下成功的情况。[[SpringEvent]] 和 [[PublishSubscribePattern|发布订阅模式]] 无法提供订阅异常→回滚能力，因此不适合强一致性场景。

## 关联连接
- [[EventualConsistency]] — 对立概念
- [[SpringEvent]] — 不适用该一致性的机制
- [[PublishSubscribePattern]] — 不适用该一致性的模式
- [[transaction-management|事务管理]] — 强一致性的实现手段
- [[CAP理论]] — 一致性理论框架
