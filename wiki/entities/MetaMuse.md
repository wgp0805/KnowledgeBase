---
title: "Meta Muse"
type: entity
tags: [AI产品, PersonalAgent, Agent, Meta, 个人助理]
sources: [raw/01-articles/2026-09-24-体验完Meta的Muse，原来这才是我们想要的AI助理.md, raw/01-articles/2026-09-25-扎克伯格谈Muse：个人Agent必须从预训练开始设计，虚拟机、记忆和权限系统是巨头的全栈护城河.md, raw/01-articles/2026-09-27-Meta Muse为超级智能买单.md, raw/01-articles/2026-09-29-豆包连夜”抄作业”，字节版Muse要来了？.md, raw/01-articles/2026-09-29-Manus终于像个通用Agent了.md, raw/01-articles/2026-09-30-Muse 爆火之后，腾讯、阿里、字节集体冲进Personal Agent.md, raw/01-articles/2026-09-30-a16z 最新深度对话：这才是 personal agent 的正确打开方式.md]
last_updated: 2026-10-08
---

## 定义
Meta 于 2026-09-08 推出的 Personal AI Agent（被称"美版豆包"），定位不是一问一答的聊天机器人，而是围绕用户长期目标 24 小时持续工作的个人助理：记住偏好、连接邮件/日历/社交账号、在云端 Secure VM 中执行数小时至数天的后台任务。

## 关键信息
- **数据**：12 天约 280 万下载、上线约 10 天登顶 App Store 第一（超过 ChatGPT）；截至 9-22 累计下载超 250 万
- **架构**：持续运行的 Secure VM（自有浏览器、文件系统、终端），可跑子 Agent、定时任务与自写 Skill；后台任务不依赖用户手机；机密虚拟机 + 独立凭据存储 + 监控 Agent 三重隐私设计
- **能力栈**：浏览器操作、长期记忆（夜间写入反思、记忆可查看编辑并支持从 ChatGPT/Claude 迁移）、Connector（Instagram、Notion、邮件日历、Spotify、钱包）、目标拆解与主动推进（Proactive）、Ideas 推荐页、Artifacts 结果留存
- **权限模型**：登录、付款、发送邮件、披露敏感信息需明确授权，遵循最小权限原则；Muse 不能自行扩大权限
- **商业**：每周 1 亿 token + 一台虚拟机免费额度起步；与 Stripe 合作接入支付，计划从交易抽佣金（可由商家承担）；2026-09-23 Connect 大会追加 Mac 桌面操控、视频通话、智能眼镜集成承诺
- **争议**：上线两周内被 Patrick Wardle 披露 `endo_voyager_dictation_endpoint` 0-day 漏洞（24 小时热修复）；电话订餐被曝为外包真人模仿 AI 语调（404 Media 曝光后撤回测试）；上线第 13 天被 Amazon 以"未授权 AI 代理"封杀购物功能；数据用于训练选项默认开启
- **出身**：Meta 超级智能实验室产品负责人 Nat Friedman 承认产品思路深受 [[OpenClaw]] 启发，团队内部早大量使用 OpenClaw，目标是改造成几十亿用户易接触的产品
- **下载与资本数据（2026-09-29 视角）**：Sensor Tower 口径——上线 6 天下载超 90 万，9-21 累计超 250 万，另有报道称截至 9-24 超 340 万次并一度登顶美国 App Store；9-08 至 9-29 期间 Meta 股价涨两成多、市值多三千多亿美元
- **"入口战"第一枪**：亚马逊以"未经授权的 AI 代理访问违反使用条款"封杀 Muse，同日 Shopify 宣布与 Meta 合作让 Agent 直接在商家店铺结账——一家封一家迎，是 Agent 时代第一场入口战（详见 [[摘要-豆包Spell对标Muse]]）
- **竞争与对比**：下载量约为 xAI Grok Bot 独立 App 的 4 倍（彭博智库），佐证"分发能力才是消费级 Agent 的护城河"；[[Manus]] 的 Cue 走"一支有身份的小团队"路线与之对照（Muse 是"给你一个管家"）；国内字节 [[Spell]]、腾讯 [[LightVela]] 均以之为对标
- **下载数据口径差异（2026-09-30 补充，非矛盾）**：不同统计方口径不一——Apptopia 估算上线前 12 天**美加 iOS 约 180 万下载**（同期 ChatGPT 130 万，首次有消费级 AI 应用在此口径跑赢 ChatGPT）；Sensor Tower 口径为 6 天全球超 90 万、9-21 累计超 250 万（详见 [[摘要-muse爆火大厂冲进personal-agent]]）。9-21 登顶美区 App Store 免费榜消息当日 **Meta 股价单日大涨 11.43%**（去年 4 月以来最大单日涨幅）
- **被封细节补全（2026-09-30）**：亚马逊给的三条理由——Meta 事先没打招呼、Muse 浏览网站不表明 AI 身份、疑似抓取存储登录凭证；**更深层理由是 AI 替用户购物绕过亚马逊个性化推荐**（广告/推荐/复购是平台商业起点），Meta 回应称 Muse 看不到用户密码和支付信息；Meta 已签沃尔玛、丝芙兰、Expedia、OpenTable、Shopify，名单恰缺美国电商最大玩家（详见 [[围墙花园]]）
- **a16z 评价**：Muse 与 Instinct 是当前市场两个主导的免费产品，背后是 Meta/OpenAI 烧钱补贴，长尾初创难与免费大玩家竞争；且"122 个 personal agent 产品中真正能活下来的可能只有个位数"（详见 [[a16z]]、[[摘要-a16z-personal-agent对话]]）

## 关联连接
- [[摘要-meta-muse-个人ai助理体验]] — 来源（产品评测）
- [[摘要-扎克伯格谈muse-全栈护城河]] — 来源（设计哲学访谈）
- [[摘要-meta-muse-承诺税]] — 来源（承诺税批判）
- [[摘要-ai自动下单消费的信任困局]] — 来源（海外消费执行 Agent 并列提及）
- [[Meta]] — 开发公司
- [[扎克伯格]] — "个人超级智能"定位的提出者
- [[personal-ai-agent]] — 所属产品概念
- [[最小权限原则]] — 权限系统设计原则
- [[OpenClaw]] — 产品思路的启发来源
- [[Anthropic]] — Computer Use 能力先行者（能力非独创）
- [[OpenAI]] — Operator 能力先行者
- [[Amazon]] — 封杀其购物功能的伙伴
- [[豆包]] — 被称"美版豆包"的对标产品
- [[摘要-豆包Spell对标Muse]] — 来源（2026-09-29 下载数据、入口战与国内对标）
- [[摘要-Manus2通用Agent]] — 来源（Cue 对照）
- [[Spell]] — 字节的对标产品
- [[LightVela]] — 腾讯"住进微信"的同类形态
- [[Manus]] — Cue 给 Agent 配"身份证"的差异化路线
- [[GrokBot]] — 下载量被其 4 倍反超的竞品
- [[通用Agent]] — 所属产品概念
- [[ChatGPT]] — 登顶榜单时被超越的产品、记忆迁移来源
- [[摘要-muse爆火大厂冲进personal-agent]] — 来源（Apptopia 口径、股价反应与封禁细节）
- [[摘要-a16z-personal-agent对话]] — 来源（主导免费产品地位与 122 产品存活判断）
- [[围墙花园]] — 亚马逊封禁背后的平台墙
- [[a16z]] — 评价方
- [[Instinct]] — 并列主导产品（路线相反的无界面派）
