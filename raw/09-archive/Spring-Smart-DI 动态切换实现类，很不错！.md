---
title: "Spring-Smart-DI 动态切换实现类，很不错！"
source: "https://mp.weixin.qq.com/s/e4_DPp5GTUPvpikvtL0Hnw"
---
小哈学Java *2026年9月1日 15:15*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/Spring-Smart-DI%20%E5%8A%A8%E6%80%81%E5%88%87%E6%8D%A2%E5%AE%9E%E7%8E%B0%E7%B1%BB%EF%BC%8C%E5%BE%88%E4%B8%8D%E9%94%99%EF%BC%81/ca60f581a07794dd8a2c1b63e8cf377e_MD5.webp)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- [1.spring-smart-di](http://1.spring-smart-di/) 简介
- 2、快速开始
- 2.1 引入依赖
	- 2.2 启用功能
	- 2.3 @EnvironmentProxySPI 注解的使用
	- 2.4 配置当前使用的服务商
	- 2.5 @AutowiredProxySPI 注入使用
	- 2.6 定义不同的配置点

---

在系统开发的实际场景中，我们常常会碰到这样一类需求：同一个功能需要对接多个服务提供商。这么做主要基于两个重要原因。其一，为了规避某个服务商的服务出现不可用的风险，以便在出现问题时能够迅速切换到其他服务商，确保系统的稳定性和业务的连续性；其二，不同服务商的收费标准存在差异，从成本控制的角度出发，需要根据实际情况进行灵活切换。

传统的快速切换逻辑实现方法是，先为每个服务商编写对应的实现类，然后在配置点（这个配置点可以是数据库，也可以是像 Nacos 这样的配置中心）配置当前正在使用的服务商。在每次执行相关业务逻辑时，都要从配置点获取当前使用的服务商信息，再去执行该服务商对应的业务逻辑。

以系统接入多个短信服务商为例，用户可以根据自身需求动态地在不同服务商之间进行切换。下面我们详细看看如果手动实现这个功能，具体步骤是怎样的。

第一步，在某个配置位置（例如 Nacos 或者数据库）配置当前使用的服务商对应的标识值。比如，我们设置 `             sms.impl            = "某腾短信"` 。

第二步，在代码中执行发短信操作时，手动获取 `              sms.impl            ` 对应的服务商实现类。以下是相应的伪代码示例：

```
void sendSmsTouser(Req req) {
    // 1、获取当前使用的服务商
    String name = get("
            sms.impl"
          );
    // 2、获取对应的实现类
    SmsService smsService = 
            springContext.getBean(name);
          
    // 3、使用 smsService 执行具体业务逻辑
    
            smsService.sendMsg(req);
          
}
```

不过，这种实现方式存在明显的弊端，它比较繁琐，每次执行都需要手动去获取配置并加载对应的实现类。那么，有没有一种更优雅的方式，让 Spring 的 `@Autowired` 注解在注入时能够自动根据配置点的配置去注入对应的实现类，并且当配置发生变化时，注入的实现类也能自动更新呢？ `spring-smart-di` 的 `AutowiredProxySPI` 就是为解决这个问题而精心设计的。

## 1\. spring-smart-di 简介

`spring-smart-di` 是对 Spring `@Autowired` 注解的一次创新性扩展，它为用户提供了自定义 `Autowired` 注入逻辑的能力。目前，它实现了两个非常重要的注解： `@SmartAutowired` 和 `@AutowiredProxySPI` 。在本文中，我们将重点聚焦于如何使用 `AutowiredProxySPI` 来实现动态切换服务提供商的功能。

假设我们的系统对接了多个短信服务商，下面我们通过一个快速上手的案例，详细了解如何使用 `AutowiredProxySPI` 来实现动态切换。

## 2、快速开始

### 2.1 引入依赖

首先，我们需要在项目中引入 `spring-smart-di` 的依赖。在 Maven 项目的 `              pom.xml            ` 文件中添加以下依赖代码：

```
<dependency>
    
            io.github.burukeyou
          
    <artifactId>spring-smart-di-all</artifactId>
    <version>0.2.0</version>
</dependency>
```

### 2.2 启用功能

在 Spring 配置类上标记 `@EnableSmartDI` 注解，以此来启用 `spring-smart-di` 的强大功能。

### 2.3 @EnvironmentProxySPI 注解的使用

`@EnvironmentProxySPI` 注解代表着一个配置点，其主要作用是配置如何获取具体实现类的逻辑。

假设我们的系统中有两个短信服务商，需要实现动态切换。我们需要在接口上配置 `@EnvironmentProxySPI` 注解，表示从环境变量配置点中获取当前使用的服务商。这里我们将配置信息存储在属性 `${             sms.impl}           ` 中。

```
@EnvironmentProxySPI("${
            sms.impl}
          ")
publicinterface SmsService {
}

// 给实现类定义别名
@BeanAliasName("某腾短信服务")
@Component
publicclass ASmsService implements SmsService {
}

@BeanAliasName("某移短信服务")
@Component
publicclass BSmsService implements SmsService {
}
```

### 2.4 配置当前使用的服务商

我们可以在配置文件中配置当前使用的服务商。配置的值可以是 `@BeanAliasName` 注解指定的值，也可以是 `@Component` 注解指定的值，还可以是具体的全路径类名。

```
sms:
  impl: 某移短信服务
```

### 2.5 @AutowiredProxySPI 注入使用

接下来，我们只需要像使用 `@Autowired` 注解一样使用 `@AutowiredProxySPI` 注解即可。

```
// 依赖注入
@AutowiredProxySPI
private SmsService smsService;
```

通过以上步骤，我们就成功完成了动态切换服务提供商的需求。只要我们改变配置属性 `${             sms.impl}           ` 的值，系统就会实时生效，而无需重启服务。这是因为 `@AutowiredProxySPI` 注入的是一个代理对象，每次执行时会先实时获取当前使用的实现类，然后再执行调用操作。并且，在使用上与直接使用 `@Autowired` 注解基本没有区别。

### 2.6 定义不同的配置点

`@EnvironmentProxySPI` 注解主要用于配置环境变量相关的配置点。如果我们想要自定义配置，例如从数据库中获取配置信息，可以实现自己的 `ProxySPI` 注解。

下面是一个自定义 `DBProxySPI` 注解的示例，我们需要标记上 `@ProxySPI` 注解，并指定具体的配置获取逻辑实现类 `AnnotationProxyFactory` 。

```
@Inherited
@Target({
            ElementType.FIELD,
           
            ElementType.METHOD,
           
            ElementType.TYPE})
          
@Retention(
            RetentionPolicy.RUNTIME)
          
@ProxySPI(
            DbProxyFactory.class)
           // 指定配置获取逻辑
public @interface DBProxySPI {
    String value();
}

@Component
publicclass DbProxyFactory implements AnnotationProxyFactory<DBProxySPI> {
    @Autowired
    private SysConfigMapper sysConfigDao;

    @Override
    public Object getProxy(Class<?> targetClass, DBProxySPI spi) {
        // 根据注解从数据库获取要注入的实现类
        String configName = 
            sysConfigDao.getConfig(spi.value());
          
        return 
            springContext.getBean(configName);
          
    }
}

@DBProxySPI("${
            sms.impl}
          ")
publicinterface SmsService {
}
```

通过以上的步骤，我们就可以灵活地实现动态切换服务提供商的功能，并且可以根据不同的需求自定义配置获取逻辑。 `spring-smart-di` 为我们提供了一种简洁、高效的方式来处理这种动态切换的场景，让我们的代码更加灵活和易于维护。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/Spring-Smart-DI%20%E5%8A%A8%E6%80%81%E5%88%87%E6%8D%A2%E5%AE%9E%E7%8E%B0%E7%B1%BB%EF%BC%8C%E5%BE%88%E4%B8%8D%E9%94%99%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~3. 每天骑的共享单车是什么通信原理，有人了解过吗？4. 技术总监：公司不在乎你干了多少活！
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文