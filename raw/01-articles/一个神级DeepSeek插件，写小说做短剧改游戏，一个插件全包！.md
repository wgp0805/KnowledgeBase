---
title: "一个神级DeepSeek插件，写小说做短剧改游戏，一个插件全包！"
source: "https://mp.weixin.qq.com/s/KOlImTpdg8j11-3EIhe6xw"
author:
  - "[[丛林]]"
published:
created: 2026-11-19
description: "一个神级DeepSeek插件，写小说做短剧改游戏，一个插件全包！"
tags:
  - "clippings"
---
程序员追风 *2026年11月18日 22:00*

最近翻到一个虽然不热门但感觉挺牛的插件，叫 oh-story-dsh，这个插件装完之后，DeepSeek Harness 里就多了四个创作工作台，小说、短剧、互动游戏、视频解说各一个。

写连载、出短剧、把小说改成能玩的游戏、给视频配解说，这些任务都可以在我们熟悉的 DeepSeek Harness 中完成了，而且操作上我觉得还是比较丝滑的，看得出作者是有这方面经验的。

今天给大家分享一下这个开源插件。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/c2decf9c1f46f421d0700afe20fb48dc_MD5.webp)

## 先说清楚它是什么

oh-story-dsh 是 DeepSeek Harness 的社区插件，里面打包了四套创作技能包，都是固定版本的：小说的有 14 个 Skills 和 7 个专业角色，短剧的 12 个 Skills，互动游戏 5 个，视频解说 2 个。每套技能包都配了一个图形工作台，干活的时候不用光盯着对话框。

用起来和原来的 DSH 没什么区别，Agent、会话、模型配置、权限审批，全是原来那套东西，不用重新学。写出来的东西也都在你本地目录里，就是普通的 Markdown、JSON 和媒体文件，打开文件夹就能看到。

平时打开写代码的仓库，它根本不露面，目录里真有创作工程了，工作台才展开。

## 小说工作台：管好一部长篇连载

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/3962158d15240e5e60e2f0c4de93f11f_MD5.gif)

界面是三栏的，左边文件树，中间 Markdown 编辑器，右边就是 DSH 原来的对话。Agent 写设定、写大纲、写章节的时候，编辑器实时跟着变，点对话里的文件路径就直接打开那份稿子。你自己改到一半还没保存的草稿，也不会被它写东西的时候冲掉，这块它有保护。

能实现的功能不少：选题、扫榜、拆文、长短篇连载、审稿、去 AI 味，还有番茄小说的建书资料整理和封面提示词。建书资料这个，它只整理你确认过的内容存成文件，不替你登录后台发布。

工程里有个「追踪/上下文.md」，AI 会一直维护它，记着当前写到第几章、哪些伏笔没回收、有什么连贯性风险。官方演示工程里，第 20 章写完的时候，这个文件里就记着一条 F016：钟嘉嘉的军方家庭背景还没公开，第 7 章埋的，回收章未定。

## 短剧工作台：一个镜头拆成五份文档管

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/8de2b3b9c35bc5dd2a5b7912b39343f8_MD5.gif)

短剧这边是另一套做法，每集维护五份文档：剧本.md、视觉设定.md、分镜.md、图片提示词.md、视频提示词.md。

官方演示里有个例子，能看出为什么要拆这么细。「视觉设定.md」里有种叫连戏锁的东西，把跨镜头不能变的造型钉死，比如主角那件松枝绿常服，锁定词是 pine-green lapel service jacket，这个词会原样贴进后面每个相关镜头的提示词里。

「分镜.md」只管这个镜头从什么画面开始、做什么动作、到什么画面结束。「视频提示词.md」再把动作翻译成视频模型能执行的英文。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/9a771b6f444601c4a4c83c6d31489997_MD5.png)

界面默认是一张无限画布，剧本场次、角色参考板、分镜关键帧、视频片段都摆在上面，随便缩放拖动，看中哪个镜头可以直接带进右边对话继续改。「制作详情」还会自动查断链，分镜引用了不存在的场次、视频提示词绑错镜头号，直接报出文件名和行号。

## 互动游戏工作台：做好就能直接试玩

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/6c5f1b5a2bf4136c8c8a18628683b1f4_MD5.png)

游戏工作台是三个视角：试玩、创作画布、文稿。做好的游戏构建直接在左侧沙箱里跑，我们可以一边试玩，一边在右边跟 AI 说哪里要改。画布上摆的是原著依据、玩法设计、人物世界，以及它们和当前试玩版的对应关系。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/fe0cb7ae7794fbd6d76bfa896d38c6ee_MD5.png)

有个细节挺舒服。切换视图、收起对话都不会中断试玩进度，Agent 做出新版本以后，也是你自己决定什么时候载入，不会玩到一半被顶掉。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/79edaf7645edd5715302a26f49c4ca8e_MD5.png)

入口是 /novel-to-game quick，把小说文件丢给它改编成可玩的互动切片，做出来的东西都在 game-adaptations 目录里。

## 视频解说工作台：给现成视频配中文解说

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/4f60ef5a1325be90b14c5cbe40773cf1_MD5.png)

这个工作台干的事，是把现成视频做成解说成片。丢一个视频文件给它，它会拆剪、写分段解说词、配音、烧字幕。界面里可以边看成片边核对每段解说，有剪辑对应关系的地方能一键跳回原片画面。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/f607f9bbd3392acdcd11347d8d84dd0e_MD5.png)

解说词可以一段一段改了保存，时间轴不动，已经配好音的段落不会因为你改别的段就擅自重做。目录也不绕：原片在 sources，中间产物在 work，最终成片在 outputs。

机器上的 ffmpeg 带 libass 的话，字幕直接烧进画面，没有的话就给你一份外挂的 SRT 字幕文件。

## 安装和要准备的东西

需要 [Node.js](http://node.js/) 24.9 以上，然后两条命令：

```
npx -y --package pnpm@11.7.0 --package @deepseek-ai/dsh@0.2.
            2-rc.1
           dsh plugin --profile web add @oh-story/dsh@0.1.26 &&
npx -y @deepseek-ai/dsh@0.2.
            2-rc.1
           web
```

跑完以后终端别关，浏览器一般会自己弹出本地页面，没弹的话就把终端里那个带 token 的链接复制出来打开。进去以后在「设置 → 模型」里填 Provider 和 API Key，用 DeepSeek 官方接口的话，提前把 DEEPSEEK\_API\_KEY 这个环境变量设好也行。

插件装完，纯文字的任务就能干了，也就是小说、互动游戏可以设计了。要出图、出视频、出成片，还得按这张表配东西：

| 需求 | 除了插件还需要什么 |
| --- | --- |
| 写小说、长篇连载 | 模型 Key 就够；拆文、导入旧稿、追踪这几个功能要 Python 3 |
| 短剧剧本、分镜等五份文档 | 模型 Key 就够 |
| 短剧关键帧图片 | GPT Image 2 的 Key |
| 短剧视频片段 | Seedance（火山方舟）或 MiniMax H3 的 Key |
| 短剧配音配乐 | MiniMax 的 Key |
| 短剧合成成片 | Python 3.9+、ffmpeg / ffprobe |
| 视频解说成片 | Python 3.10+、ffmpeg / ffprobe、MIMO\_API\_KEY；用 Fish Audio 配音再加 FISH\_API\_KEY |

看着多，按需配就行。缺哪个没配，短剧工作台的「制作详情」会直接告诉你缺哪个环境变量。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/eadea107dc65c8e2f51b0303710a45fb_MD5.jpg)

## 我的看法

我觉得这插件最值的一点，是它在我们熟悉的 DSH 里直接改出了四个创作工作台，工具不用换，习惯也不用改，原生 DeepSeek 用着就挺好。

写出来的设定、大纲、正文、追踪全是本地文件，AI 每动一笔你都能看到改了哪个文件。对写连载的人来说，这算刚需；靠聊天窗口写，聊几十轮就失忆，二十章以后基本没法用。

另外提醒一下，完整的短剧、视频流水线要配的东西可是不少，Python、ffmpeg、各家媒体的 Key，纯小白上手有门槛，更像是给本来就折腾过 AI 工具的人准备的。严格来说，插件安装才只是第一步，这套并不能算开箱即用的东西。

## 开源地址

开源仓库：zenstory-ai/oh-story-dsh

用 Claude Code / Codex 的可以直接装这四个独立技能包，都在同一个 GitHub 组织下面：oh-story-claudecode（小说）、drama-skills（短剧）、novel-to-game（游戏）、video-recap-skills（视频解说）。

![图片](assets/%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7DeepSeek%E6%8F%92%E4%BB%B6%EF%BC%8C%E5%86%99%E5%B0%8F%E8%AF%B4%E5%81%9A%E7%9F%AD%E5%89%A7%E6%94%B9%E6%B8%B8%E6%88%8F%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%85%A8%E5%8C%85%EF%BC%81/000659fdef65615a176821139f9416c4_MD5.webp)