---
title: "DripTable"
type: entity
tags: [开源项目, 前端, React, 低代码, 京东]
sources: [raw/09-archive/京东又开源一款新框架，用起来真优雅！.md]
last_updated: 2026-11-19
---

## 定义
DripTable 是[[京东]]零售（JDFED）推出的企业级中后台**动态列表解决方案**，基于 [[React]] 和 JSON Schema，通过简单配置快速生成页面动态列表，降低列表开发难度、提高工作效率，主打 [[Lowcode]] 方式搭建中后台 CMS 列表页。

## 关键信息

### 子项目
- **drip-table**：核心库，支持符合 JSON Schema 标准的数据自动渲染列表内容
- **drip-table-generator**：可视化配置工具，用于生成符合 JSON Schema 标准的配置数据（依赖 drip-table，需先安装）

### 优势
- **高效开发**：Lowcode 方式快速生成列表页
- **配置化渲染**：JSON Schema 描述字段即可自动渲染所需列表
- **动态可扩展**：通过 API 快速生成自定义/业务功能的单元格组件
- **界面框架自由**：支持多种主题包与自定义主题包

### 两种应用场景
| 场景 | 职能 | 安装 |
| --- | --- | --- |
| 配置端 | 可视化/low-code 生成 JSON Schema 配置数据 | `yarn add drip-table-generator` |
| 应用端 | 将 JSON Schema 配置渲染成动态列表 | `yarn add drip-table` |

### 最小示例
```jsx
import DripTable from "drip-table";
import "drip-table/dist/index.min.css";

const schema = {
  size: "middle",
  columns: [
    { key: "columnKey", title: "列标题", dataIndex: "dataIndexName",
      component: "text", options: { mode: "single" } },
  ],
};
return <DripTable schema={schema} dataSource={[]} />;
```

### 适用场景
- 中后台 CMS 列表页快速搭建（JSON Schema 配置即生成，无需硬编码）
- Lowcode 列表搭建的前端 Table 预览与实现

## 关联连接
- [[摘要-jd-driptable动态列表]] — 来源
- [[京东]] — 开源方（京东零售）
- [[React]] — 技术底座
- [[Lowcode]] — 所属开发范式
