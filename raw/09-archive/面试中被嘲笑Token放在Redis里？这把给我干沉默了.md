---
title: "面试中被嘲笑Token放在Redis里？这把给我干沉默了..."
source: "https://mp.weixin.qq.com/s/_0c6JbmwtMytnJrMWSarsQ"
---
Java专栏 *2026年6月23日 12:20*

面试被问登录认证怎么做，你说"Token 放 Redis 里"。面试官笑了一下，说你不懂 JWT 的无状态设计。这场景不少见。知乎上有人专门问过，底下争了半天，说的其实是同一件事：选型没问题，但你没说清楚为什么选。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/9e6929586f20dc05282882a5090e01d0_MD5.webp)

这篇文章把这件事说清楚：从 JWT 是什么，到放 Redis 的原因，再到面试里怎么回答。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/cbcaaf22f406380157c49da576b866f9_MD5.webp)

01

JWT 到底是什么

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/2d550a8c83585413cdfa8f2a56bfaf34_MD5.webp)
- Payload ：存用户信息（用户 ID、角色、过期时间）。只是 Base64 编码，不是加密 ——任何人拿到 token 都能解码看到内容，密码绝对不能放
![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/782648a6fb79e0f6fd12e951b0de643b_MD5.jpg)

整个验证流程：

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/0cc234bc4a14124b0a88050bc70edd9c_MD5.png)

JWT认证完整流程：用户登录→服务端签发Token→客户端存储→请求时带上Token→服务端验签

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

JWT"无状态"的代价：四个致命场景

无状态听起来很美，上线后就知道了。

1. 账号被盗，无法立即踢人 。Token 有效期 2 小时，现在还剩 1 小时 45 分钟。怎么让它立刻失效？纯 JWT 做不到——已签发的 token 在过期前一直有效。
2. 封禁用户不生效 。账号封了，但手里的 token 还能用。
3. 改密码不踢其他设备 。用户改了密码，想让其他设备全部失效。纯 JWT 做不到。
4. token 过期吞表单 。用户填了 20 多分钟的表单，点提交，token 过期了，整个内容全丢。

这四个场景加在一起，几乎是所有正经业务系统都会碰到的问题。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

03

为什么要把 Token 放 Redis

解决上面这些问题，最直接的方案是黑名单 。用户被踢下线时，把 token 加进黑名单。每次请求先查黑名单，在里面就拒。

黑名单存哪？内存不行（多台服务器不共享，重启丢），数据库太慢（每个请求都查一次受不了），Redis 最合适 ——查询不到 1ms，分布式共享。

```
// 退出登录时，把 token 加入黑名单
publicvoidlogout(String token){
    long expiration = 
            jwtUtil.getExpiration(token);
          
    long ttl = expiration - 
            System.currentTimeMillis();
          
    if (ttl > 0) {
        
            redisTemplate.opsForValue().
          set(
            "blacklist:" + token, "1", ttl, 
            TimeUnit.MILLISECONDS
          
        );
    }
}

// 验证 token 时，先查黑名单
public boolean isTokenValid(String token){
    if (
            redisTemplate.hasKey(
          "blacklist:" + token)) {
        returnfalse;
    }
    return 
            jwtUtil.verify(token);
          
}
```

Redis 只存"已失效"的 token，平时没什么写入，查询也快。还有更彻底的方案：直接把 token 存 Redis，每次验证都去 Redis 查。 这和传统 Session 没太大区别，只是借了 JWT 格式当 Session ID 用。

黑名单 vs 白名单：两种方案的本质区别

| 方案 | 存什么 | 查几次 Redis | 能否主动吊销 | 是否无状态 |
| --- | --- | --- | --- | --- |
| 纯 JWT | 不存 | 0 次 | 不能 | 是 |
| JWT+黑名单 | 存失效的 token | 1 次 | 能 | 不完全是 |
| token 存 Redis（白名单） | 存所有 token | 1 次 | 能 | 否 |

黑名单 相对轻量，正常请求不写 Redis，只有踢人时才写，多数业务选这个。白名单 控制力更强，能做限制同时在线设备数、实时查看在线状态，代价是每次请求都依赖 Redis。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

双 Token 续期方案

Token 到期了，用户正在操作怎么办？

- AccessToken ：有效期短（30 分钟），做实际鉴权
- RefreshToken ：有效期长（7 天），只用来换 AccessToken

AccessToken 过期，前端用 RefreshToken 换新的，对用户无感。RefreshToken 存 Redis，用户改密码就删掉，自动让他下次操作时重新登录。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

05

Redis 本身可靠吗

有人担心引入单点故障。Redis 的高可用方案跑了十几年：

- Sentinel（哨兵模式） ：主节点挂了自动选新主
- Cluster（集群模式） ：数据分片，横向扩展
![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/c680a620ea671b7d52384d341b9ba628_MD5.jpg)

Redis Cluster架构：数据分片分布在多个节点，支持横向扩展和自动故障转移

性能方面 Redis 单次查询 1ms 以内，单机 QPS 十几万。说"不能放 Redis 因为会单点故障"——这逻辑说不通。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

06

面试官到底在嘲笑什么

两种情况。

第一种 ：你用了 JWT 但验证时完全不走签名，每次都去 Redis 查 token 是否存在。这等于只借了 JWT 格式，没用它的能力——不如直接生成随机字符串当 Session ID，还省了编解码开销。面试官嘲笑的是这里。

第二种 ：你确实有业务需求需要主动吊销，选了 JWT+Redis 方案。但面试里只说了"放 Redis"，没说为什么。面试官误以为你不懂无状态设计。

第一种要改方案，第二种要改表达。

![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

07

纯 JWT 什么时候真的合适

- 跨服务调用 ：网关层做一次验签，用户信息往下游传。订单服务、支付服务直接从 JWT 取 userId，不用再查 Redis。这里 JWT 承担的是身份传递角色，不是管理登录会话。
- 一次性凭证 ：邮箱验证链接、密码重置链接、临时分享链接。签一次用一次，不需要续期和吊销。
- 安全要求不高的内部工具 ：用户量少，不需要踢人下线。纯 JWT 省一层依赖。
![图片](assets/%E9%9D%A2%E8%AF%95%E4%B8%AD%E8%A2%AB%E5%98%B2%E7%AC%91Token%E6%94%BE%E5%9C%A8Redis%E9%87%8C%EF%BC%9F%E8%BF%99%E6%8A%8A%E7%BB%99%E6%88%91%E5%B9%B2%E6%B2%89%E9%BB%98%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

08

面试怎么答

别上来就说"放 Redis"，也别上来就说"JWT 无状态"。

先说业务需求：需不需要主动踢人？改密码后需不需要其他设备立刻失效？需不需要限制同时在线设备数？

然后根据需求说方案：需要的话选 JWT+Redis 黑名单，说清楚纯 JWT 做不了主动吊销；不需要的话纯 JWT 够了，说清楚签名验证流程和密钥管理。

面试官真正想听的不是你选了哪个，是你知不知道每个方案的边界。 "Token 放 Redis"这件事本身没问题，问题是说不出来为什么放。