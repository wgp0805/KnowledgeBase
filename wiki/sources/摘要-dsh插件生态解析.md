---
title: "摘要-dsh插件生态解析"
type: source
tags: [来源, DeepSeekHarness, dsh, 插件生态, 开源]
sources: [raw/09-archive/2026-10-12-DeepSeek Harness 插件生态解析 - 我才是银古.md]
last_updated: 2026-10-13
---

## 核心摘要
基于 `awesome-dsh-plugin` 清单对 [[DeepSeekHarness]]（`dsh`）插件生态的全量数据解析。**插件是 dsh 的唯一扩展面**——模型、工具、沙箱、会话存储、UI 甚至 agent loop 本身都能替换；一个插件 = 在 `package.json` 声明 `dsh.bundle.patch` 的 npm 包，底层跑在 Cordis + Schemastery 上。生态共 4,349 个仓库 / 23 类目，57% 近 30 天有提交，但 star 极度头部化（Top 25 占 79.8%），是一个**供给过剩、注意力稀缺的早期生态**。

## 关键信息

### 插件身份与装配
- 唯一硬门槛：`"dsh": { "bundle": { "patch": "./cordis.patch.yml" } }`，官方 CI 会扫根包与 `packages/`/`plugins/`/`apps/` 子包
- 装配是**声明式补丁描述**而非 `require()` 代码，是 Cordis 框架的能力织入模型
- `client.inject` 显式列出要注入哪些官方 UI 包，同时给出不匹配时的失败边界
- peer 依赖写在非标准的 `peer` 字段，说明 dsh 有自己的依赖解析路径
- 分发走 npm，下载量自动采集；插件可只针对某个 profile 生效（`--profile web/headless/pi-tui/data`）

### ⚠️ semver 预发布陷阱
dsh 官方仍在 rc 阶段（`^0.2.0-rc.2`）：**不带显式预发布分支的 peer 范围会静默排除所有预发布构建**。看起来全匹配的 `>=0.0.0-0 <0.2.0-0` 也匹配不到 `0.1.0-rc.6`，用户 `npm install` 撞 ERESOLVE 却看不出是版本范围写错。正确写法是显式加 `||` 分支。

### 生态数据
- 4,349 仓库 / 4,508 条目（476 条指向 monorepo 子包）/ 23 类目；中位数 2⭐，P90 20⭐，P99 687⭐
- 原生插件仓库 4,009 个，上游集成子包 313 个；剔除后 star 第一是 `dsh-web`（8,650⭐，monorepo），单包形态第一是 `dsh-routing-suite`（7,019⭐）
- **类目热度**：Memory 209 条 100,218⭐ + Docs & Rendering 68 条 83,320⭐ 合计吃掉全站 49%；WSL 互操作 77 条仅 160⭐、Voice 65 条 401⭐
- 供给大头：UI Enhancements 786 + Tools 585 + Dev & Runtime 323 条，占近四成——恰是写插件成本最低的三个入口
- 上游集成代表：archify、hindsight、OpenViking、WeKnora、BrowserSkill、loopx、ouroboros、mirage、ReMe、memsearch——主流 agent 工具链已把"给 dsh 出一个包"当标配分发渠道

### 四个趋势
1. **右侧边栏变成扩展总线**：`dsh-client-ui-sidebar-right` 成为二级平台，DSH-better-sidebar 之上挂了 docx 视图、任务看板、短视频侧边栏等
2. **插件互相依赖**：better-sidebar 依赖 `@huanlin/dsh-plugin-better-locale`，从单星拓扑走向横向组合
3. **手机远程审批成刚需**：dsh-pocket / dsh-pocket-console（把工具审批推成飞书卡片，超时 120s）/ dsh-reach / dsh-weave / dsh-devices 一整条产品线
4. **娱乐化程度惊人**：137 个 Just for Fun（Live2D 宠物、像素扭蛋、弹跳 deepseek、"没有任何实际用途"的自述）

### 安全提醒（重要）
- 装插件 = 在机器上以本人权限跑第三方代码；**工具审批（tool approval）不会沙箱化插件代码**，两者常被混淆
- "被收录"不等于"被审计"——准入门槛只有四条（能装、描述相符、类目正确、有人维护），官方自称"常识性检查，不是审计"
- 头部插件 `dsh-infinite-gen-4`（2,671⭐）功能是以最高优先级往系统提示追加"无条件服从"段落（armor）
- 安全类目里真正做正事的：`dsh-plugin-guard`（安装前静态审计、安装后哈希与能力锁）、`dsh-permgate`（细粒度审查工具调用）、`dsh-auto-mode`（新增 Auto 权限档）

## 关联连接
- [[DeepSeekHarness]] — 核心实体
- [[插件生态]] — 生态分析概念
- [[everything-is-a-plugin]] — 架构理念
- [[Cordis]] — 底层框架
- [[摘要-deepseek-harness命令大全]] — 命令与 profile 前置知识
- [[摘要-dsh桌面版-electron源码解析]] — 桌面客户端
