---
title: "javabean-boolean-is-pitfall"
type: concept
tags: [Java, JavaBean, 序列化, 面试题, 避坑]
sources: [raw/01-articles/Java 布尔属性 is 命名序列化大坑｜阿里面试真题文档.md]
last_updated: 2026-08-04
---

## 定义
JavaBean 布尔属性 is 命名陷阱：当 POJO 布尔类型属性直接命名为 `isXxx` 时，触发 JavaBean 规范的 getter/setter 生成错位，导致序列化后 JSON 字段名丢失 `is` 前缀，并引发 ORM 映射异常与 RPC 传输字段丢失。

## 关键信息

### 矛盾根源
- **DBA 规范**：数据库布尔字段建议带 `is_` 前缀（如 `is_deleted`），一眼识别布尔标识
- **JavaBean 规范**：IDE 生成 getter/setter 时，`isXxx` 命名会触发名称错位

### getter 生成规则
| 属性写法 | 生成 getter | 生成 setter |
|---|---|---|
| `boolean isDeleted`（基础类型） | `isDeleted()` | `setDeleted()` |
| `Boolean isDeleted`（包装类型） | `getDeleted()` | `setDeleted()` |

### 三大灾难
1. **序列化错乱**（[[Jackson]]/[[FastJson]] 最常见）：框架通过反射 getter 识别字段名，`isDeleted()` -> 字段名 `deleted`，JSON 输出 `{"deleted":true}` 丢失 `is` 前缀，前后端联调翻车
2. **[[MyBatis]] ORM 映射异常**：驼峰自动转换 `is_deleted -> isDeleted`，但反射调用 `setDeleted()`，字段映射失败，布尔值恒为 null/false
3. **[[Dubbo]]/RPC 序列化问题**：跨服务传输依赖 JavaBean 规范，属性名与 getter 不匹配致字段丢失、反序列化失败

### 标准解决方案
数据库保持 `is_deleted`，**Java 实体属性命名为 `deleted`**（不带 is 前缀），靠 MyBatis 驼峰自动映射：
- `private Boolean deleted;` -> getter `getDeleted()` -> JSON `{"deleted":true}`

若对外接口必须返回 `isDeleted`，用 [[Jackson]] 注解显式指定：
```java
@JsonProperty("isDeleted")
private Boolean deleted;
```

### 常见误区
- ❌ 只有 boolean 基础类型才有问题 -> 全都有问题，只是 getter 名不同
- ❌ 改 setter/getter 名能根治 -> 破坏 JavaBean 标准，部分 ORM/RPC 仍异常
- ❌ 不做前后端交互就无所谓 -> MyBatis、Dubbo 等所有依赖 JavaBean 反射的组件都受影响

## 关联连接
- [[摘要-java-boolean-is-naming-pitfall]] - 来源
- [[Jackson]] - JSON 序列化框架，陷阱主要发生地
- [[FastJson]] - 阿里 JSON 库，同类陷阱
- [[MyBatis]] - ORM 框架，映射异常
- [[Dubbo]] - RPC 框架，传输字段丢失
- [[Java]] - 所属语言
- [[api-compatibility]] - API 兼容性设计关联
