---
title: "摘要-springbatch-quartz定时批量任务"
type: source
tags: [来源, SpringBatch, Quartz, 批处理, 定时任务]
sources: [raw/09-archive/2026-11-15 - SpringBoot + SpringBatch + Quartz整合定时批量任务.md]
last_updated: 2026-11-16
---

## 核心摘要
小哈学Java 转载的 SpringBoot + SpringBatch + Quartz 整合实战：PC 网页触发设备升级记录后，后台用 Quartz 定时、SpringBatch 批量完成设备更新下发。核心链路是 `JobLauncher.run(job, jobParameters)` 触发 Job → `JdbcCursorItemReader` 按 taskId 读待升级设备 → Processor 逐条调下发接口 → `ItemWriter` 批量回写状态与重试次数 → JobListener 在 afterJob 中检查失败设备数，有失败则用 QuartzManager 调度一个延时单次 Job 重试。作者踩坑总结：ItemReader/ItemWriter 自定义 SQL 是最坑的两处；SpringBatch 的 chunk 模式是"读 5000 条 → 逐条 processor → 最后一次性 writer"，processor 阶段不能批量操作。内容已并入 [[SpringBatch]] 与 [[Quartz]]。

## 关联连接
- [[SpringBatch]] — 本篇主角框架（新建实体页）
- [[Quartz]] — 定时触发与失败重试调度
- [[SpringBoot]] — 承载框架
- [[小哈]] — 来源作者
- [[任务调度]] — 所属概念域
