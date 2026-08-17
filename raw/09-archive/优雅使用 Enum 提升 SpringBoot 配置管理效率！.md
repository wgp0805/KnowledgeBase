---
title: "优雅使用 Enum 提升 SpringBoot 配置管理效率！"
source: "https://mp.weixin.qq.com/s/TM8o96cbBDcKZevS5-qSMw"
---
小哈学Java *2026年8月17日 15:07*

![图片](assets/%E4%BC%98%E9%9B%85%E4%BD%BF%E7%94%A8%20Enum%20%E6%8F%90%E5%8D%87%20SpringBoot%20%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E6%95%88%E7%8E%87%EF%BC%81/42dc8bcbda19d95edadd38fd505cd90f_MD5.webp)

来源： [https://juejin.cn/post/7459363593475326002](https://juejin.cn/post/7459363593475326002)

**目录**

- 业务背景
- 配置管理的重要性
- 枚举类的应用
- 具体示例
- 项目依赖 （ [pom.xml）](http://pom.xml\)/)
	- 配置文件 （ [application.yml）](http://application.yml\)/)
	- 定义枚举类 （ [UserTypeEnum.java）](http://usertypeenum.java\)/)
	- 配置类 （ [AppConfig.java）](http://appconfig.java\)/)
	- 控制器 （ [UserController.java）](http://usercontroller.java\)/)
	- Thymeleaf 前端页面 （ [user-types.html）](http://user-types.html\)/)

---

![优雅使用 Enum](assets/%E4%BC%98%E9%9B%85%E4%BD%BF%E7%94%A8%20Enum%20%E6%8F%90%E5%8D%87%20SpringBoot%20%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E6%95%88%E7%8E%87%EF%BC%81/26b7f9bf25fc6df583ddcfcb39a36fce_MD5.webp)

优雅使用 Enum

## 业务背景

在软件开发中，配置管理是确保应用程序能够在不同环境中灵活运行的关键环节。对于 Spring Boot 项目，配置文件（如 `              application.yml            ` 或 `              application.properties            ` ）通常用于存储各种配置项，如数据库连接信息、服务端口、API 密钥等。然而，随着业务逻辑的复杂化，直接使用字符串或数字作为配置项可能会导致代码的可读性和可维护性下降。

枚举类（Enum）提供了一种将一组固定的值封装在一起的方法，这不仅提高了代码的可读性，还能避免硬编码（ `magic number` ）带来的潜在问题。通过将业务中的固定状态、类型等内容定义为枚举，可以使得代码更加严谨和可维护。例如，用户角色、订单状态、支付方式等都可以通过枚举来管理。

在实际业务中，可能需要根据不同的环境或配置动态调整这些枚举值。 `@ConfigurationProperties` 注解允许开发者将外部配置文件中的内容映射到 Java 类中，从而实现配置的动态管理。结合枚举类和 `@ConfigurationProperties` ，可以实现一种高效、灵活且易于维护的配置管理方式。

## 配置管理的重要性

在 Spring Boot 项目中，配置管理通常通过 `              application.yml            ` 或 `              application.properties            ` 文件来实现。这些文件可以存储不同环境的配置信息，如数据库连接、服务器端口等。然而，随着业务逻辑的复杂化，直接使用字符串或数字作为配置项会带来以下问题：

- **可读性差：** 代码中直接使用字符串或数字，难以理解其含义。
- **维护成本高：** 修改配置时需要在多处查找和替换，容易出错。
- **硬编码问题：** 直接使用字符串或数字容易导致潜在的错误。

## 枚举类的应用

Enum 在 Java 中是一种特殊的数据类型，它允许开发者定义一组常量。

在实际业务中，Enum 通常用于表示业务中的固定状态、类型等内容，如用户角色、订单状态、支付方式等。

通过将这些常量定义在枚举中，不仅可以提高代码的可读性，还能避免硬编码（ `magic number` ）带来的潜在问题。

结合 `@ConfigurationProperties` 注解，开发者可以将外部配置文件中的内容映射到 Java 类中。

这使得配置管理更加灵活、易于维护，特别是对于较为复杂的配置结构，如枚举值的配置管理。

![配置管理与 Java Enum 应用示意图](assets/%E4%BC%98%E9%9B%85%E4%BD%BF%E7%94%A8%20Enum%20%E6%8F%90%E5%8D%87%20SpringBoot%20%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E6%95%88%E7%8E%87%EF%BC%81/370db696a5db62730bdf0ae7a1468e89_MD5.jpg)

配置管理与 Java Enum 应用示意图

## 具体示例

文章通过一个具体的示例展示了如何在 Spring Boot 项目中结合 Enum 和 `@ConfigurationProperties` 实现配置化管理。示例包括以下几个部分：

- **项目依赖：** 使用 Maven 的 `              pom.xml            ` 文件定义项目依赖，包括 `Spring Boot Starter Web` 、 `Thymeleaf` 模板引擎和 Lombok。
- **配置文件：** 在 [application.yml](http://application.yml/) 文件中定义用户类型的配置。
- **枚举类：** 定义一个 `UserTypeEnum` 枚举类，包含三种用户类型及其描述。
- **配置类：** 使用 `@ConfigurationProperties` 注解将配置文件中的内容映射到 Java 类中。
- **控制器：** 创建一个控制器类 `UserController` ，用于处理 `/user-types` 请求，并将用户类型的描述传递到前端。
- **前端页面：** 使用 Thymeleaf 模板引擎渲染从后端传递过来的数据，展示用户类型的描述。

### 项目依赖 （ pom.xml）

```
<dependencies>
    <!-- Spring Boot Starter Web -->
    <dependency>
        
            org.springframework.boot
          
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <!-- Thymeleaf 模板引擎 -->
    <dependency>
        
            org.springframework.boot
          
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>

    <!-- Lombok 用于简化 Java 代码 -->
    <dependency>
        
            org.projectlombok
          
        <artifactId>lombok</artifactId>
        <scope>provided</scope>
    </dependency>

    <!-- Spring Boot Starter Validation 用于参数校验 -->
    <dependency>
        
            org.springframework.boot
          
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>

    <!-- Spring Boot DevTools 用于开发时的热部署 -->
    <dependency>
        
            org.springframework.boot
          
        <artifactId>spring-boot-devtools</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

### 配置文件 （ application.yml）

```
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/your_database
    username: your_username
    password: your_password
  server:
    port: 8080

app:
  user-type:
    admin: ADMIN
    user: USER
    guest: GUEST
```

### 定义枚举类 （ UserTypeEnum.java）

```
public enum UserTypeEnum {
    ADMIN("管理员"),
    USER("普通用户"),
    GUEST("游客"),
    VIP("VIP用户"),
    MODERATOR("版主");

    private final String description;

    UserTypeEnum(String description) {
        
            this.description
           = description;
    }

    public String getDescription() {
        return description;
    }
}
```

#### 详细说明

- `UserTypeEnum` 是一个枚举类，定义了三种用户类型：管理员（ `ADMIN` ）、普通用户（ `USER` ）和游客（ `GUEST` ）。
- 每种用户类型都有一个描述（ `description` ），用于提供对应的中文描述。
- 枚举常量声明：
- ADMIN 对应 "管理员"。
	- USER 对应 "普通用户"。
	- GUEST 对应 "游客"。
- 构造函数 `UserTypeEnum(String description)` 用于初始化枚举常量的描述。
- `getDescription` 方法返回对应的描述。

### 配置类 （ AppConfig.java）

使用 `@ConfigurationProperties` 注解将配置文件中的内容映射到 Java 类中，并使用 Enum 来表示这些配置项。

```
import 
            org.springframework.boot.context.properties.ConfigurationProperties;
          
import 
            org.springframework.stereotype.Component;
          

import 
            com.icoderoad.enumconfig.enums.UserTypeEnum;
          

import 
            lombok.Data;
          

@Data
@Component
@ConfigurationProperties(prefix = "app")
public class AppConfig {
    private UserType userType;
    private Database database;
    private Server server;

    @Data
    public static class UserType {
        private UserTypeEnum admin;
        private UserTypeEnum user;
        private UserTypeEnum guest;
        private UserTypeEnum vip;
        private UserTypeEnum moderator;
    }

    @Data
    public static class Database {
        private String url;
        private String username;
        private String password;
    }

    @Data
    public static class Server {
        private int port;
    }
}
```

#### 详细说明

- `AppConfig` 类是一个 Spring 配置类，用于加载和存储应用程序配置。
- `@Data` 注解来自 Lombok，自动生成 `getter` 、 `setter` 、 `toString` 、 `equals` 和 `hashCode` 方法。
- `@Component` 注解将类标记为 Spring 组件，以便在 Spring 容器中进行管理。
- `@ConfigurationProperties(prefix = "app")` 注解将类标记为配置属性类，并指定配置前缀为 "app"。
- `AppConfig` 类包含一个嵌套的静态类 `UserType` ，用于定义用户类型的配置：
- admin 对应管理员用户类型。
	- user 对应普通用户类型。
	- guest 对应游客用户类型。

### 控制器 （ UserController.java）

创建一个控制器来展示如何使用从配置中读取到的枚举值。

```
import 
            com.example.demo.config.AppConfig;
          
import 
            org.springframework.beans.factory.annotation.Autowired;
          
import 
            org.springframework.stereotype.Controller;
          
import 
            org.springframework.ui.Model;
          
import 
            org.springframework.web.bind.annotation.GetMapping;
          

@Controller
public class UserController {

    @Autowired
    private AppConfig appConfig;

    @GetMapping("/user-types")
    public String getUserTypes(Model model) {
        
            model.addAttribute(
          "adminType", 
            appConfig.getUserType().getAdmin().getDescription());
          
        
            model.addAttribute(
          "userType", 
            appConfig.getUserType().getUser().getDescription());
          
        
            model.addAttribute(
          "guestType", 
            appConfig.getUserType().getGuest().getDescription());
          
        
            model.addAttribute(
          "vipType", 
            appConfig.getUserType().getVip().getDescription());
          
        
            model.addAttribute(
          "moderatorType", 
            appConfig.getUserType().getModerator().getDescription());
          
        return "index";
    }
}
```

#### 详细说明

- `UserEnumController` 是一个 Spring MVC 控制器类，用于处理 `/user-types` 请求。
- `@Controller` 注解将类标记为 Spring MVC 控制器。
- `appConfig` 属性通过 `@Autowired` 注解进行自动注入，引用 `AppConfig` 配置类的实例。
- `getUserTypes` 方法处理 GET 请求 `/user-types` ：
- "adminType" 对应管理员用户类型的描述。
	- "userType" 对应普通用户类型的描述。
	- "guestType" 对应游客用户类型的描述。
- 从 `appConfig` 获取用户类型的描述，将描述添加到 Model 对象中：
	- 返回视图名称 "index"，用于展示用户类型的描述。

### Thymeleaf 前端页面 （ user-types.html）

通过 `Thymeleaf` 模板引擎渲染从后端传递过来的数据。

在 `src/main/resources/templates` 目录下创建 `              index.html            ` 文件

```
<!DOCTYPE html>
<html lang="zh-CN" xmlns:th="
            http://www.thymeleaf.org"
          >
<head>
    <meta charset="UTF-8">
    <title>用户类型</title>
    <link rel="stylesheet" href="
            https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
          >
</head>
<body>
<div class="container">
    <h1 class="mt-5">用户类型</h1>
    <table class="table table-bordered mt-3">
        <thead>
        <tr>
            <th>角色</th>
            <th>描述</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>ADMIN</td>
            <td th:text="${adminType}"></td>
        </tr>
        <tr>
            <td>USER</td>
            <td th:text="${userType}"></td>
        </tr>
        <tr>
            <td>GUEST</td>
            <td th:text="${guestType}"></td>
        </tr>
        <tr>
            <td>VIP</td>
            <td th:text="${vipType}"></td>
        </tr>
        <tr>
            <td>MODERATOR</td>
            <td th:text="${moderatorType}"></td>
        </tr>
        </tbody>
    </table>
</div>

<script src="
            https://code.jquery.com/jquery-3.6.0.min.js"
          ></script>
<script src="
            https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
          ></script>
</body>
</html>
```

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E4%BC%98%E9%9B%85%E4%BD%BF%E7%94%A8%20Enum%20%E6%8F%90%E5%8D%87%20SpringBoot%20%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E6%95%88%E7%8E%87%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. Spring Event 别瞎用！被它坑的绩效都没了！3. 面试官：什么是异地多活？4. 懵了！面试官问我：什么是 IO 密集，什么是 CPU 密集？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文