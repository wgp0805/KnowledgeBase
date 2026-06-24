---
title: "同事：“Claude Code都能自动写代码了，还要什么Spec Coding？” 我反问：“屎山代码你来维护？”"
source: "https://mp.weixin.qq.com/s/Ck31lCgPFOikjlhGPHssWw"
---
苏三说技术 *2026年6月24日 08:20*

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)

> 让AI写代码，踩坑比上手快。写完能跑，但不一定符合你的需求。不是模型不够强大，而是你提供的规范不够。OpenSpec就是用来解决这个问题的：先和你探讨方案，然后出规范和计划，没问题它再写，今天就来聊聊它在项目中的实际使用！

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/120fc0032d790118e773ec1a67b88378_MD5.webp)

## OpenSpec简介与核心工作流

OpenSpec是一个面向AI编程的规范驱动框架，核心思想是"先对齐需求，再写代码"，目前在Github山已有 `53k+star` 。 每次功能变更会先生成提案、需求规格、技术设计和任务清单等规划文档，经人工确认后再让AI实现，让AI编程的结果更加符合预期。

OpenSpec核心的工作流主要包括如下：

- `/opsx:explore` ：进入探索模式，通过对话方式探讨需求，理清需求再动手。
- `/opsx:propose` ：生成规划制品，把需求写入规划文档，涵盖proposal+specs+design+tasks。
- [proposal.md：变更提案，为什么要做和做什么。](http://proposal.md：变更提案，为什么要做和做什么。)
	- pecs/ [spec.md：需求规格，用结构化格式描述具体需求和验收场景。](http://spec.md：需求规格，用结构化格式描述具体需求和验收场景。)
	- [design.md：技术设计，描述技术实现方案。](http://design.md：技术设计，描述技术实现方案。)
	- [tasks.md：任务清单，列出实现步骤。](http://tasks.md：任务清单，列出实现步骤。)
- `/opsx:apply` ：按按清单逐项实现，生成实际代码+tasks进度更新。
- `/opsx:archive` ：完成后归档存档，将规划文档移入archive目录。

下面是OpenSpec的工作流全景图，能清晰地描述流程及对应流程的产物。

![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/c9c0283ee8f4aabe6f0dc0b3be1f9b86_MD5.png)

## 安装及初始化

> 这里以OpenCode为例，介绍下OpenSpec的安装及初始化。

- 使用npm命令来安装OpenSpec非常简单，使用如下命令即可安装；
```
npm install -g @studyzy/openspec-cn@latest
```
- 安装完成后进入项目并初始化；
```
cd your-project
openspec-cn init --tools opencode
```
- 初始化完成后在项目中会创建 `openspec` 目录，用于存放规划制品，在OpenCode中还会添加 `opsx` 开头的命令；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/6fd1e8f0e46660244a3c1189e4eeb7a7_MD5.png)

- 如果想打开仪表盘查看OpenSpec的变更可以使用如下命令；
```
openspec-cn view
```
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/150c1a3a921689dd88f0bdff03eaef11_MD5.png)

## 使用

> 这里以开发一个前后端分离的博客网站为例，介绍下OpenSpec的使用。

- 使用OpenSpec的第一步，通过 `/opsx-explore` 命令进入探索模式，主要是通过纯对话的方式来理清需求；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/19f821de5d83d48cc37281f125745bad_MD5.png)

- 当我们提出需求后，OpenSpec会抛出几个问题，帮助我们确认项目需求的基本方向；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/788d6b30fb8cefd2378c300acf6ac873_MD5.png)

- 基本方向确定好后，OpenSpec会给我们提供3个技术方案供我们选择；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/7968aa25c7619506a68b93bca1fd1b15_MD5.png)

- 针对我们选择的技术方案，OpenSpec会提出几个关键设计点让我们选择；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/c67582016886a3944062d24a5ac3f474_MD5.png)

- 之后OpenSpec会设计好数据模型供我们确认；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/acce3340842d16327888168a04b2f85e_MD5.png)

- 然后是几个自然浮现的话题；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/90f143f6804ae4500e84fe6eed2f225b_MD5.png)

- 接下来是一些实现维度方面的问题；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/648be829a95de9c3c92069ac2d55a1a6_MD5.png)

- 还有一些实现细节方面的问题；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/0c2ea9ca2cbc06a66026ecb5cbce64d4_MD5.png)

- 整个项目需求和技术方案都探讨的差不多了，OpenSpec会把项目的全貌发给我们看下；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/8e03ff1c1d48d7e353188c817cca5487_MD5.png)

- 看了下没什么问题了，就可用 `opsx-propose` 命令生成规范制品了；
```
/opsx-propose init-project
```
- 我这里的博客网站生成的规划制品如下；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/1713069acd652e2aa1fad792fd38f5dc_MD5.png)

- 接下来就可以使用 `/opsx-apply` 命令开始执行任务了；
```
/opsx-apply init-blog-platform
```
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/fb09ebdb75a928e6e277e0f6c7d5691a_MD5.png)

- 任务完成会输出任务完成总览；
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/970be466b01bed09bcb0c9325f3f814a_MD5.png)

- 最后通过 `/opsx-archive` 命令来完成归档，此时之前生成的规划文档将移入archive目录。
![图片](assets/%E5%90%8C%E4%BA%8B%EF%BC%9A%E2%80%9CClaude%20Code%E9%83%BD%E8%83%BD%E8%87%AA%E5%8A%A8%E5%86%99%E4%BB%A3%E7%A0%81%E4%BA%86%EF%BC%8C%E8%BF%98%E8%A6%81%E4%BB%80%E4%B9%88Spec%20Coding%EF%BC%9F%E2%80%9D%20%E6%88%91%E5%8F%8D%E9%97%AE%EF%BC%9A%E2%80%9C%E5%B1%8E%E5%B1%B1%E4%BB%A3%E7%A0%81%E4%BD%A0%E6%9D%A5%E7%BB%B4%E6%8A%A4%EF%BC%9F%E2%80%9D/f966a3990537ca5274e59c463a76ac3b_MD5.png)

## 总结

今天以博客网站的开发为例，给大家介绍了OpenSpec中核心工作流的使用，从需求探讨->规划文档生成->执行编码->归档。

整体而言，OpenSpc只是增加了一层轻量的规范（spec）机制，让AI编程的结果更可控、更贴合项目实际，感兴趣的小伙伴可以尝试下它。

## 项目地址

- 原版： [https://github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- 中文版： [https://github.com/studyzy/OpenSpec-cn](https://github.com/studyzy/OpenSpec-cn)

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)