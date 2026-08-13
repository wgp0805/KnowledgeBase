---
title: "Git"
type: entity
tags: [版本控制]
sources: [raw/09-archive/git常用命令.md, raw/09-archive/git推送远程方法.md, raw/09-archive/服务器上搭建git.md, raw/01-articles/面试官：Git 如何撤回已 Push 的代码？问倒一大片。。。.md]
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

## Git 工程规范（大厂实践）
大厂将 Git 规范视为团队协作基石，核心价值四点：规模化协作、问题可追溯、CI/CD 自动化、规范即"省事"。

### 分支模型与命名
- **三种主流分支模型**：[[GitFlow]]（经典）、[[GitHubFlow]]（轻量）、[[TrunkBasedDevelopment]]（主干开发）
- **分支命名规范**：`<类型>/<内容>`（feature/、bugfix/、hotfix/、release/、chore/），可追加工单号 `feature/PROJ-123-user-login`，release/hotfix 带版本号 `release/v2.1.0`

### 提交与版本
- **[[ConventionalCommits]]**：`<type>(<scope>): <subject>` 约定式提交，支持自动生成 changelog
- **[[语义化版本]]**：`主.次.修` 三段式版本号 + Tag 管理（`git tag -a v2.1.0`）
- **[[Commitlint]] + [[Husky]]**：自动校验 commit message，不符合直接拒绝

### 代码审查与门禁
- 分支保护规则：禁止直接 push main/master、合并前必须 Code Review + CI 检查、至少 2 名审批人
- 标准 PR 模板 + 审查清单（测试覆盖率 ≥80% 等）
- CI/CD 多层质量门禁：编译 → 测试 → Lint → 安全扫描

## 关联连接
- [[GitHub]] - 代码托管平台
- [[Gitee]] - 代码托管平台
- [[IntelliJIDEA]] - IDE 集成
- [[GitFlow]] - 分支模型
- [[GitHubFlow]] - 分支模型
- [[TrunkBasedDevelopment]] - 分支模型
- [[ConventionalCommits]] - 提交规范
- [[语义化版本]] - 版本规范
- [[Commitlint]] - 提交校验工具
- [[Husky]] - Git 钩子工具
- [[code-review]] - 代码审查
- [[CI-CD]] - 持续集成/交付
- [[摘要-git常用命令]] - Git 版本控制的常用命令总结，涵盖初始化、克隆、分支管理、…
- [[摘要-git推送远程方法]] - Git 远程仓库操作指南，包括推送代码、设置上游分支、版本回…
- [[摘要-git-撤回已push代码]] - 撤回已 push 代码的四种方法对比（revert/新建分支/reset+force push）
- [[摘要-一线大厂Git规范]] - 大厂 Git 规范全景
- [[摘要-idea链接svn报错]] - 解决 IntelliJ IDEA 连接 SVN 时 SSL …
- [[摘要-IDEA使用Git提交报错]] - 解决 IntelliJ IDEA 使用 Git 提交时 "u…
