---
title: "Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23881"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.35
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23881  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.35

arXiv:2606.23881v1 Announce Type: new Abstract: Knowledge-Based Visual Question Answering (KB-VQA) requires grounding visual queries to external knowledge beyond directly observable content in images. While recent multi modal large language models (MLLMs) show strong perceptual abilities, they struggle on KB-VQA tasks requiring groundings from both fine-grained entity and evidence levels. Most existing multi-modal retrieval augmented generation (MM-RAG) methods tightly couple entity discrimination and section-level evidence ranking into a single re-ranking stage, leading to high cost and limited generalization. In this work, we revisit existing MM-RAG solutions from a workflow perspective and argue both entity-level and fact-level groundings are key bottlenecks. We observe that although MLLMs often fail under open-ended entity naming, they can better identify the correct entity when selecting from a small set of candidate names. Based on this insight, we propose a simple and training-free identify-before-answer IBA framework that decouples entity identification from section-level re-ranking. Our approach prompts an MLLM to select high-confidence entities using only candidate names, followed by an off-the-shelf textual re-ranker for evidence selection. Experiments on Encyclopedic-VQA and InfoSeek show that our method consistently outperforms fine-tuned multi-modal re-ranking baselines while reducing training and inference complexity. Additional analyses reveal that the improvements arise not only from better entity identification, but also from selecting more informative evidence once correct entity is fixed. Our implementation is made public to ease reproducibility.


---
> 原文链接: https://arxiv.org/abs/2606.23881