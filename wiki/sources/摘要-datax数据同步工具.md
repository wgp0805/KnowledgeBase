---
title: "摘要-datax数据同步工具"
type: source
tags: [来源, 数据同步, 大数据, MySQL]
sources: [raw/09-archive/2026-11-17 - 阿里又开源一款数据同步工具，稳定又高效，好用到爆！.md]
last_updated: 2026-11-19
---

## 核心摘要
小哈学Java 2026-11-17 文章（内容源自 CSDN），系统介绍阿里云开源的离线数据同步工具 [[DataX]]——阿里云 DataWorks 数据集成的开源版本，用于关系型数据库（MySQL、Oracle）、HDFS、Hive、ODPS、HBase、FTP 等异构数据源间的稳定高效离线同步。文章详解其 Framework + Plugin 架构（Reader/Writer 插件 + Framework 中间传输通道）与核心架构（Job → Task 切分 → TaskGroup 并发调度），并给出完整的 Linux 安装与 MySQL→MySQL 实战：3 百万行数据 42 秒同步完成（约 7.5 万条/秒），全量同步与基于 `where` 条件筛选的增量同步两种模式。

## 关键要点
- **背景痛点**：五千万级数据跨库同步，`mysqldump` 备份+同步耗时长且备份期间仍有新数据产出（同步等于没同步），存储过程方式 3 小时仅同步 2 千条
- **星型数据链路**：DataX 把复杂的网状同步链路变成星型——新数据源只需对接 DataX，即可与所有已接入数据源无缝同步
- **架构三角色**：Reader（采集）、Writer（写入）、Framework（缓冲/流控/并发/数据转换）
- **调度公式**：Task / Channel = TaskGroup；单个 Task 固定启动 Reader → Channel → Writer 线程
- **安装坑**：tar 包解压后必须删除 `/usr/local/datax/plugin/*/._*` 隐藏文件，否则报 plugin.json 不存在
- **全量 vs 增量**：唯一区别是增量同步在 reader 端加 `where` 条件筛选；注意增量续传时要删掉 writer 端的 `preSql`（如 truncate）
- **依赖**：JDK 1.8+、Python 2/3；配置为 JSON 格式，`python datax.py -r mysqlreader -w mysqlwriter` 可生成模板

## 关联连接
- [[DataX]] — 文章主角，阿里开源同步工具
- [[阿里云]] — 开源方（DataWorks 数据集成的开源版本）
- [[MySQL]] — 实战中的同步两端数据库
- [[小哈]] — 作者
- 离线数据同步 — 文章所属领域（架构与调度细节见 [[DataX]] 页面）
