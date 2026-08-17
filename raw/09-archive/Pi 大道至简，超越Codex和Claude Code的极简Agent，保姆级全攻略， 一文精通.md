---
title: "Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通"
source: "https://mp.weixin.qq.com/s/RxcXqLM46U2QFafUl_N-xw"
---
技术爬爬虾 技术爬爬虾 *2026年8月16日 22:09*

Pi是最近热度超高的AI Agent，用四个字形容就是大道至简。Pi只有四个基础工具，系统提示词也仅仅只有1000 Token。在Pi里面说句你好，只有1100的上传Token，只占用0.4%的上下文。然而在Codex里面，仅仅打个招呼就占用18000的Token，什么事情都没做，白白消耗了7%的上下文窗口。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/95134bd96ad27b382032d1a4b49118ce_MD5.webp)

Pi极致的精简带来了极致的效率提升。根据Composio上个月的一组基准测试，Pi Agent完成编程任务的速度，比起其他的Coding Agent快了1.5到2倍，任务成本比起主流框架也低了不少。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/574c45a9f3b29c8cf449b18e5917e8b8_MD5.webp)

在编程质量方面，数据服务大厂Databricks，在自家一个百万行代码的仓库上面，运行了一个基准测试。这个图的横轴是任务成本，纵轴则是任务通过率，也就是代码质量。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/5fb0b2e8ac0841e853b7735e35bfcc2a_MD5.webp)

红色这条线则展示了同等成本下，任务成功率最高的Agent加模型的组合。我们看到，Pi在大部分场景下面的表现，都要好于Claude Code和Codex。而整张图代码质量的最高点，就是Pi加Claude [Opus4.8的组合。本期带来一个Pi](http://opus4.xn--8-858a727hn5g.xn--pi-uu2cmgw00f0jmucsw/) Agent的完整教程，主要分为以下11个章节，每个章节都会穿插一些重要的知识，对Pi的全部功能进行细致讲解。好废话不多说，我们直接开始。

## Pi的安装配置

我们先来把Pi装一下，我先介绍Windows操作系统，然后是Mac。这里我用了一台全新的Windows电脑来进行测试。装Pi并不需要任何的准备工作。在桌面点击右键，在终端打开，打开Windows PowerShell的控制台。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/fbfb0fdafabab0db37965a2bbb0f6421_MD5.jpg)

然后我们来到Pi的官网，找到这个Powershell的一键装命令，把它复制一下，粘贴到控制台里面回车。
```
powershell -c "irm 
            https://pi.dev/install.ps1
           | iex"
```
![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/04283b93f1c97f340f76e60a9bc20c8c_MD5.jpg)

Pi检测到这台电脑没有 [Node.js，这里我输入y回车，先装Node.js。到这一步还是输入y回车，装Pi的本体。Pi使用git](http://node.xn--js,y,node-z22o2jw39c2k8ami7ih1uaquae1bwzv.js.xn--y,pi-k84fi4e4zfmybf2uhs2byjco2sxh9aeo7ci1uquat0bpa.xn--pigit-4b3hr36t/) bash作为命令行运行环境，如果你的电脑上没有装过Git，它会先询问。这里建议选择输入w，让Pi先帮你把Git在Windows上面装好。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/57609831fa66684517642ceb8e155a08_MD5.jpg)

好到这一步，Pi装就结束了。我们需要先关闭掉当前的命令行窗口，然后右键重新打开一个终端输入pi，把Pi启动起来。如果能成功显示的对话窗口，我们的Pi就装完毕了。接下来我们看MacOS的装。这里还是先打开终端，然后去Pi官网。注意这里要复制这条curl的命令，粘贴进终端执行。
```
curl -fsSL 
            https://pi.dev/install.sh
           | sh
```

这样在Mac上面Pi也装好了。

## 配置模型

接下来我们给Pi配置模型。先把Pi启动起来，来到这个界面，然后输入命令/login。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/35929a7b6d93505cc6768a5df0e05177_MD5.jpg)

这有两种配置模型的方法，一个是API key，还有一个是用模型订阅。这里我先选择API key。Pi支持40多家模型供应商，基本上覆盖了市面上常见的所有模型选择。这里我以DeepSeek为例，我们可以先输入关键词筛选出DeepSeek，然后回车。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/988f04b779067ebd3cca71f3189869c7_MD5.jpg)

接下来我们来到DeepSeek的官网，点击API开放平台，首先确保你有些额度，然后点击API keys，点击创建API key，随便填个名字。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/35e9f901a11aa36a876942c6ec854d2d_MD5.jpg)

然后把新生成的API key复制一下，填写到Pi里面回车。打个招呼，这样给到了回复，我们的DeepSeek模型就配置完成了。现在我们使用的默认模型是DeepSeek V4 Pro，我们可以输入命令/model来切换模型。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/872c36856318abe5cfecbc0a895c4a81_MD5.jpg)

比如这里可以切换成DeepSeek V4 Flash。使用快捷键Shift+Tab（Mac同）来切换模型的思考强度，可以根据任务的复杂程度，来选择模型的思考强度。敲快捷键Control+L（Mac同）也可以快速打开这个模型选择器。接下来我们看使用模型订阅来给Pi Agent接入模型。还是先输入命令/login，我们选择上面这个sign in with account。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/51ac9a3ac74c4deed1267c272e8736ec_MD5.jpg)

然后这里我以我的OpenAI订阅为例，我选择OpenAI Codex，然后选择第一个用浏览器登录。接着浏览器里会打开一个登录窗口，这里登录一下我的OpenAI账户。登录完成以后，我们回到Pi，敲快捷键Control + L，模型列表里面就出现了ChatGPT的模型。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/a00e96b93378f04700ce67707f3e154d_MD5.jpg)

## 基础操作

这里我新建了一个文件夹作为项目文件夹，进来以后右键在终端打开，输入Pi启动起来。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/c503e5058072593391a7064e7e8e926c_MD5.jpg)

在Pi窗口里面就显示了当前的文件夹，也就是项目文件夹。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/74bdffb3c3429897581cb7cd9b7b5b1b_MD5.jpg)

我们后续下指令，它就会把代码写到这个项目文件夹里面。使用react框架做一个宠物洗护店的网页。如果我们的指令是多行的，想进行换行，这里不要按回车，按回车就直接发送出去了。我们可以敲Shift+回车（Mac同），这样新起一行，再输入第二行。还有一种方式是按快捷键Control + G (Mac同)打开一个记事本，我们可以在记事本里面更加方便的编辑提示词。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/f95ab61363b8c974eeae0362cf4dc07f_MD5.jpg)

编辑完成以后保存一下，叉掉记事本，提示词就会同步出现在窗口里面。让我输入了3行提示词，回车执行。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/d6482cdc111e6b583a2564ae3d6bc9d0_MD5.jpg)

Pi就完成了代码编写。我们先来看最下面这一行信息。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/d0f1d756eae9468ef7dbd381facb0c72_MD5.jpg)

这里上箭头表示整个Session的输入Token。Session就是一个连续的对话记录，记录了AI多轮对话的整个工作过程。我们可以在Pi里面敲/new新开一个Session。在新的Session里面，AI就没有过去的对话历史，上下文窗口也就清空了。下箭头输出Token，总共输出了11000的Token。大写的R是Cache Read，也就是整个Session里面有多少Token命中了缓存。CH是Cache Hit Rate，是最近一次的请求缓存命中率。注意这里的缓存命中率不是统计的整个Session的，而是统计的最近一次AI调用请求的缓存命中率。后面还有一个这次对话的预估成本，括号sub是subscription，也就是订阅的意思。也就是我现在使用的是chatgpt的订阅，所以前面的成本仅供参考。最后4.6%表示现在占用了模型4.6%的上下文窗口。然后/后面是模型总的上下文窗口， [GPT5.6总的上下文窗口是272k。auto是上下文压缩机制，auto表示自动压缩。也就是说当上下文使用量达到阈值的时候，Pi会自动触发一次上下文压缩。](http://gpt5.xn--6272k-5h1hha280jr60aryl3wbmx8grcl.xn--auto,auto-tb6nla819jrmbvzfha9674eslcpxgxr2i11yaka126mem0b.xn--,pi-s18dsbecf26et2dw5a24c8my9tvzb47f57ak91hnpmrh4ana54viubu24eis9cunhu14d0dqwt8cm4mlt2awvok16a./)![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/dd99b7bfe3064753ba4d354f997d1343_MD5.jpg)

最后面是模型的提供商，还有现在使用的模型的名字。点后面是当前模型的思考强度。代码编写好了以后，它提示我们可以用npm run dev来启动起来。这里最方便的方式是我们可以直接在当前窗口运行命令。我们敲一个英文的叹号，然后输入这个命令npm run dev回车。这样我们的开发服务器就启动起来了。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/7787df987fad3426791830575dad2429_MD5.jpg)

所以叹号的功能就是在当前的对话窗口临时运行一个命令。我们使用叹号运行命令，命令运行的结果还有过程AI是可以看到的。如果不想让AI看到我们运行的命令，这里可以敲两个叹号，然后再输入命令。

在这个方式下面输入的命令，AI是看不到的。我们可以打开这个链接查看AI给我们开发的网页。如果对哪一部分不满意，可以直接截图跟AI进行沟通。比如我不喜欢这边的布局，我直接截一个图，来到Pi。Windows电脑直接敲快捷键Alt+V，Mac电脑快捷键Control + V，把刚才截的图片粘贴过来。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/26416ab3c1eea66debed7ad5a9e9f579_MD5.jpg)

然后我告诉AI，浮动卡片的数量太少了。Pi读取了这张图片，过了一会完成了修改。这样卡片加多了两个。除了粘贴截图，我们还可以用另外一种方式跟AI进行交流。就是输入@，然后就可以选择某个代码文件。这里我选择src目录，然后输入/选择main文件。我告诉AI不要把代码都放到一个文件里面，把它拆分成模块开始。这样我们通过@文件的方式完成了这一轮的沟通，AI帮我们把代码拆分成了模块。

## 指令追加

接下来我让Pi把项目做成前后端的应用，我需要预约信息能存入数据库。我们看到这里AI想用express框架来做后端，但是我更想使用 [Next.js框架来做后端。遇到这种情况，在Pi里面我们不需要打断AI的执行，可以直接在对话里面给AI补充提示词。我在对话框里面输入，说我需要Next.js框架，然后数据库用SQLite。这里直接敲回车。我们看到我们新输入的这条指令前面写着Steering。](http://next.xn--js-ic4cm4liz5a4nap6a950i.xn--,piai,ai-f49ly3ecct41bjpbgxc3xm6moja803ti0u43fxnbwm17vw3am45asm4isqc22xb2dc43clh5dfxak60a2lu1pav79iildvxtta7734cyjdva.xn--,next-ep5h875a3ujdynea095o177ghogkjal39bduie5wisb.xn--js,sqlite-sv8ox93gfgm5kgzyiy8b9v8dy9n.xn--zbs301aslbgw9ad41autaf3i.xn--steering-mp1mrca017emta49dsmk66sca445bwrqqhi839fyocf9az899acpbd74h./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/41b66087a8318fc263b933e1bb8fd2ce_MD5.jpg)

Steering翻译过来就是控制，引导的意思，它英文原本意思是打方向盘。当我们发现AI在执行过程中理解错了我们的意思，这时候应该果断地通过Steering，也就是打方向盘，对AI的行为进行一定的引导干预。在Pi里面，当用户追加指令的时候，默认就是引导。我们看到，当这个Steering指令发出去以后，AI立即改变了它的执行方向，开始为我们装 [Next.js相关的依赖。除了默认的Steering引导，Pi](http://next.xn--js-bv3cq3eu17f3tav66j.xn--steering,pi-ix9qg41lgcj0s2ghw8cwgvb715a/) Agent还提供了另外一种指令追加的方式，叫做Follow-up。Follow-up的意思是排队。

Follow-up跟Steering最大的区别是，Follow-up不会影响AI当前这一轮的工作，而是等待AI完成这一轮的全部工作，AI才会看到并且执行用户接下来一轮的指令。在Windows系统里面，使用Follow-up需要修改一个配置。我们先右键打开PowerShell的设置，在操作里面找到这组快捷键Alt+回车，也就是让PowerShell全屏化的快捷键。先把这个快捷键删除，因为它跟Pi默认Follow-up的快捷键冲突了，

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/6c1e9a79d80d1aa3204241443f59602c_MD5.jpg)

然后点击右下角的保存。把它删除以后，我们回到Pi。接下来再输入一条指令，输入完成以后，我们不要使用回车，我们使用Alt + 回车。Mac电脑上面的快捷键是Option + 回车。我们看到这条指令前面写的是Follow-up，也就进入了排队。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/8602323767d040c2aadbeeb6482d187d_MD5.jpg)

Follow-up指令需要等待AI把这一轮的工作全部做完，才可以继续处理。当指令在排队的过程中，我们也可以输入快捷键Alt + 上箭头，把这条指令拿回来重新编辑。比如这里我进行了一点修改，修改完成以后再点击Alt+回车，把它送入队列进行排队。过了一会，AI把这一轮的工作全部做完了，然后AI才能看到并且执行我最新一条的指令，也就是增加一个后台面板可以查看用户的预约。在这个例子里面，我们就看到了Pi Agent最经典的两种指令追加的方式。一个是Steering，在执行的中途进行引导；还有一个是Follow-up，让指令在后面排队。这里简单补充下Pi的Follow-up跟Steering两种指令追加的实现原理。Pi的核心Agent Loop是一个双层循环机制。我们先看内层循环。Pi在内层循环里面调用大模型，然后根据模型的指令来调用工具，再把工具处理结果返回给模型，由模型判断是否完成了工作。如果没有完成工作，再进入下一轮的循环。这里有一个巧妙的设计，也就是当进入下一轮循环的时候，Pi会把Steering的消息注入上下文。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/7b72e8a82b2d6d7467bfd60b5a0a376e_MD5.jpg)

这样Pi就能对用户的指令进行实时的反应。而Follow-up的消息则处于外层循环，需要等待内层循环处理完毕。也就是Pi完成手头的工作以后，还会读取到Follow-up的消息。这时候Pi如果发现有Follow-up的消息，它会开启外层循环继续工作。除了我们输入Pi在常规模式下面运行，Pi还提供了一次性的非交互模式。这里我们可以在后面输入 -p，然后在引号里面填上我要它处理的指令。我让Pi查找下今天的天气，然后在桌面写一个天气.txt文件回车。这样Pi就会在后台静默执行这个需求，中间过程我们是看不到的。等他执行完毕以后，他就会把结果输出出来，天气文件也在桌面上写好了。这种非交互模式特别适合把Pi当做一次性的CLI命令来使用。

## 会话管理与对话树

Pi Agent会话管理的单元是Session。比如我跟AI进行了三次对话，让AI在水果列表里面，新增苹果，新增香蕉，新增橘子。这三次对话的全部历史就是一个Session。然后我可以输入/new创建一个新的Session。在新的Session里面，再让AI在蔬菜列表里面添加茄子，添加芹菜，添加白菜。这样我们就拥有了两份对话历史，两个Session。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/9a9c2d1fb623aa61cab8c1eaa72d2b32_MD5.jpg)

当我们把窗口关闭以后，下次想继续工作，可以输入pi -c从最近的一次Session进行对话，也就是蔬菜列表这个。也可以输入pi -r挑选一个Session进行对话。比如这次我挑选水果的Session，我们就回到了水果这次的对话历史。在Pi里面，每个Session并非是纯线性的结构，而可以是一个树状结构。这就是Pi的特色功能对话树。比如我可以来到蔬菜的这个Session里面，输入命令/tree进入对话树。这里我可以选择新增芹菜这个节点敲回车，然后再敲一次回车。这样就把对话回退到了之前的一个历史状态上面。我们可以基于这个历史状态给对话创建分支，进行不同的尝试。比如这一次我不想再增加蔬菜了，我想让它新增一个海鲜。这里AI帮我们新增好了文件，并且写入了皮皮虾。我们可以再输入/tree来看一下。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/d4ef9af5c2ddc73694b0aa996eee4ecc_MD5.jpg)

我们可以在对话树里面看到，在这一次的对话历史上面产生了时间线的分支。在有一个时间线上面继续添加蔬菜，另外一个时间线上面则是新增了海鲜。如果把这个Session画成一棵树的话，大约是这个样子。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/fb1ef6aa81435c1406f317e9d0c20f0a_MD5.jpg)

这里要注意，当我们使用树来回退对话历史，已经写完的代码并不能做相应的回退。比如我想通过这棵树把对话历史回退到茄子的这个状态，然后把后面的皮皮虾还有芹菜白菜全部在代码里面移除。我们使用树来进行回退的时候，只能回退对话历史，不能回退代码。如果想回退代码，我们需要配合git来使用。这里我还是输入/tree命令，找到新增茄子这个对话记录，回车。这样我们通过树先把对话历史进行了回退。接下来我们来通过git把代码也进行回退。我这套代码已经用git管理起来了，如果对git还有AI配合不熟悉的观众朋友们，可以参考这一期视频。我们找到新增茄子这一次提交，然后复制它的commit ID。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/3c64871550a1d2383f818007667ea4b3_MD5.jpg)

回到Pi这边，输入叹号，然后接这个命令：git reset –hard ，也就是强制把代码回退到新增茄子那一次提交的状态回车。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/e3fa137217156566f347b78efbe7cbd1_MD5.jpg)

这样我们再打开代码看一下，现在代码里面只有一个茄子，没有其他的蔬菜了。这样我们就使用git命令搭配对话树，把一段历史从对话记录还有代码两个层面全部进行了回滚。这里要补充一点，我们回退对话历史的时候，Pi给了三个选项。第一个是不总结，也就是一个彻底的回退。第二个是进行总结，也就是把你丢弃的这部分对话历史让AI做一个总结。第三个是告诉AI应该怎么总结。这里我们来看一下这张图。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/99dcb5503638eb014d2e8038ed5592ac_MD5.jpg)

比如现在我想从白菜这次对话历史回退到茄子这个。如果我们选择不总结，AI就把后面的对话历史完全抛弃掉了。如果我们选择总结，AI会对当前分支上这段对话历史进行一个总结。当我们完成回退以后，AI会对这段分支过去处理过的工作有一个大概的印象。这里有一点要注意，AI总结的时候只是总结这段分支上面的工作，它不会去总结别的分支，也就是说皮皮虾这次对话记录它是不会进行总结的。这里我们来试一下，现在在白菜的这次对话上面，然后我输入/tree展开对话树，现在我要回退到茄子这次对话。找到茄子这次对话点击回车，然后这里我们选择summarize，也就是把我回退掉的这段分支上面的对话总结一下回车。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/eae91cde12c2812bb8243daa653c32c0_MD5.jpg)

这样完成了总结，我们可以点Control+O展开。我们看到只有我回退掉的这段分支上面的总结，另外一个分支也就是皮皮虾那个分支它是不会进行总结的。Pi会话管理还有3个重要命令。

首先是克隆，克隆就是把当前的Session完整复制一份成为一个新的Session。比如我现在在蔬菜的Session里面输入/clone，就把当前的Session完整复制进了一个新的Session。然后我可以按两下Control+C退出Pi，接下来输入pi -r看一下现在的Session。我们看到蔬菜的Session就被复制成了两份。

跟克隆类似的命令是/fork，fork不是克隆整棵树，而是可以选择一个对话节点基于这个节点复制出一个新的Session。比如我现在水果的Session里面，我可以选择香蕉这个节点然后进行fork，这样可以创造出一个新的Session。fork出来的新Session只会携带之前的对话历史。这里我来到这个水果的Session里面输入命令/fork，然后选择香蕉这一次对话记录回车。我们看到一个新的Session被创建出来了，而且它只有之前的对话历史。下一个命令/compact，这个命令用来手动触发上下文压缩。比如这是视频开头创建宠物洗护网站的Session，我们看到这里的百分比显示18.1%，表示历史对话内容占用了模型多少上下文空间。当上下文用量超过阈值的时候，Pi就会自动对对话历史进行压缩，从而释放出更多的上下文空间。这里我们也可以使用/compact命令来手动压缩。pi会把之前的对话历史进行总结和精简。我们看到上下文用量从18%降到了10%。这样可以有效提高AI的专注力，并且降低后续的Token消耗。不过在Agent领域，有一个通用经验是清空好于压缩。因为过多的历史会话会干扰AI的注意力，所以当我们执行完一轮任务以后，最好的方式是直接输入/new新开一个Session。也就是新开一个对话来清空模型的上下文，这样有助于AI把注意力全部集中到新的任务上面来，从而提高任务的执行效果。

## 工具设计与插件扩展

Pi是一个极简的Agent，默认只有四个基础工具：读文件(Read)写文件(Write)改文件(Edit)还有运行命令(Bash)。Pi的设计理念是用最小的一组工具来覆盖绝大多数的编程任务。其实这四个工具已经足够强大，特别是运行命令行的bash工具，本身就是一个强大的万能工具。比如可以使用bash调用find来搜索文件，调用grep来检索代码，调用ls来调查目录等等。除了这四个核心工具，Pi还支持Agent Skill，然后就没有其他了。Pi没有MCP，没有SubAgent，没有Plan Mode，没有Todo，也没有btw。Pi的设计哲学是核心越小越干净，模型反而能更好的发挥。同时让用户有最大的自由度去组装其他的能力，正如Pi的官网首页上这句话：让工具来适应你的工作流，而不是让你去适应工具。Pi提供了非常丰富的扩展能力，主要体现在两个方面：一个是插件，另外一个是Skill。在本章节我们来看怎么通过配置插件来给Pi扩展出各种能力。给Pi装插件非常简单，我们先来到Pi的官网，然后找到这个package，这里就是它的插件列表。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/a0a041283981c67617645f2de70abc8d_MD5.jpg)

我们先看几个比较重要的，首先是这个pi-web-access，让Pi具有联网搜索的能力，而且可以更方便的提取网页信息。这里有它的一键装命令，我们把它复制一下。

还是打开Windows的控制台，把命令粘贴过来回车。这样联网插件就装好了。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/bf854df7846d2d1e284aaf4f083bc8a0_MD5.jpg)

然后我们把Pi启动起来。这里有一个\[Extensions\]显示现在有了联网插件。我们可以来测试一下，问它一下青岛天气怎么样。我们看到Pi调用联网搜索的能力然后做了个总结显示出来了。这个插件非常好的一点，它是零配置模式，它接入了Exa MCP服务，而且不需要任何的API key，装上就能用，非常的方便。如果想在Pi里面卸载一个插件也非常容易，我们就把这个装命令的install改成uninstall就可以了。这样就把联网搜索的插件卸载掉了。我们再来看一个插件pi-subagents。这个插件可以让Pi拥有并行运行多个子代理的能力。我们还是复制一下安装命令。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/4821d21312e761caf01efed07f943609_MD5.jpg)

我们使用默认装命令，它是把插件装到Pi的全局目录下面。也就是说这个插件会对所有的项目生效。我们每装一个插件，其实都是增加了一部分系统提示词，如果有的项目里用不到这个插件，其实是给模型增加负担。所以我们还有另外一种装方式，就是把这个插件仅仅装到我这个项目里面，也就是pi\_test这个工程里面，而不是进行全局的装。如果想进行项目级别的装，我们可以在后面敲一个空格接 -l，l就是local的意思，然后回车。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/bd5b1e1773e617554efd8282022f6094_MD5.jpg)

这里来到项目目录看一下，我们看到这个插件就被装到了项目目录.pi这个文件夹下面。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/76be6db710608156f73edb0d3c809338_MD5.jpg)

也就是这个插件现在是一个项目级别的插件，只对当前这个文件夹生效。这样我们还是把Pi启动起来，因为这个目录下面有一个插件，所以第一次启动的时候它询问我是否信任当前目录。这里我选择信任。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/fc9deee299695fabaedb927eaf8b3dc3_MD5.jpg)

这里看到我们的插件就装好了。这里我们输入/pi-subagents调用这个插件自带的技能。![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/8a9f45ff9455a548c062554add295eae_MD5.jpg)

我让它给我设计5个不同风格的个人网页回车。我们看到Pi启动了5个worker，也就是5个sub Agents并行开发这个页面。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/ab0dce6ae53c2229427bdf613b0bb162_MD5.jpg)

5个页面总共是5种不同的风格。这样Pi使用5个子代理并行完成了工作，并且完成了并行的审查与修复，交付了5个个人网页。可以来到目录看一下实际的效果，还是不错的。Pi默认是没有MCP功能的，我们可以通过装这个pi-mcp-adapter插件来让它具备MCP功能。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/0d554df79284ff79f2d6e8b5244cbf2c_MD5.jpg)

这里我还是把装命令复制一下粘贴进Windows控制台执行。我们可以进插件看一下MCP Server怎么配置。这里写了它自动读取. [mcp.json这个文件。那这样我来到项目目录，新建一个.mcp.json这个配置文件。这里我准备配置一个高德地图MCP，我把这一段复制一下。](http://mcp.xn--json-of5f95bn18gk00e.xn--,-0n6a4en5o04ttpa86m8tij5d7pc956ea5304f1kc4x8b.mcp.xn--json-of5f95bn18gwk6bz44albd.xn--mcp,-k84fea2g6m034ao9ar96atsa59r3c277kjejla31ug61fbt0f1qsdpa920gvjdx33g./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/bfbda1b5612651dc11184c9fffb2d9ba_MD5.jpg)

后面这里的key需要替换上从高德地图官网申请的key。这里我在地图应用的开放平台申请了一个key，把它复制一下粘贴过来。好这样就配置完成了。接下来我们把pi启动起来，这里显示MCP Server有一个准备就绪了。我们来测试一下，我让它查一下从太平角公园到崂山仰口公共交通怎么走。我们看到Pi可以调用高德地图MCP查找这些坐标信息还有规划的路线等等。Pi给我们输出了一份完整的线路攻略，效果很不错。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/48a7da0409a7215ca5f41ce37d4aad38_MD5.jpg)

我以前使用Claude Code的时候，经常依赖一个功能叫做btw，也就是by the way的缩写。btw可以在AI工作的同时开启一个旁路对话，我们可以在这个旁路对话里面询问AI一些问题，这种旁路对话不会打断AI的工作。Pi原生是没有btw功能的，我们可以通过配置插件来把这个功能给它添加上。这里我还是来到Pi的packages，然后在filter这里搜索btw。如果有多个同名插件，建议装这个更新时间更靠前然后下载量更大的。这里我选择最前面这个，还是复制一下装命令。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/a432e6aee9aad7e336dd42046710b009_MD5.png)

打开Windows控制台，粘贴过来回车。这样就装完成。然后我们把Pi启动起来。这里我先让AI调查一下这个项目的功能。在AI紧张工作的同时，我可以开启一个旁路对话，输入/btw，后面可以提问一个技术问题。比如我问它Nextjs是什么回车。Pi打开了一个子窗口来为我们回答问题。我们看到现在处于一个旁路对话里面，它不会影响AI工作。我们可以在这个窗口里面继续提问，也可以敲快捷键Control+C退出这个子对话回到主对话。我们看到刚才我们的旁路提问没有干扰主对话，主对话还在继续工作。再介绍一个我每天都会用的功能，也就是Plan Mode计划模式。我们在插件这里搜索plan，找到第一个Plan Mode相关的把它复制一下。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/86d1bda2426b18fd22a71c7fd3784ade_MD5.jpg)

来到控制台执行，这样Pi就有了计划模式。我们把Pi启动起来。这里我们输入/plan-mode回车。我们看到下面有一个plan的小标记，表示现在计划模式里面。在计划模式里面，AI不会动手干活，而是会先输出一份计划，然后我们可以调整并且更改这份计划。当AI跟我的需求对齐以后，我就会关闭掉计划模式，让AI着手执行。我们来试一下，我说把数据库改造成Supabase的数据库。我们看到Pi先是生成了一份计划写到了 [PLAN.md文件里面。我们可以修改这份计划，如果对这些计划确认无误，就可以再次输入Plan](http://plan.xn--md-zg3cw96fbt4cf9g.xn--,,plan-bj8iutd9d9j54ipzg8pag8dca612fia322yuily7a957fdgpzvdbxou5ws85f1lwfga6g15jkt3co6bha/) Mode命令关闭掉plan模式。然后输入指令说确认实施计划，接下来Pi就开始正式开发了。再介绍一个插件Pi Goal。Goal模式也是前段时间Codex跟Claude Code都支持的一个功能。可以输入/goal命令然后后面给AI一个目标。可以让Pi在多个轮次中朝着一个固定的目标执行工作，直至完成最后的目标。这里我们还是把装命令复制一下来到Windows控制台装一下插件。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/a8800deda08f3a8eccfef922af63ff93_MD5.jpg)

然后我们把Pi启动起来，输入命令/goal。这里我给它一个比较大的目标：做一个html的坦克大战，编写完成以后启动起来试玩一下，然后输出测试结论再重做一个版本。我需要多次迭代，最终效果跟红白机的坦克大战越像越好开始。我们看到现在Pi启动了这个go模式，它开始编写游戏。Pi总共迭代了三次然后完成了游戏的开发。我们可以在iterations里面看到它的历史迭代过程。然后我们可以试玩一下，我这个是 [GPT5.6](http://GPT5.6) Sol模型做的，相当不错

Dynamic Workflows是Claude Code上面的一个特色功能，翻译过来就是动态工作流。它可以根据任务的复杂程度编写一段JavaScript的编排脚本，然后在后台自动调度运行几十或者上百个子代理同时协同工作，让Claude Code可以在单次对话里面实现大规模长时间的执行任务。现在我们也可以通过配置插件给Pi也添加上Dynamic workflows的功能。这里我在插件里面搜索workflow，找到这个pi-dynamic-workflows插件，在Windows的控制台里面装一下。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/9138dbcf1d4475b2a77571061f936798_MD5.jpg)

把Pi启动起来，这里我们先敲workflows通过关键字来触发动态工作流。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/b274e4fe92ef03a631e6d4ae30f85f8b_MD5.jpg)

我让Pi调研22年到26年AI领域具有重大影响力的论文回车开始。我们看到Pi启动了Dynamic workflows功能，它启动了10个Agents正在工作。我们可以输入/workflows命令来查看它的后台工作。我们可以看到这10个子代理的工作情况，比如选择第一个子代理，我们看到它主要检索2022年的论文，状态是running。我们通过这个插件在Pi里面使用动态工作流，它的体验跟Claude Code是几乎一模一样的，非常的方便。现在很多桌面Agent都有连接手机的即时通信功能，我们也可以通过插件的方式给Pi配置上这个能力。这里我还是来到它的插件列表，搜索这个即时通信。我们装这个插件把它复制一下打开Windows控制台装。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/98c11c99b6060260ef1533fe50880669_MD5.jpg)

装完成以后把Pi启动起来，然后输入这个命令 /wechat login，接下来用手机扫码完成配对。

接下来输入命令 /wechat start 启动Pi跟手机上的连接。

我们来测试一下，我们在手机通讯录里面找到Bot，先打个招呼。这里给到了回复，我再让他查一下济南的天气怎么样。我们在电脑端可以看到消息过来了，然后Pi这边同步也开启了任务。过了一会查询到了天气，并且推送到了手机上，效果很好。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/50cd99cdffe26e60c6b72e4c03ba61a2_MD5.jpg)

## Agent Skills 的配置与使用

给Pi扩展能力的另外一个重要渠道是Skills。Agent Skills是这一年以来的热点，相信大家也非常熟悉了。Pi Agent遵循标准的Skills协议，我们只需要按照这个路径把Skills放到相应的地方就可以了。这里要放到 项目目录/.agnets/skills/ 文件夹下面，如果有多个Skills都放到这个文件夹下面就可以了。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/f2d05fd9fbd7b6871f6322775e0fb1ee_MD5.jpg)

我们先看第一个，也是我之前视频里面反复介绍过的Skill：Playwright CLI。这是一个让AI获得浏览器自动化能力的Skill。这里第一步我们先执行这个命令把这个Playwright CLI工具本体装一下。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/1536cf6c1e3ff803bb24ac9854a05e98_MD5.jpg)

Playwright CLI工具本体装完成以后，我们开始装配套的Skill。可以直接敲这个命令，我准备用另外一种方法。我们看到源代码的这个目录 /skills/playwright-cli/ [SKILL.md文件在这里。所以我们要的就是把这个文件夹复制出来，这里在code里边点击download](http://skill.xn--md-zg3cw42asvsl71d23c.xn--,codedownload-2h1u68fhdyhv96cya78ix70e0qj52ac53ciu8a48ah9cb13bele79kjp9enzwbh78ibhwbu5aja775pfa/) zip先拿到playwright cli的源代码。然后我们找到这个Skills文件夹，这里我来到项目目录新建一个.agents文件夹，然后把我们刚才下的playwright cli源码里面的skills目录直接复制进来。我们来看这个目录结构， [SKILL.md放到项目目录/.agents/skills/playwright-cli这个目录下面了，](http://skill.xn--md-sh5co21cd4gju2aa8089d/.agents/skills/playwright-cli%E8%BF%99%E4%B8%AA%E7%9B%AE%E5%BD%95%E4%B8%8B%E9%9D%A2%E4%BA%86%EF%BC%8C)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/0a30906ad3cee407ad46fc8d1929ba52_MD5.jpg)

也就是说符合这个Agent Skills的标准。那这样Pi就可以直接识别出来。我们还是来到项目目录先把Pi启动起来。看到Skills里面有了Playwright CLI Skill。这是一个浏览器自动化的Skill，它可以自动操作Chrome浏览器完成各种工作。我们来试一下，这里输入指令，打开谷歌搜索并且进入Pi Agent的官网，让我能看到执行过程开始。这里Pi读取了Playwright CLI技能，操作Chrome浏览器打开了谷歌填入了搜索词，搜索到了Pi Agent的官网，成功在浏览器里面打开了官网，这样任务完成，表现不错。刚才这个例子里面，我们把Playwright CLI技能放到了项目目录下面，如果想让这个技能在所有的项目里面都能生效，我们要把它放到全局的配置目录里面，也就是放到用户的 ~/.agents文件夹下面。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/da47c244444d25a8d61aab52c90d5d06_MD5.jpg)

我们来试一下。这里来到C:，找到这个.agents文件夹。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/ee48afc9d2d352cec258c6697a3664b3_MD5.jpg)

如果没有这个文件夹可以新建一个。这是我刚才在项目里面用到Skills，我直接把这个包含了Skills的文件夹从项目目录拖拽到全局目录里面。我们再看一下目录结构，用户/你的用户名/.agents/skills，然后是playwright-cli技能，技能里面有一个 [SKILL.md文件，这样就可以了。接下来我们在任意一个项目里面启动Pi，启动完成以后，我们在加载的Skills里面就可以看到playwright](http://skill.xn--md,-3h9d0qhd373bg9qrztwegzq6j.xn--pi,,skillsplaywright-9d45a5gm0al4lha2oh62b870f15c5gd519h33a26aea262zoa5494b6nf771dy2i2as372p0v4b4s1l5eemsby965eyuyaya9786eza034m/) CLI技能。这样我们就把它从一个项目级别的技能变成了一个全局的技能。除了我们在Github上面寻找技能，SkillHub也是一个不错的检索技能的渠道。接下来我们来SkillHub上面找几个有意思的技能装一下。比如我要装这个Markdown Converter技能，可以把任意格式的文档转换成Markdown格式。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/fe2ab55ba83f92fab3e7aa7daa5a483d_MD5.jpg)

我们进入这个技能，我们可以通过下zip压缩包然后放到指定目录的方式来装，也可以试试把提示词发给AI让AI来装。这里我把这段提示词复制一下，然后来到Pi把提示词粘贴给他。过了一会Pi就完成了装，不过它提示我电脑上缺少uvx来运行转换Markdown的工具。接下来我跟Pi说你帮我把UV装一下，过了一会，Pi就完成了UVX的装。然后我找一个PDF文件来测试一下。这是一个PDF格式的教案，我把它复制一下然后来到Pi的对话窗口，Control+V粘贴过来，我告诉Pi把它转换成Markdown格式。过了一会，Pi就完成了转换，把PDF格式转换成了Markdown格式。

## Web UI 界面安装与使用

可能有些观众朋友们用不惯命令行风格的Pi，希望有一个简单易用的UI界面，在社区里面也有不少作者配套开发出了一些Pi Web UI，也就是把Pi接入到网页里面去使用。这里面star数量最高的应该是这个项目，有4,200个star，这是前几个月一位国内作者第四种黑猩猩发布的。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/bea0c7b51ea7f50d2f043eadc58db67a_MD5.jpg)

我们来把它装一下。找到GitHub的首页，这里quick start，我们找到这个npx的装命令，在终端里面执行一下输入y。装完成以后它就会自动打开一个网页版的UI界面，我们可以在这个页面里面操作Pi。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/94289dfea40215efee8dbef3103423fe_MD5.jpg)

我们可以在左上角切换项目，这里展示了本期视频我用过的几个项目，然后还可以点击自定义路径打开本地电脑上的一个路径当做项目文件夹，接下来Pi的工作就是在这个项目里面进行处理。左下角是文件浏览器，这里面展示了项目文件夹里面的文件。左下角还有一个模型按钮，我们可以在这里面配置模型订阅。比如添加provider，比如这里我配一个Kimi的模型，选moon shot AI cn，在Kimi的后台创建一个API key，把这个key复制下来填写到这里保存，这样我们就有了Kimi的模型。有了模型以后，我们可以在屏幕中间的模型选择器里面选择到这些Kimi的模型。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/5bb061beb10ad56acb3be36004b14f5c_MD5.jpg)

左下角可以管理技能和插件，比如我选择技能，我们看到这里列出的技能分成两部分。一个是project技能，也就是存放在当前项目目录下面的技能；还有global技能，就是全局的技能。我们可以选择这里的技能，然后选择把它开启或者关闭。关闭以后就在提示词里面隐藏了，模型就看不到这个技能了。及时关闭用不到的技能，可以帮助模型更加节省Token。技能的右边是插件，同样插件也区分project还有global。project插件就是只在本项目里面生效，global就是全局都生效的插件。我们在这个UI里面也可以控制插件的关闭或者开启。在技能管理面板下面，还有一个添加技能，我们可以在这里面搜索技能并且添加。比如我来一个TTS技能，这里就用Edge TTS，也就是文本转语音的技能。它不需要配置API key，是完全零成本的。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/c8f21f62946432af13f977b4e15e4f69_MD5.jpg)

然后我们还可以选择它的装方式是装到项目下面还是装到全局。比如这里我选择项目，点击装，这样技能装好了。我们来测试一下，我让Pi帮我把这段话转成音频发送。我们并不需要特别指定哪个技能，Pi可以根据自己的工作场景来选择使用哪个技能。我们看到它读取到了edge-tts Skill，然后使用工具帮我把音频生成出来了。我们点进去试一下播放。 在中央的对话面板，我们同样可以使用斜线命令来使用Pi的内置命令，使用@符号来选择某个文件，同样我们也可以直接截图然后按Control+V粘贴到Web UI里面。在这里可以调整模型的思考强度。当Pi执行完一个任务以后，在下面还会显示输入跟输出的Token还有预估的花费等等。只要掌握了我视频前半部分介绍的那些TUI功能，这个Web UI应该也可以很快的上手，没有什么使用门槛。当我们关闭掉浏览器，但是还想使用Web UI的时候，可以运行这个命令重新启动，这样Web UI又重新打开了。

## 跨Session记忆与

每当我们开启一个新的对话，就进入了一个全新的上下文，AI完全不记得之前发生了什么，进行过什么样的对话，甚至对整个项目的记忆都是空白的。当项目变得复杂以后，每次对话都要给AI重新交代一遍项目背景，或者让它自己读代码自己摸索，这是一种非常低效的方式。本章节我们就来看怎么给Pi增加跨Session的记忆。通用方法就是，在项目的根目录创建一个 [AGENTS.md文件。这个文件在Codex、OpenCode等等其他的AI](http://agents.xn--md-zg3cw96f.xn--codexopencodeai-q32n2743b4sc7qo41bn82aqc0epx4dg6xaa8597k/) Agent工具里面也是通用的。这里我来到水果蔬菜列表的那个项目的目录，右键新建一个 [AGENTS.md文件。](http://agents.xn--md-zg3cw96f./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/6c610db2c2da6ddcedca3c552e5f0963_MD5.jpg)

这个文件就是AI每次对话时候必读的一个指南。有了这个文件以后，后续我们跟Pi所有对话都会带上这个文件的内容作为上下文。这个文件有助于帮助AI更快地理解项目。然后我们打开它，比如这里我给AI补充了一些上下文，我叫技术爬爬虾，然后擅长的语言，对前端一窍不通，如果遇到网页问题需要用大白话给我解释。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/be8d00f540dba82cbb074e57e62863da_MD5.jpg)

[AGENTS.md文件编写好以后我们保存一下。这里我们还是在终端里面运行Pi，我问Pi我叫什么擅长什么技术，我们看到Pi自动把AGENTS.md文件里面的内容作为上下文带入了对话。](http://agents.xn--md-wu2csby0fhb3d65hdyg0zhemr8hffozi8kgu0h.xn--pi,pi,piagents-427va25rba24fka076ornc85kkwv7k8dfacg133a1i332dwuk2jid39lqp2ae72ariyoy7c4i7c9iajb485oha5972brcez2u.xn--md-rv2ce7ukqfzyyc8k9iw40hewal3tn12aha1960e034d3kwakiy./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/05e07aace3ed5417638d96ae2d3ce38e_MD5.jpg)

如果我们自己编写这个 [AGENTS.md文件也有点麻烦，我们可以让Pi帮我们来编写。比如这里我来到宠物洗护那个项目，我让Pi通读当前文件夹，然后把它学到的关于项目的知识保存到AGENTS.md文件里面。](http://agents.xn--md,pi-rw1hj5aubd7g648a5phmm1b3mlga972lthgvvbbw5gzzas39sg2zc8w5e.xn--,pi,agents-ws2pu1bu1bq6f77hhldgad85cx30a0j2axnbjxwqja2yixf31forrea257aywah35en8nrw0bfijrm1bfjjwk3bca433bta984h915tbcbv8dzz9eyrcx9iupqyl5fxa.xn--md-zg3cw96fbt4cf9g./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/bb689500c2f4b18e515ace67061f44cf_MD5.jpg)

我们看到Pi已经通读了整个项目的源码配置文档，并且创建了 [AGENTS.md文件，可以打开看一下。](http://agents.xn--md,-s18d1b04fmdv67bs6yethu7itz8c./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/807f16094f949fca8a2afc8bf461d0ed_MD5.jpg)

他把关于项目的重要知识都写入了这个文件。后续当我们开启新的对话的时候，Pi就会自动的获取这些知识，可以帮助他更快的上手项目。所以对于复杂项目来说，这个 [AGENTS.md文件是必须要写的。](http://agents.xn--md-zg3c13hjszw2hw7az51f6y9aok5a./)

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/af1a8584dd49e35ecaba9597f310c1c3_MD5.jpg)

我们把 [AGENTS.md文件放到项目目录，它只对当前这个项目生效，如果我们想给Pi补充一些全局的提示词，Pi为我们提供了另外一种方式，可以编写全局的AGENTS.md，可以对这台电脑上面的所有项目都生效。这里我来到这个目录](http://agents.xn--md,,pi,pi,agents-0l9yda40fhk48ccn98cqei1wn9nu6oc3aka23mq7in1a111brdyiy09p2ldrz0a5kerodpa5202a3scpc217h9lmna210tga157pepak1ihsdlu5bk46o2vqava223dai7857a7th4j8fdjd5t7sryzbfr5cwm8gla.xn--md,-x28d42be8ria965nkknzlhd7emm5cciap1orwbf33g4r4cokesy0bste.xn--ciqw1hqwo6tc48i37yx13bda106b/) C:.pi，如果是Mac电脑的话就是 Home目录.pi文件夹，然后来到这个agent文件夹。在这里面就可以新建一个 [AGENTS.md文件，这个文件就是一个全局的AGENTS.md文件，它对所有的项目都会生效。因为之前我看过一些新闻，AI有时候会编写命令失误把用户的整个D盘都删除了，所以我一般会加一个全局的提示词。我们打开这个AGENTS.md文件添加这一段：我这个提示词要求禁止Pi批量删除文件或者目录，只能通过明确的文件路径单个删除，如果需要批量删除文件应该停止操作，并且向用户请求让用户来手动删除。这里我随便开一个项目来测试一下，我问Pi删除文件有什么规矩，我们看到它遵循了我给它的全局提示词。除了这个AGENTS.md文件，Pi还支持另外一种补充全局提示词的方法。还是在Pi的全局配置目录，新增一个APPEND\_SYSTEM.md文件。这里append就是追加的意思，system是系统。这个文件的意思就是追加系统提示词。Pi会把这个文件里面的内容直接追加到系统提示词里面。所以写到这个文件里面的提示词优先级更高，效果也更强。不过一般场景下，我还是建议用这个通用的AGENTS.md文件就足够了。](http://AGENTS.md文件，这个文件就是一个全局的AGENTS.md文件，它对所有的项目都会生效。因为之前我看过一些新闻，AI有时候会编写命令失误把用户的整个D盘都删除了，所以我一般会加一个全局的提示词。我们打开这个AGENTS.md文件添加这一段：我这个提示词要求禁止Pi批量删除文件或者目录，只能通过明确的文件路径单个删除，如果需要批量删除文件应该停止操作，并且向用户请求让用户来手动删除。这里我随便开一个项目来测试一下，我问Pi删除文件有什么规矩，我们看到它遵循了我给它的全局提示词。除了这个AGENTS.md文件，Pi还支持另外一种补充全局提示词的方法。还是在Pi的全局配置目录，新增一个APPEND_SYSTEM.md文件。这里append就是追加的意思，system是系统。这个文件的意思就是追加系统提示词。Pi会把这个文件里面的内容直接追加到系统提示词里面。所以写到这个文件里面的提示词优先级更高，效果也更强。不过一般场景下，我还是建议用这个通用的AGENTS.md文件就足够了。)

## 安全机制

Pi只有一个非常非常基础的安全机制，就是当我们在一个包含了插件或者Skill的陌生目录下面启动Pi的时候，它会询问用户是否信任并且加载这些插件或者Skill。在我们之前装Skills的时候见过这个提示。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/c385067cc39d56d123fef7d4a2debcf3_MD5.jpg)

一旦Pi开始了运行，它就没有任何的安全限制了，永远处于最高的权限下面，他编辑文件、执行命令等等都是自动执行，不会停下来询问用户。Pi也没有任何的沙箱机制。这是开发者有意为之，因为Pi的设计哲学是打造一个极简的Agent，开发者希望Pi本体永远保持简洁高效，让Pi有足够的能力并且用最快的速度来完成任务，而不是在Pi内部制造一个看似安全但实际不完整的沙箱。如果用户刚需Agent具备极高的安全性，我们则可以用其他的方案来保障Pi的安全性。这里有两种方案，第一个是官方文档里面推荐使用容器虚拟机等沙箱来运行Pi。比如之前视频里面我介绍过WSL，也就是运行在Windows上的Linux虚拟机。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/73cc8baa33c7c721f997dd8095ddfbc7_MD5.jpg)

我们使用WSL来运行Pi，即使AI把环境搞坏了，通常也只需要删掉虚拟机然后重建一个虚拟机即可，它不会影响宿主机。还有类似的方案，比如可以用Windows上的虚拟机Hyper v，还有用Docker容器等来运行Pi，都是非常好的选择。因为Pi的极简轻量，使得Pi成为了最适合在容器或者虚拟机里面运行的Agent。它启动速度非常快，占用内存非常低，很适合使用Docker容器或者K8S进行批量部署。我们也可以通过装插件的形式来给Pi提升安全性。比如我们可以装这个pi-permission-system，装完成以后，Pi如果需要执行敏感操作它都会先弹出审批窗口，等待用户审批以后再执行，就有点像Claude code的那个权限系统了。这种插件会拖慢我的开发效率，所以我是不装的，这里我就不演示了。

## 自己动手DIY定制插件

Pi开放了大量接口，几乎允许用户对任意的功能进行自由定制。包括模型、工具系统、会话管理甚至UI界面都能修改，自由度非常的高。本期视频前面介绍的那些插件，都是社区开发者基于Pi提供的开放接口实现的。Pi最有意思的地方在于，就是你可以自己动手DIY插件，把它改造成真正适合自己的Agent。本章节我们就来编写属于自己的插件。编写插件我们也不需要自己写代码，Pi本身就内置了插件相关的开发知识，也就是说，Pi不仅仅是能装插件，甚至还能自己给自己写插件。我们先来看第一个例子，我们来看一个例子来定制Pi的UI。我让Pi编写一个插件，我需要它根据IP查询我的地理坐标，然后再根据地理坐标查询我当地的天气，最后把天气展示到对话窗口的上面回车。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/cfcccc5118123668b7d3319842ef4c9d_MD5.jpg)

我们看到Pi自己读取了关于开发插件的文档，然后开始为我们编写插件。AI帮我们编写好了插件，放到了项目目录/.pi/extensions这个文件夹下面。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/74c98c6dbc395a09e462cc262c5837bb_MD5.jpg)

这个插件本身就是一个ts文件非常的简单。现在我们只需要敲命令/reload重新加载一下。我们看到我的地理位置坐标天气所有的数据都显示到了对话框上面。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/c3520c7da85d93d8431b8fa5839adc22_MD5.jpg)

这样我们就让AI编写了插件，完全定制了Pi UI。我们看到刚才编写好的插件是放到了项目目录/.pi/extensions文件夹下面，所以它是一个项目级别的插件，只对这个项目生效。我们也可以把这个插件变成一个全局的插件，对所有项目都生效。这里我们还是来到Pi配置目录 C:.pi，如果Mac系统的话就是~/.pi，然后来到这个agent文件夹。这个文件夹就是Pi的全局配置目录。接下来我们只需要把项目目录里面存放了插件的extensions文件夹复制一下，然后粘贴到Pi的配置目录里面。接下来我们在任意一个项目，比如这个宠物洗护的项目来启动Pi。我们看到天气插件都生效了。

也就是说，我们把自己编写的插件装到Pi的全局目录下面，对所有的项目都可以生效了。我们再来看一个例子，跟权限相关的。我让Pi给自己开发一个插件，这个插件禁止AI后续编辑读取这个受保护的.env文件，如果AI尝试操作直接阻止，并且提示这是受保护的文件开始。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/5f26f01d5e7e3ffcc0c69495070bacfa_MD5.jpg)

好Pi完成了插件的编写，这里我们reload加载一下插件。我让AI看看.env文件里面有什么。这里插件生效了，AI无法读取里面的内容。我们再来编写一个插件，我让Pi当准备执行rm也就是删除命令的时候，先弹窗询问我是否允许执行开始。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/9bc91fac7a9c3d6db5cc3bfd19646ee0_MD5.jpg)

好Pi完成了插件的编写，我们还是reload激活一下插件。我在项目目录放了一个测试文件，我试一试Pi能不能删除。我们看到Pi在删除的时候，弹窗询问我是否要删除，这里我选择no。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/45da3e0c442d607e9024d44ba5b7634d_MD5.jpg)

没有删除成功，文件还在。我们再试一下，这次选择yes，文件就被删除了。刚才我开发的三个插件都是我使用 [GPT5.6](http://GPT5.6) SOL一把就跑通的。所以我们使用Pi自己给自己开发插件一点也不难，只需要跟AI讲清楚需求，很快就能完成开发。

## 源代码架构与 SDK 集成

我们来到最后一个章节，简单介绍下Pi的源代码架构。这里我们打开Pi在Github上面的仓库，找到这个packages文件夹。我们重点来看这几个包Agent、ai、coding-agent还有tui。ai这个包负责模型调用，它主要负责把市面上几十个模型厂商做成统一的调用规范，让Pi能使用一套相同的接口来调用模型。

![图片](assets/Pi%20%E5%A4%A7%E9%81%93%E8%87%B3%E7%AE%80%EF%BC%8C%E8%B6%85%E8%B6%8ACodex%E5%92%8CClaude%20Code%E7%9A%84%E6%9E%81%E7%AE%80Agent%EF%BC%8C%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A8%E6%94%BB%E7%95%A5%EF%BC%8C%20%E4%B8%80%E6%96%87%E7%B2%BE%E9%80%9A/da7ef4b04d2c3596088a60fbf1d8f307_MD5.jpg)

agent这个包主要实现的是Agent loop，也就是我们之前介绍的Pi核心双层循环机制。coding-agent则是对编程功能的具体实现，里面定义了Pi的四个基础工具，定义了Pi的系统提示词，它的Skills机制还有插件的实现机制等等。tui则负责实现我们看到的这个命令行界面的全部功能。Pi的源码就是一个Agent设计规范的教科书，如果你是从事Agent开发等相关职业的话，这套源代码非常值得深入学习一下。Pi的开发者已经把这几个核心包封装成SDK，比如你的项目需要一个接入市面上所有大模型的功能，我们就可以直接引用Pi AI的SDK。先npm install在你的项目里装一下。然后我们直接引用createModel方法，就可以在你的项目里面接入任何一种模型，并且跟模型进行对话。还有Pi Coding Agent现在也是一个SDK，同样也是使用npm命令在你的项目装一下。然后你的项目里面就有一个开箱即用的Agent。我们先创建一个Seesion，然后就可以直接开启任务。好这就是本期视频全部内容了，感谢大家，我们下期再见。

**微信扫一扫赞赏作者**