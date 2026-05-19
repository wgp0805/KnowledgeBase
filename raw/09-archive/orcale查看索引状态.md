---
title: orcale查看索引状态
tags:
  - orcale
categories:
  - orcale
date: 2023-12-06 13:50:01
---

> 方法：1、利用“select status from user_indexes where index_name='索引名称'”语句，若结果返回VALID，则索引没有失效；2、利用“select status from DBA_IND_PARTITIONS”语句查看分区索引状态；3、利用“select status from dba_indexes”查看普通索引状态。

## oracle查看索引

1、打开PLSQL，输入账号密码，登陆需要判断索引状态的数据库。打开SQL窗口，输入如下SQL

已复制

```sql
select status from user_indexes where index_name= '索引名称';
```

如果返回结果为VALID，则表示索引有效！

![image-20231206134608078](image-20231206134608078.png)

2、在相应用户下执行一下语句：

复制

```
select status from DBA_IND_PARTITIONS --分区索引
```

如果状态不是VALID的，那么就是失效的索引。

3、在相应用户下执行一下语句

复制

```
select status from dba_indexes --普通索引
```

如果状态不是VALID的，那么就是失效的索引。

扩展：

ORACLE查看某个表的索引状态

![image-20231206134234046](image-20231206134234046.png)

状态列STATUS说明：

​     valid:当前索引有效

​     N/A :分区索引 有效

​     unusable:索引失效

推荐教程：《[Oracle视频教程](https://www.php.cn/course/list/52.html)》

以上就是oracle怎么查看索引失效的详细内容，更多请关注php中文网其它相关文章！
