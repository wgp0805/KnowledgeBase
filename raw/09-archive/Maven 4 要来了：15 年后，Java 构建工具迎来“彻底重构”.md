---
title: "Maven 4 要来了：15 年后，Java 构建工具迎来“彻底重构”"
source: "https://mp.weixin.qq.com/s/sq4LWmo7Bmnkg_6R6Acc2Q"
---
小锋 java1234 *2026年7月7日 09:06*

大家好，我是锋哥。

> Maven作为基于POM（项目对象模型）强大的Java项目自动化构建工具，历经15年，当前最新版本：Apache Maven 4.0.0-rc-5（候选发布版），正式GA版本也快了。

![图片](assets/Maven%204%20%E8%A6%81%E6%9D%A5%E4%BA%86%EF%BC%9A15%20%E5%B9%B4%E5%90%8E%EF%BC%8CJava%20%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7%E8%BF%8E%E6%9D%A5%E2%80%9C%E5%BD%BB%E5%BA%95%E9%87%8D%E6%9E%84%E2%80%9D/d62c1d517e75f68e877a2d9317d7d7e0_MD5.webp)

---

## 目录

- 一、为什么 Maven 4 等了这么久？
- 二、Maven 4 现在走到哪一步了？
- 三、核心变化：Build POM 与 Consumer POM 分离
- 四、POM 4.1.0：少写重复配置
- 五、新工具与日常体验升级
- 六、从 Maven 3 迁移，可以怎么做？

---

## 一、为什么 Maven 4 等了这么久？

如果你用 Java 做项目，Maven 大概率不陌生。

2004 年 Maven 2 发布，2010 年 Maven 3 上线——之后十多年，社区一直在 [3.x](http://3.x/) 小版本上迭代。不是团队偷懒，而是 **POM 文件背负了太多东西** ：既要描述"怎么构建"，又要告诉下游"怎么依赖我"。

一旦改 POM 格式，Maven Central、IDE、Gradle 互操作、各类插件都要跟着动。于是 POM 4.0.0 的语法几乎被"冻住"了，很多 2005 年就提过的改进（比如自动推断父 POM 版本）一直拖到现在。

Maven 4 的思路很直白： **把"构建用的 POM"和"给别人用的 POM"分开** 。构建时可以大胆进化，发布到仓库时仍保持兼容。这才是标题里"彻底重构"的真正含义——不是换皮，而是把底层架构理顺了。

---

## 二、Maven 4 现在走到哪一步了？

截至 2026 年 7 月，Maven 4 已发布多个 RC（Release Candidate）版本，最新为 **4.0.0-rc-5** （2025-11-13）。官方仍标注为测试用途，生产环境建议等 GA 正式版。

几个硬性变化需要提前知道：

| 项目 | Maven [3.x](http://3.x/) | Maven 4 |
| --- | --- | --- |
| 运行 Maven 本身 | Java 8+ | **Java 17+** |
| 编译项目代码 | 自行配置 | 仍可编译 Java 8/11/17 等 |
| POM 模型 | 4.0.0 | 构建可用 **4.1.0** |
| 依赖解析 | Resolver [1.x](http://1.x/) | **Resolver 2.0** |

> 注意：Java 17 只是运行 Maven 的要求，不代表你的项目必须升到 Java 17。老项目照样可以用 Toolchains 指定编译 JDK。

![图片](assets/Maven%204%20%E8%A6%81%E6%9D%A5%E4%BA%86%EF%BC%9A15%20%E5%B9%B4%E5%90%8E%EF%BC%8CJava%20%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7%E8%BF%8E%E6%9D%A5%E2%80%9C%E5%BD%BB%E5%BA%95%E9%87%8D%E6%9E%84%E2%80%9D/efac66f2f7e557a63ccbe36196292f3b_MD5.jpg)

---

## 三、核心变化：Build POM 与 Consumer POM 分离

这是 Maven 4 最重要的架构调整。

- **Build POM** ：存在 Git 仓库里，包含插件配置、属性、父 POM 引用等完整信息。
- **Consumer POM** ：发布到 Maven Central 的精简版，只保留下游真正需要的依赖信息。

构建完成后，Maven 4 会自动从 Build POM 生成 Consumer POM。Consumer POM 会去掉 parent 引用（继承内容已内联）、去掉插件配置、只保留实际用到的依赖。

![图片](assets/Maven%204%20%E8%A6%81%E6%9D%A5%E4%BA%86%EF%BC%9A15%20%E5%B9%B4%E5%90%8E%EF%BC%8CJava%20%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7%E8%BF%8E%E6%9D%A5%E2%80%9C%E5%BD%BB%E5%BA%95%E9%87%8D%E6%9E%84%E2%80%9D/e8ef9bef60273a70e5c291f8bca39506_MD5.png)

### 构建与发布流程

![图片](assets/Maven%204%20%E8%A6%81%E6%9D%A5%E4%BA%86%EF%BC%9A15%20%E5%B9%B4%E5%90%8E%EF%BC%8CJava%20%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7%E8%BF%8E%E6%9D%A5%E2%80%9C%E5%BD%BB%E5%BA%95%E9%87%8D%E6%9E%84%E2%80%9D/96149cad917ae55e6adf54ecc494bd22_MD5.png)

### 如何开启 Consumer POM 发布？

在 rc-5 中，Consumer POM 扁平化 **默认关闭** ，需要显式开启：

```
maven.consumer.pom.flatten=true
```

或在命令行传递：

```
mvn deploy -Dmaven.
            consumer.pom
          .flatten=true
```

---

## 四、POM 4.1.0：少写重复配置

升级到 POM 模型 4.1.0 后，很多"复制粘贴式"的配置可以删掉了。Maven 3 的 4.0.0 POM 仍然能正常构建，不升级也不影响。

### 1\. 父 POM 版本自动推断

2005 年的老需求，Maven 4 终于内置了。子模块不必再写 `<version>` ：

```xml
<project xmlns="
            http://maven.apache.org/POM/4.1.0"
                   xmlns:xsi="
            http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="
            http://maven.apache.org/POM/4.1.0
                   " 
             target="_blank" 
             style="color: #576b95; text-decoration: none;">
            https://maven.apache.org/xsd/maven-4.1.0.xsd">
          
  <!-- 省略 version，Maven 自动从父目录推断 -->  <parent>    <groupId>
            com.example
          </groupId>    <artifactId>my-app-parent</artifactId>  </parent>
  <artifactId>my-service</artifactId>
  <dependencies>    <!-- 同仓库子模块依赖也可省略 version -->    <dependency>      <groupId>
            com.example
          </groupId>      <artifactId>my-common</artifactId>    </dependency>  </dependencies></project>
```

### 2\. 子模块自动发现

父 POM 使用 `pom` 打包，且没有手动写 `<subprojects>` 时，Maven 4 会自动扫描子目录里的 `              pom.xml            ` ：

```xml
<project xmlns="
            http://maven.apache.org/POM/4.1.0"
          >  <modelVersion>4.1.0</modelVersion>  <groupId>
            com.example
          </groupId>  <artifactId>my-app-parent</artifactId>  <version>1.0.0-SNAPSHOT</version>  <packaging>pom</packaging>
  </project>
```

### 3\. CI 友好版本号，不再需要 Flatten 插件

Maven 3 时代常用 `${revision}` 配合 flatten-maven-plugin。Maven 4 内置完整支持：

```
<groupId>
            com.example
          </groupId>
<artifactId>my-app</artifactId>
<version>${revision}</version>
```
```
# 在 CI 流水线中指定版本
mvn verify -Drevision=1.2.0
```

或在 `.mvn/             maven.config           ` 中固定：

```
-Drevision=1.0.0-SNAPSHOT
```

### 4\. 新的 BOM 打包类型

BOM（Bill of Materials）有了专属 `packaging` 类型，和 parent POM 职责分得更清楚：

```xml
<project xmlns="
            http://maven.apache.org/POM/4.1.0"
          >  <modelVersion>4.1.0</modelVersion>  <groupId>
            com.example
          </groupId>  <artifactId>my-app-bom</artifactId>  <version>1.0.0</version>  <packaging>bom</packaging>
  <dependencyManagement>    <dependencies>      <dependency>        <groupId>
            org.springframework.boot
          </groupId>        <artifactId>spring-boot-dependencies</artifactId>        <version>3.4.0</version>        <type>pom</type>        <scope>import</scope>      </dependency>    </dependencies>  </dependencyManagement></project>
```

### 5\. 多源码目录，告别 Build Helper 插件

```xml
<build>  <sources>    <source>      <scope>main</scope>      <directory>src/main/java</directory>    </source>    <source>      <scope>main</scope>      <directory>src/main/kotlin</directory>    </source>    <source>      <scope>test</scope>      <directory>src/test/java</directory>    </source>  </sources></build>
```

---

## 五、新工具与日常体验升级

### Maven Upgrade Tool（mvnup）

官方提供的迁移助手，先检查、再自动修复：

```
# 检查项目与 Maven 4 的兼容问题
mvnup check

# 自动应用推荐的 POM 修复
mvnup apply
```

### Maven Shell（mvnsh）

类似 REPL 的交互式 Shell，改完代码不用反复敲完整命令：

```
mvnsh
# 进入交互模式后
mvn> compile
mvn> test -pl my-service
mvn> exit
```

### 构建失败后一键续跑

多模块项目构建失败后，Maven 4 的 `-r` （ `--resume` ）更聪明——会自动从失败模块续跑，并跳过已成功构建的模块：

```
# 首次全量构建
mvn verify

# 修复代码后，从失败处继续
mvn verify -r
```

### 迁移决策流程

![图片](assets/Maven%204%20%E8%A6%81%E6%9D%A5%E4%BA%86%EF%BC%9A15%20%E5%B9%B4%E5%90%8E%EF%BC%8CJava%20%E6%9E%84%E5%BB%BA%E5%B7%A5%E5%85%B7%E8%BF%8E%E6%9D%A5%E2%80%9C%E5%BD%BB%E5%BA%95%E9%87%8D%E6%9E%84%E2%80%9D/456ad1ab0661e8e6f048fadded39a5c8_MD5.png)

## 六、从 Maven 3 迁移，可以怎么做？

不必一步到位。比较稳妥的路径：

1. **本地先试** ：装 Maven 4 RC + JDK 17，跑 `mvnup check` 。
2. **升级插件** ：enforcer、shade、remote-resources 等插件升到最新版。
3. **固定插件版本** ：Maven 4 的 Super POM 默认插件版本有变化，建议在 POM 里显式写死版本，避免"没改代码构建行为却变了"。
4. **CI 并行验证** ：保留 Maven 3 流水线，新增一条 Maven 4 试验线。
5. **等 GA 再全面切换** ：RC 阶段适合尝鲜和反馈，生产环境建议等正式版。

一个最小验证示例：

```bash
# 下载并解压 Maven 4curl -L -O 
            https://archive.apache.org/dist/maven/maven-4/4.0.0-rc-5/binaries/apache-maven-4.0.0-rc-5-bin.tar.gz
          tar -xzf 
            apache-maven-4.0.0-rc-5-bin.tar.gz
          
# 指定 Maven 4 运行（不影响系统默认 Maven 3）/path/to/
            apache-maven-4.0.0-rc-5/bin/mvn
           -version
# 在项目目录检查兼容性/path/to/
            apache-maven-4.0.0-rc-5/bin/mvnup
           check
```

[最近，锋哥又开始收Java+AI大模型编程学员了！](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571719&idx=1&sn=8a19d877e40d49d46ce3637575bb7403&scene=21#wechat_redirect)