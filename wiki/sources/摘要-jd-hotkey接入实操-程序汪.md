---
title: "摘要-jd-hotkey接入实操-程序汪"
type: source
tags: [来源, 原始文件, 热key, 高并发, 本地缓存]
sources: [raw/01-articles/2026-11-25 - 为什么越来越多人用 JD-hotkey？.md]
last_updated: 2026-11-26
---

## 核心摘要
程序汪视角拆解京东开源的 JD-hotkey 原理与接入方式，与已有 [[摘要-jd-hotkey热key探测]]（苏三视角，侧重"核心矛盾是探测不是缓存"）互补——本文更偏**接入实操**：四组件架构、客户端初始化代码、规则配置 JSON、业务代码四种用法、以及六条实际使用的注意点。背景数据：经 2020 年 618 与多次压测，线上每天探测 key 数十亿计，worker 单机压测 QPS 可达 35 万。

## 关键信息
- **热 key 不处理的后果**：Redis 单 key 请求都落到同一线程同一台机器，热点集中时网卡和 CPU 先到上限；key 同时过期则大量请求穿透到数据库即缓存击穿。处理思路是请求到达 Redis/DB 之前由 client 把每次访问的 key 上报给独立 worker 集群统计，超阈值判为热 key 推送到该应用所有机器 JVM 内存，之后直接读本地 Caffeine 缓存不再访问 Redis。热用户/热接口同用法，区别在业务侧拿到判断结果后怎么处理（热商品本地缓存 / 热用户直接拒绝 / 热接口熔断或返回默认值）
- **四组件**：etcd 集群（配置中心，存规则/worker 地址/探测出的热 key，提供监听订阅）、client jar（引入业务系统，负责 key 上报/监听变更/热 key 本地缓存）、worker 集群（独立 Java 程序，接收上报 key 累加计算判定后推送）、dashboard 控制台（配规则/查看和手工增删热 key/记录探测历史）。整个框架不依赖 Redis，client 与 worker 走 Netty 长连接，worker 无状态多机分摊连接，扩容把新节点注册到 etcd 后 client 自动感知
- **客户端接入**：Gitee 开源（jd-platform-opensource/hotkey），先打包到本地仓库或私服再引 `com.jd.platform.hotkey:hotkey-client:1.0-SNAPSHOT`；应用启动 `@PostConstruct` 里 `ClientStarter.Builder()` 设 appName（须与控制台一致）/etcdServer（多个逗号分隔）/caffeineSize（默认 5 万）/pushPeriod（默认 500ms）后 `startPipeline()`
- **规则配置 JSON 示例**：`{"key":"product_","prefix":true,"interval":2,"threshold":20,"duration":600}` 即商品 key 2 秒内被访问 20 次判为热 key、本地缓存 10 分钟
- **业务代码 JdHotKeyStore 四方法**：`isHotKey`（判断是否热 key 同时上报访问）、`get`（只读本地缓存）、`smartSet`（仅在 key 为热 key 时写入缓存）、`getValue`（读不到时自动上报）。商品查询写法：`isHotKey(key)` 为 true 时先 `get` 命中就返回，未命中查 DB 后 `smartSet` 回写；黑名单场景只取判断结果 `if(isHotKey("black_user_"+userId)) throw`
- **六条注意点**：①`isHotKey` 每次调用都上报计数，一个请求别重复调同一 key、需多次判断先存结果；②`push-period` 非越小越好，单机 QPS 不高保持默认 500ms，调太小产生大量空上报；③客户端依赖较新版本 Guava，老项目版本过低先升级或排冲突否则启动报 NoSuchMethodError；④热 key 缓存的是 JVM 内存，规则 duration 要结合业务数据更新频率设，避免长时间存旧数据；⑤worker 至少部署两台，client 同时保持多条长连接，单台下线不影响探测；⑥控制台支持手工添加热 key，大促前把已知活动商品提前录入不用等流量上来再探测

## 关联连接
- [[JD-hotkey]] — 主角实体（含苏三视角的完整原理与优缺点）
- [[摘要-jd-hotkey热key探测]] — 同主题另一视角来源（苏三，"核心矛盾是探测不是缓存"）
- [[热key探测]] — 核心方法论概念
- [[热点Key]] — 问题本体
- [[Etcd]] — 配置中心组件
- [[Netty]] — client-worker 长连接
- [[Caffeine]] — 本地缓存实现
- [[缓存击穿]] — 热点集中+过期导致的穿透问题
- [[程序汪]] — 来源作者
