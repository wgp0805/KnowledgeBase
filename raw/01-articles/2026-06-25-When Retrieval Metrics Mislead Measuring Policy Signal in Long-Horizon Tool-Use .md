---
title: "When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23937"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.25
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23937  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.25

arXiv:2606.23937v1 Announce Type: new Abstract: Exact-match retrieval recall is often used as a proxy for whether a retriever supplies useful policy context to a downstream decision model. We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. We then replace the benchmark-designated policy clause with the top-ranked clause retrieved from decision-time context. Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. We do not detect a macro-F1 difference between retrieved and gold clauses in this configuration, although the interval remains too wide to establish non-inferiority. The same qualitative pattern appears with a second retriever and at 7B, while varying across fine-tuning configurations. These results indicate that exact-match clause recall can underestimate downstream policy utility in this benchmark setting, motivating evaluation with retrieved policies in the classification loop rather than recall alone.


---
> 原文链接: https://arxiv.org/abs/2606.23937