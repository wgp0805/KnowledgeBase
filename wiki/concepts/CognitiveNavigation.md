---
title: "CognitiveNavigation"
type: concept
tags: [AI, Agent, 可观测性, 诊断]
sources: [raw/01-articles/2026-07-17-当AI Agent开始"自己拿主意"，你怎么知道它没在犯错？.md]
last_updated: 2026-07-20
---

## 定义
认知导航（Cognitive Navigation）是一种 Agent 运行时健康诊断框架，以诊断侧车（Diagnostic Sidecar）形式嵌入 Agent 执行流程。在 Agent 每一步执行前后执行三件事：量化健康度、拆解驱动因素、输出导航指令。核心思想是"运行时感知"而非"事后复盘"。

## 关键信息
### 健康度公式
S = T - C - D
- **S（健康度）**：0-1 分，实时量化 Agent 当前状态
- **T（转化力）**：Agent 推进任务的能力还剩多少
- **C（约束力）**：Agent 是否撞到了边界（权限不够、文件找不到、上下文超限）
- **D（内部消耗）**：Agent 是否在空转（推理越来越长、输出越来越水）

### 导航指令
- **CONTINUE**：一切正常，继续
- **NARROW_SCOPE**：别贪多，收窄范围
- **RESET_CONTEXT**：上下文脏了，清理一下
- **HALT**：出问题了，等人来

### 与 Trace 的区别
- Trace（追踪，如 Langfuse/DeepEval）回答"Agent 走了哪条路"
- Diagnosis（诊断，认知导航）回答"Agent 身体怎么样——这正常吗、该继续吗、该干预吗"
- 两者互补：一边 Trace 一边 Diagnose

### 实测效果
- **Qoder CN 金融尽调**（3 Agent）：合规质量 0.24 → 0.86 (+258%)，法规覆盖率 60% → 100% (+67%)，Token 消耗 18,330 → 11,325 (-38%)
- **WorkBuddy 代码编写**（5 Agent）：交付 ~640 行 Python（EU AI Act 合规检查模块），全程可知每个 Agent 状态

## 关联连接
- [[摘要-ai-agent-cognitive-navigation]] — 来源
- [[Agent]] — 被诊断的目标
- [[Qoder]] — 应用平台
- [[WorkBuddy]] — 多 Agent 协作验证
