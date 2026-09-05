---
title: "AI native: Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师"
source: "博客园"
url: "https://www.cnblogs.com/fnng/p/20914242"
date: "2026-06-29T03:37:00Z"
score: 0.65
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# AI native: Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/fnng/p/20914242  
> **抓取日期**: 2026-06-29  
> **相关性评分**: 0.65

# Casebook

Casebook 是面向 AI Agent 时代的测试用例工程化工作流。

> 测试工程师应该使用 Lingma、Trae、Codex、Claude Code、Cursor 等 AI Agent 在项目中理解需求、生成用例、重构用例；Casebook 负责把这些工程化用例变成可以本地浏览、评审、标记、执行和生成报告的工作台。

Casebook 不是另一个测试用例管理平台，而是在 AI Agent 时代重新定义测试用例资产该如何被创建、维护和使用。

## 设计理念

传统测试用例管理的常见思路是：上传需求到平台，生成 XMind 或 Excel，用例再被下载、导入、复制、维护。即使接入了 AI，本质上仍然是把 AI 包装进平台流程里，测试用例依旧是孤立的表格资产。

Casebook 的设计从一开始就是 AI-native 的工程项目：

  * 需求文档放在 `docs/requirements/`，成为 AI 理解业务的输入。
  * 测试设计方法写进 `.agents/skills/`，让 AI 知道如何像测试人员一样设计用例。
  * 用例结构由 `schema/test-case-schema.json` 约束，保证 AI 输出稳定可校验。
  * YAML 用例存放在 `releases/`，可以被 Git 管理、Code Review、回滚和追踪。
  * 评审标记、执行结果和报告数据独立保存，不污染用例定义。
  * 本地 Web UI 只负责查看、评审、标记、轻量编辑、执行和报告，不试图替代 AI Agent 的生成能力。



因此，Casebook 不是把 AI 当作平台上的一个“生成按钮”，而是把 AI Agent 当作测试用例工程的主要生产力。

### Casebook 下的分工

  * **🧑 人负责判断** ：需求是否理解正确、风险是否覆盖充分、用例是否值得执行、失败是否真实有效。
  * **🤖 AI Agent 负责生产** ：读取需求和技能包，生成、补充、删除、重构 YAML 用例。
  * **📐 Schema 负责约束** ：保证用例结构稳定，降低 AI 输出漂移。
  * **🌿 Git 负责协作** ：让用例变成可审查、可追踪、可回滚的工程资产。
  * **🧰 Casebook 负责工作台** ：浏览、筛选、标记、轻量编辑、执行统计和报告生成。



## 完整工作流程

Casebook 推荐的流程是一个闭环：

![flow](https://img2024.cnblogs.com/blog/311516/202606/311516-20260629113445795-515388141.png)
    
    
    docs/requirements/ 需求文档
      + .agents/skills/ 测试设计技能包
      + schema/test-case-schema.json 格式约束
        -> AI Agent 理解需求并生成 YAML 用例
        -> releases/<需求或版本目录>/<功能>.yaml
        -> casebook export <需求或版本目录>
        -> 可分发的静态 HTML 评审/冒烟用例包
        -> casebook serve <需求或版本目录>
        -> 本地浏览、评审、标记、轻量编辑、执行
        -> .casebook/marks.json + test-runs/<run-id>.json
        -> casebook report <run-file>
        -> HTML 测试报告
    

这也是 Casebook 和一般AI测试用例平台最大的区别：

对比维度 | 一般 AI 测试用例平台 | Casebook  
---|---|---  
中心 | 测试管理平台 | Git 仓库 + AI Agent  
AI 角色 | 生成用例文本的接口 | 理解需求、维护用例、重构资产的生产者  
用例资产 | 平台数据库记录 | YAML 文件  
需求资产 | 平台字段、附件、富文本 | `docs/requirements/` 中的 Markdown/文档  
约束方式 | 平台表单和后端校验 | `schema/test-case-schema.json`  
协作方式 | 平台流程 | Git diff / PR / Code Review  
人的工作 | 填表、编辑、维护状态 | Review、判断、执行、验收  
去掉 AI 后 | 平台仍完整运行 | Casebook 仍能浏览/执行，但用例生产和持续维护能力大幅下降  
  
传统平台本质上是“人填数据，AI 辅助生成”。Casebook 本质上是“AI 维护工程资产，人做质量判断”。

## 安装

在本仓库中安装：
    
    
    pip install casebook
    

安装后可以使用：
    
    
    casebook --help
                                                                                                  
     Usage: casebook [OPTIONS] COMMAND [ARGS]...                                                   
                                                                                                   
     Render, review, and edit YAML test cases locally.                                             
                                                                                                   
    ╭─ Options ───────────────────────────────────────────────────────────────────────────────────╮
    │ --version          Show the Casebook version and exit.                                      │
    │ --help             Show this message and exit.                                              │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ──────────────────────────────────────────────────────────────────────────────────╮
    │ serve  Start the local Casebook web UI.                                                     │
    │ init   Create a new Casebook test case project.                                             │
    │ export Export YAML test cases to a standalone review HTML file.                             │
    │ report Generate an HTML test report from a test run JSON file.                              │
    │ renumber  Renumber test case IDs in one YAML file.                                          │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────╯
    
    

## Casebook 使用旅程

下面用一个从需求到报告的完整闭环，快速跑通 Casebook。

### 1\. 创建用例工程

先创建一个新的 Casebook 项目：
    
    
    casebook init my-casebook
    cd my-casebook
    

初始化后，你会得到一套标准工程结构：
    
    
    my-casebook/
      AGENTS.md
      .agents/skills/casebook-test-cases/SKILL.md
      docs/requirements/login.md
      releases/example/login.yaml
      schema/test-case-schema.json
    

其中 `docs/requirements/login.md` 和 `releases/example/login.yaml` 是一组配套示例，可以直接用来体验完整流程。

### 2\. 启动本地工作台

如果使用初始化自带示例，可以运行：
    
    
    casebook serve releases/example
    

默认地址：
    
    
    http://127.0.0.1:8089
    

### 3\. 评审和轻量编辑用例

![test-case](https://img2024.cnblogs.com/blog/311516/202606/311516-20260629113513203-708776923.png)

在本地工作台中，你可以：

  * 按文件浏览 YAML 用例。
  * 按优先级、Mark 状态和关键词筛选用例。
  * 展开用例查看前置条件、步骤和预期结果。
  * 使用 Mark 标记需要关注或后续调整的用例。
  * 对已有用例做轻量编辑，并保存回 YAML 文件。
  * 评审插入或删除用例后，使用 `ID 更新` 按当前 YAML 顺序重排用例 ID。



> 如果评审后需要新增、删除、拆分或重构用例，推荐继续交给 AI Agent 修改 YAML，而不是在页面中逐条维护。  
>  `ID 更新` 只适合评审阶段；选择测试计划后会禁用，避免执行结果和用例 ID 错位。

### 4\. 导出静态 HTML 用例包

如果评审场景无法使用自己的电脑，或者需要把冒烟用例发给开发，可以将 YAML 用例导出为一个可离线打开的 HTML：

![test-case-html](https://img2024.cnblogs.com/blog/311516/202606/311516-20260629113524833-1380084810.png)
    
    
    casebook export releases/example
    

默认目录会聚合为一个 HTML，例如：
    
    
    releases/example -> casebook-example.html
    

也可以导出单个 YAML，或指定输出文件：
    
    
    casebook export releases/example/login.yaml
    casebook export releases/example --output login-review.html
    

导出的 HTML 是评审视图，支持搜索、筛选、展开/收起，并内置 `Needs update` 标记和备注。标记和备注保存在浏览器本地，也可以通过 `Export review notes` 下载为 JSON。

可以按标签或优先级导出部分用例：
    
    
    casebook export releases/example --tag smoke
    casebook export releases/example --priority P0
    

### 5\. 创建测试计划并执行用例

![test-plan](https://img2024.cnblogs.com/blog/311516/202606/311516-20260629113537430-462865784.png)

测试计划默认折叠，不影响用例评审。进入执行阶段后，可以展开顶部测试计划面板：

  * 创建或选择测试计划。
  * 为每条用例选择 `Passed`、`Failed` 或 `Blocked`。
  * 记录执行备注和 JIRA 缺陷链接。
  * 查看执行进度条和统计数据。
  * 点击 `Complete plan` 完成测试计划，并写入测试环境和测试人员。



执行数据会保存到：
    
    
    test-runs/<run-id>.json
    

这些数据不会写入 YAML 用例文件，而是作为后续生成测试报告的依据。

### 6\. 生成 HTML 测试报告

执行完成后，使用测试计划 JSON 生成报告：
    
    
    casebook report test-runs/run-20260625093000-login-smoke.json --output reports/login-smoke.html
    

将命令中的 run 文件名替换成你本地 `test-runs/` 目录下实际生成的文件。

![Casebook HTML 测试报告](./images/test-report.png)

报告包含：

  * 测试计划基本信息。
  * 执行概览和通过率统计。
  * ECharts 图表。
  * 失败用例列表，包含执行备注和缺陷链接。
  * 阻塞用例列表，包含执行备注和缺陷链接。



到这里，一个从需求、AI 生成用例、本地评审、用例执行到 HTML 测试报告的 Casebook 闭环就完成了。

## 使用 AI Agent 生成用例

Casebook 的推荐方式不是在页面里点击“生成用例”，而是在项目工程里让 AI Agent 直接读取需求、技能包、schema 和已有 YAML 文件，然后写入 `releases/` 目录。

这样做有几个好处：

  * AI 能同时理解需求、历史用例和项目规范。
  * 用例变更可以被 Git 追踪、审查和回滚。
  * 新增、删除、拆分、合并、重构用例可以一次性完成，不需要人在页面里逐条维护。
  * `schema/test-case-schema.json` 可以约束 AI 输出，减少格式漂移。



### AI 需要读取哪些文件

每次让 AI Agent 生成或维护用例时，建议明确让它读取这些文件：

文件 | 作用  
---|---  
`AGENTS.md` | 告诉 AI 当前项目如何工作，以及应该引用哪个技能包  
`.agents/skills/casebook-test-cases/SKILL.md` | 告诉 AI 如何理解需求、设计用例、写得像测试人员  
`schema/test-case-schema.json` | 约束 YAML 用例结构，确保输出可被 Casebook 读取  
`docs/requirements/` | 需求、接口、业务规则和验收标准  
`releases/` | 已有 YAML 用例，也是 AI 写入和维护的目标目录  
  
### 生成用例

新需求第一次生成用例时，可以直接把下面这段提示词给 AI Agent：
    
    
    请阅读以下文件：
    - AGENTS.md
    - .agents/skills/casebook-test-cases/SKILL.md
    - schema/test-case-schema.json
    - docs/requirements/login.md
    
    请根据需求生成 YAML 测试用例，写入：
    releases/v1-auth/login.yaml
    
    要求：
    - 严格符合 schema/test-case-schema.json。
    - 用例要覆盖正常场景、异常场景、边界条件、权限/状态相关场景。
    - 优先级使用 P0/P1/P2。
    - 用例标题要像测试人员写的，不要像需求标题。
    - 步骤和预期结果要具体，可执行、可评审。
    - 如果需求信息不足，请在生成前指出缺失信息，并基于合理假设继续生成。
    

![AI-generated](https://img2024.cnblogs.com/blog/311516/202606/311516-20260629113637074-1184863943.png)

生成完成后，启动当前需求目录进行评审：
    
    
    casebook serve releases/v1-auth
    

### 生成后的检查清单

AI Agent 完成修改后，建议做一次检查：

  * YAML 文件是否在 `releases/<需求或版本目录>/` 下。
  * 是否符合 `schema/test-case-schema.json`。
  * 是否覆盖正常场景、异常场景、边界条件和关键业务规则。
  * 用例标题是否清晰，步骤是否可执行，预期结果是否可验证。
  * 是否存在重复用例、空泛用例或与需求无关的用例。
  * 是否可以通过 `casebook serve <目录>` 在本地工作台正常浏览。



Casebook 的核心思路是：AI Agent 负责生成和维护 YAML，人负责评审、判断和执行。这样测试用例不再是散落在平台里的表格，而是可被 AI 理解、可被 schema 校验、可被 Git 管理的工程资产。

## 用例 ID 重排

用例评审阶段经常会删除、插入或调整用例。Casebook 推荐保持 YAML 中的用例顺序不变，只按当前文件顺序重新整理用例 ID。

重排范围是当前 YAML 文件，不会跨文件处理。重排规则是以第一条用例 ID 为起点，例如第一条是 `TC_LOGIN_018`，后续用例会依次变成 `TC_LOGIN_019`、`TC_LOGIN_020`。

命令行重排：
    
    
    casebook renumber releases/example/login.yaml
    

本地工作台重排：

  * 打开某个 YAML 文件。
  * 确认当前没有选择测试计划。
  * 点击用例列表上方的 `ID 更新`。



测试计划模式下不支持 ID 重排。测试计划的执行结果以 `文件路径#用例ID` 记录，重排会导致执行结果和用例错位，因此页面会在选择测试计划后禁用 `ID 更新`。

重排时，当前文件里的 Mark 标记会按旧 ID 到新 ID 自动迁移，避免评审标记丢失。

## 静态 HTML 用例导出

`casebook serve` 适合本机评审和执行，但会议室电脑、开发冒烟用例交付、离线分享等场景更适合直接打开一个静态 HTML 文件。

导出整个需求或版本目录：
    
    
    casebook export releases/v1-auth
    

目录会默认聚合为一个 HTML 文件，命名规则类似：
    
    
    releases/v1-auth -> casebook-v1-auth.html
    

导出单个 YAML 文件：
    
    
    casebook export releases/v1-auth/login.yaml
    

单个 YAML 默认输出同名 HTML：
    
    
    releases/v1-auth/login.yaml -> releases/v1-auth/login.html
    

指定输出位置：
    
    
    casebook export releases/v1-auth --output login-review.html
    

按标签或优先级导出部分用例：
    
    
    casebook export releases/v1-auth --tag smoke
    casebook export releases/v1-auth --priority P0
    casebook export releases/v1-auth --tag smoke --priority P0
    

`--tag` 和 `--priority` 都可以重复传入，也支持逗号分隔：
    
    
    casebook export releases/v1-auth --tag smoke --tag api
    casebook export releases/v1-auth --priority P0,P1
    

导出的 HTML 是偏评审视图的只读用例包，包含：

  * 文件元信息、用例数量和优先级统计。
  * 用例 ID、标题、描述、优先级、类型和标签。
  * 前置条件、步骤和预期结果。
  * 页面内搜索、优先级筛选、标签筛选、展开/收起。
  * 每条用例的 `Needs update` 标记和评审备注。



导出的 HTML 不读取项目中的 `.casebook/marks.json`，因此不会把本地工作台的 Mark 状态带出去。HTML 中的评审标记和备注保存在浏览器 localStorage 中，适合会议室电脑临时评审；评审结束后可以点击 `Export review notes` 下载 JSON，把备注带回项目继续处理。

## 测试计划与用例执行

Casebook 将执行数据保存在独立文件中，不写入 YAML 用例定义。
    
    
    test-runs/<run-id>.json
    

测试计划不是必选项。用例评审时可以完全不启用测试计划；需要进入执行阶段时，再展开顶部测试计划面板并创建或选择计划。

测试计划绑定当前 `casebook serve <目录>` 的启动目录。比如：
    
    
    casebook serve releases/v1-auth
    

此时创建的测试计划只属于 `releases/v1-auth`，不会混入其他需求目录的计划。

每个测试计划会记录名称、范围、开始时间、完成时间和每条用例的执行结果。执行过程中，最近一次执行、备注或缺陷链接更新时间会写入 `completed_at`；完成计划时，测试环境默认是 `Test environment`，测试人员默认来自当前启动范围内 YAML 文件的 `owner`，多个 owner 使用逗号分隔。

用例结果以 `文件路径#用例ID` 作为 key：
    
    
    {
      "run": {
        "id": "run-20260625093000-login-smoke",
        "name": "Login smoke test",
        "status": "completed",
        "scope": ["releases/v1-auth"],
        "environment": "Test environment",
        "tester": "qa",
        "started_at": "2026-06-25T01:30:00+00:00",
        "completed_at": "2026-06-25T02:30:00+00:00"
      },
      "results": {
        "releases/v1-auth/login.yaml#TC_LOGIN_001": {
          "status": "passed",
          "notes": "Passed",
          "defects": [],
          "executed_at": "2026-06-25T01:35:00+00:00"
        }
      }
    }
    

支持的执行状态：
    
    
    passed, failed, blocked
    

未出现在 `results` 中的用例视为未执行。

## 项目状态文件

Casebook 的标记数据保存在项目根目录：
    
    
    .casebook/marks.json
    

示例：
    
    
    {
      "releases/example/login.yaml#TC_LOGIN_001": {
        "needs_update": true,
        "updated_at": "2026-06-24T02:00:00+00:00"
      }
    }
    

这些状态不写入 YAML 用例文件，因此不会影响用例正文和 schema 校验。

执行数据保存在：
    
    
    test-runs/*.json
    

这些文件是后续生成测试报告的重要数据来源。测试计划按启动目录隔离，适合围绕单个需求、版本或模块做执行统计。

## HTML 测试报告

执行完成后，可以从测试计划 JSON 生成 HTML 报告：
    
    
    casebook report test-runs/run-20260625093000-login-smoke.json
    

默认会在同目录生成同名 `.html` 文件：
    
    
    test-runs/run-20260625093000-login-smoke.html
    

也可以指定输出位置：
    
    
    casebook report test-runs/run-20260625093000-login-smoke.json --output reports/login-smoke.html
    

报告内容包括：

  * 测试计划基本信息：ID、名称、状态、范围、测试环境、测试人员、开始时间和完成时间。
  * 执行概览：用例总数、已执行、已通过、失败、阻塞、待测试。
  * ECharts 环形图：执行状态分布、失败/阻塞优先级分布。
  * 失败用例列表，包含执行备注和缺陷链接。
  * 阻塞用例列表，包含执行备注和缺陷链接。



报告 HTML 通过 CDN 引入 ECharts 渲染图表；即使图表脚本未加载，报告中的概览数字和用例列表仍然可以直接查看。


---
> 原文链接: https://www.cnblogs.com/fnng/p/20914242