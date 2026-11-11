---
title: "摘要-rbac权限系统设计"
type: source
tags: [来源, 原始文件, RBAC, SpringSecurity, JWT, 权限]
sources: [raw/01-articles/万能通用！权限系统就该这么设计.md]
last_updated: 2026-11-11
---

## 核心摘要

小哈学Java（2026-11-10，源自 segmentfault）系统讲解"权限系统设计"全链路：RBAC 权限模型 → Spring Security 基础使用 → 集成 JWT 前后端分离 → JSON 登录 → 密码加密 → 数据库认证。

**一、RBAC 权限分析**
- **定义**：基于角色的访问控制，用户通过角色获得权限，角色是用户与权限的桥梁——修改权限时只改角色即可，减少权限漏洞
- **四个模型**：**RBAC0**（最常用，用户-角色多对一或多对多，如张三既是行政也负责财务有两权限）→ **RBAC1**（增加子角色与继承）→ **RBAC2**（增加约束：角色互斥如会计与审计不能兼、基数约束如 CEO 只能一个、先决条件如先有副总才能有经理、运行时互斥如总经理与专员不能同时生效）→ **RBAC3**（RBAC1 + RBAC2 统一模型）
- **什么是权限**：资源的集合——页面访问权限、菜单可见权限、数据增删查改权限
- **用户组**：把众多用户划为一组批量授予角色（如部门一万员工同角色），减少工作量、便于多级管理

**二、Spring Security 简单使用**：加 `spring-boot-starter-security` 依赖 → 默认所有接口被保护、启动日志打印随机密码 → 配置文件写死用户名密码与角色（`spring.security.user.name/password/roles`）→ `WebSecurityConfigurerAdapter` 配置内存认证（`auth.inMemoryAuthentication().withUser(...).roles(...)`）→ `HttpSecurity` 配置请求拦截（`authorizeRequests().antMatchers(...).permitAll()/authenticated()`）

**三、集成 JWT（前后端分离）**：jjwt 0.9.1 依赖 → `JwtUser implements UserDetails` → `JwtTokenUtil`（generateToken 用 HS512 签名 + 过期时间、getClaimsFromToken、isTokenExpired、refreshToken、validateToken）→ `JwtAuthenticationTokenFilter extends OncePerRequestFilter`（从 header 取 token → 解析用户名 → 校验 → 塞入 SecurityContextHolder）→ `UserDetailsService` 实现类查库加载用户与角色 → 登录 Service 用 AuthenticationManager 认证后签发 token → `WebSecurityConfigurerAdapter` 里 `csrf().disable()` + `STATELESS` + `addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)` + CORS 配置

**四、JSON 登录**：重写 `UsernamePasswordAuthenticationFilter#attemptAuthentication`，Content-Type 为 JSON 时用 Jackson 反序列化取用户名密码；`addFilterAt(customFilter, UsernamePasswordAuthenticationFilter.class)` 替换原 filter（`formLogin()` 必须保留否则原 filter 不出现）

**五、密码加密**：`BCryptPasswordEncoder` 作为 PasswordEncoder Bean，注册时 `encode()`、登录时 `matches()` 比对（BCrypt 自带盐、非对称哈希）

**六、数据库认证**：`configure(AuthenticationManagerBuilder auth)` 传入 `userDetailsService` 实现类查库验证；`antMatchers("/admin/**").hasRole("admin")` 按角色拦截

**小结**：RBAC（模型与粒度）+ Spring Security（框架能力：内存/数据库认证、请求拦截）+ JWT（无状态令牌）+ JSON 登录（前后端分离）+ BCrypt（密码存储）构成一套完整的传统权限系统方案。

## 关联连接
- [[rbac]] — 核心权限模型（本文补全 RBAC0/1/2/3 四模型）
- [[SpringSecurity]] — 框架实现（本文为完整教程）
- [[JWT]] — 无状态认证方案
- [[小哈]] — 作者
- [[SpringBoot]] — 宿主框架
- [[ABAC]] — 更细粒度的替代模型（对照）
