---
source_url: "https://mp.weixin.qq.com/s/FG9CfKk8rDuUHCVBRhtr3A"
title: "LatchUtils：简化 Java 异步任务同步的利器"
account: "小哈学Java"
published_at: "2026-10-25 15:55:01"
saved_at: "2026-10-26 07:35:09"
sync_id: "art_d233659bb21b40e8ba405f9c7a30d340"
parse_status: "ok"
---

# LatchUtils：简化 Java 异步任务同步的利器

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](https://mmbiz.qpic.cn/mmbiz_png/pUq1tpL9smoIibDjVfxeecWd8HJIGqu3Rq0wabByhRMhYnQU1MptjAhw7bO82TGjAgpHibvj4ib6zV9Ygc47EgyxvfezZ2F23AtFHKcIctkuao/640?wx_fmt=png&from=appmsg)

来源：网络

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- 详细代码
- 核心思想
- API 概览
- 实战示例
- 对比：如果不使用 LatchUtils
- 对比分析

在 Java 应用开发中，为了提升系统性能和响应速度，我们经常需要将一些耗时操作（如调用外部 API、查询数据库、复杂计算等）进行异步并行处理。当主流程需要等待所有这些并行任务执行完毕后再继续时，我们通常会用到  `ExecutorService` 、 `CountDownLatch`  等并发工具。

然而，直接使用这些原生工具，往往意味着需要编写一些重复的、模式化的“胶水代码”，这不仅增加了代码量，也让核心业务逻辑显得不够清晰。

为了解决这个问题，我封装了一个名为  `LatchUtils`  的轻量级工具类。它能够以一种极其简洁的方式来组织和管理这一类异步任务。

## 详细代码

其代码如下，后面会有使用说明和示例以及和传统实现代码的对比

```
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Executor;
import java.util.concurrent.TimeUnit;

publicclass LatchUtils {

    privatestaticfinal ThreadLocal<List<TaskInfo>> THREADLOCAL = ThreadLocal.withInitial(LinkedList::new);

    public static void submitTask(Executor executor, Runnable runnable) {
        THREADLOCAL.get().add(new TaskInfo(executor, runnable));
    }

    private static List<TaskInfo> popTask() {
        List<TaskInfo> taskInfos = THREADLOCAL.get();
        THREADLOCAL.remove();
        return taskInfos;
    }

    public static boolean waitFor(long timeout, TimeUnit timeUnit) {
        List<TaskInfo> taskInfos = popTask();
        if (taskInfos.isEmpty()) {
            returntrue;
        }
        CountDownLatch latch = new CountDownLatch(taskInfos.size());
        for (TaskInfo taskInfo : taskInfos) {
            Executor executor = taskInfo.executor;
            Runnable runnable = taskInfo.runnable;
            executor.execute(() -> {
                try {
                    runnable.run();
                } finally {
                    latch.countDown();
                }
            });
        }
        boolean await = false;
        try {
            await = latch.await(timeout, timeUnit);
        } catch (Exception ignored) {
        }
        return await;
    }

    privatestaticfinalclass TaskInfo {
        privatefinal Executor executor;
        privatefinal Runnable runnable;

        public TaskInfo(Executor executor, Runnable runnable) {
            this.executor = executor;
            this.runnable = runnable;
        }
    }
}
```

## 核心思想

 `LatchUtils`  的设计哲学是：多次提交，一次等待。

- 任务注册： 在主流程代码中，可以先通过  `LatchUtils.submitTask()`  提交 Runnable 任务和其对应的 Executor（该线程池用来执行这个 Runnable）。
- 执行并等待： 当并行任务都提交完毕后，你只需调用一次  `LatchUtils.waitFor()`  。该方法会立即触发所有已注册任务的执行，并阻塞等待所有任务执行完成或超时。

## API 概览

这个工具类对外暴露的接口极其简单，只有两个核心静态方法：

#### submitTask()

```
public static void submitTask(Executor executor, Runnable runnable)
```

**功能：** 提交一个异步任务。

**参数：**

- executor：  `java.util.concurrent.Executor`  - 指定执行此任务的线程池。
- runnable：  `java.lang.Runnable`  - 需要异步执行的具体业务逻辑。

#### waitFor()

```
public static boolean waitFor(long timeout, TimeUnit timeUnit)
```

**功能：** 触发所有已提交任务的执行，并同步等待它们全部完成。

**参数：**

- timeout：  `long`  - 最长等待时间。
- timeUnit：  `java.util.concurrent.TimeUnit`  - 等待时间单位。

**返回值：**

- true： 如果所有任务在指定时间内成功完成。
- false： 如果等待超时。

**注意：** 该方法在执行后会自动清理当前线程提交的任务列表，因此可以重复使用。

## 实战示例

让我们来看一个典型的应用场景：一个聚合服务需要同时调用用户服务、订单服务和商品服务，拿到所有结果后再进行下一步处理。

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

publicclass Main {

    public static void main(String[] args) {
        // 1. 准备一个线程池
        ExecutorService executorService = Executors.newFixedThreadPool(3);

        System.out.println("主流程开始，准备分发异步任务...");

        // 2. 提交多个异步任务
        // 任务一：获取用户信息
        LatchUtils.submitTask(executorService, () -> {
            try {
                System.out.println("开始获取用户信息...");
                Thread.sleep(1000); // 模拟耗时
                System.out.println("获取用户信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // 任务二：获取订单信息
        LatchUtils.submitTask(executorService, () -> {
            try {
                System.out.println("开始获取订单信息...");
                Thread.sleep(1500); // 模拟耗时
                System.out.println("获取订单信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        // 任务三：获取商品信息
        LatchUtils.submitTask(executorService, () -> {
            try {
                System.out.println("开始获取商品信息...");
                Thread.sleep(500); // 模拟耗时
                System.out.println("获取商品信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        System.out.println("所有异步任务已提交，主线程开始等待...");

        // 3. 等待所有任务完成，最长等待5秒
        boolean allTasksCompleted = LatchUtils.waitFor(5, TimeUnit.SECONDS);

        // 4. 根据等待结果继续主流程
        if (allTasksCompleted) {
            System.out.println("所有异步任务执行成功，主流程继续...");
        } else {
            System.err.println("有任务执行超时，主流程中断！");
        }

        // 5. 关闭线程池
        executorService.shutdown();
    }
}
```

输出结果：

```
主流程开始，准备分发异步任务...
所有异步任务已提交，主线程开始等待...
开始获取商品信息...
开始获取用户信息...
开始获取订单信息...
获取商品信息成功！
获取用户信息成功！
获取订单信息成功！
所有异步任务执行成功，主流程继续...
```

从这个例子中可以看到，业务代码变得非常清晰。我们只需要关注“提交任务”和“等待结果”这两个动作，而无需关心  `CountDownLatch`  的初始化、 `countDown()`  的调用以及异常处理等细节。

## 对比：如果不使用 LatchUtils

为了更好地理解  `LatchUtils`  带来的价值，让我们看看要实现与上面完全相同的功能，用传统的 Java 并发 API 需要如何编写代码。通常有两种主流方式：使用  `CountDownLatch`  或使用  `CompletableFuture` 。

#### 方式一：直接使用 CountDownLatch

这是最经典的方式，开发者需要手动管理  `CountDownLatch`  的生命周期。

```
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

publicclass ManualCountDownLatchExample {

    public static void main(String[] args) {
        // 1. 准备一个线程池
        ExecutorService executorService = Executors.newFixedThreadPool(3);

        // 2. 手动初始化 CountDownLatch，数量为任务数
        CountDownLatch latch = new CountDownLatch(3);

        System.out.println("主流程开始，准备分发异步任务...");

        // 3. 提交任务，并在每个任务的 finally 块中手动调用 latch.countDown()
        // 任务一：获取用户信息
        executorService.execute(() -> {
            try {
                System.out.println("开始获取用户信息...");
                Thread.sleep(1000);
                System.out.println("获取用户信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown(); // 手动减一
            }
        });

        // 任务二：获取订单信息
        executorService.execute(() -> {
            try {
                System.out.println("开始获取订单信息...");
                Thread.sleep(1500);
                System.out.println("获取订单信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown(); // 手动减一
            }
        });

        // 任务三：获取商品信息
        executorService.execute(() -> {
            try {
                System.out.println("开始获取商品信息...");
                Thread.sleep(500);
                System.out.println("获取商品信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                latch.countDown(); // 手动减一
            }
        });

        System.out.println("所有异步任务已提交，主线程开始等待...");

        // 4. 手动调用 latch.await() 进行等待
        boolean allTasksCompleted = false;
        try {
            allTasksCompleted = latch.await(5, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            // 需要处理中断异常
            Thread.currentThread().interrupt();
            System.err.println("主线程在等待时被中断！");
        }

        // 5. 根据等待结果继续主流程
        if (allTasksCompleted) {
            System.out.println("所有异步任务执行成功，主流程继续...");
        } else {
            System.err.println("有任务执行超时，主流程中断！");
        }

        // 6. 关闭线程池
        executorService.shutdown();
    }
}
```

#### 方式二：使用 CompletableFuture

使用  `CompletableFuture`  实现，其代码如下

```
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

publicclass CompletableFutureExample {

    public static void main(String[] args) {
        // 1. 准备一个线程池
        ExecutorService executorService = Executors.newFixedThreadPool(3);

        System.out.println("主流程开始，准备分发异步任务...");

        // 2. 创建 CompletableFuture 任务
        CompletableFuture<Void> userFuture = CompletableFuture.runAsync(() -> {
            try {
                System.out.println("开始获取用户信息...");
                Thread.sleep(1000);
                System.out.println("获取用户信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }, executorService);

        CompletableFuture<Void> orderFuture = CompletableFuture.runAsync(() -> {
            try {
                System.out.println("开始获取订单信息...");
                Thread.sleep(1500);
                System.out.println("获取订单信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }, executorService);

        CompletableFuture<Void> productFuture = CompletableFuture.runAsync(() -> {
            try {
                System.out.println("开始获取商品信息...");
                Thread.sleep(500);
                System.out.println("获取商品信息成功！");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }, executorService);

        System.out.println("所有异步任务已提交，主线程开始等待...");

        // 3. 使用 CompletableFuture.allOf 将所有任务组合起来
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(userFuture, orderFuture, productFuture);

        // 4. 等待组合后的 Future 完成
        try {
            allFutures.get(5, TimeUnit.SECONDS);
            System.out.println("所有异步任务执行成功，主流程继续...");
        } catch (Exception e) {
            // 需要处理多种异常，如 InterruptedException, ExecutionException, TimeoutException
            System.err.println("任务执行超时或出错，主流程中断！ " + e.getMessage());
        }

        // 5. 关闭线程池
        executorService.shutdown();
    }
}
```

## 对比分析

| 特性 | LatchUtils | 手动 CountDownLatch | CompletableFuture.allOf |
| --- | --- | --- | --- |
| 代码简洁性 | ** 极高 ** 。业务逻辑和并发控制分离，核心代码清晰。 | ** 中等 ** 。需要在每个任务中嵌入 latch.countDown()，分散了关注点。 | ** 较高 ** 。链式调用风格，但需要创建多个 Future 对象。 |
| 状态管理 | ** 自动 ** 。工具类内部自动管理 CountDownLatch。 | ** 手动 ** 。需要自己创建、维护和传递 CountDownLatch 实例。 | ** 自动 ** 。由 CompletableFuture 框架管理任务状态。 |
| 错误处理 | ** 简化 ** 。waitFor 内部处理 InterruptedException，仅返回布尔值。 | ** 复杂 ** 。需要显式地在 finally 中 countDown()，并为主线程的 await() 处理 InterruptedException。 | ** 复杂 ** 。get() 方法会抛出多种受检异常，需要统一处理。 |
| 关注点分离 | ** 优秀 ** 。开发者只需关注“提交”和“等待”两个动作。 | ** 一般 ** 。并发控制逻辑（countDown()）侵入到了业务 Runnable 中。 | ** 良好 ** 。任务的定义和组合是分开的，但仍需处理组合后的 Future。 |
| 易用性 | ** 非常简单 ** 。几乎没有学习成本。 | ** 需要理解 CountDownLatch ** 。容易忘记 countDown() 或错误处理。 | ** 需要理解 CompletableFuture ** 。API 较为丰富，有一定学习曲线。 |

##### 结论很明显：

对于“分发一组并行任务，然后等待它们全部完成”这一特定但常见的模式，LatchUtils 通过适度的封装，极大地简化了开发者的工作。它隐藏了并发控制的复杂性，让业务代码回归其本质，从而提高了代码的可读性和可维护性。

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI 2.x + Spring Boot 4.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&retryload=1&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/knmrNHnmCLEdM2gtRgy5eLztKXrUhee76MZ9wAicNPicsnAHPibicaSHUVqFkkibxWlrGO0acUxQmycZpqCNGcibaicxA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=6)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 网易二面：CPU狂飙900%，该怎么处理？
3. 面试官：Kafka 如何实现顺序消费？
4. 比 VMware 更快，更轻的虚拟机，横空出世！
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢啦
```

---
原文链接：https://mp.weixin.qq.com/s/FG9CfKk8rDuUHCVBRhtr3A
