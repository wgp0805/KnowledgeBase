---
title: "摘要-从winforms到vue-ds-ui-gui框架"
type: source
tags: [GUI, 框架, 前端, WinForms, Vue]
sources: [raw/01-articles/2026-07-22-从 WinForms 到 Vue：我为什么决定在 Web 上重做一套完整的 GUI 框架 - delete19910520.md]
last_updated: 2026-07-23
---

## 核心摘要
作者从 WinForms 桌面开发转向 Vue Web 开发后，发现对于高信息密度、长时间运行的企业级软件（ERP、临床系统、财务系统等），Vue 的声明式响应式模型不如 WinForms 的控件对象模型直接。作者选择用 Canvas 自研了一套完整的 GUI 框架 ds-ui，核心思想是让业务开发人员面对的是业务控件（Button、DataGrid、Tree、Window），而框架承担控件内部的复杂度。这不是简单的"把 Web 写回桌面"，而是为专业 GUI 软件建立统一的对象模型、生命周期、事件路由和焦点管理。

## 关联连接
- [[Vue3]] — Web 开发框架对比
- [[ds-ui]] — 作者自研的 Canvas 专业 GUI 框架
- [[JavaScript]] — 实现语言
- [[AICoding]] — 现代 Web 开发范式