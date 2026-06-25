---
title: "Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability?"
source: "arXiv AI"
url: "https://arxiv.org/abs/2606.24026"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.45
tags: ["AI", "论文", "研究"]
auto_captured: true
---

# Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability?

> **来源**: arXiv AI  
> **链接**: https://arxiv.org/abs/2606.24026  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.45

arXiv:2606.24026v1 Announce Type: new Abstract: Mechanistic interpretability has made substantial progress in automatically localizing circuits, but explaining what localized components do remains labor-intensive and difficult to standardize. In this work, we study whether language model (LM) agents can assist with this explanation problem once a circuit has already been identified. We introduce AgenticInterpBench, a benchmark for circuit explanation built from 84 semi-synthetic transformer circuits with 163 component-level annotations. We propose HyVE (Hypothesize, Validate, Explain), an agentic explainer that analyzes each component through an iterative loop of observation, hypothesis generation, and causal validation, eventually producing a component-level explanation and a circuit-level task description. Across four LM backbones, HyVE recovers useful component- and task-level explanations, but no backbone is uniformly best. Our analysis shows that strong backbones usually form observation-grounded hypotheses, while failures more often arise later in the validation loop, through incomplete validation plans, code execution errors, or unresolved hypotheses. A case study on an arithmetic circuit in Llama-3-8B shows that the same formulation can extend beyond semi-synthetic benchmarks to naturally trained models. Overall, LM agents are promising circuit explainers, but reliable validation remains the key obstacle.


---
> 原文链接: https://arxiv.org/abs/2606.24026