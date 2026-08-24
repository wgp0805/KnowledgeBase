---
title: "同一个SOCKS5代理，为什么requests能用，aiohttp却一直报407 Proxy Authentication Required？"
source: "SegmentFault"
url: "https://segmentfault.com/q/1010000048194115"
date: "2026-08-23T15:00:10+08:00"
score: 1.0
tags: ["中文", "编程", "问答", "技术"]
auto_captured: true
---

# 同一个SOCKS5代理，为什么requests能用，aiohttp却一直报407 Proxy Authentication Required？

> **来源**: SegmentFault  
> **链接**: https://segmentfault.com/q/1010000048194115  
> **抓取日期**: 2026-08-23  
> **相关性评分**: 1.0

同一个SOCKS5代理，为什么requests能用，aiohttp却一直报407 Proxy Authentication Required？

我在使用9HTTP的动态住宅代理时，发现一个奇怪的现象：同样的代理配置（主机、端口、用户名、密码），在 requests 库中可以正常使用，但换成 aiohttp 或 httpx 就会一直报 407 Proxy Authentication Required。

这个问题卡了我两天，同样的代理信息在curl里也能用，但aiohttp就是不行，希望有大佬指点一下。

你的预期是什么？  
我希望在 aiohttp 中也能像 requests 一样正常使用SOCKS5代理，发送请求并正常返回结果。

你的环境是什么？  
Python版本：3.10.11

操作系统：Windows 11 / Ubuntu 22.04（两边都试过，现象一致）

代理服务商：9HTTP 动态住宅代理

代理协议：SOCKS5

代理地址：global.9http.com:9091（用户名密码认证）

出现问题的代码  
能正常工作的代码（requests）：

python  
import requests

proxy_url = "socks5h://username:password@global.9http.com:9091"  
proxies = {"http": proxy_url, "https": proxy_url}

response = requests.get("https://api.ipify.org?format=json", proxies=proxies)  
print(response.json())

## 正常返回代理出口IP ✅

不能正常工作的代码（aiohttp）：

python  
import aiohttp  
import asyncio

proxy_url = "socks5://username:password@global.9http.com:9091"

async def fetch():
    
    
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.ipify.org?format=json",
            proxy=proxy_url
        ) as response:
            print(await response.json())
    

asyncio.run(fetch())

## 报错：407 Proxy Authentication Required ❌

同样报错的httpx版本：

python  
import httpx

proxy_url = "socks5://username:password@global.9http.com:9091"

with httpx.Client(proxy=proxy_url) as client:
    
    
    response = client.get("https://api.ipify.org?format=json")
    print(response.json())

## 同样报407 ❌

我已经尝试过的排查步骤  
确认代理信息正确：反复核对用户名密码，在requests和curl中都能正常使用

确认认证方式：9HTTP的SOCKS5代理使用的是用户名/密码认证（RFC 1929），不是HTTP Basic Auth

确认端口和主机：global.9http.com:9091 在requests中工作正常

尝试不同的aiohttp版本：分别测试了3.8.0到3.10.0，现象一致

确认依赖安装：pip install aiohttp[socks] 已安装

我的分析  
我查了一下资料，发现可能的原因有：

aiohttp 的SOCKS5代理实现方式与 requests 不同：requests 底层依赖 urllib3，而 aiohttp 使用 aiohttp-socks 库，两者的认证握手实现可能有差异。SOCKS5的认证发生在协议级别，而不是通过HTTP头部。

httpx 同样存在这个问题：GitHub上有人讨论过类似的问题，SOCKS5代理认证在 requests 和 curl 中工作，但在 httpx 和 aiohttp 中失败。

代理服务商的认证实现可能有特殊要求：某些代理服务商（包括9HTTP）在SOCKS5认证时可能要求特定的握手顺序或编码方式。

我猜测问题出在 aiohttp-socks 和 httpx 的SOCKS5认证实现与9HTTP的代理服务器不完全兼容。希望了解这两个库底层实现的大佬指点一下，或者有没有workaround可以解决这个问题？

补充信息  
curl测试命令（可以正常工作）：

bash  
curl -x socks5://username:password@global.9http.com:9091 [https://api.ipify.org](<https://link.segmentfault.com/?enc=47l03kWzB%2FwubDMgwtJD8A%3D%3D.np7Ye3ANYTvfC85NRob%2Fqqr6guTjuYtcYeW6miWvM4s%3D>)  
报错完整信息：

text  
aiohttp.client_exceptions.ClientProxyConnectionError: Cannot connect to host global.9http.com:9091 ssl:default [407 Proxy Authentication Required]

## Python #aiohttp #代理 #SOCKS5 #httpx

确认代理信息正确：反复核对用户名和密码，在curl和requests中都能正常使用

确认认证方式：9HTTP的SOCKS5代理使用的是标准的用户名/密码认证（RFC 1929），不是HTTP Basic Auth

测试不同库版本：分别测试了aiohttp 3.8.0到3.10.0，以及httpx多个版本，现象一致

确认依赖安装：已正确安装 aiohttp[socks]

查阅GitHub Issues：搜索后发现有人遇到类似问题，但未找到明确的解决方案

了解 aiohttp 和 httpx 的SOCKS5认证实现与 requests 有何不同

确认是否有配置方式能让 aiohttp 和 httpx 正常通过SOCKS5代理认证

如果这是 aiohttp-socks 库与代理服务商兼容性的问题，希望确认以便我更换方案


---
> 原文链接: https://segmentfault.com/q/1010000048194115