---
title: "Claude(Code)桌面APP，保姆级全攻略，一期视频精通"
source: "https://mp.weixin.qq.com/s/QSybuRUrQe8LSjHNG5-W7w"
author:
  - "[[技术爬爬虾]]"
published:
created: 2026-11-11
description: "你对 Claude Code 的认识可能已经过时了。"
tags:
  - "clippings"
---
技术爬爬虾 技术爬爬虾 *2026年11月10日 15:37*

你对 Claude Code 的认识可能已经过时了。最近 Claude 桌面端有了一大波功能更新，随着一步步的迭代，它已经把 Claude Code 的编程能力、Claude Design 的设计能力，以及 Claude Cowork 的办公等核心能力，全部收入进了同一个桌面客户端。特别是 Claude Code，已经从原本黑乎乎的命令行工具，进化成了桌面客户端的完全体形态。再搭配上超强的 Opus 5.5 模型，Claude 客户端已经能称得上是地表顶级的 Agent 工具。

本期视频带来一个 Claude 桌面端的手把手教程，分为以下 11 个章节，我们对 Claude 桌面端的全部功能进行细致讲解，一起来看看地表顶级的 Agent 工具到底长什么样。好，废话不多说，我们直接开始。

## 把 Claude 桌面端接入国产模型

在上期视频里面，我详细介绍过如何稳定使用 Claude 官方订阅，我用这个方法已经稳定使用 1 年了，对这块不熟悉的观众朋友们可以去看一下那期视频。当然，使用官方订阅确实比较复杂，本章节我就来介绍一个方法：把 Claude Code 桌面端接入国产模型。

我们来到 Claude 桌面端，这里不需要登录，我们直接点击左上角的菜单，在“故障排查”里面点击“启用开发者模式”。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/cbeb86f5ae71fc4fa839516face459ea_MD5.webp)

然后还是在菜单里面找到“开发者”，找到“配置第三方推理”，在这个页面就可以配置任意的大模型 API。这里 Credential 我选择 static API key。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/4c7bdb19ba04e8905d57adf3fa73a815_MD5.jpg)

本期视频我以 DeepSeek 的 API 为例。来到 DeepSeek 的 API 开放平台，找到 API keys，点击创建，创建一个 API key，然后复制下来，填写到这一行 Gateway API keys。接下来填写 Base URL：我们点击 DeepSeek 的接口文档，选择这个 anthropic 的 URL，把它复制一下，填写到上面，然后把这个开关开启起来，使用百万上下文。

接着在模型列表这里配置模型。我们在 DeepSeek 的文档里面可以看到，Claude Opus 开头的模型会被映射到 DeepSeek V4 Pro，Claude Sonnet 开头的模型会被映射到 DeepSeek Flash。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/2dd3abf2d6debba79373e33f7de0c370_MD5.jpg)

我一般使用的模型就是 DeepSeek Flash，所以这里我一般填一个 `              claude-sonnet-5.5            ` ，名字也填它。然后点击 Apply changes，点击“保存并且重启”。

接下来我们就进入了 Claude 桌面端，这里可以打个招呼，给到了回复，我们的配置就成功了。DeepSeek 的 API 还有个好处，它原生支持 Claude Code 的搜索功能。比如这里我让它搜索一下青岛的天气，我们看到它可以调用搜索的 API，搜到青岛的天气。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/9a6ce68d93e7151d7f05014bb17c5e88_MD5.jpg)

我们把第三方模型接入 Claude 桌面端存在一个问题，就是它的功能不全，比如它没有内置浏览器，然后也没有 Claude Design、PPT、Excel 等等这些功能。所以本期视频我主要还是以官方订阅为例进行演示。

## 三栏布局与三种工作模式

Claude 桌面端是经典的三栏布局：左侧是对话列表，中间是对话窗口，右侧是多功能区域。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/676f8b9ad74e067d01d0944e341090fa_MD5.jpg)

桌面端主要有三种工作模式：Chat、Cowork 还有 Code，我们可以在对话列表的顶部进行切换。在 Home 里面是 Chat 跟 Cowork 模式的入口，我们可以在对话窗口里面切换 Chat 或者 Cowork；在对话窗口的顶部，还可以切换成 Code 模式。

最近 Claude 桌面端正在灰度测试一个新版本的 UI 功能，就是把 Chat 跟 Cowork 两个模式合并起来。新，新版本的 UI 顶部变成了这么两个小按钮：Claude 还有 Code。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/75142a32cd1450af1b38ab55eae4eb52_MD5.jpg)

这个 Claude 就是原来的 Home 页面。进来以后还有一个变化，就是它去掉了原来的 Chat 还有 Cowork 的切换按钮，Claude 会自动根据工作类型，判断使用 Chat 模式还是 Cowork 模式。

Chat 模式的核心定位是对话 Agent，它最适合用来问问题、解释代码、翻译、查资料等等。Chat 模式的功能仅限于对话，它不会操作本地电脑来工作。Cowork 模式的定位是通用办公 Agent，最适合用来做调研、分析文件，还有做文档、做报表、PPT 等等。Code 模式也就是我们常说的 Claude Code，它的核心定位是软件开发 Agent，最适合用来改代码、跑命令、测试、修 bug 等等。

不过我目前测试下来，感觉 Code 的功能比 Cowork 更加强大，而且干活更积极主动，所以在大部分场景下，建议直接使用 Code 模式。还有一点要注意，这三个模式都是要消耗订阅额度的，包括你从网页端的聊天，也是一样会消耗额度的。

## 创建工作区：本地环境

让 Claude 帮你干活，第一步就是先创建工作区。工作区可以把文件夹、对话进行集中管理。Code 跟 Cowork 模式对于工作区有不同的叫法：在 Code 模式里面叫做 Environment（环境），而在 Cowork 那边叫做 Project（项目）。先看 Code 模式，创建一个新的工作区，也就是环境。在 Cowork 这边也是点击按钮，然后点击 New project，创建一个新的项目。

我们来看一个例子。我在 Code 里面先创建一个 Environment，Environment 里面可以设置环境变量。比如我要做个 AI 画图功能的项目，我可以来到 OpenAI 的开放平台，创建一个 OpenAI 的 API key，然后把它复制下来，再来到 Environment 这边，点击创建环境变量，然后输入 `OPENAI_API_KEY=` ，后面是刚才创建的 API key。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/3431279715c9ad1fe8aa75b146475bd5_MD5.jpg)

把这个 API key 配置到环境变量里面，这样我不用写文件，也不用污染电脑上的全局环境变量，就能让这个环境获得 AI 画图的能力。

接下来我给环境起一个名字，然后选择一个文件夹作为工作文件夹。这里也可以添加多个文件夹，比如你可以把前端、后端两部分代码分成两个文件夹管理，加到同一个环境里面。最后点击保存。

我们来测试一下。我跟 Claude Code 说：我需要项目有 AI 画图能力，环境变量里面我已经配置了 OpenAI 的 API key。Claude Code 写了两个脚本，把这个画图功能跑通了。接下来我让它画一只猫，看到也成功画出来了。

## 创建云端工作环境

当我们创建环境的时候，除了在这里添加本地文件夹来创建本地工作环境，我们也可以创建云端工作环境。我们创建云端工作环境，一般要添加 GitHub 上面的代码仓库，让它基于那个仓库进行工作。

第一步，我们要给 Claude 配置 GitHub 的连接器。这里我们来到 Claude 左侧菜单，找到这个 Customize，找到 Connectors → Yours，这里有一个 GitHub 集成，我们点击这个 Connect 按钮，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/31b2d38f33df2c5fd34763d9c377ab2f_MD5.jpg)

登录一下你的 GitHub 账号，这样就连接成功了。这样 Claude 就能读取到你 GitHub 上面的项目了。

然后我们再来创建环境，选择云端，这里就可以选择 GitHub 上面的项目作为工作环境，比如我选择这个项目。在下面还有 4 个选项，非常好用。第一个可以选择云端环境是否可以访问网络，它默认是白名单机制，这里我选择可以访问全部网络。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e02a0244713b96ab4a4fdab21844690f_MD5.jpg)

然后下面可以设置密钥、设置环境变量，这个也非常好用：因为我们的 GitHub 仓库里面是不会上传密钥的，我们就可以把密钥等环境变量直接填到 Claude 的环境里面，提供给 Claude 去使用。这里 setup script 可以设置一个启动脚本，Claude 每次启动云端开发环境的时候，都会先运行一下这个脚本。配置完成以后点击 Add Environment，这样我们就创建好了一个云端开发环境。

比如我让 Claude Code 总结下这个项目是做什么用的。我们在右侧环境这里有一个云彩，表示这是一个云端环境，也就是即使我们关闭了本地的 Claude Code 桌面端，它一样可以在后台运行。使用云端环境还有一个好处：我们在网页端的 Claude Code 里面也可以指挥它干活，这样不需要我们电脑开着，它也能处理工作、完成任务。

## 模型、思考强度与权限模式

在对话窗口的下面，可以选择模型跟思考强度。对于编程、创意性任务，还有高难度的任务，建议选 Opus 5.5。在权威测试榜单 Artificial Analysis 上面可以看到，Fable 5.1 的评分还不如 Opus 5.5，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/1ab5898d7ba9accab5584155152720bf_MD5.jpg)

所以我基本上不会使用 Fable 模型。普通难度的任务可以选择 Sonnet，简单的重复任务可以选择 Haiku。还是在 AA 的榜单里面可以看到，Haiku 的智力水平比绝大部分的开源模型都要高，选择 Haiku 模型可以用极其低廉的成本获得很不错的智力水平。

然后在 Effort 这里可以选择推理强度，这里可以根据任务的复杂度来选择对应的思考强度。Opus 模型选择 medium 或者 high 的强度，就足够应付大部分的任务了。

在模型右边的按钮是权限，这里建议无脑选择 Auto，也就是自动权限模式。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/cd6ca90d1be1bef650c38fd4c538d8a4_MD5.jpg)

Claude Code 会对将要执行的命令进行自动审查，自动判断哪些命令可以放行，并且对高危命令进行自动拦截。这个模式非常好用，它几乎不会遇到停下来等待你审批这种问题，这个模式取得了效率跟安全的完美平衡。

Claude Code 默认是不启用沙箱功能的，它的安全防护主要是靠模型的自动审查。虽然没有沙箱，但是它出事故的概率更低，还有丝滑程度明显比 Codex 更好用，这里必须要夸一下。

除了默认的 Auto 模式，还有一个 Plan 模式我经常会用。启动 Plan 模式以后，Claude Code 就不会直接修改代码，它会先出一份计划，等待用户确认计划以后，才会进行修改代码。所以新版本的 Claude 常用的权限模式，就是一个 Auto 还有 Plan 这两种。

## 用量限额

在权限的右边是用量限额，这里有两个限额，一个是 5 小时限额，还有一个周限额，这两个任何一个到达上限，Claude 桌面端都不能继续使用了。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/753180364f160b70b5979e7621d1dfb9_MD5.jpg)

我们点击这个 See all，可以查看几种工作模式消耗的订阅用量。我这里最多的是 Claude Code，然后是对话。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/3be98f0781db8dc82ea4c71e84cbab21_MD5.jpg)

注意，在 Claude 里面 Chat 模式会消耗订阅额度，包括你在网页上的对话，一样会消耗额度。

## 三种追加指令的方式

接下来我们看怎么在 Claude 的执行过程中给它追加指令。Claude 有三种追加指令的方式，分别是 Steering、Queue 还有 Send Now。

其中，Claude 桌面端默认的指令追加方式是 Steering，也就是控制引导。我们可以在 AI 的执行过程中直接追加一条指令，Claude 会在执行完手头这次工具调用以后，读到我们追加的指令。这里说的工具调用，指的是读文件、写文件、读网页这类的具体动作。也就是说，AI 可以在做完这个动作以后，立即根据新追加的指令对后续工作进行调整。

我们来看一个例子。我先让 Claude 查一下芝加哥的天气，就在它的执行过程中，我又新输入了一条指令，然后直接回车发送给它。Claude 先把手头的这次读取网页的工具调用执行完毕，然后读到了新发过来的指令，它开始查询纽约的天气，最后把两个城市的天气整合到一个输出结果里面给到我。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e33b8e5b90edfec3261beb0c5ce9ed48_MD5.jpg)

我们来看第二种指令追加的方式，就是 Queue（排队）。这里还是先让它查询芝加哥的天气，接下来输入指令查询纽约的天气，不过这次我不是直接按回车发送，我是按 Ctrl + 回车发送。我们看到，我们新一条的指令在输入窗口这里正在排队。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/9b125cd5582e31449d2aec7eb99872fd_MD5.jpg)

也就是 Claude 会把手头的这一整轮工作全部处理完成，并且给了我们回复以后，它才能读到这个排队的指令，然后进行下一轮的处理。这种指令追加的方式就叫做排队。

接下来我们看第三种指令追加的方式，叫做 Send Now，这也是最激进的一种。我们还是按回车追加指令，然后这次我可以在对话窗口里面点击这个 Send Now 的小按钮，也就是立即发送。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/a02193e8b28db3a8741439937e610eea_MD5.jpg)

Send Now 会直接打断 Claude 手头的这次工具调用，直接把新的指令插入进去，这是一种更激进的方式。如果你觉得它这一轮的工具调用完全错误，就可以使用 Send Now 直接打断它。

## 后台任务：等待时不消耗 Token

我们再来插播一个 Claude Code 完爆了其他 Agent 的功能。我现在正在用 Claude Code 做本期视频的开头，现在这一步，Claude Code 已经把代码写好了，它正在把这些代码渲染成一个视频文件，这一步是比较耗时的。

我们看到 Claude Code 是怎么做的：它直接停下来了。它并没有启动一个会话来轮询，比如说隔 1 分钟上来看一次，而是它直接停下了工作，然后启动了一个后台任务在执行。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/021cd6379ec62b6a8f1a2db3cdcaae23_MD5.jpg)

当后台任务执行完毕以后，后台任务会发一个通知，再回到主窗口，然后主窗口拿到这个通知以后，再继续把任务跑完。后台任务现在跑完了，它给到了通知，给到了主窗口。

这个功能既保证了任务的丝滑流畅，而且又特别的省 Token，因为主 Session 完全停下来等待后台任务，等待过程中是完全没有 Token 消耗的。过了一会，视频渲染完毕了，然后 Claude Code 检查了视频，询问我是否要导出终稿。我点击导出终稿，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/eccdbafc1268434dd27c9abb2e1dfbae_MD5.jpg)

我们视频开头的那个片段就制作完成了。

## 对话侧边栏：环境、产物与上下文用量

接下来我们来看右边这个区域，叫做 Session Rail，也就是对话侧边栏。这里有三个功能：顶部是环境，就是我们刚才创建的那个 Environment，还有当前的工作文件夹；最下面的 Outputs 是产物区域，集中展示了 Claude Code 修改的代码，还有生成的图片等等；中间的 Context 是上下文使用量的展示窗口，里面详细展示了每部分的上下文占用量，比如展示了系统工具、对话历史、MCP 工具、系统提示词等等占用的上下文用量。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e7302c3eb77e6731c904a416a1322601_MD5.jpg)

这个功能真的是完爆了 Codex，不知道从哪个版本开始，Codex 连上下文用量的百分比都不展示了。Claude 模型虽然有百万上下文，但是我建议使用上下文窗口的时候不要超过 50%。如果上下文窗口过大，会导致注意力下降，还有 Token 消耗过快等问题。所以如果上下文积攒的比较多了，可以考虑新开一个对话，或者手动进行一次上下文压缩。

我们来看这个例子。比如我这个对话已经占用了 39% 的上下文了，我可以在对话窗口输入这个命令 `/compact` ，手动触发一次上下文压缩，在后面还可以填上你的需求，就是这次压缩重点保存哪些信息。在上下文压缩的时候，Claude Code 会对对话历史进行精简摘要，把一些不重要的信息排除掉。我们看到压缩完成以后，上下文用量从 39% 降到了 8%。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/8d18d1bd2ce13306400a8de51ff75fc5_MD5.jpg)

## 远程控制：在手机上继续对话

在对话侧边栏还有一个重要开关，叫做 Remote Control，也就是远程控制。开启以后，你就可以在手机上面看到这个对话了。这里我来到 Claude 手机端，打开左侧菜单，在对话历史里面就能看到我们刚才的对话，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/63bda0abc9399e272bf1ea36b693517e_MD5.jpg)

可以在这里输入指令，然后电脑那边就可以继续接着做。

也可以在左下角点击你的头像，在设置里面找到 Connect new session to Remote Control，也就是每次新对话都自动打开远程控制开关。下面这个开关 Keep this computer awake 也建议开启，可以保持电脑不休眠，随时接受远程控制。中间这个开关允许你通过手机或者网页端，给电脑上的 Claude Code 创建新的对话，如果经常手机跟电脑协同工作的话，这个开关建议开启。

## 用计划模式开发一个小项目

接下来我们开发一个小项目，来演示后面的更多功能。这里我让 Claude Code 做个宠物洗护的网站，用户可以提交洗护的预约信息，可以调用生图能力自动生成配图。因为这是一个全新的项目，我希望 Claude Code 先给我出一份计划，我确认后再实施，这样可以保证开发方向不会跑偏。所以在右下角的权限设置这里，我改成计划模式，敲回车开始。

使用计划模式有一个好处，是 Claude Code 很倾向于使用这种弹窗卡片的形式跟我来确认需求。它先问我生图功能怎么用，这里我选择生成固定的图片来装点网站。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/ec6645d9c3decd42209ebcca26649b68_MD5.jpg)

接下来它问我数据怎么存储，给的这两个方案我都不满意，这里我填上自己的需求： [Node.js](http://node.js/) 后端，再加上 SQLite 的本地数据库。

过了一会，Claude Code 为我们输出了一份完整的计划。我确认没问题以后，点击执行按钮，Claude Code 就按照计划开始编程，它把计划拆分成了几个步骤，然后依次完成。过了一会，开发工作就完成了，并且它已经把后台服务启动起来了。我们可以在会话侧边栏这里看到一个 Server，这里有一个启停按钮，我们可以随时在这里启停服务。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/edf163534ea6622d30423f144741bb03_MD5.jpg)

现在运行在 `localhost:3000` 端口，在浏览器里输入这个地址，就打开了 Claude Code 为我们开发的页面。

这个网页在我看来有一个问题，就是它的预约模块放到了整个网页的最下面，太不显眼了。我需要把整个模块往上提，放到一个比较显眼的位置，这样方便客户来预约。

## 侧边栏工具：终端、Changes、内置浏览器与文件列表

接下来我们就使用 Claude Code 对这个功能进行更改。我新开了一个对话，第一步我先让 Claude 把整个项目初始化成一个 Git 工程，方便后续对代码进行管理。然后输入我的需求：把预约模块放到 hero 下面，并且去掉宠物名字，还有宠物具体品种的输入。过了一会，Claude 完成了项目的开发。

我们再看一下右侧的几个功能。首先第一个 Terminal，也就是终端、命令行窗口，点击一下就打开了我 Windows 电脑上的 PowerShell 命令行窗口。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/84fea9f347c4716130223d337fbfc85f_MD5.jpg)

然后我可以在这里输入一些自己的命令，比如我可以手动地使用命令行来启停项目。

然后我们再来看这个 Changes 按钮，点击以后打开一个面板，这个面板展示的是当前工作区到 main 分支还没有提交的代码。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/1031bc77bea7e5a6c1e863a02ec2c2c5_MD5.jpg)

我之前有一期完整视频介绍关于 Git 和 GitHub 的使用，对 Git 不熟悉的观众朋友们可以去看一下那期视频。

在右边一个按钮是内置浏览器，Claude 可以使用内置浏览器对网页进行调试。内置浏览器里面有一个很好用的功能，叫做元素选择器：我们点击这个选择器，然后选择页面里面的任意一个元素，接着它就可以把这个元素的信息贴到对话框里面。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/23e59035d9f56c7a67c98492d0c534b2_MD5.jpg)

比如我说“把按钮调大一点”，这里就不用再指明是哪个按钮，使得我们跟 AI 沟通更加的高效。过了一会，它帮我把按钮调大了。

侧边栏下一个功能是文件列表，点击一下就展示了当前工作目录里面所有的文件。

## 回滚改动：Rewind

接下来我们介绍几个对对话还有代码进行管理的进阶技巧。我们先介绍第一个实用技巧，也就是如果对某个改动后悔了，怎么进行回滚。

比如我对刚才修改预约模块位置的那个改动后悔了，我想把这个改动回滚掉，并且把这次对话记录也删掉，最好当做无事发生。我可以找到这次不想要的对话，然后点击 Revert 按钮，这里会弹出三个选项给我们选：一，回退代码跟对话历史；二，只回退对话历史；三，只回退代码。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/9100b50e4a5cc45fc53c2ebb7a7cd312_MD5.jpg)

这里我选择一，全部回退，这样我们就在代码跟对话历史两个层面进行了回退。

Rewind 是通过 Claude Code 底层的文件快照机制实现的，它并不依赖 Git，非常的方便。不过 Rewind 也有局限性，就是它只能回退由 Claude Code 直接修改的文件，而不能回退通过运行命令等其他渠道产生的文件。

Rewind 还有一种快捷触发方式，就是连按两下 Esc，然后就会展示这个对话里面所有的对话历史。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/05c613027048f1c77e49a794ba6443d2_MD5.jpg)

比如这里我选择第二条，然后选择回退代码跟对话，这样就把这条对话历史还有以后的所有历史全部进行了回滚。

## Fork 与 Git Worktree：并行开发

我们再来介绍一个进阶技巧：Fork。Fork 的意思是会话分叉。比如我来到修改预约模块之前的这条记录，然后点击 Fork，这样就把会话进行了分叉。从分叉点以后的对话历史都留在原来的 Session 里面，Fork 出来的新 Session 只有分叉点以前的对话历史。使用 Fork 功能可以让我们基于不同的对话历史进行探索，或者进行并行开发。

但这里有一点要注意，Fork 只能 Fork 对话历史，是不会同步 Fork 代码的。也就是说，我们使用了 Fork 功能以后，代码还停留在原来的状态。如果想把代码也进行分叉，或者想在多个 Session 里面使用不同的版本代码进行并行开发，那就可以借助 Git Worktree。

Worktree 这个名字听起来比较唬人，其实它本质上就是用 Git 创建一个新的分支，然后把这个分支的代码完整地复制到一个新的文件夹里面，这个新文件夹就是一个 Worktree。主文件夹和分支文件夹可以并行工作，我们可以在两个文件夹里面各自修改代码，互相不干扰。然后我们还可以基于主干创建多个分支，它们在底层通过 Git 关联在一起，分支文件夹的改动随时都能轻松合并回主干。

接下来我们就把 Fork 跟 Worktree 配合起来使用。这里我在 Fork 出来的新分支上面，让它基于当前对话节点的代码状态创建一个 Worktree。这样 Claude Code 就为我们创建好了 Worktree，它把项目代码完整复制了一份到另外一个文件夹里面，然后我们就可以在这个文件夹上面进行工作，从而不影响主干。在右上角的状态面板里面也显示了当前的状态处于 Worktree 下面，还显示了当前分支的名字。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e001db25df289fa788753e0f822b9920_MD5.jpg)

我们在右侧面板可以看到，现在我这份代码是不包含那个预约模块的改动的，那个改动目前还留在主干，并不在这个 Worktree 里面。

然后我可以让 Claude Code 基于这个 Worktree 开发一个功能。我告诉它：这是我们店的地图，我需要你通过绘图能力把这个地图转换成一个 Q 版的卡通地图，然后附在网站里面。过了一会，Claude Code 为我们完成了开发。现在我们在主干还有 Worktree 上面并行开发了两个功能：主干上面改动了预约模块，然后 Worktree 上面添加了地图。

我告诉它把这个 Worktree 上面的改动合并回主干，并且删除掉当前 Worktree，这样就合并完成了。接下来我们就可以把这个 Fork 对话删除了，这样两个改动就都合并进了主干。在网页上可以看到，在线预约这个模块已经挪到了一个显眼的位置，然后地图也放到了整个网页的最下面。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/1337cdb65afcf95d34f99b26a3114b42_MD5.jpg)

我们就通过 Fork 加 Worktree 完成了一次并行开发。

## 新建会话时直接使用 Worktree，以及 /btw 侧边对话

Worktree 还有另外一种典型用法。比如我们还是在刚才项目的环境上面点击加号，创建一个新的 Session，然后在开始对话之前，直接先勾选上 Worktree。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/c7d1f999c4543cb2bea05335576584bf_MD5.jpg)

这样 Claude 工作的时候，它就会先创建一个 Worktree，在 Worktree 上面的改动不会影响主干。比如这里我想进行一个改动，把服务项目里面的这些价格数据全部写入到数据库里面。这里我就跟 Claude 说：把服务项目的价格数据写入数据库，UI 上是从数据库里面获取数据并且显示。

在开发过程中，如果我们想中途询问 AI 某些技术细节，或者处理一些临时的小任务，而不想打断主线工作，我们就可以开启临时对话。这里输入命令 `/btw` ，也就是 by the way 的缩写。比如我询问 AI 它是用什么框架来操作数据库的，这里 AI 在右侧开启了一个 Side Chat 侧边对话，回答了我的问题。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/35c8a17f66f529ee2ab74f64f9f8f1b3_MD5.jpg)

我们也可以点击这个加号，开启多个侧边对话。侧边对话可以看到主线对话的内容，但是它不会污染主线对话，也不会中断主线对话。还有一种方式是点击右上角的三个点，然后选择开启 Side Chat，或者按快捷键 `Ctrl + ;`，都可以快速开启这个面板。

功能开发完毕以后，我们看到现在的改动还在 Worktree 上面，还没有合并回主干。这里我让 Claude 帮我把改动合并回主干，这样 Claude 帮我把 Worktree 合并进了主干。

## Split View 分屏

在新版的 Claude 中，我们可以在左侧的对话列表里面找到一条对话记录，然后把它拖拽到主窗口里面，形成这样左右并列的两个窗口。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/883a8cde0c8a27bb2bc5c66f264926e5_MD5.jpg)

这个功能叫做 Split View，也就是分裂视图。除了左右分裂，我们还可以通过拖拽形成上下分裂的两个视图；我们也可以这样拖拽，形成上下左右这么 4 个视图，或者 3 个纵向视图并列。

## Nested Session 嵌套会话

接下来我们看一个重要的会话管理机制，这也是 Claude 桌面端最近更新的功能，叫做 Nested Session，也就是嵌套会话。这里我输入提示词：使用嵌套会话查询一下美国人口最多的 5 个州的天气。我们看到，在这个主 Session 下面，它又开启了 5 个子 Session 来并行查询天气。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/4792706cff3cec94d5f53901d1bf6517_MD5.jpg)

它非常像 Claude Code 里面的 Sub Agent，也就是子代理的功能：由一个主代理把任务委托给几个子代理并行完成，然后每个子代理都有自己的任务，最后它把结果汇总到主代理里面，这个任务就完成了。嵌套会话最大的好处，就是在这个会话列表里面，每个子会话都做了什么事情，看得一目了然，这个功能以后会逐渐取代 Sub Agent。我们也可以选择一个子 Session，点击 Detach to top level，把这个子 Session 上提一级，变成跟主 Session 平级并列的关系。

## 记忆系统：Code 模式的 CLAUDE.md

本章节我们来介绍 Claude 桌面端的记忆系统。Claude 桌面端记忆系统有两种：Chat 模式跟 Cowork 模式共用一套记忆系统，然后 Code 模式是单独的另外一套记忆系统。这两套记忆系统是泾渭分明、完全独立的，这里不要搞混。

我们先来看 Code 模式的记忆系统。Code 模式也就是 Claude Code 的记忆系统，它依赖一个核心文件 `              CLAUDE.md            ` 。比如我这个宠物洗护的应用，里面代码已经很多了，AI 如果每次着手修改代码，它都必须要读一下所有的代码文件，然后才能搞清楚这个应用是做什么用的，这样会比较浪费时间、浪费 Token。所以我们可以让 Claude 给我们生成一份项目记忆。

这里我们进入 Claude 桌面端，然后输入这个命令 `/init` ，也就是初始化的意思。这个命令可以让 Claude 通读一下整个文件夹，然后把它学到的内容输出到一个 `              CLAUDE.md            ` 文件里面，这个文件就是它对于这个项目的记忆。以后在每个新 Session 里面，Claude 着手工作之前，它都会先读一下这个记忆文件，快速掌握对这个项目的基础知识。我们看到过了一会，这个 `              CLAUDE.md            ` 文件就编写好了。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/3574203962c320458de6ebedd611e9c4_MD5.jpg)

这个文件浓缩了 AI 对于这个项目的全部记忆。

当然我们也可以手动修改这个文件，比如你可以加上一些代码规范或者测试规范等等，后续 AI 处理项目的时候都会遵循这个文件里面的规范。 `              CLAUDE.md            ` 文件不应该太长，最好保持 200 行以内。如果这个文件太长了，我们可以按模块把它切分一下。比如我这个项目是分为前端、后端的，我让它把 `              CLAUDE.md            ` 文件再切分一下，分成前端和后端两部分，然后把这两部分放到对应的文件夹里面，最后在主文件里面留下这两部分的指针。好，它帮我把这个文件拆成了三部分：前端、后端，还有主文件。在主文件里面，它保留了前端还有后端文件的指针，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/881c9faf0c958424e1d6aa34f31cd7a1_MD5.jpg)

如果 AI 需要相关的知识，它可以进入前端或者后端目录去读取相应的知识。

这个文件的名字可以叫做 `              CLAUDE.md            ` ，我们也可以写作 `              AGENTS.md            ` 。一般情况我更推荐把它写成 `              AGENTS.md            ` ，因为这个文件是所有 Agent 通用的，比如我们换到 Codex 或者 WorkBuddy 里面，它都可以读这个 `              AGENTS.md            ` ，学到相关的知识；而这个 `              CLAUDE.md            ` 文件往往是 Claude 自己用的。

## 全局记忆与隐藏的项目记忆

除了设置项目级别的记忆文件，Claude Code 也支持全局的记忆文件，对所有的项目都生效。这里我们来到 C 盘、用户、你的用户名，然后 `.claude` 这个文件夹，苹果电脑的话就是屏幕上这个地址。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/53f918933b75d3af961e9f4683e6ef4c_MD5.jpg)

然后我们在这个文件夹里面，可以直接新建一个 `              CLAUDE.md            ` 文件，这个文件就是全局的记忆文件，对所有的项目都生效。比如这里我说：我对后端技术比较精通，但对前端技术比较欠缺，所以沟通前端技术的时候，最好给我讲得详细一点。

我们新开一个 Session 试一下。我问 Claude 我的职业是什么，它可以读到全局的记忆文件，找到我的职业，还有我的特点。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/fcddada2b5a9d8f4e65644b99bf4a2ae_MD5.jpg)

这里我们要注意，这个 `              CLAUDE.md            ` 文件只对 Code 模式，也就是 Claude Code 生效。当我们切换到 Chat 模式或者 Cowork 模式，我再问它，它就不知道了。所以我说它们两个记忆系统是完全分离的。

除了项目里面的 `              CLAUDE.md            ` ，Claude Code 还有另外一套隐藏的记忆系统。这里我们可以直接问它，我问它：除了 `              CLAUDE.md            ` ，你是不是还有另外一个记忆系统？这里 Claude 给了我回答：除了 `              CLAUDE.md            ` ，它还有一套按项目隔离的记忆，是存在这个目录下面，每条记忆都是一个单独的 Markdown 文件。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/f11c4b3cf8762e71fbc90259a198c69e_MD5.jpg)

不过根据我的经验，Claude 的这第二套记忆系统，在大部分情况下 Claude 都不会主动去写，一般我也不会用它第二套记忆，大部分情况下我都写这个 `              CLAUDE.md            ` 文件就足够了。这样我们就讲完了 Code 模式的记忆系统。

## Chat 与 Cowork 模式的记忆

接下来我们看左边这个 Chat 跟 Cowork 模式的记忆系统。接下来我们看怎么给 Chat 或者 Cowork 模式增加记忆能力，这里也很简单，我们直接来到设置，然后找到 Your Claude，我们可以把全局的记忆填在这里，比如还是那句话，这样保存一下。然后我再问它一下，这次它就答上来了。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/3d1d6a2d2f700f069e674580c3a29818_MD5.jpg)

所以 Chat 跟 Cowork 模式，它依赖的是 Your Claude 这里面填的记忆，然后 Code 模式主要依赖 `              CLAUDE.md            ` 这个文件，它们两个是完全不同的。

Chat 模式里面还有关于记忆的更多设置。我们看到这里 Memory，这里有一个开关，允许 Claude 去搜索过去的对话历史，可以按需开启；还有一个开关，允许 Claude 从你过去的对话里面总结记忆，这个也可以按需开启。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/377efbfb3e29784e17f9baa8115f1a1c_MD5.jpg)

不过我们要注意，这两个开关只对 Chat 或者 Cowork 模式生效，它对 Code 模式是不起作用的。

## 浏览器自动化：操作 Chrome

Claude 可以自动操作浏览器进行工作，它有两种浏览器自动化的方案，分别是 Chrome 浏览器还有内置浏览器。

我们先看 Chrome 浏览器。打开 Chrome 浏览器，右上角三个点，找到 Extensions，也就是插件，点击 Manage extensions，点击这个“发现插件”按钮，然后搜索 Claude，把 Claude 插件安装一下。然后我们回到 Claude 桌面端，点击左下角的头像，点击设置，选择 Claude in Chrome，然后把这个开关开启起来。

这里我插一句，可能因为 Claude 版本不同，它的设置位置也不一样，有的版本它是在 Capabilities 里面，在这里 Claude in Chrome。如果找不到具体设置在哪里，还可以在 Search 这里搜索，这样一样可以搜索到开关。这样基本配置就完成了。

下面还有一个进阶配置，分别是白名单模式还有黑名单模式。选择这个 Allow all sites，就是允许 Claude 访问所有的网站，下面有一个 Blocked sites，在这里面可以添加禁止 Claude 访问的网站，比如这里我可以填一个百度，这个就是黑名单模式。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/9acc39642737c5baf57aeed09f8656bc_MD5.jpg)

还有另外一种白名单模式，我们选择 Block all sites，就是禁止访问所有的网站，然后在下面可以配置白名单，这样只允许 Claude 访问白名单里面的网站。

配置完成以后，我们来测试一下。这里我让它使用 Chrome 浏览器打开谷歌，然后查询一下芝加哥的天气。这样 Claude 成功操作我的 Chrome，打开了谷歌，然后搜索到了芝加哥的天气。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/5ba9b182626c4b4cfe57a6868bb18f64_MD5.jpg)

我们注意到在右上角，我的谷歌是登录过的。比起内置浏览器方案，操作 Chrome 最大的好处是自带登录状态，各种网站都不需要再重复登录。

## 浏览器自动化：内置浏览器

接下来我们看第二个方案，就是内置浏览器。我给 Claude 说：使用内置浏览器也搜索一下芝加哥的天气。我们看到它一样可以搜索到天气，点击这个内置浏览器的小按钮，就打开了它的内置浏览器，看到它已经打开了搜索天气的这个页面。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/d4be03baf31d060fb1b1547e424406e8_MD5.jpg)

接着我让 Claude 使用内置浏览器测试一下刚才宠物预约洗护的项目，过了一会它完成了测试，发现了两个小问题。Claude 使用内置浏览器比使用 Chrome 更加顺手，它可以更方便地查看网络请求、查看控制台输出，所以我们开发网页应用的时候，尽量让它使用内置浏览器进行测试。

Claude 内置浏览器也是可以保留登录状态的，不过这里要做一些设置。我们点击 Browser，打开内置浏览器，然后点击这三个点，找到这个 Cookie。它默认的设置是 Until quit，就是我们关闭 Claude 桌面端的时候，它就会把 Cookie 清除，把登录状态清除。如果想让登录状态长期保存，我们可以选择中间这个 Shared，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/4a8b79047c42e117f81e50e0a7091f93_MD5.jpg)

这样我们登录的网站就可以长期保存 Cookie 了。第三个是 Per session，就是每个 Session 都保留一套 Cookie，这个做一些特殊测试的时候可能会用到。

## Computer Use：电脑自动化

除了我们刚才介绍的浏览器自动化，Claude 还有另外一种自动化方案，叫做 Computer Use，也就是电脑自动化。这里我们还是来到设置，在 Capabilities 里面找到这个 Computer Use，然后这里有个开关 Enable computer use，把它开启起来。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/35a04bece69601f80e364f82c64f6aaa_MD5.jpg)

这样它就可以控制我电脑的鼠标键盘来操作一些软件。下面 Denied apps 可以选择禁止 Claude 使用哪个软件。

我们看到在官方文档里面也说了，Computer Use 虽然适用范围最广，但是速度最慢，而且特别的费 Token。所以 Claude 推荐的操作电脑的方式的优先级是这么几个：如果有连接器，它会优先使用连接器，也就是说在 Customize → Connectors 里面这里配置的连接器，它会优先使用连接器；如果没有连接器，它会使用 Bash 命令；浏览器操作，它会用 Chrome 浏览器；最后都不得已，它才会使用 Computer Use。

好，我们来测试一下。我让 Claude 打开 VS Code，然后安装这个插件，再用插件统计一下本项目有多少代码。Claude 操作电脑打开了 VS Code，然后搜索并且安装了这个插件，最后把代码的行数统计出来了。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/89e11a953f92442c630fa07b3f0059d8_MD5.jpg)

## Claude Design 与 Design System

Claude Design 是一款 AI 可视化设计工具，它原本是个独立应用，现在已经被整合进了 Claude 桌面端。我们可以用自然语言，在 Claude Design 里面生成 UI 界面、交互原型、信息图、海报等设计作品，并且它支持在画布上直接编辑元素。

Claude Design 最大的特色，就是可以把一套设计语言固化成 Design System。Design System 里面包含配色、字体、图片等等各种设计规范，然后我们就可以很轻松地使用这套设计规范，设计出统一风格的 UI 界面、演示文稿等等。

Claude Design 的设计过程一般有三个阶段。我们首先准备一个 `              DESIGN.md            ` 文件，这个文件就像一个文字版的规则手册， `              DESIGN.md            ` 是 AI 设计界的一个通用规则。然后 Claude Design 可以把它转换成 Design System，也就是一个 Claude 里面专用的设计系统，这个过程就像把抽象的设计语言，转变成一个个可以看到的界面元素。最后，Claude Design 可以把 Design System 里面的元素拼装成我们需要的设计成品。

首先第一步，我们准备 `              DESIGN.md            ` 文件。当然这个文件一般我们也不需要自己写，在 GitHub 上面有一个开源项目叫做 Awesome Claude Design，里面列出了各大厂商的 UI 设计风格，还有统一的设计语言，比如这里有 Claude、Cohere、ElevenLabs 等等，下面还有 Cursor，包括苹果、IBM、英伟达等等。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/b48852d45a5b525682924d7095e2e1af_MD5.jpg)

这些文件记录了这些厂商产品的统一设计语言。这里我们就以这个 Claude 为例，我们点击进去，点击这个按钮 Download [DESIGN.md，这样我们就把这个文字版的设计规范下载下来了。不过这个是纯文字版的，看起来比较抽象。](http://design.xn--md,-128da8pwymzr13fi3bw40atkbgyukxgzldjt5dsbph76cu20at1hnrao37d91bfa.xn--,-qo6apd555dvwil9du7a78d4vp6hqy4klrbm04cx07bbodvtkx6ajj./)

接下来我们就把这个文件转换成一个 Claude 里面的 Design System。我们来到 Claude 桌面端，然后点击这个 Artifacts。现在 Claude Design 已经集成进了 Claude 桌面端，我们直接点击这个 Design，然后在对话框这里选择 Make new design system，把刚才下载的 `              DESIGN.md            ` 文件拖拽进来，然后说：基于这个文件创建一个 Design System。

这个就是 Claude 官网的设计语言，我们看到它已经把配色、字体、控件，然后各种样式等等，都固化成了一个个元素。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/567d1c2c895c2ba990326071520f4ab2_MD5.jpg)

如果对哪块样式不满意，我们可以点击右上角的 Comment 按钮，比如我希望它把标题加大加粗，然后我就说“把这一块的标题加大加粗”，过了一会，Claude 为我们完成了修改。

## 实战：用 Design System 制作网页版 PPT

接下来我们看一个实战案例。这里我找到 Anthropic 的一篇研究文章《Agent 记忆的组成部分》，这是一篇发表在 Anthropic 官网上的研究文章。接下来我们就用 Claude Design 把这篇文章转换成一个可以演示交互的 HTML 网页版 PPT，然后要保留 Anthropic 官网的这种设计语言跟设计风格。

这里我直接把文章链接复制一下，然后在 Artifacts 里面找到我们刚才创建的那个 Design System，点击右上角的 Chat，把文章贴进去。我让 Claude 把这篇文章转换成一个 HTML 的互动演示 PPT，配图可以从原文下载，或者使用生图工具生成。

我们来看一下最终效果。这个 PPT 基本上完美继承了 Anthropic 官网的设计风格，包括字体、图标、元素等等。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e92bc307f6fbfe7ef136789714c5d401_MD5.jpg)

这个就是 Claude Design 的意义所在：我们使用一套设计规范，就可以批量制作风格相同的公司资产，非常的方便。

## Artifacts：Docs 云文档

除了我们刚才介绍的 Design，接下来我们介绍 Artifacts 里面其他几个功能，这里有 Docs、Slides 还有 Dashboard。

我们先看 Docs。Docs 功能简单来说，就是一个类似飞书云文档的功能，我们可以使用 Claude 创建一个云文档，然后可以由人跟 AI 共同编辑，还可以把这个文档发给同事进行协作，或者导出成 Word 或者 PDF 格式。

我们来试一下。这里选择 Docs，然后我输入这个提示词：帮我写一份宠物店一周年活动庆典方案的文档，然后需要包含表格、日期清单、图表、流程图这种。Docs 的功能非常的灵活，它可以往里面插入各种各样丰富的元素控件。我们看到，Claude 写文档跟人写文档的步骤基本上是一样的，它先列提纲，然后在里面再填充细节，然后我们还可以看到它一步步写的全过程，非常的有意思。

我们看到文档的功能非常丰富，它可以添加这种日期表格、甘特图，还有这种任务看板、图表、折线图、流程图、四象限推理图、插入图片，还有这种待办事项勾选等等，是一个功能非常全面的云文档。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/a4ec7c126e0488c13d9616e76b273691_MD5.jpg)

然后我们可以点击右上角的 Share 按钮，输入一个邮箱，就可以把文档分享给其他人，还可以点击这个 Export，导出成 Word 或者 PDF 等等格式。

## Artifacts：Slides 演示文稿

Artifacts 里面另一个模块叫做 Slides，其实就是 PPT。

这里我就用刚才设计的那个 Claude 官网的 Design System。这里我还是找到一篇 Anthropic 官网上的文章，我把它复制一下，我让 Claude 还是把这个文章提炼成可以演讲的 PPT，我需要能导出成 PPTX 文件，图片可以用生图功能或者从原文下载。

然后 Claude 在右侧打开了一个画板，开始一步步地生成这个 PPT，它的生成过程我们都可以看到。Claude 为我们完成了 PPT 的编写，这里面每个元素都是可以直接修改的，在这里面可以修改字体。然后我们可以点击右上角的 Share，找到这个 Export，把它导出成一个真正的 PPT 文件，选择 PowerPoint。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/544988056faa302e9132bb63257f80f6_MD5.jpg)

这样我们使用 PPT 软件也可以打开并且编辑这个 PPT 了。

## Artifacts：Dashboard 数据看板

接下来我们看 Artifacts 里面最后一个功能，叫做 Dashboard。通过 Dashboard 可以生成图表、数据看板等等，而且它生成出来的报表数据是活的，如果你能提供给它一个实时的数据源的话，它可以随时更新数据。

我们来试一下。这里选择 Dashboard，然后我告诉 Claude：这是我的 YouTube API key，以下是我关注的 YouTube 频道，你把这些频道近期的数据做一个数据看板出来。好，我们的数据看板就生成好了，在这里面包含热力图、柱状图，还有表格等等，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/1eccaa08c8abd8b19d0a2a74b9d8bca4_MD5.jpg)

拉取了近 90 天所有视频的数据。

然后像这种数据它是活的，我们可以让它设置一个定时任务，每天自动重新抓取数据。这里我们点“好，每天刷新”，定时任务创建好了。我们在这个 Routines 里面，就可以看到 Claude 为我们创建的定时任务。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/0b78ed0be51c982ead748e25b0d85b9e_MD5.jpg)

点进去以后可以查看它的详情，还可以点击右上角的 Run now，来手动测试一遍这个定时任务。下次我们想看看板的时候，还是点击这个 Artifacts，然后找到这个 YouTube 看板，点击进去就可以查看到看板数据，而且它是每天更新的，非常的有意思。

## Skills：给 Claude 扩展能力

Claude 桌面端本身的功能已经很强大了，接下来我们看怎么给它扩展功能，其中最重要的就是 Skills。Skill 是给 AI Agent 的一个专业技能包，或者说是一种带目录的说明书。我们可以把工作流、专业能力或者某些规范封装成一个个 Skill，交给 AI Agent，让 Agent 在执行特定任务的时候更稳定、更高效，输出也更可靠。在之前的这期视频里面，我介绍了 Skill 的概念与技术原理，本章节我们主要介绍两种给 Claude 安装 Skill 的方法，分别是我们从网上下载 Skill，还有自己编写 Skill。

## 安装网上下载的 Skill

Claude Opus 5.5 模型最出圈的能力，就是生成这种知识讲解视频，叫做“Vibe 知识大赏”。现在我们使用 Claude 桌面端复刻一个这种视频是非常容易的，在 GitHub 上面也有很多这种 Skill 可以帮我们来复刻这种视频，比如这个 vibe-knowledge-film。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/21b4d861d89f3797df2974622b27e21b_MD5.jpg)

我们要做的第一步，就是先把这个 Skill 下载一下，这里在 Code 里面点击 Download ZIP。然后我创建了一个全新的文件夹作为项目文件夹，这里我在 Claude 里面创建一个新的环境，把我们的文件夹添加进来。然后我们在项目文件夹里面创建一个 `.claude` 的子文件夹。注意，这个 Claude Code 只认这种子文件夹，在其他的 Agent 工具里面可以写 `.agents` ，但是在 Claude 里面只能写 `.claude` 。然后进入这个文件夹，我们再创建一个 `skills` 文件夹，再进入 `skills` 里面。找到我们刚才下载的那个项目，找到这个 `              SKILL.md            ` 文件，把这个文件上一级的文件夹复制一下，然后粘贴进 `skills` 目录里面，这样就配置完成了。

我们新开一个对话，选到我们刚才创建的环境，然后输入这个命令 `/reload-skills` ，重新加载一下 Skill，然后我们再输入这个命令 `/` ，就可以找到这个 Vibe 知识大赏的 Skill。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/0905a9da2f8c735b9acd18c1c6de9a43_MD5.jpg)

然后你给它一段文案，它就能输出对应的视频了。比如我给它粘上这么一段文案，然后让 Claude 给我做视频，过了一会，Claude 完成了这个视频，我们来看一下。

现在我们这个 Skill 是放到这个项目目录里面的，它只对当前这个项目生效。我们也可以把它放到全局目录里面，对所有的项目生效。如果想对所有项目生效，我们可以来到 C 盘、用户、你的用户名，然后 `.claude` 这个文件夹，苹果电脑的话就是屏幕上这个文件夹。在这里面我们也新建一个 `skills` 目录，然后我们把项目里面包含了 Skill 的文件夹复制到全局的 `skills` 目录，这样这个 Skill 就可以在所有的项目里面被找到了。比如我来到宠物店的那个项目，直接 `/reload-skills` ，让它重新加载一下电脑的 Skill，然后输入 `/` 就可以找到这个 Skill。

## 从 0 开始编写一个 Skill

除了使用别人已经编写好的 Skill，接下来我们看怎么从 0 开始编写一个 Skill。这里我又创建了一个项目文件夹，然后新建了一个环境。爬爬虾作为一个视频博主，有一个需求，就是经常要把自己做好的视频配上字幕。然后我需要给它一段没有字幕的视频，它能自动识别里面的语音，然后自动生成 SRT 格式的字幕文件。

我们直接在对话框输入 `/` ，找到这个技能 `anthropic-skills:skill-creator` ，这是一个用来创建技能的技能，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/1a0d71cf90d9ed2643cda20aee5cb827_MD5.jpg)

然后描述我们的需求。

让 AI 来创建 Skill 非常容易，我们只需要给它足够的工具，比如这里我给它相应的语音识别模型，还有对应的 API key，然后我们还有验收标准，这里我给它一个真实的视频文件，让它用来测试并且验收。过了一会，Claude 为我们编写好了 Skill，它放到了这个 `video-to-srt` 文件夹里面，这里面有 `              SKILL.md            ` 文件。然后我们把这个文件夹复制一下，可以粘贴到用户全局的这个 `skills` 里面，这样就可以在所有项目里面生效。

这里我新开一个 Session， `/reload-skills` ，然后输入 `/` ，就可以找到我们新创建出来的 Skill。有了这个 Skill 以后，我再随便扔给它一个视频，它就能帮我输出 SRT 文件了。

## 连接器：接入 Supabase 与 Vercel

给 Claude 扩充能力的另外一个重要方式是连接器。我们在菜单 Customize 里面的 Connectors，就可以找到连接器，我们可以通过连接器把 Claude 的能力接入这些在线服务。当然这些服务还是以海外的居多，我们看到用得比较多的就是谷歌几件套：Google Drive、Gmail 还有谷歌日历等等。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/a4d974219780551cdc82f9ce63e435cf_MD5.jpg)

这里我们找几个比较有用的来举个例子。首先第一个 Supabase，爬爬虾之前有一期完整视频介绍关于 Supabase 的使用。Supabase 简单来说就是一个云端的、零成本的 Postgres 数据库。现在我们宠物店应用使用的是本地数据库，我们把宠物洗护的应用接入 Supabase 以后，它就拥有了云端数据库，就不再使用本地数据库了。这里我点击加号，点击 Continue，然后登录一下 Supabase 的账号，然后点击 Authorize Claude，再点击 Open，这里把权限改成 Always allow，这样我们就配置好了 Supabase 的连接器。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/c4ac173936843cc05ad37f8ba4dd0319_MD5.jpg)

接下来我们再配置一个连接器：Vercel。Vercel 是一个云服务厂商，借助它，我们可以把使用 [Node.js](http://node.js/) 编写的项目直接零成本部署到云端。这里还是点击 Connect to Claude，还是登录一下 Vercel 账号，然后点击 Allow access。

这里我再回到我的宠物洗护应用，输入我的需求：使用 Supabase 连接器把项目改造成云数据库，然后再使用 Vercel 把项目部署上线。开始，Claude 完成了任务，然后把项目部署到云端。我们访问这个地址，就可以看到我们的网站，然后数据库是存在 Supabase 的云端数据库里面，在这里面可以看到预约表，还有服务表里面的数据。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/bf83e33009ea4f7d13497517ec908729_MD5.jpg)

这样我们就通过连接器，把一个本地项目部署到云端，并且发布上线了。

## Claude Code Project：AI 主导的并行工作流

接下来我们介绍 Claude Code 里面一个全新的功能：Project。我们先来区分一个概念，就是在 Cowork 和 Code 两个模式中，Project 完全不是一个东西。在 Cowork 中，一个 Project 就是一个工作区，我们可以在 Cowork 里面通过 Project 把一个或者多个文件夹组织起来，变成一个工作区，或者说一个项目来集中处理。而在 Claude Code 中，Project 是一套由 AI 主导的全新工作流的编排方式，这是上个月刚刚上线的一个全新功能。所以本章节我们主要来看 Claude Code 里面的 Project。

我们来到 Claude Code，然后找到 Project，点击 New project。这里先给项目起个名字，这里我叫“性能优化”，然后给项目填一个目标：我的目标是尽量优化性能，优化导出速度，还有 UI 性能等等。接下来我们可以选择文件夹或者文件。

这里有一点要注意，Project 主要是通过启动云端开发环境，在云端完成任务，所以最理想的工作状态，是我们给它一个 GitHub 上面的远端仓库，然后让它基于 GitHub 仓库来完成任务，而不是基于我们的本地文件夹。虽然 Project 也能操作本地电脑，但那不是最佳实践，如果一个任务的大量工作都需要在本地完成，那就不适合用 Project 来做。

所以这里我不给它添加本地文件夹，而是通过下面的 Connect GitHub 来给它添加远端项目。这里我先登录一下自己的 GitHub 账户，点击这个 review request，然后点击接受，好，这样就配置完成了，再点击授权。接下来我们就可以选择 GitHub 上面的远端仓库，比如这里我选择这个仓库，点击 Create project。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/18b568ccdf8c1f004eda5ac9249bbcf1_MD5.jpg)

当我们把 Project 创建完成以后，它就会自动对目标进行分析。我们看到 Claude Code 帮我们创建了一个 Thread，在右边的面板显示，也就是一个线程，来帮我们分析代码，找出性能瓶颈。我们可以点击这个线程的小按钮，然后看到它的工作状态，我们也可以在这个 Thread 里面输入自己的意见，来引导这个线程工作。比如我让它重点分析拖拽遮罩时候的卡顿是什么原因。我们看到，这个调查性能瓶颈的线程输出了一份完整的性能报告，

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/e74a30de459aa1b85cf3428d4ca756c2_MD5.jpg)

然后交还给左侧的协调员，协调员设计了三个线程来优化性能问题。

这就是 Claude Code Project 最大的价值所在：我们不再需要手动管理 Session，只需要给出任务，Claude 协调员就能根据任务自动拆解出 Thread，并且可以并行工作。这里它拆解出了 3 个 Thread，然后我们点击 Start，这样三个线程就开始了并行工作。我们在右侧的线程面板可以看到 Working 3，也就是三个线程正在并行工作。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/4275dcdfdc35b3296a772042bb600ab6_MD5.jpg)

过了一会，三个并行工作的 Thread 就完成了。我们看到这里它们三个都举着手，也就是等待我提示下一步的操作。这里它问我是否要把改动推送并且提交 PR，这里我选择推送并且开 PR，这三个我都选推送并且开 PR。我们看到，Claude 基于这个性能优化的任务进行了三处修改，它是通过 3 个线程并行完成的，然后提交了 3 个 PR，等待我们审批。

![图片](assets/Claude(Code)%E6%A1%8C%E9%9D%A2APP%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%E4%B8%80%E6%9C%9F%E8%A7%86%E9%A2%91%E7%B2%BE%E9%80%9A/4db10810f97d77f7b84ffcb78ad4e58c_MD5.jpg)

我们可以点击一个 PR，然后查看 AI 修改的代码，如果认为代码没问题，直接点击这个 Merge 按钮把代码合并，这样开发工作就完成了。这里我先把前面两个 PR 合并了，然后第三个 PR 有冲突了，我让 Claude 帮我解决一下。我们看到，Claude 可以正确地把这个解决冲突的任务，分配给之前的一个工作线程来继续工作，因为之前的这个线程它更熟悉这块代码。这里 Claude 为我解决了冲突，我们再来看一下 PR，这次看起来正常，没问题了，我点击 Merge 按钮，这样三个 PR 都 Merge 了，整个开发工作就完成了。

这就是一个 Claude Code Project 工作流的典型用法，这是一个更智能的、AI 主导的多任务并行工作流的编排方案。

**微信扫一扫赞赏作者**