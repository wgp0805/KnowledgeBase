---
title: "JDK27"
type: entity
tags: [Java, JDK, 2026]
sources: [raw/09-archive/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
Java Development Kit 27（JDK 27），对应 JSR 402，是 Java SE 27 的参考实现。2026年9月15日发布，包含9项JEP增强功能，其中G1 GC成为所有环境的默认、对象头紧凑化以及后量子加密默认启用是三大默认行为变更。

## 关键信息
- **发布时间**：2026年9月15日，Oracle 正式发布
- **核心JEP**：JEP 523（G1默认GC），JEP 534（紧凑对象头），JEP 527（TLS 1.3后量子混合密钥交换），JEP 531-538 等
- **默认行为变更**：G1 GC全场景默认，对象头从96位压缩至64位（堆占用降低25%），TLS 1.3默认启用后量子算法
- **预览/孵化特性**：惰性常量（JEP 531，第三预览），原始类型模式匹配（JEP 532，第五预览），结构化并发（JEP 533，第七预览），Vector API（JEP 537，第十二孵化）
- **安全增强**：JFR 进程内数据脱敏，PEM 编码API（JEP 538，第三预览）

## 关联连接
- [[OpenJDK]] — Java开源参考实现
- [[Oracle]] — 公司，JDK 27的发布方
- [[G1 GC]] — 垃圾回收器概念
- [[Compressed OOP]] — 对象压缩概念
- [[Post-quantum cryptography]] — 后量子加密概念
- LazyConstant — 惰性常量概念
- StructuredTaskScope — 结构化并发概念
- [[Vector API]] — 向量计算概念
- [[摘要-jdk27-正式发布-人麻了]] — JDK 27 正式发布解读来源