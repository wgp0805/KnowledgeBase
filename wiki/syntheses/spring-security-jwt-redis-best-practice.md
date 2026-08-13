---
title: "spring-security-jwt-redis-best-practice"
type: synthesis
tags: [SpringSecurity, JWT, Redis, 认证, 最佳实践]
sources:
  - raw/09-archive/SpringBoot 4 + Spring Security 7 + Vue3 前后端分离项目设计最佳实践.md
  - raw/09-archive/面试中被嘲笑Token放在Redis里？这把给我干沉默了.md
  - raw/09-archive/SpringSecurity.md
  - raw/09-archive/SpringBoot整合SpringSecurity及框架的简单使用.md
last_updated: 2026-06-08
---

# Spring Security + JWT + Redis 最佳实践

## 架构总览

```
用户 → Nginx → JwtAuthFilter → SecurityFilterChain → Controller
                    ↓               ↑
                验签+黑名单        STATELESS
                    ↓
                Redis(黑名单) + JWT(无状态)
```

## 一、依赖配置 (Spring Boot 4 + Security 7)

```gradle
implementation 'org.springframework.boot:spring-boot-starter-security'
implementation 'org.springframework.boot:spring-boot-starter-data-redis'
implementation 'io.jsonwebtoken:jjwt-api:0.12.3'
runtimeOnly 'io.jsonwebtoken:jjwt-impl:0.12.3'
runtimeOnly 'io.jsonwebtoken:jjwt-jackson:0.12.3'
```

## 二、SecurityConfig (核心配置)

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {

    private final JwtAuthFilter jwtAuthFilter;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .sessionManagement(sm -> sm.sessionCreationPolicy(STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/login", "/api/auth/refresh").permitAll()
                .anyRequest().authenticated()
            )
            .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }
}
```

## 三、JWT 工具类

```java
@Component
public class JwtUtil {
    @Value("${jwt.secret}")
    private String secret;
    @Value("${jwt.access-token-expiration}")
    private long accessExpiration;

    public String generateAccessToken(Long userId, String role) {
        return Jwts.builder()
            .claim("userId", userId)
            .claim("role", role)
            .issuedAt(new Date())
            .expiration(new Date(System.currentTimeMillis() + accessExpiration))
            .signWith(getSigningKey())
            .compact();
    }

    public Claims parseToken(String token) {
        return Jwts.parser()
            .verifyWith(getSigningKey())
            .build()
            .parseSignedClaims(token)
            .getPayload();
    }

    private SecretKey getSigningKey() {
        return Keys.hmacShaKeyFor(secret.getBytes());
    }
}
```

## 四、JWT 认证过滤器 + Redis 黑名单

```java
@Component
public class JwtAuthFilter extends OncePerRequestFilter {

    private final JwtUtil jwtUtil;
    private final StringRedisTemplate redisTemplate;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain chain) {
        String token = extractToken(request);
        if (token == null) {
            chain.doFilter(request, response);
            return;
        }

        // 1. 查 Redis 黑名单
        if (Boolean.TRUE.equals(redisTemplate.hasKey("blacklist:" + token))) {
            throw new TokenInvalidException("Token已失效");
        }

        // 2. 验签
        Claims claims = jwtUtil.parseToken(token);

        // 3. 构造 Authentication
        UsernamePasswordAuthenticationToken auth =
            new UsernamePasswordAuthenticationToken(
                claims.get("userId"), null,
                List.of(new SimpleGrantedAuthority("ROLE_" + claims.get("role")))
            );
        SecurityContextHolder.getContext().setAuthentication(auth);
        chain.doFilter(request, response);
    }
}
```

## 五、双 Token 续期

```java
@RestController
public class AuthController {

    @PostMapping("/api/auth/login")
    public Result login(@Valid @RequestBody LoginReq req) {
        String accessToken = jwtUtil.generateAccessToken(user.getId(), user.getRole());
        String refreshToken = jwtUtil.generateRefreshToken(user.getId());

        redisTemplate.opsForValue().set(
            "refresh:" + refreshToken, user.getId().toString(),
            7, TimeUnit.DAYS
        );
        return Result.ok(new TokenPair(accessToken, refreshToken));
    }

    @PostMapping("/api/auth/refresh")
    public Result refresh(@RequestBody RefreshReq req) {
        String uid = redisTemplate.opsForValue().get("refresh:" + req.refreshToken());
        if (uid == null) return Result.fail(401, "RefreshToken已失效");
        String newAccess = jwtUtil.generateAccessToken(Long.valueOf(uid), "USER");
        return Result.ok(new TokenPair(newAccess, req.refreshToken()));
    }

    @PostMapping("/api/auth/logout")
    public Result logout(@RequestHeader("Authorization") String header) {
        String token = header.replace("Bearer ", "");
        long ttl = jwtUtil.getExpiration(token) - System.currentTimeMillis();
        if (ttl > 0) {
            redisTemplate.opsForValue().set(
                "blacklist:" + token, "1", ttl, TimeUnit.MILLISECONDS
            );
        }
        SecurityContextHolder.clearContext();
        return Result.ok();
    }
}
```

## 六、关键设计决策

| 决策 | 方案 | 原因 |
|------|------|------|
| Session 策略 | STATELESS | 前后端分离不用 Session |
| CSRF | 关闭 | JWT 天然防 CSRF |
| Token 存储 | 黑名单模式 | 只存失效 Token，比白名单省存储 |
| AccessToken 有效期 | 30 分钟 | 短时效降低泄露风险 |
| RefreshToken 有效期 | 7 天 | 长时效减少登录频率 |
| RefreshToken 存 Redis | 支持吊销 | 改密码/封号时立即失效 |
| 密码编码 | BCrypt | Spring Security 默认推荐 |

## 关联连接
- [[SpringSecurity]] — 安全框架
- [[JWT]] — 认证方案
- [[jwt-stateless]] — JWT 无状态原理
- [[token-blacklist]] — Token 黑名单机制
- [[dual-token-mechanism]] — 双 Token 续期方案
- [[摘要-springboot4-security7-vue3-best-practice]] — 工程实践来源
- [[摘要-token-redis-interview]] — JWT+Redis 深度分析
- [[SpringBoot]] — 后端框架
- [[Redis]] — 黑名单存储
- [[frontend-backend-separation]] — 前后端分离架构
- [[rbac]] — 权限模型
- [[cors]] — 跨域处理
