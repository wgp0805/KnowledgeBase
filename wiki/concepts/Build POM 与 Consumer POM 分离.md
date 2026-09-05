---
title: "Build POM 与 Consumer POM 分离"
type: concept
tags: [Maven, 构建工具, POM, 架构设计]
sources: [raw/01-articles/Maven 4 要来了：15 年后，Java 构建工具迎来"彻底重构".md]
last_updated: 2026-07-07
---

## 定义
Maven 4 最核心的架构调整：将"构建用的 POM"和"给下游用的 POM"分离。Build POM 存于 Git 仓库，包含完整信息；Consumer POM 发布到 Maven Central，只保留下游真正需要的依赖信息。这让构建格式可以大胆进化而不破坏兼容性。

## 关键信息

### 两者职责
- **Build POM**：存在 Git 仓库，包含插件配置、属性、父 POM 引用等完整信息
- **Consumer POM**：发布到 Maven Central 的精简版，去掉 parent 引用（继承内容已内联）、去掉插件配置、只保留实际用到的依赖

### 生成机制
构建完成后，Maven 4 自动从 Build POM 生成 Consumer POM。

### 开启方式（rc-5）
Consumer POM 扁平化默认关闭，需显式开启：
```
maven.consumer.pom.flatten=true
```
或命令行：
```
mvn deploy -Dmaven.consumer.pom.flatten=true
```

### 为什么等了 15 年
- POM 格式一旦改动，Maven Central、IDE、Gradle 互操作、各类插件都要跟着动
- POM 4.0.0 语法被"冻住"，很多 2005 年提出的改进一直拖到现在
- 分离后，构建时可以大胆进化，发布时仍保持兼容——这才是"彻底重构"的真正含义

## 关联连接
- [[Maven]] — 所属构建工具
- [[摘要-maven-4-重构]] — 来源
- [[小锋]] — 来源作者
