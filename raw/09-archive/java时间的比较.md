---
title: java时间的比较
tags:
  - JAVA
categories:
  - JAVA
date: 2022-05-28 18:53:43
---
### java时间的比较

```
1. 直接用Date自带方法before()和after()比较
Copy
//获取活动开始时间 
String beginTime = new String("2020-12-11 00:00:00"); 
//结束时间
String endTime = new String("2020-12-26 00:00:00");
Copy
//设置日期格式
SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
//获取活动开始时间和截止时间精确到秒
Date sd1=df.parse(beginTime);
Date sd2=df.parse(endTime);

.compareTo()方法:前后时间一模一样时返回(前后时间相等时)true,否则返回false.
.after()方法:当前面的时间晚于后面的时间时返回true,否则返回false.
例如:当前时间beginTime，结束时间endTime
	此时:beginTime.after(endTime )=true

.before()方法:当前面的时间早于后面的时间时返回true,否则返回false.
例如:当前时间beginTime 结束时间endTime
	此时:beginTime.before(endTime )=true
Copy
```

- java.util.Date中的before和after方法只会比较到Day，不管你的date是yyyy-MM-dd HH:mm:ss还是yyyy-MM-dd格式的。

  - 如果不是对上边的函数足够的了解的话，还是建议用gettime（）

  2.用getTime（）去比较时间

  ```
  //获取活动开始时间 和 结束时间
  String beginTime = new String("2020-12-11 00:00:00"); 
  String endTime = new String("2020-12-26 00:00:00");
  //设置日期格式
  SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
  //获取活动开始时间和截止时间精确到秒
  Date sd1=df.parse(beginTime);
  Date sd2=df.parse(endTime);
  //转换后的开始时间和结束时间
  long startTime =sd1.getTime();
  long overTime= sd2.getTime();
  ```

