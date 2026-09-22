---
title: "TypeSafeAI"
type: entity
tags: [AI公司, 模型厂商, 创业公司]
sources: [raw/01-articles/为什么越来越多人用 Jev ？.md, raw/01-articles/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的“判断模型”路线靠谱吗？.md]
last_updated: 2026-09-21
---

## 定义
TypeSafe AI 是由前 OpenAI 研究员 [[DiogoAlmeida]] 创办的 AI 公司，于 2026-09-15 发布了"不生成文本、只输出结构化决策"的模型 [[Jev]]。

## 关键信息

### 宣言与路线
- 宣言：**"We're building prod, not God."**（我们要造能投入生产的东西，不是造神）
- 反 AGI 路线：不参加 AGI 竞赛，公开称"今天的模型早已越过创造巨大经济价值所需的智能门槛"；砍掉文本生成这个行业最大的卖点，做一个不会说话的模型。这就是 think different
- 创始人核心观点："花了多年时间让 AI 更擅长与人互动。但如果 AI 要真正改变工作完成的方式，人就不能是智能唯一的消费者。大多数智能最终应该住在软件里，在后台安静运行。"

### Manifesto：一份少见的反 AGI 宣言
1. **无马马车**：早期汽车被设计成"没有马的马车"（保留高座椅、马车弹簧、鞭子插槽）。新技术总是先被塞进旧事物的形状。今天的 AI 也一样——被训练成"乐于助人、口齿伶俐的助手"，前提是假设另一端坐着一个人。可预见的后果是 AI 需要 human in the loop，而不是在后台运行
2. **SQL 之前的数据库**：今天的智能像 SQL 出现之前的数据库——强大，但每次使用都是定制的。一旦一次聪明的决策变得像数据库查询一样可靠、可调用，建设者就会像堆叠软件一样堆叠智能。寒武纪大爆发从来不是顶层设计出来的
3. **安全是分层的前提**：让一个组件无人值守是因为它可靠；在它之上构建是因为它可信。在这份宣言里，安全不是对齐哲学，是工程纪律
4. **Neuro-symbolic 的旧梦**：神经网络负责感知，符号逻辑负责推理，被戏称为"smart if-statements"

### 五大用例方向（Use Case Map）
- **AI Automation Software**：代码拥有控制流，Jev 处理语义判断，可后台跑一百万次，不需要 human co-pilot
- **Real-time applications**：150ms 级前沿智能，快过人类感知，可嵌进 UI 甚至驱动游戏
- **AI Map Reduce**：便宜 100 倍意味着可扫海量数据（分类巨型 agent 轨迹、从大语料提取特征）
- **Universal Verification**：验证其他 AI 的输入、抽取、推理链和工具调用，检测越狱/引用错误/幻觉，成本只是 LLM 调用的零头
- **Harness Engineering**：模型路由、语义上下文检索、LLM 错误检测和护栏

### 产品状态
- 官网 console.typesafe.ai，文档 docs.typesafe.ai，已免费开放
- 模型版本 1.13，上下文仅 32k，不能多轮对话，不能输出复杂结构化内容
- 完全闭源，只提供云端 API；新架构、并行采样器、[[RLCD]] 训练细节全部未公开，无论文（Hacker News 上从 encoder-only 猜到扩散模型，公司只说论文"以后可能有"）
- 官方 SDK 只有 Python 和 JavaScript；Java/Kotlin/MCP 由社区补齐

## 关联连接
- [[Jev]] — 公司发布的模型
- [[DiogoAlmeida]] — 创始人
- [[RLCD]] — 公司披露的训练方法
- [[SystemOneModel]] — 产品定位所属类别
- [[置信度校准]] — Manifesto 强调的自动化前提
- [[Anthropic]] — RLHF 路线代表的同行（创始人出身自前沿实验室）
