---
title: "37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用"
source: "人人都是产品经理"
url: "https://www.woshipm.com/share/6466411.html"
date: "Fri, 18 Sep 2026 06:57:49 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/share/6466411.html  
> **抓取日期**: 2026-09-18  
> **相关性评分**: 1.0

> 37K Star 的 1Panel 开放了 AI 网关的独立部署能力，10 人及以下团队可以免费使用。网关能集中管理各家模型的原始密钥，给成员分配权限、按任务分配模型，也能看清每个人的调用用量，再据此调整配额。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/e8bfcd209d00acbfb11bf03271ff254b_MD5.png)

之前介绍过一个开源项目，叫 1Panel。

它是一款 Linux 服务器管理工具。

可以通过网页控制台来**搭建网站、安装应用、管理数据库、****部署 AI 应用****和做备份** ，减少手动输入命令的操作。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/fd859f8307b0cb1c465398431601c76f_MD5.png)

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/82a8a7e3b06f27054b834df83a2bb146_MD5.png)

这次，1Panel开放了AI 网关的独立部署能力。

10 人及以下团队可以免费使用。

接入后，团队使用的不同模型可以放在一起管理。

给成员分配访问权限，给应用设置用量配额、调整模型调用，都可以在网关里完成。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/9c7a69dd6a36c41c2ddfa73b9fcfb8b0_MD5.png)

## 01 团队接入网关，网关再连接模型

当你的团队接入了这个开源项目来管理 AI 模型，接入后的调用关系是：

**团队的 AI 应用 → 1Panel AI 网关 → 云端模型或本地模型**

公司的管理员先把模型资源配置到网关中，再给应用分发网关的访问地址和密钥。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/4b575e8b153b067aabd0091494087021_MD5.png)

比如团队在 DeepSeek 官方、腾讯云 TokenHub 都买了套餐。

这些 AI 大模型供应商的原始密钥可以在网关侧集中管理。

然后往下分发给团队里面的人。

> 地址：https://github.com/1Panel-dev/1Panel

下面以一个假设的 8 人团队为例。同事各自用 AI，权限和用量统一管理

同事用 AI 写文案、整理资料、辅助编程，可以在各自熟悉的工具里操作。

对于支持兼容接口、允许自定义模型地址和密钥的工具，接入 1Panel AI 网关后，就能集中管理这些调用。

给不同成员分配权限。

每人使用自己的密钥，管理员按用户组设置可用模型和配额。

人员离职或密钥泄露时，单独停用对应密钥就行了。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/03b9a4575de74be98b64475b33ea4b7c_MD5.png)

按任务分配模型。

配置智能路由后，可以让简单的整理、提取任务优先使用成本较低的模型，复杂任务再交给能力更强的模型。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/143b2f494c6feb84b4f247b2f1b170db_MD5.png)

看清每个人的用量。

网关可以查看每个人的调用次数和模型用量，帮助负责人了解谁用得多、主要用了哪些模型，再据此调整配额。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/1847761f9ca3eb9f8c9098ab67d4aa72_MD5.png)

## 02 两种部署方式

已经在使用 1Panel 的团队，可以进入应用商店，**搜索 1Panel AI 网关** ，按页面提示安装。

![](assets/2026-09-18-37K%20Star%20%E7%9A%84%20GitHub%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E5%BC%80%E6%94%BE%20AI%20%E7%BD%91%E5%85%B3%EF%BC%8C10%20%E4%BA%BA%E5%9B%A2%E9%98%9F%E5%85%8D%E8%B4%B9%E7%94%A8/6c636cd7f6c7fe4a6d4da6ef74a50740_MD5.png)

也可以通过官方 Docker 镜像独立部署。

这种方式需要准备能够运行 Docker 的服务器，并由熟悉服务器配置的成员操作：

> docker run –pull always -d \
> 
> –name 1panel-ai-gateway \
> 
> –restart unless-stopped \
> 
> -p 8080:8080 \
> 
> -v /opt/ai-gateway:/opt/ai-gateway \
> 
> 1panel/ai-gateway

首次启动后，通过日志查看管理员临时密码：

> docker logs 1panel-ai-gateway

首次登录后应修改临时密码。

官方建议将 8080 端口的访问限定在可信内网，正式使用时配置 HTTPS 反向代理，通过加密连接访问服务。

安装完成后，可以先接入一个调用情况比较熟悉的应用，给它分配独立密钥，设置可用模型和配额。

运行一段时间，确认调用正常、统计记录能帮助排查问题，再逐步接入其他应用。

作者：逛逛GitHub 公众号：逛逛GitHub

本文由 @逛逛GitHub 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自 Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/share/6466411.html