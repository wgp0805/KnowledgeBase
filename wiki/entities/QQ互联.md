---
title: "QQ互联"
type: entity
tags: [实体, 第三方登录, 腾讯, OAuth]
sources: [raw/09-archive/搞定 OAuth 2.0 第三方登录，So Easy !.md]
last_updated: 2026-09-16
---

## 定义
QQ 互联是腾讯开放平台的第三方登录授权服务，基于 OAuth 2.0 协议，允许第三方应用获取 QQ 用户授权后调用 OpenAPI 访问用户信息。

## 关键信息
- **官网**：connect.qq.com
- **文档地址**：https://wiki.connect.qq.com/
- **接入流程**：
  1. 开发者注册并实名认证
  2. 进入 QQ 互联管理中心创建网站应用
  3. 备案域名并通过审核
  4. 注册应用信息，获取 APP ID 和 APP Key
- **OAuth 2.0 处理流程**：
  1. 申请接入，获取 appid 和 apikey
  2. 开发应用并设置协作者账号测试联调
  3. 放置 QQ 登录按钮
  4. 通过用户登录验证和授权获取 Access Token（有效期 30 天）
  5. 通过 Access Token 获取用户 OpenID
  6. 调用 OpenAPI 请求访问或修改用户授权的资源
- **关键接口**：
  - `https://graph.qq.com/oauth2.0/authorize` — 授权请求
  - `https://graph.qq.com/oauth2.0/token` — 换取 access_token
  - `https://graph.qq.com/oauth2.0/me` — 获取 openid
  - `https://graph.qq.com/user/get_user_info` — 获取用户信息
- **Code 有效期**：10 分钟内过期
- **Token 有效期**：30 天（用户再次登录时自动刷新）

## 关联连接
- [[OAuth2]] — 使用的协议
- [[腾讯]] — 所属公司
- [[GitHub]] — 对比的第三方登录平台
- [[State-CSRF防护]] — CSRF 防护机制
- [[摘要-oauth2-第三方登录]] — 来源