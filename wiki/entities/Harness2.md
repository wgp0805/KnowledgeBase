---
title: "Harness2"
type: entity
tags: [开源项目, Agent, Harness, 自动优化, Google]
sources: ["raw/09-archive/谷歌开源的AI Harness自进化框架，在GitHub短短一个月狂揽25K+Star，太强了！！.md"]
last_updated: 2026-11-24
---

## 定义
Harness2（github.com/google-research/harness2）是 Google Research 开源（非官方支持产品，Apache 2.0）的 **harness 自动进化框架**：不训练模型、权重全程锁死，只把模型外面那层配置（提示词、工具说明、记忆、Skills、插件等）当作可迭代优化的对象，靠"同任务不同壳改动的行为差异对比"替代"等一个标准答案"。

## 关键信息
- **把 harness 拆成 8 个可编辑组件 / 4 组**：
  - 上下文组：系统提示词、Guardrails、Memory、Skills（决定模型看到什么、记住什么、被什么约束）
  - 工具接口组：工具说明、Scripts（决定模型怎么理解它能调什么）
  - 委派组：Subagents（任务怎么分出去）
  - 中间件组：Plugins（工具调用循环里的横切行为）
- **动机是 open world**：任务在设计 harness 时根本没出现过，所以不追求"一次调好一个通用 harness"，而是让每个新任务触发一次针对性改进
- **两层递归**：
  1. 第一层（单任务）：初始 harness 跑一遍 → 编辑器提通用型/领域特定型两类建议 → 每个候选在同一任务各跑一次 → 组合器对比行为差异，合成精炼 harness 完成任务。**不需要 ground truth**，靠差异判断哪些改动值得留
  2. 第二层（跨任务）：任务结束后反思，把被采纳的改动与有证据的结论写入持久"改进 harness"，下个任务的编辑器参考它，避免从零开始
- **预算控制**：`--k 1` 单步最省；`--k K --mode parallel` 往宽探（K 个通用 + K 个领域候选再组合）；`--k K --mode sequential` 往深改（连续 K 步精炼）
- **执行器**：支持 [[OpenCode]] 与 [[Codex]]（`--substrate cx` 切换）
- **自报结果**：单步 Harness2 即可让 [[GLM]]-5 与 [[Gemini]] 3.5 Flash 超过各自基础 harness；WorkBuddy-Bench 最高 +11.5 分、LAB 部分通过率 +11.8 个百分点、JobBench +4.5 分；加大第一层预算还能继续涨（均为"最高"数字，非普遍预期）
- **上手**：Linux + Python 3.12 + uv；`harness2-demo --k 2` 零凭证跑本地 demo（确定性编辑器 + 真实 Python 执行）；接真实模型需 Node.js 20+、Google Cloud CLI、`.env`（Vertex AI 项目/模型 ID）与 `gcloud auth application-default login`；LAB 要 Pandoc/Poppler，WorkBuddy-Bench 要 Docker
- **命令链**：`harness2-setup <bench>` → `harness2-check` → `harness2 --bench ... --k ... --mode ...` → `harness2-judge` → `harness2-report`；judge/report 必须与精炼步同基准、同执行器、同子集、同 `--k`/`--mode`/种子；结果落 `runs/`，可断点续跑
- **三条风险**：①要花钱（每任务多候选，`--k` 大成本涨得快）；②网络默认开放、Codex 沙箱关，公开基准评分标准可能被搜到，正式评测前必须限网；③非 Google 官方支持产品
- **方法论价值（大于分数）**：把"改一版、跑一下、感觉好点就留、不对就回滚，中间不留判断依据"的手工调参，变成"提出修改 → 跑一遍看差异 → 沉淀有证据的结论"的可记录、可积累流程

## 关联连接
- [[Harness]] — 被优化的对象
- [[HarnessEngineering]] — harness 工程实践
- [[递归式自我改进]] — 两层递归的思想同源
- [[OpenCode]] / [[Codex]] — 支持的执行器
- [[GLM]] / [[Gemini]] — 被评测模型
- [[Subagent]] — 委派组对应机制
- [[ContextEngineering]] — 上下文组所属领域
- [[Google]] — 出品方（Google Research）
- [[摘要-harness2自进化框架]] — 来源
