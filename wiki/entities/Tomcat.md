---
title: "Tomcat"
type: entity
tags: [Web服务器, Java, Servlet]
sources:
  - raw/09-archive/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md
  - "raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"
last_updated: 2026-10-26
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

### Tomcat 11 新特性（2026-10，详见 [[摘要-tomcat-11-new-features]]）
- 当前最新版本 11.0.27；三条维护版本线：9.0.x（Java EE 8 / Servlet 4.0 / `javax.*` / Java 8）、10.1.x（Jakarta EE 10 / Servlet 6.0 / `jakarta.*` / Java 11）、11.0.x（Jakarta EE 11 / Servlet 6.1 / `jakarta.*` / 最低 Java 17）。Spring Boot 4.x 默认内嵌 Tomcat 11。
- 实现的 Jakarta EE 11 Web 规范组：Servlet 6.1、Pages（JSP）4.0、EL 6.0、WebSocket 2.2、Authentication 3.1、Annotations 3.0。
- 架构分工：Connector（代号 Coyote）管网络通信；Engine→Host→Context→Wrapper（代号 Catalina）管"找到谁来处理"。虚拟线程动的就是 Connector 层线程模型。
- 虚拟线程：Connector 上 `useVirtualThreads="true"`，或定义 `org.apache.catalina.core.StandardVirtualThreadExecutor`（须写在 Connector 前，可多连接器共用）；Spring Boot 一行 `spring.threads.virtual.enabled=true`。
- 做减法：彻底移除 SecurityManager 支持（Java 17 废弃、Java 24 JEP 486 永久禁用）；移除 HTTP/2 Server Push（Servlet 6.1 降级为可选、浏览器已不支持）；清理 10.1 废弃 API 及 JSP 3.1 / EL 5.0 废弃 API（自定义 Valve、Realm 等内部类组件升级前需重新编译检查）。
- 默认更严格：`maxParameterCount` 默认值 10000→1000（防海量参数 DoS，业务表单字段多需手动调大）；Cookie 解析严格遵循 RFC 6265（引号成为值的一部分）；字节转字符失败直接抛异常而非静默乱码。
- HTTPS：经 Java FFM API（外部函数与内存 API）直接调用系统 OpenSSL（官方文档写 Java 25 起可用），免装 tomcat-native JNI 本地库，对容器化部署友好。
- Docker 运维坑：官方镜像 `webapps` 目录默认为空（直接访问 404 属正常），默认欢迎页与管理后台在 `webapps.dist`；war 包 `docker cp` 到 webapps 自动部署。

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
- [[摘要-tomcat-11-new-features]] — 来源（Tomcat 11 新特性全景）
- [[Java]] — Java 17 基线与虚拟线程版本要求
- [[虚拟线程]] — Connector 虚拟线程线程模型
- [[servlet-6-1]] — Tomcat 11 实现的 Servlet 规范
- [[HTTP2]] — HTTP/2 Server Push 移除涉及
