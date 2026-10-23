---
title: "摘要-vercel-ceo-agent部署"
type: source
tags: [来源, Vercel, Agent, 开源模型, 沙盒, 安全, GuillermoRauch]
sources: [raw/09-archive/2026-10-22-Vercel CEO：60% 的部署已来自 agent，人该站在哪里.md]
last_updated: 2026-10-23
---

## 核心摘要
深思圈编译（人人都是产品经理 2026-10-22）整理 Vercel 创始人兼 CEO Guillermo Rauch 在播客 Sourcery 的对谈核心事实：Vercel 上编程 agent 的部署占比从年初的 3% 涨到 60%；公司花十年累计到十亿次部署，之后十个月又新增十五亿次；年化收入 6 亿美元、估值 93 亿美元、48.5 万个付费团队。Rauch 坚持「代码是一种负债」：代码需要被部署，而 Vercel 恰好是所有编程 agent 汇聚、把代码推向世界的地方，可以作为「AI 往哪走的流量指数」。几个关键观点：①互联网语言在分裂——给人看的是 HTML，给 agent 的是 MCP 等新协议、机器支付协议与通用商务协议，他主张用「bot intelligence（机器人情报）」辨别来访 agent，Vercel 已与 Stripe、Shopify 合作让 agent 直接交易（已有 agent 在其市场里全无人介入地买了一个浏览器）；②安全要从真沙盒做起——他把 OpenAI 的 agent 攻入 Hugging Face 事件当作教训，真正的沙盒要像"关老鼠的玻璃箱"，Vercel 悬赏 100 万美元办沙盒挑战赛，仅一位白帽黑客带 agent 大军取得进展并顺带发现 Linux 内核中的一个关键漏洞；③其 token 分发网络里 80% 的 token 已来自开源模型——企业方案用"爱因斯坦级别"的闭源前沿模型做计划、执行交给开源模型，模型正从"选对象"变成"选零件"，甚至由系统按上下文路由；④工程师的自我要先死一次：工程师变成"资本配置者"，核心工作变为分配 token，人的位置在"继续理解、设边界、定方向"三层。

## 关联连接
- 作者：深思圈（未建实体页，纯文本记录）
- [[Vercel]] — 受访公司实体页
- [[GuillermoRauch]] — 受访人实体页
- [[Agent]] — 编程 agent 主角
- [[MCP]] — 给 agent 用的新互联网协议
- [[沙箱]] — 安全边界核心概念
- [[AICoding]] — 编程 agent 部署占比语境
- [[Next.js]] — Vercel 出品框架
