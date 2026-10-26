---
title: "Mem0"
type: entity
tags: [记忆框架, Agent, 开源, 长期记忆]
sources:
  - raw/09-archive/2026-09-19-长对话先收口：用“工作记忆 vs 长期记忆“管理 AI 上下文 - Jessica_留学中.md
  - raw/09-archive/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md
  - raw/09-archive/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md
last_updated: 2026-10-13
---

## 定义
Mem0 是一个面向生产级 AI Agent 的可扩展长期记忆层（Long-term Memory Layer），本质是"自动收口 + 按需检索"，给 Agent 装一层跨会话的长期记忆。

## 关键信息
- 出处：Chhikara et al. 2025《Mem0: Building production-ready AI agents with scalable long-term memory》(arXiv:2504.19413)
- 与 [[Zep]]、[[LangMem]] 同属 Agent Memory / Long-term Memory Layer 一类框架

### 记忆冲突处理的两种版本策略
| 策略 | v2 写入时消歧 | v3 只追加 + 检索时推理 |
|------|------|------|
| 做法 | 发现矛盾当场 UPDATE/DELETE 旧记忆，库永远干净一致 | 两条带时间戳的事实并存，查询时语义检索 + 时间排序取最新 |
| 优点 | 库干净一致 | 无不可逆丢失，LLM 调用少 |
| 代价 | 删错不可逆、每条要检索+二次 LLM 判断，贵 | 库会变大，依赖检索排序质量 |

- 结论：**追加比删除安全**，因为删除不可逆，排序错了改规则还能修
- 详见 记忆冲突处理

### 工作流定位（2026-10-13 增补，详见 [[摘要-一文搞懂agent-memory]]）
Mem0 是三条记忆工程路线中的"自动化记忆服务"一派：1) 从用户对话中提取重要事实 2) 查找相关已有记忆 3) 执行保存或维护 4) 后续任务检索相关信息。其能力与更新策略随版本变化（早期自动更新流程与部分新版实现不同），并探索了图结构表达实体关系。适合为产品增加用户长期记忆能力的场景。

## 关联连接
- 记忆冲突处理 — Mem0 引发的记忆冲突方法论
- [[Zep]] / [[LangMem]] — 同类记忆框架
- [[Letta]] — Agent 自主管理记忆的另一条路线
- [[ClaudeCode]] — 文件系统记忆路线
- [[长期记忆]] — 所服务的能力
- [[摘要-长对话先收口-工作记忆vs长期记忆]] — 来源
- [[摘要-10道ai-agent高频面试题]] — 来源（v2/v3 冲突处理）
