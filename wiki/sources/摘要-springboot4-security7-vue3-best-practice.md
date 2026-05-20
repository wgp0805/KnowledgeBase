---
title: "摘要-springboot4-security7-vue3-best-practice"
type: source
tags: [SpringBoot, SpringSecurity, Vue3, 前后端分离, JWT, RBAC]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 核心摘要

本文是一份生产级前后端分离项目架构指南，基于 SpringBoot 4 + Spring Security 7 + Vue3 技术栈。后端采用 JWT 无状态认证 + Redis 黑名单实现 Token 管理，通过双 Token 机制（AccessToken 30分钟 + RefreshToken 7天）解决续期问题。RBAC 权限模型采用用户-角色-菜单五表设计，支持按钮级权限控制。前端使用 Pinia 管理状态、Axios 拦截器实现 Token 无感刷新、v-permission 指令控制按钮显隐。文章涵盖了统一响应体设计、全局异常处理、CORS 跨域配置、Docker Compose 部署等完整工程实践。

## 关联连接
- [[SpringBoot]] — 后端框架
- [[SpringSecurity]] — 安全框架
- [[JWT]] — 认证方案
- [[Redis]] — Token 黑名单存储
- [[MyBatisPlus]] — 持久层框架
- [[Vue3]] — 前端框架
- [[Pinia]] — 状态管理
- [[Axios]] — HTTP 客户端
- [[ElementPlus]] — UI 组件库
- [[rbac]] — RBAC 权限模型
- [[frontend-backend-separation]] — 前后端分离架构
- [[dual-token-mechanism]] — 双 Token 机制
- [[cors]] — 跨域处理
