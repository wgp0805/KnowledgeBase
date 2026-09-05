---
source_url: "https://mp.weixin.qq.com/s/Dfv8NzSkBVVfqn6kOOmjZg"
title: "面试官：ElasticSearch 为什么快？"
account: "小哈学Java"
published_at: "2026-08-31 09:14:11"
saved_at: "2026-08-31 12:31:34"
sync_id: "art_f30320ea8536459494744b84acd3c952"
parse_status: "ok"
---

# 面试官：ElasticSearch 为什么快？

![](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/f4fc870c1c5e65b272707a78121464cc_MD5.jpg)

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

## 面试考察点

- 原理深度 ：光答 “倒排索引” 这四个字不够，面试官要听的是你能不能讲清它内部的查询结构（Term Index、Term Dictionary、Posting List），这一条直接区分 “背答案的” 和 “真懂的”。
- 对比思维 ：考察你能不能把 ES 和 MySQL 的  `B+`  树做对比，说清楚各自擅长什么场景。能做对比的人，通常真用过这两个东西。
- 架构视野 ：除了单机数据结构，面试官还想看你能否从分布式（分片并行）、近实时（NRT）、缓存这些架构层面来分析性能。答到这层，冲高级岗就有底气了。

## 核心答案

先给结论：ES 快是**一堆优化叠出来**的，没有单点魔法，核心可以拆成三层看：

| 层面 | 关键设计 | 一句话解释 |
| --- | --- | --- |
| 数据结构层 | 倒排索引 | 从 “关键词” 直接定位 “文档”，跳过全表扫描 |
| 数据结构层 |  `FST`  + Term Index | 词典的 “目录页” 常驻内存，磁盘最少寻址一次 |
| 数据结构层 | FOR 压缩 + 跳表 + Roaring 位图 | Posting List 压缩存储，多条件求交集飞快 |
| 存储层 | Segment 不可变 | 无锁读取、友好压缩、吃满 Page Cache |
| 存储层 | Doc Values 列式存储 | 排序聚合不用回源解析原文 |
| 架构层 | 分片并行查询 | 一份查询拆到 N 个节点同时算 |
| 架构层 | NRT 近实时写入 | 1 秒可见性，换来写入高吞吐 |

面试时建议按 “数据结构 → 存储 → 架构” 这个顺序答，层次感一下就出来了。

![ES 为什么快](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/ff1b876f8c7208229a3b832ab945f17d_MD5.jpg)

ES 为什么快

## 深度解析

### 一、倒排索引：一切的起点

先搞清楚正排和倒排的区别。MySQL 里存的是 “文档 → 内容”，这就是正排。你想搜包含 “关注” 两个字的文章，数据库只能一条条翻， `like '%关注%'`  直接全表扫描，数据量一大就是灾难。

倒排索引反过来，存的是 “关键词 → 文档列表”：

![ES 倒排索引示例](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/b5d1fd4cead09bb3f7ad85d25d16a3b2_MD5.jpg)

ES 倒排索引示例上图的对比就是本质区别：

- 正排索引 ：从文档找内容容易，但从内容找文档，只能逐条匹配
- 倒排索引 ：写入时先分词（“关注犬小哈” 会拆成 “关注”、“犬小哈” 两个 Term），然后建立 “Term → 文档 ID 列表” 的映射
- 查询时 ：搜 “犬小哈” 直接拿到 Posting List  `[1, 2]`  ，O(1) 级别定位，根本不用扫描原文

一句话：**写入时多干活（分词、建索引），查询时少干活**。搜索引擎 20 年前的核心思想，到现在依然能打。

![ES 倒排索引查询](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/f5ecc6028ffbd30b5e9c22738388b60b_MD5.jpg)

ES 倒排索引查询但光有倒排索引还不够。假设 Term 有上亿个（英文单词、中文词、各种数字组合），怎么快速找到目标 Term 本身就是个问题。总不能每个查询都在磁盘上二分查找几万次吧？

### 二、Term Index + Term Dictionary：字典的 “目录页”

Lucene 把词典查询拆成了三层结构，这是我认为整道题最出彩的部分：

![ES 词典查询结构](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/272145a0c71eca3d0271c019aa830769_MD5.jpg)

ES 词典查询结构这三层的文字讲解：

- 第一层 Term Index ：可以理解成字典的 “目录页”，只存 Term 的前缀，不存完整内容，所以体积极小，可以整个放进内存。它用的是  `FST`  （Finite State Transducer，有限状态转换器）结构
- 第二层 Term Dictionary ：真正有序的词典，存在磁盘上。通过内存里的 Term Index，直接定位到目标 Term 所在的磁盘块， 最少只需要一次磁盘寻址
- 第三层 Posting List ：拿到了 Term，也就拿到了对应的文档 ID 列表，后面就是算交集、取原文

 `FST`  这玩意值得单独说两句。它有三个漂亮的特点：

- 前缀共享 ：  `cat`  、  `catalog`  、  `catalogue`  共用  `cat`  前缀，重复部分只存一份，压缩率极高
- **查询 O(len)**：时间复杂度只跟查询词长度有关，跟词典总量无关
- 内存占用小 ：正是够小，Term Index 才能常驻堆内存

这三层结构像不像你查字典的过程？先翻目录（内存里的 FST）找到页码，再翻到那一页（磁盘上的 Term Dictionary），最后看到词条解释（Posting List）。

![ES FST 词典](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/99122adba19f5f5b61eda4cdf88f937c_MD5.jpg)

ES FST 词典

### 三、存储层的暗器：Segment 不可变 + Doc Values

**Segment 不可变设计**。Lucene 底层由一个个 Segment 组成，每个 Segment 生成后就不再修改（删除只是打个标记）。这个设计带来三个性能红利：

- 读取无锁 ：不可变数据天生线程安全，并发查询不需要任何锁竞争
- 压缩率高 ：内容不变就能放心用激进的压缩算法，省下来的空间全是 IO
- 吃满 Page Cache ：不可变文件可以被操作系统放心缓存，热数据几乎全部驻留内存，查询基本不打磁盘

**Doc Values 列式存储**。倒排索引擅长 “找到文档”，但排序和聚合需要 “按字段值” 来算，用倒排就得把所有文档原文拉出来解析一遍，太浪费了。所以 ES 写入时会额外存一份列式存储的 Doc Values，排序聚合直接读它，快得多。

另外提一句，数值类型和地理位置用的是  `BKD-Tree` （空间多维索引），范围查询效率高，跟倒排索引各管一摊。

顺带补充一个容易忽视的点：Posting List 在磁盘上也不是裸存的，文档 ID 会先做 delta 编码，再用 Frame of Reference 压缩成块，配上跳表（Skip List）支持快速跳块。多个条件 AND 求交集时不用一个个遍历。而 Roaring Bitmap 主要用在 filter 缓存上，缓存下来的 DocIdSet 求交并集飞快。

![ES Doc Values](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/5278cfb6fb77f62ada72917a479515b9_MD5.jpg)

ES Doc Values

### 四、写入侧：为什么说是 “近实时”？

ES 写入不是立刻落盘可查的，中间走了一套流水线：

![](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/549ed3823ae90eb8675685867a3507e8_MD5.jpg)

这张图的文字讲解：

- 第一步 ：数据先进内存 Buffer，同时写 Translog（事务日志，防止宕机丢数据）
- 第二步 refresh ：默认每 1 秒（  `index.refresh_interval`  可调），Buffer 里的数据生成一个新 Segment，直接放进 文件系统缓存 ，这时数据就能被搜到了。注意，这一步 没有落盘 ，这就是 “近实时（NRT）” 的由来：放弃强实时的落盘，换来 1 秒可见性 + 高吞吐写入
- 第三步 flush ：Segment 真正 fsync 到磁盘，清空 Translog，默认 30 分钟或 Translog 太大（默认 512MB）时触发

所以严格来说，ES 不是实时搜索引擎，是**近实时**（Near Real-Time）。这个追问频率极高，答不上来会很减分。

![ES 近实时 refresh](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/848c439086d26e23f691055d1c698452_MD5.jpg)

ES 近实时 refresh

### 五、架构层：分片并行 + 缓存体系

单机再快也有天花板，ES 是天生的分布式架构：

- 分片并行 ：一个索引拆成 N 个分片，散落在不同节点。查询时协调节点把请求广播到所有分片 并行执行 ，各自算完再汇总（scatter-gather 模式）。数据量翻倍，加机器就是了，查询延迟基本不涨
- 缓存体系 ：文件系统缓存（Page Cache）扛大头，加上 ES 自己的 Shard Request Cache（缓存分片级聚合结果）、Query Cache（缓存过滤查询的位图），热点数据的查询几乎就是纯内存操作

![ES 分片并行和缓存](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/756309188c3105006e6f0b16ded4d5fa_MD5.jpg)

ES 分片并行和缓存

## 面试高频追问

- ES 是实时的吗？ 不是，是近实时。写入到可搜索之间默认有 1 秒的 refresh 间隔。要强一致场景（比如秒杀扣库存）别用 ES，那是 MySQL 的事。
- ES 为什么深分页慢？  `from + size`  查询，每个分片都要取  `from + size`  条数据到协调节点排序。翻到第 1000 页时，每个分片都扛不住了。生产环境用  `search_after`  ，导出场景用 Scroll。
- refresh、flush、force merge 分别干什么？ refresh 是 Buffer 生成 Segment 进缓存（可搜索），flush 是 Segment 落盘并清 Translog，force merge 是把多个小 Segment 合并成大的（查询提速，但很吃资源，建议低峰期做）。
- 既然 Segment 不可变，那更新和删除怎么办？ 打标记（.del 文件记录删除的文档号），查询时过滤掉，真正的物理删除要等 Segment 合并时才发生。

## 常见面试变体

- “ES 的写入流程说一下？”（本文第四节展开答）
- “倒排索引是什么？画一下结构”
- “MySQL 的  `B+`  树和 ES 的倒排索引有什么区别？各自适合什么场景？”
- “为什么用 ES 不直接用 MySQL 的  `like`  ？”

## 记忆口诀

**结构看三层：目录（Term Index/FST）→ 词典（Term Dictionary）→ 倒排列表（Posting List）；存储两板斧：不可变 Segment + 列式 Doc Values；架构一手牌：分片并行加缓存；写入近实时：1 秒 refresh 见。**

## 总结

一句话：ES 快 = 倒排索引让查询避开全表扫描 + FST 目录常驻内存让定位最少一次磁盘寻址 + 不可变 Segment 与列式存储吃满缓存 + 分片并行把压力摊到多台机器。面试时把这四层讲清楚，从数据结构聊到架构，这道题就是你的送分题。

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI + Spring Boot 3.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-08-31%20-%20%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AElasticSearch%20%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BF%AB%EF%BC%9F/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 每天骑的共享单车是什么通信原理，有人了解过吗？
3. 技术总监：公司不在乎你干了多少活！
4. 告别if-else噩梦：流程编排技术真的太香了！
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢
```

---
原文链接：https://mp.weixin.qq.com/s/Dfv8NzSkBVVfqn6kOOmjZg
