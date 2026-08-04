视频链接：[https://v.douyin.com/Kz2VaZWY3F0/](https://link.wtturl.cn/?target=https%3A%2F%2Fv.douyin.com%2FKz2VaZWY3F0%2F&scene=im&aid=497858&lang=zh "autolink")

主题：阿里二面真题：布尔变量，DBA 要求数据库字段带`is`，POJO 属性写`isXXX`，面试直接挂掉，根源是 Java 序列化机制陷阱

## 一、现象：前后两套标准互相冲突

1. **DBA 规范（数据库层面）**
    
    布尔类型字段，命名建议带上 `is_`
    
    示例：`is_deleted`、`is_enable`
    
    逻辑：一眼识别是布尔标识，数据库设计通用规范。
    
2. **程序员下意识做法**
    
    数据库：`is_deleted tinyint(1)`
    
    实体类直接映射：
    

java

运行

```
private Boolean isDeleted;
// 或者基础类型
private boolean isDeleted;
```

**这行代码就是面试扣分核心！**

> 矛盾点：数据库规范要 is，但是 Java 实体布尔属性直接 isXXX 命名，触发 Java Bean 规范 + 序列化致命 bug。

## 二、底层原理：JavaBean 规范 & getter 方法生成规则

IDE 自动生成 getter/setter 规则：

### 情况 1：基础类型 boolean（原始类型）

java

运行

```
private boolean isDeleted;
```

IDE 生成：

java

运行

```
public boolean isDeleted() {
    return isDeleted;
}
// 没有 getDeleted()
public void setDeleted(boolean deleted) {
    isDeleted = deleted;
}
```

✅ getter：`isDeleted()`

✅ setter：`setDeleted()`

### 情况 2：包装类型 Boolean

java

运行

```
private Boolean isDeleted;
```

IDE 生成：

java

运行

```
public Boolean getDeleted() {
    return isDeleted;
}
public void setDeleted(Boolean deleted) {
    isDeleted = deleted;
}
```

✅ getter：`getDeleted()`

❌ **不存在 isDeleted ()**

## 三、三大线上 & 序列化灾难（面试重点）

### 坑 1：序列化 / 反序列化错乱（Jackson、FastJSON 最常见）

序列化框架依靠反射寻找 getter/setter 实现字段映射。

场景：

java

运行

```
private boolean isDeleted;
// getter: isDeleted()
// setter: setDeleted()
```

序列化时：

框架通过 `isDeleted()` → 识别字段名 **deleted**

最终 JSON 输出：

json

```
{"deleted":true}
```

**期望 JSON：{"isDeleted":true}，实际字段名丢失前缀 is！**

前后端联调直接翻车：前端传 `isDeleted`，后端接收不到值。

### 坑 2：MyBatis ORM 映射异常

数据库字段：`is_deleted`

实体属性：`isDeleted`

MyBatis 开启驼峰自动转换：`is_deleted → isDeleted`

但是！反射调用 setter 方法是 `setDeleted()`

Mybatis 字段映射匹配失败，出现**查出来数据布尔值一直为 null/false，无法赋值**。

### 坑 3：Dubbo、RPC、Java 原生序列化问题

RPC 通信依赖 JavaBean 规范，属性名称和 getter 不匹配，跨服务传输时字段丢失、反序列化失败。

## 四、重点区分：boolean 与 Boolean 两种写法不同陷阱

1. `private boolean isDeleted`（基本类型）
    
    getter：`isDeleted()`
    
    序列化 JSON key = `deleted`
    
2. `private Boolean isDeleted`（包装类型）
    
    getter：`getDeleted()`
    
    序列化 JSON key = `deleted`
    

👉 **结论：不管是基础类型还是包装类型，属性名直接写 isXXX 都会导致序列化后字段丢失 is 前缀！**

## 五、解决方案【标准工程写法，面试标准答案】

### 正确方案（兼顾 DBA 数据库规范 + Java Bean 规范）

数据库字段保持：`is_deleted`（遵循 DBA 规范不动）

**Java 实体类属性不要命名 isDeleted！**

推荐命名：

java

运行

```
// 正确写法
private Boolean deleted;
// 或者
private boolean deleted;
```

IDE 自动生成：

java

运行

```
public Boolean getDeleted(){}
public void setDeleted(Boolean deleted){}
```

映射关系：

数据库 `is_deleted`（下划线）→ 实体 `deleted`（驼峰）

Mybatis 驼峰转换自动匹配，序列化 JSON 输出：

json

```
{"deleted": true}
```

#### 如果业务强制要求 JSON 对外必须返回 `isDeleted`

两种兼容方案：

方案 1：Jackson 注解指定别名（最常用）

java

运行

```
@JsonProperty("isDeleted")
private Boolean deleted;
```

方案 2：不修改属性名，手动手写 getter，**不推荐维护成本高**

## 六、面试标准回答话术（可直接背诵）

> DBA 要求数据库布尔字段使用 is_前缀如 is_deleted，这是数据库设计规范。
> 
> 但 Java POJO 中不能直接定义 `Boolean isDeleted`。
> 
> 依据 JavaBean 规范，IDE 生成 getter/setter 会造成名称错位。序列化框架（Jackson/FastJSON）会将序列化后的字段解析为 deleted，丢失 is 前缀；同时会引发 MyBatis 字段映射异常、RPC 序列化传输字段丢失问题。
> 
> 最佳实践：实体属性命名为 deleted，数据库保留 is_deleted，依靠 MyBatis 驼峰命名自动映射；若对外接口必须返回 isDeleted 字段，使用 @JsonProperty 注解显式指定 JSON 名称。

## 七、常见误区避坑

1. ❌ 误区：只有 boolean 基础类型才有问题，Boolean 包装类没事
    
    → 全都有问题，只是生成 getter 名字不一样，最终都会丢失 is 前缀
2. ❌ 误区：改一下 setter/getter 名字就能根治
    
    → 手动修改 getter 破坏 JavaBean 标准，部分 ORM、RPC 框架依然兼容异常
3. ❌ 误区：只是 JSON 问题，不做前后端交互就无所谓
    
    → MyBatis、Dubbo 等所有依赖 JavaBean 反射的组件都会受影响

## 八、总结对照表

表格

|写法|属性|getter|序列化 JSON 字段|是否推荐|
|---|---|---|---|---|
|错误|`boolean isDeleted`|`isDeleted()`|deleted|❌禁止|
|错误|`Boolean isDeleted`|`getDeleted()`|deleted|❌禁止|
|标准|`Boolean deleted`|`getDeleted()`|deleted|✅推荐|

如果你需要，我可以额外输出一份**可直接放进简历 / 面试笔记的精简一页速记版**。