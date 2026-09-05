---
title: "摘要-llm后训练算法-ppo详解"
type: source
tags: [来源, 原始文件, PPO, RLHF, 后训练, 强化学习, LLM]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 核心摘要
bradinz 系统梳理 LLM 后训练算法系列第一篇，深度解析 PPO（Proximal Policy Optimization）算法在 LLM 语境下的原理、数学推导与工程实现。覆盖：LLM 三阶段训练（预训练→SFT→后训练/RLHF）、RL 变量在 LLM 中的映射、Policy Gradient 基础、Credit Assignment 问题、优势函数与 Actor-Critic 协同、GAE（广义优势估计）、重要性采样与 Off-policy 训练、PPO-Clip 裁剪目标与 PPO-Penalty KL 惩罚、LLM 中 Actor-Critic 网络结构。核心贡献：将 RL 理论（MDP、轨迹、回报、优势函数、TD residual、GAE、重要性采样、TRPO 约束、PPO 裁剪）逐步推导至 LLM 场景，解释为何 PPO 能解决基础 Policy Gradient 的高方差、Credit Assignment 粗糙、采样效率低等问题，以及 GRPO 如何省去 Critic 进一步简化。

## 关联连接
- [[PPO]] — 核心算法
- [[RLHF]] — 后训练范式
- [[后训练]] — 训练阶段
- [[GRPO]] — PPO 简化变体
- [[ActorCritic]] — 网络架构
- [[GAE]] — 优势估计
- [[重要性采样]] — Off-policy 训练基础
- [[CreditAssignment]] — 信用分配问题
- [[KL散度约束]] — TRPO/PPO-Penalty 核心
- [[PolicyGradient]] — 策略梯度基础
- [[RewardModel]] — 奖励建模
- [[SFT]] — 监督微调前置阶段
- [[预训练]] — 基座模型阶段