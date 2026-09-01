---
title: "PolicyGradient"
type: concept
tags: [强化学习, 基础理论, REINFORCE, 策略梯度]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
Policy Gradient（策略梯度）是直接优化策略参数 θ 以最大化期望回报的方法。基础形式 REINFORCE：对每步 log-prob 梯度求和，用整条轨迹回报加权。

## 关键信息
### 核心公式推导
```
J(θ) = E_{τ~π_θ}[R(τ)]                          # 目标：期望回报
∇J(θ) = E_{τ~π_θ}[ (Σ_t ∇log π_θ(a_t|s_t)) R(τ) ]  # Log-derivative trick
```

### 核心缺陷
1. **Credit Assignment 粗糙**：整轨迹回报加权所有步骤，无法区分单步贡献
2. **方差极大**：单标量回报包含大量噪声，梯度估计不稳定
3. **采样效率低**：On-policy，每次更新需重新采样，环境交互成本高

### 改进链路
REINFORCE → Reward-to-go → Baseline/Advantage → GAE → Actor-Critic → 重要性采样/Off-policy → TRPO约束 → PPO-Clip/Penalty → GRPO(省Critic)

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[PPO]] — 终极工程化形态
- [[REINFORCE]] — 基础形式
- [[CreditAssignment]] — 核心缺陷
- [[GAE]] — 优势估计改进
- [[ActorCritic]] — 架构改进
- [[重要性采样]] — 采样效率改进
- [[RLHF]] — 所属范式