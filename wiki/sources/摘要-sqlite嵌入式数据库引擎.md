---
title: "SQLite 3.x：全球部署最广泛的零配置嵌入式ACID关系型数据库引擎"
type: source
tags: [SQLite, 嵌入式数据库, RDBMS, ACID, WAL, 数据库引擎]
sources: [raw/01-articles/2026-09-13-[嵌入式数据库RDBMS] SQLite 3.x 全球部署最广泛的零配置、单文件、嵌入式 ACID 关系型数据库引擎 - 千千寰宇.md]
last_updated: 2026-09-14
---

# 摘要：SQLite 3.x 嵌入式数据库引擎

## 核心摘要
SQLite是由D. Richard Hipp于2000年发布的自包含、零配置、事务性嵌入式SQL数据库引擎，整个数据库通常就是磁盘上的一个普通文件。截至2026年最新版本为3.53.4，3.x系列已连续演进20余年，官方估计全球活跃使用中的SQLite数据库超过一万亿个，是嵌入式数据库事实上的标准。

## 关键要点
- 产品定位：嵌入式/进程内关系型数据库引擎，面向"不需要DBA、不需要单独服务器"的场景
- 许可证：公有领域（Public Domain），无任何版权限制，可任意复制、修改、商用
- 核心架构：分层管道式 Interface→Tokenizer→Parser→Code Generator→VDBE→B-tree→Pager→VFS
- 事务模式：默认rollback journal，WAL模式支持读不阻塞写、写不阻塞读（但同一时刻仍只有一个写事务）
- 核心优势：零部署零配置、极小体积（数百KB）、单文件可移植、极高可靠性、无版权风险、跨平台
- 主要短板：写并发受限、不支持网络访问、无用户权限体系、无内置加密、SQL方言不完全标准
- 适用场景：移动端App本地存储、浏览器桌面应用、嵌入式IoT设备、单机工具软件、边缘计算缓存
- 知名用户：微信（WCDB+SQLCipher）、Apple iOS/macOS、Firefox、Chrome、Android、Windows 10/11、Dropbox、Adobe Lightroom

## 详细内容

### 产品概述
SQLite不是传统的客户端/服务端数据库，而是被直接链接到应用进程中的C语言库。诞生于2000年8月，最初为美国海军舰艇项目打造，目标是摆脱传统RDBMS"需要安装、配置、管理"的依赖。

### 发展历程关键节点
- 2000年 1.0.0：首次发布，确立嵌入式零配置定位
- 2004年 3.0.0：3.x时代开端，manifest类型系统、BLOB支持、UTF-8/UTF-16双编码
- 2010年 3.7.0：首次引入WAL模式
- 2015年 3.9.0：加入JSON1扩展、FTS5全文检索、表达式索引
- 2018年 3.24/3.25：支持UPSERT和窗口函数
- 2022年 3.38.0：JSON函数从扩展变为内置默认
- 2024年 3.45.0：引入JSONB二进制JSON存储格式
- 2026年 3.53.4：当前最新稳定版

### 工作原理与架构
分层管道式架构：上层把SQL文本编译成字节码，下层由VDBE执行字节码并通过B-tree/Pager/VFS落盘。

核心概念：
- **B-tree/B+tree**：用B+tree组织表数据，B-tree组织二级索引
- **Page（页）**：默认4096字节，是Pager调度与缓存的最小单位
- **Pager（分页器）**：负责页读入内存、脏页写回、管理journal或WAL，是事务与崩溃恢复核心
- **WAL**：所有修改先追加到-wal文件，读可走WAL，写只追加，读不阻塞写、写不阻塞读
- **VFS**：最底层抽象，屏蔽Unix/Windows/RTOS差异
- **VDBE**：虚拟数据库引擎，执行SQL编译产生的字节码

### 事务与锁机制
- rollback journal模式（默认）：写事务前对整个数据库文件加RESERVED/EXCLUSIVE锁，写期间其他连接只能读
- WAL模式：写者把新页追加到-wal文件不修改主库，读者同时看到主库+WAL快照，写者之间仍通过WAL头部锁互斥，同一时刻只有一个写事务

### 核心优势
- 零部署零配置：没有服务进程，没有my.cnf，不需要root权限，链接即用
- 极小体积：编译后通常仅数百KB
- 单文件可移植：数据库是普通磁盘文件，可直接拷贝备份
- 极高可靠性：公有领域、十余年高强度测试
- 无版权风险：公有领域可任意闭源商用
- 读性能优秀：无网络开销、无进程间通信，单机读多写少场景常高于C/S数据库

### 主要短板
- 写并发受限：WAL模式下同一时刻仍只能有一个写事务
- 不支持网络访问：没有内置C/S协议
- 无用户权限体系：访问控制依赖操作系统文件权限
- 无内置加密：核心版不加密，官方另有商业SEE扩展
- SQL方言不完全标准：不支持RIGHT/FULL OUTER JOIN、存储过程体系较弱

### 竞品对比
SQLite在"嵌入式+完整SQL+ACID+公有领域"组合上几乎没有真正对手：
- Berkeley DB/LevelDB/RocksDB：放弃SQL，面向KV
- H2/Derby：绑定Java/JVM
- DuckDB：面向OLAP，与SQLite面向OLTP互补
- MySQL/PostgreSQL：C/S架构，适合多客户端并发写

### 行业应用案例
- **微信**：WCDB框架基于SQLite+SQLCipher，本地聊天记录、联系人、会话列表加密存储
- **Chroma向量数据库**：0.4.0起用SQLite做元数据存储（chroma.sqlite3）
- **Apple iOS/macOS**：原生应用主数据存储，Core Data默认持久化栈即SQLite
- **Firefox**：places.sqlite存书签历史、favicons.sqlite存图标
- **Chrome/Android**：Chrome历史Cookie等本地档案；Android原生内置SQLite
- **Windows 10/11**：将SQLite作为系统核心组件
- **Adobe Lightroom**：照片目录.lrcat文件本身就是SQLite数据库
- **Airbus A350 XWB**：飞行软件中使用SQLite

### 为什么被反复选择
零部署零管理（随应用打包分发）、单文件可移植可归档、跨平台跨语言、可靠性与免费、可加密扩展（如SQLCipher）。

## 关联连接
- [[SQLite]]
- [[嵌入式数据库]]
- [[WAL模式]]
- [[Chroma向量数据库]]
- [[WCDB]]
- [[DuckDB]]
