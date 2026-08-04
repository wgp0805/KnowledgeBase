---
title: "为什么越来越多人用Sa-Token？"
source: "https://mp.weixin.qq.com/s/NAsaVb5iOuTCmK4FVIm8IQ"
---
苏三 苏三说技术 *2026年8月4日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

> 从Spring Security到Sa-Token，Java权限认证的一次效率革命

前阵子帮一个团队做技术评审，发现了一个非常典型的现象。

他们的新项目在技术选型的时候，团队内部吵得不可开交——架构师坚持要用Spring Security，说这是“企业级标准”；

资深开发说Spring Security太复杂了，用Shiro就够了；

而团队里几个年轻的同事则力荐Sa-Token这个后起之秀。

最后怎么定的？

他们用Sa-Token三天就把权限系统跑通了，比预期快了整整一周。

这个案例不是个例。

Sa-Token在中文社区迅速崛起，GitHub上已经积累了 **超过46K Stars** 。

越来越多的Java项目开始从Spring Security、Shiro迁移到Sa-Token。

**2026年3月，Sa-Token [v1.45.0正式发布，全面适配Spring](http://v1.45.xn--0,spring-9f6m42rku6a3zch61dff4h4bezv4a/) Boot 4** ，并新增了Jackson3插件等能力。

今天这篇文章，我就把Sa-Token为什么这么火的原因，从底层架构到实战用法，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、为什么我们需要权限框架？

在聊Sa-Token之前，我们先理解一个根本问题—— **为什么不能自己手写权限控制，非要用框架？**

想象一下，你要为一个电商系统实现权限控制，手写代码大概长这样：

```
public void updateProduct(Long productId, ProductDTO dto) {
    // 1. 检查用户是否登录
    User user = getCurrentUser();
    if (user == null) {
        throw new UnauthorizedException("请先登录");
    }
    // 2. 检查用户是否有编辑权限
    if (!
            user.hasPermission(
          "product:update")) {
        throw new ForbiddenException("没有操作权限");
    }
    // 3. 检查是否是自己的商品
    Product product = 
            productService.getById(productId);
          
    if (!
            product.getOwnerId().equals(user.getId()))
           {
        throw new ForbiddenException("只能修改自己的商品");
    }
    // 4. 实际业务逻辑
    
            productService.update(productId,
           dto);
}
```

**看到问题了吗？**

- 每个方法都要重复写登录检查
- 每个方法都要重复写权限校验
- 每个方法都要自己管理Session/Token
- 密码加密、CSRF防护要自己实现
- 审计日志、安全事件处理要自己写

安全逻辑像“幽灵代码”一样渗透到业务代码的每个角落。

**权限框架的价值，就是把这些问题抽象化、标准化、自动化** 。

而Sa-Token，就是把这些事情做到极致的那一个。

## 二、一张图看懂Sa-Token的整体架构

在深入代码之前，我们先建立一个整体认知。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Sa-Token%EF%BC%9F/6f10b0a2e917285f8d251fffbc99443b_MD5.jpg)

Sa-Token采用 **分层架构设计** ，将核心功能划分为 **认证层、权限层、存储层和扩展层** 四个层次，各层之间通过接口解耦。

这种分层架构的核心价值在于： **每一层都可以被替换** 。

你不想用内存存储？

换成Redis。

不想用默认的Token生成策略？

自己实现一个。

框架把控制权彻底交给了开发者。

## 三、核心-插件-适配器模型

Sa-Token最精妙的设计，是它基于 **核心-插件-适配器（Core-Plugin-Adapter）模型** 构建的整个框架。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Sa-Token%EF%BC%9F/561b58a335246b580145a94d386d6691_MD5.jpg)

**核心层（sa-token-core）** 是整个框架的心脏， **零外部依赖** ，只包含最纯粹的认证逻辑、Session模型和SPI接口定义。这意味着它可以在任何Java环境中运行，不绑定任何Web框架。

**插件层（sa-token-plugin）** 提供了所有可插拔的功能扩展——Redis存储、JWT、SSO、 [OAuth2.0等。你只需要引入你需要的插件，不需要的绝不拖进来。](http://oauth2.xn--0-hl5c.xn--,-ro6aa34gepa237aovggp4a0sicxc42pvq3cea9613a8t9adaf2102ay33aeag./)

**适配层（sa-token-starter）** 负责将核心逻辑桥接到具体的Web框架——Spring Boot、Spring WebFlux、Solon、JFinal等。

### 3.1 SaManager：全局组件注册中心

SaManager是整个框架的 **中央注册表** ，持有所有全局组件的静态引用。

无论是存储层、策略层还是上下文处理器，都通过SaManager进行统一管理。

### 3.2 SaStrategy：策略模式的核心

SaStrategy是一个单例，允许开发者 **在不修改核心代码的情况下，覆盖内部算法** 。

比如：

| 策略函数 | 默认行为 | 你可以替换成 |
| --- | --- | --- |
| `createToken` | 生成UUID随机字符串 | 自定义Token格式 |
| `createSession` | 返回SaSession实例 | 自定义Session实现 |
| `routeMatcher` | 由Starter实现 | 自定义路由匹配规则 |
| `createStpLogic` | 返回默认StpLogic | 多账号体系隔离 |

这种设计让框架的 **每一个核心行为都可以被替换** ，同时保持了核心代码的纯净和稳定。

## 四、登录认证的完整链路

这是Sa-Token最核心的功能。我们逐层拆解，看看 `              StpUtil.login(10001)            ` 这一行代码背后到底发生了什么。

### 4.1 登录流程全景图

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Sa-Token%EF%BC%9F/2f5b5d9f36f41270a5addac77578470e_MD5.jpg)

### 4.2 登录前的安全校验

进入 `              StpLogic.login()            ` 方法后，首先执行的是 **账号封禁检查** ：

```
// 封禁key的拼接规则：satoken:login:disable:loginType:loginId
String disableKey = splicingKeyLoginDisable(loginId);
if (
            SaManager.getSaTokenDao().get(disableKey)
           != null) {
    throw new DisableLoginException("账号已被封禁");
}
```

这意味着，如果一个账号被管理员封禁了，任何登录尝试都会被 **在框架层面直接拦截** ，业务代码完全不需要关心。

### 4.3 Token的生成与存储

通过安全校验后，框架开始生成Token：

```
// 简化版Token生成
public static String generateAccessToken(long loginId) {
    // 1. 生成随机字符串作为token主体
    String token = 
            IdUtil.simpleUUID();
          
    // 2. 构建token信息对象
    SaTokenInfo tokenInfo = new SaTokenInfo()
        .setLoginId(loginId)
        .setToken(token)
        .setCreateTime(
            System.currentTimeMillis())
          
        .setExpireTime(
            System.currentTimeMillis()
           + 
            StpLogic.getTokenTimeout());
          
    // 3. 存储token信息
    
            SaTokenDaoFactory.getDao().setTokenInfo(token,
           tokenInfo);
    return token;
}
```

这里有一个关键设计： **Token的存储是可插拔的** 。

默认存在内存里，但你可以轻松切换到Redis，实现分布式会话共享。

### 4.4 写入当前上下文

生成Token后，框架需要把Token注入到当前请求的上下文中：

```
public void setTokenValue(String tokenValue, int cookieTimeout) {
    SaTokenConfig config = getConfig();
    SaStorage storage = 
            SaHolder.getStorage();
          
    String tokenPrefix = 
            config.getTokenPrefix();
          
    if (
            SaFoxUtil.isEmpty(tokenPrefix))
           {
        
            storage.set(splicingKeyJustCreatedSave(),
           tokenValue);
    } else {
        
            storage.set(splicingKeyJustCreatedSave(),
           tokenPrefix + " " + tokenValue);
    }
    // 注入Cookie（自动）
    
            SaHolder.getResponse().addCookie(...);
          
}
```

**你完全不需要手动操作Cookie或Header** 。

Sa-Token利用Cookie自动注入的特性，让前端感应不到Token的存在，却能在下次请求时自动带上凭证。

### 4.5 多账号体系的隔离

在实际项目中，一个系统往往需要 **多套独立的认证体系** ——普通用户、管理员、API调用方等。

RuoYi-Vue-Plus通过自定义 `StpLogic` 子类实现了这种隔离：

```
public class StpAdminUtil {
    // 管理员专属的StpLogic实例
    public static final StpLogic stpLogic = new StpLogic("admin") {
        @Override
        public String splicingKeyTokenValue(String tokenValue) {
            return "admin:" + tokenValue;  // Key前缀隔离
        }
    };
}
```

这种设计使得 **同一个系统可以同时存在多个互不干扰的认证域** ，每个域有独立的Token命名空间和会话管理。

## 五、分布式会话

> 有些小伙伴在工作中可能会遇到这个问题：单机跑得好好的，一上集群就出事了——登录态丢失、频繁掉线、会话不一致。

Sa-Token默认把会话数据存放在 **JVM内存** 中。

单机开发时，读写速度飞快，没有任何序列化/反序列化损耗。

但一旦应用重启，所有会话数据全部丢失。

在集群部署环境中，每个节点都有自己的内存，用户的登录请求落在节点A，下次请求落在节点B，节点B找不到会话，直接返回401。

### 5.1 分布式架构图

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Sa-Token%EF%BC%9F/3ea3177b2376f70a38619a009977fd74_MD5.jpg)

**解决方案：接入Redis** 。

```
<dependency>
    <groupId>
            cn.dev33
          </groupId>
    <artifactId>sa-token-redis</artifactId>
    <version>1.45.0</version>
</dependency>
```

配置完成后的效果：

- **登录态多节点共享** ：用户在任意节点登录，所有节点都能识别
- **水平扩展能力** ：增加节点不影响会话一致性
- **重启不丢数据** ：应用重启，Redis里的会话依然有效

## 六、Sa-Token vs Spring Security对比

| 对比维度 | Sa-Token | Spring Security |
| --- | --- | --- |
| **核心定位** | 轻量级权限认证框架 | 企业级全面的安全解决方案 |
| **学习曲线** | **极低**  —— `              StpUtil.login()            ` 即可上手 | **高**  ——需理解过滤器链和SecurityContextHolder |
| **架构模式** | Core-Plugin-Adapter | 过滤器链+SecurityContextHolder |
| **侵入性** | **低**  ——静态工具类，随处调用 | **高**  ——需继承/实现类 |
| **配置方式** | 零配置启动 | 大量配置类 |
| **功能边界** | 聚焦高频认证场景 | 瑞士军刀，功能全面 |
| **分布式会话** | 原生支持Redis扩展 | 需Spring Session等组件 |

Spring Security的强大源于其深度集成与高度可定制性，但这也带来了著名的“学习曲线陡峭”问题。

新手开发者常常会陷入“ **我只是想加个登录，为什么需要理解整个过滤器链和SecurityContextHolder** ”的困惑中。

相比之下，Sa-Token的设计哲学是 **“让安全变得简单”** 。

它的核心API设计得非常直观——登录、注销、权限检查，几乎一行代码搞定。

**一句话总结：Spring Security是“安全领域的瑞士军刀”，功能全面但复杂；Sa-Token是“安全领域的美工刀”，简单实用且灵活。**

## 七、优缺点

### 优点

**1\. 极低的学习成本** 你几乎不需要理解任何底层原理，只需引入依赖、添加几行配置，就能让一个登录接口跑起来。开发者不需要先啃完一本安全理论书才能写出第一行代码。

**2\. 一行代码搞定认证** 登录只需要 `              StpUtil.login(id)            ` ，校验登录只需要 `              StpUtil.checkLogin()            ` 。大多数功能都可以一行代码解决。

**3\. 五大核心模块，功能全面** 目前已集成：登录认证、权限认证、分布式Session会话、微服务网关鉴权、单点登录、 [OAuth2.0、踢人下线、Redis集成、前后台分离、记住我模式、模拟他人账号、临时身份切换、账号封禁、多账号认证体系、注解式鉴权、路由拦截式鉴权、花式token生成、自动续签、同端互斥登录、会话治理、密码加密、jwt集成、Spring集成、WebFlux集成。](http://oauth2.xn--0redistokenjwtspringwebflux-371zafaaaaaaaafaaaadg81846amubjyhk7bka14lb8cl3bg3esgv64l4ba85wy9ftnav85dumafb19k7ct244bp8ubba122bb68eqabb473cy26d8aqhit38rzx1akra724apx4crzfv55aea7417dca8242d4ndd65tn1vabrbe52ehh5ad94aezeg00bxumvk1b8l2bz8d2q4hdnrvt1pg7pbbcbv6cx8ex88ciaf144u6if24sgz3iha7884kucaij./)

**4\. 开源免费，持续迭代** 2026年3月发布的 [v1.45.0已适配Spring](http://v1.45.xn--0spring-6h0nq817auyc/) Boot 4，新增了重复登录处理策略和Jackson3插件。

**5\. 与Spring生态完美集成** 支持Spring Boot 2/3/4、WebFlux、Solon、JFinal等常见框架。

### 缺点

**1\. 生态不如Spring Security成熟** 作为后起之秀，第三方集成和社区积累不如Spring Security。

**2\. 功能边界相对聚焦** Sa-Token主要提供认证、授权和会话管理等功能。如果项目需要CSRF保护等更复杂的安全防护措施，Spring Security可能是更好的选择。

**3\. 部分高级功能需要额外配置** 虽然核心功能开箱即用，但JWT、SSO、OAuth2等高级功能需要引入独立插件。

## 八、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **Spring Boot新项目** | ✅✅✅ 强烈推荐 | 零配置启动，三天跑通权限系统 |
| **从Spring Security迁移** | ✅✅✅ 强烈推荐 | 代码量直接砍一大截，学习成本极低 |
| **需要快速交付的项目** | ✅✅✅ 强烈推荐 | 一行代码搞定登录认证 |
| **微服务架构** | ✅✅✅ 强烈推荐 | 网关统一鉴权+Redis分布式会话 |
| **多端登录策略复杂** | ✅✅✅ 强烈推荐 | 原生支持同端互斥登录、多端登录策略 |
| **团队对安全不熟悉** | ✅✅✅ 强烈推荐 | 上手即用，不需要理解复杂的过滤器链 |
| **高安全/复杂合规需求** | ⚠️ 需评估 | Spring Security功能更全面 |

## 九、写在最后

回到最初的问题： **为什么越来越多人用Sa-Token？**

答案其实很简单—— **因为它解决了权限认证这个高频场景下的核心矛盾：既要功能强大，又要简单易用。**

Spring Security虽然功能强大，但学习曲线陡峭，配置复杂。新手开发者常常陷入“我只是想加个登录，为什么需要理解整个过滤器链”的困惑中。

手写权限控制虽然灵活，但安全逻辑会像“幽灵代码”一样渗透到业务代码的每个角落。

**Sa-Token走了一条“第三条路”** ——基于 **核心-插件-适配器** 模型，既保持了核心的轻量和纯净，又通过插件机制提供了强大的扩展能力。

你只需要一行 `              StpUtil.login(id)            ` ，背后自动完成了Token生成、Session创建、Cookie注入等一系列工作。

路由拦截模式让你告别“每个接口都贴注解”的机械劳动。

分布式会话、踢人下线、多端登录策略——这些生产环境的刚需，全部原生支持。

从Spring Security到Sa-Token，不是“谁取代谁”，而是 **在合适的场景选择更合适的工具** 。

开源地址

- **GitHub** ： [https://github.com/dromara/Sa-Token](https://github.com/dromara/Sa-Token)
- **Gitee** ： [https://gitee.com/dromara/sa-token](https://gitee.com/dromara/sa-token)
- **官方文档** ： [https://sa-token.cc](https://sa-token.cc/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

苏三星球中的实战项目中Spring Security和Sa-Token都有使用，感兴趣的小伙伴，可以扫描下方👇🏻二维码，加入星球学习，嘎嘎香。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8Sa-Token%EF%BC%9F/db16b333e690c0b9bd98abca0793bc82_MD5.png)