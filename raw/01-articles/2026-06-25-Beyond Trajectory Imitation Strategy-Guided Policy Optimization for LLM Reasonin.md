---
title: "Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning"
source: "arXiv AI"
url: "https://arxiv.org/abs/2606.24064"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.8
tags: ["AI", "论文", "研究"]
auto_captured: true
---

# Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning

> **来源**: arXiv AI  
> **链接**: https://arxiv.org/abs/2606.24064  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.8

arXiv:2606.24064v1 Announce Type: new Abstract: Distilling reasoning capabilities from strong to weak language models typically involves imitating specific solution trajectories, effectively transferring what to answer rather than how to reason. This trajectory-level imitation encourages memorization of instance-specific steps rather than acquisition of transferable problem-solving skills, limiting generalization to novel problems. We propose Strategy-Guided Policy Optimization (SGPO), which replaces instance-level trajectory imitation with reusable strategy distillation. SGPO extracts structured strategy descriptions from strong-model responses and, for each problem, constructs both autonomous and strategy-guided trajectories to enable direct comparison of the model's behavior with and without strategic guidance. The framework then addresses two key questions. For how to distill, a token-level forward-KL objective selectively transfers the distributional shift induced by strategy conditioning into the unguided policy, with proximal constraints ensuring stability. For when to distill, adaptive instance-level weighting strengthens guidance when autonomous exploration falls short and reduces it as the model's own competence grows. Experiments on four mathematical benchmarks across two model families show that SGPO consistently outperforms SFT, on-policy RL, and hybrid-policy baselines, improving the average score by 2.2 points over the strongest baseline on Qwen2.5-7B-Instruct. Analysis reveals that the forward-KL objective provides an inherently selective distillation signal that outperforms direct trajectory imitation, and that strategy distillation exhibits complementary scaling with base model capability.


---
> 原文链接: https://arxiv.org/abs/2606.24064