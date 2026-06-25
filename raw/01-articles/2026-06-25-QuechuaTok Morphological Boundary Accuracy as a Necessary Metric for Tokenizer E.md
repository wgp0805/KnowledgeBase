---
title: "QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23943"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.55
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23943  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.55

arXiv:2606.23943v1 Announce Type: new Abstract: Tokenization is a foundational step in NLP pipelines, yet standard evaluation metrics such as fertility rate fail to capture morphological correctness for agglutinative languages. We present QuechuaTok, a systematic benchmark comparing four tokenization strategies - BPE, Unigram LM, WordPiece, and a morphology-aware PRPE tokenizer - for Southern Quechua (quz), a low-resource agglutinative language spoken by 8-10 million people in South America. Using a 200k-sentence corpus and the SQUOIA finite-state morphological analyzer (Rios, 2016) as silver standard, we evaluate three metrics: fertility rate, OOV rate, and morphological boundary accuracy (MorphAcc). Our results show that BPE achieves the lowest fertility rate (1.636 at 16k vocab) by memorizing surface word forms, while achieving only 6.67% MorphAcc. PRPE achieves 83.33% MorphAcc - the highest of all systems - demonstrating that fertility rate alone is insufficient to evaluate tokenizers for agglutinative languages. All code and models are publicly available at kaggle.com/code/macmaky/quechuatok


---
> 原文链接: https://arxiv.org/abs/2606.23943