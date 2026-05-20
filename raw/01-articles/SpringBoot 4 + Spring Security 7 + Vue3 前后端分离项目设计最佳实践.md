---
title: "SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践"
source: "https://mp.weixin.qq.com/s/u4ObrxCrtcGCDAZ71gExCA"
---
大家好，我是锋哥。

> **"前后端分离就像异地恋，各自独立生长，却要靠一套约定保持默契。"**

---

## 一、写在前面：为什么又要写这种"全家桶"文章？

如果你在 2026 年还在用 `session` 做前后端分离的认证，那我只能说——勇士，你的 `JSESSIONID` 在跨域面前已经哭晕在厕所了。

SpringBoot 4 已经正式发布，基于 **Spring Framework 7** 和 **Java 21+**，带来了声明式 HTTP 客户端、结构化并发、30% 启动速度提升等一系列令人兴奋的新特性。Spring Security 也升级到了  **[7.x](http://7.x)** ，内置 MFA 支持，DSL 配置更加优雅。再配上 Vue3 的 `Composition API` + `Pinia` + `TypeScript`，这套组合拳打出去，项目架构直接起飞。

本文不是"Hello World 缝合怪"，而是从**真实项目架构**出发，手把手带你搭建一套**生产级**的前后端分离方案。

**阅读本文，你将收获：**

- 一套完整的前后端分离架构设计思路
- Spring Security 7 的 JWT 无状态认证最佳实践
- RBAC 权限模型的优雅实现
- Vue3 前端鉴权的全链路方案
- 若干踩坑经验（都是泪）

---

## 二、技术栈全景

| 层级 | 技术选型 | 版本 | 一句话点评 |
| --- | --- | --- | --- |
| **后端框架** | Spring Boot | 4. [0.x](http://0.x) | Java 21+，起飞的速度 |
| **安全框架** | Spring Security | [7.x](http://7.x) | 终于对 SPA 友好了 |
| **持久层** | MyBatis-Plus | 3. [5.x](http://5.x) | 能少写 SQL 就少写 |
| **缓存** | Redis | [7.x](http://7.x) | Token 黑名单的好帮手 |
| **前端框架** | Vue | 3. [5.x](http://5.x) | Composition API 真香 |
| **构建工具** | Vite | [6.x](http://6.x) | 快到模糊 |
| **状态管理** | Pinia | [3.x](http://3.x) | 比 Vuex 优雅一万倍 |
| **HTTP 客户端** | Axios | [1.x](http://1.x) | 拦截器 YYDS |
| **UI 组件** | Element Plus | [2.x](http://2.x) | 企业级首选 |
| **认证方案** | JWT | \- | 无状态，天生适合分布式 |

---

## 三、系统架构设计：先看全貌，再抠细节

### 3.1 整体架构图

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/440bab81ddca24135c191cea06ba91e2_MD5.png)

###   

### 3.2 认证授权流程——一图胜千言

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/8b987d99f6d7b252e99b6b89271b8d05_MD5.png)

### **经验之谈**：千万别把所有东西都揉在一个包里。按业务模块分包（`modules`），而不是按技术层分包（controller/service/mapper 各放一堆），这样当你删掉一个业务模块时，直接干掉一个文件夹就行，而不是在三个文件夹里翻找。

---

## 四、后端项目结构：规矩不能少

```text
backend/  
├── pom.xml  
└── src/main/java/com/example/  
    ├── Application.java                    # 启动类  
    ├── common/                             # 公共模块  
    │   ├── result/  
    │   │   ├── R.java                      # 统一响应体  
    │   │   └── ResultCode.java             # 响应码枚举  
    │   ├── exception/  
    │   │   ├── BizException.java           # 业务异常  
    │   │   └── GlobalExceptionHandler.java # 全局异常处理  
    │   └── constant/  
    │       └── SecurityConstants.java      # 安全相关常量  
    ├── config/                             # 配置层  
    │   ├── SecurityConfig.java             # Spring Security 核心配置  
    │   ├── RedisConfig.java                # Redis 配置  
    │   └── CorsConfig.java                 # 跨域配置  
    ├── security/                           # 安全模块  
    │   ├── filter/  
    │   │   └── JwtAuthenticationFilter.java  
    │   ├── handler/  
    │   │   ├── LoginSuccessHandler.java  
    │   │   ├── LoginFailureHandler.java  
    │   │   ├── AccessDeniedHandlerImpl.java  
    │   │   └── AuthenticationEntryPointImpl.java  
    │   └── util/  
    │       └── JwtUtils.java  
    ├── modules/                            # 业务模块  
    │   ├── auth/  
    │   │   ├── controller/AuthController.java  
    │   │   ├── service/AuthService.java  
    │   │   └── dto/LoginRequest.java  
    │   ├── user/  
    │   │   ├── controller/UserController.java  
    │   │   ├── service/UserService.java  
    │   │   ├── mapper/UserMapper.java  
    │   │   └── entity/User.java  
    │   └── role/  
    │       ├── controller/RoleController.java  
    │       ├── service/RoleService.java  
    │       └── entity/Role.java  
    └── resources/  
        ├── application.yml  
        └── mapper/
```

> **经验之谈**：千万别把所有东西都揉在一个包里。按业务模块分包（`modules`），而不是按技术层分包（controller/service/mapper 各放一堆），这样当你删掉一个业务模块时，直接干掉一个文件夹就行，而不是在三个文件夹里翻找。

---

## 五、后端核心实现：让代码说话

### 5.1 Maven 依赖

  
```xml
<!-- pom.xml 核心依赖 -->  
<parent>  
    <groupId>org.springframework.boot</groupId>  
    <artifactId>spring-boot-starter-parent</artifactId>  
    <version>4.0.5</version>  
</parent>  
  
<properties>  
    <java.version>21</java.version>  
    <mybatis-plus.version>3.5.9</mybatis-plus.version>  
    <jjwt.version>0.12.6</jjwt.version>  
</properties>  
  
<dependencies>  
    <!-- Web -->  
    <dependency>  
        <groupId>org.springframework.boot</groupId>  
        <artifactId>spring-boot-starter-web</artifactId>  
    </dependency>  
  
    <!-- Spring Security -->  
    <dependency>  
        <groupId>org.springframework.boot</groupId>  
        <artifactId>spring-boot-starter-security</artifactId>  
    </dependency>  
  
    <!-- Redis -->  
    <dependency>  
        <groupId>org.springframework.boot</groupId>  
        <artifactId>spring-boot-starter-data-redis</artifactId>  
    </dependency>  
  
    <!-- MyBatis-Plus -->  
    <dependency>  
        <groupId>com.baomidou</groupId>  
        <artifactId>mybatis-plus-spring-boot3-starter</artifactId>  
        <version>${mybatis-plus.version}</version>  
    </dependency>  
  
    <!-- JWT -->  
    <dependency>  
        <groupId>io.jsonwebtoken</groupId>  
        <artifactId>jjwt-api</artifactId>  
        <version>${jjwt.version}</version>  
    </dependency>  
    <dependency>  
        <groupId>io.jsonwebtoken</groupId>  
        <artifactId>jjwt-impl</artifactId>  
        <version>${jjwt.version}</version>  
        <scope>runtime</scope>  
    </dependency>  
    <dependency>  
        <groupId>io.jsonwebtoken</groupId>  
        <artifactId>jjwt-jackson</artifactId>  
        <version>${jjwt.version}</version>  
        <scope>runtime</scope>  
    </dependency>  
  
    <!-- MySQL -->  
    <dependency>  
        <groupId>com.mysql</groupId>  
        <artifactId>mysql-connector-j</artifactId>  
        <scope>runtime</scope>  
    </dependency>  
  
    <!-- Lombok -->  
    <dependency>  
        <groupId>org.projectlombok</groupId>  
        <artifactId>lombok</artifactId>  
        <optional>true</optional>  
    </dependency>  
  
    <!-- Validation -->  
    <dependency>  
        <groupId>org.springframework.boot</groupId>  
        <artifactId>spring-boot-starter-validation</artifactId>  
    </dependency>  
</dependencies>
```

### 5.2 application.yml——全局配置

```yml
```

```
```

### 5.3 统一响应体——别让前端猜你的返回格式

这是前后端分离项目的**第一条军规**：统一响应格式。前端不应该猜你返回的是啥结构。

```
/**
```

```
/**
```

> **Tips**: 业务错误码从 1000 开始编排，和 HTTP 状态码区分开。前端可以通过 `code < 1000` 判断是系统级错误还是业务级错误。

### 5.4 JWT 工具类——令牌的锻造师

```
@Component
```

### 5.5 Spring Security 7 核心配置——安全的大门

这是整个后端最关键的配置类。Spring Security 7 已经**完全移除了 `and()` 方法**，全面拥抱 Lambda DSL，配置起来更加清爽。

```
@Configuration
```

> **划重点**：前后端分离项目中，`csrf` 必须关闭（因为不依赖 Cookie），`sessionManagement` 设为 `STATELESS`（因为不用 Session）。这两步缺一不可，否则你会收获一堆玄学 Bug。

### 5.6 JWT 认证过滤器——每个请求的安检员

```
@Component
```

### 5.7 认证端点——登录/登出/刷新

```
@RestController
```

### 5.8 异常处理——优雅地告诉用户"你错了"

```
@RestControllerAdvice
```

```
/**
```

### 5.9 方法级权限控制——精确到按钮

Spring Security 7 的 `@EnableMethodSecurity` 让权限控制可以精细到每一个接口方法：

```
@RestController
```

> **权限编码规范**：采用 `模块:资源:操作` 的三段式命名，如 `system:user:add`。前端可以根据用户拥有的权限列表，动态控制按钮的显示/隐藏。

---

## 六、RBAC 权限模型设计

### 6.1 ER 关系图

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/3de78613479b758aeeffb3cb92178e7b_MD5.png)

###   

### 6.2 建表 SQL

```
-- 用户表
```

---

## 七、前端核心实现：Vue3 的优雅姿态

### 7.1 前端项目结构

```
frontend/
```

### 7.2 Axios 封装——请求拦截一把梭

这是前端和后端"对话"的翻译官，负责自动附加 Token、处理响应、Token 过期自动刷新。

```
// src/api/
            request.ts
```

> **这段代码的精髓在于 Token 无感刷新**：当 AccessToken 过期时，不会直接跳到登录页，而是静默地用 RefreshToken 换取新的 AccessToken，然后重发失败的请求。用户甚至感知不到 Token 曾经过期过。多个并发请求同时遇到 401 时，通过 `pendingRequests` 队列确保只刷新一次。

### 7.3 Pinia 用户状态管理

```
// src/stores/
            user.ts
```

### 7.4 路由守卫——前端的门卫大爷

```
// src/router/
            guards.ts
```

### 7.5 权限指令——按钮级别的权限控制

```
// src/directives/
            permission.ts
```

在模板中这样使用：

```
<template>
```

> **小贴士**：`v-permission` 指令只能控制按钮的"显示/隐藏"，但挡不住用户手动调接口。所以后端的 `@PreAuthorize` 才是真正的安全防线。前端权限控制本质上是**用户体验优化**，后端权限控制才是**安全保障**。两手都要抓，两手都要硬。

---

## 八、跨域处理：前后端分离的"必修课"

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/4ceb6f8d6f4a93c9239a013b6692d802_MD5.webp)

### 开发环境：Vite Proxy

```
// 
            vite.config.ts
```

### 生产环境：后端 CORS 配置

```
@Configuration
```

### 生产环境：Nginx 配置（推荐方案）

```
server {
```

> **划重点**：`try_files $uri $uri/ /[             index.html           ](http://index.html)`
>            这行配置是 SPA 的生命线。没有它，用户刷新页面就是一片 404 的汪洋大海。

---

## 九、部署架构：从开发到生产

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/5c1c3d2a9f09b73e0211c141dd5ec16a_MD5.png)

### Docker Compose 一键部署

```
# 
            docker-compose.yml
```

---

## 十、最佳实践清单：血泪经验总结

### 10.1 安全篇

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/31738b287b3c1d46d23df0dec55b8d83_MD5.png)

### 10.2 前后端协作的 10 条军规

| # | 规则 | 说明 |
| --- | --- | --- |
| 1 | **统一响应格式** | `{ code, message, data, timestamp }` 雷打不动 |
| 2 | **统一错误码** | 系统级 < 1000，业务级 ≥ 1000，前端用 code 做逻辑判断 |
| 3 | **RESTful 风格** | GET 查询、POST 新增、PUT 修改、DELETE 删除 |
| 4 | **接口版本化** | `/api/v1/users`，SpringBoot 4 原生支持 API 版本化 |
| 5 | **时间格式统一** | ISO 8601：`2026-04-12T10:30:00+08:00` |
| 6 | **分页参数统一** | `page`（从 1 开始）+ `size`，返回 `total` |
| 7 | **枚举值传数字** | 前端不应该传 "ACTIVE"，而应该传 `1` |
| 8 | **字段命名统一** | 后端 `snake_case` ↔ 前端 `camelCase`，JSON 序列化自动转换 |
| 9 | **Token 续期透明** | 对用户无感知，前端 Axios 拦截器自动处理 |
| 10 | **接口文档先行** | 用 Swagger / Knife4j 生成文档，别用嘴说 |

### 10.3 性能优化清单

```
// 1. SpringBoot 4 虚拟线程 —— 免费午餐
```

---

## 十一、常见"翻车"场景及解决方案

### 翻车 1：前端刷新页面后 Pinia 状态丢失

**症状**：用户登录后刷新页面，直接被踢到登录页。

**原因**：Pinia 状态存在内存里，刷新就没了。

**解决方案**：Token 存 `localStorage`，用户信息在路由守卫中重新拉取。

```
// 路由守卫中的关键逻辑
```

### 翻车 2：多个请求同时 401，Token 被刷新多次

**症状**：页面同时发了 5 个请求，AccessToken 都过期了，RefreshToken 被调了 5 次。

**解决方案**：用 `isRefreshing` 标志位 + 请求队列，确保只刷新一次（前面 Axios 封装已实现）。

### 翻车 3：Spring Security 的过滤器顺序问题

**症状**：CORS 预检请求（OPTIONS）被 Security 拦截，返回 401/403。

**解决方案**：确保 `CorsFilter` 在 `SecurityFilterChain` 之前执行：

```
// 方案一：在 SecurityConfig 中配置 cors
```

### 翻车 4：JWT Token 太大导致 Header 超限

**症状**：把用户所有角色、权限、菜单都塞进 JWT，Header 超过 Nginx 的 8KB 限制。

**解决方案**：JWT 只存必要信息（userId、username），权限数据从 Redis 取。

```
✅ JWT payload: { sub: "admin", userId: 1, exp: ... }          → ~200 bytes
```

---

## 十二、总结与全链路数据流

![图片](assets/SpringBoot%204%20+%20Spring%20Security%207%20+%20Vue3%20%E5%89%8D%E5%90%8E%E7%AB%AF%E5%88%86%E7%A6%BB%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/72cafa543cddc5ca0cfe9bd9eab84aa4_MD5.webp)

让我们用一张图总结整个请求的生命旅程：

1. **用户操作** → Vue3 组件触发事件
2. **API 调用** → Axios 请求拦截器自动附加 JWT Token
3. **网络传输** → Nginx 反向代理分发请求
4. **安全过滤** → JWT 过滤器验证 Token，加载用户认证信息
5. **权限校验** → `@PreAuthorize` 检查是否有操作权限
6. **业务处理** → Controller → Service → Mapper
7. **数据返回** → 统一 `R<T>` 响应体封装
8. **前端处理** → Axios 响应拦截器统一处理 code，展示数据或错误提示

---

## 十三、写在最后

前后端分离不是把一个项目拆成两个 Git 仓库就完事了。它是一种**架构思想**，要求前后端团队在**接口规范、认证方案、错误处理、权限模型**等方面达成高度一致。

**这套方案的核心理念：**

- **无状态认证**：JWT 让你的后端天生可水平扩展
- **双 Token 机制**：安全性和用户体验的平衡艺术
- **前后端双重权限控制**：前端管体验，后端管安全
- **统一约定**：响应格式、错误码、接口风格，让协作丝滑如德芙

SpringBoot 4 带来的虚拟线程、声明式 HTTP 客户端、模块化架构等新特性，让后端开发体验上了一个新台阶。Spring Security 7 对 SPA 的原生支持和更优雅的 DSL 配置，也让安全配置不再是"面向 Stack Overflow 编程"。

如果你觉得这篇文章有帮助，请记住这句话：

> **"代码是写给人看的，顺便能在机器上跑。"** —— 《计算机程序的构造和解释》

祝你的前后端分离之路，一路顺风，永不翻车。🚀