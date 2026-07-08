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

## [2026-07-06] query | 对比 ReAct 与 Plan-and-Execute 的区别
- **输出**: 即时回答 + 已保存为 [[react-vs-plan-execute]]
- **引用**: [[ReAct_Agent]], [[Research-Plan-Execute-Review-Ship]], [[Agent]], [[AICoding]], [[VibeEngineering]], [[claude-code-best-practice]]

# Wiki 操作日志

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

## [2026-07-08] query | 解析 IntelliJ IDEA 中 AI agents 选项的 Junie
- **输出**: 即时回答未保存（本地知识库无 Junie 条目，引用 JetBrains/junie GitHub 仓库与 IDEA 2026.1 官方文档）

## [2026-07-08] query | 追问 Junie 是否支持国产模型 API
- **输出**: 即时回答未保存（引用 JetBrains/junie registry-staging.json ACP 注册表与 README BYOK 说明）
