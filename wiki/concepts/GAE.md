---
title: "GAE"
type: concept
tags: [强化学习, 优势估计, PPO, 方差偏差权衡]
sources: [raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
GAE（Generalized Advantage Estimator，广义优势估计器）通过超参数 λ 平衡优势函数估计的方差与偏差：λ→0 时退化为单步 TD residual（高偏差低方差），λ→1 时退化为完整 Monte Carlo 回报（低偏差高方差）。

## 关键信息
### 数学形式
```
δ_t = r_t + γ V(s_{t+1}) - V(s_t)  # TD residual
Â_t = Σ_{l=0}^{∞} (γλ)^l δ_{t+l}   # GAE 优势估计
```

### λ 的作用
| λ 值 | 行为 | 方差 | 偏差 |
|------|------|------|------|
| λ → 0 | 单步 TD residual | 低 | 高 |
| λ → 1 | 完整 MC 回报 | 高 | 低 |
| 0 < λ < 1 | 加权平衡 | 中 | 中 |

### 工程意义
- PPO 中用 GAE 替代原始回报作为 Actor 更新权重
- Critic 越准确 → TD residual 越小 → 优势估计越稳
- 典型取值：λ = 0.95 ~ 0.97

## 关联连接
- [[摘要-llm后训练算法-ppo详解]] — 来源
- [[PPO]] — 采用 GAE 的算法
- [[ActorCritic]] — Critic 提供 V(s) 用于 GAE
- [[TD残差]] — GAE 基础构件
- [[CreditAssignment]] — 解决细粒度信用分配
- [[后训练]] — 训练阶段