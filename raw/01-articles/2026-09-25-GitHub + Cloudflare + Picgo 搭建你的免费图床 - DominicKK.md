---
title: "GitHub + Cloudflare + Picgo 搭建你的免费图床 - DominicKK"
source: "博客园"
url: "https://www.cnblogs.com/dominickk/p/23120855"
date: "2026-09-25T06:39:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# GitHub + Cloudflare + Picgo 搭建你的免费图床 - DominicKK

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/dominickk/p/23120855  
> **抓取日期**: 2026-09-25  
> **相关性评分**: 0.6

## 教程简介

本教程会逐步指导你搭建一个**稳定、私有、免费** 的图床方案。

**使用工具** ：

  * GitHub私有仓库：提供免费存储空间

  * Cloudflare Workers：提供免费CDN加速和反代

  * PicGo（可选）：简化图片上传流程

  * Typora markdown编辑器（可选）：使用Typora内置集成的PicGo，简化图片上传流程，方便文档编写过程。




**适用场景** ：个人博客、小型网站、文档系统等。

## 准备工作

### 必需的工具

  * GitHub账号：👉[前往注册](<https://github.com/signup>)👈

  * Cloudflare账号：👉[前往注册](<https://dash.cloudflare.com/sign-up>)👈




### 可选的工具

  * PicGo：👉[前往下载](<https://picgo.app/download/>)👈

  * Typora markdown编辑器：👇前往使用免费版👇

<https://blog.dominickk.top/archives/hPPjiDwq>




## 配置步骤

### 1\. GitHub私有仓库

#### 创建私有仓库

  1. 登录GitHub，点击右上角的 "+" 按钮，选择 "New repository"创建新仓库  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844020-1726696191.png)

​

  2. 填写仓库信息  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143843703-1719769238.png)

​

  3. 点击最下面的​Create repository​即可完成。




#### 生成访问令牌

一定要生成一个可控权限的令牌，以保证仓库的隐私性和安全性，使用令牌才能上传和访问图片。

  1. 进入设置  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844739-888469668.png)

​

  2. 进入开发者设置  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844027-713201730.png)

​




以下方式二选一即可。

##### F**ine-grained token（权限更严，推荐）**

  1. 创建一个Fine-grained token  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844386-75923139.png)

​

  2. 设置token信息

     * name随意填写

     * Expiration：过期时间，建议 **No expiration** 永不过期，如果不放心，可以选择其他时长，缺点是需要定期重新配置token；

​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844212-1076000641.png)

​

     * Repository access：选择你的图床仓库，该token只会享有指定库的访问权限；

     * Permissions：选择权限，必选：

       * Contents:Read and write 仓库内容读写权限

       * Metadata:Read-only 仓库基本元信息读权限（会自动强制勾选）

​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844485-965239834.png)

​

  3. 复制token并保存到你自己的密码本，token内容是​`github_pat_xxxxxx`​，只可见这一次，页面刷新后不能再查看，一定要复制并保存到安全的地方，如果忘记、丢失或泄露了，点击后面的​Delete​删掉重建即可。  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844815-695881305.png)

​




##### Personal access token(classic)（权限更松，不推荐）

  1. 创建一个token  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844745-1341322663.png)

​

  2. 设置token信息  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844598-51808057.png)

​

     * Note：随意填写；

     * Expiration：过期时间，建议 **No expiration** 永不过期，如果不放心，可以选择其他时长，缺点是需要定期重新配置token；

     * Select scopes：选择权限范围，必选这两个：

       * repo - 完整仓库权限

       * write:packages - 写入包权限

  3. 点击最下面的​Generate token​即可完成配置

  4. 复制token并保存到你自己的密码本，token内容是​`ghp_xxxxxx`​，只可见这一次，页面刷新后不能再查看，一定要复制并保存到安全的地方，如果忘记、丢失或泄露了，点击后面的​Delete​删掉重建即可。  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143845138-516091222.png)

​




### 2\. Cloudflare Workers反代

#### 创建并部署Workers

  1. 登录并访问 👉[Cloudflare Dashboard](<https://dash.cloudflare.com/>)👈

  2. 进入 ​`Workers和Pages`​ ，创建一个应用程序  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844451-1033364910.png)

​

选择“从Hello World！开始”  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844056-989446669.png)

​

名称随意，点击​部署​即可  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844581-345932119.png)

​

  3. 点击​编辑代码​进入到编辑器  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143845011-420831951.png)

删掉原有的代码，粘贴以下代码👇，可以根据自己的喜好修改样式和文案
         
         let token = "";
         
         export default {
           async fetch(request, env) {
             const url = new URL(request.url);
         
             if (url.pathname !== '/') {
               let githubRawUrl = 'https://raw.githubusercontent.com';
         
               if (new RegExp(githubRawUrl, 'i').test(url.pathname)) {
                 githubRawUrl += url.pathname.split(githubRawUrl)[1];
               } else {
                 if (env.GH_NAME) {
                   githubRawUrl += '/' + env.GH_NAME;
                   if (env.GH_REPO) {
                     githubRawUrl += '/' + env.GH_REPO;
                     if (env.GH_BRANCH) githubRawUrl += '/' + env.GH_BRANCH;
                   }
                 }
                 githubRawUrl += url.pathname;
               }
         
               // Token 处理逻辑
               if (env.GH_TOKEN && env.TOKEN) {
                 if (env.TOKEN == url.searchParams.get('token')) {
                   token = env.GH_TOKEN || token;
                 } else {
                   token = url.searchParams.get('token') || token;
                 }
               } else {
                 token = url.searchParams.get('token') || env.GH_TOKEN || env.TOKEN || token;
               }
         
               const githubToken = token;
         
               if (!githubToken || githubToken == '') {
                 return new Response('🔑 啊哦，门钥匙丢去哪里了？', { status: 400 });
               }
         
               // 构建请求头
               const headers = new Headers();
               headers.append('Authorization', `token ${githubToken}`);
         
               // 发起请求
               const response = await fetch(githubRawUrl, { headers });
         
               // 检查请求是否成功
               if (response.ok) {
                 return new Response(response.body, {
                   status: response.status,
                   headers: response.headers
                 });
               } else {
                 const errorText = env.ERROR || '✨ 哎呀呀，文件被嗅嗅叼走啦！要不试试 “Accio Niffler (嗅嗅飞来)”？';
                 return new Response(errorText, { status: response.status });
               }
             } else {
               // 处理首页访问
               const envKey = env.URL302 ? 'URL302' : (env.URL ? 'URL' : null);
               if (envKey) {
                 const URLs = await ADD(env[envKey]);
                 const URL = URLs[Math.floor(Math.random() * URLs.length)];
                 return envKey === 'URL302'
                   ? Response.redirect(URL, 302)
                   : fetch(new Request(URL, request));
               }
         
               // 返回伪装页面
               return new Response(await nginx(), {
                 headers: {
                   'Content-Type': 'text/html; charset=UTF-8',
                 },
               });
             }
           }
         };
         
         // 伪装页面
         async function nginx() {
           const text = `
           <!DOCTYPE html>
           <html>
           <head>
           <title>Welcome to Platform 9¾ (not nginx)</title>
           <style>
             body {
               width: 35em;
               margin: 0 auto;
               font-family: 'Comic Sans MS', 'Georgia', Tahoma, Verdana, Arial, sans-serif;
               background-color: #2c3e50;
               color: #ecf0f1;
               text-align: center;
               padding-top: 80px;
               background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><text x="40" y="70" fill="%23f1c40f" font-size="20" opacity="0.55" transform="rotate(30,40,70)">🔑</text><text x="160" y="50" fill="%23f1c40f" font-size="16" opacity="0.5" transform="rotate(10,160,50)">✨</text><text x="220" y="120" fill="%23f1c40f" font-size="24" opacity="0.6" transform="rotate(350,220,120)">💼</text><text x="90" y="180" fill="%23f1c40f" font-size="22" opacity="0.5" transform="rotate(20,90,180)">🧹</text><text x="200" y="230" fill="%23f1c40f" font-size="18" opacity="0.7" transform="rotate(340,200,230)">🔮</text><text x="50" y="260" fill="%23f1c40f" font-size="26" opacity="0.55" transform="rotate(30,50,260)">🪄</text><text x="130" y="150" fill="%23f1c40f" font-size="20" opacity="0.6" transform="rotate(15,130,150)">🧙</text></svg>');
               background-repeat: repeat;
               background-size: 1000px 1300px;
             }
             h1,h2 {
               color: #f1c40f;
               text-shadow: 2px 2px #8e44ad;
             }
             a {
               color: #f39c12;
               text-decoration: none;
               font-weight: bold;
               background-color: #34495e;
               padding: 8px 16px;
               border-radius: 20px;
               display: inline-block;
               margin-top: 10px;
             }
             a:hover {
               background-color: #8e44ad;
               color: white;
               transform: scale(1.1);
             }
             .funny {
               font-size: 1.2em;
               margin-top: 30px;
               background-color: rgba(0,0,0,0.5);
               padding: 20px;
               border-radius: 15px;
               border: 2px solid #f1c40f;
             }
             small {
               color: #bdc3c7;
             }
           </style>
           </head>
           <body>
           <h1>🧹 欢迎来到 Platform 9¾ </h1>
           <h2>—— 不是 nginx！</h2>
           <p>你似乎误入了魔法世界的候车大厅，这里可不是麻瓜的 nginx 服务器！</p>
           <div class="funny">
             <p>🔮 <strong>真正的魔法入口在这里</strong> </p>
             <p><a href="https://www.dominickk.top/" target="_blank">🪄 通过飞路网前往 Dominic 的魔法世界</a></p>
             <p>或者… 你可以继续等待霍格沃茨特快，但文件可不会自己出现～</p>
             <p>（温馨提示：如果遇到摄魂怪，请大声念出 “Expecto Patronum! (呼神护卫)”！）</p>
           </div>
           <p><small>（开玩笑的，如果你在找文件，那它可能被嗅嗅藏进了纽特的小皮箱里 💼）</small></p>
           </body>
           </html>
           `;
           return text;
         }
         
         // 处理环境变量
         async function ADD(envadd) {
           var addtext = envadd.replace(/[\t|"'\r\n]+/g, ',').replace(/,+/g, ',');
           if (addtext.charAt(0) == ',') addtext = addtext.slice(1);
           if (addtext.charAt(addtext.length - 1) == ',') addtext = addtext.slice(0, addtext.length - 1);
           const add = addtext.split(',');
           return add;
         }
         
         
         

​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844873-1512718655.png)

​

  4. 尝试访问Cloudflare提供的域名，如果觉得慢，且正好有自己的域名，可以使用Cloudflare DNS代理自己域名，然后添加到Workers的域中（可选步骤）  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844599-1279967563.png)

​

  5. 配置环境变量  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844366-1951004884.png)

​

变量名 | 示例值 | 必填 | 说明  
---|---|---|---  
​`GH_TOKEN`​ | ​`github_pat_xxxxxx`​ ​`ghp_xxxxxxxxxxxx`​ | ✅ | GitHub Fine-grained token 或 Personal Access Token  
​`GH_NAME`​ | ​`Dominic-kk`​ | ✅ | GitHub 用户名  
​`GH_REPO`​ | ​`picbed`​ | ✅ | GitHub 仓库名  
​`GH_BRANCH`​ | ​`main`​ | ✅ | 仓库分支名  
  
添加完成后再次点击​部署​




### 3\. 配置PicGo（可选）

仅展示windows环境下PicGo图形化程序的配置步骤。

添加一个GitHub图床，配置信息按照前面步骤里获取到的填写：  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844388-603555095.png)

​

设定存储路径表示图片在仓库内的二级路径，留空则上传到根目录，推荐给不同上传渠道起不同的名字，如果不知道是什么，可以自己设置一个看看效果。

推荐给PicGo安装一个插件​`rename-file`​，用于给上传的图片自动格式化命名，避免文件名冲突，也让存储桶更好看一点。

在插件这里搜索安装，文件格式可以自定义，参考我的配置：​`{y}/{m}/{d}{h}{i}-{rand:3}`​

​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844194-1645777743.png)

​

测试功能：在仪表盘选择GitHub图床，链接格式选择url类型，上传文件成功后，会自动复制链接，粘贴到浏览器地址栏后即可直接看到图片。  
​

![](https://img2024.cnblogs.com/blog/2469043/202609/2469043-20260925143844313-1780606908.png)

​

### 4\. 配置Typora markdown编辑器（可选）

👇参考这篇文档👇

<https://blog.dominickk.top/archives/fY6u3Aoc>

## 本文参考文档 & 鸣谢🥤

<https://cactusli.net/tutorials/tools/network/Github-Cloudflare-image-hosting-setup.html>


---
> 原文链接: https://www.cnblogs.com/dominickk/p/23120855