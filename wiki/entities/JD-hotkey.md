---
title: "JD-hotkey"
type: entity
tags: [开源框架, 高并发, 热key, 本地缓存, 京东, 稳定性]
sources: [raw/09-archive/为什么越来越多人用JD-hotkey？.md]
last_updated: 2026-10-27
---

## 定义

JD-hotkey（hotkey-client）是京东开源的热 key 探测与高并发缓存框架（Gitee: jd-platform-opensource/hotkey）：一个独立的探测集群（Worker + Etcd + Dashboard）加一个客户端 jar 包，毫秒级判定"突然变热"的 key 并推送到应用**所有**服务器的 JVM 本地缓存，解决突发流量集中打在单个 key 上打穿 Redis 的问题。

## 关键信息

- **诞生动因**：秒杀商品详情页平时 QPS 几百、活动开始瞬间几万——Redis 集群 CPU 打满（全部请求砸同一个秒杀商品 key），Tomcat 线程池堵死（每个请求都在等 Redis）。做了缓存也被打穿：缓存解决"重复查询"，解决不了"突发流量集中打在一个 key 上"
- **架构四步**：①业务代码查 Redis 前先调 `JdHotkey.isHotKey(key)`，本地攒批每 500ms 上报 Worker；②Worker 用滑动窗口计数（规则如"2 秒内 20 次算热"）判定；③判定后经长连接推送到订阅该应用的**所有** Client，key 放进本地 Caffeine 缓存；④业务方自己去 Redis 查一次 value，调 `smartSet(key, value)` 塞进本地（只有热 key 才真正 set），之后的 `get` 直接走 JVM 内存零网络开销
- **探测与缓存解耦**：框架只负责判定并推送"这个 key 热了"，不替业务存 value——同一套代码自动适配冷/热两种状态，不需要写两套逻辑；还可用判定结果做限流、熔断、黑名单拦截
- **性能**：每 10 秒处理 270 万–310 万 key（约 30 万 QPS）；protobuf 序列化后秒级 36 万+ 稳定 CPU 60%，压测 5 小时+ 无异常；1 台 Worker 撑 1000 台业务服务器，比扩容 Redis 集群成本低太多
- **优点**：轻量完全不依赖 Redis、不改 Redis 源码；探测与缓存解耦灵活性高；集群一致（热 key 推送到所有服务器 JVM，不会 A 机热 B 机不热）；毫秒级响应（秒杀也能扛）；成本低；京东大促验证（历经 2020 年 618/双 11，日探测数十亿 key，捕获大量爬虫和刷子用户）
- **缺点**：需额外部署 Etcd 集群（规则与地址同步）+ Worker 集群（计算）+ Dashboard（配规则）；业务代码需显式调用 isHotKey（非零侵入）；框架本身不存 value（本地缓存被淘汰仍要回 Redis 查）；阈值需按业务调优（太敏感误判浪费内存、太迟钝热 key 先打穿 Redis）
- **接入**：Maven 坐标 `com.jd.platform:hotkey-client`；application.yml 配 `app-name`/`etcd-server`/`caffeine-size`（默认 5 万条）/`push-period`（默认 500ms）
- **适用场景**：秒杀/大促商品详情、爬虫/刷子用户识别（isHotKey 判用户 ID 高频访问直接限流）、热接口熔断、Redis 热 key 本地缓存、黑名单用户本地缓存；小流量内部系统与无突发流量业务不推荐
- **效果**：大促期间经 hotkey 探测出的热 key 本地缓存占应用总访问量 50%+，多数请求走本地查询，减轻 Redis 层一半以上负担

## 关联连接

- [[摘要-jd-hotkey热key探测]] — 来源
- [[热key探测]] — 核心方法论概念
- [[热点Key]] — 问题本体
- [[京东]] — 出品方与验证方
- [[Caffeine]] — 客户端本地缓存实现
- [[Etcd]] — 规则与 Worker 地址同步组件
- [[多级缓存]] — 本地缓存所处的缓存架构
- [[秒杀系统]] — 典型触发场景
- [[苏三]] — 来源作者
