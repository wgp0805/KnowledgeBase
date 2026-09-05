---
title: "ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？"
source: "https://mp.weixin.qq.com/s/F9n7YPzYsXiiR6PTwOnj0Q"
---
犬小哈 小哈学Java *2026年9月2日 09:00*

![图片](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/16fa2c24623c02bb35afcd3ba8598a5e_MD5.webp)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **基础掌握度** ：数据类型是 Mapping 的地基。面试官想知道你是真的建过索引、写过 DSL，还是只在项目里 “摸过” ES。
2. **选型能力** ： `text` 和 `keyword` 选错、金额用了 `double` ，这些在线上都是实打实的事故。类型选型直接暴露你的实践深度。
3. **知识迁移能力** ：业务里最常见的场景就是 “MySQL 的数据同步到 ES 做搜索”。能不能把 MySQL 的概念、字段类型准确翻译成 ES 的，考察的是你对两套存储体系的理解，死记硬背应付不了追问。

## 核心答案

ES 的数据类型可以分成五大类：

| 分类 | 常用类型 | 一句话说明 |
| --- | --- | --- |
| 核心类型 | `text`  、 `keyword` | 字符串二兄弟，一个分词一个不分 |
| 数字类型 | `long`  、 `integer` 、 `short` 、 `byte` 、 `double` 、 `float` 、 `half_float` 、 `scaled_float` | 整数 4 档，浮点 5 档 |
| 时间类型 | `date` | 既能存时间戳也能存格式化字符串 |
| 布尔类型 | `boolean` | 就是 true / false |
| 复杂类型 | `object`  、 `nested` 、 `join` 、 `geo_point` 、 `ip` 、 `dense_vector` 等 | 对象、嵌套、父子、地理、向量 |

和 MySQL 的概念映射一张表说清楚：

| MySQL | ES | 备注 |
| --- | --- | --- |
| Database | Index | ES 7.0 之后没有 Type 的概念了 |
| Table | Type（已废弃）→ 现在直接对应 Index | 老面试题里的 “Type” 是历史产物 |
| Row | Document | 一行数据就是一个 JSON 文档 |
| Column | Field | 文档里的一个字段 |
| Schema | Mapping | 定义字段名和类型 |
| SQL | Query DSL | 查询语言 |

![ES 数据类型总览](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/4241f2bef68b812b2108167db06ee9a8_MD5.jpg)

ES 数据类型总览

## 深度解析

### 一、先搞懂 ES 独有的 text 和 keyword

这是和 MySQL 差异最大的地方，也是面试的重头戏。

MySQL 的 `VARCHAR` 一个字段既 `WHERE name = '手机'` 精确匹配，又 `LIKE '%手机%'` 模糊查询，一个字段两副面孔。到了 ES 这里，拆成了两个类型：

```
PUT /product
{
  "mappings": {
    "properties": {
      "productName": {
        "type": "text",
        "analyzer": "ik_max_word",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  }
}
```

上面这段是生产环境最经典的写法，拆开看：

- \*\* `text` \*\*：会分词。写入 “小米折叠屏手机” 会被拆成 “小米”、“折叠屏”、“手机” 这些词条（term），建立倒排索引。适合全文检索，也就是 `match` 查询
- \*\* `keyword` \*\*：不分词，整条字符串原样进索引。适合精确匹配（ `term` 查询）、排序、聚合。注意默认 `ignore_above` 是 256，超过 256 个字符的内容不会被索引，这是个经典坑
- **`fields` 子字段** ：主字段用 `text` 做搜索，子字段用 `keyword` 做排序聚合。查询时用 `              productName.keyword            ` 就能走精确匹配。一次定义，两种玩法

一句话记住：\*\*要搜用 `text` ，要查（精确匹配）、要排序、要聚合用 `keyword` \*\*。生产上绝大多数字符串字段都是这个组合拳。

![ES text 和 keyword 区别](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/d0938749023a25b1bab4c5e1702c996c_MD5.jpg)

ES text 和 keyword 区别

### 二、概念映射：从 MySQL 平移到 ES

![图片](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/6169a4559bb1f6dbacee657e3336c828_MD5.jpg)

对照着看就很清晰了：

- **Database → Index** ：一个库对一个索引，隔离逻辑相同。但注意 ES 7.0 移除了 Type（就是老教程里 “Table 对应 Type” 的那个 Type），原因是 ES 的 Type 共用同一份 Lucene 索引，不同 Type 的字段会互相干扰，属于历史设计缺陷， [8.x](http://8.x/) 彻底删干净了
- **Row → Document** ：MySQL 一行是一条记录，ES 一条是一个 JSON 文档，字段结构可以不一样（Schema Free）
- **Column → Field** ：字段的概念一致，但 ES 的字段类型在索引创建后不能改（底层是 Lucene 段的不可变结构），要改只能重建索引（reindex），这和 MySQL `ALTER TABLE` 的成本完全不是一个量级
![MySQL 和 ES 概念映射](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/5d4a7d7c6064b9e7f27f640e11ef00b8_MD5.jpg)

MySQL 和 ES 概念映射

### 三、字段类型映射表（重点背这个）

| MySQL 类型 | ES 类型 | 注意事项 |
| --- | --- | --- |
| `BIGINT` | `long` | Java 的 `Long` 直接对应 |
| `INT` | `integer` | 32 位，Java 的 `Integer` |
| `SMALLINT`  / `TINYINT` | `short`  / `byte` | 用得少，知道就行 |
| `DOUBLE` | `double` | 64 位双精度 |
| `FLOAT` | `float` | 32 位单精度 |
| `DECIMAL` | `scaled_float` | ⚠️ 重点，下面细说 |
| `VARCHAR`  / `TEXT` | `text`  \+ `keyword` 子字段 | 搜索和精确匹配全都要 |
| 枚举、状态字段 | `keyword` | 不需要分词的直接上 keyword |
| `DATETIME`  / `TIMESTAMP` | `date` | 支持多种 format |
| `TINYINT(1)`  / `BOOLEAN` | `boolean` | — |
| `BLOB` | `binary` | Base64 编码存储，不能搜索 |
| `JSON`  （5.7+） | `object`  / `nested` | 一对多必须用 `nested` ，object 会 “拍平” 数据导致查询错乱 |
| `POINT`  （空间类型） | `geo_point` | ES 的地理检索比 MySQL 空间索引强太多 |
| — | `ip`  、 `dense_vector` | ES 特色，MySQL 没有直接对应 |

重点说说 `DECIMAL → scaled_float` 这个坑。ES 没有真正的十进制精确类型， `double` 存金额会有精度问题（0.1 + 0.2 ≠ 0.3 这个经典问题）。 `scaled_float` 的原理是指定一个 `scaling_factor` （比如 100），底层实际存的是 `long` （价格 19.99 存成 1999），展示时再除回去，既省空间又精确。所以订单金额这种字段，要么 `scaled_float` ，要么直接 `long` 存 “分”，别裸用 `double` 。

![MySQL 字段映射 ES 类型](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/497b956fa71cdba5d9f3dda5efcb1796_MD5.jpg)

MySQL 字段映射 ES 类型

### 四、动态映射的坑

如果你建索引时没写 Mapping，ES 会自动推断类型，这就是动态映射（Dynamic Mapping）。推断规则大致是：

- JSON 整数 → `long` （不是 `integer` ）
- JSON 浮点数 → `float` （不是 `double` ）
- `true` / `false` → `boolean`
- 字符串 → `text` + `keyword` 子字段
- 符合日期格式的字符串 → `date` （默认开启日期检测，date\_detection）

坑就在最后一条：假设有个字段存商品编号，前几条数据恰好长得很像日期（比如 “2024-01-15”），ES 会把它推断成 `date` ，后面再来一条普通编号 “SP001”，直接写入失败。所以生产环境一律建议 **显式定义 Mapping，关掉不该开的自动检测** ，别把类型推断交给运气。

![ES 动态映射误判](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/f1a9892bb40e80d3a6004207f62ba455_MD5.jpg)

ES 动态映射误判

## 面试高频追问

1. **text 和 keyword 的区别？** 必问。分词 vs 不分词、 `match` vs `term` 、倒排索引怎么建，三板斧答下来就稳了。
2. **为什么 ES 7.0 要移除 Type？** 不同 Type 共用同一份底层 Lucene 索引，字段会互相干扰（A Type 里字段是 date，B Type 里同名字段就得是 date），设计上就不合理，官方干脆砍了。
3. **nested 和 object 的区别？** `object` 会把嵌套数组 “拍平”，丢失对象之间的边界，查 “颜色=红 且 尺寸=XL” 会误命中 “红L + 蓝XL”； `nested` 给每个嵌套对象单独建索引文档，保住边界，代价是查询稍慢、更新麻烦。
4. **MySQL 的数据怎么同步到 ES？** 双写、Canal 监听 binlog、Flink CDC、Logstash 定时拉取，各有优劣，能对比着说就是加分项。
5. **为什么 ES 的字段类型定义后不能改？** 底层 Lucene 段不可变，倒排索引结构建好就固定了。要改类型只能建新索引 + `_reindex` 迁移。

## 常见面试变体

- 变体一：“ `text` 和 `keyword` 有什么区别，分别什么场景用？”
- 变体二：“MySQL 的 `LIKE '%xx%'` 和 ES 的全文检索有什么区别？”（考点：B+ 树无法利用前置 %，全表扫描 vs 倒排索引）
- 变体三：“为什么有了 MySQL 还要 ES？两者怎么选型？”

## 记忆口诀

**类型选择** ：搜用 text，查排聚合 keyword；整数 long，小数 scaled；日期 date，一对多 nested。

**概念映射** ：库索引、行文档、列字段、表映射——Table 没了，Mapping 顶上。

## 总结

ES 数据类型按 “核心、数字、时间、布尔、复杂” 五大类记，重点是 `text` / `keyword` 的组合拳和 `scaled_float` 存金额。和 MySQL 的映射按 “Database→Index、Row→Document、Column→Field、Schema→Mapping” 对照理解，再记住 Type 已死这条版本演进线。能顺嘴说出两三个生产坑（keyword 256 上限、动态映射误判 date、object 拍平），面试官对你的评价会直接上一个档次。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/ES%20%E6%94%AF%E6%8C%81%E5%93%AA%E4%BA%9B%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%EF%BC%8C%E5%92%8C%20MySQL%20%E4%B9%8B%E9%97%B4%E7%9A%84%E6%98%A0%E5%B0%84%E5%85%B3%E7%B3%BB%E6%98%AF%E6%80%8E%E4%B9%88%E6%A0%B7%E7%9A%84%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. Spring-Smart-DI 动态切换实现类，很不错！4. 每天骑的共享单车是什么通信原理，有人了解过吗？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

Java 面试题 | 八股文汇总 · 目录

阅读原文