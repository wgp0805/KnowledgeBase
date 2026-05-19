---
title: "Kibana"
type: entity
tags: [可视化, Elasticsearch, 数据分析, ELK]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

Kibana 是一个针对 Elasticsearch 的开源分析及可视化平台，用于搜索、查看和交互存储在 Elasticsearch 索引中的数据。通过图表和仪表盘（Dashboard）进行高级数据分析及展示，是 ELK Stack 的核心组件之一。

## 关键信息

- 操作简单，基于浏览器界面，无需编码即可快速创建仪表盘
- 版本需与 Elasticsearch 保持一致
- 默认语言为英文，支持通过 `i18n.locale: "zh-CN"` 配置切换为中文
- 内置 Dev Tools 工具栏，提供 Console 界面方便执行 ES 查询命令

## 关联连接
- [[Elasticsearch]] — 数据存储与检索引擎
- [[摘要-elasticsearch-quick-start]] — 来源
