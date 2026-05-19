---
title: CompletableFuture的使用
tags:
  - JAVA
categories:
  - JAVA
date: 2023-11-13 11:28:52
---

# CompletableFuture的使用

之前在java开发过程中，之前在使用多线程的时候都是使用`Runable` 、`Future` 、 `Thread` 、`ExecutorService`、`Callable` 这些，但是后续发现这些写法在一些特殊的场景下使用还是有些许的不方便，直到之前在一个循环调用一个接口时，发现这个调用时间太长了，在没有什么好办法的时候想起了多线程去调用，但是之前写实现类和继承的方式多多少少有些麻烦，在有主要是 **Thread+Runnable** 来完成，但是这种方式有个弊端就是没有返回值。如果想要返回值怎么办呢，大多数人就会想到 **`Callable + Thread`** 的方式来获取到返回值。如下：

```java
public class TestCompletable {
    public static void main(String[] args) throws Exception {

        FutureTask<String> task = new FutureTask((Callable<String>) () -> {
            TimeUnit.SECONDS.sleep(2);
            return UUID.randomUUID().toString();
        });
        new Thread(task).start();
        String s = task.get();
        System.out.println(s);
    }
}
```

从运行上面代码可以知道当调用代码 `String s = task.get();` 的时候，当前主线程是阻塞状态，另一种方式获取到返回值就是通过轮询 `task.isDone()` 来判断任务是否做完获取返回值。因此JDK8之前提供的异步能力有一定的局限性：

- Runnable+Thread虽然提供了多线程的能力但是没有返回值。
- Callable+Thread的方法提供多线程和返回值的能力但是在获取返回值的时候会阻塞主线程。
- ![image-20231114105951895](image-20231114105951895.png)

所以上述的情况只适合不关心返回值，只要提交的Task执行了就可以。另外的就是能够容忍等待。因此我们需要更大的异步能力为了去解决这些痛点问题。比如一下场景：

- 两个Task计算合并为一个，这两个异步计算之间相互独立，但是两者之前又有依赖关系。
- 对于多个Task,只要一个任务返回了结果就返回结果

等等其他的一些负载的场景， JDK8 就引入了 **`CompletableFuture`**

## CompletableFuture与Future的关系

**`CompletableFuture`** 实现了 **`Future`** 接口和 **`CompletionStage`** 。因此 CompletableFuture是对 Futrue的功能增强包含了Future的功能。从继承的另一个 **`CompletionStage`** 的名称来看完成阶段性的接口。这个怎么理解，这个就是下面要说的CompletableFuture本质。

`Future`的局限性，它没法直接对多个任务进行链式、组合等处理，需要借助并发工具类才能完成，实现逻辑比较复杂。

而`CompletableFuture`是对Future的扩展和增强。`CompletableFuture`实现了`Future`接口，并在此基础上进行了丰富的扩展，完美弥补了`Future`的局限性，同时`CompletableFuture`实现了对任务编排的能力。借助这项能力，可以轻松地组织不同任务的运行顺序、规则以及方式。从某种程度上说，这项能力是它的核心能力。而在以往，虽然通过`CountDownLatch`等工具类也可以实现任务的编排，但需要复杂的逻辑处理，不仅耗费精力且难以维护。

`CompletionStage`接口定义了任务编排的方法，执行某一阶段，可以向下执行后续阶段。**异步执行的，默认线程池是`ForkJoinPool.commonPool()`，但为了业务之间互不影响，且便于定位问题，强烈推荐使用自定义线程池**。

CompletableFuture中默认线程池如下：

```java
// 根据commonPool的并行度来选择,而并行度的计算是在ForkJoinPool的静态代码段完成的
private static final boolean useCommonPool =
    (ForkJoinPool.getCommonPoolParallelism() > 1);

private static final Executor asyncPool = useCommonPool ?
    ForkJoinPool.commonPool() : new ThreadPerTaskExecutor();
```

`ForkJoinPool`中初始化`commonPool`的参数

```java
static {
    // initialize field offsets for CAS etc
    try {
        U = sun.misc.Unsafe.getUnsafe();
        Class<?> k = ForkJoinPool.class;
        CTL = U.objectFieldOffset
            (k.getDeclaredField("ctl"));
        RUNSTATE = U.objectFieldOffset
            (k.getDeclaredField("runState"));
        STEALCOUNTER = U.objectFieldOffset
            (k.getDeclaredField("stealCounter"));
        Class<?> tk = Thread.class;
        ……
    } catch (Exception e) {
        throw new Error(e);
    }

    commonMaxSpares = DEFAULT_COMMON_MAX_SPARES;
    defaultForkJoinWorkerThreadFactory =
        new DefaultForkJoinWorkerThreadFactory();
    modifyThreadPermission = new RuntimePermission("modifyThread");

    // 调用makeCommonPool方法创建commonPool,其中并行度为逻辑核数-1
    common = java.security.AccessController.doPrivileged
        (new java.security.PrivilegedAction<ForkJoinPool>() {
            public ForkJoinPool run() { return makeCommonPool(); }});
    int par = common.config & SMASK; // report 1 even if threads disabled
    commonParallelism = par > 0 ? par : 1;
}
```

## 常用方法

### 依赖关系

- `thenApply()`：把前面任务的执行结果，交给后面的`Function`
- `thenCompose()`：用来连接两个有依赖关系的任务，结果由第二个任务返回

### and集合关系

- `thenCombine()`：合并任务，有返回值
- `thenAccepetBoth()`：两个任务执行完成后，将结果交给`thenAccepetBoth`处理，无返回值
- `runAfterBoth()`：两个任务都执行完成后，执行下一步操作(`Runnable`类型任务)

### or聚合关系

- `applyToEither()`：两个任务哪个执行的快，就使用哪一个结果，有返回值
- `acceptEither()`：两个任务哪个执行的快，就消费哪一个结果，无返回值
- `runAfterEither()`：任意一个任务执行完成，进行下一步操作(`Runnable`类型任务)

### 并行执行

- `allOf()`：当所有给定的 CompletableFuture 完成时，返回一个新的 CompletableFuture
- `anyOf()`：当任何一个给定的`CompletablFuture`完成时，返回一个新的CompletableFuture

### 结果处理

- `whenComplete`：当任务完成时，将使用结果(或 null)和此阶段的异常(或 null如果没有)执行给定操作

- `exceptionally`：返回一个新的`CompletableFuture`，当前面的`CompletableFuture`完成时，它也完成，当它异常完成时，给定函数的异常触发这个`CompletableFuture`的完成

### 异步操作

`CompletableFuture`提供了四个静态方法来创建一个异步操作：

```java
public static CompletableFuture<Void> runAsync(Runnable runnable)
public static CompletableFuture<Void> runAsync(Runnable runnable, Executor executor)
public static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier)
public static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier, Executor executor)
```

这四个方法的区别：

- `runAsync()` 以`Runnable`函数式接口类型为参数，没有返回结果，`supplyAsync()` 以`Supplier`函数式接口类型为参数，返回结果类型为U；Supplier接口的 `get()`是有返回值的(会阻塞)

- 使用没有指定`Executor`的方法时，内部使用`ForkJoinPool.commonPool()` 作为它的线程池执行异步代码。如果指定线程池，则使用指定的线程池运行。

- 默认情况下`CompletableFuture`会使用公共的`ForkJoinPool`线程池，这个线程池默认创建的线程数是 CPU 的核数（也可以通过 `JVM option:-Djava.util.concurrent.ForkJoinPool.common.parallelism` 来设置`ForkJoinPool`线程池的线程数）。**如果所有`CompletableFuture`共享一个线程池，那么一旦有任务执行一些很慢的 I/O 操作，就会导致线程池中所有线程都阻塞在 I/O 操作上，从而造成线程饥饿，进而影响整个系统的性能。所以，强烈建议你要根据不同的业务类型创建不同的线程池，以避免互相干扰**

### 获取结果

`join()和get()方法都是用来获取CompletableFuture异步之后的返回值`。join()方法抛出的是uncheck异常（即未经检查的异常),不会强制开发者抛出,但是绝大多数时RuntimeException。get()方法抛出的是经过检查的异常，ExecutionException, InterruptedException 需要用户手动处理（抛出或者 try catch）

### 结果处理

当[CompletableFuture](https://so.csdn.net/so/search?q=CompletableFuture&spm=1001.2101.3001.7020)的计算结果完成，或者抛出异常的时候，我们可以执行特定的 Action。主要是下面的方法：

```java
public CompletableFuture<T> whenComplete(BiConsumer<? super T,? super Throwable> action)
public CompletableFuture<T> whenCompleteAsync(BiConsumer<? super T,? super Throwable> action)
public CompletableFuture<T> whenCompleteAsync(BiConsumer<? super T,? super Throwable> action, Executor executor)
```

- `Action`的类型是`BiConsumer<? super T,? super Throwable>`，它可以处理正常的计算结果，或者异常情况。

- 方法不以`Async`结尾，意味着Action使用相同的线程执行，而`Async`可能会使用其它的线程去执行(如果使用相同的线程池，也可能会被同一个线程选中执行)。

- 这几个方法都会返回`CompletableFuture`，当Action执行完毕后它的结果返回原始的CompletableFuture的计算结果或者返回异常

```java
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
    }
    if (new Random().nextInt(10) % 2 == 0) {
        int i = 12 / 0;
    }
    System.out.println("执行结束！");
    return "test";
});
// 任务完成或异常方法完成时执行该方法
// 如果出现了异常,任务结果为null
future.whenComplete(new BiConsumer<String, Throwable>() {
    @Override
    public void accept(String t, Throwable action) {
        System.out.println(t+" 执行完成！");
    }
});
// 出现异常时先执行该方法
future.exceptionally(new Function<Throwable, String>() {
    @Override
    public String apply(Throwable t) {
        System.out.println("执行失败：" + t.getMessage());
        return "异常xxxx";
    }
});

future.get();
```

上面的代码当出现异常时，输出结果如下

```
执行失败：java.lang.ArithmeticException: / by zero
null 执行完成！
```

## 应用场景

### 结果转换

##### thenApply

`thenApply`接收一个函数作为参数，使用该函数处理上一个`CompletableFuture`调用的结果，并返回一个具有处理结果的`Future`对象。

常用使用：

```java
public <U> CompletableFuture<U> thenApply(Function<? super T,? extends U> fn)
public <U> CompletableFuture<U> thenApplyAsync(Function<? super T,? extends U> fn)
```

具体使用：

```java
CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
    int result = 100;
    System.out.println("第一次运算：" + result);
    return result;
}).thenApply(number -> {
    int result = number * 3;
    System.out.println("第二次运算：" + result);
    return result;
});
```

##### thenCompose

`thenCompose`的参数为一个返回`CompletableFuture`实例的函数，该函数的参数是先前计算步骤的结果。

常用方法：

```java
public <U> CompletableFuture<U> thenCompose(Function<? super T, ? extends CompletionStage<U>> fn);
public <U> CompletableFuture<U> thenComposeAsync(Function<? super T, ? extends CompletionStage<U>> fn) ;
```

具体使用：

```java
CompletableFuture<Integer> future = CompletableFuture
    .supplyAsync(new Supplier<Integer>() {
        @Override
        public Integer get() {
            int number = new Random().nextInt(30);
            System.out.println("第一次运算：" + number);
            return number;
        }
    })
    .thenCompose(new Function<Integer, CompletionStage<Integer>>() {
        @Override
        public CompletionStage<Integer> apply(Integer param) {
            return CompletableFuture.supplyAsync(new Supplier<Integer>() {
                @Override
                public Integer get() {
                    int number = param * 2;
                    System.out.println("第二次运算：" + number);
                    return number;
                }
            });
        }
    });
```

**thenApply 和 thenCompose的区别**：

- `thenApply`转换的是泛型中的类型，返回的是同一个`CompletableFuture`；

- `thenCompose`将内部的`CompletableFuture`调用展开来并使用上一个`CompletableFutre`调用的结果在下一步的`CompletableFuture`调用中进行运算，是生成一个新的`CompletableFuture`。

### 结果消费

与**结果处理**和**结果转换**系列函数返回一个新的`CompletableFuture`不同，结果消费系列函数只对结果执行`Action`，而不返回新的计算值。

根据对结果的处理方式，结果消费函数又可以分为下面三大类：

- `thenAccept()`：对单个结果进行消费
- `thenAcceptBoth()`：对两个结果进行消费
- `thenRun()`：不关心结果，只对结果执行`Action`

##### thenAccept

观察该系列函数的参数类型可知，它们是函数式接口Consumer，这个接口只有输入，没有返回值。

常用方法：

```java
public CompletionStage<Void> thenAccept(Consumer<? super T> action);
public CompletionStage<Void> thenAcceptAsync(Consumer<? super T> action);
```

具体使用：

```java
CompletableFuture<Void> future = CompletableFuture
    .supplyAsync(() -> {
        int number = new Random().nextInt(10);
        System.out.println("第一次运算：" + number);
        return number;
    }).thenAccept(number ->
                  System.out.println("第二次运算：" + number * 5));
```

##### thenAcceptBoth

`thenAcceptBoth`函数的作用是，当两个`CompletionStage`都正常完成计算的时候，就会执行提供的`action`消费两个异步的结果。

常用方法：

```java
public <U> CompletionStage<Void> thenAcceptBoth(CompletionStage<? extends U> other,BiConsumer<? super T, ? super U> action);
public <U> CompletionStage<Void> thenAcceptBothAsync(CompletionStage<? extends U> other,BiConsumer<? super T, ? super U> action);
```

具体使用：

```java
CompletableFuture<Integer> futrue1 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(3) + 1;
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("任务1结果：" + number);
        return number;
    }
});

CompletableFuture<Integer> future2 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(3) + 1;
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("任务2结果：" + number);
        return number;
    }
});

futrue1.thenAcceptBoth(future2, new BiConsumer<Integer, Integer>() {
    @Override
    public void accept(Integer x, Integer y) {
        System.out.println("最终结果：" + (x + y));
    }
});
```

##### thenRun

`thenRun`也是对线程任务结果的一种消费函数，与`thenAccept`不同的是，`thenRun`会在上一阶段 `CompletableFuture`计算完成的时候执行一个`Runnable`，而`Runnable`并不使用该`CompletableFuture`计算的结果。

常用方法：

```java
public CompletionStage<Void> thenRun(Runnable action);
public CompletionStage<Void> thenRunAsync(Runnable action);
```

具体使用：

```java
CompletableFuture<Void> future = CompletableFuture.supplyAsync(() -> {
    int number = new Random().nextInt(10);
    System.out.println("第一阶段：" + number);
    return number;
}).thenRun(() ->
           System.out.println("thenRun 执行"));
```

### 结果组合

##### thenCombine

合并两个线程任务的结果，并进一步处理。

常用方法：

```java
public <U,V> CompletableFuture<V> thenCombine(CompletionStage<? extends U> other,BiFunction<? super T,? super U,? extends V> fn);

public <U,V> CompletableFuture<V> thenCombineAsync(CompletionStage<? extends U> other,BiFunction<? super T,? super U,? extends V> fn);

public <U,V> CompletableFuture<V> thenCombineAsync(CompletionStage<? extends U> other,BiFunction<? super T,? super U,? extends V> fn, Executor executor);
```

具体使用：

```java
CompletableFuture<Integer> future1 = CompletableFuture
    .supplyAsync(new Supplier<Integer>() {
        @Override
        public Integer get() {
            int number = new Random().nextInt(10);
            System.out.println("任务1结果：" + number);
            return number;
        }
    });
CompletableFuture<Integer> future2 = CompletableFuture
    .supplyAsync(new Supplier<Integer>() {
        @Override
        public Integer get() {
            int number = new Random().nextInt(10);
            System.out.println("任务2结果：" + number);
            return number;
        }
    });
CompletableFuture<Integer> result = future1
    .thenCombine(future2, new BiFunction<Integer, Integer, Integer>() {
        @Override
        public Integer apply(Integer x, Integer y) {
            return x + y;
        }
    });
System.out.println("组合后结果：" + result.get());
```

### 任务交互

线程交互指**将两个线程任务获取结果的速度相比较，按一定的规则进行下一步处理**。

##### applyToEither

两个线程任务相比较，先获得执行结果的，就对该结果进行下一步的转化操作。

常用方法：

```java
public <U> CompletionStage<U> applyToEither(CompletionStage<? extends T> other,Function<? super T, U> fn);
public <U> CompletionStage<U> applyToEitherAsync(CompletionStage<? extends T> other,Function<? super T, U> fn);
```

具体使用：

```java
CompletableFuture<Integer> future1 = CompletableFuture
    .supplyAsync(new Supplier<Integer>() {
        @Override
        public Integer get() {
            int number = new Random().nextInt(10);
            try {
                TimeUnit.SECONDS.sleep(number);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("任务1结果:" + number);
            return number;
        }
    });
CompletableFuture<Integer> future2 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(10);
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("任务2结果:" + number);
        return number;
    }
});

future1.applyToEither(future2, new Function<Integer, Integer>() {
    @Override
    public Integer apply(Integer number) {
        System.out.println("最快结果：" + number);
        return number * 2;
    }
});
```

##### acceptEither

两个线程任务相比较，先获得执行结果的，就对该结果进行下一步的消费操作。

常用方法:

```java
public CompletionStage<Void> acceptEither(CompletionStage<? extends T> other,Consumer<? super T> action);
public CompletionStage<Void> acceptEitherAsync(CompletionStage<? extends T> other,Consumer<? super T> action);
```

具体使用：

```java
CompletableFuture<Integer> future1 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(10) + 1;
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("第一阶段：" + number);
        return number;
    }
});

CompletableFuture<Integer> future2 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(10) + 1;
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("第二阶段：" + number);
        return number;
    }
});

future1.acceptEither(future2, new Consumer<Integer>() {
    @Override
    public void accept(Integer number) {
        System.out.println("最快结果：" + number);
    }
});

```

##### runAfterEither

两个线程任务相比较，有任何一个执行完成，就进行下一步操作，不关心运行结果。

常用方法：

```java
public CompletionStage<Void> runAfterEither(CompletionStage<?> other,Runnable action);
public CompletionStage<Void> runAfterEitherAsync(CompletionStage<?> other,Runnable action);
```

具体使用：

```java
CompletableFuture<Integer> future1 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(5);
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("任务1结果：" + number);
        return number;
    }
});

CompletableFuture<Integer> future2 = CompletableFuture.supplyAsync(new Supplier<Integer>() {
    @Override
    public Integer get() {
        int number = new Random().nextInt(5);
        try {
            TimeUnit.SECONDS.sleep(number);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("任务2结果:" + number);
        return number;
    }
});

future1.runAfterEither(future2, new Runnable() {
    @Override
    public void run() {
        System.out.println("已经有一个任务完成了");
    }
}).join();
```

##### anyOf

`anyOf() `的参数是多个给定的 `CompletableFuture`，当其中的任何一个完成时，方法返回这个 `CompletableFuture`。

常用方法：

```java
public static CompletableFuture<Object> anyOf(CompletableFuture<?>... cfs)
```

具体使用：

```java
Random random = new Random();
CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> {
    try {
        TimeUnit.SECONDS.sleep(random.nextInt(5));
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    return "hello";
});

CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> {
    try {
        TimeUnit.SECONDS.sleep(random.nextInt(1));
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    return "world";
});
CompletableFuture<Object> result = CompletableFuture.anyOf(future1, future2);
```

##### allOf

allOf方法用来实现多 CompletableFuture 的同时返回。

常用方法：

```java
public static CompletableFuture<Void> allOf(CompletableFuture<?>... cfs)
```

具体使用：

```java
CompletableFuture<String> future1 = CompletableFuture.supplyAsync(() -> {
    try {
        TimeUnit.SECONDS.sleep(2);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    System.out.println("future1完成！");
    return "future1完成！";
});

CompletableFuture<String> future2 = CompletableFuture.supplyAsync(() -> {
    System.out.println("future2完成！");
    return "future2完成！";
});

CompletableFuture<Void> combindFuture = CompletableFuture.allOf(future1, future2);

try {
    combindFuture.get();
} catch (InterruptedException e) {
    e.printStackTrace();
} catch (ExecutionException e) {
    e.printStackTrace();
}
```

![image-20231114112841694](image-20231114112841694.png)

## 使用案例

### **实现最优的“烧水泡茶”程序**

著名数学家华罗庚先生在《统筹方法》这篇文章里介绍了一个烧水泡茶的例子，文中提到最优的工序应该是下面这样：

![image-20231114112802621](image-20231114112802621.png)

对于烧水泡茶这个程序，一种最优的分工方案：用两个线程 T1 和 T2 来完成烧水泡茶程序，T1 负责洗水壶、烧开水、泡茶这三道工序，T2 负责洗茶壶、洗茶杯、拿茶叶三道工序，其中 T1 在执行泡茶这道工序时需要等待 T2 完成拿茶叶的工序。

### 基于Future实现

```java
public class FutureTaskTest{

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        // 创建任务T2的FutureTask
        FutureTask<String> ft2 = new FutureTask<>(new T2Task());
        // 创建任务T1的FutureTask
        FutureTask<String> ft1 = new FutureTask<>(new T1Task(ft2));

        // 线程T1执行任务ft2
        Thread T1 = new Thread(ft2);
        T1.start();
        // 线程T2执行任务ft1
        Thread T2 = new Thread(ft1);
        T2.start();
        // 等待线程T1执行结果
        System.out.println(ft1.get());

    }
}

// T1Task需要执行的任务：
// 洗水壶、烧开水、泡茶
class T1Task implements Callable<String> {
    FutureTask<String> ft2;
    // T1任务需要T2任务的FutureTask
    T1Task(FutureTask<String> ft2){
        this.ft2 = ft2;
    }
    @Override
    public String call() throws Exception {
        System.out.println("T1:洗水壶...");
        TimeUnit.SECONDS.sleep(1);

        System.out.println("T1:烧开水...");
        TimeUnit.SECONDS.sleep(15);
        // 获取T2线程的茶叶
        String tf = ft2.get();
        System.out.println("T1:拿到茶叶:"+tf);

        System.out.println("T1:泡茶...");
        return "上茶:" + tf;
    }
}
// T2Task需要执行的任务:
// 洗茶壶、洗茶杯、拿茶叶
class T2Task implements Callable<String> {
    @Override
    public String call() throws Exception {
        System.out.println("T2:洗茶壶...");
        TimeUnit.SECONDS.sleep(1);

        System.out.println("T2:洗茶杯...");
        TimeUnit.SECONDS.sleep(2);

        System.out.println("T2:拿茶叶...");
        TimeUnit.SECONDS.sleep(1);
        return "龙井";
    }
}
```

### 基于CompletableFuture实现

```
public class CompletableFutureTest {

    public static void main(String[] args) {

        //任务1：洗水壶->烧开水
        CompletableFuture<Void> f1 = CompletableFuture
            .runAsync(() -> {
                System.out.println("T1:洗水壶...");
                sleep(1, TimeUnit.SECONDS);

                System.out.println("T1:烧开水...");
                sleep(15, TimeUnit.SECONDS);
            });
        //任务2：洗茶壶->洗茶杯->拿茶叶
        CompletableFuture<String> f2 = CompletableFuture
            .supplyAsync(() -> {
                System.out.println("T2:洗茶壶...");
                sleep(1, TimeUnit.SECONDS);

                System.out.println("T2:洗茶杯...");
                sleep(2, TimeUnit.SECONDS);

                System.out.println("T2:拿茶叶...");
                sleep(1, TimeUnit.SECONDS);
                return "龙井";
            });
        //任务3：任务1和任务2完成后执行：泡茶
        CompletableFuture<String> f3 = f1.thenCombine(f2, (__, tf) -> {
            System.out.println("T1:拿到茶叶:" + tf);
            System.out.println("T1:泡茶...");
            return "上茶:" + tf;
        });
        //等待任务3执行结果
        System.out.println(f3.join());
    }

    static void sleep(int t, TimeUnit u){
        try {
            u.sleep(t);
        } catch (InterruptedException e) {
        }
    }
}
```

文章转载摘抄至：

[CompletableFuture使用详解_sermonlizhi的博客-CSDN博客](https://blog.csdn.net/sermonlizhi/article/details/123356877)

[CompletableFuture详解 (baidu.com)](https://baijiahao.baidu.com/s?id=1739828295604310156&wfr=spider&for=pc)

