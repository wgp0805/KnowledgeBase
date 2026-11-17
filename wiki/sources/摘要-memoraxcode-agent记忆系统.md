---
title: "摘要-memoraxcode-agent记忆系统"
type: source
tags: [来源, MemoraXCode, AgentMemory, 长期记忆, CodingAgent]
sources: [raw/09-archive/GitHub上开源了一个神级Agent记忆系统，强的有点力离谱！.md]
last_updated: 2026-11-16
---

## 核心摘要
冰河 2026-11-16 介绍开源项目 MemoraX Code（github.com/memorax-ai/memorax-code）：面向代码智能体的长期记忆系统，解决"新开会话项目默契全部归零"的痛点——单纯拉大上下文窗口解决不了，因为窗口分不清调试废话和决定重构的硬约束。**记忆两层**：本地记忆盯代码仓库（代码结构/关键入口/Issue 历史/项目演进），云端记忆存跨任务、跨对话、跨 Agent 的项目经验/开发偏好/失败方案并支持团队共享；**召回按当前任务意图检索**，只喂相关记忆——在 Codex 里沉淀的认知切到 Claude Code 继续生效。核心差异化是**可学习的记忆框架**：不走人工写规则路线（规则一多互相打架），而是构造代码训练数据集 + 记忆评估与奖励信号，让记忆模型自己学"什么值得留、什么过时了、什么时机该召回"，训练体系与用户私有记忆数据隔离。**Procedure Memory（过程记忆）** 从历史开发轨迹自动提取可复用的分析/执行/验证步骤提炼成结构化工程经验（123 个历史任务片段提炼 15 条经验/4 类），3 小时长程任务对比：不开记忆综合得分 11.71（关键检查项 2/13），开启后 70.30（10/13），调用成本降约 22.6%——省的是重复摸索已踩过坑的 token。克制性数据：85.5% 记忆触发与人的判断一致、81.2% 内容获正向反馈。AML（Agent Memory Leaderboard）Coding Track 62 分第一，较 Claude Mem 解题率提升 10%；原生支持 Codex/Claude Code/DeepSeek Harness/OpenCode 四款 Agent；记忆可在官方平台查看/编辑/删除（防黑箱）。内容已并入 [[MemoraXCode]] 与 [[ProcedureMemory]]。

## 关联连接
- [[MemoraXCode]] — 本篇主角（新建实体页）
- [[ProcedureMemory]] — 过程记忆概念（新建）
- [[AgentMemory]] — 所属概念域（增量更新）
- [[Mem0]] — 同域记忆框架对照
- [[冰河]] — 来源作者
- [[ClaudeCode]] / [[Codex]] / [[DeepSeekHarness]] / [[OpenCode]] — 原生适配的四大 Coding Agent
- [[AgentEval]] — AML 榜单所属的 Agent 评测域
- [[KVCache]] — 对照：Latent Memory 路线（MemoraX 走的是外部文本检索注入路线）
