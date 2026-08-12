---
title: "SpringBoot 中获取真实客户端 IP 的终极方案"
type: source
tags: [SpringBoot, IP, X-Forwarded-For, 代理, 安全, Tomcat, 限流, 黑名单]
sources: [raw/01-articles/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md]
last_updated: 2026-08-12
---

## 核心摘要
小哈学Java 发布的生产级方案，解决 Spring Boot 中获取真实客户端 IP 的常见坑：`request.getRemoteAddr()` 在多层代理链路下只能拿到代理 IP 而非用户真实 IP。文章提供完整的 `IpUtils` 工具类（支持 X-Forwarded-For 解析、内网 IP 过滤、IPv6 兼容）、Tomcat 代理信任配置（Java/YAML 两种方式）、IP 安全过滤器（黑名单 + 令牌频率限制 + 可疑请求检测）以及生产环境最佳实践。

## 关键要点

### IP 传递底层逻辑
现代 Web 请求链路：`用户 → CDN → 负载均衡器 → 网关 → 应用服务器`，每层中间件都会修改请求信息，导致 `getRemoteAddr()` 失效。

核心请求头（可信度从高到低）：
| 请求头 | 含义 | 可信度 |
|--------|------|--------|
| X-Forwarded-For | 代理链 IP 序列 | ⭐⭐⭐⭐ |
| X-Real-IP | 最后一个代理 IP | ⭐⭐⭐ |
| Proxy-Client-IP | Apache 代理 IP | ⭐⭐ |
| WL-Proxy-Client-IP | WebLogic 代理 IP | ⭐⭐ |

**X-Forwarded-For 格式**：`客户端真实IP, 代理服务器1IP, 代理服务器2IP, ...`（最左侧为原始客户端 IP，逗号分隔）

### IpUtils 工具类核心逻辑
1. **优先解析 X-Forwarded-For**：从后往前过滤内网 IP，优先返回第一个有效公网 IP
2. **降级解析其他代理头**：X-Real-IP、Proxy-Client-IP、WL-Proxy-Client-IP、HTTP_CLIENT_IP、HTTP_X_FORWARDED_FOR
3. **最终降级 getRemoteAddr**：兼容 IPv6 本地回环地址转换（`0:0:0:0:0:0:0:1` → `127.0.0.1`）
4. **内网 IP 过滤**：10.x、192.168.x、172.16-31.x 段
5. **IP 格式校验**：IPv4 正则 + IPv6 简单判断（包含冒号即合法）

### Tomcat 代理信任配置
- **Java 配置**：`WebServerFactoryCustomizer<TomcatServletWebServerFactory>` 设置 `remoteIpHeader`、`protocolHeader`、`internalProxies`
- **YAML 配置**（推荐）：`server.tomcat.remoteip.remote-ip-header`、`protocol-header`、`internal-proxies`
- **核心安全原则**：`internal-proxies` 仅信任内网代理 IP 段，防止客户端伪造 X-Forwarded-For

### IP 安全防护
1. **IP 日志拦截器**：`HandlerInterceptor` 记录每个请求的真实 IP、URI、User-Agent
2. **IP 安全过滤器**：`Filter` 实现黑名单拦截（403）、频率限制（令牌桶 1 分钟 60 次，429）、可疑请求检测（无 User-Agent / 访问敏感路径自动加入黑名单）

### 生产环境最佳实践
1. 动态配置信任代理 IP（Nacos/Apollo 配置中心）
2. 环境隔离配置（开发/测试/生产不同代理规则）
3. 分布式频率限制（Redis 替代单机 ConcurrentHashMap）
4. 合理缓存 IP 结果（短期缓存 10 秒，减少重复解析）

### 核心安全原则
> 永远不要信任客户端直接传递的任何信息，所有 IP 相关字段必须经过可信代理服务器转发后再解析。

## 关联连接
- [[SpringBoot]] — 框架层面配置代理识别
- [[Tomcat]] — 嵌入式容器代理信任配置
- [[X-Forwarded-For]] — 代理链 IP 传递核心头字段
- [[代理链路]] — 多层代理下 IP 传递机制
- [[IP伪造防护]] — 通过 internal-proxies 配置防伪造
- [[IP限流]] — 令牌桶频率限制实现
- [[Filter]] — Servlet 责任链实现安全过滤
- [[Interceptor]] — Spring MVC 拦截器实现 IP 日志
- [[小哈]] — 文章作者
