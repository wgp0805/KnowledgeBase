---
title: "ip2region"
type: entity
tags: [开源库, IP归属地, 离线定位, Java]
sources: [raw/09-archive/全网显示 IP 归属地，准确率 99.9%，这个开源的 API 离线库强大到离谱！.md]
last_updated: 2026-10-10
---

## 定义
ip2region 是开源离线 IP 地址定位库（GitHub 搜索 ip2region，Maven 坐标 `org.lionsoul:ip2region`），用于把 IP 地址转为地理归属地信息，是各平台"评论区显示 IP 归属地"一类功能的典型底层实现，也是 [[NginxPulse]] 等日志分析产品的归属地查询引擎。

## 关键信息
- **性能与体积**：准确率号称 99.9%，查询耗时 0.0x 毫秒级，离线数据库文件仅约 10MB——相比收费开放平台 API（免费额度有限）更适合生产环境
- **多语言与多算法**：提供 Java、PHP、C、Python、Node.js、Golang、C# 等查询绑定；支持 Binary、B 树、内存三种查询算法
- **结果格式**：`国家|区域|省份|城市|ISP`，缺省地域信息为 0（示例：`中国|0|河北省|保定市|联通`）；国内国外 IP 均支持
- **Java 使用三步**：① 引入依赖 `org.lionsoul:ip2region:2.7.0`；② 下载离线库文件 `ip2region.xdb`；③ `Searcher.newWithFileOnly(dbPath)` 创建 searcher → `searcher.search(ip)` 查询 → 用完 `searcher.close()`
- **并发注意**：并发使用时每个线程需要独立创建一个 searcher 对象，不可共享

## 关联连接
- [[摘要-ip2region离线ip库]] — 来源
- [[NginxPulse]] — 采用本库做日志 IP 归属地分析的产品
