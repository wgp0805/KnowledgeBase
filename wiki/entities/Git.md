---
title: "Git"
type: entity
tags: [版本控制]
sources: [raw/01-articles/git常用命令.md, raw/01-articles/git推送远程方法.md, raw/01-articles/服务器上搭建git.md, raw/01-articles/面试官：Git 如何撤回已 Push 的代码？问倒一大片。。。.md]
last_updated: 2026-07-08
---

## 定义
Git 是一个分布式版本控制系统，用于追踪文件变更、协作开发和代码管理，是现代软件开发的基础工具。

## 关键信息
- 分布式架构，每个开发者拥有完整仓库副本
- 核心操作：init/clone/add/commit/push/pull/merge/rebase
- 分支管理：branch/checkout/switch/stash
- 暂存区（Stage/Index）概念区分工作区和仓库
- 远程仓库支持 SSH/HTTPS 协议
- 标签（Tag）用于版本发布标记

## 撤回已 Push 代码的四种方法

当错误代码已推送到远程仓库时，有四种撤回方案：

| 方案 | 安全性 | 适用场景 | 关键操作 |
|------|--------|----------|----------|
| 手动对比恢复 | 低（易遗漏） | 改动简单 | IDEA Compare Versions 手动删除差异代码 |
| `git revert` | 高（保留记录） | 回退少量提交 | 右键错误提交 -> Revert Commit -> 自动生成反向提交 -> push |
| 新建分支 | 高（保留原版本） | 回退大量提交 | 在目标 commit 右键 -> New Branch |
| `git reset --hard` + Force Push | 低（重写历史） | 需彻底清除提交记录 | Reset Current Branch -> Hard -> Force Push |

### git revert（推荐）
- 自动产生一个 Revert 记录，将指定提交的代码变更反向应用
- **安全**：保留完整改动记录，不重写历史
- **局限**：一次仅能回退一次 push，大量提交时操作繁琐

### git reset 四种模式
- **Soft**：工作区和暂存区不变
- **Mixed**：工作区不变，暂存区重置
- **Hard**：文件恢复到所选提交状态，已提交和未提交的更改全部丢失
- **Keep**：提交内容丢失，但未提交的本地修改保留

> **注意**：受保护分支（如 master）无法执行 Force Push 操作，需检查分支保护配置。

## 关联连接
- [[GitHub]] - 代码托管平台
- [[Gitee]] - 代码托管平台
- [[IntelliJIDEA]] - IDE 集成
- [[摘要-git常用命令]] - Git 版本控制的常用命令总结，涵盖初始化、克隆、分支管理、…
- [[摘要-git推送远程方法]] - Git 远程仓库操作指南，包括推送代码、设置上游分支、版本回…
- [[摘要-git-撤回已push代码]] - 撤回已 push 代码的四种方法对比（revert/新建分支/reset+force push）
- [[摘要-idea链接svn报错]] - 解决 IntelliJ IDEA 连接 SVN 时 SSL …
- [[摘要-IDEA使用Git提交报错]] - 解决 IntelliJ IDEA 使用 Git 提交时 "u…
