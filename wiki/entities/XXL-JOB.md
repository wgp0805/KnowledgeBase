---
title: "XXL-JOB"
type: entity
tags: [Java, 任务调度, 分布式, 开源框架]
sources: [raw/01-articles/项目终于用上了 PowerJob，睡觉真香！.md, raw/09-archive/xxl-job已正式接入AI.md]
last_updated: 2026-10-13
---

## 定义
XXL-JOB 是大众点评开源的分布式任务调度平台，提供 Web 界面进行任务管理与监控，采用基于数据库锁的调度策略。

## 关键信息
- **调度方式**：基于数据库锁，存在性能瓶颈
- **定时类型**：支持 CRON 表达式
- **任务类型**：内置 Java、GLUE Java、Shell、Python 等脚本
- **分布式任务**：静态分片
- **在线任务治理**：支持
- **日志白屏化**：支持
- **系统依赖**：[[MySQL]]
- **报警监控**：邮件
- **DAG 工作流**：不支持

## AI 执行器（2026-10-13，详见 [[摘要-xxl-job接入ai]]）
从 **v3.1.0** 引入 [[AI执行器]]，内置基于 Bean 模式（`@XxlJob("handlerName")`）的 AI Handler，与 Spring AI、[[Ollama]]、[[Dify]] 打通；**v3.4.0** 集成 [[OpenClaw]] 新增 `openClawJobHandler`。核心主张：**AI 任务与普通任务共用同一套调度、重试、告警与日志**，无需为 AI 任务单独搭系统。
- `ollamaJobHandler` / `difyWorkflowJobHandler` / `openClawJobHandler` 均为标准 Bean 模式 Handler
- `prompt`、`input` 从**任务参数**动态获取（而非硬编码），同一 Handler 可跑不同 AI 任务；Dify 的 `baseUrl`/`apiKey` 也已从执行器侧文件优化为任务参数配置，支持多应用集成
- 调度中心保持无感知：只管"何时触发、触发哪个 Handler、传什么参数"，AI 执行器负责"怎么调 AI"
- 边界：AI 任务需单独部署 AI 执行器；任务参数受字段长度限制；**不支持流式输出**（同步等待）；复杂多轮对话与工具调用仍需自定义 Handler

## 关联连接
- [[摘要-powerjob-分布式任务调度]] — 对比来源
- [[摘要-xxl-job接入ai]] — 来源（AI 执行器）
- [[AI执行器]] — AI 能力集成概念
- [[PowerJob]] — 竞品，无锁化设计
- [[Quartz]] — 同类框架
- [[任务调度]] — 所属概念
- [[MySQL]] — 系统依赖
- [[Java]] — 开发语言
