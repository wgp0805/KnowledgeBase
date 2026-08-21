---
title: "装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux"
source: "博客园"
url: "https://www.cnblogs.com/myvin/p/22225871"
date: "2026-08-20T11:11:00Z"
score: 0.8
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 装闭 RenoPit 源码解析（14）：Demo模式、健康检查与Docker部署 - fthux

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/myvin/p/22225871  
> **抓取日期**: 2026-08-20  
> **相关性评分**: 0.8

![1785883049455](https://img2024.cnblogs.com/blog/779193/202608/779193-20260804233953925-183821980.png)

前面的文章已经走完装修素材到 AI 报告的业务链，最后还需要解释应用如何演示、部署和判断依赖是否可用。装闭 RenoPit 的完整运行配置与诊断代码都已开源在 [fthux/RenoPit](<https://github.com/fthux/RenoPit>)。

## 一、Demo 模式如何脱离后端运行

前端入口 `main.tsx` 在创建 React 根节点前检查 `VITE_DEMO_MODE`。值为 `true` 或 `1` 时，动态导入 `demo/mockApi.ts` 并调用 `enableMockApi()`。

它保存原始 `window.fetch`，再替换为包装函数：
    
    
    window.fetch = async (input, init) => {
      for (const handler of mockHandlers) {
        const response = handler(url, init)
        if (response) {
          await new Promise((resolve) => setTimeout(resolve, 200))
          return response
        }
      }
      return originalFetch(input, init)
    }
    

每次请求先尝试匹配 Mock Handler，命中后等待 200 毫秒模拟网络延迟；未命中的外部请求继续交给真实 `fetch`，例如首页读取 GitHub Star 数量。

## 二、Mock API 如何复用真实页面

`normalizePath()` 先去除查询参数，再兼容 `/api` 和完整 `/api/v1` 地址。`matchPath()` 支持 `:id` 动态参数，因此一个处理器可以匹配任意 Demo 项目 ID。

内置处理器覆盖项目列表、项目详情、文件、图片、分析结果和状态接口，并从 `demoData.ts` 返回固定数据。创建、复制、删除和启动分析等写操作返回 400，提示用户部署完整后端。

页面组件本身没有 Demo 专用副本。`ProjectsPage`、`ProjectPage` 和 `AnalysisPage` 仍然调用原来的 `/api`，只是请求在浏览器里被拦截。PDF 下载是一个例外：报告页在 Demo 模式下直接读取打包进前端的示例 PDF。

## 三、健康检查分成三组

后端 `/health/data` 调用 `run_all_checks()`，依次执行八项检查，并分成三组：

分组 | 检查项 | 对总状态的影响  
---|---|---  
核心依赖 | PostgreSQL、Redis、文件系统 | 错误时 `unhealthy`  
业务依赖 | LLM、Celery、应用数据 | 错误或警告时 `degraded`  
信息检查 | Python 运行时、外部网络 | 只展示信息  
  
![health](https://img2024.cnblogs.com/blog/779193/202608/779193-20260804234055935-720684265.png)

数据库检查执行 `SELECT 1` 并读取连接池状态；Redis 检查执行 `PING` 并获取内存信息；文件系统检查验证上传和报告目录可写、临时文件可读写以及磁盘剩余空间。

LLM 检查先测试目标主机 TCP 连接，再请求模型列表并确认 `LLM_MODEL_NAME` 是否存在。Celery 检查统计在线 Worker 和 Redis 队列深度。应用数据检查确认 `pitfalls.json`、中文字体和必要环境变量存在。

运行时检查返回 Python 版本、进程内存、线程、文件描述符和 GC 统计；网络检查单独验证 LLM 地址的 DNS 与 TLS。

## 四、健康面板如何渲染

`health.py` 同时提供 JSON 接口和 HTML 仪表盘。仪表盘在浏览器端请求 `/health/data`，把检查结果分组渲染成表格，并显示延迟和 `extra` 诊断字段。

总体状态由核心依赖优先决定：任一核心项为 error 时直接 `unhealthy`；核心正常但业务依赖出现 error 或 warning 时为 `degraded`；否则为 `healthy`。

FastAPI 还提供自定义 Swagger 和 ReDoc 页面，用同一份 `/openapi.json` 展示接口结构。

![redoc](https://img2024.cnblogs.com/blog/779193/202608/779193-20260804234111126-460981601.png)

## 五、Docker Compose 如何启动依赖

Compose 定义 PostgreSQL、Redis、FastAPI、Celery Worker 和前端五个服务。数据库与 Redis 都有容器健康检查，backend 和 worker 通过 `depends_on.condition: service_healthy` 等待核心依赖准备完成。

三个命名卷分别保存：

  * `postgres_data`：数据库文件；
  * `uploads`：项目图片和文档；
  * `reports`：生成报告。



backend 与 worker 挂载相同的上传和报告卷，因此 FastAPI 保存的文件可以被 Celery 读取，Worker 生成的内容也能被 API 返回。

## 六、开发代理与生产代理

开发环境中，Vite 在 5173 端口启动，并把 `/api` 代理到 `localhost:8000`。生产镜像由 Nginx 提供构建后的 React 静态文件，对普通路径使用 `try_files ... /index.html` 支持前端路由刷新。

Nginx 将 `/api/` 转发到 Compose 网络中的 `backend:8000`，同时传递客户端地址和协议头。针对 SSE，它关闭代理缓冲、启用分块传输并把读取超时设为一小时。

浏览器始终只访问前端域名下的 `/api`，开发和生产的差异由代理层吸收，React 页面无需维护两套后端地址。

## 七、运行体系小结

RenoPit 的运行层包含三条互补路径：Demo 模式用内置数据展示完整前端；健康检查持续验证数据库、队列、LLM 和文件系统；Docker Compose 与 Nginx 则把真实前端、API、Worker 和持久化依赖连接起来。

至此，14 篇文章已经覆盖从入口、数据模型、上传、异步任务、Prompt、LLM、文档核查到网页和 PDF 报告的完整源码链。项目的全部代码、部署文件和后续更新都可以继续在 [fthux/RenoPit](<https://github.com/fthux/RenoPit>) 中查看。


---
> 原文链接: https://www.cnblogs.com/myvin/p/22225871