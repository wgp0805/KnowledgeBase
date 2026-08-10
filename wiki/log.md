## [2026-08-05] ingest | 摄入「面试经典：高并发短链接系统设计」
- **变更**: 新增 source [[摘要-高并发短链接系统设计]]; 新增 concepts [[短链接系统]], [[分布式发号器]], [[Base62编码]], [[布隆过滤器]], [[哈希碰撞]], [[HTTP重定向]], [[缓存雪崩]]; 新增 entities [[Caffeine]], [[Leaf]]; 增量更新 [[雪花算法]]（补充发号器场景与 Leaf 关联）、[[sharding]]（补充短链分库分表场景关联）; 更新 [[index.md]]（1 source + 7 concepts + 2 entities）
- **冲突**: 无
- **归档**: raw/01-articles/面试经典：如何设计高并发短链接系统.md -> raw/09-archive/

## [2026-08-05] ingest | 摄入「携程二面：什么是熔断」面试文章
- **变更**: 新增 source [[摘要-携程二面-熔断]]; 新增 concepts [[熔断]], [[雪崩效应]], [[限流]], [[降级]]; 新增 entities [[Hystrix]], [[Resilience4j]]; 增量更新 [[Sentinel]]（补充熔断三态、关键参数、与 Hystrix 差异）; 更新 [[index.md]]（1 source + 4 concepts + 2 entities）
- **冲突**: 无

## [2026-08-06] ingest | 摄入 DeepSeek Harness 内测与 Agent 工程化面试题深度解析
- **变更**: 新增 source [[摘要-deepseek-harness内测]]; 新增 concepts [[Harness]]（Model + Harness = Agent 核心概念）, [[混合检索]]（KNN + BM25 混合检索技术）; 增量更新 [[DeepSeekHarness]]（覆盖旧定义，重新定义为用户端 Agent 产品，评测框架降级为次要用途）, [[PaiCLI]]（补充 Agent 完整流程/审批机制/工具 Schema 约束/容错等）, [[ReAct_Agent]]（补充完整 ReAct 流程 5 步骤与局限性）, [[context-compression]]（补充 200K 窗口触发阈值公式与三步压缩流程）, [[DeepSeek]]（补充 DSH 内测信息）, [[沉默王二]]（补充新来源）; 更新 [[index.md]]（1 source + 2 concepts + 6 updates）
- **冲突**: [[DeepSeekHarness]] 定义冲突（评测框架 vs 用户端 Agent 产品），用户选择 B) 用新知识覆盖，已更新定义并标注处理记录
- **归档**: raw/01-articles/DeepSeek员工：Harness开始内测...md → raw/09-archive/
- **变更**: 新增 source [[摘要-多Agent协作开发框架]]; 新增 concepts [[role-isolation]], [[adversarial-review]]; 增量更新 [[multi-agent-collaboration]]（新增模式 B：Planner/Coder/Reviewer 三角色框架 + 文件交接 + 防包容机制，与既有 Skill 驱动分工模式并列）; 更新 [[index.md]]（1 source + 2 concepts + 1 update）
- **冲突**: 无（新内容与既有页面互补，无冲突）
- **归档**: raw/01-articles/multi-agent-collaboration.md -> raw/09-archive/
- **输出**: 引用 [[oh-my-vs-kick-开源项目命名差异]]; 知识库已有直接对应的 synthesis 页面，直接引用回答（全家桶配置 vs 极简起步模板）；即时回答未保存

## [2026-08-06] query | oh-my-* 项目与 kickstart.* 项目的区别
- **输出**: 引用 [[oh-my-vs-kick-开源项目命名差异]]; 用户反馈原总结不完整，经 exa 联网搜索（oh-my-zsh 命名起源/Robby Russell 访谈、oh-my-posh 历史、oh-my-bash/oh-my-fish/oh-my-tmux 家族、kickstart.nvim 官方定位、kickstart vs LazyVim/NvChad distribution 对比）后，重写 synthesis 页面：新增命名起源章节、家族成员图谱、"反 distribution"路线、distribution 生态对照表；新增实体 [[RobbyRussell]]（oh-my-zsh 创建者/curator）；更新 [[index.md]]（1 entity + 1 synthesis 描述）
- **冲突**: 无

## [2026-08-05] query | 推荐 pi 工作开发的扩展安装清单
- **输出**: 引用 [[pi-扩展生态与开发指南]], [[PiAgent]], [[MCP]]; 按三档给出推荐（必装安全类/工作流类/按需类）；已补充进 [[pi-扩展生态与开发指南]] 新增"六、工作开发推荐安装清单"章节
- **冲突**: 无

## [2026-08-05] query | Pi 现成扩展查找渠道与扩展开发规范
- **输出**: 引用 [[PiAgent]], [[Skill]], [[Agent]], [[MCP]], [[OpenCode]]; 知识库无扩展生态内容，经 web 综合（官方 docs/extensions.md、examples 目录、pi.dev、npm registry）；已固化为 [[pi-扩展生态与开发指南]]（更新 index.md）
- **冲突**: 无

## [2026-08-05] query | 解释"个人高手/要掌控一切/省钱/多模型适合 Pi"的画像含义
- **输出**: 引用 [[PiAgent]], [[OpenCode]], [[ClaudeCode]]; 展开四特质含义（原语组合哲学/控制权/零订阅+低token/多模型按任务分配），并给出反例画像（开箱即用党不适合）; 即时回答未保存

## [2026-08-05] query | 确认 pi 是否适合非高手用于工作开发（选型确认）
- **输出**: 引用 [[PiAgent]], [[OpenCode]], [[ClaudeCode]], [[Codex]]; 确认"求稳用成熟工具"成立，并补充 pi 是"毛坯房非危房"、OpenCode 为务实折中选择；即时回答未保存

## [2026-08-05] query | pi-agent 对 Node.js 的最低版本要求
- **输出**: 引用 [[PiAgent]]; 知识库无版本要求记录，降级声明后经 web 验证（earendil-works/pi changelog + npm EBADENGINE + Pi Agent Platform 发布文档）——最低 Node.js >= 22.19.0; 即时回答未保存

## [2026-08-05] query | 验证 cc-switch / Codex++ 对 Codex 桌面版多模型与插件支持的说法
- **输出**: 引用 [[Codex]]; 知识库无 cc-switch/Codex++/插件市场 专门页面，经 web 验证（cc-switch issue #3340/#3605、openai/codex issue #21959/#16903、CodexPlusPlus GitHub、Codex 官方插件文档）；已固化为 [[codex-desktop-多模型与插件支持现状]]（更新 index.md）
- **冲突**: 无

## [2026-08-05] ingest | 摄入「面试官皱眉：superpowers 和 grill-me 怎么选」苏三文章
- **变更**: 新增 source [[摘要-superpowers-grill-me怎么选]]; 新增 entity [[GrillMe]]（编码前需求澄清 skill，追问设计分支至共识）; 增量更新 [[superpowers]]（补充"与 grill-me 的配合"章节、组合工作流、关联连接）、[[MattPocock]]（补充新来源与 GrillMe 关联）、[[苏三]]（补充新来源与提炼实体）; 更新 [[index.md]]（1 source + 1 entity）
- **冲突**: [[GrillMe]] 与 [[MattPocock]] 记载的"作者已撤下 /grill-me 从默认推荐位"表述并存——前者讲作者对自家 skill 编排的调整，后者讲 grill-me 相对 superpowers 的定位差异，已在 [[GrillMe#知识冲突]] 区块标注，非覆盖性冲突
- **归档**: raw/01-articles/面试官皱眉：你懂 Vibe Coding，那你说superpowers和grill-me怎么选？，我：小孩才做选择，我全都要！.md → raw/09-archive/

## [2026-08-04] ingest | 批量摄入 5 篇已处理文章（补充索引同步）
- **变更**: 补充注册 6 个已存在但未同步索引的摘要到 [[index.md]]：[[摘要-通用万能Prompt模板]], [[摘要-提示词三大原则-定角色明任务给素材]], [[摘要-java-boolean-is-naming-pitfall]], [[摘要-java-boolean-is-serialization-pitfall]], [[摘要-pi-agent-core-principles]], [[摘要-pi-agent-production-guide]]
- **冲突**: 无（所有摘要、实体、概念页面此前已创建，本次仅同步索引）
- **归档**: raw/01-articles/ 下 5 个文件 → raw/09-archive/

## [2026-08-04] query | mvnd 完全讲解教程
- **输出**: 已保存至 [[mvnd-complete-guide]]（web 搜索 + 综合整理）
- **冲突**: 无（知识库此前无 mvnd 相关内容）

## [2026-08-04] ingest | 摄入 Sa-Token 权限认证框架深度解析文章
- **变更**: 新增摘要 [[摘要-为什么越来越多人用Sa-Token]]; 新增实体 [[Sa-Token]]; 新增概念 [[权限认证框架]], [[分布式会话]], [[核心-插件-适配器模型]]; 增量更新 [[SpringSecurity]]（补充与 Sa-Token 对比表）; 增量更新 [[sa-token-vs-jwt-spring-security]]（补充来源）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/为什么越来越多人用Sa-Token？.md → raw/09-archive/

## [2026-08-03] ingest | 摄入 LangChain4j 入门指南（苏三）
- **变更**: 新增摘要 [[摘要-LangChain4j入门指南-苏三]]; 增量更新 [[LangChain4j]]（补充 ChatMessage 五种类型、优缺点总结、与 Spring AI 对比表、生产避坑指南6条）; 增量更新 [[ChatMemory]]（补充"记忆 vs 历史记录"关键区分）; 增量更新 [[AIService]]（补充支持的能力列表：静态/动态系统消息/共享记忆/多用户记忆/RAG检索增强）; 增量更新 [[RAG]]（补充进阶版 RAG 流水线化特性）; 更新 [[index.md]]
- **冲突**: 无（LangChain4j 版本 1.15.1 为过时快照，已有统一版本 1.17.2，未产生冲突）
- **归档**: raw/01-articles/LangChain4j 入门指南.md → raw/09-archive/

## [2026-08-03] ingest | 批量摄入 5 篇新文章（book-to-skill / DeepSeek V4-Flash / Embabel / OKF / MCP 第五版）
- **变更**: 新增摘要 [[摘要-book-to-skill]], [[摘要-deepseek-v4-flash发布]], [[摘要-embabel]], [[摘要-okf]], [[摘要-mcp-v5-openclaw-net]]; 新增实体 [[BookToSkill]], [[DeepSeekHarness]], [[崔添翼]], [[Embabel]], [[RodJohnson]], [[OKF]], [[OpenWiki]], [[OpenClawNET]]; 新增概念 [[DiscoveryLoopTax]], [[后训练]], [[GOAP]], [[UtilityAI]], [[LLMWiki]], [[MRTR]]; 增量更新 [[DeepSeek]]（补充 V4-Flash 正式版/后训练案例）, [[SpringAI]]（补充与 Embabel 分层关系）, [[MCP]]（补充第五版无状态化/MRTR/扩展）, [[OpenClaw]]（补充 OpenClaw.NET 关联）, [[程序员追风]]（补充 book-to-skill 来源）; 更新 [[index.md]]
- **冲突**: 无（注意到 4 个 raw 文件内容完全重复为同一篇 book-to-skill 文章，合并为单一摘要）
- **归档**: raw/01-articles 下 8 个文件 → raw/09-archive/

## [2026-07-31] ingest | 摄入 Spring Boot JSON 安全性排行文章
- **变更**: 新增 [[摘要-spring-boot-json-security]]; 新增实体 [[Gson]], [[FastJson2]], [[JSON-B]]; 新增概念 [[AutoType]], [[SafeMode]], [[多态反序列化]]; 增量更新 [[Jackson]]（补充 Jackson 3/2026 CVE）, [[FastJson]]（补充 FastJson2 分代/多轮 CVE）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/Spring Boot 中使用 JSON：安全性排行推荐.md → raw/09-archive/

## [2026-07-31] ingest | 摄入 Spring Boot 4 模块化架构文章
- **变更**: 新增 [[摘要-springboot4-模块化架构]]; 增量更新 [[SpringBoot]]（补充"SpringBoot 4 模块化架构"章节：模块拆分、测试 Starter 模块化、迁移指南、Classic Starters 过渡方案）; 更新 [[index.md]]
- **冲突**: 无（本文模块化架构与已有 Undertow 移除/4.1.0 特性为互补视角）
- **归档**: raw/01-articles/SpringBoot4 新特性：模块化架构.md → raw/09-archive/

## [2026-07-29] ingest | 摄入 Spring Boot 4.0 弃用 Undertow 文章
- **变更**: 新增 [[摘要-spring-boot-4-0-removes-undertow]]; 新增实体 [[Undertow]], [[Jetty]], [[RedHat]], [[JakartaEE]]; 新增概念 [[servlet-6-1]]; 增量更新 [[SpringBoot]]（补充 Spring Boot 4.0 Servlet 6.1 强制依赖与 Undertow 移除）、[[Servlet]]（补充 Servlet 6.1 章节）、[[Tomcat]]（补充 Tomcat 11 Servlet 6.1 支持）；更新 [[index.md]]
- **冲突**: 无

## [2026-07-29] lint | 修正 OpenSpec synthesis 页面中 explore 自动比对的错误表述
- **变更**: 更新 [[openspec-archive-modify-and-token-tradeoff]]（"explore 阶段先做差异核对"->"手动要求差异核对"，明确 explore 是纯对话工具不会自动扫描代码；修正实践建议中"必做 explore 差异核对"->"主动要求 AI 做差异核对"）
- **冲突**: 无（纠正本会话之前的表述不精确）

## [2026-07-29] query | 澄清 explore 命令不会自动比对代码与 spec
- **输出**: 引用 [[OpenSpec]]; 即时回答未保存（等待用户确认是否修正已有 synthesis）

## [2026-07-29] synthesis | 更新 OpenSpec 权衡分析，补充 spec rot 风险与补录机制
- **变更**: 更新 [[openspec-archive-modify-and-token-tradeoff]]（新增"三、跳过流程的代价：未记录小改动与 spec rot"章节，补全"小活儿别用"结论的边界条件）；补充 tags 增加 SpecRot
- **引用**: [[OpenSpec]], [[delta-spec]], [[openspec-brownfield-usage-guide]], [[摘要-spec-superflow-融合工作流]], [[SpecSuperflow]]
- **冲突**: 无

## [2026-07-29] query | 解析 OpenSpec 未记录小改动的 spec rot 风险与补录机制
- **输出**: 引用 [[OpenSpec]], [[delta-spec]], [[openspec-brownfield-usage-guide]], [[摘要-spec-superflow-融合工作流]], [[SpecSuperflow]]; 即时回答未保存（等待用户确认是否更新已有 synthesis）

## [2026-07-29] synthesis | 固化 OpenSpec 归档修改流程与 Token 成本权衡分析
- **变更**: 新增 [[openspec-archive-modify-and-token-tradeoff]]；更新 [[index.md]] Syntheses 分类；更新 [[openspec-brownfield-usage-guide]]（补充反向关联链接）
- **引用**: [[OpenSpec]], [[delta-spec]], [[规范驱动开发]], [[摘要-claude-code-best-practice-苏三视角]], [[ContextEngineering]], [[VibeCoding]], [[SpecSuperflow]], [[摘要-OpenSpec规范驱动AI编程框架]], [[摘要-spec-superflow-融合工作流]]
- **冲突**: 无

## [2026-07-29] query | 解析 OpenSpec 已归档需求的修改流程及 token 消耗权衡分析
- **输出**: 引用 [[OpenSpec]], [[delta-spec]], [[摘要-OpenSpec规范驱动AI编程框架]], [[摘要-spec-superflow-融合工作流]], [[规范驱动开发]], [[摘要-claude-code-best-practice-苏三视角]], [[ContextEngineering]], [[VibeCoding]], [[SpecSuperflow]]; 即时回答未保存（等待用户确认是否固化为 synthesis）

## [2026-07-24] ingest | 摄入 Maven 4 重构文章与生产级 Agent 设计面试文章
- **变更**: 更新 [[摘要-maven-4-重构]]（补充 Artifact 类型、Tree-based Lifecycle、条件表达式等）；更新 [[Maven]]（补充核心架构调整细节）；新增 [[摘要-生产级Agent设计]]；更新 [[PaiCLI]]（补充三种运行模式、记忆系统、上下文压缩等）；更新 [[context-compression]]（补充 Map-Reduce 分片摘要）；更新 [[渐进式披露]]（补充三阶段实现）；更新 [[沉默王二]]（补充来源）；新增 [[指数退避重试]]；新增 [[记忆系统-时间衰减加权]]；新增 [[智能客服Agent设计]]；新增 [[电商流量尖峰处理]]；更新 [[index.md]]
- **冲突**: 无

## [2026-07-27] ingest | 批量摄入 4 篇技术文章（SkyWalking Agent/Druid 优化/OnlyOffice 集成/AI Agent 项目推荐）
- **变更**: 新增 [[摘要-skywalking-java-agent-使用]]、[[摘要-druid-连接池极致优化]]、[[摘要-springboot-onlyoffice-在线编辑]]、[[摘要-推荐5个AI-Agent项目]]；新增 [[Halo]]、[[OnlyOffice]]、[[Apdex]]；更新 [[SkyWalking]]（补充 Java Agent 配置与 Web 界面功能）；更新 [[Druid]]（补充参数调优/监控/安全/泄漏检测）；更新 [[在线文档处理]]（补充 OnlyOffice 方案）；更新 [[index.md]]
- **冲突**: 无

## [2026-07-27] lint | 自动修复死链和未同步索引
- **变更**: 修复 `[[marka.md]]`→`[[marka]]`（3 处概念页面 + index.md）；修复大小写 `[[Claude-code-best-practice]]`→`[[claude-code-best-practice]]`、`[[LM Studio]]`→`[[LM_Studio]]`、`[[Context Tray]]`→`[[ContextTray]]`；注册 13 个未同步索引文件到 [[index.md]]（Entities: ArchitectureDiagramGenerator, CocoonAI, JetBrainsMono, RadixUI, React, TailwindCSS; Concepts: AI终端, Checkpoint, Protobuf, ToolCalling, auto-mode, gRPC, 知识图谱）
- **冲突**: 无
- **变更**: 新增 [[摘要-skywalking-java-agent-使用]]、[[摘要-druid-连接池极致优化]]、[[摘要-springboot-onlyoffice-在线编辑]]、[[摘要-推荐5个AI-Agent项目]]；新增 [[Halo]]、[[OnlyOffice]]、[[Apdex]]；更新 [[SkyWalking]]（补充 Java Agent 配置与 Web 界面功能）；更新 [[Druid]]（补充参数调优/监控/安全/泄漏检测）；更新 [[在线文档处理]]（补充 OnlyOffice 方案）；更新 [[index.md]]
- **冲突**: 无

## [2026-07-23] synthesis | 固化 Agent 与 RAG 通信方式对比
- **变更**: 新增 [[agent-rag-communication-comparison]]；更新 [[index.md]] Syntheses 分类
- **引用**: [[MCP]], [[FunctionCalling]], [[RAG]], [[Agent]], [[Skill]], [[知识库-skill-solutions]], [[摘要-RAG-KAG双引擎知识库系统]], [[摘要-rag-api-call]], [[摘要-codegraph-mcp-gateway]], [[LangChain4j]], [[SpringAI]]
- **冲突**: 无

## [2026-07-23] query | Agent 与 RAG 通信方式对比
- **输出**: 引用 [[MCP]], [[FunctionCalling]], [[知识库-skill-solutions]], [[RAG]], [[Agent]], [[摘要-RAG-KAG双引擎知识库系统]], [[摘要-rag-api-call]], [[摘要-codegraph-mcp-gateway]]; 即时回答未保存（待用户确认是否固化为 synthesis）
- **结论**: 通信方式不止 MCP，至少四种——Function Calling/@Tool（进程内）、MCP（标准化跨进程）、HTTP API（独立服务）、Skill（轻量文件检索）

## [2026-07-23] query | 解释 RAG 概念
- **输出**: 引用 [[RAG]], [[摘要-为什么Claude-Code不用RAG检索代码]], [[AgenticSearch]]; 即时回答未保存
- **引用**: [[RAG]], [[AgenticSearch]], [[AgenticRAG]], [[GraphRAG]], [[ContextEngineering]]

## [2026-07-23] query | 对比 Trae 智能体与 Claude Code 智能体功能
- **输出**: 即时回答未保存
- **引用**: [[ClaudeCode]], [[动态工作流]], [[Command-Agent-Skill编排]], [[子Agent编排]], [[Skill]]

## [2026-07-23] synthesis | 保存 Trae vs Claude Code 智能体对比
- **变更**: 新增 [[trae-vs-claude-code-agent-comparison]]；更新 [[index.md]]
- **冲突**: 无

## [2026-07-23] query | 知识库优先检索的 Skill 实现方案
- **输出**: 即时回答未保存
- **引用**: [[Skill]], [[CLAUDEmd]], [[AutoMemory]], [[RAG]], [[Hooks]]

## [2026-07-23] synthesis | 保存知识库优先检索方案
- **变更**: 新增 [[knowledge-base-skill-solutions]]；更新 [[index.md]]
- **冲突**: 无
- **变更**:
  - 新增 source [[摘要-git-撤回已push代码]]（小哈学Java，Git 撤回已 push 代码的四种方法对比）
  - 增量更新 entity [[Git]]（补充"撤回已 Push 代码的四种方法"章节：手动恢复/git revert/新建分支/git reset+force push，含四种 reset 模式 Soft/Mixed/Hard/Keep 对比表）
  - 更新 [[index.md]] 加入 1 个新 source 条目
- **冲突**: 无
- **归档**: raw/01-articles/面试官：Git 如何撤回已 Push 的代码？问倒一大片。。。.md -> raw/09-archive/

## [2026-07-08] ingest | 摄入 Gateway 网关、Agent/Tools/Workflow 区别、无人图书柜 3 篇文章
- **变更**:
  - 新增 sources: [[摘要-gateway网关]], [[摘要-agent-tools-workflow区别]], [[摘要-无人图书柜项目]]
  - 新增 entities: [[Zuul]], [[程序汪]], [[UniApp]]
  - 新增 concepts: [[网关]], [[AI工作流]], [[MQTT协议]]
  - 增量更新 entity [[SpringCloudGateway]]（补充网关五大核心作用、Route/Predicate/Filter 三核心概念、Gateway vs Zuul 对比、自定义鉴权过滤器）
  - 增量更新 concept [[Agent]]（补充 Tools/Workflow/Agent 层级递进关系与 Anthropic "简单胜于复杂"选型原则）
  - 增量更新 concept [[FunctionCalling]]（补充 Tools 概念：离散函数、description 字段决定工具选择）
  - 更新 [[index.md]] 加入 9 个新条目（3 source + 3 entity + 3 concept）
- **冲突**: 无（[[AI工作流]] 与已有 [[dynamic-workflow]] 为不同概念，已在页面中明确区分标注）

## [2026-07-08] ingest | 批量摄入 8 篇 raw/01-articles 技术资料 + 2 篇补归档
- **变更**:
  - 新增 sources: [[摘要-powerjob-分布式任务调度]], [[摘要-双亲委派模型]], [[摘要-aot-vs-jit编译]], [[摘要-springboot脚手架搭建]], [[摘要-springboot3.2-graalvm上手]], [[摘要-logback-vs-log4j2]], [[摘要-ponytail-ai减代码]], [[摘要-gsd-core-ai工作流]]
  - 新增 entities: [[PowerJob]], [[XXL-JOB]], [[Quartz]], [[GraalVM]], [[HotSpot]], [[MapStruct]], [[Golang]], [[Rust]], [[ActixWeb]], [[Logback]], [[Log4j2]], [[SLF4J]], [[Ponytail]], [[GSDCore]]
  - 新增 concepts: [[双亲委派模型]], [[类加载器]], [[SPI机制]], [[AOT编译]], [[JIT编译]], [[任务调度]], [[日志框架]], [[过度工程化]]
  - 更新 [[index.md]] 加入 30 个新条目（8 source + 14 entity + 8 concept）
- **冲突**: 无
- **归档**: raw/01-articles/ 11 个源文件至 raw/09-archive/；补归档 2 个已有 source 对应的文件

## [2026-07-08] ingest | 摄入 Transformer 与训练-微调范式科普文章
- **变更**:
  - 新增 source [[摘要-transformer-训练微调范式]]（博客园橙子家，Transformer 架构 + 训练-微调范式系统讲解）
  - 新增 entities: [[Transformer]], [[Google]], [[Sora]], [[AlphaFold2]], [[FigureAI]], [[Tesla]], [[LlamaFactory]]
  - 新增 concepts: [[自注意力机制]], [[QKV]], [[预训练]], [[基座模型]], [[SFT]], [[RLHF]], [[PEFT]], [[合成数据]], [[CNN]], [[RNN]]
  - 增量更新 entity [[LoRA]]（补充行业占比 95%+、参数占比 0.1%~1%、消费级显卡 RTX 4090 支持、成本骤降数据）
  - 增量更新 concept [[微调]]（补充微调三阶段分类体系 SFT→RLHF→PEFT、行业趋势、合成数据与端侧微调）
  - 更新 [[index.md]] 加入 18 个新条目（1 source + 7 entity + 10 concept）
- **冲突**: 无
- **归档**: raw/01-articles/2026-07-07-Transformer...md + raw/_daily_digest.md → raw/09-archive/

## [2026-07-07] query | 解析 CC + 国产模型组合的泄露风险
- **输出**: 引用 [[ClaudeCode]], [[AI中转站]], [[摘要-AI中转站盈利与风险分析]], [[摘要-AI-agent工具应该怎么使用]], [[摘要-沉默王二-claude-code-底层深扒]], [[摘要-codex-vs-claude-code-对比]], [[OpenCode]], [[Codex]], [[Ollama]], [[DeepSeek]], [[摘要-Ollama+DeepSeek本地部署]]; 即时回答未保存（待用户确认是否固化为 synthesis）
- **结论**: 风险分三层——CC 必然把上下文发给 Provider / 国产厂商收到全部上下文 / 中转站叠加明文泄露与模型偷换风险；CC 非开源不可审计，建议敏感场景用开源 Harness 或离线模型

## [2026-07-07] query | 解析 OpenCode vs ClaudeCode 能力差距、隐写术风险与 IDEA 迁移方案
- **输出**: 引用 [[OpenCode]], [[ClaudeCode]], [[摘要-codex-vs-claude-code-对比]], [[摘要-沉默王二-claude-code-底层深扒]], [[沉默王二]], [[摘要-claude-code-learning-roadmap]], [[摘要-ECC-OpenCode-使用指南]], [[ECC]], [[MiMoCode]], [[AI中转站]], [[摘要-AI-agent工具应该怎么使用]]; 即时回答未保存（待用户确认是否固化为 synthesis）
- **降级**: 知识库无"隐写术/水印"专门页面，仅 [[摘要-沉默王二-claude-code-底层深扒]] 记录"阿里 7 月 10 日全面禁用 Claude"事件未明原因；该部分已按降级策略声明并以通用知识补充

## [2026-07-07] query | 解析 Redis/MySQL 双写一致性问题
- **输出**: 引用 [[Redis]], [[MySQL]], [[transaction-management]], [[idempotency]], [[distributed-lock]], [[Redisson]], [[RocketMQ]], [[RabbitMQ]], [[摘要-rabbitmq-idempotency]]; 即时回答未保存（待用户确认是否固化为 synthesis）
- **降级**: 知识库无专门讨论"Redis/MySQL 双写一致性"的页面，已按降级策略声明并基于通用知识 + 本库相关概念综合回答

## [2026-07-07] lint | 死链修复 + 索引同步 + 知识冲突解决
- **变更**:
  - 修复 2 个死链：[[Obsidian]] 中 `[[wikilink]]` → `` `[[wikilink]]` ``；[[自生长知识库]] 中 `[[ingest]]` → `` `ingest` ``
  - 注册 synthesis [[sa-token-vs-jwt-spring-security]] 到 [[index.md]] Syntheses 分类（此前文件存在但未同步索引）
  - 联网查证 [[LangChain4j]] GitHub 最新 Release 为 1.17.2，将 `## 知识冲突` 区块升级为 `## 版本信息（已统一）`，确认旧知识 1.15.1（2026-05）和新资料 1.11.0（2026-02-04）均为不同时间点真实快照，非事实冲突，已统一为 1.17.2
- **冲突**: [[LangChain4j]] 版本冲突已解决（联网核实 GitHub Release 1.17.2）
- **关联**: 与同日 [[#修复 69 个孤儿页面的反向链接]] 合计完成本轮 lint 全部修复

## [2026-07-07] lint | 修复 69 个孤儿页面的反向链接
- **变更**:
  - 扫描 wiki/ 全目录，定位 69 个无入站链接的孤儿页面（59 source + 7 synthesis + 重复项）
  - 读取每个孤儿的 `## 关联连接`，按"优先 entity、其次 concept"规则选择 1 个目标，在目标页面的 `## 关联连接` 末尾追加 `- [[孤儿]] — 简短描述`
  - 修改 34 个 entity/concept 页面，共追加 67 条反向链接（含修正首次因数组取下标 bug 误截 chosen 首字符导致的 6 项漏处理）
  - 修正 58 条因描述提取正则 bug 而误写为"核心摘要"的描述，重新基于 `## 核心摘要` 首段或正文标题生成 10-20 字描述
  - 清理 36 个文件中相邻列表项间多余空行，保持列表格式一致
- **跳过**:
  - [[摘要-追番]]：关联连接区域为"无"，无任何技术 entity/concept 关联，无法匹配目标
- **冲突**: 无
- **结果**: 剩余孤儿页面从 69 降至 1（仅剩 [[摘要-追番]]，属个人记录无技术关联）

## [2026-07-07] ingest | 摄入 4 种消息队列选型对比文章
- **变更**:
  - 新增 source [[摘要-4种消息队列如何选型]]（Kafka/RabbitMQ/RocketMQ/ActiveMQ 全面对比）
  - 新增 entity [[ActiveMQ]]（Apache JMS 消息中间件，已边缘化）
  - 增量更新 entity [[Kafka]]（补充重要概念/分区策略/优缺点/选型建议）
  - 增量更新 entity [[RabbitMQ]]（补充 AMQP 模型/交换器类型/优缺点/选型建议）
  - 增量更新 entity [[RocketMQ]]（补充架构细节/优缺点/选型建议）
  - 增量更新 concept [[message-queue]]（补充两大模式：点对点/发布订阅，六大应用场景：解耦/异步/削锋/日志/通信/广播）
  - 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/4 种消息队列，如何选型？.md → raw/09-archive/

## [2026-07-07] ingest | 摄入 3 篇 raw/01-articles 技术资料 + 1 篇每日摘要归档
- **变更**:
  - 新增 sources: [[摘要-ai大模型学习路线]], [[摘要-maven-4-重构]], [[摘要-codex-97percent-技巧]]
  - 新增 entities: [[冰河]], [[小锋]], [[Coze]], [[Dify]]
  - 新增 concepts: [[提示词工程]], [[思维链]], [[幻觉]], [[微调]], [[Build POM 与 Consumer POM 分离]], [[计划模式]], [[Worktree]]
  - 增量更新 entities: [[Maven]]（补充 Maven 4 变化）, [[Codex]]（补充 10 条技巧）, [[苏三]]（补充新来源）
  - 增量更新 concept: [[CLAUDEmd]]（补充 AGENTS.md 四块关键内容写作方法）
  - 更新 [[index.md]]
  - 归档 raw/01-articles/ 3 个源文件 + raw/_daily_digest.md 至 raw/09-archive/
- **冲突**: 无

## [2026-07-07] query | 解析 Maven *.lastUpdated 文件用途
- **变更**: 新增 synthesis [[maven-lastUpdated-file]]；更新 [[index.md]] Syntheses 分类
- **输出**: 引用 [[摘要-maven]]，固化 synthesis 页面，包含失败缓存机制、副作用分析与清理脚本

## [2026-07-06] ingest | 摄入 LangGraph ReAct 循环手写实现文章
- **变更**: 新增 [[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]]; 新增实体 [[LangGraph]], [[LangChain]]; 新增概念 [[StateGraph]]; 增量更新 [[ReAct_Agent]]（补充实现结构：2节点+1条件边、add_messages reducer、双重安全阀、ToolMessage 失忆 Bug）; 更新 [[index.md]]
- **冲突**: 无（本文从 Python LangGraph 实现角度补充 ReAct 细节，与现有 Java 框架视角为互补）
- **归档**: raw/01-articles/构建你的第一个 Tool Agent：从零理解 ReAct 循环.md → raw/09-archive/

## [2026-06-30] ingest | 摄入 5 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-reader-filterreader-pushbackreader源码]], [[摘要-casebook-ai-native-testcase-workflow]], [[摘要-langchain4j-langgraph4j-comparison]], [[摘要-step-3-7-flash-agent横评]], [[摘要-claude-code-learning-roadmap]]
  - 新增 entities: [[Reader]], [[FilterReader]], [[PushbackReader]], [[Casebook]], [[LangGraph4j]], [[Step3Flash]], [[Qwen]]
  - 新增 concepts: [[AI原生测试用例工程化]], [[Agent工作流编排]]
  - 增量更新 entities: [[ClaudeCode]], [[LangChain4j]], [[DeepSeek]], [[Gemini]], [[Java]]
  - 增量更新 concepts: [[AICoding]], [[Agent]], [[Skill]], [[MCP]], [[RAG]], [[FunctionCalling]], [[multi-agent-collaboration]], [[装饰器模式]]
  - 更新 [[index.md]]
  - 归档 raw/01-articles/ 5 个源文件至 raw/09-archive/
- **冲突**: [[LangChain4j]] 最新版本信息存在差异（旧知识 1.15.1/2026-05，新资料 1.11.0/2026-02-04），已按用户选择保留两种说法并标注在“知识冲突”区块


- **变更**: 新增 source [[摘要-doubao-seed2-1-pro-douyin]]（秋芝2046 对豆包 Seed2.1 Pro 的办公 Agent、前端生成、视频转文字与多工具调用实测）；更新 [[index.md]] Sources 分类
- **冲突**: 无

## [2026-07-06] query | 讲解 ReAct 循环的概念与工作原理
- **输出**: 即时回答 + 已保存为 [[react-loop-explanation]]
- **引用**: [[ReAct_Agent]], [[ReActAgent]], [[Agent]], [[ToolPipeline]], [[HarnessAgent]], [[SpringAI_Alibaba]], [[SolonAI]], [[AgentScope_Java]]

## [2026-07-30] query | OpenSpec 在已有项目的安装步骤
- **输出**: 引用 [[OpenSpec]], [[openspec-brownfield-usage-guide]], [[openspec-archive-modify-and-token-tradeoff]], [[摘要-OpenSpec规范驱动AI编程框架]]; 即时回答未保存

## [2026-07-29] ingest | 摄入 AgentBro 多 Agent Skill 治理工具文章
- **变更**:
  - 新增 source [[摘要-agentbro-skill-management]]（程序员追风/石人闯的 AgentBro macOS 多 Agent Skill 治理工具详解）
  - 新增 entity [[AgentBro]]（macOS 多 Agent Skill 治理工具，中心库唯一事实源 + 技能包开关 + 扫描接管 + 远程管理）
  - 新增 entity [[AgentBroRemote]]（远程管理组件，SSH 隧道远程服务器 Agent 统一管理）
  - 新增 entity [[AgentBroMarket]]（内置技能市场，按创作者分组）
  - 新增 entity [[ShirenChuang]]（程序员追风，AgentBro 作者）
  - 新增 concept [[SkillCentralLibrary]]（中心库唯一事实源）
  - 新增 concept [[SkillPackage]]（技能包开关机制）
  - 新增 concept [[SkillSoftLink]]（软链接分发机制）
  - 新增 concept [[SkillScanTakeover]]（扫描接管存量机制）
  - 新增 concept [[SkillConflictResolution]]（同名冲突解决）
  - 新增 concept [[SkillTestPackage]]（测试包观察期）
  - 新增 concept [[AgentSpecificSkillPackages]]（Agent 维度技能包隔离）
  - 新增 concept [[RemoteAgentManagement]]（远程 Agent 管理）
  - 更新 [[index.md]]
- **冲突**: 无

## [2026-07-28] ingest | 摄入分库分表分页查询面试文章
- **变更**: 新增 [[摘要-分库分表分页查询]]; 新增实体 [[得物]], [[Canal]]; 新增概念 [[游标分页]], [[异构索引]], [[CQRS]]; 增量更新 [[小哈]]（补充新来源）; 增量更新 [[sharding]]（展开分页查询四大方案详解）; 更新 [[index.md]]
- **冲突**: 无

## [2026-07-28] ingest | 补充归档 Matt Pocock 文章
- **变更**: 源文件 `Matt Pocock...grill-me...这几个.md` 此前已完整编译为 [[摘要-mattpocock-skills]] 和 [[MattPocock]]，仅遗漏归档步骤，本次补齐
- **冲突**: 无
- **归档**: raw/01-articles/Matt Pocock... → raw/09-archive/

## [2026-07-06] query | 对比 ReAct 与 Plan-and-Execute 的区别
- **输出**: 即时回答 + 已保存为 [[react-vs-plan-execute]]
- **引用**: [[ReAct_Agent]], [[Research-Plan-Execute-Review-Ship]], [[Agent]], [[AICoding]], [[VibeEngineering]], [[claude-code-best-practice]]

# Wiki 操作日志

## [2026-08-05] query | 汇总 Pi Agent 完全教程
- **输出**: 引用 [[PiAgent]], [[摘要-pi-agent-core-principles]], [[摘要-pi-agent-production-guide]], [[pi-扩展生态与开发指南]], [[CLAUDEmd]], [[ContextEngineering]]; 知识库无完整教程，经 web 补充（官方 docs quickstart/usage）后综合成十八章节教程；已固化为 [[pi-agent-complete-guide]]（更新 index.md）
- **冲突**: 无

## [2026-06-29] ingest | 摄入双 Token 续签设计文章 + 补归档 Token-Redis 面试文
- **变更**:
  - 新增 source [[摘要-jwt-双token续签设计]]（胖虎《一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？》）
  - 新增 concept [[refresh-token-rotation]]（轮换 + Token Family 重放检测 + 前端 401 并发刷新坑 + 退出/改密/封禁场景）
  - 增量合并 [[dual-token-mechanism]]：补充"单 Token 根本矛盾"、"Refresh Token 不应做成 JWT 的可撤销登录态"、"存储位置建议"、"不适合双 Token 的场景"四节
  - 已存在的 [[摘要-token-redis-interview]] 对应源文件 `面试中被嘲笑Token放在Redis里？.md` 此次仅归档
  - 更新 [[index.md]] 加入 2 个新条目（1 source + 1 concept）
  - 归档 raw/01-articles/ 2 个文件至 raw/09-archive/
- **冲突**: 无（两篇文章为互补视角，token-redis-interview 偏"是什么/怎么做"，本次新文偏"为什么/工程边界"）

## [2026-06-29] ingest | 补归档 4 个已编译源文件
- **变更**: 将 raw/01-articles/ 下 4 个文件移入 raw/09-archive/，对应 sources [[摘要-codex-vs-claude-code-对比]]、[[摘要-fastapi-入门教程]]、[[摘要-国产大模型实战横评]]、[[摘要-二维码扫码登录原理]] 此前已创建并注册到 [[index.md]]，仅遗漏归档步骤本次补齐
- **冲突**: 无

## [2026-06-26] query | 解答 ECC 是什么、能干什么、怎么用
- **输出**: 即时回答未保存；引用 [[ECC]], [[摘要-ECC使用教程]]，对比 [[Superpowers]] / [[OpenSpec]] / [[SpecKit]] / [[规范驱动开发]]

## [2026-06-26] synthesis | 横向对比 4 套 Claude Code 增强框架
- **输出**: 新增 [[claude-code-增强框架对比]]（synthesis 页），覆盖 [[ECC]] / [[Superpowers]] / [[OpenSpec]] / [[SpecKit]] 的定位、关键差异、选型指南、组合实践；更新 [[index.md]] Syntheses 分类

## [2026-06-26] ingest | 摄入 Spring Boot 4.1 与 AI 编程治理三方对比
- **变更**:
  - 新增 sources: [[摘要-spring-boot-4.1-发布]], [[摘要-superpowers-openspec-speckit对比]], [[摘要-superpowers到底是什么]], [[摘要-程序员AI画图技巧]], [[摘要-claude-code-best-practice-苏三视角]]
  - 新增 entities: [[Superpowers]], [[SpecKit]], [[Mermaid]], [[PlantUML]], [[Graphviz]], [[draw-io]], [[ObsidianCanvas]], [[SVG]]
  - 新增 concepts: [[文本绘图]], [[规范驱动开发]]
  - 更新 [[SpringBoot]] 加入 4.1.0 章节；更新 [[OpenSpec]] 关联三方对比来源；更新 [[claude-code-best-practice]] 补充三条实战技巧与跨模型组合
  - 更新 [[index.md]]
  - 归档 raw/01-articles/ 全部 9 个待处理文件（含 4 个已处理的二次剪藏副本，以 `.duplicate-2026-06-25.md` 后缀保存）
- **冲突**: 无

## [2026-06-08] ingest | 摄入 MinIO 介绍与 2 篇 ES 深度文章
- **变更**: 新增 [[摘要-minio-intro]], [[摘要-elasticsearch-8.10-install]], [[摘要-elasticsearch-comprehensive-guide]]; 新增实体 [[MinIO]]; 新增概念 [[BM25]]; 更新 [[Elasticsearch]], [[analyzer]], [[inverted-index]], [[full-text-search]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-19] ingest | 批量摄入 raw/01-articles/ 全部 71 个文件到知识库
- **变更**: 新增 71 篇 source 摘要; 新增 24 个实体页面; 新增 6 个概念页面; 更新 [[index.md]]
- **冲突**: 无（知识库首次构建）

## [2026-05-19] query | MyBatis-Plus 是否需要 MySQL 驱动包
- **输出**: 引用 [[摘要-springboot整合mybatisPlus]], [[MyBatisPlus]], [[MySQL]]

## [2026-05-19] ingest | 摄入 Elasticsearch 入门教程
- **变更**: 新增 [[摘要-elasticsearch-quick-start]]; 新增实体 [[Elasticsearch]], [[Kibana]], [[Lucene]], [[Solr]]; 新增概念 [[inverted-index]], [[full-text-search]], [[analyzer]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-19] query | Solr vs ES 对比及技术选型
- **输出**: 引用 [[Solr]], [[Elasticsearch]], [[elasticsearch-disadvantages]]

## [2026-05-19] query | ES 使用缺点分析
- **输出**: 已保存至 [[elasticsearch-disadvantages]]

## [2026-05-19] ingest | 摄入 Spring Boot 集成 LangChain4j 教程
- **变更**: 新增 [[摘要-如何在Spring-Boot中无缝集成LangChain4j]]; 更新 [[LangChain4j]], [[AIService]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-19] ingest | 摄入 DeepSeek TUI 编程神器介绍
- **变更**: 新增 [[摘要-推荐deepseek-v4-编程神器]], [[DeepSeek]], [[DeepSeekTUI]]; 更新 [[Agent]], [[MCP]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 引入字节跳动百亿级消息队列设计解析
- **变更**: 新增 [[摘要-bytedance-mq-design]], [[Kafka]], [[RabbitMQ]], [[Pulsar]], [[BookKeeper]]; 新增概念 [[message-queue]], [[sequential-io]], [[tiered-storage]], [[consistent-hashing]], [[isr]]; 更新 [[RocketMQ]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入 skill-creator 使用与优化指南
- **变更**: 新增 [[摘要-skill-creator-guide]], [[SkillCreator]], [[meta-skill]]; 更新 [[ClaudeCode]], [[Skill]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入 Claude Code 不用 RAG 检索代码的分析文章
- **变更**: 新增 [[摘要-为什么Claude-Code不用RAG检索代码]], [[AgenticSearch]], [[Ripgrep]], [[Cursor]], [[BorisCherny]]; 更新 [[ClaudeCode]], [[RAG]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入 JWT+Redis 认证分析文章
- **变更**: 新增 [[摘要-token-redis-interview]], [[JWT]], [[jwt-stateless]], [[token-blacklist]], [[dual-token-mechanism]]; 更新 [[Redis]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入 SpringBoot 4 + Spring Security 7 + Vue3 前后端分离最佳实践
- **变更**: 新增 [[摘要-springboot4-security7-vue3-best-practice]], [[Vue3]], [[Pinia]], [[Axios]], [[ElementPlus]], [[frontend-backend-separation]], [[rbac]], [[cors]]; 更新 [[SpringBoot]], [[SpringSecurity]], [[Redis]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入高并发防重复下单文章
- **变更**: 新增 [[摘要-prevent-duplicate-order]], [[idempotency]], [[distributed-lock]]; 更新 [[Redis]], [[RocketMQ]], [[index.md]]
- **冲突**: 无

## [2026-05-20] ingest | 摄入 Java 泛型详解文章
- **变更**: 新增 [[摘要-java-generics-explained]], [[generics]]; 更新 [[Java]], [[index.md]]
- **冲突**: 无

## [2026-05-22] ingest | 摄入 Claude Code Spring Boot Skills 实战文章
- **变更**: 新增 [[摘要-claude-code-springboot-skills]]; 新增实体 [[dr-jskill]], [[agent-skill-java-spring-framework]], [[sivalabs-agent-skills]], [[spring-testing-skills]]; 新增概念 [[ai-agent-skill]]; 更新 [[ClaudeCode]], [[index.md]]
- **冲突**: 无

## [2026-05-22] query | 查询4个Spring Skill的使用时机
- **输出**: 引用 [[dr-jskill]], [[agent-skill-java-spring-framework]], [[sivalabs-agent-skills]], [[spring-testing-skills]], [[摘要-claude-code-springboot-skills]]

## [2026-05-22] ingest | 固化Spring Skill使用指南为synthesis
- **变更**: 新增 [[spring-skill-usage-guide]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-22] query | Spring AI vs LangChain4J 企业级选型对比
- **输出**: 引用 [[LangChain4j]], [[摘要-LangChain4j-Java-AI智能体开发]], [[sivalabs-agent-skills]], [[spring-testing-skills]]; 即时回答未保存

## [2026-05-22] ingest | 固化 Spring AI vs LangChain4J 对比为 synthesis
- **变更**: 新增 [[spring-ai-vs-langchain4j]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-22] ingest | 摄入 raw/01-articles/ 全部 5 篇技术资料
- **变更**: 新增 [[摘要-jenkins]], [[摘要-spring-ai]], [[摘要-spring-security]], [[摘要-maven]], [[摘要-java-ai-langchain4j]]; 新增实体 [[Jenkins]], [[GitLab]], [[Maven]], [[SpringAI]], [[Ollama]], [[Nexus]]; 新增概念 [[CI-CD]], [[ChatClient]]; 更新 [[SpringSecurity]], [[LangChain4j]], [[RAG]], [[FunctionCalling]], [[MCP]], [[index.md]]
- **冲突**: 无

## [2026-05-22] ingest | 批量摄入 raw/02-papers/ 全部 46 个 PDF 文件
- **变更**: 新增 10 篇 source 摘要（[[摘要-mysql-course]], [[摘要-alibaba-product-manual]], [[摘要-frontend-engineering]], [[摘要-microservice-governance]], [[摘要-cherry-studio-knowledge-base]], [[摘要-java-concurrency]], [[摘要-java-mycat]], [[摘要-java-performance-tuning]], [[摘要-spring-cloud-alibaba]], [[摘要-springboot3]]）; 新增实体 [[Mycat]], [[CherryStudio]]; 更新 [[MySQL]], [[SpringBoot]], [[jvm-tuning]], [[microservices]], [[frontend-backend-separation]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-22] lint | 知识库健康巡检与自动修复
- **变更**: 修复 28 处命名不一致断链（Claude Code→ClaudeCode 等 6 类）；修复 log.md 笔误（摘2要→摘要）；注册 30 个未同步文件到 index.md（4 Entities + 26 Concepts）；移动 [[message-queue]] 从 Entities 到 Concepts；移除 Entities 中重复的 [[AgenticSearch]]
- **冲突**: 无

## [2026-05-22] query | MySQL 存储引擎对比与底层架构
- **输出**: 引用 [[MySQL]], [[摘要-mysql-course]]; 知识库中无存储引擎的详细文本内容，基于通用知识回答

## [2026-05-25] ingest | 摄入 raw/01-articles/ 4篇技术文章
- **变更**: 新增 [[摘要-rabbitmq-idempotency]], [[摘要-springboot-startup-flow]], [[摘要-sharding-database-table]], [[摘要-singleton-pattern]]; 新增实体 [[ShardingSphere]]; 新增概念 [[sharding]], [[singleton-pattern]]; 更新 [[RabbitMQ]], [[idempotency]], [[SpringBoot]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-25] query | Kubernetes (K8s) 详细介绍
- **输出**: 知识库无 K8s 相关内容，基于通用知识回答；引用 [[Docker]], [[microservices]]

## [2026-05-25] ingest | 固化 Kubernetes 介绍为 synthesis
- **变更**: 新增 [[kubernetes-introduction]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-25] query | K8s 与 Docker 的依赖关系澄清
- **输出**: 纠正 K8s 不依赖 Docker，使用 CRI/containerd；更新 [[kubernetes-introduction]]

## [2026-05-25] query | 生成详细 K8s 教程与注意事项
- **输出**: 已保存至 [[kubernetes-detailed-guide]]; 引用 [[Docker]], [[microservices]], [[SpringBoot]], [[CI-CD]], [[Jenkins]], [[Nginx]]

## [2026-05-25] query | n8n 详细介绍与使用教程
- **输出**: 引用 [[摘要-使用n8n搭建Agent项目笔记]]; 即时回答未保存

## [2026-05-25] ingest | 固化 n8n 介绍为 synthesis
- **变更**: 新增 [[n8n-complete-guide]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-25] ingest | 摄入 Spring 设计模式详解文章
- **变更**: 新增 [[摘要-spring-design-patterns]]; 新增实体 [[BeanFactory]], [[ApplicationContext]], [[JdbcTemplate]], [[ApplicationEvent]], [[HandlerAdapter]], [[Resource]], [[Filter]], [[Interceptor]], [[BeanWrapper]], [[HttpRequestDecorator]], [[DefaultSingletonBeanRegistry]], [[DispatcherServlet]]; 新增概念 [[设计模式]], [[工厂模式]], [[代理模式]], [[模板方法模式]], [[观察者模式]], [[适配器模式]], [[策略模式]], [[责任链模式]], [[装饰器模式]]; 更新 [[Spring]], [[singleton-pattern]], [[index.md]]
- **冲突**: 无

## [2026-05-26] query | 查询 Claude Code 执行过程中纠正 AI 的方法
- **输出**: 即时对话纠正、/rewind 回滚、Git 版本管理、Auto Memory 反馈、CLAUDE.md 永久规则；引用 [[ClaudeCode]], [[摘要-60分钟全面掌握Claude-Code]], [[CLAUDEmd]]

## [2026-05-26] ingest | 摄入"AI 正在重新定义程序员"深度分析文章
- **变更**: 新增 [[摘要-vibe-engineering-era]]; 新增实体 [[AndrejKarpathy]], [[PeterSteinberger]], [[SimonWillison]], [[RomainHuet]], [[AaronFriel]], [[CSDN]], [[Greptile]]; 新增概念 [[VibeCoding]], [[VibeEngineering]], [[cognitive-offloading]], [[silicon-time]], [[ai-schizophrenia]]; 更新 [[OpenAI]], [[Anthropic]], [[BorisCherny]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-26] query | AI 时代程序员如何提升核心竞争力
- **输出**: 引用 [[摘要-vibe-engineering-era]], [[VibeEngineering]], [[VibeCoding]], [[cognitive-offloading]], [[AaronFriel]], [[RomainHuet]]; 已保存至 [[ai-programmer-survival-guide]]

## [2026-05-28] ingest | 摄入 PostgreSQL vs MySQL 技术对比文章
- **变更**: 新增 [[摘要-PostgreSQL-vs-MySQL]]; 新增实体 [[PostgreSQL]], [[TDSQL]], [[PolarDB]], [[GaussDB]], [[openHalo]], [[TimescaleDB]], [[Citus]], [[PgAdmin]]; 新增概念 [[MVCC]], [[WAL]], [[流复制]], [[逻辑复制]], [[Sequence]], [[JSONB]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-28] ingest | 摄入 Anthropic 工程师 Skills 经验分享文章
- **变更**: 新增 [[摘要-anthropic-engineer-skills]]; 新增实体 [[Thariq]]; 新增概念 [[渐进式披露]], [[Gotchas]], [[Hooks]]; 更新 [[Anthropic]], [[ClaudeCode]], [[Skill]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-05-29] lint | 知识库健康巡检与批量修复
- **变更**:
  - 修复 `[[单例模式]]` → `[[singleton-pattern]]` 链接映射（4 个文件）
  - 为 10 个孤儿页面补充关联链接（ai-schizophrenia, sharding, singleton-pattern, Greptile, 6 个 syntheses）
  - 新增 28 个实体页面：GitHub, Gitee, DockerDesktop, Ubuntu, CentOS, Tomcat, VMware, Windows, Hyper-V, WSL2, MyBatis, PageHelper, Lombok, Hikari, Druid, Jackson, FastJson, Hutool, SpringCloudGateway, Sentinel, Redisson, RedisTemplate, SpringDataRedis, Jedis, FreeMarker, CompletableFuture, JHipster, SpringTesting
  - 新增 6 个概念页面：IoC, CGLIB代理, JDK动态代理, duplicate-submit, code-review, api-compatibility
  - 清理 68 处死链：28 个创建页面解决，40 个去掉双链格式
  - 更新 [[index.md]] 注册所有新页面
- **冲突**: 无

## [2026-06-01] ingest | 摄入 ECC 使用教程
- **变更**: 新增 [[摘要-ECC使用教程]]; 新增实体 [[ECC]], [[OpenCode]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-02] ingest | 摄入 Claude Code 官方插件开源与 Codex 极致用法两篇文章
- **变更**: 新增 [[摘要-claude-code-plugins-official]], [[摘要-把Codex用到极致]]; 新增概念 [[durable-threads]], [[steering]], [[queuing]], [[automations]], [[goals]]; 更新 [[ClaudeCode]], [[Codex]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-02] ingest | 摄入字节面试官 RAG 解析文章
- **变更**: 新增 [[摘要-字节面试官什么是RAG为什么需要RAG]]; 新增概念 [[AgenticRAG]], [[GraphRAG]], [[ContextEngineering]]; 新增实体 [[Chroma]], [[LoRA]], [[Gemini]]; 更新 [[RAG]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-02] lint | 为 64 个孤儿来源页补充双向关联连接
- **变更**: 为 64 个 wiki/sources/ 页面的 `## 关联连接` 区域补充了指向已存在 entity/concept 的双链，每个页面至少 2-3 个关联连接；移除了引用不存在页面的死链
- **冲突**: 无

## [2026-06-05] ingest | 摄入 Java 开发栈 Skills 全面指南
- **变更**: 新增 [[摘要-java-stack-skills-guide]]; 新增实体 [[PatternsDev]], [[VercelLabs]]; 新增概念 [[multi-agent-collaboration]]; 更新 [[Skill]], [[ai-agent-skill]], [[index.md]]
- **冲突**: 无

## [2026-06-05] ingest | 摄入 Codex 高效工作流方法论文章
- **变更**: 新增 [[摘要-再见吧-codex]]; 更新 [[Codex]], [[AICoding]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-02] lint | 知识库健康巡检与批量修复
- **变更**:
  - 修复 9 个死链：大小写修正（[[Goals]]→[[goals]], [[Automations]]→[[automations]]）、前缀修正（[[docker安装及使用-windows环境]]→[[摘要-docker安装及使用-windows环境]]）、重定向（[[Kubernetes]]→[[kubernetes-introduction]]）、移除无效链接（[[QoderCLI]]、[[Java-Collections]]、[[Grep]] 改为有效引用）、创建缺失页面（[[Servlet]], [[RestClient]]）
  - 补建 3 个缺失文件：[[ECC]], [[OpenCode]], [[摘要-ECC使用教程]]
  - 清理残留测试文件：test.md
  - 为 64 个孤儿来源页补充双向关联连接
  - 更新 [[index.md]] 注册新页面
- **冲突**: 无

## [2026-06-08] query | 创建 Hermes Agent 完整教程
- **变更**: 新增 [[HermesAgent]], [[NousResearch]], [[hermes-agent-tutorial]]; 更新 [[index.md]]; 从 raw/09-archive 提取资料
- **冲突**: 无

## [2026-06-08] query | 补充 Windows 安全部署章节
- **变更**: 更新 [[hermes-agent-tutorial]] — 新增"Windows 安全部署方案"章节（WSL2+Docker 分层隔离架构、/mnt/c 控制、浏览器操作安全）
- **输出**: 即时回答未保存

## [2026-06-08] ingest | 摄入 AI Agent 工具使用技巧文章
- **变更**: 新增 [[摘要-AI-agent工具应该怎么使用]], [[PaiCLI]]; 更新 [[Codex]], [[AICoding]], [[CLAUDEmd]], [[index.md]]
- **冲突**: 无

## [2026-06-08] ingest | 摄入 Java AI 框架选型指南
- **变更**: 新增 [[摘要-java-ai框架选型指南-2026]]; 新增实体 [[SpringAI_Alibaba]], [[SolonAI]], [[JBoltAI]], [[AgentScope_Java]], [[DashScope]]; 新增概念 [[ReAct_Agent]], [[A2A]], [[Skill_Registry]]; 更新 [[SpringAI]], [[LangChain4j]], [[MCP]], [[AgentHarness]], [[ai-agent-skill]], [[Skill]]; 更新 [[index.md]]
- **冲突**: 标注冲突 [[SpringAI#知识冲突]]（Spring AI Alibaba 定位新旧说法差异，用户选择用新说法覆盖，已移除冲突标注）

## [2026-06-08] query | Spring Security + JWT + Redis 最佳实践

## [2026-06-09] query | 补充 Docker 命令参数知识
- **变更**: 更新 [[Docker]] — 新增 `docker logs -f` 和 `docker rm -f` 参数详解
- **输出**: 即时回答未保存

## [2026-06-09] query | 创建 Kafka 完整教程
- **变更**: 新增 [[kafka-complete-tutorial]]; 更新 [[Kafka]], [[index.md]]
- **输出**: 引用 [[Kafka]], [[message-queue]], [[摘要-bytedance-mq-design]], [[sequential-io]], [[isr]], [[Docker]]

## [2026-06-09] query | Kafka 创建主题方法
- **输出**: 引用 [[kafka-complete-tutorial]]

## [2026-06-09] ingest | 摄入 Docker 和 K8s 核心概念比喻式讲解
- **变更**: 新增 [[摘要-同事一个比喻，让我搞懂了Docker和k8s的核心概念]]; 新增概念 [[Pod]]; 更新 [[Docker]]（补充 Dockerfile/docker-compose/镜像容器关系）; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-09] ingest | 摄入 Ollama+DeepSeek 本地部署教程
- **变更**: 新增 [[摘要-Ollama+DeepSeek本地部署]]; 更新 [[Ollama]]（补充安装步骤/环境变量/CLI使用）; 更新 [[DeepSeek]]（补充 R1 模型系列）; 归档 [[摘要-elasticsearch-8.10-install]] 对应的原始文件
- **冲突**: 无

## [2026-06-09] ingest | 摄入全链路灰度发布8步实战教程
- **变更**: 新增 [[摘要-全链路灰度发布-8步实战教程]]; 新增实体 [[OpenFeign]], [[Prometheus]], [[Grafana]]; 新增概念 [[grayscale-release]], [[gray-tag-propagation]]; 更新 [[Nacos]], [[SpringCloudGateway]]; 更新 [[index.md]]
- **冲突**: 无
- **变更**: 新增 [[spring-security-jwt-redis-best-practice]]; 更新 [[index.md]]
- **输出**: 引用 [[SpringSecurity]], [[JWT]], [[jwt-stateless]], [[token-blacklist]], [[dual-token-mechanism]], [[摘要-springboot4-security7-vue3-best-practice]], [[摘要-token-redis-interview]], [[SpringBoot]], [[Redis]], [[frontend-backend-separation]]

## [2026-06-10] ingest | 整理 URule 规则引擎文章并补充知识网络
- **变更**: 增量更新 [[URule]]（补充注解机制、API 用法、Pro 版功能对比）; 增量更新 [[规则引擎]]（补充决策表对比、职级晋升实战案例）; 注册 [[摘要-Spring-Boot-URule-规则引擎]], [[URule]], [[规则引擎]] 到 [[index.md]]
- **冲突**: 无

## [2026-06-10] ingest | 摄入 MyBatis-Plus SqlSession 复用机制深度解析文章
- **变更**: 新增 [[摘要-spring-mybatis-plus-sqlsession-reuse]]; 增量更新 [[MyBatisPlus]]（补充缓存机制、SqlSession 复用、JPA 对比）; 增量更新 [[transaction-management]]（补充 SqlSession 与事务绑定）; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-11] query | 双 Token 安全设计分析
- **输出**: 已保存至 [[dual-token-security-analysis]]

## [2026-06-11] query | 生成双 Token 设计完整案例文档
- **变更**: 新增 [[dual-token-design-complete]]; 更新 [[index.md]]
- **输出**: 引用 [[dual-token-mechanism]], [[dual-token-security-analysis]], [[token-blacklist]], [[jwt-stateless]], [[JWT]], [[spring-security-jwt-redis-best-practice]]

## [2026-06-11] ingest | 摄入最强AI设计智能体Lovart入门教程
- **变更**: 新增 [[摘要-最强AI设计智能体Lovart入门教程]]; 新增实体 [[Lovart]]; 新增概念 [[AI设计智能体]], [[五要素法]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-11] ingest | 摄入小米 MiMo Code 发布与 Harness 架构解析文章
- **变更**: 新增 [[摘要-mimo-code发布]], [[MiMoCode]], [[Xiaomi]], [[max-mode]], [[dynamic-workflow]], [[checkpoint-rebuild]]; 增量更新 [[goals]], [[AgentHarness]], [[ContextManagement]], [[OpenCode]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入用Codex制作仙侠塔防游戏全流程文章
- **变更**: 新增 [[摘要-用Codex制作仙侠塔防游戏]], [[Godot4]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Codex 必装 skill 推荐文章
- **变更**: 新增 [[摘要-codex必装skill推荐]], [[Web-access]], [[Agent-Reach]], [[HumanizerZh]], [[GitNexus]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 AI 中转站盈利与风险分析文章
- **变更**: 新增 [[摘要-AI中转站盈利与风险分析]], [[AI中转站]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入用 Codex 制作中国风文字冒险游戏全流程文章
- **变更**: 新增 [[摘要-用Codex制作中国风文字冒险游戏]], [[RenPy]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 OpenClaw 小龙虾教程汇总文章
- **变更**: 新增 [[摘要-OpenClaw小龙虾教程汇总]], [[OpenClaw]], [[WorkBuddy]], [[QoderWork]], [[QClaw]], [[ClawBot]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 GPT-image-2 儿童画风玩法文章
- **变更**: 新增 [[摘要-GPT-image-2儿童画风玩法]], [[GPT-image-2]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 GPT-image-2 服装设计玩法文章
- **变更**: 新增 [[摘要-GPT-image-2服装设计玩法]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Hermes Agent 小白入门指南文章
- **变更**: 新增 [[摘要-HermesAgent小白入门指南]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Obsidian 保姆级入门教程文章
- **变更**: 新增 [[摘要-Obsidian保姆级入门教程]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Claude Skills 保姆级教程文章
- **变更**: 新增 [[摘要-ClaudeSkills保姆级教程]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Claude Code 小白入门教程文章
- **变更**: 新增 [[摘要-ClaudeCode小白入门教程]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Codex 保姆级入门教程文章
- **变更**: 新增 [[摘要-Codex保姆级入门教程]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 Docker 部署 OmnoBox 文章
- **变更**: 新增 [[摘要-Docker部署OmnoBox]], [[OmnoBox]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 批量摄入 raw/01-articles/ 全部 13 个文件
- **变更**: 新增 13 篇 source 摘要; 新增 13 个实体页面; 新增 1 个概念页面; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-23] ingest | 摄入 AgentScope Java 2.0 发布文章
- **变更**: 新增 [[摘要-AgentScopeJava2.0发布]]; 增量更新 [[AgentScope_Java]]; 新增概念 [[ReActAgent]], [[HarnessAgent]], [[Middleware]], [[分布式部署]], [[多租户隔离]], [[Workspace]], [[事件流]], [[子Agent编排]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-24] ingest | 摄入 OpenSpec 规范驱动 AI 编程框架文章
- **变更**: 新增 [[摘要-OpenSpec规范驱动AI编程框架]], [[OpenSpec]]; 增量更新 [[AICoding]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-24] ingest | 摄入 Claude Code 一键配置插件 claude-code-setup
- **变更**: 新增 [[摘要-claude-code-setup-plugin]], [[claude-code-setup]], [[claude-automation-recommender]], [[claude-plugins-official]]; 增量更新 [[ClaudeCode]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-24] ingest | 摄入 Claude Code 最佳实践开源仓库 claude-code-best-practice (57k+ Star)
- **变更**: 新增 [[摘要-claude-code-best-practice]], [[claude-code-best-practice]]; 新增概念 [[Command-Agent-Skill编排]], [[Research-Plan-Execute-Review-Ship]], [[跨模型工作流]]; 增量更新 [[ClaudeCode]]; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-26] ingest | 摄入 ECC + OpenCode 使用指南文章
- **变更**: 新增 [[摘要-ECC-OpenCode-使用指南]]; 新增概念 [[TDD]]; 增量更新 [[ECC]]（补充三种安装方式对比、核心工作流速查表）; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-26] ingest | 摄入 MyBatis Plus 12 个性能优化技巧文章
- **变更**: 新增 [[摘要-mybatis-plus-12-optimization-tips]]; 新增概念 [[ORM]], [[逻辑删除]], [[乐观锁]]; 增量更新 [[MyBatisPlus]]（补充最佳实践）; 更新 [[index.md]]
- **冲突**: 无

## [2026-06-29] ingest | 摄入 4 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-ai-agent-抓包协作]], [[摘要-Spring-Cloud-Gateway-War-Tomcat]], [[摘要-Claude-Code-Workflows-vs-MetaSKILL]], [[摘要-Spring-Boot-to-Solon-注解迁移]]
  - 增量更新 entities: [[SpringCloudGateway]]（补充 War 包部署外置 Tomcat 方案）, [[ClaudeCode]]（补充 Dynamic Workflows 章节）, [[OpenClaw]]（补充 MetaSKILL 编排引擎章节）, [[SolonAI]]（补充 Spring Boot → Solon 注解迁移章节）
  - 增量更新 concepts: [[dynamic-workflow]]（补充 Claude Code Workflows 实现与 MetaSKILL 对比）, [[meta-skill]]（补充 OpenClaw.NET MetaSKILL 声明式 DAG 编排）
  - 更新 [[index.md]]
- **冲突**: 无

## [2026-06-29] ingest | 摄入 4 篇 raw/01-articles 文章（Codex/FastAPI/国产模型/QR登录）
- **变更**:
  - 新增 sources: [[摘要-codex-vs-claude-code-对比]], [[摘要-fastapi-入门教程]], [[摘要-国产大模型实战横评]], [[摘要-二维码扫码登录原理]]
  - 新增 entities: [[FastAPI]], [[Pydantic]], [[Uvicorn]], [[Kimi]], [[MiniMax]], [[GLM]]
  - 新增 concepts: [[ASGI]], [[QR码登录]], [[Token认证机制]]
  - 增量更新 entities: [[ClaudeCode]]（补充与 Codex 2026-06 对比小节）, [[Codex]]（补充 Harness 架构与对比小节）, [[DeepSeek]]（补充 V4 Pro 2026-06 实战横评表现）
  - 更新 [[index.md]]
- **冲突**: 无
- **归档**: 4 篇原始文章移动到 raw/09-archive/

## [2026-06-29] ingest | 摄入抖音视频《Vibe Coding实战篇总结：开发全流程（上）》
- **变更**:
  - 新增 source [[摘要-vibe-coding-实战篇总结-上]]（抖音创作者敲代码的小虾米的 Vibe Coding 实战工作流上篇）
  - 新增 entity [[敲代码的小虾米]]（抖音 Vibe Coding 实战教学创作者）
  - 增量更新 concept [[VibeCoding]]（补充实战工作流四步法：立项/选技术栈/搭架构/写 Agent 宪法）
  - 更新 [[index.md]] 加入 2 个新条目（1 source + 1 entity）
- **冲突**: 无（[[VibeCoding]] 原页面仅含 Karpathy 定义和 Vibe Engineering 对比，实战工作流为互补视角）
## [2026-06-29] ingest | 摄入抖音视频《Vibe Coding实战篇总结：开发全流程（下）》
- **变更**:
  - 新增 source [[摘要-vibe-coding-实战篇总结-下]]（敲代码的小虾米的 Vibe Coding 实战工作流下篇：立真源/落文档/敲代码/阶段验收）
  - 增量更新 concept [[VibeCoding]]（补充执行方法论：拆真源文档、分阶段推进、逐阶段验收；合并上下篇为完整工作流）
  - 更新 [[index.md]] 加入 1 个新 source 条目
- **冲突**: 无（与上篇互补，合在一起构成完整开发全流程）

## [2026-07-01] ingest | 摄入《谁再说 try catch 必须放 for 循环外面，直接走人！》
- **变更**:
  - 新增 source [[摘要-try-catch-异常边界]]（胖虎 Java专栏，try catch 内外之争的本质）
  - 新增 concept [[异常边界]]（Exception Boundary：失败停在哪里 + 事务/性能/catch 纪律三坑）
  - 新增 entity [[胖虎]]（公众号作者，同时关联既有 [[摘要-jwt-双token续签设计]]）
  - 更新 [[index.md]] 加入 3 个新条目（1 source + 1 entity + 1 concept）
- **冲突**: 无（[[transaction-management]] 已有事务回滚/REQUIRES_NEW/自调用失效知识，本文从异常边界视角互补引用，未覆盖）

## [2026-07-01] ingest | 摄入《RocketMQ 已正式接入 AI ！》
- **变更**:
  - 新增 source [[摘要-rocketmq-接入ai]]（苏三说技术，RocketMQ 5.5.0 面向 AI 的升级）
  - 新增 concept [[LiteTopic]]（轻量主题：百万级/自动创建/TTL/断点续传，支撑 Multi-Agent 异步通信）
  - 新增 entity [[苏三]]（公众号作者，连接既有 6+ 篇 source 引用，消除孤岛）
  - 增量更新 entity [[RocketMQ]]（补充 RocketMQ for AI 章节：LiteTopic/异步通信/会话管理/智能调度/MCP+A2A 生态）
  - 更新 [[index.md]] 加入 3 个新条目（1 source + 1 entity + 1 concept）
- **冲突**: 无（[[RocketMQ]] 原页面为传统消息队列能力，AI 能力为新增章节互补）

## [2026-07-02] ingest | 摄入《测评国内多模态大模型，到底哪个更省事？》
- **变更**:
  - 新增 source [[摘要-多模态大模型横评-苏三]]（Step 3.7 Flash / MiniMax M3 / Qwen3.6-flash 在流程图与发票两个生产场景下的三维度横评）
  - 新增 concept [[多模态大模型]]（Multimodal LLM 定义 + 生产可用性三维评估：质量/速度/成本）
  - 增量更新 entity [[Step3Flash]]（补充多模态横评综合胜出的两场景实测数据）
  - 增量更新 entity [[MiniMax]]（补充 M3 多模态实测：质量达标但 Token 消耗与耗时偏高）
  - 增量更新 entity [[Qwen]]（补充 3.6-flash 多模态实测：稳定但速度和 Token 居中偏后，流程图少 1 步）
  - 增量更新 entity [[苏三]]（补充横评方法论与新收录 source/concept）
  - 更新 [[index.md]] 加入 2 个新条目（1 source + 1 concept）
- **冲突**: 无（既有 Step3Flash / MiniMax / Qwen 页面此前只覆盖 Coding Agent 或长上下文视角，多模态视角为互补新增）
- **归档**: raw/01-articles/测评国内多模态大模型，到底哪个更省事？.md → raw/09-archive/

## [2026-07-02] ingest | 摄入《干掉 if...else，推荐一个小而美的规则引擎》
- **变更**:
  - 新增 source [[摘要-easy-rules-规则引擎]]（苏三说技术，用规则对象干掉 if...else）
  - 新增 entity [[EasyRules]]（j-easy 轻量级 Java 规则引擎：四大抽象/四种定义方式/两种引擎/三种复合规则/优缺点/选型）
  - 新增 entity [[MartinFowler]]（规则引擎朴素定义提出者，Easy Rules 设计灵感来源）
  - 增量更新 concept [[规则引擎]]（把 EasyRules 从列表一句话扩展为双链实体条目，补充 Drools/Easy Rules/URule 三者选型路径与关联连接）
  - 增量更新 entity [[苏三]]（新增本文 source 与提炼实体，补充 sources frontmatter）
  - 更新 [[index.md]] 加入 3 个新条目（1 source + 2 entity）
- **冲突**: 无（[[规则引擎]] 原页面以 URule 可视化路线为主，Easy Rules 为代码/注解路线的互补新增）
- **归档**: raw/01-articles/干掉if...else，推荐一个小而美的规则引擎.md → raw/09-archive/

## [2026-07-06] ingest | 批量摄入 4 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-solon-chatmodel-java-llm]], [[摘要-ai-agent-day10-tool-pipeline]], [[摘要-loop-engineering-guide]], [[摘要-spring-ai-2-agent-tips]]
  - 新增 concepts: [[ChatSession]], [[DialectPattern]], [[ToolPipeline]], [[LoopEngineering]], [[AdvisorChain]]
  - 增量更新 entities: [[SolonAI]]（补充 ChatModel API、方言模式、ChatSession 三种实现、Providers 表）, [[SpringAI]]（补充 Spring AI 2.0 Agent 最佳实践：@Tool/AdvisorChain/ToolCallingAdvisor/流式/可观测性）, [[ClaudeCode]]（补充 Loop Engineering 引用）, [[Codex]]（补充 Loop Engineering 引用）
  - 增量更新 concepts: [[ChatClient]]（补充 Spring AI 2.0 @Tool/ToolCallingAdvisor/Advisor 链/记忆集成）, [[ChatMemory]]（补充 Spring AI 2.0 MessageChatMemoryAdvisor）, [[FunctionCalling]]（补充 Spring AI 2.0 @Tool 注解）, [[distributed-lock]]（补充 Agent 会话锁场景）, [[ReAct_Agent]]（补充 ToolPipeline 对比）
  - 更新 [[index.md]]
  - 归档 raw/01-articles/ 4 个源文件至 raw/09-archive/
- **冲突**: 无（所有内容为互补新增，未与现有知识冲突）

## [2026-07-03] ingest | 摄入 Claude Code 底层深扒文章与 Codex+Obsidian 自生长知识库教程
- **变更**:
  - 新增 sources: [[摘要-沉默王二-claude-code-底层深扒]], [[摘要-codex-obsidian-自生长知识库]]
  - 新增 entities: [[沉默王二]], [[Obsidian]], [[Xuan_酱]]
  - 新增 concept: [[自生长知识库]]
  - 增量更新 entity [[ClaudeCode]]（补充底层架构：Query Loop 异步生成器/StreamingToolExecutor 推测执行/自声明工具系统/7 级权限模式含 auto LLM 分类器/子 Agent 作为独立 Query Loop 实例/Hook 优先级覆盖）
  - 更新 [[index.md]]
- **冲突**: 无（ClaudeCode 权限模式新旧为用户视角与源码视角的互补，非冲突）

## [2026-07-14] ingest | 归档 Kaku 终端文章（已处理）
- **变更**: 源文件 `又一个神级终端诞生了！让 Claude Code和Codex 用得更爽！.md` 此前已完整编译到 [[Kaku]]（实体）和 [[摘要-kaku-ai-terminal]]（来源），但遗漏归档步骤，本次补齐
- **冲突**: 无
- **归档**: raw/01-articles/又一个神级终端诞生了！让 Claude Code和Codex 用得更爽！.md → raw/09-archive/；raw/_daily_digest.md → raw/09-archive/_daily_digest_2026-07-13.md

## [2026-07-08] query | 解析 IntelliJ IDEA 中 AI agents 选项的 Junie
- **输出**: 即时回答未保存（本地知识库无 Junie 条目，引用 JetBrains/junie GitHub 仓库与 IDEA 2026.1 官方文档）

## [2026-07-08] query | 追问 Junie 是否支持国产模型 API
- **输出**: 即时回答未保存（引用 JetBrains/junie registry-staging.json ACP 注册表与 README BYOK 说明）

## [2026-07-08] query | 查询 OpenCode 使用教程
- **输出**: 引用 [[OpenCode]]、[[ECC]]、[[摘要-ECC-OpenCode-使用指南]]；知识库主要为 ECC+OpenCode 配合教程，OpenCode 本体安装需补官方文档

## [2026-07-08] ingest | 整理 Junie 及国产模型配置指南
- **变更**: 新增 [[Junie]]、[[junie-国产模型配置指南]]；更新 [[index.md]]、[[IntelliJIDEA]]
- **冲突**: 无

## [2026-07-08] query | 查询 IDEA 的 AI Assistant 能做什么
- **输出**: 引用 [[IntelliJIDEA]]、[[Junie]]、[[junie-国产模型配置指南]]；即时回答未保存（待用户决定是否固化为 synthesis）

## [2026-07-08] query | 整理 IDEA AI Assistant 三次提问（能力/ACP/补全/免费方案）
- **输出**: 已固化为 synthesis [[idea-ai-assistant-guide]]；更新 [[index.md]] Syntheses 分类
- **冲突**: 无（代码补全部分为通用知识，已在页面中标注）

## [2026-07-08] query | IDEA 自带热更新报错 schema change not implemented
- **输出**: 即时回答未保存；知识库无 HotSwap 专门条目（现有"热更新"均指 K8s/OSGi），引用 [[IntelliJIDEA]]、[[JVM]]、[[HotSpot]] 作为关联实体；回答内容为通用知识（JVM 标准 HotSwap 仅支持方法体替换，schema change 需 DCEVM/JRebel/DevTools）

## [2026-07-09] ingest | 摄入 3 篇 AI 编程工作流与 Spring AI 文章
- **变更**: 新增来源 [[摘要-spec-superflow-融合工作流]]、[[摘要-spring-ai-2-对话记忆实战]]、[[摘要-spring-ai-2-vs-alibaba选型]]；新建实体 [[SpecSuperflow]]、[[FissionAI]]、[[MageByte-Zero]]、[[程序员追风]]；新建概念 [[execution-contract]]、[[seven-state-machine]]、[[delta-spec]]、[[review-gate]]、[[subagent-driven-development]]；增量更新 [[OpenSpec]]、[[Superpowers]]、[[SpringAI]]、[[SpringAI_Alibaba]]、[[苏三]]、[[ChatMemory]]；同步 [[index.md]]
- **冲突**: [[SpringAI]] 版本基线更新——旧记「Spring Boot 3.x+」，新文（2026-07-09）明确 Spring AI 2.0 GA 基于 Spring Boot 4.1 + Spring Framework 7.0，已据更权威的新来源纠正

## [2026-07-09] ingest | 补注册 + 归档 2 篇已处理文章与每日摘要
- **变更**:
  - 注册 source [[摘要-architecture-diagram-generator]] 和 [[摘要-claude-code-实战防搞炸]] 到 [[index.md]] Sources 分类（此前页面已存在但索引缺失）
  - 归档: raw/01-articles/面试官坏笑...md → raw/09-archive/
  - 归档: raw/01-articles/又一个神级画图 Skill 开源...md → raw/09-archive/
  - 归档: raw/_daily_digest.md → raw/09-archive/_daily_digest_2026-07-09.md
- **冲突**: 无

- **冲突**: 无

## [2026-07-10] query | AI Agent 运行出错后的纠正方法
- **输出**: 引用 [[steering]], [[摘要-claude-code-实战防搞炸]], [[摘要-6条Claude-Code实践经验与思考]], [[摘要-claude-code-best-practice-苏三视角]], [[摘要-AI-agent工具应该怎么使用]], [[摘要-codex-97percent-技巧]]；即时回答未保存（待用户确认是否固化为 synthesis）
- **结论**: 纠正手段分即时（Steering 增量纠偏）+ 流程（Plan 模式先行/Plan-Execute 分 Session）+ 自动（Hooks 拦截/测试）+ 回退（小步 Git commit + diff）+ 协作（多模型交叉验证）五层

## [2026-07-10] synthesis | 固化"AI Agent 运行出错纠正策略"为 synthesis 页面
- **变更**: 新增 [[agent-error-correction-strategies]]（五层纠正体系：即时/流程/隔离/自动/回退），更新 [[index.md]] Syntheses 分类
- **引用**: [[steering]], [[Hooks]], [[计划模式]], [[CLAUDEmd]], [[Worktree]], [[ContextManagement]], [[code-review]], [[auto-mode]], [[ClaudeCode]], [[Codex]]

- **冲突**: 无

## [2026-07-10] ingest | 摄入诗词大模型本地微调全方案文章
- **变更**:
  - 新增 source [[摘要-开源诗词数据集poetry_dataset]]（poetry_dataset 开源项目 + shi-ci.cn 配套站点的诗词大模型本地微调全方案）
  - 新增 entities: [[poetry_dataset]], [[shi-ci.cn]]
  - 增量更新 entities: [[Qwen]]（新增本地微调章节，支持 Qwen2.5 系列底座模型）、[[LoRA]]（新增 MLX + poetry_dataset 实战案例）
  - 更新 [[index.md]]（1 source + 2 entities）
- **冲突**: 无
- **归档**: raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md → raw/09-archive/

## [2026-07-21] ingest | 摄入 Spring Cloud Stream 整合 RocketMQ 完全指南
- **变更**: 新增 [[摘要-spring-cloud-stream-rocketmq]]; 新增实体 [[SpringCloudStream]], [[SpringCloudAlibaba]]; 新增概念 [[死信队列]]; 增量更新 [[RocketMQ]]（补充 Spring Cloud Stream 集成章节、版本兼容对照表、函数式编程模型）
- **冲突**: 无
- **归档**: raw/01-articles/Spring Cloud Stream 整合 RocketMQ 完全指南.md → raw/09-archive/；raw/_daily_digest.md → raw/09-archive/_daily_digest_2026-07-21.md

## [2026-07-09] lint | 修复 7 个问题（4 死链 + 3 孤儿）
- **变更**: 修复死链 4 个--[[Obsidian]] 去除示例文本 [[wikilink]] 双链模式；[[SpringAI_Alibaba]] 与 [[摘要-spring-ai-2-vs-alibaba选型]] 的 [[摘要-spring-ai-vs-langchain4j]] 前缀笔误纠正为 [[spring-ai-vs-langchain4j]]；[[idea-ai-assistant-guide]] 的 [[ACP]] 改为普通文本。修复孤儿 3 个--[[Transformer]] 补 [[Tesla]]（inline 双链）与 [[FigureAI]]（关联连接）；[[Junie]] 补 [[idea-ai-assistant-guide]] 引用。[[摘要-追番]] 作为个人记录保留原样。
- **冲突**: 无

## [2026-07-13] ingest | 批量摄入 7 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-shadcn-ui介绍]], [[摘要-LangChain与LangGraph对比]], [[摘要-SolonAI-ReActAgent智能客服]], [[摘要-ShadcnUI构建Java桌面应用]], [[摘要-RAG-KAG双引擎知识库系统]]
  - 新增 entities: [[shadcn_ui]], [[JxBrowser]], [[Neo4j]]
  - 新增 concepts: [[KAG]], [[HITL]]
  - 增量更新 entities: [[FastAPI]], [[LangChain]], [[LangGraph]], [[SolonAI]]
  - 更新 [[index.md]] 加入 10 个新条目（5 source + 3 entity + 2 concept）
- **冲突**: 无
- **归档**: raw/01-articles/ 5 个源文件至 raw/09-archive/（2 篇已有摘要的 FastAPI/LangChain 文章仅增量更新，未重复创建 source）
## [2026-07-14] ingest | Claude Code 最佳实践最新版 + spec-superflow 源码级详解
- **变更**: 新增 [[摘要-claude-code-best-practice-最新版]], [[摘要-spec-superflow-融合工作流-源码级详解]]; 新增 [[计划模式]], [[DP-3]] concepts; 更新 [[ClaudeCode]], [[SpecSuperflow]], [[eight-state-machine]] entities; 更新 [[index.md]]
- **冲突**: 无（spec-superflow 七状态机 vs 八状态机为版本演化，已标注在 eight-state-machine 页面）

## [2026-07-14] ingest | 摄入 Kaku AI 终端介绍文章
- **变更**:
  - 新增 source [[摘要-kaku-ai-terminal]]（沉默王二，Kaku AI 终端：Rust+WezTerm 定制，Claude Code+Codex 双面板对决）
  - 新增 entities: [[Kaku]], [[WezTerm]], [[Lazygit]], [[Yazi]]
  - 增量更新 entity [[沉默王二]]（补充 2026-07-14 推荐 Kaku 新来源）
  - 更新 [[index.md]] 加入 5 个新条目（1 source + 4 entity）
- **冲突**: 无
- **归档**: ⚠️ 待手动归档 — raw/01-articles/又一个神级终端诞生了！让 Claude Code和Codex 用得更爽！.md → raw/09-archive/（checkpoint writer 无文件移动权限）

## [2026-07-14] ingest | 摄入 SpringBoot 电子文件签字盖章系统文章
- **变更**:
  - 新增 source [[摘要-springboot-电子文件签字盖章系统]]（小哈学Java，SpringBoot+Thymeleaf 实现电子文件在线签字盖章系统）
  - 新增 entities: [[PageOffice]], [[MobOffice]], [[ZhuozhengSoft]]
  - 新增 concepts: [[在线文档处理]], [[电子签名]], [[数字签名]]
  - 更新 [[index.md]] 加入 7 个新条目（1 source + 3 entity + 3 concept）
- **冲突**: 无
- **归档**: raw/01-articles/SpringBoot 实现电子文件签字+合同系统！.md → raw/09-archive/

## [2026-07-15] ingest | 摄入 Trellis 实践、Trellis 手册与 Codex Java 落地文章
- **变更**: 新增 [[摘要-从-vibe-coding-到-spec-coding]]、[[摘要-codex-从原理到-java落地]]、[[摘要-trellis使用手册]]；新增 [[Trellis]]、[[项目级AI工作流]]；增量更新 [[Codex]]、[[苏三]]、[[AgentHarness]]、[[规范驱动开发]]、[[VibeCoding]]；更新 [[index.md]]。
- **冲突**: 无。Codex 文章中的具体模型、基准、效率、资源与成本数据已保留为来源作者观点，未作为未经核验的通用事实合并。
- **原始资料**: 遵循 raw 不可变契约，未移动、修改或删除任何 `raw/` 文件；`raw/_daily_digest.md` 仅记录“无新增文章”，未生成知识页。

## [2026-07-15] archive | 补归档 3 篇已编译源文件 + 每日摘要
- **变更**:
  - 归档 raw/01-articles/ 3 个源文件至 raw/09-archive/（补全 2026-07-15 ingest 遗漏的归档步骤）
  - 归档 raw/_daily_digest.md → raw/09-archive/_daily_digest_2026-07-14.md（无新增文章）
- **冲突**: 无

## [2026-07-16] ingest | 批量摄入 5 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-aliyun-llms-txt]], [[摘要-sso-single-sign-on]], [[摘要-mysql-primary-key-strategy]], [[摘要-loop-engineering-pitfalls]]
  - 新增 entities: [[AlibabaCloud]], [[阶跃星辰]]
  - 新增 concepts: [[llms-txt协议]], [[两级索引架构]], [[CAS协议]], [[SSO]], [[Session]], [[Cookie]], [[OAuth2]], [[聚簇索引]], [[页分裂]], [[B+树]], [[可观测性]]
  - 增量更新 concept [[LoopEngineering]]（补充生产环境五大坑：硬隔离/原样转发/停止规则/状态落地/目标可验证）
  - 更新 [[index.md]] 加入 15 个新条目（4 source + 2 entity + 11 concept）
- **冲突**: 无（[[Session]] 与既有 [[ChatSession]] 为不同概念：前者是 Web 会话管理，后者是 AI 对话记忆）
- **归档**: raw/01-articles/ 5 个源文件 + raw/_daily_digest.md → raw/09-archive/

## [2026-07-16] ingest | 摄入 marka.md Rust Markdown 编辑器文章
- **变更**:
  - 新增 source [[摘要-markamd-rust-markdown-ai]]（小锋，marka.md 专为 AI 设计的轻量 Markdown 编辑器）
  - 新增 entities: [[marka.md]], [[Tauri]], [[CodeMirror]], [[Shiki]]
  - 新增 concepts: [[ContextTray]], [[本地优先]], [[AI就绪上下文包]]
  - 增量更新 entities: [[Rust]]（补充 marka.md 应用案例）、[[小锋]]（补充新来源）、[[Mermaid]]（补充 marka.md 使用场景）、[[Obsidian]]（补充同类工具对比）
  - 增量更新 concept [[AICoding]]（补充 AI 就绪上下文包概念）
  - 更新 [[index.md]] 加入 8 个新条目（1 source + 4 entity + 3 concept）
- **冲突**: 无

## [2026-07-17] ingest | 摄入 CodeGraph MCP 网关部署与 Claude Code 状态栏工具 2 篇文章
- **变更**:
  - 新增 sources: [[摘要-codegraph-mcp-gateway]], [[摘要-claude-code-statusline]]
  - 新增 entities: [[CodeGraph]], [[ccstatusline]], [[claude-hud]]
  - 更新 [[index.md]] 加入 5 个新条目（2 source + 3 entity）
- **冲突**: 无

## [2026-07-20] ingest | 批量摄入 3 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-spring-why-abandon-feign]], [[摘要-rag-api-call]], [[摘要-ai-agent-cognitive-navigation]]
  - 新增 entities: [[FAISS]]
  - 新增 concepts: [[HttpExchange]], [[CognitiveNavigation]]
  - 增量更新 entities: [[苏三]]（补充 Spring Feign 来源）、[[OpenFeign]]（补充 @HttpExchange 对比章节）、[[DashScope]]（补充 API 兼容模式与 RAG 实践）、[[Qwen]]（补充三层模型选型）
  - 增量更新 concept: [[Agent]]（补充 CognitiveNavigation 运行时健康诊断引用）
  - 更新 [[index.md]] 加入 8 个新条目（3 source + 1 entity + 2 concept + 2 关联更新）
- **冲突**: 无

## [2026-07-20] ingest | 摄入 FastCode 代码库理解框架文章
- **变更**:
  - 新增 source [[摘要-fastcode-hkuds-codebase-understanding]]（港大 HKUDS 开源的代码库理解神器，Scouting-First 策略）
  - 新增 entities: [[FastCode]], [[HKUDS]]
  - 新增 concept: [[Scouting-First]]
  - 更新 [[index.md]] 加入 4 个新条目（1 source + 2 entity + 1 concept）
- **冲突**: 无

## [2026-07-20] ingest | 摄入画图 Skill 推荐文章（苏三）
- **变更**:
  - 增量更新 source [[摘要-architecture-diagram-generator]]（补充苏三来源，6.3k Star 数据，Claude Desktop 安装方式）
  - 增量更新 entities: [[ArchitectureDiagramGenerator]]（补充 6.3k Star、Claude Desktop 安装方式）、[[CocoonAI]]（补充新来源）
  - 新增 entity [[ProcessFlowDiagramGenerator]]（CocoonAI 流程图生成 Skill）
  - 更新 [[index.md]] 加入 1 个新 entity 条目
- **冲突**: 无

## [2026-07-20] ingest | 摄入 CodeGraph 深度解析文章（苏三）
- **变更**:
  - 新增 source [[摘要-codegraph-deep-dive]]（苏三全面介绍 CodeGraph：tree-sitter 构建代码知识图谱）
  - 新增 entity [[TreeSitter]]（高性能增量 AST 解析库）
  - 增量更新 entity [[CodeGraph]]（补充完整架构/性能数据/CLI 命令/MCP 工具/安装方式）
  - 更新 [[index.md]] 加入 3 个新条目（1 source + 2 entity）
- **冲突**: 无

## [2026-07-21] ingest | 摄入 Apache PDFBox 全面解析文章
- **变更**:
  - 新增 source [[摘要-apache-pdfbox]]（苏三说技术，Apache PDFBox 开源 Java PDF 处理库全解析）
  - 新增 entity [[Apache_PDFBox]]（Apache 基金会维护的 Java PDF 处理库）
  - 新增 concepts: [[PDFBox-双层架构]]（COS 层与 PD 层设计）、[[Apache-2.0协议]]（对商业友好的开源协议）
  - 增量更新 entity [[苏三]]（补充 PDFBox 来源与提炼的实体/概念）
  - 更新 [[index.md]] 加入 5 个新条目（1 source + 1 entity + 2 concept + 1 关联更新）
- **冲突**: 无
- **归档**: raw/01-articles/为什么越来越多人使用PDFBox？.md → raw/09-archive/

## [2026-07-22] ingest | 批量摄入 5 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-dataway-dataql]], [[摘要-minio-rustfs]], [[摘要-skywalking-install]], [[摘要-agent-engineering]], [[摘要-hermes-agent-complete-guide]]
  - 新增 entities: [[Dataway]], [[DataQL]], [[Hasor]], [[IT码徒]], [[RustFS]], [[AiStor]], [[SkyWalking]], [[OpenJDK]], [[Rivet]], [[Vellum]], [[OpenAIAgentsSDK]]
  - 新增 concepts: [[distributed-object-storage]], [[open-source-commercialization]], [[distributed-tracing]], [[augmented-llm]], [[prompt-chaining]], [[routing-workflow]], [[parallelization-workflow]], [[orchestrator-workers]], [[evaluator-optimizer]], [[autonomous-agent]], [[guardrails]], [[context-compression]], [[persistent-memory]], [[mixture-of-agents]], [[kanban-swarm]], [[gateway-messaging]], [[task-delegation]]
  - 增量更新 entities: [[MinIO]]（覆盖社区版已移除 Web 界面 + 商业化信息）、[[HermesAgent]]（大幅扩展：上下文文件/持久记忆/技能系统/Kanban 多 Agent 协作/MoA 等）、[[NousResearch]]（补充 Skills Hub 生态建设）
  - 更新 [[index.md]] 加入 33 个新条目（5 source + 11 entity + 17 concept）
- **冲突**: [[MinIO]] Web 控制台信息冲突（旧文称有控制台/2024 年后社区版已移除），用户选择用新知识覆盖
- **归档**: raw/01-articles/ 5 个源文件至 raw/09-archive/

## [2026-07-22] query | 手搓 Agent 完整指南
- **输出**: 引用 [[Agent]], [[ReAct_Agent]], [[构建你的第一个Tool-Agent-从零理解ReAct循环]], [[摘要-agent-tools-workflow区别]], [[LangGraph]], [[ToolPipeline]]; 已保存为 [[hand-craft-agent-guide]]
- **变更**: 新增 synthesis [[hand-craft-agent-guide]]；更新 [[index.md]] Syntheses 分类

## [2026-07-22] query | RocketMQ 重复消费问题
- **输出**: 引用 [[摘要-rabbitmq-idempotency]], [[idempotency]], [[摘要-spring-cloud-stream-rocketmq]], [[摘要-prevent-duplicate-order]]; 已保存为 [[重复消费解决方案]]
- **变更**: 新增 synthesis [[重复消费解决方案]]；更新 [[index.md]] Syntheses 分类

## [2026-07-23] ingest | 批量摄入 6 篇 raw/01-articles 技术资料
- **变更**:
  - 新增 sources: [[摘要-从winforms到vue-ds-ui-gui框架]], [[摘要-skywalking-docker-compose-install]], [[摘要-dyad-ai全栈构建器]], [[摘要-胖虎-skill教程]], [[摘要-jeandle-llvm-jit编译器]], [[摘要-分库分表六大痛点]]
  - 新增 entities: [[ds-ui]], [[Dyad]], [[Supabase]], [[LM_Studio]], [[Jeandle]], [[蚂蚁集团]], [[小哈]], [[Seata]]
  - 新增 concept: [[LLVM]]
  - 增量更新 entity [[SkyWalking]]（补充 Docker Compose 部署方式与健康检查配置）
  - 增量更新 entity [[胖虎]]（补充 Skill 教程新文章）
  - 增量更新 concept [[sharding]]（补充六大痛点详解：跨库 Join/分页排序/分布式事务/全局ID/数据迁移/聚合统计）
  - 增量更新 concept [[JIT编译]]（补充 Jeandle 基于 LLVM 的 JIT 编译器新发展）
  - 更新 [[index.md]] 加入 15 个新条目（6 source + 8 entity + 1 concept）
- **冲突**: 无
- **归档**: raw/01-articles/ 6 个源文件 + raw/_daily_digest.md → raw/09-archive/

## [2026-07-23] query | Loop/Prompt/Skill 区别与最佳实践
- **输出**: 引用 [[LoopEngineering]], [[Skill]], [[提示词工程]], [[ClaudeCode]], [[Codex]], [[ECC]], [[Superpowers]], [[摘要-loop-engineering-guide]], [[摘要-loop-engineering-pitfalls]], [[摘要-胖虎-skill教程]]; 已保存为 [[loop-prompt-skill-guide]]
- **变更**: 新增 synthesis [[loop-prompt-skill-guide]]；更新 [[index.md]] Syntheses 分类

## [2026-07-23] synthesis | 固化 Loop 最佳实践（Java 全栈版）
- **变更**: 新增 synthesis [[loop-best-practice-java-fullstack]]（16 章：三种循环机制对比/五大设计原则源自生产坑/STATE.md 六段规范/CLAUDE.md 配置/8 个场景模板含分诊与迁移/Java 测试金字塔分层/四种编排模式含 builder-checker 隔离/L1-L3 渐进信任/停止规则与中断恢复/Token 预算/12 坑对策/反模式/2 端到端实战案例）
- **关联**: 补充 [[LoopEngineering]] 五大坑的工程落地、[[ClaudeCode]] 权限与子Agent隔离、[[TDD]] 嵌套循环、[[计划模式]] 先对齐后执行
- **冲突**: 无（与现有 [[LoopEngineering]] 和 [[loop-prompt-skill-guide]] 互补，不冲突）

## [2026-07-22] ingest | 摄入 AgentScope 入门指南（苏三）
- **变更**: 
  - 新增 source [[摘要-AgentScope入门指南]]（苏三撰写的 AgentScope-Java 2.0 入门实战指南）
  - 增量更新 entity [[AgentScope_Java]]（新增入门开发要点：@Tool 注解系统/Hello World 三步骤/MCP 集成/子Agent 文件驱动/与 Spring AI Alibaba 定位对比）
  - 增量更新 entity [[苏三]]（补充 AgentScope 入门指南新来源）
  - 增量更新 concept [[HarnessAgent]]（补充工程能力一览表/MCP 自动集成/子Agent 两种定义方式）
  - 增量更新 concept [[ReActAgent]]（补充适用场景与实践建议）
  - 增量更新 concept [[MCP]]（补充 AgentScope 集成方式：tools.json/三种传输协议/常用 Server）
  - 增量更新 concept [[子Agent编排]]（补充两种定义方式/orchestrator+workers 模式/实战示例）
  - 增量更新 concept [[Workspace]]（补充新来源引用）
  - 更新 [[index.md]] 加入 1 个新 source 条目
- **冲突**: 无（所有内容为互补新增，未与现有知识冲突）

## [2026-07-24] ingest | 摄入程序汪肉鸽小游戏二期项目
- **变更**: 新增 [[摘要-程序汪-肉鸽小游戏二期]]; 新增 [[CocosCreator]], [[Netty]]; 新增 [[roguelike-game]], [[jsbridge]]; 增量更新 [[程序汪]]（新增代表项目与来源）
- **冲突**: 无
- **归档**: raw/01-articles/程序汪4万20天接的肉鸽类小游戏，二期项目.md → raw/09-archive/

## [2026-07-29] query | 解答 ECC 是什么、类似框架对比及使用方式
- **输出**: 引用 [[ECC]], [[ClaudeCode]], [[摘要-ECC-OpenCode-使用指南]], [[claude-code-增强框架对比]], [[Superpowers]], [[OpenSpec]], [[SpecKit]], [[规范驱动开发]], [[VibeCoding]]; 知识库已有完整合成页面 [[claude-code-增强框架对比]]，未另存 synthesis

## [2026-07-29] query | 棕地项目选型及 AI 遗忘原始决策的解决方法
- **输出**: 引用 [[OpenSpec]], [[claude-code-增强框架对比]], [[delta-spec]], [[规范驱动开发]], [[ContextManagement]], [[persistent-memory]]; 未另存 synthesis

## [2026-07-29] query | 棕地项目 OpenSpec 详细使用方案
- **输出**: 引用 [[OpenSpec]], [[delta-spec]], [[SpecSuperflow]], [[规范驱动开发]], [[摘要-OpenSpec规范驱动AI编程框架]], [[摘要-spec-superflow-融合工作流-源码级详解]], [[摘要-claude-code-best-practice-最新版]], [[ClaudeCode]], [[Superpowers]]; 已固化 synthesis [[openspec-brownfield-usage-guide]]

## [2026-07-29] query | OpenSpec init --tools 是否支持多工具
- **输出**: 引用 [[OpenSpec]]; 联网查证官方 CLI 文档确认 --tools 支持逗号分隔多工具/all/none，共 31 个工具 ID；增量更新 [[OpenSpec]] 安装与初始化章节

## [2026-07-30] ingest | Hutool Sftp.upload 不会自动创建目录踩坑
- **变更**: 增量更新 [[Hutool]]（新增「踩坑记录」章节，记录 Sftp.upload 与 Ftp.upload 差异及解决方式）
- **冲突**: 无

## [2026-07-30] ingest | 批量摄入 4 篇 raw/01-articles 文章
- **变更**:
  - 新增 sources: [[摘要-写好提示词的三大原则]], [[摘要-前端转全栈-36行规则]], [[摘要-Docker部署Keycloak]], [[摘要-HermesAgent-0基础教程]]
  - 新增 entities: [[舒克无良]], [[JeecgBoot]], [[Keycloak]], [[Let's Encrypt]], [[秋芝2046]]
  - 新增 concepts: [[SuperProgramming开发流程]], [[OIDC]], [[SAML]], [[辅助模型]]
  - 增量更新 [[提示词工程]]（补充三大原则：简洁/框架/迭代）
  - 增量更新 [[SSO]]（补充 OIDC/SAML/Keycloak 关联连接）
  - 增量更新 [[HermesAgent]]（补充秋芝2046零基础教程来源、辅助模型关联）
  - 更新 [[index.md]] 加入 13 个新条目（4 source + 5 entity + 4 concept）
- **冲突**: 无
- **归档**: raw/01-articles/ 4 个源文件至 raw/09-archive/

## [2026-08-03] lint | 修复全库健康检查问题
- **变更**: 修复 34 处正文死链，注册 2 个未同步索引页，新增 14 个缺失概念/实体页
  - 改写 11 处指向错名页面: [[CentralLibrary]]->[[SkillCentralLibrary]], [[SoftLinkDistribution]]->[[SkillSoftLink]], [[CAS]]->[[CAS协议]], [[知识库-skill-solutions]]->[[knowledge-base-skill-solutions]], [[构建你的第一个Tool-Agent-从零理解ReAct循环]]->[[摘要-构建你的第一个Tool-Agent-从零理解ReAct循环]], [[多Agent协作]]->[[multi-agent-collaboration]], [[multi-agent-orchestration]]->[[multi-agent-collaboration]], [[zero-code-api-configuration]]->[[Dataway]], [[dataql-query-language]]->[[DataQL]]
  - 改写 5 处 [[摘要-又一个神级终端诞生了让-codex-用得更爽]]->[[摘要-kaku-ai-terminal]]（AI终端/JetBrainsMono/Lazygit/WezTerm/Yazi）
  - 新增 concepts: [[UUID]], [[雪花算法]], [[Token估算]], [[重试机制]], [[数据隐私]], [[EventSourcing]], [[spec-merger]], [[wikilink]], [[SSHTunnel]], [[code-first-orchestration]], [[binary-installation]]
  - 新增 entities: [[Node.js]], [[JetBrains]], [[markdown-it]]
  - 注册 2 个未同步页面: [[摘要-推荐5个AI-Agent项目]], [[MattPocock]]
  - 更新 [[index.md]] 共 16 个新条目
- **结果**: 正文死链 34 -> 0，未同步索引 2 -> 0，孤儿页面 0
- **保留**: log.md 中 20 处历史死链按 append-only 原则保留

## [2026-08-03] query | 查询 Agent 工具生成视频方案
- **输出**: 引用 [[Codex]], [[ClaudeCode]], [[Sora]], [[Lovart]], [[摘要-codex必装skill推荐]], [[摘要-codex-97percent-技巧]], [[摘要-最强AI设计智能体Lovart入门教程]]; 即时回答未保存（已询问是否固化 synthesis）

## [2026-08-03] query | 解析 opencode 生成视频的实现路径
- **输出**: 引用 [[OpenCode]], [[HyperFrames]], [[Remotion]], [[Sora]], [[Lovart]], [[摘要-codex必装skill推荐]], [[摘要-codex-97percent-技巧]], [[摘要-最强AI设计智能体Lovart入门教程]], opencode 官方 docs（tools/skills/mcp）; 提出三种途径（Skill 扩展 / bash+Remotion / MCP 接入视频模型），即时回答未保存（待用户确认是否固化 synthesis）

## [2026-08-03] ingest | 固化 synthesis 页面 opencode 生成视频三种途径
- **变更**: 新增 [[opencode-video-generation-paths]]（三途径对比表 + 选型建议）; 更新 [[index.md]] Syntheses 分类; 更新 [[log.md]]

## [2026-08-03] query | 查询 Gemini 2.5 Flash 编码水平
- **输出**: 引用 [[Gemini]], [[摘要-step-3-7-flash-agent横评]], [[Step3Flash]]; 知识库无专门评测，已声明降级并补充网络检索（混合推理/可控 Thinking/LiveCodeBench 超上一代 Flash/Flash Lite 428 tokens/s）; 即时回答未保存（待用户确认是否固化 synthesis）

## [2026-08-03] query | Gradle 与 Maven 的区别及为何不用 Gradle
- **输出**: 引用 [[Maven]], [[摘要-maven]], [[摘要-maven-4-重构]], [[Jenkins]], [[Nexus]]; 知识库无 Gradle 专门条目，Gradle vs Maven 对比基于通用知识回答；即时回答未保存

## [2026-08-05] ingest | 摄入苏三《为什么越来越多人用Nacos？》
- **变更**: 新增 [[摘要-为什么越来越多人用Nacos]]; 新增实体 [[Eureka]]; 新增概念 [[Distro协议]], [[AI Registry]], [[长轮询]]; 增量更新 [[Nacos]]（AP/CP 双模、JRaft、Distro、长轮询、2.0 gRPC 性能、3.0 AI Registry、四中心对比、优缺点、实战接入）; 更新 [[index.md]]; 归档源文件至 raw/09-archive/
- **冲突**: 无（Nacos 原"遵循 AP 原则"描述已被"AP/CP 双模按场景切换"补充细化）

## [2026-08-05] query | 联网复核 Codex 桌面版第三方模型与插件支持现状
- **输出**: 引用 [[codex-desktop-多模型与插件支持现状]], [[Codex]]; 百度/Bing 联网核实用户五条说法：①cc-switch 桌面模型门控 ✅（issue #3922 + 多篇排障文）②API Key 模式插件入口灰色锁定 ✅（知乎问题 + Codex++ 解锁文档）③"不能用 GitHub 插件市场" ⚠️ 不准确（CLI marketplace add 可用，桌面版为配置/目录 bug）④Codex++ 展示模型列表更稳 ✅（CDP 注入机制 + 无需路由）⑤官方订阅基本无问题 ✅（但接不了国产模型）
- **待确认**: Codex++ 仓库名存疑（知识库记 BigPizzaV3/CodexPlusPlus，百度检索见 hkxiaoyao/CodexPlusPlus）；GitHub 本次不可达，issue 编号与 v3.16.5 修复细节未能逐条直连核实
- **输出**: 即时回答未保存（已存在 synthesis 页面，待用户确认是否并入新证据）

## [2026-08-05] query | GitHub 上 oh-my-* 与 kick-* 系列项目命名差异
- **输出**: 知识库无相关页面，降级为通用知识回答（oh-my-* = 全家桶增强配置框架，kick-* = 极简起步模板，如 oh-my-zsh vs kickstart.nvim）；即时回答未保存
- **冲突**: 无

## [2026-08-05] query | GitHub 上 oh-my-* 与 kick-* 系列项目命名差异（固化）
- **输出**: 已保存至 [[oh-my-vs-kick-开源项目命名差异]]（通用知识总结，含核心对比表与一句话记忆）；更新 [[index.md]] Syntheses 分类
- **冲突**: 无

## [2026-08-06] query | 生成 Codex 操作手册并保存
- **输出**: 新增 synthesis [[codex-operation-manual]]; 更新 [[index.md]]（1 synthesis）
- **冲突**: 无

## [2026-08-06] ingest | 归档已摄取源文件
- **变更**: 归档两个已完整摄取的源文件至 raw/09-archive/ — [[摘要-LangChain4j入门指南-苏三]]（源: LangChain4j 入门指南.md）、[[摘要-40分钟学会Codex零基础教程]]（源: 40分钟学会Codex零基础终级教程.md）
- **冲突**: 无
- **备注**: 两文件此前已分别于 2026-08-03、2026-05-19 完成知识摄取（sources/entity/concept 页面已创建，index.md 已注册），本次仅补完步骤6归档操作

## [2026-08-06] sync | 补充苏三对比文章摘要的组合拳实践
- **变更**: [[摘要-codex-vs-claude-code-对比]] 新增"最佳实践(组合拳)"区块,补充 Claude Code 复杂重构 + Codex 批量并行的互补用法,新增双链至 [[摘要-AI-agent工具应该怎么使用]],并标注异步串行接力特性
- **冲突**: 无
- **备注**: 该摘要页已于 2026-06-29 完成 ingest(index.md 已登记,Codex/ClaudeCode entity 已双链),本次为内容完善。另:sources frontmatter 路径仍为 raw/01-articles/,实际文件已归档至 raw/09-archive/,留待后续 lint 统一修正

## [2026-08-06] ingest | 摄入「为什么越来越多人使用 Flowable」工作流引擎文章
- **变更**: 新增 source [[摘要-为什么越来越多人使用Flowable]]; 新增 entities [[Flowable]], [[Activiti]], [[Camunda]], [[jBPM]]; 新增 concepts [[工作流引擎]], [[流程实例]], [[任务服务]], [[运行时服务]], [[嵌入式设计]], [[异步执行器]], [[BPMN 2.0]], [[CMMN]], [[DMN]]; 更新 [[index.md]]（1 source + 4 entities + 9 concepts）
- **冲突**: 无
- **归档**: raw/01-articles/为什么越来越多人使用 Flowable  ？.md → raw/09-archive/

## [2026-08-10] ingest | 摄入《微服务架构设计模式》第三章读书笔记（进程间通信）
- **变更**: 新增 source [[摘要-微服务架构-进程间通信]]; 新增 concepts [[进程间通信]], [[同步RPC]], [[异步消息]], [[服务发现]], [[事务性发件箱]]; 增量更新 [[idempotency]]（补消息幂等两方案）, [[api-compatibility]]（补语义化版本+API优先设计）, [[gRPC]]（补 REST vs gRPC 对比）, [[microservices]]（补通信选型原则）, [[message-queue]]（补三大难题与选型）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/2026-08-06-《微服务架构设计模式》第三章读书笔记：微服务架构中的进程间通信 - LY双土.md → raw/09-archive/

## [2026-08-10] ingest | 摄入 LangChain RAG 构建知识库（理论）
- **变更**: 新增 source [[摘要-langchain-rag构建知识库-理论]]; 新增 concepts [[DocumentLoader]], [[TextSplitter]], [[Embeddings]], [[VectorStore]], [[Retriever]]; 新增 entity [[MinerU]]; 增量更新 [[LangChain]]（补 RAG 组件集）, [[Chroma]]（补集成与 search 类型）, [[Ollama]]（补 OllamaEmbeddings）, [[DashScope]]（补 text-embedding 系列）, [[Qwen]]（补 Qwen3-Embedding）, [[RAG]]（补 LangChain 组件流程段）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md → raw/09-archive/

## [2026-08-10] ingest | 摄入一线大厂的 Git 规范
- **变更**: 新增 source [[摘要-一线大厂Git规范]]; 新增 concepts [[GitFlow]], [[GitHubFlow]], [[TrunkBasedDevelopment]], [[ConventionalCommits]], [[语义化版本]], [[FeatureToggle]]; 新增 entities [[Commitlint]], [[Husky]]; 增量更新 [[Git]]（补分支模型/提交规范/审查门禁）; 增量更新 [[code-review]]（补分支保护/PR模板/审查清单）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/一线大厂的Git规范.md → raw/09-archive/

## [2026-08-10] ingest | 摄入《用好 Agent，先从这4招开始！》
- **变更**: 新增 source [[摘要-用好Agent四招]]; 新增 concept [[Agent四类任务]]; 新增 entity [[DuMate]]; 增量更新 [[秋芝2046]]（补来源与 DuMate 测评）, [[persistent-memory]]（关联 DuMate 长期记忆）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/用好Agent，先从这4招开始！【小白教程】.md → raw/09-archive/

## [2026-08-10] ingest | 摄入 OpenCode 架构演进剖析
- **变更**: 新增 source [[摘要-opencode-架构演进剖析]]; 新增 concept [[渐进式重构]], [[FeatureToggle]]（关联支撑）; 增量更新 [[OpenCode]]（补 2.0 插件 API/Skill/SDK、Desktop v1→v2 演进、MCP 深度集成、兼容迁移策略）; 更新 [[index.md]]
- **冲突**: 无
- **归档**: raw/01-articles/OpenCode架构演进剖析.md → raw/09-archive/
