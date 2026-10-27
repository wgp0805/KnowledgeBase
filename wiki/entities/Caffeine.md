---
title: "Caffeine"
type: entity
tags: [实体, 缓存, Java, 本地缓存]
sources: [raw/09-archive/面试经典：如何设计高并发短链接系统.md, "raw/09-archive/为什么越来越多人用JD-hotkey？.md"]
last_updated: 2026-10-27
---

## 定义
Caffeine 是 Java 高性能本地缓存库，基于 W-TinyLFU 算法实现高命中率和低延迟。常作为 Redis 之外的多级缓存第一层，承载热点数据。

## 关键信息
- **定位**：应用进程内本地缓存，与远程 [[Redis]] 缓存组成多级缓存
- **优势**：命中率高、吞吐量大、GC 友好，性能优于 Guava Cache
- **短链接场景**：热点短链叠加 Caffeine 本地缓存，减少 Redis 访问，扛住极高读 QPS
- **典型组合**：Caffeine（本地）+ Redis（分布式）+ MySQL（兜底）三级缓存架构
- **热 key 场景（2026-10-27 补充）**：[[JD-hotkey]] 探测判定为热 key 后，value 正是落进 Caffeine——业务查到后调 `smartSet(key, value)` 写入（非热 key 不写），后续 `get` 直接走 JVM 内存零网络开销；配置项 `caffeine-size` 控制本地缓存最大条数（默认 5 万）

## 关联连接
- [[摘要-高并发短链接系统设计]] - 来源
- [[短链接系统]] - 应用场景
- [[缓存雪崩]] - 多级缓存防护
- [[Redis]] - 上游分布式缓存
- [[JD-hotkey]] - 热 key 探测框架的本地缓存载体（2026-10-27 补充）
- [[热key探测]] - 探测方法论
- [[摘要-jd-hotkey热key探测]] - 来源
