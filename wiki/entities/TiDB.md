---
title: "TiDB"
type: entity
tags: [数据库, 分布式数据库, NewSQL, HTAP, MySQL兼容]
sources: [raw/09-archive/2026-09-25 - 分库分表，可能真的要退出历史舞台了！.md, raw/09-archive/为什么越来越多人用 TiDB？.md]
last_updated: 2026-11-19
---

## 定义

TiDB 是 [[PingCAP]] 自主设计研发的开源分布式关系型数据库（新架构型 [[newsql]]），同时支持在线事务处理与在线分析处理（[[htap]]），兼容 MySQL 5.7 协议与 MySQL 生态，具备水平扩缩容、金融级高可用、实时 HTAP、云原生等特性，目标是一站式 OLTP/OLAP/HTAP 解决方案。由 [[黄东旭]] 受 Google F1/Spanner 论文启发创建。

## 关键信息

### 核心特性
- **水平弹性扩展**：存储计算分离，计算、存储可分别在线扩缩容，对应用与运维透明
- **分布式事务**：100% 支持标准 ACID 事务，TiKV 通过两阶段提交保证跨 Region 读写约束
- **金融级高可用**：基于 Raft 多数派选举，Multi-Raft 同步事务日志、多数派写入成功才提交，少数副本故障不影响可用，可配置副本地理位置与数量满足容灾
- **实时 HTAP**：行存 TiKV + 列存 TiFlash，TiFlash 经 Multi-Raft Learner 协议实时复制，配合 TiSpark 免 ETL；设计目标 100% OLTP + 80% OLAP 场景
- **云原生**：与 Kubernetes 深度耦合，支持公有云/私有云/混合云
- **高度兼容 MySQL**：兼容 5.7 协议与常用功能，多数情况无需改代码迁移；提供 Syncer 等工具，分库分表后的 MySQL 集群也可实时迁移

### 架构组件
| 组件 | 职责 |
| --- | --- |
| TiDB Server | 无状态 SQL 计算层，接 SQL、通过 PD 定位 TiKV，可无限水平扩展（前置 LVS/HAProxy/F5） |
| PD Server | 存元信息、调度与负载均衡（数据迁移、Leader 迁移）、分配全局唯一递增事务 ID；Raft 保证自身一致性，建议奇数节点，Leader 选举约 3 秒 |
| TiKV Server | 分布式事务型 KV 存储，基本单位 Region（Key Range 左闭右开），默认 3 副本构成 Raft Group，Leader 提供读写 |
| TiFlash | 列式存储节点，为分析场景加速 |
| TiSpark | 把 Spark SQL 跑在 TiDB 存储层，补复杂 OLAP |

### Region 机制
- 超过 144MB 自动分裂、过小自动合并，便于 PD 调度（口径说明：144MB 是自动分裂的触发阈值，96MB 是 Region 的默认目标大小——2026-11-19 苏三文章与入门文两个数字并存，非矛盾）
- 副本调度流程：目标节点加 Learner → 追平后转 Follower → 移除旧副本；Leader 调度再加一次 Leader Transfer
- 写请求只在 Leader 写入且需多数副本成功（默认 3 副本中至少 2 个）才返回

### 高可用行为
- TiDB 无状态，单实例失效只影响其上 Session，重连即可
- PD 非 Leader 失效无感；Leader 失效重新选举（约 3 秒不可服务）
- TiKV 节点失效 10 分钟未恢复，PD 会把其数据迁走

### 兼容性差异（不支持的 MySQL 特性）
存储过程与函数、触发器、事件、自定义函数、外键约束、临时表、全文/空间函数与索引、SYS schema、XML 函数、X-Protocol、Savepoints、列级权限、`XA` 语法（内部用两阶段提交但未通过 SQL 接口公开）、`CREATE TABLE ... AS SELECT`、`CHECK TABLE`、`CHECKSUM TABLE`、`GET_LOCK/RELEASE_LOCK`。另：自增列只保证唯一、不保证多 server 连续；视图不支持 UPDATE/INSERT/DELETE；默认字符集 utf8mb4、排序规则 utf8mb4_bin、`lower_case_table_names` 只能为 2、外键默认 OFF。

### 应用场景
1. MySQL 分片与合并（作为从库接在主 MySQL 后做跨库实时查询，"多主一从"）
2. 直接替换 MySQL（无需分库分表，分布式由数据库层完成）
3. 数据仓库（TPC-H 复杂查询 10 秒内，超出能力部分用 TiSpark）
4. 作为其他系统模块（底层 KV 可作 HBase 替代，提供事务 API 与 Raw API 两套接口）

### 版本
社区版免费；企业版收费，提供服务与安全性支持。

### 苏三实操补充：定位、迁移与 AI 慢查询分析（2026-11-19，详见 [[摘要-为什么越来越多人用tidb]]）
- **一句话定位**：分库分表是在应用层"模拟"分布式（数据仍存多个独立 MySQL 实例，跨片查询/分布式事务/全局一致性自己解决），TiDB 是数据库本身"就是"分布式——把分布式从应用层收回数据库层，面对一个逻辑上完整的数据库，背后怎么分布它自己管
- **AUTO_RANDOM 与写入热点**：表无显式主键时 TiDB 用 `_tidb_rowid` 作行标识，与自增列**共用一个分配器可能跳号**；大写入量表建议显式主键 + `AUTO_RANDOM`（TiDB 特有，打散自增主键的写入热点，避免连续 ID 写同一 Region）
- **从 MySQL 迁移三步**：① 连接串端口 3306→4000，JDBC 驱动/连接池/大部分 SQL 语法不动；② 建表语句处理 AUTO_INCREMENT 坑（见上）；③ 跨库 JOIN 直接写——分库分表时代要么应用层拼要么广播表，TiDB 自己决定拆算合并
- **AI 辅助慢查询分析**：TiDB 慢查询日志结构化——把慢查询日志 + EXPLAIN 结果喂给 AI，让它分析"为什么没走索引、该加什么索引"（例：`WHERE status='PENDING' AND created_at>...` 只有单列索引 → 建联合索引 `(status, created_at)`）；AI 会提示 DDL 在线不锁表但耗资源宜低峰执行、`status` 区分度低可用**部分索引**（partial index，只索引 `status='PENDING'` 的行减小索引体积）；边界——AI 帮你理解执行计划，"索引到底该不该加"（写入代价 vs 查询收益）由人权衡
- **新案例（2026-11）**：[[Kimi]] 用 TiDB Cloud 为 AI Agent 提供数据库基础设施，1 秒内创建隔离数据库；Flipkart 用 TiDB on Kubernetes 每秒 100 万查询；擎文集团从 MySQL 分库分表 + Hive T+1 迁到一套 TiDB 同时支撑在线业务与实时分析
- **适用场景速查**：数据量大分库分表运维痛苦 / HTAP（交易+实时分析）/ 金融级高可用 / AI Agent 数据库基础设施 → 强烈推荐；依赖存储过程/触发器/全文索引 → 需评估；小数据量低并发 → 不推荐（资源消耗不划算）

## 关联连接

- [[PingCAP]] — 开发商
- [[黄东旭]] — 作者
- [[newsql]] — 所属数据库品类
- [[htap]] — 混合负载定位
- [[Raft]] — 多副本共识协议
- [[MySQL]] — 协议兼容与迁移来源
- [[sharding]] — 被替代/合并的对象
- [[kubernetes-introduction]] — 云原生部署所依托的编排平台
- [[摘要-tidb-newsql入门]] — 来源
- [[摘要-为什么越来越多人用tidb]] — 来源（2026-11-19 苏三：定位/迁移三步/AUTO_RANDOM/AI 慢查询分析/新案例）
- [[苏三]] — 2026-11-19 来源作者
- [[ShardingSphere]] — 被替代方案的代表中间件（痛点来源）
