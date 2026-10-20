---
title: "推荐一款GitHub 37.2K+ Star的开源AI网关，个人和10 人及以下团队免费用！"
source: "https://mp.weixin.qq.com/s/vCjH4tuP4XmueIr7ufXF9Q"
---
冰v河 冰河技术 *2026年10月20日 09:40*

**大家好，我是冰河~~**

1Panel 原本是一款面向 Linux 服务器的开源管理工具。它把建站、应用安装、数据库管理、AI 应用部署、备份等常见运维动作放进网页控制台，让不少工作不再依赖逐条输入命令。

最近，1Panel 又把 AI 网关做成了可以独立部署的组件，并且对 10 人及以下团队免费开放。对于开始频繁调用大模型、但又不想一开始就搭复杂平台的小团队来说，这是一个比较轻量的切入点。

![图片](https://mmbiz.qpic.cn/mmbiz_png/mciaHGibPzCIR1aDPj7dCsalmfve6t8lcibkjjRicxNEcmvZ44jm2PRW8eBvrSsmBq2TZ1jqHzQG9TdOzvMZWceDrSia8qXG3kSydkXbbyw7nh50/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 调用关系：应用先连网关，网关再连模型

接入之后，团队里的 AI 应用不需要各自保存不同厂商的密钥，而是统一走一条链路：

**团队 AI 应用 → 1Panel AI 网关 → 云端模型或本地模型**

管理员先在网关中配置模型资源，再把网关的访问地址和密钥分发给应用。比如团队同时在 DeepSeek 官方、腾讯云 TokenHub 等渠道购买了服务，这些上游密钥可以集中放在网关侧管理，再由网关向下游应用或成员分发。

这样做的直接好处是：密钥不再散落在每个人的工具配置里，后续调整模型、停用某个密钥、查看调用情况，都有统一入口。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mciaHGibPzCISuv5SPt04qTs82W7ZJGiaibQjNe2VmXAsjXLVUHEicnC9zlibKmibM6ibEDkqiaicV3G7SQTldMLpUcTibEdELjPiaHLC7xXMf2VndVnpicY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

## 一个 8 人团队可以怎么用

假设团队有 8 个人，日常工作包括写文案、整理资料、辅助编程。成员仍然可以在自己熟悉的工具里使用 AI。只要工具支持兼容接口，允许自定义模型地址和密钥，就可以接入 1Panel AI 网关，把调用纳入集中管理。

管理员可以按用户组分配权限：每个人使用自己的密钥，不同组可用的模型和配额由管理员设置。这样一来，人员离职或某个密钥泄露时，不需要大范围改配置，单独停用对应密钥即可。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mciaHGibPzCIRk7mpMUoN7icYL9g9XPkosmZicob3uQEv8Fz5rwWgpFLy5RTXxPUlx1d6icvzhDDrmIehwscicKPdNejYfWGbmqT4szyP8bbzQYQg/640?wx_fmt=png&from=appmsg#imgIndex=2)

成本控制也可以通过模型分配来做。配置智能路由后，整理、提取这类相对简单的任务可以优先交给成本较低的模型，复杂任务再交给能力更强的模型。网关还能查看每个人的调用次数和模型用量，负责人可以据此判断谁用得多、主要用了哪些模型，再调整配额。

## 两种部署路径

已经在使用 1Panel 的团队，可以直接进入应用商店，搜索“1Panel AI 网关”，按页面提示安装。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mciaHGibPzCISqUZibeyhGA20DeicYqjE179her7OKP2ibfXsSjPibt1atvcZ2qyS871yv5jdKPJrN6HnVA3Om7ArVySP2hoC8LPjAs2YzSzCHEqU/640?wx_fmt=png&from=appmsg#imgIndex=3)

也可以使用官方 Docker 镜像独立部署。这种方式需要一台能运行 Docker 的服务器，并由熟悉服务器配置的成员操作：

```
docker run --pull always -d \
  --name 1panel-ai-gateway \
  --restart unless-stopped \
  -p 8080:8080 \
  -v /opt/ai-gateway:/opt/ai-gateway \
  1panel/ai-gateway
```

首次启动后，通过日志查看管理员临时密码：

```
docker logs 1panel-ai-gateway
```

首次登录后应修改临时密码。安全方面，官方建议将 8080 端口的访问限定在可信内网；正式使用时，再配置 HTTPS 反向代理，通过加密连接访问服务。

## 上线节奏：先跑通一个应用，再逐步扩展

安装完成后，不必急着把所有应用一次性接进来。可以先选一个调用情况比较熟悉的应用，给它分配独立密钥，设置可用模型和配额。运行一段时间，确认调用正常，统计记录也能帮助排查问题，再逐步接入其他应用。这样既能控制上线风险，也更容易发现配置和权限上的问题。

项目地址： [https://github.com/1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)

**好了，今天就到这儿吧，我是冰河，我们下期见~~**

推荐阅读：

[给大家推荐一款AI短剧生成平台](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515806&idx=1&sn=6214e0ec2a9ebc09b1c68eb23e818eae&scene=21#wechat_redirect)

[给大家推荐一款可直接使用的AI-CR系统](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515790&idx=1&sn=5aeda9e93df686b5e753cb9870fda0da&scene=21#wechat_redirect)

**微信扫一扫赞赏作者**

AI大模型 · 目录

阅读原文