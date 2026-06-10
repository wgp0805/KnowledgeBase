
在 Spring 与 MyBatis-Plus 整合的开发中，理解 `SqlSession` 的生命周期与事务的绑定关系，是掌握一级缓存生效机制、避免性能陷阱的核心。本文将结合底层源码原理，深度剖析“事务内 SqlSession 复用”的底层逻辑。

## 一、 核心桥梁：SqlSessionTemplate 与 ThreadLocal

在原生 MyBatis 中，`SqlSession` 是线程不安全的，通常遵循“用完即关”的原则。但在 Spring 环境中，Spring 提供了一个线程安全的代理类 `SqlSessionTemplate`。

`SqlSessionTemplate` 是 Spring 与 MyBatis 的粘合剂。它内部利用 `ThreadLocal`（线程本地变量）来管理 `SqlSession` 的获取与释放。当我们在 Mapper 接口上执行 SQL 时，`SqlSessionTemplate` 会首先检查当前线程是否已经绑定了 `SqlSession`，从而决定是复用现有会话，还是创建一个全新的会话。

## 二、 场景对比：事务如何决定 SqlSession 的创建次数

`SqlSession` 的创建次数与复用机制，完全取决于当前方法是否处于 Spring 事务的管理之下。

### 1. 未开启事务：每次查询独立创建 SqlSession

假设我们在 Service 层编写了一个普通的查询方法，且**没有**添加 `@Transactional` 注解：

java

编辑

```
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    public void getUserInfo(Long userId) {
        // 第一次查询
        User user1 = userMapper.selectById(userId); 
        // 第二次查询
        User user2 = userMapper.selectById(userId); 
    }
}
```

**底层执行流程：**

- 当执行 `user1` 的查询时，`SqlSessionTemplate` 发现当前线程没有事务上下文，于是通过 `SqlSessionFactory` **新建**一个 `SqlSession`。查询完毕后，该 `SqlSession` 立即被自动关闭并归还资源。
- 当执行 `user2` 的查询时，由于前一个 `SqlSession` 已销毁，Spring 再次**新建**一个全新的 `SqlSession`。

**结果：** 两次查询使用了不同的 `SqlSession`，MyBatis 的一级缓存（作用域为 `SqlSession`）完全失效，数据库被真实访问了两次。

### 2. 开启事务：整个事务生命周期内复用 SqlSession

现在，我们在方法上加上 `@Transactional` 注解：

java

编辑

```
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    @Transactional // 关键：开启 Spring 事务
    public void getUserInfo(Long userId) {
        // 第一次查询
        User user1 = userMapper.selectById(userId); 
        // 第二次查询
        User user2 = userMapper.selectById(userId); 
    }
}
```

**底层执行流程：**

- 当方法被调用时，Spring 的事务拦截器（AOP）介入，获取数据库连接，并**新建一个 `SqlSession`**。
- 接着，Spring 通过 `TransactionSynchronizationManager` 将这个 `SqlSession` 封装为 `SqlSessionHolder`，并绑定到当前线程的 `ThreadLocal` 中。
- 执行 `user1` 查询时，`SqlSessionTemplate` 从 `ThreadLocal` 中获取到已绑定的 `SqlSession` 并执行 SQL。
- 执行 `user2` 查询时，`SqlSessionTemplate` 再次检查 `ThreadLocal`，发现**已存在**活跃的 `SqlSession`，于是**直接复用**该会话。
- 直到整个方法执行完毕，Spring 统一提交事务，并关闭这个 `SqlSession`。

**结果：** 两次查询共享同一个 `SqlSession`，第二次查询直接命中一级缓存，数据库仅被访问一次。

## 三、 进阶理解：事务传播与 SqlSession 继承

在实际开发中，我们常会遇到“方法本身没有加事务注解，但依然复用了 SqlSession”的情况。这得益于 Spring 的**事务传播机制**。

java

编辑

```
@Service
public class OrderService {
    @Autowired
    private UserService userService;

    @Transactional // 外层方法开启了事务
    public void createOrder() {
        // 调用未加事务注解的方法
        userService.getUserInfo(1001L); 
    }
}
```

在上述代码中，虽然 `getUserInfo` 方法自身没有 `@Transactional` 注解，但它在被 `createOrder` 调用时，默认会“加入”（Propagation.REQUIRED）外层的事务上下文。因此，`getUserInfo` 内部执行的 SQL，依然会复用 `createOrder` 开启并绑定在 `ThreadLocal` 中的那个 `SqlSession`，一级缓存同样能够正常生效。

## 四、 总结与最佳实践

“在事务生命周期内复用同一个 SqlSession”的本质，是 Spring 借助 `ThreadLocal` 将 `SqlSession` 与当前事务进行了强绑定。只要还在同一个事务上下文中，无论执行多少次 Mapper 方法，Spring 都会把同一个 `SqlSession` 拿出来反复使用。

**开发建议：**

1. **涉及多次数据库操作时务必加事务**：在涉及多个 SQL 操作的业务方法中，始终使用 `@Transactional` 注解。这不仅能减少 `SqlSession` 的创建开销，还能确保数据一致性，并让一级缓存发挥应有的性能优势。
2. **只读查询也可加事务**：对于复杂的只读报表查询，可以使用 `@Transactional(readOnly = true)`，这同样能复用 `SqlSession` 并触发缓存，同时向数据库和 Spring 表明该事务无需回滚支持，进一步提升性能。

深度解析：Spring 事务与 MyBatis-Plus SqlSession 复用机制

创建于 06-10 16:34

![](assets/#%20%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90%EF%BC%9ASpring%20%E4%BA%8B%E5%8A%A1%E4%B8%8E%20MyBatis-Plus%20SqlSession%20%E5%A4%8D%E7%94%A8%E6%9C%BA%E5%88%B6/fbdd9383c59006eb22512a0e7597af0f_MD5.webp)

![](assets/#%20%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90%EF%BC%9ASpring%20%E4%BA%8B%E5%8A%A1%E4%B8%8E%20MyBatis-Plus%20SqlSession%20%E5%A4%8D%E7%94%A8%E6%9C%BA%E5%88%B6/cb5ee7bfecba89b2d6751d6a8a01c6cb_MD5.ico)

![](assets/#%20%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90%EF%BC%9ASpring%20%E4%BA%8B%E5%8A%A1%E4%B8%8E%20MyBatis-Plus%20SqlSession%20%E5%A4%8D%E7%94%A8%E6%9C%BA%E5%88%B6/fbdd9383c59006eb22512a0e7597af0f_MD5.webp)

7篇来源

将第一次的提问也整合进来

# 深度解析：MyBatis-Plus 缓存机制与 Spring 事务下的 SqlSession 复用

在 Spring 与 MyBatis-Plus 整合的开发中，理解缓存机制以及 `SqlSession` 的生命周期与事务的绑定关系，是掌握性能优化、避免底层陷阱的核心。本文将结合底层源码原理，从 MyBatis-Plus 与 JPA 的缓存对比出发，深度剖析“事务内 SqlSession 复用”的底层逻辑。

## 一、 宏观对比：MyBatis-Plus 与 JPA 的缓存机制差异

MyBatis-Plus 支持缓存机制，其底层直接继承自 MyBatis。但在默认行为和设计理念上，MyBatis-Plus 与 JPA（如 Hibernate）存在显著差异。简单来说，MyBatis-Plus 支持一级和二级缓存，但默认只开启一级缓存，二级缓存需要手动配置；而 JPA 则内置了更为透明和自动化的缓存与延迟加载支持。

### 1. 一级缓存（Local Cache）

- **MyBatis-Plus**：默认开启，无法关闭。它的作用域是 `SqlSession` 级别（即单次数据库会话）。在同一个会话中，如果执行了相同的查询，会直接从缓存中获取结果。需要注意的是，在 Spring 集成环境中，`SqlSession` 通常与事务绑定，事务结束后缓存就会失效，因此在分布式环境下无效。
- **JPA**：同样默认开启一级缓存，由 `EntityManager` 管理，在同一个持久化上下文中生效。

### 2. 二级缓存（Global Cache）

- **MyBatis-Plus**：默认关闭。要使用二级缓存，必须手动进行配置（例如在配置文件中设置 `cache-enabled: true`，并在 Mapper 中声明 `<cache/>` 标签或实体类加注解）。它的作用域是 Mapper 级别（跨 `SqlSession` 共享）。此外，MyBatis-Plus 推荐并支持集成 Redis、Ehcache 等外部存储来增强分布式缓存能力。
- **JPA**：内置支持二级缓存，配置相对透明。开发者可以通过注解（如 `@Cacheable`）轻松启用，框架会在幕后自动管理缓存的读取和失效。

### 3. 设计理念：手动控制 vs 自动化透明

- **MyBatis-Plus**：强调手动控制。开发者需要自己处理事务边界、配置缓存策略（如 LRU 淘汰算法、刷新间隔等），以及处理可能出现的脏读问题。这种设计避免了“魔法”操作，让开发者对实际执行的 SQL 和缓存状态有 100% 的控制权。
- **JPA**：强调自动化与透明。JPA 提供了完善的内置缓存和延迟加载（Lazy Loading）支持，极大减少了样板代码。但代价是，如果配置不当，可能会遇到经典的“N+1 查询”等性能陷阱，需要开发者深入理解其内部机制才能做好调优。

## 二、 核心桥梁：SqlSessionTemplate 与 ThreadLocal

在原生 MyBatis 中，`SqlSession` 是线程不安全的，通常遵循“用完即关”的原则。但在 Spring 环境中，Spring 提供了一个线程安全的代理类 `SqlSessionTemplate`。

`SqlSessionTemplate` 是 Spring 与 MyBatis 的粘合剂。它内部利用 `ThreadLocal`（线程本地变量）来管理 `SqlSession` 的获取与释放。当我们在 Mapper 接口上执行 SQL 时，`SqlSessionTemplate` 会首先检查当前线程是否已经绑定了 `SqlSession`，从而决定是复用现有会话，还是创建一个全新的会话。

## 三、 场景对比：事务如何决定 SqlSession 的创建次数

MyBatis-Plus 的一级缓存是否生效，完全取决于当前方法是否处于 Spring 事务的管理之下。`SqlSession` 的创建次数与复用机制，也与此紧密相关。

### 1. 未开启事务：每次查询独立创建 SqlSession

假设我们在 Service 层编写了一个普通的查询方法，且没有添加 `@Transactional` 注解：

java

编辑

```
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    public void getUserInfo(Long userId) {
        // 第一次查询
        User user1 = userMapper.selectById(userId); 
        // 第二次查询
        User user2 = userMapper.selectById(userId); 
    }
}
```

**底层执行流程：**

- 当执行 `user1` 的查询时，`SqlSessionTemplate` 发现当前线程没有事务上下文，于是通过 `SqlSessionFactory` 新建一个 `SqlSession`。查询完毕后，该 `SqlSession` 立即被自动关闭并归还资源。
- 当执行 `user2` 的查询时，由于前一个 `SqlSession` 已销毁，Spring 再次新建一个全新的 `SqlSession`。

**结果：** 两次查询使用了不同的 `SqlSession`，MyBatis 的一级缓存（作用域为 `SqlSession`）完全失效，数据库被真实访问了两次。

### 2. 开启事务：整个事务生命周期内复用 SqlSession

现在，我们在方法上加上 `@Transactional` 注解：

java

编辑

```
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    @Transactional // 关键：开启 Spring 事务
    public void getUserInfo(Long userId) {
        // 第一次查询
        User user1 = userMapper.selectById(userId); 
        // 第二次查询
        User user2 = userMapper.selectById(userId); 
    }
}
```

**底层执行流程：**

- 当方法被调用时，Spring 的事务拦截器（AOP）介入，获取数据库连接，并新建一个 `SqlSession`。
- 接着，Spring 通过 `TransactionSynchronizationManager` 将这个 `SqlSession` 封装为 `SqlSessionHolder`，并绑定到当前线程的 `ThreadLocal` 中。
- 执行 `user1` 查询时，`SqlSessionTemplate` 从 `ThreadLocal` 中获取到已绑定的 `SqlSession` 并执行 SQL。
- 执行 `user2` 查询时，`SqlSessionTemplate` 再次检查 `ThreadLocal`，发现已存在活跃的 `SqlSession`，于是直接复用该会话。
- 直到整个方法执行完毕，Spring 统一提交事务，并关闭这个 `SqlSession`。

**结果：** 两次查询共享同一个 `SqlSession`，第二次查询直接命中一级缓存，数据库仅被访问一次。

## 四、 进阶理解：事务传播与 SqlSession 继承

在实际开发中，我们常会遇到“方法本身没有加事务注解，但依然复用了 SqlSession”的情况。这得益于 Spring 的事务传播机制。

java

编辑

```
@Service
public class OrderService {
    @Autowired
    private UserService userService;

    @Transactional // 外层方法开启了事务
    public void createOrder() {
        // 调用未加事务注解的方法
        userService.getUserInfo(1001L); 
    }
}
```

在上述代码中，虽然 `getUserInfo` 方法自身没有 `@Transactional` 注解，但它在被 `createOrder` 调用时，默认会“加入”（Propagation.REQUIRED）外层的事务上下文。因此，`getUserInfo` 内部执行的 SQL，依然会复用 `createOrder` 开启并绑定在 `ThreadLocal` 中的那个 `SqlSession`，一级缓存同样能够正常生效。

## 五、 总结与最佳实践

“在事务生命周期内复用同一个 SqlSession”的本质，是 Spring 借助 `ThreadLocal` 将 `SqlSession` 与当前事务进行了强绑定。只要还在同一个事务上下文中，无论执行多少次 Mapper 方法，Spring 都会把同一个 `SqlSession` 拿出来反复使用。

**开发建议：**

1. **涉及多次数据库操作时务必加事务**：在涉及多个 SQL 操作的业务方法中，始终使用 `@Transactional` 注解。这不仅能减少 `SqlSession` 的创建开销，还能确保数据一致性，并让一级缓存发挥应有的性能优势。
2. **只读查询也可加事务**：对于复杂的只读报表查询，可以使用 `@Transactional(readOnly = true)`，这同样能复用 `SqlSession` 并触发缓存，同时向数据库和 Spring 表明该事务无需回滚支持，进一步提升性能。
3. **合理评估二级缓存**：对于 MyBatis-Plus 的二级缓存，在单机简单场景下可手动开启；但在分布式微服务架构中，建议直接使用 Redis 等分布式缓存方案，以避免多节点间的数据不一致问题。