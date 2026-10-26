---
title: "摘要-ip2region离线ip库"
type: source
tags: [来源, IP归属地, 开源库, Java]
sources: [raw/09-archive/全网显示 IP 归属地，准确率 99.9%，这个开源的 API 离线库强大到离谱！.md]
last_updated: 2026-10-10
---

## 核心摘要
文章解释各平台"评论区显示 IP 归属地"功能的实现方式：付费开放平台 API 免费额度有限、生产环境不够用，推荐开源离线 IP 定位库 [[ip2region]]——准确率号称 99.9%、查询 0.0x 毫秒、数据库仅 10MB，支持 Java/PHP/C/Python/Node.js/Go/C# 等多语言绑定与 Binary/B 树/内存三种查询算法。Java 使用三步：引入 `org.lionsoul:ip2region:2.7.0` 依赖 → 下载 ip2region.xdb 离线库文件 → `Searcher.newWithFileOnly(dbPath)` 创建 searcher 后 `searcher.search(ip)`；结果格式为 `国家|区域|省份|城市|ISP`（缺省为 0），国内国外 IP 均支持。注意并发使用时每个线程需独立创建 searcher 对象。

## 关联连接
- [[ip2region]] — 核心开源库
- [[NginxPulse]] — 同样使用 ip2region 做日志 IP 归属地分析的产品
