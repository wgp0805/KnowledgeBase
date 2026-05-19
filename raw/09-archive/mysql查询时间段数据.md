---
title: mysql查询时间段数据
tags:
  - MySQL
categories:
  - MySQL
date: 2022-05-28 18:54:33
---
参照文章（ mysql查询时间段内数据）进行了操作。

```
    先来建表语句：
    SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------

-- Table structure for t_user

-- ----------------------------

DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `userId` bigint(20) NOT NULL,
  `fullName` varchar(64) NOT NULL,
  `userType` varchar(16) NOT NULL,
  `addedTime` datetime NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------

-- Records of t_user

-- ----------------------------

INSERT INTO `t_user` VALUES ('1', '爽爽', '普通', '2018-01-21 10:20:09');
INSERT INTO `t_user` VALUES ('2', '贵贵', '普通', '2017-11-06 10:20:22');
INSERT INTO `t_user` VALUES ('3', '芬芬', 'vip', '2017-11-13 10:20:42');
INSERT INTO `t_user` VALUES ('4', '思思', 'vip', '2018-01-21 10:20:55');
INSERT INTO `t_user` VALUES ('5', '妍妍', 'vip', '2017-09-17 10:21:28');



    下面是sql语句：
-- 今天  
select fullName,addedTime from t_user where to_days(addedTime) <= to_days(now()); 
-- 昨天  
select fullName,addedTime from t_user where to_days(NOW()) - TO_DAYS(addedTime) <= 1;  
--查询前一天的数据
select * from t_user t where date_sub(CURDATE(),INTERVAL -1 DAY) <= DATE(addedTime)
-- 近7天  
select fullName,addedTime from t_user where date_sub(CURDATE(),INTERVAL 7 DAY) <= DATE(addedTime);  
-- 近30天  
SELECT fullName,addedTime FROM t_user where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(addedTime);
-- 本月  
SELECT fullName,addedTime FROM t_user WHERE DATE_FORMAT( addedTime, '%Y%m' ) = DATE_FORMAT( CURDATE() , '%Y%m' );
-- 上一月  
SELECT fullName,addedTime FROM t_user WHERE PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( addedTime, '%Y%m' ) ) =1; 
-- 查询本季度数据  
select fullName,addedTime FROM t_user where QUARTER(addedTime)=QUARTER(now()); 
-- 查询上季度数据  
select fullName,addedTime FROM t_user where QUARTER(addedTime)=QUARTER(DATE_SUB(now(),interval 1 QUARTER));  
-- 查询本年数据  
select fullName,addedTime FROM t_user where YEAR(addedTime)=YEAR(NOW());  
-- 查询上年数据  
select fullName,addedTime FROM t_user where year(addedTime)=year(date_sub(now(),interval 1 year));  
-- 查询距离当前现在6个月的数据  
select fullName,addedTime FROM t_user where addedTime between date_sub(now(),interval 6 month) and now();  

-- 查询当前这周的数据  
SELECT fullName,addedTime FROM t_user WHERE YEARWEEK(date_format(addedTime,'%Y-%m-%d')) = YEARWEEK(now());  
-- 查询上周的数据  
SELECT fullName,addedTime FROM t_user WHERE YEARWEEK(date_format(addedTime,'%Y-%m-%d')) = YEARWEEK(now())-1;  
-- 查询上个月的数据   
select fullName,addedTime FROM t_user where date_format(addedTime,'%Y-%m')=date_format(DATE_SUB(curdate(), INTERVAL 1 MONTH),'%Y-%m'); 
-- 查询当前月份的数据
select fullName,addedTime FROM t_user where DATE_FORMAT(addedTime,'%Y%m') = DATE_FORMAT(CURDATE(),'%Y%m');
select fullName,addedTime FROM t_user where date_format(addedTime,'%Y-%m')=date_format(now(),'%Y-%m'); 

-- 查询指定时间段的数据
select fullName,addedTime FROM t_user where addedTime between  '2017-1-1 00:00:00'  and '2018-1-1 00:00:00';   
select fullName,addedTime FROM t_user where addedTime >='2017-1-1 00:00:00'  and addedTime < '2018-1-1 00:00:00'; 



    归纳一下：
    1、查询时间段内的数据，一般可以用between and 或 <> 来指定时间段。

    2、mysql的时间字段类型有：datetime，timestamp，date，time，year。
Copy
```



```
   3、 获取系统当前时间的函数：

    select CURDATE();
    select NOW();

    4、获取时间差的函数：

    period_diff()    datediff(date1,date2)      timediff(time1,time2)

   5、日期加减函数：

    date_sub() 

    date_add()     adddate()      addtime()

    period_add(P,N)    

    --------以上参考文章（mysql日期加减）




    6、时间格式转化函数：

    date_format(date, format) ，MySQL日期格式化函数date_format()
    unix_timestamp() 
    str_to_date(str, format) 
    from_unixtime(unix_timestamp, format) ，MySQL时间戳格式化函数from_unixtime



    --------以上参考文章（MYSQL日期 字符串 时间戳互转）
Copy
```



```
    顺带写一下oracle的查询语句：
    select * from Oracle.alarmLog where alarmtime between to_date('2007-03-03 18:00:00','yyyy-mm-dd hh24:mi:ss') and to_date('2007-09-04 18:00:00','yyyy-mm-dd hh24:mi:ss')
Copy
```