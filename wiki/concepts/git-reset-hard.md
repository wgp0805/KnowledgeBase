---
title: "git reset --hard"
type: concept
tags: [Git, 危险操作, 回退]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 定义
git reset --hard 是 Git 中最危险的操作之一，将 HEAD 指针移到指定提交的同时强制更新工作目录和暂存区，物理删除所有"多余"的文件和改动。

## 关键信息
- 作用：移动分支指针 + 清空暂存区 + 清空工作目录
- 恢复方式：git reflog 找到 reset 前的 commit hash，再 git reset --hard 恢复
- 安全替代：git reset --soft（只移 HEAD）或 git reset --mixed（默认，移 HEAD + 重置暂存区）
- 核心原则：每次 reset 前先看 git status，不确定时先 git stash
- 底层原理：Git 每次提交都是完整快照，reset 只移动指针，被"丢弃"的提交在垃圾回收前一直存在

## 关联连接
- [[git-reflog]] — 恢复丢失提交的保险绳
- [[git-stash]] — 暂存工作区的安全方案
- [[git-push-force]] — 同类危险操作
- [[摘要-git中的8个坑]] — 来源
