---
title: "--force-with-lease"
type: concept
tags: [Git, 安全操作, 团队协作]
sources: [raw/01-articles/聊聊Git中的8个坑.md]
last_updated: 2026-09-03
---

## 定义
--force-with-lease 是 git push --force 的安全替代方案，只在远程分支没有被其他人更新过的情况下才执行强制推送。

## 关键信息
- 行为：检查远程分支是否与上次 fetch 时一致，不一致则拒绝推送并提示先 pull
- 对比 --force：--force 是"盲写"，--force-with-lease 是"带条件地写"
- 使用场景：amend 后需要推送、需要重写远程历史时
- 限制：仅适用于你一个人使用该分支的情况，团队共享分支仍需 pull --rebase

## 关联连接
- [[git-push-force]] — 危险替代方案
- [[git-reset-hard]] — 同类操作
- [[摘要-git中的8个坑]] — 来源
