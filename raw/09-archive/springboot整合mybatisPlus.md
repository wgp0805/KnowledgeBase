---
title: springboot整合mybatis-plus
tags:
  - mybatis-plus
categories:
  - mybatis-plus
date: 2023-06-15 08:59:00
---

## 一、创建一个demo项目

在ide中创建项目的时候需要选中spring web的包，还有lombok，hutool，然后新建项目，这里我也多选了`security`的包，因为打算后期还要在这个demo的项目上去整合springsecurity的功能，

| 技术栈               |  版本  |
| -------------------- | :----: |
| jdk                  |   17   |
| springboot           | 3.1.0  |
| mybatis-plus         | 3.5.3  |
| hutool               | 5.8.18 |
| mysql数据库          | 5.7.34 |
| mysql-connector-java | 8.0.30 |
| druid                | 1.1.22 |

mybatis-plus官网地址[ MyBatis-Plus (baomidou.com)](https://baomidou.com/pages/24112f/#特性)

```xml
 <dependencies>
        <!-- spring web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!-- mybatis-plus -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.5.3</version>
        </dependency>
        <!-- hutool工具包 -->
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>5.8.18</version>
        </dependency>
        <!-- lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <!--Mysql jdbc驱动-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.30</version>
        </dependency>
        <!--引入druid依赖-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.22</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
```



## 二、设置启动端口

如果不设置启动端口的话，系统启动的时候默认就是8080端口，这里方便管理也以防冲突我设置了8081端口

```
server:
  port: 8080
```

一般新建完项目之后配置文件时怕`properites`的这里我修改为`yml`

## 三、整合mybatis-plus

### 设置数据库链接

```yml
# 端口号
server:
  port: 8081

# 数据库链接
spring:
  datasource:
    #配置数据源类型这里使用的是springboot自带的数据源hikari，也可以切换为Druid
    type: com.zaxxer.hikari.HikariDataSource
    #配置连接数据库的各个信息
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/demo?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8&AllowPublicKeyRetrieval=True
    username: demo123
    password: 123321

```

这里我是使用的自己的服务器创建的数据库，如果使用自己的数据库的，直接将地址和用户名密码切换成自己的即可

### 创建数据库表

```sql
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `account` varchar(20) DEFAULT NULL COMMENT '用户账号',
  `user_name` varchar(50) DEFAULT NULL COMMENT '用户姓名',
  `pass_word` varchar(200) DEFAULT NULL COMMENT '密码',
  `salt` varchar(100) DEFAULT NULL COMMENT '盐',
  `mobile` varchar(20) DEFAULT NULL COMMENT '手机号码',
  `sex` char(1) DEFAULT '0' COMMENT '用户性别（0男 1女 2未知）',
  `state` char(1) DEFAULT '0' COMMENT '帐号状态（0正常 1停用）',
  `locked_flag` char(1) DEFAULT '0' COMMENT '数据锁定（0正常，1锁定）',
  `create_by` varchar(64) DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` varchar(64) DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

然后在表中随意创建两条数据

```sql
INSERT INTO `demo`.`user` (`account`, `user_name`, `pass_word`, `salt`, `mobile`, `create_by`, `create_time`) VALUES ('15946051148', '汪广平', '123', 'qweqweqw', '15946051148', 'admin', '2023-06-15 10:17:46')
Time: 0.041s

INSERT INTO `demo`.`user` (`account`, `user_name`, `pass_word`, `salt`, `mobile`, `create_by`, `create_time`) VALUES ('15045085006', 'wangguangping', '456', 'asdasdasdsa', '15545331491', 'admin', '2023-06-15 10:18:36')
```

### 创建表对应的实体类

> user.java

```java
package com.wgp.demo.bean;

import com.baomidou.mybatisplus.annotation.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.experimental.Accessors;

import java.time.LocalDateTime;

/**
 * @Description: 用户表
 * @Name: User
 * @Author: wgp
 * @DateTime: 2023/6/15 9:54
 */
//获取getset方法
@Data
//声明有参构造无参构造
@AllArgsConstructor
@Accessors(chain = true)
@TableName("user")
public class User {
    /**
     * 序列化
     */
    private static final long serialVersionUID = 1L;

    /**
     * 用户id
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    /**
     * 用户账号
     */
    private String account;
    /**
     * 姓名
     */
    private String userName;
    /**
     * 密码
     */
    private String passWord;
    /**
     * 盐
     */
    private String salt;
    /**
     * 手机号码
     */
    private String mobile;
    /**
     * 用户性别（0男 1女 2未知）
     */
    private String sex;
    /**
     * 帐号状态（0正常 1停用）
     */
    private String state;
    /**
     * 数据锁定（0正常，1锁定）
     */
    private String lockedFlag;
    /**
     * 创建者
     */
    private String createBy;
    /**
     * 创建时间
     */
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;
    /**
     * 更新者
     */
    private String updateBy;
    /**
     * 更新时间
     */
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
    /**
     * 备注
     */
    private String remark;
}

```

#### 实体类中常用的注解

##### **@TableName("user")**

1. 如果 实体类User和 表名user是对应的，就可以映射上，则 @TableName 可以省略 

2. 如果 实体类User 和 表名user不对应，需要使用 @TableName 进行指定

```java
@TableName("sys_user")
public class User {
    private Long id;
    private String name;
    private Integer age;
    private String email;
}
```

##### @TableId(value = "id", type = IdType.AUTO)

- 描述：主键注解
- 使用位置：实体类主键字段

| 属性  | 类型   | 必须指定 | 默认值      | 描述         |
| :---- | :----- | :------- | :---------- | :----------- |
| value | String | 否       | ""          | 主键字段名   |
| type  | Enum   | 否       | IdType.NONE | 指定主键类型 |

###### idType

| 值          | **描述**                                                     |
| ----------- | ------------------------------------------------------------ |
| AUTO        | 数据库 ID 自增                                               |
| NONE        | 无状态，该类型为未设置主键类型（注解里等于跟随全局，全局里约等于 INPUT） |
| INPUT       | insert 前自行 set 主键值                                     |
| ASSIGN_ID   | 分配 ID(主键类型为 Number(Long 和 Integer)或 String)(since 3.3.0),使用接口`IdentifierGenerator`的方法`nextId`(默认实现类为`DefaultIdentifierGenerator`雪花算法) |
| ASSIGN_UUID | 分配 UUID,主键类型为 String(since 3.3.0),使用接口`IdentifierGenerator`的方法`nextUUID`(默认 default 方法) |

#####  @TableField(fill = FieldFill.INSERT_UPDATE)

- 描述：字段注解（非主键）

```java
@TableName("sys_user")
public class User {
    @TableId
    private Long id;
    @TableField("nickname")
    private String name;
    private Integer age;
    private String email;
}
```

| 属性           | 类型    | 必须指定 | 默认值                | 描述                                                         |
| -------------- | ------- | -------- | --------------------- | ------------------------------------------------------------ |
| value          | String  | 否       | ""                    | 数据库字段名                                                 |
| exist          | boolean | 否       | true                  | 是否为数据库表字段                                           |
| update         | String  | 否       | ""                    | 字段 `update set` 部分注入，例如：当在version字段上注解`update="%s+1"` 表示更新时会 `set version=version+1` （该属性优先级高于 `el` 属性） |
| insertStrategy | Enum    | 否       | FieldStrategy.DEFAULT | 举例：NOT_NULL `insert into table_a(<if test="columnProperty != null">column</if>) values (<if test="columnProperty != null">#{columnProperty}</if>)` |
| updateStrategy | Enum    | 否       | FieldStrategy.DEFAULT | 举例：IGNORED `update table_a set column=#{columnProperty}`  |
| whereStrategy  | Enum    | 否       | FieldStrategy.DEFAULT | 举例：NOT_EMPTY `where <if test="columnProperty != null and columnProperty!=''">column=#{columnProperty}</if>` |
| fill           | Enum    | 否       | FieldFill.DEFAULT     | 字段自动填充策略                                             |
| select         | boolean | 否       | true                  | 是否进行 select 查询                                         |

关于`jdbcType`和`typeHandler`以及`numericScale`的说明:

`numericScale`只生效于 update 的 sql. `jdbcType`和`typeHandler`如果不配合`@TableName#autoResultMap = true`一起使用,也只生效于 update 的 sql. 对于`typeHandler`如果你的字段类型和 set 进去的类型为`equals`关系,则只需要让你的`typeHandler`让 Mybatis 加载到即可,不需要使用注解

###### FieldStrategy

| 值        | 描述                                                        |
| :-------- | :---------------------------------------------------------- |
| IGNORED   | 忽略判断                                                    |
| NOT_NULL  | 非 NULL 判断                                                |
| NOT_EMPTY | 非空判断(只对字符串类型字段,其他类型字段依然为非 NULL 判断) |
| DEFAULT   | 追随全局配置                                                |
| NEVER     | 不加入SQL                                                   |

###### FieldFill

| 值            | 描述                 |
| :------------ | :------------------- |
| DEFAULT       | 默认不处理           |
| INSERT        | 插入时填充字段       |
| UPDATE        | 更新时填充字段       |
| INSERT_UPDATE | 插入和更新时填充字段 |



##### @OrderBy

- 描述：内置 SQL 默认指定排序，优先级低于 wrapper 条件查询

| 属性   | 类型    | 必须指定 | 默认值          | 描述           |
| :----- | :------ | :------- | :-------------- | :------------- |
| isDesc | boolean | 否       | true            | 是否倒序查询   |
| sort   | short   | 否       | Short.MAX_VALUE | 数字越小越靠前 |

**这里的内容都是来自官网，我只取了些常用的**

官网地址：https://baomidou.com/pages/223848/#keysequence

### 创建mapper

```
package com.wgp.demo.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.wgp.demo.bean.User;
import org.apache.ibatis.annotations.Mapper;

/**
 * @Description: UserMapper
 * @Name: UserMapper
 * @Author: wgp
 * @DateTime: 2023/6/15 10:10
 */
@Mapper
public interface UserMapper extends BaseMapper<User> {

}
```

这里使用了使用了`@Mapper`注解就可以不用使用官网的`@MapperScan`个人感觉使用官网的注解不太灵活，不如直接在需要扫描的类上直接加上`@Mapper`当然这个是根据自己的业务所决定的，不是绝对的！

在使用MyBatisplus的mapper必须要继承`BaseMapper<User>`

### 创建Service

```java
package com.wgp.demo.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.wgp.demo.bean.User;

/**
 * @Description: UserService
 * @Name: UserService
 * @Author: wgp
 * @DateTime: 2023/6/15 10:04
 */
public interface UserService extends IService<User> {
}
```

这里的继承也是要写

### 创建ServiceImpl

```java
package com.wgp.demo.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.wgp.demo.bean.User;
import com.wgp.demo.mapper.UserMapper;
import com.wgp.demo.service.UserService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * @Description: UserServiceImpl
 * @Name: UserServiceImpl
 * @Author: wgp
 * @DateTime: 2023/6/15 10:10
 */
@Service
//声明事务
@Transactional(rollbackFor = Exception.class)
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {

}

```

创建Controller

```java
package com.wgp.demo.controller;

import com.wgp.demo.bean.User;
import com.wgp.demo.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @Description: 用户controller
 * @Name: UserController
 * @Author: wgp
 * @DateTime: 2023/6/15 9:54
 */
//声明所有方法返回json
@RestController
//使用lombok注入要使用的类
@RequiredArgsConstructor
@RequestMapping("/user")
public class UserController {

    private final UserService userService;

    /**
     * query 获取全部用户信息
     *
     * @param 
     * @return java.lang.String
     * @author wgp
     * @date 2023/6/15 10:17
     */
    @GetMapping("/list")
    public String query(){
        List<User> list = userService.list();
        return list.toString();
    }
}
```

### 启动项目访问测试链接

```http
GET http://localhost:8081/user/list
```

![image-20230615140746764](image-20230615140746764.png)

这时就可以看见回参了，证明没有问题

{% note success %}
这篇文章主要讲怎么整合和一些插件的使用，至于CRUD的操作，直接访问官网即可，写的非常详细
{% endnote %}

[CRUD 接口 | MyBatis-Plus (baomidou.com)](https://baomidou.com/pages/49cc81/#service-crud-接口)

### 将链接池切换为Druid

```yml
# 端口号
server:
  port: 8081

# 数据库链接
spring:
  datasource:
    # 指定DURID驱动
    type: com.alibaba.druid.pool.DruidDataSource
    #配置连接数据库的各个信息
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/demo?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8&AllowPublicKeyRetrieval=True
    username: demo123
    password: 123321
```

增加配置类

```java
package com.wgp.demo.config;

import com.alibaba.druid.pool.DruidDataSource;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

/**
 * @Description: Druid配置为druid数据源
 * @Name: DruidDataSourceConfig
 * @Author: wgp
 * @DateTime: 2023/6/15 13:44
 */
@Configuration
public class DruidDataSourceConfig {

    @ConfigurationProperties("spring.datasource")
    @Bean
    public DataSource dataSource() {
        DruidDataSource druidDataSource = new DruidDataSource();
        return druidDataSource;
    }
}

```

这时执行项目发现链接池编程druid

![image-20230615141821290](image-20230615141821290.png)

查询结果

![image-20230615142232312](image-20230615142232312.png)

这里的查询结果是接口返回的，但是有个小问题，就是控制台并没有打印sql的执行日志

### mybatis-plus开启sql日志打印

在网上搜了搜，发现日志打印还是又很多种的，这里就汇总下都试一下

#### 直接开启打印

```yml
#开启sql日志
mybatis-plus:
  configuration:
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl 
 
或者：
#关闭sql日志
mybatis-plus:
  configuration:
    log-impl: org.apache.ibatis.logging.nologging.NoLoggingImpl 
```

然后测试链接打印日志

![image-20230615144322289](image-20230615144322289.png)

这个是mybatisplus自带的日志打印，感觉不是很友好，再试试其他的打印方式

#### 引入官方插件

```xml
<!-- https://mvnrepository.com/artifact/p6spy/p6spy -->
<dependency>
    <groupId>p6spy</groupId>
    <artifactId>p6spy</artifactId>
    <version>3.9.1</version>
</dependency>
```

yml配置

```
spring:
  datasource:
    #配置数据源类型
#    type: com.zaxxer.hikari.HikariDataSource
    # 指定DURID驱动
    type: com.alibaba.druid.pool.DruidDataSource
#    #配置连接数据库的各个信息
#    driver-class-name: com.mysql.cj.jdbc.Driver
#    url: jdbc:mysql://39.99.146.124:3306/demo?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8&AllowPublicKeyRetrieval=True
    # 引入官方sql日志打印插件
    driver-class-name: com.p6spy.engine.spy.P6SpyDriver
    url: jdbc:p6spy:mysql://39.99.146.124:3306/demo?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8&AllowPublicKeyRetrieval=True

    username: demo
    password: j2rSZJsEJNFAYwzX
```

spy.properties配置

```perl
#3.2.1以上使用
modulelist=com.baomidou.mybatisplus.extension.p6spy.MybatisPlusLogFactory,com.p6spy.engine.outage.P6OutageFactory
#3.2.1以下使用或者不配置
#modulelist=com.p6spy.engine.logging.P6LogFactory,com.p6spy.engine.outage.P6OutageFactory
# 自定义日志打印
logMessageFormat=com.baomidou.mybatisplus.extension.p6spy.P6SpyLogger
#日志输出到控制台
appender=com.baomidou.mybatisplus.extension.p6spy.StdoutLogger
# 使用日志系统记录 sql
#appender=com.p6spy.engine.spy.appender.Slf4JLogger
# 设置 p6spy driver 代理
deregisterdrivers=true
# 取消JDBC URL前缀
useprefix=true
# 配置记录 Log 例外,可去掉的结果集有error,info,batch,debug,statement,commit,rollback,result,resultset.
excludecategories=info,debug,result,commit,resultset
# 日期格式
dateformat=yyyy-MM-dd HH:mm:ss
# 实际驱动可多个
#driverlist=org.h2.Driver
# 是否开启慢SQL记录
outagedetection=true
# 慢SQL记录标准 2 秒
outagedetectioninterval=2
```

执行方法测试

![image-20230615145923678](image-20230615145923678.png)

这次打印的结果好多了，但是还是不舒服，也不打印查询结果，该插件有性能损耗，不建议生产环境使用。

*官方明确写明了，生产时不要开，**因为很耗资源**，总之根据自己的实际开发需求，二选一吧，如果可以的话也可以自己写拦截器，然后打印sql，这个就视业务情况而定了，这里就不多写了*

### 多数据源

多数据源这里个人认为，在小项目中使用的并不多所以这里就不作展开了，有兴趣可以参考官网对于多数据源的讲解，很清楚。

[多数据源 | MyBatis-Plus (baomidou.com)](https://baomidou.com/pages/a61e1b/)

对于多数据源的注解切换也可以在它本身<span class="label label-primary">@DS</span>的基础上封装

```java
@Target({ ElementType.TYPE, ElementType.METHOD })
@Retention(RetentionPolicy.RUNTIME)
@Documented
@DS("fk")
public @interface Fk {

}
```

这里发个示例就不过多的讲解了

### 分页插件

mybatis-plus的官网对于分页插件这里讲解的不是很深，所以这里详细说下，分页插件的使用

#### 创建分页插件配置类

```java
package com.wgp.demo.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @Description: mybatisplus配置类
 * @Name: MyBatisPlusConfig
 * @Author: wgp
 * @DateTime: 2023/6/15 9:24
 */
@Configuration
public class MybatisPlusConfig {
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        //配置插件类
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        //具体到配置哪一个插件
        interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return interceptor;
    }
}
```

#### yml配置信息

```yml
# MyBatis配置
mybatis-plus:
    # 搜索指定包别名
    typeAliasesPackage: com.**.**.mapper
    # 配置mapper的扫描，找到所有的mapper.xml映射文件
    mapperLocations: classpath*:mapper/**/*Mapper.xml
    # 加载全局的配置文件
    configLocation: classpath:mybatis/mybatis-config.xml
```

这里也可以选择不配置

#### 改造controller方法

```java
    private final UserMapper mapper;

    /**
     * query 获取全部用户信息
     *
     * @param 
     * @return java.lang.String
     * @author wgp
     * @date 2023/6/15 10:17
     */
    @GetMapping("/list")
    public String query(Page page){
        Page page1 = mapper.selectPage(page, null);
        return page1.toString();
    }
```

查询结果

![image-20230615152439721](image-20230615152439721.png)

### 代码生成器

这里的代码生成器的解析官网，我个人看确实有点不明朗，这里我找了篇文章，贴在这里，感觉讲解的很详细

转载自：[(166条消息) MyBatis-Plus代码生成器（新）使用_mybatisplus代码生成器_深情不及里子的博客-CSDN博客](https://blog.csdn.net/qq_42263280/article/details/126531993)

#### 一，MyBatis-Plus基本简介。

MyBatis-Plus，又简称为“MP”，是一个MyBatis的增强工具，在MyBatis原有的使用功能基础上只做增强，不做改变。纯粹为了简化开发，提高效率而生。

为什么需要这样的工具呢？

因为最简单的一点，相比于同类型的数据库框架JPA而言，原生的MyBatis框架在处理JDBC和SQL语句上无疑更为繁琐，因为需要独立编写SQL语句，虽然更加灵活，性能较高，并且易于维护与阅读，但是相较于JPA直接集成jpaRepository省去大部分sql语句而言，开发效率明显不如jpa。所以，产生了MyBatis-plus，在Mybatis的基础上进一步增强了他的功能（理由并不唯一）。

详情可参考MyBatis-plus官方文档：https://baomidou.com/

#### 二，特性

- 无侵入：Mybatis-Plus 在 Mybatis 的基础上进行扩展，只做增强不做改变，引入 Mybatis-Plus 不会对现有的 Mybatis 构架产生任何影响，而且 MP 支持所有 Mybatis 原生的特性
- 依赖少：仅仅依赖 Mybatis 以及 Mybatis-Spring
- 损耗小：启动即会自动注入基本CURD，性能基本无损耗，直接面向对象操作
- 预防Sql注入：内置Sql注入剥离器，有效预防Sql注入攻击
- 通用CRUD操作：内置通用 Mapper、通用 Service，仅仅通过少量配置即可实现单表大部分 CRUD 操作，更有强大的条件构造器，满足各类使用需求
- 多种主键策略：支持多达4种主键策略（内含分布式唯一ID生成器），可自由配置，完美解决主键问题
- 支持ActiveRecord：支持 ActiveRecord 形式调用，实体类只需继承 Model 类即可实现基本 CRUD 操作
- 支持代码生成：采用代码或者 Maven 插件可快速生成 Mapper 、 Entity、 Service 、 Controller 层代码，支持模板引擎，更有超多自定义配置等您来使用（P.S. 比 Mybatis 官方的 Generator 更加强大！）
- 支持自定义全局通用操作：支持全局通用方法注入（ Write once, use anywhere ）
  支持关键词自动转义：支持数据库关键词（order、key……）自动转义，还可自定义关键词
- 内置分页插件：基于Mybatis物理分页，开发者无需关心具体操作，配置好插件之后，写分页等同于普通List查询
- 内置性能分析插件：可输出Sql语句以及其执行时间，建议开发测试时启用该功能，能有效解决慢查询
- 内置全局拦截插件：提供全表 delete 、 update 操作智能分析阻断，预防误操作

#### 三，实现代码自动生成工具

虽然IDEA中一些类似于easycode，RestfulToolkitX Code等插件也能实现代码自动生成，但是他们并不全面，而且缺乏灵活度。而MyBatis-Plus比他们更全面，虽然需要我们自己编写一些配置代码，但是在构建Springboot项目中，通过代码自动生成，直接构建出项目全面的基本结构。例如常用的POJO，DAO，Service，Service实现类，Controller层以及mapper.xml文件 ，并且在service中继承了封装好的IService类，一般的sql和实现类基本不用书写就能在controller中调用，并且我们还可以自己编辑自己的业务SQL语句，可谓相当灵活！话不多，直接上过程：

##### 3.1，准备一个初始项目，数据表，连接好数据库

![img](43aae33f0b3042659bd8fa4e1bf931a9.png)

#####  3.2，导入Mybatis-Plus相关依赖

```xml
<!--        mybatis-plus依赖-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.5.1</version>
        </dependency>
<!--        MP代码生成器依赖-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-generator</artifactId>
            <version>3.5.1</version>
        </dependency>
<!--        模板引擎依赖-->
        <dependency>
            <groupId>org.apache.velocity</groupId>
            <artifactId>velocity-engine-core</artifactId>
            <version>2.3</version>
        </dependency>
```


由于项目依赖于springboot，还需要数据库，数据表。因次，需要使用到的相关注解依赖也要一并引入，如果没有用到，可自行添减。

```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <!--        swagger依赖-->
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-boot-starter</artifactId>
            <version>3.0.0</version>
        </dependency>
```

##### 3.3，配置数据库配置文件application.yml

```yml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    password: 123456
    username: root
    url: jdbc:mysql://localhost:3306?test_user&useSSL=true&useUnicode=true&characterEncoding=utf-8&serverTimezone=UTC
 
server:
  port: 8086
```

##### 3.4，构建代码自动生成工具类，其他更多的配置可参考官网=》[苞米豆](https://baomidou.com/)

```java
package com.wgp.demo.config;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.*;
import com.baomidou.mybatisplus.generator.config.querys.MySqlQuery;
import com.baomidou.mybatisplus.generator.config.rules.DateType;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

import java.util.Collections;

/**
 * @Description: mybatisplus 代码生成器配置
 * @Name: CodeGeneration
 * @Author: wgp
 * @DateTime: 2023/6/16 9:47
 */
public class CodeGeneration {
    public static void main(String[] args) {
        /**
         * 先配置数据源
         */
        MySqlQuery mySqlQuery = new MySqlQuery() {
            @Override
            public String[] fieldCustom() {
                return new String[]{"Default"};
            }
        };



        DataSourceConfig dsc = new DataSourceConfig.Builder("jdbc:mysql://39.99.146.124:3306/demo?serverTimezone=UTC&useUnicode=true&characterEncoding=utf-8&AllowPublicKeyRetrieval=True","demo","j2rSZJsEJNFAYwzX")
                .dbQuery(mySqlQuery).build();
        //通过datasourceConfig创建AutoGenerator
        AutoGenerator generator = new AutoGenerator(dsc);

        /**
         * 全局配置
         */
        String projectPath = System.getProperty("user.dir"); //获取项目路径
        String filePath = projectPath + "/src/main/java";  //java下的文件路径
        GlobalConfig global = new GlobalConfig.Builder()
                .outputDir(filePath)//生成的输出路径
                .author("wgp")//生成的作者名字
                //.enableSwagger()//开启swagger，需要添加swagger依赖并配置
                .dateType(DateType.TIME_PACK)//时间策略
                .commentDate("yyyy年MM月dd日")//格式化时间格式
                .disableOpenDir()//禁止打开输出目录，默认false
                .fileOverride()//覆盖生成文件
                .build();

        /**
         * 包配置
         */
        PackageConfig packages = new PackageConfig.Builder()
                .entity("bean")//实体类包名
                .parent("com.wgp.demo")//父包名。如果为空，将下面子包名必须写全部， 否则就只需写子包名
                .controller("controller")//控制层包名
                .mapper("dao")//mapper层包名
                .xml("mapper.xml")//数据访问层xml包名
                .service("service")//service层包名
                .serviceImpl("service.impl")//service实现类包名
                .other("output")//输出自定义文件时的包名
                .pathInfo(Collections.singletonMap(OutputFile.mapperXml, projectPath + "/src/main/resources/mapper")) //路径配置信息,就是配置各个文件模板的路径信息,这里以mapper.xml为例
                .build();
        /**
         * 模板配置
         */

        // 如果模板引擎是 freemarker
//        String templatePath = "/templates/mapper.xml.ftl";
//         如果模板引擎是 velocity
        // String templatePath = "/templates/mapper.xml.vm";



        TemplateConfig template = new TemplateConfig.Builder()
//            .disable()//禁用所有模板
                //.disable(TemplateType.ENTITY)禁用指定模板
//                .service(filePath + "/service.java")//service模板路径
//                .serviceImpl(filePath + "/service/impl/serviceImpl.java")//实现类模板路径
//                .mapper(filePath + "/mapper.java")//mapper模板路径
//                .mapperXml("/templates/mapper.xml")//xml文件模板路路径
//                .controller(filePath + "/controller")//controller层模板路径
                .build();

        /**
         * 注入配置,自定义配置一个Map对象
         */
//    Map<String,Object> map = new HashMap<>();
//        map.put("name","wgp");
//        map.put("age","22");
//        map.put("sex","男");
//        map.put("description","深情不及黎治跃");
//
//    InjectionConfig injectionConfig = new InjectionConfig.Builder()
//            .customMap(map)
//            .build();

        /**
         * 策略配置开始
         */
        StrategyConfig strategyConfig = new StrategyConfig.Builder()
                .enableCapitalMode()//开启全局大写命名
                //.likeTable()模糊表匹配
                .addInclude()//添加表匹配，指定要生成的数据表名，不写默认选定数据库所有表
                //.disableSqlFilter()禁用sql过滤:默认(不使用该方法）true
                //.enableSchema()启用schema:默认false

                .entityBuilder() //实体策略配置
                //.disableSerialVersionUID()禁用生成SerialVersionUID：默认true
                .enableChainModel()//开启链式模型
                .enableLombok()//开启lombok
                .enableRemoveIsPrefix()//开启 Boolean 类型字段移除 is 前缀
                .enableTableFieldAnnotation()//开启生成实体时生成字段注解
                //.addTableFills()添加表字段填充
                .naming(NamingStrategy.underline_to_camel)//数据表映射实体命名策略：默认下划线转驼峰underline_to_camel
                .columnNaming(NamingStrategy.underline_to_camel)//表字段映射实体属性命名规则：默认null，不指定按照naming执行
                .idType(IdType.AUTO)//添加全局主键类型
                .formatFileName("%s")//格式化实体名称，%s取消首字母I
                .build()

                .mapperBuilder()//mapper文件策略
                .enableMapperAnnotation()//开启mapper注解
                .enableBaseResultMap()//启用xml文件中的BaseResultMap 生成
                .enableBaseColumnList()//启用xml文件中的BaseColumnList
                //.cache(缓存类.class)设置缓存实现类
                .formatMapperFileName("%sMapper")//格式化Dao类名称
                .formatXmlFileName("%sMapper")//格式化xml文件名称
                .build()

                .serviceBuilder()//service文件策略
                .formatServiceFileName("%sService")//格式化 service 接口文件名称
                .formatServiceImplFileName("%sServiceImpl")//格式化 service 接口文件名称
                .build()

                .controllerBuilder()//控制层策略
                //.enableHyphenStyle()开启驼峰转连字符，默认：false
                .enableRestStyle()//开启生成@RestController
                .formatFileName("%sController")//格式化文件名称
                .build();
        /*至此，策略配置才算基本完成！*/

        /**
         * 将所有配置项整合到AutoGenerator中进行执行
         */


        generator.global(global)
                .template(template)
//                .injection(injectionConfig)
                .packageInfo(packages)
                .strategy(strategyConfig)
                .execute();
    }
}

```

执行完成后即可看到我们相关的文件已经全部生成，并且注解，介绍已经基本到位。这样就能为我们的开发节省很多时间。 

![img](2f19973d67e3428fbcf15c14f09db953.png)

#### 四，新旧代码生成器简单分析及补充

##### 4.1，源码上的简单分析

通过源码可以看到旧版本是通过实现不同配置类的实现类，实列化后的配置对象陆续设置我们所需要的配置后，最后通过AutoGenerator 执行execute方法实现。

![img](2c51c26866774e12bd232aab65ce8ee5.png)

 但是新版本的代码生成器明显有了结构上的变化。

![img](b3c67e193ce241fe963d35f5e1fb900e.png)

 很多配置类采用单例模式的方法，用pricate修饰了构造器，主要用于执行代码生成器的AutoGenerator类必须通过将配置好的DataSourceConfig类传给它才能实现实列化，也就是说优先处理数据源配置。至于其他策略，全局配置则采用了建造者模式，通过Bulider().Build()来进行配置类实例化。这样在一些ture or false的配置上省了很多功夫，用户需要使用时就调用其方法即可，不用设置true or false。发挥了单例模式和建造者模式的优势，值得我们学习参考。

##### 4.2，模板配置TemplateConfig说明。

模板配置决定了代码生成的代码模板，一般情况下导入了模板引擎，然后执行模板配置即可，不需要我们额外自己配置。当然，该类也可以让我们自定义模板配置，可以 copy 源码 mybatis-plus/src/main/resources/template 下面内容修改， 放置到自己的项目src/main/resources/template 目录下。当然这个笔者没有过多研究，大家去自行参考学习。

![img](64d82eba2aea4836907efd4551fe1d4d.png)

>   // 如果模板引擎是 freemarker
>        String templatePath = "/templates/mapper.xml.ftl";
>        // 如果模板引擎是 velocity
>        // String templatePath = "/templates/mapper.xml.vm"; 

新版的代码生成器并未有过多说明，但是不配置并不会影响代码生成的正常执行，官方旧版上有一定的使用说明，可供大家学习参考。

如有不足之处欢迎指出~

补充

有小伙伴反馈mapper.xml文件一直在java下的目录生成，放在资源目录下需要Ctrl+X,V比较麻烦，不做修改就得在pom中配置build，导出src/main/java下的mapper.xml文件，上面我已作出修改了，在包配置下自定义xml文件生成路径即可。

> pathInfo(Collections.singletonMap(OutputFile.xml, projectPath + "/src/main/resources/mapper"))

```java
package com.wgpqw.generator;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.generator.FastAutoGenerator;
import com.baomidou.mybatisplus.generator.config.OutputFile;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

import java.util.Collections;

/**
 * @Description: 代码生成器
 * @Name: CodeGeneration
 * @Author: wgp
 * @DateTime: 2023/7/5 11:00
 */
public class CodeGeneration {

    public static void main(String[] args) {
        generation("demo","user","role","role_menu","menu","user_role");
    }

    public static void generation(String databaseName,String... tableName){
        FastAutoGenerator.create("jdbc:mysql://39.99.146.124:3306/"+databaseName+"?&useSSL=true&useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai","demo","j2rSZJsEJNFAYwzX")
                //全局配置(GlobalConfig)
                .globalConfig(builder -> {
                    builder.author("wgp")
                            //启用swagger
                            //.enableSwagger()
                            // 覆盖已生成文件
                            .fileOverride()
                            //指定输出目录
                            .outputDir(System.getProperty("user.dir")+"/src/main/java")
                            //禁止打开指定目录
                            .disableOpenDir();
                })
                //包配置(PackageConfig)
                .packageConfig(builder -> {
                    builder.entity("entity")//实体类包名
                            .parent("com.wgpqw.web")//父包名。如果为空，将下面子包名必须写全部， 否则就只需写子包名
                            .controller("controller")//控制层包名
                            .mapper("mapper")//mapper层包名
                            //.other("dto")//生成dto目录 可不用
                            .service("service")//service层包名
                            .serviceImpl("service.impl")//service实现类包名
                            //自定义mapper.xml文件输出目录
                            .pathInfo(Collections.singletonMap(OutputFile.xml,System.getProperty("user.dir")+"/src/main/resources/mapper"));
                })
                //策略配置(StrategyConfig)
                .strategyConfig(builder -> {
                    //设置要生成的表名
                    builder.addInclude(tableName)
                            //设置表前缀过滤
                            .addTablePrefix("sys_")
                            .entityBuilder()
                            .enableLombok()
                            .enableChainModel()
                            .naming(NamingStrategy.underline_to_camel)//数据表映射实体命名策略：默认下划线转驼峰underline_to_camel
                            .columnNaming(NamingStrategy.underline_to_camel)//表字段映射实体属性命名规则：默认null，不指定按照naming执行
                            .idType(IdType.AUTO)//添加全局主键类型
                            .formatFileName("%s")//格式化实体名称，%s取消首字母I,
                            .mapperBuilder()
                            .enableMapperAnnotation()//开启mapper注解
                            .enableBaseResultMap()//启用xml文件中的BaseResultMap 生成
                            .enableBaseColumnList()//启用xml文件中的BaseColumnList
                            .formatMapperFileName("%sMapper")//格式化Dao类名称
                            .formatXmlFileName("%sMapper")//格式化xml文件名称
                            .enableFileOverride()//设置mapper允许覆盖
                            .serviceBuilder()
                            .formatServiceFileName("%sService")//格式化 service 接口文件名称
                            .formatServiceImplFileName("%sServiceImpl")//格式化 service 接口文件名称
                            .enableFileOverride()//设置service允许覆盖
                            .controllerBuilder()
                            .enableRestStyle();
                })
//                .injectionConfig(consumer -> {
//            Map<String, String> customFile = new HashMap<>();
//            // 配置DTO（需要的话）但是需要有能配置Dto的模板引擎，比如freemarker，但是这里我们用的VelocityEngine，因此不多作介绍
//            customFile.put("DTO.java", "/templates/entityDTO.java.ftl");
//            consumer.customFile(customFile);
//           })
                .execute();
    }

}

```

