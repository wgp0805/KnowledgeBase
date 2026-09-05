---
title: "分布式链路追踪系统之skywalking java agent 的使用、skywalking web界面简介 - Linux-1874"
source: "博客园"
url: "https://www.cnblogs.com/qiuhom-1874/p/21920759"
date: "2026-07-26T13:40:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 分布式链路追踪系统之skywalking java agent 的使用、skywalking web界面简介 - Linux-1874

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/qiuhom-1874/p/21920759  
> **抓取日期**: 2026-07-26  
> **相关性评分**: 1.0

## java 博客系统halo追踪案例

Halo 是一款现代化的个人独立博客系统，而且可能是最好的Java博客系统，从 1.4.3 起，版本要求为 11 以上的版本，1.4.3 以下需要1.8以上的版本。安装要求具体请参考官方文档[https://docs.halo.run/getting-started/prepare ](<https://docs.halo.run/getting-started/prepare>);

### java 环境准备

#### 安装jdk-17
    
    
    root@skywalking-halo-java-agent:~# apt install -y openjdk-17-jdk
    

#### 验证java版本
    
    
    root@skywalking-halo-java-agent:~# java --version
    openjdk 17.0.19 2026-04-21
    OpenJDK Runtime Environment (build 17.0.19+10-1-22.04.2-Ubuntu)
    OpenJDK 64-Bit Server VM (build 17.0.19+10-1-22.04.2-Ubuntu, mixed mode, sharing)
    root@skywalking-halo-java-agent:~# 
    

> java版本是对应安装版本表示java环境准备就绪

### 准备skywalking java agent

#### 下载skywalking java agent

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260725232445675-2049661181.png)

> skywalking 有很多编程语言的agent,根据自己项目选择下载对应的agent即可；
    
    
    root@skywalking-halo-java-agent:~# mkdir /skywalking-agent
    root@skywalking-halo-java-agent:~# cd /skywalking-agent
    root@skywalking-halo-java-agent:/skywalking-agent# wget https://archive.apache.org/dist/skywalking/java-agent/8.13.0/apache-skywalking-java-agent-8.13.0.tgz
    --2026-07-26 05:04:40--  https://archive.apache.org/dist/skywalking/java-agent/8.13.0/apache-skywalking-java-agent-8.13.0.tgz
    Resolving archive.apache.org (archive.apache.org)... 65.108.204.189, 2a01:4f9:1a:a084::2
    Connecting to archive.apache.org (archive.apache.org)|65.108.204.189|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 31443304 (30M) [application/x-gzip]
    Saving to: ‘apache-skywalking-java-agent-8.13.0.tgz’
    
    apache-skywalking-java-agent-8.13.0.tgz    100%[=======================================================================================>]  29.99M  12.9KB/s    in 34m 50s 
    
    2026-07-26 05:39:31 (14.7 KB/s) - ‘apache-skywalking-java-agent-8.13.0.tgz’ saved [31443304/31443304]
    
    root@skywalking-halo-java-agent:/skywalking-agent# ls
    apache-skywalking-java-agent-8.13.0.tgz
    root@skywalking-halo-java-agent:/skywalking-agent#
    

**解压skywalking agent**
    
    
    root@skywalking-halo-java-agent:/skywalking-agent# ls
    apache-skywalking-java-agent-8.13.0.tgz
    root@skywalking-halo-java-agent:/skywalking-agent# tar xf apache-skywalking-java-agent-8.13.0.tgz 
    root@skywalking-halo-java-agent:/skywalking-agent# ls
    apache-skywalking-java-agent-8.13.0.tgz  skywalking-agent
    root@skywalking-halo-java-agent:/skywalking-agent# cd skywalking-agent/
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# ls
    LICENSE  NOTICE  activations  bootstrap-plugins  config  licenses  logs  optional-plugins  optional-reporter-plugins  plugins  skywalking-agent.jar
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# 
    
    

### 配置skywalking java agent
    
    
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# grep -e agent.namespace= -e agent.service_name= -e  collector.backend_service= config/agent.config
    agent.service_name=${SW_AGENT_NAME:halo}
    agent.namespace=${SW_AGENT_NAMESPACE:myapp}
    collector.backend_service=${SW_AGENT_COLLECTOR_BACKEND_SERVICES:192.168.112.73:11800}
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# 
    

> skywalking agent 主要配置以上这三个参数即可，agent.service_name用来描述服务名称；agent.namespace用来描述对应服务所属名称空间，核心配置collector.backend_service用来描述skywalking serverIP地址；即skywalking agent收集的监控数据该发往的server地址；

### 下载java博客 halo jar包
    
    
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# mkdir /myapp
    root@skywalking-halo-java-agent:/skywalking-agent/skywalking-agent# cd /myapp/
    root@skywalking-halo-java-agent:/myapp# wget https://dl.halo.run/release/halo-1.6.1.jar
    --2026-07-26 05:56:49--  https://dl.halo.run/release/halo-1.6.1.jar
    Resolving dl.halo.run (dl.halo.run)... 172.67.178.140, 104.21.43.113, 2606:4700:3036::ac43:b28c, ...
    Connecting to dl.halo.run (dl.halo.run)|172.67.178.140|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 96866805 (92M)
    Saving to: ‘halo-1.6.1.jar’
    
    halo-1.6.1.jar                             100%[=======================================================================================>]  92.38M  2.52MB/s    in 42s     
    
    2026-07-26 05:57:34 (2.20 MB/s) - ‘halo-1.6.1.jar’ saved [96866805/96866805]
    
    root@skywalking-halo-java-agent:/myapp# ls
    halo-1.6.1.jar
    root@skywalking-halo-java-agent:/myapp# 
    

### 启动java 博客系统halo
    
    
    root@skywalking-halo-java-agent:/myapp# java -javaagent:/skywalking-agent/skywalking-agent/skywalking-agent.jar -jar /myapp/halo-1.6.1.jar 
    

> -javaagent参数来指定java agent对应jar包路径，-jar来指定被监控的目标程序jar包；

### 验证halo web界面，安装halo博客系统

**初始化halo博客系统**

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726134623886-1442549196.png)

> halo这个博客系统默认监听在8090端口，我们访问部署halo服务器的8090端口即可访问到halo博客系统的后台地址；第一次访问我们需要填写对应信息安装halo博客系统；

**halo 博客登录界面**

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726134741772-939004842.png)

### 生成测试数据

**编写文章产生访问信息**

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726135044607-1489616688.png)

### skywalking数据验证

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726135146228-235219855.png)

> 能够在skywalking web端看到对应skywalking agent中配置的服务名称和名称空间，表示对应agent已经采集到数据发送给server端了；

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726135241901-1063616186.png)

> 点击对应服务名称 进入界面就可以看到对应服务的各种监控数据；说明skywalking agent已经收集到数据并发送给服务端了；

## skywalking web界面介绍

### skywalking仪表盘简介

#### 普通服务-->服务

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726143943194-810318913.png)

  * Service：服务列表，服务(Service)-表示对请求提供相同行为的一系列或一组工作负载(服务名称),在使用Agent或SDK的时候,可以自定义服务的名字,如果不定义的话,SkyWalking将会使用你在平台(比如 Istio)上定义的名字。 
    * service names: 服务名称。
    * Load (calls / min)：每分钟访问次数。
    * Success Rate (%)：成功率。
    * Latency (ms)：验延迟时间。
    * Apdex：应用性能指数。
  * Topology：架构图
  * Trace：跟踪信息
  * Log：日志



**Apdex简介**

  * Apdex全称是(Application Performance Index,应用性能指数),是由Apdex联盟开放的用于评估应用性能的标准,Apdex 联盟起源于2004年,Apdex标准从用户的角度出发,提供了一个统一的测量和报告用户体验的方法,将其量化为范围为0-1的满意度评价,把最终用户的体验和应用性能作为一个完整的指标进行统一度量。
  * 在网络中运行的任何一个应用(Web服务),它的响应时间决定了用户的满意程度,用户等待所有交互完成时间的长短直接影响了用户对应用的满意程度,这才是对用户有真正意义的“响应时间”,Apdex把完成这样一个任务所用的时间长短称为应用的“响应性”。
  * Apdex 定义了应用响应时间的最优门槛为T,另外根据应用响应时间结合T定义了三种不同的性能表现: 
    * Satisfied(满意)-应用响应时间小于或等于Apdex阈值,比如Apdex阈值为1s,则一个耗时0.6s或者1s的响应结果则可以认为是满意的。
    * Tolerating(可容忍)-应用响应时间大于Apdex阈值,但同时小于或等于4倍的Apdex阈值,假设应用设定的Apdex阈值为1s,则4*1=4s为应用响应时间的容忍上限。
    * Frustrated(烦躁期)-应用响应时间大于4倍的Apdex阈值。



#### 普通服务-->服务--> halo|myapp|-->Overview(服务概览)

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726143859953-329014669.png)

  * Service Apdex（数字）:当前服务的评分
  * Successful Rate（数字）：请求成功率
  * Service Load (calls / min) 数字: 分钟请求数
  * Service Avg Response Times（ms）：平均响应延时，单位ms
  * Service Apdex（折线图）：一段时间内Apdex评分
  * Service Response Time Percentile (ms)折线图：服务响应时间百分比
  * Service Load (calls / min) 折线图: 分钟请求数
  * Success Rate (%)折线图：分钟请求成功百分比
  * Message Queue Consuming Count(折线图)：消息队列消耗计数
  * Message Queue Avg Consuming Latency (ms)折线图：消息队列平均消耗延迟（毫秒）
  * Service Instances Load (calls / min)：节点请求次数
  * Slow Service Instance (ms)：每个服务实例(物理机、云主机、pod)的最大延时
  * Service Instance Success Rate (%)：每个服务实例的请求成功率
  * Endpoint Load in Current Service (calls / min)：每个端点(URL)的请求次数
  * Slow Endpoints in Current Service (ms)：当前端点(URL)的最慢响应时间
  * Success Rate in Current Service (%)：当前服务成功率（%）



#### 普通服务-->服务--> halo|myapp|-->Instance-->选择实例-->Overview(实例概览信息):

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726145017773-645543160.png)

  * Service Instance Load (calls / min）：当前实例的每分钟请求数。
  * Service Instance Success Rate (%)：当前实例的请求成功率。
  * Service Instance Latency (ms)：当前实例的响应延时。
  * Database Connection Pool：数据库连接池信息
  * Thread Pool：线程池信息



#### 普通服务-->服务--> halo|myapp|-->Endpoint(端点信息):

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726145249804-1150973043.png)

  * Endpoints： URL
  * Load (calls / min)：平均请求次数(默认时间范围半小时)，比如半小时内总请求次数6次，6%30=0.20
  * Success Rate (%)：平均成功率(默认时间范围半小时)
  * Latency (ms)：平均延迟时间(默认时间范围半小时)



#### 普通服务-->服务--> halo|myapp|-->Topology(拓扑图)

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726145804898-1867995956.png)

> 这个拓扑图是skywalking 通过agent收集到的数据自动生成出来的程序调用关系图，这个图能够清楚反应程序之间的调用关系；

#### 普通服务-->服务--> halo|myapp|-->Instance-->Trace(请求跟踪信息):

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726150158612-415781615.png)

#### 普通服务-->服务--> halo|magedu|-->Instance-->JVM(实例JVM信息):

![image](https://img2024.cnblogs.com/blog/1503305/202607/1503305-20260726150415322-1363294372.png)

  * JVM CPU (%)：jvm占用CPU的百分比。
  * JVM Memory (MB)：JVM内存占用大小，单位m，包括堆内存，与堆外内存（直接内存）。
  * JVM GC Time (ms)：JVM垃圾回收时间，包含YGC和OGC。
  * JVM GC Count：JVM垃圾回收次数，包含YGC和OGC
  * JVM Thread Count：JVM线程计数统计
  * JVM Thread State Count：JVM线程状态计
  * JVM Class Count：JVM类计数




---
> 原文链接: https://www.cnblogs.com/qiuhom-1874/p/21920759