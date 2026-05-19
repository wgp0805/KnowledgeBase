---
title: "incident-severity-classification"
type: concept
tags: [工程实践, 运维]
sources: [raw/01-articles/软件开发事故级别分类.md]
last_updated: 2026-05-19
---

## 定义
事故级别分类（P0-PX）是软件开发中对线上故障严重程度进行分级的标准体系，用于确定响应优先级和资源投入。

## 关键信息
- P0：核心功能完全不可用，影响所有用户，需立即响应
- P1：主要功能受损，影响大量用户，需高优先级处理
- P2：次要功能受影响，有临时替代方案
- P3：轻微问题，不影响正常使用
- PX：内部低影响问题，可排期修复

## 关联连接
- [[code-review]] — 代码审查
- [[api-compatibility]] — API 兼容性
