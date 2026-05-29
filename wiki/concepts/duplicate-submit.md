---
title: "duplicate-submit"
type: concept
tags: [Web开发, 幂等性, 防重复]
sources: []
last_updated: 2026-05-29
---

## 定义
重复提交（Duplicate Submit）是指用户对同一表单或操作多次提交的问题，在网络延迟、用户误操作或恶意攻击场景下会导致数据重复或业务异常。

## 关键信息
- 前端防重：提交后禁用按钮、Token 机制（页面唯一 Token）
- 后端防重：幂等性设计、分布式锁、数据库唯一约束
- Token 方案：服务端生成 Token 存入 Session，提交时校验并删除
- 分布式锁：基于 Redis 的 SETNX，防止并发重复提交
- 数据库唯一约束：从根本上防止重复数据

## 关联连接
- [[idempotency]] — 幂等性设计
- [[distributed-lock]] — 分布式锁防重
- [[Redis]] — Token 存储和分布式锁实现
- [[摘要-重复提交问题]] — 来源
- [[摘要-prevent-duplicate-order]] — 高并发防重方案
