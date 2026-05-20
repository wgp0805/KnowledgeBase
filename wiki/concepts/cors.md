---
title: "cors"
type: concept
tags: [Web, 跨域, 安全]
sources: [raw/01-articles/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md]
last_updated: 2026-05-20
---

## 定义

CORS（Cross-Origin Resource Sharing）跨域资源共享，是一种允许浏览器向跨源服务器发出 XMLHttpRequest 请求的机制。前后端分离项目必须处理 CORS 问题。

## 核心原理

### 跨域场景

当前端和后端部署在不同域名/端口时，浏览器会阻止跨域请求。

### 解决方案

#### 开发环境：Vite Proxy

```typescript
// vite.config.ts
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8080',
      changeOrigin: true
    }
  }
}
```

#### 生产环境：后端 CORS 配置

```java
@Configuration
public class CorsConfig {
    @Bean
    public CorsFilter corsFilter() {
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(true);
        config.addAllowedOriginPattern("*");
        config.addAllowedHeader("*");
        config.addAllowedMethod("*");
        config.addExposedHeader("Authorization");
        config.setMaxAge(3600L);
        return new CorsFilter(source);
    }
}
```

#### 生产环境：Nginx 反向代理（推荐）

```nginx
location /api/ {
    proxy_pass http://backend:8080/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Spring Security 注意事项

- CORS 预检请求（OPTIONS）可能被 Security 拦截
- 确保 `CorsFilter` 在 `SecurityFilterChain` 之前执行
- 在 SecurityConfig 中配置：`http.cors(cors -> cors.configurationSource(...))`

## 关联连接
- [[Nginx]] — 反向代理方案
- [[SpringSecurity]] — Security 中的 CORS 配置
- [[Vue3]] — Vite Proxy 配置
- [[摘要-springboot4-security7-vue3-best-practice]] — 完整实践
- [[frontend-backend-separation]] — 前后端分离架构
