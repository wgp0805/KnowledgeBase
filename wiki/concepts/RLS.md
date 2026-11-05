---
title: "RLS"
type: concept
tags: [概念, PostgreSQL, 多租户, 数据库, 安全]
sources: [raw/09-archive/推荐一个牛逼的SaaS智能客服系统.md]
last_updated: 2026-11-05
---

## 定义

RLS（Row-Level Security，行级安全）是 PostgreSQL 的原生安全机制：为表启用行级安全策略后，数据库会**按当前会话的上下文变量自动过滤行**，即使 SQL 忘记写 `WHERE tenant_code = ?`，也不会读到/改到其他租户的数据。它是多租户系统"数据库层强制隔离"的最后一道防线。

## 关键信息

### 启用步骤

```sql
-- 1. 对每张带 tenant_code 的表启用并强制 RLS
ALTER TABLE public.<table> ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.<table> FORCE ROW LEVEL SECURITY;

-- 2. 定义策略（示例：只允许访问当前租户的行）
CREATE POLICY tenant_isolation ON public.<table>
    USING (tenant_code = current_setting('app.tenant_code', true));

-- 3. 应用每次借出连接时写入租户上下文
SELECT set_config('app.tenant_code', '<current-tenant>', false);
```

- `ENABLE` 让策略生效；`FORCE` 让表 owner 也受策略约束（否则 owner 绕过）
- `set_config(..., false)` 表示会话级（非事务级）生效
- 应用层通过连接池的 beforeUse / 借出钩子自动注入，业务代码无感

### 在多租户架构中的位置

云梯智能客服系统的**四层防线**（详见 [[云梯智能客服系统]]、[[多租户隔离]]）：
1. 网关从 JWT 认租户（不信任前端请求头）
2. 应用层所有表带 `tenant_code`，唯一索引含租户
3. **PostgreSQL RLS（本页）**——数据库层兜底
4. 独立 Schema 模式（物理隔离）

第 3 层价值：**应用层代码漏写租户条件时，数据库仍然兜底**——把"依赖开发者自觉"变成"机制强制"。

### 边界与代价

- **不是所有库都开了 RLS**：云梯的 ai_db 未启用，Python 直连 customer_db 时也没有自动设置 RLS 上下文 → 只能算"应用层隔离 + 显式查询过滤"，不是与业务库同级的数据库强制隔离（要诚实表述）
- **性能**：策略谓词会参与查询，通常可走索引（`tenant_code` 建索引）
- **运维复杂度**：新增表必须记得 ENABLE/FORCE + 建策略，最好用迁移脚本自动化（云梯用"基线 + 增量脚本"管理）
- **与连接池配合**：必须保证每次借出连接都设置正确的租户上下文，否则会串租户

## 关联连接
- [[摘要-云梯saas智能客服]] — 来源
- [[云梯智能客服系统]] — 实践案例
- [[多租户隔离]] — 上位方法论（RLS 是第三道防线）
- [[PostgreSQL]] — 提供 RLS 能力的数据库
- [[ScopedValue]] — 应用层租户上下文传递
