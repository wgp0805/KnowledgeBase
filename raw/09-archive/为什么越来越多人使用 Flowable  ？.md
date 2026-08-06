---
title: "为什么越来越多人使用 Flowable  ？"
source: "https://mp.weixin.qq.com/s/Ej8Q0neo1W9AJ0enD4BnJQ"
---
小锋 java1234 *2026年8月6日 09:06*

大家好，我是锋哥。

> 如果你做过 OA 审批、订单流转、工单系统，大概率绕不开「工作流引擎」这个话题。近几年，Flowable 在国内 Java 项目里的出镜率越来越高。它到底是什么？凭什么能从 Activiti、Camunda 这些老面孔里脱颖而出？今天锋哥必须好好聊聊这个开源项目。

---

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/f61e4b2bd831c16b4ec1d6c81a7be06a_MD5.webp)

---

## 目录

- 一、Flowable 是什么？
- 二、为什么越来越多人选它？
- 三、和其他 Java 工作流引擎怎么比？
- 四、Flowable 典型架构
- 五、入门案例一：Spring Boot 请假审批
- 六、入门案例二：独立引擎快速体验

---

## 一、Flowable 是什么？

简单说， **Flowable 是一个开源的 Java 工作流引擎** ，帮你把「谁审批、走到哪一步、条件怎么分支」这些业务逻辑，从代码里抽出来，变成可视化的流程图来管理。

它遵循 **BPMN 2.0** 标准——这是业界通用的流程建模规范。画一张流程图，部署到引擎里，引擎就能帮你跑：创建流程实例、分配待办任务、记录审批历史。

Flowable 的历史也很有意思：它最早是从 **Activiti** 分叉出来的。Activiti 的核心开发团队离开后，在 Activiti 的基础上做了大量优化和新功能，于是有了 Flowable。所以如果你之前接触过 Activiti，上手 Flowable 会觉得很亲切。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/18c3af2f4f3845be8be3cc16c3ea6e46_MD5.webp)

---

## 三、为什么越来越多人选它？

归纳起来，大概是这几条原因：

**1\. 和 Java / Spring 生态贴合**

国内大量后端项目是 Spring Boot 搭的。Flowable 提供了 `flowable-spring-boot-starter` ，引入依赖、配好数据库，流程引擎就能跑起来。不需要单独部署一套重型 BPM 平台。

**2\. 功能比较全，但又不臃肿**

除了 BPMN 流程，Flowable 还支持 **CMMN（案例管理）** 和 **DMN（决策表）** 。做复杂审批、规则判断时，不必再额外引入别的组件。

**3\. 性能比 Activiti 更好**

Flowable 在异步执行器、锁粒度、批处理等方面做了优化。同样硬件条件下，高并发场景下通常比原版 Activiti 更稳。

**4\. 嵌入式设计，部署灵活**

可以嵌入到你的 Java 应用里，也可以单独部署成服务。银行、政务、制造等行业常见的「内网部署 + 现有数据库」模式，Flowable 都能适应。

**5\. 中文资料逐渐多起来**

社区教程、掘金/CSDN 上的实战文章、国内企业落地案例，都在增加。对新团队来说，学习成本比一些「文档全英文、案例偏海外」的引擎低不少。

---

## 四、和其他 Java 工作流引擎怎么比？

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/fd845cd10e747e8e2c5c27920359f8a0_MD5.jpg)

### Flowable vs Activiti

| 对比项 | Flowable | Activiti |
| --- | --- | --- |
| 维护活跃度 | 高，持续发版 | 相对较低 |
| 性能 | 异步优化更好 | 基础能力够用 |
| DMN / CMMN | 支持 | 支持有限 |
| 适合场景 | 新项目首选 | 老项目维护 |

两者 API 很像。如果是 **新项目** ，一般更推荐 Flowable；如果老系统已经跑在 Activiti 上，迁移要评估数据库脚本和业务兼容，不必为了追新而强行换。

### Flowable vs Camunda

| 对比项 | Flowable | Camunda |
| --- | --- | --- |
| 架构风格 | 经典嵌入式引擎 + 关系型数据库 | Camunda 7 类似；Camunda 8 走云原生事件流 |
| 上手难度 | 中等 | Camunda 8 学习曲线更陡 |
| 运维工具 | 基础 UI + 可自建 | Cockpit / Operate 等更完善 |
| 超高并发 | 够用，需自己调优 | Camunda 8 + Zeebe 更强 |
| 适合场景 | Spring 单体 / 微服务嵌入 | 大规模分布式、云原生 |

一句话： **Camunda 在监控和超大规模场景更猛，Flowable 在「嵌入现有 Java 系统、快速落地」这条路上更省心。**

### 还有 jBPM 呢？

jBPM 和 Drools 规则引擎是一家的，如果你的业务 **规则特别复杂** （风控、定价策略），jBPM 值得考虑。但如果只是常规审批流，Flowable 或 Camunda 往往更轻。

---

## 五、Flowable 典型架构

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/7e0fb017b52a41878ed5de5fe161c1ed_MD5.jpg)

最常见的落地方式是这样的：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/15e542e3335c9c3eba7dde21c4db5d94_MD5.png)

流程图（`.             bpmn20.xml           ` ）放在 `resources/processes/` 目录，应用启动时自动部署。业务代码通过 `RuntimeService` 、 `TaskService` 等 API 驱动流程运转，数据落在关系型数据库里，运维同学熟悉的套路。

---

## 六、入门案例一：Spring Boot 请假审批

### 流程长什么样？

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/75ceb3562b1481b6c67d2cbdb2798967_MD5.png)

### 核心步骤

**1\. 引入依赖**

```xml
<dependency>    <groupId>
            org.flowable
          </groupId>    <artifactId>flowable-spring-boot-starter-process</artifactId>    <version>7.0.1</version></dependency>
```

**2\. 编写 BPMN 流程文件**

```bash
<process id="leaveApproval" name="请假审批" isExecutable="true">    <startEvent id="startEvent"/>    <userTask id="managerApprove" name="经理审批"              flowable:assignee="${manager}"/>    <endEvent id="endEvent"/></process>
```

**3\. 启动流程、查询待办、完成任务**

```javascript
// 员工提交请假String instanceId = runtimeService    .startProcessInstanceByKey("leaveApproval", variables)    .getId();
// 经理查待办List<Task> tasks = taskService.createTaskQuery()    .taskAssignee("李经理")    .list();
// 经理点「通过」taskService.complete(taskId, variables);
```

启动应用后，调用接口就能跑通：

```bash
# 提交申请POST /leave/apply?employee=张三&manager=李经理&days=3
# 查看待办GET /leave/tasks?assignee=李经理
# 完成审批POST /leave/complete?taskId=xxx&approved=true
```

这个案例覆盖了 Flowable 最核心的三个动作： **部署流程、启动实例、处理任务** 。大部分业务系统都是在这三件事上叠功能。

---

## 七、入门案例二：独立引擎快速体验

有时候你只是想 **本地试一下** ，不想搭 Spring Boot。Flowable 也支持 standalone 模式，用 H2 内存数据库，一个 `main` 方法就能跑：

```java
ProcessEngine engine = ProcessEngineConfiguration    .createStandaloneInMemProcessEngineConfiguration()    .setDatabaseSchemaUpdate(DB_SCHEMA_UPDATE_TRUE)    .buildProcessEngine();
// 部署 → 启动 → 查任务 → 完成任务Deployment deployment = 
            engine.getRepositoryService()
              .createDeployment()    .addClasspathResource("
            expense-process.bpmn20.xml"
          )    .deploy();
String instanceId = 
            engine.getRuntimeService()
              .startProcessInstanceByKey("expenseProcess", variables)    .getId();
```

这个报销流程更简单：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8%20Flowable%20%20%EF%BC%9F/b0f012584f269704c4d140bef18c5ed8_MD5.png)

适合用来验证「流程文件有没有写对」「任务能不能正常流转」，之后再迁移到 Spring Boot 项目里。

---

官方仓库地址： [https://github.com/flowable/flowable-engine](https://github.com/flowable/flowable-engine)

[2026年，锋哥又开始收Java+AI大模型编程学员了！目前活动，送AI编程+Python+AI大模型VIP。。](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571915&idx=1&sn=6deb7659b60dc4dc3647a22babe9aad3&scene=21#wechat_redirect)