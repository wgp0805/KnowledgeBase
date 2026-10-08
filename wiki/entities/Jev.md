---
title: "Jev"
type: entity
tags: [AI模型, 判断模型, TypeSafeAI]
sources: [raw/01-articles/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的"判断模型"路线靠谱吗？.md, raw/01-articles/2026-09-20-Jev新决策模型的试用心得.md, raw/01-articles/全网爆火的 Jev 究竟是什么？一篇文章为你讲透！.md, raw/01-articles/为什么越来越多人用 Jev ？.md, raw/01-articles/2026-09-21-一万字Jev 工程实践长文：把 Agent 的"判断题"从大模型里拆出来.md, raw/01-articles/2026-09-22-大厂后训练视角看Jev模型的更新（大白话）.md, raw/01-articles/2026-09-22-新模型Jev爆火：曾帮ChatGPT学会聊天的人，为啥做个不聊天AI？.md, raw/01-articles/2026-09-22-Jev爆火，具身智能迎来大救星？.md, raw/01-articles/2026-09-26-Jev 爆火背后：AI Agent 正在从“三体人”变成“地球人”.md, raw/01-articles/2026-09-26-基元律动发布 NeoHorse-Jev，开源 Jev 综合评测第一.md, raw/01-articles/2026-09-30-“哑巴模型”Jev火了，会给AI产业带来什么改变.md]
last_updated: 2026-10-08
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
- **新度量指标（2026-09-26）**：Decision per Dollar（每美元完成多少次可靠决策）；传统大模型基本单位是 Response（回答），Jev 的基本单位是 Action Selection（行动选择）
- **经济逻辑**：Agent 生产环境中大量重复判断（工具调用是否安全、是否拦截交易、是否转人工、交给哪个模型）不应每次都完整推理——"第一次出现推理是智能，第一万次出现还在重复推理就是成本"
- **产品单位差异**：典型落地场景为终端命令安全判断、企业邮件分类、模型路由与 Agent 监控（TechCrunch 报道）
- **比喻**：当下大模型像《三体》里思考即表达的"三体人"，Jev 路线是让 Agent 把反复经验沉淀成直觉、变成"地球人"
- **Memory ≠ Learning**：Jev 代表的 Judgment 与后训练结合，才是从"拥有记忆"走向"形成能力"的路径，见 [[智能压缩]]
- **"哑巴模型"产业视角（2026-09-30，详见 [[摘要-jev哑巴模型产业改变]]）**：
  - 浏览器 Agent 实测：Browser Use 创始人用 Jev 查 Google Flights 苏黎世→伦敦机票，全流程 7.1 秒、单次成本 0.0039 美元、循环中位延迟约 178ms；Vercel AI Gateway 上输入约 0.04 美元/百万 Token、输出免费
  - 行业背景：Agent 从代码向办公扩散（OpenAI 数据：2→6 月企业周活 Codex 用户在法律/销售招聘/营销增长 108×/41×/26×），调用频率激增催生 [[模型分化]]，Jev 是分化的极端样本
  - 局限：同一判断正着问一遍再反着问，两组概率之和有时超过 1——概率校准尚未达标，"躲开编造答案的风险，但概率照样会错"
  - 生态位：Jev 名字取自"杰文斯悖论"——判断更便宜后调用量反而上升；按任务路由多模型的 Agent 入口（WorkBuddy Auto 模式、Cursor Router）因此更重要

## 关联连接
- [[TypeSafeAI]] — Jev母公司
- [[RLCD]] — 校准决策强化学习
- [[SystemOne]] — 快思考模型
- [[SystemOneModel]] — Jev 的模型类别
- [[快慢分工]] — Agent 架构中的分工
- [[决策数据]] — Jev 判断沉淀的数据资产
- [[智能压缩]] — 判断能力的形成过程
- [[决策接口]] — 同类模型的调用范式
- [[NeoHorse]] — 同类开源决策模型
- [[Agent]] — 智能体架构中的判断层
- [[工单分类]] — 典型应用场景
- [[浏览器Agent]] — 动作选择
- [[模型路由]] — 工具选择
- [[置信度校准]] — 概率可信度
- [[非自回归]] — 推理方式
- [[摘要-Jev爆火背后AI-Agent从三体人变地球人]] — 来源资料
- [[摘要-基元律动发布NeoHorse-Jev评测第一]] — 来源资料
- [[摘要-jev哑巴模型产业改变]] — 来源资料（产业影响与校准局限）
- [[模型分化]] — Jev 所处的行业趋势
- [[DiogoAlmeida]] — 创始人
