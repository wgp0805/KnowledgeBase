---
title: "SpringBoot + mybatis-plus项目的SQL映射问题（完全萌新？"
source: "SegmentFault"
url: "https://segmentfault.com/q/1010000048092604"
date: "2026-07-29T18:07:10+08:00"
score: 1.0
tags: ["中文", "编程", "问答", "技术"]
auto_captured: true
---

# SpringBoot + mybatis-plus项目的SQL映射问题（完全萌新？

> **来源**: SegmentFault  
> **链接**: https://segmentfault.com/q/1010000048092604  
> **抓取日期**: 2026-07-30  
> **相关性评分**: 1.0

完全的萌新第一个SpringBoot项目，主要爆红问题是：  
**MyBatis-Plus尝试执行某个 Mapper 方法，却找不到与之对应的 SQL 映射**  
具体爆红日志如下：
    
    
    2026-07-29T16:57:48.976+08:00 ERROR 38512 --- [nio-8080-exec-6] o.a.c.c.C.[.[.[/].[dispatcherServlet]    : Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed: org.apache.ibatis.binding.BindingException: Invalid bound statement (not found): com.silver.mapper.CategoryMapper.selectList] with root cause
    
    org.apache.ibatis.binding.BindingException: Invalid bound statement (not found): com.silver.mapper.CategoryMapper.selectList
        at org.apache.ibatis.binding.MapperMethod$SqlCommand.<init>(MapperMethod.java:229) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperMethod.<init>(MapperMethod.java:53) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.lambda$cachedInvoker$0(MapperProxy.java:96) ~[mybatis-3.5.19.jar:3.5.19]
        at java.base/java.util.concurrent.ConcurrentHashMap.computeIfAbsent(ConcurrentHashMap.java:1724) ~[na:na]
        at org.apache.ibatis.util.MapUtil.computeIfAbsent(MapUtil.java:36) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.cachedInvoker(MapperProxy.java:94) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.invoke(MapperProxy.java:86) ~[mybatis-3.5.19.jar:3.5.19]
        at jdk.proxy2/jdk.proxy2.$Proxy73.selectList(Unknown Source) ~[na:na]
        at com.baomidou.mybatisplus.extension.repository.IRepository.list(IRepository.java:300) ~[mybatis-plus-extension-3.5.17.jar:na]
        at com.baomidou.mybatisplus.extension.repository.IRepository.list(IRepository.java:321) ~[mybatis-plus-extension-3.5.17.jar:na]
        at com.silver.service.impl.CategoryServiceImpl.getAllCategory(CategoryServiceImpl.java:22) ~[classes/:na]
        at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104) ~[na:na]
        at java.base/java.lang.reflect.Method.invoke(Method.java:565) ~[na:na]
        at org.springframework.aop.support.AopUtils.invokeJoinpointUsingReflection(AopUtils.java:359) ~[spring-aop-7.0.8.jar:7.0.8]
        at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:715) ~[spring-aop-7.0.8.jar:7.0.8]
        at com.silver.service.impl.CategoryServiceImpl$$SpringCGLIB$$0.getAllCategory(<generated>) ~[classes/:na]
        at com.silver.controller.CategoryController.getCategoryList(CategoryController.java:20) ~[classes/:na]
        at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104) ~[na:na]
        at java.base/java.lang.reflect.Method.invoke(Method.java:565) ~[na:na]
        at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:252) ~[spring-web-7.0.8.jar:7.0.8]
        at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:184) ~[spring-web-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:117) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:934) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:853) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:86) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:963) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:866) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1000) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:892) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:622) ~[tomcat-embed-core-11.0.22.jar:6.1]
        at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:874) ~[spring-webmvc-7.0.8.jar:7.0.8]
        at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:710) ~[tomcat-embed-core-11.0.22.jar:6.1]
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:128) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53) ~[tomcat-embed-websocket-11.0.22.jar:11.0.22]
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:107) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:100) ~[spring-web-7.0.8.jar:7.0.8]
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116) ~[spring-web-7.0.8.jar:7.0.8]
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:107) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.springframework.web.filter.FormContentFilter.doFilterInternal(FormContentFilter.java:93) ~[spring-web-7.0.8.jar:7.0.8]
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116) ~[spring-web-7.0.8.jar:7.0.8]
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:107) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:199) ~[spring-web-7.0.8.jar:7.0.8]
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116) ~[spring-web-7.0.8.jar:7.0.8]
        at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:107) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:165) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:77) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:492) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:113) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:83) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:72) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:341) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:397) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:63) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:1272) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1801) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:52) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:946) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:480) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:57) ~[tomcat-embed-core-11.0.22.jar:11.0.22]
        at java.base/java.lang.Thread.run(Thread.java:1474) ~[na:na]
    
    2026-07-29T16:57:48.979+08:00 ERROR 38512 --- [nio-8080-exec-2] o.a.c.c.C.[.[.[/].[dispatcherServlet]    : Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed: org.apache.ibatis.binding.BindingException: Invalid bound statement (not found): com.silver.mapper.ArticleMapper.selectList] with root cause
    
    org.apache.ibatis.binding.BindingException: Invalid bound statement (not found): com.silver.mapper.ArticleMapper.selectList
        at org.apache.ibatis.binding.MapperMethod$SqlCommand.<init>(MapperMethod.java:229) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperMethod.<init>(MapperMethod.java:53) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.lambda$cachedInvoker$0(MapperProxy.java:96) ~[mybatis-3.5.19.jar:3.5.19]
        at java.base/java.util.concurrent.ConcurrentHashMap.computeIfAbsent(ConcurrentHashMap.java:1724) ~[na:na]
        at org.apache.ibatis.util.MapUtil.computeIfAbsent(MapUtil.java:36) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.cachedInvoker(MapperProxy.java:94) ~[mybatis-3.5.19.jar:3.5.19]
        at org.apache.ibatis.binding.MapperProxy.invoke(MapperProxy.java:86) ~[mybatis-3.5.19.jar:3.5.19]
        at jdk.proxy2/jdk.proxy2.$Proxy72.selectList(Unknown Source) ~[na:na]

在豆包的帮助下，我认为问题应该存在于`pom.xml`文件和`mapper`文件

以下给出两类文件的主要代码
    
    
    <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>4.0.7</version>
            <relativePath/> <!-- lookup parent from repository -->
        </parent>
        <groupId>com.silver</groupId>
        <artifactId>blog_simple</artifactId>
        <version>0.0.1-SNAPSHOT</version>
        <name>blog_simple</name>
        <description>blog_simple</description>
        <properties>
            <java.version>17</java.version>
        </properties>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-webmvc</artifactId>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>4.0.1</version>
            </dependency>
    
            <dependency>
                <groupId>com.mysql</groupId>
                <artifactId>mysql-connector-j</artifactId>
                <scope>runtime</scope>
            </dependency>
            <dependency>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <optional>true</optional>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-webmvc-test</artifactId>
                <scope>test</scope>
            </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter-test</artifactId>
            <version>4.0.1</version>
            <scope>test</scope>
        </dependency>
    
    
    //是三个单独的类，重复部分（导包）省略
    package com.silver.mapper;
    
    import com.baomidou.mybatisplus.core.mapper.BaseMapper;
    import com.silver.entity.Article;
    import org.apache.ibatis.annotations.Mapper;
    
    @Mapper
    public interface ArticleMapper extends BaseMapper<Article> {
    }
    
    
    @Mapper
    public interface CategoryMapper extends BaseMapper<Category> {
    }
    
    @Mapper
    public interface CommentMapper extends BaseMapper<Comment> {
    }

我也不是很清楚问题是否会出现在什么别的地方，希望各位佬高抬贵手，帮帮孩子（TaT

我主要也是跟着豆包的回答尝试修改，都没有什么成效  
例如是版本问题，包名路径问题，然后感觉豆包都是一些过时的信息（免费的是这样  
其余尝试修改的几个方向都没什么参考价值，就不说了


---
> 原文链接: https://segmentfault.com/q/1010000048092604