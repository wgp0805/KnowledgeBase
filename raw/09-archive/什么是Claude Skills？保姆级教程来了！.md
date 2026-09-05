---
title: "什么是Claude Skills？保姆级教程来了！"
source: "https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653262911&idx=1&sn=3e4b44b92f4ff03140faf4214816c7ef&scene=21&poc_token=HDrWOWqjWKFOscZt4xeDQZarJleZuSwscbDLe5pk"
---
小灰&Smith 程序员小灰 *2026年4月2日 13:05*

大家好，我是程序员小灰。

最近一段时间，AI圈子兴起一股养虾热潮，就连菜市场的大爷大妈都在谈论“养小龙虾”的经验。

然而，有一项了不起的AI技术却被OpenClaw的光芒所掩盖，这项技术就是Claude Skills。

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/009fd5bebca05054058ada9549c438f6_MD5.webp)

今天，我们就来为大家全面讲解Claude Skills的概念、原理、用法与实战。文章较长，建议先收藏、不迷路。

一、什么是Skills？它能干什么？

Anthropic 官方在 2025 年 10 月 16 日正式发布了 Claude Skills 功能，Skills 从此横空出世。截止到2026年4月社区贡献突破上万个skill。

## 1\. Skills 是什么？

Skills 是可复用的说明、知识、工作流，通常包含一个 `SKILL.md` 以及可运行脚本、资源文件。

## 2\. Skills 的应用场景是什么？

Skills的应用场景非常广泛，主要集中在需要特定工作流或者外部工具写协作的地方。

**场景1：自动化工作流**

自媒体人员可以创建一个自动化的文章热点采集、编写和发布的工作流skill，提高发文效率。

**场景** **2** **：文档与资源处理**

Skills可以让Claude Code获得处理Excel、PDF、PPT的能力，例如，document-skills 允许 Claude 直接从复杂的 PDF 表单中提取字段并填入数据库。

**场景** **3** **：统一团队编码规范**

开发团队在写代码时，需要特定的架构设计或代码审查编码规范，来约束团队成员产出的代码，在新的成员加入时，直接安装skill到本地就可以了。比如BMAD方案就有很多代码质量管理的skill。

**场景** **4** **：实时数据获取与检索**

大模型很聪明，但是不能获取外部实时信息就不能做出最佳决策。比如用户查询今天要去哪里旅游，ai可以先查天气看看适合出门。

企业内部有私有数据库，可以实现数据库的skill来帮助企业设计产品和决策。

**3\. Skills** **解决了什么问题？**

Skills 的出现解决了 AI Agent 在实际落地中的几个痛点：

**痛点** **1** **：上下文窗口的** **“** **瘦身** **”** **与效率提升**

之前调用外部工具时，需要把所有规则一次性放入提示词，浪费了很多Token。Skills采用渐进式披露机制，启动时只加载skill介绍了解skill是做什么的信息，当要调用时才加载全部SKILL.md内容。

痛点 **2** **：知识的** **“** **资产化** **”** **与可复用性**

之前用提示词的方式，需要自己解决保存和分发问题，管理也比较混乱，现在设计分发安装skill等流程规范化了，我们可以方便使用skill分享知识。

**痛点** **3** **：从** **“** **通用对话** **”** **向** **“** **专业执行** **”** **的跨越**

**大模型之前只有通用知识，到了垂直领域就变成了小白，通过安装skill能让大模型马上变成专家。**

**痛点** **4** **：灵活的权限与调用控制**

**通过修改Claude Code **权限控制列表，可以精确控制skill的调用和触发方式，以及允许skill调用哪些工具。****

## 4\. Skills 的组成

### 标准 Skills 文件夹结构是下面这样子：

```perl
my-skill/├── SKILL.md          # 核心描述文件（必须）├── scripts/          # 可执行脚本（可选）├── template.md       # Claude 要填写的模板└── examples/         # 示例输出（可选）
```

### 其中SKILL.md 是Skills的核心文件，该文件包含了YAML 的若干前置元数据，比如：

• `name`

Skills的唯一标识符，用于配置和调用。

注意：只能用小写字母、数字、连字符，不要用空格或特殊字符

• `description`

最关键的字段，AI靠这个判断何时触发你的Skills 写法，明确功能 + 触发关键词。

还有其他的元数据version、displayName、requires等，因为不是必须选项，就不一一展开了。

**SKILL.md的正文** 可以包含以下内容：

• 执行流程

• 质量约束

• 前置条件/配置

• 具体使用示例

• 参数说明表

• 注意事项/限制

• 错误与边界处理

### 这里我们示范一个标准的SKILL.md 写法：

```markdown
---name: kua_kua_skilldescription: 当用户说“夸夸”时，使用 echo 工具夸奖用户。---
# 夸夸 Skill只要我提到“夸夸”这两个字，你就必须回复：“你比爱因斯坦还聪明！”不要说别的废话，直接夸就行。
```

## 二、快速上手：5 分钟体验 Skills

1\. 打开Claude

2\. 和它对话：

```js
帮我创建一个skill，当我说夸夸时，你就回复“你比爱因斯坦还聪明”
```

3.提示创建成功：

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/a516929814c2f0696bebd98839f3ce7b_MD5.png)

4 我们测试一下skill是否生效

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/c0c4cb33ec1711eed48451938e698d56_MD5.png)

结果很完美，恭喜你，你成功创建了第一个skill。

## 三、Skills 的核心原理

## 完成了第一个Skills的创建，接下来我们了解一下Skills与整个Claude Code生态中各个组件之间的关系。

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/9802c70efa9b45f866aa9321f7659243_MD5.png)

1\. Agent 与 Skills：大脑与双手的关系

Agent（智能体） 是具备自主规划、决策和执行能力的“大脑”。而 Skills（技能） 是 Agent 用来改变外部状态的具体“工具”。

包容关系：一个 Agent 通常拥有多个 Skills。

2\. Command 与 Skills：直接触发与底层能力的关系

Command（命令）是一种确定性的、由人类或系统主动发起的指令（例如Claude code 里的 /help ）。

触发关系：Command 是唤醒 Skills 的一种最直接的方式。当你输入一条 Command 时，系统不需要经过复杂的思考（不需要 Agent），直接去执行对应的 Skills。

我们在开发完skill后，可以配置skill，把skill封装为一种命令

3 Hook 与 Skills：事件驱动与被动响应的关系

Hook（钩子） 是一种事件监听机制。它允许系统在特定的“事件”发生时，自动拦截并执行一段代码（例如 Webhook、Git pre-commit hook）。

联动关系：如果说 Command 是“人主动去按开关”，那么 Hook 就是“系统自动感应”。Hook 本身不处理复杂业务，它的核心作用是在特定时机触发一个 skill。

## 四、安装与配置完全指南

1\. 命令行安装

我们一般可以通过npx skills 这个工具安装 Skills （项目目录https://github.com/vercel-labs/skills），安装命令：

```cs
npx skills add <skill链接>
```

我们来演示一下：

```cs
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/bc9a62fa2a01608b9a75b78bc526218d_MD5.png)

注意：必须要有网络工具，不然访问不了仓库就安装失败了。

2\. 复制安装

复制下载的skills文件夹，到全局skills目录或者项目skills目录安装：

```bash
全局skills目录 ~/.claude/skills/项目skills目录 .claude/skills/
```

## 五、必装 skill 推荐（按场景分类）

## 看到这里，相信大家对Skills的概念和使用都有了一定的了解，接下来我们为大家推荐一系列常用的skill。

## 1\. 通用skill

• **查找s **kill的 skill：****

```cs
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

**创建 skill 的 skill**

```cs
npx skills add https://github.com/anthropics/skills --skill skill-creator
```

## 2\. 产品开发类skill

• **产品需求头脑风暴规划**

```cs
npx skills add https://github.com/obra/superpowers --skill brainstorming
```

• **前端开发 React 编码规范 skill**

```cs
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
```

• **前端开发 UI/UX 美化**

```cs
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max
```

• **浏览器自动化 skill**

```cs
npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
```

## 3\. 职场办公类skill

• **办公文档相关 skill (PDF/XLSX/DOCX/PPTX)**

```cs
npx skills add https://github.com/anthropics/skills --skill pdfnpx skills add https://github.com/anthropics/skills --skill xlsxnpx skills add https://github.com/anthropics/skills --skill docxnpx skills add https://github.com/anthropics/skills --skill pptx
```

## 4\. 优质 Skills 资源仓库

Anthropic 官方 Skills 仓库：

```javascript
https://github.com/anthropics/skills
```

Vercel Lab 出品的 skill 排行榜：

```javascript
https://skills.sh
```

## 六、Skills进阶教程

## 在这一部分，我们介绍一些Skills相关的进阶内容，包括Skill的底层工作原理，以及Skill编写的额外技巧。

## 1\. Skill的工作原理解析

## Skill是Claude Code的核心扩展能力之一，他采用渐进式披露的设计，平时只要知道skill会什么，在真正调用时才去加载具体的使用手册内容及执行脚本。

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/df1057a017efcb4ca7f7c63e1fa01cd0_MD5.png)

## Skill采用3级渐进披露设计，平衡了能力扩展和上下文成本的问题，我们通过下方的表格，来看看这3级分别是什么：

| 加载级别 | 触发时机 | 消耗成本 | 加载内容 |
| --- | --- | --- | --- |
| 第一级：元数据 | 启动时 | 约 100 Tokens | YAML 前置内容中的 name 和 description |
| 第二级：指令 | 匹配/调用时 | 约 1k~5k Tokens | SKILL.md 的主体说明、SOP 流程、最佳实践 |
| 第三级：资源 | 被引用时 | 动态 | 脚本执行输出、额外的 Markdown 参考文档、API 规范 |

2\. Skill编写的额外技巧

技巧1：控制SKILL.md的内容，尽量控制在500行以内。

技巧2：按需价值外部资源，如果你的skill包含复杂的子任务，把子任务内容描述拆分到 `references目录中。`

技巧3：把通用的脚本放scripts里面。

技巧4：明确写出skill的触发条件，能力和边界。

技巧5：做防御性的设计，如果出错要怎么处理。

如果你觉得自己写skill太麻烦了，要考虑的东西那么多，大家可以使用创建skill的skill(skill-creator)去创建。

skill-creator已经包含了最佳实践的知识（使用下面命令安装npx skills add https://github.com/anthropics/skills --skill skill-creator）。

温馨提示：我们不要什么东西都写成skill，最好把重复3次以上的任务做成skill。

## 七、Skills的安全问题

Skills虽然很强大，但我们在使用和编写skill时，一定要考虑充分到风险，不然可能会造成重要信息泄露及丢失。

1\. 只从可信的安装源安装skill。

2\. 如果必须从不可信的安装源安装skill，必须要做必要的审查，可以把

3\. skill安装在隔离环境，不要让他接触到你的重要数据

4\. 不要给skill超过任务所需的权限。

5\. 在编写skill时，不要在skill中明文暴露出apikey和密码等信息，尽量引用环境变量。

好了，关于Claude Skills的概念、原理与应用，我们就介绍到这里。本文的篇幅有些长，大致内容总结到了这幅图中：

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/376ad390e88174260ed4fa319b60ec6f_MD5.jpg)

如果觉得这篇文章对你有所帮助，欢迎点赞、关注和转发。在2026年，希望我们都能抓住AI时代的红利！

**< END >**

**

最近小灰创建了一个AI副业交流群，对AI和副业变现感兴趣的朋友，都欢迎进群交流。扫码添加小灰微信，备注“ai“即可进群：

![图片](assets/%E4%BB%80%E4%B9%88%E6%98%AFClaude%20Skills%EF%BC%9F%E4%BF%9D%E5%A7%86%E7%BA%A7%E6%95%99%E7%A8%8B%E6%9D%A5%E4%BA%86%EF%BC%81/0831b9d142c9d3f2abc6443423d2758a_MD5.webp)**

继续滑动看下一个

程序员小灰

向上滑动看下一个