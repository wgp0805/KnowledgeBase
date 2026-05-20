---
title: "面试中被嘲笑Token放在Redis里？这把给我干沉默了...."
source: "https://mp.weixin.qq.com/s/iGuqH-MvOC7FZHoXMUbM7A"
---
面试被问到登录认证怎么做，你说"Token放Redis里"。然后面试官笑了一下，说你不懂JWT的无状态设计。

这场景不少见。知乎上有人专门问过这件事，底下的回答挺有意思，争了半天，其实说的是同一件事：**选型没问题，但你没说清楚为什么选。**

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/60308b7877688de24084dd23e4002b19_MD5.webp)

这篇文章就把这件事说清楚：**从JWT是什么，到放Redis的原因，再到面试里怎么回答，一块讲完。**

---

# JWT到底是什么

JWT全称是JSON Web Token。说白了就是一段字符串，长这样：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

看起来一堆乱码，但其实结构很清晰。用点号分成三段：Header、Payload、Signature。

![JWT的三段结构：Header（算法类型）、Payload（用户信息）、Signature（签名），三部分Base64编码后用点号连接](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/1429049e0607cc0d00d325a7739c5df2_MD5.webp)

JWT的三段结构：Header（算法类型）、Payload（用户信息）、Signature（签名），三部分Base64编码后用点号连接

**Header** 说明这个Token用的什么算法，比如HS256。

**Payload** 存用户信息，比如用户ID、角色、过期时间。但注意，这部分只是Base64编码，并没有加密。任何人拿到token都能解码看到里面的内容，所以密码这类东西绝对不能放进去。

**Signature** 是用Header和Payload加上服务端密钥算出来的签名。作用是防篡改。别人拿到token改了里面的信息，签名就对不上了，服务端一验就知道。

用 [jwt.io这个网站可以直接解码：](http://jwt.io这个网站可以直接解码：)

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/7f804162d32cfb84757253d6d3ff74d8_MD5.webp)

整个验证流程大概是这样：

![JWT认证完整流程：用户登录→服务端签发Token→客户端存储→请求时带上Token→服务端验签](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/b1ef5c16106c60f6242799f48b7b49bf_MD5.webp)

JWT认证完整流程：用户登录→服务端签发Token→客户端存储→请求时带上Token→服务端验签

登录成功，服务端签发Token，客户端保存起来（一般放localStorage）。以后每次请求，在Header里带上：

```
Authorization: Bearer <token>
```

服务端收到请求，验证签名，从Payload里取用户信息。全程不查数据库，不查Redis，自给自足。这就是"无状态"的意思。

---

# JWT"无状态"的问题在哪里

无状态听起来很美，上线后就知道了。

**场景一：用户密码被盗**

产品经理找过来说：用户A的账号被盗了，要立刻把他踢下线。

然后你看了一眼系统，token的有效期是2小时，现在还剩1小时45分钟。

怎么让这个token立刻失效？纯JWT方案，没有办法。已经签发出去的token，在过期之前一直有效。服务端压根不记录签发过哪些token，自然也没法说"这个作废了"。

**场景二：封禁用户**

运营后台要封一个违规账号。账号封了，但他手里的token还能用，还能继续操作。

**场景三：修改密码**

用户改了密码，想让其他设备上的登录状态全部失效。纯JWT做不到，除非等token自然过期。

**场景四：用户正在填表单**

用户填了一个大表单，填了20多分钟，点提交。token过期了，请求被拒，整个表单内容全丢了。

这几个场景加在一起，几乎是所有正经业务系统都会碰到的问题。

---

# 为什么要把Token放Redis

解决上面这些问题，有几种思路。

> 最直接的是黑名单。

用户被踢下线的时候，把这个token加进黑名单。每次请求来了先查黑名单，在里面就拒掉。

黑名单存哪里？内存不行，多台服务器之间不共享，重启还会丢。数据库太慢，每个请求都查一次受不了。Redis最合适，查询不到1ms，分布式场景下多台服务器也能共享。

代码大概是这样：

```
// 退出登录时，把 token 加入黑名单public void logout(String token) {    long expiration = 
            jwtUtil.getExpiration(token);
              long ttl = expiration - 
            System.currentTimeMillis();
              if (ttl > 0) {        // key加前缀，TTL和token过期时间对齐，不会留垃圾数据        
            redisTemplate.opsForValue().set(
                      "blacklist:" + token, "1", ttl, 
            TimeUnit.MILLISECONDS
                  );    }}// 验证token时，先查黑名单public boolean isTokenValid(String token) {    if (
            redisTemplate.hasKey(
          "blacklist:" + token)) {        return false; // 在黑名单里，直接拒    }    return 
            jwtUtil.verify(token);
           // 验签名}
```

这就是黑名单方案。Redis只存"已失效"的token，平时没什么写入，查询也快。

还有另一种方案，更彻底：**直接把token存Redis，每次验证都去Redis查，不走JWT验签那套。** 这和传统Session方案没太大区别，只是用了JWT的格式来当Session ID用。

---

# 两种方案到底有什么区别

| 方案 | 存什么 | 查几次Redis | 能否主动吊销 | 是否无状态 |
| --- | --- | --- | --- | --- |
| 纯JWT | 不存 | 0次 | 不能 | 是 |
| JWT+黑名单 | 存失效的token | 1次 | 能 | 不完全是 |
| token存Redis（白名单） | 存所有token | 1次 | 能 | 否 |

黑名单方案相对轻量，正常请求不写Redis，只有踢人的时候才写，多数业务选这个。

白名单方案控制力更强，能做限制同时在线设备数、实时查看在线状态之类的功能，代价是每次请求都依赖Redis。

---

# 续期问题

token到期了，用户正在操作怎么办？

常见的做法是**双token**。签发两个：

- • **AccessToken**：有效期短，比如30分钟，用来做实际鉴权
- • **RefreshToken**：有效期长，比如7天，只用来换AccessToken

流程是这样：AccessToken过期了，前端用RefreshToken去换一个新的AccessToken，对用户无感。

RefreshToken存哪里？要支持主动吊销的话，存Redis。用户修改密码，就删掉对应的RefreshToken，自动让他下次操作时重新登录。

---

# Redis本身可靠吗

有人担心把token放Redis会不会引入单点故障？这个问题其实问的是Redis本身的可靠性。

Redis的高可用方案有两套：

- • **Redis Sentinel（哨兵模式）**：主节点挂了，自动选出新的主节点，应用基本无感知
- • **Redis Cluster（集群模式）**：数据分片存储，横向扩展，一个节点挂了不影响整体
![Redis Cluster架构：数据分片分布在多个节点，支持横向扩展和自动故障转移](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/08baa65ee9fde9ec6494f15effdaccf9_MD5.webp)

Redis Cluster架构：数据分片分布在多个节点，支持横向扩展和自动故障转移

用Redis存Session是业界跑了十几年的方案，稳定性没什么可质疑的。说"不能放Redis因为会单点故障"，这逻辑说不通。

性能方面，Redis单次查询在1ms以内，单机QPS能到十几万。普通业务规模下，Redis完全不是瓶颈。

---

# 面试官在嘲笑什么

说清楚了技术背景，再来看面试官笑了那下是什么意思。

有两种情况。

**第一种**：你用了JWT，但验证时完全不走签名那套，每次都去Redis查token是否存在。这等于只借了JWT的格式，没用它的能力。这种情况不如直接生成一个随机字符串当Session ID，还省了JWT编解码的开销。面试官嘲笑的是这里，用了一个工具但没用对。

**第二种**：你确实有业务需求，需要主动吊销token，选了JWT+Redis黑名单方案。但你在面试里只说了结果（"放Redis里"），没说为什么，让面试官误以为你不清楚JWT无状态的设计理念。

第一种情况，确实是方案选错了，得改。第二种情况，方案没问题，表达出了问题。

---

# 纯JWT什么时候真的合适

不是说JWT必须配Redis。有些场景下纯JWT确实够用。

**跨服务调用**。微服务架构里，网关层做一次验签，把用户信息往下游传。订单服务、支付服务从JWT里直接取userId，不用再查Redis。这种场景下JWT的无状态真的减少了很多冗余查询。

```
用户请求  → 网关（验证JWT签名）    → 订单服务（直接从JWT解析userId）    → 支付服务（直接从JWT解析userId）
```

这里JWT承担的是服务间传递用户身份的角色，不是管理登录会话的。

**一次性凭证**。邮箱验证链接、密码重置链接、临时分享链接。签一次，用一次，不需要续期也不需要主动吊销。JWT自包含的特性在这里最舒服。

**对安全要求不高的工具类系统**。比如内部小工具，用户量少，不需要踢人下线。纯JWT省一层依赖，也完全够用。

---

# 面试怎么答

别上来就说"我把token放Redis里"，也别上来就说"我用JWT无状态方案"。

先说业务需求：系统需不需要主动踢人下线？用户改密码后，需不需要其他设备立刻失效？需不需要限制同时在线的设备数量？

然后根据需求说方案：

**需要的话**：选JWT+Redis黑名单，或者直接用Redis管理token。把纯JWT做不了主动吊销这件事说清楚，说明你是因为业务需要才引入Redis，而不是乱加。

**不需要的话**：纯JWT够了，说清楚签名验证的流程、过期策略，以及密钥怎么管理。

面试官真正想听的不是你选了哪个，是你知不知道每个方案的边界在哪。"Token放Redis"这件事本身没问题，问题是说不出来为什么放。

---

# 小结

JWT无状态的核心优势在于验签不依赖服务端存储，适合跨服务身份传递。但无状态带来的代价是没法主动吊销，只要业务有"踢人下线"的需求，就得引入外部存储。

Redis黑名单是目前最常见的折中方案，只存已失效的token，正常请求不写Redis。双token方案解决续期问题，短期AccessToken做鉴权，长期RefreshToken存Redis做吊销控制。

"Token放Redis"本身是合理的，Redis的性能和可靠性都撑得住。面试里被怼，大多数时候不是选错了，是没说清楚。先想业务需求，再解释技术选型，这个顺序比较重要。