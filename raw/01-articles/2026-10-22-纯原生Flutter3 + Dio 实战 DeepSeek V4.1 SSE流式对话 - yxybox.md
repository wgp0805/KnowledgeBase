---
title: "纯原生Flutter3 + Dio 实战 DeepSeek V4.1 SSE流式对话 - yxybox"
source: "博客园"
url: "https://www.cnblogs.com/yxybox/p/23405031"
date: "2026-10-22T13:39:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 纯原生Flutter3 + Dio 实战 DeepSeek V4.1 SSE流式对话 - yxybox

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/yxybox/p/23405031  
> **抓取日期**: 2026-10-22  
> **相关性评分**: 1.0

2026最新：用 **Flutter3.41 + Dio** 接入 **DeepSeek V4.1** ：流式AI对话App开发实践。

## 项目技术栈一览 📦

类别 |  技术/插件 |  版本 |  说明  
---|---|---|---  
UI 框架 |  Flutter |  3.41.5 |  跨平台 UI 框架  
编程语言 |  Dart |  3.11 |  Flutter 配套语言  
大模型 |  DeepSeek-V4.1-Flash |  — |  聊天大模型，支持流式输出与深度思考  
网络请求 |  dio |  ^5.11.1 |  HTTP 客户端，处理 SSE 流式请求  
路由 / 状态管理 |  get |  ^4.7.3 |  路由跳转、依赖注入、响应式状态管理  
本地存储 |  get_storage |  ^2.1.1 |  轻量级键值存储，保存会话与配置  
Markdown 解析 |  flutter_markdown_plus |  ^1.0.12 |  核心 Markdown 渲染引擎  
代码高亮 |  flutter_highlight |  ^0.7.0 |  代码块语法高亮  
LaTeX 公式 |  flutter_markdown_plus_latex |  ^1.0.5 |  行内/块级数学公式渲染  
Mermaid 图表 |  flutter_mermaid |  ^0.1.0 |  流程图/时序图/甘特图渲染  
弹框组件 |  shirne_dialog |  ^4.9.0 |  自定义弹窗、Toast、底部弹层  
图片预览 |  easy_image_viewer |  ^1.5.1 |  点击放大、手势缩放、滑动切换  
环境变量 |  flutter_dotenv |  ^6.0.1 |  读取 `.env` 配置，管理 API Key 等敏感信息  
  
## 功能特性 ✨

模块 |  功能点 |  说明  
---|---|---  
基础能力 |  Flutter3.41 + Dart3 搭建项目 |  跨平台运行 Android / iOS / Web / Windows  
大模型 |  接入 DeepSeek-V4.1 |  支持流式打字输出，对话丝滑流畅  
思考模式 |  深度思考 |  展示推理过程 / 思考链，可折叠  
数学公式 |  LaTeX 公式渲染 |  支持行内 `$...$` 与块级 `$$...$$`  
代码体验 |  代码块横向滚动 |  长代码不撑破布局  
代码体验 |  代码高亮 |  多语言语法高亮  
代码体验 |  复制代码 |  一键复制代码块内容  
会话能力 |  多轮上下文会话 |  携带历史消息，连续对话不丢失上下文  
数据存储 |  本地存储对话 |  GetStorage 持久化会话 / 历史记录  
富文本 |  图片预览 |  点击放大、手势缩放  
富文本 |  链接跳转 |  Markdown 链接安全打开  
富文本 |  表格渲染 |  支持 AI 返回的 Markdown 表格  
多端布局 |  手机端 / 桌面端 750px |  窄屏单栏，≥750px 切桌面/宽屏布局  
  
## 项目结构目录

## flutter项目环境变量
    
    
    # 项目名称
    APP_NAME = 'Flutter3-DeepSeek'
    
    # DeepSeek API配置
    DEEPSEEK_API_KEY = your apikey
    DEEPSEEK_BASE_URL = https://api.deepseek.com

## main.dart配置
    
    
    import 'dart:io';
    import 'package:flutter/material.dart';
    import 'package:flutter/services.dart';
    import 'package:get/get.dart';
    import 'package:get_storage/get_storage.dart';
    import 'package:shirne_dialog/shirne_dialog.dart';
    import 'package:flutter_dotenv/flutter_dotenv.dart';
    
    import 'controller/app.dart';
    import 'controller/chat.dart';
    
    // 引入路由配置
    import 'router/index.dart';
    
    void main() async {
      // 初始化存储服务
      await GetStorage.init();
    
      // 将.env文件内容加载到dotenv中
      await dotenv.load(fileName: '.env');
    
      // 注册GetxController
      Get.put(AppStore());
      Get.put(ChatStore());
    
      runApp(const MyApp());
    }
    
    class MyApp extends StatelessWidget {
      const MyApp({super.key});
    
      @override
      Widget build(BuildContext context) {
        // 获取AppStore实例
        final appStore = AppStore.to;
        
        return AnnotatedRegion(
          value: SystemUiOverlayStyle(
            /**
             * 修复flutter3.32以上会出现底部导航栏背景黑色
             * The bottom navigation bar is always black from flutter: 3.32.1.
             * It's working fine on flutter: 3.29.3
            */
            systemNavigationBarColor: Colors.transparent,
            systemNavigationBarIconBrightness: Brightness.dark,
          ),
          child: GetMaterialApp(
            title: 'Flutter3-DeepSeek',
            debugShowCheckedModeBanner: false,
            theme: ThemeData(
              colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFF5842F2)),
              useMaterial3: true,
              fontFamily: Platform.isWindows ? 'Microsoft YaHei' : null,
            ),
            // 初始路由
            initialRoute: appStore.isLogin ? '/' : '/login',
            // 路由页面
            getPages: routePages,
            // 初始弹窗key
            navigatorKey: MyDialog.navigatorKey,
            localizationsDelegates: [
              // Add your ShirneDialogLocalizations delegate here
              ShirneDialogLocalizations.delegate,
            ],
          ),
        );
      }
    }

## 整体布局结构
    
    
    @override
    Widget build(BuildContext context) {
      return Scaffold(
        key: scaffoldKey,
        backgroundColor: Colors.white,
        appBar: AppBar(
          ...
          actions: [
            IconButton(icon: Icon(Icons.try_sms_star_outlined), onPressed: () => handleCreate(),),
          ],
        ),
        body: Center(
          child: ConstrainedBox(
            constraints: BoxConstraints(
              maxWidth: 750.0,
            ),
            child: Flex(
              direction: Axis.vertical,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Stack(
                    children: [
                      GestureDetector(
                        child: ScrollConfiguration(
                          behavior: CustomScrollBehavior().copyWith(scrollbars: false),
                          // GetBuilder响应流式输出
                          child: Obx(() {
                            if (chatStore.currentMessages.isEmpty) {
                              // 欢迎信息
                              return Welcome(
                                onChanged: (value) {
                                  textEditingController.text = value;
                                },
                              );
                            }
                            return ListView.builder(
                              keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag, // 当滚动时候隐藏键盘
                              controller: scrollController,
                              padding: EdgeInsets.all(10.0),
                              reverse: true,
                              shrinkWrap: true,
                              itemCount: chatStore.currentMessages.length,
                              itemBuilder: (context, index) {
                                ...
                              }
                            );
                          }),
                        ),
                        onTap: () {
                          focusNode.unfocus();
                        },
                      ),
                      // 滚动到底部
                      AnimatedPositioned(
                        ...
                      ),
                    ],
                  ),
                ),
                // 底部编辑器区域
                ChatEditor(controller: textEditingController),
              ]
            ),
          ),
        ),
        // 侧边栏
        drawer: Drawer(
          child: Sidebar(),
        ),
      );
    }

至此，完成了从零搭建 **Flutter3.41 + Dart3** ​ 集成 **DeepSeek-V4.1** ​ 的跨平台 AI 流式对话应用。

这套方案通过 **SSE 流式响应** ​ 与 **GetX 状态管理** ，实现了丝滑的打字机式对话交互，并扩展了 **深度思考、LaTeX 公式、Mermaid 图表、代码高亮、图片预览** ​ 等能力，让 Flutter 在 AI 应用场景中有了更完整的表现力。


---
> 原文链接: https://www.cnblogs.com/yxybox/p/23405031