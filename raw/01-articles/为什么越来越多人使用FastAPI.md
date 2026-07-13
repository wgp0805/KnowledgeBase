---
title: "为什么越来越多人使用FastAPI?"
source: "https://mp.weixin.qq.com/s/ECNGeoDXAcDTXZ05lUEh3g"
---
苏三 苏三说技术 *2026年7月12日 09:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

> Java开发者也能看懂的Python高性能框架指南

最近这几年，Python在AI和数据处理领域如日中天，很多Java开发者也开始接触Python生态。

在Python的众多Web框架中， **FastAPI** 的崛起速度让人瞠目结舌。

GitHub上，FastAPI已经斩获了 **80K+ Star** ，增长速度超过了Flask和Django，成为Python生态中增长最快的Web框架。

微软、Netflix、滴滴等公司都在生产环境中使用它。

很多小伙伴问我：“三哥，我一个写Java的，为什么要学FastAPI？”

我的回答很简单： **如果你需要快速搭建一个高性能的API服务，尤其是涉及AI模型部署、数据处理或微服务场景，FastAPI可能是目前最好的选择之一。**

今天这篇文章，我就从Java开发者的视角出发，用你熟悉的对比方式，把FastAPI从头到尾讲清楚。

图文并茂，代码可复制，跟着做就行。

希望对你会有所帮助。

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8FastAPI/120fc0032d790118e773ec1a67b88378_MD5.webp)

## 一、FastAPI到底是什么？

### 1.1 一句话说清

FastAPI是一个基于Python的现代Web框架，专为 **构建高性能API** 而设计。

它由西班牙开发者Sebastián Ramírez于2018年创建，核心设计目标是解决传统Python Web框架在性能、开发效率和类型安全方面的痛点。

它的技术定位可以概括为“三高”： **高开发效率、高运行性能、高类型安全** 。

### 1.2 跟Java开发者熟悉的框架对比

为了让Java开发者快速理解FastAPI的定位，我用一个表格来对比：

| 对比维度 | FastAPI (Python) | Spring Boot (Java) | Flask (Python) |
| --- | --- | --- | --- |
| **核心定位** | 高性能API框架 | 企业级全栈框架 | 轻量级微框架 |
| **性能** | 极高（接近Go/ [Node.js）](http://node.js\)/) | 高 | 中等 |
| **开发速度** | 极快 | 较慢 | 快 |
| **自动文档** | ✅ 原生支持 | 需SpringDoc等集成 | ❌ 需第三方 |
| **类型安全** | ✅ Pydantic强校验 | ✅ Java强类型 | ⚠️ 较弱 |
| **异步支持** | ✅ 原生async/await | ✅ Spring WebFlux | ⚠️ 需扩展 |
| **学习曲线** | 低 | 陡峭 | 低 |
| **适用场景** | API服务、微服务、AI部署 | 大型企业应用 | 简单Web应用 |

FastAPI和Spring Boot的关系，有点像 **跑车和SUV** ——跑车轻快灵活，适合高速冲刺；SUV稳重扎实，适合长途跋涉和复杂路况。

各有各的好，关键看你要干什么。

### 1.3 FastAPI到底能做什么？

FastAPI官方文档总结了它的核心能力：

**高性能** ：基于Starlette（异步Web框架）和Pydantic（高性能数据校验），在Python Web框架中属于性能天花板。

**自动生成API文档** ：无需编写文档，自动生成Swagger UI（ `/docs` ）和ReDoc（ `/redoc` ）。

**使用Python类型提示自动校验参数** ：自动请求参数校验、自动响应模型校验、IDE自动补全体验极佳。

**原生异步支持** ：完全支持 `async/await` ，适合高并发I/O场景。

**依赖注入系统** ：支持权限校验、Token校验、DB会话管理、统一行为注入。

**易维护** ：类型提示 + 自动补全，适合微服务架构。

## 二、FastAPI为什么这么快？

> 有些小伙伴可能会问：同样是Python写的，FastAPI凭什么比Flask快那么多？

答案是三个字： **ASGI** 。

### 2.1 WSGI vs ASGI：一场革命

传统的Python Web框架（如Flask、Django）基于 **WSGI** （Web Server Gateway Interface）规范。

WSGI是 **同步** 的——每个请求独占一个线程，直到处理完才能释放。这就好比一个餐厅里，每个服务员一次只能服务一桌客人，其他客人只能干等着。

而FastAPI基于 **ASGI** （Asynchronous Server Gateway Interface）规范。

ASGI是 **异步非阻塞** 的——每个请求在事件循环中被调度，而不是独占线程资源。

这就像同一个服务员可以同时服务多桌客人——点完一桌的菜，趁厨房做菜的时间去给另一桌点单，效率自然高出一大截。

这就是为什么FastAPI能够轻松处理 **数千个并发连接** 。

### 2.2 三引擎驱动架构

FastAPI的架构可以概括为“星型模型”，由三个核心引擎驱动：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8FastAPI/891d03b89be0a89084853263ad961576_MD5.png)

**① 路由系统** ：基于路径操作装饰器（ `@             app.get           ` 、 `@             app.post           ` ）实现RESTful路由，支持路径参数和查询参数的自动解析。其路径匹配算法采用正则表达式优化，在路径参数较多时比Flask的Werkzeug路由\*\*性能提升达40%\*\*。

**② 依赖注入系统** ：通过 `Depends` 关键字实现服务依赖的自动解析，特别适合数据库连接等资源的统一管理。其底层实现采用函数装饰器模式，通过 `__wrapped__` 属性保留原始函数，在运行时动态注入依赖项。

**③ 数据验证引擎** ：FastAPI的数据验证基于Pydantic的 `BaseModel` ，验证流程包含字段类型检查、约束条件验证、嵌套模型验证和额外属性检查。

### 2.3 Pydantic验证流程

当一个请求到达FastAPI时，数据验证的流程是这样的：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8FastAPI/736b7302e7f96f782607b959f3ba31a7_MD5.png)

如果在请求中传入非字符串类型的 `username` ，框架会立即返回422错误，并明确指出哪个字段失败及原因。

这种“在门口就把不合格的请求拦住”的设计，大大减少了业务代码里的防御性判断。

### 2.4 性能数据

在TechEmpower基准测试中，FastAPI在JSON序列化场景下达到 **18,732 req/sec（同步模式）和32,451 req/sec（异步模式）** 。

JSON序列化性能达到Django的 **8倍** ，接近Go语言框架Gin的水平。

对于API开发来说，FastAPI的速度大约是Flask的 **2-3倍** 。

在I/O密集型场景下，这个差距会更加明显。

## 三、环境搭建：5分钟跑起来

### 3.1 安装Python环境

建议使用Python 3.9+版本：

```
# 使用pyenv管理Python版本（推荐）
brew install pyenv
pyenv install 3.11.5
pyenv global 3.11.5

# 或直接使用系统Python
python3 --version
```

### 3.2 创建项目并安装依赖

```
# 创建项目目录
mkdir fastapi-demo
cd fastapi-demo

# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装FastAPI和Uvicorn
pip install fastapi uvicorn[standard]
```

Uvicorn是一个ASGI服务器，相当于Java中的Tomcat或Netty。

### 3.3 编写第一个API

创建 `              main.py            ` 文件：

```
from fastapi import FastAPI

# 创建应用实例
app = FastAPI(title="我的第一个FastAPI应用", version="1.0.0")

# 定义路由
@
            app.get("/")
          
async def root():
    return {"message": "Hello World"}

@
            app.get("/hello/{name}")
          
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
```

### 3.4 启动服务

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

参数说明：

- `main:app` —— `              main.py            ` 文件中的 `app` 实例
- `--reload` —— 开发模式下自动重启（生产环境不要用）
- `--host` —— 监听地址
- `--port` —— 端口号

启动后，访问以下地址：

- **API服务** ：http://localhost:8000
- **Swagger文档** ：http://localhost:8000/docs
- **ReDoc文档** ：http://localhost:8000/redoc

访问 `/docs` 你会看到一份交互式的API文档—— **你什么都没写，文档已经自动生成了** 。这就是FastAPI最让人惊艳的特性之一。

## 四、核心概念实战

### 4.1 路径参数与查询参数

```
from fastapi import FastAPI

app = FastAPI()

# 路径参数：从URL路径中提取
@
            app.get("/users/{user_id}")
          
asyncdef get_user(user_id: int):# 自动类型转换 + 校验
    return {"user_id": user_id, "name": f"User_{user_id}"}

# 查询参数：从URL问号后面提取
@
            app.get("/items")
          
asyncdef list_items(
    skip: int = 0,      # 默认值
    limit: int = 10,    # 默认值
    category: str | None = None  # 可选参数
):
    return {"skip": skip, "limit": limit, "category": category}
```

**代码解读** ：

- 路径参数 `{user_id}` 会从URL中提取， `user_id: int` 会自动进行类型转换和校验——传入非数字会返回422错误
- 查询参数从`?skip=0&limit=10` 中提取，有默认值的参数是可选的
- 类型注解让IDE能提供自动补全，也让框架能自动校验

访问示例：

- `GET /users/123` → `{"user_id": 123, "name": "User_123"}`
- `GET /items?skip=5&limit=20&category=books`

### 4.2 请求体与Pydantic模型

这是FastAPI最核心的能力之一——用Pydantic模型定义请求和响应的数据结构。

```
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

app = FastAPI()

# 定义请求体模型
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="用户名")
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=8, description="密码")
    age: Optional[int] = Field(None, ge=0, le=150, description="年龄")
    tags: list[str] = []

# 定义响应体模型
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    age: Optional[int]
    created_at: datetime

@
            app.post("/users",
           response_model=UserResponse)
asyncdef create_user(user: UserCreate):
    # 业务逻辑：创建用户
    return UserResponse(
        id=1,
        username=
            user.username,
          
        email=
            user.email,
          
        age=
            user.age,
          
        created_at=
            datetime.now()
          
    )
```

**代码解读** ：

- `UserCreate` 定义了请求体的结构， `Field` 提供了额外的校验规则（最小长度、最大长度、取值范围等）
- `EmailStr` 会自动校验邮箱格式
- `response_model=UserResponse` 指定了响应的数据结构，框架会自动过滤掉不在模型中的字段
- 如果请求缺少必填字段或字段类型不对，FastAPI会自动返回422错误并说明原因

这就是“ **声明式编程** ”的魅力——你只需要声明“我要什么”，框架帮你处理“怎么校验”。

### 4.3 依赖注入

FastAPI的依赖注入系统非常灵活，适合处理权限校验、数据库会话管理等横切关注点。

```
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# 定义一个依赖：验证Token
asyncdef verify_token(authorization: str = Header(...)):
    """从请求头中提取并验证Token"""
    ifnot 
            authorization.startswith(
          "Bearer "):
        raise HTTPException(status_code=401, detail="无效的认证格式")
    token = 
            authorization.replace(
          "Bearer ", "")
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="无效的Token")
    return {"user_id": 1, "username": "admin"}

# 使用依赖
@
            app.get("/protected")
          
asyncdef protected_route(user: dict = Depends(verify_token)):
    return {"message": f"欢迎, {user['username']}!", "user": user}
```

**代码解读** ：

- `verify_token` 是一个依赖函数，从请求头中提取 `Authorization` 并验证
- `Depends(verify_token)` 将依赖注入到路由函数中
- 如果验证失败，自动返回401错误
- 验证通过后，返回的用户信息会作为 `user` 参数传入路由函数

这种设计让 **认证逻辑和业务逻辑完全分离** ，代码更清晰、更可测试。

### 4.4 异步支持

FastAPI原生支持 `async/await` ，这是它高性能的关键。

```
import asyncio
from fastapi import FastAPI

app = FastAPI()

# 同步函数（适用于CPU密集型操作）
@
            app.get("/sync")
          
def sync_endpoint():
    # 同步操作，会阻塞线程
    return {"result": "done"}

# 异步函数（适用于I/O密集型操作）
@
            app.get("/async")
          
asyncdef async_endpoint():
    # 模拟I/O操作：数据库查询、外部API调用等
    await 
            asyncio.sleep(
          1)
    # 在等待期间，事件循环可以处理其他请求
    return {"result": "done after 1 second"}

# 混合使用：在异步函数中调用同步代码
@
            app.get("/mixed")
          
asyncdef mixed_endpoint():
    # 使用 run_in_executor 将同步代码放到线程池执行
    result = await 
            asyncio.to_thread(sync_heavy_work)
          
    return {"result": result}

def sync_heavy_work():
    # CPU密集型操作
    return sum(range(1000000))
```

**代码解读** ：

- 异步函数用 `async def` 定义，在等待I/O时释放线程资源
- `await              asyncio.sleep(1)           ` 模拟I/O等待，期间事件循环可以处理其他请求
- 对于CPU密集型操作，使用 `              asyncio.to_thread            ` 放到线程池执行，避免阻塞事件循环

## 五、数据库集成

### 5.1 异步SQLAlchemy集成

```
from fastapi import FastAPI, Depends
from 
            sqlalchemy.ext.asyncio
           import create_async_engine, AsyncSession, async_sessionmaker
from 
            sqlalchemy.orm
           import declarative_base, Mapped, mapped_column
from sqlalchemy import select

# 数据库配置
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

# 定义模型
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

# 依赖：获取数据库会话
asyncdef get_db():
    asyncwith AsyncSessionLocal() as session:
        yield session

app = FastAPI()

@
            app.get("/users")
          
asyncdef get_users(db: AsyncSession = Depends(get_db)):
    result = await 
            db.execute(select(User))
          
    users = 
            result.scalars().all()
          
    return [{"id": 
            u.id,
           "username": 
            u.username,
           "email": 
            u.email}
           for u in users]
```

**代码解读** ：

- `create_async_engine` 创建异步数据库引擎
- `AsyncSessionLocal` 是异步会话工厂
- `get_db` 是一个依赖，每个请求创建一个数据库会话，请求结束后自动关闭
- 所有数据库操作都是异步的，不会阻塞事件循环

## 六、统一响应与异常处理

在生产环境中，统一的响应格式和异常处理是必不可少的。

### 6.1 统一响应模型

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    """统一API响应格式"""
    code: int = 200
    msg: str = "success"
    data: Optional[T] = None

app = FastAPI()

@
            app.get("/users/{user_id}",
           response_model=ApiResponse)
asyncdef get_user(user_id: int):
    if user_id <= 0:
        return ApiResponse(code=400, msg="用户ID必须大于0")
    # 模拟查询
    user = {"id": user_id, "name": f"User_{user_id}"}
    return ApiResponse(data=user)
```

### 6.2 全局异常处理

```
from fastapi import FastAPI, Request
from 
            fastapi.responses
           import JSONResponse

app = FastAPI()

@
            app.exception_handler(HTTPException)
          
asyncdef http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=
            exc.status_code,
          
        content={"code": 
            exc.status_code,
           "msg": 
            exc.detail,
           "data": None}
    )

@
            app.exception_handler(Exception)
          
asyncdef general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"code": 500, "msg": "服务器内部错误", "data": None}
    )
```

有了全局异常处理，任何未捕获的异常都会被统一格式化为规范的响应结构，前端对接时再也不用猜“这个接口返回的格式是什么”了。

## 七、中间件

中间件可以在请求进入路由之前或响应返回之前进行统一处理。

```
from fastapi import FastAPI, Request
import time

app = FastAPI()

# 日志中间件：记录每个请求的耗时
@
            app.middleware("http")
          
asyncdef log_requests(request: Request, call_next):
    start_time = 
            time.time()
          
    
    # 记录请求信息
    print(f"收到请求: {
            request.method}
           {
            request.url.path}
          ")
    
    # 继续处理请求
    response = await call_next(request)
    
    # 记录响应信息
    process_time = 
            time.time()
           - start_time
    print(f"请求完成: {process_time:.4f}秒")
    
    # 在响应头中添加处理时间
    
            response.headers[
          "X-Process-Time"] = str(process_time)
    return response
```

## 八、自动文档：写代码=写文档

FastAPI最让人惊艳的特性之一，就是 **自动生成API文档** 。

你不需要写任何额外的文档代码，FastAPI会根据你的路由定义、Pydantic模型和类型注解，自动生成两份文档：

- **Swagger UI** （ `/docs` ）：交互式文档，可以在线调试API
- **ReDoc** （ `/redoc` ）：更美观的静态文档
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="电商API",
    description="这是一个电商平台的API文档",
    version="1.0.0",
    contact={"name": "技术团队", "email": "dev@
            example.com"
          }
)

class Product(BaseModel):
    name: str
    price: float
    stock: int

@
            app.post("/products",
           
          summary="创建商品",
          description="创建一个新的商品，需要提供名称、价格和库存",
          response_description="创建成功的商品信息")
asyncdef create_product(product: Product):
    """创建商品接口"""
    return {"id": 1, **
            product.model_dump()}
```

启动服务后访问 `/docs` ，你会看到一份完整的、可交互的API文档—— **参数说明、请求示例、响应示例全部自动生成** 。

前后端联调时，后端把服务地址发给前端，前端打开 `/docs` 就能看到所有接口的详细信息，还能在线测试。

这种体验，用过一次就再也回不去了。

## 九、优缺点

### 优点

**1\. 极高的开发效率** ：通过Python类型注解自动生成API文档，无需手动编写Swagger配置。定义一个用户注册接口，代码量较传统框架缩短 **60% **。在真实项目中，开发周期可以从6周缩短至** 2周** 。

**2\. 卓越的性能** ：基于ASGI异步架构，在TechEmpower基准测试中JSON序列化性能达到Django的 **8倍** ，接近Go语言框架Gin的水平。

**3\. 自动文档生成** ：写代码的同时文档自动生成，前后端联调效率大幅提升。

**4\. 类型安全** ：通过Pydantic模型在运行时自动检查数据类型，错误响应会准确指出哪个字段失败及原因。

**5\. 原生异步支持** ：天然支持 `async/await` ，非常适合I/O密集型工作负载（API调用、数据库查询、文件操作）。

**6\. 依赖注入系统** ：非常灵活，支持权限校验、Token校验、DB会话管理等。

**7\. 生产级特性** ：内置CORS、GZip、HTTPS重定向等中间件，支持WebSocket实时通信。

### 缺点

**1\. 生态不如Django完善** ：ORM、Admin等功能不如Django完整。

**2\. Pydantic学习成本** ：初学者需要适应Model模式。

**3\. 高度依赖类型提示** ：代码量相比Flask会多一些。

**4\. 部分组件需自行封装** ：如全局异常、中间件体系等。

**5\. 社区相对较新** ：虽然增长迅速，但相比Django和Flask，在某些特定场景下可能缺乏足够的支持和资源。

**6\. CPU密集型场景不如Java** ：在CPU密集型场景下，Spring Boot（Java）凭借JIT优化和线程池优势，性能更稳定。

## 十、一张图看懂适用场景

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8FastAPI/6af2f348e21b70c0dc5c5801141a0445_MD5.png)

### 最佳使用场景

**AI模型部署** ：机器学习模型要对外提供服务，FastAPI的高并发+自动文档两个特性完美契合。某AI公司使用FastAPI部署模型预测服务，开发周期大幅缩短。

**微服务架构** ：某电商平台使用FastAPI重构订单服务后，开发周期从6周缩短至2周，错误率下降72%，支持每秒2000+的并发请求。

**数据处理API** ：需要对外提供数据查询、统计、导出等接口的场景。

**实时应用** ：WebSocket聊天、实时监控等需要双向通信的场景。

**快速原型** ：需要快速验证想法、展示Demo的场景。

### 不太适合的场景

**大型企业级全栈应用** ：如果需要强大的Admin后台、完善的ORM、内置的用户认证系统，Django可能更合适。

**CPU密集型计算** ：复杂算法、大数据处理等场景，Java（Spring Boot）凭借JIT优化性能更稳定。

**已有Java技术栈的团队** ：如果团队全是Java开发者，引入Python需要额外的学习成本和运维成本。

## 十一、和Spring Boot的真实对比

一位开发者做了一个真实的实验：同一个业务服务，用FastAPI和Spring Boot各写一遍，同时上线跑六个月。

**开发阶段** ：FastAPI只用了 **两天** 就把服务跑起来了，而Spring Boot那边还在跟Maven依赖作斗争。几行代码就搞定了自动参数校验、自动生成文档。

**压测阶段（1000并发用户）** ：

- FastAPI：响应时间50分位45ms，吞吐量2400次/秒，内存占用180MB
- Spring Boot：响应时间50分位80ms，吞吐量1800次/秒

FastAPI在开发速度和首轮性能上全面领先。

但最终结果是 **写Java的同事赢了** ——不是因为性能，而是因为 **运维体系、监控告警、日志聚合、错误追踪这些“非功能需求”** ，Spring Boot的生态更成熟。

这个实验告诉我们： **技术选型不能只看开发速度和性能，还要看整个团队的技术栈、运维体系和长期维护成本。**

## 十二、写在最后

FastAPI不是一个要“取代”Spring Boot的框架，而是一个在 **特定场景下** 能让你事半功倍的工具。

**如果你是Java开发者** ，遇到以下情况时，可以考虑把FastAPI加入你的技术工具箱：

- 需要快速部署一个AI模型推理服务
- 需要搭建一个高性能的数据API
- 需要快速验证一个产品原型
- 团队中已经有Python能力

**如果你是完全的Python新手** ，FastAPI可能是最好的入门框架之一——语法简洁、文档优秀、社区活跃，而且能让你快速看到成果。

技术选型没有银弹。

FastAPI在API开发、微服务、AI部署等场景下表现惊艳，但在大型企业级全栈应用、CPU密集型计算等场景下，Spring Boot依然是更稳妥的选择。

> **我的建议是** ：花一个周末把FastAPI跑一遍，写一个完整的CRUD服务。感受一下“写代码=写文档”的体验，体会一下“类型注解自动校验”的便利。然后根据你的实际项目需求，决定是否引入生产环境。

毕竟， **多一个趁手的工具，就多一条解决问题的路** 。

**开源地址** ：

- **FastAPI** ： [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi) （80K+ Star）
- **官方文档** ： [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

我的企业智能知识库系统python后端中就用到了FastAPI，感兴趣的小伙伴，可以加入星球学习一下。