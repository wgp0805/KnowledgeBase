---
title: "generics"
type: concept
tags: [Java, 类型安全, 编程基础]
sources: [raw/01-articles/图文详解Java泛型，写得太好了！.md]
last_updated: 2026-05-20
---

## 定义

泛型（Generics）是一种可以接收数据类型的数据类型，是 Java 5 引入的特性。它允许在定义类、接口和方法时使用类型参数，实现代码的类型安全和复用。

## 核心原理

### 使用泛型的好处

1. **提升健壮性**：编译时检查类型，防止类型不匹配
2. **提高安全性**：添加元素时进行类型约束
3. **减少类型转换**：避免运行时 ClassCastException
4. **代码复用**：同一套代码适用于多种类型

### 泛型定义

```java
// 泛型类
class Person<E> {
    E s;  // 属性类型
    public Person(E s) { this.s = s; }  // 参数类型
    public E f() { return s; }  // 返回类型
}

// 使用时指定具体类型
Person<String> p1 = new Person<>("hello");
Person<Integer> p2 = new Person<>(123);
```

### 泛型接口

```java
interface Im<U, R> {
    void hi(R r);
    void hello(R r1, R r2, U u1, U u2);
    default R method(U u) { return null; }
}
```

### 泛型方法

```java
class U<X, Y, Z> {
    // 使用类声明的泛型
    public void hi(X x, Y y) {}
    
    // 自定义泛型方法（独立于类的泛型）
    public <T, S> void m1(T t, S s) {}
}
```

### 注意事项

- **泛型数组不能初始化**：`A[] a = new A[];` 是错误的
- **静态方法不能使用类定义的泛型**：因为静态成员与类相关，在类加载时对象还未创建
- **类型参数约定**：T（Type）、E（Element）、K（Key）、V（Value）、N（Number）

## 关联连接
- [[Java]] — Java 编程语言
- [[摘要-java-generics-explained]] — 来源
- Java Collections — 集合框架中的泛型应用
