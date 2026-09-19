---
title: "微信和 VS Code 强强联合！WeChat AHP 来了 - formulahendry"
source: "博客园"
url: "https://www.cnblogs.com/formulahendry/p/23036505"
date: "2026-09-19T03:37:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 微信和 VS Code 强强联合！WeChat AHP 来了 - formulahendry

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/formulahendry/p/23036505  
> **抓取日期**: 2026-09-19  
> **相关性评分**: 1.0

大家好！我是韩老师。

大家应该知道，差不多半年前，我发布了 WeChat ACP：

[深夜发布！微信可以连上 Claude、Codex、Copilot、Qwen、Gemini、OpenCode 等各类 Agent！](<https://mp.weixin.qq.com/s?__biz=MzIwODE4Nzg2NQ==&mid=2650564681&idx=1&sn=3e7a4626aa02f2196d3c9303a8e29c02&scene=21&poc_token=HKICrmqjBAV2F8RQZSO9QUk2ey1e6IcCU2a2Yazg>)

如今，已经有超过 14K 的下载量了：

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/2acdd85b9b05e8e55071e8ca8f66ba11_MD5.webp)

在之前的文章中（[六天小长假，开始！](<https://mp.weixin.qq.com/s?__biz=MzIwODE4Nzg2NQ==&mid=2650565124&idx=1&sn=671d68ccbfca2122fb1893f850690bbc&scene=21&poc_token=HMECrmqjhCwVuwaYjmxDeVkEi-0wNxiED9qwNYB6>)），我提到了我领导的项目 Agent Rosetta: AHP x ACP - Universal Agent Host 获得了第一届 CoreAI China hackathon 的 People's Choice Award 大奖！

那么，AHP 又是个什么东西？

9/5 我在 PyCon 的分享中，我帮大家问了：

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/0fe77ed3bce8b930367c0810aae84ec0_MD5.webp)

不过，不要慌，AHP 和 ACP 是强强联合的关系：

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/c38fd1e822c33b96facc995f7677dfc7_MD5.webp)

然后，铺垫了这么多，我们就可以回到主题了：微信和 VS Code 的强强联合！

今天，我很高兴和大家分享：

我发布了 VS Code 的 WeChat AHP extension。

[WeChat AHP - Visual Studio Marketplace](<https://marketplace.visualstudio.com/items?itemName=formulahendry.wechat-ahp>)

[https://open-vsx.org/extension/formulahendry/wechat-ahp](<https://open-vsx.org/extension/formulahendry/wechat-ahp>)

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/d041dbca1aae886c88cb151e3c6f419d_MD5.webp)

它可以让你的微信和 VS Code 的 Agent session 双向实时同步，在何时何地，都能通过微信远程操控你的 VS Code Agent！

VS Code 的 session：

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/6c74bbe63d19bb2a766f3f7835bd5eae_MD5.webp)

微信的 session：

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/2ec182db78b249cff56351d2367161fe_MD5.webp)

通过 AHP，他们的 read-write 操作，都是毫秒级实时同步的！

![](assets/2026-09-19-%E5%BE%AE%E4%BF%A1%E5%92%8C%20VS%20Code%20%E5%BC%BA%E5%BC%BA%E8%81%94%E5%90%88%EF%BC%81WeChat%20AHP%20%E6%9D%A5%E4%BA%86%20-%20formulahendry/d01e0213797ce0f33179b574d2255567_MD5.webp)

想一下这个场景：

你先在 VS Code 启动了一个 agent session。然后累了，躺在床上，拿出手机微信，因为 session 是实时同步到微信的，你又能无缝继续肝。接下来，你又坐到电脑前，VS Code 的 agent session 是同步更新到最新的，你又可以在电脑前无缝继续肝。

ACP 解决了连接任何 Agent Harness 的问题，

AHP 解决了多 Client 实时同步 Agent Session 的问题。

其实，我们的需求，很简单：

随时随地，用任何 Client，操控任何 Agent；再随时随地，无缝切换到其他 Client，继续操控任何 Agent。

代码完全开源：

[https://github.com/formulahendry/vscode-wechat-ahp](<https://github.com/formulahendry/vscode-wechat-ahp>)

欢迎围观。

也可以通过命令行一键安装：
    
    
    code --install-extension formulahendry.wechat-ahp
    


---
> 原文链接: https://www.cnblogs.com/formulahendry/p/23036505