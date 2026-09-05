---
title: "Cloudflare"
type: entity
tags: [CDN, 安全, 风控, 反滥用]
sources: [raw/01-articles/秒杀系统怎么区分真实用户和黄牛脚本？.md]
last_updated: 2026-08-20
---

## 定义
Cloudflare 是全球领先的 CDN、网络安全与边缘计算服务商，提供 DDoS 防护、WAF、Bot 管理、验证码等反滥用能力。

## 关键信息
- 业务：CDN、DDoS 防护、WAF、Bot 管理、边缘计算
- 反滥用产品：[[Turnstile]]（风险驱动验证码）
- 风控理念：风险驱动——低风险访客自动通过，可疑流量才拿到交互挑战
- 官方数据：Turnstile 拦下上百万次自动化注册的同时，正常注册转化没有可观察的变化

## 关联连接
- [[Turnstile]] — 风险驱动验证码产品
- [[风险驱动验证]] — 其产品体现的方法论
- [[摘要-秒杀系统防刷分层体系]] — 来源
