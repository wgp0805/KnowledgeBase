---
title: "摘要-try-catch-异常边界"
type: source
tags: [来源, 原始文件, Java, 异常处理, Spring事务]
sources: [raw/01-articles/谁再说 try catch 必须放 for 循环外面，直接走人！.md]
last_updated: 2026-07-01
---

## 核心摘要
胖虎《谁再说 try catch 必须放 for 循环外面，直接走人！》指出 `try catch` 放 `for` 里还是外，本质不是性能问题，而是**异常边界**问题——即"某条数据失败后，后面还要不要继续跑"。放外面表达"整批是一个整体，一条失败整批停"（如订单状态迁移、批量转账等强一致场景）；放里面表达"每条独立，单条失败记录原因后继续"（如批量导入、批量发消息等场景）。文章还深入三个易踩的坑：`@Transactional` 内 catch 不抛导致事务被错误提交；大事务里循环 catch 无法实现单条独立提交（需 `REQUIRES_NEW` 拆事务，且要避免自调用导致代理失效）；把异常当 `if else` 用（如用 `parseInt` 抛异常判断数字）才是真正的性能杀手。最后强调 catch 不是垃圾桶，能处理才 catch，且子类异常要放父类前面。

## 关联连接
- [[异常边界]] — 本文提炼的核心概念
- [[transaction-management]] — 事务回滚规则、REQUIRES_NEW、自调用失效
- [[Spring]] — @Transactional 与 AOP 代理机制
- [[AOP]] — 事务生效依赖代理，自调用绕过代理
- [[Java]] — 异常表、异常对象栈填充成本
- [[胖虎]] — 原文作者
