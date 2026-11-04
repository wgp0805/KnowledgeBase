---
title: "摘要-mysql自增id用尽"
type: source
tags: [来源, 原始文件, MySQL, 面试, 自增id]
sources: [raw/09-archive/2026-11-02 - 面试官：线上 MySQL 的自增 id 用尽怎么办？.md]
last_updated: 2026-11-03
---

## 核心摘要

「Java学习者社区」（2026-11-02，源自简书）拆解 MySQL 各类自增 id 达到上限后的行为与处理，覆盖表自增 id、InnoDB row_id、Xid、InnoDB trx_id、thread_id 五种。

**关键结论**：
1. **表自增 id（unsigned int，4 字节）**：达到 2^32-1 后 AUTO_INCREMENT 不再增长，再插入拿相同 id 报主键冲突（ERROR 1062）——影响可用性但不丢数据。频繁插入删除的表可能用完，建表前评估应直接上 `bigint unsigned`（8 字节）
2. **InnoDB 系统 row_id（6 字节，仅无主键表）**：全局 dict_sys->row_id 递增，范围 0~2^48-1；达到 2^48 后归 0 循环，若表中已存在同 row_id 行则**新行覆盖旧行**——数据丢失，影响可靠性。结论：应主动创建自增主键，宁可主键冲突（可用性）也不被覆盖（可靠性）
3. **Xid（server 层，8 字节）**：global_query_id 纯内存变量，重启清零；靠"重启生成新 binlog 文件"保证同 binlog 内 Xid 唯一。理论上 2^64 次后可能同 binlog 重复，概率极小可忽略
4. **InnoDB trx_id（max_trx_id，8 字节，持久化）**：每行记录更新它的 trx_id，事务一致性视图与之对比判断可见性。**只读事务不分配 trx_id**（显示值=指针地址+2^48 的临时计算值，为减小视图活跃数组 + 减少锁冲突）。若 max_trx_id 达到 2^48-1 归 0 循环，会出现**必现脏读 bug**（新数据版本 trx_id=0 < 低水位 2^48-1，全被判定可见）；重启不清零，TPS 50w 下约 17.8 年触发，目前无实例达到但理论上必现
5. **thread_id（4 字节）**：thread_id_counter 达到 2^32-1 归 0，但 MySQL 用唯一数组保证 processlist 中不出现相同 thread_id

**核心权衡**：覆盖数据=数据丢失（可靠性受损）vs 主键冲突=插入失败（可用性受损），一般可靠性优于可用性。

## 关联连接
- [[MySQL]] — 主题实体（自增 id 用尽章节）
- [[MVCC]] — trx_id 与一致性视图的可见性判断机制
- 主键 — 自增主键 vs 无主键 row_id 的可靠性权衡（无独立页，纯文本标注）
- 脏读 — max_trx_id 循环导致的必现脏读 bug（无独立页，纯文本标注）
- [[transaction-management]] — Xid/trx_id 的事务标识体系
- [[摘要-mysql-primary-key-strategy]] — 关联的主键选型话题
- [[摘要-mysql-course]] — MySQL 完整教程来源
