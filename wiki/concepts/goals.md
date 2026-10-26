---
title: "goals"
type: concept
tags: [AI Agent, 任务管理, 验证, Codex, MiMo Code]
sources: [raw/09-archive/如何把Codex用到极致.md, raw/09-archive/小米版Claude Code正式发布，这次开源能给到夯.md, raw/09-archive/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md]
last_updated: 2026-09-28
---

## 定义
Goals（目标）是 AI Agent 中带验证器的长跑型任务，Agent 持续向一个明确的、可验证的终点推进，而非一次性对话指令。

## 关键信息

### 通用概念
- **弱目标**："按这个 Markdown 里的计划实现一下"（无验证器，只是愿望）
- **强目标**："把这个内部工具从 Python 迁到 Rust。目录要建好，功能要对齐，单元测试全部通过才算完成"（有验证器）
- 没有验证器的目标只是愿望。测试、benchmark、复现脚本、端到端流程把"继续努力"变成"有没有更接近完成"
- 不是任务越大越适合交给 Agent，而是越能被验证的任务，越适合让 Agent 长时间推进

### MiMo Code Goal 实现
- **机制**：用户设定自然语言描述的停止条件（如"所有测试通过且代码已提交"），Agent 每次尝试终止时，系统自动发起独立模型调用审查完整对话历史，判断条件是否真正满足
- **未满足**：把具体差距反馈给 Agent，让它继续干
- **不可能完成**：判定为不可能并退出
- **验证者独立性**：不参与实际工作，不会对 Agent 已完成部分产生认同偏差，每次获得与 Agent 完全相同的上下文（包括工具实际输出）
- **死循环控制**：误拦比漏放更常见，整体死循环概率小于 0.5%，到达上限后自动退出

### 与 Max Mode 的维度差异
- [[max-mode]] 是并行维度，同一步花 N 倍算力选最优
- [[goals]] 是串行维度，在同一个任务上做更长的自我检查和执行
- 两者可以同时启用

### Claude Code 的 /goal：目标状态收敛（v2.1.139，2026-09）
来自 [[摘要-claude-code-agent视图与goal]]。`/goal <目标>` 设置后，Claude 每个 turn 结束自动评估是否达到目标状态，不满足就自动发起下一 turn，直到满足或手动停止；界面 overlay 显示已用时间、turn 数、token 消耗。与普通 prompt 的本质区别是**控制权归属**：普通指令每个 turn 结束后等用户决定是否继续，`/goal` 把「是否完成」的判断权交给模型——架构上与 Kubernetes Reconcile Loop（设定目标状态、执行者自主收敛）同构，但判断基于语言理解而非精确状态，存在误判可能。

- **适用**：测试修复循环（jest 退出码 0）、代码质量收敛（ESLint 0 error）、类型检查修复（tsc --noEmit 无报错）等输出精确可读的场景
- **不适用**：目标模糊或主观（「把这个模块写得优雅」）——模型可能无限循环或自欺欺人宣称完成
- **写法铁律**：目标越具体越可验证执行质量越高，把验证命令与期望输出写进 goal（`curl health 返回 ok 且 npm test 无失败`），否则模型可能走捷径（如注释掉测试让它"通过"）
- 与 Codex Goals、MiMo Code Goal 同属「带验证器的长跑任务」，只是验证由模型自己判读

## 关联连接
- [[摘要-把Codex用到极致]] — Codex 来源
- [[摘要-mimo-code发布]] — MiMo Code 来源
- [[摘要-claude-code-agent视图与goal]] — Claude Code /goal 来源
- [[Codex]] — Codex 所属产品
- [[MiMoCode]] — MiMo Code 所属产品
- [[ClaudeCode]] — /goal 所属产品
- [[agent-view]] — 同版本的 Agent 视图
- [[durable-threads]] — 长线程承载 goals 的持续上下文
- [[automations]] — 定期执行的自动化任务
- [[max-mode]] — 并行维度的可靠性机制
- [[dynamic-workflow]] — 复杂任务的流程编排
