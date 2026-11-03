---
title: "一个窗口同时跑 Codex、Claude、Cursor ，还能互相派活，这个 GitHub 项目火了！！"
source: "https://mp.weixin.qq.com/s/LozQtFCJqRYYrUpf5qzsfw"
author:
  - "[[冰v河]]"
published:
created: 2026-11-03
description: "这个Codex、Claude、Cursor ，还能互相派活的开源项目真的很好用！！\x0d\x0ahttps://binghe.site"
tags:
  - "clippings"
---
冰v河 冰河技术 *2026年11月3日 07:45*

**大家好，我是冰河~~**

同时用几个 AI 编程工具的人，大多经历过窗口管理的麻烦：Codex 开一个终端，Claude Code 开另一个，Cursor CLI 再开一个，彼此之间不通气，会话一关，之前的记录就散了。

想让一个 agent 把查到的资料交给另一个继续处理，只能靠手动复制粘贴。OpenBot 想解决的就是这个割裂状态。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mciaHGibPzCIR9v1B2ZYznSR1ejMDib1wMvyw71cFLla3XiaDGvY88ydaQRItKMdUNJr7RLQGbBHSPAGicI8UL9eGcXIHc3OKIoNkn77xGKQXnLA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 它不提供模型，只负责调度本机已有的 CLI

OpenBot 是一个桌面应用，本身不带模型。它调用的是你本地已经登录好的命令行工具，然后把每个 agent 配置成独立角色：名字、头像、指令、工作目录、对话记录都分开保存。应用关掉再打开，这些信息还在。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mciaHGibPzCIRpYX6X8OUxaH4PXYx7RMtPI0DntBwT7IKNpsUwVTdiaor3NlAqW3BicCpVvvQpPdrN3DiaHniafWrwLUFeXia17X8c35o1UfbebLWY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

原生支持的是 Codex 和 Claude Code；Grok CLI、OpenCode、Gemini、Cursor CLI、Cline CLI 通过 ACP 协议接入。

如果本机跑着 Ollama 或 LM Studio，启动时能自动识别，本地模型也可以直接用。

模型是按 agent 单独设置的，推理档位、供应商都可以不同。用了一半想换供应商，比如从 Codex 切到 Claude Code，工作区和之前的对话会保留，不用从头再来。

## 工作区和持久化：agent 能攒下东西

每个 agent 的文件放在 `~/OpenBot/Agents/<agent-id>` 下，需要共享的文件走 `~/OpenBot/Shared` ，传输时带清单和校验值。对话和任务队列存在本地 SQLite 数据库里。这样 agent 就有记忆的载体：之前聊过什么、改过哪些文件，重开应用还能接着来。

任务队列是先进先出，可以暂停、恢复、取消。应用崩溃后重开，队列不会丢。agent 正在处理上一条消息时，新消息会排在后面按顺序处理。

## agent 之间可以直接对话

普通终端窗口做不到的一点是：两个 agent 之间能直接发消息，还能回表情、传文件。一个 agent 查完资料，可以直接把结果发给负责写代码的agent，不需要人在中间转手。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mciaHGibPzCISJsnIM4QeicUL18OHRz17lgYIWdiay6UawD0QIs7xaQXlLkmbHicmPY3AyuBXJNUQebzkHsTjwcOQj8OqXdVKvDvODHyuCoNGT3A/640?wx_fmt=png&from=appmsg#imgIndex=2)

频道（Channel）相当于多个 agent 的公共聊天区。一个任务同一时间只有一个负责人，可以指定交给谁，界面上有 Stop、Resume、Reassign、Archive 这些操作。查资料、写稿、校对分给不同 agent，放进一个频道里就能跑起来。

## 附加能力：浏览器、Computer Use、上下文压缩和技能库

应用内置一个浏览器，agent 可以在里面开网页、看内容、操作页面。另外有一个可选的 Computer Use 功能，macOS、Windows、Linux 都支持，驱动随安装包一起走，不用单独装。macOS 上需要授予屏幕录制和辅助功能两个权限。

对话快到模型上下文上限时，应用会自动压缩，不需要手动清理。agent 还可以把常用流程存成 skill，放进本地技能库，其他 agent 也能安装使用。

## 手机端和服务器模式

iPhone 和 Android 都有客户端，连的是你自己电脑上跑的 OpenBot，所以电脑得开着。如果想让它一直在线，可以装到一台常开的服务器上，官方提供了一键脚本和 Docker 镜像，之后用手机或网页端连上去。

## 用之前需要知道的三件事

**权限放得很大。** 项目目前还是开发预览版，agent 跑在 `danger-full-access` 模式下，第一次启动同意之后，读写文件、执行命令、上网、操作浏览器都不会再逐项询问。比较稳妥的做法是先装在备用机、虚拟机或 Docker 里用一段时间，不要直接上主力机。

**许可证有边界。** 用的是 PolyForm Noncommercial 1.0.0，个人和非商用免费，商用需要另外购买授权。0.1.11 之前的旧版本是 [Apache-2.0。公司如果打算用于工作，这一点要先确认清楚。](http://apache-2.0.xn--,-0n6aqrs0am4ebg22oezn21j77khtoe7e39r02ijkrklmy6md64d9qij1v./)

**本地优先不等于完全离线。** 数据存在你自己机器上，但只要 agent 用的是云端模型，对话内容仍然会发给 OpenAI、Anthropic、xAI 这些厂商。想彻底不联网，就得接 Ollama 这类本地模型。

如果你本来就订着 ChatGPT、Claude、Gemini、Grok 里的一两家，平时又经常同时开几个 agent，可以装一个试试；OpenCode 还有不用登录的免费模型可用。如果需要关掉电脑也能跑的云端方案，或者公司对审计、沙箱有硬性要求，先观望一段时间更合适。

开源地址： [https://github.com/nightly-labs/openbot](https://github.com/nightly-labs/openbot)

**好了，今天就到这儿吧，我是冰河，我们下期见~~**

推荐阅读：

[给大家推荐一款AI短剧生成平台](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515806&idx=1&sn=6214e0ec2a9ebc09b1c68eb23e818eae&scene=21#wechat_redirect)

[给大家推荐一款可直接使用的AI-CR系统](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515790&idx=1&sn=5aeda9e93df686b5e753cb9870fda0da&scene=21#wechat_redirect)

**微信扫一扫赞赏作者**

AI开源合集 · 目录

阅读原文