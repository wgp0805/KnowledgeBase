---
title: "Maven"
type: entity
tags: [构建工具, 项目管理, Java]
sources: [raw/01-articles/Maven依赖管理项目构建工具.md]
last_updated: 2026-05-22
---

## 定义
Maven 是 Apache 旗下的 Java 项目构建和依赖管理工具，通过 POM（Project Object Model）统一管理项目的构建、依赖、文档和报告。

## 关键信息
- GAVP 坐标：GroupId、ArtifactId、Version、Packaging（jar/war/pom）
- 构建生命周期：清理周期（clean）→ 默认周期（compile → test → package → install → deploy）
- 依赖管理：自动解析传递依赖，支持短路优先和先声明优先冲突解决原则
- 依赖范围：compile（默认）、test、provided、runtime、system、import
- 继承与聚合：父工程统一管理依赖版本（dependencyManagement），聚合多个子模块批量构建
- 私服 Nexus：局域网仓库代理，缓存中央仓库构件，支持第三方构件部署
- 插件机制：编译插件、Tomcat 插件、MyBatis 逆向工程等

### 阿里云镜像配置
修改 settings.xml 添加阿里云 mirror 加速依赖下载。

### 依赖冲突解决
- 自动：短路优先（路径短优先）、先声明优先
- 手动：exclusions 标签排除特定依赖

## 关联连接
- [[Jenkins]] — CI/CD 构建集成
- [[Nexus]] — Maven 私服仓库
- [[SpringBoot]] — Maven 管理的 Spring 项目
- [[摘要-maven]] — 来源
