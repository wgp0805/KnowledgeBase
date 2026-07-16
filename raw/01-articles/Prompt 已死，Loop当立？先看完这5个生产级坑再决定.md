---
title: "Prompt 已死，Loop当立？先看完这5个生产级坑再决定"
source: "https://mp.weixin.qq.com/s/qAWRMJ-NYiaGUO9aw7Bgcw"
---
CSDN程序人生 *2026年7月9日 17:26*

![图片](https://mmbiz.qpic.cn/mmbiz_gif/1hReHaqafad4H57UlgDZZl7lILyDiaAWDsRcksUcCYeT76ibEllhuHJU9PxRtFgAQC7QPgW6qicToOuMjnSsmsErQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

责编 | 梦依丹

出品 | CSDN（ID：CSDNnews）

今年，AI 编程圈出现了一个新口号："Prompt 已死，Loop 当立。"

黄仁勋在最近的演讲里说了句："没人再写提示词了。"Anthropic 内部工程师透露：超过 80% 的团队已经在用自改进循环构建产品，3 到 6 个月内，这个数字会变成100%。Claude Code 的缔造者 Boris Cherny 公开宣布他已经放弃 prompting，现在只写 loops。谷歌工程主管 Addy Osmani 给这件事起了个正式的名字：Loop Engineering。

这个概念听起来很理想。但任何真正在生产环境里搭过 Loop 的人都知道，理想和现实之间隔着一条很深的沟。

这些坑，不是教程里会告诉你的。它们是真正在生产环境里跑过几十个循环之后，用真金白银和加班时间换来的经验。

7 月 17-18 日，由 CSDN 与奇点智能研究院联合举办的 2026 奇点智能产品大会诚邀阶跃星辰开放平台的产品负责人陶炳哲带来《Loop 工程在阶跃的最佳实践》主题分享。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/S1iaf4GgGjExbGRWcYPEiczfwQBHcsezEH6pbnmEvMrygVFo0l9ic8Jib7Dr45aOLDlBsH9DwtibtbYMPN9lgicV0OuVDFD80py55ibA0cbusmsEdY/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

2026 奇点智能产品大会最新最全日程正式发布，距离报名通道关闭仅剩 8 天，请大家抓紧报名。

从阿里云可观测产品负责人，到字节跳动对内可观测产品负责人，再到现在的阶跃星辰开放平台产品负责人——十年时间，陶炳哲一直在做同一件事：让系统自己能告诉你它怎么了。而现在，他要告诉你，怎么让 Loop 系统真正跑起来，而不是跑飞了。

可观测性（Observability）听起来很技术，但本质上解决的是一个非常朴素的问题：当一个复杂的分布式系统出问题时，你怎么知道问题出在哪？日志、指标、追踪链路，这些工具不是为了让你看得更爽，而是为了让你在系统崩溃时，不用一个个机器去登录排查。

陶炳哲在这个领域干了十年。他见过凌晨三点被叫醒的值班工程师，见过因为监控盲区导致的故障扩大了整整一个小时才发现，也见过花了几百万买的监控平台，最后工程师还是靠 SSH 登录机器看日志。

这些经历让他对"自动化"和"可观测性"有一种近乎本能的敏感。当他看到 Loop Engineering 这个概念时，他的第一反应不是"这个很酷"，而是"这个在生产环境里怎么才能保证不翻车"。

这也是他在阶跃星辰正在做的事。

阶跃星辰的 Step 3.7 Flash 模型，也是目前业界最适合跑 Loop 的模型之一。400 Tokens/s 的推理速度，意味着每次检查的等待时间极短，一个五轮循环下来，模型推理的总耗时可能还不如你喝一口水的时间。如果换一个 50-100 TPS 的模型，同样的循环可能要等好几分钟——等久了人就会忍不住去手动干预，而手动干预恰恰是 Loop Engineering 要消除的东西。

除了模型速度。在陶炳哲看来，Loop Engineering 要真正跑通，需要解决五个核心问题：

第一，生成和验证必须硬隔离。 这不是靠提示词约束，而是工具可见性的硬隔离。写代码的 builder 必须有 Write 和 Edit 权限，而查代码的 checker 只能有 Read、Grep、Glob 和 Bash。从底层就保证 checker 无法修改任何文件。

第二，编排器必须原样转发失败信息。 编排器拿到 checker 的报告后，不能自己解读或过滤，必须完整转发给 builder。模糊的报告会让 builder 瞎猜，浪费整整一轮循环。

第三，必须有明确的停止规则。 最多几轮、什么情况下停止、什么情况下升级给人工，这些规则必须在循环启动前就写死。没有刹车的 Loop，会在暗坑里疯狂燃烧。

第四，状态必须落地。 所有进度不能只存在对话里，必须写进状态文件。AI 对话是"失忆"的，关了窗口就全忘，但状态文件存在磁盘上，下次循环从上次停下的地方继续。

第五，目标必须可验证。 "把这个功能做好"不是合格目标，"所有单元测试通过、TS 编译无报错、Diff 不超过 500 行"才是。目标不可验证，Loop 就没法安全停止。

这五个坑，每一个都足以让一条精心设计的 Loop 在生产环境里翻车。陶炳哲在阶跃的实践中，用 Infra 的方式把这五个坑逐一补平——不是写更长的提示词，而是搭建一套真正无人值守、自己会自检的生产级 Agent 循环系统。

在 2026 奇点智能产品大会现场的分享中，他还会用灰度反馈自动化作为真实案例，展示一条生产级 Loop 怎么从零搭起来，五个坑分别在什么场景下出现，以及阶跃星辰的 Infra 团队如何用工程化手段把它们逐一填平。

演讲的最后，他会给出一份设计准则清单——不是抽象的"最佳实践"，而是可以直接贴进项目 [CLAUDE.md](http://claude.md/) 的规则模板。

2026 奇点智能产品大会进入倒计时最后 8 天。

7月17-18日，北京金隅喜来登大酒店，40+位来自字节、百度、阿里、腾讯、宇树、360、京东、蚂蚁、科大讯飞等一线产品技术领袖，围绕 Agent 智能体、企业级 AI、AI Coding、具身智能、AI 原生组织等 12 大专题，全链路拆解AI原生落地闭环。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/0WDtulD6cGaxdzHUrqXHic3VM1dwbmHcxNaGWFKlUzEKN9GZU4zNW6ESNBIz4l0SibthOZXBS5icX5wYdibmIAkfR8Boz8cB3Vu836XCN1oZlYs/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

阅读原文