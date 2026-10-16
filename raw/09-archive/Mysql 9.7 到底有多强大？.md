---
title: "Mysql 9.7 到底有多强大？"
source: "https://mp.weixin.qq.com/s/V63BQapbLDwclShpHlXznA"
---
苏三 苏三说技术 *2026年10月16日 08:57*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

2026年4月21日，Oracle发布了MySQL 9.7.0 LTS。

如果你对MySQL的版本节奏不太熟悉，我简单说一下：MySQL [9.x走的是“创新版本”路线，每季度一个小版本，功能激进、迭代快。](http://9.xn--x,,-3o0af425v051cvjao1dizpwobj21d75be1or1e442av3bh8gha848uw3s7wmja511xh70czgm715f35cc2tqpa./)

而LTS版本大约每两年发布一次，主打稳定，提供5年Premier Support加3年Extended Support。

所以MySQL 9.7.0 LTS的发布，意味着 [9.x这条线从“尝鲜”进入了“敢上生产”的阶段。](http://9.xn--x-phnadb5561e0yavhjm64tm46azixuyfs1q1j7ajxebp6brl8djbax61wqc2a./)

但真正让我想写这篇文章的，是一个做DBA的朋友跟我吐槽的一句话：“ **用了十年MySQL，终于不用为了看复制延迟去买企业版授权了。** ”

这句话背后，是MySQL 9.7做的一件让社区等待了很久的事—— **把一批原本只有企业版才有的功能，正式开放给了社区版** 。

## 一、MySQL 9.7到底“给了”什么？

> 有些小伙伴可能会说：“MySQL版本更新跟我有什么关系？能跑就行。”

**关系很大。**

因为这次开放的功能，直接关系到你日常运维的三大痛点： **复制监控、复杂查询优化、数据安全** 。

我把这次社区版新开放的功能整理了一下：

| 功能 | 之前状态 | MySQL 9.7状态 |
| --- | --- | --- |
| **Replication Applier Metrics** | 仅企业版 | **社区版可用** |
| **Group Replication Flow Control Statistics** | 仅企业版 | **社区版可用** |
| **Group Replication Primary Election** | 仅企业版 | **社区版可用** |
| **Group Replication Resource Manager** | 仅企业版 | **社区版可用** |
| **OpenTelemetry/OTLP 遥测** | 仅企业版 | **社区版可用** |
| **Hypergraph Optimizer** | 仅企业版 | **社区版可用** |
| **JSON Duality Views DML** | 社区版只读 | **社区版可增删改** |
| **Profile-Guided Optimization (PGO)** | 仅企业版 | **社区版可用** |

数据来源：

**这个列表的意义在于** ：过去几年MySQL社区版和企业版的差距越拉越大，很多运维刚需功能被锁在企业版里。

9.7这一波开放，算是把差距往回拉了一大截。

## 二、几张图看懂MySQL 9.7的核心变化

![图片](assets/Mysql%209.7%20%E5%88%B0%E5%BA%95%E6%9C%89%E5%A4%9A%E5%BC%BA%E5%A4%A7%EF%BC%9F/af58aa9c88d858ff91c09a0af8b4dd96_MD5.jpg)

![图片](assets/Mysql%209.7%20%E5%88%B0%E5%BA%95%E6%9C%89%E5%A4%9A%E5%BC%BA%E5%A4%A7%EF%BC%9F/f68aadfc14ae5924eeb6f1bde532c360_MD5.jpg)

![图片](assets/Mysql%209.7%20%E5%88%B0%E5%BA%95%E6%9C%89%E5%A4%9A%E5%BC%BA%E5%A4%A7%EF%BC%9F/196fb9707e30d75e0bd87bf99a2584bb_MD5.jpg)

下面我挑几个对Java开发者影响最大的能力逐一拆解。

## 三、复制可观测性：终于不用自己猜了

> 有些小伙伴在工作中可能遇到过这样的场景：主从复制延迟突然飙高，但你不知道原因——是主库写入太猛？是从库SQL线程卡了？还是网络抖动？你只能靠猜。

**Replication Applier Metrics** 就是来解决这个问题的。

它提供了 **细粒度的复制延迟指标** 。

以前你只能看 `Seconds_Behind_Master` 这个粗糙的数字，现在你能看到复制应用器的 **线程级指标** ——每个worker线程在处理什么、卡在哪里、延迟多少。

**Group Replication Flow Control Statistics** 则针对组复制场景，暴露了流控的详细统计信息。

组复制里最头疼的问题之一就是“明明没多少流量，但流控一直触发”，有了这个指标，你就能定位到底是哪个节点拖慢了整个组。

这些指标现在可以直接和Prometheus对接，不需要为了监控再去买企业版授权。

## 四、Hypergraph Optimizer：复杂JOIN的救星

这是MySQL 9.7在查询优化上最大的变化。

**传统MySQL的优化器用的是“左深树”结构** 来生成执行计划。

简单查询没问题，但一旦涉及多表关联、嵌套子查询，它就容易选错执行计划——要么全表扫描，要么用了错误的索引。

**Hypergraph Optimizer把整个查询构建成一个超图** ，用动态规划的方式找出最优的执行计划。

```
-- 以前：多表JOIN可能选错执行计划
SELECT 
            o.id,
           
            u.name,
           
            p.title
          
FROM orders o
JOIN users u ON 
            o.user_id
           = 
            u.id
          
JOIN products p ON 
            o.product_id
           = 
            p.id
          
JOIN categories c ON 
            p.category_id
           = 
            c.id
          
WHERE 
            o.created_at
           > '2026-01-01'
  AND 
            c.name
           = 'electronics';

-- MySQL 9.7：开启超图优化器
SET optimizer_switch='hypergraph_optimizer=on';
```

**但有一个重要的提醒** ：Percona创始人Peter Zaitsev对超图优化器有一个很清醒的判断—— **新的优化器并不意味着你的workload一定更快，有时候可能相反** 。

所以 **不要全局无脑开启** 。

建议先在测试环境针对复杂JOIN场景做对比测试，确认有提升后再逐步铺开。

## 五、PGO：一个“免费的午餐”式性能提升

这是MySQL 9.7另一个值得关注的优化。

**Profile-Guided Optimization（PGO）** 是一种编译器优化技术。

它的做法是：先让程序跑一遍典型负载，收集执行 profile，然后用这些数据指导编译器重新编译代码，让热点路径的指令更紧凑、分支预测更准。

Percona做了一组非常严谨的PGO对比测试，结果如下：

| Buffer Pool | 平均提升 | 最佳场景 |
| --- | --- | --- |
| **2GB** | **3.0%** | 4线程时5.5% |
| **12GB** | **4.1%** | 4线程时8.6% |
| **32GB** | **12.2%** | 1线程时14.3% |

**关键发现** ：PGO的收益 **完全来自CPU层面的优化** ——更好的指令缓存利用率、更好的分支预测、更优的函数内联。

Buffer pool命中率、锁竞争、I/O指标在PGO和非PGO版本之间 **几乎完全一致** 。

这意味着： **你不需要改任何配置、不需要换硬件，升级到PGO构建的版本就能拿到性能提升** 。

对于buffer pool较大的服务器（32GB以上），这个提升尤其明显。

## 六、JSON Duality Views

JSON Duality Views是MySQL的一个特色功能——它让同一份数据 **既能以关系表的形式访问，也能以JSON文档的形式访问** 。

但之前社区版有个尴尬的限制： **只能查，不能写** 。

你只能用SELECT读JSON视图，但INSERT、UPDATE、DELETE都不支持。

MySQL 9.7把这个限制去掉了。

现在社区版可以对JSON Duality Views做完整的DML操作，包括使用自增列作为主键。

```
-- 社区版现在可以这样写了
INSERT INTO user_json_view (name, email, address)
VALUES ('张三', 'zhangsan@
            example.com'
          , '{"city": "北京"}');

UPDATE user_json_view
SET address = '{"city": "上海"}'
WHERE name = '张三';
```

对于需要同时支持关系查询和文档查询的场景，这个功能的实用价值提升了不少。

## 七、但有一件事，MySQL 9.7还是没做

> 有些小伙伴可能会问：“说了这么多，那AI相关的能力呢？”

**社区版依然没有。**

MySQL 9.7确实引入了 `VECTOR` 数据类型，可以存储向量，支持 `TO_VECTOR()` 和 `FROM_VECTOR()` 函数。

**但关键的相似度搜索函数—— `DISTANCE()` 和 `VECTOR_DISTANCE()` ——只在HeatWave MySQL（Oracle云上版本）中提供，社区版和企业版本地部署都不包含** 。

这意味着： **你可以在MySQL 9.7里存向量，但没法用SQL做向量相似度搜索。**

Percona Server for MySQL 9.7.2通过自己的实现补上了 `DISTANCE()` 函数，支持COSINE、EUCLIDEAN、MANHATTAN、DOT等度量方式。但这不是Oracle官方的方案。

**所以如果你在社区版上做RAG，目前的选择是** ：要么用Percona的版本，要么把向量数据同步到专门的向量数据库。

## 八、优缺点

### 优点

**1\. 社区版能力大幅增强** 复制可观测性、组复制流控、超图优化器、OpenTelemetry遥测——这些原本企业版专属的功能现在社区版都能用。

**2\. PGO带来实打实的性能提升** 无需改配置、无需换硬件，升级即受益。32GB buffer pool场景下平均提升12.2%。

**3\. Hypergraph Optimizer改善复杂JOIN** 多表关联、嵌套子查询场景下有机会获得更好的执行计划。

**4\. JSON Duality Views支持DML** 社区版终于可以对JSON视图做增删改，实用价值大幅提升。

**5\. 8年支持周期** 5年Premier Support加3年Extended Support，规划有保障。

### 缺点

**1\. 向量搜索能力缺失** `VECTOR` 类型有了，但相似度搜索函数只在HeatWave里。社区版做RAG仍然需要外部方案。

**2\. Hypergraph Optimizer需要谨慎测试** 新优化器不保证所有workload都更快，有社区基准显示写密集场景可能退化。

**3\. 移除和废弃了一批旧功能** `innodb_log_file_size` 、 `innodb_undo_tablespaces` 等旧变量被移除，升级需要调整配置。

**4\. 社区Commit数量下降** 有分析指出MySQL公开仓库的年度commit数量明显下降。

## 九、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **需要复制可观测性的OLTP系统** | ✅✅✅ 强烈推荐 | 社区版终于能用细粒度复制指标 |
| **复杂JOIN查询较多的报表系统** | ✅✅✅ 强烈推荐 | Hypergraph Optimizer有机会大幅改善 |
| **32GB+ Buffer Pool的大内存服务器** | ✅✅✅ 强烈推荐 | PGO在这个场景收益最大 |
| **需要JSON+关系混合访问的应用** | ✅✅✅ 强烈推荐 | JSON Duality Views现在可写 |
| **从8.4升级的长期项目** | ✅✅ 推荐 | 8年支持周期，但需要测试兼容性 |
| **社区版做RAG/向量搜索** | ⚠️ 需评估 | 相似度函数缺失，需要Percona或外部方案 |
| **写密集型的超高频OLTP** | ⚠️ 需评估 | 社区基准显示部分场景可能退化 |

## 十、写在最后

回到最初的问题： **MySQL 9.7到底有多强大？**

复制可观测性、超图优化器、PGO、JSON Duality Views DML——这些功能每一个都切中了社区用户的真实痛点。

过去几年MySQL社区版被诟病“企业版吃肉，社区版喝汤”，9.7把差距往回拉了一大截。

**但无论怎么说，MySQL 9.7是一个“值得升级”的版本。**

尤其如果你正在被复制延迟问题困扰、或者正在跑复杂的JOIN查询、或者你的服务器buffer pool在32GB以上——升级带来的收益是实打实的。

**升级前记得做三件事** ：备份数据、在测试环境跑一遍兼容性测试、针对复杂JOIN场景对比一下Hypergraph Optimizer开启前后的执行计划。

**数据库的升级从来不是“越新越好”，而是“在你确认它解决你的问题之后，越早越好”。**

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)