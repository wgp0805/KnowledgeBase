---
title: "Spring Cloud Gateway 打 War 包部署外置 Tomcat 全攻略：原理、实现与踩坑实录 - 码猿手"
source: "博客园"
url: "https://www.cnblogs.com/huangrenhui/p/20841399"
date: "2026-06-26T07:34:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Spring Cloud Gateway 打 War 包部署外置 Tomcat 全攻略：原理、实现与踩坑实录 - 码猿手

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/huangrenhui/p/20841399  
> **抓取日期**: 2026-06-26  
> **相关性评分**: 0.6

> 这是一篇深度技术复盘，记录了一套让标准 Spring Cloud Gateway（WebFlux 版）以 War 包形式部署到外置 Tomcat 的完整改造方案，包含核心原理剖析、源码级实现和实际效果评估。

* * *

## 一、背景与动机

Spring Cloud Gateway（SCG）作为微服务网关的标配，官方设计上以 **jar 包 + 内嵌 Netty** 运行，**不支持 War 包外置 Servlet 容器部署** 。但在一些传统企业环境中，运维基础设施强依赖外置 Tomcat 统一托管多个 War 应用，这催生了"能否让 SCG 也能打成 War 包跑在 Tomcat 里"的需求。

本文完整记录了这条探索之路：从底层请求链路的分析，到核心改造方案，再到最终的效果评估。

* * *

## 二、请求处理全链路剖析

在动手改造前，先理清 SCG 在 Servlet 容器中的请求流转全过程。

### 2.1 请求流程调用链
    
    
    DefaultWebFilterChain#filter
      → DispatcherHandler#handle
        → RouterFunctionMapping#getHandlerInternal
        → RoutePredicateHandlerMapping#getHandlerInternal
          → RoutePredicateHandlerMapping#lookupRoute
            → this.routeLocator.getRoutes()
              → concatMap(route → Mono.just(route).filterWhen(r → {
                  exchange.getAttributes().put(GATEWAY_PREDICATE_ROUTE_ATTR, r.getId());
                  return r.getPredicate().apply(exchange);
                }))
      → CachingRouteLocator#getRoutes  【关键卡点：获取路由信息】
      → DispatcherHandler#invokeHandler
      → SimpleHandlerAdapter#handle
      → FilteringWebHandler#handle
        → DefaultGatewayFilterChain#filter
          → NettyRoutingFilter#filter
    

其中 **`CachingRouteLocator#getRoutes`** 是整个流程的命门——如果前面的 `getRoutes()` 没有正确 `onNext`，后续路由匹配将直接卡死，请求无法到达后端服务。

### 2.2 核心类职责一览

类 | 角色 | 职责  
---|---|---  
`SpringServletContainerInitializer` | 容器入口 | 扫描并执行所有 `WebApplicationInitializer`  
`AbstractReactiveWebInitializer` | 官方适配 | Spring-web 提供的 Reactive→Servlet 适配实现  
`WebHttpHandlerBuilder` | HttpHandler 构造 | 组装 `HttpHandler`（实现类为 `HttpWebHandlerAdapter`）  
`ServletHttpHandlerAdapter` | Servlet 实现 | 将 `ServletRequest`/`ServletResponse` 适配为 `ServerHttpRequest`/`ServerHttpResponse`  
`HttpWebHandlerAdapter` | HttpHandler | 网络层→应用层转换，封装 `ServerWebExchange`  
`DispatcherHandler` | WebHandler | 核心调度器，遍历所有 `HandlerMapping` 并执行匹配  
`HandlerMapping` | 路由匹配 | 包含 `RoutePredicateHandlerMapping`（Gateway 路由）和 `RouterFunctionMapping`  
  
### 2.3 请求处理流程简图
    
    
    ServletHttpHandlerAdapter（Servlet）
        ↓ 适配 Servlet 请求
    HttpWebHandlerAdapter（HttpHandler）
        ↓ 封装 ServerWebExchange
    DispatcherHandler（WebHandler）
        ↓ 遍历匹配
    HandlerMapping
        ↓ 路由到目标服务
    

* * *

## 三、改造方案详解

### 3.1 官方适配方案的问题

Spring-web 包中提供了 `AbstractReactiveWebInitializer`，但在实际运行中发现，通过它适配 Servlet 时**缺少大量 WebFlux 运行时必需的 Bean** ，导致路由无法匹配、过滤器失效等问题。根本原因在于 `ApplicationContext` 的创建方式与 jar 包模式不一致。

### 3.2 自定义 WebApplicationInitializer

核心思路：**参考`AbstractReactiveWebInitializer` 的流程，但改用 `SpringApplication.run()` 启动上下文**，保持与 jar 包启动方式完全一致。

#### 3.2.1 ApplicationContext 的创建

使用 `new SpringApplication(...).run()` 创建 ApplicationContext，与 jar 启动方式一致，能避免运行时配置相关的各类问题。

但问题来了：`SpringApplication.run()` 会同时启动内嵌 WebServer（Netty/Tomcat），而 War 包运行在外置 Servlet 容器中不需要额外的 WebServer。

**解决方案：实现一个"空壳"WebServer + 排除自动配置类。**

#### 3.2.2 处理 WebServer 冲突

  * 排除 `ReactiveWebServerFactoryAutoConfiguration` 自动配置类
  * 创建一个空实现的 `ReactiveWebServerFactory` 和 `WebServer`
  * 仅在 Servlet 容器运行时生效，jar 包运行时完全不影响



#### 3.2.3 HttpWebHandlerAdapter 的获取

通过 `SpringApplication.run()` 创建上下文后，WebFlux 相关自动配置类正常生效，`HttpWebHandlerAdapter` 已作为 Bean 注册，直接从 ApplicationContext 获取即可，无需再通过 `WebHttpHandlerBuilder` 创建。

### 3.3 核心实现代码
    
    
    abstract class AbstractReactiveWebApplicationInitializer implements WebApplicationInitializer {
    
        public static final String IS_EMBEDDED = "ReactiveWebApplicationInitializer.isEmbedded";
    
        // 空实现的 WebServer
        public static final WebServer NOOP_WEB_SERVER = new WebServer() {
            @Override
            public void start() throws WebServerException { }
            @Override
            public void stop() throws WebServerException { }
            @Override
            public int getPort() { return -1; }
        };
    
        public static final ReactiveWebServerFactory NOOP_REACTIVE_WEB_SERVER_FACTORY =
            new ReactiveWebServerFactory() {
                @Override
                public WebServer getWebServer(HttpHandler httpHandler) {
                    return NOOP_WEB_SERVER;
                }
            };
    
        // 仅在 Servlet 容器中生效的配置
        @Configuration
        @ConditionalOnProperty(value = IS_EMBEDDED, havingValue = "false")
        public static class NoEmbeddedAutoConfiguration {
    
            // 排除内嵌 WebServer 自动配置
            @Configuration
            @EnableAutoConfiguration(exclude = {
                ReactiveWebServerFactoryAutoConfiguration.class
            })
            public class DisableReactiveWebServerFactoryAutoConfiguration { }
    
            // 注册空 WebServer Factory
            @Bean
            public ReactiveWebServerFactory noopReactiveWebServerFactory() {
                return NOOP_REACTIVE_WEB_SERVER_FACTORY;
            }
        }
    
        @Override
        public void onStartup(ServletContext servletContext) throws ServletException {
            // 创建 ApplicationContext
            ApplicationContext applicationContext = createApplicationContext(servletContext);
            // 获取 HttpHandler
            HttpHandler httpHandler = applicationContext.getBean(HttpHandler.class);
            // 注册 ServletHttpHandlerAdapter...
        }
    
        protected ApplicationContext createApplicationContext(ServletContext servletContext) {
            return createSpringApplication(servletContext).run();
        }
    
        protected SpringApplication createSpringApplication(ServletContext servletContext) {
            SpringApplication springApplication = new SpringApplication(getConfigClasses());
            Map<String, Object> defaultProperties = new HashMap<>(16);
            // 标记为非内嵌模式
            defaultProperties.put(IS_EMBEDDED, false);
            // 设置 context-path
            defaultProperties.put("server.servlet.context-path",
                servletContext.getContextPath());
            springApplication.setDefaultProperties(defaultProperties);
            return springApplication;
        }
    
        protected Class<?>[] getConfigClasses() {
            return new Class[]{ getClass() };
        }
    }
    

### 3.4 处理 Context-Path 不兼容问题

War 包部署必然带 `context-path`（如 `/gateway`），而 Spring Cloud Gateway 和低版本 RouterFunction 的 Path 条件不兼容 `context-path`，会导致请求 404。

**解决方法：AOP 切面修复。**

使用 AOP 拦截 `DispatcherHandler#handle(ServerWebExchange)` 方法，在执行前修改 `ServerWebExchange` 中 `ServerHttpRequest` 的 Path，将 `context-path` 前缀去掉，再替换原 `ServerWebExchange`，继续后续路由匹配。

* * *

## 四、效果评估与局限性分析

### 4.1 可正常工作的能力

能力 | 状态  
---|---  
基础路由转发、断言匹配 | ✅ 正常  
普通 GlobalFilter、局部 Filter | ✅ 正常  
Nacos/Apollo 配置路由、动态路由刷新 | ✅ 正常  
普通 HTTP 接口、健康检查端点 | ✅ 正常  
外置 Tomcat 多 War 包共存（context-path 隔离） | ✅ 正常  
  
### 4.2 存在的致命短板

#### （1）底层 IO 模型冲突，响应式核心能力受损

标准 Gateway 核心优势是 **Netty 非阻塞 Reactor 响应式模型** ，而 War 部署外层套了 **Tomcat Servlet 阻塞容器** ：

  * 外层 Tomcat 是 BIO/NIO 阻塞线程池，内层 Gateway 是 Reactor 非阻塞，两层嵌套导致**线程池互相阻塞、吞吐量暴跌**
  * 背压机制失效，高并发下极易出现请求堆积、超时
  * WebSocket、SSE 长连接稳定性差，大量场景断连、消息丢失



#### （2）Gateway 高阶特性兼容 Bug

  * `NettyRoutingFilter` 底层依赖 Netty 客户端，外层 Tomcat 导致长链接复用、连接池管控异常
  * 限流组件（`RequestRateLimiter` 基于 Redis + Reactor）在 Servlet 适配层出现**限流计数不准**
  * 全局 CORS、路径重写、Header 转换过滤器偶现失效
  * 灰度路由、权重路由、负载均衡在高并发下匹配异常



#### （3）生命周期与监控缺陷

  * 空 WebServer 只是空壳，健康探针错乱，Actuator 部分 metrics 指标丢失（Netty 连接数、响应式线程指标）
  * Tomcat 关闭时，Reactor 上下文、Netty 客户端连接无法优雅销毁，出现**句柄泄漏**
  * 动态路由热更新偶发失效（`CachingRouteLocator` 缓存刷新线程与 Tomcat 线程竞争锁）



#### （4）Context-Path 修复是临时补丁

通过 AOP 修改 `ServerHttpRequest` 路径属于侵入式改造：

  * 多层路径、正则路由、重写路径场景下路径替换逻辑易出错
  * 链路追踪（Sleuth/Micrometer）trace 路径统计错乱，日志路径与实际访问路径不一致



#### （5）官方不支持，无版本兼容保障

  * Spring 官方明确 **WebFlux Gateway 不支持 War 部署** ，此方案为企业自研 Hack
  * Spring Cloud / Spring Boot 版本升级后，`DispatcherHandler`、`ServletHttpHandlerAdapter` 内部类结构变更，改造代码大概率失效
  * 出现问题无法在开源社区提 Issue，只能自行排坑



### 4.3 部署层面隐患

  * Tomcat 线程池资源隔离差，网关流量打满会导致同 Tomcat 下其他 War 应用卡死
  * 无法利用 Netty 专属优化（连接复用、零拷贝、EPoll），**QPS 相比原生 jar 包下降 50% 以上**
  * 容器化（K8s/Docker）部署不友好，行业标准统一使用 jar 包，War 外置 Tomcat 运维链路更复杂



* * *

## 五、场景适用性判定

### ✅ 勉强可用的场景

**内部低并发管理网关** ，仅少量路由、无长连接需求、测试/预发布环境：

基础转发、简单过滤器能正常工作，可作为临时方案使用。

### ❌ 严禁上线的场景

**线上流量入口网关** ，高并发、WebSocket、限流灰度、生产核心流量：

存在性能、稳定性、可观测性多重隐患，**严禁上线** 。

* * *

## 六、总结与建议

### 从不同维度看这套方案

维度 | 评价  
---|---  
能否打包 War、能否启动 | ✅ 完整可行  
基础路由是否生效 | ✅ 基本正常  
Gateway 完整功能 | ❌ 大量高阶特性不兼容  
生产稳定性 | ❌ 存在底层架构冲突  
性能 | ❌ QPS 下降 50% 以上  
官方规范 | ❌ 官方不支持，属 Hack 方案  
  
### 终极建议

  1. **最优方案** ：放弃 War 部署幻想，使用**原生 jar 包 + 内嵌 Netty** ，这是 Spring Cloud Gateway 的设计初衷，也是唯一官方保证稳定的运行方式。

  2. **折中方案** ：如果运维环境强制要求 Servlet 容器，改用 **`spring-cloud-starter-gateway-mvc`** （Spring Cloud Gateway 官方 Servlet 版）。虽然并发能力不如 WebFlux 版，但无需任何侵入式 Hack 改造，稳定性和可维护性有保障。

  3. **本文方案定位** ：这是一次**技术探索和验证** ，证明了"理论可行"但"生产不推荐"，适合作为学习 Spring Cloud Gateway 内部机制和 WebFlux-Servlet 适配原理的参考材料。




* * *

> **后记** ：技术选型时，"能跑起来"和"能稳定跑在生产环境"之间有巨大的鸿沟。在底层架构模型冲突面前，任何 Hack 补丁都是脆弱的。尊重框架的设计哲学，往往是最省力的路。


---
> 原文链接: https://www.cnblogs.com/huangrenhui/p/20841399