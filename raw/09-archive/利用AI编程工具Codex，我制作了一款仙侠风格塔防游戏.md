---
title: "利用AI编程工具Codex，我制作了一款仙侠风格塔防游戏"
source: "https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653263520&idx=1&sn=96b219fc173a09a69358bea01fb3481b&scene=21&poc_token=HL7WOWqjyzkpWhkk9FIRflFqTILtFkDM47YlEOLX"
---
小灰 程序员小灰 *2026年6月14日 11:19*

大家好，我是程序员小灰。

前几天小灰发布了一篇文章，说自己打算入局AI游戏开发，并给出了一份投票调研，看看大家最希望看到的游戏类型：

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/3a55514e3a3a351c75602a677f6adb03_MD5.webp)

经过调研发现，大家最喜欢的游戏类型是塔防类游戏，类似于《植物大战僵尸》、《王国保卫战》。

既然如此，小灰安排上！很快，我就用Codex制作出了一款仙侠风格塔防游戏的Demo。

这个Demo虽然不大，但是麻雀虽小五脏俱全，既包含了游戏主界面、战斗界面、设置界面，也包含了背景音乐和音效，还包含了存档和读档功能，更包含了塔防游戏的核心玩法。

游戏中的所有代码、文案、美工、音乐素材，全部由AI生成，大家可以看一下游戏演示的视频：

，时长02:23

<video src="https://mpvideo.qpic.cn/0bc3w4cdqaaeyaabdlbj5fvfjn6dhc3qioaa.f10002.mp4?dis_k=deb3cacb3dcc31cf5d48500ebcbbf6f7&amp;dis_t=1782175424&amp;play_scene=10120&amp;auth_info=J6SF3uRdGC1i4prxr1x3P2ZqHj8bAHhsFwAJJCc0EjYaCD9SI3MDYBUtOEU4NnofcmA=&amp;auth_key=50af5e42693fbc5837e6764b6ff1c3d9&amp;vid=wxv_4559248051659554818&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

小灰从策划到完成游戏Demo，前后仅仅用了不到3个小时，我是如何做到的呢？接下来我为大家做一个详细的拆解。

一、写策划文案

要开发一款游戏，第一步既不是写代码，也不是画美工素材，而是写出一份游戏策划文案。

小灰把这个光荣的任务交给Codex来完成，让Codex生成一个仙侠风格塔防游戏的策划文案，提示词如下：

做一个仙侠类塔防游戏，帮我做一个完整的游戏策划案。

很快，Codex为我生成了一段冗长的策划文案，看得小灰有些头晕：

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/2d5954629950f296d9b3e3ec15e0225f_MD5.png)

于是小灰改变提问方式，让Codex为我策划一个最小的可运行Demo，提示词如下：

想先做一个Demo，塔的类型只有两种，分别是两个门派的弟子，每一种弟子可以升5级，级别名字根据流行修仙小说来设计。地图也只做一个。怪物设计2种。10波战斗。再设计出游戏主界面。

Codex为我提供的策划文案仍然有些复杂，于是小灰再次做了简化，提示词如下：

再简化一些，暂时只有一次升级，怪物只有两种，UI和界面先不用美工素材，特效也先不要。请列出相应的美工素材清单。

终于，Codex为我列出了一份相对简单的策划案，并提供了所需美工素材的清单。

根据清单描述，我们需要地图素材一份，人物素材10份，怪物素材2份。

美工素材的提示词如何写呢？不用我们来操心，直接让Codex写出来。提示词如下：

给出美术素材的中文提示词，我要用GPT-image-2生成图片。

最终，Codex为我们生成了所有素材的提示词，大部分可直接复制使用。

二、美工素材制作

有了美工素材的提示词，我们可以让公认最强的AI绘画模型GPT-image-2

开始干活了。

首先画出地图素材：

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/39453d86c17981cb77a4847fcc98da4c_MD5.png)

然后画出人物（防御塔）素材：

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/01c8642435643298899e5a6e67625d3b_MD5.png)![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/a89260e1d3c641d4acc3895b1d47f1c0_MD5.png)

其中每一个人物包含5个等级，两个人物加起来总共10张素材图，由于篇幅原因，我们这里只展示其中4张图。

最后是怪物素材：

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/817025478abe9faad76287b582216e35_MD5.png)

三、游戏音乐制作

如今国内外有很多强大的AI音乐制作平台，其中网易天音（tianyin.163.com）比较适合游戏音乐的制作。

音乐生成的提示词怎么写呢？我们仍然让Codex给出，提示词如下：

想生成一个跟游戏匹配的背景音乐，给出提示词。

很快Codex给出了提示词，我们把提示词复制到网易天音平台，一口气生成多首曲子，从中选择最合适的一首作为游戏背景音乐。

![图片](assets/%E5%88%A9%E7%94%A8AI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7Codex%EF%BC%8C%E6%88%91%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E6%AC%BE%E4%BB%99%E4%BE%A0%E9%A3%8E%E6%A0%BC%E5%A1%94%E9%98%B2%E6%B8%B8%E6%88%8F/52d4c5f7a3f5f6e3d976139cf592fc9f_MD5.png)

四、第一版代码

如今万事俱备，只欠东风。我们把先前生成的所有素材统一放在一个文件夹之下，让Codex为我们生成游戏代码，提示词如下：

按照刚才的设计，用Godot 4引擎制作一个2D塔防游戏demo，带有可执行的exe文件，游戏美工素材在 ”D:\\塔防游戏素材”。

大约等待10分钟，Codex就为我们生成了可以直接运行的游戏Demo，第一版Demo的运行效果如下：

，时长02:28

<video src="https://mpvideo.qpic.cn/0bc37acnqaaek4ajtxzj55vfj6gd3d4ajwaa.f10002.mp4?dis_k=9e8309174d2d2a6642fc5ced5a55c38d&amp;dis_t=1782175424&amp;play_scene=10120&amp;auth_info=euWlj4kHSnhl4sv2rgwib2c8TGQbUy1tQAJecyIxTGVHCGVScCtRNRItaUI5Zi9PczY=&amp;auth_key=a9b6275c9a3f80a39cb3e8eb0bc021ad&amp;vid=wxv_4559352073687138306&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

五、第二版代码

虽然游戏的可运行版本出来了，但仍然存在一些不足之处，比如：

1\. 游戏主界面相对简陋。

2\. 从主界面直接跳转到塔防界面有些突兀，缺少一个地图选择界面作为过渡。

3\. 缺少游戏设置界面，用于调节游戏的分辨率和音量。

4\. 游戏缺少存档和读档功能。

不过这些都不是什么大问题，我们把迭代的想法发给Codex，让Codex为我们生成更多美工资源的提示词，并再次编写游戏代码。

我们第二版的游戏效果，就是大家在文章开头所看到的。

怎么样？这个新版本的完成度是不是高了很多？

六、写在最后

好了，关于如何利用Codex开发仙侠风格塔防游戏，我们就介绍到这里。

文中展示的开发流程看似简单，但实际使用 Codex 及各类 AI 工具时，我做了不少尝试与调整，整个开发过程耗时约 3 小时。

后续，小灰计划把这款游戏发布到Steam平台，敬请期待~~

对了，“万法守山”只是AI随意起的游戏名，我们这款游戏还未正式命名。如果各位公众号的朋友想到什么好听又好记的名字，欢迎在留言区提出。

