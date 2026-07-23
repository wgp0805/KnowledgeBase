---
title: "蚂蚁又开源了一个顶级Java项目！"
source: "https://mp.weixin.qq.com/s/h1oWHcawrj3ApX4l9XxaOQ"
---
我是程序汪 *2026年7月23日 10:24*

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/17f46ec5ecc383053097d9d62b76db55_MD5.webp)

来源：JavaGuide

**目录**

- Jeandle 介绍
- 什么是 JIT 编译器
	- 什么是 LLVM
- 未来规划
- 项目地址

---

就在前几天，Java 领域又一重磅级开源项目诞生。 **蚂蚁集团正式开源了基于 LLVM 的全新 JVM JIT 编译器 —— Jeandle。** 项目以"筋斗云"（Jeandle）为名，寓意深远。它希望为 JVM 插上翅膀，让 Java 应用能如孙悟空驾驭筋斗云一般，突破性能边界，瞬息万里。

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/f907d26d204418c711dd86e78d87d77a_MD5.webp)

Jeandle 项目

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/ed8c35498ff25f3ed660e429b7f3a379_MD5.webp)

Jeandle 介绍

## Jeandle 介绍

简单来说，Jeandle 是基于 OpenJDK Hotspot JVM 的全新 Just-In-Time（简称 JIT，即时）编译器，利用 LLVM 进行编译优化与代码生成， **将 LLVM 的性能优势和生态优势引入 JVM 中** 。

下面是维基百科对即时编译的介绍：

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/065352b530855a936356da291a679fee_MD5.jpg)

即时编译介绍

要理解 Jeandle 的颠覆性，我们得先快速了解两个核心概念：JIT 和 LLVM。

### 什么是 JIT 编译器

Java 能够实现"一次编译，到处运行"靠的就是"解释器"。无论 Java 程序运行在什么 CPU 上，都通过一个跨平台的解释器不断地读取 Java 代码，并代替它执行。

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/cb612765690cdda83a6efe637f4df132_MD5.jpg)

解释器工作原理

但是解释器终究是低效的，好比在翻译英文时，机械地查找每个单词的含义然后组装起来，这样的翻译结果不仅冗长，还让人难以理解；而经验丰富的译员会读取整段英文，对这段文字进行分析，结合上下文精确地理解每个单词，去除冗余句子，并通过重排词句顺序、精简句子结构来使结果更易懂。

JIT 编译器如同经验丰富的译员，当 JVM 中的解释器发现一段代码的执行频率很高时，就会使用 JIT 编译器对这段代码进行编译，通过对这段代码的深入分析与优化，产出一系列高效的指令以提高它的运行效率。

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/6be5dbc4bc6ecfc57e7ec91ccb916970_MD5.jpg)

JIT 编译器工作原理

### 什么是 LLVM

LLVM 是目前最受欢迎的开源编译器基础设施，它拥有模块化的设计、优秀的编译优化能力与完备的后端支持。我们可以将其视为一套现成的超级零件箱，用它快速地拼出一个新编译器：

1. 编写语言前端：将编程语言代码转换成 LLVM IR（Intermediate Representation）
2. 利用 LLVM 的优化器，对 LLVM IR 进行分析与优化
3. 通过 LLVM 的代码生成器，从 LLVM IR 生成真正的 CPU 指令，使程序最终可以运行
![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/b9004a502d5329d160e68bee2f55e9cc_MD5.jpg)

LLVM 编译流程

除此之外，LLVM 的优势还体现在以下方面：

- **极致的性能优化：** 拥有业界顶尖的代码分析和优化能力。
- **高度模块化：** 按需取用，灵活扩展，是现代编程语言（如 Rust、Swift）的首选。
- **繁荣的开源生态：** 全球顶尖公司、研究机构和开发者共同维护，技术始终保持前沿，尤其在 AI 领域展现出巨大潜力。

目前已经有大量基于 LLVM 的编译器实践。同时，LLVM 在 AI 领域和许多新编程语言的应用也展现出持久的生态活力。

Jeandle 诞生的愿景是想把 LLVM 的优点引入 JVM 中，让 JVM "坐上筋斗云"。 **JDK 和 LLVM 各自丰富的生态也为 Jeandle 带来了更多想象空间。**

![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/38f1166c53318cc508d370b13884642d_MD5.jpg)

Jeandle 愿景

## 未来规划

将 JVM 和 LLVM 这两大复杂的系统优雅地结合，是一项巨大的挑战，Jeandle 团队需要攻克诸多技术难题，例如：

- 完美支持 JVM 的垃圾回收（GC）机制。
- 为 Java 的动态特性（如 synchronized）定制 LLVM 功能。
- 基于 LLVM 实现一套专为 Java 优化的算法。
- ...
![图片](assets/%E8%9A%82%E8%9A%81%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E4%B8%AA%E9%A1%B6%E7%BA%A7Java%E9%A1%B9%E7%9B%AE%EF%BC%81/4249693ef63cd8ea90a62d82abc3d86e_MD5.jpg)

未来规划

目前，Jeandle 尚处在开源初期，但路线图已经非常清晰：

- **2025 年底：实现全量 Bytecode 支持** ：完成对 Exception、GC、Synchronization 等所有基础功能的支持，实现对 Java 字节码的全面覆盖。
- **2026 年：聚焦性能优化的"黑科技"**
- **推出 Java 定制优化套件：** 研发一系列针对 Java 语言特性的高级优化算法，如锁优化、逃逸分析、高级内联（Inlining）等。
	- **引入 Intrinsic：** 为特定场景和常用库函数定制手写的高效汇编代码，压榨极致性能。
	- **支持 On-Stack Replacement (OSR)：** 实现运行中代码的动态热替换。
	- **支持 G1 GC：** 兼容并支持现代主流的 G1 垃圾回收器。