---
title: "拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？"
source: "https://mp.weixin.qq.com/s/tQ-8H-UgmziuqAlblgsY8w"
---
Java学习者社区 *2026年8月28日 15:33*

将 Java学习者社区设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/441a0f0d82ff306f1213fd87f15a437e_MD5.webp)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **技术选型意识** ：面试官想看的其实是你有没有想清楚——什么场景该用 ES，什么场景 MySQL 就绰绰有余。盲目上 ES 也是要扣分的。
2. **原理理解深度** ：倒排索引 vs B+Tree 索引，这是这道题的灵魂。能讲清楚这两个数据结构的差异，才算真正理解“为什么快”。
3. **架构实践经验** ：实际项目里 MySQL 和 ES 怎么分工、数据怎么同步，这是区分“背过八股”和“真用过”的分水岭。

## 核心答案

先说结论： **MySQL 是“存”的专家，ES 是“搜”的专家** 。两者不是谁取代谁，更像一对搭档，各管一滩。

为什么要用 ES？因为传统关系数据库在“搜”这件事上有硬伤：

| 痛点场景 | MySQL 的表现 | ES 的表现 |
| --- | --- | --- |
| 模糊搜索 `LIKE '%手机%'` | 前置 `%` 导致索引失效，全表扫描 | 倒排索引直接命中，毫秒级返回 |
| 全文检索 + 分词 | 不支持分词，只能整串匹配 | 内置分词器，搜“手机”能命中“智能手机” |
| 多条件组合查询 | 多字段 `LIKE` + `OR` ，性能崩塌 | 结构化 + 全文混合查询，统一 DSL |
| 相关度排序 | 只能按字段排序，没有“相关度”概念 | BM25 算法打分（ES 5.0 起默认，取代 TF-IDF），最相关的排最前 |
| 聚合统计分析（类似 GROUP BY） | 数据量大时分组聚合很慢 | 列式存储 + 预聚合，亿级数据秒出 |

说白了： **数据量上了千万、搜索条件一复杂，MySQL 就开始喘，ES 就是为这种场景准备的** 。

![ES 和 MySQL 区别](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/7ec1a5378c393fcf45e82c4bdf169beb_MD5.jpg)

ES 和 MySQL 区别

## 深度解析

### 一、MySQL 的 B+Tree，为什么“搜不动”

MySQL（InnoDB 引擎）的索引底层是 B+Tree。它本质上是把索引列的值排好序，查询时从根节点往下走，时间复杂度稳定在 O(log n)，等值查询和范围查询都非常快。

但它的前提是： **能走上索引** 。来看这个 SQL：

```
-- 想搜标题里带"手机"的商品
SELECT * FROM product WHERE title LIKE'%手机%';
```

`%` 放在前面，意味着开头可以是任意字符，B+Tree 的有序性完全用不上，优化器只能放弃索引，走全表扫描，一行一行扫过去，挨个做字符串匹配。

这里补个容易被追问的细节：如果查询的列刚好都在某个二级索引里（覆盖索引），MySQL 有时会选择全扫描那棵更小的二级索引树，而不去扫聚簇索引，代价小一些。但本质上还是“整棵树挨个摸一遍”，数据量一大照样慢，没有质的区别。

100 万数据可能还能忍，1000 万、上亿呢？用户在搜索框敲下回车，等来的是超时。

```
-- 这种能走索引，因为前缀固定
SELECT * FROM product WHERE title LIKE'手机%';
```

但真实业务里，用户搜的词在标题的哪个位置都有可能，后置匹配根本不解决问题。

![MySQL LIKE 索引失效](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/2121040b459f7c5e5b3fa1bb6cebeda9_MD5.jpg)

MySQL LIKE 索引失效

### 二、ES 的倒排索引，为什么“搜得快”

ES 底层是 Apache Lucene，核心数据结构是 **倒排索引（Inverted Index）** 。这个名字听着唬人，原理其实一句话就能讲明白。

先看什么是“正排”：MySQL 的思路是文档 → 找出里面的词。倒排反过来： **词 → 找出包含它的文档列表** 。

拿三个文档举例，分词后：

- 文档 1：“智能手机”
- 文档 2：“手机壳”
- 文档 3：“智能手表”

建立倒排索引：

![ES 倒排索引示例](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/7a0b02969e81879d2b6d90906aae1902_MD5.jpg)

ES 倒排索引示例

上图就是倒排索引的核心逻辑：

- **建索引阶段** ：ES 先对文本分词（比如 `ik_max_word` 中文分词器），把每个词条（Term）指向包含它的文档 ID 列表（这个列表叫 Postings List）
- **查询阶段** ：用户搜“手机”，分词后直接去词条字典（Term Dictionary）里查这个词，拿到文档列表，完事
- **关键差异** ：MySQL 是拿着关键词去扫全部文档，ES 是提前把“哪个词在哪些文档里”整理成了一张查找表，典型的 **空间换时间**

这就好比查字典：MySQL 的做法是从第一页翻到最后一页，每页都看看有没有这个词；ES 的做法是直接翻到目录页，这个词在第几页，一目了然。

补充一个细节：词条字典本身也是排好序的，Lucene 在它之上还用了 FST（Finite State Transducer）压缩存储，海量词条能常驻内存，查起来非常快。

![ES 倒排索引原理](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/991052c8cd3844b773aaea1d3886031e_MD5.jpg)

ES 倒排索引原理

### 三、概念对照：ES 和 MySQL 怎么对应

两者很多概念是相通的，面试时说清楚对应关系，能体现你是真用过：

| ElasticSearch | MySQL | 说明 |
| --- | --- | --- |
| Index（索引） | Table（表） | 注意！ES [7.x](http://7.x/) 之后才有这个对应关系 |
| Document（文档） | Row（行） | 一条数据就是一个 JSON 文档 |
| Field（字段） | Column（列） | 文档里的一个属性 |
| Mapping（映射） | Schema（表结构） | 定义字段类型 |
| DSL 查询语句 | SQL | ES 用 JSON 格式的 DSL |

这里有个版本演进的历史包袱：ES [6.x](http://6.x/) 及以前，还有个 `Type` 的概念对应 Table，那时 Index 对应 Database。6.0 开始一个索引只允许一个 Type，官方在 7.0 把 Type 的 API 废弃了，8.0 彻底移除。现在的对应关系就是上面表格这样。面试时能主动提这个版本差异，妥妥的加分项。

### 四、实时性差异：ES 是“近实时”

一个容易被追问的点：ES 的写入是 **近实时（NRT，Near Real-Time）** ，不是 MySQL 那种实时可见。

![ES 近实时写入流程](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/8fdd2b139fe3d7f5f8dc7cd2862fa906_MD5.jpg)

ES 近实时写入流程

ES 写入流程分三步：

- **第一步：写内存** 。数据先进入 `index buffer` （内存缓冲区），同时把操作记录追加到 `translog` （类似 MySQL 的 redo log，用来宕机恢复）。这时候数据是 **搜不到的** 。
- **第二步：refresh（默认 1 秒）** 。缓冲区里的数据被生成一个新的 segment（Lucene 的最小索引单元），数据变成可搜索状态。这就是“近实时”的由来：从写入到可搜索，默认有约 1 秒的延迟。
- **第三步：flush** 。segment 持久化到磁盘， `translog` 清空。

MySQL 则不同：事务一提交，数据立即可查。所以面试时别只说“ES 快”，要能说出 **ES 快在搜索、弱在实时性和事务** ，这才是完整的认知。

![ES refresh 机制](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/08e8781b44a37ab989b664c004999d5a_MD5.jpg)

ES refresh 机制

### 五、ES 不是银弹：这些场景别用它

面试官问“为什么用 ES”，其实也在等你说“什么时候不用”。只吹不贬，反而显得没实践过。

- **强事务场景别用** ：ES 没有真正的 ACID 事务，跨文档没法回滚。账户扣款、订单状态流转这类强一致业务，老老实实用 MySQL。
- **频繁更新的场景别用** ：ES 的底层 segment 是不可变的，更新实际上是“标记删除 + 新写入”，写放大严重。比如库存这种一秒改 N 次的字段，放 ES 里是灾难。
- **多表关联查询别用** ：ES 的 `join` 能力很弱（nested / parent-child 有各种性能坑），复杂 ER 关系还是关系数据库的强项。
- **内存成本** ：ES 是吃内存大户，JVM 堆 + 操作系统文件缓存都要预留足，小公司小数据量上 ES 纯属给自己找事。

### 六、生产架构：MySQL + ES 是黄金搭档

实际项目中，标准玩法是 **MySQL 做主存储，ES 做搜索引擎** ，各干各擅长的活：

![MySQL 同步 ES 架构](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/e8fc5b1d6fd73d48bb46761ec7bea444_MD5.jpg)

MySQL 同步 ES 架构

![MySQL ES 同步架构](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/ef1115b92b14ae339b2893adef597c0d_MD5.jpg)

MySQL ES 同步架构

这套架构的要点：

- **MySQL 是唯一数据源（Source of Truth）** ，所有写操作先进 MySQL，保证数据不丢、事务完整
- 通过 **Canal 监听 Binlog** （或者 Flink CDC），把数据变更投递到 MQ，再消费写入 ES，业务代码和同步逻辑解耦
- 搜索请求全部打到 ES，MySQL 只服务正常的业务读写
- 中间加 MQ 是为了削峰 + 失败重试，保证最终一致性

我之前做过一个电商项目，商品 5000 多万条，多条件筛选 + 关键词搜索，MySQL 上根本跑不动，上了这套架构后搜索响应稳定在百毫秒内。这套“双库”方案你面试时讲出来，基本就是标准答案。

## 面试高频追问

1. **ES 为什么是近实时而不是实时？**
	因为写入先进内存缓冲区，要等 refresh（默认 1 秒）生成 segment 后才可搜索。可配置 `refresh_interval` 调整，但调太小会让 segment 过多，反而拖垮性能。
2. **MySQL 和 ES 的数据一致性怎么保证？**
	主流方案就是 Binlog + Canal/Flink CDC + MQ 异步同步，保证最终一致性。同时要考虑消费失败重试、对账补偿任务兜底。双写方案（业务代码同时写 MySQL 和 ES）耦合高、没有事务保障，不推荐。
3. **ES 的写入流程了解吗？**
	写 buffer + translog → refresh 生成 segment（可搜索）→ flush 落盘清 translog。追问方向是 translog 的刷盘策略（ `              index.translog.durability            ` 参数）。
4. **ES 深分页问题怎么解决？**
	`from + size` 默认最多查 1 万条（ `max_result_window` 默认 10000），深分页要用 `search_after` 或 Scroll API。

## 常见面试变体

- 变体一：“ES 的倒排索引是怎么工作的？”
- 变体二：“ES 和 MySQL 的数据同步方案有哪些？各有什么优缺点？”
- 变体三：“什么情况下不应该使用 ES？”
- 变体四：“ES 的 refresh、flush、merge 分别是干什么的？”

## 记忆口诀

**MySQL 管存，ES 管搜** ：MySQL 负责“存得住、算得清”（事务、关联），ES 负责“找得快、排得准”（搜索、聚合）。

**正排知行，倒排知词** ：正排索引从文档找词（MySQL），倒排索引从词找文档（ES）。

## 总结

一句话：ES 用倒排索引换来了飞快的全文搜索，代价是放弃事务和实时性；MySQL 用 B+Tree 保证了稳定的增删改查和 ACID，代价是模糊搜索无能为力。生产环境两者不是二选一，而是 MySQL 主存储 + ES 搜索引擎的双库架构，数据通过 Binlog + Canal 异步同步。把“倒排 vs B+Tree”和“近实时机制”这两块讲透，这道题就稳了。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E6%8B%BC%E5%A4%9A%E5%A4%9A%E4%BA%8C%E9%9D%A2%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E4%BD%BF%E7%94%A8%20ElasticSearch%EF%BC%9F%E5%92%8C%E4%BC%A0%E7%BB%9F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93%20MySQL%20%E6%9C%89%E4%BB%80%E4%B9%88%E4%B8%8D%E5%90%8C%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 终于找到一个好用的 Nginx 日志分析工具了3. EasyExcel凉了？FastExcel又"改名"了？这次它进了Apache，再不会跑了！4. 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文