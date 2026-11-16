---
title: "SpringBatch"
type: entity
tags: [Java, Spring, 批处理, 框架]
sources: [raw/09-archive/2026-11-15 - SpringBoot + SpringBatch + Quartz整合定时批量任务.md]
last_updated: 2026-11-16
---

## 定义
SpringBatch 是 Spring 生态的批处理框架，提供 Job/Step/Chunk 模型处理大批量数据的读取-处理-写入，与 [[SpringBoot]] 无缝集成（`@EnableBatchProcessing` 启用，`spring.batch.job.enabled=false` 可关闭启动时自动跑 Job）。

## 关键信息
- **核心模型**：Job（一次批处理任务，由 JobLauncher + JobParameters 触发）→ Step（一个处理阶段）→ chunk（一批数据量，如 5000），每条数据经 ItemProcessor 逐条处理后，整批一次性交给 ItemWriter
- **读组件**：`JdbcCursorItemReaderBuilder` 支持自定义 SQL + 参数化查询（`@StepScope` 使 Bean 能感知 Job 运行时参数），RowMapper 映射结果实体
- **写组件**：`ItemWriter` 收到整批 ProcessResult 后做批量回写，可加 `@Transactional` 保证批次原子性
- **Job 参数传递**：`JobParametersBuilder().addString("taskId", ...)` 传入，JobExecutionListener 的 beforeJob 中取出（每次可用 UUID 参数保证 Job 实例唯一）
- **执行特性（作者实测小结）**：读 5000 条 → processor 逐条处理（此阶段不能做批量操作）→ 5000 条处理完再一次性执行 ItemWriter；最坑的两处是 ItemReader 与 ItemWriter 的自定义 SQL
- **与 [[Quartz]] 整合模式**（详见 [[摘要-springbatch-quartz定时批量任务]]）：Quartz 负责"定时触发"——到点调 Service 执行 `jobLauncher.run(job, jobParameters)`；JobListener.afterJob 检查失败设备数，仍失败则用 QuartzManager 调度延时单次 Job 做下一轮重试，形成"定时驱动 + 失败重试闭环"
- **定位**：单机批处理首选；需要分布式调度、任务治理、告警监控时看 [[XXL-JOB]] / [[PowerJob]]（对比见 [[Quartz]] 页能力表）

## 关联连接
- [[SpringBoot]] — 承载框架
- [[Quartz]] — 定时触发搭档
- [[任务调度]] — 所属概念域
- [[XXL-JOB]] / [[PowerJob]] — 需要分布式治理时的替代方案
- [[PostgreSQL]] — 实战示例使用的数据库
- [[小哈]] — 实战文章作者
- [[摘要-springbatch-quartz定时批量任务]] — 来源
