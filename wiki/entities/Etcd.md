---
title: "Etcd"
type: entity
tags: [分布式, KV存储, 中间件, Raft]
sources: [raw/09-archive/为什么越来越多人用JD-hotkey？.md]
last_updated: 2026-10-27
---

## 定义

etcd 是基于 Raft 共识算法的分布式键值存储，提供强一致的配置存储与元数据管理，是 Kubernetes 集群状态的底座组件，也常作为各类框架的规则/元数据同步中枢。

## 关键信息

- **CAP 语义**：属 CP 系统——网络分区时拒绝服务以保一致性（与 ZooKeeper 同类，见 [[CAP理论]]）
- **底层共识**：[[Raft]] 算法（领导者选举随机超时、日志复制多数派提交、成员变更联合共识）
- **在 [[JD-hotkey]] 架构中的角色**：Client/Worker 通过 Etcd 同步热 key 判定规则（如"2 秒内 20 次算热"）与 Worker 集群地址；业务侧以 `hotkey.etcd-server` 配置指向（默认 `http://127.0.0.1:2379`）
- **其他常见角色**：Kubernetes 中保存集群所有状态数据（见 k8s 相关 syntheses）；TiKV 等分布式存储用 Paxos/Raft 共识多副本实现热备

## 关联连接

- [[Raft]] — 底层共识算法
- [[CAP理论]] — CP 语义分类
- [[JD-hotkey]] — 热 key 框架的规则/地址同步组件
- [[摘要-jd-hotkey热key探测]] — 来源
