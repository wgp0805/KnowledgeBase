---
title: "IP伪造防护"
type: concept
tags: [安全, IP, 代理, Tomcat]
sources: [raw/01-articles/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md]
last_updated: 2026-08-12
---

## 定义
IP 伪造防护是指防止恶意客户端通过直接设置 [[X-Forwarded-For]] 等请求头来冒充其他 IP 地址的安全措施。核心原则：永远不要信任客户端直接传递的任何 IP 相关信息。

## 伪造原理
HTTP 请求头可被客户端任意构造。攻击者在请求中直接设置 `X-Forwarded-For: 1.2.3.4`，若应用无条件信任该头字段，则会误判来源 IP，导致：
- IP 黑名单绕过
- 频率限制规避
- 审计日志污染
- 地域访问控制失效

## 防护方案

### Tomcat internal-proxies 配置
通过 `internal-proxies` 正则表达式指定信任的内网代理 IP 段：
```
192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}
```

**机制**：Tomcat 仅当 `getRemoteAddr()` 匹配 `internal-proxies` 时才解析 X-Forwarded-For，否则忽略该头字段。客户端直接请求（非经可信代理）的 XFF 会被忽略。

### 应用层过滤
- 内网 IP 段过滤：10.x、192.168.x、172.16-31.x
- IP 格式校验：IPv4 正则 + IPv6 判断
- unknown 值排除：过滤 `"unknown"` 字符串

## 关联连接
- [[X-Forwarded-For]] — 伪造的目标头字段
- [[代理链路]] — 可信代理的识别依据
- [[Tomcat]] — internal-proxies 配置入口
- [[IP限流]] — 伪造防护的下游应用
- [[摘要-springboot获取真实客户端ip]] — 完整防护方案
