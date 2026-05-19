---
title: "SpringSecurity"
type: entity
tags: [安全框架, Spring]
sources: [raw/01-articles/SpringBoot整合SpringSecurity及框架的简单使用.md]
last_updated: 2026-05-19
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

## 关联连接
- [[SpringBoot]] — 整合框架
- [[Spring]] — 基础框架
