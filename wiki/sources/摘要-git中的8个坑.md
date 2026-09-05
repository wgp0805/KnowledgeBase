---
title: "摘要-git中的8个坑"
type: source
tags: [来源, 原始文件, Git, 苏三]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 核心摘要
苏三整理了 Git 使用中最常见的 8 个操作陷阱：reset --hard 丢代码、合并冲突解决后忘记提交、stash pop 冲突丢 stash、push --force 覆盖别人代码、rebase 基线搞错、cherry-pick 冲突处理误区、branch -D 误删分支、commit --amend 推送后被拒。核心原则是"每次操作前先看 git status"，养成习惯比学会所有命令更重要。

## 关联连接
- [[苏三]] — 作者
- [[Git]] — 关联实体
- [[git-reset-hard]] — 概念：reset --hard 危险操作
- [[git-push-force]] — 概念：force 推送覆盖
- [[git-reflog]] — 概念：恢复丢失提交
- [[--force-with-lease]] — 概念：安全替代 force
- [[git-stash]] — 概念：暂存工作区
- [[合并冲突]] — 概念：冲突解决流程
