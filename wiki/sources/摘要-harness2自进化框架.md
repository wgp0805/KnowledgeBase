---
title: "摘要-harness2自进化框架"
type: source
tags: [来源, Harness, Agent, 自动优化, Google]
sources: ["raw/09-archive/谷歌开源的AI Harness自进化框架，在GitHub短短一个月狂揽25K+Star，太强了！！.md"]
last_updated: 2026-11-24
---

## 核心摘要
冰河 2026-11-24 介绍 Google Research 开源的 [[Harness2]]（github.com/google-research/harness2，一个月 25K+ Star）。前提判断：同一个模型，换个提示词写法、工具描述措辞、记忆策略，跑出来的结果差异可能比换模型还大；而调 harness 一直是靠人反复试的手艺活，没有系统方法。Harness2 的做法是**不训练模型、权重全程锁死，只把 harness 变成可迭代优化的对象**。

它先把 harness 拆成 8 个可单独编辑的组件、按运行时职责分 4 组：上下文组（系统提示词、Guardrails、Memory、Skills）、工具接口组（工具说明、Scripts）、委派组（Subagents）、中间件组（Plugins）——把"改 harness"从模糊动作落到"这次改哪一块"。动机是标题里的 **open world**：Agent 面对的任务在设计 harness 时根本没出现过，所以不追求"一次调好一个通用 harness"，而是让每个新任务触发一次针对性改进。

架构是两层递归：**第一层管当下任务**——初始 harness 跑一遍 → 编辑器提两类修改建议（通用型/领域特定型）→ 每个候选在同一任务上各跑一次 → 组合器对比几次运行的行为差异，合成精炼 harness 完成任务。关键设计是**不需要标准答案**：没有 ground truth 就没有打分反馈，靠"不同壳改动下的行为差异"判断哪些改动值得留，这在真实场景比依赖评分实用得多。**第二层管以后的任务**——每个任务跑完做反思，把被采纳的改动与有证据支持的结论写进持久的"改进 harness"，下个任务的编辑器参考它，避免从零开始。

预算通过 `--k` 控制：`--k 1` 走一遍三步最省；`--k K --mode parallel` 往宽探（K 个通用 + K 个领域候选再组合）；`--k K --mode sequential` 往深改（连续 K 步精炼）。执行器支持 [[OpenCode]] 与 [[Codex]]（`--substrate cx` 切换）。项目自报在 JobBench（专业工作任务）、LAB（法律）、WorkBuddy-Bench（办公/网页/代码）上，单步 Harness2 就能让 GLM-5 与 Gemini 3.5 Flash 超过各自基础 harness，最大提升为 WorkBuddy-Bench 的 11.5 分与 LAB 部分通过率的 11.8 个百分点、JobBench 4.5 分；加大第一层预算还能继续涨（均为"最高"数字，不是普遍预期）。

上手：Linux + Python 3.12 + uv，`harness2-demo --k 2` 可零凭证跑本地 demo（确定性编辑器 + 真实 Python 执行，两种递归都演示）；接真实模型需 Node.js 20+、Google Cloud CLI、`.env`（Vertex AI 项目与模型 ID）与 `gcloud auth application-default login`；LAB 额外要 Pandoc/Poppler，WorkBuddy-Bench 要 Docker。命令链 `harness2-setup` → `harness2-check` → `harness2 --bench lab --k 1 --mode parallel --only-domains ...` → `harness2-judge` → `harness2-report`，judge/report 必须与精炼步保持同基准、同执行器、同子集、同 `--k`/`--mode` 与随机种子，结果落 `runs/`，可断点续跑。

三条提醒：①**要花钱**，每任务多候选执行，`--k` 开大成本涨得快；②**网络默认开放**，Codex 运行时沙箱是关的，公开基准的评分标准可能被搜到，正式评测前必须配网络限制，否则结果不干净；③**不是 Google 官方支持产品**（Apache 2.0，不在 Google 开源漏洞奖励范围）。

## 关联连接
- [[Harness2]] — 项目本身
- [[Harness]] — 被优化的对象
- [[HarnessEngineering]] — harness 工程实践
- [[递归式自我改进]] — 两层递归的思想同源
- [[OpenCode]] / [[Codex]] — 支持的执行器
- [[GLM]] / [[Gemini]] — 被评测的模型
- [[ContextEngineering]] — 上下文组（提示词/Guardrail/Memory/Skills）所属领域
- [[Subagent]] — 委派组对应机制
