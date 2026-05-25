---
title: "kubernetes-introduction"
type: synthesis
tags: [容器, 编排, DevOps, 微服务]
sources: []
last_updated: 2026-05-25
---

## 核心摘要

Kubernetes（K8s）是 Google 开源的容器编排平台，用于自动化部署、扩展和管理容器化应用。它把多台服务器抽象成一个"超级计算机"，自动决定容器在哪里运行、怎么运行。[[Docker]] 是"打包应用的箱子"，K8s 是"管理成千上万个箱子的调度中心"。

## 核心功能

| 功能 | 说明 |
|------|------|
| 自动调度 | 根据资源需求自动把容器分配到合适的服务器 |
| 自我修复 | 容器挂了自动重启，节点挂了自动迁移 |
| 水平扩展 | 一条命令增加/减少容器副本数 |
| 服务发现 | 容器之间自动找到对方，无需手动配置 IP |
| 滚动更新 | 零停机发布新版本，出问题自动回滚 |
| 配置管理 | ConfigMap/Secret 统一管理配置和密钥 |
| 存储编排 | 自动挂载本地/云存储/网络存储 |

## K8s vs Docker

| 维度 | Docker | Kubernetes |
|------|--------|------------|
| 定位 | 单机容器引擎 | 多机容器编排平台 |
| 管理范围 | 单台机器上的容器 | 集群中所有机器的容器 |
| 扩展能力 | 手动 docker-compose up | 自动扩缩容（HPA） |
| 高可用 | 需要自己实现 | 内置副本机制、故障自愈 |
| 适用规模 | 几个~几十个容器 | 几百~几万个容器 |
| 学习曲线 | 低（几小时上手） | 高（概念多、配置复杂） |

K8s 不是 Docker 的替代品，而是容器编排平台。**K8s 不依赖 Docker**：K8s 1.24+ 已移除 dockershim，改用 CRI 标准接口，默认运行时是 containerd（Docker 的核心组件）。用 Docker 打包的镜像 K8s 能跑（遵循 OCI 标准），但运行时不一定是 Docker。

## 适用场景

**适合**：
- [[microservices]] 架构（几十上百个服务需要协调）
- 需要高可用（服务不能停）
- 流量波动大（需要自动扩缩容）
- 多环境部署（开发/测试/生产一致性）
- [[CI-CD]] 流水线（自动化部署）

**不适合**：
- 单体应用（一个 JAR 包搞定的事）
- 个人项目/小团队（运维成本太高）
- 容器数量 < 10 个（杀鸡用牛刀）
- 没有专职运维人员

## 核心概念

```
集群 (Cluster)
├── Master 节点（控制中心）
│   ├── API Server（接收指令）
│   ├── Scheduler（决定容器跑在哪）
│   ├── Controller Manager（维持期望状态）
│   └── etcd（存储集群状态）
│
└── Worker 节点（干活的机器）
    ├── kubelet（汇报状态、管理容器）
    ├── kube-proxy（网络转发）
    └── Pod（最小调度单位）
        ├── Container A
        └── Container B
```

**核心资源对象**：
- **Pod**：最小部署单元，一个 Pod 可包含多个容器
- **Deployment**：管理 Pod 的副本数、滚动更新
- **Service**：为 Pod 提供稳定的网络入口（负载均衡）
- **Ingress**：集群入口，域名路由到 Service
- **ConfigMap/Secret**：配置和密钥管理
- **PV/PVC**：持久化存储

## 学习路径

1. 先掌握 [[Docker]]
2. 理解 [[microservices]]
3. 学习 K8s 核心概念（Pod、Deployment、Service）
4. 本地实践（minikube 跑 Spring Boot 应用）
5. 生产部署（托管 K8s 服务如阿里云 ACK）

## 关联连接
- [[Docker]] — 容器引擎，K8s 的管理对象
- [[microservices]] — 微服务架构，K8s 的主要应用场景
- [[CI-CD]] — 持续集成/交付，K8s 的部署场景
- [[SpringBoot]] — Java 应用容器化部署
