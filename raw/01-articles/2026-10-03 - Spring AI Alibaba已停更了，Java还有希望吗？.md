---
source_url: "https://mp.weixin.qq.com/s/PcjCWkWwwUYC9LxGzoQGWQ"
title: "Spring AI Alibaba已停更了，Java还有希望吗？"
account: "苏三说技术"
published_at: "2026-10-03 09:48:09"
saved_at: "2026-10-03 12:09:55"
sync_id: "art_51359691b9a848ab9af60e53cd26beed"
parse_status: "ok"
---

# Spring AI Alibaba已停更了，Java还有希望吗？

**大家好，我是苏三，又跟大家见面了。**

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐14个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247536010&idx=1&sn=69cbb5fdfc59c9c636559fb556386b24&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

最近技术群里有个话题讨论得特别激烈——“Spring AI Alibaba是不是停更了？”

起因很简单。

有人翻了GitHub的Releases页面，发现**上一个正式版还是v1.1.2.2，发布于2026年3月10日**。

到9月中旬，整整半年没有新正式版。

半年不发版，对一个拥有**10.8k Star**的项目来说，确实反常。

群里有人开始焦虑：“我们刚把生产系统迁过去，这就停更了？”“是不是得赶紧换框架？”“Java做AI是不是真的没戏了？”

说实话，看到这个消息的第一反应，我也有些担心。

但花了一上午把GitHub的commit记录、Release页面和官方博客翻完之后，我的判断跟传闻不太一样。

**它不是弃坑，是在换心脏。**

## 一、先看传闻里“真”的那一半

> 有些小伙伴可能会说：“半年不发版就是停更，这还有什么好洗的？”

这个说法对了一半。

**半年没发正式版，这部分是真的。**

把时间线拉出来看得很清楚：

| 版本 | 发布日期 | 说明 |
| --- | --- | --- |
| v1.1.0.0 | 2025-12-30 | 1.1.x首个稳定版 |
| v1.1.2.0 | 2026-02-02 | Agent Skills + 多智能体并行 |
| ** v1.1.2.2 ** | ** 2026-03-10 ** | ** 最后一个正式版 ** |
| v2.0.0-M1.1 | 2026-06-25 | 预发布版，跟进Spring AI 2.0 |
| 至今 | — | ** 再无正式版 ** |

对一个已经在生产环境使用的框架来说，半年不发正式版，用户等得心焦是完全可以理解的。

## 二、但“另一半真相”更值得琢磨

如果把视线从Release页面移开，去看GitHub的commit记录，画面就完全不一样了。

**main分支的提交并没有停。**

8月25日还有最新提交，往前翻，7月24日到8月25日这一个月合了**35个PR**，8月24日单日合了**8个**。

v1.1.2.2发布之后到现在，main分支总共合了**137个提交**。

这不是一个被放弃的仓库该有的样子。

**那这些提交在干什么？**

翻一下内容就知道：Graph序列化的修复、Admin控制台的中文化、JUnit 5迁移、文档链接修正。

**以修复和测试为主，没有大的功能主线**。

说白了，项目在“养护”，不在“建设”。

**更耐人寻味的是最后一个正式版做了什么。**

v1.1.2.2最大的新特性是什么？

**首次引入AgentScope Java集成**——新增 `spring-ai-alibaba-starter-agentscope` ，用一个 `AgentScopeAgent` 把AgentScope的ReActAgent封装成 `BaseAgent` ，塞进SAA的Graph工作流里编排。

一个被传“放弃维护”的项目，最后一次大更新是在**拥抱自家兄弟框架**。

这不像弃坑，倒像**交接前的铺路**。

## 三、一张图看懂这场“换心脏”的真相

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HUV4yMdu0reibVGQeMOow6dVyHOxlMVqMxTOoVRic4RTw59NcKeSY7ZiaQ1NelwD9uLGyrkKIkKwFHTFZfsYb23wia1FWNiaMzfmbSDSnWIhbwRA/640?wx_fmt=webp&from=appmsg)

**关键证据在官方博客里，而且一年前就写好了。**

java2ai.com上有一篇官方公告，《一文讲透 Spring AI Alibaba 与 AgentScope 的定位与区别》，发布在AgentScope-Java 2025年9月开源后不久。

公告里说得很直白：**开放框架呈现两种趋势，SAA以Graph为核心（工作流编排），AgentScope以Agentic为核心（最大化利用基础模型能力），“两种设计理念都将是企业主流选择”，两者独立发展、不存在替代关系**。

但趋势比公告更直接：**同一个阿里，AgentScope Java的节奏是2.0.2（9月3日）→ 2.0.3（9月7日），四天一个版本；SAA正式版半年一发**。

**一边周更，一边半年更。资源往哪倾斜，肉眼可见。**

## 四、Java AI的“三层台阶”

这场停更风波，其实暴露了一个更深层的问题：**很多人在选框架的时候，没搞清楚自己需要的是哪一层的能力。**

Java AI框架可以分成三层：

![](https://mmbiz.qpic.cn/mmbiz_jpg/HUV4yMdu0rfXcUSF7Xd1N0ibZyCLTlQnVAZYPPib6aGiaMZghZfN9XC9Lxicl3pyEJ8NDwic55dX4ZDtnyAQNdgmvdsibzw9N9hficfTSnXjnVbAiak/640?wx_fmt=webp&from=appmsg)

**第一层解决的是“怎么连上模型”**——模型接入、工具调用、向量库。

Spring AI 2.0和LangChain4j都在这一层，而且**这两家一直很活跃**。

**第二层解决的是“怎么编排多个步骤”**——Graph工作流、条件路由、状态持久化。

Spring AI Alibaba在这一层，Embabel也在这一层。

**第三层解决的是“怎么让Agent长期稳定运行”**——会话持久化、多租户隔离、沙箱执行、断点恢复。AgentScope在这一层。

**关键认知：如果你的需求只是在Java里调用大模型、做RAG、搞工具调用，Spring AI 2.0完全够用，而且它很活跃。** Spring AI 2.0于2026年6月正式GA，基于Spring Boot 4.1和Spring Framework 7.0构建。

**如果你需要的是Graph工作流编排，SAA依然是可用的，它只是不再快速迭代新功能了。** 如果你需要的是让Agent自主执行长任务、管理上下文、多租户隔离—— **那你要的其实是AgentScope，不是SAA。**

## 五、Java该何去何从？

### 选择一：如果你只是“接入模型”

**留在Spring AI 2.0或LangChain4j。**

Spring AI 2.0的ChatClient API非常干净，工具调用被提升为Advisor链的一等公民，可组合、可重试。LangChain4j的模型覆盖最广，30+模型开箱即用。

**这一层没有停更风险。** 这两个框架都在持续迭代。

### 选择二：如果你需要“工作流编排”

**SAA仍然可用，但要接受它进入“养护模式”的现实。**

v1.1.2.0带来的Agent Skills和并行多智能体能力是实打实的。Agent Skills先只注入技能列表，模型需要时才加载完整内容，能省Token；多智能体并行执行可以一次选多个子智能体跑，适合并行查询后汇总。

如果你的项目已经用了SAA，**不需要恐慌性迁移**。它的核心功能是稳定的，bug修复也在继续。

但如果你在选新框架，**需要评估“半年一更”是否满足你对迭代速度的期待**。

### 选择三：如果你需要“Agent自主执行”

**看看AgentScope。**

AgentScope Java 2.0于2026年6月发布，是阿里巴巴集团内部使用最广泛的智能体框架，在十余条核心业务线生产环境深度使用。

它的核心差异化能力是**身份持续**（工作区即Agent的人格与长期记忆）、**上下文可控**（自动压缩，大工具结果落盘）、**状态可恢复**（同sessionId跨进程恢复完整对话）。

**如果你的需求是“让Agent长期稳定地跑”，这才是正确的选择。**

## 六、一个更重要的判断

这场停更风波，最容易引发的误判是“Java做AI不行了”。

**完全不是。**

真实的图景是：**Java AI生态正在分层。**

- 接入层 ：Spring AI 2.0、LangChain4j，活跃且成熟
- 编排层 ：SAA（养护模式）、Embabel（确定性规划），各有定位
- 运行时层 ：AgentScope，快速迭代

**“Java AI框架停更”这个说法，准确的说法是“某一个特定定位的框架，进入了特定阶段”。**

而且还有一条容易被忽略的路径：**跨语言接入Harness。**

现在主流的开源Harness是TypeScript写的，Java应用完全可以在旁边起一个TS运行时，通过gRPC或HTTP调用。

有开发者说得直白：“**没必要因为业务是Java写的，就要求Agent引擎也必须是Java。** ”

## 七、写在最后

回到最初的问题：**Spring AI Alibaba已停更，Java该何去何从？**

**SAA没有“死”，它在“换心脏”。**

Release停了，但commit没停。

最后一个正式版在拥抱AgentScope，这是铺垫，不是告别。

**Java AI也没有“凉”，它在“分层”。** 接入层很热闹，编排层在分化，运行时层有AgentScope顶着。

**真正该做的事，不是恐慌性换框架，而是搞清楚自己的需求在哪一层。**

如果你的需求是“在Java里调用大模型、做RAG、搞工具调用”——Spring AI 2.0和LangChain4j都在，活得很好。

如果你的需求是“Graph工作流编排”——SAA依然可用，只是不再快速迭代。

如果你的需求是“让Agent自主执行长任务”——AgentScope才是答案。

**技术选型最怕的，是用“某个框架停更”的焦虑，掩盖了“我到底需要哪一层能力”的思考。**

## 八、参考资源

- Spring AI 2.0官方文档 ：https://docs.spring.io/spring-ai
- LangChain4j官方文档 ：https://docs.langchain4j.dev
- Spring AI Alibaba GitHub ：https://github.com/alibaba/spring-ai-alibaba
- AgentScope Java官方文档 ：https://java.agentscope.io
- 框架对比仓库 ：https://github.com/java-ai-in-action/framework-compare

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐14个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247536010&idx=1&sn=69cbb5fdfc59c9c636559fb556386b24&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

---
原文链接：https://mp.weixin.qq.com/s/PcjCWkWwwUYC9LxGzoQGWQ
