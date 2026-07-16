---
title: "用雪花 id 和 uuid 做 MySQL 主键，被领导怼了"
source: "https://mp.weixin.qq.com/s/lF6_pTeT3ybiGs36HzhLRQ"
---
小哈学Java *2026年7月15日 16:41*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smrNo8xcgLRXErt9L3vHiaPxdEJ1CFZN5hnEgqqJ3P1lY1ZO3eUHxSSgzsVVpvW9SFkDNSWeojQLibRLL9KoNreKVia3XsVyCv0VAM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

来源： [https://www.cnblogs.com/wyq178/p/12548864.html](https://www.cnblogs.com/wyq178/p/12548864.html)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 前言
- 一、mysql 和程序实例
- 1.1.要说明这个问题,我们首先来建立三张表
	- 1.2.光有理论不行,直接上程序,使用 spring 的 jdbcTemplate 来实现增查测试
	- 1.3.程序写入结果
	- 1.4.效率测试结果
- 二、使用 uuid 和自增 id 的索引结构对比
- 2.1.使用自增 id 的内部结构
	- 2.2.使用 uuid 的索引内部结构
	- 2.3.使用自增 id 的缺点
- 三、总结

---

## 前言

在 mysql 中设计表的时候,mysql 官方推荐不要使用 uuid 或者不连续不重复的雪花 id(long 形且唯一，单机递增),而是推荐连续自增的主键 id,官方的推荐是 auto\_increment,那么为什么不建议采用 uuid,使用 uuid 究竟有什么坏处？

本篇博客我们就来分析这个问题,探讨一下内部的原因。

## 一、mysql 和程序实例

### 1.1.要说明这个问题,我们首先来建立三张表

分别是 user\_auto\_key,user\_uuid,user\_random\_key,分别表示自动增长的主键,uuid 作为主键,随机 key 作为主键,其它我们完全保持不变.

根据控制变量法,我们只把每个表的主键使用不同的策略生成,而其他的字段完全一样，然后测试一下表的插入速度和查询速度：

##### 注：这里的随机 key 其实是指用雪花算法算出来的前后不连续不重复无规律的 id:一串 18 位长度的 long 值

id 自动生成表：

![图片](https://mmbiz.qpic.cn/mmbiz_png/pUq1tpL9smotEj6GPibkPEgSZyLFibVe6P63RuDVw6QkjFBTDII8RbSibxEYuDK4fre2ygZZ5l8uia3RbXaoAzkKYddpBkFPticS6rhFNNSDWVWg/640?wx_fmt=png&from=appmsg#imgIndex=1)

id 自动生成表

用户 uuid 表：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smrCg1TMV0icic0t9WFhIibl2pIV7j7sXOhCSzgh0JuvaEf9vqIyCFkH09c38ZPzkJfFekicPbxtHzWJjbqtKYNd13TicMWYSkCIho9c/640?wx_fmt=png&from=appmsg#imgIndex=2)

用户 uuid 表

随机主键表：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smos9Z0FK2o3RzGrE5d9AZJGzlkDEtU97HzvGsfKAqfvxsVgo2QTLK2ibxdPrjT4kibiaibu6heRVlVQFsTiaUfcWnqDhvwFzqzGqnSU/640?wx_fmt=png&from=appmsg#imgIndex=3)

随机主键表

### 1.2.光有理论不行,直接上程序,使用 spring 的 jdbcTemplate 来实现增查测试

技术框架：springboot+jdbcTemplate+junit+hutool,程序的原理就是连接自己的测试数据库,然后在相同的环境下写入同等数量的数据，来分析一下 insert 插入的时间来进行综合其效率，为了做到最真实的效果,所有的数据采用随机生成，比如名字、邮箱、地址都是随机生成。

```
package 
            com.wyq.mysqldemo;
          
import 
            cn.hutool.core.collection.CollectionUtil;
          
import 
            com.wyq.mysqldemo.databaseobject.UserKeyAuto;
          
import 
            com.wyq.mysqldemo.databaseobject.UserKeyRandom;
          
import 
            com.wyq.mysqldemo.databaseobject.UserKeyUUID;
          
import 
            com.wyq.mysqldemo.diffkeytest.AutoKeyTableService;
          
import 
            com.wyq.mysqldemo.diffkeytest.RandomKeyTableService;
          
import 
            com.wyq.mysqldemo.diffkeytest.UUIDKeyTableService;
          
import 
            com.wyq.mysqldemo.util.JdbcTemplateService;
          
import 
            org.junit.jupiter.api.Test;
          
import 
            org.springframework.beans.factory.annotation.Autowired;
          
import 
            org.springframework.boot.test.context.SpringBootTest;
          
import 
            org.springframework.util.StopWatch;
          
import 
            java.util.List;
          

@SpringBootTest
class MysqlDemoApplicationTests {

    @Autowired
    private JdbcTemplateService jdbcTemplateService;

    @Autowired
    private AutoKeyTableService autoKeyTableService;

    @Autowired
    private UUIDKeyTableService uuidKeyTableService;

    @Autowired
    private RandomKeyTableService randomKeyTableService;

    @Test
    void testDBTime() {

        StopWatch stopwatch = new StopWatch("执行sql时间消耗");

        /**
         * auto_increment key任务
         */
        final String insertSql = "INSERT INTO user_key_auto(user_id,user_name,sex,address,city,email,state) VALUES(?,?,?,?,?,?,?)";

        List insertData = 
            autoKeyTableService.getInsertData();
          
        
            stopwatch.start(
          "自动生成key表任务开始");
        long start1 = 
            System.currentTimeMillis();
          
        if (
            CollectionUtil.isNotEmpty(insertData))
           {
            boolean insertResult = 
            jdbcTemplateService.insert(insertSql,
           insertData, false);
            
            System.out.println(insertResult);
          
        }
        long end1 = 
            System.currentTimeMillis();
          
        
            System.out.println(
          "auto key消耗的时间:" + (end1 - start1));

        
            stopwatch.stop();
          

        /**
         * uudID的key
         */
        final String insertSql2 = "INSERT INTO user_uuid(id,user_id,user_name,sex,address,city,email,state) VALUES(?,?,?,?,?,?,?,?)";

        List insertData2 = 
            uuidKeyTableService.getInsertData();
          
        
            stopwatch.start(
          "UUID的key表任务开始");
        long begin = 
            System.currentTimeMillis();
          
        if (
            CollectionUtil.isNotEmpty(insertData))
           {
            boolean insertResult = 
            jdbcTemplateService.insert(insertSql2,
           insertData2, true);
            
            System.out.println(insertResult);
          
        }
        long over = 
            System.currentTimeMillis();
          
        
            System.out.println(
          "UUID key消耗的时间:" + (over - begin));

        
            stopwatch.stop();
          

        /**
         * 随机的long值key
         */
        final String insertSql3 = "INSERT INTO user_random_key(id,user_id,user_name,sex,address,city,email,state) VALUES(?,?,?,?,?,?,?,?)";
        List insertData3 = 
            randomKeyTableService.getInsertData();
          
        
            stopwatch.start(
          "随机的long值key表任务开始");
        Long start = 
            System.currentTimeMillis();
          
        if (
            CollectionUtil.isNotEmpty(insertData))
           {
            boolean insertResult = 
            jdbcTemplateService.insert(insertSql3,
           insertData3, true);
            
            System.out.println(insertResult);
          
        }
        Long end = 
            System.currentTimeMillis();
          
        
            System.out.println(
          "随机key任务消耗时间:" + (end - start));
        
            stopwatch.stop();
          

        String result = 
            stopwatch.prettyPrint();
          
        
            System.out.println(result);
          
    }
}
```

### 1.3.程序写入结果

user\_key\_auto 写入结果：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smrwaw9vKV44tlRYl9S4NEjEgMefTlMhS4E7jv1YsWplkAJ5kwiaibt8GdAbG6dToYY5SIAgrNdffviawYI51KANcJa3p77quOFgLA/640?wx_fmt=png&from=appmsg#imgIndex=4)

user\_key\_auto 写入结果

user\_random\_key 写入结果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/pUq1tpL9smorxKem1OKOdGPPwsKfD1IlA0F3b56M36H8Rc2UoBNAOduNYWI5nPiapHiaSv2KflUqVneWvEWWJ3szHMD5MlRPrJeN1mkacxV9Y/640?wx_fmt=png&from=appmsg#imgIndex=5)

user\_random\_key 写入结果

user\_uuid 表写入结果：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smrqHV6LMjrRpyTBCbic2D5YicLAIIs75v0VuawIaqB9kQ3QBtibdtqZsS9yObOx3vT2wrN0kLF9vDhtQ1uSJzO4pLcicDJvGJnemyM/640?wx_fmt=png&from=appmsg#imgIndex=6)

user\_uuid 表写入结果

### 1.4.效率测试结果

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smr7jH9DnsDZxvdDBAXjZwo4AQle0JTP6QTzls1k2W70cVm5NSyiblpBnAAs4qUOPY9tjichfeFo27bqG66xOWv04aicdJXUQcT0fM/640?wx_fmt=png&from=appmsg#imgIndex=7)

效率测试结果

在已有数据量为 130W 的时候：我们再来测试一下插入 10w 数据，看看会有什么结果：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smpTjibwUpBfZ69mZDlFy9ibb75icrcromDLL63pVMmEkM7z5v8WEQWzS1AlqJjkcC7tGsYrRlgpqfjlkpDuNQGJsia3B8cQTuAfKgw/640?wx_fmt=png&from=appmsg#imgIndex=8)

插入 10w 数据测试结果

可以看出在数据量 100W 左右的时候,uuid 的插入效率垫底，并且在后序增加了 130W 的数据，uudi 的时间又直线下降。

时间占用量总体可以打出的效率排名为：auto\_key>random\_key>uuid,uuid 的效率最低，在数据量较大的情况下，效率直线下滑。那么为什么会出现这样的现象呢？带着疑问,我们来探讨一下这个问题：

## 二、使用 uuid 和自增 id 的索引结构对比

### 2.1.使用自增 id 的内部结构

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smqgaaGr0ibCwLakaPia0FsymdXynJRrX6bP2FbhoB9cYSZBg17b62Y4525YICEVTLayqC4dJzfEGiczibk1kdT64LSjCjRMjs2bNUY/640?wx_fmt=png&from=appmsg#imgIndex=9)

自增 id 的内部结构

自增的主键的值是顺序的,所以 Innodb 把每一条记录都存储在一条记录的后面。当达到页面的最大填充因子时候(innodb 默认的最大填充因子是页大小的 15/16,会留出 1/16 的空间留作以后的修改)：

①下一条记录就会写入新的页中，一旦数据按照这种顺序的方式加载，主键页就会近乎于顺序的记录填满，提升了页面的最大填充率，不会有页的浪费

②新插入的行一定会在原有的最大数据行下一行,mysql 定位和寻址很快，不会为计算新行的位置而做出额外的消耗

③减少了页分裂和碎片的产生

### 2.2.使用 uuid 的索引内部结构

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smpG4p0Etycr2QBEc5aDtqbEdMpxWufLlP6bJr7mzvsA3rKTkgA0Hq0RwrgOHZcUvpx4IVF66xO85R1uM6EW74vPTtyJmic9KC3o/640?wx_fmt=png&from=appmsg#imgIndex=10)

uuid 的索引内部结构

因为 uuid 相对顺序的自增 id 来说是毫无规律可言的,新行的值不一定要比之前的主键的值要大,所以 innodb 无法做到总是把新行插入到索引的最后,而是需要为新行寻找新的合适的位置从而来分配新的空间。

这个过程需要做很多额外的操作，数据的毫无顺序会导致数据分布散乱，将会导致以下的问题：

①写入的目标页很可能已经刷新到磁盘上并且从缓存上移除，或者还没有被加载到缓存中，innodb 在插入之前不得不先找到并从磁盘读取目标页到内存中，这将导致大量的随机 IO

②因为写入是乱序的,innodb 不得不频繁的做页分裂操作,以便为新的行分配空间,页分裂导致移动大量的数据，一次插入最少需要修改三个页以上

③由于频繁的页分裂，页会变得稀疏并被不规则的填充，最终会导致数据会有碎片

在把随机值（uuid 和雪花 id）载入到聚簇索引(innodb 默认的索引类型)以后,有时候会需要做一次 OPTIMEIZE TABLE 来重建表并优化页的填充，这将又需要一定的时间消耗。

结论：使用 innodb 应该尽可能的按主键的自增顺序插入，并且尽可能使用单调的增加的聚簇键的值来插入新行

### 2.3.使用自增 id 的缺点

那么使用自增的 id 就完全没有坏处了吗？并不是，自增 id 也会存在以下几点问题：

①别人一旦爬取你的数据库,就可以根据数据库的自增 id 获取到你的业务增长信息，很容易分析出你的经营情况

②对于高并发的负载，innodb 在按主键进行插入的时候会造成明显的锁争用，主键的上界会成为争抢的热点，因为所有的插入都发生在这里，并发插入会导致间隙锁竞争

③Auto\_Increment 锁机制会造成自增锁的抢夺,有一定的性能损失

##### 附：Auto\_increment 的锁争抢问题，如果要改善需要调优 innodb\_autoinc\_lock\_mode 的配置

## 三、总结

本篇博客首先从开篇的提出问题,建表到使用 jdbcTemplate 去测试不同 id 的生成策略在大数据量的数据插入表现，然后分析了 id 的机制不同在 mysql 的索引结构以及优缺点，深入的解释了为何 uuid 和随机不重复 id 在数据插入中的性能损耗，详细的解释了这个问题。

在实际的开发中还是根据 mysql 的官方推荐最好使用自增 id，mysql 博大精深，内部还有很多值得优化的点需要我们学习。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&tp=webp#imgIndex=1)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. SpringBoot 实现电子文件签字+合同系统！3. 面试官：BeanFactory 和 FactroyBean 的关系？4. 使用 Shadcn UI 构建 Java 桌面应用
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文