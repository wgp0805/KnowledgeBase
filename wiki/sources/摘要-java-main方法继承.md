---
title: "摘要-java-main方法继承"
type: source
tags: [来源, Java, 面试题, main方法]
sources: [raw/09-archive/阿里二面：main 方法可以继承吗？.md]
last_updated: 2026-10-21
---

## 核心摘要

小哈（犬小哈）以「阿里二面：main 方法可以继承吗」为题，梳理 `main` 方法的三个经典追问：**能重载吗、能被其他方法调用吗、可以继承吗**。

**格式定义**：`public static void main(String[] args)`。`public`——main 由 JVM 加载，可访问权限最高；`static`——方法调用要么通过对象要么通过类，main 由虚拟机调用无需生成对象；`main`——名字参考 C 语言；`void`——退出时无返回值需要返回；`String[]`——运行时接收用户输入参数，字符串通用性最强，数组是因为参数不止一个。自 JDK 1.5 引入动态参数后，`String[] args` 也可以写成 `String... args`。**除 JVM 规定的入口 main 之外，其他 main 方法与普通静态方法没有区别。**

**能重载**——可以。示例中重载 `main(String args)`，在 `main(String[])` 里调用 `main("test")`，编译运行无问题。

**能被其他方法调用**——可以。示例用 `main2` 递归调用 `main`，配合 `times` 计数器与 `System.exit(0)` 退出，输出依次为 3、2、1、0。注意点是控制程序关闭方式，别陷入死循环。

**可以继承**——可以。父类 `Main` 定义 `public static void main(String[] args)`，子类 `Main2 extends Main` 不定义 main，直接运行子类同样打印父类的 `hello world`，说明 main 方法是可以继承的；子类自己定义 main 则**隐藏**（override 静态方法）父类实现，打印 `hello world Main2`。

结论：除了 main 作为应用程序入口比较特殊外，其他情况下与正常的静态方法没什么区别。

## 关联连接

- [[JavaMain方法]] — 提炼概念：格式/重载/调用/继承三问
- [[Java]] — 所属语言
- [[小哈]] — 本文作者
- [[摘要-java-main方法继承]] — 本页来源
