---
title: "RichardSutton"
type: entity
tags: [人物, 强化学习, AI理论, BitterLesson]
sources: [raw/09-archive/2026-09-29-关于 AI Agent，为什么我的想法可能不靠谱？——重读〈The Bitter Lesson〉 - ahfuzhang.md]
last_updated: 2026-10-08
---

## 定义
Richard Sutton，强化学习奠基者，2019 年写下仅一页半的研究随笔《The Bitter Lesson》（苦涩的教训），该文成为后来讨论 Scaling、LLM、AGI、RL 时被引用最多的短文之一（其个人 publication list 里标注为 "blog, one and a half pages"）。

## 关键信息
- **核心观点**：AI 历史上最终取得巨大进步的，往往不是人类把知识精巧写进系统，而是能随计算量增加不断变强的通用方法——特别强调搜索（search）+ 学习（learning）两类
- **历史模式**：早期研究者把人类知识编码进系统短期有效，但几年十几年后依赖大量计算的通用算法最终超过人工设计系统（象棋、围棋、计算机视觉、语音识别反复重演）
- **关键概念 scaling**：能吸收更多计算/数据/经验并持续转化成更强智能的方法最终胜出；不是说领域知识完全没用，而是不要让人工知识成为系统性能增长的主要来源
- **工程师式总结**：不要过度优化 human knowledge，优化 scaling law——设计一种机制让机器用计算自己学会如何思考

## 关联连接
- [[摘要-重读苦涩的教训]] — 来源
- [[BitterLesson]] — 其提出的理论框架
- [[AGI]] — 该文常被用于讨论的上位议题
