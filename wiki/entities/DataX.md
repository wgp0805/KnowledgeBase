---
title: "DataX"
type: entity
tags: [开源项目, 数据同步, 大数据, 阿里]
sources: [raw/09-archive/2026-11-17 - 阿里又开源一款数据同步工具，稳定又高效，好用到爆！.md]
last_updated: 2026-11-19
---

## 定义
DataX 是 [[阿里云]] DataWorks 数据集成的开源版本，用于实现数据间的**离线同步**，致力于包括关系型数据库（MySQL、Oracle 等）、HDFS、Hive、ODPS、HBase、FTP 等各种异构数据源间稳定高效的数据同步。为解决异构数据源同步问题，DataX 将复杂的网状同步链路变成**星型数据链路**——自身作为中间传输载体，新数据源只需对接 DataX 即可与所有已接入数据源无缝同步。

## 关键信息

### Framework + Plugin 架构
数据源读取和写入抽象为 Reader/Writer 插件：
| 角色 | 作用 |
| --- | --- |
| Reader（采集模块） | 采集数据源的数据，发送给 Framework |
| Writer（写入模块） | 从 Framework 取数据写入目的端 |
| Framework（中间商） | 连接 Reader 与 Writer 的数据传输通道，处理缓冲、流控、并发、数据转换 |

### 核心架构（Job → Task → TaskGroup）
- **Job**：单个数据同步作业的中枢管理节点，承担数据清理、子任务切分、TaskGroup 管理；启动后按源端切分策略把 Job 切成多个 Task 并发执行
- **Scheduler**：按配置并发数把 Task 组装成 TaskGroup，计算公式 `Task / Channel = TaskGroup`
- 每个 Task 固定启动 **Reader → Channel → Writer** 线程；Job 监控所有 TaskGroup，全部完成后成功退出（异常退出时退出值非 0）

### 实战性能（MySQL→MySQL）
3,000,000 行数据、channel=5 并发，同步耗时 **42 秒**（约 74,999 条/秒、2.57MB/s），读写失败 0 条——对比传统方案：`mysqldump` 备份+同步耗时长且备份期间仍有数据产出，存储过程方式 3 小时仅同步 2 千条。

### 全量同步 vs 增量同步
- 全量：reader `column: ["*"]` + `splitPk: "ID"`（按主键切分并行）
- 增量：唯一区别是 reader 增加 **`where` 条件筛选**（如 `"ID <= 1888"`，续传用 `"ID > 1888 AND ID <= 2888"`）
- 注意：增量续传时删掉 writer 的 `preSql`（如 `truncate t_member`），否则刚同步的数据会被清空

### 安装与使用要点
- 依赖：JDK 1.8+、Python 2/3；tar 包方式无需 Maven
- **必踩坑**：解压后必须 `rm -rf /usr/local/datax/plugin/*/._*` 删除隐藏文件，否则报 `[.../._drdsreader/plugin.json] 不存在`
- 配置为 JSON；`python datax.py -r mysqlreader -w mysqlwriter` 生成模板，`python datax.py job.json` 执行
- writer 常用参数：`preSql`（同步前执行）、`writeMode: insert`、`session`（如 `set session sql_mode='ANSI'`）

## 关联连接
- [[摘要-datax数据同步工具]] — 来源
- [[阿里云]] — 开源方
- [[MySQL]] — 实战同步两端
