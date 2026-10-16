---
title: "JSONDualityViews"
type: concept
tags: [数据库, JSON, MySQL, 关系文档双模]
sources: [raw/09-archive/Mysql 9.7 到底有多强大？.md]
last_updated: 2026-10-16
---

## 定义

JSON Duality Views（JSON 对偶视图）是 [[MySQL]] 的特色功能：让同一份数据**既能以关系表形式访问，也能以 JSON 文档形式访问**。MySQL 9.7 解除了社区版"只读"限制，开放完整 DML（INSERT/UPDATE/DELETE，含使用自增列作为主键）。

## 关键信息

- 之前状态：社区版只读（仅 SELECT）；MySQL 9.7 起社区版可增删改
- 9.7 之前：该功能写能力仅企业版可用，社区版存在"能查不能写"的尴尬限制
- 9.7 之后：社区版可执行完整 DML，例如：

```sql
INSERT INTO user_json_view (name, email, address)
VALUES ('张三', 'zhangsan@example.com', '{"city": "北京"}');

UPDATE user_json_view
SET address = '{"city": "上海"}'
WHERE name = '张三';
```

- 适用场景：需要同时支持关系查询和文档查询的应用，实用价值在 9.7 后显著提升

## 关联连接

- [[MySQL]] — 载体数据库
- [[摘要-mysql-9-7-lts]] — 来源
- [[摘要-springboot整合mybatisPlus]] — 关系映射侧的对照技术
