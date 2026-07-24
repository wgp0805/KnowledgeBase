---
title: "Maven 4 要来了：15 年后，Java 构建工具迎来“彻底重构”"
source: "https://mp.weixin.qq.com/s/gYseZJSE7UpzqIjPtgHKfw"
---
点击关注 👉 Java技术指北 *2026年7月24日 08:15*

自2010 年 Maven 3 发布以来，Maven 对 Java 构建生态的整体支持方式，几乎没有发生过颠覆性的变化。  
然而在这 15 年里，Java 世界早已天翻地覆：  
•模块化成为标配  
•并行构建成为刚需  
•云原生与容器化成为主流  
•JDK 以一年两个大版本的节奏持续快速演进  
  
相比之下，Maven 本身却显得有些“老态”。

Maven 4 的出现，正是为了解决这些长期积累的历史包袱。

虽然 Maven 4 仍未公布正式 GA 发布日期，但目前已经迭代到第五个发布候选版本（RC5），从项目成熟度和变更稳定性来看，距离正式发布已相当接近。

现在正是提前了解、评估和准备升级的合适时机。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

01

到 4.1.0

Maven 4 将 POM 的模型版本升级为4.1.0：

```
<project
    xmlns="
            http://maven.apache.org/POM/4.1.0"
          
    xmlns:xsi="
            http://www.w3.org/2001/XMLSchema-instance"
          
    xsi:schemaLocation="
            http://maven.apache.org/POM/4.1.0
          
                        
            http://maven.apache.org/xsd/maven-4.1.0.xsd"
          >
  <modelVersion>4.1.0</modelVersion>
</project>
```

- 向后兼容：Maven 4 仍然可以构建 4.0.0 的 POM
- 新能力只对 4.1.0 生效
- modelVersion理论上可以省略，Maven 会从 schema 推导

也就是说：

不升级 POM 也能用 Maven 4，但升级后才能真正“吃到红利”。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=3)

02

Build POM / Consumer POM 分离：终于解决“POM 污染”

这是 Maven 4最重要、也是最颠覆性的变化之一。

在 Maven 3 中，发布到仓库的 POM 同时包含：

- 插件配置
- 构建细节
- 父 POM 引用
- 各种属性

依赖使用者会被迫解析大量“与我无关”的信息。

Maven 4 的解决方法是POM 扁平化（Flattening）。

Maven 4 正式区分：

| 类型 | 用途 |
| --- | --- |
| Build POM | 项目自身构建 |
| Consumer POM | 提供给依赖方 |

Consumer POM 具备以下特征：

- 不包含插件配置
- 不包含父 POM
- 不包含未使用依赖
- 只保留真实传递依赖
- 属性已被解析为具体值

开启方式：

```
mvn clean install -
            Dmaven.consumer.pom.flatten=
          true
```

Maven 3 时代需要额外的 Flatten Maven Plugin，Maven 4 中已成为原生能力。

这一步，直接让依赖解析更快、更干净、更可预测。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=5)

03

新 Artifact Type：显式控制 classpath / module path

在 Maven 3 中：

- 普通 JAR → classpath
- 含 [module-info.class](http://module-info.class/) → module path（自动推断）

这种“隐式规则”在 Java 模块化时代并不够清晰。

Maven 4 新增类型：

```
<type>classpath-jar</type>
<type>module-jar</type>
```

开发者终于可以显式声明依赖放在哪里。

Maven 4 还新增了专门的注解处理器类型：

- processor
- classpath-processor
- modular-processor

以 Lombok 为例：

```
<dependencies>
  <dependency>
    <groupId>
            org.projectlombok
          </groupId>
    <artifactId>lombok</artifactId>
    <version>${
            lombok.version}
          </version>
    <type>classpath-processor</type>
</dependency>

<dependency>
    <groupId>
            org.projectlombok
          </groupId>
    <artifactId>lombok</artifactId>
    <version>${
            lombok.version}
          </version>
    <scope>provided</scope>
</dependency>
</dependencies>
```

Maven 4明确区分了 API classpath 与 processor classpath，构建语义更清晰，也更利于工具链优化。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=7)

04

“让路”

Java 9 引入模块系统后：

- Maven Modules
- Java Modules

长期让新手和工具“集体懵逼”。

Maven 4 的选择是：

- modules → subprojects
- modules 标记为 deprecated

```
<subprojects>
  <subproject>project-a</subproject>
  <subproject>project-b</subproject>
</subprojects>
```

同时还支持：

- Parent 推断：空\<parent />自动识别
- 子项目自动发现：无需显式声明
- 统一构建时间戳
- 安全发布：子项目失败 → 全部不发布

这是一次语义层面 + 工程实践层面的双重升级。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=9)

05

树形生命周期：并行构建终于“名正言顺”

Maven 3 的生命周期是线性的，即使多模块，也很难高效并行。

Maven 4 引入Tree-based Lifecycle：

- 每个子项目独立推进生命周期
- 依赖就绪即可启动
- 大型多模块构建速度显著提升

开启方式：

```
mvn -b concurrent verify
```

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=11)

06

配置能力显著增强的“小变化”

1\. 条件表达式 Profile

```
<condition>
  exists('${
            project.basedir}/src/**/*.xsd'
          )
  && length(${
            user.name}
          ) > 5
</condition>
```

不再只是 [os.name、jdk这种基础判断，而是真正的表达式系统。](http://os.xn--namejdk,-im3gq721asonx6tfvtbub4y3bow4bifcrwhqxipxrolj9ugo59c11yb6sa./)

2\. 统一的 Sources 模型

Maven 3：

```
<sourceDirectory>...</sourceDirectory>
<testSourceDirectory>...</testSourceDirectory>
```

Maven 4：

```
<sources>
  <source>
    <scope>main</scope>
    <directory>my-custom-dir/foo</directory>
  </source>
  <source>
    <scope>test</scope>
    <directory>my-custom-dir/bar</directory>
  </source>
</sources>
```

更适合：

- 多目录
- 多版本
- 模块化项目
- 无插件配置场景

Maven 4 还提供了官方升级工具：

```
mvnup check   # 只生成报告
mvnup apply   # 自动修改
```

它会分析：

- POM
- 插件
- 项目结构

并给出可执行的升级建议。

—END—

写在最后

2019年，因自己做副业走向创业以后，我应该是全网最早一批呼吁大家，一定要有第二职业的自媒体博主了。

因为我从上班的第一天起，人一定要把命运仅仅的握在自己手上，而不是依赖于外部的环境。

所以，我上班永远都是给自己干，拼命的干只是为了积累经验，从上班的第一天起我就没有停止过折腾。

大家见过的没见过的项目或者副业，我基本都干过还干的不错，包括什么炒域名、线下创业融资、给海外做支付等等。

失败过无数次，最终才走到今天。

但其实最重要的是走出的那第一步，在职场外赚到的第一元钱，会让你对这个世界有完全不一样的了解。

那就是世界很大一切皆有可能。

如果你对副业或者第二职业感兴趣，可以加我微信会自动给你发一份资料，也是我实践十几个项目后选到最佳的。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/kiaNs19uFIvwg7CNXEgic9K2APKKd836v4yKXmTdlmJYHicY2g9gNFNYDG5Ph9ngib5DibUVEBEfiaCY6lyZzwjIDQA8CUJOaYzSNqtT7x11n6Wics/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

**加上面微信，备注：微笑，发一份项目资料。**