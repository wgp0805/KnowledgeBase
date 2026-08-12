---
title: "Tomcat"
type: entity
tags: [Web服务器, Java, Servlet]
sources:
  - raw/01-articles/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md
last_updated: 2026-08-12
---

## 定义
Apache Tomcat 是 Apache 软件基金会的开源 Servlet 容器和 Web 服务器，实现了 Java Servlet、JavaServer Pages（JSP）和 WebSocket 规范，是 Java Web 应用最常用的运行环境。

## 关键信息
- Servlet 容器：实现 Java Servlet 和 JSP 规范
- 嵌入式支持：Spring Boot 内嵌 Tomcat 作为默认 Web 服务器
- 连接器：Coyote（HTTP/HTTPS/AJP）
- 部署方式：WAR 包部署或嵌入式运行
- 版本与 Servlet 规范对应：Tomcat 10 → Servlet 6.0、Tomcat 11.x → Servlet 6.1（Jakarta EE 11）
- Spring Boot 4.0 默认使用 Tomcat 11，全面适配 Servlet 6.1

### 代理信任配置（RemoteIpValve）
Tomcat 通过 `RemoteIpValve` 解析代理转发的 IP 头字段，核心配置项：
- `remote-ip-header`：指定 IP 头字段名（通常为 `X-Forwarded-For`）
- `protocol-header`：协议头字段（通常为 `X-Forwarded-Proto`）
- `internal-proxies`：信任的内网代理 IP 正则表达式，仅匹配此表达式的请求才解析 XFF，防止客户端伪造

**Spring Boot YAML 配置示例**：
```yaml
server:
  tomcat:
    remoteip:
      remote-ip-header: X-Forwarded-For
      protocol-header: X-Forwarded-Proto
      internal-proxies: 192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}
```

详见 [[摘要-springboot获取真实客户端ip]] 和 [[IP伪造防护]]。

## 关联连接
- [[SpringBoot]] — 内嵌 Tomcat
- [[Nginx]] — 常作为反向代理
- [[Filter]] — Servlet 规范中的责任链实现
- [[Servlet]] — Java Web 基础规范
- [[X-Forwarded-For]] — 代理链 IP 传递头字段
- [[IP伪造防护]] — internal-proxies 防伪造配置
- [[代理链路]] — 多层代理下 IP 传递机制
- [[摘要-springboot获取真实客户端ip]] — 代理信任配置完整方案
