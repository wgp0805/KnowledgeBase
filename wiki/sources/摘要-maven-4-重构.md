---
title: "摘要-maven-4-重构"
type: source
tags: [Maven, 构建工具, Java, POM, 迁移]
sources: [raw/01-articles/Maven 4 要来了：15 年后，Java 构建工具迎来"彻底重构".md]
last_updated: 2026-07-24
---

## 核心摘要
Maven 4 历经 15 年等待，核心变化是"Build POM 与 Consumer POM 分离"——构建时可以大胆进化，发布到仓库时仍保持兼容。当前最新版本 4.0.0-rc-5（2025-11-13），需 Java 17+ 运行，POM 模型升级至 4.1.0，带来父 POM 版本自动推断、子模块自动发现、CI 友好版本号等减少重复配置的特性。新增树形生命周期、显式 classpath/module path 类型、条件表达式 Profile 等多项能力。

## 关键信息

### 版本现状（截至 2026-07）
- 最新版本：4.0.0-rc-5（2025-11-13），仍为 RC，生产环境建议等 GA

### 硬性变化
| 项目 | Maven 3.x | Maven 4 |
|------|-----------|---------|
| 运行 Maven 本身 | Java 8+ | **Java 17+** |
| 编译项目代码 | 自行配置 | 仍可编译 Java 8/11/17 |
| POM 模型 | 4.0.0 | 构建可用 **4.1.0** |
| 依赖解析 | Resolver 1.x | **Resolver 2.0** |

### 核心架构变化
- **Build POM / Consumer POM 分离**：Maven 4 最重要的架构调整。Build POM 用于项目自身构建，Consumer POM 提供给依赖方，不包含插件配置、父 POM、未使用依赖，属性已被解析为具体值。Maven 4 原生支持 flatten，无需额外插件。开启：`mvn clean install -Dmaven.consumer.pom.flatten=true`

### 新增 Artifact 类型
- `classpath-jar` / `module-jar`：显式声明依赖放在 classpath 还是 module path，不再依赖隐式推断
- `processor` / `classpath-processor` / `modular-processor`：专门用于注解处理器，区分 API classpath 与 processor classpath

### modules → subprojects 重命名
- modules 标记为 deprecated，改用 `<subprojects>` 标签
- 支持 Parent 推断（空 `<parent />` 自动识别）
- 子项目自动发现（无需显式声明）
- 安全发布：子项目失败 → 全部不发布

### 树形生命周期（Tree-based Lifecycle）
- Maven 3 生命周期线性推进，难以高效并行
- Maven 4 每个子项目独立推进生命周期，依赖就绪即可启动
- 开启：`mvn -b concurrent verify`
- 大型多模块构建速度显著提升

### POM 4.1.0 新特性
1. 父 POM 版本自动推断（2005 年的老需求终于实现）
2. 子模块自动发现（pom 打包时自动扫描子目录）
3. CI 友好版本号（内置 `${revision}` 支持，不再需要 flatten 插件）
4. 新的 BOM 打包类型（`<packaging>bom</packaging>`）
5. 多源码目录（告别 Build Helper 插件）

### 配置能力增强
- **条件表达式 Profile**：不再只是 os.name、jdk 等基础判断，而是真正的表达式系统，支持 `exists()`、`length()` 等函数
- **统一 Sources 模型**：Maven 4 使用 `<sources>` 标签替代散落的 `<sourceDirectory>` 等配置，支持多目录、多版本、模块化项目

### 新工具
- **mvnup（Maven Upgrade Tool）**：迁移助手，`mvnup check` 只生成报告，`mvnup apply` 自动修改，分析 POM、插件、项目结构并给出可执行升级建议
- **mvnsh（Maven Shell）**：类似 REPL 的交互式 Shell
- **-r / --resume**：构建失败后从失败模块续跑

### Maven 3 迁移路径
1. 本地先试（Maven 4 RC + JDK 17，跑 mvnup check）
2. 升级插件（enforcer、shade、remote-resources）
3. 固定插件版本（Super POM 默认版本有变化）
4. CI 并行验证
5. 等 GA 再全面切换

## 关联连接
- [[Maven]] — 核心实体
- [[小锋]] — 来源作者
- [[Build POM 与 Consumer POM 分离]] — 核心架构变化
- [[Java]] — 运行环境要求
- [[Jenkins]] — CI/CD 集成
- [[摘要-maven]] — Maven 基础教程（前置知识）
- [[maven-lastUpdated-file]] — Maven 3 缓存文件问题