---
title: "摘要-jd-driptable动态列表"
type: source
tags: [来源, 低代码, React, 前端, 京东]
sources: [raw/09-archive/京东又开源一款新框架，用起来真优雅！.md]
last_updated: 2026-11-19
---

## 核心摘要
小哈学Java 2026-11-18 文章，介绍京东零售开源的企业级中后台动态列表解决方案 [[DripTable]]——基于 [[React]] 和 JSON Schema，通过简单配置快速生成页面动态列表，降低列表开发难度。项目含两个子项目：drip-table（核心库，支持符合 JSON Schema 标准的数据自动渲染列表）与 drip-table-generator（可视化 JSON Schema 配置生成工具），主打 Lowcode 方式快速搭建中后台 CMS 列表页。

## 关键要点
- **优势**：高效开发（Lowcode 快速生成列表页）、配置化渲染（JSON Schema 描述字段自动渲染）、动态可扩展（自定义单元格组件 API）、界面框架自由（多主题包 + 自定义主题）
- **两种应用场景**：配置端（可视化/low-code 生成 JSON Schema 配置数据，依赖 `drip-table-generator`）与应用端（将 JSON Schema 渲染成动态列表，依赖 `drip-table`）；配置端依赖应用端，需先安装 drip-table
- **上手成本极低**：`yarn add drip-table` → 引入样式 → `<DripTable schema={schema} dataSource={[]} />` 三步完成；schema 中 columns 定义 key/title/dataIndex/component/options
- **适用场景**：中后台 CMS 列表页快速搭建、Lowcode 列表搭建的前端 Table 预览与实现
- **开源地址**：github.com/JDFED/drip-table

## 关联连接
- [[DripTable]] — 文章主角，京东开源动态列表方案
- [[京东]] — 开源方（京东零售 JDFED）
- [[React]] — 技术底座
- [[Lowcode]] — 所属开发范式
- JSON Schema — 配置数据标准（DripTable 的描述核心，无独立概念页）
- [[小哈]] — 作者
