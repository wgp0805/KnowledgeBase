---
title: "RuoYi 全栈 AI 平台开源了（若依）。"
source: "https://mp.weixin.qq.com/s/eYOBUK7tDiXuiixsRXipKw"
---
沉默王二 沉默王二 *2026年2月25日 14:04*

大家好，我是二哥呀。

提起若依，大家都不陌生。很多二开的项目都是基于 RuoYi-Vue-Plus 这个版本开发的。

二哥之前的 OA 流项目 [PmHub](https://mp.weixin.qq.com/s?__biz=MzUxNzAzMTU4OQ==&mid=2247485586&idx=1&sn=7c4d593474b095762d80320e916cd2aa&scene=21#wechat_redirect) 就用到了若依的权限管理模块，省了不少事。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/e1a7a48d88d04ff6e22b54086fac3d7a_MD5.webp)

今天给大家分享的这个 RuoYi AI，是在 RuoYi-Vue-Plus 基础上扩展了 AI 功能的开源项目。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/582f69ef9d525d231f4afa2d8d5aa859_MD5.webp)

基于 Spring Boot 3.4 + Spring AI + Langchain4j 构建，深度集成了 FastGPT、扣子、DIFY 等主流 AI 平台，本地就能跑 RAG、知识图谱、数字人、AI 流程编排。

如果你正在找企业级的 AI 应用落地参考，或者想学习 Java AI 应用开发，RuoYi AI 值得花时间研究一下。

当然了。

这个项目并不完美，坑还是蛮多的，我就踩了不少 😄。

但这个项目的价值我认为是这样的，它给了 Java 开发者一个完整的 AI 应用落地参考。

如果你正在琢磨怎么把 RAG、Agent、工作流这些 AI 能力整合到现有的 Java 项目里，RuoYi AI 是值得研究二开的。

特别是 [v3.0.0](http://v3.0.0) 分支，新增了不少实用能力，比如 AI 流程编排、自然语言生成图表、Agent Skills 等。

## 01、部署 RuoYi AI

和二哥之前的项目技术派、派聪明 RAG 一样，RuoYi AI 也支持本地部署和 Docker 部署两种方式。

但我用 Docker 启动的时候直接报错了。提示 Web 和 admin 端都没有镜像，挺尴尬的。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/ab82690b007ea5dca50260845c2beac8_MD5.png)

不过这里可以直接用 Qoder Cli 找到构建脚本，拉取镜像。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/152ef169a981f63acb5898f2552106b4_MD5.png)

我们先直接打开官方的 demo 看一下。首先是工作流编排，类似 dify 和 coze。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/79a3de153313f9ee2ff69962408505c5_MD5.png)

不过官方的 demo 无法演示，因为体验账号的权限不足。大家如果想体验完整的工作流的编排，可以去看看 PaiAgent 项目，简单却五脏俱全。

> 1、教程地址： [https://paicoding.com/column/14/1](https://paicoding.com/column/14/1) 2、源码地址： [https://github.com/itwanger/PaiAgent](https://github.com/itwanger/PaiAgent)

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/d48d5defd00672d403c9b50cbadc4585_MD5.jpg)

算是年后要发布的 PaiFlow（微服务 Agent 项目）的初级版本，大家可以期待下。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/0cae2138d9e2477cc4b6b42879011734_MD5.png)

不知道大家的感受如何，我是在 2026 年的 1 月份突然感觉到被 AI 冲击到了。

不管是 coding 上，还是内容创作上，冲击力很大，以前我从来没有这种感觉。

以至于经常深夜 emo，思考马年该如何重新出发。真心话，焦虑完全大于兴奋。

相似感受的小伙伴可以在评论区扣个 1。

## 02、RAG 知识库实战

RAG 是 2025 年 AI 落地最火的技术方向之一，简单说就是先从知识库里检索相关内容，再扔给大模型生成回答，能有效解决大模型幻觉问题。

二哥的项目 [派聪明 RAG](https://mp.weixin.qq.com/s?__biz=MzYyNTc5ODUxNg==&mid=2247483983&idx=1&sn=80899181c67f5b101ae0893e2ed4a843&scene=21#wechat_redirect) 相信大家都不陌生，很多 26 届的同学都是靠这个项目拿到了满意的 offer。

RuoYi AI 是用的 Langchain4j 框架 + [BGE-large-zh-v1.5](http://BGE-large-zh-v1.5) 中文向量模型实现了一套纯 Java 的 RAG 方案。

和派聪明不同，派聪明的向量是用的 ElasticSearch。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/48927951124595a8407adfd02b640adc_MD5.png)

但从体感上来说，派聪明 RAG 要比若依 AI 中的 RAG 做的更完善。我认为原因是若依 AI 涉及的内容太多了，没办法专精。

现在有很多公司想做 AI 应用，又不想把核心数据传给第三方平台，RAG 这种本地化方案正好解决了这个痛点。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/2873c904c04a037b81614bbd4d0a5055_MD5.jpg)

2026 年其实还有市场，据我了解到，很多国企也都在推进 RAG 的落地，但进度缓慢。

## 03、 v3.0.0 分支的进化

RuoYi AI 除了主分支，还有个 [v3.0.0](http://v3.0.0) 分支，集成了一些更实用的能力。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/8dcb05d17757969c3cd2761e635f7c10_MD5.png)

比如说自然语言生成图表和 Agent Skills（PaiFlow项目就有这一块面试题，最近几个月Skills的热度太高了，面试很大概率会被问到）。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/2e48c35f25fba822202a46cb1ef6ab14_MD5.png)

简单说，Skills 就是给 AI 定义一套可以调用的工具集。比如你可以定义一个查询天气的 Skill，包含调用哪个 API、需要哪些参数、返回什么格式。AI 在对话过程中，会根据用户意图自动选择合适的 Skill 执行。

这个设计的好处是扩展性强。你可以根据自己的业务需求，定义专属的 Skills。我在Claude Code中就定义了蛮多Skills，对工作效率的提升还是蛮大的。

![图片](assets/RuoYi%20%E5%85%A8%E6%A0%88%20AI%20%E5%B9%B3%E5%8F%B0%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%88%E8%8B%A5%E4%BE%9D%EF%BC%89%E3%80%82/2183810a80860fe8f52e221d6c8ef4ff_MD5.png)

本质上，Skills还是提示词，只不过渐进式披露让你不用一次性把所有的提示词都扔给大模型，按需使用。

但在我看来，如果大模型足够强大，Skills也会被淘汰，道理很简单。

两个人沟通的时候，面对面讲是最有效的，如果你还需要带 100页的 word进行前置条件的沟通，那效率自然不会太高。

## 04、如何写到简历上

**项目名称：** 企业级 AI 智能助手平台

**项目简介：** 基于 Spring Boot 3.4 + Spring AI + Langchain4j 构建的全栈式 AI 开发平台，集成 RAG 知识库、多模型接入、AI 流程编排等企业级能力，支持完全本地化部署。

**技术栈：** Java 17、Spring Boot 3.4、Spring AI、Langchain4j、Vue 3、Vben Admin、Milvus、Redis

**核心职责：**

- 基于 Langchain4j 框架 + [BGE-large-zh-v1.5](http://BGE-large-zh-v1.5) 中文向量模型实现本地化 RAG 方案，支持 PDF、Word、Excel 等多格式文档解析和向量化存储，知识检索准确率提升 40%
- 设计统一聊天服务接口，实现 FastGPT、扣子、DIFY 三大 AI 平台的无缝切换和负载均衡，降低单一平台依赖风险
- 集成 Spring AI MCP 协议，构建可扩展的 AI 工具生态系统，支持动态接入 OpenAI、通义千问、智谱 AI 等多家大模型
- 基于可视化工作流引擎实现 AI 流程编排能力，支持传统节点编排和智能路由两种模式，业务流程配置效率提升 60%
- 开发 Agent Skills 机制，设计工具注册、参数解析、结果回调的完整链路，实现 AI 助手的自主工具调用和任务执行
- 实现自然语言到可视化图表的自动生成能力，通过大模型理解需求并生成 ECharts 配置代码，非技术人员也能快速制作数据报表

## 05、ending

我们评价一个开源项目，到底应该看什么？

是代码有多精妙？架构有多优雅？还是功能有多完善？

其实都不是。

真正有价值的开源项目，应该是【能让更多人上手，能解决真实问题，能让开发者少走弯路】。

RuoYi AI 不是最完美的，工作流编排没有 Dify 强大，RAG 方案没有派聪明精细，但它把这些能力整合在一起，用 Java 开发者熟悉的 Spring Boot 技术栈呈现出来。

这就够了。

我们可以用它快速搭建一个 AI 客服系统。

可以用它做企业内部的知识库问答。

可以用它学习 Spring AI 和 Langchain4j 怎么用。

可以把它写进简历，作为 AI 项目经验的敲门砖。

开源的意义不是造出完美无缺的轮子。

开源的意义是降低门槛，让更多人参与进来，一起把事情做好。

我能从若依AI上看到的是，这个项目证明了一件事：

【Java 在 AI 时代，不是旁观者，而是参与者】。

我们下期见～

派聪明AI · 目录

作者提示: 个人观点，仅供参考

阅读原文