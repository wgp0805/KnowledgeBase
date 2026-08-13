---
title: "Shiro"
type: entity
tags: [Java, 安全框架, 认证, 授权]
sources: []
last_updated: 2026-08-13
---

## 定义
Apache Shiro 是 Java 安全框架，提供认证（Authentication）、授权（Authorization）、会话管理（Session）、加密（Cryptography）四大核心能力。以 API 简单、学习曲线平缓著称，与 [[SpringSecurity]] 并列为 Java 安全两大主流方案。

## 关键信息
- **四大核心**：Authentication（认证）/ Authorization（授权）/ Session Management（会话）/ Cryptography（加密）
- **架构**：Subject（主体）/ SecurityManager（核心管理器）/ Realm（数据源，连接 DB/LDAP）
- **权限模型**：基于角色（RBAC）与权限字符串（`user:delete`）
- **优势**：轻量、API 直观、不绑定 Spring；适合中小项目或非 Web 场景
- **对比 [[SpringSecurity]]**：Shiro 简单灵活，Spring Security 功能全但重、与 Spring 生态深度绑定
- **对比 [[Sa-Token]]**：Sa-Token 更轻更现代（国产），Shiro 生态成熟但迭代慢

## 关联连接
- [[SpringSecurity]] — 对标安全框架
- [[Sa-Token]] — 国产轻量安全框架对标
- [[权限认证框架]] — 安全框架总类
