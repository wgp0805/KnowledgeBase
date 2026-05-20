---
title: "rbac"
type: concept
tags: [权限, 安全, 访问控制]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

RBAC（Role-Based Access Control）基于角色的访问控制，是一种广泛使用的权限管理模型。用户通过角色获得权限，角色是用户和权限之间的桥梁。

## 核心原理

### 数据库设计（五表）

```
用户表 t_user
    ↓ N:N
用户角色关联表 t_user_role
    ↓
角色表 t_role
    ↓ N:N
角色菜单关联表 t_role_menu
    ↓
菜单权限表 t_menu（目录/菜单/按钮）
```

### 权限编码规范

采用 `模块:资源:操作` 三段式命名：
- `system:user:list` — 用户列表查询
- `system:user:add` — 新增用户
- `system:user:edit` — 编辑用户
- `system:user:delete` — 删除用户

### 后端实现

```java
@GetMapping
@PreAuthorize("hasAuthority('system:user:list')")
public R<IPage<UserVo>> list() { ... }
```

### 前端实现

```vue
<el-button v-permission="'system:user:add'">新增用户</el-button>
```

### 安全原则

- **前端权限控制**：用户体验优化，控制按钮显隐
- **后端权限控制**：安全保障，`@PreAuthorize` 才是真正的安全防线
- **两手都要抓**：前端管体验，后端管安全

## 关联连接
- [[SpringSecurity]] — 权限框架实现
- [[摘要-springboot4-security7-vue3-best-practice]] — 完整实践
- [[frontend-backend-separation]] — 前后端分离架构
