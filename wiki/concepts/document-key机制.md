---
title: "document-key机制"
type: concept
tags: [OnlyOffice, 协同编辑, 在线文档, 版本管理]
sources: [raw/01-articles/为什么越来越多人用 OnlyOffice？.md]
last_updated: 2026-09-28
---

## 定义
document.key 是 [[OnlyOffice]] 协同编辑中**当前文档内容版本的唯一身份标识**——它不是文件 ID，而是一次协同编辑会话的版本 ID。它决定五件事：多个用户是否进入同一协同会话、是否复用已有 Editor.bin 缓存、是否认为文件已变化、是否重新下载原始文件、是否属于同一编辑版本。

## 关键信息

### 编辑生命周期（浏览器编辑的是缓存，不是原始 Word 文件）
1. 第一次打开文档（key = key0）→ 下载原始 Word → 转换为 **Editor.bin** 缓存在 `/var/lib/onlyoffice/documentserver/App_Data`
2. 多人进入协同 → 使用同一 key0 → 进入同一会话，所有人编辑的是 Editor.bin
3. 编辑过程中所有修改都写缓存，原始 Word 文件可能完全没变
4. **真正的保存时机**是所有人退出或强制保存后：生成 `output.docx`，回调 status = 2 或 6
5. 集成方必须此时下载 output.docx 并**更新版本 key**，否则下次打开仍是旧文件

### 常见坑
- **把 document.key 当文件 ID**：导致协同会话错乱、版本冲突、内容看似"丢失"
- **"内容丢失"的真相**：多数是回调后没有下载 output.docx、仍保留旧文件——不是丢了，是新的根本没保存
- **key 不更新**：内容变化后 key 不变，OnlyOffice 认为文件没变，继续用缓存 Editor.bin

### Java 集成要点
- 编辑器配置中 `key` 取 `doc.getVersionKey()`，内容每次变化必须换 key
- `/callback` 中 status 为 "2" 或 "6" 时下载保存文档，并调用 `updateVersionKey` 更新版本 key

## 关联连接
- [[OnlyOffice]] — 所属系统（增量更新）
- [[摘要-为什么越来越多人用onlyoffice]] — 来源
- [[摘要-springboot-onlyoffice-在线编辑]] — 集成实现摘要
- [[在线文档处理]] — 上位概念
