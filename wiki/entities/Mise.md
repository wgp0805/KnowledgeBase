---
title: "Mise"
type: entity
tags: [实体, 工具, 开发环境, 多版本管理]
sources: [raw/01-articles/Mise 开发环境迁移完整手册.md]
last_updated: 2026-10-20
---

## 定义
mise 是多语言运行时与工具的版本管理器，统一管理 Java、Node、Maven、PHP 等多版本，替代 nvm/sdkman 等零散工具，通过项目级配置文件实现"进入目录自动切换版本"的多项目环境隔离。

## 关键信息
- **核心机制**：
  - `MISE_DATA_DIR` 环境变量指定 SDK 统一存放目录（Windows 示例 `D:\java\mise-software`），**一旦确定不可修改**，改动会导致已下载 SDK 全部失效
  - **shims 代理**：`shims/` 下的 java.exe/node.exe 不是真实程序，转发到当前激活版本；选 `installs/xxx/` 则固定版本不受切换影响
  - **版本优先级**：项目目录 `mise.toml` > 全局 mise 版本；`mise use` 在项目目录执行即写入 mise.toml，可提交 Git 团队共享（拉代码后 `mise install` 装齐）
- **基础命令**：`mise ls` / `mise ls-remote` / `mise install 工具@版本` / `mise use -g 工具@版本`（全局）/ `mise shell`（临时）/ `mise current` / `mise doctor` / `mise self-update`
- **自动激活（PowerShell）**：profile 中 `mise activate powershell` 初始化 + `prompt` 钩子调 `mise hook-env -s powershell`，cd 进项目目录即切换；改完脚本必须关闭全部终端重开才生效；IDEA 内置终端需开启 Shell integration
- **Java 版本格式坑**：注册表格式为 `java@temurin-8.0.422`，不能单独写 `temurin@...`
- **PHP**：Windows 需第三方插件 `mise plugins install vfox:version-fox/vfox-php`，且依赖 VC++ 运行库（vcruntime140.dll）
- **既有 SDK 托管**：`mise link java@8.0.211 D:\path` 可接管本地已解压 SDK
- **IDEA 两方案**：固定 installs 目录（稳定不自动切）或 shims 目录（跟随 mise.toml 联动）；**必须二选一统一**，否则 IDEA 与终端版本不一致引发编译运行冲突
- **避坑**：不手动改系统 PATH 切换版本；Node 跨大版本原生编译类 npm 全局包需重装；不要与 nvm/sdkman 同时启用（PATH 冲突）；先验证新环境可用再删旧环境

## 关联连接
- [[摘要-mise开发环境迁移手册]] — 来源
- [[IntelliJIDEA]] — 配套 IDE 配置
- [[Maven]] — 由 mise 管理，自动继承激活的 JAVA_HOME
- [[Java]] / [[Node.js]] — 管理的目标运行时
