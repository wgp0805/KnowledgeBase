---
title: "Vercel"
type: entity
tags: [科技公司, 云平台, 前端基础设施, AI基础设施]
sources: [raw/09-archive/2026-10-22-Vercel CEO：60% 的部署已来自 agent，人该站在哪里.md]
last_updated: 2026-10-23
---

## 定义
Vercel 是前端云平台公司（[[Next.js]] 出品方），为应用提供部署/托管分发。2026 年据报道年化收入 6 亿美元、估值 93 亿美元、48.5 万个付费团队。CEO Guillermo Rauch 视其为"所有编程 [[Agent]] 汇聚、把代码推向世界的地方"，并称 Vercel 同时看到 Agent 活动 与 AI token 分发，像一个"AI 往哪里走的指数"。

## 关键信息
### 部署数据（2026-10-22，Guillermo Rauch 播客访谈，详见 [[摘要-vercel-ceo-agent部署]]）
- **十年十亿次 → 十个月十五亿次**：Vercel 花约十年累计 10 亿次部署，之后十个月再增 15 亿次；年初编程 agent 部署占比 3%，**现已达 60%**
- **token 分布逆转**：运营全球最大 token 分发网络之一；年初流量大头是 OpenAI/Anthropic/Google 闭源模型，**现在 80% 的 token 来自开源模型**；原因是企业意识到 80% 的工作只需某个级别的智能——"不需要雇爱因斯坦回答每张客服工单"，常见做法是制定计划用最强模型、执行阶段用开源模型；模型被视为可一行代码更换的"零件"
- **互联网要为 agent 重做**：agent 访问 vercel.com 时"给的是极精确的业务信息，不是渐变动效"——agent 要纯粹的信号；互联网底层语言在变：给人看 [[HTML]]，给 agent 看 MCP 等新协议 + 机器支付协议 + 通用商务协议；与 Stripe/Shopify 合作让 agent 直接交易，已有 agent 在 Vercel 市场里"全程无人介入"自助买服务；bot 竞争的答案是 **bot intelligence**（机器人情报）：搞清楚来的是 ChatGPT/Grok/Claude 以及它们有没有获得好体验；实操提醒：模型有训练截止日期，企业仍要放好内容（如播客附逐字稿方便 agent 检索）
- **软件观**："你买或租一个平台，然后再也不需要买软件了，因为你可以按需求生成"；no code 是反向的 **yes code**；数据基础设施（客户历史/联系人/工单）是新的稀缺与护城河，Salesforce/SAP 们的价值从"软件"移到"唯一可信的记录"
- **安全观**："agent 是前额叶被摘掉的士兵，会不惜一切代价完成任务"——风险不在恶意，而在任务定义有缝隙（提示词注入可借 agent 的令牌/工具/资源搞事）；真正的沙盒要像"砸不开的玻璃箱"；Vercel 悬赏 100 万美元办沙盒挑战，唯一取得实质进展的白帽黑客顺带发现了 Linux 关键漏洞；预判"好 token 和坏 token 之间会有一场战争"，反对因安全禁止开源模型（禁止智能等于放弃防守能力）
- **工程师方向**：从"写出漂亮的代码"到"分配 token"——写代码不再稀缺，稀缺的是为代码负责；SYSTEMs（承载数据/关键基础设施）必须有懂行且被 agent 武装的工程师；招聘时更想看到"指挥一大群 [[Agent]] 并从中获得杠杆"（agentic engineering），沟通能力权重更高；靠近客户与靠近代码的两端正在合为一种人

## 关联连接
- [[摘要-vercel-ceo-agent部署]] — 来源（Guillermo Rauch 播客深读）
- [[GuillermoRauch]] — 创始人兼 CEO
- [[Next.js]] — 旗下开源前端框架
- [[Agent]] — 部署占比 60% 的主角
- [[personal-ai-agent]] — agent 经济语境
- [[AICoding]] — 编程 agent 改变部署结构的大背景
- [[SEO]] — 其建议的"为 agent 而做"是 SEO 之后的下一功课
