---
title: "ScopedValue"
type: concept
tags: [概念, Java, Java25, 并发, 上下文传递]
sources: [raw/09-archive/推荐一个牛逼的SaaS智能客服系统.md]
last_updated: 2026-11-05
---

## 定义

ScopedValue 是 Java 25 引入的作用域值 API（JEP 506 正式转正），用于在线程内传递不可变的上下文数据（如登录态、租户、TraceId），是 `ThreadLocal` 的现代替代方案。核心思想：**值只在明确的作用域内可见，作用域结束自动失效**，无需手动 `remove()`。

## 关键信息

### 基本用法

```java
ScopedValue.Carrier carrier = ScopedValue.where(CURRENT, state);
if (tenant != null && !tenant.isBlank()) {
    carrier = carrier.where(TenantContext.CURRENT, tenant);
}
return carrier.call(action);   // 在绑定作用域内执行 action
```

- `ScopedValue.where(key, value)` 创建绑定，`carrier.call(...)` 在该作用域内执行逻辑
- 支持多值绑定（登录态 + 租户 + TraceId 层层 where）
- 作用域结束后绑定自动失效，**无需 try/finally 手工清理**

### 相比 ThreadLocal 的优势

| 维度 | ThreadLocal | ScopedValue |
|------|-------------|-------------|
| 生命周期 | 线程级，需手动 remove | 作用域级，自动失效 |
| 线程池复用风险 | 忘记 remove 会串用户数据/内存泄漏 | 作用域结束即失效，天然不串 |
| 可变性 | 可 set/get 修改 | 绑定后不可变（更安全） |
| 虚拟线程友好 | 大量虚拟线程下 ThreadLocal 内存开销大 | 专为虚拟线程设计，开销低 |
| 传递模型 | 隐式可变状态 | 显式作用域绑定 |

### 典型应用：多租户请求上下文

云梯智能客服系统（详见 [[云梯智能客服系统]]）用 ScopedValue 管理登录态与租户：

```java
public static <R, X extends Throwable> R bind(
        AuthState state,
        CallableOp<? extends R, X> action) throws X {
    ScopedValue.Carrier carrier = ScopedValue.where(CURRENT, state);
    String tenant = state.user() == null ? null : state.user().tenantCode();
    if (tenant != null && !tenant.isBlank()) {
        carrier = carrier.where(TenantContext.CURRENT, tenant);
    }
    return carrier.call(action);
}
```

**解决的真实问题**：线程池复用 + 手写 `ThreadLocal.remove()` 容易遗漏，导致 A 用户请求结束后 B 用户请求复用了同一线程却读到 A 的租户/登录态——"串租户"。ScopedValue 让作用域结束自动失效，从机制上杜绝这类事故（关联 [[多租户隔离]]）。

## 关联连接
- [[摘要-云梯saas智能客服]] — 来源
- [[云梯智能客服系统]] — 实践案例
- [[ThreadLocal]] — 被替代的方案（有内存泄漏与线程池串数据风险）
- [[多租户隔离]] — 上下文隔离的应用场景
- [[虚拟线程]] — ScopedValue 与之配套（低开销上下文）
