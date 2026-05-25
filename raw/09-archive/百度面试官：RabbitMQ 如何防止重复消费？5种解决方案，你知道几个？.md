---
title: "百度面试官：RabbitMQ 如何防止重复消费？5种解决方案，你知道几个？"
source: "https://mp.weixin.qq.com/s/buTegauDVcxTTmWjiUNFdQ"
---

## 面试考察点

1. **问题溯源** ：面试官不仅仅是想知道怎么防重复，更是想确认你是否清楚重复消费是怎么产生的（网络抖动、消费者重启、ACK 超时等），而不是一上来就背方案。
2. **幂等性设计** ：是否理解 "防重复消费" 的本质是业务幂等，能否给出具体的实现方案（唯一 ID、去重表、状态机等）。
3. **方案选型能力** ：能否根据业务场景选择合适的幂等方案，而不是上来就 "用 Redis"。

## 核心答案

先理清一条关键逻辑：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/pUq1tpL9smpWm0tQOTZqXicUhwwXH6sJ3XH5X5FAgZjdq7mtyC6BkWy5qpJ67KEy8JF2OdoItdSoDtcU55pVBQVqWjMW0PQfCYtgIRGBgIhk/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

img

上图展示了重复消费产生的典型场景。根本原因在于： **消费者处理完了业务逻辑，但在发送 ACK 之前挂了或网络断了，RabbitMQ 没收到 ACK，就会把消息重新投递** 。

所以核心思路是： **不管消息被投递多少次，业务结果只生效一次——这就是幂等性** 。

常见的幂等方案对比：

| 方案 | 实现方式 | 适用场景 | 复杂度 |
| --- | --- | --- | --- |
| **唯一消息 ID + 去重表** | 给每条消息分配全局唯一 ID，消费前查去重表 | 通用方案，最常用 | 中 |
| **数据库唯一约束** | 利用表的主键或唯一索引防重复插入 | 新增类操作（下单、充值） | 低 |
| **Redis SETNX** | 用 `SETNX` 命令判断是否已处理 | 高并发、对性能敏感 | 低 |
| **乐观锁 / 版本号** | 更新时带上版本号条件 | 更新类操作（扣库存、改余额） | 中 |
| **状态机** | 业务状态只能单向流转（如 待支付 → 已支付） | 订单、工单等有明确状态的业务 | 中 |

## 深度解析

### 一、唯一消息 ID + 去重表（最通用）

这是生产环境用得最多的方案，几乎所有场景都能覆盖。

**原理** ：给每条消息分配一个全局唯一 ID（ `messageId` ），消费前先查去重表，如果已存在就跳过，不存在就处理并写入去重表。

```java
// 消费者伪代码
@RabbitListener(queues = "
            order.queue"
          )
public void handleOrder(Message message, Channel channel)
        throws Exception {

    String messageId = 
            message.getMessageProperties().getMessageId();
          

    try {
        // 1. 查去重表：这条消息处理过没？
        if (
            duplicateMapper.existsById(messageId))
           {
            // 处理过了，直接 ACK，别再投递了
            
            channel.basicAck(message.getMessageProperties()
          
                .getDeliveryTag(), false);
            return;
        }

        // 2. 没处理过，执行业务逻辑
        
            orderService.createOrder(parseOrder(message));
          

        // 3. 写入去重表，标记已处理
        
            duplicateMapper.insert(
          new DuplicateRecord(messageId));

        // 4. 确认消费
        
            channel.basicAck(message.getMessageProperties()
          
            .getDeliveryTag(), false);

    } catch (Exception e) {
        // 业务异常，拒绝并重回队列
        
            channel.basicNack(message.getMessageProperties()
          
            .getDeliveryTag(), false, true);
    }
}
```

这里有个关键细节： **步骤 2 和步骤 3 必须在同一个本地事务中** ，要么一起成功，要么一起失败。否则业务执行了但去重表没写进去，下次还会重复执行。

去重表结构很简单：

```sql
CREATE TABLE \`msg_duplicate\` (
    \`message_id\` VARCHAR(64) PRIMARY KEY COMMENT '消息唯一 ID',
    \`create_time\` DATETIME DEFAULT NOW() COMMENT '处理时间'
);
```

生产环境建议定期清理去重表（比如只保留 7 天），不然会无限膨胀。
### 二、数据库唯一约束（最省事）

如果你的业务本身就是 "新增" 操作（比如下单、注册），那直接用数据库的唯一约束就够了，连去重表都省了。

```java
@RabbitListener(queues = "
            order.queue"
          )
public void handleOrder(Message message, Channel channel) {

    Order order = parseOrder(message);

    try {
        // order_no 上有唯一索引，重复插入会抛 DuplicateKeyException
        
            orderMapper.insert(order);
          

    } catch (DuplicateKeyException e) {
        // 唯一索引冲突 → 说明已经处理过了，直接跳过
        
            log.warn(
          "重复消息，已跳过: {}", 
            order.getOrderNo());
          
    }

    // 不管是成功还是重复，都 ACK
    
            channel.basicAck(...);
          
}
```

这个方案我最喜欢， **简单粗暴且可靠** ，只要你的业务表有天然的唯一键（订单号、支付流水号等），直接用就完了。

### 三、Redis SETNX（高性能）

高并发场景下，每次消费都查数据库去重表可能有性能瓶颈。用 Redis 的 `SETNX` （ `SET if Not eXists` ）可以实现高性能去重。

```java
@RabbitListener(queues = "
            order.queue"
          )
public void handleOrder(Message message, Channel channel) {

    String messageId = 
            message.getMessageProperties().getMessageId();
          

    // SETNX：如果 key 不存在则设置成功返回 true，已存在返回 false
    Boolean isFirst = 
            stringRedisTemplate.opsForValue()
          
        .setIfAbsent("msg:dedup:" + messageId, "1",
                     24, 
            TimeUnit.HOURS);
            // 设过期时间，防止 key 堆积

    if (
            Boolean.FALSE.equals(isFirst))
           {
        // 已处理过，跳过
        
            channel.basicAck(...);
          
        return;
    }

    // 执行业务逻辑
    
            orderService.createOrder(parseOrder(message));
          
    
            channel.basicAck(...);
          
}
```

注意这里有个坑：\*\* `SETNX` 成功和业务执行之间存在时间差，如果业务执行失败，Redis 里已经标记为 "已处理" 了，消息就丢了\*\*。解决办法是用 Lua 脚本保证原子性，或者干脆用方案一（数据库去重表 + 本地事务）。

### 四、乐观锁（适合更新操作）

扣库存、改余额这种 "更新" 操作，用唯一 ID 不太好使，因为同一条消息可能需要重复更新。这时候乐观锁更合适。

```sql
-- 扣减库存，带上版本号条件
UPDATE goods_stock
SET stock = stock - 1, version = version + 1
WHERE goods_id = 1001
  AND version = 5    -- 版本号必须匹配
  AND stock > 0;     -- 库存必须充足
```

如果这条 SQL 返回影响行数为 0，说明要么版本号变了（重复消费），要么库存不足，两种情况都不需要重试。

## 面试高频追问

1. **RabbitMQ 能不能从自身机制上避免重复投递？**
	不能完全避免。RabbitMQ 的 `ACK` 机制只能保证 "至少一次投递"（ `at least once` ），不保证 "恰好一次"（ `exactly once` ）。所以业务层幂等是必须的。
2. **去重表和业务表不在同一个数据库怎么办？**
	可以用分布式事务（ `Seata` ），但引入了复杂度。更实际的做法是：先写去重表（带状态字段），再通过定时任务补偿执行业务逻辑。或者直接用 Redis `SETNX` + 数据库唯一约束双重保障。
3. **消息量特别大，去重表会不会成为瓶颈？**
	会。可以分层：Redis 做第一层快速去重（设过期时间），数据库去重表做第二层兜底。Redis 命中了直接跳过，没命中再查数据库。

## 常见面试变体

- "RabbitMQ 消息重复消费怎么解决？"
- "如何保证消息的幂等性？"
- "消息队列的 `exactly once` 语义怎么实现？"

## 记忆口诀

**防重复 = 业务幂等** ，RabbitMQ 只保 "至少一次"，不保 "恰好一次"。

**五种方案** ：去重表最通用、唯一约束最省事、Redis `SETNX` 最快、乐观锁适合更新、状态机适合订单流转。

## 总结

一句话：RabbitMQ 重复消费不可避免（ACK 机制决定），真正的解法是 **业务层做幂等** 。生产环境最常用的是 "唯一消息 ID + 去重表"，如果业务本身有唯一键（订单号），直接用数据库唯一约束更简洁。高并发场景用 Redis `SETNX` 加速。面试时先说清楚 "为什么会产生重复消费"，再给出 2-3 种方案并分析适用场景，这道题就是满分。
