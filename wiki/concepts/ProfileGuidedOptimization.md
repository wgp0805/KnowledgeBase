---
title: "ProfileGuidedOptimization"
type: concept
tags: [数据库, 性能优化, 编译器, MySQL, PGO]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 定义

Profile-Guided Optimization（PGO，按剖析引导优化）是一种编译器优化技术：先让程序跑一遍典型负载收集执行 profile，再用这些数据指导编译器重新编译，让热点路径指令更紧凑、分支预测更准、函数内联更优。[[MySQL]] 9.7 将其从企业版下放社区版，被称为"免费的午餐"式性能提升。

## 关键信息

- Percona 对比测试（MySQL 9.7）：

| Buffer Pool | 平均提升 | 最佳场景 |
| --- | --- | --- |
| 2GB | 3.0% | 4 线程时 5.5% |
| 12GB | 4.1% | 4 线程时 8.6% |
| 32GB | 12.2% | 1 线程时 14.3% |

- **收益来源**：完全来自 CPU 层面（指令缓存利用率、分支预测、函数内联）；Buffer Pool 命中率、锁竞争、I/O 指标在 PGO 与非 PGO 版本间几乎完全一致
- **零成本升级**：不改配置、不换硬件，升级到 PGO 构建版本即可受益；32GB 以上 Buffer Pool 大内存服务器收益最明显

## 关联连接

- [[MySQL]] — 载体数据库
- [[摘要-mysql-9-7-lts]] — 来源
- [[Percona]] — 基准测试提供方
