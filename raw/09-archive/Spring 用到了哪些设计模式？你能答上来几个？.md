---
title: "Spring 用到了哪些设计模式？你能答上来几个？"
source: "https://mp.weixin.qq.com/s/dX-3P5T-ZxWzYYn0NGr49A"
---

## 面试考察点

1. **设计模式认知广度** ：面试官不仅仅是想听你背出几个模式的名字，更是想知道你能否将设计模式与 Spring 的具体实现对应起来，而不是泛泛而谈。
2. **源码阅读深度** ：能准确说出每个设计模式在 Spring 中的对应组件，说明你确实读过源码，而不只是看过八股文。面试官特别在意这点。
3. **理论联系实际** ：考察你是否理解为什么要用这些设计模式，解决了什么问题，以及在你自己的项目中能否借鉴运用。

## 核心答案

Spring 框架中用到的设计模式非常多，面试中最常被考察的有 **9 大设计模式** ：

| 设计模式 | Spring 中的典型应用 | 一句话说明 |
| --- | --- | --- |
| 工厂模式 | `BeanFactory`  、 `ApplicationContext` | 把对象的创建过程封装起来 |
| 单例模式 | Bean 的默认作用域 | 整个容器中只有一个实例 |
| 代理模式 | AOP（JDK 动态代理 / CGLIB） | 不改源码就能增强功能 |
| 模板方法模式 | `JdbcTemplate`  、 `RestTemplate` | 固定骨架，可变步骤留给子类 |
| 观察者模式 | 事件机制 `ApplicationEvent` | 一处发布，多处监听 |
| 适配器模式 | `HandlerAdapter`  、 `MessageConverter` | 让不兼容的接口能协同工作 |
| 策略模式 | `Resource`  接口、 `InstantiationStrategy` | 同一接口，不同实现策略 |
| 责任链模式 | `Filter`  链、 `Interceptor` 链 | 请求沿着链条依次处理 |
| 装饰器模式 | `BeanWrapper`  、 `HttpRequestDecorator` | 动态增强对象功能 |

下面挑最核心的几个展开讲。

## 深度解析

### 一、工厂模式（Spring 的心脏）

工厂模式是 Spring 的基石。你天天写 `@Component` 、 `@Service` ，有没有想过这些对象是谁创建的？就是 `BeanFactory` 。
[Open: file-20260525161604088.png](assets/Spring%20%E7%94%A8%E5%88%B0%E4%BA%86%E5%93%AA%E4%BA%9B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%9F%E4%BD%A0%E8%83%BD%E7%AD%94%E4%B8%8A%E6%9D%A5%E5%87%A0%E4%B8%AA%EF%BC%9F/25b91c7f3d4c1e66d5f71943be102515_MD5.jpg)
![](assets/Spring%20%E7%94%A8%E5%88%B0%E4%BA%86%E5%93%AA%E4%BA%9B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%9F%E4%BD%A0%E8%83%BD%E7%AD%94%E4%B8%8A%E6%9D%A5%E5%87%A0%E4%B8%AA%EF%BC%9F/25b91c7f3d4c1e66d5f71943be102515_MD5.jpg)

上图展示了 Spring 工厂体系的层次结构：

- \*\* `BeanFactory` \*\*：最顶层的工厂接口，提供了 `getBean()` 这样的基本能力，属于 "懒加载"，用到 Bean 的时候才创建。
- \*\* `ApplicationContext` \*\*： `BeanFactory` 的超集，除了创建 Bean，还集成了国际化、事件发布、资源加载等功能。我们平时用的 `@SpringBootApplication` 启动后拿到的就是它。
- 具体实现有 `ClassPathXmlApplicationContext` （XML 配置时代）和 `AnnotationConfigApplicationContext` （注解时代），不同的工厂实现从不同的配置源读取 Bean 定义，但对外暴露的 `getBean()` 接口完全一致。

这就是工厂模式的核心思想： **把对象的创建逻辑封装在工厂内部，调用方不需要关心对象是怎么 new 出来的** 。

### 二、单例模式（Spring Bean 的默认作用域）

Spring 的单例不是传统意义上的 "写个 `private` 构造器 + `static` 实例" 那种单例，而是 **容器级别的单例** ——由容器来保证同一个 `id` 的 Bean 只创建一次。

```java
// Spring 的单例实现（DefaultSingletonBeanRegistry 源码简化）
publicclass DefaultSingletonBeanRegistry {

    // 一级缓存：存放完全初始化好的单例 Bean
    privatefinal Map<String, Object> singletonObjects = new ConcurrentHashMap<>();

    public Object getSingleton(String beanName) {
        Object singleton = 
            singletonObjects.get(beanName);
          
        if (singleton == null) {
            singleton = createBean(beanName);
            
            singletonObjects.put(beanName,
           singleton);
        }
        return singleton;
    }
}
```

Spring 用 **三级缓存** 来解决单例 Bean 的循环依赖问题，这个在面试中经常和单例模式一起追问。有兴趣的可以去看 `DefaultSingletonBeanRegistry` 的源码，三个 `Map` 摆在那里，一目了然。

补充一句：Spring 的单例是非线程安全的。因为单例 Bean 在容器中只有一个实例，如果 Bean 里有可变状态，多线程并发访问就会出问题。所以 Spring 官方推荐 Bean 设计为 **无状态** 的。

### 三、代理模式（AOP 的灵魂）

这个应该是大家最熟悉的。Spring AOP 的两种实现方式——JDK 动态代理和 CGLIB 代理，本质上都是代理模式的应用。

```java
// JDK 动态代理示例（Spring AOP 的原理简化）
publicclass JdkProxyDemo implements InvocationHandler {

    private Object target;

    public Object createProxy(Object target) {
        this.target = target;
        return 
            Proxy.newProxyInstance(
          
            
            target.getClass().getClassLoader(),
          
            
            target.getClass().getInterfaces(),
          
            this
        );
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 前置通知
        
            System.out.println(
          "Before: " + 
            method.getName());
          
        // 执行目标方法
        Object result = 
            method.invoke(target,
           args);
        // 后置通知
        
            System.out.println(
          "After: " + 
            method.getName());
          
        return result;
    }
}
```

代理模式的精髓在于： **不修改原有代码的前提下，对功能进行增强** 。不管是日志、事务、权限控制，统统可以通过代理来织入，这就是 AOP 能成立的基础。

### 四、模板方法模式（JdbcTemplate 一族）

模板方法模式在 Spring 中用得非常多，但凡名字里带 `Template` 的，基本都是。

```java
// JdbcTemplate 的典型用法

            jdbcTemplate.query(
          "SELECT * FROM user WHERE id = ?",
    (rs, rowNum) -> {         // ← 你只需要关注这一部分
        User user = new User();
        
            user.setId(rs.getLong(
          "id"));
        
            user.setName(rs.getString(
          "name"));
        return user;
    },
    1L                        // 参数
);
// 连接获取、Statement 创建、异常处理、资源关闭 —— 全部由模板搞定
```

模板方法模式的套路是： **父类定义算法骨架（固定流程），子类实现可变步骤** 。 `JdbcTemplate` 把 JDBC 那套繁琐的 `try-catch-finally` 流程全部封装好了，你只需要告诉它 "SQL 是什么" 和 "结果怎么映射"，其他的一概不用操心。

Spring 中类似的还有 `RestTemplate` 、 `JmsTemplate` 、 `RedisTemplate` ，套路完全一样。

### 五、观察者模式（事件机制）

Spring 的事件机制就是标准的观察者模式：一个事件发布者，N 个事件监听者。

```java
// 1. 定义事件
publicclass OrderCreatedEvent extends ApplicationEvent {
    private Order order;
    public OrderCreatedEvent(Object source, Order order) {
        super(source);
        this.order = order;
    }
}

// 2. 发布事件
@Service
publicclass OrderService {
    @Autowired
    private ApplicationEventPublisher publisher;

    public void createOrder(Order order) {
        // 业务逻辑...
        
            publisher.publishEvent(
          new OrderCreatedEvent(this, order));
    }
}

// 3. 监听事件（可以有多个监听者）
@Component
publicclass EmailNotifier {
    @EventListener
    public void onOrderCreated(OrderCreatedEvent event) {
        // 发邮件通知
    }
}

@Component
publicclass PointsService {
    @EventListener
    public void onOrderCreated(OrderCreatedEvent event) {
        // 积分奖励
    }
}
```

这个模式在实际项目中非常有用。下单之后要发短信、送积分、更新库存……如果全写在一个方法里，耦合度爆炸。用事件机制解耦之后，各干各的，互不影响，新增功能只需要加个 `@EventListener` 就行。

### 六、适配器模式（Spring MVC 的核心）

Spring MVC 中 `HandlerAdapter` 就是典型的适配器模式。
[Open: file-20260525161635389.png](assets/Spring%20%E7%94%A8%E5%88%B0%E4%BA%86%E5%93%AA%E4%BA%9B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%9F%E4%BD%A0%E8%83%BD%E7%AD%94%E4%B8%8A%E6%9D%A5%E5%87%A0%E4%B8%AA%EF%BC%9F/1522daea579c59b2c2f2343e4d44ecfa_MD5.jpg)
![](assets/Spring%20%E7%94%A8%E5%88%B0%E4%BA%86%E5%93%AA%E4%BA%9B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%9F%E4%BD%A0%E8%83%BD%E7%AD%94%E4%B8%8A%E6%9D%A5%E5%87%A0%E4%B8%AA%EF%BC%9F/1522daea579c59b2c2f2343e4d44ecfa_MD5.jpg)
上图的逻辑是：

- `DispatcherServlet` 拿到一个 Handler 后，不知道它具体是什么类型（可能是传统 `Controller` 接口，可能是 `@RequestMapping` 注解方法，也可能是 `HttpRequestHandler` ）。
- 于是 `DispatcherServlet` 不直接调用 Handler，而是找到对应的 `HandlerAdapter` ，由适配器来负责调用。每种 Handler 都有自己专属的适配器实现。
- 这样 `DispatcherServlet` 只需要面向 `HandlerAdapter` 这个统一接口编程，完全不用关心底层 Handler 的差异。

这就是适配器模式的价值： **让原本不兼容的接口能够协同工作** 。

### 七、策略模式

Spring 中策略模式的应用也很多，比如资源加载：

```java
// Resource 接口有多种实现策略
Resource resource1 = new ClassPathResource("
            config.xml"
          );     // 类路径
Resource resource2 = new FileSystemResource("/etc/
            config.xml"
          ); // 文件系统
Resource resource3 = new UrlResource("
            https://example.com/config.xml"
          ); // 网络

// AbstractApplicationContext 中的资源加载策略
public interface ResourceLoader {
    Resource getResource(String location);
}
```

调用方只面向 `Resource` 接口编程，至于底层是从类路径读、从磁盘读、还是从网络读，由具体的策略实现来决定。

## 面试高频追问

1. **Spring 的单例是线程安全的吗？**
- 不是。Spring 只保证容器中只有一个实例，但不保证线程安全。Bean 中如果包含可变状态（比如成员变量），需要自己处理并发问题。所以 Spring 官方推荐 Bean 设计为无状态的。
3. **Spring 的三级缓存是怎么回事？**
- `singletonObjects` （一级）、 `earlySingletonObjects` （二级）、 `singletonFactories` （三级）。三级缓存主要为了解决循环依赖场景下的代理对象创建问题。不是所有循环依赖都能解决——构造器注入的循环依赖就搞不定。
5. **工厂模式和简单工厂有什么区别？**
- 简单工厂通过参数决定创建哪个产品，违反了开闭原则。Spring 用的是工厂方法模式（每个 BeanDefinition 对应一个创建逻辑）和抽象工厂模式（ `BeanFactory` 接口有多种实现），扩展性更好。

## 常见面试变体

- "说说 Spring MVC 中用到了哪些设计模式？"
- "Spring 的 AOP 用了什么设计模式？具体怎么实现的？"
- "为什么要用工厂模式？直接 new 不行吗？"
- "你在项目中有用到过设计模式吗？"

## 记忆口诀

\*\*"工单代模观，适策责装"\*\*——工厂、单例、代理、模板方法、观察者、适配器、策略、责任链、装饰器。9 大模式一口吞。

## 总结

Spring 框架几乎把 GoF 23 种设计模式用了个遍。面试中重点掌握工厂模式（ `BeanFactory` ）、单例模式（Bean 作用域）、代理模式（AOP）、模板方法模式（ `JdbcTemplate` ）这四个，再能讲清楚适配器模式（ `HandlerAdapter` ）和观察者模式（事件机制），就足够让面试官满意了。关键是每个模式都要能对应到 Spring 的具体实现组件，而不是干巴巴地背概念。
