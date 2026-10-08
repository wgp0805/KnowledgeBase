---
source_url: "https://mp.weixin.qq.com/s/0L58hIOdz0nUSTnMq8H2iw"
title: "消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思"
account: "小哈学Java"
published_at: "2026-10-01 21:39:11"
saved_at: "2026-10-02 09:18:13"
sync_id: "art_32f4c9e6583c487b97af0c26d7fb64e7"
parse_status: "ok"
---

# 消息重试框架 Spring-Retry 和 Guava-Retry，这个框架有点意思

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![Spring-Retry 和 Guava-Retry](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/debd53dc9428e823b405d280077d3b7e_MD5.webp)

来源：blog.csdn.net/zzzgd_666/article/details/84377962

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- 一 重试框架之 Spring-Retry
- 1.Spring-Retry 的普通使用方式
- 2.Spring-Retry 的注解使用方式

- 二 重试框架之 Guava-Retry
- 总结

## 一 重试框架之 Spring-Retry

Spring Retry 为 Spring 应用程序提供了声明性重试支持。它用于 Spring 批处理、Spring 集成、Apache Hadoop(等等)。它主要是针对可能抛出异常的一些调用操作，进行有策略的重试

### 1. Spring-Retry 的普通使用方式

#### 1. 准备工作

我们只需要加上依赖:

```
<dependency>
    <groupId>org.springframework.retry</groupId>
    <artifactId>spring-retry</artifactId>
    <version>1.2.2.RELEASE</version>
</dependency>
```

准备一个任务方法，我这里是采用一个随机整数，根据不同的条件返回不同的值，或者抛出异常

```
package com.zgd.demo.thread.retry;

import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.RandomUtils;
import org.springframework.remoting.RemoteAccessException;

/**
 * @Author: zgd
 * @Description:
 */
@Slf4j
public class RetryDemoTask {

  /**
   * 重试方法
   * @return
   */
  public static boolean retryTask(String param)  {
    log.info("收到请求参数:{}",param);

    int i = RandomUtils.nextInt(0,11);
    log.info("随机生成的数:{}",i);
    if (i == 0) {
      log.info("为0,抛出参数异常.");
      throw new IllegalArgumentException("参数异常");
    }elseif (i == 1){
      log.info("为1,返回true.");
      returntrue;
    }elseif (i == 2){
      log.info("为2,返回false.");
      returnfalse;
    }else{
      //为其他
      log.info("大于2,抛出自定义异常.");
      throw new RemoteAccessException("大于2,抛出远程访问异常");
    }
  }

}
```

##### 2. 使用 SpringRetryTemplate

这里可以写我们的代码了

```
package com.zgd.demo.thread.retry.spring;

import com.zgd.demo.thread.retry.RetryDemoTask;
import lombok.extern.slf4j.Slf4j;
import org.junit.Test;
import org.springframework.remoting.RemoteAccessException;
import org.springframework.retry.backoff.FixedBackOffPolicy;
import org.springframework.retry.policy.SimpleRetryPolicy;
import org.springframework.retry.support.RetryTemplate;

import java.util.HashMap;
import java.util.Map;

/**
 * @Author: zgd
 * @Description: spring-retry 重试框架
 */
@Slf4j
public class SpringRetryTemplateTest {

  /**
   * 重试间隔时间ms,默认1000ms
   */
  private long fixedPeriodTime = 1000L;
  /**
   * 最大重试次数,默认为3
   */
  private int maxRetryTimes = 3;
  /**
   * 表示哪些异常需要重试,key表示异常的字节码,value为true表示需要重试
   */
  private Map<Class<? extends Throwable>, Boolean> exceptionMap = new HashMap<>();

  @Test
  public void test() {
    exceptionMap.put(RemoteAccessException.class,true);

    // 构建重试模板实例
    RetryTemplate retryTemplate = new RetryTemplate();

    // 设置重试回退操作策略，主要设置重试间隔时间
    FixedBackOffPolicy backOffPolicy = new FixedBackOffPolicy();
    backOffPolicy.setBackOffPeriod(fixedPeriodTime);

    // 设置重试策略，主要设置重试次数
    SimpleRetryPolicy retryPolicy = new SimpleRetryPolicy(maxRetryTimes, exceptionMap);

    retryTemplate.setRetryPolicy(retryPolicy);
    retryTemplate.setBackOffPolicy(backOffPolicy);

    Boolean execute = retryTemplate.execute(
            //RetryCallback
            retryContext -> {
              boolean b = RetryDemoTask.retryTask("abc");
              log.info("调用的结果:{}", b);
              return b;
            },
            retryContext -> {
              //RecoveryCallback
              log.info("已达到最大重试次数或抛出了不重试的异常~~~");
              returnfalse;
            }
    );

    log.info("执行结果:{}",execute);

  }

}
```

简单剖析下案例代码， `RetryTemplate`  承担了重试执行者的角色，它可以设置  `SimpleRetryPolicy` (重试策略，设置重试上限，重试的根源实体)， `FixedBackOffPolicy` （固定的回退策略，设置执行重试回退的时间间隔）。

 `RetryTemplate`  通过  `execute`  提交执行操作，需要准备  `RetryCallback`  和  `RecoveryCallback`  两个类实例，前者对应的就是重试回调逻辑实例，包装正常的功能操作， `RecoveryCallback`  实现的是整个执行操作结束的恢复操作实例.

只有在调用的时候抛出了异常，并且异常是在  `exceptionMap`  中配置的异常，才会执行重试操作，否则就调用到  `excute`  方法的第二个执行方法  `RecoveryCallback`  中

当然,重试策略还有很多种,回退策略也是:

#### 重试策略

- NeverRetryPolicy： 只允许调用  `RetryCallback`  一次，不允许重试
- AlwaysRetryPolicy： 允许无限重试，直到成功，此方式逻辑不当会导致死循环
- SimpleRetryPolicy： 固定次数重试策略，默认重试最大次数为 3 次，  `RetryTemplate`  默认使用的策略
- TimeoutRetryPolicy： 超时时间重试策略，默认超时时间为 1 秒，在指定的超时时间内允许重试
- ExceptionClassifierRetryPolicy： 设置不同异常的重试策略，类似组合重试策略，区别在于这里只区分不同异常的重试
- CircuitBreakerRetryPolicy： 有熔断功能的重试策略，需设置 3 个参数  `openTimeout`  、  `resetTimeout`  和  `delegate`
- CompositeRetryPolicy： 组合重试策略，有两种组合方式，乐观组合重试策略是指只要有一个策略允许即可以重试，悲观组合重试策略是指只要有一个策略不允许即可以重试，但不管哪种组合方式，组合中的每一个策略都会执行

#### 重试回退策略

重试回退策略，指的是每次重试是立即重试还是等待一段时间后重试。

默认情况下是立即重试，如果需要配置等待一段时间后重试则需要指定回退策略  `BackoffRetryPolicy` 。

- NoBackOffPolicy： 无退避算法策略，每次重试时立即重试
- FixedBackOffPolicy： 固定时间的退避策略，需设置参数  `sleeper`  和  `backOffPeriod`  ，  `sleeper`  指定等待策略，默认是  `Thread.sleep`  ，即线程休眠，  `backOffPeriod`  指定休眠时间，默认 1 秒
- UniformRandomBackOffPolicy： 随机时间退避策略，需设置  `sleeper`  、  `minBackOffPeriod`  和  `maxBackOffPeriod`  ，该策略在  `minBackOffPeriod`  ,  `maxBackOffPeriod`  之间取一个随机休眠时间，  `minBackOffPeriod`  默认 500 毫秒，  `maxBackOffPeriod`  默认 1500 毫秒
- ExponentialBackOffPolicy： 指数退避策略，需设置参数  `sleeper`  、  `initialInterval`  、  `maxInterval`  和  `multiplier`  ，  `initialInterval`  指定初始休眠时间，默认 100 毫秒，  `maxInterval`  指定最大休眠时间，默认 30 秒，  `multiplier`  指定乘数，即下一次休眠时间为  `当前休眠时间*multiplier`
- ExponentialRandomBackOffPolicy： 随机指数退避策略，引入随机乘数可以实现随机乘数回退

我们可以根据自己的应用场景和需求，使用不同的策略，不过一般使用默认的就足够了。

上面的代码的话,我简单的设置了重试间隔为 1 秒，重试的异常是  `RemoteAccessException` ，下面就是测试代码的情况: 重试第二次成功的情况:

![1](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/73861cbd793e4e81194be297c2a63ae5_MD5.png)

重试第二次成功的情况重试一次以后，遇到了没有指出需要重试的异常，直接结束重试，调用  `retryContext`

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/73861cbd793e4e81194be297c2a63ae5_MD5.png)

遇到没有指定重试的异常，直接结束重试重试了三次后，达到了最大重试次数，调用  `retryContext`

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/354d7fbb9a9af70736dd625de0543e75_MD5.png)

重试三次后达到最大重试次数

### 2. Spring-Retry 的注解使用方式

既然是 Spring 家族的东西，那么自然就支持和 Spring-Boot 整合

#### 1. 准备工作

依赖:

```
<dependency>
    <groupId>org.springframework.retry</groupId>
    <artifactId>spring-retry</artifactId>
    <version>1.2.2.RELEASE</version>
</dependency>

<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.1</version>
</dependency>
```

##### 2. 代码

在 application 启动类上加上  `@EnableRetry`  的注解

```
@EnableRetry
public class Application {
...
}
```

为了方便测试，我这里写了一个  `SpringBootTest`  的测试基类，需要使用  `SpringBootTest`  的只要继承这个类就好了

```
package com.zgd.demo.thread.test;

/**
 * @Author: zgd
 * @Description:
 */

import com.zgd.demo.thread.Application;
import lombok.extern.slf4j.Slf4j;
import org.junit.After;
import org.junit.Before;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

/**
 * @Author: zgd
 * @Date: 18/09/29 20:33
 * @Description:
 */
@RunWith(SpringRunner.class)
@SpringBootTest(classes = Application.class)
@Slf4j
public class MyBaseTest {

  @Before
  public void init() {
    log.info("----------------测试开始---------------");
  }

  @After
  public void after() {
    log.info("----------------测试结束---------------");
  }

}
```

我们只要在需要重试的方法上加  `@Retryable` ，在重试失败的回调方法上加  `@Recover` ，下面是这些注解的属性

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/14c8863b1f112c5f98c108f0914179a3_MD5.png)

@Retryable 和 @Recover 注解属性建一个 service 类

```
package com.zgd.demo.thread.retry.spring;

import com.zgd.demo.thread.retry.RetryDemoTask;
import com.zgd.demo.thread.test.MyBaseTest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.remoting.RemoteAccessException;
import org.springframework.retry.ExhaustedRetryException;
import org.springframework.retry.annotation.Backoff;
import org.springframework.retry.annotation.Recover;
import org.springframework.retry.annotation.Retryable;
import org.springframework.stereotype.Component;

/**
 * @Author: zgd
 * @Description:
 */
@Service
@Slf4j
public class SpringRetryDemo {

  /**
   * 重试所调用方法
   * @param param
   * @return
   */
  @Retryable(value = {RemoteAccessException.class},maxAttempts = 3,backoff = @Backoff(delay = 2000L,multiplier = 2))
  public boolean call(String param){
      return RetryDemoTask.retryTask(param);
  }

  /**
   * 达到最大重试次数,或抛出了一个没有指定进行重试的异常
   * recover 机制
   * @param e 异常
   */
  @Recover
  public boolean recover(Exception e,String param) {
    log.error("达到最大重试次数,或抛出了一个没有指定进行重试的异常:",e);
    returnfalse;
  }

}
```

然后我们调用这个 service 里面的 call 方法

```
package com.zgd.demo.thread.retry.spring;

import com.zgd.demo.thread.test.MyBaseTest;
import lombok.extern.slf4j.Slf4j;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

/**
 * @Author: zgd
 * @Description:
 */
@Component
@Slf4j
public class SpringRetryDemoTest extends MyBaseTest {

  @Autowired
  private SpringRetryDemo springRetryDemo;

  @Test
  public void retry(){
    boolean abc = springRetryDemo.call("abc");
    log.info("--结果是:{}--",abc);
  }

}
```

这里我依然是  `RemoteAccessException`  的异常才重试， `@Backoff(delay = 2000L,multiplier = 2))`  表示第一次间隔 2 秒，以后都是次数的 2 倍,也就是第二次 4 秒，第三次 6 秒.

**来测试一下：**

遇到了没有指定重试的异常,这里指定重试的异常是  `@Retryable(value = {RemoteAccessException.class}...` ，所以抛出参数异常  `IllegalArgumentException`  的时候，直接回调 @Recover 的方法

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/60775393827711026ebef16e3cc542dc_MD5.png)

遇到没有指定重试的异常，回调 @Recover 方法重试达到最大重试次数时，调用  `@Recover`  的方法

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/795c04481ce3912590058afabdcaab5b_MD5.png)

达到最大重试次数时调用 @Recover 方法重试到最后一次没有报错，返回 false

![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-C654zNXg-1653985491810)(https://i.imgur.com/fQshFGG.png)\]](https://mmbiz.qpic.cn/mmbiz_png/pUq1tpL9smoNmfLde7G5FiaRr2R2pyzKruBTViaQ9oBdNuJ3FdfP3bia2klVt6B1N08xlnRDiciciaPZet7zQlzVpbibETmRiak9Pia4V0j8vXL2E1eE/640?wx_fmt=png&from=appmsg)

最后一次没有报错，返回 false

## 二 重试框架之 Guava-Retry

Guava retryer 工具与 spring-retry 类似，都是通过定义重试者角色来包装正常逻辑重试，但是 Guava retryer 有更优的策略定义，在支持重试次数和重试频度控制基础上，能够兼容支持多个异常或者自定义实体对象的重试源定义，让重试功能有更多的灵活性。

Guava Retryer 也是线程安全的，入口调用逻辑采用的是  `Java.util.concurrent.Callable`  的 call 方法，示例代码如下：

pom.xml 加入依赖

```
<!-- https://mvnrepository.com/artifact/com.github.rholder/guava-retrying -->
<dependency>
    <groupId>com.github.rholder</groupId>
    <artifactId>guava-retrying</artifactId>
    <version>2.0.0</version>
</dependency>
```

更改一下测试的任务方法

```
package com.zgd.demo.thread.retry;

import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.RandomUtils;
import org.springframework.remoting.RemoteAccessException;

/**
 * @Author: zgd
 * @Description:
 */
@Slf4j
public class RetryDemoTask {

  /**
   * 重试方法
   * @return
   */
  public static boolean retryTask(String param)  {
    log.info("收到请求参数:{}",param);

    int i = RandomUtils.nextInt(0,11);
    log.info("随机生成的数:{}",i);
    if (i < 2) {
      log.info("为0,抛出参数异常.");
      throw new IllegalArgumentException("参数异常");
    }elseif (i < 5){
      log.info("为1,返回true.");
      returntrue;
    }elseif (i < 7){
      log.info("为2,返回false.");
      returnfalse;
    }else{
      //为其他
      log.info("大于2,抛出自定义异常.");
      throw new RemoteAccessException("大于2,抛出自定义异常");
    }
  }

}
```

这里设定跟 Spring-Retry 不一样，我们可以根据返回的结果来判断是否重试，比如返回 false 我们就重试

```
package com.zgd.demo.thread.retry.guava;

import com.github.rholder.retry.*;
import com.zgd.demo.thread.retry.RetryDemoTask;
import org.junit.Test;
import org.springframework.remoting.RemoteAccessException;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.function.Predicate;

/**
 * @Author: zgd
 * @Description:
 */
public class GuavaRetryTest {

  @Test
  public void fun01(){
    // RetryerBuilder 构建重试实例 retryer,可以设置重试源且可以支持多个重试源，可以配置重试次数或重试超时时间，以及可以配置等待时间间隔
    Retryer<Boolean> retryer = RetryerBuilder.<Boolean> newBuilder()
            .retryIfExceptionOfType(RemoteAccessException.class)//设置异常重试源
            .retryIfResult(res-> res==false)  //设置根据结果重试
            .withWaitStrategy(WaitStrategies.fixedWait(3, TimeUnit.SECONDS)) //设置等待间隔时间
            .withStopStrategy(StopStrategies.stopAfterAttempt(3))//设置最大重试次数
            .build();

    try {
      retryer.call(() -> RetryDemoTask.retryTask("abc"));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

}
```

运行测试一下

遇到了我们指定的需要重试的异常，进行重试，间隔是 3 秒

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/7047d2507b0fd39121b3b171a9f90894_MD5.png)

遇到指定重试的异常，间隔 3 秒重试重试次数超过了最大重试次数

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/2486a1b7c9568194aa4a818444f72a93_MD5.png)

超过最大重试次数返回为 true，直接结束重试

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/e7ed711ed8cf178a8881aee697f695e9_MD5.png)

返回 true，直接结束重试遇到了没有指定重试的异常，结束重试

![](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/93366ac92ffb919b7ac171db68d9d958_MD5.png)

遇到没有指定重试的异常，结束重试返回 false，重试

![](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/0dab922b3d27a3c732f516c890dd7d73_MD5.png)

返回 false，重试我们可以更灵活的配置重试策略，比如:

- retryIfException：  `retryIfException`  ，抛出  `runtime`  异常、  `checked`  异常时都会重试，但是抛出  `error`  不会重试。
- retryIfRuntimeException：  `retryIfRuntimeException`  只会在抛  `runtime`  异常的时候才重试，  `checked`  异常和  `error`  都不重试。
- retryIfExceptionOfType：  `retryIfExceptionOfType`  允许我们只在发生特定异常的时候才重试，比如  `NullPointerException`  和  `IllegalStateException`  都属于  `runtime`  异常，也包括自定义的  `error`  。

如:

```
retryIfExceptionOfType(NullPointerException.class)// 只在抛出空指针异常重试
```

- retryIfResult:  `retryIfResult`  可以指定你的  `Callable`  方法在返回值的时候进行重试，如

```
// 返回false重试
.retryIfResult(Predicates.equalTo(false))

//以_error结尾才重试
.retryIfResult(Predicates.containsPattern("_error$"))

//返回为空时重试
.retryIfResult(res-> res==null)
```

- RetryListener： 当发生重试之后，假如我们需要做一些额外的处理动作，比如 log 一下异常，那么可以使用  `RetryListener`  。每次重试之后，  `guava-retrying`  会自动回调我们注册的监听。可以注册多个  `RetryListener`  ，会按照注册顺序依次调用。

```
.withRetryListener(new RetryListener() {
  @Override
  public <T> void onRetry(Attempt<T> attempt) {
    logger.error("第【{}】次调用失败" , attempt.getAttemptNumber());
  }
})
```

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/d93ed49d8a8e47e1a0c6ba284bc4266d_MD5.png)

RetryListener 运行结果

![在这里插入图片描述](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/18603513c43cd9897997b478d89c114c_MD5.png)

RetryListener 运行结果

## 总结

spring-retry 和 guava-retry 工具都是线程安全的重试，能够支持并发业务场景的重试逻辑正确性。两者都很好的将正常方法和重试方法进行了解耦，可以设置超时时间、重试次数、间隔时间、监听结果、都是不错的框架。

但是明显感觉得到，guava-retry 在使用上更便捷，更灵活，能根据方法返回值来判断是否重试，而 Spring-retry 只能根据抛出的异常来进行重试。

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI + Spring Boot 3.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-10-01%20-%20%E6%B6%88%E6%81%AF%E9%87%8D%E8%AF%95%E6%A1%86%E6%9E%B6%20Spring-Retry%20%E5%92%8C%20Guava-Retry%EF%BC%8C%E8%BF%99%E4%B8%AA%E6%A1%86%E6%9E%B6%E6%9C%89%E7%82%B9%E6%84%8F%E6%80%9D/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 这五款牛逼的 IDEA 插件，堪称代码质量检查利器！
3. 美团动态线程池，香啊！
4. 面试官：如何理解 select、poll、epoll？
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
原文链接：https://mp.weixin.qq.com/s/0L58hIOdz0nUSTnMq8H2iw
