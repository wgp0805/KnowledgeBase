---
title: "SpringCloudStream"
type: entity
tags: [Spring, 消息队列, 微服务]
sources: [raw/01-articles/Spring Cloud Stream 整合 RocketMQ 完全指南.md]
last_updated: 2026-07-21
---

## 定义
Spring Cloud Stream（SCS）是 Spring 官方提供的事件驱动微服务抽象层，通过 Binder 机制屏蔽底层消息中间件差异，让业务代码只需面向 Supplier/Consumer/Function 函数式编程模型。

## 关键信息
- **核心架构**：业务代码 → SCS 统一 API → Binder → 具体消息中间件（RocketMQ/Kafka/RabbitMQ）
- **函数式编程模型**：Supplier（纯生产者）、Consumer（纯消费者）、Function（处理器，消费+生产）、BiConsumer（双输入消费者）
- **Binding 命名约定**：`{函数名}-{方向}-{索引}`（如 `sendMessage-out-0`）
- **StreamBridge**：推荐的生产者 API，支持按需发送消息，无需声明 Supplier Bean
- **高级消息头**：通过 `RocketMQHeaders.TAGS/KEYS/DELAY_LEVEL/TRANSACTIONAL` 设置消息元数据
- **多 Binder 支持**：通过 `spring.cloud.stream.binders` 配置多个独立 NameServer 集群

### 与原生 SDK 对比
| 维度 | 原生 RocketMQ SDK | Spring Cloud Stream |
|------|------------------|-------------------|
| 学习成本 | 需掌握 Producer/Consumer/PushConsumer | 只需掌握 Supplier/Consumer/Function |
| 中间件切换 | 需重写代码 | 更换 Binder 依赖 + 修改配置 |
| 高级特性 | 完整支持 | 通过扩展属性支持 |
| 生态集成 | 独立使用 | 与 Spring Cloud 无缝集成 |

## 关联连接
- [[摘要-spring-cloud-stream-rocketmq]] — 来源
- [[SpringCloudAlibaba]] — 版本兼容依赖
- [[RocketMQ]] — 底层消息中间件
- [[SpringBoot]] — 基础框架
- [[message-queue]] — 消息队列核心概念
