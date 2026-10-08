---
source_url: "https://mp.weixin.qq.com/s/RUrQTaqoleYlsQPi7oVUVw"
title: "WorkBuddy 开发微信小程序，保姆级教程来了"
account: "程序员小灰"
published_at: "2026-10-02 14:51:00"
saved_at: "2026-10-02 15:12:32"
sync_id: "art_fe4df7e025a047abad764e75f739bf21"
parse_status: "ok"
---

# WorkBuddy 开发微信小程序，保姆级教程来了

大家好，我是程序员小灰。

随着 AI 工具的不断发展，如今 WorkBuddy 俨然成为了国内最流行的 AI Agent 产品。

![](https://mmbiz.qpic.cn/mmbiz_png/9ojSnBX2WWaqiashkxaK9wwYFXYa3AXKsfaXI8icI3ENW8iaIrULWVWUYHZ6Eiaibjy4bD7SicbTxl9onq7X29zbeT5UooBjphdLfmJiabbjGZPyNU/640?wx_fmt=png&from=appmsg)

之前我们介绍过 WorkBuddy 中常用的一些技能，以及如何在 WorkBuddy 内使用这些技能完成特定任务。

今天这篇文章，我们来介绍一下如何使用 WorkBuddy 去开发微信小程序。

本篇文章我们会使用"待办事项"这样一个简单的案例来进行说明，介绍在 WorkBuddy 里面完成微信小程序核心开发流程的具体步骤，希望大家能有所收获。

# 一、WorkBuddy 和微信小程序生态介绍

WorkBuddy 是腾讯云推出的 AI 工作台，9 月 24 日上线了小程序的生成、预览、发布能力，等于把微信小程序的发布链路直接接了进来。

在没有集成微信小程序开发流程之前，如果我们想做一个小程序，传统意义上需要先下载安装微信开发者工具、创建项目，再找个 AI 编程工具打开项目写代码，写完还得回到微信开发者工具里去测试，几个客户端来回切。现在 WorkBuddy 里相当于是集成了微信小程序的核心发布流程。

而如果涉及到注册账号、备案、微信审核这些，还是得按微信平台的规矩来，这些是在 WorkBuddy 里面没办法完成的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vsAViaKGWic0VkXaT9XsW0sy22YicywpjkknbZUGiamj3xLiaVnSB3Zd2dscic8iaG2A8OR073icz4zV20K3UE5dSMVRymZ3LRUEicXibdwyXhoIXicuAg/640?from=appmsg#imgIndex=0)

# 二、基本操作流程

## 1. 要开发的待办清单

AI 时代，每天我们都有很多要做的事情。如果你不简单地记录下来，可能过几分钟、过一段时间就忘记了。所以我们制作这款待办清单小程序，用来管理每日待办事项。

这个待办清单一共就五个功能：

- 新增待办
- 点击待办标记完成，完成后自动移入“已完成”区域，这个区域默认折叠
- 已完成的事项可以恢复成未完成
- 删除是独立操作，需要二次确认，避免误删
- 单人使用，不需要登录和多人协作

功能不多，但是验证起来比较方便。

## 2. 描述需求、写代码

![](https://mmbiz.qpic.cn/mmbiz_png/vsAViaKGWic0V1bRkKLhDtvaFOOXxVjbYQOtficdw5u9t8WxIEFxMVCfTSMAEP1f2WE5rdfM6Jgu3RO7kCjIFXZLJibicFBlUnam8GlibHAqhu8xE/640?from=appmsg#imgIndex=1)

其实也就下面的四个步骤：

- 选择代码开发
- 选择小程序开发（选择之后，前面就会出现一个小程序的标识，表示将来你要开发小程序了）
- 描述需求，选择一个本地的文件夹作为工作目录
- 配置一下模型，给它权限，然后就直接让它去开发这个小程序了

![](https://mmbiz.qpic.cn/mmbiz_png/vsAViaKGWic0W1TgibHjfMmq37s1Mow9PknLKqxPGuU4TESPmjl0A8O0ZCvoDVSnZGRIupxicMFNwXRRXEVbheGrf6ltOH1JMR9ahwZM43kTc50/640?from=appmsg#imgIndex=2)

中途可能会弹出来问你是否需要云环境，然后你就选择“是”就可以了。不然的话，你是没有办法在 WorkBuddy 里面使用它的预览功能的

给 WorkBuddy 的需求，我是这么写的：

做一个单人使用的待办清单小程序：1）可以新增待办；2）点击待办标记完成，完成后自动移入“已完成”区域，这个区域默认折叠；3）已完成的事项可以恢复成未完成；4）删除是独立操作，需要二次确认，避免误删；5）不需要登录和多人协作。

因为待办清单这个东西功能非常明确，如果你想详细描述一下需求，可以和 AI 去对齐一下。

如果你选择的模型足够智能，其实只需要告诉它做一个待办清单小程序，它完全可以自己去决定做哪些功能。这些都可以根据我们自己的需求进行选择。

## 3. 小程序卡片预览

因为 Workbuddy 里面已经集成了小程序开发的一些流程，所以它可以给你一个小程序卡片，你点击卡片就可以在右边看到预览的效果：

![](https://mmbiz.qpic.cn/mmbiz_png/vsAViaKGWic0UaQH9Mj3YvA13mSvMYtffqB36icAN60hDMEkpul3ic12Kiag35Kj0uORs9yMV5mk5YnMlREeibdZWE2zdiasMLr3BtLbJwvHzqMbkE/640?from=appmsg#imgIndex=3)

如果你没有出现这个小程序卡片，你就没办法在侧边栏预览。

这个时候你可以直接在对话框里问他：“把小程序的卡片给我。”

如果他还是没有给你，就可能是因为你没有选择那个云服务的环境。

卡片到手之后，主要验收这么几件事：

- 新增条目
- 标记该待办事项完成
- 完成区增加折叠功能
- 如果不小心误删可以恢复这条事项
- 确认删除

## 4. 分享预览发布

小程序是否有问题？开发完成之后怎么测试？我们可以点击右上角分享的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/vsAViaKGWic0VC4PzPJGUPWaicic8hwSEWJEX8ic7Bic0cgBDmUkXsfNMvjHGkDWNX3f9XgwX8Jr1FJsEhrJ8ibnKYQN6pZRHH82gkRPiaBPYll5I64/640?from=appmsg#imgIndex=4)

这时候它会弹出一个弹窗，问你是绑定已有的小程序账号，还是创建试用版小程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vsAViaKGWic0Uxt3FtT7Oe0U5nLyEv9q8sPVzoEZlqednRhsLcJfzlDQDgbkHeC7PlODZiaeCxdzL9SWPEJbszicmPepFQA16SHYYKSQ6ReUGiaw/640?from=appmsg#imgIndex=5)

如果你没有小程序账号，就没办法绑定，只能创建试用版；但一旦创建了试用版，它就再也没办法绑定小程序账号了。目前系统不支持转换，不存在试用之后再转成正式版并绑定小程序账号的可能。

所以，如果你一开始就打算上线小程序给用户使用，而不是只当个玩具，一定要提前注册好小程序账号。

注册也不复杂：打开微信公众平台 mp.weixin.qq.com，在“账号分类”里选择“小程序”，填写相关信息就能完成注册。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vsAViaKGWic0WjqRNfFj8tV8ZO9LjdTr0rFkgLD5ZSKIhkcbTcPIdkuzPG0kopv4qY4ciaXkt3CopBJOwMOdajRCwTCXNReuYGEMvJ5icSl2khY/640?from=appmsg#imgIndex=6)

选了“绑定已有小程序账号”，就用小程序管理员的微信扫一下二维码，选中你注册的那个账号完成授权。

否则选了创建试用版，它就只能永远是一个试用版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vsAViaKGWic0VHRPr55CCgZSjKKEqEMNmAvfKWeicm8YlYiadDJ8xtWEBNWSKR94lWnlzw0rh5lByPBrrYJtm2yNFtqeC41Y5TZcdgJesicRjwkA/640?from=appmsg#imgIndex=7)

# 3. 账号额度与限制

WorkBuddy 免费版和付费版，它的用户额度是不一样的。

- 试用版 ：单个微信号最多创建 5 个试用小程序，每个有效期 14 天。
- 正式版 ：单个小程序每周最多提交 3 次微信审核。
- 云环境 ：免费版可托管 10 个应用，需求量大再考虑升级套餐。

如果你的需求量比较大，需要稍微注意一下这些额度的限制

# 总结

写到这里，我们简单地总结一下这篇文章的内容

动手之前先想清楚：这个小程序你是要上线的，还是只想体验一下流程。要上线，就提前把微信小程序个人账号注册好，第一次点分享时直接扫码绑定——注册入口在 mp.weixin.qq.com，选“小程序”即可。要是先建了试用版，那它就一直是试用版，再也绑不了账号了。只想体验的话，发个两周的试用版就够了。

还有个容易栽的坑：描述完需求，WorkBuddy 会问你需不需要云开发、配不配云环境，这里一定要选“是”。不选，小程序卡片出不来，侧边栏就没法预览。真没出卡片，就在对话框里要一句："把小程序的卡片给我。"

需求量大的话，留意上面说的这个额度即可。

![](https://mmbiz.qpic.cn/mmbiz_png/vsAViaKGWic0WbaImETfm5piaWRFPP228A8r5g841ED37F6gibbjvMaJtpmMbNCd24ibzRVxicvj9ZtrLXoNCTECrIDlWo0WBABEyA5QGkvmbeXQw/640?from=appmsg#imgIndex=8)

好了，关于 WorkBuddy 做微信小程序的流程和这次遇到的试用版限制，我今天就先聊到这里。

我是程序员小灰，我会持续为大家分享最新的 AI 工具和 AI 玩法。如果想第一时间收到推送，也可以给我个星标⭐ 我们下次再见~~

< END >

最近小灰创建了一个AI副业交流群，对AI和副业变现感兴趣的朋友，都欢迎进群交流。扫码添加小灰微信，备注“ai“即可进群：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9ojSnBX2WWYldee3Gj74lfp6Kbbgt96EmYFQEebMoF2gNGQ9jcKFMcsVeISHYIiaREDcSuPhib2h6oNhYj7V1hoYmxNRWhXDRKyGibSwqFUWqk/640?wx_fmt=png&from=appmsg)

---
原文链接：https://mp.weixin.qq.com/s/RUrQTaqoleYlsQPi7oVUVw
