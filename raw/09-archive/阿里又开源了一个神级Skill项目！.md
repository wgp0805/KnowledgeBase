---
title: "阿里又开源了一个神级Skill项目！"
source: "https://mp.weixin.qq.com/s/cTefF32girOuUn-A94L-Vg"
---
我是程序汪 *2026年8月14日 09:07*

> 用 Claude Code 这类 AI 编程智能体写代码很顺手，但遇到生成图片、视频、语音这些多模态需求，还得切出去手动操作，体验相当割裂。最近发现阿里开源的 qianwen-ai，它把 QianWen 的全套 AI 能力直接集成到了 Agent 里，体验下来确实是个神级 Skill 项目！

## 简介

qianwen-ai 是阿里开源的一套 Agent 原生多模态 AI 技能包，它把文本、图像、视频、语音、视觉理解等 8 个技能打包成了标准的 Agent Skills，可以直接接入 Claude Code 等支持 Agent Skills 的 AI 编程智能体。它主要有如下亮点：

- `Agent 原生` ：Agent 帮你选模型、调参数、处理报错，你只管提需求；
- `一行安装` ：一条命令装完即用，零配置，无需对接 SDK；
- `技能齐全` ：文本、图像、视频、语音、视觉、模型选择、认证、用量查询，8 个技能全部内置；
- `适配广泛` ：可接入多种支持 Agent Skills 的 Agent，即装即用。

## 安装

- qianwen-ai 的 skill 安装非常简单，首先需要确保已经安装了 `             Node.js            18` 以上版本，然后使用如下命令安装；
```
npx skills add QianWen-AI/qianwen-ai
```
- 出现技能选择提示时用空格选择、回车安装即可；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/c3a1366abdc5e98e057a9a72c9558e19_MD5.png)

- 安装过程中可以选择安装到哪个 AI 编程智能体，我这里选择的是 Claude Code；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/1866371df43a7e643b220962ae09700a_MD5.png)

- 安装完成后输入 `/qianwen` 开头，就会提示对应的 skill 命令了；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/384a02fc8dc634790c3be297443fd758_MD5.png)

- 每个 skill 的具体作用可以参考下表。
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/075add5160c44f917d629fd107b8f9c4_MD5.png)

## 使用

> 接下来挑几个常用的 skill 实测一下它们的作用。

- 第一步我们需要使用 `/qianwen-ops-auth` 命令来进行 QianWen API 的认证配置，如果不配置的话是无法使用 qianwen-ai 的一系列 skill 的，具体使用说明如下；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/10d06f38862a10765eeee8157108c967_MD5.png)

- 这个 skill 实际上就是在你的工作目录里创建一个 `.env` 配置文件，在里面添加你自己的 API KEY 即可，API KEY 可以到千问 AI 平台上创建获取，需要注意的是这里要配置 `sk-xxxxx` 开头的 KEY；
```
DASHSCOPE_API_KEY=sk-your-key-here
```
- 这里测试下它的 `图片生成` 功能（对应 `/qianwen-image-generation` ），输入提示词 `画一条青色的龙做吉祥物` ，这里 qianwen-ai 将会自动选择图片生成模型 `              wan2.6-t2i            ` 来生成图片，最后生成图片如下；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/13732415e4cfc8010d835f4f566f5931_MD5.png)

- 我的 Claude Code 目前设置的模型是不支持图片识别的，但是装了这个 skill 以后，就能通过 `/qianwen-vision` 这个 skill 来识别图片；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/16fb2bf05720b7e2deace88112a4eebe_MD5.png)

- 然后再测试下 `语音` 功能（对应 `/qianwen-audio-tts` ），让它用温暖女声朗读《上学歌》，它会自动调用 `qwen3-tts-instruct-flash` 模型来生成；
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/041bd5ed67dac598e9b56eb2c98dba4d_MD5.png)

- 最后测试下 `视频` 功能（对应 `/qianwen-video-generation` ），让它生成一个 5 秒的孙悟空三打白骨精动画，它会调用 `              wan2.6-t2v            ` 模型来生成视频。
![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/059035da58b971654ef0bddf81845d2a_MD5.png)

## 总结

qianwen-ai 让你只需在对话框里说一句需求，Agent 就会自动选择合适的模型完成图片、视频、语音等多模态任务，全程无需关心 API 调用细节。对于模型本身不支持图片识别的场景，装上 `/qianwen-vision` 后还能直接补齐短板。如果你也在用支持 Agent Skills 的 AI 编程智能体，不妨花一分钟装上试试！

## 项目地址

[https://github.com/QianWen-AI/qianwen-ai](https://github.com/QianWen-AI/qianwen-ai)

![图片](assets/%E9%98%BF%E9%87%8C%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%E9%A1%B9%E7%9B%AE%EF%BC%81/6fbf395625d014d585c0686474a9ebb1_MD5.gif)