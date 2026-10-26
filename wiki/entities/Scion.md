---
title: "Scion"
type: entity
tags: [实体, 版本控制, Anthropic, 基础设施]
sources: [raw/09-archive/2026-10-19-周一上线 DeepSeek 开始卷“许愿式编程”，Agent 手机来了，Character.AI 申请破产 - 小七-七牛开发者.md]
last_updated: 2026-10-20
---

## 定义
Scion 是 Anthropic 自研的版本控制系统，为应对 Agent 大规模写代码把 Git 撑到极限而生，把历史查询、diff、合并等能力集中到服务端处理。

## 关键信息
- **背景**：Anthropic monorepo 每天合并变更从约 2500 次涨到超过 3 万次，CI 每天执行约 2500 万次 checkout，Git 成为瓶颈
- **架构方向**：服务端集中处理历史查询、diff、合并（区别于 Git 的本地全量历史）
- **效果**：代码 checkout 从分钟级降到秒级，相关基础设施资源占用大幅下降
- **信号**：Agent 自动写代码的规模正在倒逼版本控制这类最底层的软件基础设施重做

## 关联连接
- [[摘要-周一上线-许愿式编程与agent手机]] — 来源
- [[Anthropic]] — 研发方
- [[Git]] — 被替代/对比的版本控制系统
