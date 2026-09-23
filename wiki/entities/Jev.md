---
title: "Jev"
type: entity
tags: [AI模型, 判断模型, TypeSafeAI]
sources: [raw/01-articles/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的"判断模型"路线靠谱吗？.md, raw/01-articles/2026-09-20-Jev新决策模型的试用心得.md, raw/01-articles/全网爆火的 Jev 究竟是什么？一篇文章为你讲透！.md, raw/01-articles/为什么越来越多人用 Jev ？.md, raw/01-articles/2026-09-21-一万字Jev 工程实践长文：把 Agent 的"判断题"从大模型里拆出来.md, raw/01-articles/2026-09-22-大厂后训练视角看Jev模型的更新（大白话）.md]
last_updated: 2026-09-23
---

## 定义
Jev是由前OpenAI研究员Diogo Almeida创办的TypeSafe AI发布的判断模型，不生成文本只输出结构化决策。被称为System One Model（快思考），70-500ms返回结果，比LLM快193倍、便宜444倍，输出Token永久免费。

## 关键信息
- **三种能力**：Choice（候选项选择）、Score（打分）、Noul（概率判断）
- **训练方法**：RLCD（Reinforcement Learning for Calibrated Decisions，面向校准决策的强化学习）
- **推理方式**：非自回归单次并行推理，跳过自回归解码
- **速度**：中位延迟105ms，比GPT-5.6 Luna快5-18倍
- **成本**：输入$0.042/百万Token，输出永久免费
- **置信度**：每个答案附带校准后的概率值，校准误差仅0.07
- **Java生态**：社区Java SDK（不依赖Spring AI ChatModel）、Spring Boot Starter、Kotlin客户端、MCP Server
- **使用渠道**：TypeSafe AI官网（已免费开放）、OpenRouter、Vercel
- **Agent架构定位**：「快慢分工」——大模型负责规划/推理/生成（慢思考），Jev负责高频原子判断（快判断）

## 关联连接
- [[TypeSafeAI]] — Jev母公司
- [[RLCD]] — 校准决策强化学习
- [[SystemOne]] — 快思考模型
- [[Agent]] — 智能体架构中的判断层
- [[工单分类]] — 典型应用场景
- [[浏览器Agent]] — 动作选择
- [[模型路由]] — 工具选择
- [[置信度校准]] — 概率可信度
- [[非自回归]] — 推理方式
