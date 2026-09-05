---
title: "摘要-Anthropic官方指南-AI-Native-SDLC"
type: source
tags: [来源, AI产品, SDLC, Anthropic, 工程实践]
sources: [raw/01-articles/2026-08-26-Anthropic 官方指南：AI Native 开发手册.md]
last_updated: 2026-08-27
---

## 核心摘要
编译自 Anthropic 官方博客《The AI-Native SDLC Playbook》（2026-08-21，作者 Louis Claxton）。核心论点：代码不再是瓶颈，瓶颈转移到构建阶段左右两侧（规划、审查/测试、部署），管控手段与现实脱节，治理成本上升。AI 原生 SDLC 把线性流程改造成循环，AI 嵌入每个节点，核心概念是"提交的产物（committed artifact）"——每个阶段结束往版本控制写一个产物（intent.md → spec.md → plan.md → 代码 diff 及测试 → 带 REVIEW.md 审查结论的 PR → 事故记录），下一阶段从读取该产物开始。手册按六阶段（规划/设计/构建/测试/部署/运维）给出 Play，涵盖 intent.md 捕获意图、Plan Mode 默认起点、CLAUDE.md 机构知识、Skills 可执行化、Hooks 护栏、并行会话与子 Agent、CI 持续 Eval、AI 参与 PR 审查、Hooks 作为审批门禁、Claude Tag 闭合循环等。

## 关键信息
- **关键转变**：瓶颈从构建转移到规划/审查/部署；逐行审查跟不上 agent 产出；治理成本上升
- **committed artifact**：intent.md（意图）→ spec.md（需求设计）→ plan.md（实施计划）→ 代码 diff + 测试 → PR + REVIEW.md → 事故记录，commit 链即审计链
- **intent.md**：发起人与 Claude 头脑风暴产出 proto-spec，模板可编码为 skill
- **Plan Mode**：工程师在 plan mode 下给 Claude spec.md，反复迭代计划直到满意，提交为 plan.md，接受后 Claude 实施
- **CLAUDE.md**：新人入职第一天需要知道的东西；"Claude 犯同一个错两次，纠正就进 CLAUDE.md"；控制一页以内
- **Skills**：需要一致性执行的机构知识写成 skill，放 .claude/skills/，策略变化时集中更新
- **Hooks**：Skill 是建议性管控，Hook 是确定性层；构建阶段阻止受保护路径编辑、跑 formatter/linter、挡凭证
- **并行会话与子 Agent**：并行会话用各自 git worktree；子 agent 定义在 .claude/agents/，有独立上下文和工具权限
- **反馈回路**：始终给 Claude 验证工作的方式；修 bug 先写失败测试；修代码的 agent 不能同时削弱对那段代码的检查
- **CI 持续 Eval**：20-50 个真实任务写成 eval；每个生产事故变成 eval 永久留在套件
- **AI 参与 PR 审查**：Claude 既做审查者也做被审查者；REVIEW.md 定义审查维度和 Important/Nit 标准
- **Hooks 作为审批门禁**：团队 hook 放 .claude/settings.json，不可协商 hook 放 managed settings
- **回滚**：应该是流水线里演练最多的路径
- **闭合循环**：确定性脚本监控生产，控制带突破时调用 Claude；bands.yaml 定义 1σ/2σ/3σ 响应分级
- **Claude Tag**：Slack/Teams 里 Claude 以自己身份成为频道成员，第一响应事故

## 关联连接
- [[AINativeSDLC]] — 本文核心概念，AI 原生软件开发生命周期
- [[Anthropic]] — 指南发布方
- [[ClaudeCode]] — 指南核心工具
- [[CLAUDE-md]] — 机构知识文件
- [[Skills]] — 机构知识可执行化
- [[Hooks]] — 确定性护栏
- [[MCP]] — 模型上下文协议
- [[Subagent]] — 子 Agent
- [[AutoMemory]] — 自动记忆
- [[Checkpoint]] — 检查点恢复
- [[PlanMode]] — 计划模式
- [[AutoMode]] — 自动模式
- [[IntentMd]] — 意图文件
- [[SpecMd]] — 需求设计文件
- [[PlanMd]] — 实施计划文件
- [[ReviewMd]] — 审查指令文件
- [[AgentEval]] — Agent 评测
- [[ClaudeTag]] — Claude 频道成员
- [[Bands]] — 监控响应分级
- [[LouisClaxton]] — 原文作者
- [[SDLC]] — 软件开发生命周期
