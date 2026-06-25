---
title: "Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23915"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.35
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23915  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.35

arXiv:2606.23915v1 Announce Type: new Abstract: Practice often treats automatic metrics for attribution in LLM retrieval-augmented generation as interchangeable. We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. In the construct with the most multi-dataset human-labeled coverage -- generated-answer attribution (AttributionBench's four source datasets, n = 1,610, with independent HAGRID, n = 2,150) -- none does: the per-dataset metric rankings invert (Kendall tau = -0.64, p = 0.031 on AttributedQA vs. LFQA), and an off-the-shelf NLI scorer that is best on short-claim AttributedQA (AUROC 0.90) collapses to AUROC 0.53 (chance) on long-form LFQA, where BERTScore wins (0.91); the flip is not a length or truncation artifact. This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. A prompt-based LLM judge avoids the chance-level collapses the automatic scorers suffer (no LFQA collapse) but is not uniformly best, ~100x costlier, and non-deterministic -- relocating, not removing, the validation burden.


---
> 原文链接: https://arxiv.org/abs/2606.23915