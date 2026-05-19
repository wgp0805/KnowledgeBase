---
title: "用Qoder完成LLM节点开发（DeepSeek+通义千问）"
source: "https://paicoding.com/column/14/3"
author:
published: 2026-02-08
created: 2026-05-19
description: "用 Qoder CLI 为 DeepSeek 节点增加基本配置用 Qoder CLI 打通 DeepSeek 节点用 Qoder CLI 打通通义千问节点"
tags:
  - "clippings"
---
大家好，我是二哥呀。

[上一节](https://paicoding.com/article/detail/2603900057933826) 我们已经跑通了输入输出节点，说明最简单的一个工作流我们已经跑通了，接下来我们需要在此基础上新增一个大模型 LLM 节点，负责把用户输入的内容转正符合播客风格的文本内容。

然后再将这段文本内容传递给输出节点，最终呈现给用户。

至于超拟人音频合成节点，我们留给下一节来完成。小步快跑，快速迭代，也更符合现阶段的开发流程。

源码已开源至 GitHub，类似 dify 这样的工作流 Agent 项目，源码已经提交至 GitHub： [https://github.com/itwanger/PaiAgent/tree/PaiAgent-Three](https://github.com/itwanger/PaiAgent/tree/PaiAgent-Three) 整体架构如下所示，全程使用 Qoder CLI 完成，体验基本上和 Claude Code 持平，想要学 Vibe Coding 的同学可以快速上手实践，写到简历上也非常有看头。

![](https://cdn.paicoding.com/paicoding/befc3b60b961824bd24a0fdff17fa82c.png)

用到的技术栈包括以下这些，SpringAI、SpringAI alibaba、Spring Boot 3.4.1、Java 21、FastJSON2、MinIO 等，LangGraph4J 也提交到了仓库，只不过还没来得及写教程。

![](https://cdn.paicoding.com/paicoding/e77e54b8b973e5b8dcaa0afa417f699e.png)

我们先明确一下需求，在画布上添加 LLM 节点后，我们首先需要配置节点需要的 API Key，然后再将输入节点作为参数传递给 LLM 节点，LLM 生成结束后再将文本内容作为参数传递给输出节点。

![](https://cdn.paicoding.com/paicoding/d8eae23174926f0fc484cd8d13197f1b.png)

好，我们开工！

## 一、申请 DeepSeek API Key

首先我们需要去 DeepSeek 官网申请一下 API Key，申请方式非常简单，直接到： [https://platform.deepseek.com/api\_keys](https://platform.deepseek.com/api_keys) 然后创建 api key 就行了，复制好 key 就可以了。

![](https://cdn.paicoding.com/paicoding/cb31193990e9004d30211a8e3ee7ae9a.png)

记得充钱。

然后请求的 URL 为 [https://api.deepseek.com/v1/chat/completions](https://api.deepseek.com/v1/chat/completions) model 为 `deepseek-chat` 。

## 二、申请通义千问 API Key

登录 [阿里百炼平台](https://bailian.console.aliyun.com/?spm=5176.29619931.J_SEsSjsNv72yRuRFS2VknO.2.74cd10d7ICPxnY&tab=demohouse#/api-key) ，进入密钥管理这里。如果没有，点击右侧创建，如果有，直接复制这个 API Key 就可以了。

![](https://cdn.paicoding.com/paicoding/ba295ee506cf9bb070ff008b4a0b2cb7.png)

## 三、用 Qoder CLI 为 DeepSeek 节点增加基本配置

如果想退出当前的 Qoder CLI 对话，可以键入 `/quit` 命令，退出后会有一个当前 session 的统计信息，比如说这次对话我们新增了 899 行代码。

![](https://cdn.paicoding.com/paicoding/de6aa430103403aff03f8944a3fe679a.png)

然后再次在终端中键入 `qodercli` 重新启动 Qoder CLI。然后再键入 `/resume` 命令选择对应的 session 以恢复之前的对话。

![](https://cdn.paicoding.com/paicoding/d8326112d4fca650bbf3e88586bf3904.png)

这样就完全不用担心我们之前的上下文信息会丢失，非常方便。

![](https://cdn.paicoding.com/paicoding/3f05708d3a0a95403f7c693808683ca6.png)

准备工作完成后，我们把需求直接告诉 Qoder CLI：

> 当选中 DeepSeek 节点的时候,我们需要为该节点配置一些基本信息,第一个是模型的接口地址,第二个是 API 密钥,第三个是温度,也就是目前已经存在的,第四个参数是模型的 model 名

![](https://cdn.paicoding.com/paicoding/fa4b7b06fbe68453f580bc79d15df15d.png)

能看得出，考虑的非常周全，我虽然只讲了 DeepSeek 节点的配置，但 Qoder 自己悟道了，把通义千问节点和 OpenAI 节点也做了处理，并且：

- API 地址为必填
- API 密钥用密码框隐藏显示
- 模型名称也猜到了是 deepseek-chat
- 温度这个配置项可能有同学不理解，我这里解释下。和水温类似，用来控制生成结果的多样性和随机性。数值越低越严谨；数值越高越发散。
- 点击“保存配置”的时候会把这些信息保存到节点的 data 字段中，如果点击工作流的“保存”按钮，还会持久化到数据库中，很 nice。

确认一下，没问题。

![](https://cdn.paicoding.com/paicoding/84a46144822ec448e7a6f94d3ee6763c.png)

确认一下保存也是没问题的。

![](https://cdn.paicoding.com/paicoding/dc1d7c0ef001be71bcb87aeeea2ea13b.png)

好，我们继续。

> 接下来,我们需要把输入节点的用户输入信息传递给 DeepSeek 节点,也就是说,选择 DeepSeek 节点的时候,有一个输入选项,可以引用输入节点的用户输入信息作为参数,然后我们还可以给模型节点添加用 户提示词（目前已经有配置项了）,提示词的基本格式是

下面是用户提示词，我一并分享出来。

```bash
# 角色
你是一位专业的广播节目编辑，负责制作一档名为“AI电台”的节目。你的任务是将用户提供的原始内容改编为适合单口相声播客节目的逐字稿。
# 任务
将原始内容分解为若干主题或问题，确保每段对话涵盖关键点，并自然过渡。
# 注意点
确保对话语言口语化、易懂。
对于专业术语或复杂概念，使用简单明了的语言进行解释，使听众更易理解。
保持对话节奏轻松、有趣，并加入适当的幽默和互动，以提高听众的参与感。
注意：我会直接将你生成的内容朗读出来，不要输出口播稿以外的东西，不要带格式，
# 示例 
欢迎收听AI电台，今天咱们的节目一定让你们大开眼界！ 
没错！今天的主题绝对精彩，快搬小板凳听好哦！ 
那么，今天我们要讨论的内容是……
# 原始内容：{{input}}
复制代码
```

OK，确认没问题。

但是输入参数这里直接绑定死了，我们需要灵活一点，可以追加其他的参数。

> DeepSeek 节点这里的输入参数不应该直接绑定死,也应该是可追加的方式,比如说我点添加,第一个输入框为参数名名,第二个参数是参数类型,可以选择引用或者输入,输入的时候第三个参数是文本框,可以直接输入;选择引用的时候,可以从前一个节点选择

OK，确认没问题。

我们继续，为 DeepSeek 节点添加一个输出配置参数。

> OK,我们需要给 DeepSeek 节点增加一个输出参数配置,第一个是变量名,文本框,第二个是变量类型,目前是只有 string,第三个参数是描述,可为空

确认没问题。

## 四、用 Qoder CLI 打通 DeepSeek 节点

我们来执行一下整个工作流。

失败了，不要怕，直接把问题扔给 Qoder CLI，让它帮我们解决。

原因是没有 DeepSeek 节点的执行器，创建好后来测试一下。

虽然流程没问题，但从测试的数据来看，似乎是没有走正常的 DeepSeek API 调用，看一眼代码，果不其然，这里还是 TODO。

> 从测试的结果来看,这是 DeepSeek 对输入内容的模拟回复。我需要的是你在DeepSeekNodeExecutor去调用真实的 DeepSeek API,我把输入的参数,提示词,API key 都已经告诉你了

这里刚好碰上上下文长度超过了 92%，Qoder CLI 就会对其进行提前压缩。

压缩完后，它继续执行我们新的任务。这个很重要，不然上下文如果丢失了，AI Coding 就会失智。

来确认一下代码，这次修改后确认有真正去发 HTTP 请求，但还有一些细节需要处理，比如说 `/v1/chat/completions` 我们其实已经在 DeepSeek 的节点中配置了，应该直接从节点配置中读取就可以了。

这就需要我们有一些基本的工程能力，能够及时指出 AI Coding 的问题，然后他自己可能需要下一趴出错了才能感知到。

> apiUrl不用再拼接 "/v1/chat/completions",我们的配置就是完整的 [https://api.deepseek.com/v1/chat/completions](https://api.deepseek.com/v1/chat/completions)

我们再来确认一下。

从执行日志上来看，能明显感觉到，DeepSeek 节点耗时增加了。从后台日志也能看得出来，DeepSeek 节点有在正确执行。

请求 DeepSeek API: [https://api.deepseek.com/v1/chat/completions](https://api.deepseek.com/v1/chat/completions)

请求体包括 model、 temperature、messages 等参数。

```json
{"model":"deepseek-chat","temperature":0.7,"messages":[{"role":"user","content":"# 角色\n你是一位专业的广播节目编辑，负责制作一档名为“AI电台”的节目。你的任务是将用户提供的原始内容改编为适合单口相声播客节目的逐字稿。\n# 任务\n将原始内容分解为若干主题或问题，确保每段对话涵盖关键点，并自然过渡。\n# 注意点\n确保对话语言口语化、易懂。\n对于专业术语或复杂概念，使用简单明了的语言进行解释，使听众更易理解。\n保持对话节奏轻松、有趣，并加入适当的幽默和互动，以提高听众的参与感。\n注意：我会直接将你生成的内容朗读出来，不要输出口播稿以外的东西，不要带格式，\n# 示例 \n欢迎收听AI电台，今天咱们的节目一定让你们大开眼界！ \n没错！今天的主题绝对精彩，快搬小板凳听好哦！ \n那么，今天我们要讨论的内容是……\n# 原始内容：你好"}]}
复制代码
```

API 响应状态码: 200 OK

API 响应内容有返回的 content，有 token 的消耗统计 total\_tokens。

```json
{"id":"1a8498d9-090c-4745-b908-ac12fcfabffc","object":"chat.completion","created":1764299201,"model":"deepseek-chat","choices":[{"index":0,"message":{"role":"assistant","content":"欢迎收听AI电台，我是您的主持人小智！今天咱们不聊什么高深莫测的科技话题，就从最简单、最日常的两个字开始——“你好”。您可能会说，这有什么好聊的？不就是打个招呼嘛！但您知道吗，就这俩字，背后可藏着不少学问呢。\n\n首先，咱们来说说“你好”的起源。您猜怎么着？在古代，人们见面可不说“你好”，而是行个礼，或者问一句“吃了吗”？这“你好”其实是近代才流行起来的，它代表着一种平等和尊重的问候方式。想想看，现在咱们用得多自然啊，一见面就“你好”，既礼貌又亲切。\n\n接下来，咱们聊聊“你好”在不同场合的用法。比如在正式场合，您得用“您好”，显得更庄重；跟朋友聊天，直接来句“嗨”或者“嘿”，更随意。有时候，一句“你好”还能化解尴尬呢！想象一下，在电梯里碰到邻居，您微微一笑说声“你好”，气氛立马就缓和了，是不是很神奇？\n\n再说说“你好”在科技里的应用。现在AI助手遍地都是，您一喊“你好，小助手”，它就开始为您服务了。这背后可是语音识别和自然语言处理的技术在支撑，简单说就是让机器听懂人话。不过有时候它也会闹笑话，比如您说“你好”，它回一句“我不好”，那可就逗乐了！\n\n最后，咱们来点互动。听众朋友们，下次您跟人打招呼的时候，不妨试试用不同的语气说“你好”，看看对方什么反应。说不定能带来意想不到的乐趣呢！好了，今天关于“你好”的闲聊就到这儿，希望让您会心一笑。感谢收听AI电台，咱们下期再见！"},"logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":198,"completion_tokens":375,"total_tokens":573,"prompt_tokens_details":{"cached_tokens":0},"prompt_cache_hit_tokens":0,"prompt_cache_miss_tokens":198},"system_fingerprint":"fp_ffc7281d48_prod0820_fp8_kvcache"}
复制代码
```

## 五、用 Qoder CLI 打通通义千问节点

DeepSeek 节点打通后，我们来看通义千问节点的配置，我们需要 API 地址、API Key 和 model 名。

直接切到智能会话窗口，选择【智能问答】和【auto】，然后把我们的问题扔进去：“我准备配置通义千问节点，模型名称、API 地址我应该配置什么”，这样 Qoder 就会联网去查找。

给出我们答案（你看，开发再也不用跳转到浏览器去检索了）

- API 地址: [https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions](https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions)
- 模型名称就选 qwen-turbo

直接将这些信息填入到通义千问的配置项中。

保存工作流后，我们来测试一下，输入“沉默王二牛逼”，点击【执行工作流】，执行状态 OK 了。

控制台的输出数据，确认也没问题。

通义千问的输出节点中，output 的 json 数据也是 OK 的，看了一下文字，还真挺不错哈。

```json
{output=欢迎收听AI电台，今天咱们的节目一定让你们大开眼界！  
没错！今天的主题绝对精彩，快搬小板凳听好哦！  
那么，今天我们要讨论的内容是——沉默王二牛逼！  

你可能一听这名字就懵了，啥叫沉默王二牛逼？是不是有个叫王二的人特别能干，还特别安静？  
其实啊，这可不是什么名人，而是网络上一个梗，用来形容那些平时不说话，但关键时刻一开口就能让人惊掉下巴的人。  

你说他牛逼吧，他从来不吹牛，人家就是实力派。  
你说他沉默吧，但他一说话，那内容简直比相声演员还逗。  

这就像你家里有个老哥，平时在家一声不吭，可是一到饭桌上，一开口就讲段子，全场都笑翻了。  
这种人啊，不是不会说话，而是懒得说，但一旦说起来，那叫一个精彩。  

所以说啊，沉默王二不是真的沉默，而是“静水深流”，表面看着不起眼，内里藏着大智慧。  

你有没有遇到过这样的人？平时话不多，但一聊天就让你觉得：“哎呦，这哥们儿真有料！”  
那今天咱们就聊聊，为什么有些人越是沉默，越显得牛逼？  

接下来咱们继续聊，保证让你听完以后，对“沉默”这个词有新的认识！}
复制代码
```

确认一下节点的请求参数，API 的 URL、model 名、温度、输入内容、提示词等等，都没问题。

## 六、小节

总结一下本篇完成的主要内容，包括：

- 添加 LlmInputParam 和 LlmOutputParam 接口定义
- 实现 LLM 节点配置状态管理，包含 apiUrl、apiKey、model、temperature、prompt
- 支持 LLM 输入参数和输出参数的添加、删除、修改操作
- 在节点点击时加载 LLM 节点的配置数据
- 实现 LLM 配置保存功能，包含参数合法性校验和提示词模板引用检测
- 更新节点配置右侧面板，新增 LLM 节点输入参数和输出参数的 UI 表单
- 增加提示词模板、API 地址、API Key、模型名称和温度的配置输入框
- 调整节点配置面板宽度，优化表单布局样式

顺带总结一下这次可以写到简历上的点：

项目名：PaiAgent - AI 工作流编排平台

核心职责：

- 负责通义千问与 DeepSeek 大模型节点的信息配置，抽象出统一的 LLM 节点配置模型（模型选择、API Key、温度、最大 Token 等），支撑不同厂商大模型在同一画布下无缝切换与组合。
- 设计并实现“输入节点 → LLM 节点 → 输出节点”的端到端工作流执行链路，输入节点负责封装用户原始输入，LLM 节点根据配置调用对应大模型（通义千问、DeepSeek），输出节点聚合上游节点结果并支持自定义模板渲染，最终形成用户可见的回复内容。
- 在工作流引擎中扩展 LLM 节点执行逻辑，为通义千问、DeepSeek 分别实现独立的 NodeExecutor，并统一纳入 DAG 引擎的调度流程中，实现根据拓扑排序结果按依赖顺序执行节点。
- 优化节点配置与类型约束，为不同类型节点定义清晰的输入/输出 Schema，提升工作流的可维护性。

通过这次对 LLM 节点的完整落地，可以更清晰地看到 Qoder 在工程化方向上的实际能力，它真的已经不再是一个 IDE 了，而是一个真正能支撑复杂业务场景、提升团队开发效率的高级工程师。