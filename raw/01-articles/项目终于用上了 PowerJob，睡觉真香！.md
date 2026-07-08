---
title: "项目终于用上了 PowerJob，睡觉真香！"
source: "https://mp.weixin.qq.com/s/uqxvIasqGeZcGvyeOmwcPg"
---
小哈学Java *2026年6月17日 14:58*

![图片](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/212d07eab008ced951fc3bc58a5f478c_MD5.webp)

来源： [blog.csdn.net/qq\_24950043/article/details/130175241](http://blog.csdn.net/qq_24950043/article/details/130175241)

**在线 Java 面试刷题（已更新241题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 简介
- 定时任务类型
- 安装
- 定时任务创建
- 任务配置参数详解

---

最近项目中使用了 PowerJob 做任务调度模块，感觉这个框架真香，今天我们就来深入了解一下新一代的定时任务框架——PowerJob！

## 简介

PowerJob 是基于 java 开发的企业级的分布式任务调度平台，与 xxl-job 一样，基于 web 页面实现任务调度配置与记录，使用简单，上手快速，其主要功能特性如下：

- **使用简单** ：提供前端 Web 界面，允许开发者可视化地完成调度任务的管理（增、删、改、查）、任务运行状态监控和运行日志查看等功能。
- **定时策略完善** ：支持 CRON 表达式、固定频率、固定延迟和 API 四种定时调度策略。
- **执行模式丰富** ：支持单机、广播、Map、MapReduce 四种执行模式，其中 Map/MapReduce 处理器能使开发者寥寥数行代码便获得集群分布式计算的能力。
- **工作流支持** ：支持在线配置任务依赖关系（DAG），以可视化的方式对任务进行编排，同时还支持上下游任务间的数据传递，以及多种节点类型（判断节点 & 嵌套工作流节点）。
- **执行器支持广泛** ：支持 Spring Bean、内置/外置 Java 类，另外可以通过引入官方提供的依赖包，一键集成 Shell、Python、HTTP、SQL 等处理器，应用范围广。
- **运维便捷** ：支持在线日志功能，执行器产生的日志可以在前端控制台页面实时显示，降低 debug 成本，极大地提高开发效率。
- **依赖精简** ：最小仅依赖关系型数据库（MySQL/PostgreSQL/Oracle/MS SQLServer…）
- **高可用 & 高性能** ：调度服务器经过精心设计，一改其他调度框架基于数据库锁的策略，实现了无锁化调度。部署多个调度服务器可以同时实现高可用和性能的提升（支持无限的水平扩展）。
- **故障转移与恢复** ：任务执行失败后，可根据配置的重试策略完成重试，只要执行器集群有足够的计算节点，任务就能顺利完成。

相对于其他定时任务框架具有无锁化设计，更强悍的性能支撑，我们通过官网的产品对比可以了解详情：

| 项目 | QuartZ | xxl-job | SchedulerX 2.0 | PowerJob |
| --- | --- | --- | --- | --- |
| 定时类型 | CRON | CRON | CRON、固定频率、固定延迟、OpenAPI | CRON、固定频率、固定延迟、OpenAPI |
| 任务类型 | 内置 Java | 内置 Java、GLUE Java、Shell、Python 等脚本 | 内置 Java、外置 Java（FatJar）、Shell、Python 等脚本 | 内置 Java、外置 Java（容器）、Shell、Python 等脚本 |
| 分布式任务 | 无 | 静态分片 | MapReduce 动态分片 | MapReduce 动态分片 |
| 在线任务治理 | 不支持 | 支持 | 支持 | 支持 |
| 日志白屏化 | 不支持 | 支持 | 不支持 | 支持 |
| 调度方式及性能 | 基于数据库锁，有性能瓶颈 | 基于数据库锁，有性能瓶颈 | 不详 | 无锁化设计，性能强劲无上限 |
| 报警监控 | 无 | 邮件 | 短信 | 邮件，提供接口允许开发者扩展 |
| 系统依赖 | 关系型数据库（MySQL、Oracle…） | MySQL | 人民币 | 任意 Spring Data Jpa 支持的关系型数据库（MySQL、Oracle…） |
| DAG 工作流 | 不支持 | 不支持 | 支持 | 支持 |

官网文档： [http://www.powerjob.tech/](http://www.powerjob.tech/)

### 定时任务类型

与传统的定时任务框架对比，powerJob 支持更多的定时任务类型：

- **API** ：通过客户端提供的 api 接口触发，服务端不会主动调度，适用于与业务服务上下连接或只调度一次的业务场景
- **CRON** ：通过 cron 表达式调度，这是多数定时任务框架都支持的
- **固定频率** ：每隔多少毫秒执行一次。
- **固定延迟** ：延迟多少毫秒执行一次
- **工作流** ：配合工作流进行调度，服务端不会主动调度，当工作流节点执行到该任务时运行。

## 安装

PowerJob 支持两种安装方式，一是通过 jar 包运行，一是通过 docker 安装

docker 的安装较为简单，且官网有详细说明，这里就不单独讲解了，大家可参考官方文档：

- [https://www.yuque.com/powerjob/guidence/docker-compose](https://www.yuque.com/powerjob/guidence/docker-compose)

**如何通过 jar 形式运行的**

1、首先我们可以在 github 上下载源码，可以自己编译打包

- [https://github.com/PowerJob/PowerJob](https://github.com/PowerJob/PowerJob)

可以在 releases 中下载指定版本

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/099b0c4b042eb7660ceb6b97ca952482_MD5.png)

2、在 IDE 中打开后，我们 `powerjob-server` 就是我们要的服务端源码，可以直接编译，而 `powerjob-worker-samples` 就是 springboot 下的使用示例

3、在运行编译服务端之前，我们需要先创建数据库，在指定的数据库下创建即可

```
CREATE DATABASE IF NOT EXISTS \`powerjob-daily\` DEFAULT CHARSET utf8mb4
```

4、然后将 `powerjob-server/powerjob-server-starter` 下的 `              application-daily.properties            ` 配置文件中的数据库配置改成你服务器的

其中 daily, pre, product 表示日常、预生产、生产环境下的配置，与我们常见的 dev, test, prod 类似，可以根据需要进行调整

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/1f3aabb78d7701b9d08fa1299c0e5dbc_MD5.png)

其中还有邮箱及其他配置，如果有需要也可以调整，服务端的参数配置可参考官网文档。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

5、我们先来本地运行启动类 PowerJobServerApplication 一下试试，启动成功后，访问 http://localhost:7700，出现登陆页则说明运行成功

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/41b38baa7c2dd4f6bac87c8002775487_MD5.png)

6、先注册一个执行器，注意这里的应用名称不能顺便取，下文在客户端的配置的 app-name 要与该名称保持一致

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/14869c57e618a705f02d364f4c6f5be3_MD5.png)

7、然后用该执行器名和密码登录

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/f74f0247959835b6987ccbd3c9ac47c5_MD5.png)

8、如下，我们就登录成功了

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/7f12ddc4df81478561cd036ca5ccb539_MD5.png)

9、如果需要发布到服务器或虚拟机上运行，可以进行编译打包操作：

1）点击 `mvn install` 将依赖包打包到本地仓库

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/eb9c1db79a1e74d95f543e6020e659f7_MD5.png)

注意，如果这里报错

```
Please refer to /Library/project/study/java/
            PowerJob-4.3.2/powerjob-server/powerjob-server-starter/target/surefire-reports
           for the individual test results.
```

那么可以将 maven 的健康检查关闭

点击如图所示按钮，并且看到 test 置灰，则表示关闭

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/25b141c210ccfda74ecf89a84b31058a_MD5.png)

2）执行 mvn package 打包项目

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/b465f1c0d937aa0f5fe5ba183b3b6404_MD5.png)

10、在 `powerjob-server-starter` 的 target 目录下即可看到打包出来的 jar，将其上传到指定服务器，通过 `java -jar` 指令即可运行

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/bab8414f260be03e2e7996ea5b50cec4_MD5.png)

## 定时任务创建

1、创建一个 springboot 项目，用于定时任务客户端，引入客户端依赖，如果是 spring 或其他 java 项目引入，可参考官网文档：

- [https://www.yuque.com/powerjob/guidence/ygonln](https://www.yuque.com/powerjob/guidence/ygonln)
```
<dependency>
    
            tech.powerjob
          
    <artifactId>powerjob-worker-spring-boot-starter</artifactId>
    <version>4.3.2</version>
</dependency>
```

2、修改配置文件

```
powerjob:
  worker:
    enabled:true
    enable-test-mode:false
    # 数据传输端口，默认27777
    port:27777
    # 应用名称，与服务端创建的应用账号的名称保持一致
    app-name:powerjob-agent-test
    # 服务端地址，多个用,隔开
    server-address:127.0.0.1:7700
    # 通讯协议，4.3.0之后支持http和akka，4.3.0之前仅支持akka，官方推荐http
    protocol:http
    # 任务返回结果信息的最大长度，超过该值将被截断
    max-result-length:4096
    # 同时运行的轻量级任务数量上限
    max-lightweight-task-num:1024
    # 同时运行的重量级任务数量上限
    max-heavy-task-num:64
```

3、启动类上添加注解 @EnableScheduling

4、通过申明 BasicProcessor 接口，实现 process 方法来书写一个简单的定时任务示例类，注意要声明为 bean

```
/**
 * @author benjamin_5
 * @Description 简单任务执行器
 * @date 2023/5/3
 */
@Component
public class SimpleJobServer implements BasicProcessor {

    @Override
    public ProcessResult process(TaskContext taskContext) throws Exception {
        String jobParams = 
            taskContext.getJobParams();
          
        
            System.out.println(
          "参数: " + jobParams);

        
            System.out.println(
          "定时任务执行");

        return new ProcessResult(true, "定时任务执行成功");
    }
}
```

5、启动客户端项目，运行成功后，可以在服务端首页看到机器实例

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/39b9d8358efb69d048db4296cdabd87f_MD5.png)

6、服务端任务管理点击新建任务

其中处理器配置是通过书写处理器的全类路径名来声明的，比如我这里是 `              com.example.powerjobdemo.job.SimpleJobServer            `

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/7335abec96b8af31287f5f454d3ce9bd_MD5.png)

7、创建成功后，可以在列表看到新建的任务

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/20570ea63ea80c8ce7a39e09558c7426_MD5.png)

8、打开客户端控制台，也能看到输出的参数和执行打印，说明任务执行成功

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/1b61de8761ec83f13f5769f2df16941a_MD5.png)

9、同时我们可以在运行记录中看到执行日志

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/787cd8d7ad35e1b321b2a0d92434f76c_MD5.png)

至此，针对 powerjob 的最简单使用就完成了，接下来我们继续来看关于 powjob 的配置详解

## 任务配置参数详解

创建任务时我们可以看到如下图所示的配置：

![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/6c3ff167486355f412f066e8a00547c3_MD5.png)

**定时信息：**

主要选择定时任务类型，支持 API, CRON，固定频率、固定延迟、工作流、每日固定间隔等几种定时任务类型。

**生命周期：**

这是比其他任务框架更便捷的功能，指定了任务的生效周期，如果该任务是预定某时间段内执行的，可以通过该参数配置

**执行配置：**

- 执行类型支持单机执行、广播执行、Map 执行、MapReduce 执行
- 单机执行表示只需要有一个节点执行任务即可的场景
- 广播执行表示需要全部节点一同执行的场景，比如清除机器日志、各节点数据统计
- Map 与 MapReduce 执行都是表示分布式、分批执行，用来拆分计算量、耗时较大的任务，区别在于 Map 执行是一种简单的数据处理逻辑，特点是将输入数据拆分成多个子块，并交给多个分布式节点同时执行，以提高数据处理效率，适用于简单的数据处理场景
- MapReduce 执行是一种大数据处理框架，处理逻辑是将复杂的数据处理拆分成 Map 和 Reduce 阶段进行处理，通过数据分组计算后合并来提供数据处理效率，更适合复杂的大数据场景

**运行时配置：**

- 支持 `HEALTH_FIRST` 和 `RANDOM` ，即第一个健康节点和随机，用于选择执行处理器节点的策略。
- 最大实例数用于控制处理器节点数量，线程并发度用于控制并发，运行时间限制

更多说明，可在官方文档中查看：

- [https://www.yuque.com/powerjob/guidence/ysug77](https://www.yuque.com/powerjob/guidence/ysug77)
![在这里插入图片描述](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/8566169799647e51e63fa14d4ba9e992_MD5.png)

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%A1%B9%E7%9B%AE%E7%BB%88%E4%BA%8E%E7%94%A8%E4%B8%8A%E4%BA%86%20PowerJob%EF%BC%8C%E7%9D%A1%E8%A7%89%E7%9C%9F%E9%A6%99%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 企业级消息推送架构设计，太强了！3. 面试官：RAG 中的混合检索是什么？为什么要用混合检索而不是纯向量检索？4. 字节面试官：post 为什么会发送两次请求？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢啦
```

阅读原文