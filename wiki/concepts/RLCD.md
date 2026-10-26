---
title: "RLCD"
type: concept
tags: [训练方法, 强化学习, 判断模型]
sources: [raw/01-articles/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的"判断模型"路线靠谱吗？.md, raw/01-articles/为什么越来越多人用 Jev ？.md, raw/09-archive/2026-09-22-大厂后训练视角看Jev模型的更新（大白话）.md]
last_updated: 2026-09-23
---

## 定义
RLCD（Reinforcement Learning for Calibrated Decisions，面向校准决策的强化学习）是Jev的训练方法核心。与RLHF优化"人类觉得好的答案"不同，RLCD优化"带诚实概率的答案"——它说95%的时候，统计意义上真的有95%是对的。

## 关键信息
- 不是像RLHF那样优化"人类觉得好的答案"
- 而是优化"带诚实概率的答案"
- 使Jev的置信度经过校准，具有统计意义上的可信度
- 校准误差仅0.07（基线模型0.14-0.18）
- 保留最自信的一半答案，平均准确率提升7.6个百分点

## 关联连接
- [[Jev]] — 使用RLCD训练的模型
- [[RLHF]] — 人类反馈强化学习（对比）
- [[置信度校准]] — RLCD的核心目标
- [[校准误差]] — 衡量置信度可信度
- [[摘要-jev判断模型靠谱吗]] — RLCD 判断模型路线梳理来源
