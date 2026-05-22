---
title: "Jenkins"
type: entity
tags: [CI/CD, 自动化部署, DevOps]
sources: [raw/01-articles/Jenkins.md]
last_updated: 2026-05-22
---

## 定义
Jenkins（原名 Hudson）是开源的持续集成（CI）和持续交付（CD）自动化服务器，帮助开发团队自动化构建、测试和部署流程。

## 关键信息
- 安装方式：war 包直接运行或 Docker 容器部署
- 与 GitLab 集成实现代码变更自动触发构建
- 与 Maven 集成实现自动化编译打包
- Pipeline 流水线支持声明式（Declarative）和脚本式（Scripted）两种语法
- 插件生态丰富，支持 SSH 发布、邮件通知、Blue Ocean 可视化等
- Jenkins cron 表达式使用 H 哈希散列值避免任务集中执行
- 集群化构建可实现多机器并发，提升构建效率

### Pipeline 核心结构
- pipeline：整条流水线
- agent：指定执行器（节点标签）
- stages/stage：构建阶段
- steps：阶段内的执行步骤
- post：构建后处理（always/success/failure）

## 关联连接
- [[GitLab]] — Git 仓库与 CI/CD
- [[Maven]] — 项目构建工具
- [[Docker]] — 容器化部署
- [[CI-CD]] — 持续集成/持续交付
- [[摘要-jenkins]] — 来源
