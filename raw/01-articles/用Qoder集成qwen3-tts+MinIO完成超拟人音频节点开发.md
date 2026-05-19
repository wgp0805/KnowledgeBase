---
title: "用Qoder集成qwen3-tts+MinIO完成超拟人音频节点开发"
source: "https://paicoding.com/column/14/4"
author:
published: 2026-02-08
created: 2026-05-19
description: "使用 Qoder CLI 创建全新的 AudioTTS 节点基础模板，在工作流引擎中实现 AudioTTS 节点的执行逻辑，调用阿里百炼 qwen3-tts-flash，将生成的音频 URL 返回给下一节点增加 URL 结果的合法性校验，并支持后续扩展为自动上传至 MinIO 的能力将音频节点纳入“输入节点 → 音频节点 → 输出节点”的完整链路，验证整个工作流的可执行性"
tags:
  - "clippings"
---
大家好，我是二哥呀。

关于超拟人音频节点，我首先想到的解决方案是 qwen3-tts-flash——阿里百炼平台上提供的一种语音合成服务，提供了多种拟人音色，还支持英语、汉语，以及方言。

输入参数也很简单，必须参数仅需一个要合成音频的文本 text；一个音色 voice，可选 Cherry（阳光积极、亲切自然小姐姐）、Serena（温柔小姐姐）、Ethan（标准普通话，带部分北方口音。阳光、温暖、活力、朝气）等等；还有一个 language\_type，默认是自适应。

![](https://cdn.paicoding.com/paicoding/5cc2d70c2c2f18e90296a1d8bfe8c58e.png)

返回参数是一个 URL，有效期是 24 小时，后续我们可以在本地安装 MinIO，将音频保存到 MinIO 服务中。

整体的思路不复杂，接下来我们通过拆分任务，让 Qoder 来实现它：

- 定义超拟人音频节点的输入/输出参数结构，包括 text、voice、languageType
- 使用 Qoder CLI 创建全新的 AudioTTS 节点基础模板，让节点具备标准的 initConfig、schema、executor 结构
- 为音频节点加入完整的配置表单，包括文本输入框、音色选择器、语言类型下拉框
- 在工作流引擎中实现 AudioTTS 节点的执行逻辑，调用阿里百炼 qwen3-tts-flash，将生成的音频 URL 返回给下一节点
- 增加 URL 结果的合法性校验，并支持后续扩展为自动上传至 MinIO 的能力
- 将音频节点纳入“输入节点 → 音频节点 → 输出节点”的完整链路，验证整个工作流的可执行性

## 一、为超拟人音频合成节点配置参数

直接告诉 Qoder 我们的需求：

> 我们要为超拟人音频节点添加基本配置，当选中超拟人音频节点时，右侧的节点配置中，第一个参数为 API key，第二个参数为模型名称，默认值为 qwen3-tts-flash；删除之前遗留的提示词、温度等配置项，这两个暂时不需要。

![](https://cdn.paicoding.com/paicoding/f6745fea62d009966b88df71ce53dc4d.png)

确认一下，没问题。

![](https://cdn.paicoding.com/paicoding/88908c4bc0e20f3f442f9361f2fc5dff.png)

这里的 API key 仍然是上一节我们在阿里百炼平台上申请的，直接填过来就行。

> 接着，我们需要为超拟人音频合成节点增加三个输入参数：第一个参数为 text，类型可以是输入/引用，输入的时候是文本框，引用的时候可以选择上一个工作流节点的输出，比如说输入节点的用户输入；第二个参数为 voice，用于指定音色，可选参数有 Cherry、Serena、Ethan；第三个参数为language\_type，可选参数为 Auto。

确认一下是没问题的，但是我们应该把它放到输入配置项里。

> 最好是把这三项和基本信息配置区分开,就放到节点配置的输入配置中,我还要增加一个输出配置项,里面包括一个 voice\_url

前端的所有配置项目我们都搞定了，并且新的工作流输入 → 超拟人音频合成 → 输出我们也配置完成了。

## 二、在工作流引擎中实现 AudioTTS 节点的执行逻辑

我们来测试一下工作流，按理说我们还没有在工作流引擎当中实现 AudioTTS 节点的执行逻辑呢，但目前测试的结果是 OK 的。

那这个时候，我们就应该抱着怀疑的态度去检查一下源码，发现 TTSNodeExecutor 提供了一个简单的模拟实现。

那接下来，我们就要对接真正的阿里音频合成服务。

> 我在前端已经完成了阿里百炼 qwen3-tts-flash 的超拟人音频节点配置，接下来，我需要在工作流引擎中实现具体的 AudioTTS 节点执行逻辑，调用阿里百炼 qwen3-tts-flash，并将生成的音频 URL —— voice\_url 返回给下一节点，目前我们的工作流是，输入节点 → 超拟人音频合成节点 → 输出节点

看一眼代码，大体上没什么问题。

重启后端服务再来测试一下。很遗憾失败了，后端报错了，提示“task can not be null”。

我们直接把错误扔给 Qoder CLI 来看看反馈。

需要联网检查，我们直接放行。这次修改了参数的请求格式。

再来测试一下，发现仍然失败，还是原来的问题。

```json
2025-11-30T07:06:00.908+08:00 ERROR 20334 --- [PaiAgent] [nio-8080-exec-7] c.p.e.executor.impl.TTSNodeExecutor      : 调用阿里百炼 TTS API 失败

org.springframework.web.client.HttpClientErrorException$BadRequest: 400 Bad Request on POST request for "https://dashscope.aliyuncs.com/api/v1/services/audio/tts": "{"request_id":"a6bf0828-f7bf-4be9-bab0-1c65592ba007","code":"InvalidParameter","message":"task can not be null"}"
        at org.springframework.web.client.HttpClientErrorException.create(HttpClientErrorException.java:103) ~[spring-web-6.2.1.jar:6.2.1]
复制代码
```

那这时候，我们就需要去官网看看具体的 API 调用方式了。发现官网用的是 DashScope SDK，和 Qoder 原来自研的不太一样。

那我们直接切换一下。

> 嗯，再次执行，发现仍然出现了 task can not be null 的错误，所以我希望切换到 DashScope SDK 的方式实现，并且官方的请求发起是这样的 Constants.baseHttpApiUrl = " [https://dashscope.aliyuncs.com/api/v1";](https://dashscope.aliyuncs.com/api/v1%22;)

```java
MultiModalConversation conv = new MultiModalConversation();
MultiModalConversationParam param = MultiModalConversationParam.builder()
        // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx")
        .apiKey(System.getenv("DASHSCOPE_API_KEY"))
        .model(MODEL)
        .text("Today is a wonderful day to build something people love!")
        .voice(AudioParameters.Voice.CHERRY)
        .languageType("English") // 建议与文本语种一致，以获得正确的发音和自然的语调。
        .build();
MultiModalConversationResult result = conv.call(param);
String audioUrl = result.getOutput().getAudio().getUrl();
System.out.print(audioUrl);
复制代码
```

2.17.3？感觉和官方要求的最低版本不太一样，这时候就需要我们主动出击，去看看最新的 DashScope SDK 版本到底是多少？

COM.ALIBABA DASHSCOPE-SDK-JAVA 2.22.2 INCLUDEBACKLINKS -->

找到 pom.xml 文件，修改版本号。

保存后，直接让 Qoder CLI 来执行 `./mvnw spring-boot:run` ，这样好方便遇到编译错误后，Qoder CLI 能够自我修复。

但 AI Coding 有时候是需要我们去质疑的，这不，当 AI 发现 2.22.2 的 SDK 加载失败后，又重新切换到了旧的代码版本。

这时候怎么办呢？

并不是因为 AI 降智了，而是官方的 doc 和 AI 已知的 doc 不匹配了，需要我们主动给 AI 提供更多的信息，不管是用 DashScope SDK，还是 AI 自研的 Coding，肯定最终都是可以实现我们预期效果的，只是现阶段，我们需要让 AI 知道的更多。

OK，AI 发现了第一个问题，就是请求的 URL 有问题，应该是 `https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation` 。

然后请求的参数应该是：

```json
{                                                                                                   
    "model": "qwen3-tts-flash",                                                                       
    "input": {                                                                                        
      "text": "文本内容",                                                                             
      "voice": "Cherry",                                                                              
      "language_type": "Auto"                                                                         
    }                                                                                                 
  } 
复制代码
```

再接着看，返回的参数格式是 output.audio.url 而不是 output.audio\_url。

```json
{                                                                                                   
    "output": {                                                                                       
      "audio": {                                                                                      
        "url": "http://dashscope-result-wlcb.oss-cn-wulanchabu.aliyuncs.com/..."                      
      }                                                                                               
    }                                                                                                 
  } 
复制代码
```

另外提醒大家一点的是，Qoder CLI 可以通过 ctrl+r 组合键切换详细和省略模式，省略模式是这样的：

再次测试，发现超拟人音频合成节点可以工作了。

到此为止，流程已经跑通，nice。

## 三、为超拟人音频合成节点添加播放器

> 当输出节点中配置了
> 
> ```bash
> <source src="{{output}}" type="audio/mpeg">
> 复制代码
> ```
> 
> 我们需要在调试面板中，为最终输出这里增加一个音频播放器，让用户点一下后就可以直接播放音频。

代码主要体现在这一块。

```typescript
const outputValue = (outputData as Record<string, any>)?.['output'];
console.log('outputValue:', outputValue);
console.log('outputValue type:', typeof outputValue);

// 检查是否包含 audio 标签
if (outputValue && typeof outputValue === 'string' && outputValue.includes('<audio')) {
  // 提取 audio 标签中的 src 属性
  const audioMatch = outputValue.match(/<source\s+src="([^"]+)"/);
  console.log('audioMatch:', audioMatch);
  
  if (audioMatch && audioMatch[1]) {
    const audioUrl = audioMatch[1];
    console.log('audioUrl:', audioUrl);
    return <AudioPlayer audioUrl={audioUrl} />;
  }
}
复制代码
```

来看一下最终的效果。

OK，目前修改的内容包括：

- 后端新增 aliyun dashscope-sdk-java 依赖以支持阿里百炼TTS API调用
- 重构 TTSNodeExecutor，调用阿里百炼 qwen3-tts-flash HTTP API生成音频URL
- 支持通过节点配置动态指定文本来源、音色及语言类型参数
- 前端编辑器新增TTS节点配置面板，支持API Key、模型名称及输入文本配置
- 前端调试面板（DebugDrawer）完善音频输出检测和播放支持

## 四、集成 MinIO 来保存音频文件

qwen3-tts 返回的音频是有过期时间的，所以我们需要将其保存到本地，或者集成到 MinIO 来持久化存储它。通常情况下，我们会选择后者，因为保存到本地服务器上不容易集中管理，MinIO 天然提供了一个管理端。

好，那接下来我们的思路是，把 MinIO 作为一个轻量级的自建对象存储，然后把音频文件托管起来，生成一个稳定可访问的 URL，再把这个 URL 回写到工作流的输出里就好了。

### 01、安装 MinIO Server

访问这个链接： [https://dl.min.io/server/minio/release/](https://dl.min.io/server/minio/release/)

根据自己的系统选择对应的版本，比如说我是 Apple 芯片就选第二个，Windows 就选倒数第一个。下载完成后，macOS 需要给它执行权限。

执行 `chmod +x minio` ，然后为 MinIO 创建一个数据目录 data，之后执行 `./minio server data/` 就可以启动了。

Windows 的话，下载后的就直接是 exe 文件，可以直接执行，当然了，也要记得创建数据目录。如果一切正常的话，应该会输出以下信息，

完事直接点击 webui 的访问地址 [http://192.168.0.113:55624](http://192.168.0.113:55624/) 启动。注意这个端口号是会变化的，看自己的控制台就好了。

输入用户名和密码 minioadmin，就可以看到 MinIO 的管理端主页了。

### 02、创建 MinIO 的 Bucket

MinIO 中的 **Bucket（桶）** 是对象存储的核心概念之一，它相当于传统文件系统中的“文件夹”或“目录”，是存储对象（Object）的容器。

我们可以创建一个名为 paiagent 的桶，我们就把临时的音频文件存储到这个桶里面。

权限设置为 Public

### 03、使用 Qoder 集成 MinIO

> 从阿里百炼 TTS 拿到audioUrl 后，我希望上传到 MinIO 存储起来，然后把 URL 重新写入到 output 我的 MinIO 配置是

```
minio:
  endpoint: http://localhost:9000
  accessKey: minioadmin
  secretKey: minioadmin
  bucketName: paiagent
  publicUrl: http://localhost:9000
```

这里提醒一下，如果 Qoder CLI timeout 的话，直接键入 `继续` 就好了。

Qoder CLI 完成工作了，主要做了以下这些修改。

我们重启后端后来测试一下。

从输出节点的数据当中也能看得出来，确实是从 MinIO 中拿到的 URL。

```
"{\"output\":\"http://localhost:9000/paiagent/audio/audio_2116e0a3-fd11-49c4-a10d-146fdebb271d.wav\"}"
```

从 MinIO 的管理端，也是能够看到已经保存好的音频文件，很 nice 👍啊。

## 五、小结

这篇我们利用 Qoder 完成了这些开发内容：

• 给超拟人音频节点补齐了参数模型，以及输入输出参数配置。  
• 在工作流引擎里实现了完整的执行逻辑，从 text → 调用 qwen3-tts → 拿到临时音频 URL → 拉取二进制音频 → 生成节点输出，整个链路跑通无压力。  
• 给调试面板加上原生音频播放器，执行完节点后能实时播放生成的音频，让工作流的用户体验瞬间提升一大截。  
• 为解决大模型返回的临时音频 URL 会过期的问题，我们集成了 MinIO 来搭建本地对象存储，这样就可以统一管理音频文件。

好，接下来，我们来总结一下简历上可以写的点：

- 负责超拟人音频合成节点的设计与实现，集成阿里云百炼平台 DashScope SDK，支持 Cherry、Elise 等多种超拟人音色，实现文本到音频的转换。通过灵活的参数提取机制，支持从上游 LLM 节点引用输出或配置面板直接输入，从而提升工作流的自动化能力。
- 集成 MinIO 对象存储服务，设计并实现配置类（MinioConfig）和服务层（MinioService），支持本地文件流上传和远程 URL 转存两种模式，从而解决 qwen3-tts-flash 临时 URL 过期问题。
- 扩展工作流引擎的节点类型体系，在 DAG 引擎中注册 TTS 节点执行器，实现"输入 → LLM → TTS → 输出"的完整数据流链路。通过拓扑排序和依赖调度，确保节点按顺序执行并正确传递参数（output → text → audioUrl），使工作流具备端到端的音频生成能力。
- 优化项目配置管理，通过 Spring Boot 的 @ConfigurationProperties 实现 MinIO 配置的外部化，支持不同环境（开发/测试/生产）快速切换存储服务。封装了 bucket 自动创建、文件上传、公共 URL 生成等通用逻辑。

这篇我们折腾了参数建模、节点执行链路、播放器能力、MinIO 存储，一路走下来你会发现这样一个事实：换成以前，开发这些功能，即便是一名工作三五年的高级程序员，没有一个一周是搞不定的；但放到 Qoder 里，前后我们也就花了 10 个小时的 Vibe Coding 时间。

工具的进步，就是让我们能够把精力集中在真正有价值的地方——设计、抽象、业务、体验、创造。

持续进化吧！

代码我已经提交到了： [https://github.com/itwanger/PaiAgent-one/tree/PaiAgent-Four](https://github.com/itwanger/PaiAgent-one/tree/PaiAgent-Four)