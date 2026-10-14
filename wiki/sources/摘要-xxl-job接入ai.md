---
title: "摘要-xxl-job接入ai"
type: source
tags: [来源, XXL-JOB, AI执行器, Ollama, Dify, Java]
sources: [raw/01-articles/xxl-job已正式接入AI.md]
last_updated: 2026-10-13
---

## 核心摘要
[[苏三]] 拆解 [[XXL-JOB]] 的 AI 执行器能力：从 **v3.1.0** 引入 AI 执行器（内置多个 AI 任务 Handler，与 Spring AI、Ollama、Dify 打通），到 **v3.4.0** 进一步集成 [[OpenClaw]] 新增 `openClawJobHandler`。核心主张：**AI 任务和普通任务应在同一套调度体系里管理**，共用同一套重试、告警、日志——不需要为"每天跑一次 AI"单独搭系统。"定时任务 + AI = 把跑批变成跑智能"。

## 关键信息

### 架构本质
- 调度中心不关心执行的是 AI 任务还是普通任务，只管"什么时候触发、触发哪个 Handler、传什么参数"
- AI 执行器负责"怎么调 AI"：把 AI 调用封装成标准 **Bean 模式 Handler**（`@XxlJob("handlerName")` 自动注册为可调度任务）
- GLUE 模式另一种，不推荐用于 AI 场景

### 内置 Handler
| Handler | 作用 | 配置来源 |
|------|------|------|
| `ollamaJobHandler` | 调用本地 Ollama 模型 | `prompt` / `input` 从任务参数动态获取 |
| `difyWorkflowJobHandler` | 触发 Dify 工作流 | 早期 baseUrl/apiKey 放执行器文件，后优化为任务参数动态配置，支持多 Dify 应用 |
| `openClawJobHandler` | 集成 OpenClaw（v3.4.0 新增） | — |

### 落地四步
1. 调度中心新建执行器（AppName 必须为 `xxl-job-executor-sample-ai`，示例代码用这个 AppName 注册）
2. Spring Boot 引入 `xxl-job-core` 3.4.0 并配置 admin 地址 / appname / port
3. 调度中心新建任务：选执行器、Cron、运行模式 BEAN、JobHandler、任务参数（JSON 含 prompt 与 input）
4. 调度日志查看执行状态、耗时与 AI 返回结果（`XxlJobHelper.log` 记录）

### 优缺点
- **优点**：统一调度管理、内置失败重试（模型服务不可用/超时自动重试）、完整执行日志、动态配置不改代码、多 AI 后端、零额外基础设施
- **缺点**：AI 执行器需单独部署（普通执行器不能跑 AI 任务）、任务参数字段长度限制、**不支持流式输出**（同步等待，长文本生成耗时长）、内置 Handler 灵活性有限（复杂多轮对话与工具调用仍需自定义 Handler）

### 适用场景
定时 AI 数据摘要/内容生成、定时触发 Dify 工作流、定时 AI 数据清洗、已有 XXL-JOB 的项目——均为强烈推荐；需复杂 AI 编排要评估；需流式输出不推荐。

## 关联连接
- [[XXL-JOB]] — 核心实体
- [[AI执行器]] — 核心概念
- [[Ollama]] — 本地模型后端
- [[Dify]] — 工作流后端
- [[OpenClaw]] — v3.4.0 集成
- [[SpringAI]] — 相关生态
- [[摘要-powerjob-分布式任务调度]] — 同类调度框架对比
- [[摘要-为什么越来越多人用Sa-Token]] — 同一作者相关文章
