---
title: "DiogoAlmeida"
type: entity
tags: [人物, AI研究者, 创业]
sources: [raw/01-articles/为什么越来越多人用 Jev ？.md, raw/01-articles/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的“判断模型”路线靠谱吗？.md, raw/09-archive/2026-09-30-“哑巴模型”Jev火了，会给AI产业带来什么改变.md]
last_updated: 2026-10-08
---

## 定义
Diogo Almeida 是 [[TypeSafeAI]] 的创始人，前 OpenAI 研究员，**RLHF（人类反馈强化学习）与 ChatGPT 的早期贡献者**。被形容为"RLHF 的核心贡献者背叛了自己的发明"。

## 关键信息
- 他的名字的分量：RLHF 正是让 ChatGPT 成为 ChatGPT 的技术，整个行业过去四年都在这条路上狂奔——把模型训练得更健谈、更讨喜、更像一个坐在你对面的聪明人。而 Almeida 的新公司，建立在对这条路线的公开批判之上
- 核心观点（原文）："I spent years working on models designed to make AI better at interacting with people. But if AI is going to fundamentally change how work gets done, people can't be the only consumers of intelligence. Most intelligence should eventually live inside software, running quietly in the background."——花了多年时间让 AI 更擅长与人互动。但如果 AI 要真正改变工作完成的方式，人就不能是智能唯一的消费者。大多数智能最终应该住在软件里，在后台安静运行
- 关键判断："我们优化人类语言优化了四年，但对自动化来说，这没用。因为计算机说的是另一种语言。"——[[Jev]] 说的就是计算机的语言：类型、概率、确定性
- 亲手把模型训练成讨好人类的人，否定了自己过去的范式，并敢于说"LLM 这条路对生产软件是错的"
- 这种"从足够底层的一个小角度偏离，后面看待问题的视角就和主流大相径庭"的创新，被称为 think different 的创新火花
- **RLHF 反思的另一面（2026-09-30，详见 [[摘要-jev哑巴模型产业改变]]）**：人类反馈推动模型生成更符合人类偏好的回答，也让模型养成另一种习惯——面对自己把握不大的问题，仍然倾向给出流畅、完整、笃定的回答；Jev 试图让模型把不确定性写进输出（八成把握就输出接近八成的正确率概率），系统拿到概率后自行设门槛：把握高的自动放行、把握不足的转人工或转强模型
- **未竟目标**：让模型实现可靠的自动化决策是他想抵达的方向，但 Jev 目前还没走到（正反问概率之和会超过 1 的校准问题）

## 关联连接
- [[TypeSafeAI]] — 创办的公司
- [[Jev]] — 其产品
- [[RLCD]] — 其新路线的训练方法
- [[SystemOneModel]] — 其产品所属类别
- [[OpenAI]] — 曾任职机构
- [[Anthropic]] — 同为前沿实验室出身转向工程的同行
- [[摘要-jev哑巴模型产业改变]] — 来源（RLHF 反思与校准局限）
- [[RLHF]] — 其反思的训练范式
- [[模型分化]] — 其产品助推的行业趋势
