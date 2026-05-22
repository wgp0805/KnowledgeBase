---
title: "SpringSecurity"
type: entity
tags: [安全框架, Spring]
sources: [raw/01-articles/SpringBoot整合SpringSecurity及框架的简单使用.md, raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md, raw/01-articles/SpringSecurity.md]
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

## 关联连接
- [[SpringBoot]] — 整合框架
- [[Spring]] — 基础框架
- [[JWT]] — 认证方案
- [[rbac]] — 权限模型
- [[cors]] — 跨域处理
- [[摘要-springboot4-security7-vue3-best-practice]] — Security 7 最佳实践
- [[摘要-spring-security]] — 完整教程
