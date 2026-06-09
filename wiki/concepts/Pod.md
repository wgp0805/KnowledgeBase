---
title: "Pod"
type: concept
tags: [Kubernetes, 容器编排, 调度]
sources: [raw/01-articles/同事一个比喻，让我搞懂了Docker和k8s的核心概念.md]
last_updated: 2026-06-09
---

## 定义
Pod 是 Kubernetes 集群调度的最小单元，一个 Pod 内可以包含一个或多个容器，这些容器共享网络命名空间和存储卷。

## 为什么需要 Pod
K8s 不直接调度容器，而是通过 Pod 封装一层，因为有些场景下容器需要紧密配合：
- **共享网络**：同一 Pod 内的容器用 localhost 通信
- **共享存储**：访问同一个挂载卷
- **同生共死**：一起启动、一起销毁，由 K8s 统一调度到同一台机器

## 关键信息
- 大多数微服务场景下一个 Pod 只放一个容器
- Pod 是"逻辑主机"的概念抽象
- Pod 内的容器共享 IP 地址和端口空间
- Pod 是 K8s 扩缩容、滚动更新的基本单位

## 关联连接
- [[摘要-同事一个比喻，让我搞懂了Docker和k8s的核心概念]] — 来源
- [[kubernetes-introduction]] — K8s 入门介绍
- [[kubernetes-detailed-guide]] — K8s 详细教程
- [[Docker]] — 容器引擎，Pod 内的运行实体
- [[microservices]] — 微服务架构，Pod 的主要使用场景
