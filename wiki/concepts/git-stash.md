---
title: "git stash"
type: concept
tags: [Git, 工作区管理, 暂存]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 定义
git stash 将当前工作目录的未提交修改暂存到栈中，清理工作区以便切换分支或执行其他操作。

## 关键信息
- 基本操作：git stash push（暂存）、git stash pop（恢复并删除）、git stash apply（恢复但保留）
- pop vs apply：pop 冲突时 stash 可能丢失；apply 更安全，确认没问题再手动 drop
- 推荐用法：git stash apply + git stash drop，而非 git stash pop
- 带消息暂存：git stash push -u -m "描述信息"
- 查看内容：git stash show -p stash@{0}

## 关联连接
- [[git-reset-hard]] — 暂存前的安全保障
- [[合并冲突]] — stash 恢复时的冲突处理
- [[摘要-git中的8个坑]] — 来源
