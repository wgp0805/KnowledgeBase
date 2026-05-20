---
title: "Pinia"
type: entity
tags: [前端, 状态管理, Vue]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

Pinia 是 Vue 的官方状态管理库，是 Vuex 的替代品。它提供了更简洁的 API 和更好的 TypeScript 支持。

## 关键信息

### 核心特性

- **Composition API 风格**：使用 `defineStore` 定义 store，`ref`/`computed` 定义状态
- **模块化设计**：每个 store 独立，支持跨 store 引用
- **DevTools 支持**：集成 Vue DevTools，方便调试
- **轻量**：打包体积小，无 mutations，直接修改状态

### 用户状态管理示例

```typescript
export const useUserStore = defineStore('user', () => {
  const token = ref('')
  const userInfo = ref(null)
  const permissions = ref([])

  async function login(params) { /* 登录逻辑 */ }
  async function fetchUserInfo() { /* 获取用户信息 */ }
  function hasPermission(perm) { /* 权限判断 */ }

  return { token, userInfo, permissions, login, hasPermission }
})
```

### 状态持久化

Pinia 状态存储在内存中，刷新页面会丢失。Token 应存储在 localStorage，用户信息在路由守卫中重新拉取。

## 关联连接
- [[摘要-springboot4-security7-vue3-best-practice]] — Pinia 在项目中的应用
- [[Vue3]] — 前端框架
- [[Axios]] — HTTP 客户端
