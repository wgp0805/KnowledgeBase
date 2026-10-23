---
title: "从零开始搭建后台系统（vue3+TypeScript+Vite）01 - 落花看风雪"
source: "博客园"
url: "https://www.cnblogs.com/myflowers/p/23399187"
date: "2026-10-22T10:56:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 从零开始搭建后台系统（vue3+TypeScript+Vite）01 - 落花看风雪

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/myflowers/p/23399187  
> **抓取日期**: 2026-10-22  
> **相关性评分**: 1.0

# vue3Admin

这个模板应该能帮助你开始在Vite中使用Vue3进行开发。

参照vue3-element-admin，[点击查看官网](<https://www.youlai.tech/docs/>)。技术栈包括TypeScript、JSX、Vue Router、Pinia。 UI框架采用[element-plus 2.14.7](<https://element-plus.org/zh-CN/>)

## Project Setup（初始化）
    
    
    # 创建名为vue3Admin的项目
    pnpm create vue@latest vue3Admin
    
    
    # 初始化项目选择
    pnpm create vue@latest vue3Admin
    TypeScript → Yes
    JSX → No（除非你需要，例如动态性极高的场景。比如你要写一个高度可配置的动态表单生成器。属于进阶选择。）
    Vue Router → 按需（本项目Yes）
    Pinia → 按需 （本项目Yes）
    Vitest / E2E → No（基础脚手架可先跳过）
    ESLint / Prettier → 按需 （本项目Yes）
    
    
    # 进入项目目录
    cd vue3Admin

### Install Dependencies（安装依赖）
    
    
    # 安装依赖
    pnpm install

### Compile and Hot-Reload for Development（开发编译，含热重启）
    
    
    # 开发编译，含热重启
    pnpm dev

### Type-Check, Compile and Minify for Production（生产编译，含检查、压缩）
    
    
    # 生产编译，含检查、压缩
    pnpm build

# 开发实录

这是一个空白模板，从零开始搭建后台系统。

# 项目结构
    
    
    vue3Admin
    ├── index.html
    ├── README.md
    ├── .env.development
    ├── .env.production
    ├── public
    │   ├── favicon.ico
    │   └──
    ├── src
    │   ├── router
    │   │   └── index.ts
    │   ├── views
    │   │   ├── Home.vue
    │   │   ├── login
    │   │   │   ├── index.vue
    │   │   │   └── components
    │   │   |       ├── Register.vue
    │   │   |       ├── QrCodeLogin.vu
    |   │   |       └── ResetPwd.vue

## 入口 HTML 文件

`index.html` 是 Vite 项目的入口 HTML 文件，也是浏览器加载应用时第一个请求的页面。

#### 网站标题（title）
    
    
    <!-- index.html -->
    <title>%VITE_APP_TITLE%</title>

VITE_APP_TITLE在.env文件中进行`全局`配置。本项目更多配置方式见[环境变量配置](<https://file+.vscode-resource.vscode-cdn.net/Users/peony/Documents/wgh/test/vue3Admin/README.md#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E9%85%8D%E7%BD%AEenv>)。

#### 网站图标（favicon）
    
    
    <!-- index.html -->
    <link rel="icon" href="/favicon.ico" />

#### 网站描述（description）
    
    
    <!-- index.html -->
    <meta name="description" content="%VITE_APP_DESCRIPTION%" />

#### `全局`样式（style）
    
    
    <!-- index.html -->
    <style>
      /* 全局样式 */
    </style>

## 环境变量配置（.env）

.env文件是 Vite 项目的环境变量配置文件，用于在不同的开发、测试、生产环境中设置不同的配置。更多配置方式见官方文档[环境变量配置](<https://vitejs.dev/config/#env-variables>)。

#### 开发环境（.env.development）
    
    
    # .env.development
    VITE_APP_TITLE=Vue3Admin
    VITE_APP_DESCRIPTION=这是一个Vue3Admin项目

#### 生产环境（.env.production）
    
    
    # .env.production
    VITE_APP_TITLE=Vue3Admin
    VITE_APP_DESCRIPTION=这是一个Vue3Admin项目

## 应用入口文件`main.ts`配置

main.ts(路径:/src/main.ts) 是 Vue 3 + Vite 项目的应用入口文件，负责创建 Vue 应用实例、安装全局插件、挂载根组件。它和 index.html 分工明确：index.html 提供页面骨架和入口脚本引用，main.ts 则是真正的应用启动逻辑。

## 路由配置

文件路径:src/router/index.ts
    
    
    import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
    
    // 静态路由
    export const constantRouters: RouteRecordRaw[] = [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
      },
      {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/index.vue'),
      }
    ]
    
    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
      routes: constantRouters,
      // 刷新时，滚动条位置还原
      scrollBehavior: () => ({ left: 0, top: 0 }),
      // 路由守卫
      // beforeEach: (to, from, next) => {}
    })
    
    export default router

## home(首页)配置
    
    
    # src/views/Home.vue
    <template>
        <div>
            <h1>花花工作室</h1>
            <p>欢迎来到花花工作室！</p>
        </div>
        <div>
            <!-- 登录 -->
            <el-button type="primary" @click="handleLogin">登录</el-button>
        </div>
    </template>
    
    <script setup>
    import { useRouter } from 'vue-router';
    const router = useRouter();
    
    const handleLogin = () => {
        // 跳转到登录页面
        router.push('/login');
    };
    </script>

## login(登录页)配置
    
    
    # src/views/login/index.vue
    <template>
        <div>登录页面</div>
        <!-- 登录 -->
        <div>用户名：admin</div>
        <div>密码：123456</div>
        <!-- 注册 -->
        <el-button type="primary" @click="register">注册</el-button>
        <!-- 忘记密码 -->
        <el-button type="primary" @click="forgetPwd">忘记密码</el-button>
    </template>
    
    <script setup>
    import { useRouter } from 'vue-router';
    const router = useRouter();
    // 注册
    const register = () => {
        router.push('./components/Register.vue');
    }
    // 忘记密码
    const forgetPwd = () => {
        router.push('/ForgetPwd');
    }
    </script>

### register(注册页)配置
    
    
    # src/views/login/components/Register.vue
    <!-- 注册组件 -->
    <template>
        <div class="register-container">
            <h2>注册</h2>
            <form @submit.prevent="handleRegister">
                <div class="form-group">
                    <label for="username">用户名</label>
                    <input type="text" id="username" v-model="username" required />
                </div>
                <div class="form-group">
                    <label for="email">邮箱</label>
                    <input type="email" id="email" v-model="email" required />
                </div>
                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" id="password" v-model="password" required />
                </div>
                <button type="submit">注册</button>
            </form>
        </div>
    </template>
    
    <script setup>
    import { ref } from 'vue';
    
    const username = ref('');
    const email = ref('');
    const password = ref('');
    
    const handleRegister = () => {
        // 处理注册逻辑
    };
    </script>


---
> 原文链接: https://www.cnblogs.com/myflowers/p/23399187