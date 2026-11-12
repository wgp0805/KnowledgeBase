---
title: "Coze 下线了，开源版 WorkBuddy 来了"
source: "https://mp.weixin.qq.com/s/p9KyqXPYcdrb2zjMzNd7Jg"
author:
  - "[[cxuanAI]]"
published:
created: 2026-11-12
description:
tags:
  - "clippings"
---
苏三说技术 *2026年11月12日 08:20*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

Coze 在 10 月 29 日发布了一份产品整合升级公告，给现有企业套餐列出了下线时间表。

![扣子企业版下线公告](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQS3ETcBaSZV2KtensLAJN3waq8mU3fq4FIfwYc24ttryXpicKnFSP4ibMgY0iaBTz0senUDt8ib5CKXtA5RjagL21Cc9nRtkttgtL4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

*图源：扣子官方公告。*

看到这份公告，还是挺感慨的。

扣子之前有多火？我说个实际的例子，我在二线，当时我们隔壁公司调查企业级部署就用的 Coze 。

这也能理解，毕竟当时 Coze 把知识库、插件工作流全都放在了一个界面，你拖几个节点就能搭建 AI 应用了，很多人第一次接触 Agent、第一次跑通工作流，用的就是它。

所以这次 Coze 的官方声明，我看了还是挺感慨的，这就意味已经把业务放上去的企业来说，确实的重新考虑一下了。

而且好像 dify 也没啥声音了。

**我觉得企业选 Agent 平台，得看能不能长期掌握自己的知识、流程和部署环境，放到更靠前的位置。**

这也是我这次在想着看看有没有开源项目的原因。

这次我找到了一个项目：

![image-20261110001350386](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQTZmy4mPIwwML5yEWxflwIOXMbNk3cg9awLYOvscLjzibS2yrl1C5cuqicwxxEicN6TqjFsD6YSPFMrB7u7cNxJOH4AgfDticA8utE/640?wx_fmt=png&from=appmsg#imgIndex=1)

项目 repo： [https://github.com/dataelement/bisheng](https://github.com/dataelement/bisheng) ，目前已经有 1.2w star 了，从 Issue、PR 和 Contributors 上来看，很活跃。

![image-20261109140023895](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQStRdt9Bo0767s8Nj5kDiaaK8HiaGzKVic7Xiakh84bEuPCJdhXpGlpLj6lmicnuWH3c0cA7yqStP23M0o0ficPakgLa0Xs2ofCCohPU/640?wx_fmt=png&from=appmsg#imgIndex=2)

image-20261109140023895

这是 BISHENG 团队做的开源项目。

**这是一个可以私有化部署的开源企业级 Agent 平台。** 模型、知识库、工作流，可以放到企业自己管理的环境里，再围绕实际业务搭建 AI 应用。

同时它也是一个开源 AgentOps，专攻办公效率场景，能帮助公司或团队搭建一个 Agent 平台，模型、知识、工具和使用权限。

我之前在 DeepSeek Harness 官方桌面端发布之前，曾介绍过一款第三方客户端—— `DSH Desktop` ，这个也是他们做的。

重新看了一下 DSH Desktop ，这次有 93w + 的下载量了，之前我写文章的时候，才 23w+ ，这才过了俩月。。增速真离谱。

![image-20261109140815571](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQRQkaL6vsFTib3R9LMia4QgwQ5XsnrBTfl5Ug60afV3KB6XWLd5icNdy18HsArfwfSnf1sKyRH5UCAbh2qRaYJEo3c8ga9lN9SmjY/640?wx_fmt=png&from=appmsg#imgIndex=3)

image-20261109140815571

而这个 BISHENG 的桌面端，就是围绕 DSH Desktop 做了改造。

**可以把它理解为一个开源的 WorkBuddy 或者豆包工作，让企业把 AI 能力掌握在自己手中。**

最近建了一些AI技术交流群，加我微信：li\_su223，备注：AI，即可进群交流和学习，获取最新资讯。

## 安装部署

下面我就实操部署跑一下这个 BISHENG 的开源项目，看看到底咋样。

我这次用的是 Mac + OrbStack，部署版本固定在 [v3.0.0。平台通过](http://v3.0.0.xn--kpr97vp33bqja/) Docker Compose 运行，我把检查环境、调整镜像和启动服务这些操作交给了本机 AI。

手动部署也有现成的脚本。准备好 Docker 和 Docker Compose 后，下面是下载固定版本、运行官方安装脚本的基础流程：

```
git clone --branch 
            v3.0.0
           --depth 1 
            https://github.com/dataelement/bisheng.git
          
cd bisheng
bash docker/
            install.sh
```

脚本会准备配置、拉取镜像并启动服务。

如果你也想交给 AI 来装，可以直接用这段：

```
帮我在本机部署 BISHENG 
            v3.0.0：https://github.com/dataelement/bisheng。
          
按官方 Docker Compose 方式安装，先检查系统架构、内存和端口占用，选择兼容镜像，保留已有 Docker 服务。
完成后检查服务健康状态，给我访问地址和启动、停止方法。以浏览器能打开注册页为完成标准。
```

所以手动安装和 AI 辅助安装，底下跑的都是这套 Docker 服务。

本机部署完成后，打开 `http://127.0.0.1:3001/` ，先注册账号。默认第一个注册用户会成为管理员。

![image-20261109143542366](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQQWTGBbOQ1UuZ9GGE8Jnya7yHXa2Ss2ezULDxHHfK9MWN4cicr0iaRmicVr5jjCWLa1u10vA0TCIRnicN74sSWz3lcw4wLcG6Ytdt4/640?wx_fmt=png&from=appmsg#imgIndex=4)

登录后先看到统计看板。刚装完还没有创建应用和知识库，显示 0 或暂无数据很正常。

![image-20261109162612663](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQQSk8k10gibl8S9HTnrWkUSywMqaBibTmQpSZbibdoR4EXPT3FJpJVKmQYwfoXbD6YXlKlpgOARTzDl5RhWYwLWEgjfEz7nXC5v7o/640?wx_fmt=png&from=appmsg#imgIndex=5)

## 企业级 DSH 内核

由于这种方式是直接启动了一个 webui 版本，如果你想要桌面端的话，需要从这里下载。

![image-20261109173015642](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQTJNOibyyFnbclRdvFEXcTG2cesKBZiaCbN7yeXdqjoMiasd7vCZ3h5ZeqMI9AWNdAPCHbGiaibu0LWra2026SKUdibFRibJDgcwyZKy0/640?wx_fmt=png&from=appmsg#imgIndex=6)

这里两个产品的关系要捋一下：DSH Desktop 是桌面 Agent 的基础，BISHENG 客户端在这个基础上连接企业平台。网页平台负责搭建和管理，桌面端让员工调用平台资源、处理日常工作。

所以可以看出，这次 DSH Desktop 是和 BISHENG 桌面端打通了。

我先在桌面端的设置 → 模型里配置了 DeepSeek，填入自己的 API Key。

![image-20261109173815217](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQTCoZMvPjKjFE3AdakZQoob9fNyf8ZUl6Gia74RicQiaJOibJrEEoU7OEbdCK6svbl3CO22iaia5ASedaj0ICXZhTTERtLlA0tj00CFo/640?wx_fmt=png&from=appmsg#imgIndex=7)

由于我本机是用的是 OrbStack ，部署上面的企业端之后，OrbStack 会给 BISHENG 容器提供一个 **HTTPS 地址** ，把这个地址配置到企业账号企业平台地址就能登录了。

![image-20261109182835148](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQSKz34ls4UGE3sgIhb0icP7EB2KibV9vBVUntEPC1o5h3tW8Harr7yblYOgbibWR8cqiaWeqVFnJzw3lqibyRGYt8pU8pH6L72MT2Qc/640?wx_fmt=png&from=appmsg#imgIndex=8)

image-20261109182835148

如果大家不会配置，可以直接让 AI 来配置。

<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="146" style="display:block;width:100%;max-width:100%;height:146px;" role="img" aria-label="插图"><foreignObject x="0" y="0" width="100%" height="146"><section xmlns="http://www.w3.org/1999/xhtml" style="display: block;box-sizing: border-box;width: 100%;max-width: 100%;height: 146px;overflow: hidden;border-radius: 10px;border: 1px solid #d6e1f7;background: #f7f9fe;background-color: #f7f9fe;"><section style="display: block;box-sizing: border-box;width: 100%;height: 42px;line-height: 42px;padding: 0 18px;font-size: 12px;letter-spacing: 0;white-space: nowrap;overflow: hidden;text-overflow: ellipsis;color: #53627a;background: #edf3ff;border-bottom: 1px solid #d6e1f7;font-family: -apple-system, &quot;PingFang SC&quot;, &quot;Helvetica Neue&quot;, &quot;Microsoft YaHei&quot;, sans-serif;"><span style="display: inline-block;vertical-align: middle;box-sizing: border-box;margin-right: 10px;padding: 3px 7px;border-radius: 4px;font-size: 10px;font-weight: 700;line-height: 18px;letter-spacing: 0.08em;font-family: &quot;JetBrains Mono&quot;, Menlo, Consolas, monospace;color: #ffffff;background: #1a5eff;"><span leaf="">Prompt</span></span> <span style="vertical-align: middle;font-weight: 500;color: #53627a;"><span leaf="">上下滑动查看</span></span> <span style="vertical-align: middle;margin-left: 8px;font-variant-numeric: tabular-nums;font-family: &quot;JetBrains Mono&quot;, Menlo, Consolas, monospace;color: #1a5eff;"><span leaf="">3 行</span></span></section><section style="display: block;box-sizing: border-box;width: 100%;height: 104px;overflow-y: auto;overflow-x: hidden;-webkit-overflow-scrolling: touch;padding: 16px 18px;scrollbar-color: #9db3df transparent;scrollbar-width: thin;"><section style="display: block;box-sizing: border-box;margin: 0;padding: 0;background: transparent;font-family: &quot;SFMono-Regular&quot;, &quot;JetBrains Mono&quot;, &quot;PingFang SC&quot;, &quot;Microsoft YaHei&quot;, monospace;font-size: 14px;line-height: 24px;color: #24324a;"><section style="display: block;box-sizing: border-box;min-height: 24px;margin: 0;padding: 0;white-space: normal;word-break: break-word;overflow-wrap: anywhere;"><span leaf="">帮我把 BISHENG 桌面端连接到已经部署的 BISHENG WebUI，做到能成功登录即可。</span></section><section style="display: block;box-sizing: border-box;min-height: 24px;margin: 0;padding: 0;white-space: normal;word-break: break-word;overflow-wrap: anywhere;"><span leaf="">检查平台的 HTTPS 地址，启用服务端桌面接入，处理本地证书信任，然后发起浏览器登录。</span></section><section style="display: block;box-sizing: border-box;min-height: 24px;margin: 0;padding: 0;white-space: normal;word-break: break-word;overflow-wrap: anywhere;"><span leaf="">密码和验证码由我填写。以桌面端实际显示我的账号为成功标准，并告诉我下次如何启动。</span></section></section></section></section></foreignObject></svg>

上面的 webui 形式是企业端，它像 Coze 一样会包含很多企业级的模块，比如文档知识库、测评、标注、权限和模型额度分配、审计等。

## Chat/Work 双模式切换

BISHENG 桌面端模式分为两种

Chat模式：适用于简单问答，快速响应。网页端、桌面端、手机端三端数据同步。

Work模式：适用于复杂任务，基于电脑本地文件持续工作。内置了 Office 三件套的模板能力。

![image-20261109195634537](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQQ9YLE0uwRKfiaYhC3RjtmlQia84V70r1cISXxicPPUe6Kdc2OMgYsiaGpKC4g7qLLtzVl5iaqP3dppNvsbG5iakSWjoFxib6iczvqbTyw/640?wx_fmt=png&from=appmsg#imgIndex=9)

我基于 2024 - 2025 年蔚小理的车辆销售情况，然后搭配这个 Blue Professional 模板做了一个 PPT 给大家看下效果，我觉得这达到了企业汇报的效果，因为我们公司每年的年终述职做的还没这个视觉好。

，时长00:13

<video src="https://mpvideo.qpic.cn/0bc3iiaayaaacqaowgxsgbvfaqwdbrbaadaa.f10002.mp4?dis_k=34a64a96733b00c7b3891861708eb1bb&amp;dis_t=1794444103&amp;play_scene=10120&amp;auth_info=SeuS3e5+Yw9356OOo3YpF0FqMGhPbT8aMVVTKztdAk5vdDRDXTYcdQZ2ZzJZTSU0&amp;auth_key=17f803a3bf816ca50045406e147ea1b6&amp;vid=wxv_4776667334516162561&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

## 搭一个 workflow

回到企业版中。

我们重点讲一下这个构建，也就是 AI 圈俗称的 `build` ，后续我们也要用 build 来称谓，没啥就是装个 B 。

ok ，我们看一下有哪些东西需要 build 。

BISHENG 内置了一些应用模板可以 build ，我们选择一个研究下，这次就选这个文章助手看看。

![image-20261109214302494](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQR42PraBzADsVDJllMdOdYQn5sPUaZ3kb6u6xduLE1NQAOMssb9rEibdgBfCujXkjwjvpAaLY9a67dKphC0wtt5JPVSPOKuecx8/640?wx_fmt=png&from=appmsg#imgIndex=10)

ok ，可以看到有非常多的节点啊，这每个节点都可以自定义。

![image-20261109214553435](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQSNISvd5kDt3JeLhqoEpSn4p2JibPkRiaeibnpBcnicQY2891RtiaZaApQCZrDtS6jvuqXCBzcnSEfM2aR1FRK6mfsEVywcyHRUQXtU/640?wx_fmt=png&from=appmsg#imgIndex=11)

比如我就用一些工具节点来自己绘制了一个 workflow。

![image-20261109223836837](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQRZ95s5E7OyciaQibKibOEeub644s0dHUX496s7qUJjWa7Lkc1u1LRWicAibW4IAf8PzDsos36hNhLbibBsWMXN29LOcjOQ1ibdgad53s/640?wx_fmt=png&from=appmsg#imgIndex=12)

点击右上侧的运行，可以实际跑一下这个 workflow 。

比如我就用这个 workflow 研读了一下 [DeepSeek-V4.1-Flash](http://deepseek-v4.1-flash/) 的论文。

![image-20261109224636912](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQTkgxX4qGZyrDneHibjGMGQx4exL5uf93ufXzUp9IKiarUibszst3CXsWTntklARTfA1LsibiafWHibw4dsb679y3xZNVTQ9WwPRThPg/640?wx_fmt=png&from=appmsg#imgIndex=13)

## 托管 Vibe 应用

还有一个玩法是，我们现在不是一般都 Vibe 很多 app 出来么，现在 BISHENG 这个企业端可以一键托管你的 app ，供员工使用和访问，也方便企业统一管理。

我觉得很多企业应该会喜欢这个功能。

桌面端 Agent 帮助员工完成个人任务， **团队还会不断产生新的需要团队协作的应用需求** ：一张培训报名表、一个项目台账、一套部门数据看板。并非所有需求都适合对话或工作流，有些工作，或许更需要一个专门的应用来承载。

用户可以继续使用熟悉的开发工具，也可以借助 Coding Agent，在本地完成页面设计与业务逻辑开发。

在 build 的首页，可以看到我们刚刚创建的 app 。

![image-20261110001009564](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQQ0VVHLygD5hft3fHuCN7TdXLu4BZTd922jKQO86uUyu2FDMr1dmueQ2JjfymUdDRpHMxmwFxWTk5m0uQnaE5s9skPjEIs4ic7s/640?wx_fmt=png&from=appmsg#imgIndex=14)

开发完成后，提交到 BISHENG 平台，应用会依次经过 **预检、密钥扫描、构建与发布审批** 。审批通过后会让你的 Vibe 应用成为团队共享的业务工具。

比如下面这张图就是 BISHENG 团队非研发团队开发的部分业务应用：

![075e36387cf101ccbc8f5565f4ff2748](https://mmbiz.qpic.cn/mmbiz_png/62IfW4JXnQQTYHx5ooPrAKrQdkeB9dTNEXP88TEobkRQbWV1tzzPJ3460nzOmUdBibc0JfoE0ibvSdrWyFo4IccnFEZ31iahkVYnJw5sbP1e0c/640?wx_fmt=png&from=appmsg#imgIndex=15)

## 模型、用量和权限，企业统一管理

在客户端 -> 模型权限这块，可以按部门和角色分配模型。

![image-20261109200307441](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQRicBTPbm4zI80ZEgOAyyibOiaQICFFM70w0mz56iaoINj5WNZgIv84TX8Iak9z0kicljh0nasBkXwzSW8fPFu7VTpAL4qjMKO3mqP4/640?wx_fmt=png&from=appmsg#imgIndex=16)

在用量这块，可以看到按部门和角色的用量信息。

![image-20261109213919442](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQTextYTq4U8kZRc5wdYib3icqFtJibqGx6V95a7ic0ia1uibA9PIpdP3CyibD8pHCf8T0gYuVia9xxaGhoFwwF0Nr98pbz0eq7w6GzwD5w/640?wx_fmt=png&from=appmsg#imgIndex=17)

在左侧的积分设置可以按照部门和角色分配积分，保证积分限额情况，比如我刚给自己分配了 1w 积分，我太开心了。

![image-20261109201906665](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQRrdymrYaFM0K6omuWkos9WicmInsZTKuW1bLvXicwPAvbibNsyPhVhOdCdDdXFwRy0Q6iaQP0Q7ha8CNxdicBgJmHHHGdNkrrzvh2Y/640?wx_fmt=png&from=appmsg#imgIndex=18)

然后下面就是审计、审批和组织架构这块了，企业可按自身管理规则，自动审查员工在客户端调用模型时发送的内容、AI 返回的结果，以及相关工具调用中传入的敏感或涉密信息。

![image-20261109202429693](https://mmbiz.qpic.cn/sz_mmbiz_png/62IfW4JXnQSojpS4U1hkm8cn8je2mSxuSB6mFUUicx8Yaia5hiawOyfIpw4MpJ2gAPO81vThRcVxFNx7JXpXWfsogNdC40k7Te65RDZeG01QqQ/640?wx_fmt=png&from=appmsg#imgIndex=19)

同样还支持自建知识库、根据知识库创建数据集、同时也可以做模型微调等。

---

## 写在最后

这次从安装、连接桌面端，到做 PPT、搭 workflow 跑下来。

我觉得这个 BISHENG 的开源项目价值挺明确： **让员工把 AI 用进日常工作，也让企业便于管理。**

员工可以在桌面端围绕文件做任务，企业统一管理模型、知识、工具和使用权限。

个人可以直接下载开源的 DSH Desktop 个人版客户端，自己配好模型就能用。

公司则可以部署开源的 BISHENG 平台，然后按自己的需求配置模型、知识库、工具等内容，再让员工通过 BISHENG 桌面端登录使用。

对企业来说，应该比较在意的还是长期使用这件事，恰好 BISHENG 团队在一直维护。

虽然工具会变，但已经积累的知识和业务流程，最好掌握在自己手里。

相关开源推荐：

[https://github.com/dataelement/bisheng](https://github.com/dataelement/bisheng)

[https://github.com/dvsusan/susanSayJava](https://github.com/dvsusan/susanSayJava)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)