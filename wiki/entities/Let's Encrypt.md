---
title: "Let's Encrypt"
type: entity
tags: [SSL, HTTPS, 证书, 安全, 免费]
sources: [raw/01-articles/2026-07-29-Docker部署Keycloak：企业级身份认证平台搭建 - 暮色之狐.md]
last_updated: 2026-07-30
---

## 定义
Let's Encrypt 是一个免费、自动化、开放的证书颁发机构（CA），提供免费 SSL/TLS 证书，帮助网站低成本启用 HTTPS 加密。

## 关键信息
- **定位**：非营利性数字证书认证机构，由互联网安全研究小组（ISRG）运营
- **特点**：免费、自动化、开放、无需人工审核域名
- **使用方式**：通过 ACME 协议自动申请和续签证书，常用客户端有 Certbot、acme.sh 等
- **与 Keycloak 的关系**：被推荐为 Keycloak 生产环境 HTTPS 的免费证书方案

## 关联连接
- [[Keycloak]] — 建议搭配使用的身份认证平台
- [[Nginx]] — 使用 Let's Encrypt 证书的反向代理
- [[摘要-Docker部署Keycloak]] — 来源
