---
title: "Post-quantum cryptography"
type: concept
tags: [Security, Cryptography, JDK 27]
sources: [raw/09-archive/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
后量子加密，是指即使面对大规模量子计算机的攻击也能保持安全的加密算法。JDK 27的JEP 527为TLS 1.3引入 **后量子混合密钥交换算法**，默认启用，无需修改代码。

## 核心概念
- **混合算法策略**：将抗量子算法与传统算法结合，即使传统算法被破解，抗量子算法部分仍保安全
- **支持的算法**：
  - **X25519MLKEM768**（默认优先级最高）
  - **SecP256r1MLKEM768**
  - **SecP384r1MLKEM1024**
- **默认启用**：使用 `javax.net.ssl` API的应用升级JDK 27后自动获得保护
- **攻防策略**：攻击者“先存后破”策略——现在存储加密流量，量子计算成熟后解密
- **无代码改动**：现有HTTPS通信在升级JDK 27后自动获得后量子保护

## 关联连接
- [[JDK27]] — 包含该特性的版本
- TLS 1.3 — 传输层安全协议
- X25519MLKEM768 — 具体后量子算法
- Quantum Computing — 量子计算威胁
- SSL/TLS Security — 安全协议概念