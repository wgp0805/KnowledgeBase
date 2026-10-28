---
title: "如何做到无感刷新Token?"
source: "https://mp.weixin.qq.com/s/yOMmaWTsYYQIJwBx2AV2gg"
author:
published:
created: 2026-10-28
description:
tags:
  - "clippings"
---
小哈学Java *2026年10月28日 11:40*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E5%A6%82%E4%BD%95%E5%81%9A%E5%88%B0%E6%97%A0%E6%84%9F%E5%88%B7%E6%96%B0Token/409416a17d8f4ddcc52ba67d378da2db_MD5.webp)

来源： [juejin.cn/post/7316797749517631515](http://juejin.cn/post/7316797749517631515)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 为什么需要无感刷新 Token？
- 自动刷新 token
- 前端 token 续约
- 疑问及思考

---

![图片](assets/%E5%A6%82%E4%BD%95%E5%81%9A%E5%88%B0%E6%97%A0%E6%84%9F%E5%88%B7%E6%96%B0Token/e19627362eca5e9f730644d33c99e2a0_MD5.webp)

## 为什么需要无感刷新 Token？

- **「最近浏览到一个文章里面的提问，是这样的：」**
	当我在系统页面上做业务操作的时候会出现突然闪退的情况，然后跳转到登录页面需要重新登录系统，系统使用了 Redis 做缓存来存储用户 ID，和用户的 token 信息，这是什么问题呢？
- **「解答：」**
	突然闪退，一般都是由于你的 token 过期的问题，导致身份失效。
- **「解决方案：」**
	自动刷新 token
	token 续约
- **「思路」**
	如果 Token 即将过期，你在验证用户权限的同时，为用户生成一个新的 Token 并返回给客户端，客户端需要更新本地存储的 Token，
	还可以做定时任务来刷新 Token，可以不生成新的 Token，在快过期的时候，直接给 Token 增加时间

## 自动刷新 token

自动刷新 token 是属于后端的解决方案，由后端来检查一个 Token 的过期时间是否快要过期了，如果快要过期了，就往请求头中重新

放一个 token，然后前端那边做拦截，拿到请求头里面的新的 token，如果这个新的 token 和老的 token 不一致，直接将本地的 token 更换

接下来拿代码举例子

- 先引入依赖
```
<dependency>
    <groupId>
            cn.hutool
          </groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.5.1</version>
</dependency>
<dependency>
    <groupId>
            com.alibaba
          </groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.33</version>
</dependency>
<dependency>
    <groupId>
            io.jsonwebtoken
          </groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```
- 这是一个生成 token 的例子
```
import 
            io.jsonwebtoken.Claims;
          
import 
            io.jsonwebtoken.JwtBuilder;
          
import 
            io.jsonwebtoken.Jwts;
          
import 
            io.jsonwebtoken.SignatureAlgorithm;
          

import 
            javax.crypto.SecretKey;
          
import 
            javax.crypto.spec.SecretKeySpec;
          
import 
            java.util.Base64;
          
import 
            java.util.Date;
          
import 
            java.util.UUID;
          

public class JwtUtil {
    // 有效期为
    public static final Long JWT_TTL = 60 * 60 * 1000 * 24;// 60 * 60 * 1000 * 24  一个小时
    // 设置秘钥明文 --- 自己改就行
    public static final String JWT_KEY = "qx";
    // 用于生成uuid，用来标识唯一
    public static String getUUID(){
        String uuid = 
            UUID.randomUUID().replaceAll(
          "-", "");//token用UUID来代替
        return uuid;
    }

    /**
        id      : 标识唯一
        subject : 我们想要加密存储的数据
        ttl     : 我们想要设置的过期时间
     */

    // 生成token  jwt加密 subject token中要存放的数据（json格式）
    public static String createJWT(String subject) {
        JwtBuilder builder = getJwtBuilder(subject, null, getUUID());// 设置过期时间
        return 
            builder.compact();
          
    }

    // 生成token  jwt加密
    public static String createJWT(String subject, Long ttlMillis) {
        JwtBuilder builder = getJwtBuilder(subject, ttlMillis, getUUID());// 设置过期时间
        return 
            builder.compact();
          
    }

    // 创建token jwt加密
    public static String createJWT(String id, String subject, Long ttlMillis) {
        JwtBuilder builder = getJwtBuilder(subject, ttlMillis, id);// 设置过期时间
        return 
            builder.compact();
          
    }

    private static JwtBuilder getJwtBuilder(String subject, Long ttlMillis, String uuid) {
        SignatureAlgorithm signatureAlgorithm = 
            SignatureAlgorithm.HS256;
          
        SecretKey secretKey = generalKey();
        long nowMillis = 
            System.currentTimeMillis();
          
        Date now = new Date(nowMillis);
        if(ttlMillis==null){
            ttlMillis=
            JwtUtil.JWT_TTL;
          
        }
        long expMillis = nowMillis + ttlMillis;
        Date expDate = new Date(expMillis);
        return 
            Jwts.builder()
          
                .setId(uuid)              //唯一的ID
                .setSubject(subject)   // 主题  可以是JSON数据
                .setIssuer("sg")     // 签发者
                .setIssuedAt(now)      // 签发时间
                .signWith(signatureAlgorithm, secretKey) //使用HS256对称加密算法签名, 第二个参数为秘钥
                .setExpiration(expDate);
    }

    // 生成加密后的秘钥 secretKey
    public static SecretKey generalKey() {
        byte[] encodedKey = 
            Base64.getDecoder().decode(JwtUtil.JWT_KEY);
          
        SecretKey key = new SecretKeySpec(encodedKey, 0, 
            encodedKey.length,
           "AES");
        return key;
    }

    // jwt解密
    public static Claims parseJWT(String jwt) throws Exception {
        SecretKey secretKey = generalKey();
        return 
            Jwts.parser()
          
                .setSigningKey(secretKey)
                .parseClaimsJws(jwt)
                .getBody();
    }
}
```
- 写个单元测试，测试一下
```
@Test
void test() throws Exception {
    String token = 
            JwtUtil.createJWT(
          "1735209949551763457");
    
            System.out.println(
          "Token: " + token);
    Date tokenExpirationDate = getTokenExpirationDate(token);
    
            System.out.println(tokenExpirationDate);
          
    
            System.out.println(tokenExpirationDate.toString());
          
    long exp = 
            tokenExpirationDate.getTime();
          
    long cur = 
            System.currentTimeMillis();
          
    
            System.out.println(exp);
          
    
            System.out.println(cur);
          
    
            System.out.println(exp
           - cur);
}
// 解析令牌并获取过期时间
public static Date getTokenExpirationDate(String token) {
    try {
        SecretKey secretKey = generalKey();
        Claims claims = 
            Jwts.parser()
          
                .setSigningKey(secretKey)
                .parseClaimsJws(token)
                .getBody();
        return 
            claims.getExpiration();
          
    } catch (ExpiredJwtException | SignatureException e) {
        throw new RuntimeException("Invalid token", e);
    }
}
```

Token 有点长，就不放全部了

![单元测试输出](assets/%E5%A6%82%E4%BD%95%E5%81%9A%E5%88%B0%E6%97%A0%E6%84%9F%E5%88%B7%E6%96%B0Token/b7c71f3895fe2d29c8e678b766c7f572_MD5.jpg)

单元测试输出

可以看到我们的 exp 过期时间的毫秒数为 1703651262000

可以看到我们的 cur 当前时间的毫秒数为 1703564863035

我们将两者相减得到的值为 86398965ms，我们可以算一下一天的毫秒数是多少 1000 \* 60 \* 60 \* 24 ms = 86400000ms

这样我们就能够拿到 token 的过期时间 tokenExpirationDate 了

我们就可以通过在校验 token 的时候，如果 token 校验通过了，此时我们拿到该 token 的过期时间，以 (过期时间 - 当前时间) 进行判断

如果说 (过期时间 - 当前时间) 小于约定的值，那么我们就重新根据 token 里面的信息，重新创建一个 token，将新的 token 放到请求头中

返回给前端，前端去进行本地存储更新 token

## 前端 token 续约

token 的续约偏向于前端的解决方案，即由前端来进行 token 的过期时间的判断，首先前后端需要对接商量好一个 token 续约的接口，

当前端发现这个 token 快要过期的时候，向后端发送该 token，然后后端将该 token 的过期时间延长。

**「前端采用的是双 Token 的方式，access-token 和 refresh-token 即 AT 和 RT」**

**「而对于纯后端的方式，就是只有 access-token 这一个 token」**

- **「那么问题来了 AT 和 RT 到底有什么区别？为什么需要 RT？」**
	**「在前端实现方案来说，RT 是用来在 AT 即将过期的时候，用 RT 获取最新的 token」**
	我解释一下我的观点：
	AT 的暴露机会更多，每个请求都要携带，所以设置的过期时间短一点， **「减少劫持风险」**
	RT 只会暴露在 auth 服务中用来刷新 at，设置的过期时间长一点， **「增加便利性。」**
	AT 和 RT 是为了网络传输安全，网络传输中，容易暴露 AT，因为 AT 时间短，暴露后风险系数才低
	**「这种是标准的安全处理，其实已经无需探讨他的合理性，就好像 https 之于 http 一样」**

## 疑问及思考

要是前端有一个表单页面，长时间不进行请求的发送，此时用户填写完表单了，再点击提交的时候，后端返回 401 了，怎么办？

也就是说，虽然你后端可以无感刷新 Token，但是你后端无感刷新 Token 的前提是：前端得发请求，如果用户长时间不进行页面的交互，

即没有进行任何业务逻辑的跳转什么的，就单纯的往表单上面填东西，什么请求也没发的情况下，后端是无法感知 Token 过期的

**「这种情况怎么解决？」**

- 对于纯后端的解决方案，我是这样想的
	让前端在表单填写内容的时候做处理，如果提交返回的是 401，那么前端就需要获取表单存在本地存储 然后跳转登录页，登录成功后
	返回这个页面，然后从本地存储取出来再回显到表单上面。
- 对于前端的解决方案，我是这样想的
	对于后端来说就是 AT 过期了，而对于前端来说就是 AT 和 RT 都过期了，怎么处理？
1. 需要监听 refresh token 的过期时间，在接近过期的时候向后端发起请求来刷新 refresh token 或者是定期刷新一下 refresh token
2. 和后端的解决方案一样，前端做一个类似草稿箱的功能对表单等元素进行保存

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI [2.x](http://2.x/) + Spring Boot [4.x](http://4.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E5%A6%82%E4%BD%95%E5%81%9A%E5%88%B0%E6%97%A0%E6%84%9F%E5%88%B7%E6%96%B0Token/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 为什么王者荣耀不使用微服务架构？3. 面试官：Kafka 如何保证消息不丢失？4. LatchUtils：简化 Java 异步任务同步的利器
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢啦
```

阅读原文