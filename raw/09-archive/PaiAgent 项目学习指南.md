# PaiAgent 项目学习指南

> 本指南是你学习 PaiAgent 项目的"路线图 + 讲解归档本"。
> - **左边（学习路线）**：按阶段规划，每阶段给出「目标 / 要追的代码 / 引导问题」，你照着追代码。
> - **右边（讲解归档）**：每个阶段末尾预留了「📝 讲解归档」区。当你提问后，我会把详细讲解（数据请求链路、设计原因、代码执行流程、走了哪些方法）总结回填到对应位置，方便你后续复习。

---

## 0. 项目一句话认知

PaiAgent = **拖拽式 AI 工作流编排平台**。用户在前端画布上拖节点（输入 / LLM / TTS / 输出…）、连线成一张有向图，后端把这张图解析成可执行的工作流，按顺序调度每个节点执行，节点间传递数据，并通过 SSE 把执行过程实时推回前端。

**两条最重要的主线（学完这两条就掌握了 70%）：**
1. **工作流执行主线**：`前端点击执行 → ExecutionController → EngineSelector 选引擎 → WorkflowEngine(DAG) → 拓扑排序 → 逐个 NodeExecutor 执行 → Spring AI 调 LLM → 结果回传`
2. **工作流编排主线**：`前端 ReactFlow 画布 → Zustand 存储节点/边 → 序列化成 JSON → WorkflowController 保存 → MySQL`

---

## 技术栈速查

| 层 | 技术 |
|---|---|
| 前端 | React 18 + TypeScript + Vite + ReactFlow + Ant Design + Zustand |
| 后端 | Java 21 + Spring Boot 3.4.1 + MyBatis-Plus 3.5.5 + MySQL 8 |
| AI | Spring AI 1.0.0-M5 + Spring AI Alibaba（通义千问）+ LangGraph4j |
| 存储 | MySQL（主）+ MinIO（文件，可选） |
| 实时 | SSE（Server-Sent Events） |

---

# 学习路线（按阶段推进）

> 建议顺序：**先跑起来 → 通读架构 → 追一条最简单的完整链路（登录）→ 攻核心引擎 → 再看扩展功能**。
> 每个阶段标注了 ⭐ 重要程度（⭐=了解即可，⭐⭐⭐⭐⭐=核心必攻）。

---

## 阶段 1：环境搭建，把项目跑起来 ⭐⭐

**目标**：本地能启动前后端，能登录，能创建并执行一个最简单的工作流。跑通比读代码更能建立直觉。

**要做的事**：
1. 建 MySQL 库，导入 `backend/src/main/resources/schema.sql`
2. 配置 `backend/.env`（数据库密码、JWT 密钥）
3. 启动后端：`cd backend && ./mvnw spring-boot:run`（端口 8084）
4. 启动前端：`cd frontend && npm install && npm run dev`（端口 5173）
5. 用 `admin / admin123` 登录，拖 `输入 → OpenAI → 输出` 三个节点跑一次

**要看的文件**：
- `README.md`（根目录，已读，整体介绍）
- `backend/src/main/resources/application.yml`（后端配置：端口、数据源、AI 配置）
- `backend/src/main/resources/schema.sql`（数据库表结构 —— **强烈建议先看表，理解数据模型**）
- `frontend/.env.example`（前端连后端的地址配置）

**引导问题**：
- 数据库里有哪些表？各自存什么？（workflow / execution_record / ...）
- 后端启动时做了哪些初始化？（提示：`config/` 目录下的 `*Runner` 类）

### 📝 讲解归档（阶段 1）

#### 数据模型全景（schema.sql 讲解）

12 张表按职责分 5 组：

**第 1 组：核心工作流（★最重要）**

- **`workflow`（工作流表）**：全项目核心。关键字段 **`flow_data`（JSON）** 一个字段存下前端画布的整张图（节点 + 连线 + 每个节点的配置）。`engine_type` 字段（'dag'/'langgraph'）决定用哪个引擎执行。
  - flow_data 结构示意：
    ```json
    {
      "nodes": [
        {"id":"node_1","type":"input","data":{"config":{}}},
        {"id":"node_2","type":"openai","data":{"config":{"apiKey":"...","prompt":"{{input}}"}}},
        {"id":"node_3","type":"output","data":{"config":{}}}
      ],
      "edges": [
        {"source":"node_1","target":"node_2"},
        {"source":"node_2","target":"node_3"}
      ]
    }
    ```
  - **为什么用一个 JSON 字段而不拆表**：图结构半结构化、频繁变化，整存整取最简单；不拆表避免了保存时拆表、执行时 JOIN 拼回的复杂度。代价是不能用 SQL 查"哪些工作流用了某节点"，但本项目不需要。这是可视化编排类项目的常见设计。

- **`node_definition`（节点定义表）**：节点的"说明书/元数据"（系统支持哪些节点类型）。区别于 `flow_data`（用户实际用了哪些节点=实例）。预置节点：input/output(IO)、openai/deepseek/qwen/step/react_agent(LLM)、tts(TOOL)、condition(CONTROL)。
  - 每种节点有 3 个 Schema：`input_schema` / `output_schema` / `config_schema`。**`config_schema` 是前端动态渲染配置表单的依据**（"配置驱动 UI"，加新节点类型前端表单不用硬编码）。

**NodeDefinitionController/Service 的执行链路**（`GET /api/node-types`，给前端 NodePanel 加载节点类型用）：
```
GET /api/node-types
  → Controller.listNodeTypes()
  → Service.listAllNodeDefinitions()
      ① this.list()                        // MyBatis-Plus 查 node_definition 表全部
      ② 按 nodeType 放进 LinkedHashMap       // DB 优先(同名去重)
      ③ putIfAbsent 补 6 个内置节点定义        // DB 没有才补(内置兜底)
           - llm(大模型)/memory_write/memory_retrieve/knowledge_upsert/knowledge_retrieve/image_generate/video_generate
      ④ filter: 排除 HIDDEN_STANDALONE_AGENT_NODE_TYPES(8 个 ReAct 内部工具)
           react_agent/web_search/web_fetch/vision_analyze/memory_*/knowledge_*
      ⑤ filter: 排除 category=LLM 但 nodeType≠"llm" 的(兜住 react_agent)
  → 返回 List<NodeDefinition>
```
- **DB + 内置兜底**：`putIfAbsent` 语义=DB 有就用 DB 的,没有才用内置。DB 空表也能跑,且 DB 可覆盖内置(管理员配一条 `nodeType=llm` 的记录即覆盖代码内置的)。
- **过滤 Agent 内部工具**：`memory_*`/`knowledge_*`/`web_search`/`web_fetch`/`vision_analyze`/`react_agent` 是 ReAct Agent 内部循环调用的工具,不作为独立节点暴露给前端画布拖拽。第 ⑤ 步的 `category=LLM && nodeType≠llm` 专门兜住 `react_agent`(它不在 HIDDEN 列表里)。
- **JSON Schema 三件套**：`inputSchema`(节点接受什么输入,如 prompt)、`outputSchema`(产出什么,如 imageUrl)、`configSchema`(配置项,如 model/size/steps/seed)。前端 NodePanel 拿列表按 category 分组渲染可拖拽节点,拖到画布后右侧面板按 `configSchema` 自动渲染表单——"节点类型后端驱动,前端不硬编码"。
- Service 还有 `getByNodeType(nodeType)`(含 llm/react_agent 内置分支),但当前代码未见调用方,属预留方法。
- 可简化点(预先存在,未动)：`memory_*`/`knowledge_*` 4 个在 listAllNodeDefinitions 里被 putIfAbsent 补进去,紧接着又被 HIDDEN 过滤掉——补了又删,因 getByNodeType 未被调用,目前无实际效果。

**第 2 组：执行记录（★重要）** —— 三个粒度：
| 表 | 粒度 | 存什么 |
|---|---|---|
| `execution_record` | 整次执行（1条） | 输入/输出/状态(SUCCESS/FAILED)/总耗时/节点结果汇总 |
| `execution_snapshot` | 单节点（N条） | 节点输入/输出/状态/耗时/执行顺序/重试次数，用 `execution_id` 关联 record |
| `execution_variable` | 变量 | 断点续执行的变量快照 |
- **为什么拆快照表**：支持断点续执行 + 可视化调试（前端要展示每个节点跑到哪、输入输出、失败点），需要节点级细粒度记录。

**第 3 组：`llm_global_config`（全局模型配置）**：集中配置 LLM/TTS/图片/视频/向量模型的 apiKey/apiUrl/model，节点通过 `configId` 引用，避免每个节点重复填。`is_default` 标记默认配置。

**第 4 组：Agent 记忆**：`agent_memory`（长期记忆，scope=workflow/user/global）+ `agent_memory_embedding`（记忆向量，语义检索）。给 ReAct Agent 用。

**第 5 组：知识库/RAG**：`knowledge_base` → `knowledge_document`（原始文本）→ `knowledge_chunk`（分片+向量embedding），`knowledge_index_task` 跟踪向量化进度。chunk_size 默认 800。

**表关系图**（一张图看懂数据模型）：
```
                    ┌─────────────────┐
                    │ node_definition │  节点"说明书"(系统支持的节点类型+参数Schema)
                    └─────────────────┘
                            ╎ (前端据此渲染节点面板和配置表单)
                            ╎
  ┌──────────┐   flow_data  ┌──────────┐   engine_type
  │ 前端画布 │ ───JSON────→ │ workflow │ ──────────→ 决定用 DAG / LangGraph 引擎
  └──────────┘              └────┬─────┘
                                 │ flow_id
                                 ▼
                        ┌──────────────────┐  一次执行
                        │ execution_record │
                        └────────┬─────────┘
                                 │ execution_id
                    ┌────────────┴────────────┐
                    ▼                          ▼
          ┌────────────────────┐   ┌────────────────────┐
          │ execution_snapshot │   │ execution_variable │  (节点级快照/变量,支持断点续跑)
          └────────────────────┘   └────────────────────┘

  独立配置/能力表:llm_global_config(模型配置) | agent_memory(Agent记忆)
                  mcp_tool_config(MCP工具)   | knowledge_*(知识库RAG)
```

**三个核心结论**：
1. `workflow.flow_data` 一个 JSON 存整张图 —— "编排"的载体（阶段 4/5）。
2. `engine_type` 决定走哪个引擎 —— "双引擎"的数据基础（阶段 6/10）。
3. 执行三张表（record/snapshot/variable）三个粒度 —— 支撑调试可视化和断点续跑（阶段 6/9/12）。

#### 启动初始化：两个 ApplicationRunner（回答"启动时做了哪些初始化"）

阶段1 引导问题"config/ 目录下的 *Runner 类做什么"——两个 `ApplicationRunner`（Spring 启动完成后自动执行）：

**SchemaMigrationRunner（@Order(0)，最先跑）** —— 幂等 schema 升级，给老库自动补建新表新列：
- `createTableIfMissing`：查 `information_schema.TABLES` 判断表不存在才 CREATE。补建 `knowledge_base`/`knowledge_document`/`knowledge_index_task`/`knowledge_chunk`/`mcp_tool_config`/`execution_snapshot`/`execution_variable`（新功能表，老库没有就建）。
- `addColumnIfMissing`：查 `information_schema.COLUMNS` 判断列不存在才 ALTER ADD。给 `llm_global_config` 加 `embedding_model`/`image_model`/`video_model`/`memory_enabled`；给 `knowledge_chunk` 加 `document_id`/`chunk_index`/`status`/`char_count`。
- **为什么需要它**：`schema.sql` 给全新库用；老库（新功能上线前建的）不重跑 schema.sql，靠这个 Runner 增量补齐。幂等（先查存在性再执行），跑多次无副作用。Java 类比：像 Flyway/Liquibase 的轻量替代，手写 information_schema 查询。
- **重点关注**：`@Order(0)` 保证它最先跑——后续 Runner/业务依赖表存在，必须先建表。

**ConfigValidationRunner（启动配置校验，安全兜底）** —— 校验 4 项关键配置：
1. `validateJwtSecret`：JWT_SECRET 弱密钥黑名单（`secret`/`password`/`123456`/仓库默认值等 8 个）+ 长度 ≥ 32。命中弱密钥或未配置 → **throw IllegalStateException 阻止启动**。`JwtSecretProvider.isGeneratedForLocalDevelopment` 时只警告不阻止（开发友好）。
2. `validateDatabasePassword`：空密码→试连接，连不上→阻止启动；弱密码（`123456`/`password`/`root`）→警告。
3. `validateMinioCredentials`：默认 `minioadmin/minioadmin` →警告。
4. `validateDefaultCredentials`：默认管理员 `admin/admin` 等弱密码→警告。
- **重点关注**：这是**生产环境安全兜底**——防止用默认弱配置上线。JWT/数据库空密码会直接阻止启动（throw），其他弱配置只警告。开发环境用临时密钥可正常启动（`JwtSecretProvider` 兜底生成）。

**两个 Runner 的分工**：SchemaMigrationRunner 管"库结构够不够新"（@Order(0) 最先），ConfigValidationRunner 管"配置安不安全"。

---

## 阶段 2：整体架构与目录结构 ⭐⭐⭐

**目标**：脑中建立"包 → 职责"的映射，知道遇到问题该去哪个目录找。

**要看的文件**：
- `backend/README.md`（后端项目结构说明）
- `docs/SUMMARY.md`、`docs/mermaid.md`（架构图，如果有）
- 后端包结构（对照下面的职责表通读一遍类名）：

| 包 | 职责 |
|---|---|
| `controller/` | REST API 入口 |
| `service/` | 业务逻辑 |
| `mapper/` | MyBatis-Plus 数据访问 |
| `entity/` | 数据库实体 |
| `dto/` | 请求/响应传输对象 |
| `engine/` | ⭐ 工作流引擎（核心） |
| `engine/dag/` | 自研 DAG 引擎（拓扑排序+循环检测） |
| `engine/langgraph/` | LangGraph4j 状态图引擎 |
| `engine/executor/` | 节点执行器（工厂+模板方法） |
| `engine/llm/` | Spring AI LLM 调用层 |
| `engine/skill/` | Skills 技能系统 |
| `engine/agent/` | ReAct Agent 工具体系 |
| `config/` | 配置类 + 启动初始化 Runner |
| `interceptor/` | 认证拦截器 |

**引导问题**：
- `engine/` 下为什么要分 `dag` 和 `langgraph` 两套？（双引擎设计动机）
- Controller → Service → Mapper 这条经典三层链路，本项目哪里有变化？

### 📝 讲解归档（阶段 2）
_（待你提问后回填）_

---

## 阶段 3：认证登录链路（第一条完整的前后端链路）⭐⭐⭐

**目标**：用最简单的功能打通"前端发请求 → 拦截器 → Controller → Service → 数据库 → 返回 → 前端存 token"的完整认知，为后面复杂链路铺路。

**要追的代码（按调用顺序）**：
1. 前端：`frontend/src/pages/LoginPage.tsx` → `frontend/src/api/auth.ts` → `frontend/src/utils/request.ts`（axios 封装、token 注入）
2. 前端存储：`frontend/src/store/authStore.ts`
3. 后端入口：`controller/AuthController.java`
4. 业务：`service/AuthService.java`
5. 配置：`config/JwtSecretProvider.java`
6. 拦截：`interceptor/AuthInterceptor.java` + `config/WebConfig.java`（拦截器注册）

**引导问题**：
- token 生成用的什么算法？存哪里？前端每次请求怎么带上？
- `AuthInterceptor` 拦截哪些路径？放行哪些？在哪注册的？
- 默认账户 admin/admin123 是硬编码的吗？在哪配置？

### 📝 讲解归档（阶段 3）

#### 前端登录流程详解

涉及 8 个文件，各司其职：

| 文件 | 职责（Java 类比） |
|---|---|
| `main.tsx` | 程序入口，把根组件挂到 HTML |
| `App.tsx` | 路由表（类似 Spring 路由配置） |
| `pages/LoginPage.tsx` | 登录页组件（UI + 提交逻辑） |
| `api/auth.ts` | API 接口封装（类似 Service 接口） |
| `utils/request.ts` | axios 实例 + 拦截器（类似 HTTP 客户端 + Filter） |
| `utils/auth.ts` | token 存取工具（读写 localStorage） |
| `store/authStore.ts` | 全局登录态（类似全局 Session） |
| `config/api.ts` + `vite.config.ts` | 后端地址 + 跨域代理 |

#### React 必备扫盲（对照 Java）
- **组件**：一个返回 UI 的函数，JSX = 在 JS 里写 HTML。
- **useState**：组件内"可变变量"，`setXxx` 后 React 重新执行整个组件函数重渲染 UI。类比带 getter/setter 的字段，setter 自动触发刷新。
- **事件 onXxx**：`<Form onFinish={onFinish}>` 表单提交时调用 onFinish。类比监听器/回调。
- **async/await**：`await login(values)` 等 HTTP 返回后继续。类比 `Future.get()`。
- **useXxx（Hook）**：从"能力提供者"取东西，如 `useNavigate()` 取跳转、`useAuthStore()` 取全局状态。

#### 完整执行链路（带行号）
1. **页面加载**：`main.tsx:6` 挂载 `<App/>`；`App.tsx:14` 路由 `/login → LoginPage`。
2. **点登录**：`LoginPage.tsx:42-77` `<Form onFinish={onFinish}>`，Ant Design 先校验（`rules` 49/59行），通过后把 `{username,password}` 传给 onFinish。
3. **onFinish**（`LoginPage.tsx:16-32`）：`setLoading(true)` → `await login(values)` → 成功则 `setAuth(token,...)` → `navigate('/')`。
4. **login 函数**（`api/auth.ts:29-31`）：`api.post('/api/auth/login', data)`。
5. **请求拦截器**（`request.ts:25-36`）：读 localStorage 的 token 注入 `Authorization: Bearer xxx`。登录时无 token 跳过；之后每次请求都自动带。
6. **路径与跨域代理**：`config/api.ts` `API_BASE_URL` 默认 `'/api'`（非 http）→ `request.ts:15` `baseURL=''` → 实际请求 `/api/auth/login` 发到前端 5173 → `vite.config.ts:12-17` Vite proxy 把 `/api` 转发到 `http://localhost:8084` → 后端 AuthController。
7. **响应拦截器**（`request.ts:42-43`）：统一返回 `response.data`，让 login 直接拿业务数据。
8. **存登录态双写**（`authStore.ts:22-25`）：`setStoredAuth` 写 localStorage（token/refreshToken/username）+ `set(...)` 更新 Zustand 内存状态。
9. **跳转**（`LoginPage.tsx:23`）：`navigate('/')` → `App.tsx:19` 重定向到 `/editor` → EditorPage。

#### 关键设计点
1. **token 存两份**：localStorage 管"持久"（刷新不丢），Zustand 管"响应式"（状态变 UI 联动）。`authStore.ts:17-20` 初始化时从 localStorage 读作初始值，打通两者。
2. **双 token**：access token（短，每次请求带）+ refresh token（长，只用来换新 access）。过期后静默换新，用户无感。`request.ts:45-65` 收到 401 自动 `refreshAccessToken` + 重试原请求。
3. **两层拦截器**：请求拦截器统一注入 token；响应拦截器统一处理 401 + 返回 data。类比 Servlet Filter 横切所有请求。
4. **refreshPromise 单例**（`utils/auth.ts:9,71`）：多个请求同时 401 时，用模块级变量保证同时刻只有一个刷新在飞，其他等同一 Promise。类比单例+锁合并并发。
5. **isTokenExpiringSoon 主动刷新**（`utils/auth.ts:23-63`）：`decodeJwtPayload` 解码 JWT 中间段读 `exp`，快过期（30秒缓冲）就提前刷，避免"发出去才被告知 401 再重试"的来回。

#### 数据请求链路图
```
【登录请求】
LoginPage 点登录
 → onFinish (LoginPage.tsx:16)
 → login(values) (api/auth.ts:29)
 → api.post('/api/auth/login') (axios实例)
 → 请求拦截器: 无token,跳过 (request.ts:25)
 → baseURL='' + '/api/auth/login' → 发到 5173
 → Vite proxy 转发 → http://localhost:8084/api/auth/login
 → 后端 AuthController.login
 → 响应拦截器: 返回 response.data (request.ts:42)
 → onFinish: setAuth → 写localStorage + 更新Zustand
 → navigate('/') → /editor

【登录后任意请求】
 → api.get('/api/workflows')
 → 请求拦截器: 读localStorage token, 注入 Authorization: Bearer xxx
 → Vite proxy → 后端(AuthInterceptor 校验token)
 → 若401: 响应拦截器捕获 → refreshAccessToken换新
     成功 → 新token重试原请求
     失败 → clearStoredAuth + 跳回 /login
```

#### 后端登录流程详解

涉及 5 个后端文件：

| 文件 | 职责 |
|---|---|
| `AuthController.java` | REST 入口：登录/登出/刷新/获取当前用户 |
| `AuthService.java` | 核心业务：校验密码、生成/校验 token、Redis 存取 refresh token |
| `JwtSecretProvider.java` | JWT 密钥管理（防弱密钥、本地自动生成临时强密钥） |
| `AuthInterceptor.java` | 拦截器：校验后续请求的 token |
| `WebConfig.java` | 注册拦截器 + CORS 配置 |

##### 登录链路（带行号）
1. 前端 `POST /api/auth/login` body `{username,password}` → Vite proxy → 8084
2. Spring MVC 路由到 `AuthController.login`（`AuthController.java:28`），`@Valid @RequestBody LoginRequest`（`@NotBlank` 非空校验，JSR-303）
3. 调 `authService.login(username, password)`
4. `AuthService.login`（`AuthService.java:57-66`）：读默认账户配置（`@Value` 从 `application.yml` 的 `APP_AUTH_DEFAULT_USERNAME/PASSWORD` 注入，默认 admin/admin123），匹配 → `issueTokens`；否则 `return null`
5. `issueTokens`（`AuthService.java:118-129`）：`createAccessToken`(JWT) + `createRefreshToken`(UUID) + `Redis.set("auth:refresh:"+token, username, 7天)` → 返回 `AuthTokens`
6. `createAccessToken`（`AuthService.java:131-142`）：jjwt 生成 JWT，subject=username、claim tokenType=access、issuedAt、expiration(+2h)、HS256 签名
7. 回 `AuthController`：组装 `LoginResponse` → `Result.success`

##### 后续请求校验链路（拦截器）
1. 前端请求带 `Authorization: Bearer <accessToken>` → Vite proxy → 8084
2. `AuthInterceptor.preHandle`（`AuthInterceptor.java:20-45`）：
   - OPTIONS 放行（CORS 预检）
   - 取 Authorization 去掉 `Bearer ` 前缀；无则取 query 参数 `token`（兼容 SSE，EventSource 不能设自定义头）
   - `authService.validateToken`（`AuthService.java:88`）：解析 JWT + 校验 tokenType=access + 未过期
   - 无效 → 401 JSON `{"code":401,"message":"未认证或认证已过期"}`，return false（拦截）
   - 有效 → `getUsernameByToken` + `request.setAttribute("username",...)`，return true（放行）
3. 拦截器注册（`WebConfig.java:42-47`）：拦截 `/api/**`，放行 login/refresh/current/node-types/swagger

##### 刷新链路（access 过期，含 Controller 细节）
用 refresh token 换一对全新的 access + refresh token。

1. 前端收到 401 → `POST /api/auth/refresh` body `{refreshToken}`。此接口被 `WebConfig.java:46` **排除拦截**（不需 accessToken，否则 accessToken 过期来换新又卡 accessToken 死循环），用 refreshToken 自身查 Redis 做凭证。
2. `AuthController.refresh`（`AuthController.java:45-59`）：
   - 参数校验：refreshToken 为空 → 401 "Refresh Token 不能为空"
   - 调 `authService.refresh` → 返回 null → 401 "Refresh Token 无效或已过期"
   - 成功 → 组装 `LoginResponse(新access, 新refresh, user)` → `Result.success`
3. `AuthService.refresh`（`AuthService.java:68-76`）三步：
   - `getUsernameByRefreshToken`（148-153）：Redis GET `auth:refresh:<token>` → username。查不到（无效/过期/已撤销）→ null → Controller 报 401
   - `revokeRefreshToken`（111-116）：Redis DEL `auth:refresh:<token>` ← 旧的一次性作废
   - `issueTokens`（118-129）：新 JWT(exp+2h) + 新 UUID + Redis SET 新 refresh(7天)
4. 前端用新 token 重试原请求

两种 401：

| 触发 | 含义 |
|---|---|
| "Refresh Token 不能为空" | 请求体没带 refreshToken |
| "Refresh Token 无效或已过期" | Redis 查不到（过期/被撤销/伪造）|

一次性轮换（rotation）防盗用：refresh token 被盗 → 黑客用一次 → Redis 旧记录被删 → 合法用户再用失败 → 被迫重登发现异常。refresh token 是 UUID 无签名，有效性完全靠 Redis 有无记录（不像 access token 靠 JWT 签名自证）。

##### 关键设计点
1. **access 用 JWT（无状态），refresh 用 UUID+Redis（有状态）**：JWT 不查库快但无法主动失效；refresh 有状态可撤销。组合 = 短期无状态(性能) + 长期有状态(可控)，业界经典双 token 模式。
2. **refresh token 一次性使用（rotation）**：refresh 时先删旧再发新（`AuthService.java:74-75`）。被盗则攻击者用一次即失效，合法用户再用失败 → 被迫重登发现异常。
3. **JwtSecretProvider 防弱密钥**：黑名单 `WEAK_JWT_SECRETS` 拒常见弱密钥；本地开发自动生成 48 字节随机强密钥避免启动失败；生产强制显式配置；双重检查锁懒加载。
4. **默认账户无数据库表**：admin/admin123 经 `@Value` 读环境变量，不存库。留空则禁用。所以 schema.sql 无 user 表（MVP 简化）。
5. **拦截器放行清单考量**：login 无 token 必放；refresh 自校验放行；current 内部自解析 token 放行（方便前端探测登录态）。

##### 登录数据存储位置（澄清）
登录信息**完全没碰 MySQL**：

| 数据 | 存哪 | 为什么 |
|---|---|---|
| 用户名/密码 | 配置文件（`application.yml` 的 `default-username/password`，环境变量 `APP_AUTH_DEFAULT_USERNAME/PASSWORD`） | MVP 简化，无 user 表 |
| access token (JWT) | 哪都不存（无状态） | JWT 靠签名+过期时间自校验，服务端不记录 |
| refresh token | Redis（`auth:refresh:<token>` → username，7天） | 需主动撤销/判盗用，必须存起来 |
| 执行记录 | MySQL（`execution_record` 等） | 工作流执行结果，与登录无关 |

代码佐证：`AuthService.login`（57-66）不查库，直接比配置值；`schema.sql` 无 user 表；refresh token 存 Redis（`AuthService.java:122`）。生产环境要做用户注册/管理，需新建 user 表（密码 BCrypt 加密存 MySQL）。

##### ⚠️ 启动依赖提醒
后端启动 **MySQL 和 Redis 都必需**：
- MySQL：存工作流、执行记录（application.yml 默认 localhost:3306，密码 123456）
- Redis：存 refresh token（application.yml 默认 localhost:6379，密码 123456）。未装 Redis 则登录到 `issueTokens` 的 `stringRedisTemplate.set` 抛异常，登录失败。

##### 前后端闭环图
```
【登录闭环】
前端 LoginPage 点登录
 → POST /api/auth/login {username,password}
 → Vite proxy → 8084
 → AuthController.login (AuthController.java:28)
 → @Valid 校验 LoginRequest (@NotBlank)
 → AuthService.login (AuthService.java:57)
   匹配默认账户 → issueTokens (AuthService.java:118)
     createAccessToken: JWT(subject=username, exp+2h, HS256) (AuthService.java:131)
     createRefreshToken: UUID (AuthService.java:144)
     Redis.set("auth:refresh:"+refreshToken, username, 7天) (AuthService.java:122)
 → AuthController 组装 LoginResponse → Result.success
 → 前端 setAuth → localStorage + Zustand → navigate('/editor')

【后续请求校验闭环】
前端 api.get('/api/workflows') + Authorization: Bearer <accessToken>
 → Vite proxy → 8084
 → AuthInterceptor.preHandle (AuthInterceptor.java:20)
   取 Bearer token → AuthService.validateToken (AuthService.java:88)
     parseClaims + 校验 tokenType=access + 未过期
   有效 → setAttribute("username") → 放行 → 目标Controller
   无效 → 401 → 前端响应拦截器 → refreshAccessToken

【刷新闭环】
前端 POST /api/auth/refresh {refreshToken}
 → AuthService.refresh (AuthService.java:68)
   Redis.get("auth:refresh:"+token) → username
   Redis.delete(旧refreshToken)   ← 一次性轮换!
   issueTokens(发新access+新refresh)
 → 前端用新token重试原请求
```

---

## 阶段 4：工作流 CRUD 与数据模型 ⭐⭐⭐

**目标**：理解工作流是怎么存的（JSON 存图结构），MyBatis-Plus 怎么用。

**要追的代码**：
1. `controller/WorkflowController.java`（CRUD 入口，已读）
2. `service/WorkflowService.java`
3. `entity/Workflow.java`（重点看 `config` 字段怎么存节点和边、`engineType` 字段）
4. `mapper/WorkflowMapper.java`
5. `dto/WorkflowRequest.java` / `WorkflowResponse.java`
6. `config/MyMetaObjectHandler.java`（自动填充 createTime 等）

**引导问题**：
- 前端画的图（节点+连线）在数据库里是怎么一个字段存下来的？格式长什么样？
- `WorkflowConfig` / `WorkflowNode` / `WorkflowEdge`（在 `engine/model/`）和 `entity/Workflow` 什么关系？何时互转？

### 📝 讲解归档（阶段 4）

#### 定位
阶段 4 是桥梁：衔接前端画图（阶段5，ReactFlow 序列化 JSON）与后端执行（阶段6，解析 JSON 调度）。核心是 `flow_data` 一个 JSON 字段的**存**与**取**。

**WorkflowController 定位澄清**：纯 CRUD，零复杂逻辑。5 个方法（create/update/delete/get/list）全是"接请求 → 调 Service → 返回"，Controller 层不写业务；Service 层也只是 set 字段 + save/updateById/getById/list。工作流的"复杂"不在定义管理，而在**执行链路**：`ExecutionController`（执行入口）→ `EngineSelector`（按 engineType 选引擎）→ `WorkflowEngine`（DAG 调度：拓扑排序/循环检测/逐节点执行/数据流转）。即 **WorkflowController 管"工作流长什么样"（定义），ExecutionController 管"工作流怎么跑"（执行）**。要看复杂逻辑去阶段 6。

#### 三层 CRUD 链路（创建工作流，带行号）
```
前端 POST /api/workflows {name, description, flowData, engineType}
 → WorkflowController.createWorkflow (WorkflowController.java:28)
 → workflowService.createWorkflow(request) (WorkflowService.java:24)
 → new Workflow() + set 各字段 → this.save(workflow) (WorkflowService.java:31)
 → MyBatis-Plus ServiceImpl.save → INSERT INTO workflow(...)
 → MyMetaObjectHandler.insertFill 自动填 createdAt/updatedAt
 → toResponse → Result.success
```
更新/删除/查询同理，都是 `this.updateById`/`removeById`/`getById`/`list`，**零 SQL**。

#### MyBatis-Plus 机制
- `WorkflowService extends ServiceImpl<WorkflowMapper, Workflow>`：白嫖 CRUD（save/updateById/getById/list/removeById），泛型基类全实现，只写业务特有逻辑。
- `WorkflowMapper extends BaseMapper<Workflow>`：空接口即有 insert/updateById/selectById 等，运行时按注解生成 SQL。
- 实体注解：`@TableName("workflow")` 映射表；`@TableId(IdType.AUTO)` 自增；`@TableField(fill=FieldFill.INSERT/INSERT_UPDATE)` 自动填充时间；`@TableLogic` 逻辑删除（删=UPDATE deleted=1，查自动加 WHERE deleted=0）。
- `MyMetaObjectHandler`：INSERT/UPDATE 时回调自动塞 createdAt/updatedAt=now()，Service 不手动 set 时间。

#### 核心：flow_data 存与取
- **存**：ReactFlow 画布 → 序列化 JSON 字符串 → `WorkflowRequest.flowData(String)` → `Workflow.flowData(String)` → MySQL `workflow.flow_data`(JSON 类型)。MyBatis-Plus 当字符串存取不解析。
- **取**：执行时引擎拿 `flowData` 字符串 → `WorkflowConfigParser.parse(flowData)` → `WorkflowConfig{nodes, edges}`。

#### 数据模型对照（engine/model/）
```
WorkflowConfig
 ├─ nodes: List<WorkflowNode>
 │    ├─ id        节点ID(node_1)
 │    ├─ type      业务节点类型(openai/input/output...)  ← resolveNodeType 剥外层后
 │    ├─ position  {x,y} 画布坐标(执行用不到,前端展示用)
 │    └─ data: Map<String,Object> 节点配置(如 {apiKey, prompt, model})
 └─ edges: List<WorkflowEdge>
      ├─ source/target   数据流向 source→target
      └─ sourceHandle/targetHandle  端口(条件分支用)
```
`WorkflowNode.data` 装该节点具体配置，字段由 `node_definition.config_schema` 约束（阶段1）。

#### resolveNodeType 适配（易混淆点，WorkflowConfigParser.java:57-65）
ReactFlow 节点有两个 type：顶层 `type`（自定义组件名，通常 `"workflow"`，即 `REACT_FLOW_NODE_TYPE`）和 `data.type`（业务类型如 `"openai"`）。
```java
if ((nodeType == null || "workflow".equals(nodeType)) && dataType != null) {
    return dataType;  // 取业务类型 openai
}
return nodeType;
```
原因：ReactFlow 为统一渲染把顶层 type 设 `"workflow"`，真业务类型藏 `data.type`；后端执行器要按业务类型匹配（阶段7 NodeExecutorFactory），故解析时剥掉外层。这是**前端渲染需求 vs 后端执行需求**的适配。

#### 关键设计点
1. **flow_data 整存整取**：图结构半结构化，JSON 最简单（阶段1已述）。
2. **ServiceImpl 继承复用 CRUD**：零 SQL 高效；代价是复杂查询要自己写。
3. **entity(Workflow) 与 model(WorkflowConfig) 分离**：Workflow 是持久化实体（关心存 flowData 字符串），WorkflowConfig 是引擎模型（关心节点/边结构），用 WorkflowConfigParser 转换。**存储结构与执行结构解耦**，改一方不波及另一方。类比 DTO 与 Domain 分离。
4. **@TableLogic 逻辑删除**：保留审计、可恢复。
5. **MyMetaObjectHandler 自动填充**：时间字段集中处理。

#### CRUD 链路图
```
【保存】前端 ReactFlow → 序列化 JSON(flowData)
 → POST /api/workflows {name, description, flowData, engineType}
 → WorkflowController.createWorkflow → WorkflowService.createWorkflow
   new Workflow + set → this.save → ServiceImpl → BaseMapper.insert
   MyMetaObjectHandler.insertFill 填时间
 → MySQL: INSERT INTO workflow(..., flow_data=<JSON>, engine_type, ...)

【执行时解析(阶段6)】
workflow.getFlowData() → JSON 字符串
 → WorkflowConfigParser.parse → WorkflowConfig{nodes, edges}
   resolveNodeType 剥"workflow"取业务 type
 → 交给 DAGParser 拓扑排序 + 逐节点执行
```

---

## 阶段 5：前端可视化编排器 ⭐⭐⭐

**目标**：理解 ReactFlow 画布怎么管理节点/边，Zustand 怎么存状态，如何序列化成后端要的 JSON。

**要追的代码**：
1. `frontend/src/pages/EditorPage.tsx`（编辑器主页面）
2. `frontend/src/components/FlowCanvas.tsx`（ReactFlow 画布核心）
3. `frontend/src/components/NodePanel.tsx`（左侧可拖拽节点面板）
4. `frontend/src/store/workflowStore.ts`（节点/边状态管理）
5. `frontend/src/utils/workflowNode.ts`（节点数据结构工具）
6. `frontend/src/api/workflow.ts`（保存/执行 API 调用）

**引导问题**：
- 拖一个节点到画布，数据是怎么加到 store 里的？
- 点"保存"时，画布的节点和边如何序列化成后端 `WorkflowRequest`？
- 节点的配置（如 LLM 的 apiKey、prompt）存在节点数据的哪个字段？

### 📝 讲解归档（阶段 5）

#### EditorPage.tsx 详解（工作流编辑器主页面）

**定位**：用户在这里拖节点、连线、配置节点参数、保存、调试执行。前端编排核心，把 ReactFlow 画布、配置表单、持久化、执行全串起来。近 3000 行。

**布局**：顶部工具栏（工作流名/引擎选择 DAG|LangGraph/新建/加载/保存/调试/登出/知识库/MCP）+ 左 NodePanel（可拖拽节点）+ 中 FlowCanvas（ReactFlow 画布）+ 右节点配置面板（按选中节点动态渲染）+ 浮层（DebugDrawer/加载 Modal）。

**数据三来源**：① workflowStore(Zustand)：nodes/edges/selectedNode/currentWorkflowId，画布共享；② 本地 useState：workflowName/engineType/llmConfig/ttsConfig/outputParams 等临时编辑态；③ 后端 API：getWorkflow/create/update/execute 持久化。

**生命周期（useEffect）**：进页面 fetchLLMGlobalConfigs + getKnowledgeBases + getMcpTools（给配置下拉用）；URL 有 /editor/:id 触发 loadWorkflowById；全局配置异步加载完补齐选中节点展示配置。

**五大核心功能**：
1. **拖拽节点**（handleDragStart, 228）：NodePanel 起拖写 dataTransfer，FlowCanvas drop 创建节点加 store。
2. **点击节点**（handleNodeClick, 235）★：setSelectedNode + 按类型加载配置到本地 state（output→outputParams，LLM→llmConfig，TTS→ttsConfig）。本地 state 是 node.data 的镜像，编辑改 state，防抖后写回。
3. **保存工作流**（handleSave, 461）★：`JSON.stringify({nodes: serializeWorkflowNodes(nodes), edges: map取id/source/target/handle})` → 有 id 则 updateWorkflow，无则 createWorkflow + navigate(/editor/{id})。**这就是阶段4 flow_data 的生成处**。
4. **加载工作流**（loadWorkflowById, 396）：getWorkflow → JSON.parse(flowData) → setNodes/setEdges 恢复画布。enrichKnowledgeBaseNames 补知识库名，hasLoadedRef 防重复。
5. **执行工作流**（handleExecute, 512）：DebugDrawer 调（传 inputData）→ executeWorkflow → 后端 POST /api/workflows/{id}/execute。**阶段6 引擎触发点**。

**节点配置体系（精髓）**：右侧面板按 selectedNode.data.type 动态渲染表单——input(只读)/output(输出参数+回答内容模板{{参数名}})/LLM类(输入参数/输出参数/提示词/Agent策略/工具/记忆/知识库/全局配置/温度/技能)/TTS(输入/全局配置/语音参数/输出)/AgentPlan类(web_search/web_fetch/memory/knowledge/image/video 各自配置)。

**参数引用机制（核心）★**：参数两种类型——`input`(静态值) / `reference`(引用上游节点输出，下拉选"节点.参数名")。getReferenceableNodes(566) 只允许引用直接上游（通过 edges 找 target=当前节点的 source），防止引用未执行的下游。执行时后端 PromptTemplateService 把 reference 替换成上游实际输出、{{参数名}} 也替换。**节点间数据流转的配置基础，不写代码即可编排**。

**全局配置 vs 手动配置**：选 configId 则 apiUrl/apiKey/model 从 llm_global_config 读，节点不存 apiKey（安全）；没选手动填存 node.data。`useGlobalConfig ? '' : apiKey`。

**自动保存防抖（1013/1058/1118）**：三个 useEffect 监听 output/llm/tts 配置变化 → 500ms debounce → updateNode 存 store。autoSaveTimerRef 管理定时器。改配置不用点按钮也自动生效。

**关键设计点**：
1. 配置驱动 UI：右侧按 node.data.type 动态渲染，呼应后端 node_definition。
2. 参数引用机制：reference 让节点间数据流转可视化。
3. flowData 序列化：serializeWorkflowNodes + edges → JSON，呼应阶段4 WorkflowConfigParser 反向解析。
4. 全局配置优先：apiKey 不存节点，安全。
5. 自动保存防抖：500ms debounce 平衡性能体验。
6. 状态分层：store(共享)/useState(临时)/API(持久) 各司其职。
7. URL 驱动加载：/editor/:id 触发，hasLoadedRef 防重复。

**数据流图**：
```
【拖节点】NodePanel dragStart → dataTransfer → FlowCanvas drop → store.addNode
【点节点】FlowCanvas onNodeClick → handleNodeClick → setSelectedNode + 加载配置到 useState → 右侧渲染
【改配置】右侧 onChange → setLlmConfig 等 → 500ms 防抖 → updateNode(存 store 的 node.data)
【保存】handleSave → serialize(nodes+edges) → flowData JSON → create/updateWorkflow → MySQL flow_data
【加载】loadWorkflowById → getWorkflow → JSON.parse(flowData) → setNodes/setEdges → 画布恢复
【执行】DebugDrawer → handleExecute(inputData) → executeWorkflow → 后端引擎(阶段6)
```

#### 其他前端文件详解（workflowNode / workflowStore / api/workflow / NodePanel / FlowCanvas）

**分工**：workflowNode.ts(节点工具函数：序列化/反序列化/默认值) / workflowStore.ts(Zustand 全局状态：画布数据源) / api/workflow.ts(API 封装：CRUD/执行/SSE) / NodePanel.tsx(左侧节点面板：可拖拽列表) / FlowCanvas.tsx(中间画布：ReactFlow)。

**必备概念（对照 Java）**：
- ReactFlow：图形库（类比 Swing/JavaFX）。节点=React 组件，边={source,target}，Handle=连接端口(target 入/source 出)。
- Zustand：状态管理（类比全局单例+观察者）。create() 建 store，set() 后订阅组件自动重渲染。
- 拖拽(HTML5)：draggable + onDragStart(写 dataTransfer) + onDrop(读 dataTransfer)。
- useNodesState/useEdgesState：ReactFlow Hook，管本地节点/边状态。

**workflowNode.ts**：
- getWorkflowNodeType(22)：取业务类型(优先 data.type)。
- normalizeWorkflowNode(31)：规范化——顶层 type 设 'workflow'(渲染用)，真实类型藏 data.type，label 缺失补默认。**加载时用**。
- serializeWorkflowNodes(49)：序列化——存库前转 {id, type:业务类型, position, data}。**保存时用**。
- createDefaultWorkflowNodes(60)：默认 input+output。**新建时用**。
- **normalize/serialize 与后端 resolveNodeType 对称**：前端把真实类型藏 data.type、顶层统一 'workflow'，后端剥外层取业务类型。

**workflowStore.ts**：Zustand store，画布数据源。状态 nodes/edges/selectedNode/currentWorkflowId；方法 setNodes(带 normalize)/addNode/updateNode(按 id 更新 data，EditorPage 改配置用)/deleteNode(删节点+相关边)/clear。所有组件 useWorkflowStore() 读改。

**api/workflow.ts**：HTTP 封装。CRUD(getWorkflows/getWorkflow/create/update/delete)、执行(executeWorkflow 普通 / executeWorkflowStream SSE)、执行记录(getLatestExecution/getExecutionSnapshots/resumeWorkflowExecution)、getNodeTypes(NodePanel 用)。executeWorkflowStream(170) 用 EventSource 监听 WORKFLOW_START/NODE_START/NODE_SUCCESS 事件回调 onEvent（阶段9）。

**NodePanel.tsx**：进页面 getNodeTypes() 从后端 node_definition 加载节点类型 → 按 category 分组(LLM/TOOL/CONTROL) → 每节点 div draggable + onDragStart 写 nodeType/displayName 到 dataTransfer。**节点类型后端驱动，前端不硬编码**。

**FlowCanvas.tsx（最复杂）**：
- WorkflowNodeCard(109)：自定义节点组件，按 data.type 显示图标/标签/参数数/条件/工具/知识库。Handle 规则：input 无 target(起点)，output 无 source(终点)，condition 多 source Handle(每分支一个 id=分支标识) → **阶段6 sourceHandle 路由的前端来源**。
- nodeTypes={workflow:WorkflowNodeCard}(211)：顶层 type='workflow' 用此组件渲染。
- 状态双向同步(219-261)：useEffect(store→本地) + handleNodesChange(本地→store)。双状态：useNodesState(本地交互快) + Zustand(全局共享)。
- onDrop(280)：读 dataTransfer → 算位置 → 建节点{type:'workflow', data:{type:业务类型}} → setStoreNodes。
- handleConnect(263)：拖 Handle → addEdge → setStoreEdges。
- handleNodeClick(316)：点节点 → 回调 EditorPage onNodeClick。

**协作数据流**：
```
【加载节点类型】后端 node_definition → NodePanel getNodeTypes → 渲染可拖拽列表
【拖节点】NodePanel onDragStart(写dataTransfer) → FlowCanvas onDrop(读) → 建节点 → setStoreNodes → 渲染
【连线】拖 Handle → handleConnect → addEdge → setStoreEdges → 渲染
【点节点】FlowCanvas handleNodeClick → EditorPage onNodeClick → 加载配置
【改配置】EditorPage → store.updateNode → data 更新
【保存】serializeWorkflowNodes → flowData JSON → create/updateWorkflow → MySQL
【加载】getWorkflow → JSON.parse → normalizeWorkflowNodes → store.setNodes → 渲染
```

**关键设计点**：
1. store+本地双状态：Zustand(共享) + useNodesState(本地交互)，useEffect 双向同步。
2. normalize/serialize 对称：呼应后端 resolveNodeType。
3. nodeTypes 自定义渲染：所有节点同一 WorkflowNodeCard，按 data.type 显示不同样式。
4. Handle 端口：condition 多 source Handle(分支标识)，阶段6 sourceHandle 路由来源。
5. 节点类型后端驱动：NodePanel 从 node_definition 加载，加类型只需后端加数据。

---

## 阶段 6：核心 —— DAG 工作流执行引擎 ⭐⭐⭐⭐⭐

**目标**：这是项目的心脏。彻底搞懂一次"执行工作流"从 HTTP 请求到逐节点跑完的全过程。

**要追的代码（严格按执行顺序）**：
1. `controller/ExecutionController.java`（执行入口 `POST /{id}/execute`，已读）
2. `engine/EngineSelector.java`（选引擎，已读）
3. `engine/WorkflowExecutor.java`（引擎统一接口）
4. `engine/WorkflowEngine.java`（DAG 引擎实现 —— **核心中的核心，重点精读**）
5. `engine/dag/DAGParser.java`（拓扑排序 Kahn 算法 + DFS 循环检测）
6. `engine/WorkflowConfigParser.java`（JSON 配置解析）
7. `engine/model/WorkflowConfig.java` / `WorkflowNode.java` / `WorkflowEdge.java`

**引导问题（这些搞懂了这阶段就通了）**：
- `EngineSelector` 怎么根据 `engineType` 选到 DAG 还是 LangGraph 引擎？用了什么 Spring 特性？（提示：注入 `List<WorkflowExecutor>`）
- Kahn 拓扑排序具体怎么实现的？入度为 0 的节点怎么找？
- 循环检测（DFS）在哪一步做？检测到循环怎么处理？
- 一个节点的输出怎么变成下一个节点的输入？数据在哪个 Map 里流转？
- 执行记录（ExecutionRecord）、快照（ExecutionSnapshot）在什么时机写库？

### 📝 讲解归档（阶段 6）

#### DAG 工作流执行引擎详解（项目心脏）

**三文件分工**：`WorkflowExecutor`(引擎统一接口，支持 DAG/LangGraph 双引擎) / `WorkflowEngine`(DAG 引擎实现：解析→排序→执行→流转→记录) / `DAGParser`(Kahn 拓扑排序 + DFS 循环检测)。

**完整执行链路**（executeWithCallback, 57）：
1. `workflowConfigParser.parse(flowData)`(60)：JSON → WorkflowConfig（阶段4）
2. `dagParser.parse(config)`(61)：拓扑排序 + 循环检测 → sortedNodes 执行顺序
3. `buildEdgeIndexes`(63)：edgesBySource/edgesByTarget（O(1) 查出/入边）
4. `createRunningRecord`(64)：INSERT execution_record(RUNNING) 占位
5. `eventCallback(workflowStart)`(67)：SSE
6. `executeNodes`(70)：★核心循环

**executeNodes 核心循环（126）★**：遍历排序后节点，每个节点：
- 168 resolveNodeInput（解析输入：前驱输出 merge）
- 175 createOrUpdateSnapshotStart（建快照 RUNNING）
- 178 eventCallback(nodeStart) → SSE
- 187-188 executorFactory.getExecutor(type).execute(node,input,callback) ← 阶段7
- 191 nodeOutputs.put(nodeId, output)（存输出）
- 206 eventCallback(nodeSuccess) → SSE（带 input/output/duration）
- 209 currentInput = output（数据链式流转）
- 212-215 condition 节点：markSkippedNodes（标记未选分支跳过）
- 217-229 异常：snapshot(FAILED) + nodeError + throw → 被外层 catch(239)接住置 status=FAILED，正常返回 ExecutionResponse(FAILED)，**不抛到 Controller**；Controller 的 catch 只兜初始化失败(parse 配置/选引擎/建记录)
循环后：outputData=最终输出(237) → workflowComplete(250) → UPDATE record(263) → return ExecutionResponse

**DAGParser 算法**：
- 构建依赖图：dependencies(节点→前置) / dependents(节点→后继)。target 依赖 source。
- **循环检测**（detectCycle, 62）—— DFS + 递归栈(recStack)：
  ```
  hasCycleDFS(nodeId, visited, recStack):
    if recStack 含 nodeId: 发现环!return true   ← 关键：当前路径上再次遇到即成环
    if visited 含 nodeId: 已访问无环,return false
    visited.add; recStack.add  ← 入栈
    for dep in dependencies[nodeId]: 递归检查前置
    recStack.remove  ← 出栈（回溯）
  ```
  recStack 记录当前 DFS 路径，区别于 visited（永久标记）。成环 = 路径上回到自己。
- **拓扑排序**（topologicalSort, 106）—— Kahn 算法：
  ```
  1. 入度 = dependencies[nodeId].size（每个节点依赖几个前置）
  2. 入度 0 的节点入队（无依赖，可先执行）
  3. while 队列非空:
       出队 nodeId → result.add
       for 后继 in dependents[nodeId]:
         后继入度 -1            ← "解锁"
         if 入度变 0: 入队
  4. if result.size != 总节点数: 还有环（兜底）
  ```
  入度 0 = 没有前置依赖，可以先执行。出队后"解锁"后继。
- **双重检测环**：DFS 提前抛清晰错误（"工作流存在循环依赖,节点: xxx"）+ Kahn 排序后 result.size!=总节点数 兜底。两道保险。

**数据流转机制（核心）★**：
1. `nodeOutputs`: Map<nodeId, output> 存所有已执行节点输出。
2. `resolveNodeInput`(285)：当前节点入边的 source 输出 merge 成当前输入；多前驱汇聚时合并字段；空则用 fallbackInput。
3. `currentInput = output`(209)：上一节点输出作下一节点默认输入（链式传递，即使无显式连线也能传）。
4. `__nodeOutputs__`(303)：把全量输出塞进当前输入，供后端 PromptTemplateService 解析 reference 引用（EditorPage 配置的 reference 的运行时载体）。stripRuntimeFields 序列化时剔除（不存库）。

**条件分支路由**（212 + 310）：condition 节点输出 `__selectedBranch__`。markSkippedNodes 按出边 sourceHandle（分支标识）区分活跃/非活跃分支，递归标记非活跃分支下游跳过。markDownstreamSkipped 只当节点所有入边都来自已跳过节点才跳过（避免误跳多入度汇聚节点）。这就是 IF/ELSE 实现：未选分支整条路径跳过。

**SSE 事件回调**（阶段9）：workflowStart(67)/nodeStart(178)/nodeSuccess(206)/nodeError(226)/workflowComplete(250)。eventCallback 推前端 DebugDrawer 实时展示。null 时跳过（普通执行无 SSE）。

**执行记录与快照**：execution_record(383, 整次, RUNNING→SUCCESS/FAILED) + execution_snapshot(404, 每节点, RUNNING→SUCCESS/FAILED via markSnapshotSuccess/markSnapshotFailed)。粒度：record 整次 / snapshot 单节点。支持断点续跑。
**快照读出口** getExecutionSnapshots(110)：selectById record 校验 flowId 归属(防越权) → selectByExecutionId 按 execution_order ASC 排序 → toSnapshotResponse 转 DTO(inputData/outputData 实体 JSON 字符串→DTO Map)。重试时 createOrUpdateSnapshotStart(404) 按 (executionId,nodeId) 查已有快照复用 → retryCount+1 而非新建——同一节点重试多次只留一条快照(最新态)。

**断点续执行**（resumeExecution, 73）：查 record → 重新 parse+排序 → 查快照 snapshotsByNode → resolveResumeStartNodeId 定起点(指定/第一个FAILED/第一个未SUCCESS) → buildResumeState 从快照恢复已成功节点输出到 nodeOutputs(跳过) → modifiedVariables 覆盖(存 execution_variable) → record=RUNNING → executeNodes 从起点继续。

**关键设计点**：
1. 接口+多实现：WorkflowExecutor 统一双引擎，EngineSelector 路由，开闭原则。
2. 拓扑排序保证顺序：Kahn，入度0先执行，DAG 天然适合顺序编排。
3. 双重循环检测：DFS 抛错 + Kahn 数量兜底。
4. 数据流转三件套：nodeOutputs(全量) + resolveNodeInput(merge前驱) + currentInput=output(链式)。支持顺序/分支/汇聚。
5. __nodeOutputs__ 注入：支持 reference 引用任意上游；stripRuntimeFields 剔除运行时字段。
6. 条件分支跳过：sourceHandle 标识分支，递归标记，多入度不误跳。
7. 快照+记录双写：实时调试 + 断点续跑。
8. SSE 事件驱动：执行过程实时推前端。
9. NodeExecutor 工厂：按 type 取执行器，可扩展（阶段7）。

**完整链路图**：
```
ExecutionController.executeWorkflow
 → EngineSelector.selectEngine(按 engineType)
 → WorkflowEngine.executeWithCallback (57)
   1. parse(flowData) → WorkflowConfig
   2. dagParser.parse → sortedNodes(构建依赖图→detectCycle→topologicalSort Kahn)
   3. buildEdgeIndexes → edgesBySource/edgesByTarget
   4. createRunningRecord → INSERT execution_record(RUNNING)
   5. eventCallback(workflowStart) → SSE
   6. executeNodes (126):
      for node in sortedNodes:
        跳过(断点已成功/条件未选中)
        resolveNodeInput: 前驱输出 merge + __nodeOutputs__
        createOrUpdateSnapshotStart → snapshot(RUNNING)
        eventCallback(nodeStart) → SSE
        executorFactory.getExecutor(type).execute(node,input,callback)  ← 阶段7
        nodeOutputs.put(nodeId, output)
        eventCallback(nodeSuccess) → SSE
        currentInput = output  ← 数据流转
        if condition: markSkippedNodes
        异常: snapshot(FAILED) + nodeError + throw
   7. outputData = 最终输出
   8. eventCallback(workflowComplete) → SSE
   9. UPDATE execution_record(SUCCESS/FAILED + 结果)
   10. return ExecutionResponse
```

---

## 阶段 7：节点执行器体系（工厂 + 模板方法）⭐⭐⭐⭐⭐

**目标**：理解"一个节点怎么被执行"，以及项目如何用设计模式消除多个 LLM 节点的重复代码。

**要追的代码**：
1. `engine/executor/NodeExecutor.java`（执行器接口）
2. `engine/executor/NodeExecutorFactory.java`（工厂：type → executor）
3. `engine/executor/impl/InputNodeExecutor.java` / `OutputNodeExecutor.java`（最简单的，先看这俩）
4. `engine/executor/impl/AbstractLLMNodeExecutor.java`（⭐ 模板方法基类，重点）
5. `engine/executor/impl/OpenAINodeExecutor.java` / `DeepSeekNodeExecutor.java` / `QwenNodeExecutor.java`（看它们如何靠继承只写几行）
6. `engine/executor/impl/ConditionNodeExecutor.java`（条件分支节点，配合 `ConditionBranchRoutingTest` 看）

**引导问题**：
- `NodeExecutorFactory` 怎么根据节点 type 找到对应执行器？注册时机？
- `AbstractLLMNodeExecutor` 用模板方法固定了哪些步骤？子类只需实现什么？（对照 README 说的"800 行精简到 75 行"）
- Input/Output 节点的输入输出 Map 结构分别长什么样？

### 📝 讲解归档（阶段 7）

#### 节点执行器体系（工厂模式 + 模板方法）

**核心设计**：
1. **工厂模式 + Spring 自动注册**（NodeExecutorFactory）：Spring 启动时把所有 `@Component` 的 NodeExecutor 收集成 List 注入，工厂用 `getSupportedNodeType()` 作 key 建索引 `executors` Map。`getExecutor(nodeType)` 查 Map。**加新节点类型零成本**：写新类 `@Component`+实现 `getSupportedNodeType()`，工厂自动收录不改代码（开闭原则）。
2. **模板方法模式**（AbstractLLMNodeExecutor）：LLM 调用逻辑在基类 `execute()`(78-168) 固定 7 步，子类只覆写 `getNodeType()` 返回类型标识。`getSupportedNodeType()`(592) 基类实现 `return getNodeType()`，子类实现 getNodeType 即同时满足工厂注册。

   **OpenAINodeExecutor 就这么多**（所有 LLM 厂商节点都这样）：
   ```java
   @Component
   public class OpenAINodeExecutor extends AbstractLLMNodeExecutor {
       @Override
       protected String getNodeType() { return "openai"; }
   }
   ```
   DeepSeek/Qwen/智谱/AIPing 全都只写 `getNodeType()="xxx"` 几行。所有公共逻辑（配置提取、模板替换、调 API、构建输出）在基类。这就是 README 说的"800 行精简到 75 行"——**子类只填差异点**。类比 Java：基类是模板，子类是填空。

   **为什么这样设计**：多厂商 LLM 调用逻辑几乎相同（配置→模板→调 API→输出），差异只是 provider 标识。模板方法把公共流程固定，避免每个厂商复制粘贴 800 行。加新厂商（如 Claude）只需写 3 行 `getNodeType`。

**AbstractLLMNodeExecutor 7 步流程**：
1. extractConfig(86,454)：从 node.data 提取。优先级：有 configId→读 llm_global_config 全局；否则读节点 data。canonicalizeProvider(532) 规范化 provider 别名（"通义千问"→qwen、"阶跃星辰"→step）。
2. validateResolvedConfig(87)：校验 provider/apiUrl/apiKey/model 齐全。
3. skillRegistry.getSkill(101)：加载技能 + loadAllReferences 打包完整内容（阶段11）。
4. buildSystemPrompt(119)：系统提示（含技能内容）。
5. promptTemplateService.processTemplate(122)：处理 {{参数名}} + reference 解析（阶段8）。
6. buildContextPrompt(127)：memoryEnabled→agentMemoryService.retrieve 召回记忆；knowledgeBaseId→knowledgeBaseService.searchRuntime 检索知识库（阶段12）。
7. 创建 ChatClient + 调 LLM(134-154)：三模式——streaming+callback→executeStreaming(SSE推chunk)；functions非空→executeWithFunctions(函数调用循环最多5次)；否则→executeNormal。
8. buildOutput(164)：按 outputParams 映射 + token 统计。

**其他执行器**：
- **InputNodeExecutor**：`return new HashMap<>(input)` 直接透传输入（起点）。
- **OutputNodeExecutor**（模板替换 + reference 解析）★：读 responseContent 模板 + outputParams；reference 参数（格式"节点ID.参数名"）**优先从 input.__nodeOutputs__[节点ID][参数名] 取（阶段6注入！），兜底 input[参数名]**；user_input fallback 到 input["input"]；正则 `{{参数名}}` 替换成值 → 最终输出。
- **ConditionNodeExecutor**（条件分支）★：读 conditions（每条 id/field/operator/value）；遍历第一个匹配的 conditionId 作 `__selectedBranch__`，无匹配→"default"；resolveField(84) 支持嵌套字段(.分隔)+JSON字符串解析；evaluateCondition(134) 12 种操作符(eq/neq/gt/gte/lt/lte/contains/notContains/startsWith/endsWith/isEmpty/isNotEmpty)；输出 `__selectedBranch__`+`__conditionNodeId__`。**这是阶段6 markSkippedNodes 的数据来源**，按出边 sourceHandle 匹配标记未选分支跳过。
- **VisionAnalyzeNodeExecutor**（视觉质检，多模态）★：extends AbstractAgentPlanNodeExecutor，`getSupportedNodeType()="vision_analyze"`。取 imageUrl/videoUrl + criteria（判断素材是否满足要求，0-100 分）→ `configResolver.resolve(node, "vision")` + validateApiConfig（用 Agent Plan 配置，全局配置优先）→ `chatClientFactory.createClient(provider, apiUrl, apiKey, model, temperature=0.2)` → 构造 prompt（质检要求+图片/视频 URL）→ `chatClient.prompt().call().content()` 调**多模态 LLM** 看图/视频 → 解析 score/pass（粗糙：含"不通过"→60 否则 85；pass=score≥80 且不含"不通过"）→ 输出 description/score/issues/pass/output。**特点**：和图片/视频生成节点共用 `AgentPlanConfigResolver` + `AbstractAgentPlanNodeExecutor`，但产物是"质检结论"而非媒体文件；用多模态 LLM（能读图）做内容审核。score 逻辑是简化 demo，生产应让 LLM 返回结构化 JSON。

**与阶段6衔接**：executeNodes 循环里 `executorFactory.getExecutor(node.getType()).execute(node, nodeInput, eventCallback)` → 工厂查 Map → 调执行器 execute → 返回 output → 存 nodeOutputs + currentInput 链式流转。

**关键设计点**：
1. 工厂+Spring自动注册：加节点不改工厂，开闭原则。
2. 模板方法消除重复：LLM 逻辑在基类固定7步，子类只填 getNodeType。
3. 三种执行模式：流式/函数/普通。
4. 配置优先级：全局 configId > 节点 data；provider 别名规范化。
5. 输出映射：outputParams 让一个 LLM 输出映射多个变量名。
6. OutputNode reference 解析：__nodeOutputs__ 优先（阶段6注入），input 兜底。前后端 reference 闭环。
7. ConditionNode 与阶段6联动：__selectedBranch__ → markSkippedNodes 路由。IF/ELSE 完整实现。
8. 另一条线：AbstractAgentPlanNodeExecutor 给 web_search/memory/knowledge/image/video 等 Agent Plan 节点用（阶段12）。

**数据流图**：
```
【LLM 节点执行】(阶段6 executeNodes 调 executor.execute)
WorkflowEngine → executorFactory.getExecutor(node.type) → AbstractLLMNodeExecutor.execute
  1. extractConfig: node.data → LLMNodeConfig(优先 configId 全局,canonicalizeProvider 规范化)
  2. validateResolvedConfig: 校验
  3. skillRegistry.getSkill + loadAllReferences
  4. buildSystemPrompt: 系统提示(含技能)
  5. promptTemplateService.processTemplate: {{参数名}} 替换 + reference 解析(阶段8)
  6. buildContextPrompt: 记忆召回 + 知识库检索(如启用)
  7. chatClientFactory.createClientWithFunctions: 建 ChatClient(阶段8)
  8. 调 LLM: streaming(SSE推chunk)/ functions(循环)/ normal
  9. buildOutput: outputParams 映射 + token 统计
 → 返回 output 给 WorkflowEngine(存 nodeOutputs + currentInput 流转)

【Input 节点】直接返回 input(透传,起点)
【Output 节点】responseContent 模板 + outputParams reference 解析(__nodeOutputs__优先) → {{参数名}}替换 → 最终输出
【Condition 节点】conditions 遍历匹配 → __selectedBranch__ → 阶段6 markSkippedNodes 路由
```

---

## 阶段 8：Spring AI LLM 调用层 ⭐⭐⭐⭐

**目标**：理解多厂商大模型如何被统一封装、动态创建、模板变量如何替换。

**要追的代码**：
1. `engine/llm/ChatClientFactory.java`（⭐ 动态创建不同厂商 ChatClient）
2. `engine/llm/LLMNodeConfig.java`（LLM 节点配置模型）
3. `engine/llm/PromptTemplateService.java`（`{{variable}}` 模板替换、上下游参数引用）
4. `service/LLMGlobalConfigService.java` + `entity/LLMGlobalConfig.java`（全局模型配置）
5. `controller/LLMConfigController.java`

**引导问题**：
- 为什么 OpenAI/DeepSeek/智谱/AIPing 能共用一套 OpenAI 兼容接口，而通义千问要单独处理？
- `ChatClientFactory` 如何根据 apiKey/apiUrl/model 运行时创建 ChatClient？为什么不用单例？
- `{{变量}}` 是怎么被上游节点的输出替换的？`input` 静态值和 `reference` 动态引用有什么区别？

### 📝 讲解归档（阶段 8）

#### Spring AI LLM 调用层详解

**五文件分工**：ChatClientFactory(动态创建多厂商 ChatClient，核心) / LLMNodeConfig(LLM 节点配置 DTO) / PromptTemplateService({{变量}} 模板替换+reference 解析) / LLMGlobalConfigService(全局配置 CRUD+默认管理) / LLMGlobalConfig(全局配置实体)。

#### ChatClientFactory（核心）★
阶段7第7步 `chatClientFactory.createClientWithFunctions` 的实现。

**provider 分流**（69-77）：
```java
ChatModel chatModel = switch (normalizedProvider) {
    case "openai","deepseek","qwen","step","zhipu","ai_ping","agnes" ->
        createOpenAICompatibleModel(apiUrl, apiKey, model, temperature);  // OpenAI 兼容
    case "apifree" -> createApifreeChatModel(...);  // 特殊:text/plain
    case "volcengine_agent_plan" -> createVolcengineArkChatModel(...);  // 特殊:自定义路径
    default -> throw 不支持;
};
ChatClient.builder(chatModel).build();
```

**为什么 OpenAI/DeepSeek/智谱/AIPing/通义千问能共用一套接口**：它们都实现了 OpenAI 兼容协议（`POST /v1/chat/completions`），只是 baseUrl 和 apiKey 不同。用同一个 `createOpenAICompatibleModel` 传入不同 apiUrl/apiKey。Spring AI 的 `OpenAiApi` 支持自定义 baseUrl。
```java
OpenAiApi openAiApi = new OpenAiApi(normalizedApiUrl, apiKey);  // 自定义 baseUrl
OpenAiChatOptions options = OpenAiChatOptions.builder().model(model).temperature(temperature).build();
return new OpenAiChatModel(openAiApi, options);
```

**两个特殊 provider**：
- **apifree**（119）：SkyClaw 的 endpoint 有时以 `text/plain` 返回 JSON，Spring AI 默认 JSON converter 不接收 text/plain。需自定义 RestClient 的 messageConverter 支持 text/plain。
- **volcengine_agent_plan**（146）：火山方舟 Agent Plan 的接口路径不是标准 `/v1/chat/completions`，而是 `/api/plan/v3/chat/completions`。需显式指定 completionsPath 和 embeddingsPath。

**容错 normalizeBaseUrl**（175）：用户误填完整接口地址（带 `/v1/chat/completions` 或 `/v1`），工厂自动剥离只留根地址（Spring AI 会自己拼 `/v1/chat/completions`）。

**provider 规范化 normalizeProvider**（217）：中英文别名统一：`open ai→openai`、`通义千问→qwen`、`阶跃星辰→step`、`智谱→zhipu`、`火山方舟→volcengine_agent_plan`。

**为什么动态创建而非单例**：每个节点的 apiKey/apiUrl/model 不同（多配置/多租户），运行时根据配置创建。ChatClient 不是 Spring 单例 bean，每次执行创建新实例。

#### PromptTemplateService（模板替换）★
阶段7第5步 `promptTemplateService.processTemplate` 的实现。

**两种参数类型 buildParamValues**（51）：
```java
for (param : inputParams) {
    if (param.type == "input") {
        paramValues.put(paramName, param.value);  // 静态值:直接从配置取
    } else if (param.type == "reference") {
        reference = param.referenceNode;  // "节点ID.参数名"
        refParamName = reference.split(".")[最后一段];
        refValue = runtimeInput.get(refParamName);  // 从上游输出取
        if (refValue == null && refParamName == "user_input") refValue = runtimeInput.get("input");  // fallback
        paramValues.put(paramName, refValue);
    }
}
```

**模板替换 replaceTemplateVariables**（95）：`{{变量}}` 正则 `\{\{(.*?)\}\}` 匹配，用 paramValues 替换。

**关键**：`runtimeInput` 就是阶段6 `resolveNodeInput` 的结果（含上游输出 merge + `__nodeOutputs__`）。reference 引用的上游输出值在这里被替换进 prompt。

**示例**：prompt 模板 `"请把 {{user_input}} 翻译成英文"` + inputParams `[{name:"user_input", type:"reference", referenceNode:"input-1.user_input"}]` + runtimeInput `{user_input:"你好"}` → 替换后 `"请把 你好 翻译成英文"`。

#### 配置模型
- **LLMNodeConfig**：provider/apiUrl/apiKey/model/temperature/promptTemplate/inputParams/outputParams/streaming/skillName/configId。阶段7 extractConfig 从 node.data 提取填充。
- **LLMGlobalConfig**（实体）：provider/configName/apiUrl/apiKey/model/ttsModel/embeddingModel/imageModel/videoModel/memoryEnabled/temperature/isDefault。**一个配置可存多类模型**（LLM/TTS/向量/图片/视频），节点按需取；`is_default` 标记默认配置。

#### LLMGlobalConfigService（全局配置管理）
- listByProvider/getDefaultConfig：查询。
- saveConfig（68）：新增/更新。第一个配置自动设默认；设默认时先清同 provider 其他默认。
- setDefaultConfig（46）：切换默认（先清后设）。
- deleteConfig（167）：硬删除；若删的是默认，自动把下一个设默认。
- canonicalizeProvider：provider 规范化（与 ChatClientFactory 一致）。
- purgeDeletedDuplicate：同名逻辑删除记录先物理删除（避免唯一约束冲突）。

#### 完整调用链路（从阶段7进入）
阶段7 AbstractLLMNodeExecutor.execute：
1. extractConfig → LLMNodeConfig（configId → LLMGlobalConfigService.getById → LLMGlobalConfig → 取 apiUrl/apiKey/model）
2. processTemplate（122）：buildParamValues（input 静态值 / reference 从 runtimeInput 取上游输出）→ replaceTemplateVariables（{{变量}} 替换）→ userPrompt
3. createClientWithFunctions（134）：normalizeProvider → switch provider（OpenAI兼容/apifree/火山）→ normalizeBaseUrl → OpenAiApi+OpenAiChatOptions → OpenAiChatModel → ChatClient
4. chatClient.prompt().user(userPrompt).call().chatResponse()（阶段7 executeNormal）→ Spring AI 调 LLM API → 响应

#### 关键设计点
1. **OpenAI 兼容协议统一**：多厂商共用 /v1/chat/completions，差异只是 baseUrl/apiKey。Spring AI OpenAiApi 支持自定义 baseUrl，一套代码多厂商。
2. **动态创建非单例**：每节点配置不同，运行时创建。ChatClient 是临时对象。
3. **provider 规范化**：中英文别名统一，三处一致（AbstractLLMNodeExecutor/ChatClientFactory/LLMGlobalConfigService）。
4. **normalizeBaseUrl 容错**：用户误填完整接口地址也能工作。
5. **特殊 provider 单独处理**：apifree（text/plain）、火山方舟（自定义路径）。不一刀切。
6. **input vs reference**：input 静态值从配置取，reference 引用上游从 runtimeInput 取。reference 的"节点ID.参数名"取最后段作 key。
7. **user_input fallback**：输入节点输出的是 input，reference 引用 user_input 时 fallback 到 input["input"]。
8. **全局配置多模型字段**：一个配置存 LLM/TTS/向量/图片/视频模型，节点按需取。
9. **默认配置自动管理**：第一个自动默认，切换/删除时自动迁移。

#### 数据流图
```
【LLM 调用完整链路】(阶段7 AbstractLLMNodeExecutor.execute 进入)
1. extractConfig(阶段7):
   configId → LLMGlobalConfigService.getById → LLMGlobalConfig
   → LLMNodeConfig{provider, apiUrl, apiKey, model, promptTemplate, inputParams...}
2. processTemplate(PromptTemplateService):
   buildParamValues:
     input → param.value(静态值)
     reference → runtimeInput[refParamName](上游输出,阶段6 resolveNodeInput 注入)
   replaceTemplateVariables: {{变量}} → 值
   → 最终 userPrompt
3. createClientWithFunctions(ChatClientFactory):
   normalizeProvider(open ai→openai, 通义千问→qwen)
   switch provider:
     OpenAI兼容 → OpenAiApi(baseUrl,apiKey) + OpenAiChatOptions(model,temp) → OpenAiChatModel
     apifree → 自定义 RestClient(支持 text/plain)
     火山方舟 → 自定义路径 /api/plan/v3/chat/completions
   normalizeBaseUrl(剥离 /v1/chat/completions 后缀)
   → ChatClient
4. chatClient.prompt().user(userPrompt).call().chatResponse()
   → Spring AI 调 LLM API → content + token 统计
```

---

## 阶段 9：SSE 实时流式执行 ⭐⭐⭐⭐

**目标**：理解执行过程如何实时推送到前端（调试面板的实时日志）。

**要追的代码**：
1. `controller/ExecutionController.java` 的 `executeWorkflowStream`（SSE 入口，已读）
2. `dto/ExecutionEvent.java`（事件模型：start/success/error/complete）
3. `engine/WorkflowExecutor.java` 的 `executeWithCallback` 方法
4. 前端：`frontend/src/components/DebugDrawer.tsx`（接收 SSE、渲染日志）
5. 前端：`frontend/src/api/workflow.ts` 里的 SSE / EventSource 部分

**引导问题**：
- 后端为什么用 `new Thread(...)` 单独起线程执行？SseEmitter 生命周期怎么管理？
- 每执行完一个节点，`ExecutionEvent` 是在哪触发、怎么 push 出去的？
- 前端 EventSource 怎么按 event name（start/success/error）分别处理？

### 📝 讲解归档（阶段 9）

#### SSE 实时流式执行详解

**ExecutionEvent（事件模型，6 种）**：用工厂方法构造，贯穿执行链。
| 事件类型 | 触发时机 | data |
|---|---|---|
| WORKFLOW_START | 工作流开始 | executionId |
| NODE_START | 节点开始 | —(status=RUNNING) |
| NODE_SUCCESS | 节点成功 | {input, output, duration} |
| NODE_PROGRESS | 流式 LLM 每个 chunk | {chunk, accumulated} |
| NODE_ERROR | 节点失败 | —(message=error) |
| WORKFLOW_COMPLETE | 工作流完成 | output(含总耗时) |

#### 后端 SSE 链路（ExecutionController.executeWorkflowStream）
阶段6/7/8 提到的 eventCallback 的**出口**——事件怎么推到前端：
```java
@GetMapping(value="/{id}/execute/stream", produces=TEXT_EVENT_STREAM_VALUE)
public SseEmitter executeWorkflowStream(id, inputData) {
    SseEmitter emitter = new SseEmitter(300000L);  // 5分钟超时
    emitters.put(emitterId, emitter);
    emitter.onCompletion/onTimeout/onError → emitters.remove(emitterId);  // 生命周期清理

    Consumer<ExecutionEvent> eventCallback = event ->
        emitter.send(SseEmitter.event().name(event.getEventType()).data(event));  // ★推SSE

    new Thread(() -> {  // ★异步线程执行
        WorkflowExecutor executor = engineSelector.selectEngine(workflow);
        executor.executeWithCallback(workflow, inputData, eventCallback);  // 阶段6引擎
        emitter.complete();
    }).start();
    return emitter;  // 立即返回emitter，连接保持
}
```

**三个关键设计**：
1. **SseEmitter（Spring SSE 核心）**：代表到客户端的长连接，`emitter.send()` 推一帧。`produces=TEXT_EVENT_STREAM_VALUE` 让响应是 SSE 流。
2. **new Thread 异步执行**：HTTP 请求-响应阻塞，但工作流执行可能很久。立即返回 emitter 保持连接，新线程跑执行边跑边 send 推进度。**不阻塞 HTTP 线程**。
3. **eventCallback 闭包**：把"推 SSE"封装成回调传给引擎。引擎只管 `eventCallback.accept(event)`，不关心怎么推（解耦）。

**事件触发时机**（WorkflowEngine.executeNodes，阶段6）：workflowStart(67) → 每节点 nodeStart(178) → execute → nodeSuccess(206)/nodeError(226) → workflowComplete(250)。

#### 流式 LLM：executeStreaming 推 NODE_PROGRESS（阶段7）
```java
chatClient.prompt().user(userPrompt).stream().content()
    .doOnNext(chunk -> {  // 每来一个 chunk
        accumulated.append(chunk);
        progressCallback.accept(ExecutionEvent.nodeProgress(nodeId, type, "生成中...",
            {chunk, accumulated: accumulated.toString()}));  // ★推 NODE_PROGRESS
    })
    .blockLast();
```
LLM 逐字生成，每来一个 chunk 推 NODE_PROGRESS，前端"打字机"效果。

#### 前端 SSE 接收（api/workflow.ts executeWorkflowStream）
```ts
const token = await ensureValidAccessToken();
const url = buildBackendUrl(`/api/workflows/${id}/execute/stream?inputData=...&token=${token}`);
const eventSource = new EventSource(url);  // ★建立 SSE 连接
eventSource.addEventListener('WORKFLOW_START', e => onEvent(JSON.parse(e.data)));
eventSource.addEventListener('NODE_START', ...);
eventSource.addEventListener('NODE_SUCCESS', ...);
eventSource.addEventListener('NODE_PROGRESS', ...);  // 流式 chunk
eventSource.addEventListener('NODE_ERROR', ...);
eventSource.addEventListener('WORKFLOW_COMPLETE', e => { onEvent(...); eventSource.close(); onComplete(); });
eventSource.onerror = () => { /* 认证失败/连接中断 */ };
```

**关键设计**：
1. **token 放 query 参数**：`EventSource` API **不能设自定义请求头**（不能加 Authorization）。所以 token 走 query。后端 `AuthInterceptor.preHandle` 有 `request.getParameter("token")` 兜底（阶段3）——**这就是拦截器支持 query token 的原因**。
2. **按 event name 分发**：addEventListener 的 name 对应后端 emitter.send 的 name。每种事件单独处理。
3. **WORKFLOW_COMPLETE 关连接**：完成后 eventSource.close() 释放资源。

#### 前端 DebugDrawer 渲染（事件 → UI）
DebugDrawer.handleExecute 调 executeWorkflowStream，onEvent 按事件类型更新 UI：
```tsx
switch (event.eventType) {
  case 'WORKFLOW_START': activeExecutionId = event.data; addLog('🚀 工作流开始');
  case 'NODE_START': tempNodeStatusMap.set(nodeId, {status:'RUNNING'}); addLog('📍 节点开始...');
  case 'NODE_SUCCESS': 解析耗时; 设 {status:'SUCCESS', input, output}; addNodeSuccessLog ✅
  case 'NODE_PROGRESS': addProgressLog(event);  // 📊 流式 chunk
  case 'NODE_ERROR': 设 {status:'FAILED', error}; addLog('❌ 失败');
  case 'WORKFLOW_COMPLETE': setExecutionResult(最终结果);
}
```
渲染区域：执行状态（进度条+Tag）/ 节点执行结果（折叠面板，输入/输出支持 Markdown/JSON）/ 最终输出（智能识别图片`<img>`/视频`<video>`/音频`AudioPlayer`/Markdown）/ 执行日志（实时滚动）。**断点续跑按钮**：失败时显示"从失败节点继续执行"，调 resumeWorkflowExecution（阶段6 resumeExecution）。

#### 关键设计点
1. **SSE vs WebSocket**：SSE 单向（服务端→客户端）基于 HTTP 简单；WebSocket 双向。本项目只需服务端推送进度，SSE 够用且简单。
2. **SseEmitter + new Thread**：立即返回 emitter 保持长连接，新线程异步执行推送。不阻塞 HTTP 线程。
3. **token 走 query**：EventSource 不能设自定义头，query 传 token，后端拦截器 getParameter("token") 兜底。**这就是阶段3 拦截器支持 query token 的原因**。
4. **事件驱动解耦**：引擎只管 eventCallback.accept(event)，不关心怎么推；前端按 event name 自己决定怎么渲染。后端逻辑与展示分离。
5. **流式 LLM 体验**：executeStreaming 用响应式 doOnNext 推 chunk，前端"打字机"效果，不用等 LLM 全部生成完。
6. **emitters ConcurrentHashMap**：管理多个并发执行的 emitter，按 emitterId（含时间戳）区分。onCompletion/onTimeout/onError 清理防泄漏。
7. **断点续跑闭环**：DebugDrawer 失败后显示"继续"按钮 → resumeWorkflowExecution → 后端 resumeExecution（阶段6 从快照恢复）。

#### 完整链路图
```
【后端推送】
前端点"执行工作流" → GET /api/workflows/{id}/execute/stream?inputData=...&token=...
 → ExecutionController.executeWorkflowStream
   new SseEmitter(300s) + emitters.put(emitterId, emitter)
   new Thread(异步):
     engineSelector.selectEngine → executor.executeWithCallback(workflow, inputData, eventCallback)
     eventCallback = event → emitter.send(name=event.eventType, data=event)  ★推SSE
   → WorkflowEngine.executeWithCallback → executeNodes 循环:
       eventCallback(workflowStart) → SSE: WORKFLOW_START
       每节点:
         eventCallback(nodeStart) → SSE: NODE_START
         executor.execute(node, input, callback)
           (LLM流式 executeStreaming → doOnNext → eventCallback(nodeProgress) → SSE: NODE_PROGRESS)
         eventCallback(nodeSuccess) → SSE: NODE_SUCCESS
         异常: eventCallback(nodeError) → SSE: NODE_ERROR
       eventCallback(workflowComplete) → SSE: WORKFLOW_COMPLETE
     emitter.complete()

【前端接收】
api/workflow.ts executeWorkflowStream:
  ensureValidAccessToken → token
  new EventSource(buildBackendUrl(...?inputData=...&token=token))
  addEventListener 按 event name 分发 → onEvent(JSON.parse(e.data))
  WORKFLOW_COMPLETE → close + onComplete

DebugDrawer.handleExecute:
  executeWorkflowStream(workflowId, inputData, onEvent, onComplete, onError)
  onEvent switch:
    WORKFLOW_START → 记 executionId, addLog 🚀
    NODE_START → 设 RUNNING, addLog 📍
    NODE_SUCCESS → 设 SUCCESS+input/output, addLog ✅
    NODE_PROGRESS → addProgressLog 📊(流式chunk)
    NODE_ERROR → 设 FAILED, addLog ❌
    WORKFLOW_COMPLETE → setExecutionResult 最终
  渲染: 进度条 + 节点结果折叠 + 最终输出(图/视频/音频/Markdown) + 日志流
```

---

## 阶段 10：LangGraph4j 状态图引擎（第二引擎）⭐⭐⭐

**目标**：理解第二引擎如何在不改动已有节点执行器的前提下，用适配器模式接入。

**要追的代码**：
1. `engine/langgraph/LangGraphWorkflowEngine.java`（引擎实现）
2. `engine/langgraph/builder/GraphBuilder.java`（构建 StateGraph）
3. `engine/langgraph/adapter/NodeAdapter.java`（⭐ 把 NodeExecutor 适配成 AsyncNodeAction）
4. `engine/langgraph/state/StateManager.java` + `WorkflowState.java`（状态管理）

**引导问题**：
- LangGraph 引擎和 DAG 引擎都实现了 `WorkflowExecutor`，`getEngineType()` 分别返回什么？
- `NodeAdapter` 如何零改动复用已有的 `NodeExecutor`？适配器模式体现在哪？
- 条件分支/动态路由在 LangGraph 里怎么表达？和 DAG 引擎的条件节点有何不同？

### 📝 讲解归档（阶段 10）

#### LangGraph4j 第二引擎详解（适配器模式）

**五文件分工**：LangGraphWorkflowEngine(引擎实现，getEngineType="langgraph") / GraphBuilder(WorkflowConfig→StateGraph) / NodeAdapter(★适配器：NodeExecutor→AsyncNodeAction) / StateManager(状态初始化/提取) / WorkflowState(状态模型)。

#### 双引擎对照（与阶段6 DAG）
LangGraphWorkflowEngine 和 WorkflowEngine(DAG) 都 implements WorkflowExecutor：

| | DAG 引擎(阶段6) | LangGraph 引擎(阶段10) |
|---|---|---|
| getEngineType() | "dag" | "langgraph" |
| 图调度 | 自研 Kahn 拓扑排序+for 循环 | LangGraph4j 库 StateGraph |
| 状态传递 | nodeOutputs Map + currentInput 链式 | state Map(currentInput/nodeOutputs/status) |
| 执行方式 | 手动 for 遍历 sortedNodes | compiledGraph.invoke(state) 库负责遍历 |
| 入口出口 | 拓扑排序自然有序 | 无入边=入口,无出边=出口 |
| 节点执行 | executorFactory.getExecutor(type).execute | **同样**调 NodeExecutor(经 NodeAdapter 适配) |

**关键**：两者都调阶段7的 NodeExecutor！LangGraph 通过 NodeAdapter 适配，**节点执行器零改动复用**。

#### LangGraphWorkflowEngine 执行流程（executeWithCallback, 53）
1. eventCallback(workflowStart)(67)
2. workflowConfigParser.parse(flowData) → WorkflowConfig(71)
3. graphBuilder.buildGraph(config, callback) → CompiledGraph(76)
4. stateManager.initializeState(inputData) → 初始 state(79)
5. compiledGraph.invoke(state) → 执行图 → finalState(83)
6. stateManager.isSuccessful 检查(96)
7. getFinalOutput/extractNodeResults 提取(102/106)
8. INSERT execution_record(125)
9. eventCallback(workflowComplete)(129)
10. 构建 ExecutionResponse

#### GraphBuilder（构建 StateGraph）
```java
StateGraph<AgentState> graph = new StateGraph<>(AgentState::new);
addNodes(graph, nodes, callback);     // 每节点 NodeAdapter 适配成 NodeAction
addEdges(graph, edges);               // source→target
setEntryAndExit(graph, nodes, edges); // START→入口, 出口→END
return graph.compile();               // 编译成 CompiledGraph
```
**入口出口自动识别**：findEntryNode(129) 没入边的节点=入口，graph.addEdge(START, entryNode)；findExitNode(144) 没出边的节点=出口，graph.addEdge(exitNode, END)。类比 DAG 入度为 0 找起点。

#### NodeAdapter（★适配器模式，核心）
阶段10 灵魂。LangGraph4j 要求节点是 `AsyncNodeAction<AgentState>`（返回 CompletableFuture<Map>），但阶段7 NodeExecutor.execute 返回 Map<String,Object>。**接口不兼容**，NodeAdapter 适配：
```java
public AsyncNodeAction<AgentState> adaptNode(WorkflowNode node, Consumer<ExecutionEvent> callback) {
    return (AgentState state) -> {  // LangGraph 要求的 AsyncNodeAction
        // 1. 从 state 取 currentInput
        Map<String,Object> currentInput = state.data().get("currentInput");
        // 2. ★为 output 节点注入 __nodeOutputs__(reference 引用需要)
        if ("output".equals(node.getType())) {
            currentInput.put("__nodeOutputs__", state.data().get("nodeOutputs"));
        }
        // 3. 调用已有 NodeExecutor(阶段7，零改动!)
        NodeExecutor executor = executorFactory.getExecutor(node.getType());
        Map<String,Object> output = executor.execute(node, currentInput, callback);
        // 4. 更新 state:存 nodeOutputs + currentInput 流转
        newStateData.put("nodeOutputs", nodeOutputs.put(node.getId(), output));
        newStateData.put("currentInput", output);  // 链式传递给下一节点
        // 5. 触发事件(和 DAG 引擎一致)
        callback.accept(nodeStart / nodeSuccess / nodeError);
        return CompletableFuture.completedFuture(newStateData);  // LangGraph 要求的返回
    };
}
```

**适配器模式体现**：
- **目标接口**：AsyncNodeAction<AgentState>（LangGraph4j 要求，异步返回 CompletableFuture）
- **被适配者**：NodeExecutor（阶段7，同步返回 Map）
- **适配器**：NodeAdapter 负责转换——从 state 取输入 → 调 NodeExecutor → 输出存回 state → 包装成 CompletableFuture

**零改动复用**：阶段7的 AbstractLLMNodeExecutor/InputNodeExecutor/OutputNodeExecutor/ConditionNodeExecutor 全部不用改，NodeAdapter 桥接。加新执行器两个引擎自动都能用。

**__nodeOutputs__ 注入**（59-65）：为 output 节点注入全量 nodeOutputs，和阶段6 DAG 的 resolveNodeInput 注入一致。**前后端 reference 闭环，两个引擎行为一致**。

#### StateManager + WorkflowState（状态模型）
- **StateManager**：initializeState(26) 建 currentInput:{input:inputData}+nodeOutputs:{}+status:RUNNING；getFinalOutput(89) 取最终 currentInput；extractNodeResults(127) 从 nodeOutputs 转 NodeResult 列表；isSuccessful(104) 检查 status。
- **WorkflowState**：currentNodeId/globalContext/nodeOutputs/status/errorMessage/inputData，封装状态访问。
- **状态传递类比 DAG**：DAG 用 nodeOutputs Map + currentInput 链式(阶段6)，LangGraph 用 state Map 装同样的 currentInput/nodeOutputs。**本质相同，载体不同**（DAG 局部变量 vs LangGraph state Map）。

#### 关键设计点
1. **接口统一+开闭原则**：LangGraphWorkflowEngine implements WorkflowExecutor，EngineSelector 按 engineType 路由(阶段6)。加新引擎只需实现接口+getEngineType()，不改选择器。
2. **适配器模式零改动复用**：NodeAdapter 桥接 LangGraph AsyncNodeAction 和 NodeExecutor。阶段7全部执行器不用改，两个引擎共享。**适配器模式标准应用**。
3. **状态模型对照 DAG**：DAG 用局部变量(nodeOutputs+currentInput)，LangGraph 用 state Map。本质相同载体不同。
4. **入口出口自动识别**：无入边=入口，无出边=出口。类比 DAG 入度为 0。
5. **invoke 同步执行**：compiledGraph.invoke(state) 让 LangGraph4j 负责图遍历，不用手动 for。库处理调度。
6. **事件回调一致**：NodeAdapter 触发相同 nodeStart/nodeSuccess/nodeError，**前端 SSE 无感知引擎差异**(阶段9 同一套 DebugDrawer 适用两引擎)。
7. **__nodeOutputs__ 注入一致**：output 节点注入全量，reference 闭环。两引擎行为统一。
8. **与 DAG 定位差异**：DAG 自研简单可控(拓扑排序+for)；LangGraph 用库支持复杂状态图(循环/条件分支/动态路由)。当前 LangGraph 实现较简化，主要价值是**双引擎架构**和**适配器复用**。

#### 完整链路图
```
EngineSelector(engineType="langgraph") → LangGraphWorkflowEngine.executeWithCallback
  1. parse(flowData) → WorkflowConfig
  2. graphBuilder.buildGraph(config, callback):
     addNode: 每节点 NodeAdapter.adaptNode → AsyncNodeAction
     addEdge: source → target
     setEntryAndExit: START → 入口(无入边), 出口(无出边) → END
     compile → CompiledGraph
  3. stateManager.initializeState(inputData) → state{currentInput:{input}, nodeOutputs:{}, status:RUNNING}
  4. compiledGraph.invoke(state) → 执行图:
     每节点 NodeAdapter:
       取 state.currentInput
       (output节点注入 __nodeOutputs__)
       executorFactory.getExecutor(type).execute(node, currentInput, callback)  ← 阶段7执行器
       存 state.nodeOutputs[nodeId]=output, state.currentInput=output  ← 链式流转
       eventCallback(nodeStart/nodeSuccess/nodeError)  ← 与DAG一致
  5. finalState → getFinalOutput(currentInput) + extractNodeResults(nodeOutputs)
  6. INSERT execution_record
  7. eventCallback(workflowComplete)
```

---

## 阶段 11：Skills 技能系统 ⭐⭐⭐

**目标**：理解声明式技能定义 + 三级渐进式加载 + Spring AI Function 集成。

**要追的代码**：
1. `backend/src/main/resources/skills/ai-podcast/SKILL.md`（先看一个真实技能长啥样）
2. `engine/skill/Skill.java`（技能模型）
3. `engine/skill/SkillLoader.java`（解析 SKILL.md 的 YAML Frontmatter）
4. `engine/skill/SkillRegistry.java`（启动扫描 + ConcurrentHashMap 缓存）
5. `engine/skill/LoadSkillDetailFunction.java` / `LoadSkillReferenceFunction.java`（Spring AI FunctionCallback）
6. `controller/SkillController.java`
7. 前端：`frontend/src/components/SkillSelector.tsx`

**引导问题**：
- "三级渐进式加载"（摘要→详情→引用）为什么能省 Token？分别在什么时候加载？
- LLM 是怎么"自主"决定调用某个技能的？FunctionCallback 机制怎么工作？

### 📝 讲解归档（阶段 11）

#### 一、整体定位：技能系统解决什么问题

一句话：把"领域最佳实践"从代码里抽出来，变成**声明式的 Markdown 文档**，LLM 按需加载使用。

类比：Spring 里你写 `@Service` 类是把业务逻辑封装；这里你写一份 `SKILL.md` 是把"怎么做某类任务的方法论"封装。区别在于——技能不是给 Java 代码调用的，是**给 LLM 读**的。LLM 读了技能，就知道"生成播客脚本要分开场白/主体/互动/结尾，1分钟150-180字，口语化"。

为什么需要？同一个 LLM，给不给方法论，输出质量天差地别。直接让它"写播客脚本"，它会写出书面语、超长、没结构的文字。给它一份 ai-podcast 技能（固定双人对话、150字、四段结构），它就能稳定产出合格脚本。**技能 = 可复用的 prompt 工程资产**。

#### 二、声明式技能定义：SKILL.md 长啥样

真实技能 `skills/ai-podcast/SKILL.md`：

```markdown
---
name: ai-podcast
description: 生成专业播客脚本，包含开场白、话题展开、问答环节和结尾...
---

# AI 播客脚本生成

## 执行规则
**重要**：你必须直接根据用户的提示词生成播客脚本，绝对不要反问用户任何问题。

## 固定参数（不可更改）
| 参数 | 固定值 |
| 播客风格 | 双人对话（主持人A和主持人B）|
| 时长要求 | 1分钟（约150-180字）|
| 目标听众 | 程序员/技术人员 |

## 脚本结构
### 1. 开场白 ...
### 2. 主体内容 ...
### 3. 互动环节 ...
### 4. 结尾 ...

## 可用的参考文档
- script-template: 完整的播客脚本模板
- voice-guide: 语音风格指南
- structure-patterns: 不同类型的结构模式
```

结构两部分：
1. **YAML frontmatter**（顶部 `---` 之间）：元数据，只有 `name` 和 `description`。机器读的（注册中心建索引）。
2. **Markdown 主体**（下面）：给人/LLM 读的方法论。

Java 类比：frontmatter 像 Java 注解 `@Skill(name="ai-podcast", description="...")`，主体像注解修饰的类里的方法体。只不过这里"方法体"是自然语言而非 Java 代码。

目录里还有 `reference/` 子目录，放更细的参考文档（模板、语音指南）。技能本体只列文件名，内容按需加载——这就是"渐进式"的体现。

#### 三、数据模型：Skill.java

`Skill` 是加载后的技能对象，6 个字段：

```java
@Data @Builder
public class Skill {
    private String name;              // frontmatter 解析
    private String description;       // frontmatter 解析
    private String content;           // SKILL.md 主体(去 frontmatter)
    private Path skillPath;           // 技能目录路径(用于加载 reference)
    private List<String> references; // reference 文件名列表(不含 .md)
}
```

关键不是字段，是 **3 个拼 Prompt 的方法**——根据场景给不同详略程度：

| 方法 | 用途 | 内容 |
|------|------|------|
| `getSummary()` | 列表展示 | name + description + 主体 + reference 文件名列表 |
| `getFullContent()` | 详情查看 | name + 主体 + reference 文件名列表（不含 reference 内容） |
| `getFullExecutionPrompt(refs)` ★ | 实际执行 | name + description + 主体 + **所有 reference 内容直接内嵌** |

第三个是节点执行器实际用的。把 references（Map<文件名,内容>）全塞进 prompt，LLM 一次拿全：

```java
public String getFullExecutionPrompt(Map<String, String> referenceContents) {
    StringBuilder sb = new StringBuilder();
    sb.append("# 技能: ").append(name).append("\n\n");
    sb.append(description).append("\n\n---\n\n");
    sb.append("## 技能指南\n\n").append(content).append("\n\n");
    if (referenceContents != null && !referenceContents.isEmpty()) {
        sb.append("## 参考文档\n\n");
        for (Map.Entry<String, String> entry : referenceContents.entrySet()) {
            sb.append("### ").append(entry.getKey()).append("\n\n");
            sb.append(entry.getValue()).append("\n\n");
        }
    }
    return sb.toString();
}
```

#### 四、加载链路：SkillLoader + SkillRegistry

**SkillLoader——解析单个 SKILL.md**

两个入口：
- `load(Path skillPath)`：从文件系统目录加载（开发时）
- `loadFromContent(content, references, sourceName)`：从 classpath 资源内容加载（jar 部署时）

核心是 `parseSkill()`——用正则切 frontmatter：

```java
private static final Pattern FRONTMATTER_PATTERN = Pattern.compile(
    "^---\\s*\\n([\\s\\S]*?)\\n---\\s*\\n([\\s\\S]*)$"
);
// group(1) = frontmatter(YAML), group(2) = 主体(Markdown)
```

`parseFrontmatter()` 简单按行 split 冒号解析键值对，**不引入 SnakeYAML 依赖**——因为 frontmatter 只有 name/description 两个字段，杀鸡不用牛刀。这是"简洁优先"原则。

`loadReferenceList()`：扫描 `reference/` 目录下的 `.md` 文件名（去掉后缀），排序返回。

`loadReference(skillPath, referenceName)`——加载单个 reference 内容，**带路径遍历防护**：

```java
Path referenceDir = skillPath.resolve("reference").normalize();
Path referenceFile = referenceDir.resolve(referenceName + ".md").normalize();
if (!referenceFile.startsWith(referenceDir)) {
    throw new IOException("Invalid reference path: " + referenceName);
}
```

`normalize()` 会消除 `../` 之类的路径穿越，`startsWith()` 保证最终文件还在 reference 目录内。双重防护防 `../../../etc/passwd` 攻击。

**SkillRegistry——注册中心（★核心）**

Spring `@Component`，启动时自动扫描所有技能，运行时提供查询。

启动加载（`@PostConstruct init()`）：

```java
@PostConstruct
public void init() {
    int classpathLoaded = loadFromClasspath();
    if (classpathLoaded > 0) {
        return;  // classpath 加载到就用它
    }
    loadFromFileSystem();  // 降级到文件系统
}
```

**classpath 优先 + 文件系统降级**：
- jar 部署：技能打包进 jar 的 `classpath:skills/`，用 `PathMatchingResourcePatternResolver.getResources("classpath*:skills/*/SKILL.md")` 扫描
- 开发时：从源码目录 `backend/src/main/resources/skills/` 读

`getSkillsPath()` 还会试多个位置（user.dir / backend/src/main/resources / src/main/resources），保证不同启动目录都能找到。

两个缓存（`ConcurrentHashMap`）：
- `skills`：技能本体（name → Skill），启动加载后不变
- `referenceCache`：reference 内容（name → {refName → content}），首次加载后缓存

运行时查询：
- `getSkill(name)` → Optional<Skill>
- `getSkillSummaries()` → [{name, description}] 列表（给前端展示）
- `loadReference(skillName, referenceName)` → 单个 reference 内容（带缓存）
- `loadAllReferences(skillName)` → 全部 reference（Map，带缓存）

`loadReference` 三重安全：
1. skill 必须存在
2. `SAFE_REFERENCE_NAME` 正则白名单 `^[a-zA-Z0-9._-]+$`（防特殊字符注入）
3. referenceName 必须在 `skill.getReferences()` 列表里（防任意文件读）
4. （SkillLoader 里还有）normalize + startsWith 路径遍历防护

#### 五、三级渐进式披露（progressive disclosure）★

这是技能系统的设计灵魂。

三个粒度，对应三种场景：

| 级别 | 触发 | 返回 | Token 成本 | 场景 |
|------|------|------|-----------|------|
| L1 摘要 | GET /api/skills | [{name, description}] | 极低 | 前端技能列表展示 |
| L2 详情 | load_skill_detail | 主体 + reference 文件名列表 | 中 | LLM 知道技能细节 |
| L3 参考 | load_skill_reference | 单个 reference 文件内容 | 按需 | LLM 需要具体模板 |

**为什么能省 Token？**

假设 10 个技能，每个 3 个 reference，每个 reference 5000 字。全加载：10×3×5000 = 15 万字塞进 prompt——token 爆炸，且 LLM 注意力被稀释（找不到重点）。

渐进式：L1 只给 10 个 name+description（几百字），LLM 知道有哪些技能；L2 只给要用的那 1 个的主体（几千字）+ reference 文件名列表；L3 只给真正需要的 reference（5000 字）。实际可能只走 L1+L2，或 L1+L2+L3（其中一个），总 token 大幅下降。

**Java 类比**：像懒加载（Lazy Initialization）。不用 `@PostConstruct` 全 new 出来，用到哪个 new 哪个。这里是不全塞 prompt，用到哪份文档加载哪份。

#### 六、双套工具：Function vs Tool

项目里有两套"加载技能"的工具实现，这是要诚实指出的设计现状：

**套装一：LoadSkillDetailFunction / LoadSkillReferenceFunction**

`implements FunctionCallback`（Spring AI 原生接口）。给 Spring AI 的 ChatClient 用，走 LLM 原生 Function Calling 协议。

```java
public class LoadSkillDetailFunction implements FunctionCallback {
    @Override public String getName() { return "load_skill_detail"; }
    @Override public String getInputTypeSchema() { return "{...JSON Schema...}"; }
    @Override public String call(String functionInput) {
        String skillName = parseSkillName(functionInput);
        return skillRegistry.getSkill(skillName)
            .map(skill -> skill.getFullContent())
            .orElse("错误：未找到技能 '" + skillName + "'");
    }
}
```

机制：LLM 收到 system prompt 里告知"有这些函数可用"，LLM 自己决定要不要调、调哪个、传什么参数。返回值喂回 LLM 继续推理。这是 LLM"自主"调用技能的标准机制。

**套装二：LoadSkillDetailTool / LoadSkillReferenceTool**

`implements AgentTool`（项目自研接口，在 `engine/agent/`）。给 ReAct Agent 用（阶段 12）。

```java
@Component
public class LoadSkillDetailTool implements AgentTool {
    @Override public String getName() { return "load_skill_detail"; }
    @Override public Map<String, Object> execute(Map<String, Object> arguments, AgentToolContext context) {
        // 返回 Map 而非 String
    }
}
```

返回 `Map<String,Object>`（结构化），而非 Function 的 `String`。因为自研 ReAct 循环对工具返回值的处理和 Spring AI 不同。

**为什么两套？**

因为项目有两条 LLM 调用链路：
- **工作流节点**（AbstractLLMNodeExecutor）→ Spring AI ChatClient → 配 Spring AI FunctionCallback
- **ReAct Agent**（ReActAgentNodeExecutor，阶段 12）→ 自研推理循环 → 用自研 AgentTool

两套机制不同，所以技能工具也分两套。名字相同（`load_skill_detail`），实现不同。

#### 七、集成点：节点执行器怎么用技能（★关键，有演进）

`AbstractLLMNodeExecutor.execute()` 第 96-119 行：

```java
// 2. 获取关联的 Skill（如果有）
Optional<Skill> skill = Optional.empty();
Map<String, String> skillReferences = new HashMap<>();
List<FunctionCallback> functions = new ArrayList<>();

if (config.getSkillName() != null && !config.getSkillName().isBlank()) {
    skill = skillRegistry.getSkill(config.getSkillName());
    if (skill.isPresent()) {
        // 直接加载所有 references，打包进 Prompt
        skillReferences = skillRegistry.loadAllReferences(config.getSkillName());
        // 不再需要注册函数，直接打包所有内容
        // functions.add(new LoadSkillDetailFunction(skillRegistry));      // 注释掉了
        // functions.add(new LoadSkillReferenceFunction(skillRegistry));   // 注释掉了
    }
}

// 3. 构建系统提示（直接包含所有 Skill 内容）
String systemPrompt = buildSystemPrompt(skill, skillReferences);
```

`buildSystemPrompt`：

```java
if (skill.isPresent()) {
    sb.append(skill.get().getFullExecutionPrompt(references));  // 全打包
}
```

**这里有个重要的设计演进，要诚实讲**：

设计上预留了"渐进式 Function 调用"（LoadSkillDetailFunction/LoadSkillReferenceFunction 类还在，代码完整）。但节点执行器这条链路，**实际把 Function 注册注释掉了，改成直接打包所有 references 进 system prompt**。

权衡：
- 渐进式（Function）：省 token，但要 LLM 多轮调用——慢、可能调错参数、不确定
- 直接打包：费 token，但快、确定、一次出结果

工作流节点追求**确定性和速度**（节点要稳定输出），选了直接打包。而 LoadSkillDetailTool/LoadSkillReferenceTool（AgentTool 版本）留给 ReAct Agent 用，那里需要 LLM 自主探索。

所以引导问题 2 的诚实回答：**当前节点执行器里，LLM 不是"自主"调用技能的——是后端在执行前直接把技能内容打包进 system prompt。FunctionCallback 机制代码完整存在（给未来或 Agent 链路用），但工作流节点这条链路走的是直接打包。**

`LLMNodeConfig` 里 `skillName` 字段来自节点配置 `node.data.skillName`（前端编排时用户选的技能），`extractConfig()` 第 489 行 `config.setSkillName(trimString(data.get("skillName")))` 提取。

#### 八、REST API：SkillController

3 个接口，给前端编排界面用：

| 接口 | 方法 | 作用 |
|------|------|------|
| GET /api/skills | listSkills | 技能摘要列表（name+description），前端下拉选 |
| GET /api/skills/{name} | getSkill | 技能完整详情 |
| GET /api/skills/{skillName}/references/{referenceName} | getSkillReference | 单个 reference 内容 |

前端用户在 LLM 节点配置里，GET /api/skills 拉列表 → 选一个 → skillName 存入节点 data。执行时后端按 skillName 查注册中心。

**Controller 执行细节**：
- `listSkills`：`getSkillSummaries()` 遍历 skills Map 转 `SkillSummary(name,description)`,按 name 排序——只给摘要,省 token(渐进式披露 L1)。
- `getSkill(name)`：用 `Optional` 优雅处理不存在——
  ```java
  return skillRegistry.getSkill(name)
          .map(Result::success)                              // 存在 → 200 + Skill(含 content)
          .orElse(Result.error(404, "Skill not found: "+name)); // 不存在 → 404
  ```
  这是项目里少见的 Optional.map/orElse 404 模式。
- `getSkillReference(skillName, referenceName)`：方法体 try-catch,异常一律转 404。内部走 `SkillRegistry.loadReference` 的三层校验(skill 存在 → referenceName 匹配 `^[a-zA-Z0-9._-]+$` → 在 references 列表里)+ `referenceCache` 缓存(命中直接返回,未命中读文件再缓存)。Controller 层 try-catch 把所有 IOException 兜成 404,不暴露内部错误。

**架构定位（与其他 Controller 对比）**：SkillController 直接依赖 `SkillRegistry`（引擎运行时组件）而非 MyBatis-Plus Service、不查 DB。技能是文件系统只读 Markdown,所以**只有查询接口、没有增删改**。

| | McpToolConfig/Media/NodeDefinition | SkillController |
|---|---|---|
| 依赖 | Service(查 DB) | SkillRegistry(查内存) |
| 数据源 | 数据库 | 文件系统 Markdown |
| 接口 | CRUD + 查询/上传 | 纯查询,无增删改 |
| 扩展方式 | INSERT 数据 | 加 `skills/xxx/SKILL.md` 重启 |

这是项目里唯一一个"数据源是文件系统而非数据库"的查询型 Controller。

#### 九、完整数据请求链路

**链路 A：启动加载技能**

```
Spring 启动
  → SkillRegistry @PostConstruct init()
  → loadFromClasspath()
    → PathMatchingResourcePatternResolver.getResources("classpath*:skills/*/SKILL.md")
    → 对每个 SKILL.md:
        readResource(读字节转 UTF-8)
        loadClasspathReferences(同时读 reference/*.md 内容)
        → skillLoader.loadFromContent(content, references, sourceName)
          → parseSkill:正则切 frontmatter → parseFrontmatter(按行 split 冒号)
          → Skill.builder().name().description().content().references().build()
        → register(skill)  存入 skills Map
        → referenceCache.put(skillName, references)
```

**链路 B：工作流执行用技能（★核心）**

```
前端编排:用户在 LLM 节点选技能 skillName → 存入 node.data.skillName
  ↓ flow_data JSON 整存
执行:WorkflowExecutor → AbstractLLMNodeExecutor.execute(node, input)
  → extractConfig():config.setSkillName(data.get("skillName"))
  → if skillName 非空:
      skillRegistry.getSkill(skillName)          // 查缓存
      skillRegistry.loadAllReferences(skillName) // 读所有 reference(带缓存)
  → buildSystemPrompt():skill.getFullExecutionPrompt(references)  // 全打包
  → systemPrompt + userPrompt → ChatClient → LLM
  → LLM 按 SKILL.md 指南(四段结构/150字/口语化)生成结果
  → buildOutput() → 节点输出
```

**链路 C：前端查技能列表**

```
前端 SkillSelector 组件
  → GET /api/skills
  → SkillController.listSkills()
  → skillRegistry.getSkillSummaries()
  → 返回 [{name:"ai-podcast", description:"..."}]
  → 前端渲染下拉
```

#### 十、关键设计点总结

1. **声明式**：技能是 Markdown 文档不是 Java 代码，新增技能不用改代码——加个 `skills/xxx/SKILL.md` 重启即可
2. **YAML frontmatter 简易解析**：只两个字段，正则+按行解析，不引 SnakeYAML
3. **classpath 优先 + 文件系统降级**：jar 部署和开发都可用
4. **三级渐进式披露**：L1摘要/L2详情/L3参考，省 token（设计意图）
5. **节点执行器实际走直接打包**（非渐进式）：getFullExecutionPrompt 全塞 system prompt，求确定性。Function 代码留存但注释
6. **双套工具**：FunctionCallback（Spring AI，给 ChatClient）+ AgentTool（自研，给 ReAct Agent）
7. **三重安全**：正则白名单 + referenceName 白名单 + normalize/startsWith 路径遍历防护
8. **双缓存**：skills（本体）+ referenceCache（reference 内容），避免重复读文件

---

---

## 阶段 12：扩展功能（按兴趣选学）⭐⭐

学完前面主线后，这些是同构的扩展，可挑感兴趣的追：

- **知识库 / RAG**：`controller/KnowledgeBaseController.java` → `service/KnowledgeBaseService.java` → `engine/executor/impl/KnowledgeRetrieveNodeExecutor.java` / `KnowledgeUpsertNodeExecutor.java`
- **ReAct Agent 与工具**：`engine/executor/impl/ReActAgentNodeExecutor.java` + `engine/agent/`（AgentTool / AgentToolRegistry + 各 tool 实现）+ `docs/react-agent-phases.md`
- **MCP 工具集成**：`controller/McpToolConfigController.java` → `service/McpToolConfigService.java` / `SearchInfinityMcpClient.java`
- **媒体生成**（图/视频/TTS）：`controller/MediaController.java` + `service/*ImageClient.java` / `AgnesVideoClient.java` + `engine/executor/impl/ImageGenerateNodeExecutor.java` / `VideoGenerateNodeExecutor.java` / `TTSNodeExecutor.java`
- **Agent Plan（火山引擎）**：`service/VolcengineAgentPlanClient.java` + `AgentPlanConfigResolver.java` + `docs/agent-plan-harness-integration-plan.md`
- **断点续执行 / 执行快照**：`entity/ExecutionSnapshot.java` + `docs/resume.md` + `ExecutionController` 的 `resumeExecution`

### 📝 讲解归档（阶段 12）

#### 知识库 / RAG 模块详解（KnowledgeBaseController）

**模块定位**：RAG 的"建库"与"检索"。建库=文档→切片→每片算向量→存；检索=问题算向量→比相似度→取 topK→喂 LLM。

**9 个接口**：GET/POST `/api/knowledge-bases`(列表/创建)、GET/DELETE `/{id}`(详情/删除)、POST `/{id}/documents/text|upload`(导入文本/上传文件)、GET `/{id}/documents`(文档列表)、POST `/{id}/documents/{docId}/preview-chunks`(预览分片)、POST `/{id}/documents/{docId}/index`(建立索引)、POST `/{id}/search`(检索测试)。

**前端交互**（KnowledgePage.tsx）：三栏布局(列表+详情+弹窗)。进页面 loadBases → 选中 loadBaseDetail → 新建/导入/预览/索引/检索 各调对应 API。导入两 tab：粘贴文本 importKnowledgeText / 上传文件 uploadKnowledgeTextFile(FormData multipart)。

**四条核心数据流**：

1. **创建知识库**（createKnowledgeBase, 91）：new KnowledgeBase + set(chunkSize/向量模型/configId) + status=DRAFT + 计数0 → INSERT knowledge_base。此时空库。
2. **导入文档**（importText 108 / uploadTextFile 124）：new KnowledgeDocument + set rawText + status=IMPORTED → INSERT knowledge_document → refreshBaseStats 更新统计。存了原文但没分片没向量。uploadTextFile 读文件字节转 UTF-8 再复用 importText。
3. **建立索引**（indexDocument, 170，★核心）：
   - createTask(RUNNING, progress=0)
   - splitContent(407)：原文按 chunkSize 滑动窗口切片，step=size-overlap 有重叠
   - markOldChunksDeleted：旧分片 deleted=1（逻辑删）
   - resolveKnowledgeConfig：解析向量模型 apiUrl/apiKey/model
   - 循环每片：agentPlanClient.createEmbedding(火山API)算向量 → INSERT knowledge_chunk(content+embedding, READY) → 更新 task.progress
   - document=READY, task=SUCCESS → refreshBaseStats(chunkCount)
   - 异常：document/task=FAILED
   - 一致性副作用：catch 吞异常不 rethrow，@Transactional 不回滚 → 已插入的 READY chunk 残留（document 标 FAILED 但底下有 READY 块），且残留块会被 refreshBaseStats 计入 chunkCount。若非预期，可在 catch 里 rethrow 让事务回滚，或失败分支把已插 chunk 也清掉
4. **检索测试**（search 222 → retrieve 293，★核心）：createEmbedding(query)算问题向量 → 查 READY chunks → 每片 score=max(向量余弦, 文本相关度)混合 → 过滤 threshold + 降序取 topK → 拼 context → 返回 {chunks, citations, context}。

**数据模型（4 表）**：
```
knowledge_base(配置chunkSize/向量模型/统计)
 └─ knowledge_document(原文rawText/状态)
      └─ knowledge_chunk(content+embedding向量/READY)
 knowledge_index_task(进度progress/状态)
```
状态流转：知识库 DRAFT→IMPORTED→READY；文档 IMPORTED→READY/FAILED；任务 RUNNING→SUCCESS/FAILED。

**关键设计点**：
1. **分片 overlap**：step=size-overlap，相邻片重叠，避免切断语义。默认 800/100。
2. **混合检索**：score=max(向量余弦, 文本相关度)。向量找语义相近，文本(textRelevance 中文 n-gram 2-4字+停用词)精确匹配关键词。取 max 鲁棒，任一命中即召回。
3. **向量化调外部 API**：agentPlanClient.createEmbedding 调火山引擎向量接口，配置存 llm_global_config 经 configId 引用。canEmbed 判断三者齐全才调，否则存空向量降级。
4. **索引任务跟踪进度**：knowledge_index_task 每片更新 progress，前端看进度条。
5. **逻辑删除旧分片**：markOldChunksDeleted set deleted=1（配合 @TableLogic），再插新的。
6. **运行时接口（工作流衔接）**：searchRuntime/upsert/retrieve 不在 Controller 暴露，给工作流节点调用——KnowledgeRetrieveNodeExecutor→searchRuntime/retrieve，KnowledgeUpsertNodeExecutor→upsert。resolveBaseForRuntime 支持按 ID/名称找库，找不到"默认知识库"自动创建。**这是知识库与工作流引擎的衔接点**。
7. **refreshBaseStats 统计聚合**：变化后 COUNT 聚合更新 documentCount/chunkCount/charCount，冗余存避免每次 JOIN。
8. **返回 Map 而非 DTO**：Service 返 List<Map>，Controller 透传，灵活但牺牲类型安全。
9. **检索降级与内存检索**：检索时配置缺失或 createEmbedding 异常 → queryEmbedding 退化为空 → 退化为纯文本检索（vectorScore 恒 0，不报错）。retrieve 全量 selectList READY chunk 在内存算余弦，**无向量库/ANN 索引**，O(块数×维度)，数据量大时是瓶颈。threshold<=0 时用 0.000001 过滤掉 score=0 的无关块。

**完整链路图**：
```
【建库】新建→INSERT knowledge_base(DRAFT)→导入→INSERT knowledge_document(IMPORTED,rawText)
→建立索引→createTask(RUNNING)→splitContent切N片→循环每片:createEmbedding→INSERT knowledge_chunk(READY)→document/task=SUCCESS
【检索】search→createEmbedding(query)→查READY chunks→score=max(向量余弦,文本相关度)→过滤+topK+拼context→返回{chunks,citations,context}
【工作流衔接】KnowledgeRetrieveNodeExecutor→searchRuntime/retrieve | KnowledgeUpsertNodeExecutor→upsert
```

#### uploadText 上传文件链路详解（Controller.uploadText）

**注意命名差异**：Controller 方法叫 `uploadText`，Service 方法叫 `uploadTextFile`——名字略不同。

**Controller 方法（62-66）**：
```java
@Operation(summary = "上传文本文件")
@PostMapping("/{id}/documents/upload")
public Result<Map<String, Object>> uploadText(@PathVariable Long id,
                                              @RequestParam("file") MultipartFile file) throws Exception {
    return Result.success(knowledgeBaseService.uploadTextFile(id, file));
}
```
- 路径：`POST /api/knowledge-bases/{id}/documents/upload`
- 参数：路径 `id`（知识库 ID）+ `file`（MultipartFile 表单文件，`multipart/form-data`）
- 职责：Controller 层很薄，只接收 HTTP 请求转交 Service。`@RequestParam("file")` 从 multipart 表单取名为 file 的文件部分
- 调 `Service.uploadTextFile(id, file)`

Java 类比：Controller 像"前台"，只负责接单转交，不做业务。

**Service.uploadTextFile（124-141）★核心**：
```java
@Transactional
public Map<String, Object> uploadTextFile(Long knowledgeBaseId, MultipartFile file) throws Exception {
    // 1. 校验文件非空
    if (file == null || file.isEmpty()) throw new IllegalArgumentException("上传文件不能为空");
    // 2. 取文件名(默认 uploaded.txt)
    String fileName = firstText(file.getOriginalFilename(), "uploaded.txt");
    // 3. 校验是文本文件(只支持 txt/md/markdown)
    if (!isTextFile(fileName)) throw new IllegalArgumentException("当前版本仅支持 txt、md、markdown 文本文件");
    // 4. ★读文件字节转 UTF-8 字符串
    String content = new String(file.getBytes(), StandardCharsets.UTF_8);
    // 5. 构造 importText 的请求对象
    KnowledgeTextImportRequest request = new KnowledgeTextImportRequest();
    request.setTitle(fileName);
    request.setContent(content);
    // 6. ★复用 importText 导入
    Map<String, Object> output = importText(knowledgeBaseId, request);
    // 7. 回填 fileName(上传文件特有字段)
    KnowledgeDocument document = knowledgeDocumentMapper.selectById(((Number) output.get("id")).longValue());
    document.setFileName(fileName);
    knowledgeDocumentMapper.updateById(document);
    // 8. 返回文档详情
    return toDocumentMap(document);
}
```
关键设计——**复用 importText**：上传文件 = 读文件转字符串 + 调 importText。和"粘贴文本"走同一条入库路径，避免重复逻辑。Java 类比：像方法重载，public 入口方法委托给核心方法。

第 7 步为什么要 selectById 再 update？importText 插入文档时没设 fileName（粘贴文本没文件名概念）。上传文件需要记 fileName，所以**插入后再 update 补上**。略增一次 DB 操作，换来逻辑清晰——importText 保持通用，uploadTextFile 补特有字段。

**Service.importText（108-121）★被复用**：
```java
@Transactional
public Map<String, Object> importText(Long knowledgeBaseId, KnowledgeTextImportRequest request) {
    KnowledgeBase base = requireBase(knowledgeBaseId);  // 校验知识库存在
    KnowledgeDocument document = new KnowledgeDocument();
    document.setKnowledgeBaseId(base.getId());
    document.setTitle(firstText(request.getTitle(), "未命名文本"));
    document.setSourceType("TEXT");
    document.setRawText(request.getContent());      // ★存原文
    document.setTags(trimToNull(request.getTags()));
    document.setStatus("IMPORTED");                  // ★状态=已导入(没分片没向量)
    document.setCharCount((long) request.getContent().length());
    knowledgeDocumentMapper.insert(document);        // ★INSERT knowledge_document
    refreshBaseStats(base.getId(), "IMPORTED");       // 刷新知识库统计
    return toDocumentMap(document);
}
```
做了什么：
1. requireBase：校验知识库存在（不存在抛异常）
2. new KnowledgeDocument，设字段：knowledgeBaseId / title(默认"未命名文本") / sourceType=TEXT / rawText=原文 / status=IMPORTED(★已导入，存了原文但没分片没向量) / charCount
3. knowledgeDocumentMapper.insert：INSERT knowledge_document 表
4. refreshBaseStats：刷新知识库统计
5. 返回文档 Map

**关键：此时只存了原文，没分片没向量**。建索引（分片+向量化）是另一个方法 `indexDocument`。这是**导入与索引分离**的设计——索引慢（要调向量 API），不能和导入耦合。用户可以先批量导入，再按需建索引。

**refreshBaseStats（386-405）★统计聚合**：
```java
private void refreshBaseStats(Long baseId, String status) {
    KnowledgeBase base = requireBase(baseId);
    Long documentCount = knowledgeDocumentMapper.selectCount(... knowledgeBaseId=baseId);
    Long chunkCount = knowledgeChunkMapper.selectCount(... knowledgeBaseId=baseId, status="READY");
    List<KnowledgeDocument> documents = knowledgeDocumentMapper.selectList(...);
    long charCount = documents.stream().map(getCharCount).filter(非null).sum();
    base.setDocumentCount(documentCount.intValue());
    base.setChunkCount(chunkCount.intValue());
    base.setCharCount(charCount);
    base.setStatus(status);  // IMPORTED
    knowledgeBaseMapper.updateById(base);
}
```
做了什么：
1. COUNT knowledge_document（该库文档数）
2. COUNT knowledge_chunk（status=READY 的分片数）
3. SUM 所有文档的 charCount（总字符数）
4. 更新 knowledge_base 的统计字段 + status
5. UPDATE knowledge_base

**为什么聚合存冗余字段？** 避免每次查询都 JOIN 三表 COUNT。冗余存 documentCount/chunkCount/charCount，前端列表直接读。这是"读优化"——用写入时的聚合换查询时的效率（呼应阶段 4 设计哲学）。

**完整执行链路（HTTP → 数据库）**：
```
前端:KnowledgePage 上传文件 tab → 选文件 → FormData(file)
  → uploadKnowledgeTextFile(api/knowledge.ts)
  → POST /api/knowledge-bases/{id}/documents/upload  (multipart/form-data)
  ↓
KnowledgeBaseController.uploadText(id, file)                              [62]
  → knowledgeBaseService.uploadTextFile(id, file)
  ↓
KnowledgeBaseService.uploadTextFile                                       [124]
  1. 校验 file 非空
  2. fileName = file.getOriginalFilename() || "uploaded.txt"
  3. isTextFile 校验(只支持 txt/md/markdown)
  4. content = new String(file.getBytes(), UTF_8)  ★读字节转字符串
  5. 构造 KnowledgeTextImportRequest(title=fileName, content=content)
  6. → importText(knowledgeBaseId, request)  ★复用
     ↓
     KnowledgeBaseService.importText                                       [108]
       a. requireBase(id) 校验知识库存在
       b. new KnowledgeDocument:
          - knowledgeBaseId, title, sourceType=TEXT
          - rawText=content ★存原文
          - status=IMPORTED ★(没分片没向量)
          - charCount
       c. knowledgeDocumentMapper.insert  ★INSERT knowledge_document
       d. refreshBaseStats(id, "IMPORTED")
          ↓
          - COUNT knowledge_document
          - COUNT knowledge_chunk(status=READY)
          - SUM charCount
          - UPDATE knowledge_base(documentCount/chunkCount/charCount/status)
       e. 返回 toDocumentMap(document)
  7. selectById 拿刚插入的 document
  8. document.setFileName(fileName) + updateById  ★补文件名
  9. 返回 toDocumentMap(document)
  ↓
Controller 返回 Result.success(文档Map)
  ↓
前端:文档列表刷新,显示新文档(status=IMPORTED,还没建索引)
```

**关键设计点**：
1. **复用 importText**：上传文件 = 读文件转字符串 + importText。粘贴文本和上传文件走同一条入库路径，避免重复逻辑
2. **导入与索引分离**：importText 只存原文（status=IMPORTED），分片+向量化是 indexDocument 单独做。索引慢（调向量 API），不耦合。可先批量导入再按需建索引
3. **两步 update 补 fileName**：importText 不知道文件名，插入后再 update 补上。略增一次 DB 操作，换逻辑清晰
4. **统计冗余存**：documentCount/chunkCount/charCount 存 knowledge_base，避免每次查询 JOIN 三表 COUNT。读优化
5. **status 状态机**：知识库 DRAFT→IMPORTED→READY。导入后 IMPORTED，建索引后 READY
6. **文件类型校验**：isTextFile 只支持 txt/md/markdown，防二进制文件
7. **UTF-8 转码**：file.getBytes() 转 UTF_8 字符串，保证中文不乱码
8. **@Transactional**：uploadTextFile 和 importText 都加事务，中途异常回滚（INSERT 文档 + UPDATE 统计 原子）

**和"粘贴文本"（importText）对比**：

| | importText(粘贴文本) | uploadText→uploadTextFile(上传文件) |
|---|---|---|
| 入口 | POST /documents/text(@RequestBody JSON) | POST /documents/upload(MultipartFile) |
| 内容来源 | request.getContent() | file.getBytes() 转 UTF-8 |
| 标题 | request.getTitle() | file.getOriginalFilename() |
| 文件名 | 无 | ★有(fileName 字段) |
| 核心 | 直接 INSERT | 读文件 + 复用 importText + 补 fileName |

两者最终都进 importText，数据库状态一致（都 status=IMPORTED，都没分片）。区别只在前端入口和文件名。

---

#### ReAct Agent 与工具模块详解（ReActAgentNodeExecutor）

**模块定位**：让 LLM"边想边做"的自主 Agent。ReAct = Reasoning + Acting，LLM 输出决策（用哪个工具）→ 执行工具 → 结果喂回 LLM → 再决策，直到给出最终答案。对比阶段 7 LLM 节点的单次调用，ReAct 是多轮循环、LLM 自主决定用哪个工具调几次，适合查资料/检索/计算等多步任务。

**Java 类比**：LLM 节点像无状态方法 `String result = llm.call(prompt)`；ReAct Agent 像带循环的控制器 `while(未完成){ 决策=llm.call(历史); 执行工具; 历史.add(结果); }`。

**四个核心类**：

1. **AgentTool 接口（策略模式）**：`getName/getDescription/getInputSchema(JSON Schema)/execute(arguments, context)→Map`。和阶段 11 Spring AI FunctionCallback 对比：AgentTool 返回 Map（结构化），FunctionCallback 返回 String；AgentTool 的 execute 多了 AgentToolContext（能访问节点配置和输入）。
2. **AgentToolContext（record）**：`(WorkflowNode node, Map<String,Object> currentInput)`。工具执行上下文，工具能拿到当前节点配置（knowledgeBaseId/mcpToolIds）和节点输入。
3. **AgentToolRegistry（自动注册）**：`@Component`，构造器注入 `List<AgentTool>`，Spring 自动收集所有 `@Component` 工具进 `Map<name, tool>`。**和阶段 7 NodeExecutorFactory 完全同模式**。`getTools(selectedNames)` 按名过滤（空则全返回），`getRequiredTool(name)` 按名取没有抛异常。加新工具不改 Registry，加个 `@Component` 实现类即可。
4. **ReActAgentNodeExecutor（★核心）**：`extends AbstractLLMNodeExecutor`——继承阶段 7 LLM 执行器基类，复用 extractConfig/chatClientFactory/promptTemplateService/skillRegistry（模板方法模式：父类管通用零件，子类管 ReAct 循环）。**但重写 execute()**，不走父类"一次 LLM 调用"，改成 ReAct 多轮循环——只复用父类的零件，不复用执行流程。

**ReAct 主循环（execute, 84-132）**：

```java
for (int step = 1; step <= maxSteps; step++) {
    // 1. 把目标+历史 trace 打包成这轮 user prompt
    String userPrompt = buildStepPrompt(goalPrompt, input, trace, step, maxSteps);
    // 2. 调 LLM(systemPrompt 固定, userPrompt 每轮带历史)
    ChatResponse response = chatClient.prompt(new Prompt(List.of(
            new SystemMessage(systemPrompt), new UserMessage(userPrompt)))).call().chatResponse();
    // 3. 解析 JSON 决策
    AgentDecision decision = parseDecision(content);
    // 4a. final_answer → 结束返回
    if ("final_answer".equals(decision.action())) return buildOutput(decision.finalAnswer(), trace, ...);
    // 4b. 非标准动作 → 容错按最终答案处理
    if (!"tool_call".equals(decision.action())) return buildOutput(content, trace, ...);
    // 5. 执行工具
    AgentTool tool = toolRegistry.getRequiredTool(decision.toolName());
    Map<String,Object> observation = tool.execute(decision.toolInput(), toolContext);
    // 6. 结果记入 trace(下轮喂回 LLM)
    trace.add(本步 action/toolName/toolInput/observation);
    emitProgress(...);  // SSE 推送
}
// 7. 达到 maxSteps → 返回"达到最大步数"
return buildOutput("达到最大 ReAct 步数限制", trace, true, ...);
```

**关键：trace 是 ReAct 的"记忆"**。每轮 `buildStepPrompt` 把整个 trace 序列化进 user prompt（`payload.put("previousSteps", trace)`），LLM 看到历史（前面调过 web_search 查了 X 结果 Y），再决定下一步。没有 trace，LLM 每轮失忆。

**JSON 决策强制格式 + 三层容错**：

system prompt 强制 LLM 只输出两种 JSON 之一：
```json
{"action":"tool_call","reasoningSummary":"为什么需要这个工具","toolName":"工具名","toolInput":{}}
{"action":"final_answer","reasoningSummary":"为什么可以结束","finalAnswer":"最终答案"}
```

为什么不用自然语言（经典 ReAct 论文是 Thought/Action/Observation 文本）？自然语言解析不可靠——LLM 可能输出多余的话、格式漂移。强制 JSON，parseDecision 用 fastjson2 解析，确定性强。

三层容错：
1. `stripCodeFence`：LLM 偶尔包 ` ```json ... ``` ` 代码块，剥掉
2. `normalizeAction`：`"tool"`/`"call_tool"`/`"function_call"` 归一成 `"tool_call"`；`"final"`/`"answer"` 归一成 `"final_answer"`（LLM 用词不稳定）
3. 解析失败兜底：JSONException 时按 final_answer 处理，content 原样返回——不崩，保证有输出

`reasoningSummary` 而非完整推理链：省 token，只给一句行动理由。system prompt 明确"不要暴露完整隐藏推理链"。

**System Prompt 构建（buildSystemPrompt, 138）**：
1. 角色："你是运行在 PaiAgent 工作流节点里的 ReAct Agent，必须通过 JSON 决策，不要输出 Markdown 代码块"
2. 知识库提示：有 knowledgeBaseId → 强制"必须先调用 knowledge_retrieve 检索知识库，再基于 observation 回答"
3. Skill 提示：有 skillName → 嵌入 `skill.getSummary()`
4. 可用工具列表：每个工具的 name/description/inputSchema
5. JSON 决策格式说明

**★关键衔接点（呼应阶段 11）**：ReAct 里 Skill 用 `getSummary()`，**不是** `getFullExecutionPrompt()`！因为 ReAct 是多轮自主探索，先给技能摘要（name+description+主体+reference 文件名列表），LLM 需要细节时自己调 `load_skill_detail`/`load_skill_reference` 工具（AgentTool 版）。**阶段 11 讲的"渐进式披露"在 ReAct 里真正生效了！** 节点执行器直接打包（求确定），ReAct 用渐进式（让 LLM 自主按需加载）。`LoadSkillDetailTool`/`LoadSkillReferenceTool`（AgentTool 版）就是为这个场景准备的——阶段 11 留的扣子，这里接上。

**工具自动注入（依赖推断，resolveToolNames, 297）**：
```java
// 规则1：有 knowledgeBaseId → 自动加 knowledge_retrieve
if (hasText(data.get("knowledgeBaseId")) && !toolNames.contains("knowledge_retrieve"))
    toolNames.add("knowledge_retrieve");
// 规则2：有 web_search → 自动加 web_fetch（搜索完得能抓网页看详情）
if (toolNames.contains("web_search") && !toolNames.contains("web_fetch"))
    expanded.add("web_fetch");
```
用户选了"联网搜索"，系统自动补上配套的"抓网页"——依赖推断，像 Maven 选 spring-web 自动带 spring-core，用户不用操心依赖。

**maxSteps 限制（防死循环）**：`DEFAULT_MAX_STEPS=5`，`MAX_ALLOWED_STEPS=20`，`resolveMaxSteps` clamp 到 [1,20]。ReAct 系统必备保险，防 LLM 死循环烧 token。Java 类比像 while 循环加计数器保险。

**工具集（8 个）**：

| 工具 | 作用 | 衔接 |
|------|------|------|
| `read_current_input` | 读当前节点输入 | 基础（看上游给啥）|
| `load_skill_detail` | 加载技能详情 | 阶段 11 Skill |
| `load_skill_reference` | 加载技能参考 | 阶段 11 Skill |
| `knowledge_retrieve` | 检索知识库 | 阶段 12 知识库（searchRuntime）|
| `memory_retrieve` | 检索记忆 | Agent 记忆表 |
| `memory_write` | 写入记忆 | Agent 记忆表（createEmbedding 算向量）|
| `web_search` | 联网搜索 | MCP（SearchInfinityMcpClient）|
| `web_fetch` | 抓取网页 | MCP |

工具参数多级 fallback（以 KnowledgeRetrieveTool 为例）：
```java
String knowledgeBaseId = firstText(
    arguments.get("knowledgeBaseId"),                  // 1. LLM 传的参数（优先）
    context.node().getData().get("knowledgeBaseId"),   // 2. 节点配置
    "default"                                           // 3. 默认值
);
```
LLM 可覆盖节点配置（传参），也可偷懒用节点配置（不传）。灵活。

**阶段二规划（LangGraph 原生，未实现）**：`docs/react-agent-phases.md` 说当前是阶段一：节点内 Runtime——ReAct 循环在 ReActAgentNodeExecutor 内部 for 循环，LangGraph 只看到一个普通节点。阶段二规划把每轮 ReAct 变成 LangGraph 图节点：
```text
START -> agent_decide
agent_decide -- tool --> tool_execute
agent_decide -- final --> END
agent_decide -- max_steps --> END
tool_execute -> agent_decide
```
用 addConditionalEdges + AsyncEdgeAction 做路由，此时每轮是独立图节点，可可视化、可断点恢复（呼应阶段 10 LangGraph）。**项目演进规划**：先做简单版（节点内循环），够用再升级图状态机。务实。

**完整数据请求链路**：
```
前端：拖 react_agent 节点 → 配 LLM(provider/model) + prompt + 选 tools + maxSteps
  ↓ flow_data JSON 整存(node.data)
执行：WorkflowExecutor → NodeExecutorFactory.get("react_agent")
  → ReActAgentNodeExecutor.execute(node, input)
    → extractConfig()(复用阶段7父类)：provider/apiUrl/model/promptTemplate/skillName
    → validateConfig：必填校验(provider/apiUrl/model/prompt 缺一抛异常)
    → processTemplate：goalPrompt(模板替换 inputParams)
    → resolveMaxSteps：clamp [1, 20]
    → toolRegistry.getTools(resolveToolNames)：按名过滤 + 依赖推断自动注入
    → buildSystemPrompt：角色 + 知识库提示 + Skill摘要 + 工具列表 + JSON格式
    → chatClientFactory.createClient(无 Function，ReAct 自己管工具)
    → for step 1..maxSteps：
        buildStepPrompt(goal, input, trace, step, maxSteps)  // JSON 打包历史
        chatClient.call() → content
        parseDecision → AgentDecision(action/toolName/toolInput/finalAnswer)
        if final_answer：buildOutput + return ★
        if 非 tool_call：容错按 final_answer ★
        toolRegistry.getRequiredTool(toolName) → tool.execute(toolInput, context) → observation
        trace.add(本步 action/toolName/toolInput/observation)
        emitProgress → SSE 推送 NODE_PROGRESS(阶段9)
    达到 maxSteps → buildOutput(maxStepsReached=true, stopReason)
  → buildOutput：output/finalAnswer/toolTrace/steps/maxStepsReached/tokens
  → 节点输出 → 下游节点
```

**和其他阶段的关系**：
- 阶段 7 AbstractLLMNodeExecutor：ReActAgentNodeExecutor 继承它，复用 extractConfig/chatClientFactory/skillRegistry。模板方法模式
- 阶段 11 Skills：ReAct 用 AgentTool 版技能工具（getSummary + load_skill_detail/reference），渐进式披露在 ReAct 里真正生效
- 阶段 12 知识库：KnowledgeRetrieveTool 调 knowledgeBaseService.searchRuntime（阶段 12 检索）
- 阶段 9 SSE：emitProgress 每步推送 NODE_PROGRESS
- 阶段 10 LangGraph：目前 ReAct 是节点内循环，非 LangGraph 条件边（阶段二规划）

**关键设计点**：
1. **ReAct = 多轮"决策→工具→观察→再决策"循环**，LLM 自主控流程（对比 LLM 节点单次调用）
2. **JSON 决策强制格式 + 三层容错**（代码块剥离/动作归一/解析失败按 final_answer），保证不崩
3. **继承 AbstractLLMNodeExecutor 复用零件，重写 execute 做循环**——模板方法模式变体
4. **AgentTool 接口 + Spring 自动注册**（和 NodeExecutorFactory 同模式），加工具不改代码
5. **trace 累积喂回 LLM 做"记忆"**，每轮 buildStepPrompt 带 previousSteps
6. **工具参数多级 fallback**（LLM 传 > 节点配置 > 默认），灵活
7. **依赖推断自动注入工具**（knowledgeBaseId→knowledge_retrieve，web_search→web_fetch），用户不用操心依赖
8. **maxSteps 保险**（默认5，上限20）防死循环烧 token
9. **reasoningSummary 而非完整推理链**，省 token
10. **阶段一节点内循环，阶段二规划 LangGraph 条件边**（未实现），务实演进

#### MCP 工具集成模块详解（SearchInfinityMcpClient）

**模块定位**：MCP = Model Context Protocol（模型上下文协议），Anthropic 提出的标准，让 LLM 能调外部工具/数据源。本项目用 MCP 接"联网搜索"——通过 stdio 启动外部进程（`mcp-server-askecho-search-infinity`），用 JSON-RPC 通信，拿搜索结果。ReAct Agent 的 `web_search` 工具背后就是 MCP。

**整体三层架构**：

| 层 | 类 | 职责 |
|---|---|---|
| 配置层 | `McpToolConfig` + `McpToolConfigService` | CRUD 管理工具配置（命令/参数/环境变量），存 `mcp_tool_config` 表 |
| 客户端层 | `SearchInfinityMcpClient` ★ | 启动 MCP server 子进程，JSON-RPC 通信，调 web_search |
| 集成层 | `WebSearchTool` / `WebFetchTool` | 包成 ReAct AgentTool，LLM 在 ReAct 循环里调 |

数据流：ReAct Agent → WebSearchTool → McpToolConfigService 查配置 → SearchInfinityMcpClient 启子进程+JSON-RPC → 结果回传。

**配置入口：McpToolConfigController（薄路由层）**

`McpToolConfigController` 挂在 `/api/mcp-tools`，是 MCP 工具配置的 REST 管理入口。它本身不写业务逻辑，只做三件事：**路由分发 + `@Valid` 参数校验 + `Result` 统一包装**，真正干活的是 `McpToolConfigService`（构造器注入）。6 个接口：

| HTTP | 路径 | Controller 方法 | Service 方法 | 执行逻辑 |
|---|---|---|---|---|
| GET | `/api/mcp-tools` | `list` | `listConfigs` | 查全部，按 updatedAt 倒序，`toSafeMap` 脱敏 |
| POST | `/api/mcp-tools` | `create` | `createConfig` | 通用新增，preset=0 |
| POST | `/api/mcp-tools/agent-plan-web-search` | `createAgentPlanWebSearch` | `createAgentPlanWebSearch` | 预设创建器，只传 apiKey |
| PUT | `/api/mcp-tools/{id}` | `update` | `updateConfig` | 按 id 取出再覆盖 |
| DELETE | `/api/mcp-tools/{id}` | `delete` | `deleteConfig` | 逻辑删除（`@TableLogic`） |
| POST | `/api/mcp-tools/{id}/test` | `test` | `testConfig` | 真正启动 uvx 子进程调一次 web_search |

参数校验靠 DTO 上的 `@NotBlank`（如 `McpToolConfigRequest.name`/`toolName`/`command`、`AgentPlanWebSearchMcpRequest.apiKey`），校验失败 Spring 直接 400，Controller 方法体不执行——校验不在 Controller 里手写。

**配置阶段 vs 运行阶段（重要区分）**：`McpToolConfigService` 的方法分两类——
- **配置阶段（被 Controller 调）**：`listConfigs`/`createConfig`/`createAgentPlanWebSearch`/`updateConfig`/`deleteConfig`/`testConfig`——前端管理界面用，CRUD + 测试
- **运行阶段（不被 Controller 调，给引擎用）**：`resolveEnabledConfigs`、`resolveFirstEnabledWebSearch`——Agent 跑联网搜索时从这张表读配置去实际调用

所以 `mcp_tool_config` 表是**双重身份**：配置阶段往里写，运行阶段从里读。Controller 只负责"写"那一半（CRUD + 测试），"读"那一半由 `WebSearchTool`/`WebSearchNodeExecutor` 在运行时调用。Java 类比：像一张"外部进程启动参数表"，配置界面填表，运行时引擎照表启动进程。

**配置层：McpToolConfig 实体**（mcp_tool_config 表）：

| 字段 | 含义 | 示例 |
|------|------|------|
| toolType | 工具类型 | `agent_plan_web_search` / `custom` |
| toolName | 工具名（对应 MCP server 暴露的工具）| `web_search` |
| transport | 传输方式 | `stdio`（MCP 标准传输之一，还有 sse/http）|
| command | 启动命令 | `uvx` |
| args | 命令参数（JSON 数组）| `["--from","git+...","mcp-server-askecho-search-infinity"]` |
| env | 环境变量（JSON）| `{"ASK_ECHO_SEARCH_INFINITY_API_KEY":"xxx"}` |
| enabled | 启用 | 1/0 |
| preset | 预设 | 1=系统预设 Agent Plan 搜索，0=用户自定义 |
| deleted | 逻辑删 | `@TableLogic` |
| created_at/updated_at | 时间 | `@TableField` 自动填充 |

Java 类比：像一个"进程启动配置"的持久化。把"怎么启动一个外部工具进程"存数据库，运行时读出来启动。换搜索源只需改配置不改代码。

**McpToolConfigService：配置 CRUD**（extends ServiceImpl，阶段 4 MyBatis-Plus 模式）：

1. `listConfigs`：查所有配置，按 updatedAt 降序，`toSafeMap` 脱敏
2. `createConfig`：新增自定义 MCP（preset=0）
3. `createAgentPlanWebSearch` ★：新增 Agent Plan 联网搜索（preset=1）。**自动填好** command=uvx、args=["--from","git+...","mcp-server-askecho-search-infinity"]、env={API_KEY: apiKey}。用户只需填一个 apiKey
4. `testConfig` ★：测试——读配置，调 `searchInfinityMcpClient.webSearch(query="今天的科技新闻")` 看能不能跑通
5. `resolveEnabledConfigs`：按 ID 列表查启用的配置（给工作流节点用，node.data.mcpToolIds → 配置）
6. `resolveFirstEnabledWebSearch` ★：从启用的配置里找第一个 `toolName=web_search` 的（给 WebSearchTool 用）
7. `parseArgs/parseEnv`：把 JSON 字符串解析回 List/Map（args/env 存数据库是 JSON 字符串）

关键设计——**env 脱敏（maskEnv）**：
```java
private Map<String, String> maskEnv(Map<String, String> env) {
    env.forEach((key, value) -> masked.put(key, isSecretKey(key) ? "******" : value));
}
private boolean isSecretKey(String key) {
    String upper = key.toUpperCase();
    return upper.contains("KEY") || upper.contains("SECRET") || upper.contains("TOKEN") || upper.contains("PASSWORD");
}
```
API Key 是敏感信息，返回前端时 KEY/SECRET/TOKEN/PASSWORD 字段值替换成 `******` 防泄露。但存数据库明文（运行时要用）。

关键设计——**预设降低门槛（createAgentPlanWebSearch）**：用户不用懂 uvx/包名/命令，只填一个 apiKey，系统自动组装好 MCP 配置。把复杂的 MCP server 启动细节封装成预设。

**SearchInfinityMcpClient：★核心（MCP 客户端）**

最硬核部分。实现 **stdio MCP 协议**——启动子进程，用 stdin/stdout 传 JSON-RPC 消息。

**McpSession 内部类（515-676）**：封装一次 MCP 会话（**一次搜索 = 一个会话 = 一个子进程**）。
- `start(command, args, env)`：用 ProcessBuilder 启动子进程，把 env 设进去（API Key 通过环境变量传给子进程）。开守护线程收集 stderr（报错诊断用）。
- `initialize()`：MCP 握手。发 `initialize` 请求（protocolVersion/capabilities/clientInfo），等响应；再发 `notifications/initialized` 通知。MCP 协议规定的前置握手——server 要先知道客户端是谁、协议版本。
- `callTool(name, arguments)` ★：发 `tools/call` 请求（name=web_search，arguments={Query/Count/SearchType/...}），等响应拿结果。
- `request(method, params, timeout)`：底层 JSON-RPC 通信：
```java
// 1. 构造消息
message = {jsonrpc:"2.0", id, method, params}
// 2. writeMessage:写到子进程 stdin(一行 JSON + 换行)
writeMessage(message);
// 3. CompletableFuture + 单线程异步读 stdout,循环到 id 匹配
CompletableFuture.supplyAsync(() -> {
    while (true) {
        JSONObject response = readMessage();
        if (response.containsKey("id") && response.getLongValue("id") == id) return response;
    }
}, readerExecutor);
// 4. future.get(timeout) 等结果,超时抛 TimeoutException(带 stderr 诊断)
response = future.get(timeout.toMillis(), TimeUnit.MILLISECONDS);
// 5. 检查 error 字段
```
**为什么用 CompletableFuture + 异步读？** stdin/stdout 是阻塞 IO。写完请求要读响应，但子进程可能先发别的消息（通知/进度）。用单独线程读 + **按 id 匹配**，避免主线程阻塞死等，也过滤掉无关通知。
- `close()`：关会话——关线程池、关流、destroy 子进程，等 3 秒不退就 destroyForcibly。**每次搜索完销毁子进程**，不复用（简化，避免状态泄漏）。

**webSearch 主流程（44-95）**：
```java
public Map<String, Object> webSearch(McpToolConfig config, String query, int count, ...) {
    try (McpSession session = McpSession.start(command, args, env)) {
        session.initialize();  // 握手
        JSONObject arguments = new JSONObject();
        arguments.put("Query", query);
        arguments.put("Count", Math.max(1, Math.min(count, image?5:50)));  // 限流
        arguments.put("SearchType", searchType);  // web/image
        JSONObject result = session.callTool("web_search", arguments);  // ★调工具
        return normalizeToolResult(result);  // 解析结果
    }  // try-with-resources 保证 close
}
```
生命周期：start 子进程 → initialize 握手 → callTool 调用 → normalizeToolResult 解析 → close 销毁。

**注意首字母大写**：arguments 的 key 是 `Query`/`Count`/`SearchType`（PascalCase），不是 query/count。这是 `mcp-server-askecho-search-infinity` 约定的参数名。Java 类比：像调第三方 API，参数名得按它的规矩来。

**normalizeToolResult（97-151）：结果归一化**——MCP server 返回格式复杂（content 数组 + structuredContent + 嵌套），归一化成统一输出：
- `summary`：可读摘要
- `webResults`：结构化搜索结果（从 WebResults 字段提取）
- `citations`：引用列表（从 url 字段提取）
- `requestId`/`resultCount`：元信息
- `isError`/`raw`：错误标志 + 原始返回（调试）

`extractWebResults`/`collectWebResults`：递归遍历 JSON 树找 WebResults 数组，提取 Id/Title/SiteName/Url/Snippet/Summary。递归是因为结果可能嵌套在 structuredContent.result 里。

`findBusinessError`：递归找 ResponseMetadata.Error，server 返回业务错误（如 API Key 无效、额度用完）时抛 IOException。

为什么这么复杂？MCP 是通用协议，不同 server 返回结构不同。这里针对 askecho-search-infinity 做了适配——把它的特定字段映射成统一输出。Java 类比：像写第三方 API 的 SDK，要适配它的响应格式。

**超时与诊断**：INITIALIZE_TIMEOUT=90s（握手）、CALL_TIMEOUT=120s（调用）。超时抛 TimeoutException，消息带 `recentStderr()`（最近 8 行 stderr）帮诊断——MCP server 启动失败/网络问题会在 stderr 打日志。

**uvx 多处兜底（resolveUvxCommand）**：找 uvx 可执行文件：`MCP_UVX_PATH` 环境变量 > `~/.local/bin/uvx` > 默认 `"uvx"`。不同环境 uvx 装的位置不同，多处兜底。

**集成层：AgentTool 包装**

WebSearchTool（ReAct 的 web_search）：
```java
public Map<String, Object> execute(Map<String, Object> arguments, AgentToolContext context) {
    String query = arguments.getOrDefault("query", "");
    int limit = ...;  // 默认 5
    McpToolConfig selectedMcp = mcpToolConfigService.resolveFirstEnabledWebSearch(
        context.node().getData().get("mcpToolIds"));  // 从节点配置读选中的 MCP
    if (selectedMcp != null) {
        return searchInfinityMcpClient.webSearch(selectedMcp, query, limit, ...);
    }
    throw new IllegalArgumentException("联网搜索工具未配置...");
}
```
衔接：节点 `data.mcpToolIds`（用户在节点配置里选的 MCP）→ `resolveFirstEnabledWebSearch` 查启用的配置 → `webSearch` 调用。

WebFetchTool（ReAct 的 web_fetch）：**注意 web_fetch 不走 MCP！** 直接用 `java.net.URLConnection` 抓网页：
```java
URLConnection connection = URI.create(url).toURL().openConnection();
connection.setConnectTimeout(8000);
connection.setReadTimeout(15000);
String text = new String(connection.getInputStream().readAllBytes(), UTF_8);
String truncated = text.length() > 8000 ? text.substring(0, 8000) : text;  // 截断 8000 字
```
为什么 web_fetch 不用 MCP？抓网页是纯 HTTP GET，Java 标准库就能做，不需要起子进程。MCP 适合"需要外部进程/复杂逻辑"的工具（如搜索要调搜索 API）。简单抓页用标准库更轻量。`MAX_PAGE_CHARS=8000` 截断，防超大网页撑爆 prompt token。这是 ReAct 系统的 token 控制。

**完整数据请求链路**：

链路 A：配置 MCP（前端）
```
前端 McpToolPage：添加按钮 → Modal 表单(name + apiKey)
  → createAgentPlanWebSearchMcp(api/mcpTools.ts)
  → POST /api/mcp-tools/agent-plan-web-search
  → McpToolConfigService.createAgentPlanWebSearch
    → new McpToolConfig + 自动填 command=uvx/args/env={API_KEY}
    → preset=1, enabled=1 → save(INSERT mcp_tool_config)
  → loadTools 刷新列表
```

链路 B：测试 MCP（前端）
```
前端测试按钮 → Modal(query 输入)
  → testMcpTool(id, {query})
  → POST /api/mcp-tools/{id}/test
  → McpToolConfigService.testConfig
    → requireConfig(id) 读配置
    → searchInfinityMcpClient.webSearch(config, query, 3, ...)
      → McpSession.start(uvx + args, env)  启动子进程
      → initialize() 握手
      → callTool("web_search", {Query, Count, SearchType})
      → normalizeToolResult 解析
      → close() 销毁子进程
    → 返回 {summary, webResults, citations, ...}
  → 前端 renderTestResult 渲染(标题/站点/URL/摘要)
```

链路 C：ReAct Agent 用 MCP 联网搜索（★核心，衔接阶段 12 ReAct）
```
ReAct 循环某步：LLM 决策 {"action":"tool_call","toolName":"web_search","toolInput":{"query":"..."}}
  → toolRegistry.getRequiredTool("web_search")
  → WebSearchTool.execute({query}, context)
    → mcpToolConfigService.resolveFirstEnabledWebSearch(node.data.mcpToolIds)
      → 查启用的 web_search 配置
    → searchInfinityMcpClient.webSearch(config, query, limit, ...)
      → McpSession.start → initialize → callTool → normalizeToolResult → close
    → 返回 {summary, results, citations}
  → observation 记入 trace
  → 下一轮 LLM 看到搜索结果,可能调 web_fetch 抓详情,或直接 final_answer
```

链路 D：工作流直连 web_search 节点（★与链路 C 平行的另一条运行路径）
```
工作流执行 web_search 节点（节点本身就是搜索，不走 ReAct）
  → WebSearchNodeExecutor.execute(node, input)   ← extends AbstractAgentPlanNodeExecutor
    → 从 node.data / 上游 input 取 query/limit/freshness/language
    → resolveFirstEnabledWebSearch(node.data.mcpToolIds)  查启用配置
    → searchInfinityMcpClient.webSearch(config, query, limit,
        normalizeTimeRange(freshness), null, normalizeSearchType(language))
    → 输出 {query, summary, results, citations, output=summary, metadata=raw}
      ↑ output 字段供下游节点消费，metadata 保留原始返回
```

**两条运行路径对比（都调 `resolveFirstEnabledWebSearch` + `webSearch`）**：

| | 链路 C：`WebSearchTool` | 链路 D：`WebSearchNodeExecutor` |
|---|---|---|
| 触发方 | ReAct Agent，LLM 自主决定何时调 | 工作流引擎，节点拓扑顺序执行 |
| query 来源 | LLM 生成 `toolInput.query` | 节点配置 / 上游节点 input |
| 输出 | 精简（summary/results/citations，给 LLM 看） | 完整（含 output + metadata=raw，给下游节点） |
| 额外参数 | 无（limit 默认 5） | freshness→TimeRange、language→SearchType |
| 注册方式 | Spring `@Component` 自动进 AgentToolRegistry | NodeExecutorFactory 按 `getSupportedNodeType="web_search"` 分发 |

两者复用同一套"配置读取 + MCP 调用"，区别只在入参来源和输出形状。Java 类比：同一 service 方法被两个"controller"以不同参数和返回包装调用——核心逻辑共享，适配层不同。

`WebSearchNodeExecutor` 的参数归一化：
- `normalizeTimeRange`：节点配置 `freshness`（day/week/month/year）→ MCP 的 `OneDay/OneWeek/OneMonth/OneYear`
- `normalizeSearchType`：`language="image"` → `SearchType="image"`，否则 `"web"`

**和 ReAct Agent 的衔接（呼应阶段 12）**：
- ReAct 的 `web_search` 工具 = WebSearchTool = 调 MCP
- ReAct 的 `web_fetch` 工具 = WebFetchTool = 直接 HTTP（不走 MCP）
- 依赖推断（阶段 12）：选 web_search 自动加 web_fetch——搜索完用 web_fetch 抓详情
- 节点 `data.mcpToolIds`：用户在 ReAct 节点配置里选要用的 MCP（多个 MCP 配置可选其一）

**关键设计点**：
1. **stdio MCP 协议**：起子进程 + stdin/stdout JSON-RPC。MCP 标准传输之一，stdio 适合本地工具
2. **一次搜索一会话**：start→initialize→callTool→close，不复用子进程。简化状态管理，避免泄漏
3. **异步读 + id 匹配**：CompletableFuture + 单线程读 stdout，按 JSON-RPC id 匹配响应（过滤无关通知）
4. **超时 + stderr 诊断**：90s/120s 超时，超时消息带最近 8 行 stderr 帮排查
5. **env 脱敏**：API Key 返回前端时 mask 成 ******（KEY/SECRET/TOKEN/PASSWORD），存库明文
6. **预设降低门槛**：createAgentPlanWebSearch 自动组装 uvx/包名/命令，用户只填 apiKey
7. **结果归一化**：把 MCP server 特定格式（WebResults/ResponseMetadata.Error）适配成统一输出
8. **web_fetch 不走 MCP**：简单 HTTP GET 用 Java 标准库，轻量。MAX_PAGE_CHARS=8000 截断防 token 爆
9. **uvx 多处兜底**：MCP_UVX_PATH > ~/.local/bin/uvx > uvx，适应不同环境
10. **配置驱动**：MCP 配置存数据库，运行时读出来启动。换搜索源只需改配置不改代码

**前端 Java 类比（McpToolPage.tsx）**：复用 KnowledgePage 的布局（`knowledge-shell`/`knowledge-layout`）：左侧 List 工具列表 + 右侧 List 详情 + Modal 弹窗。

| React 概念 | Java 类比 |
|-----------|-----------|
| `useState` | 类的成员变量（状态）|
| `useEffect(() => loadTools(), [])` | `@PostConstruct` 初始化（进页面加载列表）|
| `handleCreateAgentPlanSearch` | Controller create 方法的前端版 |
| `Form rules required` | Spring `@NotBlank` 校验 |
| `api/mcpTools.ts` | Service 层封装，5 个调用对应 5 个 REST 接口 |

`api/mcpTools.ts` 封装 5 个调用：`getMcpTools`/`createAgentPlanWebSearchMcp`/`deleteMcpTool`/`testMcpTool`（createMcpTool/updateMcpTool 也有但页面没用），和后端 REST 一一对应。

#### 媒体生成模块详解（图/视频/TTS）

**模块定位**：3 类节点执行器 + 多厂商 client + MinIO 对象存储。把文本/参考图变成图片、视频、音频。产物都转存 MinIO 拿持久 URL。

**整体架构（3 类节点）**：

| 节点类型 | 执行器 | 产物 | 调用模式 |
|---|---|---|---|
| `image_generate` | ImageGenerateNodeExecutor | 图片 URL | **同步**（一次请求拿结果）|
| `video_generate` | VideoGenerateNodeExecutor | 视频 URL | **异步**（提交任务+轮询）|
| `tts` | TTSNodeExecutor | 音频 URL | **同步**（分片+并发+合并）|

共同点（5 个）：
1. 都是节点执行器，走阶段 7 工厂分发（image/video extends AbstractAgentPlanNodeExecutor；tts 直接 implements NodeExecutor）
2. 都调厂商 client（多厂商适配）
3. 产物都**转存 MinIO**（对象存储），返回持久化 URL
4. 都用 configResolver/llmGlobalConfigService 解析配置（全局配置优先）
5. 都 emit NODE_PROGRESS（SSE 推送进度）

**AbstractAgentPlanNodeExecutor（图片/视频父类）**——模板方法模式（呼应阶段 7）。提供通用工具方法：
- `textValue(node, input, field, fallbackField)`：多级取值（node.data > input > fallbackField > input.output）
- `configuredTextInput(node, input, paramName)` ★：从 inputParams 解析输入（input 类型直接取值 / reference 类型按 referenceNode 跨节点引用）。呼应阶段 4 的 reference 机制
- `applyOutputParams(node, output)`：按 outputParams 映射输出字段
- `stringData/intData/doubleData`：类型安全的 data 取值

把"从 node.data 和 input 取值"的通用逻辑抽出来，图片/视频复用。TTS 没继承它（配置解析更复杂，自己实现了 extractInputText）。

**MinioService（对象存储，产物都转存这）**——3 个上传方法：
- `uploadFile(objectName, inputStream, contentType, size)`：流上传
- `uploadFromUrl(fileUrl, objectName, contentType)` ★：从 URL 下载再上传（图片/视频厂商返回临时 URL，转存到自己 MinIO）
- `uploadFromBytes(data, objectName, contentType)` ★：从字节数组上传（TTS 合并的音频 bytes）

`ensureBucketExists()`：bucket 不存在自动创建。返回公共 URL：`publicUrl/bucketName/objectName`。

**为什么转存 MinIO？** 厂商返回的 URL 通常是临时链接（过期失效），且不同厂商域名不同。转存到自己 MinIO：URL 持久、统一域名、可控访问。这是"数据持久化"设计——不依赖外部临时资源。

**图片生成（ImageGenerateNodeExecutor，同步）**：
```
1. 取 prompt(configuredTextInput 多级取值)
2. resolveImageConfig + validateApiConfig(全局配置优先)
3. generateImage:switch(provider) 路由
   - volcengine_agent_plan → agentPlanClient.generateImage
   - step → stepFunImageClient.generateImage
   - default → openAiCompatibleImageClient.generateImage(OpenAI 兼容,兜底)
4. persistMedia:把返回的 URL/base64 转存 MinIO
5. buildOutput:imageUrl/imageUrls/prompt/model/metadata
```
多厂商适配（switch provider）和阶段 7 LLM 执行器的 canonicalizeProvider 同思路——一个节点支持多厂商，default 走 OpenAI 兼容兜底。

persistMedia 智能转存：
- `data:image/...;base64,xxx` → 解码 base64 → uploadFromBytes
- 普通 URL → uploadFromUrl
- 失败保留原 URL（降级，不阻断流程）

OpenAiCompatibleImageClient 的 URL 归一化：`normalizeImageEndpoint` 把各种 apiUrl 归一成 `xxx/v1/images/generations`。还有 Agnes 特殊处理：`api.agnes-ai.com` → `apihub.agnes-ai.com`（域名迁移适配）。

**视频生成（VideoGenerateNodeExecutor）★核心（异步轮询）**——视频生成耗时长（几十秒到几分钟），不能同步等，所以异步：提交任务 + 轮询：
```
1. 取 prompt + referenceImageUrl(首帧)
2. resolve(node, "video") + validateApiConfig
3. emit "视频任务提交中" (SSE)
4. createVideoTask → 拿 taskId
   (agnes→agnesVideoClient / 否则→agentPlanClient 火山)
5. emit "视频任务已提交: taskId=xxx" (SSE)
6. 轮询循环 for i in 0..60:
     Thread.sleep(5000)
     getVideoTask(taskId) 查状态
     emit "视频生成中: 第 N/60 次, 已等待 Xs, 状态=running, 进度=50%" (SSE)
     if success(success/succeed/completed) → break
     if failed(fail/error/cancel) → 抛异常
7. 拿 videoUrl → emit "视频转存中" → persistMedia 转存 MinIO
8. buildOutput:taskId/videoUrl/coverUrl/model
```
MAX_POLLS=60 + POLL_INTERVAL_MS=5000 = 5 分钟超时上限。这是"长任务控制"——防止无限等待。

AgnesVideoClient 的帧数计算：`normalizeNumFrames(duration, frameRate=24)` 把时长转帧数，还做了 `(candidate-1)/8*8+1` 对齐到 8 的倍数+1（Agnes API 要求帧数满足特定公式）。这是"厂商 API 约束适配"。

字段名多 key 查找：`findString(response, "video_url", "videoUrl", "url", "remixed_from_video_id")` 递归找，因为不同厂商/版本返回字段名不一致。这是"兼容多版本响应"的容错设计。

**TTS 文字转语音（TTSNodeExecutor）★最复杂**——同步模式，但有文本分片 + 并发合成 + WAV 合并：
```
1. extractInputText:取文本(inputParams.text 参数,或 input.output/input/text)
2. resolveConfig:解析配置(全局配置优先,provider/model/voice/...)
3. validateConfig:校验(只支持 qwen/step)
4. splitText:★文本分片(按 maxLength + maxBytes,在标点处切)
5. emit "文本已分割为 N 个片段" (SSE)
6. 并发:CompletableFuture 逐片异步合成(synthesizeChunk),每片完成 emit 进度
7. allOf().join() 等全部完成
8. mergeWavFiles:★合并 WAV(手写 44 字节头 + 拼数据 + 改长度字段)
9. uploadFromBytes 上传 MinIO
10. buildOutput:audioUrl/chunks
```
为什么分片？TTS API 对单次输入有长度限制（qwen 400 字/600 字节，step 1000 字）。长文本要切片分别合成再合并。

splitText 智能切分：
- 按 maxLength 切
- 检查 UTF-8 字节数 ≤ maxBytes（中文 1 字 3 字节，字数和字节数不同）
- 优先在标点（。！？；,.!?;）处切，避免切断句子
- 字节数超了就 `end -= 10` 回退

并发合成：`CompletableFuture.supplyAsync` 每片异步，`allOf().join()` 等全部。10 片并发比串行快 10 倍。

双厂商：
- qwen（阿里百炼）：用 dashscope SDK（MultiModalConversation），返回音频 URL → downloadAudio 下载。注意 `synchronized (DASHSCOPE_HTTP_URL_LOCK)` 改全局 `Constants.baseHttpApiUrl`（SDK 设计缺陷，全局变量，并发要加锁）
- step（阶跃星辰）：直接 HTTP POST，返回 WAV 字节流

normalizeTtsModel 智能修正：用户配了非 TTS 模型（如 chat 模型），自动切换成 `stepaudio-2.5-tts` / `qwen3-tts-flash` 并 warn。这是"防呆设计"——配错自动纠正。

mergeWavFiles 手写 WAV 合并：WAV 文件头 44 字节（RIFF...fmt ...data）。合并 = 取第一个的头 + 拼所有片的 data（跳过 44 字节头）+ 改 RIFF size 和 data size 字段（小端序 4 字节）。这是"二进制文件格式处理"。Java 类比：像手动操作 ByteBuffer 改字节。

音色默认值：`voice = step ? "cixingnansheng" : "Cherry"`。不同厂商默认音色不同。

**MediaController（图片上传）**——媒体文件上传接口，挂在 `/api/media`，只有一个接口 `POST /api/media/images`（`consumes=multipart/form-data`，字段名 `file`）。Controller 只做校验+组装，真正上传在 `MinioService`（构造器注入）。

执行链路：
```
POST /api/media/images  (multipart, file)
  ├─ validateImage(file)
  │     ├─ 非空非 isEmpty
  │     ├─ size ≤ 10MB (MAX_IMAGE_SIZE)
  │     └─ 是图片：contentType 以 image/ 开头 或 文件名后缀匹配 (png|jpg|jpeg|webp|gif)  ← 双重校验
  ├─ originalName/contentType 兜底（空则默认 image.png / image/png）
  ├─ objectName = "images/uploads/" + UUID + extensionFor(name, type)
  ├─ minioService.uploadFile(objectName, inputStream, contentType, size)
  └─ 返回 {url, fileName, contentType, size}
```

- `validateImage`：双重校验——`contentType` 以 `image/` 开头 **或** 文件名后缀匹配 `png|jpg|jpeg|webp|gif`，任一通过即可。**为什么双重**：浏览器传的 contentType 不一定准，用文件名后缀兜底。
- `extensionFor`（扩展名兜底）：文件名有合法后缀就用之；否则按 contentType 反推（`image/jpeg→.jpg`、`image/webp→.webp`、`image/gif→.gif`、默认 `.png`）。
- objectName = `images/uploads/{UUID}.{ext}`：UUID 防重名覆盖，原文件名只回传不作为存储名。

**MinioService.uploadFile 内部**：
```
ensureBucketExists()  // bucket "paiagent" 不存在就 makeBucket 创建
minioClient.putObject(stream, size, partSize=-1)
return publicUrl + "/" + bucketName + "/" + objectName
     = http://localhost:9000/paiagent/images/uploads/{uuid}.png
```
- `ensureBucketExists`：懒创建 bucket，不存在自动建。
- **publicUrl 而非 endpoint**：部署时 endpoint 可能是内网地址，publicUrl 设成外网/CDN 地址，前端拿到的 URL 才能打开。
- URL 直接拼接（不用 presigned URL）：bucket 设为公开读。

**MinioConfig**（`@ConfigurationProperties(prefix="minio")`）从 application.yml 读配置造 `MinioClient` Bean：endpoint=`http://localhost:9000`、accessKey/secretKey=`admin`/`admin123456`、bucketName=`paiagent`、publicUrl=`http://localhost:9000`（均可被环境变量覆盖）。

**配置阶段 vs 运行阶段（和 McpToolConfigController 同样模式）**：MinioService 有三个上传方法，Controller 只用第一个：

| 方法 | 入参 | 谁调用 |
|---|---|---|
| `uploadFile` | 流 | **MediaController**（前端直传） |
| `uploadFromUrl` | URL 转存 | ImageGenerate/VideoGenerate NodeExecutor——第三方 API 返回临时 URL，转存到自己 MinIO |
| `uploadFromBytes` | 字节数组 | ImageGenerate（base64 解码）/ TTS NodeExecutor（合并音频 bytes） |

Service 同时服务"前端直传"和"引擎转存"两条路径，Controller 只暴露前端那一半，引擎那一半由 NodeExecutor 直接调 Service——和 `McpToolConfigController` 一模一样的套路。

给前端用——用户在工作流里上传参考图片（referenceImageUrl），先传 MinIO 拿 URL，再配到图片/视频节点。和阶段 12 知识库的 uploadKnowledgeTextFile 一样的 FormData 上传模式。

**完整数据请求链路**：

链路 A：图片生成（同步）
```
前端:image_generate 节点配 prompt + provider + 参考图
  ↓ flow_data JSON 整存
执行:WorkflowExecutor → NodeExecutorFactory.get("image_generate")
  → ImageGenerateNodeExecutor.execute(node, input)
    → configuredTextInput:取 prompt(inputParams input/reference)
    → resolveImageConfig + validateApiConfig
    → generateImage:switch(provider)
      - volcengine_agent_plan → agentPlanClient.generateImage
      - step → stepFunImageClient.generateImage
      - default → openAiCompatibleImageClient.generateImage
        → buildRequest + postJson(POST /v1/images/generations)
        → 解析 data[].url / b64_json
    → persistMedia:URL→uploadFromUrl / base64→uploadFromBytes(转存 MinIO)
    → buildOutput:imageUrl/imageUrls/prompt/model/metadata
  → 节点输出 → 下游节点
```

链路 B：视频生成（异步轮询）★
```
前端:video_generate 节点配 prompt + provider + 时长 + 首帧图
  ↓ flow_data JSON 整存
执行:WorkflowExecutor → NodeExecutorFactory.get("video_generate")
  → VideoGenerateNodeExecutor.execute(node, input, progressCallback)
    → 取 prompt + referenceImageUrl
    → resolve(node, "video") + validateApiConfig
    → emit "视频任务提交中" (SSE)
    → createVideoTask:agnes→agnesVideoClient / 否则→agentPlanClient
      → POST 创建任务,返回 taskId
    → emit "视频任务已提交: taskId=xxx" (SSE)
    → 轮询循环 for i in 0..60:
        Thread.sleep(5000)
        getVideoTask(taskId) 查状态
        emit "视频生成中: 第 N/60 次, 已等待 Xs, 状态=running, 进度=50%" (SSE)
        if success → break
        if failed → 抛异常
    → 拿 videoUrl → emit "视频转存中"
    → persistMedia:uploadFromUrl 转存 MinIO
    → buildOutput:taskId/videoUrl/coverUrl/model
  → 节点输出 → 下游节点
```

链路 C：TTS（分片并发）★
```
前端:tts 节点配 text(引用上游)+ provider + voice
  ↓ flow_data JSON 整存
执行:WorkflowExecutor → NodeExecutorFactory.get("tts")
  → TTSNodeExecutor.execute(node, input, progressCallback)
    → extractInputText:取文本(inputParams.text input/reference,或 input.output)
    → resolveConfig:全局配置优先 + provider/model/voice 默认值
    → validateConfig:只支持 qwen/step
    → splitText:按 maxLength/maxBytes + 标点切分
    → emit "文本已分割为 N 个片段" (SSE)
    → 并发:CompletableFuture 逐片
        synthesizeChunk:step→callStepTts(HTTP) / qwen→callQwenTts(SDK,加锁改全局 baseUrl)
        每片完成 emit 进度 (SSE)
    → allOf().join() 等全部
    → mergeWavFiles:44 字节头 + 拼 data + 改长度字段(小端序)
    → uploadFromBytes 上传 MinIO
    → buildOutput:audioUrl/chunks
  → 节点输出 → 下游节点
```

**和其他阶段的关系**：
- 阶段 7 节点执行器：都是 NodeExecutor，工厂分发。image_generate/video_generate/tts 三种节点类型
- 阶段 8 全局配置：configId → llmGlobalConfigService 复用
- 阶段 9 SSE：emit NODE_PROGRESS 推送进度（尤其视频轮询、TTS 分片）
- 阶段 4 reference：configuredTextInput 解析 inputParams 的 reference 类型（跨节点引用）
- Agent Plan（火山）：agentPlanClient 是火山的图片/视频客户端（下一阶段细讲）

**关键设计点**：
1. **三种调用模式**：图片同步 / 视频异步轮询 / TTS 分片并发。按任务特性选模式
2. **统一转存 MinIO**：厂商临时 URL → 持久 MinIO URL，不依赖外部资源
3. **多厂商适配**：switch(provider) 路由，default 走 OpenAI 兼容兜底。URL/参数/响应格式都做归一化
4. **模板方法 AbstractAgentPlanNodeExecutor**：图片/视频复用取值逻辑（configuredTextInput/applyOutputParams）
5. **配置全局优先**：configId → llmGlobalConfigService，节点级配置兜底
6. **TTS 智能分片**：maxLength + UTF-8 maxBytes + 标点切分，适配 API 限制
7. **TTS 并发合成**：CompletableFuture 逐片异步，allOf 等全部
8. **TTS 手写 WAV 合并**：44 字节头 + 拼 data + 改长度字段（小端序）
9. **视频轮询控制**：MAX_POLLS=60 + 5s 间隔 = 5 分钟上限，防无限等待
10. **进度全程 SSE**：每个阶段 emit NODE_PROGRESS，前端实时看进度
11. **防呆设计**：TTS 自动修正非 TTS 模型；视频 status 多 key 查找容错
12. **厂商 URL 归一化**：各种 apiUrl 格式统一成标准 endpoint，Agnes 域名迁移适配

**前端说明**：媒体生成没有独立前端页面（不像知识库/MCP 有独立 Page），节点的配置在前端 EditorPage 的节点面板里（选 provider/model/voice/上传参考图）。MediaController 的 `/api/media/images` 给前端上传参考图用。

#### Agent Plan Harness 集成体系详解（火山方舟能力套餐）★

**一句话总结**：PaiAgent 把火山方舟 **Agent Plan** 当作一份「能力套餐供应商」接进来：用户在全局配置里填一次 apiUrl/apiKey/多模型字段，工作流里的联网搜索、记忆召回、图片生成、视频生成、向量/RAG 这些能力节点就都能复用同一份配置；其中**聊天**走 Spring AI（路径特殊），**联网搜索**走 stdio MCP 子进程，**图片/视频/embedding** 走自研的 `VolcengineAgentPlanClient` 裸 HTTP 客户端，三者共享一份 `ResolvedAgentPlanConfig` 运行时配置。

**一、Agent Plan 是「套餐」，不是「节点」**（理解整个体系的前提）

Agent Plan 在 PaiAgent 里被建模成 `llm_global_config` 表里 `provider = volcengine_agent_plan` 的一条**全局配置记录**，挂了：apiUrl/apiKey/model（豆包）/embeddingModel（doubao-embedding-vision）/imageModel/videoModel/ttsModel/memoryEnabled。它**不是画布上能拖的节点**，而是「能力后端」——画布上的 `web_search`/`memory_retrieve`/`image_generate`/`video_generate`/`knowledge_retrieve` 节点运行时去这份配置取 apiUrl/apiKey/model 调对应能力 API。

**和自研 ReAct 的关系：互补，不是替代**（易混淆点）：

| 维度 | 自研 ReAct（ReActAgentNodeExecutor） | 火山 Agent Plan Harness |
|---|---|---|
| 角色 | **编排层**：决策→工具→观察→再决策循环 | **能力层**：提供 embedding/图/视频/搜索等能力 |
| 谁替代谁 | 不替代 | 不替代 |
| 谁调谁 | ReAct 工具**内部**调 Agent Plan 客户端 | 被 ReAct 工具和普通节点共用 |

证据：`MemoryRetrieveTool`（ReAct 工具）里 `configResolver.resolve(context.node(), "memory")` → `agentPlanClient.createEmbedding(config, query)` 拿向量 → `memoryService.retrieve`。ReAct 决定「调 memory_retrieve」（自研循环），工具内部取 Agent Plan 配置调客户端（能力外包）。**PaiAgent 选择自己掌控循环、只把能力外包给厂商**，不像 OpenAI Assistants 那样把整个 Agent Loop 交给厂商。

**二、整体执行链路图**

```
                llm_global_config (provider = volcengine_agent_plan)
                │ apiUrl/apiKey/model/embeddingModel/imageModel/videoModel/memoryEnabled
                ▼
        AgentPlanConfigResolver.resolve(node, capability)
                ▼
        ResolvedAgentPlanConfig (configId/provider/apiUrl/apiKey/model/...)
                │
        ┌───────┼───────────────────┐
        ▼       ▼                   ▼
  ① 聊天    ② 图/视频/embedding   ③ 联网搜索
  ChatClientFactory             SearchInfinityMcpClient
  createVolcengineArkChatModel  (stdio MCP 子进程, 阶段12 MCP 模块已讲)
  路径 /api/plan/v3/chat/      VolcengineAgentPlanClient
  completions (Spring AI)       (自研裸 HTTP)
        ▼       ▼                   ▼
  AbstractLLMNodeExecutor     ImageGenerate/VideoGenerate/
  ReActAgentNodeExecutor      Memory/Knowledge NodeExecutor
  VisionAnalyzeNodeExecutor   + 对应 ReAct 工具
```

三路客户端各管一段，不可合并（火山的接入协议不统一决定的，不是设计冗余）。

**三、VolcengineAgentPlanClient（图片/视频/embedding 裸 HTTP 客户端）**

类注释：「Thin HTTP client for Agent Plan capabilities. Endpoint details stay here instead of node executors.」——端点细节留在这层，节点执行器不碰厂商接口。

封装的 API：

| 方法 | HTTP | Path | 出参 |
|---|---|---|---|
| `createEmbedding(config, input)` | POST | `/embeddings` | `List<Double>` 向量 |
| `generateImage(config, prompt, referenceImageUrl, size, count, negativePrompt, style)` | POST | `/images/generations` | `Map{imageUrls, metadata}` |
| `createVideoTask(config, prompt, referenceImageUrl, duration, resolution, ratio, cameraMotion)` | POST | `/contents/generations/tasks` | `String taskId` |
| `getVideoTask(config, taskId)` | GET | `/contents/generations/tasks/{taskId}` | `Map{status, videoUrl, coverUrl, raw}` |

**重点：没封装「聊天」和「联网搜索」**。聊天走 Spring AI，联网搜索走 MCP。这是纯「多模态+向量」HTTP 客户端，用 `java.net.HttpURLConnection`（故意没用 RestTemplate/WebClient，避免 Spring AI 对 images 端点的假设）。

执行链路（以 generateImage 为例）：
```
generateImage: 构造 JSONObject request(model/prompt/response_format=url/output_format=png/watermark=false/stream=false; size 非空放 size; referenceImageUrl 非空放 image 字段=图生图)
  → postJson(config, "/images/generations", request)
    → openConnection: URL=normalizeBaseUrl(apiUrl)+normalizePath(path); POST/超时 15s+120s/Content-Type=application/json/Authorization=Bearer apiKey
    → 写 body 到 outputStream
  → readResponse: 2xx→inputStream 否则→errorStream; 非 2xx 抛 IOException("HTTP "+status+": "+text)
  → JSON.parseObject; 遍历 response.data 取 url 加入 urls
  → 返回 {imageUrls, metadata}
```

值得标注的细节：
- **视频任务多键兜底**：`getVideoTask` 用 `findString(response, "video_url","videoUrl","url")` 和 cover 的 `"last_frame_url","cover_url","coverUrl","poster_url"` 多键+递归查找。火山不同版本/模型返回字段名不一致，客户端做兼容。taskId 同样三键兜底（`id`/`task_id`/`taskId`）。
- **错误处理**：只看 HTTP status，非 2xx 抛 IOException，业务层错误（火山 code/message）不在这层解析，留给调用方。
- **URL 归一化**：`normalizeBaseUrl` 剥末尾 `/` 和 `/v1`（兼容用户误填 OpenAI 风格地址）。

**四、AgentPlanConfigResolver（配置解析中枢）★**

所有调 Agent Plan 能力的节点都先经过它拿 `ResolvedAgentPlanConfig`。三个 resolve 方法：`resolve(node, capability)`（通用，按 capability 选模型）/`resolveImageConfig(node)`（图片专用，多 step provider 兜底链）/`resolveKnowledgeConfig(configId, modelOverride)`（知识库用，不需 WorkflowNode）。

`resolve(node, capability)` 解析过程：
```
Step1 解析节点选的全局配置: nodeConfigId=data.configId → nodeGlobalConfig
Step2 解析节点显式指定: explicitAgentPlanConfigId=data.agentPlanConfigId（优先级最高）
Step3 决定用哪份 LLMGlobalConfig: resolveAgentPlanConfig(explicit, nodeGlobal)
   优先级: explicitAgentPlanConfigId > 节点 configId 指向的 > getDefaultConfig("volcengine_agent_plan")
Step4 字段层面(全局优先): apiUrl=firstText(globalConfig.apiUrl, data.apiUrl); apiKey 同理; provider=canonicalizeProvider(...)
Step5 按 capability 选 effectiveModel:
   embeddingModel/embedding→embeddingModel; image→imageModel(缺退到 languageModel); video→videoModel(缺退到 languageModel); default→languageModel
   embeddingModel 兜底 "doubao-embedding-vision"
Step6 memoryEnabled = globalConfig.memoryEnabled==1
Step7 组装 record 返回
```

**两层优先级**（分清楚）：
- **整条记录层**：节点 data.agentPlanConfigId（显式指定）> 节点 data.configId 指向的 > provider 默认配置
- **字段层**：globalConfig.xxx > data.xxx > 硬编码兜底（provider=volcengine_agent_plan, embeddingModel=doubao-embedding-vision）

注意：节点 data 上的 `model` 字段不是无脑覆盖，而是**按 capability 决定要不要用**——`resolve(node,"video")` 时 nodeModel 作 videoModel 候选；`resolve(node,"memory")` 时 nodeModel 作 embeddingModel 候选。这让前端用一个 `model` 输入框服务多种 capability。

`validateApiConfig`：只校验 apiUrl/apiKey/model 非空，不校验 provider（provider 归一化在 resolve 阶段强制做）。

**五、ResolvedAgentPlanConfig（解析后运行时配置，record）**

```java
public record ResolvedAgentPlanConfig(
    Long configId, String provider, String apiUrl, String apiKey,
    String model,           // 当前 capability 的有效模型
    String embeddingModel, String imageModel, String videoModel,
    boolean memoryEnabled
) {}
```

| 字段 | 来源 | 用途 |
|---|---|---|
| configId | 选定的 LLMGlobalConfig.id | 回写节点/日志 |
| provider | canonicalizeProvider 后 | 决定走哪个客户端分支 |
| apiUrl/apiKey | 全局>节点 | HTTP baseUrl/Bearer token |
| model | 按 capability 选出 | 调 API 塞 model 字段 |
| embeddingModel/imageModel/videoModel | 各能力默认值 | 这份配置上各能力的默认 |
| memoryEnabled | globalConfig.memoryEnabled==1 | 控制是否走记忆召回 |

**为什么 record**：解析后的不可变快照，多节点/ReAct 工具安全共享引用。配置变了重新 resolve 拿新快照，不污染正在执行的链路。`model` 与 embedding/image/videoModel 并存：model 是「当前调用要用的」，其他是「这份配置各能力默认值」。

**六、「Agent Plan」名字在多处的含义对照**（最易绕晕）

| 出现位置 | 实际是什么 | 数据来源 | 调用方式 |
|---|---|---|---|
| (a) 联网搜索 MCP | `McpToolConfigService.createAgentPlanWebSearch`，一条 mcp_tool_config 记录(toolType=agent_plan_web_search) | 前端只填搜索专用 apiKey | stdio 子进程 uvx mcp-server-askecho-search-infinity |
| (b) 图/视频/embedding | `VolcengineAgentPlanClient` | ResolvedAgentPlanConfig(LLMGlobalConfig) | 裸 HTTP 直连火山 |
| (c) 聊天 provider | ChatClientFactory 的 volcengine_agent_plan 分支 | LLMGlobalConfig(同 b) | Spring AI OpenAiChatModel |

**底层是同一个火山套餐，但接入方式不同**：(b)(c) 共享同一份 LLMGlobalConfig(provider=volcengine_agent_plan)，取 apiUrl/apiKey/model，区别只在客户端实现；(a) 不共享 LLMGlobalConfig，存另一张表 mcp_tool_config，只存搜索专用 apiKey(ASK_ECHO_SEARCH_INFINITY_API_KEY)，因为联网搜索走火山开源的 MCP server，MCP server 自己知道端点。

**为什么分三路**：火山 Agent Plan 没有统一 OpenAI 兼容入口覆盖所有能力——聊天接口 OpenAI 兼容但路径特殊→Spring AI 覆盖路径；图/视频/embedding 标准 HTTP POST JSON→自研客户端最直接；联网搜索火山官方只提供 MCP server 无 REST API→必须 stdio MCP。**被迫的适配，不是设计冗余**。

**七、ChatClientFactory 对 volcengine_agent_plan 的特殊处理**

聊天走单独的 `createVolcengineArkChatModel`：用 OpenAiApi 的 7 参构造函数，显式传 `chatCompletionPath="/api/plan/v3/chat/completions"` 和 `embeddingsPath="/api/plan/v3/embeddings"` 覆盖 Spring AI 默认的 `/v1/...`。`normalizeAgentPlanBaseUrl` 剥末尾 `/`、`/api/plan/v3/chat/completions`、`/api/plan/v3`，兼容用户把完整接口地址填进 apiUrl。

⚠️ **潜在坑点（重点关注）**：`VolcengineAgentPlanClient.normalizeBaseUrl` 只剥 `/v1`，`ChatClientFactory.normalizeAgentPlanBaseUrl` 剥 `/api/plan/v3`——**两个客户端对 baseUrl 归一化逻辑不一致**。如果用户把 apiUrl 填成 `https://ark.cn-beijing.volces.com/api/v3`（火山标准 Ark 路径），ChatClient 能处理，但 VolcengineAgentPlanClient 会保留 `/api/v3` 再拼 `/images/generations`，路径对不对取决于火山实际接口。建议测试时验证 apiUrl 填不同形式时的行为。

**八、AbstractAgentPlanNodeExecutor（能力节点纯工具基类）**

不绑定厂商细节，给所有「Agent Plan 能力节点」提供节点数据读取工具：`textValue`（多级兜底取值）/`configuredTextInput`（inputParams 按 name 找参数，支持 reference 跨节点引用）/`applyOutputParams`（输出字段映射）/`stringData`/`intData`/`doubleData`。继承它的子类：ImageGenerate/VideoGenerate/WebSearch/MemoryWrite/MemoryRetrieve/KnowledgeUpsert/KnowledgeRetrieve/VisionAnalyze NodeExecutor。

注意：`AbstractAgentPlanNodeExecutor` 和 `AbstractLLMNodeExecutor` 是**两个平行抽象基类**——前者给能力节点（只有数据读取工具），后者给 LLM/ReAct 节点（注入 ChatClientFactory/SkillRegistry/AgentMemoryService/KnowledgeBaseService，**也注入** AgentPlanConfigResolver + VolcengineAgentPlanClient 用于 LLM 节点记忆召回 buildContextPrompt）。所以 `ReActAgentNodeExecutor extends AbstractLLMNodeExecutor` 间接持有 agentPlanClient，但 ReAct 自己没直接用——是它的工具（MemoryRetrieveTool 等）在用。

**九、关键设计点**

1. **为什么用厂商 Agent Plan 而非自研**：联网搜索（需爬虫+索引，火山送搜索额度）、记忆召回（需向量模型，火山内置 doubao-embedding-vision）、多模态生成（图/视频模型自研成本极高）三类能力自研不现实。选择「编排自己掌控，能力外包给厂商」——不把整个 Agent 循环交给厂商，只外包具体能力节点，工作流图结构/断点续执行/节点级调试还在自己手里。
2. **配置解析两层优先级**：整条记录层（显式 agentPlanConfigId > 节点 configId > provider 默认）；字段层（全局 > 节点 > 兜底）。前端只填一份全局配置覆盖大部分场景，又允许节点级覆盖单个字段。
3. **多端点适配**：火山路径不统一（Chat `/api/plan/v3/chat/completions`、Embeddings `/api/plan/v3/embeddings`、Images `/images/generations`、Video `/contents/generations/tasks`），ChatClientFactory 显式覆盖 Spring AI 默认路径，VolcengineAgentPlanClient 自己拼路径不依赖 Spring AI。
4. **媒体产物统一转存 MinIO**：厂商临时 URL 过期，下游节点（条件分支/vision_analyze）可能复用，转存 MinIO 拿持久 URL。转存失败保留原 URL 不抛异常（降级，不阻断流程）。
5. **provider 归一化散落四处**（ChatClientFactory/AgentPlanConfigResolver/LLMGlobalConfigService/AbstractLLMNodeExecutor 各有一份 canonicalizeProvider）——同样 switch 逻辑散落四处，加新 provider 要改四处。**代码异味，待重构点**。
6. **ResolvedAgentPlanConfig 用 record**：不可变快照，线程安全，多节点/工具共享。Java 16+ record 典型用法。
7. **视频生成异步轮询 + SSE 进度**：createVideoTask 拿 taskId → 循环 getVideoTask（MAX_POLLS=60×5s=5 分钟）→ 每次轮询 emit SSE 进度（"视频生成中: 第 N/60 次, 已等待 Xs, 状态=running, 进度=45%"）→ 成功转存 MinIO。
8. **ReAct 工具和节点执行器共享底层客户端**：MemoryRetrieveTool（ReAct 工具）和 MemoryRetrieveNodeExecutor（节点执行器）注入完全相同三件套（AgentPlanConfigResolver+VolcengineAgentPlanClient+AgentMemoryService），调用代码几乎一样——保证「拖 memory_retrieve 节点」和「ReAct 调 memory_retrieve 工具」行为一致。**能力即节点 + 能力即工具**双面设计。

**十、重点关注（高优先级条目）**

1. **Agent Plan 是套餐不是节点**——理解整个体系的第一前提。画布上的 image_generate/memory_retrieve 是节点，Agent Plan 是背后配置+能力后端。
2. **三路客户端并存不可合并**：聊天 Spring AI（路径特殊）/ 图视频 embedding 自研 HTTP / 联网搜索 stdio MCP。火山接入协议不统一决定的。
3. **配置解析两层优先级**：整条记录层「显式 agentPlanConfigId > 节点 configId > provider 默认」；字段层「全局 > 节点 > 兜底」。
4. **VolcengineAgentPlanClient 没封装聊天和联网搜索**——别误以为它管所有 Agent Plan 能力。聊天在 ChatClientFactory，联网搜索在 SearchInfinityMcpClient。
5. **视频异步轮询** 5 分钟上限 + SSE 进度；图片同步返回 URL。两者结果都转存 MinIO。
6. **provider 归一化散落四处**，潜在重构点。
7. **normalizeBaseUrl 两客户端逻辑不一致**（VolcengineAgentPlanClient 剥 /v1，ChatClientFactory 剥 /api/plan/v3），填 apiUrl 要注意。
8. **ResolvedAgentPlanConfig 是 record**，不可变快照，多节点/工具安全共享。
9. **ReAct 工具和节点执行器共享底层客户端**，「能力即节点 + 能力即工具」双面设计关键。
10. **agentPlanConfigId 是节点 data 可选字段**，用于「节点想用和 configId 不同的 Agent Plan 配置」的细粒度覆盖，日常用 configId 就够，agentPlanConfigId 是高级用法。

---

**断点续执行**（原占位标记的另一项）：已在阶段 6（resumeExecution 链路：查 record → parse+排序 → 查快照 → resolveResumeStartNodeId 定起点 → buildResumeState 从快照恢复已成功节点输出 → 从起点继续）+ 阶段 9（前端 DebugDrawer 失败后显示"继续"按钮 → resumeWorkflowExecution → 后端 resumeExecution）讲过，此处不再重复。

---

# 附录：核心执行链路速查图

```
【执行工作流 - DAG 引擎完整链路】

前端 EditorPage 点击"执行/调试"
   │
   ├─ 普通执行：POST /api/workflows/{id}/execute  (api/workflow.ts)
   └─ 实时执行：GET  /api/workflows/{id}/execute/stream  (SSE, DebugDrawer)
   │
   ▼
ExecutionController.executeWorkflow / executeWorkflowStream
   │  1. workflowService.getById(id) 查工作流
   │  2. engineSelector.selectEngine(workflow) 按 engineType 选引擎
   ▼
EngineSelector.selectEngine
   │  遍历注入的 List<WorkflowExecutor>，匹配 getEngineType()
   ▼
WorkflowEngine.execute / executeWithCallback   （DAG 引擎）
   │  1. WorkflowConfigParser 解析 config JSON → WorkflowConfig
   │  2. DAGParser 拓扑排序(Kahn) + 循环检测(DFS) → 得到执行顺序
   │  3. 遍历节点：
   │       NodeExecutorFactory.getExecutor(type)  → 具体 NodeExecutor
   │       executor.execute(node, inputMap)        → 输出 Map
   │       （LLM 节点：AbstractLLMNodeExecutor → ChatClientFactory → Spring AI）
   │       上游输出写入 context，作为下游输入
   │       每步触发 ExecutionEvent 回调（SSE 推送）+ 写 ExecutionSnapshot
   ▼
汇总结果 → ExecutionResponse → 写 ExecutionRecord → 返回前端
```

---

# 使用说明（给你自己）

- 每追完一个阶段，有疑问就问我，问的时候说清楚**在看哪个文件、哪一行、想搞懂什么**。
- 我会按你 CLAUDE.md 里的要求，讲清楚：**数据请求链路 + 为什么这样设计 + 代码怎么执行 + 走了哪些方法**，然后**把讲解回填到对应阶段的「📝 讲解归档」区**。
- 复习时，直接看每个阶段的「讲解归档」即可，那是你自己的知识沉淀。
```
