---
title: "Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23700"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.35
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23700  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.35

arXiv:2606.23700v1 Announce Type: new Abstract: Emergent misalignment (EM) has been linked to the activation of misaligned persona vectors and evil character traits, suggesting that EM operates through disruption of the model's aligned character rather than direct learning of harmful content. Motivated by this connection, we study self-generated text recognition (SGTR) finetuning as a character-targeted intervention that is distinct from existing in-training defenses. We conduct two-stage finetuning experiments across three models (GPT-4.1, Qwen2.5-32B-Instruct, Seed-OSS-36B-Instruct) and multiple EM datasets to compare SGTR finetuning against benign finetuning baselines (correct domain-specific data, general knowledge, and word counting) to find it an effective defense in both reversal and prevention settings. We find that all interventions produce comparable EM reversal, but only when restoring capabilities that EM had degraded. For prevention, only SGTR finetuning consistently reduces misalignment without exacerbating any individual metric, suggesting that character fortification specifically drives prevention. We provide further evidence for EM's relation to the LLM's default character by showing that EM finetuning induces diversity into the LLM's identity self-reports, artificially corrupting self-recognition exacerbates misalignment caused by EM finetuning, and that removing the model's identity-bearing system prompt substantially reduces the effect of EM finetuning. Together, these findings reframe EM not as the adoption of a coherent misaligned persona but as the destabilization of aligned character.


---
> 原文链接: https://arxiv.org/abs/2606.23700