---
title: "摘要-github开源ai宝典6本"
type: source
tags: [来源, 开源书籍, AI教材, GitHub]
sources: ["raw/01-articles/2026-10-13-这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。.md"]
last_updated: 2026-10-14
---

## 核心摘要
逛逛GitHub 盘点 6 本在 GitHub 开源的中文 AI 教材：《深入理解 AI Agent》（4.9 万 Star，核心公式 Agent = LLM + 上下文 + 工具，强调模型之外的 Harness 工程能力才是竞争力）、其姊妹篇《深入理解 AI Infra》（4600+ Star，教你把大模型的算力账算明白）、邱锡鹏蒲公英书《神经网络与深度学习》第二版与通识版（1.9 万 Star）、《强化学习的数学原理》（1.8 万 Star）、谷歌老哥《Agentic Design Patterns》中文译本（21 个设计模式，8K+ Star）、WalkingLab 的 Hands-On Modern RL（4400+ Star，CartPole 一路讲到 RLHF/DPO/GRPO 与 LLM 对齐，浏览器里可训练）。

## 六本书详单
1. **《深入理解 AI Agent：设计原理与工程实践》**（github.com/bojieli/ai-agent-book，4.9 万 Star，持续更新）：含 PDF/配图/EPUB/配套实验代码。全书围绕 **Agent = LLM + 上下文 + 工具** 展开，覆盖上下文工程、记忆、Tool、模型后训练、Agent 进化、多 Agent 协作。
2. **《深入理解 AI Infra：量化分析与系统设计》**（github.com/bojieli/ai-infra-book，4600+ Star）：姊妹篇，讲怎么把大模型跑起来的资源账算明白——逐项估算计算量、显存、带宽和功耗，再对照硬件真实能力推导系统设计。涉及架构、推理与训练负载、分布式推理、推理优化。核心观点：延迟差几倍体验完全不同，成本差一个数量级商业模式可能都不一样。
3. **蒲公英书《神经网络与深度学习》第二版 + 通识版**（github.com/nndl/nndl，1.9 万 Star，邱锡鹏）：2020 年第一版后一直是中文深度学习入门第一教材。通识版少公式、用故事案例类比；第二版偏系统理论学习。建议先用通识版建立直觉再看第二版。
4. **《强化学习的数学原理》**（github.com/MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning，1.8 万 Star）：从数学角度讲强化学习，让读者不只知算法怎么跑，还明白为什么被这样设计、为什么有效。无需 RL 背景，需概率论和线性代数基础。获伦敦政治经济学院经济学讲席教授与南加州大学化学工程副教授来信赞誉，中英文课程在 B 站和 YouTube 播放量破 270 万。
5. **《Agentic Design Patterns》中文版**（github.com/xindoo/agentic-design-patterns，8K+ Star，xindoo 牵头翻译）：在谷歌工作多年的作者把构建 AI Agent 的套路整理成 21 个设计模式，正文 21 章 + 7 个附录全部译完，中文在线版 adp.xindoo.xyz，清华大学出版社有中文纸质书《Agentic 智能体设计模式》。内容由浅入深：提示链、路由、并行化、工具使用、规划、多智能体协作，再到记忆、RAG，以及安全防护、评估监控、资源感知优化等工程落地章节。
6. **Hands-On Modern RL**（github.com/walkinglabs/hands-on-modern-rl，4400+ Star）：开源强化学习实战教程，7 大部分 26 章。每章围绕具体实验：先用 CartPole 倒立摆直观理解状态/动作/奖励，再深入到 DQN、PPO、RLHF、DPO、GRPO 等现代算法；从马尔可夫决策过程、价值函数、策略梯度延伸到 LLM 后训练，还包括工具调用 Agent、浏览器 Agent、视觉语言模型 RL、具身智能和音频 RL。每章配可运行 Python 代码和真实训练曲线，可亲自跑实验改参数。

## 关联连接
- [[深入理解AIAgent]] — 第 1 本，Agent 工程化核心教材
- [[AgenticDesignPatterns]] — 第 5 本，21 个 Agent 设计模式中文译本
- [[AIInfra]] — 第 2 本提炼的算力账方法论
- [[逛逛GitHub]] — 作者
- [[Harness]] — "模型之外的工程能力才是竞争力"论断补充来源
- [[强化学习]] — 第 4/6 本的学科基础
- [[prompt-chaining]] — 21 模式之一
- [[orchestrator-workers]] — 21 模式之一
- [[多Agent]] — 教材覆盖的协作主题
