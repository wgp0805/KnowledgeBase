---
title: "Raft"
type: concept
tags:
  - 分布式
  - 共识算法
sources: []
last_updated: 2026-09-15
---

## 定义
可理解的分布式共识算法（Ongaro & Ousterhout 2014），拆成领导者选举（随机超时）、日志复制（多数派提交）、成员变更（联合共识）三件事，etcd/ZooKeeper 类系统用它做状态机复制。

## 关联连接
- [[Paxos]]
- [[分布式]]
- [[高可用]]
- [[脑裂]]
