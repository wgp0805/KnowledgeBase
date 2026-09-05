---
title: "面试官：为什么需要 Gateway 网关，它有什么作用？"
source: "https://mp.weixin.qq.com/s/CLiCqtV2f_AhxqLw2O2yFg"
---
Java学习者社区 *2026年7月7日 14:02*

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20Gateway%20%E7%BD%91%E5%85%B3%EF%BC%8C%E5%AE%83%E6%9C%89%E4%BB%80%E4%B9%88%E4%BD%9C%E7%94%A8%EF%BC%9F/213d1e9cc6a0947af74816e9121186bf_MD5.webp)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **架构设计思维** ：面试官不仅仅是想知道你能不能搭一个 Gateway，更是想知道你是否理解网关在微服务架构中的定位——它是整个系统的 "统一大门"，是所有外部请求的必经之路。
2. **功能掌握深度** ：考察你是否清楚网关不仅仅是个 "路由转发器"，还承担着鉴权、限流、熔断、日志等职责，能否结合实际场景说明。
3. **技术选型能力** ：能否说出 Spring Cloud Gateway 与 Zuul 的本质区别，以及为什么 Gateway 能成为主流选择。

## 核心答案

![img](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20Gateway%20%E7%BD%91%E5%85%B3%EF%BC%8C%E5%AE%83%E6%9C%89%E4%BB%80%E4%B9%88%E4%BD%9C%E7%94%A8%EF%BC%9F/6e5b011727be52c3cee1664620b35ced_MD5.webp)

img

**没有网关的微服务架构，就像一栋大楼没有大门和前台** ——每个来访者都可以直接敲任何一扇门，混乱且危险。

网关的核心作用就是为微服务系统提供一个 **统一的入口** ，将所有非业务逻辑的公共功能集中到一处处理，让各个微服务专注于业务本身。

### 网关的五大核心作用

| 作用 | 说明 | 对应技术 |
| --- | --- | --- |
| **路由转发** | 根据请求路径将请求转发到对应的微服务 | `Predicate`  \+ `Route` |
| **身份认证** | 统一校验 Token、权限，不用每个服务都鉴权一遍 | `GlobalFilter` |
| **限流熔断** | 保护后端服务不被突发流量压垮 | Sentinel / `RequestRateLimiter` |
| **日志监控** | 统一记录请求日志、响应时间、状态码 | `GlobalFilter` |
| **协议转换** | 外部 HTTP → 内部 RPC，或反向 | 自定义 `Filter` |

**一句话总结** ：网关就是微服务的 "门面 + 保安 + 流量调度员"。

## 深度解析

### 一、为什么没有网关不行？

![img](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20Gateway%20%E7%BD%91%E5%85%B3%EF%BC%8C%E5%AE%83%E6%9C%89%E4%BB%80%E4%B9%88%E4%BD%9C%E7%94%A8%EF%BC%9F/7dbb9ff877f5d0ea915fd5ad3949bad1_MD5.jpg)

img

上图对比了有无网关的架构差异。关键区别：

- **没有网关** ：客户端直连各个微服务，每个服务都要自己处理鉴权、跨域、限流等公共逻辑，导致大量重复代码，且服务地址暴露在外
- **有网关** ：所有请求先经过网关，由网关统一处理公共逻辑，再路由到对应服务。各个微服务只需关注业务，服务地址也对外隐藏

关键点在于，网关本质上是将横切关注点（鉴权、限流、日志等）从各个微服务中 **剥离** 出来，集中到一处管理。

### 二、Spring Cloud Gateway 核心概念

Gateway 的编程模型围绕三个核心概念构建：

![img](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20Gateway%20%E7%BD%91%E5%85%B3%EF%BC%8C%E5%AE%83%E6%9C%89%E4%BB%80%E4%B9%88%E4%BD%9C%E7%94%A8%EF%BC%9F/48f22c246395140760df938da33c2b98_MD5.jpg)

img

上图展示了 Gateway 处理请求的完整流程：

- **Route（路由）** ：一个路由规则包含一个 ID、一个目标 URI、一组断言和一组过滤器。可以理解为 "一条转发规则"
- **Filter（过滤器）** ：分为 Pre（前置）和 Post（后置）两种，在请求转发前和响应返回后执行自定义逻辑，比如鉴权、加请求头、记录日志等

完整链路：请求进来 → 遍历所有 Route → 找到 Predicate 匹配的路由 → 执行 Pre Filter → 转发请求到目标服务 → 执行 Post Filter → 返回响应。

### 三、路由配置实战

```
# 
            application.yml
           — Gateway 路由配置
spring:
cloud:
gateway:
routes:
# 订单服务路由
-id:order-service
uri:lb://order-service# lb:// 表示从 Nacos 获取服务实例
predicates:
-Path=/api/order/**# 匹配路径
-Method=GET,POST# 匹配请求方法
filters:
-StripPrefix=1# 去掉路径第一段（/api）
-AddRequestHeader=X-Source,gateway# 添加请求头

# 用户服务路由
-id:user-service
uri:lb://user-service
predicates:
-Path=/api/user/**
filters:
-StripPrefix=1
```

配置说明：

- `id` ：路由唯一标识，自定义名称
- `uri` ： `lb://` 前缀表示启用负载均衡，后面的 `order-service` 是注册中心的服务名
- `predicates` ：匹配条件，只有 `Path` 和 `Method` 都满足才走这条路由
- `filters` ： `StripPrefix=1` 会把 `/api/order/xxx` 变成 `/order/xxx` ，去掉路径第一段

### 四、自定义全局鉴权过滤器

这是面试常考的代码题——如何在 Gateway 中实现统一鉴权：

```
@Component
publicclass AuthGlobalFilter implements GlobalFilter, Ordered {

@Override
public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
// 1. 从请求头中获取 Token
        String token = 
            exchange.getRequest().getHeaders().getFirst(
          "Authorization");

// 2. Token 为空，返回 401 未授权
if (
            StringUtils.isBlank(token))
           {
            
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
          
return 
            exchange.getResponse().setComplete();
          
        }

// 3. 校验 Token（实际项目中调用 JWT 工具类或认证服务）
try {
            Claims claims = 
            JwtUtil.parseToken(token);
          
// 将用户信息放入请求头，传递给下游服务
            ServerHttpRequest request = 
            exchange.getRequest().mutate()
          
                    .header("X-User-Id", 
            claims.getSubject())
          
                    .build();
return 
            chain.filter(exchange.mutate().request(request).build());
          
        } catch (Exception e) {
// Token 无效或过期
            
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
          
return 
            exchange.getResponse().setComplete();
          
        }
    }

@Override
public int getOrder() {
return0;  // 数字越小优先级越高
    }
}
```

核心要点：

- 实现 `GlobalFilter` 接口，所有路由都会经过这个过滤器
- 实现 `Ordered` 接口控制过滤器执行顺序，数字越小优先级越高

### 五、Gateway vs Zuul 对比

| 对比维度 | Zuul [1.x](http://1.x/) | Spring Cloud Gateway |
| --- | --- | --- |
| 编程模型 | 同步阻塞（Servlet） | 异步非阻塞（WebFlux + Netty） |
| 性能 | 一般，线程池模型 | 高性能，少量线程处理大量并发 |
| filter 种类 | pre / route / post / error | pre / post（更简洁） |
| 编程模型 | 基于 `ZuulFilter` | 基于 `GlobalFilter` + `GatewayFilter` |
| 限流支持 | 需额外集成 | 内置 `RequestRateLimiter` |
| Spring 官方支持 | ❌ 已弃用 | ✅ 官方推荐 |
| 社区活跃度 | 低 | 高 |

**核心区别一句话** ：Gateway 基于响应式编程（Reactor + Netty），异步非阻塞，性能远超 Zuul [1.x](http://1.x/) 的同步阻塞模型。Zuul 已不在 Spring Cloud 官方路线图内。

## 面试高频追问

1. Gateway 的过滤器有哪几种？
- `GlobalFilter` ：全局过滤器，所有路由生效，适合鉴权、日志等公共逻辑
	- `GatewayFilter` ：路由级别过滤器，只对配置了该过滤器的路由生效，适合特定业务处理
3. Gateway 如何实现限流？
- 内置 `RequestRateLimiter` 过滤器，基于 Redis 令牌桶算法；生产环境通常配合 Sentinel 使用，支持更丰富的限流策略
5. Gateway 会不会成为性能瓶颈？
- 理论上会，因为是所有请求的入口。但 Gateway 基于 Netty 异步非阻塞，单机吞吐量非常高；生产环境通过多实例部署 + Nginx 负载均衡来解决
7. Gateway 和 Nginx 有什么区别？
- Nginx 是通用反向代理，性能极高但功能偏底层；Gateway 是微服务网关，内置了服务发现、动态路由等微服务能力。生产环境通常 Nginx（外层）+ Gateway（内层）配合使用

## 常见面试变体

- "Spring Cloud Gateway 的核心组件有哪些？"
- "Gateway 和 Zuul 的区别是什么？"
- "如何在 Gateway 中实现统一鉴权？"
- "Gateway 的路由是怎么配置的？Predicate 和 Filter 的作用？"

## 记忆口诀

**网关五作用** ： **路由、鉴权、限流、日志、协议转换**

**Gateway 三核心** ： **Route（路由规则）、Predicate（匹配条件）、Filter（过滤器）**

> “
> 
> "路鉴限日协，路断过三关" —— 路由、鉴权、限流、日志、协议转换；Route 断言 Filter 三道关卡。

## 总结

网关是微服务架构的统一入口，核心作用包括路由转发、身份认证、限流熔断、日志监控和协议转换。Spring Cloud Gateway 基于 WebFlux + Netty 异步非阻塞模型，性能远超 Zuul，是当前主流选择。掌握 Route、Predicate、Filter 三大核心概念，以及自定义 `GlobalFilter` 实现鉴权，是面试的必考内容。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%20Gateway%20%E7%BD%91%E5%85%B3%EF%BC%8C%E5%AE%83%E6%9C%89%E4%BB%80%E4%B9%88%E4%BD%9C%E7%94%A8%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 如何搭建漂亮的 SpringBoot 脚手架？3. 我们放弃了Nacos作为配置中心，转而选择了这款神器~
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文