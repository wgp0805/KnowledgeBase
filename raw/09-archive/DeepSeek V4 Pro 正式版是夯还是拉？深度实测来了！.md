---
title: "DeepSeek V4 Pro 正式版是夯还是拉？深度实测来了！"
source: "https://mp.weixin.qq.com/s/oiXodMMFPrDveUsrEl6GMw"
---
小灰 & 千与千寻 程序员小灰 *2026年8月15日 11:04*

大家好，我是程序员小灰。

最近DeepSeek 又搞大动作了，当模型从"会答题"走向"能干活"，竞争的主战场已经变了。

![图片](assets/DeepSeek%20V4%20Pro%20%E6%AD%A3%E5%BC%8F%E7%89%88%E6%98%AF%E5%A4%AF%E8%BF%98%E6%98%AF%E6%8B%89%EF%BC%9F%E6%B7%B1%E5%BA%A6%E5%AE%9E%E6%B5%8B%E6%9D%A5%E4%BA%86%EF%BC%81/80771171f55bd5f01df0fe9fb64a361b_MD5.webp)

2026 年 8 月 13 日，DeepSeek 悄悄把 V4 Pro 的模型版本号更新成了 0813——正式版来了。

如果只看名字，你可能以为这是一次小修小补。但翻开跑分表会发现：这根本不是同一个模型。

DeepSWE（软件工程智能体基准）从预览版的 12.8 直接飙到 62.7，涨幅接近 390%；CyberGym（网络安全智能体）从 52.7 涨到 83.3，登顶第一；Terminal-Bench 从 72.1 涨到 87.9，和榜首只差 0.1 分。

模型名没变，内核几乎换了一遍。

但与此同时，DeepSeek 也宣布了一个让开发者群体炸锅的消息：8 月 17 日起，API 实行峰谷定价，高峰时段 V4 Pro 输出价格将从 6 元/百万 token 涨到 27 元，涨幅 350%。

## 一、DeepSeek V4 Pro 模型名没变，内核几乎换了一遍

很多人第一次看到"DeepSeek-V4-Pro-0813"这个版本号，会以为是一次常规迭代。但 DeepSeek 自己放出的对比数据显示，这更像是一次"换芯"。

先看最夸张的一组数字：

| 基准测试 | 预览版（4月） | 正式版（0813） | 涨幅 |
| --- | --- | --- | --- |
| DeepSWE（软件工程） | 12.8 | 62.7 | +390% |
| CyberGym（网络安全） | 52.7 | 83.3 | +58% |
| Terminal-Bench 2.1 | 72.1 | 87.9 | +22% |
| DSBench-Hard | — | 翻倍 | — |

DeepSWE 要求模型自主理解代码仓库、定位 bug、写补丁、跑测试；CyberGym 要求模型在模拟网络环境中完成渗透测试；Terminal-Bench 要求模型直接操作终端、执行命令、解决系统问题。

换句话说， **这次升级的核心不是"更聪明"，而是"更能干活"。**

DeepSeek 官方的说法是，变化主要来自后训练（post-training），而不是基座模型重训。这意味着：预训练的知识底座没变，但指令跟随、工具调用、多步推理、错误恢复这些"Agent 能力"被系统性地强化了。

除了 Agent 能力，正式版还补齐了两个之前被诟病的短板：

**图像理解能力。** 预览版的多模态表现不稳定，正式版在视觉推理、图表理解、UI 截图分析等任务上有明显提升。有实测显示，在"根据截图生成 3D 手表实时表盘"这类复杂多模态任务上，V4 Pro 0813 拿到了 7/10 分，是所有模型中的最高分。

**长上下文稳定性。** V4 Pro 支持 100 万 token 上下文，最大输出 38.4 万 token。正式版在长文档检索、整本代码仓库理解、长文本一致性上的表现比预览版更可靠。

但这里要留一个心眼：以上数据主要来自 DeepSeek 官方发布和少量第三方实测。大规模、独立、可复现的第三方评测还需要时间。官方跑分和真实使用体验之间，往往存在落差。

## 二、DeepSeek V4 Pro和 Fable 5、Opus 4.8 比，真实差距在哪？

判断一个模型强不强，不能只看自家跑分。把 V4 Pro 0813 放到当前第一梯队里横向对比，画面更清楚。

| 基准测试 | V4 Pro 0813 | Fable 5 | Opus 4.8 | 排名 |
| --- | --- | --- | --- | --- |
| Terminal-Bench 2.1 | 87.9 | 88.0 | 85.0 | 第二（差0.1） |
| CyberGym（网络安全） | 83.3 | 83.1 | 78.3 | 第一 |
| AutomationBench（自动化） | 31.8 | 29.1 | 27.2 | 第一 |
| DeepSWE（软件工程） | 62.7 | 70.0 | 58.0 | 第二 |
| NL2Repo | 61.5 | — | 仅次于Opus | 第二 |

这张表传递了一个信号： **V4 Pro 没有一项是绝对第一，但也没有一项掉出第一梯队。**

Terminal-Bench 差 Fable 5 0.1 分，基本可以视为统计持平；CyberGym 和 AutomationBench 直接登顶；DeepSWE 落后 Fable 5 但超过 Opus 4.8。

但这里必须做几个边界说明：

**第一，跑分不等于体验。** 基准测试是标准化环境，真实开发场景涉及代码风格、团队规范、遗留系统、调试链路等复杂因素。跑分高的模型，在你的项目里不一定最好用。

**第二，部分数据来自官方。** 上表中 Fable 5 和 Opus 4.8 的对比数据，部分由 DeepSeek 官方发布，第三方独立验证尚不充分。不同评测的版本号、prompt 策略、测试集划分都可能影响结果。

**第三，Agent 能力是新赛道，基准还不成熟。** CyberGym、AutomationBench、DeepSWE 这些评测本身还在快速迭代，分数波动大，不能像 MMLU 那样当作稳定参照。

更稳妥的判断是： **V4 Pro 0813 已经稳稳进入全球第一梯队，在 Agent 和代码场景有局部优势，但和 Fable 5 的综合差距仍然存在，尤其在复杂** **软件工程** **任务上。**

不过，如果把价格因素放进来，画面就完全不一样了。

## 三、DeepSeek V4 Pro 峰谷定价：告别白菜价，还是精明的供需调节？

如果说能力升级是惊喜，那价格调整就是惊吓。

8 月 13 日，DeepSeek 同步宣布：8 月 17 日起，API 实行峰谷定价。这是 DeepSeek 首次引入动态定价机制。

先看 V4 Pro 的具体价格变化：

| 计费项 | 当前价格（8/17前） | 空闲时段 | 高峰时段 | 高峰涨幅 |
| --- | --- | --- | --- | --- |
| 输入-缓存命中 | 0.025元 | 0.15元 | 0.3元 | +1100% |
| 输入-缓存未命中 | 3元 | 4.5元 | 9元 | +200% |
| 输出 | 6元 | 13.5元 | 27元 | +350% |

高峰时段定义为北京时间每天 9:00-12:00 和 14:00-18:00，也就是国内工作日的核心办公时间。其余时间为空闲时段。

这个定价策略很有意思，它不是简单的"涨价"，而是一套供需调节机制：

**用价格** **杠杆** **引导错峰使用。** 高峰时段是国内开发者最集中的调用时间，算力压力最大。DeepSeek 用 2-4 倍的价格差，鼓励对延迟不敏感的任务（批量处理、离线分析、夜间训练）挪到空闲时段。

**缓存命中的价格涨幅最夸张。** 缓存命中输入从 0.025 元涨到 0.3 元（高峰），涨幅 1100%。这看起来离谱，但绝对值仍然很低——0.3 元/百万 token 意味着即使高峰期，缓存命中的成本几乎可以忽略。DeepSeek 可能是在为未来更复杂的缓存策略预留定价空间。

**输出价格是成本大头。** 高峰输出 27 元/百万 token，这个价格已经接近甚至超过部分海外模型的常规定价。对于长输出场景（代码生成、长文写作、Agent 多轮推理），成本会显著上升。

但即使高峰价 27 元/百万 token，和海外第一梯队比仍然便宜。Claude Opus、GPT-5 等模型的输出价格通常在 10-30 美元/百万 token（约 70-220 元人民币），V4 Pro 高峰价仍然是它们的零头。

一个实用建议： **把非紧急的批量任务安排在晚上或周末跑，能省下 60%-70% 的** **API** **费用。**

## 四、DeepSeek V4 Pro实际测评

### 4.1 OpenAI 兼容基础调用

DeepSeek API 兼容 OpenAI SDK，最简单的接入方式是 `              openai.OpenAI(base_url=...)            ` ：

```apache
from openai import OpenAIclient = OpenAI(    api_key="<DEEPSEEK_API_KEY>",    base_url="
            https://openrouter.ai/api/v1"
          ,  # 或 
            https://api.deepseek.com)
          resp = 
            client.chat.completions.create(
              model="deepseek/deepseek-v4-pro-0813",  # OpenRouter ID；官方直连为 deepseek-v4-pro    messages=[        {"role": "system", "content": "你是一个严谨的 Python 后端工程师。"},        {"role": "user", "content": "用 FastAPI 写一个支持分页的 /users 接口。"},    ],    temperature=0.2,    max_tokens=2048,)print(
            resp.choices[
          0].
            message.content)
```

4.2 1M 长上下文对话管理

1M 上下文的实际工程难点不是"塞进去"而是"如何不让早期上下文被稀释"。下面这段展示了摘要回收 + 关键 snippet 注入的混合模式：

```python
class LongContextChat:    """1M 长上下文对话管理：滑动窗口 + 摘要回收 + 关键代码注入。"""    def __init__(self, repo_root: str, max_tokens: int = 900_000):        self.client = client        self.max_tokens = max_tokens        self.files = self._index_repo(repo_root)        # 读取所有源文件        self.summary = ""                                 # 历史摘要        self.key_snippets: list[str] = []                 # 显式关注的代码片段    def _index_repo(self, root: str) -> dict[str, str]:        out = {}        for path in Path(root).rglob("*.py"):            out[str(path)] = 
            path.read_text()
                  return out    def ask(self, question: str, focus_files: list[str] | None = None) -> str:        # 1. 显式注入 focus 文件全文        focus_block = "\n\n".join(            f"=== {p} ===\n{
            self.files[p]}
          " for p in (focus_files or [])        )        # 2. 历史摘要 + 当前问题        msgs = [            {"role": "system", "content": f"前情摘要：{
            self.summary}
          "},            {"role": "user", "content": f"{focus_block}\n\n---\n\n{question}"},        ]        # 3. 用 Think High 跑        resp = self.
            client.chat.completions.create(
                      model="deepseek/deepseek-v4-pro-0813",            messages=msgs,            reasoning_effort="medium",            max_tokens=4096,        )        answer = 
            resp.choices[
          0].
            message.content
                  # 4. 把本轮压缩成摘要回收        self.summary = self._summarize(self.summary, question, answer)        return answer    def _summarize(self, prev: str, q: str, a: str) -> str:        # 用 Non-think 做一次摘要回收，避免长期上下文爆炸        ...
```

4.3 两大模型的效果对比

DeepSeek V4 Pro 的实际生成效果怎么样呢？

我们以一个2D小游戏为例，看一看 DeepSeek V4 Pro 模型与豆包的 Doubao-Seed 模型，谁的效果更好一些。

我们使用同一组提示词进行测试验证：

```
生成一个可直接浏览器打开独立HTML单文件2D小游戏，使用原生Canvas+JavaScript，不引入外部资源。游戏类型：太空躲避弹幕游戏核心玩法：1. 玩家操控飞船，方向键上下左右移动，空格键发射子弹2. 自动生成敌方陨石与敌机，敌机可以主动向玩家靠近3. 碰撞判定：子弹击中敌机销毁敌机；玩家碰到陨石/敌机游戏结束4. 计分系统：击毁敌机获得分数，实时显示分数5. 游戏机制：开始界面、游戏进行界面、死亡结束界面，支持回车重新开始硬性代码规范：1. 完整游戏主循环、边界限制、对象池优化、碰撞检测、定时器兜底，处理所有边界异常，不能出现逻辑BUG2. 代码分层清晰，变量命名规范，关键逻辑添加中文注释3. 增加视觉表现：粒子爆炸特效、飞船尾焰、平滑移动缓动、渐变背景、光影层次感4. UI美化：精致文字样式、半透明面板、颜色搭配协调，提升交互观感5. 保证运行流畅，做好帧率兼容，支持PC端操作输出要求：直接输出完整HTML全部代码，不要额外文字说明，代码复制即可运行。
```

DeepSeek V4 Pro生成效果:

![图片](assets/DeepSeek%20V4%20Pro%20%E6%AD%A3%E5%BC%8F%E7%89%88%E6%98%AF%E5%A4%AF%E8%BF%98%E6%98%AF%E6%8B%89%EF%BC%9F%E6%B7%B1%E5%BA%A6%E5%AE%9E%E6%B5%8B%E6%9D%A5%E4%BA%86%EF%BC%81/5ce28b56b76b874d7d49498f58eacef0_MD5.gif)

Doubao-Seed生成效果：

![图片](assets/DeepSeek%20V4%20Pro%20%E6%AD%A3%E5%BC%8F%E7%89%88%E6%98%AF%E5%A4%AF%E8%BF%98%E6%98%AF%E6%8B%89%EF%BC%9F%E6%B7%B1%E5%BA%A6%E5%AE%9E%E6%B5%8B%E6%9D%A5%E4%BA%86%EF%BC%81/dc27c888ab5ca65466715ee56d76dc28_MD5.gif)

## 大家觉得哪一个模型的生成效果更好？

## 五、谁该用DeepSeek V4 Pro，怎么用？

最后给一个可操作的判断框架。

**优先选择 V4** **Pro** **的场景：**

1\. 代码开发和 Code Review：LiveCodeBench 93.5、Codeforces ELO 3206，代码能力是第一梯队，价格比海外模型低很多。

2\. Agent 工作流和自动化任务：CyberGym、AutomationBench 登顶，Terminal-Bench 接近第一，适合做终端操作、自动化脚本、DevOps 助手。

3\. 长文档处理和代码仓库分析：100 万 token 上下文 + 38.4 万最大输出，整本技术文档、整个代码仓库可以直接塞进去。

4\. 网络安全和渗透测试：CyberGym 83.3 全球第一，安全研究场景有明确优势。

5\. 成本敏感的中等复杂度任务：如果任务不需要最顶级的推理能力，但调用量大，V4 Pro 的性价比仍然突出。

对行业来说，一个能力追平海外第一梯队、价格仍然显著更低的模型，会持续压缩整个市场的定价空间。这对用户是好事，对所有玩家都是压力。

好了，关于 DeepSeek V4 Pro 的实测，小灰就给大家分享到这里。

正在读这篇文章的朋友，你有尝试过 DeepSeek V4 Pro 吗？有什么样的感受？欢迎在评论区聊聊。

我是程序员小灰，我会持续为大家分享最新的AI工具和AI玩法。如果想第一时间收到推送，也可以给我个星标⭐我们下次再见~~