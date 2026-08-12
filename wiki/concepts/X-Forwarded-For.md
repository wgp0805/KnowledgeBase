---
title: "X-Forwarded-For"
type: concept
tags: [HTTP头, 代理, IP, 安全]
sources: [raw/01-articles/SpringBoot 中获取真实客户端 IP 的终极方案，99% 的人都没做对！.md]
last_updated: 2026-08-12
---

## 定义
X-Forwarded-For（XFF）是 HTTP 扩展请求头，用于在多层代理链路中传递客户端真实 IP。每经过一层代理，代理服务器将上一跳的 IP 追加到该头字段末尾，形成逗号分隔的 IP 序列。

## 格式规则
```
X-Forwarded-For: 客户端真实IP, 代理服务器1IP, 代理服务器2IP, ...
```

- **最左侧 IP**：原始客户端的真实 IP
- **后续 IP**：请求经过的各级代理服务器 IP
- **分隔符**：英文逗号

### 场景示例
| 场景 | X-Forwarded-For 值 |
|------|---------------------|
| 无代理 | null |
| 单代理 | `123.45.67.89` |
| 两级代理 | `123.45.67.89, 10.0.1.100` |
| 多级代理 | `123.45.67.89, 203.0.113.195, 198.51.100.10` |

## 安全风险
X-Forwarded-For 可被客户端伪造。攻击者可在请求中直接设置该头字段，使应用误判来源 IP。

### 防护方案
通过配置 `internal-proxies`（Tomcat）仅信任内网代理服务器 IP 段，应用会忽略客户端直接传递的 X-Forwarded-For，只解析可信代理转发的头字段。

## 解析策略
生产级解析逻辑（见 [[摘要-springboot获取真实客户端ip]] 中的 `parseXForwardedFor` 方法）：
1. 从后往前遍历 IP 列表，过滤内网 IP，返回第一个有效公网 IP
2. 无公网 IP 时，返回第一个格式合法的 IP（可能是内网 IP）
3. 无任何有效 IP 时返回 null

## 关联连接
- [[代理链路]] — XFF 在多层代理中的传递机制
- [[IP伪造防护]] — XFF 伪造风险与防护
- [[Tomcat]] — 通过 remoteIpHeader 配置解析 XFF
- [[SpringBoot]] — 应用层 XFF 解析配置
- [[摘要-springboot获取真实客户端ip]] — 生产级 XFF 解析方案
