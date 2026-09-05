---
title: "FastAPI"
type: entity
tags: [Python, Web框架, API, 高性能]
sources: [raw/01-articles/FastAPI 入门教程.md]
last_updated: 2026-06-29
---

## 定义
基于 Python 的现代 Web 框架，专为构建高性能 API 而设计，由西班牙开发者 Sebastián Ramírez 于 2018 年创建。GitHub 已斩获 80K+ Star，被微软、Netflix、滴滴等公司用于生产环境。

## 关键信息

### 技术定位"三高"
- **高开发效率**：相比传统框架代码量缩短 60%，开发周期从 6 周缩短至 2 周
- **高运行性能**：基于 [[ASGI]] 异步架构，性能接近 Go/Node.js
- **高类型安全**：[[Pydantic]] 在运行时自动校验，错误响应准确指出哪个字段失败

### 三引擎星型架构
1. **路由系统**：基于路径操作装饰器（`@app.get`、`@app.post`），路径参数较多时比 Flask 的 Werkzeug 路由性能提升 40%
2. **依赖注入系统**：通过 `Depends` 关键字实现服务依赖自动解析，底层采用函数装饰器模式 + `__wrapped__` 属性保留原函数
3. **数据验证引擎**：基于 [[Pydantic]] BaseModel，包含字段类型检查、约束条件验证、嵌套模型验证、额外属性检查

### 与其他框架对比

| 维度 | FastAPI | [[SpringBoot]] | Flask | Django |
|------|---------|----------------|-------|--------|
| 核心定位 | 高性能 API | 企业级全栈 | 轻量微框架 | 全栈框架 |
| 性能 | 极高（接近 Go） | 高 | 中等 | 中等 |
| 自动文档 | ✅ 原生 | 需 SpringDoc | ❌ | 部分 |
| 类型安全 | ✅ Pydantic | ✅ Java 强类型 | ⚠️ 弱 | ⚠️ 弱 |
| 异步支持 | ✅ async/await | ✅ WebFlux | ⚠️ 需扩展 | 部分 |
| 学习曲线 | 低 | 陡峭 | 低 | 中 |

类比：FastAPI 像跑车（轻快灵活适合冲刺），Spring Boot 像 SUV（稳重扎实适合复杂路况）。

### 性能数据
- TechEmpower 基准测试：同步模式 18,732 req/sec，异步模式 32,451 req/sec
- JSON 序列化达 Django 的 **8 倍**，接近 Go Gin 水平
- API 开发速度约为 Flask 的 **2-3 倍**
- 真实压测（1000 并发）：响应时间 45ms（50 分位）、吞吐 2400 次/秒、内存 180MB；vs Spring Boot 80ms、1800 次/秒

### 核心特性
- **自动 API 文档**：原生支持 Swagger UI (`/docs`) 和 ReDoc (`/redoc`)
- **Pydantic 强校验**：定义 BaseModel + Field 即可自动校验请求/响应
- **依赖注入**：适合权限校验、Token 校验、DB 会话管理等横切关注点
- **原生异步**：完全支持 `async/await`，I/O 密集场景表现极佳
- **生产级中间件**：内置 CORS、GZip、HTTPS 重定向、WebSocket

### 快速上手

```bash
# 安装
pip install fastapi uvicorn[standard]

# 启动
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

最小示例：
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    email: str

@app.post("/users")
async def create_user(user: UserCreate):
    return {"id": 1, **user.model_dump()}
```

### 优缺点

**优点**：
1. 极高开发效率（代码量 -60%、周期 6 周→2 周）
2. 卓越性能（Django 8 倍、接近 Go Gin）
3. 自动文档生成
4. 类型安全
5. 原生异步
6. 灵活依赖注入
7. 生产级中间件

**缺点**：
1. 生态不如 Django 完善（ORM、Admin 等）
2. Pydantic 学习成本
3. 高度依赖类型提示，代码量比 Flask 多
4. 部分组件需自行封装（全局异常、中间件体系）
5. 社区相对较新
6. CPU 密集型场景不如 Java（Spring Boot 凭 JIT 优化更稳定）

### 适用场景
- ✅ **AI 模型部署**：高并发 + 自动文档完美契合
- ✅ **微服务架构**：电商订单服务重构案例，开发周期 6 周→2 周、错误率 -72%、并发 2000+
- ✅ **数据处理 API**：查询、统计、导出
- ✅ **实时应用**：WebSocket 聊天、实时监控
- ✅ **快速原型**

不适合：大型企业级全栈应用（Django 更合适）、CPU 密集型计算（Spring Boot 更稳）、Java 技术栈团队。

### 真实选型对比（同业务 FastAPI vs Spring Boot 六个月观察）
- 开发：FastAPI 2 天跑起来 vs Spring Boot 还在战 Maven
- 性能：FastAPI 完胜
- **结论**：Java 同事最终赢——不是因为性能，而是因为**运维体系、监控告警、日志聚合、错误追踪等"非功能需求"** Spring Boot 生态更成熟

## 关联连接
- [[摘要-fastapi-入门教程]] — 来源
- [[Pydantic]] — 数据验证基石
- [[Uvicorn]] — 默认 ASGI 服务器
- [[ASGI]] — 异步规范
- [[SpringBoot]] — 对比框架
- [[Java]] — 替代语言生态
- [[async-await]] — 异步编程
- [[AIService]] — 核心应用场景
- [[microservices]] — 适用架构
- [[frontend-backend-separation]] — 前后端联调通过自动文档加速
