---
title: "PPO"
type: concept
tags: [强化学习, 后训练, RLHF, 算法, LLM]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
PPO（Proximal Policy Optimization，近端策略优化）是 RLHF 阶段核心的强化学习算法，通过重要性采样实现 Off-policy 训练，并用裁剪机制限制单次策略更新幅度，平衡学习效率与训练稳定性。

## 关键信息
### 核心改进链路
1. **Policy Gradient (REINFORCE)**：整轨迹回报加权 log-prob 梯度，Credit Assignment 粗糙、方差大
2. **Reward-to-go**：仅用未来回报评价当前动作，降低方差
3. **Baseline / 优势函数**：引入状态价值函数 V(s) 做基线，衡量"超出平均水平的部分"，进一步降低方差
4. **GAE (Generalized Advantage Estimator)**：λ 超参平衡方差-偏差，TD residual 递归展开
5. **Actor-Critic 协同**：Actor 输出策略，Critic 估计状态价值，为 Actor 提供低方差优势信号
6. **重要性采样 + Off-policy**：旧策略采样数据重复使用 K 次，提升采样效率
7. **PPO-Clip 裁剪**：目标函数 `min(r_t A_t, clip(r_t, 1-ε, 1+ε) A_t)`，防止策略偏离旧策略过远
8. **PPO-Penalty**：KL 散度惩罚项直接加入目标函数，β 自适应调整

### LLM 场景映射
| RL 概念 | LLM 对应 |
|---------|----------|
| Policy π_θ | 语言模型本身 |
| State s_t | Prompt + 已生成 Token（当前上下文） |
| Action a_t | 下一个 Token |
| Reward r_t | Reward Model / Rule-based Verifier 给分 |
| Episode 终止 | EOS / Stop Token / 达到最大长度 |

### 网络结构
- **Actor**：Transformer → LM Head → 词表分布
- **Critic**：Transformer → Value Head → 标量 V(s_t)
- 两种组织：独立双 Transformer（显存高）或共享 Backbone（显存省但优化耦合）

### 关键实现细节
- 一次 Forward 产生所有位置 hidden state，共享 Value Head 得到全序列 V(s_t)
- 相邻 V 计算 TD residual → GAE → 优势估计
- GRPO 吸引点：直接用同 Prompt 多条 Rollout 相对 Reward 构造 Advantage，省去 Critic

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[RLHF]] — 所属范式
- [[后训练]] — 训练阶段
- [[GRPO]] — 简化变体（省 Critic）
- [[ActorCritic]] — 网络架构
- [[GAE]] — 优势估计方法
- [[重要性采样]] — Off-policy 基础
- [[CreditAssignment]] — 核心解决问题
- [[KL散度约束]] — TRPO 约束/PPO-Penalty 形式
- [[PolicyGradient]] — 基础理论
- [[RewardModel]] — 奖励来源
- [[SFT]] — 前置阶段