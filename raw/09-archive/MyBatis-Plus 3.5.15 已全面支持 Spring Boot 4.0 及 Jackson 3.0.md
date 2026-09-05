---
title: "MyBatis-Plus 3.5.15 已全面支持 Spring Boot 4.0 及 Jackson 3.0"
source: "https://mp.weixin.qq.com/s/iBsUC3TU5lEp8K_kxVekLg"
---
小锋 java1234 *2026年9月3日 09:06*

大家好，我是锋哥。

> MyBatis-Plus `3.5.15` 版本，更新不大，但两件事很实在：能跟 Spring Boot 4.0 一起跑了，JSON 字段也能用上 Jackson 3。今天锋哥和大家好好聊聊 MyBatis-Plus 3.5.15 这个版本。

---

![图片](assets/MyBatis-Plus%203.5.15%20%E5%B7%B2%E5%85%A8%E9%9D%A2%E6%94%AF%E6%8C%81%20Spring%20Boot%204.0%20%E5%8F%8A%20Jackson%203.0/f7ada2c06d97d0791c287dfbc5f8010e_MD5.webp)

## 目录

- 先说一句：MyBatis-Plus 是干什么的
- 这次版本到底改了什么
- Spring Boot 4 项目怎么接
- JSON 字段换成 Jackson 3
- 升级时容易踩的坑

---

## 先说一句：MyBatis-Plus 是干什么的

如果你写过纯 MyBatis，大概体会过这种感觉：一张表的增删改查，Mapper 接口加 XML 能写老长一截。条件一多，XML 里全是 `<if test>` ，字段名改了还得全文搜。

MyBatis-Plus 就是在 MyBatis 上面加了一层常用能力。官方那句「只做增强、不做改变」听着像口号，实际体验很直接：原来怎么写 XML，现在还能怎么写；不想写的部分，交给它。

日常用得最多的大概就这几样：

- `BaseMapper` ：单表增删改查不用自己写
- `LambdaQueryWrapper` ：条件用 `User::getUsername` 这种方式写，字段名写错编译期就能发现
- 分页插件：你查列表，它帮你拼分页 SQL
- 代码生成器：表结构出来后，Entity、Mapper、Service 一把生成

说白了，它不是要替换 MyBatis，而是把那些每个项目都在重复写的东西收掉。

![图片](assets/MyBatis-Plus%203.5.15%20%E5%B7%B2%E5%85%A8%E9%9D%A2%E6%94%AF%E6%8C%81%20Spring%20Boot%204.0%20%E5%8F%8A%20Jackson%203.0/95e0dbff4f47d1db2d43711248cfe0fb_MD5.jpg)

---

## 这次版本到底改了什么

`3.5.15` 的更新日志不长。真正会碰到手的，主要是这两项：

**一是跟上 Spring Boot 4.0。** Boot 4 不是小版本升级，Starter 的 Maven 坐标都换了。以前 Boot 3 那套 `mybatis-plus-spring-boot3-starter` 直接丢进 Boot 4 项目，自动配置对不上。这次官方把 Boot 4 的 Starter 补齐了。

**二是支持 Jackson 3。** Jackson 3 把核心包从 `              com.fasterxml.jackson            ` 挪到了 `              tools.jackson            ` ，老的 `JacksonTypeHandler` 吃的还是 Jackson 2。新项目如果已经上 Jackson 3，JSON 列就该用新的 `Jackson3TypeHandler` 。

除此之外还有几处边角，用得到再关心就行：代码生成器的元数据构建调整了一下；Enjoy 模板生成 XML 的 bug 修了； `CrudRepository` 批量操作时，不在事务里会更及时地关掉连接。

两件大事凑在一个小版本里，对准备尝鲜 Boot 4 的人其实挺友好——Mapper 还是那个 Mapper，不用重新学一套写法。

![图片](assets/MyBatis-Plus%203.5.15%20%E5%B7%B2%E5%85%A8%E9%9D%A2%E6%94%AF%E6%8C%81%20Spring%20Boot%204.0%20%E5%8F%8A%20Jackson%203.0/4c5469072c4056e36d89daedbf12653e_MD5.jpg)

整条链路可以看成这样：

![图片](assets/MyBatis-Plus%203.5.15%20%E5%B7%B2%E5%85%A8%E9%9D%A2%E6%94%AF%E6%8C%81%20Spring%20Boot%204.0%20%E5%8F%8A%20Jackson%203.0/e2a354036d4fb9665dddaa95213eaa4e_MD5.png)

---

## Spring Boot 4 项目怎么接

先记住一件事： **Boot 版本和 Starter 是绑死的，别混用。**

| 你用的 Spring Boot | 该引的 Starter |
| --- | --- |
| [2.x](http://2.x/) | `mybatis-plus-boot-starter` |
| [3.x](http://3.x/) | `mybatis-plus-spring-boot3-starter` |
| [4.x](http://4.x/) | `mybatis-plus-spring-boot4-starter` |

名字差一个数字，自动配置完全不是一套。Boot 4 项目里继续引 Boot 3 的包，启动阶段就会很尴尬。

### Maven 依赖

```xml
<parent>    <groupId>
            org.springframework.boot
          </groupId>    <artifactId>spring-boot-starter-parent</artifactId>    <version>4.0.0</version></parent>
<dependencies>    <!-- 注意：这里是 boot4，不是 boot3 -->    <dependency>        <groupId>
            com.baomidou
          </groupId>        <artifactId>mybatis-plus-spring-boot4-starter</artifactId>        <version>3.5.15</version>    </dependency>    <dependency>        <groupId>
            com.mysql
          </groupId>        <artifactId>mysql-connector-j</artifactId>    </dependency></dependencies>
```

### 数据源随便配一份

```go
spring:  datasource:    url: jdbc:mysql://127.0.0.1:3306/db_demo?useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Shanghai    username: root    password: 123456
mybatis-plus:  configuration:    map-underscore-to-camel-case: true    log-impl: 
            org.apache.ibatis.logging.stdout.StdOutImpl
            global-config:    db-config:      id-type: auto
```

### 实体、Mapper、查一条数据

写法跟以前几乎一样。下面这个例子对应表 `t_user` ，没使用 Lombok，getter / setter 自己写。

```typescript
/** * 用户实体，对应表 t_user */@TableName("t_user")public class User {
    /** 主键 */    @TableId(type = IdType.AUTO)    private Long id;
    /** 用户名 */    private String username;
    /** 密码，示例环境用明文 123456 */    private String password;
    /** 性别，默认男 */    private String gender;
    /** 创建时间 */    private LocalDateTime createTime;
    public Long getId() {        return id;    }
    public void setId(Long id) {        this.id = id;    }
    public String getUsername() {        return username;    }
    public void setUsername(String username) {        this.username = username;    }
    public String getPassword() {        return password;    }
    public void setPassword(String password) {        this.password = password;    }
    public String getGender() {        return gender;    }
    public void setGender(String gender) {        this.gender = gender;    }
    public LocalDateTime getCreateTime() {        return createTime;    }
    public void setCreateTime(LocalDateTime createTime) {        this.createTime = createTime;    }}
```

Mapper 还是空接口，继承 `BaseMapper` 就够用：

```cs
/** * 用户表 Mapper */public interface UserMapper extends BaseMapper<User> {}
```

查用户名对应的那一条，用 Lambda 写条件就行：

```cpp
/** * 按用户名查询用户 */@Servicepublic class UserService {
    private final UserMapper userMapper;
    public UserService(UserMapper userMapper) {        this.userMapper = userMapper;    }
    /**     * 用方法引用写条件，少手敲列名     */    public User findByUsername(String username) {        return userMapper.selectOne(new LambdaQueryWrapper<User>()                .eq(User::getUsername, username)                .last("LIMIT 1"));    }}
```

启动类、 `@MapperScan` 这些，跟 Boot 3 没多大差别。真正要改的，往往就那一行依赖：换成 `mybatis-plus-spring-boot4-starter` 。

---

## JSON 字段换成 Jackson 3

很多表会留一列存扩展信息，比如用户的城市、标签，不想为此再拆一张表。以前 Jackson 2 用 `JacksonTypeHandler` ，现在 Jackson 3 对应的是 `Jackson3TypeHandler` 。

它干的事情很朴素：写入时把对象变成 JSON 字符串，查出来再转回对象。

![图片](assets/MyBatis-Plus%203.5.15%20%E5%B7%B2%E5%85%A8%E9%9D%A2%E6%94%AF%E6%8C%81%20Spring%20Boot%204.0%20%E5%8F%8A%20Jackson%203.0/b33b630991df6bdf1c491675b68f9360_MD5.jpg)

### 先准备一个扩展信息类

```typescript
/** * 用户扩展信息，最终会写成 JSON 存进 
            t_user.extra_info
           */public class ExtraInfo {
    /** 城市 */    private String city;
    /** 标签列表 */    private List<String> tags;
    public String getCity() {        return city;    }
    public void setCity(String city) {        this.city = city;    }
    public List<String> getTags() {        return tags;    }
    public void setTags(List<String> tags) {        this.tags = tags;    }}
```

### 挂到实体字段上

这里有个容易漏的地方： `@TableName` 上要加 `autoResultMap = true` 。不加的话，查出来的 JSON 列不会走类型处理器，字段可能是空的，或者还是原始字符串。

```typescript
/** * 带 JSON 扩展字段的用户实体 */@TableName(value = "t_user", autoResultMap = true)public class User {
    @TableId(type = IdType.AUTO)    private Long id;
    private String username;
    /**     * 用 Jackson 3 读写 extra_info 列     */    @TableField(typeHandler = Jackson3TypeHandler.class)    private ExtraInfo extraInfo;
    public Long getId() {        return id;    }
    public void setId(Long id) {        this.id = id;    }
    public String getUsername() {        return username;    }
    public void setUsername(String username) {        this.username = username;    }
    public ExtraInfo getExtraInfo() {        return extraInfo;    }
    public void setExtraInfo(ExtraInfo extraInfo) {        this.extraInfo = extraInfo;    }}
```

### 插入一条看看

```cs
/** * 保存带 JSON 扩展信息的用户 */public void saveUser() {    ExtraInfo extraInfo = new ExtraInfo();    
            extraInfo.setCity(
          "上海");    
            extraInfo.setTags(Arrays.asList(
          "vip", "spring-boot4"));
    User user = new User();    
            user.setUsername(
          "admin");    
            user.setPassword(
          "123456");    
            user.setGender(
          "男");    
            user.setExtraInfo(extraInfo);
              
            userMapper.insert(user);
          }
```

插进去之后， `extra_info` 列大概长这样：

```json
{"city":"上海","tags":["vip","spring-boot4"]}
```

项目里如果已经配过自己的 Jackson 3 `ObjectMapper` （日期格式、忽略空字段之类），最好在启动时塞给 Handler，别让它再 new 一份默认的：

```perl
/** * 复用 Spring 容器里的 ObjectMapper */@Configurationpublic class Jackson3Config {
    public Jackson3Config(ObjectMapper objectMapper) {        
            Jackson3TypeHandler.setObjectMapper(objectMapper);
              }}
```

还有个包名问题，建议复制的时候盯一眼：Jackson 3 的 `ObjectMapper` 在 `              tools.jackson.databind            ` 下面。如果手滑 import 成了 `              com.fasterxml.jackson.databind.ObjectMapper            ` ，编译也许能过，跑起来 TypeHandler 会对不上。

---

## 升级时容易踩的坑

**Starter 选错。** 这是最常见的。Boot 4 必须用 `mybatis-plus-spring-boot4-starter` 。包能下下来不代表能启动，自动配置对不上时，报错往往不在 MyBatis-Plus 自己身上，排查会绕一会儿。

**JSON 处理器和 Jackson 版本要匹配。** 实体写了 `Jackson3TypeHandler` ，classpath 里就得是 Jackson 3。老项目还停在 Jackson 2，继续用原来的 `JacksonTypeHandler` 就行，没必要为了新类名硬升。

**启动时报 `factoryBeanObjectType` 。** 有人在 `3.5.15` + Boot 4 组合下碰到过：

```bash
Invalid value type for attribute 'factoryBeanObjectType': 
            java.lang.String
```

多半是带进来的 `mybatis-spring` 偏旧。可以在 pom 里显式指定 `              org.mybatis:mybatis-spring:4.0.0            ` 。后面的 `3.5.16` 已经在 Boot 4 Starter 里把这个依赖升上去了，生产环境如果卡在这，升级一小步往往比自己排除依赖更省事。

**用了代码生成器。** 这次元数据构建有调整，Enjoy 模板生成 XML 的问题也修了。升完版本后，拿一张表重新生成一次，跟手里现有的 Mapper XML 对比一下更稳妥。

---