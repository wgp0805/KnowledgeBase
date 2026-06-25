---
title: "Agnes video Generator: 我如何用零成本做出带旁白字幕的多场景AI视频 - mobility"
source: "博客园"
url: "https://www.cnblogs.com/buptl/p/20779902"
date: "2026-06-24T11:56:00Z"
score: 0.2
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Agnes video Generator: 我如何用零成本做出带旁白字幕的多场景AI视频 - mobility

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/buptl/p/20779902  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.2

  * [ ![博客园logo](//assets.cnblogs.com/logo.svg) ](<https://www.cnblogs.com/> "开发者的网上家园")
  * [会员](<https://cnblogs.vip/>)
  * [周边](<https://cnblogs.vip/store>)
  * [新闻](<https://news.cnblogs.com/>)
  * [博问](<https://q.cnblogs.com/>)
  * [闪存](<https://ing.cnblogs.com/>)
  * [赞助商](<https://www.cnblogs.com/cmt/p/19316348>)
  * [Chat2DB](<https://chat2db-ai.com/>)


  * ![搜索](//assets.cnblogs.com/icons/search.svg) ![搜索](//assets.cnblogs.com/icons/enter.svg)
    * ![搜索](//assets.cnblogs.com/icons/search.svg)

所有博客
    * ![搜索](//assets.cnblogs.com/icons/search.svg)

当前博客
  * [ ![写随笔](//assets.cnblogs.com/icons/newpost.svg) ](<https://i.cnblogs.com/EditPosts.aspx?opt=1> "写随笔") [ ![我的博客](//assets.cnblogs.com/icons/myblog.svg) ](<https://www.cnblogs.com/my> "我的博客") [ ![短消息](//assets.cnblogs.com/icons/message.svg) ](<https://msg.cnblogs.com/> "短消息") [ ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg) ](<javascript:void\(0\)> "简洁模式启用，您在访问他人博客时会使用简洁款皮肤展示")

[ ![用户头像](//assets.cnblogs.com/icons/avatar-default.svg) ](<https://home.cnblogs.com/>)

[我的博客](<https://www.cnblogs.com/my>) [我的园子](<https://home.cnblogs.com/>) [账号设置](<https://account.cnblogs.com/settings/account>) [会员中心](<https://vip.cnblogs.com/my>) [ 简洁模式 ... ](<javascript:void\(0\)> "简洁模式会使用简洁款皮肤显示所有博客") [退出登录](<javascript:void\(0\)>)

[注册](<https://account.cnblogs.com/signup>) [登录](<javascript:void\(0\);>)



[ ![](https://assets-cdn.github.com/images/modules/logos_page/Octocat.png) ](<https://github.com/lcy362>) [ ![](assets/2026-06-25-Agnes%20video%20Generator%20%E6%88%91%E5%A6%82%E4%BD%95%E7%94%A8%E9%9B%B6%E6%88%90%E6%9C%AC%E5%81%9A%E5%87%BA%E5%B8%A6%E6%97%81%E7%99%BD%E5%AD%97%E5%B9%95%E7%9A%84%E5%A4%9A%E5%9C%BA%E6%99%AFAI%E8%A7%86%E9%A2%91%20-%20mobility/74ee3ec8cf28312d02634481fe16ffab_MD5.svg)](<http://stackoverflow.com/users/3448633/mallowfox>)

[![返回主页](/skins/custom/images/logo.gif)](<https://www.cnblogs.com/buptl/>)

# [Mobility](<https://www.cnblogs.com/buptl>)

## 

  * [ 博客园](<https://www.cnblogs.com/>)
  * [ 首页](<https://www.cnblogs.com/buptl/>)
  * [ 新随笔](<https://i.cnblogs.com/EditPosts.aspx?opt=1>)
  * [ 联系](<https://msg.cnblogs.com/send/mobility>)
  * [ 订阅](<javascript:void\(0\)>)
  * [ 管理](<https://i.cnblogs.com/>)



#  [ Agnes video Generator: 我如何用零成本做出带旁白字幕的多场景AI视频 ](<https://www.cnblogs.com/buptl/p/20779902> "发布于 2026-06-24 19:56")

> "解决的办法不是压制 AI，而是让它变成一种更平权的能力，让每个人都知道如何借 AI 创造更多。这也是我们公司很重要的愿景，让世界级的 AI 属于每一个人。"

这是 Agnes AI 创始人 Bruce Yang 接受采访时说的一段话。

现在很多国内的AI厂商，无论deepseek还是智谱，都在把AI的价格往下压。坦率的讲，像文字、代码的处理价格，确实已经被压到了一个相当低的价格。但视频不一样，现在做AI视频，门槛确实高得离谱——国外的 Runway、Pika 按月订阅几十美元，国内的即梦、可灵免费额度用完就按秒计费，想本地跑开源模型？一张能跑视频的显卡轻松上万。

客观来讲，视频的生成，现阶段确实成本较高，让工业级的视频生成能力属于每一个人，确实不现实。但普通人也应该有一些途径能更多的去尝试、去创作，感谢Agnes开放自己的视频模型，让大家有这个机会。而这个项目只是想为了这个做一些微不足道的贡献。 [Agnes Video Generator](<https://github.com/lcy362/agnes-video-generator>)（[官网](<https://video.lichuanyang.top/>)）。说白了就是一个免费的AI视频生成器，不是那种"免费试用3次"的套路，是从写文案到出片、配音、上字幕，全程不花一分钱。只需要去 [Agnes AI](<https://platform.agnes-ai.com>) 注册个免费API Key就行。

Agnes的视频模型，目前确实称不上完美，但我想用这么一个项目，和Agnes一起成长，为AI平权，贡献上一点微不足道的力量。

## 多种玩法

给它一句话描述，它还你一条视频。分几种类型：

**简单视频。** 纯粹对API的封装，用来测试效果的，接口的各种参数，基本都做成了配置。

**创意视频。** 你写一个故事创意，比如"暗黑版青蛙王子"，AI全包：扩展故事→生成角色参考图→拆分场景→写分镜提示→逐段生成视频→配音→上字幕→拼接成片。全程10步自动跑完，你只需要等着看成片。通过预生成尾帧，可以最大限度的保障场景间视频的连贯性。

**文稿视频、数字人口播。** 贴一篇长文章进去，自动按语音时长分段，每段生成画面，或者放一个数字人在那里念稿。用一条完整的TTS旁白和字幕串起来。做知识区内容的可以试试。

各模式的详细参数和玩法，可以到[官网](<https://video.lichuanyang.top/>)上看，这里就不展开了。

## 跑起来很简单
    
    
    git clone https://github.com/lcy362/agnes-video-generator.git
    cd agnes-video-generator
    ./start.sh
    

就这三步。`start.sh` 会自动帮你建虚拟环境、装依赖、启动服务。

启动后打开 `http://localhost:8765`，在页面顶部填上你的 Agnes AI API Key，选个模式，写你的创意，点生成，然后耐心等结果就行。

用 Cursor 或者 Claude 这些AI Agent的话更方便，我专门为Agent做了使用说明，直接让你的Agent读项目里的Agents.md文件，它自己就能把环境搞好、把服务跑起来。

## 看看效果

做了几个demo,可以看看效果：

  * [暗黑版《青蛙王子》无旁白版](<https://v.douyin.com/L4F6KdGnD6U/>) — 5个场景用关键帧衔接，全自动生成
  * [同一个故事加了旁白字幕](<https://v.douyin.com/l2FlbF1Jdz0/>) — AI配音 + 自动字幕，可以看看字幕的效果
  * [文稿视频](<https://v.douyin.com/eSGE9KENWVU/>) — 贴了篇长文进去自动分段，每段配不同画面



## 最后

回到开头 Bruce Yang 说的那句话——「让世界级的 AI 属于每一个人」。

这个项目不是什么宏大的事业，就是想让 AI 视频创作这道门开着。不用订阅、不用好显卡、不用花一分钱，你只需要一个免费的 API Key 和一台能跑 Python 的电脑。

代码在 [GitHub](<https://github.com/lcy362/agnes-video-generator>)，官网在 [video.lichuanyang.top](<https://video.lichuanyang.top/>)。欢迎提bug。

原文地址： <https://lichuanyang.top/posts/22470/>

posted @ 2026-06-24 19:56  [mobility](<https://www.cnblogs.com/buptl>)  阅读(93)  评论(0)    [收藏](<javascript:void\(0\)>)  [举报](<https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fbuptl%2Fp%2F20779902&targetId=20779902&targetType=0>)

刷新页面返回顶部

[ ![](assets/2026-06-25-Agnes%20video%20Generator%20%E6%88%91%E5%A6%82%E4%BD%95%E7%94%A8%E9%9B%B6%E6%88%90%E6%9C%AC%E5%81%9A%E5%87%BA%E5%B8%A6%E6%97%81%E7%99%BD%E5%AD%97%E5%B9%95%E7%9A%84%E5%A4%9A%E5%9C%BA%E6%99%AFAI%E8%A7%86%E9%A2%91%20-%20mobility/31f2f8bc4f9df511b9d79843cbce27cf_MD5.webp) ](<https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs>)

### 公告

[博客园](<https://www.cnblogs.com/>)  ©  2004-2026   
[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](<http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771>) [浙ICP备2021040463号-3](<https://beian.miit.gov.cn>)


---
> 原文链接: https://www.cnblogs.com/buptl/p/20779902