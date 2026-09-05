---
title: "ActorCritic"
type: concept
tags: [强化学习, 网络架构, PPO, 后训练]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
Actor-Critic 是强化学习的经典架构：Actor（策略网络）输出动作分布，Critic（价值网络）评估状态价值，Critic 为 Actor 提供低方差的优势估计信号，二者协同更新。

## 关键信息
### LLM 场景下的结构
| 组件 | 结构 | 输出 | 作用 |
|------|------|------|------|
| **Actor** | Transformer + LM Head | 词表分布 π_θ(a_t|s_t) | 生成下一个 Token |
| **Critic** | Transformer + Value Head | 标量 V_φ(s_t) | 预测当前前缀未来累计 Reward |

### 两种组织方式
1. **独立双 Transformer**：Actor 和 Critic 参数完全独立，Critic 可自由学习价值表示，但显存/计算成本翻倍
2. **共享 Backbone**：共享 Transformer 主干，分别接 LM Head 和 Value Head，省显存但 Actor/Critic Loss 耦合更新

### 核心关系
- Actor 回答："当前前缀下，下一个 Token 应该生成什么？"
- Critic 回答："当前已生成到这个前缀，继续生成未来大概能拿多少累计 Reward？"
- Critic 训练目标：最小化 TD residual 平方，满足 Bellman 一致性
- Critic 越准 → Actor 优势估计越稳 → 策略更新方差越小

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[PPO]] — 采用该架构的算法
- [[GRPO]] — 省去 Critic 的简化变体
- [[GAE]] — 优势估计方法
- [[TD残差]] — Critic 训练目标
- [[后训练]] — 训练阶段