---
title: "RepairLoop"
type: concept
tags: [Agent, 自动修复, 工程架构]
sources: [raw/01-articles/2026-09-04-谷歌真的急了！Gemini 3.8 Flash 刚发布，Google Harness 就跟随其后.md]
last_updated: 2026-09-05
---

## 定义
Repair Loop（自动循环修复）是 Agent 的自我纠错机制：Agent 修改代码后进入测试节点，测试通过则结束，失败则将错误日志重新交给 Agent 继续修改，连续失败超过设定次数触发 Kill Switch 停止任务。

## 关键信息
- 流程：Agent 修改代码 → 测试节点 → 通过则结束 / 失败则重试
- Kill Switch：连续失败超过设定次数（Google 示例为5次）自动停止
- Google 指出：普通聊天窗口中人类负责复制错误、重新输入、判断是否继续；当这些动作被软件化后，系统开始能够自己闭环处理
- Agent 的自主性就是这样一点点建立起来的

## 关联连接
- [[HarnessEngineering]] — Harness 工程架构
- [[AgentHarness]] — Agent 运行基础设施
- [[KillSwitch]] — 安全停止机制
- [[摘要-谷歌gemini38flash-harness-engineering]] — 来源
