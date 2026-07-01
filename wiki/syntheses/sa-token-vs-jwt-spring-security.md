---
title: "sa-token-vs-jwt-spring-security"
type: synthesis
tags: [Sa-Token, JWT, SpringSecurity, 认证, 选型对比]
sources: []
last_updated: 2026-07-01
---

# Sa-Token vs JWT + Spring Security 全面对比

## 对比总览

| 维度 | Sa-Token | JWT + Spring Security |
|------|----------|----------------------|
| **学习曲线** | 极低，API 如 `StpUtil.login()` 一行完成 | 陡峭，SecurityConfig + Filter + JWT 工具类需大量配置 |
| **开箱即用** | 登录、踢人下线、权限鉴权、OAuth2、SSO 一站式内置 | 需自行搭建完整认证体系 |
| **状态模式** | 默认基于 Redis 有状态 Token，支持 JWT 无状态模式 | JWT 无状态，需配合 Redis 黑名单实现吊销 |
| **权限控制** | RBAC + 按钮级 + 路由拦截，API 简单 | 极细粒度：`@PreAuthorize` + 过滤器链组合，功能更强 |
| **Token 续期** | 内置过期自动续签 | 需手动实现双 Token 机制 |
| **OAuth2/SSO** | Sa-OAuth2 模块即插即用 | Spring Security 内置 OAuth2 标准实现 |
| **微服务友好** | 有限，适合单体/简单分布式 | 非常成熟，网关透传 JWT 即可跨服务传递身份 |
| **生态深度** | 6k+ GitHub Stars，社区较小 | 全球最广泛的安全框架，文档极其丰富 |

## 优点

### Sa-Token
- 学习成本极低，新手半小时上手
- 企业常用功能开箱即用（同端互斥登录、二级认证、踢人下线）
- 代码量远少于 Spring Security

### JWT + Spring Security
- 无状态，天然适合前后端分离与微服务架构
- 安全控制最精细，可自定义的过滤器链灵活性最高
- OAuth2 标准兼容性最好，企业级最佳实践成熟

## 缺点

### Sa-Token
- 生态小，问题排查资源少
- JWT 模式不如原生 JWT 方案灵活
- 深度定制场景受限于框架固有能力

### JWT + Spring Security
- 配置量极大，小改动可能涉及多个类
- 纯 JWT 无法主动吊销 Token，必须引入 Redis 黑名单
- 版本升级破坏性大（Security 5→6→7 API 变动频繁）

## 选型建议

| 场景 | 推荐 |
|------|------|
| 中小项目/快速原型/管理后台 | **Sa-Token**，省时间 |
| 微服务/前后端分离/大型企业 | **JWT + Spring Security**，生态可靠 |
| 已有 Spring Security 的项目 | 继续用 Security，不要混用 |
| OAuth2/SSO 标准协议强需求 | Spring Security，标准实现最成熟 |
| 团队新手多，工期紧 | Sa-Token 是省心之选 |

## 关联连接
- [[JWT]] — JSON Web Token 认证机制
- [[SpringSecurity]] — 认证授权安全框架
- [[jwt-stateless]] — JWT 无状态认证原理
- [[token-blacklist]] — Token 黑名单机制
- [[dual-token-mechanism]] — 双 Token 续期方案
- [[spring-security-jwt-redis-best-practice]] — Spring Security + JWT + Redis 最佳实践
- [[摘要-token-redis-interview]] — JWT 与 Redis 的深度分析
