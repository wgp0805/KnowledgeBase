---
title: "为什么越来越多人用JD-hotkey？"
source: "https://mp.weixin.qq.com/s/Fez_OBpTqJYNnuu6EwQXiw"
author:
  - "[[苏三]]"
published:
created: 2026-10-27
description:
tags:
  - "clippings"
---
苏三 苏三说技术 *2026年10月27日 08:37*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

大家好，我是苏三。

不知道你有没有做过秒杀系统。

最近有球友反馈说他们有一个秒杀商品详情页，平时 QPS 也就几百，结果活动一开始，瞬间冲到了几万。

Redis 集群的 CPU 直接打满，因为所有请求都砸在同一个 key 上——就是那个秒杀商品的 ID。

应用层的 Tomcat 线程池也堵死了，因为每个请求都在等 Redis 返回。

但明明做了缓存，为什么还是被打穿了？

我问他：“你知道这个 key 什么时候会变热吗？热了之后，你的应用知道吗？”

他愣了一下：“不知道。我们是事后看监控才发现 Redis 扛不住的。”

**这就是问题所在。**

缓存解决的是“重复查询”的问题，但它解决不了“ **突发流量集中打在一个 key 上** ”的问题。

当几万个请求同时要查同一个商品，Redis 就算有缓存，也扛不住这么高的并发读。

而 **JD-hotkey** ，就是京东专门为了解决这个问题开源的框架。

它的思路非常直接： **既然你知道这个 key 热了，为什么不把它直接推到每一台应用服务器的 JVM 内存里？**

今天这篇文章就专门跟大家一起聊聊这个话题，希望对你会有所帮助。

## 一、热 key 到底是个什么“热”法？

有些小伙伴可能会说：“热 key 不就是访问量大的 key 吗？我加个本地缓存不就行了？”

加本地缓存，前提是 **你得知道哪个 key 该加** 。

问题就在这。

**热 key 是“突发”的，不是“预设”的。**

一个普通商品，平时没人看，结果因为主播一句话、或者平台一个推送，瞬间变成爆款。

这个“变热”的过程可能只有几秒钟。

你不可能提前给所有商品都加本地缓存——那是几百万个 key，内存根本放不下。

京东给出的数据很直观： **在大促期间，由 hotkey 探测出的热 key 产生的本地缓存，占应用总访问量的 50% 以上** ，使得大部分请求进行的是本地查询，减轻了 Redis 层一半以上的负担。

**所以热 key 的核心矛盾不是“缓存”，是“探测”。**

你得先知道谁热了，才能决定把谁推到本地内存。

## 二、JD-hotkey 到底是怎么“探”的？

JD-hotkey 的架构非常轻量，它 **完全不依赖 Redis** ，也不改 Redis 源码。

它就是一个独立的探测集群，配合一个客户端 jar 包。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8JD-hotkey%EF%BC%9F/f0744c69c6377f0b4710351dbc72cb51_MD5.jpg)

**整个流程就四步：**

**第一步，Client 端收集。**

你的业务代码在查 Redis 之前，先调用 `              JdHotkey.isHotKey(key)            ` 。这个调用会告诉框架“我要查这个 key”。框架在本地攒着，每 500ms 批量上报给 Worker。

**第二步，Worker 端累加。**

Worker 收到各个 Client 发来的 key，用滑动窗口做计数。比如规则配的是“2 秒内出现 20 次算热”，Worker 就盯着这个窗口，到了 20 次立刻判定为热 key。

**第三步，推送回 Client。**

Worker 判定热 key 之后，通过长连接直接推送到 **所有** 订阅了该应用的 Client 端。Client 收到后，把 key 放进本地的 Caffeine 缓存。

**第四步，业务方决定怎么用。**

框架只负责告诉你“这个 key 热了”，不负责帮你存 value。你拿到 `isHotKey` 返回 `true` 之后，自己去 Redis 查一次 value，然后调用 `smartSet(key, value)` 把 value 塞进本地缓存。后续请求再进来， `get(key)` 直接从 JVM 内存里拿， **连 Redis 都不用碰** 。

**这就是它最巧妙的地方：探测和缓存解耦。**

框架只做“指路”，你决定“怎么走”。

## 三、代码实战：接入只需要几行

### 3.1 引入依赖

JD-hotkey 的 Client 端是标准的 Maven jar。由于项目在 Gitee 上，你需要先 clone 源码打包，或者使用企业内部的私服坐标。

```
<dependency>
    <groupId>
            com.jd.platform
          </groupId>
    <artifactId>hotkey-client</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

### 3.2 配置 application.yml

```
hotkey:
  app-name: your-app-name   # 必须，用于 Worker 端区分应用
  etcd-server: http://127.0.0.1:2379  # Etcd 地址
  caffeine-size: 50000      # 本地缓存最大条数，默认 5 万
  push-period: 500          # 上报间隔(ms)，默认 500ms
```

### 3.3 在业务代码里使用

这是最关键的一步。

**你需要在查 Redis 之前，先问一句 hotkey** 。

```
@Service
publicclass ProductService {

    @Autowired
    private JdHotkey jdHotkey;

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    public Product getProduct(String productId) {
        // 1. 先问：这个 key 热不热？
        // isHotKey 内部会上报 key，让 Worker 去算
        if (
            jdHotkey.isHotKey(
          "product_" + productId)) {
            // 2. 热 key：先看本地有没有
            Object cached = 
            jdHotkey.get(
          "product_" + productId);
            if (cached != null) {
                return (Product) cached;
            }
            // 本地没有，去 Redis 查一次，然后塞进本地
            Product product = (Product) 
            redisTemplate.opsForValue().get(
          "product_" + productId);
            if (product != null) {
                
            jdHotkey.smartSet(
          "product_" + productId, product); // 只有热 key 才会被 set
            }
            return product;
        }

        // 3. 非热 key：正常走 Redis
        return (Product) 
            redisTemplate.opsForValue().get(
          "product_" + productId);
    }
}
```

**逻辑解读：**

- `isHotKey` 返回 `false` ：说明这个 key 目前不热，走正常 Redis 查询。但 **这个调用本身已经把 key 上报给了 Worker** ，Worker 会开始计数。
- `isHotKey` 返回 `true` ：说明 Worker 判定它热了。先去本地 Caffeine 里找，找到直接返回， **零网络开销** 。找不到再去 Redis 查一次，然后用 `smartSet` 塞进本地。
- `smartSet` 的行为很关键： **只有热 key 才会被真正 set** 。非热 key 调用它什么也不做。

**这意味着你不需要写两套逻辑。**

同一段代码，自动适配“冷”和“热”两种状态。

## 四、性能到底怎么样？

每10秒打印一行，totalDealCount代表处理过的key总量，可以看到每10秒处理量在270万-310万之间，对应每秒30万左右QPS。

仅需要很少的机器，即可完成海量key的实时探测计算推送任务。比扩容redis集群规模成本低太多。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8JD-hotkey%EF%BC%9F/f947498c7282cfd984a0f8e783ebdde9_MD5.jpg)

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8JD-hotkey%EF%BC%9F/9ae2f94432ec3e1b9257365eb6b30ce7_MD5.jpg)

采用protobuf序列化后性能进一步得到提升。在秒级36万以上时，能稳定在CPU 60%，压测持续时长超过5小时，未见任何异常。

30万时，压测时长超过数日，未见任何异常。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8JD-hotkey%EF%BC%9F/0dcd6fe409e6693425acd8d16fd1500f_MD5.jpg)

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8JD-hotkey%EF%BC%9F/060fcab7b485365a9498a0a388884b32_MD5.jpg)

## 五、优缺点

### 优点

**1\. 轻量，不绑 Redis** 不修改 Redis 源码，不依赖 Redis 客户端，跟 Redis 没有任何关系。它就是一个独立的探测集群 + 一个 jar 包。

**2\. 探测与缓存解耦** 框架只告诉你“热不热”，不替你管 value。业务方自己决定是本地缓存、限流还是熔断。灵活性极高。

**3\. 集群一致性** 热 key 推送到该应用部署的 **所有** 服务器 JVM 内存中。不会出现 A 机器认为热、B 机器认为不热的情况。

**4\. 毫秒级响应** 默认 500ms 上报一次，热 key 从产生到推送到所有 Client，延迟在毫秒级。秒杀场景也扛得住。

**5\. 成本极低** 1 台 Worker 撑 1000 台业务服务器。相比扩容 Redis 集群，成本几乎可以忽略。

**6\. 京东大促验证** 历经 2020 年 618、双 11 考验，每天探测数十亿 key，捕获大量爬虫和刷子用户。

### 缺点

**1\. 需要额外部署 Etcd 和 Worker** 不是“引入一个 jar 就完事”的方案。你需要部署 Etcd 集群（用于规则和地址同步）、Worker 集群（用于计算）、Dashboard（用于配置规则）。运维成本比“纯本地缓存”高。

**2\. 需要业务代码侵入** 你必须在查缓存的地方显式调用 `isHotKey` 。不是零代码接入。

**3\. 框架本身不存 value** `smartSet` 之后，value 存在本地 Caffeine 里。如果本地缓存被淘汰，还得回 Redis 查。框架不保证“热 key 的 value 永远在本地”。

**4\. 规则需要调优** “2 秒 20 次算热”还是“1 秒 100 次算热”，需要根据业务场景配置。配得太敏感，非热 key 被误判，浪费内存；配得太迟钝，热 key 已经打穿 Redis 了才反应过来。

## 六、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **秒杀/大促商品详情** | ✅✅✅ 强烈推荐 | 突发流量打同一个 key，本地缓存直接扛住 |
| **爬虫/刷子用户识别** | ✅✅✅ 强烈推荐 | `isHotKey`  判断用户 ID 是否高频访问，直接限流 |
| **热接口熔断** | ✅✅✅ 强烈推荐 | 突发海量请求同一个接口，推送后做本地熔断 |
| **Redis 热 key 本地缓存** | ✅✅✅ 强烈推荐 | 最经典的用法，减轻 Redis 读压力 |
| **黑名单用户本地缓存** | ✅✅ 推荐 | 高频访问的黑名单用户推送到本地，快速拦截 |
| **小流量内部系统** | ❌ 不推荐 | 部署 Etcd + Worker 的运维成本不值得 |
| **没有突发流量的业务** | ⚠️ 需评估 | 热 key 问题不突出，收益有限 |

## 七、写在最后

回到最初的问题： **为什么越来越多人用 JD-hotkey？**

**因为它把“热 key 探测”这件事，从“事后看监控”变成了“事前推到内存”。**

热 key 的核心矛盾不是“缓存不缓存”，是“ **你不知道谁会在下一秒变热** ”。

JD-hotkey 用轻量的 Worker 集群做分布式计数，在毫秒级判定热 key，然后直接推送到所有应用服务器的 JVM 里。业务代码只需要问一句 `isHotKey` ，剩下的框架全包了。

你需要部署 Etcd 和 Worker，需要在代码里加一行判断，需要根据业务调规则阈值。

但对于 **秒杀、大促、爬虫识别** 这些热 key 问题突出的场景来说，它用极低的成本，换来了 Redis 层一半以上的压力释放。

参考资源：

- **Gitee 仓库** ： [https://gitee.com/jd-platform-opensource/hotkey](https://gitee.com/jd-platform-opensource/hotkey)
- **京东云开发者社区实战文章** ： [https://developer.jdcloud.com/article/2854](https://developer.jdcloud.com/article/2854)
- **热 key 探测设计与实践** ： [https://developer.aliyun.com/article/1655928](https://developer.aliyun.com/article/1655928)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)