---
title: "为什么越来越多人用FastMCP？"
source: "https://mp.weixin.qq.com/s/pSeTZPMZ1s3HYA5hYjdr9Q"
---
苏三 苏三说技术 *2026年8月20日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

你知道吗？

现在市面上超过 **70%** 的 MCP 服务器，都是用同一个框架构建的。

这个数字不是某个媒体的估算，而是项目官方公布的数据。

一个框架能占据一个新兴技术领域七成以上的份额，这已经不是在“参与竞争”，而是在 **定义标准** 。

它就是 **FastMCP** 。

最近这段时间，MCP 协议本身已经很火了。

但很多人可能还没意识到，真正让 MCP 从“协议文档”变成“生产工具”的，是 FastMCP 这个框架。

它正在悄悄成为 AI Agent 接入外部工具的“默认基础设施”。

今天这篇文章，我就把 FastMCP 为什么越来越多人用的原因，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、FastMCP 到底是什么？

在聊 FastMCP 之前，我们先花 30 秒搞清楚 MCP 是什么。

**MCP（Model Context Protocol，模型上下文协议）** 是一个开放标准，它定义了 AI 模型如何与外部工具、数据源和服务进行标准化通信。

简单说，MCP 就是 **AI 的“万能遥控器”** ——让 AI 能够调用计算器、查天气、操作数据库、发邮件……

把 AI 从“只能聊天”变成“能干活”。

而 **FastMCP 是一个建立在 MCP 协议之上的 Python 框架** 。

它做了一件事： **把 MCP 协议复杂的底层细节，封装成 Python 开发者最熟悉的装饰器 + 类型提示** 。

**一句话说清：MCP 协议定义了“做什么”，FastMCP 解决了“怎么做”** 。

MCP 协议定义了标准，而 FastMCP 让开发者能用几行代码就实现这个标准。

它的口号是： **“用 Pythonic 的方式构建 MCP 应用”** 。从原型到生产，一个框架全搞定。

## 二、一张图看懂 FastMCP 的定位

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8FastMCP%EF%BC%9F/9a273d5aca1a24ef60facabdb1ef7a2b_MD5.jpg)

FastMCP 处在 **MCP 协议和具体工具之间** ，负责把协议标准翻译成开发者能直接用的 API。

## 三、为什么越来越多人用 FastMCP？

### 3.1 原因一：70% 的市场份额

它不是“一个选择”，是“默认答案”。

目前，各种版本的 FastMCP 为 **所有语言中 70% 的 MCP 服务器提供支持** 。

这个比例意味着，你在 GitHub 上看到的大部分 MCP 服务器项目，底层用的都是 FastMCP。

而 FastMCP 本身 **每天被下载一百万次** 。

作为一个 Python 库，这个下载量已经进入了“基础设施级”的范畴。

更有说服力的是数字对比：在 GitHub 上，MCP 官方 SDK 有 **405 Star** ，而 FastMCP 有 **25.5k Star** 。

**差距超过 60 倍。**

当社区用 Star 投票投出 60 倍的差距时，这说明它已经不只是一个“好用的工具”，而是整个生态的 **事实标准** 。

### 3.2 原因二：开发效率质的飞跃

MCP 协议本身是一个标准，而不是一个开发框架。直接基于原始协议开发，意味着你要手动处理：

- JSON-RPC 消息的序列化与反序列化
- 工具 Schema 的手动定义
- 错误处理机制的重复实现
- 资源管理的复杂性
- 传输协商、认证和协议生命周期管理

每次添加一个新工具，都要 **手动编写完整的 JSON Schema，定义参数验证逻辑，处理错误响应格式** 。这种开发体验， **既低效又容易出错** 。

而 FastMCP 用一行 `@             mcp.tool           ` 装饰器，把这一切都自动化了。

```
# 传统 MCP 开发：几十行样板代码
# FastMCP 开发：一个装饰器搞定
@
            mcp.tool
          
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

声明一个工具函数， **Schema、验证和文档自动生成** 。

你只关心业务逻辑，MCP 部分“开箱即用”。

### 3.3 原因三：从“能跑”到“能生产

很多框架能帮你快速跑通原型，但一上生产就出问题。

FastMCP 从一开始就考虑了生产环境。

2024 年，FastMCP 1.0 被 **正式并入官方的 MCP Python SDK** 中。

这意味着官方团队也认可了这套开发方式。

FastMCP 提供了三大支柱：

- **Servers** ：把 Python 函数包装成符合 MCP 标准的工具、资源和提示词
- **Clients** ：支持完整协议，连接任何 MCP 服务器——本地或远程，编程方式或 CLI
- **Apps** ：给工具提供交互式 UI，直接在对话中渲染

**从原型到生产，一个框架全搞定** 。

这解决了 AI 开发中最头疼的问题——“Demo 跑通了，但上线怎么搞？”

### 3.4 原因四：生态完整

有工具、有社区、有企业级方案。

FastMCP 已经形成了一个完整的生态：

**工具链完善** ：可以用 `uv` 或 `pip` 安装，代码在 GitHub 上公开维护。

**社区活跃** ：有 Discord 服务器，开发者可以交流经验。

**企业级方案** ：Prefect Horizon 是专门为 FastMCP 打造的企业级 MCP 网关，提供 SSO、RBAC、审计日志、可观测性等企业级能力。

## 四、代码实战

### 4.1 快速上手：创建一个工具服务器

先看一个最简单的MCP服务器：

```
from fastmcp import FastMCP

mcp = FastMCP("My Tools")

@
            mcp.tool
          
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    
            mcp.run()
```

运行后，任何支持 MCP 的客户端（Claude Desktop、Cursor）都能连接到它并调用 `add` 工具。

### 4.2 进阶示例一：返回复杂对象的工具

实际业务中很少只返回简单数字，更多时候需要返回结构化的数据。

比如一个查询数据库的工具：

```
from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Optional
import httpx

mcp = FastMCP("Order Service")

# 定义返回的数据结构
class Order(BaseModel):
    order_id: str
    customer_name: str
    amount: float
    status: str

@
            mcp.tool
          
async def get_orders(
    customer_id: str,
    limit: int = 10,
    status: Optional[str] = None
) -> List[Order]:
    """Get orders for a customer
    
    Args:
        customer_id: Customer ID
        limit: Max number of orders to return (default 10)
        status: Filter by order status (pending/shipped/delivered)
    """
    # 模拟从数据库或API获取数据
    async with 
            httpx.AsyncClient()
           as client:
        response = await 
            client.get(
          
            f"
            https://api.example.com/customers/
          {customer_id}/orders",
            params={"limit": limit, "status": status}
        )
        return [Order(**item) for item in 
            response.json()]
```

AI 会自动获得这个工具的所有信息：参数类型、返回结构、文档说明。

当用户问“帮我查一下张三最近的订单”，AI 会调用这个工具，传入 `customer_id` ，拿到结构化的订单列表。

### 4.3 进阶示例二：注册资源（Resource）

工具是“让 AI 主动调用”，资源是“让 AI 随时可读”。

两者都能给 AI 提供上下文，但使用方式不同。

```
from fastmcp import FastMCP
import datetime

mcp = FastMCP("Company Knowledge")

@
            mcp.resource("company://policy")
          
def get_company_policy() -> str:
    """公司请假政策"""
    return """
    1. 年假：入职满一年，每年5天带薪年假
    2. 病假：每月1天带薪病假，需提供医院证明
    3. 事假：需提前3天申请，主管审批
    """

@
            mcp.resource("company://announcements")
          
async def get_announcements() -> str:
    """最新公司公告"""
    # 模拟从API获取
    return f"[{
            datetime.date.today()}
          ] 公司中秋放假安排：9月15-17日放假3天"
```

**关键区别** ：工具（Tool）是 AI 主动按需调用，资源（Resource）像挂在对话窗口里的“知识卡片”，AI 在需要时读取，内容通常相对稳定。

### 4.4 进阶示例三：依赖注入

对于需要共享状态的场景，FastMCP 提供了依赖注入机制：

```
from fastmcp import FastMCP, Context
import sqlite3
from contextlib import closing

mcp = FastMCP("Database Tools")

@
            mcp.dependency
          
def get_db() -> 
            sqlite3.Connection:
          
    """Create a database connection for each request"""
    return 
            sqlite3.connect(
          "
            data.db"
          , check_same_thread=False)

@
            mcp.tool
          
def query_users(
    ctx: Context,  # 注入上下文
    min_age: int
) -> list[dict]:
    """查询年龄大于指定值的用户"""
    conn = 
            ctx.deps.get_db()
            # 从上下文获取依赖
    with closing(
            conn.cursor())
           as cursor:
        
            cursor.execute(
          "SELECT id, name, age FROM users WHERE age > ?", (min_age,))
        return [{"id": row[0], "name": row[1], "age": row[2]} for row in 
            cursor.fetchall()]
```

依赖注入的价值：数据库连接、配置、缓存等资源由框架统一管理，每个请求自动注入。工具函数只需声明需要什么，不用管怎么创建。

### 4.5 综合示例：完整的 MCP 服务器

把上面的能力组合起来，就是一个生产级的 MCP 服务器：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8FastMCP%EF%BC%9F/50145a35a7f3f49fb85ee517d19b0f75_MD5.jpg)

代码如下：

```
from fastmcp import FastMCP, Context

mcp = FastMCP("Enterprise Assistant")

# 依赖注入：数据库连接
@
            mcp.dependency
          
def get_db():
    return 
            sqlite3.connect(
          "
            data.db"
          )

# 资源：静态知识
@
            mcp.resource("company://policy")
          
def policy():
    return "年假5天，病假1天/月..."

@
            mcp.resource("company://announcements")
           
async def announcements():
    return "中秋放假9月15-17日..."

# 工具：动态操作
@
            mcp.tool
          
def query_users(ctx: Context, min_age: int) -> list[dict]:
    conn = 
            ctx.deps.get_db()
          
    # 查询逻辑...

@
            mcp.tool
          
def get_orders(ctx: Context, customer_id: str) -> list[dict]:
    conn = 
            ctx.deps.get_db()
          
    # 查询逻辑...

if __name__ == "__main__":
    
            mcp.run()
```

**当你把这个服务器连到 Claude Desktop 后，会发生什么？**

用户说“帮我查一下张三最近的订单，顺便看看他有没有超预算”——AI 自动调用 `get_orders` 获取订单数据，再调用 `query_users` 获取用户信息，最后综合给出回答。

整个过程，用户只提了一个需求，AI 自己完成了工具选择、参数提取、多步骤调用和结果汇总。

## 五、FastMCP vs 原生 MCP SDK

我把 FastMCP 和原生 MCP SDK 放在一起做了个对比：

| 对比维度 | FastMCP | 原生 MCP SDK |
| --- | --- | --- |
| **上手难度** | 极低——装饰器 + 类型提示 | 高——需理解 stdio、session 管理 |
| **代码量** | 10 行内搞定一个工具 | 需手动处理 JSON-RPC、Schema |
| **工具注册** | `@             mcp.tool           `  一行装饰器 | 手动注册 + 手动定义 Schema |
| **文档生成** | 自动生成 | 手动编写 |
| **适用场景** | 绝大多数 MCP 开发场景 | 高级定制化需求 |
| **生产就绪** | ✅ 内置最佳实践 | ⚠️ 需自行实现 |
| **社区生态** | 25.5k Star | 405 Star |

有人可能会说：“原生 SDK 更灵活、更底层，适合高级用户。”

话是没错，但对绝大多数开发者来说， **用更少的代码、更短的时间、更低的出错概率，完成同样的功能** ——这才是更实在的价值。

## 六、优缺点

### 优点

**1\. 开发效率极高** 一行装饰器搞定工具注册，Schema、验证、文档自动生成。传统 MCP 开发需要几十行样板代码，FastMCP 只需要几行。

**2\. 市场占有率第一** 70% 的 MCP 服务器基于 FastMCP 构建。25.5k Star vs 原生 SDK 的 405 Star。

**3\. 官方认可** FastMCP 1.0 已被并入官方 MCP Python SDK。

**4\. 从原型到生产全覆盖** 不只是快速原型工具，还提供了企业级的部署方案（Horizon）。

**5\. 三大支柱，能力完整** Servers、Clients、Apps 三件套覆盖了 MCP 应用的全部需求。

**6\. Pythonic 设计** 装饰器 + 类型提示，符合 Python 开发者的习惯。自动处理传输协商、认证、协议生命周期。

### 缺点

**1\. 主要面向 Python 生态** 虽然“70% 的 MCP 服务器跨所有语言”，但 FastMCP 本身是 Python 框架。Java/Go 开发者需要用其他方案。

**2\. 封装带来灵活性损失** 高度封装意味着底层细节被隐藏。对于需要深度定制协议行为的极端场景，原生 SDK 可能更灵活。

**3\. 学习曲线不在框架，在 MCP 本身** FastMCP 本身很简单，但理解 MCP 协议的概念（Tools、Resources、Prompts）仍需要一定学习成本。

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **为 AI 应用接入外部工具** | 强烈推荐 | 几行代码就能让 AI 调用数据库、API、企业内部系统 |
| **构建 MCP 服务器** | 强烈推荐 | 70% MCP 服务器的选择，社区最大、生态最全 |
| **桌面 AI 客户端集成** | 强烈推荐 | Claude Desktop、Cursor 都支持 MCP |
| **AI Agent 开发** | 强烈推荐 | MCP 是 Agent 调用工具的标准方式 |
| **快速原型验证** | 强烈推荐 | 10 行代码跑通一个 MCP 服务器 |
| **非 Python 技术栈** | 需评估 | Java/Go 开发者可参考其他 MCP 实现 |
| **需要深度定制协议行为** | 需评估 | 可考虑原生 MCP SDK |

## 八、写在最后

回到最初的问题： **为什么越来越多人用 FastMCP？**

答案其实不复杂—— **因为它把 MCP 协议从“标准文档”变成了“生产工具”。**

MCP 协议定义了一个很好的标准，但直接基于协议开发，你得手动处理 JSON-RPC、Schema 定义、错误处理、传输协商……每一个工具都要写几十行样板代码。

FastMCP 用一行 `@             mcp.tool           ` 装饰器，把这一切自动化了。

**70% 的市场份额** 不是凭空来的。

这是无数被 MCP 原生开发“折磨”过的开发者，用 Star 和下载量投票投出来的。

FastMCP 不是 MCP 的“替代品”，而是 MCP 的“实现方式”。

它让 MCP 从“协议”变成了“工具”，从“标准”变成了“生产力”。

开源地址

- **GitHub** ： [https://github.com/PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- **官方文档** ： [https://gofastmcp.com](https://gofastmcp.com/)
- **中文文档** ： [https://fastmcp.cn](https://fastmcp.cn/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)