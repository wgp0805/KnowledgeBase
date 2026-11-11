---
title: "SpringSecurity"
type: entity
tags: [安全框架, Spring]
sources: [raw/09-archive/SpringBoot整合SpringSecurity及框架的简单使用.md, raw/09-archive/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md, raw/09-archive/SpringSecurity.md]
last_updated: 2026-05-20
---

## 定义
Spring Security 是一个功能强大的 Java 认证和授权框架，提供全面的安全解决方案，是 Spring 生态的官方安全框架。

## 关键信息
- 用户存储：内存用户、JDBC 数据库、LDAP、自定义 UserDetailsService
- 密码编码：BCryptPasswordEncoder（推荐）、ScryptPasswordEncoder
- 请求拦截：antMatchers().permitAll()/authenticated()/hasRole()
- 表单登录配置：loginPage()、loginProcessingUrl()
- CSRF 保护与禁用场景
- 与 Shiro 的对比：Spring Security 功能更全面但更复杂
- 底层架构：DelegatingFilterProxy（Servlet-Spring 桥接）→ FilterChainProxy（委托链）→ SecurityFilterChain（过滤链）
- 默认加载 16 个 Filter 实现安全防护
- 支持 OAuth2 四种授权模式：授权码、隐藏式、密码式、客户端凭证

### Spring Security 7 新特性
- 完全移除 `and()` 方法，全面拥抱 Lambda DSL
- 内置 MFA（多因素认证）支持
- 对 SPA 应用更友好
- `@EnableMethodSecurity` 启用方法级权限控制
- `@PreAuthorize` 实现精确到按钮的权限控制

### 前后端分离配置要点
- 关闭 CSRF（用 JWT 代替）
- Session 策略设为 STATELESS
- JWT 过滤器在 UsernamePasswordAuthenticationFilter 之前
- CORS 配置必须在 Security 之前执行

### 与 Sa-Token 对比
| 维度 | Spring Security | Sa-Token |
|------|-----------------|----------|
| **定位** | 企业级全面安全解决方案 | 轻量级权限认证框架 |
| **学习曲线** | 高，需理解过滤器链和 SecurityContextHolder | 极低，`StpUtil.login()` 一行完成 |
| **配置方式** | 大量配置类 | 零配置启动 |
| **功能边界** | 瑞士军刀，功能全面 | 聚焦高频认证场景 |
| **生态深度** | 全球最广泛的安全框架，文档极其丰富 | 6k+ GitHub Stars，社区较小 |

**一句话总结**：Spring Security 是"安全领域的瑞士军刀"，功能全面但复杂；Sa-Token 是"安全领域的美工刀"，简单实用且灵活。

### 完整权限系统落地链路（2026-11-10，详见 [[摘要-rbac权限系统设计]]）

一篇从 RBAC 到可运行代码的完整教程，串联六步：
1. **身份模型**：`JwtUser implements UserDetails`（username/password/state/authorities）
2. **令牌工具**：`JwtTokenUtil` —— `generateToken`（HS512 + 过期时间）、`getClaimsFromToken`、`isTokenExpired`、`refreshToken`、`validateToken`
3. **认证过滤器**：`JwtAuthenticationTokenFilter extends OncePerRequestFilter` —— 从 header 取 token → 解析用户名 → 校验 → 写入 `SecurityContextHolder`
4. **用户加载**：`UserDetailsService` 实现类查库，`user.getRoles().stream().map(Role::getRolename).map(SimpleGrantedAuthority::new)` 转权限
5. **登录签发**：`AuthenticationManager.authenticate()` 认证成功后签发 token
6. **安全配置**：`csrf().disable()` + `SessionCreationPolicy.STATELESS` + `addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)` + CORS（`CorsUtils::isPreFlightRequest` 放行预检）

**JSON 登录**：重写 `UsernamePasswordAuthenticationFilter#attemptAuthentication`，JSON Content-Type 时用 Jackson 反序列化；`addFilterAt(customFilter, UsernamePasswordAuthenticationFilter.class)` 替换原 filter（**必须保留 `formLogin()`**，否则原 filter 不出现）。

**密码存储**：`BCryptPasswordEncoder`（自带盐、非对称哈希），注册 `encode()`、登录 `matches()`。

**数据库认证**：`configure(AuthenticationManagerBuilder auth)` 直接传入 `userDetailsService` 实现类；`antMatchers("/admin/**").hasRole("admin")` 按角色拦截。

## 关联连接
- [[SpringBoot]] — 整合框架
- [[Spring]] — 基础框架
- [[JWT]] — 认证方案
- [[rbac]] — 权限模型
- [[cors]] — 跨域处理
- [[Sa-Token]] — 轻量级替代方案
- [[权限认证框架]] — 核心概念
- [[摘要-springboot4-security7-vue3-best-practice]] — Security 7 最佳实践
- [[摘要-spring-security]] — 完整教程
- [[摘要-rbac权限系统设计]] — 来源（RBAC + Spring Security + JWT 全链路教程）
- [[摘要-为什么越来越多人用Sa-Token]] — Sa-Token 对比来源
