---
title: "摘要-powerjob-分布式任务调度"
type: source
tags: [来源, 原始文件, Java, 任务调度, PowerJob, 分布式]
sources: [raw/01-articles/项目终于用上了 PowerJob，睡觉真香！.md]
last_updated: 2026-07-08
---

## 核心摘要
PowerJob 是基于 [[Java]] 开发的企业级分布式任务调度平台，与 [[XXL-JOB]] 类似提供 Web 界面进行任务管理与监控。其核心优势在于**无锁化调度设计**，摒弃了 [[Quartz]] 和 XXL-JOB 基于数据库锁的性能瓶颈策略，支持无限水平扩展实现高可用与高性能。PowerJob 支持五种定时策略（API、CRON、固定频率、固定延迟、工作流）和四种执行模式（单机、广播、Map、MapReduce），其中 MapReduce 动态分片让开发者寥寥数行代码即获得集群分布式计算能力。此外还支持 DAG 工作流在线编排、上下游任务数据传递、判断节点与嵌套工作流节点。安装方式支持 jar 包运行和 [[Docker]] 部署，最小依赖仅关系型数据库（[[MySQL]]/PostgreSQL/Oracle 等）。客户端集成仅需引入 `powerjob-worker-spring-boot-starter` 依赖，实现 `BasicProcessor` 接口即可定义任务，配合 [[SpringBoot]] 的 `@EnableScheduling` 注解使用。

## 关联连接
- [[PowerJob]] — 本文介绍的主体框架
- [[XXL-JOB]] — 对比产品，基于数据库锁
- [[Quartz]] — 对比产品，无分布式任务治理
- [[任务调度]] — 本文提炼的核心概念
- [[SpringBoot]] — 客户端集成框架
- [[MySQL]] — 最小依赖数据库
- [[Docker]] — 推荐安装方式
- [[Java]] — 开发语言
