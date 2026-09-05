---
title: "GRPO"
type: concept
tags: [强化学习, 后训练, PPO变体, 无Critic]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
GRPO（Group Relative Policy Optimization）是 PPO 的简化变体，核心创新：利用同一 Prompt 下多条 Rollout 的相对 Reward 直接构造 Advantage，**完全省去 Critic/Value Model**，大幅降低显存和计算成本。

## 关键信息
- **动机**：PPO 需维护 Critic 为每个 Token 状态估计 V(s_t) 再计算 GAE，显存和计算成本高
- **方法**：同一 Prompt 采样 G 条回复，按 Reward 排序，相对排名构造 Advantage
- **优势**：
  - 无需 Critic 网络，参数量减半
  - 无需 GAE 计算，流程简化
  - 自然适配 LLM 批量生成评分场景
- **代价**：需要同 Prompt 多次采样（G 通常 4-16），计算量转移到推理端

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[PPO]] — 原算法
- [[RLHF]] — 所属范式
- [[后训练]] — 训练阶段
- [[ActorCritic]] — PPO 使用的架构（GRPO 省去 Critic）
- [[采样效率]] — 权衡点