---
title: "EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL"
source: "arXiv CL"
url: "https://arxiv.org/abs/2606.23693"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 0.6
tags: ["NLP", "论文", "研究"]
auto_captured: true
---

# EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL

> **来源**: arXiv CL  
> **链接**: https://arxiv.org/abs/2606.23693  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.6

arXiv:2606.23693v1 Announce Type: new Abstract: Text-to-SQL enables users to query databases using natural language by generating executable SQL queries. Recent methods have increasingly adopted Large Language Models based reinforcement learning (RL) to leverage execution feedback for training. However, existing RL methods assign uniform query-level rewards to all clauses in a SQL query, treating correct and incorrect clauses equally. This coarse-grained reward design leads to insufficient learning signals for correct SQL generation. To address this issue, we propose EXPO-SQL (EXecution-based clause-level Policy Optimization for Text-to-SQL) which provides fine-grained supervision through clause-level rewards. To assign clause-level rewards, our method identifies erroneous clauses by analyzing execution results, including error messages and clause-wise incremental execution. Experiments on widely-used Text-to-SQL benchmarks demonstrate that EXPO-SQL significantly outperforms existing supervised fine-tuning, prompting, and RL-based methods through fine-grained clause-level learning. Our code is available at https://github. com/jhn25/EXPO-SQL.


---
> 原文链接: https://arxiv.org/abs/2606.23693