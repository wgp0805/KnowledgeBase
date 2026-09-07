---
title: "沙特主权大模型 HUMAIN M3，为什么选择了 MiniMax 的开源底座"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6460052.html"
date: "Sat, 05 Sep 2026 06:13:19 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 沙特主权大模型 HUMAIN M3，为什么选择了 MiniMax 的开源底座

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6460052.html  
> **抓取日期**: 2026-09-05  
> **相关性评分**: 1.0

> HUMAIN这家沙特国家AI公司发布主权大模型HUMAIN M3：基于MiniMax M3后训练，七项阿语benchmark平均89.37，把GPT-5.6 SOL和Opus 5甩在身后。底座是开源的，主权筹码其实在文化对齐。

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/dcd12ab0624076efc7cdc032cf4812cd_MD5.jpg)

沙特国家 AI 公司 HUMAIN 发布了主权大模型 HUMAIN M3，在七项**阿拉伯语 benchmark** 上平均分第一，超过 GPT-5.6 SOL 和 Opus 5

当然，并不是说这个模型的编程水平超过了，而是这个模型背后有许多本土化的训练预料，因此在文化、语言、信仰等方面，超过了这些 OpenAI 与 Anthropic 的模型

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/85e46b8d0a4d239a36f83c1dab56c75f_MD5.jpg)

于是就有了…

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/a724bdb06ddaabd7a800dbc0110bf9ee_MD5.png)

本文由此展开

## 底座是 MiniMax M3

首先得说一下， HUMAIN 很诚实的，直接说了：commissioned by HUMAIN and **delivered by MiniMax**

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/2f82f0d22dc86524cc3c98f97a5c87c7_MD5.png)

MiniMax M3 是今年 6 月发布的模型，428B 总参数、23B active/token 的 MoE 架构，1M context，原生多模态&开源：我们开源了 MiniMax M3

**而 HUMAIN 对这个模型进行了后训练，加训了超过 1 万亿阿拉伯语 token** ，加入 Saudi-specific 的 alignment 和 guardrail，搭在自己的 HUMAIN Node 平台上，支持 In-Kingdom sovereign hosting。因此，HUMAIN M3 在阿拉伯语的 bench 下有了大幅提升

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/4aaad9e49a04699e2afbedd37a0207cf_MD5.png)

但话说回来，这事儿也大概确实好像也就是他们官方能搞…要知道在互联网上，阿拉伯语的内容并不多，这里的数据采集尤其是宗教、教育等信息的文化对齐，好想也只有他们自己的官方有数据

还有另外的…这个事似乎也只能是基于开源模型![🤔](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/95e9257027edea146e1199e192b39d99_MD5.png)

## 主权的分层

其实看到这个新闻的时候，我是想到个问题「主权大模型，用开源模型进行后训练」这事儿，符合周礼么？

然后我去翻了他们具体的说法，刚巧的是他们 CEO 在 Linkedin 上发了篇内容，这里截取了一段

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/8d21bc350bd72ff528070962e489d6d3_MD5.png)

大概是说 HUMAIN 不想把未来押在一个模型上，明确是 model-agnostic，起真正目标是 Data centers → Compute → Cloud → Models → Platforms → Applications → Sector solutions 这整个 stack，而在内的东西，都是可以替换的

HUMAIN 也确实是在按这个 stack 花钱。去年美国商务部批准它购买相当于最多 3.5 万张 Nvidia GB300 的芯片；今年 8 月底，它又在 NEOM Oxagon 推进首期约 100MW 的 AI 数据中心

![](assets/2026-09-05-%E6%B2%99%E7%89%B9%E4%B8%BB%E6%9D%83%E5%A4%A7%E6%A8%A1%E5%9E%8B%20HUMAIN%20M3%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9%E4%BA%86%20MiniMax%20%E7%9A%84%E5%BC%80%E6%BA%90%E5%BA%95%E5%BA%A7/b9db419bccf71ada524de6416e3871cb_MD5.png)

恰好我又找到了 The Information 的一个报道（并且为此支付了 $39 进行阅读），里面大致表达了这么个意思：**美国和中国主导先进 AI 研发，其他国家往往 have little choice but to depend on American or Chinese foundational models**

the difficulties most countries face when they try to develop sovereign AI systems using homegrown technologies

当大多数国家尝试用本国技术开发主权 AI 系统时，面临的现实困难

有趣的是，OpenAI 今年做模型本地化时，也表示只有少数国家有条件自行开发 frontier model。对更多国家，工作其实是把现有最强的 AI 重新适配到自己的语言、法律和文化里。

于是对于主权 AI 来说，就走上了这么一条路线：**主权方把控数据、训练方向、对齐、评测标准、算力、部署、治理，但然后其他部分，比如基模来自外部**

## 开源的另一面

我一直觉得，开源是中国 AI 在地缘博弈里打出的一张奇牌

一方面，我们可以变相的利用 token 作为承载物，去以更低成本运送&销售电力

另一方面，我们可以膈应着美国，让他们眼看着更多实验室拿着中国的模型做后训练，然后还失去了道德的高点

然后还有一个，就是我觉得：**美国的出口管制，也在中国开源模型做推广**

你看，限制英伟达出口，就导致很多国家的 AI 基础设施建设受阻；限制模型输出，就让这些国家导向开源

尤其在主权模型这一块，虽然 OpenAI 是提供定制的后训练服务的，但他们的模型仍然不会给你所有的权重，你也无法有效的改变它的 alignment，让它完全符合沙特的文化语境和监管要求。一旦 OpenAI 调整政策，或者美国出台新的数据政策，可能就G了

而对于开源模型，就可以无视这些地缘政治风险影响，只要下载下来、就能自己训练、部署，按自己的节奏去推进。能管得了芯片贸易，还能管得了模型下载么？

于是，出口管制越严，想做主权模型的国家就越需要一个能本地部署、不受远程控制的 foundation model。闭源美国模型随时可能因为政策变化被切断，而中国的开放权重模型，一旦下载，谁也拿它没办法

**打压中国 AI 的力度越大，开放权重的吸引力越强。每一道新的出口管制，都在无意中提升开放权重的相对价值**

## 最后

目前有正儿八经 AI 能力的，其实就是中国和美国，其他国家基本算是没有从零训练 frontier 基模能力的，而各种的「主权安全」也会催生出各种各种各样的多中心化 AI，很可见的也会有各种各样的「主权模型」…

作为数据支撑，CNAS 今年 8 月更新的 Sovereign AI Index 里，已有 67 个国家，184 个政府支持的项目了（Sovereign AI，简单说就是一个国家希望关键的 AI 能力掌握在自己手里）

毕竟，就像美国可以用封锁 swift 的方式制裁其他国家的金融，**大可以想象美国会以「我不给你用 Claude」来进行 token 制裁** ，总国家需要有方法为它的国民提供智能

那么，既然我没有训练基础模型的能力，我又有主权模型的需求，就势必要对开源模型进行后训练，让他能对齐国情，正如 HUMAIN 这样，去用数据主权拼接模型主权

不过吧，对于中国公司来说，这似乎也能成为一种机会：**提供后训练 &对齐技术，做模型 OEM**

本文由人人都是产品经理作者【赛博禅心】，微信公众号：【赛博禅心】，原创/授权 发布于人人都是产品经理，未经许可，禁止转载。

题图来自 Pexels，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6460052.html