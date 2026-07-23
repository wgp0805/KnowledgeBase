---
title: "loop-best-practice-java-fullstack"
type: synthesis
tags: [Loop, Java, SpringBoot, Vue3, Maven, TDD, 最佳实践]
sources: [raw/09-archive/Loop Engineering 实战指南.md, raw/09-archive/Prompt 已死，Loop当立？先看完这5个生产级坑再决定.md]
last_updated: 2026-07-23
---

# Loop 最佳实践（Java 全栈版）

> 适用技术栈：Spring Boot 3/4 + Maven + Vue 3 + MySQL/PostgreSQL
> 项目形态：单体应用、前后端分离、同一仓库（monorepo）
> 本地开发：不使用 Docker，直接本地运行

---

## 一、场景速查表

| 你的场景 | 推荐模式 | 模板位置 |
|---------|---------|---------|
| 读了一篇技术文章，想快速实现 demo | **STATE.md 驱动循环** | 模板 1 |
| 写代码时自动编译检查 | **`/loop` 定时构建** | 模板 2 |
| 改完代码自动跑测试 | **`/loop` 定时测试** | 模板 3 |
| TDD：先写测试再让代码通过 | **STATE.md 驱动 + 验证循环** | 模板 4 |
| 前后端联调，同时检查编译 | **并行编译循环** | 模板 5 |
| 长时间异步任务（等 CI/等部署） | **ScheduleWakeup 动态循环** | 模板 6 |

---

## 二、核心概念澄清

Claude Code 中有两种"循环"，不要混淆：

| | `/loop` 定时命令 | STATE.md 开发循环 |
|---|---|---|
| **本质** | 固定间隔重复执行同一任务 | 状态驱动的逐步推进 |
| **语法** | `/loop 5m <提示词>` | 对 AI 说"开始开发循环" |
| **适合** | 监控/编译/测试等重复性检查 | 读文章实现/TDD/多步骤开发 |
| **状态保持** | 不保持，每轮独立 | 通过 STATE.md 持久化进度 |

**推荐组合使用**：用 STATE.md 记录进度，用 `/loop` 或 `ScheduleWakeup` 驱动每轮执行。

---

## 三、模板详解

### 模板 1：读文章 → 技术落地循环

**适用场景**：看到一篇技术文章（如"Spring Boot 4 + Vue 3 集成 WebSocket"），想快速实现 demo。

#### 执行步骤

```
第一步：把文章丢给 AI，说下面这句话：

"请阅读这篇文章，提取核心实现要点，创建一个 STATE.md 文件
列出实现步骤，每一步都要可验证（编译通过/测试通过/页面可访问）。
然后开始开发循环，按步骤逐一实现，每完成一步更新 STATE.md 并问我是否继续。"
```

#### 配套 STATE.md 模板

将以下内容放在项目根目录的 `STATE.md` 中，每次循环自动更新：

```markdown
# 开发循环状态

## 目标
[文章标题 / 要实现的特性]

## 完成标准
- [ ] 后端编译通过（`mvn compile -q`）
- [ ] 前端编译通过（`npm run build`）
- [ ] 关键功能手动验证通过
- [ ] 数据库迁移脚本可执行

## 已完成
- [x] 1. 阅读文章，提取要点  (2026-07-23)

## 待完成
- [ ] 2. 创建 Spring Boot 项目结构 + Maven 依赖
- [ ] 3. 编写 Entity / Repository / Service 层
- [ ] 4. 编写 Controller + 配置路由
- [ ] 5. 编写 Vue 3 页面 + API 调用
- [ ] 6. 运行 `mvn compile` 确认后端编译通过
- [ ] 7. 运行 `npm run build` 确认前端编译通过
- [ ] 8. 启动应用，手动验证功能

## 当前焦点
步骤 2：创建项目结构

## 阻塞项
- 无
```

#### 完整的启动命令

```bash
# 一次性启动命令（复制后直接贴给 Claude Code）：
我已经把文章内容发给你了。请做以下事情：
1. 读取文章内容，提取核心实现要点
2. 创建 STATE.md 记录实施计划（每步必须可验证）
3. 开始开发循环，从步骤 1 开始执行
4. 每完成一步，更新 STATE.md 并问我 "是否继续"
5. 我说 "y" 或 "继续" 后执行下一步
```

---

### 模板 2：编译检查循环（后端）

**适用场景**：修改 Java 代码时，让 Claude Code 每隔几分钟自动检查编译是否通过。

```bash
# 每 3 分钟检查一次 Maven 编译
/loop 3m 运行 mvn compile -q 2>&1，如果编译失败，报告错误位置并尝试修复；如果编译通过，报告 "编译通过" 并等待下一轮

# 如果只想检查不修复（纯监控模式）：
/loop 5m 运行 mvn compile -q 2>&1，只报告编译是否通过，不要修改代码
```

**进阶用法**：跳过测试的快速编译

```bash
/loop 3m mvn compile -DskipTests -q 2>&1
```

---

### 模板 3：测试循环（后端）

**适用场景**：修改代码后自动跑测试，失败自动修复。

```bash
# 运行全部测试，失败则修复
/loop 5m 运行 mvn test 并解析结果。如果有测试失败：
1. 读取失败的测试代码和被测试代码
2. 修复 bug
3. 重新运行该测试类
4. 如果修复成功，继续等待下一轮；如果修复失败，报告具体错误

# 只跑指定模块的测试（多模块项目）
/loop 5m mvn test -pl user-service -am -q 2>&1
```

**关键技巧**：用 `-q`（quiet）模式减少输出噪音，只关注错误。

```bash
# 最简模式
/loop 5m mvn test -q 2>&1 | tail -20
```

---

### 模板 4：TDD 循环（红-绿-重构）

**适用场景**：先写测试，再让代码通过测试，最后重构。

#### 配套 STATE.md

```markdown
# TDD 循环状态

## 当前目标
[要实现的功能描述]

## 循环状态
- [ ] RED: 编写失败的测试
- [ ] GREEN: 实现代码让测试通过
- [ ] REFACTOR: 优化代码结构

## 测试结果
- 总测试数: 0
- 通过: 0
- 失败: 0

## 失败详情
- (无)
```

#### 启动命令

```bash
# 启动 TDD 循环：
开始 TDD 循环。当前目标：[功能描述]。
先写测试（RED 阶段），确认测试失败后进入实现阶段（GREEN 阶段），
实现完成后重新跑测试确认通过，然后进入重构（REFACTOR 阶段）。
每完成一个阶段更新 STATE.md 并问我是否继续。
```

#### 全自动 TDD（无人值守模式）

```bash
# 信任 AI 后使用：
开始 TDD 循环，目标：[功能描述]。
自动执行 RED→GREEN→REFACTOR 循环，不需要我确认。
每轮汇报当前阶段和测试结果即可。
目标全部完成时通知我。
```

---

### 模板 5：前后端联合编译循环

**适用场景**：同时修改了前后端代码，需要确保两端都编译通过。

```bash
# 前后端并行编译检查
/loop 5m 执行以下检查：
1. 运行 mvn compile -q -DskipTests，检查后端编译
2. 运行 npm run build --prefix src/main/frontend，检查前端构建
3. 如果两端都通过，报告 "前后端编译均通过"
4. 如果任一端失败，报告具体错误位置并尝试修复
```

**注意**：如果你的前端目录不是 `src/main/frontend`，请替换为实际路径。

---

### 模板 6：ScheduleWakeup 动态循环

**适用场景**：等待异步任务完成（如数据库迁移、文件生成、API 调用），不需要固定间隔轮询。

```bash
# 启动一个动态循环，让 AI 自己决定何时重试
/loop 动态 等待数据库迁移完成，每轮检查 flyway_schema_history 表是否有新记录，
如果迁移未完成，安排 30 秒后重试；如果完成，报告迁移结果
```

---

## 四、CLAUDE.md 配置片段

将以下内容加入你的项目 `CLAUDE.md`，让 Claude Code 知道你的项目结构和循环规则：

```markdown
## 构建与测试

### 后端
- 编译: `mvn compile -q -DskipTests`
- 测试: `mvn test -q`
- 单测: `mvn test -Dtest=XXXTest -q`
- 打包: `mvn package -DskipTests -q`

### 前端
- 目录: `frontend/` 或 `src/main/frontend/`
- 安装依赖: `npm install`
- 构建: `npm run build`
- 开发: `npm run dev`

### 数据库
- MySQL: 本地 3306 端口
- PostgreSQL: 本地 5432 端口
- 迁移工具: Flyway / Liquibase

## 循环规则
- 每次循环只做一件事，完成后更新 STATE.md
- 编译失败时先修复编译错误，再继续其他任务
- 测试失败时报告具体失败位置和原因
- 前后端修改同时存在时，两端都编译通过才算完成
```

---

## 五、快速启动速查表

| 你想做什么 | 输入 |
|-----------|------|
| **读文章 → 实现 demo** | 贴文章内容 + 说"读这篇文章，创建 STATE.md 并开始开发循环" |
| **检查编译** | `/loop 3m mvn compile -q 2>&1` |
| **跑测试** | `/loop 5m mvn test -q 2>&1 \| tail -20` |
| **TDD 模式** | 说"开始 TDD 循环，目标：[功能]" |
| **前后端都检查** | `/loop 5m 先后端编译再前端构建，都通过才报告成功` |
| **查看进度** | 说"当前进度如何" 或 `/read STATE.md` |
| **暂停循环** | 按 `Esc` 或说"暂停" |
| **切换到无人值守** | 说"自动继续，不需要确认，做完汇报" |
| **修改循环间隔** | 说"改成每 10 分钟检查一次" |

---

## 六、常见坑与对策

### 坑 1：编译输出太多，看不到关键错误
**对策**：加 `-q`（quiet）和 `| tail -20`：
```bash
/loop 3m mvn compile -q 2>&1 | tail -30
```

### 坑 2：测试跑太久，循环卡住
**对策**：指定只跑最近修改的测试类：
```bash
/loop 3m mvn test -Dtest=UserServiceTest -q 2>&1
```

### 坑 3：前端 node_modules 不存在
**对策**：在循环前先 `npm install`，或者写进 CLAUDE.md 的规则中。

### 坑 4：循环跑偏了（在做无关的事情）
**对策**：按 `Esc` 或说"回到 STATE.md 当前焦点，不要做其他事情"。

### 坑 5：上下文膨胀导致性能下降
**对策**：每 5-6 轮后手动 `/compact`，或说"压缩上下文，保留 STATE.md 状态"。

---

## 七、个性化清单

使用前请根据你的项目修改以下内容：

- [ ] 替换 `mvn` 为实际 Maven 命令（Windows 用 `mvn.cmd` 或 `mvn`）
- [ ] 确认前端目录路径（`frontend/` 还是 `src/main/frontend/`）
- [ ] 确认数据库端口（MySQL 3306 / PostgreSQL 5432）
- [ ] 确认测试命令（`mvn test` 还是 `mvn verify`）
- [ ] 复制 CLAUDE.md 配置片段到你的项目 CLAUDE.md

---

## 关联连接
- [[LoopEngineering]] — 循环工程方法论
- [[loop-prompt-skill-guide]] — Loop/Prompt/Skill 三者区别
- [[ClaudeCode]] — Claude Code 平台与 Query Loop
- [[CLAUDEmd]] — 项目指令文件规范
- [[Skill]] — 技能扩展机制
- [[摘要-loop-engineering-guide]] — 方法论来源
- [[摘要-loop-engineering-pitfalls]] — 生产实践来源
- [[SpringBoot]] — Spring Boot 框架
- [[Vue3]] — Vue 3 前端框架
- [[Maven]] — 项目构建工具
- [[MySQL]] — 数据库
- [[PostgreSQL]] — 数据库