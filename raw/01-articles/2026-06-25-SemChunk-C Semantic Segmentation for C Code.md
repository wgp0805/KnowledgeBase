---
title: "SemChunk-C: Semantic Segmentation for C Code"
source: "arXiv SE"
url: "https://arxiv.org/abs/2606.23697"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.45
tags: ["软件工程", "论文", "研究"]
auto_captured: true
---

# SemChunk-C: Semantic Segmentation for C Code

> **来源**: arXiv SE  
> **链接**: https://arxiv.org/abs/2606.23697  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.45

arXiv:2606.23697v1 Announce Type: new Abstract: Semantic segmentation of code written in a C-family language remains a challenging problem, due to the language's complex syntax, macro expansion, and irregular structural patterns. Existing chunking methods, such as fixed-sized windows, heuristic splitting, and syntax-based tools, often fail to capture meaningful functional units, limiting the efficacy of retrieval and other downstream LLM driven tasks. In this paper, we address the problem of chunking in C-related languages. First, we define a set of code chunk categories. Second, we train an LLM-based classifier to a) identify chunk boundaries, and b) assign each chunk a descriptive functional attribute (a category), which can be useful for downstream tasks. By leveraging the LLM's ability to capture semantic context within the code, we assume flexible chunk boundaries, allowing to adapt to the specific structure and context of each instance. Third, we introduce SemChunk-C, a family of lightweight language models for semantic chunking of C-related files (.c, .cpp, .h, .cs, etc.). These models are based on the first four Ettin encoders [1] with 17M, 32M, 68M, and 150M parameters. Despite their relatively small size, they are capable of identifying cohesive code units, such as data structures, interface blocks, and other components. Furthermore, we demonstrate the robustness of our approach on real-world code, including challenging constructs such as nested definitions and macros. We test our approach on various datasets, and show that it achieves high boundary accuracy and semantic coherence, matching or outperforming chunkers that are based on much larger code-oriented LLMs. We also validate the improved performance of the downstream tasks on a few curated benchmarks.


---
> 原文链接: https://arxiv.org/abs/2606.23697