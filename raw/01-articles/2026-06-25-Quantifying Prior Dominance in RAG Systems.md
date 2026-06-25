---
title: "Quantifying Prior Dominance in RAG Systems"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23695"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.4
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# Quantifying Prior Dominance in RAG Systems

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23695  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.4

arXiv:2606.23695v1 Announce Type: new Abstract: Retrieval-Augmented Generation (RAG) grounds Large Language Models in external knowledge, yet current evaluations rely on discrete heuristics that suffer from ''epistemic blindness'' - failing to distinguish genuine contextual information extraction from parametric memory recall. To address this, we introduce the Normalized Context Utilization (NCU) metric, leveraging continuous token log-probabilities across zero-shot, oracle, and adversarial conditions to strictly quantify contextual information gain. Evaluating architectures ranging from 1.5B to 72B parameters alongside a proprietary commercial API reveals that for strict factual extraction (without Chain-of-Thought reasoning), traditional scaling laws exhibit extreme diminishing returns: highly efficient Small Language Models (SLMs) match or outperform high-capacity architectures. Furthermore, we demonstrate that ``Prior Dominance'' correlates with model scale and proprietary alignments. The evaluated commercial API not only overrode explicit external evidence in nearly half of adversarial conflicts, but also frequently suffered from systemic confidence collapse (Negative Transfer) when its parametric priors were contradicted. Our findings highlight the structural epistemic advantage and superior contextual adherence of SLMs in strict extraction workflows.


---
> 原文链接: https://arxiv.org/abs/2606.23695