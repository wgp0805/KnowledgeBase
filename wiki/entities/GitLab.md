---
title: "GitLab"
type: entity
tags: [Git, 代码托管, CI/CD]
sources: [raw/01-articles/Jenkins.md]
last_updated: 2026-05-22
---

## 定义
GitLab 是一款基于 Git 的开源代码托管平台，提供仓库管理、CI/CD 流水线、代码审查、Issue 跟踪等一体化 DevOps 能力。

## 关键信息
- 安装方式：ssh 安装（依赖 openssh-server、policycoreutils-python）或 Docker 容器安装
- 系统要求：内存至少 4G，内核 3.10 以上
- 默认管理员用户名 root，初始密码存储在 /etc/gitlab/initial_root_password（24 小时后自动删除）
- 常用命令：gitlab-ctl start/stop/restart/status/reconfigure/tail
- 与 Jenkins 配合使用：通过 Webhook 回调触发 Jenkins 构建任务

## 关联连接
- [[Jenkins]] — CI/CD 集成
- [[Git]] — 版本控制基础
- [[CI-CD]] — 持续集成/持续交付
- [[摘要-jenkins]] — 来源
