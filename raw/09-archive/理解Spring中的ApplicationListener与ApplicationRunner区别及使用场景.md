---
title: 理解Spring中的ApplicationListener与ApplicationRunner区别及使用场景
tags:
  - SpringBoot
categories:
  - SpringBoot
date: 2025-02-20 10:15:43
---

# 理解Spring中的ApplicationListener与ApplicationRunner区别及使用场景

## 一、核心差异对比

| **对比维度**     | **ApplicationListener**                          | **ApplicationRunner**                    |
| ---------------- | ------------------------------------------------ | ---------------------------------------- |
| **所属框架**     | Spring Framework                                 | Spring Boot                              |
| **接口用途**     | 事件监听机制（观察者模式）                       | 应用启动后执行初始化任务                 |
| **触发时机**     | 根据事件发布时机（如容器刷新、关闭、自定义事件） | 所有单例Bean初始化完成后（仅执行一次）   |
| **参数类型**     | `ApplicationEvent` 及其子类                      | `ApplicationArguments`（封装命令行参数） |
| **执行顺序控制** | 通过`@Order`或实现`Ordered`接口                  | 通过`@Order`或实现`Ordered`接口          |
| **典型应用场景** | 解耦组件间通信、监控容器生命周期事件             | 加载配置、初始化数据、启动后台任务       |

------

## 二、调用时机说明

### 1. ApplicationListener 事件触发点

- **ContextRefreshedEvent**：容器刷新完成（所有Bean创建完毕）时触发 [5](https://blog.csdn.net/xiamaocheng/article/details/119942214)
- **ContextClosedEvent**：容器关闭时触发
- **自定义事件**：通过`applicationContext.publishEvent()` 手动发布 [1](https://www.cnblogs.com/dyaqi/p/18242522)[7](https://www.jb51.net/program/3048074ej.htm)
- **其他内置事件**：如`RequestHandledEvent`（请求处理完成）

### 2. ApplicationRunner 执行时机

- 在Spring Boot的`ApplicationContext`完全初始化后执行
- 所有单例Bean已加载完成，**晚于** `ApplicationListener<ContextRefreshedEvent>`的执行 [6](https://blog.csdn.net/yanyc0411/article/details/135208799)

------

## 三、测试用例演示

### 1. ApplicationListener 实现示例

```plain
java

复制
// 监听容器刷新事件
@Component
public class ContextRefreshListener implements ApplicationListener<ContextRefreshedEvent> {
    @Override
    public void onApplicationEvent(ContextRefreshedEvent event) {
        System.out.println("[ApplicationListener]  容器已刷新");
    }
}

// 自定义事件监听
@Component
public class CustomEventListener implements ApplicationListener<MyCustomEvent> {
    @Override
    public void onApplicationEvent(MyCustomEvent event) {
        System.out.println("[ApplicationListener]  收到自定义事件：" + event.getMessage()); 
    }
}

// 事件发布
applicationContext.publishEvent(new  MyCustomEvent("测试事件"));
```

### 2. ApplicationRunner 实现示例

```plain
java

复制
@Component
@Order(1)
public class DatabaseInitializer implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("[ApplicationRunner]  初始化数据库连接池");
    }
}

@Component
@Order(2)
public class CachePreloader implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("[ApplicationRunner]  加载缓存数据");
    }
}
```

**控制台输出顺序**：

```plain
[ApplicationListener] 容器已刷新  
[ApplicationRunner] 初始化数据库连接池  
[ApplicationRunner] 加载缓存数据
```

------

## 四、适用场景建议

### ApplicationListener 适用场景

- **组件解耦**：通过事件机制实现模块间松耦合通信 [1](https://www.cnblogs.com/dyaqi/p/18242522)
- **生命周期监控**：跟踪容器启动、关闭等关键节点 [5](https://blog.csdn.net/xiamaocheng/article/details/119942214)
- **异步处理**：配合`@Async`实现事件异步消费
- **跨模块操作**：例如在用户注册成功后触发邮件通知

### ApplicationRunner 适用场景

- **启动初始化**：数据库脚本执行、配置文件校验 [4](https://www.cnblogs.com/zzprogram/p/17501126.html)[6](https://blog.csdn.net/yanyc0411/article/details/135208799)
- **资源预加载**：缓存预热、线程池初始化
- **参数解析**：处理带`--`前缀的命令行选项参数
- **延迟任务启动**：例如初始化后启动定时任务

------

## 五、技术选型总结

| **选择依据**               | **推荐组件**         |
| -------------------------- | -------------------- |
| 需要响应容器生命周期事件   | ApplicationListener  |
| 需要处理自定义业务事件     | ApplicationListener  |
| 应用启动后执行一次性初始化 | ApplicationRunner    |
| 需要解析命令行参数         | ApplicationRunner    |
| 需要控制多个任务的执行顺序 | 两者都支持（@Order） |

通过合理选择这两个接口，可以更好地管理Spring应用的初始化流程和事件响应机制。实际开发中两者常结合使用，例如用`ApplicationListener`监听容器就绪事件，再用`ApplicationRunner`执行后续初始化。
