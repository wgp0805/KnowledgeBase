---
title: "BitterLesson"
type: concept
tags: [AI理论, Scaling, 强化学习, 方法论]
sources: [raw/01-articles/2026-09-29-关于 AI Agent，为什么我的想法可能不靠谱？——重读〈The Bitter Lesson〉 - ahfuzhang.md]
last_updated: 2026-10-08
---

## 定义
《The Bitter Lesson》（苦涩的教训）：[[RichardSutton]] 2019 年写的研究随笔，核心观点是——AI 历史上最终取得巨大进步的，往往不是人类把自己的知识精巧地写进系统，而是那些能够随着计算量增加而不断变强的通用方法（特别强调搜索 search + 学习 learning）。"苦涩"在于：研究者精心编码的人类知识优势，长期总是被利用更多计算的通用算法抹平，这对相信"人类理解的问题结构非常重要"的研究者是个很难接受的结论。

## 关键信息
- **关键词 scaling**：好方法的性质是"更多 compute / data / experience 能持续转化成更强 intelligence"；专家规则型算法 CPU×10 只涨 5%，可搜索/学习型算法 CPU×10 涨 50% 且随算力继续涨——长期 B 必赢
- **历史证据**：象棋（中心控制/兵型等专家知识 → 搜索+评估函数+更多计算）、围棋（AlphaGo/AlphaZero：神经网络学习 + 蒙特卡洛树搜索 + 海量计算超过人工规则）、计算机视觉、语音识别；NLP 从人工语法/句法规则走向"大量文本 + 神经网络 + 梯度下降 + GPU → Transformer → GPT"，模型内部的语法/概念/推理多是训练出来的而非程序员写进去的
- **正确理解**：不是说领域知识完全没用，而是不要让大量人工知识成为系统性能增长的主要来源；工程师式总结——不要过度优化 human knowledge，优化 scaling law
- **对 AI Agent 的推论**（源自 [[摘要-重读苦涩的教训]]）：Agent 上的能力提升相比模型智能提升不值一提，下一代模型智能会直接抹平过去几年在 Agent 编排上的努力；提示词工程 → 上下文工程 → Harness 工程 → Loop Engineering → 图工程等新词汇本质都是在 Agent 上强化，终被模型吸收；别指望靠长期投入 Agent 研发建立壁垒，Agent 更像薄薄的胶水层；OpenAI、Anthropic 敢开源 Agent 正因强化 Agent 与该教训矛盾
- **应用争议**：该文被用来批判腾讯 [[WorkBuddy]] 的战略——若其壁垒建立在人为编排的 workflow/harness 上，会随基础模型进步快速贬值（这是批评者的观点，非公认结论）
- **暴论延伸**：有了 RSI（递归自我改进）后，人类经验对文明发展反而可能是阻碍；human knowledge 不应成为 AI scaling 的主要来源

## 关联连接
- [[摘要-重读苦涩的教训]] — 来源
- [[RichardSutton]] — 提出者
- [[WorkBuddy]] — 被该理论点名批判的产品
- [[AgentHarness]] — 被认为终将被模型吸收的强化方向
- [[AI对齐]] — 相邻的 AI 发展方法论议题
