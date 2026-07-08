---
title: "logback VS log4j2：一倍左右的性能差异，是时候注意了！"
source: "https://mp.weixin.qq.com/s/qVvBOnH4navGkQR3RORcwQ"
---
小哈学Java *2026年7月5日 23:50*

![图片](assets/logback%20VS%20log4j2%EF%BC%9A%E4%B8%80%E5%80%8D%E5%B7%A6%E5%8F%B3%E7%9A%84%E6%80%A7%E8%83%BD%E5%B7%AE%E5%BC%82%EF%BC%8C%E6%98%AF%E6%97%B6%E5%80%99%E6%B3%A8%E6%84%8F%E4%BA%86%EF%BC%81/91d808e95a27c7427542bafbafff0649_MD5.webp)

来源： [https://juejin.cn/post/7327878308757520419](https://juejin.cn/post/7327878308757520419)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 一、简介
- 方法 1：使用 lombok（推荐）
	- 方法 2：直接使用
- 浅谈与 slf4j、log4j、logback 的关系
- 二、性能测试对比
- 1.硬件环境
	- [2.jvm](http://2.jvm/) 信息
	- [3.log4j2](http://3.log4j2/) 和 logback 的版本
	- 4.测试线程数和测试方式
	- 5.日志格式
	- 6.日志长度
- 性能对比图
	- 附：测试环境
- 三、使用方法，有需要的可以拿去
- [1.logback](http://1.logback/) 在 springboot 项目中的使用
	- [2.log4j2](http://2.log4j2/) 在 spring 项目中的使用
	- 最佳实践
- 四、附录
- 1.测试代码
	- 2.更多参考
	- 参考资料

---

## 一、简介

logback, log4j2 等都是非常优秀的日志框架，在日常使用中，我们很少会关注去使用哪一个框架，但其实这些日志框架在性能方面存在明显的差异。

尤其在生产环境中，有时候日志的性能高低，很可能影响到机器的成本，像一些大企业，如阿里、腾讯、字节等，一点点的性能优化，就能节省数百万的支出。

再次，统一日志框架也是大厂常有的规范化的事情，还可以便于后续的 ETL 流程，因此，我们选一个日志框架，其实还是比较重要的。

### 浅谈与 slf4j、log4j、logback 的关系

笼统的讲就是 slf4j 是一系列的日志接口，而 log4j logback 是具体实现了这些接口的日志框架，也可以简单理解为 slf4j 是接口，logback 和 log4j 是 slf4j 的具体实现，slf4j 具备很高的易用性和很好的抽象性。

使用 SLF4J 编写日志消息非常简单。首先需要调用 LoggerFactory 上的 getLogger 方法来实例化一个新的 Logger 对象。一共有两种方法：

#### 方法 1：使用 lombok（推荐）

直接在类上打上 lombok 的注解，这个方法是最简单，代码量最小，编程效率最高的，而且 lombok 组件在很多场景都很好用。

```
@Slf4j
public class Main {}
```

#### 方法 2：直接使用

使用 `              org.slf4j.LoggerFactory            ` 的 getLogger 方法获取 logger 实例，注意推荐 `private static final`

```
private static final Logger LOG = 
            LoggerFactory.getLogger(Main.class);
```

## 二、性能测试对比

### 性能对比图

从上图可以得出两个结论：

- log4j2 全面优于 logback，log4j2 性能是 logback 的两倍
- 随着线程数量的增加，日志输出能力并不会线性增加，在增加到约两倍于 CPU 核数的时候，日志性能达到比较高的一个值。

> “
> 
> tips: 已知的影响效率的是，打出方法名称和行号都会显著降低日志输出效率，如我们单单去掉行号，在单线程情况下，log4j2 的性能相差一倍多。

### 附：测试环境

#### 1\. 硬件环境：

```
CPU AMD Ryzen 5 3600 6-Core Processor  Base speed: 3.95 GHz
Memory 32.0 GB Speed: 2666 MHz
```

#### 2\. jvm 信息

- JDK 版本： `              semeru-11.0.20            `
- JVM 参数： `-Xms1000m -Xmx1000m`

#### 3\. log4j2 和 logback 的版本

```
<
            log4j.version>2.22.1
          
<
            logback.version>1.4.14
```

#### 4\. 测试线程数和测试方式

- 线程数：1 8 32 128
- 测试方式：统一预热，跑三次，取预热后的正式跑的平均值

#### 5\. 日志格式

日志格式对于 log 的效率会有非常大的影响，有些时候则是天差地别。

```
<!--log4j2 的配置 -->
<Property name="
            log.pattern"
          >[%d{yyyyMMdd HH:mm:
            ss.SSS}]
           [%t] [%level{length=4}] %c{1.}:%L %msg%n
<!--logback 的配置 -->
[%date{yyyyMMdd HH:mm:
            ss.SSS}]
           [%thread] [%-4level] %logger{5}:%line %msg%n
```

#### 6\. 日志长度

长度大约 129 个字符，常见长度 输出到文件 [app.log，格式统一，一模一样](http://app.xn--log,,-jg1hba3140b3etob282bgw2f/)

```
[20240125 16:24:27.716] [thread-3] [INFO] 
            c.w.d.Main:32
           main - info level ...this is a demo script, pure string log will be used!
[20240125 16:24:27.716] [thread-1] [INFO] 
            c.w.d.Main:32
           main - info level ...this is a demo script, pure string log will be used!
```

## 三、使用方法，有需要的可以拿去

### 1\. logback 在 springboot 项目中的使用

pom 文件，不需要做任何事情，spring 官方默认使用 logback，非 spring 项目可以直接引入下面的 xml，同时包含 logback 和 slf4j

```
<dependency>
    
            ch.qos.logback
          
    <artifactId>logback-classic</artifactId>
    <version>${
            logback.version}
          </version>
</dependency>
```

配置文件放置位置： `src/main/resource/             logback.xml           ` ，样例如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

 <appender name="CONSOLE" class="
            ch.qos.logback.core.ConsoleAppender"
          >
  <encoder>
   %d{HH:mm:
            ss.SSS}
           [%thread] %-5level %logger{36} - %msg%n
  </encoder>
 </appender>

 <appender name="FILE" class="
            ch.qos.logback.core.rolling.RollingFileAppender"
          >
  <encoder>
   %d{HH:mm:
            ss.SSS}
           [%thread] %-5level %logger{36} - %msg%n
   <charset>utf-8</charset>
  </encoder>
  <file>log/
            output.log
          
  <rollingPolicy class="
            ch.qos.logback.core.rolling.FixedWindowRollingPolicy"
          >
   <fileNamePattern>log/
            output.log.%i
          
  </rollingPolicy>
  <triggeringPolicy class="
            ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy"
          >
   <MaxFileSize>1MB</MaxFileSize>
  </triggeringPolicy>
 </appender>

 <root level="INFO">
  <appender-ref ref="CONSOLE" />
  <appender-ref ref="FILE" />
 </root>
</configuration>
```

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/logback%20VS%20log4j2%EF%BC%9A%E4%B8%80%E5%80%8D%E5%B7%A6%E5%8F%B3%E7%9A%84%E6%80%A7%E8%83%BD%E5%B7%AE%E5%BC%82%EF%BC%8C%E6%98%AF%E6%97%B6%E5%80%99%E6%B3%A8%E6%84%8F%E4%BA%86%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

### 2\. log4j2 在 spring 项目中的使用

由于 spring 官方默认使用 logback，因此我们需要对 spring 默认的依赖进行排除然后再引入以下依赖：

```
<dependency>
    
            org.apache.logging.log4j
          
    <artifactId>log4j-core</artifactId>
    <version>${
            log4j.version}
          </version>
</dependency>

<dependency>
    
            org.apache.logging.log4j
          
    <artifactId>log4j-api</artifactId>
    <version>${
            log4j.version}
          </version>
</dependency>

<dependency>
    
            org.apache.logging.log4j
          
    <artifactId>log4j-slf4j2-impl</artifactId>
    <version>${
            log4j.version}
          </version>
</dependency>
```

配置文件放置位置： `src/main/resource/             log4j2.xml           ` ，样例如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
 <Properties>
        <!-- 定义日志格式 -->
  <Property name="
            log.pattern"
          >%d{MM-dd HH:mm:
            ss.SSS}
           [%t] %-5level %logger{36}%n%msg%n%n
        <!-- 定义文件名变量 -->
  <Property name="
            file.err.filename"
          >log/
            err.log
          
  <Property name="
            file.err.pattern"
          >log/err.%
            i.log.gz
          
 </Properties>
    <!-- 定义Appender，即目的地 -->
 <Appenders>
        <!-- 定义输出到屏幕 -->
  <Console name="console" target="SYSTEM_OUT">
            
   <PatternLayout pattern="${
            log.pattern}
          " />
  </Console>
        
  <RollingFile name="err" bufferedIO="true" fileName="${
            file.err.filename}
          " filePattern="${
            file.err.pattern}
          ">
   <PatternLayout pattern="${
            log.pattern}
          " />
   <Policies>
                <!-- 根据文件大小自动切割日志 -->
    <SizeBasedTriggeringPolicy size="1 MB" />
   </Policies>
            <!-- 保留最近10份 -->
   <DefaultRolloverStrategy max="10" />
  </RollingFile>
 </Appenders>
 <Loggers>
  <Root level="info">
            <!-- 对info级别的日志，输出到console -->
   <AppenderRef ref="console" level="info" />
            <!-- 对error级别的日志，输出到err，即上面定义的RollingFile -->
   <AppenderRef ref="err" level="error" />
  </Root>
 </Loggers>
</Configuration>
```

### 最佳实践：

**滚动日志，永远不让磁盘满**

- 根据运行环境要求，配置最大日志数量
- 根据运行环境要求，配置日志文件最大大小

**日志如何使用才方便统计和定位问题**

- 统一日志格式，比如统一先打印方法名称，再打印参数列表
- 写好要打印参数的 toString 方法

**日志如何配置性能才比较高**

- 日志配置应该遵循结构清晰，尽量简化的原则，能不让框架计算的，尽量不让框架计算，比如方法名，行号等

**全公司，或者个人使用习惯统一，这样有助于后续的日志收集、分析和统计**

## 四、附录

### 1\. 测试代码：

```
package 
            com.winjeg.demo;
          

import 
            lombok.extern.slf4j.Slf4j;
          
import 
            org.apache.commons.lang3.concurrent.BasicThreadFactory;
          
import 
            org.slf4j.Logger;
          
import 
            org.slf4j.LoggerFactory;
          

import 
            java.util.ArrayList;
          
import 
            java.util.List;
          
import 
            java.util.concurrent.*;
          

@Slf4j
public class Main {

    private static final Logger LOG = 
            LoggerFactory.getLogger(Main.class);
          

    private static final ThreadPoolExecutor EXECUTOR = new ThreadPoolExecutor(128, 256, 1L,
            
            TimeUnit.MINUTES,
           new ArrayBlockingQueue<>(512),
            new 
            BasicThreadFactory.Builder().namingPattern(
          "thread-%d").daemon(true).build());

    public static void main(String[] args) {
        long start = 
            System.currentTimeMillis();
          
        execute(8, 160_000);
        long first = 
            System.currentTimeMillis();
          
        execute(8, 160_000);
        
            System.out.printf(
          "time cost, preheat:%d\t, formal:%d\n", first - start, 
            System.currentTimeMillis()
           - first);
    }

    private static void execute(int threadNum, int times) {
        List<Future<?>> futures = new ArrayList<>();
        for (int i = 0; i < threadNum; i++) {
            Future f = 
            EXECUTOR.submit(()
           -> {
                for (long j = 0; j < times; j++) {
                    
            log.info(
          "main - info level ...this is a demo script, pure string log will be used!");
                }
            });
            
            futures.add(f);
          
        }
        
            futures.forEach(f
           -> {
            try {
                
            f.get();
          
            } catch (InterruptedException | ExecutionException e) {
                throw new RuntimeException(e);
            }
        });
    }
}
```

对应的 [pom.xml：](http://pom.xml：)

```
<project xmlns="
            http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="
            http://www.w3.org/2001/XMLSchema-instance"
          
         xsi:schemaLocation="
            http://maven.apache.org/POM/4.0.0
           
            http://maven.apache.org/xsd/maven-4.0.0.xsd"
          >
    <modelVersion>4.0.0</modelVersion>
    
            com.winjeg.spring
          
    <artifactId>demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>
    <properties>
        <
            project.build.sourceEncoding>UTF-8
          
        <
            log4j.version>2.22.1
          
        <
            logback.version>1.4.14
          
        <
            java.version>1.8
          
    </properties>

    <dependencies>
        <dependency>
            
            org.projectlombok
          
            <artifactId>lombok</artifactId>
            <version>1.18.30</version>
        </dependency>

        <dependency>
            
            org.apache.commons
          
            <artifactId>commons-lang3</artifactId>
            <version>3.12.0</version>
        </dependency>

        <dependency>
            
            org.apache.logging.log4j
          
            <artifactId>log4j-core</artifactId>
            <version>${
            log4j.version}
          </version>
        </dependency>

        <dependency>
            
            org.apache.logging.log4j
          
            <artifactId>log4j-api</artifactId>
            <version>${
            log4j.version}
          </version>
        </dependency>

        <dependency>
            
            org.apache.logging.log4j
          
            <artifactId>log4j-slf4j2-impl</artifactId>
            <version>${
            log4j.version}
          </version>
        </dependency>

        <!--        <dependency>-->
        " 
             target="_blank" 
             style="color: #576b95; text-decoration: none;">
            ch.qos.logback-->
          
        <!--            <artifactId>logback-classic</artifactId>-->
        <!--            <version>${
            logback.version}
          </version>-->
        <!--        </dependency>-->
    </dependencies>
</project>
```

### 2\. 更多参考

这些参考资料有可能不太对，但是为了方便大家查阅，我还是给出了一些官方的和比较受欢迎的资料

- logback 官方测试结果 \[1\]
- log4j2 官方测试结果 \[2\]
- Java 日志框架：log4j vs logback vs log4j2 \[3\]

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/logback%20VS%20log4j2%EF%BC%9A%E4%B8%80%E5%80%8D%E5%B7%A6%E5%8F%B3%E7%9A%84%E6%80%A7%E8%83%BD%E5%B7%AE%E5%BC%82%EF%BC%8C%E6%98%AF%E6%97%B6%E5%80%99%E6%B3%A8%E6%84%8F%E4%BA%86%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 面试官：为什么需要 Gateway 网关，它有什么作用？3. 如何搭建漂亮的 SpringBoot 脚手架？4. 我们放弃了Nacos作为配置中心，转而选择了这款神器~
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文