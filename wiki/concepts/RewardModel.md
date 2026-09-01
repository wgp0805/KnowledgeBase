---
title: "RewardModel"
type: concept
tags: [RLHF, 奖励建模, 后训练, 偏好建模]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
Reward Model（奖励模型）是 RLHF 中的关键组件：输入 Prompt + 模型回答，输出标量奖励分数，量化回答符合人类偏好的程度。训练数据为偏好对（同一输入、更好回答、更差回答）。

## 关键信息
### LLM 场景角色
- **Reward 来源**：Reward Model 打分 / Rule-based Verifier（代码运行结果、数学答案验证）
- **训练数据**：偏好对，人工标注或模型生成多回答后人工筛选
- **DPO 对比**：DPO 直接用偏好对优化策略，省去 Reward Model 训练
- **RLVR 趋势**：代码/数学等可验证领域，用执行结果直接给奖励，无需主观 RM

### 训练目标
通常用 Bradley-Terry 模型：`P(回答1优于回答2) = σ(r_1 - r_2)`，最大化偏好对的似然。

### PPO 中的使用
PPO Actor 更新时，Reward Model 提供的 r_t 作为即时奖励，配合 Critic 估计的 V(s_t) 计算 TD residual → GAE → 优势估计。

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[RLHF]] — 核心组件
- [[PPO]] — 使用 RM 奖励的算法
- [[DPO]] — 省去 RM 的替代方案
- [[RLVR]] — 可验证奖励替代 RM
- [[后训练]] — 训练阶段
- [[偏好对]] — 训练数据形式