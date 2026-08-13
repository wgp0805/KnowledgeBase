---
title: "当下 Agent 架构全景与区别"
type: synthesis
tags: [AI, Agent, 架构, 工作流, 多Agent]
sources:
  - wiki/concepts/augmented-llm.md
  - wiki/concepts/四层架构.md
  - wiki/concepts/ReAct_Agent.md
  - wiki/concepts/autonomous-agent.md
  - wiki/syntheses/react-vs-plan-execute.md
  - wiki/sources/摘要-agent-engineering.md
  - wiki/sources/摘要-agent-tools-workflow区别.md
  - wiki/sources/摘要-生产级Agent设计.md
last_updated: 2026-08-13
---

# 当下 Agent 架构全景与区别

## 核心结论
当下 Agent 架构可按"自底向上"分为五层，越往上越自主。最根本的分界线是 **Workflow 直线 vs Agent 圆环**——前者由人预编排固定路径，后者由 LLM 自主决策循环。选型铁律：能简单绝不复杂，能用 Workflow 就别上 Agent。

## 五层架构

| 层 | 代表 | 性质 |
|----|------|------|
| ① 基础单元 | [[augmented-llm]] | LLM + 检索 + 工具 + 记忆，是构建一切的地基 |
| ② 执行循环 | ReAct / Plan-and-Execute / ToolPipeline | 单个 Agent 内部"怎么跑"，圆环 |
| ③ 工作流编排 | Anthropic 五大 Workflow | 人预编排的直线 |
| ④ 多 Agent 协作 | 三角色 / MoA / Kanban Swarm | 多个 Agent 怎么配合 |
| ⑤ 自主智能体 | [[autonomous-agent]] | 四大能力·端到端·最小人工干预 |

完整 Agent 系统的组件划分另见 [[四层架构]]（LLM 层 / Skill 层 / Tool 层 / Agent Runtime 层）。

## 最关键的区别：Workflow 直线 vs Agent 圆环
来自 [[摘要-agent-tools-workflow区别]]（基于 Anthropic《Building Effective Agents》）：
- **Workflow**：开发者写死路径，LLM 只在单步内执行，不决定走向。可控性高、Token 可预测。
- **Agent**：LLM 自主决定下一步走哪，路径不可预测。灵活但费 Token、易跑偏。
- **判据**：只有"LLM 自主决策 + 循环执行"同时成立才叫 Agent。从 Observe 回到 Think 的循环边是 Agent 本质。

## 第②层辨析：执行循环三种
- **[[ReAct_Agent]]**：思考→行动→观察→再思考，每步 LLM 决策。适合无固定流程的开放问题。局限：单次一个工具、Token 消耗大、多文件重构易越改越乱。
- **Plan-and-Execute**：先规划 DAG 任务图再按拓扑执行。适合需全局规划的任务。与 ReAct 可嵌套——执行阶段内部可跑 ReAct（见 [[react-vs-plan-execute]]）。
- **ToolPipeline**：一次性编排串行/并行工具步骤，模型只规划一次。适合流程固定的标准化任务。

## 第③层辨析：Anthropic 五大工作流
来自 [[摘要-agent-engineering]]：
1. [[prompt-chaining]] — 固定串行
2. [[routing-workflow]] — 分类分发
3. [[parallelization-workflow]] — 分段并行 / 投票并行
4. [[orchestrator-workers]] — 中央 LLM 动态拆分分配
5. [[evaluator-optimizer]] — 双 LLM 循环迭代优化

## 第④层辨析：多 Agent 协作三种
- [[multi-agent-collaboration]] — Planner/Coder/Reviewer 三角色，靠文件显式交接 + 工具白名单硬约束 + 对抗性评审
- [[mixture-of-agents]] — 多参考模型独立推理 + 聚合器综合
- [[kanban-swarm]] — 三层架构 + 9 状态 + 6 协作模式

## 第⑤层：自主智能体
[[autonomous-agent]] 四大核心能力：复杂输入理解、自主推理规划、可靠工具调用、错误自主恢复。生产级实现（如 [[摘要-生产级Agent设计]] 的 PaiCLI）通常三种模式共用一套工具/记忆/安全/审计：ReAct 主循环 + Plan-and-Execute + Multi-Agent。

## 2025 主流落地形态
外层 Workflow 编排 + 关键决策点交 Agent + Guardrails 护栏（max_iterations / Token 预算 / 失败降级），而非一上来就全自主。

## 关联连接
- [[augmented-llm]] — 基础单元
- [[四层架构]] — 系统组件划分
- [[ReAct_Agent]] — 执行循环代表
- [[autonomous-agent]] — 自主智能体
- [[react-vs-plan-execute]] — 执行循环对比
- [[摘要-agent-engineering]] — 五大工作流来源
- [[摘要-agent-tools-workflow区别]] — 直线 vs 圆环来源
- [[摘要-生产级Agent设计]] — 生产级架构来源
- [[multi-agent-collaboration]] — 多 Agent 协作
- [[loop-vs-hermes]] — Loop 与 Hermes 区别
- [[loop-vs-harness]] — Loop 与 Harness 工程区别
