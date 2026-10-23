---
title: "摘要-vue3-admin-后台系统搭建"
type: source
tags: [来源, Vue3, TypeScript, Vite, 后台系统, 搭建笔记]
sources: [raw/09-archive/2026-10-22-从零开始搭建后台系统（vue3+TypeScript+Vite）01 - 落花看风雪.md]
last_updated: 2026-10-23
---

## 核心摘要
博客园作者落花看风雪（2026-10-22）的《从零开始搭建后台系统》系列第一篇：以官方脚手架命令 `pnpm create vue@latest vue3Admin` 初始化项目，参照 vue3-element-admin 的结构与规范来搭后台。初始化选项记录：TypeScript 选 Yes，JSX 默认 No（作者注明只有在高度动态的场景如可配置表单生成器才需要，属于进阶选择），Vue Router 与 Pinia 本项目选 Yes，Vitest/E2E 先跳过，ESLint/Prettier 选 Yes；依赖安装与 `pnpm dev` / `pnpm build`（类型检查+压缩）命令各就各位。文末给出标准项目结构：`.env.development`/`.env.production` 环境文件、`src/router`、`src/views`（Home 与 login 下的 index/Register/QrCodeLogin/ResetPwd）以及入口 HTML 说明，适合作为 [[Vue3]] + TypeScript + [[Vite]] 后台模板的参照基线。

## 关联连接
- 作者：博客园用户落花看风雪（未建实体页，纯文本记录）
- [[Vue3]] — 前端框架
- [[Vite]] — 构建工具
- [[Pinia]] — 状态管理
- [[ElementPlus]] — UI 框架（element-plus 2.14.7）
- [[SpringBoot]] — 常见配套后端（本库多篇文章的搭配习惯）
