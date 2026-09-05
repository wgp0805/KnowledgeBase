---
title: "GhOst"
type: concept
tags: [MySQL, DDL, GitHub, 在线变更, binlog, 无触发器]
sources: [raw/01-articles/千万级的大表如何新增字段？.md]
last_updated: 2026-08-14
---

## 定义
gh-ost（GitHub's Online Schema Transmogrifier）是 GitHub 开源的无触发器 MySQL 在线表结构变更工具，通过异步解析 binlog 替代触发器同步增量数据，专为高并发大表 DDL 场景设计。

## 核心创新
**伪装为从库**：直连主库或从库，拉取 ROW 格式 binlog，解析 DML 事件（INSERT/UPDATE/DELETE），通过独立连接异步应用到影子表，与主库事务解耦。

## 关键流程
1. **全量拷贝**：按主键分块（`chunk-size` 控制）执行 `INSERT IGNORE INTO _table_gho SELECT ...`
2. **增量同步**：
   - INSERT → `REPLACE INTO`
   - UPDATE → 全行覆盖更新
   - DELETE → `DELETE`
3. **原子切换（Cut-over）**：
   - 短暂锁源表（毫秒级）
   - 执行 `RENAME TABLE source TO _source_del, _source_gho TO source`
   - 清理旧表

## 优势对比 PT-OSC
| 维度 | PT-OSC | gh-ost |
| --- | --- | --- |
| 增量同步 | 触发器（同事务） | binlog 异步（解耦） |
| 主库负载 | 高（触发器开销） | 低（无触发器） |
| 暂停/恢复 | 不支持 | 支持 |
| 高并发影响 | 性能下降 30%+ | 写入影响 <5% |

## 命令示例
```bash
gh-ost \
  --alter="ADD COLUMN age INT NOT NULL DEFAULT 0" \
  --host=主库IP --port=3306 --user=gh_user --password=xxx \
  --database=test --table=user \
  --chunk-size=2000 \
  --max-load=Threads_running=80 \
  --critical-load=Threads_running=200 \
  --execute --allow-on-master
```

## 监控与优化
- 进度跟踪：`echo status | nc -U /tmp/gh-ost.sock`
- 延迟控制：`--max-lag-millis=1500`，超阈值自动暂停
- 切换安全：`--postpone-cut-over-flag-file` 人工控制时机

## 适用场景
- 高并发大表（TB 级）
- 对写入影响敏感的生产环境

## 关联连接
- [[MySQL]] — 所属数据库
- [[OnlineDDL]] — 原生方案对比
- [[PT-OSC]] — 触发器方案对比
- [[摘要-千万级大表新增字段方案]] — 来源
