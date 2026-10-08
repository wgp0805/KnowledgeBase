---
title: "为什么越来越多人用OpenMuse？"
source: "https://mp.weixin.qq.com/s/Rv3vXruSfBH54hU6RnXRvQ"
---
苏三 苏三说技术 *2026年10月8日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

> 从“聊天框”到“能接管你的浏览器”，AI Agent终于有了“手”

前阵子有球友反馈说，他们在做一个自动化调研系统。

需求本身不复杂：每天定时抓取几个竞品网站的价格和功能更新，汇总成报告。

他们试了好几种方案，都不太满意。

用Python写爬虫，网站改版就挂，维护成本高。

用大模型API加工具调用，能理解页面内容了，但模型“看不到”真实的浏览器——它只能根据你喂给它的文本做判断，页面里的动态内容、登录态、复杂的交互流程，全都摸不着。

他们需要的不是一个能‘理解’网页的AI，而是一个能‘操作’浏览器的AI。

这个需求，恰恰命中了OpenMuse最核心的设计理念。

OpenMuse是CopilotKit团队在2026年9月开源的一款 **个人AI Agent** ，MIT协议。

上线不到一个月，GitHub上已经4.2K Star，积累了相当的热度。

它的定位非常清晰： **一个有浏览器、有终端、有文件系统、能持续工作的个人智能体** 。

今天这篇文章，我就把OpenMuse为什么越来越多人用的原因，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、OpenMuse到底是什么？

> 有些小伙伴可能会说：“这不就是又一个AI Agent框架吗？跟AutoGen、CrewAI有什么区别？”

**区别很大。**

AutoGen和CrewAI解决的是“多Agent怎么协作”的问题。

你定义角色，让它们在一个群聊里讨论，通过对话达成共识。

OpenMuse解决的是另一个问题： **一个Agent怎么真正“动手”完成任务。**

它给你的是一个 **完整的执行环境** ——一个持久的浏览器（Playwright Chromium）、一个隔离的Linux终端、一个文件系统。Agent在这个环境里干活，你可以随时看到它在做什么，也可以在它卡住的时候 **直接接管它的浏览器** 。

用人话说： **OpenMuse不是“对话框架”，是“Agent的工位”。**

它给Agent配了电脑、浏览器和文件柜，让Agent能像人一样坐在工位上干活。

## 二、一张图看懂OpenMuse的架构

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8OpenMuse%EF%BC%9F/68676d3e55c2f1aa4f93def4880e373d_MD5.jpg)

OpenMuse的架构有一个非常明确的取舍： **执行环境是独立的、隔离的，但你可以随时“接管”。**

浏览器运行在独立的Playwright worker里，有持久化的profile——cookies、登录态、历史记录全部保留。

Agent用这个浏览器访问网站，你可以在任何时候点击“Take control”，打开同一个实时浏览器会话，手动完成验证码或登录，然后把控制权交还给Agent。

## 三、为什么“能接管”这件事很重要？

这是OpenMuse和其他Agent工具最本质的区别。

**大多数Agent工具的工作方式是“盲执行”** 。你给它一个任务，它在后台跑，中间发生了什么你不知道。跑完了告诉你结果，跑挂了报个错。你只能等。

**OpenMuse的工作方式是“可见、可介入、可接管”** 。

它的浏览器worker是一个 **有持久化profile的Chromium实例** 。Agent操作它的时候，每一步都有截图和操作记录。你可以看到它在点哪个按钮、填哪个表单、读哪个页面。

更重要的是， **当Agent卡住的时候——比如遇到验证码、双因素认证、或者需要人工判断的复杂页面——你可以直接接管。**

“Take control”按钮打开的就是Agent正在使用的那个实时浏览器会话。你完成操作，把控制权交还，Agent继续从当前状态往下走。 **不需要重启任务，不需要重新登录，不需要从头再来。**

这个设计的价值在于： **它承认了“有些事情Agent做不了”这个现实，并给出了一个优雅的解法。**

### 3.1 Agent执行与人工接管流程

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8OpenMuse%EF%BC%9F/f989be32db7a5bf8d373453f9031e154_MD5.jpg)

**流程解读** ：

- **任务创建** ：用户通过API或界面创建任务，任务引擎负责调度
- **Agent执行** ：Agent在浏览器Worker中操作，每一步都有截图和记录
- **卡住检测** ：当Agent遇到无法处理的页面（验证码、双因素认证、复杂交互）时，标记“需要人工介入”
- **人工接管** ：用户收到通知，点击“Take control”，打开的是Agent正在使用的 **同一个实时浏览器会话**
- **交还控制** ：人工完成操作后，点击“交还控制权”，Agent从当前状态继续执行
- **任务完成** ：Agent继续抓取数据、生成报告、返回结果

**这个流程的关键在于“同一个会话”** 。

人工接管时打开的不是一个新的浏览器实例，而是Agent正在操作的那个。

登录态、cookie、页面状态全部保留。

**人工只是替Agent完成了它做不了的那一步，然后Agent接着干。**

## 四、代码实战

### 4.1 环境准备

OpenMuse需要 **[Node.js](http://node.js/) 24 LTS** 和 **pnpm 11.19.0** 。

```
# 克隆仓库
git clone 
            https://github.com/CopilotKit/OpenMuse.git
           openmuse
cd openmuse

# 安装依赖
pnpm install --frozen-lockfile

# 复制环境配置
cp .
            env.example
           .env
```

### 4.2 启动演示模式（零配置）

OpenMuse内置了 **演示模式** ，不需要API Key、不需要Google账号、不需要Docker，就能看到完整的界面和交互流程：

```
pnpm dev
```

Web客户端默认运行在 **8081端口** 。打开浏览器访问，你会看到完整的聊天界面、任务面板、文件管理器和浏览器控制台，全部使用虚构的示例数据。

**这个设计非常务实** ——你可以先花10分钟把界面摸熟，确认它解决的是不是你真正的问题，再决定要不要投入时间配置真实环境。

### 4.3 配置真实模型

在`.env` 文件中设置：

```
AGENT_BACKEND=model
MODEL=openai/gpt-5-mini
OPENAI_API_KEY=sk-...
```

或者使用Anthropic和Google：

```
MODEL=anthropic/
            claude-sonnet-4.6
          
ANTHROPIC_API_KEY=sk-ant-...

MODEL=google/gemini-3-flash
GOOGLE_API_KEY=...
```

### 4.4 启用浏览器worker

浏览器worker需要Playwright和Chromium：

```
# 安装Playwright浏览器
pnpm --dir apps/worker exec playwright install chromium

# 在.env中配置worker地址
BROWSER_WORKER_URL=http://127.0.0.1:8790
WORKER_TOKEN=至少32个字符的随机字符串
```

### 4.5 在Java项目中使用

> 有些小伙伴可能会说：“OpenMuse是TypeScript写的，Java项目怎么用？”

**OpenMuse暴露了完整的REST + WebSocket API** ，Java项目可以通过HTTP直接调用。

**Java侧调用示例** （使用Java 11+的HttpClient）：

```
import 
            java.net.URI;
          
import 
            java.net.http.HttpClient;
          
import 
            java.net.http.HttpRequest;
          
import 
            java.net.http.HttpResponse;
          

publicclass OpenMuseClient {

    privatestaticfinal String BASE_URL = "http://localhost:3000";
    privatestaticfinal String ACCESS_KEY = "your-openmuse-access-key";

    // 创建任务
    public static String createTask(String description) throws Exception {
        String json = """
            {
                "description": "%s",
                "mode": "live"
            }
            """.formatted(description);

        HttpRequest request = 
            HttpRequest.newBuilder()
          
            .uri(
            URI.create(BASE_URL
           + "/api/tasks"))
            .header("Authorization", "Bearer " + ACCESS_KEY)
            .header("Content-Type", "application/json")
            .POST(
            HttpRequest.BodyPublishers.ofString(json))
          
            .build();

        HttpClient client = 
            HttpClient.newHttpClient();
          
        HttpResponse response = 
            client.send(request,
           
            HttpResponse.BodyHandlers.ofString());
          
        return 
            response.body();
          
    }

    // 查询任务状态
    public static String getTaskStatus(String taskId) throws Exception {
        HttpRequest request = 
            HttpRequest.newBuilder()
          
            .uri(
            URI.create(BASE_URL
           + "/api/tasks/" + taskId))
            .header("Authorization", "Bearer " + ACCESS_KEY)
            .GET()
            .build();

        HttpClient client = 
            HttpClient.newHttpClient();
          
        HttpResponse response = 
            client.send(request,
           
            HttpResponse.BodyHandlers.ofString());
          
        return 
            response.body();
          
    }
}
```

**在Spring Boot项目中的典型集成** ：

```
@RestController
@RequestMapping("/api/research")
publicclass ResearchController {

    @Autowired
    private OpenMuseClient openMuseClient;

    @PostMapping("/competitor-price")
    public ResearchResult startPriceCheck(@RequestBody ResearchRequest request) {
        // 调用OpenMuse启动浏览器任务
        String taskId = 
            openMuseClient.createTask(
          
            "访问 " + 
            request.getCompetitorUrl()
           + 
            "，抓取当前价格和功能列表，保存到 
            competitor_analysis.md"
          
        );

        // 轮询或通过WebSocket等待结果
        return 
            ResearchResult.builder()
          
            .taskId(taskId)
            .status("STARTED")
            .build();
    }
}
```

**关键点** ：OpenMuse的API设计是 **任务导向** 的。你创建一个任务，它负责执行，你查询状态。Java侧不需要理解浏览器操作的细节，只需要调用API即可。

## 五、OpenMuse vs 传统Agent方案

| 对比维度 | OpenMuse | 传统Agent（AutoGen/CrewAI） |
| --- | --- | --- |
| **执行环境** | **持久浏览器 + 隔离终端 + 文件系统** | 无独立执行环境 |
| **人工接管** | ✅ **可接管实时浏览器会话** | ❌ 只能对话介入 |
| **任务持久性** | ✅ 关闭浏览器后继续执行 | ❌ 进程结束任务即停 |
| **审批机制** | ✅ 每次外部写入需审批 | ⚠️ 取决于实现 |
| **跨平台** | iOS / Android / Web | 通常仅CLI或Web |

## 六、优缺点

### 优点

**1\. 可接管的浏览器会话** 这是OpenMuse最独特的能力。Agent遇到验证码、双因素认证或复杂页面时，你可以直接接管实时浏览器，完成操作后交还给Agent。 **不需要重启任务，不需要重新登录。**

**2\. 持久化任务引擎** 任务支持暂停、恢复、取消、重试。长任务不会因为进程重启而丢失进度。

**3\. 端到端文档工作流** 可以摄取邮件附件、处理PDF表单、生成已填写的副本和回复草稿。对于需要处理大量表单的场景非常实用。

**4\. 跨平台** iOS、Android、Web端一套代码，支持在手机上查看和接管Agent的工作。

**5\. MIT协议开源** 可自由使用、修改、商用。

**6\. 演示模式零门槛** 不需要API Key、不需要Docker，就能看到完整界面和交互流程。

### 缺点

**1\. 项目处于Alpha阶段** 接口、Agent和平台API仍在快速变化中。

**2\. 配置较复杂** 启用真实模式需要配置模型Key、CopilotKit Intelligence Key、浏览器Worker等。不是一键安装。

**3\. 浏览器Worker资源占用** Playwright Chromium在浏览时占用约0.25-0.48GB内存。

**4\. 没有多用户认证** 设计上是单所有者系统，使用共享访问密钥保护。不适合多租户场景。

**5\. Java没有官方SDK** 需要通过REST API自行集成。

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **自动化网页调研** | ✅✅✅ 强烈推荐 | 持久浏览器+可接管，适合复杂网站 |
| **价格监控/竞品追踪** | ✅✅✅ 强烈推荐 | 目标监控功能原生支持 |
| **PDF表单自动化** | ✅✅✅ 强烈推荐 | 端到端文档工作流 |
| **需要人工介入的自动化** | ✅✅✅ 强烈推荐 | 接管浏览器是核心差异化能力 |
| **长时间运行的调研任务** | ✅✅✅ 强烈推荐 | 持久化任务引擎 |
| **多用户SaaS场景** | ❌ 不推荐 | 单所有者设计，无多租户认证 |
| **简单的API调用** | ⚠️ 需评估 | 杀鸡用牛刀 |

## 八、写在最后

回到最初的问题： **为什么越来越多人用OpenMuse？**

答案不复杂—— **因为它让AI Agent从“聊天框”里走了出来，真正坐到了“工位”上。**

AutoGen和CrewAI解决的是“多个Agent怎么讨论”，OpenMuse解决的是“一个Agent怎么真正干活”。它给Agent配了浏览器、终端和文件系统，让Agent能像人一样操作软件、处理文件、完成任务。

**而“接管”这个设计，才是它最聪明的地方。**

它承认了“有些事情Agent做不了”这个现实——验证码、双因素认证、复杂的业务判断。

但它没有因此放弃，而是给了你一个优雅的介入方式： **Agent卡住的时候，你接管；你搞定了，交还给它。**

这种“人机协作”的模式，比“全自动”或“全手动”都更务实。

当然，OpenMuse还很年轻，Alpha阶段、配置复杂、没有多用户认证。

但对于自动化网页调研、PDF表单处理、需要人工介入的长任务这些场景来说，它已经是一个非常值得认真评估的选项。

## 九、参考资源

- **GitHub** ： [https://github.com/CopilotKit/OpenMuse](https://github.com/CopilotKit/OpenMuse)
- **官方文档** ： [https://github.com/CopilotKit/OpenMuse/tree/main/docs](https://github.com/CopilotKit/OpenMuse/tree/main/docs)
- **本地运行指南** ： [https://github.com/CopilotKit/OpenMuse/blob/main/README.md](https://github.com/CopilotKit/OpenMuse/blob/main/README.md)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)