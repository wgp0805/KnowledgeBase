---
title: "Cloudflare"
type: entity
tags: [CDN, 安全, 风控, 反滥用]
sources: [raw/09-archive/秒杀系统怎么区分真实用户和黄牛脚本？.md, raw/01-articles/2026-09-25-GitHub + Cloudflare + Picgo 搭建你的免费图床 - DominicKK.md]
last_updated: 2026-09-28
---

## 定义
Cloudflare 是全球领先的 CDN、网络安全与边缘计算服务商，提供 DDoS 防护、WAF、Bot 管理、验证码等反滥用能力。

## 关键信息
- 业务：CDN、DDoS 防护、WAF、Bot 管理、边缘计算
- 反滥用产品：[[Turnstile]]（风险驱动验证码）
- 风控理念：风险驱动——低风险访客自动通过，可疑流量才拿到交互挑战
- 官方数据：Turnstile 拦下上百万次自动化注册的同时，正常注册转化没有可观察的变化

### Workers 反代图床（2026-09，来源：[[摘要-github-cloudflare-picgo图床]])
- Workers 把图片请求拼接为 `raw.githubusercontent.com/<owner>/<repo>/<branch>/path` 并附加 `Authorization: token`，为私有 GitHub 仓库提供免暴露的外链访问
- 环境变量：`GH_TOKEN`、`GH_NAME`、`GH_REPO`、`GH_BRANCH`（可选 `URL`/`URL302` 处理根路径随机跳转/重定向）；token 也可经 URL `?token=` 传入
- 行为细节：缺 token 返回 400；上游失败返回自定义错误页；根路径返回伪装首页；可用自有域名走 Cloudflare DNS 代理绑定到 Worker

## 关联连接
- [[Turnstile]] — 风险驱动验证码产品
- [[风险驱动验证]] — 其产品体现的方法论
- [[图床]] — Workers 反代所属方案
- [[PicGo]] — 配套上传客户端
- [[摘要-github-cloudflare-picgo图床]] — 来源
- [[摘要-秒杀系统防刷分层体系]] — 来源
