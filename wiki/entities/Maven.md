---
title: "Maven"
type: entity
tags: [构建工具, 项目管理, Java]
sources: [raw/01-articles/Maven依赖管理项目构建工具.md, raw/01-articles/Maven 4 要来了：15 年后，Java 构建工具迎来"彻底重构".md]
last_updated: 2026-07-07
---

## 定义
Maven 是 Apache 旗下的 Java 项目构建和依赖管理工具，通过 POM（Project Object Model）统一管理项目的构建、依赖、文档和报告。历经 15 年发展，Maven 4 正在进行"彻底重构"。

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

## Maven 4（截至 2026-07）

### 版本现状
- 最新版本：**4.0.0-rc-5**（2025-11-13），仍为 RC，生产环境建议等 GA
- 核心变化详见 [[摘要-maven-4-重构]]

### 硬性变化
| 项目 | Maven 3.x | Maven 4 |
|------|-----------|---------|
| 运行 Maven | Java 8+ | **Java 17+** |
| POM 模型 | 4.0.0 | **4.1.0** |
| 依赖解析 | Resolver 1.x | **Resolver 2.0** |

### 核心架构调整
- [[Build POM 与 Consumer POM 分离]] — 构建 POM 与发布 POM 分离，是"彻底重构"的真正含义
- **modules → subprojects**：`<modules>` 标记为 deprecated，改用 `<subprojects>`，支持子项目自动发现和安全发布（子项目失败 → 全部不发布）
- **树形生命周期（Tree-based Lifecycle）**：每个子项目独立推进生命周期，依赖就绪即可启动，`mvn -b concurrent verify` 开启并行构建
- **新增 Artifact 类型**：`classpath-jar` / `module-jar` 显式声明 classpath 或 module path；`processor` / `classpath-processor` / `modular-processor` 专门用于注解处理器
- **条件表达式 Profile**：支持 `exists()` / `length()` 等函数，不再限于 os.name、jdk 等基础判断
- **统一 Sources 模型**：`<sources>` 标签替代零散的 `<sourceDirectory>` 等配置，支持多目录和模块化项目

### POM 4.1.0 新特性
1. 父 POM 版本自动推断（子模块不必再写 `<version>`）
2. 子模块自动发现（pom 打包时自动扫描子目录）
3. CI 友好版本号（内置 `${revision}` 支持，不再需要 flatten 插件）
4. 新的 BOM 打包类型（`<packaging>bom</packaging>`）
5. 多源码目录（告别 Build Helper 插件）

### 新工具
- **mvnup**：迁移助手（`mvnup check` 检查兼容性，`mvnup apply` 自动修复）
- **mvnsh**：交互式 Shell（类似 REPL）
- **-r / --resume**：构建失败后从失败模块续跑

### Consumer POM 开启
```properties
maven.consumer.pom.flatten=true
```

## 关联连接
- [[Jenkins]] — CI/CD 构建集成
- [[Nexus]] — Maven 私服仓库
- [[SpringBoot]] — Maven 管理的 Spring 项目
- [[摘要-maven]] — 来源
- [[摘要-maven-4-重构]] — Maven 4 前瞻解析来源
- [[Build POM 与 Consumer POM 分离]] — Maven 4 核心架构概念
- [[小锋]] — Maven 4 文章作者
- [[maven-lastUpdated-file]] — Maven 3 *.lastUpdated 缓存问题
