---
title: "git reflog"
type: concept
tags: [Git, 恢复, 审计]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 定义
git reflog 记录本地仓库的所有 HEAD 变动历史，包括 reset、rebase、checkout 等操作，是找回误删提交的"保险绳"。

## 关键信息
- 作用：查看所有操作记录，包括被 reset/rebase 丢弃的提交
- 恢复流程：git reflog → 找到目标 commit hash → git reset --hard <hash>
- 适用场景：reset --hard 丢代码、rebase 搞错基线、branch -D 误删分支
- 限制：只记录本地操作，不包含远程仓库变动；git gc 垃圾回收后可能清除
- 原理：Git 每次提交都是完整快照，reflog 记录指针移动历史

## 关联连接
- [[git-reset-hard]] — 误操作后的恢复手段
- [[git-stash]] — 暂存工作区
- [[摘要-git中的8个坑]] — 来源
