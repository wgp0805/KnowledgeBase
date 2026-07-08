---
title: "PowerJob"
type: entity
tags: [Java, 任务调度, 分布式, 开源框架]
sources: [raw/01-articles/项目终于用上了 PowerJob，睡觉真香！.md]
last_updated: 2026-07-08
---

## 定义
PowerJob 是基于 [[Java]] 开发的企业级分布式任务调度平台，提供 Web 界面进行任务调度配置与监控，核心亮点是**无锁化调度设计**，支持无限水平扩展。

## 关键信息
- **无锁化设计**：摒弃数据库锁策略，调度性能强劲无上限，支持多服务器水平扩展实现高可用
- **定时策略**：支持 API、CRON、固定频率、固定延迟、工作流五种调度方式
- **执行模式**：单机、广播、Map、MapReduce（动态分片，寥寥数行代码获得集群分布式计算能力）
- **工作流支持**：DAG 可视化编排，支持上下游数据传递、判断节点、嵌套工作流节点
- **执行器广泛**：支持 Spring Bean、内置/外置 Java 类，可一键集成 Shell、Python、HTTP、SQL 处理器
- **运维便捷**：在线日志白屏化，执行器日志前端实时显示
- **依赖精简**：最小仅依赖关系型数据库（[[MySQL]]/PostgreSQL/Oracle/MS SQLServer）
- **安装方式**：jar 包运行或 [[Docker]] 部署，服务端默认端口 7700
- **客户端集成**：引入 `powerjob-worker-spring-boot-starter`，实现 `BasicProcessor` 接口，配合 [[SpringBoot]] `@EnableScheduling` 使用

## 关联连接
- [[摘要-powerjob-分布式任务调度]] — 来源
- [[XXL-JOB]] — 竞品，基于数据库锁
- [[Quartz]] — 竞品，无分布式任务治理
- [[任务调度]] — 所属概念
- [[SpringBoot]] — 客户端集成框架
- [[MySQL]] — 最小依赖数据库
- [[Docker]] — 推荐安装方式
- [[Java]] — 开发语言
