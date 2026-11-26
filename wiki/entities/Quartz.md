---
title: "Quartz"
type: entity
tags: [Java, 任务调度, 开源框架]
sources: [raw/09-archive/项目终于用上了 PowerJob，睡觉真香！.md, raw/09-archive/2026-11-15 - SpringBoot + SpringBatch + Quartz整合定时批量任务.md]
last_updated: 2026-11-16
---

## 定义
Quartz 是 [[Java]] 生态中经典的定时任务框架，基于数据库锁实现调度，无分布式任务治理能力。

## 关键信息
- **调度方式**：基于数据库锁，有性能瓶颈
- **定时类型**：仅支持 CRON 表达式
- **任务类型**：内置 Java
- **分布式任务**：无
- **在线任务治理**：不支持
- **日志白屏化**：不支持
- **报警监控**：无
- **系统依赖**：关系型数据库（[[MySQL]]、Oracle 等）
- **DAG 工作流**：不支持
- **定位**：单机定时任务为主，缺乏分布式治理能力，适合简单调度场景

### 与 SpringBatch 整合的定时批量模式（2026-11-15，详见 [[摘要-springbatch-quartz定时批量任务]]）
Quartz 的价值不止"到点跑一个方法"，典型组合是**定时驱动批处理 + 失败重试闭环**：
- Quartz 到点触发 Service，执行 `jobLauncher.run(updateDeviceJob, jobParameters)` 启动 [[SpringBatch]] 的 Job（taskId 等业务参数经 JobParameters 传入）
- Job 执行完由 JobListener.afterJob 统计失败数，仍失败则用 QuartzManager 调度一个延时单次 Job（`scheduleRunOnceJob`，如 10 秒后触发下一轮重试），并 `checkNameNotExist` 防重复注册
- 该模式不依赖 Quartz 的 CRON 周期，重试节奏由业务数据（重试间隔/重试次数上限）驱动，适合"网页触发 + 后台定时批量 + 逐轮重试"的设备升级/批量下发类需求

## 关联连接
- [[摘要-powerjob-分布式任务调度]] — 对比来源
- [[PowerJob]] — 新一代替代方案
- [[XXL-JOB]] — 同类分布式框架
- [[ElasticJob]] — 同类分布式框架（重写 Quartz 的 DB 分布式功能改用 Zookeeper）
- [[分布式任务调度框架]] — 所属概念
- [[任务调度]] — 所属概念
- [[MySQL]] — 系统依赖
- [[Java]] — 开发语言
- [[SpringBatch]] — 整合的批处理框架（定时触发 + 失败重试闭环）
- [[小哈]] — 整合实战来源作者
- [[摘要-springbatch-quartz定时批量任务]] — 来源
