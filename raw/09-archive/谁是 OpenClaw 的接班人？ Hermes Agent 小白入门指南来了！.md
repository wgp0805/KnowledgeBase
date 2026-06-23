---
title: "谁是 OpenClaw 的接班人？ Hermes Agent 小白入门指南来了！"
source: "https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653263064&idx=1&sn=cabdd84cc7f6f26507473c1dc654d4b7&scene=21&poc_token=HIbWOWqjkCQd2F3tPv6pGLS8Sv-3xIwCjgL7TJkN"
---
小灰 & 阿咕噜 程序员小灰 *2026年4月20日 19:46*

大家好，我是程序员小灰。

不知道有谁还记得，今年第一季度爆火的小龙虾（OpenClaw）项目？

不可否认，小龙虾依然是一款强大的智能体工具，但由于存在种种弊端，它最终淡出了多数人的视野。

就在这个时候，有一个全新的AI智能体框架在AI圈爆火了，这个AI智能体框架名为Hermes Agent，被国内玩家称为“爱马仕”。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/6131eb3527815e0e59d9862c236a5bc1_MD5.webp)

许多人在后台问小灰，能不能出一篇关于Hermes Agent的教程，于是经过三天三夜的奋战，终于有了这篇长达7000字的教程。

建议大家先收藏、不迷路。

## 一、什么是Hermes？什么是Hermes Agent？

1.什么是Hermes？

在学习Hermes Agent之前，我们先来了解一下Hermes到底是什么。

Hermes是一个AI大模型，由开源模型圈大名鼎鼎的实验室 **Nous Research** 所开发。

它的名字取自希腊神话中的众神使者赫尔墨斯，背后的寓意是“信息的传递者”。

2\. 什么是Hermes Agent？

说完了Hermes，那Hermes Agent又是什么呢？

Hermes Agent是 **Nous Research基于Hermes模型，研发的一套AI智能体框架。**

你可能用过 Cursor、Copilot 这类 AI 编程助手，也用过 ChatGPT、Claude 这种聊天机器人。但它们都有个共同的硬伤： **关掉窗口，它们就停工了。** 你想让 AI 半夜帮你跑个脚本？不行，你得自己开着电脑。

然而Hermes Agent不一样。它不是一个插件，也不是一个网页，它是一个 **部署在你服务器上的 AI 分身。**

它可以实现 7x24 小时待命，你随时通过飞书、微信给它下指令，它帮你跑脚本、查日志、处理数据，然后把结果发回。

3\. Hermes Agent 适合哪些人？

那么，Hermes Agent适合哪些人来使用呢？目前该工具主要适合下面这四类人。

独立开发者：

让 Hermes 在服务器上 24 小时待命，随时通过 Telegram 下达任务。跑脚本、查日志、处理数据，不用开电脑。

小团队：

通过 飞书/微信 共享一个 Hermes Agent，处理运维监控、自动化任务，一人配置全员可用。

自动化爱好者：

用 cron 定时执行任务，用消息网关接收结果通知。比如每天早上自动生成市场日报，推送到微信。

重视隐私的用户：

完全本地部署，数据不离开你的服务器。可以选择本地模型，不依赖任何云端服务。

二、Hermes Agent与 OpenClaw 的区别

说完了Hermes Agent 的基本概念，或许会有朋友问：“Hermes Agent 和OpenClaw的作用听起来似乎差不多？两者到底有什么不同呢？”

**1\. 记忆：小龙虾像金鱼，爱马仕像老友**

龙虾每次新对话就像失忆，你上周刚说过「用 Python 3.11」，今天它又给你写 3.12，你得反复教。Hermes Agent 会把你的偏好永久记下来，重启也不会忘，甚至能回忆起几周前你们讨论过的方案细节。

**2.技能：小龙虾靠手动装， **爱马仕** 靠自己学**

龙虾的技能生态丰富，但每个都要自己找、自己装、自己配，折腾半天。Hermes 走了另一条路——它干完一个复杂活，会在后台自动复盘，把解决过程提炼成一个可复用的技能文件，下次遇到类似任务直接调用。

比如它帮你调了一个 Bug，下次遇到同类 Bug 直接按套路来，不用你再教。你当然也可以主动让它存技能：“把刚才的数据清洗流程保存为 Skill”。

**3.隐私：小龙虾过云端，爱马仕守本地**

龙虾的不少 Skill 依赖第三方云端，你的数据要过别人的服务器。Hermes 完全跑在你自己的机器上，想用本地模型也行，数据一步都不出去。

**4.安全审批：小龙虾看不懂，爱马仕更聪明**

龙虾的授权弹窗经常是一串不明所以的数字和路径，你不清楚它到底要干什么，只能无脑批准。Hermes Agent 会智能判断指令风险等级，高危操作主动预警，低风险操作静默通过，审批体验更省心。

Hermes Agent与OpenClaw的异同，可以归纳为下面这张表：

|  | 小龙虾（OpenClaw） | 爱马仕  （Hermes Agent） |
| --- | --- | --- |
| 定位 | 多平台集成 + 庞大生态 | 自我进化 + 深度记忆 |
| 技能 | 手动安装，生态丰富 | 自动学习，越用越多 |
| 记忆 | 跨会话容易健忘 | 永久记住你的偏好 |
| 隐私 | 部分依赖云端 | 完全本地，数据不外泄 |
| 安全 | 授权看不懂，只能无脑批准 | 智能判断风险，高危预警，低风险静默 |
| 风格 | 万能工具箱 | 越用越聪明的专属分身 |

**总之，我们可以把小龙虾理解为“** 你问它答”的工具箱，是一只勤奋的“打工虾”；而爱马仕则是“教一次、记一辈子”的聪明员工，也是你的专属分身。

很多人现在两者并用，小龙虾负责执行（现成 Skill 多），爱马仕当大脑（越来越懂你）。

如果你之前养过虾，那么这里有一个好消息：借助下面的指令一键导入小龙虾的记忆、Skill、配置、API Key，可以让爱马仕实现“无痛迁移”。

```
hermes claw migrate
```

---

## 三、准备篇：安装前需要什么

### 1\. 系统要求

Hermes Agent 支持以下环境：

- Linux
- macOS
- Windows （官方建议安装 WSL2）
- Android / Termux（这个后面再说，先把PC端的玩明白）

注意：Windows 环境目前问题还比较多，如果你用的是 Windows，建议安装 WSL2（Windows Subsystem for Linux）。安装方法很简单，在 PowerShell 里运行：

```
wsl --install
```

重启电脑后，你就有了一个 Linux 环境。

安装 Hermes Agent 前只需要一个前提条件： **Git。** 大多数系统已经自带了，如果没有，用以下命令安装：

```
# Linux/WSL2
sudo apt install git

# macOS
brew install git

# Windows
# 官网下载：https://git-scm.com/download/win
# 全部默认，一路 Next。
```

### 2\. 你需要准备的东西

开始安装前，准备好以下材料：

**一台可以运行的电脑：** 可以是你的本地电脑，也可以是一台云服务器/VPS。如果你想要 7x24小时待命，建议用服务器部署。

**API Key：** 大模型API Key。推荐看我之前的一篇大模型白嫖指南，有大量免费模型可用，白嫖入门最方便。

**飞书/微信：** 在 飞书 或 微信 里和 Hermes Agent 聊天，需要申请一个 Bot。

---

## 四、安装篇：一条命令搞定

### 1\. 一键安装命令

Hermes Agent 提供了自动安装脚本，会帮你搞定所有依赖（uv、Python 、Node.js 、ripgrep、ffmpeg），你只需要运行一条命令。

**Mac / Linux / WSL2 环境：**

打开终端，输入以下命令后回车：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```
![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/940f76632c5cd73abdf2b18a9a1829bc_MD5.png)

注意：由于网络问题，有可能下载到99%的时候就失败了，别灰心，可以多重试几次。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/3fddd809ccaa2d31b1cc26f86f5d9691_MD5.png)

根据我的测试，在国内的网络环境下，耗时最长可能在2-3个小时。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/74235364b3041b42022b8f9c2f6ce0ba_MD5.png)

看到这种界面你就离成功不远了！

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/bafde8e93e57f30054cf6672c795d9b1_MD5.png)

到这儿，你就成功了！！！

---

**Windows PowerShell 环境** （如果你坚持用原生 Windows）：

```
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex

# 或者下载脚本后执行
.\install.ps1 -NoVenv -SkipSetup
```

耐心等待（愚公移山那种耐心），脚本会自动下载并安装所有依赖：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/16e4e9bcb9bf5418972a652faf286f56_MD5.png)

整个过程大概几十分钟吧，取决于你的网络速度。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/2dc64a52ac8037644a91da5d0adb019a_MD5.png)

到这里基本上就已经安装成功了。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/22ced00199be9c7a577c69637b241937_MD5.png)

### 2\. 安装后操作

一般不用，如果发现 `hermes` 命令无效可以使用下面方法

重新加载一下 shell 配置，让 `hermes` 命令生效：

```
source ~/.bashrc    # 如果你用的是 bash

source ~/.zshrc     # 如果你用的是 zsh
```

然后验证一下安装是否成功：

```
hermes version
```

如果看到版本号输出，说明安装成功。

### 3\. 手动安装方式（可选）

如果你想自己控制安装过程，或者想固定某个版本，可以用手动安装，手动安装之前需要安装好 **Python 3.11** 和 **Node.js v22**

```
# 克隆项目
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git

# 如果发现自己文件夹内容少了
git submodule update --init --recursive

# 然后进入目录
cd hermes-agent
```
![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/51b67237e21ebc928bd23ddf5ea967bf_MD5.png)
```
# 安装核心组件pip install -e "."
```
![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/7c42542fec6bde6852e94148d0b96645_MD5.png)

安装完成后执行 `hermes version，` 验证是否安装成功

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/c98652229089976a3bc7dd1fbde6ac9c_MD5.png)

手动安装和自动安装的用法完全一样，适合想改源码或研究内部实现的同学。

---

## 五、配置篇：第一次启动

### 1\. 运行配置向导

安装好后，一般会自动弹出配置向导，如没有出现可以执行下面命令，它会一步步带你完成所有设置：

```
hermes setup
```

你会看到一个交互式界面，有几个选项：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/bafde8e93e57f30054cf6672c795d9b1_MD5.png)

选择 **Quick setup，** 这是最简单的配置方式。

### 2\. 选择模型提供商

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/7b9a4a3187786cf3e0498e7fb80a4739_MD5.png)

我还是比较钟爱智谱，选择 **Z.AI，** 然后填入API Key

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/a629c5363f4e8f8724f57e75c00e7d96_MD5.png)

注意，这里有个坑，粘贴 Key 后不会显示任何内容，也不会提示；我之前就是以为没粘贴进去在这捣鼓半天。。。

### 3\. 选择默认模型

智谱免费赠送的 Token，一般仅适用于 glm-4.5-air 模型。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/50f398436e8ec309d64916099978d021_MD5.png)

### 4\. 配置消息平台（可选）

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/ee42cede41923461ebcbd6beef949502_MD5.png)

选择 **Set up messaging now，** 然后选择你要接入的平台（比如 feishu）：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/ed40c8087bb655a74e07f5fe1eeb8316_MD5.png)

选择扫码创建机器人：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/07b76504f8a98c1a5cfcc424d8a6daba_MD5.png)

扫码：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/34ed7ea4d28cbef0d204963000fd38d6_MD5.png)

可以选择创建新的机器人，也可以选择之前玩龙虾的时候创建的机器人

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/3b65dadf5842c664e2fdf8921af7aa36_MD5.jpg)

接下来配置 **authorized** ，选择 **Allow all direct messages：**

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/eb289158580487717d50cc9fef9038e1_MD5.png)

保持默认配置：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/9a880b6074c68813d63a46bc0a5f78fe_MD5.png)

这里直接回车就行：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/b7c53daf35ca328f4fc0f1eceea7d684_MD5.png)

开启服务，输入 **Y：**

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/d8f0316605f513250ad284b390a0c055_MD5.png)

还是输入 **Y，** 开启对话：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/a639f2b82a26eb73dbd6e33d601956f3_MD5.png)

开始愉快的聊天吧！

---

## 六、启动篇：验证安装成功

### 1\. 启动 Hermes Agent

配置完成后，直接运行下面命令就可以打开聊天界面：

```
hermes
```

你会看到 Hermes Agent的欢迎界面：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/354f2f84f1d0688ebf38df89724cb4a3_MD5.png)

这说明一切正常，Hermes Agent已经在运行了。

你现在可以在终端里和它对话了。

如果你想继续上次的对话，可以用：

```
hermes -c
```

这会加载上次会话的上下文，保持记忆连贯。

### 2\. 验证安装

Hermes Agent 提供了诊断命令：

```
hermes doctor
```

这会做一个全面健康检查，检查配置、依赖、连接等是否正常。如果没有明显报错，说明安装成功。

```
hermes version
```

查看当前版本号。

### 3\. 测试飞书

打开飞书，找到你的机器人，发一条消息：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/ceeed6ffe58c9f0d3ffff71da0349e48_MD5.jpg)

如果收到回复，说明消息网关工作正常。现在你可以从任何地方远程指挥 Hermes 干活了。

---

## 七、基础使用篇

### 1\. Web UI

在终端输入 `hermes dashboard` 就可以打开Web UI

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/961ea4e56168ddd260f43a4b3c0e343a_MD5.png)

不过我不太建议使用，官方 UI 体验较差。

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/55f554a3850bc21f2f029c04dbf75b75_MD5.png)

这里我推荐一个还比较好看的Web UI

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/cb94c155a477975b51d0dda11787cf4d_MD5.png)

**安装步骤：**

```
# 第一种方式
npm install -g hermes-web-ui

# 第二种方式
bash <(curl -fsSL https://cdn.jsdelivr.net/gh/EKKOLearnAI/hermes-web-ui@main/scripts/setup.sh)

# 启动
hermes-web-ui start
```
![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/100fcccad6a3bc3ca09a50f98bbb460e_MD5.png)

复制日志中的URL链接到浏览器即可打开。

**注意：** 这里可能会有一个坑，就是你安装完成后，输入 `hermes-web-ui start` 它会提示 `hermes-web-ui：未找到命令，` 这是因为环境变量未配置好，采用如下方式可以修复：

```
# 找到npm路径
NPM_BIN=$(npm config get prefix)/bin

# 配置环境变量
echo "export PATH=$NPM_BIN:\$PATH" >> /root/.bashrc

# 激活配置
source /root/.bashrc
```

Github地址：https://github.com/EKKOLearnAI/hermes-web-ui

**相关命令速查表**

| 命令 | 说明 |
| --- | --- |
| `hermes-web-ui start` | 后台启动（守护进程模式） |
| `hermes-web-ui start --port 9000` | 自定义端口启动 |
| `hermes-web-ui stop` | 停止后台进程 |
| `hermes-web-ui restart` | 重启后台进程 |
| `hermes-web-ui status` | 查看运行状态 |
| `hermes-web-ui update` | 更新到最新版本并重启 |
| `hermes-web-ui -v` | 显示版本号 |
| `hermes-web-ui -h` | 显示帮助信息 |

### 2\. 核心命令一览

| 命令 | 说明 |
| --- | --- |
| `hermes` | 启动交互式聊天 |
| `hermes chat -q "消息"` | 单次提问直接返回结果 |
| `hermes -c` | 恢复最近会话 |
| `hermes -c "会话名"` | 恢复指定名称会话 |
| `hermes setup` | 初始化配置向导 |
| `hermes model` | 选择默认模型 |
| `hermes config` | 查看 / 编辑配置 |
| `hermes login` | 登录模型服务商 |
| `hermes logout` | 登出清除认证 |
| `hermes status` | 查看组件运行状态 |
| `hermes logs` | 查看最近日志 |
| `hermes logs -f` | 实时跟踪日志 |
| `hermes sessions list` | 列出历史会话 |
| `hermes skills` | 管理技能 |
| `hermes update` | 更新 Hermes |
| `hermes backup` | 备份配置数据 |
| `hermes dashboard` | 启动 Web 面板 |
| `hermes doctor` | 检查依赖与配置问题 |
| `hermes claw migrate` | 从openclaw一键迁移 |

### 3\. 对话界面内的斜杠命令

进入对话后，输入 `/` 可以看到所有可用命令：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/852214742dfd18645fa477fa5a28d90d_MD5.png)

常用命令包括：

- `/help：`
	查看帮助
- `/skills：`
	查看技能列表
- `/model：`
	切换模型
- `/clear：`
	清空当前对话

### 4\. 多行输入与中断任务

**多行输入：** 按 `Ctrl+Enter` 可以换行，输入多行内容。

**中断任务：** 如果 Hermes Agent 正在执行一个任务，你想让它停下来，直接输入新消息按回车就行，它会中断当前任务响应你的新输入。

---

## 八、进阶篇：让它更懂你

### 1\. 灵魂定义（SOUL.md）

默认的 Hermes Agent 是一个通用 AI 助手，你可以通过 SOUL.md 文件定义它的"人格"，让它更符合你的喜好。

SOUL.md 的位置： `~/.hermes/SOUL.md`

这是一个纯文本文件，你可以直接编辑。示例模板：

```
---
name: 务实工程师
---

# 思考模式
- 先验证后回答：不确定的事先查工具确认，不靠猜测
- 先计划后执行：复杂任务先列方案，确认再动手
- 交付即验证：做完一件事，主动给出验证方法

# 输出风格
- 结论先行，代码为主，少废话
- 高危操作必须预警

# 避免
- 谄媚
- 炒作用语
```

你可以让 Hermes Agent 帮你写 SOUL.md：

```
帮我编辑 ~/.hermes/SOUL.md，定义你的风格：直接高效、不说废话、敢于反驳
```

或者让他从你的龙虾里面提取：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/65a2af950d566c4634bbcd67a7b744a4_MD5.png)

### 2\. 记忆系统简介

Hermes Agent 的记忆系统有三层：

**第一层：内置记忆（默认开启）**

- `MEMORY.md：`
	Agent 的工作笔记，记录环境事实、项目惯例、踩过的坑
- `USER.md：`
	你的画像，记录偏好、沟通风格、工作习惯

这两个文件在每次会话开始时会自动注入到上下文，确保 Agent "认识你"。

**第二层：历史会话搜索**

所有历史对话都保存在 SQLite 数据库里，支持全文搜索。当 Agent 需要回忆几周前的讨论，它会搜索历史记录，精准找回相关内容。

```
~/.hermes/state.db (SQLite) 
    ├── sessions — 会话元数据、Token 统计、计费信息 
    ├── messages — 单会话完整消息历史记录 
    ├── messages_fts — 用于全文检索的 FTS5 虚拟表 
    └── schema_version — 单行表，用于跟踪数据库迁移版本
```

**第三层：外部记忆插件（可选）**

支持 Mem0、Supermemory 等外部记忆服务，提供更强大的语义搜索和知识图谱能力。

**怎么让 Hermes Agent 记住你的偏好？**

直接明确告诉它：

```
记住我的偏好：所有 Python 代码统一用 Python 3.11，不要用 Python 3.12
```

这样更容易触发记忆写入。你也可以主动请求：

```
把这个偏好写入你的长期记忆
```

### 3\. 技能自我进化

这是 Hermes Agent 最有想象力的设计。

当 Hermes Agent 完成一个复杂任务（比如调试一个 bug、搭建一个工作流），它会把解决过程提炼成一个可复用的技能文件，保存在 `~/.hermes/skills/` 目录。

下次遇到类似问题，它会直接调用这个技能，不用从头摸索。

你也可以主动引导它创建技能：

```
把刚才的数据处理流程保存为一个 Skill，命名为 data-pipeline
```

查看已有的技能：

```
hermes skills list
```

或者在对话里输入 `/skills。`

---

## 九、常见问题与排错

### 1\. API Key 配置问题

解决方案：打开 `~/.hermes/.env` 文件，检查里面的 API Key 是否正确。如果有多余字符或格式问题，手动修正。

### 2\. 飞书发消息无响应

最常见的原因就是下图中没有选择 `Allow all direct messages`

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/eb289158580487717d50cc9fef9038e1_MD5.png)

解决方案：将 `~/.hermes/.env` 里面的属性 `FEISHU_ALLOW_ALL_USERS` 设置为 `true`

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/b5298c52ac3842219d3a8dfe08928089_MD5.png)

### 3\. 输入 hermes 提示命令找不到

shell 配置没有加载

解决方案：

```
source ~/.bashrc

# 或 
source ~/.zshrc
```

如果还是不行，检查 Hermes Agent 是否正确安装在 PATH 里。

### 4\. 输入内容填写错误想删除，却发现无法删除？

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/84defde6ff3a8dd3b93cfbe03f72792e_MD5.png)

这也是一个坑，我被坑的次数最多，是因为键盘不兼容引起的，按 `ctrl + del` 就可以删除了

---

## 十、写在最后

好了，以上我们介绍了 Hermes Agent 的基本概念、安装方式以及使用技巧。

这篇文章比较长，建议大家收藏下来，一步一步进行实操，慢慢消化吸收。

同时，如果大家希望对 Hermes Agent 有更深入的了解，也推荐大家看一看 Hermes Agent 的官方文档、Github源码，以及技能市场。

官方文档：

hermes-agent.nousresearch.com/docs

GitHub 仓库：

github.com/NousResearch/hermes-agent

技能市场：

hermes-agent.nousresearch.com/docs/skills

现如今，AI已经彻底颠覆了我们的工作和生活方式，希望大家都能把这款强大的AI工具用起来，一起抓住AI时代的红利！

< END >

最近小灰创建了一个AI副业交流群，对AI和副业变现感兴趣的朋友，都欢迎进群交流。扫码添加小灰微信，备注“ai“即可进群：

![图片](assets/%E8%B0%81%E6%98%AF%20OpenClaw%20%E7%9A%84%E6%8E%A5%E7%8F%AD%E4%BA%BA%EF%BC%9F%20Hermes%20Agent%20%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97%E6%9D%A5%E4%BA%86%EF%BC%81/0831b9d142c9d3f2abc6443423d2758a_MD5.webp)

继续滑动看下一个

程序员小灰

向上滑动看下一个