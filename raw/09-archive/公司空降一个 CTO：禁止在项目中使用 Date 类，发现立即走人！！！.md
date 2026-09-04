---
title: "公司空降一个 CTO：禁止在项目中使用 Date 类，发现立即走人！！！"
source: "https://mp.weixin.qq.com/s/8IXIpnqJkHg61ClEe4Z9-Q"
---
小哈学Java *2026年9月3日 17:44*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E5%85%AC%E5%8F%B8%E7%A9%BA%E9%99%8D%E4%B8%80%E4%B8%AA%20CTO%EF%BC%9A%E7%A6%81%E6%AD%A2%E5%9C%A8%E9%A1%B9%E7%9B%AE%E4%B8%AD%E4%BD%BF%E7%94%A8%20Date%20%E7%B1%BB%EF%BC%8C%E5%8F%91%E7%8E%B0%E7%AB%8B%E5%8D%B3%E8%B5%B0%E4%BA%BA%EF%BC%81%EF%BC%81%EF%BC%81/2a95c5153d060d5b51867d1bc7877d20_MD5.webp)

来源： [cnblogs.com/wlovet/p/18058514](http://cnblogs.com/wlovet/p/18058514)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

- 一、有什么问题吗 [java.util.Date？](http://java.util.Date？)
- 二、为啥要改？
- 三、怎么改？
- 四、小结一下

---

## 一、有什么问题吗 java.util.Date？

`              java.util.Date            ` （Date从现在开始）是一个糟糕的类型，这解释了为什么它的大部分内容在 Java 1.1 中被弃用（但不幸的是仍在使用）。

**设计缺陷包括：**

- **它的名称具有误导性：** 它并不代表一个日期，而是代表时间的一个瞬间。所以它应该被称为Instant——正如它的 `              java.time            ` 等价物一样。
- **它是非最终的：** 这鼓励了对继承的不良使用，例如 `              java.sql.Date            ` （这意味着代表一个日期，并且由于具有相同的短名称而也令人困惑）
- **它是可变的：** 日期/时间类型是自然值，可以通过不可变类型有效地建模。可变的事实Date（例如通过setTime方法）意味着勤奋的开发人员最终会在各处创建防御性副本。
- 它在许多地方（包括）隐式使用系统本地时区， `toString()` 这让许多开发人员感到困惑。有关此内容的更多信息，请参阅“什么是即时”部分
- 它的月份编号是从 0 开始的，是从 C 语言复制的。这导致了很多很多相差一的错误。
- 它的年份编号是基于 1900 年的，也是从 C 语言复制的。当然，当 Java 出现时，我们已经意识到这不利于可读性？
- **它的方法命名不明确：** `getDate()` 返回月份中的某一天，并 `getDay()` 返回星期几。给这些更具描述性的名字有多难？
- **对于是否支持闰秒含糊其辞：** “秒由 0 到 61 之间的整数表示；值 60 和 61 仅在闰秒时出现，即使如此，也仅在实际正确跟踪闰秒的 Java 实现中出现。” 我强烈怀疑大多数开发人员（包括我自己）都做了很多假设，认为 for 的范围 `getSeconds()` 实际上在 0-59 范围内（含）。
- **它的宽容没有明显的理由：** “在所有情况下，为这些目的而对方法给出的论据不必落在指定的范围内; 例如，日期可以指定为 1 月 32 日，并被解释为 2 月 1 日。” 多久有用一次？

**关键原因如下：**

![图片](assets/%E5%85%AC%E5%8F%B8%E7%A9%BA%E9%99%8D%E4%B8%80%E4%B8%AA%20CTO%EF%BC%9A%E7%A6%81%E6%AD%A2%E5%9C%A8%E9%A1%B9%E7%9B%AE%E4%B8%AD%E4%BD%BF%E7%94%A8%20Date%20%E7%B1%BB%EF%BC%8C%E5%8F%91%E7%8E%B0%E7%AB%8B%E5%8D%B3%E8%B5%B0%E4%BA%BA%EF%BC%81%EF%BC%81%EF%BC%81/27ec29d1c50debe5a0017d2387c4f27d_MD5.png)

图片

原文如下：为什么要避免使用Date类？

“

[https://codeblog.jonskeet.uk/2017/04/23/all-about-java-util-date/](https://codeblog.jonskeet.uk/2017/04/23/all-about-java-util-date/)

## 二、为啥要改？

我们要改的原因很简单，我们的代码缺陷扫描规则认为这是一个必须修改的缺陷，否则不给发布，不改不行，服了。

![图片](assets/%E5%85%AC%E5%8F%B8%E7%A9%BA%E9%99%8D%E4%B8%80%E4%B8%AA%20CTO%EF%BC%9A%E7%A6%81%E6%AD%A2%E5%9C%A8%E9%A1%B9%E7%9B%AE%E4%B8%AD%E4%BD%BF%E7%94%A8%20Date%20%E7%B1%BB%EF%BC%8C%E5%8F%91%E7%8E%B0%E7%AB%8B%E5%8D%B3%E8%B5%B0%E4%BA%BA%EF%BC%81%EF%BC%81%EF%BC%81/ae57b4f1b109184636d2e7c626d49ab7_MD5.png)

图片

解决思路：避免使用 `              java.util.Date            ` 与 `              java.sql.Date            ` 类和其提供的API，考虑使用 `              java.time.Instant            ` 类或 `              java.time.LocalDateTime            ` 类及其提供的API替代。

## 三、怎么改？

只能说这种基础的类改起来牵一发动全身，需要从DO实体类看起，然后就是各种Converter，最后是DTO。

由于我们还是微服务架构，业务服务依赖于基础服务的API，所以必须要一起改否则就会报错。这里就不细说修改流程了，主要说一下我们在改造的时候遇到的一些问题。

#### 1\. 耐心比对数据库日期字段和DO的映射

##### 1）确定字段类型

首先你需要确定数据对象中的 Date 字段代表的是日期、时间还是时间戳。

- 如果字段代表日期和时间，则可能需要使用 LocalDateTime。
- 如果字段仅代表日期，则可能需要使用 LocalDate。
- 如果字段仅代表时间，则可能需要使用 LocalTime。
- 如果字段需要保存时间戳（带时区的），则可能需要使用 Instant 或 ZonedDateTime。

##### 2）更新数据对象类

更新数据对象类中的字段，把 Date 类型改为适当的 `              java.time            ` 类型。

#### 2\. 将DateUtil中的方法改造

##### 1）替换原来的new Date()和 Calendar.getInstance().getTime()

原来的方式:

```
Date nowDate = new Date();
Date nowCalendarDate = 
            Calendar.getInstance().getTime();
```

使用 `              java.time            ` 改造后:

```
// 使用Instant代表一个时间点，这与Date类似
Instant nowInstant = 
            Instant.now();
          

// 如果需要用到具体的日期和时间（例如年、月、日、时、分、秒）
LocalDateTime nowLocalDateTime = 
            LocalDateTime.now();
          

// 如果你需要和特定的时区交互，可以使用ZonedDateTime
ZonedDateTime nowZonedDateTime = 
            ZonedDateTime.now();
          

// 如果你需要转换回
            java.util.Date，你可以这样做（假设你的代码其他部分还需要使用Date）
          
Date nowFromDateInstant = 
            Date.from(nowInstant);
          

// 如果需要与
            java.sql.Timestamp交互
          

            java.sql.Timestamp
           nowFromInstant = 
            java.sql.Timestamp.from(nowInstant);
```

一些注意点:

- Instant 表示的是一个时间点，它是时区无关的，相当于旧的 Date 类。它通常用于表示时间戳。
- `LocalDateTime` 表示没有时区信息的日期和时间，它不能直接转换为时间戳，除非你将其与时区结合使用（例如通过 `ZonedDateTime` ）。
- `ZonedDateTime` 包含时区信息的日期和时间，它更类似于 Calendar，因为 Calendar 也包含时区信息。
- 当你需要将 `              java.time            ` 对象转换回 `              java.util.Date            ` 对象时，可以使用 `              Date.from(Instant)            ` 方法。这在你的代码需要与旧的API或库交互时非常有用。

##### 2）一些基础的方法改造

**a. dateFormat**

原来的方式

```
public static String dateFormat(Date date, String dateFormat) {
    SimpleDateFormat formatter = new SimpleDateFormat(dateFormat);
    return 
            formatter.format(date);
          
}
```

使用 `              java.time            ` 改造后

```
public static String dateFormat(LocalDateTime date, String dateFormat) {
    DateTimeFormatter formatter = 
            DateTimeFormatter.ofPattern(dateFormat);
          
    return 
            date.format(formatter);
          
}
```

**b. addSecond、addMinute、addHour、addDay、addMonth、addYear**

原来的方式

```
public static Date addSecond(Date date, int second) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(13,
           second);
    return 
            calendar.getTime();
          
}

public static Date addMinute(Date date, int minute) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(12,
           minute);
    return 
            calendar.getTime();
          
}

public static Date addHour(Date date, int hour) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(10,
           hour);
    return 
            calendar.getTime();
          
}

public static Date addDay(Date date, int day) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(5,
           day);
    return 
            calendar.getTime();
          
}

public static Date addMonth(Date date, int month) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(2,
           month);
    return 
            calendar.getTime();
          
}

public static Date addYear(Date date, int year) {
    Calendar calendar = 
            Calendar.getInstance();
          
    
            calendar.setTime(date);
          
    
            calendar.add(1,
           year);
    return 
            calendar.getTime();
          
}
```

使用 `              java.time            ` 改造后

```
public static LocalDateTime addSecond(LocalDateTime date, int second) {
    return 
            date.plusSeconds(second);
          
}

public static LocalDateTime addMinute(LocalDateTime date, int minute) {
    return 
            date.plusMinutes(minute);
          
}

public static LocalDateTime addHour(LocalDateTime date, int hour) {
    return 
            date.plusHours(hour);
          
}

public static LocalDateTime addDay(LocalDateTime date, int day) {
    return 
            date.plusDays(day);
          
}

public static LocalDateTime addMonth(LocalDateTime date, int month) {
    return 
            date.plusMonths(month);
          
}

public static LocalDateTime addYear(LocalDateTime date, int year) {
    return 
            date.plusYears(year);
          
}
```

**c. dateToWeek**

原来的方式

```
public static final String[] WEEK_DAY_OF_CHINESE = new String[]{"周日", "周一", "周二", "周三", "周四", "周五", "周六"};
public static String dateToWeek(Date date) {
    Calendar cal = 
            Calendar.getInstance();
          
    
            cal.setTime(date);
          
    return WEEK_DAY_OF_CHINESE[
            cal.get(7)
           - 1];
}
```

使用 `              java.time            ` 改造后

```
public static final String[] WEEK_DAY_OF_CHINESE = new String[]{"周日", "周一", "周二", "周三", "周四", "周五", "周六"};

public static String dateToWeek(LocalDate date) {
    DayOfWeek dayOfWeek = 
            date.getDayOfWeek();
          
    return WEEK_DAY_OF_CHINESE[
            dayOfWeek.getValue()
           % 7];
}
```

**d. getStartOfDay和getEndOfDay**

原来的方式

```
public static Date getStartTimeOfDay(Date date) {
    if (date == null) {
        returnnull;
    } else {
        LocalDateTime localDateTime = 
            LocalDateTime.ofInstant(Instant.ofEpochMilli(date.getTime()),
           
            ZoneId.systemDefault());
          
        LocalDateTime startOfDay = 
            localDateTime.with(LocalTime.MIN);
          
        return 
            Date.from(startOfDay.atZone(ZoneId.systemDefault()).toInstant());
          
    }
}

public static Date getEndTimeOfDay(Date date) {
    if (date == null) {
        returnnull;
    } else {
        LocalDateTime localDateTime = 
            LocalDateTime.ofInstant(Instant.ofEpochMilli(date.getTime()),
           
            ZoneId.systemDefault());
          
        LocalDateTime endOfDay = 
            localDateTime.with(LocalTime.MAX);
          
        return 
            Date.from(endOfDay.atZone(ZoneId.systemDefault()).toInstant());
          
    }
}
```

使用 `              java.time            ` 改造后

```
public static LocalDateTime getStartTimeOfDay(LocalDateTime date) {
    if (date == null) {
        returnnull;
    } else {
        // 获取一天的开始时间，即00:00
        return 
            date.toLocalDate().atStartOfDay();
          
    }
}

public static LocalDateTime getEndTimeOfDay(LocalDateTime date) {
    if (date == null) {
        returnnull;
    } else {
        // 获取一天的结束时间，即23:59:59.999999999
        return 
            date.toLocalDate().atTime(LocalTime.MAX);
          
    }
}
```

**e. betweenStartAndEnd**

原来的方式

```
public static Boolean betweenStartAndEnd(Date nowTime, Date beginTime, Date endTime) {
    Calendar date = 
            Calendar.getInstance();
          
    
            date.setTime(nowTime);
          
    Calendar begin = 
            Calendar.getInstance();
          
    
            begin.setTime(beginTime);
          
    Calendar end = 
            Calendar.getInstance();
          
    
            end.setTime(endTime);
          
    return 
            date.after(begin)
           && 
            date.before(end);
          
}
```

使用 `              java.time            ` 改造后

```
public static Boolean betweenStartAndEnd(Instant nowTime, Instant beginTime, Instant endTime) {
    return 
            nowTime.isAfter(beginTime)
           && 
            nowTime.isBefore(endTime);
          
}
```

我这里就只列了一些，如果有缺失的可以自己补充，不会写的话直接问问ChatGPT，它最会干这事了。最后把这些修改后的方法替换一下就行了。

## 四、小结一下

这个改造难度不高，但是复杂度非常高，一个地方没改好，轻则接口报错，重则启动失败，非常耗费精力，真不想改。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E5%85%AC%E5%8F%B8%E7%A9%BA%E9%99%8D%E4%B8%80%E4%B8%AA%20CTO%EF%BC%9A%E7%A6%81%E6%AD%A2%E5%9C%A8%E9%A1%B9%E7%9B%AE%E4%B8%AD%E4%BD%BF%E7%94%A8%20Date%20%E7%B1%BB%EF%BC%8C%E5%8F%91%E7%8E%B0%E7%AB%8B%E5%8D%B3%E8%B5%B0%E4%BA%BA%EF%BC%81%EF%BC%81%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. ES 支持哪些数据类型，和 MySQL 之间的映射关系是怎么样的？3. Spring-Smart-DI 动态切换实现类，很不错！
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文