---
title: "Nacos"
type: entity
tags: [微服务, 注册中心, 配置中心]
sources: [raw/09-archive/docker部署nacos.md, raw/09-archive/pmhub微服务学习.md, raw/09-archive/为什么越来越多人用Nacos？.md]
last_updated: 2026-08-05
---

## 定义
Nacos（Dynamic Naming and Configuration Service）是阿里巴巴开源的微服务基础设施组件，提供服务发现和配置管理能力。核心价值在于把"服务注册与发现 + 动态配置管理 + 服务管理"做成**一体化**，只需维护一套系统，服务发现和配置推送共享同一套基础设施。

## 关键信息
- 服务注册与发现：替代 Eureka，支持健康检查
- 配置管理：动态配置更新，支持 namespace/group/dataId 三级隔离
- 部署模式：单机（Derby 内嵌数据库）和集群（MySQL 存储）
- Docker 部署方式：环境变量配置 MySQL 数据源
- 命名空间隔离：通过 namespace 实现环境和配置隔离（如生产/灰度），是全链路灰度发布的第一步
- 灰度实践：创建独立的 gray-namespace，灰度服务注册在此命名空间，通过 `service.gray.tag` 元数据标记节点身份

### 一致性双模（AP/CP）
Nacos 既是 AP 也是 CP，按场景切换：
- **AP 模式（服务发现）**：基于 [[Distro协议]]，最终一致性优先保证可用性。服务实例频繁上下线，多一个/少一个实例对业务体感影响有限，没必要强一致
- **CP 模式（配置管理）**：基于 JRaft（Raft 工程化实现），强一致性。配置写错导致部分节点值不一致会让业务行为"飘"，写入须多数派确认成功。工程注意：必须 ≥3 节点（Raft 需选举）、写走 Leader、Leader 挂掉重新选举期间短暂不可写、配置存 MySQL（Raft 只协调一致性不是存储）

### 架构模块
核心模块：服务发现（NameService）、配置管理（ConfigService）、**AI Registry**（3.0 新增），一致性协议层使用自研 Distro 和 Raft 保证数据一致性。

### 性能演进
- Nacos 2.0：通信从 HTTP 升级到 **gRPC**，性能提升 10 倍。实测从 1.4 升 2.1，服务发现延迟 800ms → 20ms（降 96%），连接数降 8 倍，无需改业务代码
- Nacos 3.0：定位升级为"AI Agent 应用平台"，新增 [[AI Registry]] 模块（含 MCP Registry）

### 注册表读写优化
服务发现是典型"读多写少"，注册表更新使用 **CopyOnWrite**：复制原内存结构、操作完再替换，读操作完全无锁，读永远看到一致数据。

### 配置推送机制
配置推送走**长轮询（Long Polling）**而非 WebSocket（HTTP 简单、兼容性好、天然支持超时重试、防火墙友好）。

### 对比其他注册中心
| 对比维度 | Nacos | Eureka | Consul | ZooKeeper |
| --- | --- | --- | --- | --- |
| 一致性协议 | AP+CP 双模 | AP | CP | CP |
| 配置中心 | 原生支持 | 需额外组件 | 较弱 | 需自己搞 watch |
| 控制台 | 功能丰富 | 简单 | 有 | 无 |
| 健康检查 | 心跳+多种方式 | 仅心跳 | HTTP/TCP/gRPC | 心跳 |
| Spring Cloud 集成 | 深度集成 | 原生 | 支持 | 需适配 |
| 多数据中心 | 有限 | 不支持 | 原生支持 | 不支持 |
| 服务管理 | 完善 | 无 | 有 | 无 |
| AI 原生支持 | 3.0 AI Registry | 无 | 无 | 无 |

### 优缺点
- 优点：注册+配置一体化、AP/CP 双模切换、性能强悍、Spring Cloud Alibaba 零摩擦集成、生态成熟（命名空间/灰度/推送/多语言 SDK）、AI 时代持续进化、Apache 2.0
- 缺点：多语言 SDK 不均衡（Java 最完整，Go/Node 在追）、文档更新跟不上 3.0 版本、大规模集群部署较复杂（3 节点+MySQL）、2.x gRPC 端口需额外放行（主端口+1000）

## 关联连接
- [[Docker]] — 容器化部署
- [[SpringBoot]] — 客户端集成
- [[RocketMQ]] — 消息队列
- [[SpringCloudGateway]] — API 网关
- [[grayscale-release]] — 全链路灰度发布的命名空间隔离基础
- [[Distro协议]] — AP 模式的底层协议
- [[AI Registry]] — 3.0 新增模块（面向 AI Agent）
- [[长轮询]] — 配置推送机制
- [[Eureka]] — 主要替代对象
- [[摘要-为什么越来越多人用Nacos]] — 来源
- [[摘要-alibaba-product-manual]] — 阿里巴巴产品手册，介绍阿里巴巴集团旗下各产品线、服务体系及平…
- [[摘要-pmhub微服务学习]] — 记录 PmHub 微服务项目学习路线，涵盖 Nacos 注册…
- [[摘要-SpringBoot优雅的加载配置文件的几种方式]] — 介绍 Spring Boot 加载配置文件的多种方式：@Va…
