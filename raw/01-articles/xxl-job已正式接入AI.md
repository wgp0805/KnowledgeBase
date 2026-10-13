---
title: "xxl-job已正式接入AI"
source: "https://mp.weixin.qq.com/s/MPGPF9FriY57Vbb1MVGsEQ"
---
苏三 苏三说技术 *2026年10月13日 08:38*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

> 定时任务 + AI = 把“跑批”变成“跑智能”

最近有球友反馈说：他们试过在定时任务里直接调大模型API，但问题很多。

API Key硬编码在代码里、失败了没有重试机制、任务跑没跑成功也不知道。

后来想搞个专门的AI任务调度系统，又觉得太重了。

我问他：“你们没考虑过用XXL-JOB的AI执行器？”

他愣了一下：“XXL-JOB还能跑AI任务？”

**能。而且是从 [v3.1.0就开始了。](http://v3.1.xn--0-ov6ao47afmcz0e./)**

XXL-JOB从 [v3.1.0版本正式引入了](http://v3.1.xn--0-ov6au5g0vv4a114i29gnzo/) **AI执行器** ，内置了多个AI任务Handler，与Spring AI、Ollama、Dify等集成打通。

到 [v3.4.0版本，又进一步集成了OpenClaw，新增了](http://v3.4.xn--0,openclaw,-mm8qo8cja292rjwrf11btwn4tg2txx76a979k4i7a/) `openClawJobHandler` 。

这意味着什么？

**你不需要为AI任务单独搭一套调度系统。AI任务和普通任务在同一个调度体系里管理，用同一套重试机制、同一套告警、同一套日志。**

今天这篇文章，我就把XXL-JOB的AI能力从头到尾给你拆解一遍。

希望对你会有所帮助。

最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibJZVicC7nz5jN7lz3xCSbNeNj4yNXMvNX12Fgwkvnuibx4wj2uF89ehibUGMOT4DPHibO5dg44kXwBickPvORaQ8JGA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

## 一、XXL-JOB的AI执行器到底是什么？

> 有些小伙伴可能会说：“XXL-JOB不是个定时任务调度框架吗？跑AI任务是不是有点不务正业？”

**恰恰相反。**

定时任务调度框架跑AI任务，是 **回归本质** 。

定时任务的核心使命是什么？

**在正确的时间，用正确的方式，执行正确的逻辑。**

普通任务是这样，AI任务也是这样。

过去你要做一个“每天生成业务洞察”的任务，得自己写代码：调模型API、处理失败重试、记录执行日志、配置告警。

这些事XXL-JOB本来就在做，你只是把“执行逻辑”从“查数据库”换成了“调大模型”。

**XXL-JOB AI执行器的核心思路是** ：把AI调用封装成标准的Bean模式Handler，让AI任务和普通任务用同一套调度、同一套重试、同一套日志。

**一句话说清：AI执行器 = 内置的AI任务Handler + 统一的调度管理。**

## 二、XXL-JOB AI执行器的架构

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HUV4yMdu0rdoqtP3N3ibibwyMQDJL4l8H36PMFr0qslKnbs3ciaxVkJASG3xrSBFPab2Q8zxPSTo9oAG9eQzZ26lvmr8Bf65vwr4FaXlicko5z4/640?wx_fmt=webp&from=appmsg#imgIndex=1)

**关键理解** ：调度中心不关心你执行的是AI任务还是普通任务。

它只管“什么时候触发、触发哪个Handler、传什么参数”。

AI执行器负责“怎么调AI”。

## 三、底层原理

### 3.1 Bean模式Handler

XXL-JOB的任务Handler有两种模式： **Bean模式** 和 **GLUE模式** 。

**Bean模式** 是推荐的方式：你写一个Java类，用 `@XxlJob("handlerName")` 注解标记，XXL-JOB会自动把它注册为一个可调度的任务Handler。

AI执行器就是基于这个机制实现的。

`ollamaJobHandler` 、 `difyWorkflowJobHandler` 、 `openClawJobHandler` 都是标准的Bean模式Handler。

### 3.2 ollamaJobHandler

它是调用本地模型的标准化封装。

`ollamaJobHandler` 的核心逻辑非常简洁：

```
// 简化后的逻辑
@XxlJob("ollamaJobHandler")
public void ollamaJobHandler() throws Exception {
    // 1. 从任务参数中解析prompt和input
    String param = 
            XxlJobHelper.getJobParam();
          
    JSONObject json = 
            JSON.parseObject(param);
          
    String input = 
            json.getString(
          "input");
    String prompt = 
            json.getString(
          "prompt");
    
    // 2. 调用Ollama API
    String result = 
            ollamaClient.chat(prompt,
           input);
    
    // 3. 记录执行结果
    
            XxlJobHelper.log(
          "AI任务执行完成，结果：{}", result);
    
            XxlJobHelper.handleSuccess(result);
          
}
```

**关键设计** ： `prompt` 和 `input` 从 **任务参数** 中动态获取，不是硬编码在执行器里。

这意味着同一个执行器可以跑不同的AI任务，只需要在调度中心配置不同的任务参数。

### 3.3 difyWorkflowJobHandler

它能触发Dify工作流。

`difyWorkflowJobHandler` 的逻辑类似，但对接的是Dify的工作流引擎：

```
@XxlJob("difyWorkflowJobHandler")
public void difyWorkflowJobHandler() throws Exception {
    String param = 
            XxlJobHelper.getJobParam();
          
    JSONObject json = 
            JSON.parseObject(param);
          
    String inputs = 
            json.getString(
          "inputs");
    String user = 
            json.getString(
          "user");
    
    // 调用Dify工作流API
    String result = 
            difyClient.runWorkflow(inputs,
           user);
    
    
            XxlJobHelper.handleSuccess(result);
          
}
```

**Dify配置的优化** ：早期版本中， `baseUrl` 和 `apiKey` 等Dify配置信息需要放在执行器侧的文件里。

后续版本优化为 **从调度中心“任务参数”动态配置** ，支持多Dify应用集成，提升了研发效率。

## 四、代码实战

### 4.1 前置准备

假设你已经部署了XXL-JOB调度中心和Ollama服务。

如果还没部署，参考官方文档即可。

### 4.2 配置AI执行器

在调度中心新建执行器：

```
INSERT INTO \`xxl_job_group\`(\`app_name\`, \`title\`, \`address_type\`, \`address_list\`, \`update_time\`)
VALUES ('xxl-job-executor-sample-ai', 'AI执行器Sample', 0, NULL, now());
```

\*\*AppName必须是 `xxl-job-executor-sample-ai` \*\*，因为AI执行器的示例代码用这个AppName注册。

### 4.3 在Spring Boot项目中引入AI执行器

```
<dependency>
    <groupId>
            com.xuxueli
          </groupId>
    <artifactId>xxl-job-core</artifactId>
    <version>3.4.0</version>
</dependency>
```

配置执行器：

```
xxl:
  job:
    admin:
      addresses: http://localhost:8080/xxl-job-admin
    executor:
      appname: xxl-job-executor-sample-ai
      port: 9999
```

### 4.4 在调度中心新建AI任务

在XXL-JOB调度中心新建任务：

- **执行器** ：选择 `AI执行器Sample`
- **任务描述** ：每日业务洞察生成
- **Cron** ： `0 0 6 * * ?`（每天早上6点）
- **运行模式** ：BEAN
- **JobHandler** ： `ollamaJobHandler`
- **任务参数** ：
```
{
    "input": "请基于昨天的销售数据生成一段业务洞察。数据：华东区销售额120万，环比下降12%；华南区销售额98万，环比上升8%。",
    "prompt": "你是一个数据分析师，请用简洁的语言生成业务洞察，不超过100字。"
}
```

**任务参数中的 `prompt` 和 `input` 会根据每次任务动态传入** ，同一个Handler可以跑不同的AI分析。

### 4.5 执行结果查看

任务触发后，在调度中心的“调度日志”中可以看到：

- 执行状态（成功/失败）
- 执行时间
- AI返回的结果（通过 `              XxlJobHelper.log            ` 记录）

**失败重试** ：如果AI调用失败（比如Ollama服务不可用），XXL-JOB的失败重试机制会自动重试，不需要你自己写重试逻辑。

## 五、XXL-JOB AI执行器的优缺点

### 优点

**1\. 统一的调度管理** AI任务和普通任务在同一个调度中心管理。不需要为AI任务单独搭一套系统，运维成本低。

**2\. 内置失败重试** AI调用可能因为模型服务不可用、超时等原因失败。XXL-JOB的失败重试机制自动处理，不需要自己写重试逻辑。

**3\. 完整的执行日志** 每次AI任务的执行结果、耗时、返回值都记录在调度日志里。出问题可以追溯。

**4\. 动态配置** `prompt` 、 `input` 、Dify的 `baseUrl` 和 `apiKey` 都从任务参数动态获取，不需要改代码就能调整。

**5\. 多AI后端支持** 支持Ollama、Dify、OpenClaw、Spring AI等多种AI后端。

**6\. 零额外基础设施** 如果你已经在用XXL-JOB，接入AI能力不需要引入新系统。

### 缺点

**1\. AI执行器需要单独部署** AI任务需要部署 `xxl-job-executor-sample-ai` 这个执行器示例。普通执行器不能跑AI任务。

**2\. 任务参数有长度限制** `prompt` 和 `input` 通过任务参数传递，如果内容太长可能受限于数据库字段长度。

**3\. 不支持流式输出** AI任务的执行是同步等待的，不支持流式输出。对于长文本生成任务，执行时间可能较长。

**4\. 内置Handler的灵活性有限** 目前的 `ollamaJobHandler` 和 `difyWorkflowJobHandler` 是通用封装。如果需要复杂的AI编排（比如多轮对话、工具调用），还是需要自己写Handler。

## 六、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **定时AI数据摘要** | ✅✅✅ 强烈推荐 | 每天定时跑AI总结，失败自动重试 |
| **定时AI内容生成** | ✅✅✅ 强烈推荐 | 定时生成日报、周报、业务洞察 |
| **定时触发Dify工作流** | ✅✅✅ 强烈推荐 | difyWorkflowJobHandler开箱即用 |
| **定时AI数据清洗** | ✅✅✅ 强烈推荐 | 批量数据处理+AI增强 |
| **已有XXL-JOB的项目** | ✅✅✅ 强烈推荐 | 零额外基础设施，直接接入 |
| **需要复杂AI编排的任务** | ⚠️ 需评估 | 内置Handler灵活性有限，需自定义 |
| **需要流式输出的任务** | ❌ 不推荐 | 同步执行，不支持流式 |

## 七、写在最后

回到最初的问题： **XXL-JOB接入AI，到底接了什么？**

它不是“在定时任务里加了个聊天框”，而是 **把AI调用变成了定时任务的一种标准执行逻辑** 。

**AI任务和普通任务共享同一套调度、同一套重试、同一套日志。**

你不需要为“每天早上跑一次AI分析”单独搭一套系统，不需要自己写API调用的重试逻辑，不需要自己记录执行结果。

**从 [v3.1.0到v3.4.0，XXL-JOB的AI能力在持续完善。](http://v3.1.xn--0v3-8j2e.4.xn--0,xxl-jobai-359rv61a81fz5sx91a9k3eow5asgi./)**

Ollama、Dify、OpenClaw、Spring AI——AI后端的支持越来越丰富。

Dify配置从执行器侧移到任务参数，支持多应用集成。这些迭代说明团队在认真打磨这个功能。

当然，XXL-JOB的AI执行器也有局限。

它适合的是 **“定时触发、同步执行、结果记录”** 这类标准化的AI任务。

如果你需要复杂的多轮对话、工具调用、流式输出，还是需要自己写更复杂的Handler。

**但如果你只是想“每天早上6点让AI分析一下昨天的数据”——XXL-JOB的AI执行器可能是最省心的选择。**

不需要引入新系统，不需要写重试逻辑，不需要自己管日志。

参考资源：

- **XXL-JOB官方文档** ： [https://www.xuxueli.com/xxl-job](https://www.xuxueli.com/xxl-job)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)