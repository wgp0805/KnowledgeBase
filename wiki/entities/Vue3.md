---
title: "Vue3"
type: entity
tags: [前端, 框架, JavaScript]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

Vue3 是一个渐进式 JavaScript 框架，用于构建用户界面。相比 Vue2，引入了 Composition API、更好的 TypeScript 支持和性能优化。

## 关键信息

### 核心特性

- **Composition API**：使用 `setup()` 函数组织逻辑，代码复用更灵活
- **响应式系统**：基于 Proxy 的响应式实现，性能更好
- **TypeScript 支持**：原生支持 TypeScript，类型推导更完善

### 生态体系

- **Pinia**：状态管理，替代 Vuex，更轻量优雅
- **Vite**：构建工具，开发服务器启动极快
- **Vue Router**：路由管理，支持动态路由
- **Axios**：HTTP 客户端，支持拦截器

### 前端权限控制

- **v-permission 指令**：控制按钮显隐
- **路由守卫**：控制页面访问权限
- **注意**：前端权限控制仅是用户体验优化，后端 `@PreAuthorize` 才是安全保障

## 关联连接
- [[摘要-springboot4-security7-vue3-best-practice]] — Vue3 在前后端分离项目中的实践
- [[Pinia]] — 状态管理库
- [[Axios]] — HTTP 客户端
- [[ElementPlus]] — UI 组件库
- [[frontend-backend-separation]] — 前后端分离架构
