---
title: "Loop Engineering 实战指南"
source: "https://mp.weixin.qq.com/s/BL5T_i79EY86fAJa5srOKA"
---
苏三说技术 *2026年7月5日 09:20*

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 一、Loop 落地靠三份 Markdown

把循环跑起来，你需要三份 Markdown 文件。不多不少：

| 文件 | 干什么的 | 谁来维护 |
| --- | --- | --- |
| **[AGENTS.md](http://agents.md/) / [CLAUDE.md](http://claude.md/)** | 循环的"宪法"——告诉 Agent 你的项目规则、安全边界、跑什么命令 | 你写完就稳定，除非项目规范变了 |
| **[STATE.md](http://state.md/)** | 循环的"记忆"——记住上次跑到了哪、发现了什么、下一步要干什么 | 循环每次跑完自动更新 |
| **[SKILL.md](http://skill.md/)** | 循环的"技能卡"——封装一个具体能力（分诊/修复/验证），Agent 按需加载 | 你写一次，循环反复调用 |

这三份 Markdown 的分工是： **[AGENTS.md](http://agents.md/) 约束循环的边界， [SKILL.md](http://skill.md/) 定义循环的能力， [STATE.md](http://state.md/) 记录循环的进度** 。

下面挨个说怎么写。

## 二、 AGENTS.md / CLAUDE.md ：循环的宪法

这是循环的顶层配置文件。Agent 每次启动第一件事就是读它。它定的规则循环必须遵守。

### Claude Code 写法

项目根目录放`.claude/             CLAUDE.md           ` ：

```
markdown# 
            CLAUDE.md
           — 项目循环配置

## 循环模式

- 初始阶段：L1 报告模式（只汇报，不改代码）
- 读完 
            STATE.md
           再开始分诊
- 每次跑完更新 
            STATE.md
          

## 安全规则

- 不自动合并代码，不经人工审批不能推送
- 禁止修改 .env、auth/、payments/、credentials/
- 每次改代码必须用 git worktree 隔离
- 同一个问题最多尝试 3 次，超限升级给人

## 验证要求

- 任何代码改动必须由独立的验证者子 Agent 检查
- 必须跑项目测试，不能只看代码
- 验证结果写回 
            STATE.md
```

### OpenAI Codex 写法

项目根目录放`.codex/             AGENTS.md           ` ：

```
markdown# 
            AGENTS.md
           — 循环配置

## 分诊规则

- 每天早 9 点跑 triage
- 只扫描过去 24 小时的 CI 失败和 Issue
- 产出写入 
            STATE.md
          
- 前两周报告模式，不自动修复

## 工作树规则

- 每次代码实验开独立工作树
- 实验完丢弃工作树，不污染主工作区

## 费用上限

- 每天 token 上限 100k
- 超过 80% 自动切为报告模式
- 超过 100% 直接跳过本次运行
```

### 关键：这几个字段必须写清楚

| 字段 | 为什么重要 |
| --- | --- |
| `循环模式` | L1/L2/L3 决定循环能动到什么程度，不写默认是不动 |
| `安全规则` | 不写的话循环可能改不该改的文件 |
| `验证要求` | 独立验证者是循环不出大错的核心保障 |
| `             STATE.md            更新规则` | 不写怎么更新的话，循环每次都是白跑 |

## 三、 STATE.md ：循环的记忆

循环为什么不是一次性的？因为 [STATE.md](http://state.md/) 记住了进度。

#### 模板（可直接复制到项目根目录）

```
markdown# Loop State — {{你的项目名}}

上次运行: (每次循环自动更新)

## 高优先级（循环正在处理或等人决策）

<!-- 格式:
- [ ] ID — 一句话描述
  循环操作: 上次做了什么
  人工决策: (如果有)
-->

## 观察列表

<!-- 暂时不动但持续关注 -->

## 本次忽略的噪音

<!-- 持续出现噪音说明需要调整分诊规则 -->

---
运行记录: (时间戳) | 发现 N 项 | 处理 N 项 | 升级 N 项
```

#### 循环对 STATE.md 的操作规则

写 [SKILL.md](http://skill.md/) 时必须告诉 Agent：

1. **更新 `上次运行` 时间戳**
	— 每次运行必须写
2. **追加新发现**
	— 高优先级和观察项分别追加
3. **清理已完成项**
	— 关掉的 Issue、合并的 PR 从高优先级清理掉
4. **记录噪音**
	— 分诊判断错误、重复出现的项目记到"噪音"区，用于调优
5. **不要覆盖，只追加**
	— 以前的内容是历史，追加才能看出趋势

## 四、 SKILL.md ：循环的能力单元

[SKILL.md](http://skill.md/) 是关键。一个循环依赖多个 Skill 来完成任务。标准结构：

```
skills/loop-triage/
            SKILL.md
               # 分诊
skills/minimal-fix/
            SKILL.md
               # 小修小补
skills/loop-verifier/
            SKILL.md
             # 独立验证
skills/loop-budget/
            SKILL.md
               # 费用控制
```

### SKILL.md 标准格式

每个 [SKILL.md](http://skill.md/) 有一个 YAML frontmatter 和一个 Markdown 正文。Agent 按"渐进式披露"加载：

- **Level 1（100 tokens）**
	：只加载 YAML 里的 `name` + `description` ，决定需不需要这个 Skill
- **Level 2（完整 body）**
	：确定需要后，加载完整正文

#### 所以 description 决定了你的 Skill 能不能被触发

大多数人 Skill 不触发的原因就是这个。description 写得太模糊，Agent 不知道什么时候该用它。

**写得好的 description：**

```
yaml---
name: loop-triage
description: >
  分诊最近 24 小时的 CI 失败、Issue 和提交。
  产出结构化的优先级报告供循环消费。
  将输出写入 
            STATE.md。
          
user_invocable: true
---
```

**写得差的 description：**

```
yaml---
name: triage
description: 帮助分析项目状态
---
```

第二个不会触发的——Agent 什么时候会主动调用"分析项目状态"？永远不会。

### 分诊 Skill（必装，所有循环的起点）

```
markdown---
name: loop-triage
description: >
  分诊最近 CI 失败、Issue 和提交，产出优先级报告写入 
            STATE.md。
          
  供循环消费。
user_invocable: true
---

# Loop Triage Skill

你是分诊 Agent。产出结构化的优先级列表。

## 输入（循环会提供）
- 最近 24 小时 CI/测试失败
- 负责人名下的 Open Issue
- 最近 24-48 小时 main 分支提交
- 当前 
            STATE.md
          

## 输出格式

### 1. 高优先级（立即处理）
- 一句话描述
- 为什么重要（影响/风险）
- 建议循环下一步操作
- 预估工作量

### 2. 观察项（监控但不处理）
- 同上格式，但优先级低

### 3. 噪音/忽略
- 看了但不值得处理的

### 4. 状态更新
- 循环下次需要记住的事实

## 规则

- 只有工程师今天会关心的才放"高优先级"
- 不确定的放"观察"或"噪音"，不要制造工作
- 分诊只做信号，不做架构设计
```

### 最小修复 Skill（L2+ 使用）

```
markdown---
name: minimal-fix
description: >
  对指定问题产出最小代码改动。
  不改无关代码，不重构。
user_invocable: true
---

# Minimal Fix Skill

你只修**一个特定问题**，用**最小的 diff**。

## 输入
- 失败信息、评审意见或问题描述
- 相关文件（如果有）
- 项目构建/测试命令
- 禁止修改的路径列表

## 流程
1. 确认问题根因
2. 只改必须改的，不顺便重构
3. 跑相关测试
4. 输出：改了什么、为什么、跑了什么命令

## 输出格式
\`\`\`markdown
## 修复方案
### 目标
(一句话)
### Diff 摘要
(文件 + 改动)
### 验证结果
(命令 + 输出)
### 需要人工审查?
(是/否 + 原因)
```
```
### 独立验证 Skill（L2+ 必须）

\`\`\`markdown
---
name: loop-verifier
description: >
  独立验证循环产出的代码改动。
  找理由拒绝而不是接受。跑测试。
  永远和实现者不同角色。
user_invocable: true
---

# Loop Verifier Skill

你是**检查者**。你的工作是**拒绝**，除非证据充分。

## 检查清单（全部通过才 APPROVE）

1. **范围**：只改了相关文件，没碰禁用路径
2. **意图**：改动确实解决了声明的问题
3. **测试**：跑了测试，报告通过/失败及输出
4. **不作弊**：没有跳过测试、注释断言
5. **风险**：中高风险的即使测试通过也建议人工审查

## 输出

\`\`\`markdown
## 结果: APPROVE | REJECT | ESCALATE_HUMAN
### 证据
- 测试: (命令 + 结果)
- 范围检查: (通过/失败 + 说明)
### 如果拒绝
- 原因: (编号 + 具体)
- 建议下步操作
```
```
## 五、提示词怎么写：/loop 和 /goal

有了上面的 Markdown 文件，接下来是**用什么提示词把它们串起来**。

### 启动循环

这是最核心的提示词——/loop。写法决定了循环干什么、怎么干。

**L1 报告模式（只汇报不动手）：**

\`\`\`bash
/loop 1d 跑 loop-triage Skill。先读 
            STATE.md。把高优先级项追加到
           
            STATE.md。只报告，不修代码。
```

**L2 分诊+小修（自动修复简单问题）：**

```
bash/loop 1d 跑 loop-triage Skill。高优先级中小修小补的：开工作树 → 跑 minimal-fix → 跑 loop-verifier → 验证通过的开 PR。中高风险升级给人。更新 
            STATE.md。
```

**L3 近乎无人值守（限制多的时候用）：**

```
bash/loop 2h 跑 loop-triage。可自动修复标了 quick-win 标签的问题。其他按优先级排序。依赖升级只修低风险 CVE。合代码前必须人工 approve。每天 token 上限 100k。
```

### /goal — 让循环自己判断什么时候完成

/goal 是一个目标，循环持续跑直到条件满足。

**关键词** ：循环自己判断完成的不是写代码的那个模型，是独立的验证模型。

```
bash# 持续跑直到测试全绿
/goal "test/ 目录下所有测试通过，lint 干净"

# 持续跑直到完成重构
/goal "计费模块全部迁移到新 API，旧 API 零调用"

# 持续跑直到文档写完
/goal "
            README.md
           覆盖所有 API 端点，每个端点含示例代码"
```

/goal 比 /loop 更适合持续型任务。写 Markdown 时的规则：

1. **目标客观可验证**
	：不要说"界面更好看"，要说"测试通过、lint 干净"
2. **限定范围**
	：指定目录或文件范围，避免 Agent 发散
3. **不要写方法**
	：告诉它"做到什么"，不要告诉它"怎么做"

### 分诊 Skill 调用提示词

当你在 [SKILL.md](http://skill.md/) 里写了 `user_invocable: true` ，循环里可以直接引用它：

```
bash/loop 1d 调用 $loop-triage。高优先级项，如果适合直接修复则调用 $minimal-fix。修复后调用 $loop-verifier 验证。所有结果写回 
            STATE.md。
```

`$` 前缀告诉 Agent 去加载对应的 [SKILL.md](http://skill.md/) 并使用其中的规则。

## 六、 LOOP.md ：循环自己的配置文件

除了 [AGENTS.md、STATE.md、SKILL.md，还可以加一份](http://agents.xn--mdstate-zo3f.xn--mdskill-zo3f.xn--md,-s18dy4bfe94ysyc130s/) [LOOP.md](http://loop.md/) 来描述循环本身怎么跑。

```
markdown# Loop 配置

## 活跃循环

| 模式 | 频率 | 阶段 | 触发命令 |
|------|------|------|---------|
| 每日分诊 | 1d | L1 报告模式 | /loop 1d |
| PR 保姆 | 手动 | L2 | /loop run pr-babysitter |

## 人工关口

- L2 之前不做自动修复
- 安全/支付/基础设施路径必须人工审查
- 自动合并仅限低风险依赖更新

## 预算

- 每日分诊上限 100k tokens
- PR 保姆每次上限 200k tokens
- 每个子 Agent 最多产生 2 个
- 预算耗尽切为报告模式

## 关闭开关

- 给项目打 \`loop-pause-all\` 标签 → 暂停所有调度
- 给项目打 \`loop-resume\` 标签 → 恢复调度
```

## 七、从零开始，搭一个最简单的循环

**第 1 步** ：把 [STATE.md](http://state.md/) 模板复制到项目根目录 **第 2 步** ：在`.claude/             CLAUDE.md           ` （或`.codex/             AGENTS.md           ` ）写下项目规则和安全边界 **第 3 步** ：把 loop-triage 的 [SKILL.md](http://skill.md/) 放到`.claude/skills/loop-triage/             SKILL.md           ` **第 4 步** ：在 Claude Code 里跑：

```
bash/loop 1d Call $loop-triage. Read 
            STATE.md
           first. Append findings. Report only, no fixes.
```

**第 5 周** ：读一周的 [STATE.md，调优分诊规则](http://state.xn--md,-sy9d07kjd4746bnnduoa/) **第 2 周** ：加上 minimal-fix + loop-verifier 的 [SKILL.md，开始自动修小问题](http://skill.xn--md,-8n0er8jgtoc3d9rhnx5gd3ybmeg/)

```
bash/loop 1d Call $loop-triage. For high-priority items that look like small bugfixes: open worktree → $minimal-fix → $loop-verifier → on approve, open PR. Update 
            STATE.md.
```

**到这就够了** 。大部分人走到 L2 就已经大大超过了手动提示的效率。L3（无人值守）需要你充分信任循环的判断力，这通常需要几周甚至几个月来建立。

---

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](assets/Loop%20Engineering%20%E5%AE%9E%E6%88%98%E6%8C%87%E5%8D%97/120fc0032d790118e773ec1a67b88378_MD5.webp)