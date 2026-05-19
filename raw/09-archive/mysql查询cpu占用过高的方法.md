---
title: mysql查询cpu占用过高的方法
tags:
  - mysql
categories:
  - mysql
date: 2023-06-13 10:06:28
---

## 查询mysql的进程号

```shell
ps aux | grep mysqld
```

mysql	32319	80.4	5.4	15790296	7241632	?

> 使用top查询mysql的使用情况

```shell
top -p 32319 -H
```

![img](2.png)

可以看到每个线程的资源占用情况。

#### MySQL客户端，连接登录后：

##### 通过PID号直接查看执行的语句：

```sql
select sql_text from performance_schema.events_statements_current where thread_id = (select thread_id from `performance_schema`.threads where thread_os_id = PID号);
```



##### 解释说明：

查看指定线程正在执行的语句
 根据操作系统线程ID，查看mysql数据库中对应的线程ID:

```sql
select thread_id,name ,PROCESSLIST_ID,THREAD_OS_ID from `performance_schema`.threads where thread_os_id = 16433;
```

![img](1.png)

通过数据库的线程id获取正在执行的SQL：

```sql
select sql_text from performance_schema.events_statements_current where thread_id = 188664;
```

合并一个语句：

```sql
select sql_text from performance_schema.events_statements_current where thread_id = (select thread_id from `performance_schema`.threads where thread_os_id = 16433);
```
