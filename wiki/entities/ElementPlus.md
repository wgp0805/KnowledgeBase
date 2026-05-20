---
title: "ElementPlus"
type: entity
tags: [前端, UI组件库, Vue]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

Element Plus 是基于 Vue 3 的企业级 UI 组件库，是 Element UI 的 Vue 3 版本。提供了丰富的企业级组件，适合中后台管理系统。

## 关键信息

### 核心特性

- **Vue 3 原生支持**：基于 Composition API 开发
- **TypeScript 支持**：完整的类型定义
- **组件丰富**：表格、表单、对话框、导航等企业级组件
- **主题定制**：支持 CSS 变量和 SCSS 覆盖

### 常用组件

- `el-table`：数据表格，支持分页、排序、筛选
- `el-form`：表单组件，支持校验
- `el-button`：按钮组件
- `el-tag`：标签组件
- `el-message`：消息提示

### 与权限指令配合

```vue
<el-button v-permission="'system:user:add'" type="primary">
  新增用户
</el-button>
```

## 关联连接
- [[摘要-springboot4-security7-vue3-best-practice]] — Element Plus 在项目中的应用
- [[Vue3]] — 前端框架
- [[frontend-backend-separation]] — 前后端分离架构
