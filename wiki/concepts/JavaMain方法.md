---
title: "JavaMain方法"
type: concept
tags: [概念, Java, 面试题, 基础]
sources:
  - raw/01-articles/阿里二面：main 方法可以继承吗？.md
last_updated: 2026-10-21
---

## 定义

Java `main` 方法作为**应用程序入口**的特殊性，以及它与普通静态方法的区别。面试常问三连：**能重载吗 / 能被其他方法调用吗 / 可以继承吗**——三个答案都是「可以」。

## 关键信息

### 格式定义逐项解释

```java
public static void main(String[] args) { }
```

| 修饰符 | 原因 |
|---|---|
| `public` | main 由 JVM 加载，可访问权限最高，所以需要声明为 public |
| `static` | 方法调用要么通过对象要么通过类；main 由虚拟机调用，无需生成对象，声明为 static 即可 |
| `main` | 名字参考 C 语言的方法名 |
| `void` | main 退出时并没有相关返回值需要返回 |
| `String[]` | 运行时接受用户输入的参数；字符串在 Java 中通用性最强；参数不止一个，所以用数组合适 |

> 自 **JDK 1.5 引入动态参数**后，`String[] args` 也可以写成 `String... args`：
> ```java
> public static void main(String... args) { }
> ```

**结论：除了 JVM 规定的作为应用程序入口的 main 方法比较特殊外，其他的 main 方法与普通的静态方法没有什么不同。**

### Q1：能重载吗 —— 可以
```java
public class Main {
    public static void main(String args) {
        System.out.println("hello world:" + args);
    }
    public static void main(String[] args) {
        main("test");
    }
}
```
编译运行没问题：除了 JVM 规定的入口 main，其他 main 都是比较普通的方法。

### Q2：能被其他方法调用吗 —— 可以
```java
public class Main {
    private static int times = 3;
    public static void main2(String[] args) { times--; main(args); }
    public static void main(String[] args) {
        System.out.println("main方法执行:" + times);
        if (times <= 0) { System.exit(0); }
        main2(args);
    }
}
```
输出依次为 `3 / 2 / 1 / 0`。**注意程序关闭方式，别陷入死循环。**

### Q3：可以继承吗 —— 可以
父类 `Main` 定义 `public static void main(String[] args)`，子类 `Main2 extends Main` 不定义 main，运行子类同样打印父类的 `hello world`——说明 main 方法是可以继承的。

子类自己定义 main 则**隐藏（override 静态方法）**父类实现：
```java
public class Main2 extends Main {
    public static void main(String[] args) {
        System.out.println("hello world Main2");
    }
}
```
打印 `hello world Main2`。

## 关联连接

- [[Java]] — 所属语言
- [[小哈]] — 本文作者
- [[摘要-java-main方法继承]] — 来源
