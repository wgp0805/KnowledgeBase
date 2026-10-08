---
title: "Cline免费模型接入各种Agent，多账号免费token管够"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6474226.html"
date: "Wed, 07 Oct 2026 09:46:47 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# Cline免费模型接入各种Agent，多账号免费token管够

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6474226.html  
> **抓取日期**: 2026-10-07  
> **相关性评分**: 1.0

> Cline 的免费模型列表随新模型更新，官方只支持在客户端或 VSCode 插件里用，接不进 WorkBuddy 等 Agent。作者基于 cline-free 做出 ClineFreePool，剔掉耗光赠送额度的付费模型，把多账号池轮询写成可照做的步骤。

![](https://image.woshipm.com/2023/04/14/88176256-da8d-11ed-96fe-00163e0b5ff3.jpg)

说到Cline这个编程Agent，可能接触Vibe Coding不是太多的小伙伴不大熟悉，它最早是以VSCode插件的形式推出，在开发者社区享有一定的知名度。

Cline老马没记错的话，之前是Deepseek V4.1 Flash上线后，就开始提供该模型的免费额度服务，只要你注册就可以使用，新用户好像还有另外0.5美元的额度。

但是它这个免费额度的模型，简称免费模型，并不是固定的，有点跟促销一样，定期会根据最新模型的上线，推出不同的免费模型。比如最近AI圈子又上了Space-Bunny太空兔模型，Meta的Muse Spark 1.3，小米的Mimo V2.6 Flash。

重点再强调一遍，Cline的免费模型列表，它不是固定的，经常会更新。所以有时候这个模型可以用，有时候这个模型下架了，都很正常。

一般来说，你要用Cline的免费模型，就是下载它的客户端，或者是在VSCode里面安装插件，注册账号后登录使用。但是没法直接接入其它的AI工具或者Agent，比如接入WorkBuddy，OpenClaw，Hermes，Cherry Studio等。如果要接入，就得做成本地的API，成为所谓的第三方API。

因此老马参考了之前市面上已经有的Cline开源项目，主要包括了cline-free，cline2api-workers和cline2api。发现各有千秋，同时也存在局限性。

于是以cline-free为准，做了一些改进优化。移除了会耗尽赠送0.5美元额度的付费模型，需要订阅才能使用的付费模型。免费模型也不是写死的，而是会根据Cline的免费模型列表实时更新。

其次是做了项目的部署体验优化，让小白用户也能随便用一个Agent工具，比如WorkBuddy，项目地址丢过去即可快速一键安装部署成功。剩下的就是在代码的工程质量与自检方面进行了完善，视觉模板优化调整。总的来说，原项目cline-free是能跑，而老马改进优化后的ClineFreePool项目，则是能够放心持续使用。

在这里大部分的功能界面还是保留cline-free的设计，在此也非常感谢原作者的开源分享，省去了老马从头开始重复造轮子的操作，减少了WorkBuddy开发时的积分消耗。

老马改进优化后的ClineFreePool项目，同样开源到了Github上，MIT协议的情况下也欢迎小伙伴们随便修改DIY，你看哪里不行不顺眼，哪里有bug，就让自己的Agent去修改或者优化。

## 安装部署项目

前情提要就介绍到这里了，下面进入实操，老规矩照例会用到WorkBuddy来帮我们安装部署ClineFreePool项目。打开WorkBuddy后，新建个任务，把下面的提示词直接发送过去，即可安装部署成功：

> 安装这个项目 github.com/majiabin2020/ClineFreePool

![](https://image.woshipm.com/wp-files/sha256/cf/c3/cfc3effde3953a63ef81bf5eadd0f69111b464958c13149132d92a0e11c689c0.png)

如果安装部署失败，那大概率是你的网络无法正常访问github，需要做一些优化。可以参考老马之前写的文章去操作：装上这个Skill，让你的WorkBuddy正常访问github

安装完毕后，会启动一个网页版的控制台，一般网址都是127.0.0.1:端口号。这个地址会自动在WorkBuddy会话窗口的右侧，使用内置浏览器打开，同时运行着一个后台服务，后台服务切记使用期间不要关闭。

另外这个网址你也可以用电脑的浏览器去打开访问，打开后在左侧的菜单切换到模型页面，模型列表右上角有一个刷新数据。建议每次使用的时候点击刷新一下，这样可以实时获取Cline的最新免费模型：

![](https://image.woshipm.com/wp-files/sha256/be/14/be147322594d7b8397ea83497f2d59d1bbac3ecff581a78aadbda6044fd29bcd.png)

然后就是把你要使用的免费模型，点击添加按钮添加到已启用模型的列表里面。每个模型名称下面还有一个复制的按钮，等下我们要接入其它Agent或者AI聊天工具的时候，可以点这个复制按钮去复制模型的名称。

## 注册登录 Cline 账号

当然，现在还无法直接使用Cline的免费模型，我们还得注册登录Cline的账号。在左侧菜单切换到账号页面，点击登录新账号：

![](https://image.woshipm.com/wp-files/sha256/1a/69/1a698fcbf6e905a0348c8ac57caf92529a5ed718b294c18acdcb9e0fc1852f6f.png)

这时下面的登录Cline账号列表中会出现一个打开授权页面，你点击打开：

![](https://image.woshipm.com/wp-files/sha256/af/6e/af6e8584d7d7d8581d277648d50f3f594676fca59ce369d590b6b039a015f66d.png)

在弹出的新浏览器窗口页面中，就可以看到Cline账号的注册登录界面了。这里Google账号和Github账号很多小伙伴都没有，所以推荐使用Microsoft账号，你可以点使用Microsoft继续，或者点注册都行：

![](https://image.woshipm.com/wp-files/sha256/ac/d2/acd29ab28b7c9fa47e5e240087bec76566fb3a4d79e63beef327d7175d30faf6.png)

老马是使用Microsoft账号去注册登录的，因为Microsoft账号你如果是用Windows系统的话，基本上都会去注册。且国内注册无需神秘力量，相对还是比较简单的，唯一可能需要验证的是你的手机号码：

![](https://image.woshipm.com/wp-files/sha256/04/0d/040d87208b1a8c4378cc4f935725b71e923ec704e3d6d9c2ebf90150a0569b99.png)

验证后就可以对Cline的账号设备代码进行确认了，确认就是激活设备，登录Cline账号的意思。不过这里有可能会因为激活设备超时，出现下面的报错：

![](https://image.woshipm.com/wp-files/sha256/15/40/1540a84e805a9afaca4b78e803badfeff0c5d017942a9389c3c541efa5ba1f9f.png)

没有关系，你就关掉这个浏览器窗口页面。重新回到我们的ClineFreePool控制台，看看是否提示登录未完成，授权超时：

![](https://image.woshipm.com/wp-files/sha256/48/31/48311cf88579c489b6c04cfbb3ae861e8aa59c1e66fceaf0de9331ac5988743d.png)

如上图所示，就是老马在激活设备登录Cline账号的时候超时了。点击重新登录，再走一遍上面使用Microsoft继续的注册登录流程，最后再验证一下设备码，就能够成功登录Cline账号了：

![](https://image.woshipm.com/wp-files/sha256/68/6c/686c03b9db295da273b378f273c571abd380f10ab5de2dd2936ca991bbab764c.png)

成功登录Cline账号后，那个浏览器窗口页面就可以关闭了。继续回到ClineFreePool控制台，在账号列表里面就可以看到当前已经登录的Cline账号了：

![](https://image.woshipm.com/wp-files/sha256/14/d0/14d0bbf60dcbcb6820c6d16fc624956c3cc85a2a28654db33d543dea5301d3e6.png)

## 多账号池轮询

这里是支持多个Cline账号登录的，实现多账号池的轮询。为什么要登录多个Cline账号，原因在于Cline虽然提供免费模型，但免费模型依旧可能存在429限流的情况，而官方并没有公开说明具体什么时候会限流。

为了保证我们顺畅地使用免费模型，就可以登录多个Cline账号，加入到多账号池中。当一个账号被限流了，系统会自动切换到下一个备用账号，如此循环，从而实现不会因为限流而卡住无法使用。

前面提到过，Cline账号的注册可以使用Microsoft微软的账号。而微软的账号注册是门槛很低的，所以你就可以拿家里亲戚朋友的邮箱或者手机号码去注册多个微软账号，再用微软账号注册登录成Cline账号。

这点大家搞清楚逻辑，去实际操作就很简单了。老马就不登录多个Cline账号了，而是采用一个账号给大家演示。登录完Cline账号，接下来就可以获取API的地址和Key，我们在控制台左侧菜单点击接入配置：

![](https://image.woshipm.com/wp-files/sha256/96/da/96da29c47991ce531a4d8067a5e470ed6dfbdf9123238a1fc50f080c3f98bddd.png)

## 接入 WorkBuddy 实测

如上图可以看到，Base URL和API Key都是现成可以直接复制的。凡是给Agent和AI聊天工具接入过大模型的，再熟悉不过。老马直接点击复制按钮，然后打开WorkBuddy的设置，找到模型设置，选择自定义接入第三方模型：

![](https://image.woshipm.com/wp-files/sha256/f3/bc/f3bc2635f24b0eff59b849802e43e3ccf21ffe18ddf90a75d4b6a8ca2a815a68.png)

把刚才复制的Base URL接口地址，以及API Key粘贴进去。模型名称上文中老马提到过了，你就回去控制台的模型页面，已启用的模型列表里面，选择一个免费模型复制一下模型名称填入进去就行了。

老马这里接入的是模型名称是小米的Mimo V2.6 Flash，最后点击一下测试连接，提示连接成功。这说明咱们的本地反代服务是正常的，Cline账号是登录成功的，同时获取免费模型服务也是成功的。

最后在WorkBuddy的自定义第三方模型接入页面点击保存，保存好刚才的模型配置接入信息即可。回到WorkBuddy新建个任务，左下角的模型选择刚才接入的Mimo V2.6 Flash。

老马就随便发送一句话，问它是什么模型，以及让它在本地桌面创建个Word文档写一首赞美老马的诗：

![](https://image.woshipm.com/wp-files/sha256/55/02/5502f740c5b3465837964a3f97069af9ef95dc11b19d1cdc86575c6751ee112c.png)

可以看到，都是成功的，这说明免费模型已经可以正常使用了。以上操作适合市面上主流的Agent或者AI聊天工具的接入，流程都是差不多的。有了Cline的免费模型，加上多个Cline账号轮询，你又免费实现了token自由。

而且Cline的免费模型，大部分都是最新上线的新模型，你还能抢先体验到新模型的能力。至于Cline什么时候会停止免费模型服务的福利，或者进行更严格的限流和额度限制，这就不好说了。

截止老马本文发布时，该项目和操作都是可行的。按道理讲Cline这样有投资有实力的国外公司，还具备一定的知名度和影响力，不至于会一下子就抠门拉闸的。

还是那句老话，该薅的时候抓紧薅，不要等错过了再后悔莫及。老马体验下来，免费模型的调用速度还行，日常作为平替和补充使用完全足够了，不要钱的也不能要求太高了。

作者：马佳彬 公众号：马佳彬

本文由 @马佳彬 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自 Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6474226.html