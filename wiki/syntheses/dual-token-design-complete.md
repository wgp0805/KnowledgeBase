---
title: "双 Token 设计完整案例"
type: synthesis
tags: [认证, JWT, Token, 安全, 架构设计]
sources:
  - raw/09-archive/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md
  - raw/09-archive/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md
  - raw/09-archive/SpringSecurity.md
last_updated: 2026-06-11
---

# 双 Token（AccessToken + RefreshToken）设计完整案例

## 一、要解决什么问题

### 核心矛盾

传统 Session 和纯 JWT 各有一套无法解决的缺陷：

| 方案 | 痛点 |
|------|------|
| Session | 服务端存储状态，无法水平扩展，集群方案复杂 |
| 纯 JWT | 签发后无法吊销，泄露后攻击者可用到过期（可能 7 天） |

**双 Token 的目标**：在"无状态认证"和"可吊销安全性"之间找到一个平衡点。

### 场景假设

一个电商系统，用户登录后：
- AccessToken 泄露后攻击者最多能用 30 分钟
- 用户改密码后，攻击者持有的 RefreshToken 立即失效
- 服务端可以在任何时候吊销某个用户的登录态（封号/踢下线）
- 用户不需要频繁输入密码登录

---

## 二、整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                        前端 (Vue3)                           │
│  localStorage: AccessToken(30min) + RefreshToken(7天)       │
│  Axios 拦截器: 401 自动续期，请求队列防并发                  │
└─────────────────────┬───────────────────────────────────────┘
                      │ Authorization: Bearer <AT>
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Nginx / Spring Cloud Gateway                │
│  路由转发、CORS、限流                                        │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              JwtAuthFilter (OncePerRequestFilter)            │
│  1. 提取 Authorization header                               │
│  2. 查 Redis 黑名单 → blacklist:<token>                     │
│  3. JWT 验签 → parseClaimsJws                               │
│  4. 构造 Authentication → SecurityContextHolder             │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              SecurityFilterChain (STATELESS)                 │
│  公开: /api/auth/login, /api/auth/refresh                   │
│  受保护: 其余所有 /api/**                                   │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              AuthController / Business Controllers           │
│  @PreAuthorize 或 @PostAuthorize 做细粒度权限               │
└─────────────────────────────────────────────────────────────┘
```

---

## 三、核心流程详解

### 3.1 登录 → 签发双 Token

```java
@PostMapping("/api/auth/login")
public Result login(@Valid @RequestBody LoginReq req) {
    // 1. 认证用户名密码
    Authentication auth = authenticationManager.authenticate(
        new UsernamePasswordToken(req.username(), req.password()));

    // 2. 签发 AccessToken (30分钟)
    String accessToken = Jwts.builder()
        .claim("userId", userId)
        .claim("role", "USER")
        .issuedAt(new Date())
        .expiration(new Date(System.currentTimeMillis() + 30 * 60 * 1000))
        .signWith(secretKey)
        .compact();

    // 3. 签发 RefreshToken (7天)，存入 Redis
    String refreshToken = UUID.randomUUID().toString().replace("-", "");
    redisTemplate.opsForValue().set(
        "refresh:" + refreshToken,
        userId + "::" + getClientInfo(request),       // 存用户 + 设备指纹
        7, TimeUnit.DAYS
    );

    return Result.ok(new TokenPair(accessToken, refreshToken));
}
```

**为什么 AccessToken 用 JWT 而 RefreshToken 用随机字符串？**
- AccessToken 频繁传输 → JWT 结构自带用户信息，**零 Redis 查询**即可鉴权
- RefreshToken 很少传输 → 用随机字符串，服务端完全掌控（Redis 里有啥它就代表啥），不具备 JWT 的"自包含"特性，也就更安全

### 3.2 每次请求 → 验证 AccessToken

```java
@Override
protected void doFilterInternal(HttpServletRequest request,
                                HttpServletResponse response,
                                FilterChain chain) {

    String token = extractToken(request);
    if (token == null) {
        chain.doFilter(request, response);
        return;
    }

    // 查 Redis 黑名单 — Redis 内网毫秒级，不影响性能
    if (Boolean.TRUE.equals(redisTemplate.hasKey("blacklist:" + token))) {
        throw new TokenInvalidException("Token已被吊销");
    }

    // JWT 验签 — 不查 DB，不查 Redis
    Claims claims = Jwts.parser()
        .verifyWith(secretKey)
        .build()
        .parseSignedClaims(token)
        .getPayload();

    UsernamePasswordAuthenticationToken auth =
        new UsernamePasswordAuthenticationToken(
            claims.get("userId"), null,
            List.of(new SimpleGrantedAuthority("ROLE_" + claims.get("role")))
        );
    SecurityContextHolder.getContext().setAuthentication(auth);
    chain.doFilter(request, response);
}
```

### 3.3 AccessToken 过期 → 无感刷新

```java
@PostMapping("/api/auth/refresh")
public Result refresh(@RequestBody RefreshReq req, HttpServletRequest request) {
    // 1. 从 Redis 取出 RefreshToken 对应的数据
    String data = redisTemplate.opsForValue().get("refresh:" + req.refreshToken());
    if (data == null) {
        // RefreshToken 不存在 → 已过期或已被吊销
        return Result.fail(401, "登录已过期，请重新登录");
    }

    String[] parts = data.split("::");
    String userId = parts[0];
    String clientInfo = parts.length > 1 ? parts[1] : "";

    // 2. 设备指纹校验（可选，按安全等级要求开启）
    String currentClient = getClientInfo(request);
    if (!clientInfo.equals(currentClient)) {
        // 设备变化 → 可能是 Token 被盗，触发安全策略
        revokeAllTokens(userId);     // 吊销该用户所有 RefreshToken
        notifyUser(userId);          // 通知用户
        return Result.fail(401, "设备环境异常，请重新登录");
    }

    // 3. RefreshToken Rotation：作废旧 RT，签发新 RT
    redisTemplate.delete("refresh:" + req.refreshToken());
    String newRefreshToken = UUID.randomUUID().toString().replace("-", "");
    redisTemplate.opsForValue().set(
        "refresh:" + newRefreshToken,
        userId + "::" + currentClient,
        7, TimeUnit.DAYS
    );

    // 4. 签发新 AccessToken
    String newAccessToken = generateAccessToken(Long.valueOf(userId), "USER");

    return Result.ok(new TokenPair(newAccessToken, newRefreshToken));
}
```

### 3.4 退出登录 → 吊销 AccessToken

```java
@PostMapping("/api/auth/logout")
public Result logout(@RequestHeader("Authorization") String header) {
    String token = header.replace("Bearer ", "");

    // 把当前 AccessToken 加入 Redis 黑名单
    // TTL 与 Token 剩余有效期一致，到期自动清理
    long ttl = getRemainingExpiration(token);
    if (ttl > 0) {
        redisTemplate.opsForValue().set(
            "blacklist:" + token, "1",
            ttl, TimeUnit.MILLISECONDS
        );
    }

    SecurityContextHolder.clearContext();
    return Result.ok();
}
```

### 3.5 前端 Axios 拦截器

```typescript
// 响应拦截器
let isRefreshing = false
let pendingRequests: Array<() => void> = []

service.interceptors.response.use(
  response => response,
  async error => {
    const { config, response } = error
    const originalRequest = config

    // 只对 401 且未重试过的请求做续期
    if (response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // 已有续期请求在进行中 → 排队等待
        return new Promise(resolve => {
          pendingRequests.push(() => {
            originalRequest.headers.Authorization = `Bearer ${getAccessToken()}`
            resolve(service(originalRequest))
          })
        })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        const refreshToken = getRefreshToken()
        if (!refreshToken) throw new Error('无 RefreshToken')

        const { data } = await axios.post('/api/auth/refresh', { refreshToken })
        setAccessToken(data.data.accessToken)
        setRefreshToken(data.data.refreshToken)

        // 重发排队的请求
        pendingRequests.forEach(cb => cb())
        pendingRequests = []

        originalRequest.headers.Authorization = `Bearer ${data.data.accessToken}`
        return service(originalRequest)
      } catch {
        // 续期失败 → 跳转登录页
        clearTokens()
        window.location.href = '/login'
        return Promise.reject(error)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  }
)
```

---

## 四、为什么每个环节要这么设计

### 4.1 为什么 AccessToken 要短（30 分钟而不是几小时）

| 原因 | 说明 |
|------|------|
| 缩小泄露窗口 | AccessToken 每次请求都发送，最容易被截获。30 分钟 = 攻击者最多用 30 分钟 |
| 减少黑名单压力 | Token 过期后自动失效，不需要 Redis 黑名单一直存着 |
| 无状态优先 | 绝大部分请求只走 JWT 验签 + Redis 黑名单检查（set 操作毫秒级），不查 DB |

### 4.2 为什么 RefreshToken 要长（7 天而不是几小时）

| 原因 | 说明 |
|------|------|
| 用户体验 | 用户不希望每天都要重新登录 |
| 暴露面小 | RefreshToken 只在续期时传输一次，攻击者很难截获 |
| 可吊销 | 存 Redis，管理员可以随时删除改密/封号用户的 RT |

### 4.3 为什么 RefreshToken 存 Redis 而不是也做成 JWT

| 方案 | 能否吊销 | 能否绑定设备指纹 | 存储开销 |
|------|---------|----------------|---------|
| JWT 做 RT | ❌ 不能吊销 | ❌ Payload 固定 | 零 |
| 随机字符串 + Redis | ✅ 删除即吊销 | ✅ 随 Redis value 存储 | 每个用户存一条 |

**核心逻辑**：RefreshToken 的目的是"可控的长效凭证"，而不是"无状态的便捷凭证"。存 Redis 刚好满足可控需求。

### 4.4 为什么要做 RefreshToken Rotation

- 如果 RT 不变，攻击者偷到后可以一直续期，等于永久门票
- Rotation 让每个 RT **只能用一次**
- 检测冲突：如果服务端发现同一 RT 被用了两次，判定为被盗，**吊销该用户所有 Token**

### 4.5 为什么要做前端请求队列

续期期间可能有多个请求同时返回 401：
- 不加队列 → 每个请求都触发续期 → N 次并发续期请求 → Redis 压力 + 可能冲突
- 加队列 → 只续期一次，其他请求等新 Token 出来后重发

### 4.6 为什么要检查设备指纹

- 攻击者偷到 RT 后从不同 IP/设备续期 → 校验失败 → 拒绝续期
- 触发告警 → 通知用户密码可能被盗
- 这是一个**被动检测机制**，纯 JWT 做不到

---

## 五、安全威胁模型分析

| 攻击场景 | 纯 JWT | 双 Token + Rotation |
|---------|--------|-------------------|
| XSS 偷 localStorage 中的 AT | 攻击者可用到 AT 过期 | 同左，但 AT 30 分钟就过期 |
| XSS 偷到 AT + RT | 无 RT 概念 | 攻击者有 30 分钟竞争窗口；若用户先续期，RT 作废 |
| 中间人嗅探到 HTTP 请求 | 攻击者拿到 AT | 同左，但 AT 短有效 |
| 数据库泄露（密码被破解） | 立即修改密码，但已有 JWT 仍可用 | 清除 Redis 中 RT，所有登录态立即失效 |
| 员工离职/账号封禁 | 无法吊销已签发的 JWT | 删除 RT 即可踢下线 |
| RT 被盗+抢跑续期 | 无 RT 概念 | Rotation 冲突触发告警，吊销全部 Token |

---

## 六、配置参考

```yaml
# application.yml
jwt:
  secret: "your-256-bit-secret-key-here-must-be-long-enough-for-hs256"
  access-token-expiration: 1800000        # 30 分钟 (毫秒)
  refresh-token-expiration: 604800000     # 7 天 (毫秒)

redis:
  key-prefix:
    refresh: "refresh:"                   # RefreshToken 前缀
    blacklist: "blacklist:"               # 黑名单前缀
```

---

## 七、完整数据流总结

```
登录
  ├─ 生成 AT (JWT, 30min 有效)
  ├─ 生成 RT (UUID, 存 Redis, 7天有效)
  └─ 返回给前端

请求
  ├─ 携带 AT
  ├─ 查 Redis 黑名单
  ├─ JWT 验签
  └─ 放行到 Controller

续期
  ├─ AT 过期 → 前端返回 401
  ├─ 请求队列（防并发）
  ├─ 携带 RT 请求续期
  ├─ 校验 RT 是否存在
  ├─ 校验设备指纹
  ├─ 作废旧 RT
  ├─ 生成新 AT + 新 RT
  └─ 重发排队请求

退出/吊销
  ├─ 当前 AT 加入黑名单 (TTL=剩余有效期)
  ├─ 删除 Redis 中的 RT
  └─ 前端清空 Token
```

---

## 关联连接

- [[dual-token-mechanism]] — 双 Token 概念
- [[dual-token-security-analysis]] — 双 Token 安全设计分析
- [[token-blacklist]] — Token 黑名单机制
- [[jwt-stateless]] — JWT 无状态原理
- [[JWT]] — JWT 技术实体
- [[spring-security-jwt-redis-best-practice]] — Spring Security 集成实践
- [[摘要-token-redis-interview]] — 深度分析来源
- [[摘要-springboot4-security7-vue3-best-practice]] — 工程实践来源
- [[Redis]] — 存储层
- [[SpringSecurity]] — 安全框架
- [[SpringBoot]] — 后端框架
- [[Axios]] — 前端 HTTP 客户端
