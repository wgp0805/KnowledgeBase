---
title: "BetterHarness"
type: concept
tags: [AI, Agent, 审计工具, PaiCLI, 质量评估]
sources: [raw/09-archive/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md]
last_updated: 2026-08-13
---

## 定义

Better Harness 是 [[PaiCLI]] 内置的 **Agent 质量审计工具**，通过并行启动三个取证通道采集 Agent 运行时证据，按五个维度打分评估 Agent 干活质量。注意：它**不是 Agent 产品**，与 [[Harness|DeepSeek Harness]]（Coding Agent 产品）是完全不同的概念。

## 关键信息

### 三个并行取证通道

1. **会话证据通道**
   - 从对话记录提取去标识化元数据
   - 采集：工具调用次数、模型切换记录、任务生命周期信息

2. **项目配置通道**
   - 扫描仓库里的测试文件、CI 文件和交付约束
   - 用于判断 Agent 产出是否符合项目工程规范

3. **配置通道**
   - 检查 Skill 的配置
   - 检查 MCP 的设置
   - 检查记忆入口

### 评估输出
最终按**五个维度**打分，综合检查 Agent 干活的质量（文章未列出具体五维度名称）。

### 与 DeepSeek Harness 的区别

| 维度 | DeepSeek Harness | PaiCLI Better Harness |
|------|------------------|----------------------|
| 定位 | 完整 Coding Agent 产品 | 审计工具 |
| 对标 | Claude Code、Codex | 无（独创审计定位） |
| 职责 | 接收自然语言指令，ReAct 循环调用模型和工具完成编码任务 | 检查 Agent 干得怎么样 |
| 关系 | 模型做决策，Harness 做执行 | 评估上述执行的质量 |

## 关联连接
- [[PaiCLI]] — Better Harness 的宿主项目
- [[Harness]] — 概念辨析对象（DeepSeek Harness 是 Agent 产品，Better Harness 是审计工具）
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — 来源
- [[沉默王二]] — PaiCLI 作者
