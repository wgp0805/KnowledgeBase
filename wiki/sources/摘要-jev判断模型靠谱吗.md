---
title: "摘要-jev判断模型靠谱吗"
type: source
tags: [来源, 原始文件, Jev, TypeSafeAI, RLCD, 判断模型]
sources: [raw/09-archive/2026-09-20-比 LLM 快 193 倍、输出 token 免费：Jev 的“判断模型”路线靠谱吗？.md]
last_updated: 2026-09-21
---

## 核心摘要
David Lee 梳理 [[Jev]] 的「判断模型」路线：它由前 OpenAI 研究员 [[DiogoAlmeida]] 创办的 [[TypeSafeAI]] 发布，不生成文本，只在预先定义的答案空间上一次性输出概率、评分或是否判断。训练方法 [[RLCD]] 优化「认知上诚实的概率」，让无人值守自动化可以按置信度分流；公司称其比 LLM 快 193.6 倍、便宜 444.6 倍，但主要基于自建 workflow eval，不是公开基准。文章同时泼冷水：所谓「零幻觉」只是 schema 内不出格，不保证事实正确；真正竞品还包括蒸馏小模型、传统分类器、规则引擎与结构化输出工具链，Jev 需要证明它比「通用模型 + 工程胶水」更省心。

## 关联连接
- [[Jev]] — 判断模型
- [[TypeSafeAI]] — 发布公司
- [[DiogoAlmeida]] — 创始人
- [[RLCD]] — 校准决策强化学习
- [[SystemOneModel]] — 对标快判断
- [[置信度校准]] — 概率可信度核心
- [[幻觉]] — 被重新定义的 schema 内幻觉
