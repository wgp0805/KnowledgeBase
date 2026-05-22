---
title: "CI-CD"
type: concept
tags: [DevOps, 自动化, 持续集成]
sources: [raw/01-articles/Jenkins.md]
last_updated: 2026-05-22
---

## 定义
CI/CD（Continuous Integration/Continuous Delivery）持续集成/持续交付是一套自动化构建、测试和部署的 DevOps 实践，通过自动化流水线加速软件交付。

## 关键信息
- 持续集成（CI）：代码变更后自动触发构建和测试，尽早发现集成问题
- 持续交付（CD）：自动化部署到测试/生产环境
- Jenkins 与 GitLab + Maven 组合实现 Java 项目自动化部署
- Pipeline 作为代码（Pipeline as Code）将构建流程版本化管理

### 构建触发方式
- 快照依赖构建：依赖的快照更新时触发
- 远程触发：Webhook 回调 REST API
- 定时构建：cron 表达式定期执行
- GitHub/GitLab hook：代码提交时自动触发
- Poll SCM：定期检查代码变更

## 关联连接
- [[Jenkins]] — CI/CD 自动化服务器
- [[GitLab]] — Git 仓库与 CI/CD
- [[Maven]] — 构建工具
- [[Docker]] — 容器化部署
- [[摘要-jenkins]] — 来源
