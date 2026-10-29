---
source_url: "https://mp.weixin.qq.com/s/b_e18FXg7KYQRnBOPnU4eQ"
title: "SpringBoot接口幂等性方案：4种策略+代码实战，告别重复提交"
account: "终码一生"
published_at: "2026-10-28 23:00:58"
saved_at: "2026-10-29 07:21:48"
sync_id: "art_48405af3547e42039994162c2a13e727"
parse_status: "ok"
---

# SpringBoot接口幂等性方案：4种策略+代码实战，告别重复提交

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

![](assets/2026-10-28%20-%20SpringBoot%E6%8E%A5%E5%8F%A3%E5%B9%82%E7%AD%89%E6%80%A7%E6%96%B9%E6%A1%88%EF%BC%9A4%E7%A7%8D%E7%AD%96%E7%95%A5+%E4%BB%A3%E7%A0%81%E5%AE%9E%E6%88%98%EF%BC%8C%E5%91%8A%E5%88%AB%E9%87%8D%E5%A4%8D%E6%8F%90%E4%BA%A4/881a8aea14790a031a3796c51f9cae68_MD5.png)

网络抖动、用户手抖、MQ 重试……任何一次“重复请求”都可能让钱扣钱、商品多发。

今天一次讲透 4 种常用幂等性实现，附可 copy 的代码 。

![](assets/2026-10-28%20-%20SpringBoot%E6%8E%A5%E5%8F%A3%E5%B9%82%E7%AD%89%E6%80%A7%E6%96%B9%E6%A1%88%EF%BC%9A4%E7%A7%8D%E7%AD%96%E7%95%A5+%E4%BB%A3%E7%A0%81%E5%AE%9E%E6%88%98%EF%BC%8C%E5%91%8A%E5%88%AB%E9%87%8D%E5%A4%8D%E6%8F%90%E4%BA%A4/e3415148a9018e581714e7cf7e6c0289_MD5.png)

01

Token 令牌 —— 最经典、最稳

![](assets/2026-10-28%20-%20SpringBoot%E6%8E%A5%E5%8F%A3%E5%B9%82%E7%AD%89%E6%80%A7%E6%96%B9%E6%A1%88%EF%BC%9A4%E7%A7%8D%E7%AD%96%E7%95%A5+%E4%BB%A3%E7%A0%81%E5%AE%9E%E6%88%98%EF%BC%8C%E5%91%8A%E5%88%AB%E9%87%8D%E5%A4%8D%E6%8F%90%E4%BA%A4/ea730ad34a93d53950aeb779339a74ef_MD5.png)

思路： 先拿令牌 → 再执行业务 → 用完即焚。

核心关键字： **预生成、一次性、Redis 原子删除**。

精简代码（含注解）

```
@RestController
@RequestMapping("/order")
publicclassOrderController {

    @Autowired
    private StringRedisTemplate redis;

    // ① 预生成 Token，给前端
    @GetMapping("/token")
    public String getToken(){
        Stringtoken= UUID.randomUUID().toString();
        // 10 分钟有效期，足够前端完成下单
        redis.opsForValue().set("tk:" + token, "1", Duration.ofMinutes(10));
        return token;
    }

    // ② 下单接口，Header 中带令牌
    @PostMapping
    public Result create(@RequestHeader("Idempotent-Token") String token,
                         @RequestBody OrderReq req) {
        Stringkey="tk:" + token;
        // 原子删除：成功返回 true 表示第一次使用
        Booleanfirst= redis.delete(key);
        if (Boolean.FALSE.equals(first)) {
            return Result.fail("**请勿重复下单**");
        }
        // 真正创建订单
        Orderorder= orderService.create(req);
        return Result.ok(order);
    }
}
```

注解：

- UUID 保证全局唯一，Redis TTL 防呆。
- delete 是原子操作，天然并发安全。
- 用 Header 传递令牌，保持接口语义纯净。

02

数据库唯一索引 —— 低成本、强一致

思路： 把“业务唯一键”做成唯一索引，重复写直接抛异常。

核心关键字： **天然幂等、异常即幂等**。

代码示例

```
@Entity
@Table(name = "t_payment",
       uniqueConstraints = @UniqueConstraint(columnNames = "transaction_id"))
publicclassPayment {
    @Id
    private Long id;

    // 支付平台返回的流水号
    @Column(name = "transaction_id")
    private String txId;

    private BigDecimal amount;
    private String status;
}

@Service
publicclassPayService {
    @Autowired
    private PaymentRepo repo;

    public Result pay(PayReq req){
        try {
            Paymentp=newPayment();
            p.setTxId(req.getTxId());
            p.setAmount(req.getAmount());
            p.setStatus("SUCCESS");
            repo.save(p);   // 重复就抛 DataIntegrityViolationException
            return Result.ok("**支付成功**");
        } catch (DataIntegrityViolationException e) {
            // 异常即查询结果，避免重复扣款
            Paymentexist= repo.findByTxId(req.getTxId());
            return Result.ok("**已支付**", exist.getId());
        }
    }
}
```

注解：

- 唯一索引兜底，数据库层面 100 % 防重。
- try-catch 把异常转成正常响应，用户体验丝滑。
- 无外部依赖，适配老旧系统也毫无压力。

03

分布式锁 —— 高并发大杀器

思路： 对“订单号 / 用户ID”加分布式锁，抢到锁再干活。

核心关键字： **互斥、超时、可重入**。

Redisson 简洁版

```
@Service
publicclassStockService {

    @Autowired
    private RedissonClient redisson;

    public Result deduct(DeductCmd cmd){
        StringlockKey="lock:stock:" + cmd.getProductId();
        RLocklock= redisson.getLock(lockKey);
        try {
            // 最多等 3 秒，持锁 5 秒自动释放
            if (!lock.tryLock(3, 5, TimeUnit.SECONDS)) {
                return Result.fail("**处理中，请稍后**");
            }
            // 业务幂等检查：根据请求 ID 查记录
            if (repo.existsByRequestId(cmd.getRequestId())) {
                return Result.ok("**已扣减**");
            }
            // 真正扣库存
            repo.deductStock(cmd);
            return Result.ok("**扣减成功**");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return Result.fail("**系统繁忙**");
        } finally {
            if (lock.isHeldByCurrentThread()) {
                lock.unlock();
            }
        }
    }
}
```

注解：

- Redisson 自带 watchdog，自动续期，不怕死锁。
- requestId 做幂等表，锁+唯一索引 双保险。
- lock.isHeldByCurrent线程 防止误删别人的锁。

04

请求内容摘要 —— 最透明、最通用

思路： 把请求体做 MD5/SHA256，作为幂等键。

核心关键字： **零额外交互、客户端无感**。

自定义注解 + AOP

```
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public@interface Idempotent {
    intexpire()default3600;   // 秒
}

@Aspect
@Component
publicclassIdempotentAspect {

    @Autowired
    private StringRedisTemplate redis;

    @Around("@annotation(idem)")
    public Object around(ProceedingJoinPoint pjp, Idempotent idem)throws Throwable {
        HttpServletRequestreq= ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        // ① 计算请求体摘要
        Stringbody= IOUtils.toString(req.getReader());
        Stringdigest= DigestUtils.md5DigestAsHex(body.getBytes(StandardCharsets.UTF_8));
        Stringkey="idem:digest:" + digest;

        // ② 第一次：setIfAbsent 返回 true
        Booleanabsent= redis.opsForValue().setIfAbsent(key, "1", Duration.ofSeconds(idem.expire()));
        if (Boolean.FALSE.equals(absent)) {
            return Result.fail("**重复请求**");
        }
        try {
            return pjp.proceed();
        } catch (Exception e) {
            redis.delete(key);  // 异常时释放，允许重试
            throw e;
        }
    }
}

// 使用
@RestController
publicclassTransferApi {
    @PostMapping("/transfer")
    @Idempotent(expire = 7200)
    public Result transfer(@RequestBody TransferCmd cmd){
        return Result.ok(transferSvc.doTransfer(cmd));
    }
}
```

注解：

- MD5 把任意长度报文压缩成 32 位，冲突概率极低。
- setIfAbsent 保证原子性，异常回删避免误杀。
- 注解 + AOP 零侵入，老接口 1 行代码即可拥有幂等。

05

小结

| 方案 | 延迟 | 复杂度 | 外部依赖 | 适用场景 |
| --- | --- | --- | --- | --- |
| ** Token ** | 中 | 低 | Redis | 有预生成环节：下单、支付 |
| ** 唯一索引 ** | 低 | 低 | 无 | 支付、注册 |
| ** 分布式锁 ** | 中 | 中 | Redis/ZK | 高并发抢券、秒杀 |
| ** 内容摘要 ** | 低 | 中 | Redis | 无预生成：转账、回调 |

06

实施清单

- 检查你的核心接口有没有唯一业务键。
- 优先使用数据库唯一索引，成本最低。
- 并发量高再上分布式锁或Token，不要过度设计。
- 给关键接口加上监控告警，幂等失败时第一时间知道。

来源：互联网

---
原文链接：https://mp.weixin.qq.com/s/b_e18FXg7KYQRnBOPnU4eQ
