---
title: "HashMap"
type: entity
tags: [Java, 数据结构, 哈希表, 键值对]
last_updated: 2026-09-14
---

# HashMap

## 身份定义
HashMap 是 Java 核心数据结构，基于哈希表实现的键值对存储容器，提供 O(1) 平均时间复杂度的增删改查操作。

## 核心功能/特征
- 基于哈希表的键值对存储，支持快速查找、插入和删除
- keySet() 遍历 vs entrySet() 遍历存在性能差异
- 阿里巴巴开发规约不推荐 keySet() 遍历的原因：keySet() 需要额外查 hash 表获取 value，而 entrySet() 直接遍历键值对，无需二次查找

## 关联连接
- [[Java]]
