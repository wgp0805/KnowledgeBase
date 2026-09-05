---
title: "Codex 保姆级入门教程（6000字长文）"
source: "https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653263216&idx=1&sn=7e819b29a7c9db2d1e58f91abca3149e&scene=21&poc_token=HGfVOWqjDXOVHOguHzncMOoFD9ol6H99B5gf6p4E"
---
小灰 & 阿咕噜 程序员小灰 *2026年5月2日 12:23*

大家好，我是程序员小灰。

如今的AI编程领域，可谓是百家争鸣，Cursor、Trae、ClaudeCode、Codex......全球各大AI巨头都在AI编程这个赛道展开激烈的竞争。

前几天小灰发布了一篇 Claude Code 的入门教程，反响还不错，也有许多朋友在后台留言，询问我们能不能发布一篇关于 Codex 的教程。

没问题，安排上！

今天小灰就来给大家系统性讲解 Codex 这款AI编程工具，聊一聊 **Codex 到底能不能打，普通人怎么安装、怎么上手、怎么少踩坑。**

文章较长，建议大家先收藏、不迷路。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/e30593ed28ceb60c2eb9eec8a5f2a90d_MD5.webp)

## 一、为什么 Codex 值得考虑 ？

Claude Code 好用吗？当然很好用。

然而用过 Claude Code 的朋友都知道，它有两个让人尴尬的特点：

1\. **免费额度较少** ：用着用着就要你充钱，而且还死贵。

2\. **封号风险** ：Anthropic 官方频繁封号，这一点最为致命。

因为以上的这些问题，小灰的粉丝群里经常有人问：”OpenAI 有没有类似的AI编程工具呢？”

答案是“有”，而且稳定性比 Claude Code 要好得多，不但编码能力强，而且还能接入 GitHub，这款产品就是 Codex。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/453155031e1ce32cbe2e698247d33c68_MD5.png)

## 二、什么是 Codex ？

Codex 是 OpenAI 官方出品的 AI 编码工具，能理解你的需求，帮你写代码、跑命令、调 Bug。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/2da082a5580af1301c15bab809cb8f50_MD5.png)

Codex 具有 **四种运行模式** ，覆盖你能想到的大部分使用场景：

- • **CLI（命令行）** ，在终端里跑，适合命令行党，主打一个黑框里掌控全局。
- • **App（桌面应用）** ，有图形界面，支持 macOS 和 Windows，适合不想跟终端互相折磨的人。
- • **Web（网页版）** ，打开浏览器就能用，不用装任何东西。出差用别人电脑、临时改个代码，随开随用。
- • **IDE 插件** ，支持 VS Code、Cursor、Windsurf。写代码的时候直接在编辑器里调用，不用切窗口，不用复制粘贴，代码上下文自动带过去。

四种运行模式怎么选？

终端党用 CLI，鼠标党用 App，临时救火用 Web，天天写代码用 IDE 插件。

这四种模式没有优劣之分，大家哪种模式用着顺手，就可以优先选用哪种模式。

## 三、Codex 的最新版本

如果你只是把 Codex 理解成"OpenAI 版 Claude Code"，那现在这个理解有点窄了。

2026年以来，Codex 已经不只是一个命令行编码助手，而是逐步构建为一套"AI 干活系统"。

按官方 Changelog 看，2026 年 4 月 Codex 最核心的变化就三个：

1\. **Codex App 26.415（ **2026-04-16 更新）****

桌面端从“聊天式编码工具”升级成更完整的 AI 工作台，开始支持内置浏览器、任务侧边栏、GitHub PR 处理、artifact viewer、Memories、多终端、多窗口，以及 Windows 托盘的适配。

2\. 模型版本 GPT-5.5（2026-04-23 更新）

GPT-5.5 开始进入 Codex，重点提升复杂实现、重构、调试、测试和验证这类重任务的能力。也就是说，Codex 不只是能写小脚本，而是更适合接真实项目里的复杂任务。

3\. **Codex CLI 0.128.0（ **2026-04-30 更新** ）**

CLI 加入可持久化的 `/goal` 工作流，可以把一个长期目标创建、暂停、恢复和清理；同时新增 `codex update` ，权限、沙箱和插件能力也更细。

从上面的迭代可以看出，对于现在的 Codex，不要只问"它会不会写代码"，更准确的问题是， **它能不能接住你工作流里那些重复、复杂、跨文件、需要验证的任务。**

不过这篇是入门教程，不会把每个高级功能都展开，你先知道它们存在就行，真用到的时候再按场景深入。

## 四、Codex 适合什么样的场景？

下面的五种情况，最适合选用Codex：

1. 1\. **你已经有 ChatGPT Plus/Pro** **订** **阅** ，那就优先试 Codex。你每个月交的那 20 刀，终于不只是用来写周报了。
1. 2\. **你想要 GUI** ，不想在终端里和 AI 大眼瞪小眼，想点点鼠标就把活干了。
2. 3\. **你被账号稳定性折腾怕了** ，多一个官方工具，就多一条备用工作流。
3. 4\. **你想先低成本试试** ，Codex 是否包含在你的套餐里，以官方页面和客户端显示为准。能用就先用，别先付费上头。
4. 5\. **你喜欢 OpenAI 的模型能力** ，觉得 GPT 系列写代码、解释代码、改代码都比较顺手。

如果你没有 ChatGPT 订阅，也不想充钱，那也没关系，后面会讲怎么给它接入国内大模型。

## 五、如何安装 Codex ？

Codex的安装过程并不复杂，一共就几步，只要你的电脑配置不是太差，基本都能跑起来。

### 1\. 环境要求

需要安装 `Node.js` 和 `git` 。

在本地终端检查一下环境：

```
node --version

npm --version

git --version
```

如果没有安装，先补上。这个环节没什么玄学，少一个后面都容易报错。

Node.js 下载地址：https://nodejs.org/zh-cn/download

Git 下载地址：https://git-scm.com/install/windows

这里提醒一下，如果你是 Windows 用户，最省心的方式是优先装 App。CLI 也能用，但如果遇到环境问题，可以考虑用 WSL，或者先跳到 App 部分。

### 2\. 安装 CLI

CLI 适合已经习惯终端的人。两种方式，选一个：

```
# npm 安装
npm install -g @openai/codex

# Homebrew 安装（macOS）
brew install --cask codex
```

验证安装：

```
codex --version
```

看到版本号就说明成功了。

如果这里没看到版本号，优先检查 Node.js、npm 全局路径和网络。

### 3\. App 安装

Windows 下载地址：

https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website\_cta\_psi

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/3b6574363c836062c064d32896906a25_MD5.png)

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/b0c67ce16d6a474d6e88994751691eff_MD5.png)

### 4\. 云端版

直接访问：https://chatgpt.com/codex/cloud

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/6ef63f347be1f65f25f8cecd321030ce_MD5.png)

### 5\. IDE 插件

如果你用 VS Code、Cursor 或 Windsurf，可以装插件：

安装地址：https://developers.openai.com/codex/ide

装完之后在编辑器里就能直接调用 Codex。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/4f09bd21334d45f4bebdac1a9e5bc676_MD5.png)

到这里你已经有四条路了。新手建议从 App 开始，开发者建议从 CLI 开始，已经有 GitHub 仓库的人可以直接试云端版。

别纠结入口，工具不是对象，不需要从一而终。

## 六、在 CLI 端使用 Codex

CLI 是 Codex 最像“开发者工具”的形态。你在终端里说需求，它在项目里改文件、跑命令、修问题。

### 1\. 启动

```
codex
```

首次启动会让你选择登录方式。

还有可能会报错： `Error: account/read failed during TUI bootstrap`

这个错误在官方 issue 里已经有人复现， **重新登录就恢复了** 。

这种问题就别硬刚了，先登出再登录，很多时候比你研究半小时日志更有效。

👉 直接执行：

```
codex logout
```

或者一步到位：

```
codex login
```

浏览器登录一遍基本就好了，很多人都是这样修复的。

### 2\. 登录方式

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/83343f99396c6cc03133717f8f0da25c_MD5.png)

**方案一：Sign in with ChatGPT（推荐）**

会打开浏览器，用你的 ChatGPT 账号授权。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/6e975bf8ce1d492fb30a175b14993eee_MD5.png)

363

**方案二：Enter API Key**

去 https://platform.openai.com/ 生成一个 API Key，粘贴进去。这种方式按 token 计费，适合已经习惯 OpenAI API 的用户。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/e067387ad7d6575b072fdc97500d09da_MD5.png)

### 3\. 模型选择

模型以你当前客户端显示为准。

这里别死记型号，AI 工具更新很快，今天看到的默认模型，过段时间可能就变了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/9d3ff59855c26bf9ce298e8eb3c3f77e_MD5.png)

如果想切换模型，用 `/model` 命令。

### 4\. 30 秒上手

装好了，先跑一个试试。别上来就让它重构祖传系统，先拿小游戏练手，心态比较健康。

在 D 盘新建一个 `test` 文件夹，然后打开终端输入命令：

```
cd d:\test\
```

然后输入下面命令：

```
codex "用 Python 写一个贪吃蛇的游戏"
```

就这么简单。Codex 会理解你的需求，生成代码，创建文件，甚至帮你运行。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/0a82d5e326a8985f07782d43b8c8c7b1_MD5.png)

你不需要一开始就告诉它用什么框架、怎么组织代码，它会先根据需求做判断。这就是 AI 编码工具的核心价值： **你负责描述目标，它负责拆任务、改文件、跑命令。**

试完这一个，你就知道 Codex 大概是什么感觉了。后面再把它放进真实项目里，价值会更明显。

当然，AI 写代码和人写代码一样，都需要你 review。不要把它当成完全不用检查的自动交付机器。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/2137cfbd3511811df369ad5e29ff95c3_MD5.png)

### 5\. 常用命令

| 命令 | 用途 |
| --- | --- |
| `codex login` | 登录 |
| `codex logout` | 退出 |
| `codex app` | 启动桌面应用 |
| `/init` | 初始化 |
| `/model` | 切换模型 |
| `/compact` | 压缩上下文 |
| `/new` | 开启新会话 |
| `/plan` | 开启计划模式 |
| `/ask` | 仅提问不执行 |
| `/settings` | 打开设置 |

## 七、在 App 端使用 Codex

### 1\. 启动

App 适合两类人：一类是不想一直待在终端里，另一类是希望同时看项目文件、对话记录和修改内容。

打开方式有两种，一种是直接双击桌面 `Codex` 的图标，一种是执行命令 `codex app`

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/ada47ca8f97b761499c0210975696dbe_MD5.png)

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/94be765d52e3906e26113611d3360093_MD5.png)

选择你的偏好后，点击 **继续** ，也可以点击 **跳过** ，后面再配置。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/220b9b0c546db7c32c7f4fa278ccb29b_MD5.png)

由于我之前登录过 `Codex CLI` ，所以 App 这边不用登录就可以直接使用了。后面的 `IDE 插件` 也是一样的道理，同一套登录状态可以复用。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/98b4e1d7b2de5d8b64deb1c45ce0ac7c_MD5.png)

### 2\. 基础使用

点击 `项目` ，然后选择 `使用现有文件夹` ，找到刚刚上面制作贪吃蛇的那个文件夹 `test`

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/9e524bf71b59efbac35d4be914c25123_MD5.png)

可以看到刚刚的对话都已经加载进来了。这一点很关键：Codex 不是只能单次问答，它会围绕一个项目持续工作。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/86ed75b327309a6c56551e4ec9b9c541_MD5.png)

点击右上角的 `切换文件树` ，可以看到当前目录下的文件。点击具体文件后，左侧可以预览内容，也可以直接在文件里做注释，让 Codex 按你的反馈继续修改。

这时候它就不只是“问答机器人”了，而是能围绕项目上下文继续修改。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/bccbab7e0a7b0948b589db8761159184_MD5.png)

右下角的设置里面还可以查看剩余额度。轻度使用一般够用，但额度策略会变化，最终以客户端显示为准。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/a001b7025f8987a08193f7ba77974906_MD5.png)

## 八、在云端使用 Codex

云端版适合处理已经放到 GitHub 上的项目。你可以把它理解成：本地 Codex 是在你电脑上干活，云端 Codex 是连到你的 GitHub 仓库里干活。

如果你已经有 GitHub 仓库，可以直接跳到“连接 Codex 到 GitHub”。下面这段是从零创建仓库的完整流程。

### 1\. 初始化 Git 仓库

打开终端输入命令 `cd d:\test\`

然后执行以下命令：

```
git init
```
![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/d1e6e92614750d1705a319ab5879d04d_MD5.png)

执行完成后，可以看到 App 上面多了一个 `提交` 的按钮。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/6468602cf522d875b07c388f3c1f348d_MD5.png)

点击 `提交` ，在提交消息里填一段提交说明，然后点击 `继续` ，这样我们的修改记录就保存了。

这里不要学某些老项目，全员提交信息都是 `update` ，多年以后查记录，自己都想给自己一拳。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/0586dd509f81b5f677e33ca4d57c074e_MD5.png)

### 2\. 创建 GitHub 远程仓库

接下来我们打开 GitHub，创建一个名为 `test` 的远程仓库。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/f951c0d76d3bece405f3fb5b468bfd69_MD5.png)

创建完成后可以看到这些提示。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/6f69c9b21a2d7affe3aaf1771091dec3_MD5.png)

我们在刚刚打开的终端执行如下命令。注意把下面的地址替换成你自己的仓库地址：

```
git remote add origin https://github.com/ailot/test.git
```
![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/786a3313797c5b58d89094209b56c0ca_MD5.png)

执行完成后，可以看到 App 上面的 `推送` 按钮变成可点击的了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/3b99727ba220125cd684848d8dab8f20_MD5.png)

在刚才的终端继续执行命令。

```
git branch -M main

git push -u origin main
```

在执行完第二条命令后，会提示你登录 GitHub。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/873345fafb0bc5c18d107836b772af0a_MD5.png)

选择浏览器登录 `Sign in with your browser` ，出现这个界面就表示成功了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/3a7a849c4f3480729f2fbde27b8ae8ee_MD5.png)

终端同样可以看到推送成功的日志。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/80fe3aed936557626d9bca3d2b4311db_MD5.png)

GitHub 仓库也能够看到我们刚刚推送的文件。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/869c4ba4a69d89f8e5683b4ff924884c_MD5.png)

### 3\. 连接 Codex 到 GitHub

打开 https://chatgpt.com/codex/cloud，点击\`连接到 GitHub\`

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/bd27625cb929878f2a7d5653ce8f1cc6_MD5.png)

点击 `继续 GitHub`

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/81f4bed3174961f5cd3368532934b6dc_MD5.png)

291

选择 `Authorize` 进行授权。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/186dd691396e797de7068be7cfa369c1_MD5.png)

406

然后我们进入云端 Codex 了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/753745fc30248e66e867729d47b47f06_MD5.png)

575

按照如下步骤配置远端代码仓库。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/d789639c34d839913c8c46d3bc3e5d37_MD5.png)

556

选择刚刚我们在 GitHub 上面创建的 `test` 仓库，然后点击 `Install & Authorize` ，输入密码授权。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/c31b4f20261534c270d1c3ae5dfd2c52_MD5.png)

476

刷新页面，可以看到我们的 `test` 仓库已经在 Codex 里面了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/72495f4b7c87401868c3d7fc3f9b475d_MD5.png)

我让它看一下这是个什么项目。

这一步很适合用来测试 Codex 有没有看懂仓库。别一上来就让它“重构整个系统”，先问它“这是个什么项目”。

输完提示词，点击发送，可以看到它在下面创建了一个任务在执行。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/0e7a515b2fbb3a1bc1361ec8e0f4e566_MD5.png)

532

点击进去可以看到具体的执行结果。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/7deeb14d282ba99ec8c6c5b3b7e7e6c3_MD5.png)

## 九、IDE 端使用 Codex

IDE 插件适合日常写代码的人。它最大的价值不是“再开一个聊天窗口”，而是直接读取当前项目上下文，在你写代码的位置帮你改。

这就很适合那种写到一半突然卡住的时刻：脑子说我懂了，手说你放过我。

打开 `VSCode` ，然后安装 `Codex IDE 插件` ，具体操作如下：

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/69ca19a55c01c2a1a93dea42b895fb15_MD5.png)

安装完成后重启 VS Code，然后打开刚刚我们在 D 盘的 `test` 文件夹，同样可以看到刚刚的对话都已经加载进来了。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/884c547e75e672da9dc1060838765274_MD5.png)

后面还想怎么改，可以直接在对话框里面指挥。

我建议你从这几个场景开始用：

- • 让它解释当前文件的作用
- • 选中一段代码，让它重构或补注释
- • 把报错信息贴进去，让它定位问题
- • 让它给某个函数补单元测试

IDE 插件的优势是上下文更近，适合边写边改；CLI 的优势是执行力更强，适合让它完整跑一个任务。

简单说：IDE 插件适合边写边问，CLI 适合直接派活。

## 十、进阶用法

### 1\. AGENTS.md 配置文件

在项目根目录创建一个 `AGENTS.md` 文件，告诉 Codex 你的项目规范。这个文件很重要，它相当于给 Codex 写一份”项目说明书”。

```
# 项目规范

- 语言：Python 3.11+
- 代码风格：PEP 8
- 测试框架：pytest
- 注释：中文注释
```

如果你是新手，可以先用下面这个更完整的模板：

```
# AGENTS.md

## 项目说明

这是一个 Python 项目，主要用于练习小游戏开发。

## 开发规范

- 使用 Python 3.11+
- 代码保持简单，优先可读性
- 新增功能时同步更新 README
- 修改代码后尽量运行测试或启动程序验证

## 交互偏好

- 先解释修改思路，再改代码
- 涉及删除文件、重构目录、安装依赖时先询问
- 回复使用中文

## Codex 特定配置

- 权限模式：自动审查（关键操作需确认）
- 默认模型：qwen3.6-plus（或 gpt-5.5）
- 技能路径：./.codex/skills（如有）
```

这样 Codex 后面生成代码、跑命令、解释问题时，会更贴合你的项目习惯。

AI 编码工具不是不会干活，它是不知道你的项目规则。 `AGENTS.md` 就是把规则先写清楚，省得每次都重新说明。

### 2\. 常用场景

Codex 不只是写代码，还能：

- • **代码重构** ，让它优化现有代码。
- • **写单元测试** ，给函数补测试用例。
- • **修复 Bug** ，把报错信息丢给它。
- • **代码审查** ，让它 review 你的代码。

### 3\. 安全模式

Codex 有几种常见权限模式，不同版本界面里的中文翻译可能略有差异，但核心思路差不多：

- • **默认权限** ，只给建议，适合你想先看方案。
- • **自动审查** ，可以自动编辑文件，但关键操作会请示你。
- • **完全访问** ，权限更大，可以自动执行更多操作。
![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/0a7df0afddcbe0af2abfbab3e4db341a_MD5.png)

**新手推荐配置** ：

- • 日常使用开"自动审查"模式。
- • 删除文件、安装依赖、推送代码必须手动确认。
- • 批量重构时，先让他制定方案，确认后再执行。

不要一开始就完全放权，等你熟悉了 Codex 的行为模式再逐步开放权限。

## 十一、接入国内大模型

国内很多平台提供了 OpenAI 兼容的 API，只要改一下配置和环境变量，就有机会让 Codex 使用国内模型。

但这里要先说清楚： **OpenA** **I 兼容不等于 Codex 一定可用** **。**

Codex 新版本更依赖 Responses API，如果平台只兼容 Chat Completions，可能会出现连得上但跑不起来的情况。

### 1\. 支持的平台

- • **通义千问** ，阿里系，稳定性好。
- • **硅基流动** ，聚合平台，模型多。
- • **智谱 AI** ，国产大模型，中文能力强。
- • 其他提供 OpenAI 兼容 API 的平台。

本次我们选择阿里百炼的大模型。

为什么选它？主要是它这边适配情况相对更好，折腾成本低一点。

### 2\. 配置方法

打开 App 的设置，进入配置文件进行修改。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/1065fa8c936c11eca087f88d5a182769_MD5.png)

将 `config.toml` 里面的配置改成下面内容：

```
model = "qwen3.6-plus"
model_provider = "bailian"

[model_providers.bailian]
name = "bailian"
env_key = "BAILIAN_API_KEY"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
```

然后在本地配置环境变量 `BAILIAN_API_KEY` ，具体步骤如下：

选中 `此电脑` ，点击 `右键` ，选择 `属性` 。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/d15edba5d63bc908eea572607b67feb7_MD5.png)

配置相关环境变量信息。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/a5b7f4848f0f7d126e243fdf1a397788_MD5.png)

然后重启 Codex，配置即可生效。

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/e1ac5e5a6704d3907b997d52df7a10b2_MD5.png)

### 3\. 验证国内模型是否生效

配置完成后，用这个简单任务测试一下：

```
用中文写一个 Python 脚本，打印"Hello 国内大模型"，然后运行它。
```

如果Codex能理解中文指令、生成代码、成功运行，说明配置生效了。

## 十二、常见问题

### 大家安装和使用Codex的过程中，未必是一帆风顺的，小灰在此列出几个Codex使用的常见问题和解决方案：

### 1\. Codex 登录失败

**问题表现：**

浏览器授权后回到终端，提示失败。

**解决方法** ：

1. 1\. 检查网络连接。
2. 2\. 清除浏览器缓存重试。
3. 3\. 换用 API Key 方式。
4. 4\. 执行 `codex logout` 后重新登录。

### 2\. codex 相关命令找不到

**问题表现：**

`提示错误 codex: command not found`

**解决方法** ：

```
# 重新安装
npm install -g @openai/codex

# 检查 npm 全局路径
npm config get prefix
```

确保 npm 全局路径在你的 PATH 里。

Windows 用户如果 PATH 配置很麻烦，建议先用 App，不要卡在 CLI 环境上。

### 3\. 接入国内模型时配置了环境变量，仍然提示找不到

**解决方法** ：

Windows 用户配置完环境变量后，需要重启 Codex（完全退出再打开），如果还不行，试试重启电脑。

注意：由于 Codex 新版本使用 Responses API，不支持 `wire_api = "chat"` 配置，很多大模型厂家的 API 还没适配，所以能选择的模型不多。

因此大家能跑就用，跑不起来就换平台。

其中阿里百炼支持 `Responses` 接口的模型如下：

```apache
qwen3-maxqwen3-max-2026-01-23qwen3.6-plusqwen3.6-plus-2026-04-02qwen3.5-plusqwen3.5-plus-2026-02-15qwen3.6-flashqwen3.6-flash-2026-04-16qwen3.5-flashqwen3.5-flash-2026-02-23qwen3.6-35b-a3bqwen3.5-397b-a17bqwen3.5-122b-a10bqwen3.5-27bqwen3.5-35b-a3bqwen-plusqwen-flashqwen3-coder-plusqwen3-coder-flashqwen3-coder-next
```

## 十三、写在最后

好了，以上我们介绍了Codex的基本概念、安装过程、使用方法、进阶应用等等。建议大家一边阅读，一边进行实操，这样可以加深印象。

如果你是第一次使用 Codex，建议不要一上来就让它”开发一个完整系统”，而是先拿真实小任务练手：修一个报错、给旧代码补注释、给函数补测试、把脚本改成命令行工具。

AI 编码工具最适合从小任务开始磨合。你越清楚自己要什么，它越容易给你稳定结果。

说到底，工具没有绝对的好坏，只有合不合适。真正重要的不是站队，而是把 AI 编码工具放进你的真实工作流里，让它帮你少写重复代码、少查低级错误。

正在阅读这篇文章的朋友，你有在使用 Codex 吗？，欢迎在留言区聊一聊你的体验。

< END >

最近小灰创建了一个AI副业交流群，对AI和副业变现感兴趣的朋友，都欢迎进群交流。扫码添加小灰微信，备注“ai“即可进群：

![图片](assets/Codex%20%E4%BF%9D%E5%A7%86%E7%BA%A7%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B%EF%BC%886000%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89/0831b9d142c9d3f2abc6443423d2758a_MD5.webp)

继续滑动看下一个

程序员小灰

向上滑动看下一个