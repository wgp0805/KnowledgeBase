---
title: "吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？"
source: "https://mp.weixin.qq.com/s/kmnwUWuyCD-dyoecNlDeeA"
---
小哈学Java *2026年9月8日 21:00*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/948aeed290af1f0272a7a8baa1fbfa03_MD5.webp)

来源： [https://blog.csdn.net/mycs2012/article/details/90898128](https://blog.csdn.net/mycs2012/article/details/90898128)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 1 FastThreadLocal 的引入背景和原理简介
- 2 实现源码分析
- 2.1 UnpaddedInternalThreadLocalMap 的主要属性
	- 2.2 InternalThreadLocalMap 分析
	- 2.3 ftlt 的实现分析
	- 2.4 ftl 实现分析
	- 2.5 普通线程使用 ftl 的性能退化
- 3 ftl 的资源回收机制
- 4 ftl 在 netty 中的使用

---

## 1 FastThreadLocal 的引入背景和原理简介

既然 jdk 已经有 ThreadLocal，为何 netty 还要自己造个 FastThreadLocal？FastThreadLocal 快在哪里？

这需要从 jdk ThreadLocal 的本身说起。如下图：

![JDK ThreadLocal 结构示意](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/ca9d2c5e1770c72b9c6fa13a32a49613_MD5.webp)

JDK ThreadLocal 结构示意

在 java 线程中，每个线程都有一个 ThreadLocalMap 实例变量（如果不使用 ThreadLocal，不会创建这个 Map，一个线程第一次访问某个 ThreadLocal 变量时，才会创建）。

该 Map 是使用线性探测的方式解决 hash 冲突的问题，如果没有找到空闲的 slot，就不断往后尝试，直到找到一个空闲的位置，插入 entry，这种方式在经常遇到 hash 冲突时，影响效率。

FastThreadLocal(下文简称 ftl)直接使用数组避免了 hash 冲突的发生，具体做法是：每一个 FastThreadLocal 实例创建时，分配一个下标 index；分配 index 使用 AtomicInteger 实现，每个 FastThreadLocal 都能获取到一个不重复的下标。

当调用 `              ftl.get()            ` 方法获取值时，直接从数组获取返回，如 `return array[index]` ，如下图：

![FastThreadLocal 数组下标访问示意](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/314b2beb31f3590442ddc0f8b9f9d32c_MD5.png)

FastThreadLocal 数组下标访问示意

## 2 实现源码分析

根据上文图示可知，ftl 的实现，涉及到 InternalThreadLocalMap、FastThreadLocalThread 和 FastThreadLocal 几个类，自底向上，我们先从 InternalThreadLocalMap 开始分析。

InternalThreadLocalMap 类的继承关系图如下：

![InternalThreadLocalMap 继承关系图](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/1ab9942beaf85d3d354241043664de9b_MD5.jpg)

InternalThreadLocalMap 继承关系图

### 2.1 UnpaddedInternalThreadLocalMap 的主要属性

```
static final ThreadLocal<InternalThreadLocalMap> slowThreadLocalMap = new ThreadLocal<InternalThreadLocalMap>();
static final AtomicInteger nextIndex = new AtomicInteger();
Object[] indexedVariables;
```

数组 indexedVariables 就是用来存储 ftl 的 value 的，使用下标的方式直接访问。nextIndex 在 ftl 实例创建时用来给每个 ftl 实例分配一个下标，slowThreadLocalMap 在线程不是 ftlt 时使用到。

### 2.2 InternalThreadLocalMap 分析

InternalThreadLocalMap 的主要属性：

```
// 用于标识数组的槽位还未使用
public static final Object UNSET = new Object();
/**
 * 用于标识ftl变量是否注册了cleaner
 * BitSet简要原理：
 * BitSet默认底层数据结构是一个long[]数组，开始时长度为1，即只有long[0],而一个long有64bit。
 * 当
            BitSet.set(1)的时候，表示将long[0]的第二位设置为true，即0000
           0000 ... 0010（64bit）,则long[0]==2
 * 当
            BitSet.get(1)的时候，第二位为1，则表示true；如果是0，则表示false
          
 * 当
            BitSet.set(64)的时候，表示设置第65位，此时long[0]已经不够用了，扩容处long[1]来，进行存储
          
 *
 * 存储类似 {index:boolean} 键值对，用于防止一个FastThreadLocal多次启动清理线程
 * 将index位置的bit设为true，表示该InternalThreadLocalMap中对该FastThreadLocal已经启动了清理线程
 */
private BitSet cleanerFlags;

private InternalThreadLocalMap() {
    super(newIndexedVariableTable());
}

private static Object[] newIndexedVariableTable() {
    Object[] array = new Object[32];
    
            Arrays.fill(array,
           UNSET);
    return array;
}
```

比较简单， `newIndexedVariableTable()` 方法创建长度为 32 的数组，然后初始化为 UNSET，然后传给父类。之后 ftl 的值就保存到这个数组里面。

> “
> 
> 注意，这里保存的直接是变量值，不是 entry，这是和 jdk ThreadLocal 不同的。InternalThreadLocalMap 就先分析到这，其他方法在后面分析 ftl 再具体说。

### 2.3 ftlt 的实现分析

要发挥 ftl 的性能优势，必须和 ftlt 结合使用，否则就会退化到 jdk 的 ThreadLocal。ftlt 比较简单，关键代码如下：

```
public class FastThreadLocalThread extends Thread {
  // This will be set to true if we have a chance to wrap the Runnable.
  private final boolean cleanupFastThreadLocals;

  private InternalThreadLocalMap threadLocalMap;

  public final InternalThreadLocalMap threadLocalMap() {
        return threadLocalMap;
  }
  public final void setThreadLocalMap(InternalThreadLocalMap threadLocalMap) {
        this.threadLocalMap = threadLocalMap;
  }
}
```

ftlt 的诀窍就在 threadLocalMap 属性，它继承 java Thread，然后聚合了自己的 InternalThreadLocalMap。后面访问 ftl 变量，对于 ftlt 线程，都直接从 InternalThreadLocalMap 获取变量值。

### 2.4 ftl 实现分析

ftl 实现分析基于 [netty-4.1.34](http://netty-4.1.34) 版本，特别地声明了版本，是因为在清除的地方，该版本的源码已经注释掉了 ObjectCleaner 的调用，和之前的版本有所不同。

##### 2.4.1 ftl 的属性和实例化

```
private final int index;

public FastThreadLocal() {
    index = 
            InternalThreadLocalMap.nextVariableIndex();
          
}
```

非常简单，就是给属性 index 赋值，赋值的静态方法在 InternalThreadLocalMap：

```
public static int nextVariableIndex() {
    int index = 
            nextIndex.getAndIncrement();
          
    if (index < 0) {
        
            nextIndex.decrementAndGet();
          
        throw new IllegalStateException("too many thread-local indexed variables");
    }
    return index;
}
```

可见，每个 ftl 实例以步长为 1 的递增序列，获取 index 值，这保证了 InternalThreadLocalMap 中数组的长度不会突增。

##### 2.4.2 get() 方法实现分析

```
public final V get() {
    InternalThreadLocalMap threadLocalMap = 
            InternalThreadLocalMap.get();
           // 1
    Object v = 
            threadLocalMap.indexedVariable(index);
           // 2
    if (v != 
            InternalThreadLocalMap.UNSET)
           {
        return (V) v;
    }

    V value = initialize(threadLocalMap); // 3
    registerCleaner(threadLocalMap);  // 4
    return value;
}
```

**1\. 先来看看 `              InternalThreadLocalMap.get()            ` 方法如何获取 threadLocalMap：**

```
=======================InternalThreadLocalMap=======================
public static InternalThreadLocalMap get() {
    Thread thread = 
            Thread.currentThread();
          
    if (thread instanceof FastThreadLocalThread) {
        return fastGet((FastThreadLocalThread) thread);
    } else {
        return slowGet();
    }
}

private static InternalThreadLocalMap fastGet(FastThreadLocalThread thread) {
    InternalThreadLocalMap threadLocalMap = 
            thread.threadLocalMap();
          
    if (threadLocalMap == null) {
        
            thread.setThreadLocalMap(threadLocalMap
           = new InternalThreadLocalMap());
    }
    return threadLocalMap;
}
```

因为结合 FastThreadLocalThread 使用才能发挥 FastThreadLocal 的性能优势，所以主要看 fastGet 方法。该方法直接从 ftlt 线程获取 threadLocalMap，还没有则创建一个 InternalThreadLocalMap 实例并设置进去，然后返回。

**2\. `              threadLocalMap.indexedVariable(index)            ` 就简单了，直接从数组获取值，然后返回：**

```
public Object indexedVariable(int index) {
    Object[] lookup = indexedVariables;
    return index < 
            lookup.length
           ? lookup[index] : UNSET;
}
```

**3\. 如果获取到的值不是 UNSET，那么是个有效的值，直接返回。如果是 UNSET，则初始化。**

`initialize(threadLocalMap)` 方法：

```
private V initialize(InternalThreadLocalMap threadLocalMap) {
    V v = null;
    try {
        v = initialValue();
    } catch (Exception e) {
        
            PlatformDependent.throwException(e);
          
    }

    
            threadLocalMap.setIndexedVariable(index,
           v); // 3-1
    addToVariablesToRemove(threadLocalMap, this); // 3-2
    return v;
}
```

3.1. 获取 ftl 的初始值，然后保存到 ftl 里的数组，如果数组长度不够则扩充数组长度，然后保存，不展开。

3.2. `addToVariablesToRemove(threadLocalMap, this)` 的实现，是将 ftl 实例保存在 threadLocalMap 内部数组第 0 个元素的 Set 集合中。

此处不贴代码，用图示如下：

![addToVariablesToRemove 存储结构图示](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/5b618294b9b8c100936fd13fd2202c32_MD5.png)

addToVariablesToRemove 存储结构图示

**4\. `registerCleaner(threadLocalMap)` 的实现， [netty-4.1.34](http://netty-4.1.34) 版本中的源码：**

```
private void registerCleaner(final InternalThreadLocalMap threadLocalMap) {
    Thread current = 
            Thread.currentThread();
          
    if (
            FastThreadLocalThread.willCleanupFastThreadLocals(current)
           || 
            threadLocalMap.isCleanerFlagSet(index))
           {
        return;
    }

    
            threadLocalMap.setCleanerFlag(index);
          

    // TODO: We need to find a better way to handle this.
    /*
    // We will need to ensure we will trigger remove(InternalThreadLocalMap) so everything will be released
    // and 
            FastThreadLocal.onRemoval(...)
           will be called.
    
            ObjectCleaner.register(current,
           new Runnable() {
        @Override
        public void run() {
            remove(threadLocalMap);

            // It's fine to not call 
            InternalThreadLocalMap.remove()
           here as this will only be triggered once
            // the Thread is collected by GC. In this case the ThreadLocal will be gone away already.
        }
    });
    */
}
```

由于 [ObjectCleaner.register](http://objectcleaner.register/) 这段代码在该版本已经注释掉，而余下逻辑比较简单，因此不再做分析。

### 2.5 普通线程使用 ftl 的性能退化

随着 `get()` 方法分析完毕， `set(value)` 方法原理也呼之欲出，限于篇幅，不再单独分析。

前文说过，ftl 要结合 ftlt 才能最大地发挥其性能，如果是其他的普通线程，就会退化到 jdk 的 ThreadLocal 的情况，因为普通线程没有包含 InternalThreadLocalMap 这样的数据结构，接下来我们看如何退化。

从 InternalThreadLocalMap 的 `get()` 方法看起：

```
=======================InternalThreadLocalMap=======================
public static InternalThreadLocalMap get() {
    Thread thread = 
            Thread.currentThread();
          
    if (thread instanceof FastThreadLocalThread) {
        return fastGet((FastThreadLocalThread) thread);
    } else {
        return slowGet();
    }
}

private static InternalThreadLocalMap slowGet() {
    // 父类的类型为jdk ThreadLocald的静态属性，从该threadLocal获取InternalThreadLocalMap
    ThreadLocal slowThreadLocalMap = 
            UnpaddedInternalThreadLocalMap.slowThreadLocalMap;
          
    InternalThreadLocalMap ret = 
            slowThreadLocalMap.get();
          
    if (ret == null) {
        ret = new InternalThreadLocalMap();
        
            slowThreadLocalMap.set(ret);
          
    }
    return ret;
}
```

从 ftl 看，退化操作的整个流程是：从一个 jdk 的 ThreadLocal 变量中获取 InternalThreadLocalMap，然后再从 InternalThreadLocalMap 获取指定数组下标的值，对象关系示意图：

![普通线程使用 ftl 的对象关系示意图](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/657ede8d4762334a21fa95e28113bed3_MD5.png)

普通线程使用 ftl 的对象关系示意图

## 3 ftl 的资源回收机制

在 netty 中对于 ftl 提供了三种回收机制：

**自动：** 使用 ftlt 执行一个被 FastThreadLocalRunnable wrap 的 Runnable 任务，在任务执行完毕后会自动进行 ftl 的清理。

**手动：** ftl 和 InternalThreadLocalMap 都提供了 remove 方法，在合适的时候用户可以（有的时候也是必须，例如普通线程的线程池使用 ftl）手动进行调用，进行显示删除。

**自动：** 为当前线程的每一个 ftl 注册一个 Cleaner，当线程对象不强可达的时候，该 Cleaner 线程会将当前线程的当前 ftl 进行回收。（netty 推荐如果可以用其他两种方式，就不要再用这种方式，因为需要另起线程，耗费资源，而且多线程就会造成一些资源竞争，在 [netty-4.1.34](http://netty-4.1.34) 版本中，已经注释掉了调用 ObjectCleaner 的代码。）

## 4 ftl 在 netty 中的使用

ftl 在 netty 中最重要的使用，就是分配 ByteBuf。基本做法是：每个线程都分配一块内存(PoolArena)，当需要分配 ByteBuf 时，线程先从自己持有的 PoolArena 分配，如果自己无法分配，再采用全局分配。

但是由于内存资源有限，所以还是会有多个线程持有同一块 PoolArena 的情况。不过这种方式已经最大限度地减轻了多线程的资源竞争，提高程序效率。

具体的代码在 **PoolByteBufAllocator 的内部类 PoolThreadLocalCache 中：**

```
final class PoolThreadLocalCache extends FastThreadLocal<PoolThreadCache> {

    @Override
    protected synchronized PoolThreadCache initialValue() {
        final PoolArena<byte[]> heapArena = leastUsedArena(heapArenas);
        final PoolArena<ByteBuffer> directArena = leastUsedArena(directArenas);

        Thread current = 
            Thread.currentThread();
          
        if (useCacheForAllThreads || current instanceof FastThreadLocalThread) {
            // PoolThreadCache即为各个线程持有的内存块的封装
            return new PoolThreadCache(
                    heapArena, directArena, tinyCacheSize, smallCacheSize, normalCacheSize,
                    DEFAULT_MAX_CACHED_BUFFER_CAPACITY, DEFAULT_CACHE_TRIM_INTERVAL);
        }
        // No caching so just use 0 as sizes.
        return new PoolThreadCache(heapArena, directArena, 0, 0, 0, 0, 0);
    }
}
```

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E5%90%8A%E6%89%93%20ThreadLocal%EF%BC%8C%E8%B0%88%E8%B0%88FastThreadLocal%E4%B8%BA%E5%95%A5%E8%83%BD%E8%BF%99%E4%B9%88%E5%BF%AB%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 面试官：Elasticsearch 支持事务吗？为什么？3. 新一代可视化拖拽式数据流平台4. 面试官：倒排索引是什么？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

Java 面试题 | 八股文汇总 · 目录

阅读原文