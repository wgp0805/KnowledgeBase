---
title: "Token认证机制"
type: concept
tags: [认证, 安全, Token]
sources: [raw/09-archive/抖音一面：二维码扫码登录原理.md]
last_updated: 2026-06-29
---

## 定义
**基于 Token 的认证机制**是移动互联网时代主流的身份认证范式：客户端首次账号密码登录后，服务端下发一个绑定"账号 + 设备"的 Token 字符串，后续所有 API 请求都携带 Token + 设备信息完成鉴权——客户端**不再存储密码**。

## 关键信息

### 工作流程
1. **首次登录**：客户端将账号密码 + **设备信息**一起发送给服务端
2. **服务端校验**：账号密码正确时，服务端创建一个数据结构：
   ```js
   const tokenData = {
     accountId: '账号ID',
     deviceId: '登录的设备ID',
     deviceType: 'ios | android | pc | web'
   }
   ```
3. **生成 Token**：服务端生成一个映射到该数据结构的 token 字符串，返回客户端
4. **客户端持久化**：客户端**本地保存 Token**，每次 API 调用都携带 token + 当前设备信息
5. **服务端鉴权**：通过 token 找到绑定的账号与设备，与请求中的设备信息**严格比对**，一致才放行

### 为什么不直接存密码
- **安全**：客户端被攻破时密码不会泄漏
- **可控**：服务端可单点失效任意 token（踢出登录、强制下线）
- **多端隔离**：每个设备一个 token，互不影响

### 为什么 Token 泄漏也不致命
设备信息是**第二把钥匙**：
- Token 单独泄漏 → 攻击者换其他设备访问时，设备信息不匹配 → 拒绝
- 必须 Token + 设备信息**双重泄漏**才能仿冒（设备信息通常含硬件特征，难以伪造）

### 自动登录的原理
应用首次登录后保存 Token 到本地（KeyChain/SharedPreferences），即使 App 进程被杀、手机重启，下次启动都能直接拿 Token 完成自动鉴权，无需重新输密码。

### 在扫码登录中的角色
扫码登录本质上是"让 PC 端获取属于自己的 Token"——但手机端的 Token 不能直接给 PC（Token 绑定的设备不同）。所以需要通过 [[QR码登录]] 的三阶段流程，**让服务端为 PC 设备签发 PC 专属 Token**。

### 相关方案
- [[JWT]]：无状态 Token，自包含信息，服务端不存储
- [[dual-token-mechanism]]：access token + refresh token 双 token 设计
- [[jwt-stateless]]：无状态认证模式
- [[token-blacklist]]：token 失效管理

## 关联连接
- [[摘要-二维码扫码登录原理]] — 来源
- [[QR码登录]] — 典型应用
- [[JWT]] — 自包含 Token 方案
- [[jwt-stateless]] — 无状态认证
- [[dual-token-mechanism]] — 双 token 设计
- [[token-blacklist]] — 失效管理
- [[SpringSecurity]] — Java 生态实现
