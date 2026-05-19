---
title: trunc函数用法
tags:
  - Orcale
categories:
  - Orcale
date: 2022-05-28 17:48:16
---
{% note success %} 用于截取时间或者数值，返回指定的值 {% endnote %}
### 1、截取时间
```sql
select  trunc(to_date('2018-02-01 1:00:00','YYYY-MM-DD HH:MI:SS'),'yyyy') from   dual ;--返回当年第一天
select  trunc(to_date('2018-02-01 1:00:00','YYYY-MM-DD HH:MI:SS'),'mm') from   dual ; --返回当月第一天
select  trunc(to_date('2018-02-01 1:00:00','YYYY-MM-DD HH:MI:SS'),'dd') from   dual ;--返回当前年月
select  trunc(to_date('2018-02-01 1:00:00','YYYY-MM-DD HH:MI:SS'),'d') from   dual ; --返回当前星期的第一天(星期日) 
select  trunc(to_date('2018-02-01 1:12:12','YYYY-MM-DD HH:MI:SS'),'hh') from   dual ;--返回当前日期截取到小时,分秒补0
select  trunc(to_date('2018-02-01 1:12:12','YYYY-MM-DD HH:MI:SS'),'mi') from   dual ;--返回当前日期截取到分,秒补0
```
### 2、截取数值
语法：trunc(number,decimals)
number:指需要截取的数字
```sql 
select  trunc(122.555) from  dual t; --默认取整
select  trunc(122.555,2) from  dual t;
select  trunc(122.555,-2) from  dual t;--负数表示从小数点左边开始截取2位
```