---
title: "sed"
type: entity
tags: [Linux, 文本处理, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
sed 是 Linux 文本处理三剑客之一，用于文本编辑（改），支持原地替换、行范围显示、删除空行等操作。

## 关键信息
- **定位**：文本编辑（改）
- **常用示例**：
  - `sed -i 's/old/new/g' file.txt`：原地替换
  - `sed -n '10,20p' file.txt`：只显示第 10 到 20 行
  - `sed '/^$/d' file.txt`：删除空行
- **面试要点**：与 grep（找）、awk（按列处理）区分

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[grep]] — 三剑客之一
- [[awk]] — 三剑客之一
