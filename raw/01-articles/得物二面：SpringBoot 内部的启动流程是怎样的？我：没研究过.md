---
title: "得物二面：SpringBoot 内部的启动流程是怎样的？我：没研究过..."
source: "https://mp.weixin.qq.com/s/UI8QjzQz_LW_VnwMoVF3cQ"
---

## 面试考察点

1. **源码级理解深度** ：面试官不仅仅是想听你背流程，更想知道你是否真正跟过 `              SpringApplication.run()            ` 的源码，能不能说出关键类和方法的调用链路。
2. **自动配置原理** ：Spring Boot 最核心的特性就是 "约定优于配置"，启动流程中如何实现自动配置是必考点。
3. **扩展点掌握** ：能否说出启动过程中有哪些扩展点（ `ApplicationContextInitializer` 、 `ApplicationRunner` 等），以及在实际项目中如何利用这些扩展点。

## 核心答案

一切从 `main()` 方法里这行代码开始：

```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        
            SpringApplication.run(MyApp
          .class, args);
    }
}
```

`SpringApplication.run()` 的完整启动流程可以概括为 **7 个核心步骤** ：

| 步骤 | 做了什么 | 关键源码方法 |
| --- | --- | --- |
| 1 | 创建 `SpringApplication` 对象 | `new SpringApplication()` |
| 2 | 推断应用类型（Servlet / Reactive / None） | `              WebApplicationType.deduce()            ` |
| 3 | 加载 `ApplicationContextInitializer` 和 `ApplicationListener` | `getSpringFactoriesInstances()` |
| 4 | 创建并准备 `ApplicationContext` | `createApplicationContext()` |
| 5 | 执行 `BeanDefinition` 扫描和加载 | `refresh()` |
| 6 | 自动配置（ `@EnableAutoConfiguration` ） | `AutoConfigurationImportSelector` |
| 7 | 执行 `CommandLineRunner` / `ApplicationRunner` | `callRunners()` |

## 深度解析

### 一、整体启动流程图
[Open: file-20260525105742322.png](assets/%E5%BE%97%E7%89%A9%E4%BA%8C%E9%9D%A2%EF%BC%9ASpringBoot%20%E5%86%85%E9%83%A8%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E7%A0%94%E7%A9%B6%E8%BF%87/5d393290d7e9e62c6543e5f01a6604ef_MD5.jpg)
![](assets/%E5%BE%97%E7%89%A9%E4%BA%8C%E9%9D%A2%EF%BC%9ASpringBoot%20%E5%86%85%E9%83%A8%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E7%A0%94%E7%A9%B6%E8%BF%87/5d393290d7e9e62c6543e5f01a6604ef_MD5.jpg)

上图展示了 Spring Boot 从 `run()` 到应用完全启动的全过程。整体分为 5 个阶段：

- **阶段一（创建 `SpringApplication` ）** ：这是启动的准备工作。推断当前是普通 Java 应用还是 Web 应用（Servlet 或 Reactive），通过 SPI 机制加载所有的 `ApplicationContextInitializer` 和 `ApplicationListener` 。这一步还不会创建 IoC 容器。
- **阶段三（准备上下文）** ：把 `Environment` 绑定到容器上，执行所有 `ApplicationContextInitializer` 的 `initialize()` 方法，把主配置类注册为 `BeanDefinition` 。
- **阶段四（ `refresh()` 刷新容器）** ：这是整个启动流程中最核心也最复杂的一步。包括 Bean 定义的扫描与注册、自动配置的生效、所有单例 Bean 的创建和依赖注入、内嵌 Tomcat/Jetty 的启动。可以说 Spring 容器的 "心脏跳动" 就在这一步。
- **阶段五（执行 Runner）** ：容器完全就绪后，执行所有 `CommandLineRunner` 和 `ApplicationRunner` ，应用开始对外提供服务。

### 二、第一步：new SpringApplication() 做了什么？

```java
public SpringApplication(ResourceLoader resourceLoader, Class<?>... primarySources) {
    // 1. 推断应用类型：Servlet、Reactive、还是非 Web
    this.webApplicationType = 
            WebApplicationType.deduceFromClasspath();
          

    // 2. 从 
            spring.factories
           加载 ApplicationContextInitializer
    setInitializers((Collection) getSpringFactoriesInstances(
        ApplicationContextInitializer.class));

    // 3. 从 
            spring.factories
           加载 ApplicationListener
    setListeners((Collection) getSpringFactoriesInstances(
        ApplicationListener.class));

    // 4. 推断主配置类（main 方法所在的类）
    this.mainApplicationClass = deduceMainApplicationClass();
}
```

这里有个关键点： **SPI 机制** （ `Spring Factories` ）。Spring Boot 通过 `SpringFactoriesLoader` 扫描所有 jar 包 `META-INF/             spring.factories           ` 文件，加载里面配置的类。这是自动配置的基础。

### 三、自动配置是怎么生效的？

`@SpringBootApplication` 是个复合注解，拆开来看：

```md
@SpringBootApplication
  ├── @SpringBootConfiguration    // 本质就是 @Configuration
  ├── @EnableAutoConfiguration    // 核心！开启自动配置
  │     └── @Import(AutoConfigurationImportSelector.class)
  └── @ComponentScan              // 组件扫描，扫描主类同包及子包下的组件
```

自动配置的关键在 `@EnableAutoConfiguration` ，它导入的 `AutoConfigurationImportSelector` 做了这些事：
[Open: file-20260525105813780.png](assets/%E5%BE%97%E7%89%A9%E4%BA%8C%E9%9D%A2%EF%BC%9ASpringBoot%20%E5%86%85%E9%83%A8%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E7%A0%94%E7%A9%B6%E8%BF%87/cb1d01a0ab35d544e827e6fe04a184d3_MD5.jpg)
![](assets/%E5%BE%97%E7%89%A9%E4%BA%8C%E9%9D%A2%EF%BC%9ASpringBoot%20%E5%86%85%E9%83%A8%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B%E6%98%AF%E6%80%8E%E6%A0%B7%E7%9A%84%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E7%A0%94%E7%A9%B6%E8%BF%87/cb1d01a0ab35d544e827e6fe04a184d3_MD5.jpg)

上图展示了自动配置的完整过滤链路。核心逻辑就是：

- 先从 `              spring.factories            ` 里读出一大堆 `xxxAutoConfiguration` （Spring Boot 2.7+ 也支持 `META-INF/spring/             org.springframework.boot.autoconfigure.AutoConfiguration.imports           ` 文件）。
- 然后通过 `@ConditionalOnXxx` 注解逐个过滤， **满足条件的才生效** 。比如 `DataSourceAutoConfiguration` 只有 classpath 上有数据库驱动时才生效。
- 用户自定义的 Bean 优先级更高。 `@ConditionalOnMissingBean` 保证只有用户没配的时候，Spring Boot 才提供默认实现。

这就是 Spring Boot "约定优于配置" 的精髓——你不用配，我给你默认的；你要配，你的优先。

### 四、refresh() 里面做了什么？

`refresh()` 是 Spring 容器启动的核心方法，定义在 `AbstractApplicationContext` 中，包含 **12 个步骤** ：

```
public void refresh() throws BeansException, IllegalStateException {
    // 1. 准备刷新（设置启动时间、状态标记）
    prepareRefresh();

    // 2. 获取 BeanFactory（创建 DefaultListableBeanFactory）
    ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();

    // 3. 准备 BeanFactory（设置类加载器、后置处理器等）
    prepareBeanFactory(beanFactory);

    // 4. 后置处理 BeanFactory（模板方法，子类扩展）
    postProcessBeanFactory(beanFactory);

    // 5. 执行 BeanFactoryPostProcessor（扫描 @Component、@Configuration 等）
    invokeBeanFactoryPostProcessors(beanFactory);

    // 6. 注册 BeanPostProcessor（AOP、@Autowired 等都在这里）
    registerBeanPostProcessors(beanFactory);

    // 7. 初始化消息源（国际化）
    initMessageSource();

    // 8. 初始化事件广播器
    initApplicationEventMulticaster();

    // 9. 初始化其他特殊 Bean（模板方法，子类扩展）
    onRefresh();
    //    ↑ Spring Boot 在这里启动内嵌 Tomcat！

    // 10. 注册监听器
    registerListeners();

    // 11. 实例化所有非懒加载的单例 Bean
    finishBeanFactoryInitialization(beanFactory);

    // 12. 完成刷新（发布 ContextRefreshedEvent）
    finishRefresh();
}
```

其中最关键的三步：

- **第 5 步** ：执行 `BeanFactoryPostProcessor` ，这一步会扫描 `@Component` 、 `@Configuration` 等注解，把 Bean 定义注册到容器中。自动配置的 `AutoConfigurationImportSelector` 也是在这里被触发的。
- **第 11 步** ：实例化所有非懒加载的单例 Bean，完成依赖注入。你的 `@Service` 、 `@Controller` 、 `@Repository` 标注的类，全在这一步被创建。
- **第 9 步（ `onRefresh()` ）** ：Spring Boot 重写了这个方法，在里头启动了内嵌的 Web 容器（Tomcat / Jetty / Undertow）。所以 Tomcat 是在 `refresh()` 过程中、所有 Bean 创建之前就启动了。

### 五、@SpringBootApplication 注解拆解

面试的时候如果被问到这个注解的含义，直接画出来就行：

```java
// @SpringBootApplication 等价于以下三个注解的组合
@SpringBootConfiguration    // 标记当前类是配置类（等同于 @Configuration）
@EnableAutoConfiguration    // 开启自动配置（核心！）
@ComponentScan(             // 组件扫描
    excludeFilters = {
        @Filter(type = 
            FilterType.CUSTOM,
           classes = TypeExcludeFilter.class),
        @Filter(type = 
            FilterType.CUSTOM,
           classes = AutoConfigurationExcludeFilter.class)
    }
)
public @interface SpringBootApplication { }
```

`@ComponentScan` 默认扫描 **主启动类所在包及其子包** ，这也是为什么你的 `@Controller` 、 `@Service` 必须放在启动类同包或子包下，否则扫描不到。

## 面试高频追问

1. **追问一：Spring Boot 自动配置的原理是什么？**
- 核心是 `@EnableAutoConfiguration` → `AutoConfigurationImportSelector` → 从 `              spring.factories            ` （或 `              AutoConfiguration.imports            ` ）加载所有自动配置类 → 通过 `@ConditionalOnXxx` 条件过滤 → 满足条件的自动注册 Bean。一句话： **先全量加载，再按条件过滤。**
3. **追问二： `BeanFactory` 和 `ApplicationContext` 有什么区别？**
- `BeanFactory` 是 Spring 的顶层容器接口，只提供最基本的 Bean 管理功能（懒加载）。 `ApplicationContext` 是它的子接口，扩展了国际化、事件发布、AOP 集成、资源加载等功能。Spring Boot 启动时创建的就是 `ApplicationContext` ，而不是直接用 `BeanFactory` 。
5. **追问三：如何自定义一个 Starter？**
- 核心就是写一个 `xxxAutoConfiguration` 类（用 `@ConditionalOnXxx` 做条件控制），然后在 `META-INF/             spring.factories           ` 里注册。Spring Boot 启动时会自动加载。Spring Boot 2.7+ 推荐用 `META-INF/spring/             org.springframework.boot.autoconfigure.AutoConfiguration.imports           ` 文件替代 `              spring.factories            ` 。

## 常见面试变体

- "说一下 Spring Boot 的自动配置原理？"
- " `@SpringBootApplication` 注解由哪些注解组成？"
- "Spring Boot 启动时内嵌 Tomcat 是什么时候启动的？"
- " `              spring.factories            ` 文件的作用是什么？"

## 记忆口诀

> “
> 
> **创建推断 → 准备上下文 → 刷新容器 → 执行 Runner**
> 
> 拆开就是： **创建 SpringApplication → 创建 ApplicationContext → prepareContext → refresh() → callRunners()**
> 
> 其中 `refresh()` 是最核心的： **扫 Bean 定义 → 注册后置处理器 → 启动 Tomcat → 创建单例 Bean → 发布事件**

## 总结

Spring Boot 启动流程的核心就是 `              SpringApplication.run()            ` 这一条线： **创建 `SpringApplication` 对象** （推断类型、加载扩展点）→ \*\*创建并准备 `ApplicationContext` \*\*（环境准备、执行 Initializer）→ **`refresh()` 刷新容器** （扫描注册 Bean、自动配置、启动 Tomcat、依赖注入）→ \*\*执行 `Runner` \*\*。面试时抓住 "创建、准备、刷新、执行" 这四个阶段展开就行，其中 `refresh()` 和自动配置是面试官最关注的两个点。

