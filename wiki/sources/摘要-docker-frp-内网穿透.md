---
title: "摘要-docker-frp-内网穿透"
type: source
tags: [来源, 内网穿透, Docker, FRP, 部署]
sources: [raw/01-articles/2026-08-24 - 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~.md]
last_updated: 2026-08-25
---

## 核心摘要
小哈学Java 分享如何用 Docker + FRP（Fast Reverse Proxy）实现内网穿透，将本地微服务项目（小哈书，12 个服务+多个中间件，单机吃 14G 内存）暴露到公网，避免购买昂贵的高配云服务器。FRP 通过反向代理技术，由公网 frps 服务端转发请求到本地 frpc 客户端，支持 TCP/UDP/HTTP/HTTPS 多协议。文章给出完整的 Docker 镜像拉取、frps.toml/frpc.toml 配置文件、容器运行命令、安全组放行端口、管理后台访问等全流程实操。

## 关键信息
- **FRP 核心原理**：中间服务器转发，内网设备主动连接公网代理服务器，外部访问代理时转发到内网
- **优势**：开源免费、自建服务器数据更安全、跨平台、协议支持全面
- **对比工具**：FRP（自建服务器）/ Ngrok（免建但限制多）/ ZeroTier（P2P 直连）/ 花生壳（简单但收费）
- **部署架构**：云服务器跑 frps（bindPort 7000 + 管理后台 7500），本地电脑跑 frpc，配置 [[proxies]] 规则映射 localPort 到 remotePort
- **认证方式**：token 密钥验证，客户端与服务端必须一致
- **镜像版本**：fatedier/frps:v0.61.2、fatedier/frpc:v0.61.2

## 关联连接
- [[Docker]] — 容器化部署 FRP 服务端与客户端
- [[FRP]] — 开源内网穿透工具
- [[小哈]] — 公众号「小哈学Java」作者
- [[Nginx]] — 内网穿透目标端口（前端工程）
