---
title: "RLHF"
type: concept
tags: [AI, LLM, 对齐, 强化学习, RLHF]
sources: [raw/01-articles/2026-07-07-Transformer、"训练-微调"范式-AI 相关概念之（核心技术与架构） - 橙子家.md, raw/01-articles/2026-08-27-LLM后训练算法梳理(1)-PPO算法 - bradinz.md]
last_updated: 2026-08-28
---

## 定义
RLHF（Reinforcement Learning from Human Feedback，人类反馈强化学习）是微调的第二阶段，目标是让 AI 学习"职场规矩与价值观"，确保回答专业、有同理心，且不输出有害或违规内容。

## 关键信息

### 演进路线（2025-2026 趋势）
- **传统 RLHF**：人类对模型输出打分，训练奖励模型，再用强化学习优化
- **DPO（Direct Preference Optimization）**：直接偏好优化，无需训练奖励模型，简化流程
- **RLVR（Reinforcement Learning with Verifiable Rewards）**：可验证奖励强化学习，在代码、数学等逻辑领域，AI 做对了题目系统通过代码运行结果直接给予客观奖励，无需人类主观打分，大幅提升硬核推理能力

### 在微调阶段中的位置
SFT（专业技能）→ **RLHF/DPO/RLVR（价值观对齐）** → 可用的 Chat/Agent 模型

### 类比
- SFT 后的模型 = "专业课学完的学生"
- RLHF = "学习医德和职场礼仪"

## 关联连接
- [[SFT]] — RLHF 的前置阶段
- [[微调]] — 所属大类
- [[基座模型]] — 训练链路起点
- [[摘要-transformer-训练微调范式]] — 来源
- [[摘要-llm后训练算法-ppo详解]] — PPO 算法详解来源
- [[PPO]] — RLHF 核心优化算法
- [[GRPO]] — PPO 简化变体
- [[DPO]] — 非 RL 对齐替代方案
- [[RLVR]] — 可验证奖励 RL 新范式
