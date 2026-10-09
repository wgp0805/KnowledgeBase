---
title: "State-CSRF防护"
type: concept
tags: [概念, OAuth2, CSRF, 安全, 第三方登录]
sources: [raw/01-articles/搞定 OAuth 2.0 第三方登录，So Easy !.md]
last_updated: 2026-09-16
---

## 定义
OAuth 2.0 授权流程中使用的 `state` 参数机制，用于防止 CSRF（跨站请求伪造）攻击。发起授权请求时生成随机 state 值，用户回调时校验 state 是否与发起时一致，防止恶意第三方伪造授权请求。

## 关键信息

### CSRF 攻击场景
如果没有 state 参数，攻击者可以构造恶意链接诱导用户点击，把用户跳到自己的服务器做"授权"，从而把自己的 account 与用户关联——OAuth 流程中的 CSRF 攻击。

### State 生成与校验流程
1. **发起授权时**：生成随机 state 字符串并保存（内存 Set 或 Redis）
2. **回调时**：校验 state 是否匹配，不匹配则中止流程
3. **校验后**：立即删除 state（防止重放攻击）

### Java 代码示例
```java
@Service
public class OauthService {
    private Set<String> stateSet = new HashSet<>();

    public String genState() {
        String state = UUID.randomUUID().toString();
        stateSet.add(state);
        return state;
    }

    public boolean checkState(String state) {
        if (stateSet.contains(state)) {
            stateSet.remove(state);
            return true;
        }
        return false;
    }
}
```

### 生产环境建议
- **短期**：state 存入内存 Set（如上文代码）
- **生产级**：state 存入 Redis，设置合理失效时间
- **重要**：state 参数**不能省略**，忽略该参数有可能导致 CSRF 攻击

### GitHub 与 QQ 的 state 参数
- **GitHub**：state 参数为可选，但官方强烈建议生成
- **QQ**：state 参数为可选，同样强烈建议生成

## 关联连接
- [[OAuth2]] — 核心协议
- [[GitHub]] — 实战示例
- [[QQ互联]] — 实战示例
- CSRF — 关联的 Web 安全攻击
- [[摘要-oauth2-第三方登录]] — 来源