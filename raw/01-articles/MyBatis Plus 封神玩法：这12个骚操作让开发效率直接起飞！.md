---
title: "MyBatis Plus 封神玩法：这12个骚操作让开发效率直接起飞！"
source: "https://mp.weixin.qq.com/s/4y7nDVJs4rR8kG8wUsksXw"
---
小哈学Java *2026年6月26日 16:30*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smqOn8kbfzKiawicvEd7UBGyLuUzCEZSVwh4CO0yWqojfs1n27CFgIOtK2U0x3DzmLvTbaFmzSfBicKu2eOMs3SGwGzxG8kewCbfjg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

来源： [https://juejin.cn/post/7436567167728812044](https://juejin.cn/post/7436567167728812044)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 前言
- 避免使用isNull判断
- 明确Select字段
- 批量操作方法替代循环
- Exists方法子查询
- 使用orderBy代替last
- 使用LambdaQuery确保类型安全
- 用between代替ge和le
- 排序字段注意索引
- 分页参数设置
- 条件构造处理Null值
- 查询性能追踪
- 枚举类型映射
- 自动处理逻辑删除
- 乐观锁更新保护
- 递增和递减：setIncrBy 和 setDecrBy
- 总结

---

## 前言

说起数据库 ORM，我忽然想起了小时候外婆做的那锅鲜美的羊肉汤。平常人家做的羊肉汤无非是几块肉、几片姜，味道寡淡得很，喝了和喝白开水差不多。但外婆的汤，那是另一回事儿 —— 一锅汤，香气四溢，肉质软烂，汤头浓郁得能让人连碗都想舔干净。

写代码何尝不是如此？以前写 Mybatis，就像是在煮一锅没有灵魂的羊肉汤：原料都在，但就是不够鲜美。代码繁琐，每写一个查询都像是在不断调味，却怎么也调不出那种令人惊艳的味道。直到遇见 MyBatisPlus，一切都变了 —— 这就像是从普通的羊肉汤，突然升级到了外婆秘制的顶级羊肉汤！

MyBatisPlus 就像一位精通厨艺的帮厨，它帮你处理了所有繁琐的准备工作。想要一个复杂的查询？不用自己一刀一刀地切肉、一勺一勺地调味，框架已经帮你准备好了。你只需要轻轻地指挥，代码就像汤汁一样顺滑流畅，性能更是鲜美可口。

在接下来的篇幅里，我将与你分享 12 个 MyBatisPlus 优化的"秘制配方"。相信看完这些，你写的每一行代码，都会像外婆的羊肉汤一样，让人回味无穷。

耐心看完，你一定有所收获。

## 避免使用isNull判断

```
// ❌ 不推荐
LambdaQueryWrapper<User> wrapper1 = new LambdaQueryWrapper<>();

            wrapper1.isNull(User::getStatus);
          

// ✅ 推荐：使用具体的默认值
LambdaQueryWrapper<User> wrapper2 = new LambdaQueryWrapper<>();

            wrapper2.eq(User::getStatus,
           
            UserStatusEnum.INACTIVE.getCode());
```

原因:

- 使用具体的默认值可以提高代码的可读性和维护性
- NULL 值会使索引失效，导致 MySQL 无法使用索引进行查询优化
- NULL 值的比较需要特殊的处理逻辑，增加了 CPU 开销
- NULL 值会占用额外的存储空间，影响数据压缩效率

## 明确Select字段

```
// ❌ 不推荐
// 默认select 所有字段
List users1 = 
            userMapper.selectList(null);
          

// ✅ 推荐：指定需要的字段
LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();

            wrapper.select(User::getId,
           User::getName, User::getAge);
List users2 = 
            userMapper.selectList(wrapper);
```

原因:

- 避免大量无用字段的网络传输开销
- 可以利用索引覆盖，避免回表查询
- 减少数据库解析和序列化的负担
- 降低内存占用，特别是在大量数据查询时

## 批量操作方法替代循环

```
// ❌ 不推荐
for (User user : userList) {
    
            userMapper.insert(user);
          
}

// ✅ 推荐

            userService.saveBatch(userList,
           100); // 每批次处理100条数据

// ✅ 更优写法：自定义批次大小

            userService.saveBatch(userList,
           
            BatchConstants.BATCH_SIZE);
```

原因:

- 减少数据库连接的创建和销毁开销
- 批量操作可以在一个事务中完成，提高数据一致性
- 数据库可以优化批量操作的执行计划
- 显著减少网络往返次数，提升吞吐量

## Exists方法子查询

```
// ❌ 不推荐

            wrapper.inSql(
          "user_id", "select user_id from order where amount > 1000");

// ✅ 推荐

            wrapper.exists(
          "select 1 from order where 
            order.user_id
           = 
            user.id
           and amount > 1000");

// ✅ 更优写法：使用LambdaQueryWrapper

            wrapper.exists(orderService.lambdaQuery()
          
    .gt(Order::getAmount, 1000)
    .apply("
            order.user_id
           = 
            user.id"
          ));
```

原因:

- EXISTS 是基于索引的快速查询，可以使用到索引
- EXISTS 在找到第一个匹配项就会停止扫描
- IN 子查询需要加载所有数据到内存后再比较
- 当外表数据量大时，EXISTS 的性能优势更明显

## 使用orderBy代替last

```
// ❌ 不推荐：SQL注入风险

            wrapper.last(
          "ORDER BY " + sortField + " " + sortOrder);

// ❌ 不推荐：直接字符串拼接

            wrapper.last(
          "ORDER BY FIELD(status, 'active', 'pending', 'inactive')");

// ✅ 推荐：使用 Lambda 安全排序

            wrapper.orderBy(
          true, true, User::getStatus);

// ✅ 推荐：多字段排序示例

            wrapper.orderByAsc(User::getStatus)
          
       .orderByDesc(User::getCreateTime);
```

原因:

- 直接拼接 SQL 容易导致 SQL 注入攻击
- 动态 SQL 可能破坏 SQL 语义完整性
- 影响 SQL 语句的可维护性和可读性
- last 会绕过 MyBatis-Plus 的安全检查机制

## 使用LambdaQuery确保类型安全

```
// ❌ 不推荐：字段变更后可能遗漏
QueryWrapper<User> wrapper1 = new QueryWrapper<>();

            wrapper1.eq(
          "name", "张三").gt("age", 18);

// ✅ 推荐
LambdaQueryWrapper<User> wrapper2 = new LambdaQueryWrapper<>();

            wrapper2.eq(User::getName,
           "张三")
        .gt(User::getAge, 18);

// ✅ 更优写法：使用链式调用

            userService.lambdaQuery()
          
    .eq(User::getName, "张三")
    .gt(User::getAge, 18)
    .list();
```

原因:

- 编译期类型检查，避免字段名拼写错误
- IDE 可以提供更好的代码补全支持
- 重构时能自动更新字段引用
- 提高代码的可维护性和可读性

## 用between代替ge和le

```
// ❌ 不推荐

            wrapper.ge(User::getAge,
           18)
       .le(User::getAge, 30);

// ✅ 推荐

            wrapper.between(User::getAge,
           18, 30);

// ✅ 更优写法：条件动态判断

            wrapper.between(ageStart
           != null && ageEnd != null,
               User::getAge, ageStart, ageEnd);
```

原因:

- 生成的 SQL 更简洁，减少解析开销
- 数据库优化器可以更好地处理范围查询
- 代码更易读，语义更清晰
- 减少重复编写字段名的机会

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&tp=webp#imgIndex=1)

## 排序字段注意索引

```
// ❌ 不推荐
// 假设lastLoginTime无索引

            wrapper.orderByDesc(User::getLastLoginTime);
          

// ✅ 推荐
// 主键排序

            wrapper.orderByDesc(User::getId);
          

// ✅ 更优写法：组合索引排序

            wrapper.orderByDesc(User::getStatus)
            // status建立了索引
       .orderByDesc(User::getId);     // 主键排序
```

原因:

- 索引天然具有排序特性，可以避免额外的排序操作
- 无索引排序会导致文件排序，极大影响性能
- 当数据量大时，内存排序可能导致溢出
- 利用索引排序可以实现流式读取

## 分页参数设置

```
// ❌ 不推荐

            wrapper.last(
          "limit 1000"); // 一次查询过多数据

// ✅ 推荐
Page<User> page = new Page<>(1, 10);

            userService.page(page,
           wrapper);

// ✅ 更优写法：带条件的分页查询
Page result = 
            userService.lambdaQuery()
          
    .eq(User::getStatus, "active")
    .page(new Page<>(1, 10));
```

原因:

- 控制单次查询的数据量，避免内存溢出
- 提高首屏加载速度，优化用户体验
- 减少网络传输压力
- 数据库资源利用更合理

## 条件构造处理Null值

```
// ❌ 不推荐
if (
            StringUtils.isNotBlank(name))
           {
    
            wrapper.eq(
          "name", name);
}
if (age != null) {
    
            wrapper.eq(
          "age", age);
}

// ✅ 推荐

            wrapper.eq(StringUtils.isNotBlank(name),
           User::getName, name)
       .eq(
            Objects.nonNull(age),
           User::getAge, age);

// ✅ 更优写法：结合业务场景

            wrapper.eq(StringUtils.isNotBlank(name),
           User::getName, name)
       .eq(
            Objects.nonNull(age),
           User::getAge, age)
       .eq(User::getDeleted, false)  // 默认查询未删除记录
       .orderByDesc(User::getCreateTime);  // 默认按创建时间倒序
```

原因:

- 优雅处理空值，避免无效条件
- 减少代码中的 if-else 判断
- 提高代码可读性
- 防止生成冗余的 SQL 条件

⚠️ 下面就要来一些高级货了

## 查询性能追踪

```
// ❌ 不推荐：简单计时，代码冗余
public List<User> listUsers(QueryWrapper<User> wrapper) {
    long startTime = 
            System.currentTimeMillis();
          
    List users = 
            userMapper.selectList(wrapper);
          
    long endTime = 
            System.currentTimeMillis();
          
    
            log.info(
          "查询耗时：{}ms", (endTime - startTime));
    return users;
}

// ✅ 推荐：使用 Try-with-resources 自动计时
public List<User> listUsersWithPerfTrack(QueryWrapper<User> wrapper) {
    try (
            PerfTracker.TimerContext
           ignored = 
            PerfTracker.start())
           {
        return 
            userMapper.selectList(wrapper);
          
    }
}

// 性能追踪工具类
@Slf4j
public class PerfTracker {
    private final long startTime;
    private final String methodName;

    private PerfTracker(String methodName) {
        
            this.startTime
           = 
            System.currentTimeMillis();
          
        
            this.methodName
           = methodName;
    }

    public static TimerContext start() {
        return new TimerContext(
            Thread.currentThread().getStackTrace()[2].getMethodName());
          
    }

    public static class TimerContext implements AutoCloseable {
        private final PerfTracker tracker;

        private TimerContext(String methodName) {
            
            this.tracker
           = new PerfTracker(methodName);
        }

        @Override
        public void close() {
            long executeTime = 
            System.currentTimeMillis()
           - 
            tracker.startTime;
          
            if (executeTime > 500) {
                
            log.warn(
          "慢查询告警：方法 {} 耗时 {}ms", 
            tracker.methodName,
           executeTime);
            }
        }
    }
}
```

原因:

- 业务代码和性能监控代码完全分离
- try-with-resources 即使发生异常，close() 方法也会被调用，确保一定会记录耗时
- 不需要手动管理计时的开始和结束
- 更优雅

## 枚举类型映射

```
// 定义枚举
public enum UserStatusEnum {
    NORMAL(1, "正常"),
    DISABLED(0, "禁用");

    @EnumValue // MyBatis-Plus注解
    private final Integer code;
    private final String desc;
}

// ✅ 推荐：自动映射
public class User {
    private UserStatusEnum status;
}

// 查询示例

            userMapper.selectList(
          
    new LambdaQueryWrapper<User>()
        .eq(User::getStatus, 
            UserStatusEnum.NORMAL)
          
);
```

原因:

- 类型安全
- 自动处理数据库和枚举转换
- 避免魔法值
- 代码可读性更强

## 自动处理逻辑删除

```
@TableLogic  // 逻辑删除注解
private Integer deleted;

// ✅ 推荐：自动过滤已删除数据
public List<User> getActiveUsers() {
    return 
            userMapper.selectList(null);
            // 自动过滤deleted=1的记录
}

// 手动删除

            userService.removeById(1L);
            // 实际是更新deleted状态
```

原因:

- 数据不丢失
- 查询自动过滤已删除数据
- 支持数据恢复
- 减少手动编写删除逻辑

📷 注意：

- XML 中需要手动拼接 deleted = 1

## 乐观锁更新保护

```
public class Product {
    @Version // 乐观锁版本号
    private Integer version;
}

// ✅ 推荐：更新时自动处理版本
public boolean reduceStock(Long productId, Integer count) {
    LambdaUpdateWrapper<Product> wrapper = new LambdaUpdateWrapper<>();
    
            wrapper.eq(Product::getId,
           productId)
           .ge(Product::getStock, count);

    Product product = new Product();
    
            product.setStock(product.getStock()
           - count);

    return 
            productService.update(product,
           wrapper);
}
```

原因:

- 防止并发冲突
- 自动处理版本控制
- 简化并发更新逻辑
- 提高数据一致性

## 递增和递减：setIncrBy 和 setDecrBy

```
// ❌ 不推荐：使用 setSql

            userService.lambdaUpdate()
          
    .setSql("integral = integral + 10")
    .update();

// ✅ 推荐：使用 setIncrBy

            userService.lambdaUpdate()
          
    .eq(User::getId, 1L)
    .setIncrBy(User::getIntegral, 10)
    .update();

// ✅ 推荐：使用 setDecrBy

            userService.lambdaUpdate()
          
    .eq(User::getId, 1L)
    .setDecrBy(User::getStock, 5)
    .update();
```

原因:

- 类型安全
- 避免手动拼接 sql，防止 sql 注入
- 代码可维护性更强，更清晰

## 总结

写代码如烹小鲜，讲究的是精细和用心。就像一碗好汤，不仅仅在于锅和火候，更在于厨师对食材的理解和尊重。MyBatisPlus 的这 12 个优化技巧，何尝不是程序员对代码的一种尊重和雕琢？

还记得文章开头说的外婆的羊肉汤吗？优秀的代码，和一碗好汤，都需要用心。每一个细节，每一个调整，都是为了让最终的成果更加完美。MyBatisPlus 就像是厨房里的得力助手，它帮你处理繁琐，让你专注于创造。

当你掌握了这些技巧，你的代码将不再是简单的指令堆砌，而是一首优雅的诗，一曲悦耳的交响乐。它们将像外婆的羊肉汤一样，散发着独特的魅力，让人回味无穷。

愿每一位开发者，都能用 MyBatisPlus，煮出属于自己的"秘制汤羹"！

代码，就应该是这个样子 —— 简单而不失优雅，高效而不失温度。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&tp=webp#imgIndex=1)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？3. 3个完美替代 Navicat 的工具，香~
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文