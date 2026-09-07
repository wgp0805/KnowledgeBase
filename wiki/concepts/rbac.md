---
title: "rbac"
type: concept
tags: [权限, 安全, 访问控制]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md, raw/01-articles/2026-09-06-一个项目管理软件的诞生（十一）：企业级权限设计，谁能在什么条件下做什么.md]
last_updated: 2026-09-07
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

### 企业级权限设计主干（详见 [[摘要-企业级权限设计-用户组加功能权限]]）
- **核心主张**：企业级权限主干应是"用户组 + 功能权限"，ABAC/ReBAC 只给少数需收窄的权限加条件
- **用户组按职能建立**：空间管理员/产品组/研发组/测试组/外部协作组，用户组 ≠ 组织部门
- **功能权限按业务模块和动作拆开**：两层组织（业务模块 → 动作），一个稳定动作对应一条业务命令
- **菜单权限 ≠ 功能权限**：隐藏菜单只减少入口，用户仍可通过链接/API 访问
- **多用户组权限合并**：基础功能权限取并集，条件规则再收窄范围
- **页面/看板/批量/API 同一权限点**：前端隐藏按钮只是减少误操作，不构成安全边界
- **数据/字段/流转分层授权**：对象查看 → 字段可见 → 字段编辑 → 步骤执行
- **权限失败 ≠ 业务校验失败**：前者"你能不能做"，后者"这条数据现在能不能这样变化"
- **参考产品**：[[TAPD]]（用户组+功能权限主线）、[[Jira]]（全局权限+空间权限方案+角色+安全级别）

### 安全原则

- **前端权限控制**：用户体验优化，控制按钮显隐
- **后端权限控制**：安全保障，`@PreAuthorize` 才是真正的安全防线
- **两手都要抓**：前端管体验，后端管安全

## 关联连接
- [[SpringSecurity]] — 权限框架实现
- [[摘要-springboot4-security7-vue3-best-practice]] — 完整实践
- [[摘要-企业级权限设计-用户组加功能权限]] — 企业级权限设计主干
- [[ABAC]] — 基于属性的访问控制（条件收窄）
- [[ReBAC]] — 基于关系的访问控制（对象关系限定）
- [[TAPD]] — 腾讯项目管理平台（参考案例）
- [[Jira]] — Atlassian 项目管理工具（参考案例）
- [[frontend-backend-separation]] — 前后端分离架构
