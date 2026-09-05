---
title: "CFS调度器"
type: concept
tags: [Linux, 内核, 调度器, CFS]
sources: [raw/01-articles/2026-08-24 - 面试官：什么是时间片？.md]
last_updated: 2026-08-25
---

## 定义
CFS（Completely Fair Scheduler，完全公平调度）是 Linux 从 2.6.23 开始引入的进程调度器，由内核开发者 Ingo Molnar 实现。思路与传统轮转调度完全不同：不再分配固定时间片，改成按进程权重动态分配时间片。

## 关键信息
- **核心思路**：不再分配固定时间片，按进程权重动态分配
- **sched_latency（调度延迟）**：所有可运行进程「跑完一轮」的目标总时间
  - 默认 6ms（实际按 `750000 * (1 + ilog(ncpus))` 动态计算，随 CPU 数量变化）
  - 新内核版本可能更高（如 24ms）
  - 可通过 `/proc/sys/kernel/sched_latency_ns` 查询调整
  - 每个进程实际时间片 = `sched_latency / 进程数`
- **sched_min_granularity（最小调度粒度）**：默认 0.75ms，确保每个进程至少能跑这么久，避免时间片被切得太碎
- **sched_wakeup_granularity**：唤醒抢占粒度
- **权重影响**：优先级高的进程权重高，时间片更长
- **示例**：sched_latency 为 6ms，3 个同优先级进程，每个分到 2ms
- **演进**：CFS 在 Linux 6.6（2023 年）已被 EEVDF 调度器（Earliest Eligible Virtual Deadline First）替代

## 关联连接
- [[摘要-时间片-调度]] — 来源
- [[时间片]] — CFS 动态分配的对象
- [[上下文切换]] — 调度切换的开销
