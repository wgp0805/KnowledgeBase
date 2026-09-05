---
title: "git push --force"
type: concept
tags: [Git, 危险操作, 团队协作]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 定义
git push --force 将本地仓库的分支状态直接覆盖远程仓库，不做任何检查，是团队 Git 协作中最常见、最严重的错误操作。

## 关键信息
- 风险：本地分支落后于远程时，--force 会用旧数据强行覆盖新数据，同事的代码被永久抹除
- 安全替代：git push --force-with-lease（检查远程分支是否与上次拉取时一致，不一致则拒绝）
- 正确做法：先 git pull --rebase 再 git push
- 底层原理：--force 是"盲写"，--force-with-lease 是"带条件地写"
- 绝对原则：绝对不用 git push --force，用 --force-with-lease 替代

## 关联连接
- [[--force-with-lease]] — 安全替代方案
- [[git-reset-hard]] — 同类危险操作
- [[合并冲突]] — 团队协作场景
- [[摘要-git中的8个坑]] — 来源
