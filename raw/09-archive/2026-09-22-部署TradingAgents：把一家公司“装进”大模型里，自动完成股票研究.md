---
title: "部署TradingAgents：把一家公司“装进”大模型里，自动完成股票研究"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6468328.html"
date: "Tue, 22 Sep 2026 10:47:21 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 部署TradingAgents：把一家公司“装进”大模型里，自动完成股票研究

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6468328.html  
> **抓取日期**: 2026-09-22  
> **相关性评分**: 1.0

> TradingAgents把真实机构的研究、讨论与风控流程拆成可协作的角色：基本面、技术、新闻与情绪分析师各自处理数据，多空研究员辩论，交易员形成计划，风控与组合经理审核。项目在GitHub已获超10.8万Star，四条命令即可启动。

![](https://image.woshipm.com/2023/04/13/83f37532-d9e0-11ed-9d2f-00163e0b5ff3.jpg)

今天和大家分享一个股票研究类的开源项目：**TradingAgents** 。

它是一个面向金融研究的**多智能体开源框架** 。它尝试把真实交易机构中的研究、讨论和风控流程，组织成一套可以由大模型协作完成的工作流。

目前，项目在 GitHub 上已经获得超过**10.8 万 Star** ，并持续迭代。它更适合用来研究**多智能体如何参与金融分析** ，也可以作为个人投资研究和量化实验的工具。

![图片](https://image.woshipm.com/wp-files/sha256/cf/9d/cf9dc1ac495df5a9516cd1cfbdf4c4f82480ba126f3d09545d347b99cf503440.png)

## 01 它如何组织一次分析

![图片](https://image.woshipm.com/wp-files/sha256/13/ff/13ff3962a27fe091a7e8ce1c135e4ad0e334e2a981e3d87de82f47d8c754c9f8.png)

TradingAgents 基于LangGraph 构建，将股票研究拆分为几类角色。

**分析师团队负责处理不同类型的数据** 。基本面分析师关注公司财务和经营状况，技术分析师分析价格、成交量以及 RSI、MACD 等指标，新闻分析师跟踪公司新闻和宏观事件，情绪分析师则整理 Reddit、StockTwits 等社区中的市场情绪。

研究员团队会进一步审查这些分析。多头研究员寻找上涨逻辑，空头研究员检查估值、行业环境和潜在风险。双方经过讨论后，交易员负责形成交易计划，**风险管理团队评估波动率、流动性和组合风险** ，最后由组合经理审核交易方案。

整个流程可以概括为：

![图片](https://image.woshipm.com/wp-files/sha256/e8/49/e849cfb35e19946798a8de40a7d6a5a531461100d795e4f713881f9419a82a9d.png)

## 02 和普通提问有什么不同

直接问大模型**某只股票该不该买** ，通常只能得到一次性的回答。回答看起来完整，但**分析过程可能缺少数据验证** ，结论也容易受到模型偏好和提示词的影响。

  * 直接提问：单次回答，缺少数据验证
  * TradingAgents：分工分析 + 多空交叉审查



TradingAgents 则采用了另一种思路：让不同智能体分别负责不同问题，再通过多空研究员的讨论，**对前面的分析进行交叉审查** 。

例如，基本面分析师可能认为公司长期价值较好，技术分析师却发现短期趋势转弱；新闻分析师看到行业政策变化后，风险管理团队还会进一步评估这种变化对仓位和波动率的影响。

**这种架构并不能保证结论正确** ，但可以让研究过程更加结构化，也便于发现分析中的遗漏。

项目还支持决策日志和回测功能。系统可以记录过去的分析结果，并在后续运行时参考相同股票的历史决策和实际表现。

> **注意**
> 
> 日志机制可以帮助复盘，**却不能自动形成一套稳定盈利的交易策略** 。

![图片](https://image.woshipm.com/wp-files/sha256/0a/9e/0a9e0496ba5d914370cbadd7de68102ee2d2eb4702f6de417e9deb31a7b4e66b.png)

## 03 如何部署它

下面以 Windows Subsystem for Linux，也就是WSL，加 Docker 的方式进行部署。

### STEP 1 克隆项目

> git clone https://github.com/TauricResearch/TradingAgents.git
> 
> cd TradingAgents

![图片](https://image.woshipm.com/wp-files/sha256/ff/49/ff4960de7e24950cfc3b9ebeeb5f94f65771027f96fc0e73bfff51ddb28c4647.png)

### STEP 2 配置环境变量

复制项目提供的环境变量模板：

> cp .env.example .env
> 
> nano .env

项目支持多家模型服务商，包括 OpenAI、Google、Anthropic、DeepSeek、Qwen、GLM、Ollama 等，**以及其他兼容 OpenAI API 格式的服务** 。

根据自己使用的模型服务商，在.env 文件中填写对应的 API Key。

![图片](https://image.woshipm.com/wp-files/sha256/9e/76/9e76082056899f29c42dc135a667fe0f7a6b17398c48800dc99839f40ae75ebb.png)

如果使用的模型服务商没有出现在模板中，也可以通过OpenAI 兼容接口接入：

> TRADINGAGENTS_LLM_BACKEND_URL=https://你的提供商地址/v1
> 
> OPENAI_COMPATIBLE_API_KEY=你的key

![图片](https://image.woshipm.com/wp-files/sha256/45/fa/45fa3d7b6e09e3ddb874c42f6edef603ca7442876dd4eadeac1eabd3d5d7bdc7.png)

### STEP 3 启动 Docker

> docker compose run –rm tradingagents

启动后，终端会进入交互式向导。

![图片](https://image.woshipm.com/wp-files/sha256/f7/fa/f7faafa4ce3d816639220da500bf4bcc6951557eeb1b051c2e1ef50aa7bbc543.png)

## 第一次运行：用腾讯控股做测试

TradingAgents 默认示例通常使用SPY，也就是标普 500 ETF。

项目支持 Yahoo Finance 覆盖的多个市场，输入股票代码时需要**带上交易所后缀** 。例如：

  * 美股：AAPL
  * 港股：0700.HK
  * 日股：7203.T
  * A 股：600519.SS
  * 加密资产：BTC-USD



![图片](https://image.woshipm.com/wp-files/sha256/03/14/03149babf06892dca47c650796c8ded9b16d50cc85ef676e2f592484230597f9.png)

这里输入腾讯控股的代码：0700.HK

接下来依次选择分析日期、输出语言、分析师类型和研究深度。

![图片](https://image.woshipm.com/wp-files/sha256/33/57/3357e8f6b30ad95992182b6de8d03897dce125301ddcefd0a119611f85b0ad85.png)

研究深度分为三个级别。

  1. 快速模式：适合先了解项目流程，第一次运行优先选它。
  2. 中等模式：会调用更多分析步骤，耗时和消耗都相应增加。
  3. 深入模式：适合对单只股票进行更完整的研究。



第一次运行建议先选择快速模式，**确认数据源、模型接口和配置都能正常工作** 。

![图片](https://image.woshipm.com/wp-files/sha256/f3/35/f335d82cf3046b0989d873edc49d58baedc92d574d6eaf043423e82bfe048b31.png)

然后选择模型服务商和模型 ID。

本文测试使用了阶跃的step-5-preview（官方宣称他们对金融领域特别训练过，待验证）。你也可以选择环境变量中已经配置的服务商，再填写该服务商实际提供的模型名称。

![图片](https://image.woshipm.com/wp-files/sha256/d9/41/d941aff0a7d0eedd349767437e7dce2e7dcf15be86f96f75c8271e25d8967844.png)

填写完成后，确认配置即可开始运行。

![图片](https://image.woshipm.com/wp-files/sha256/44/e3/44e351e5506363aba9b0b25152fab6ce79baff0e7ba6952ab3bb13f2929a442e.png)

运行过程中，终端会显示各个智能体的执行进度。

![图片](https://image.woshipm.com/wp-files/sha256/1c/ba/1cba7db25dc2dd6c31552571ee46adfed229f2598069c8dd2a5c6cf52cd74cc2.png)

### 分析过程和交易判断的报告

最终系统会生成一份包含（截取部分）：

![图片](https://image.woshipm.com/wp-files/sha256/9a/af/9aafa44d9c9bd36b026542b09538029781e2e4d3b68e742af90b0e693ce62414.png)  
![图片](https://image.woshipm.com/wp-files/sha256/f9/0f/f90f104534f60ac60e748e29d262c1b6626c8003abc73dd2aa33ef78f3849869.png)

## 04 数据从哪里来

TradingAgents 并不自带一套完全独立的行情数据库，**很多数据依赖外部服务** 。

![图片](https://image.woshipm.com/wp-files/sha256/23/56/23560766c656d4827882e74ac7919f7f697fab1c8f00d9b6603efeabfb1bda1b.png)

![](https://image.woshipm.com/wp-files/2026/09/OFFzH57z0eREq8OOyYys.png)

因此，项目能否顺利运行，除了取决于模型 API，也取决于行情、新闻和情绪数据源是否能够正常访问，**建议提前准备好自己的网络环境** 。

此外，不同市场的数据覆盖并不完全一致。美股公司通常能获得更完整的财务和申报数据，港股、A 股等市场则可能受到**数据源覆盖范围、ticker 格式和接口限制** 的影响。

## 写在最后

![图片](https://image.woshipm.com/wp-files/sha256/92/63/92630fbe1ace6ffd6634ccd3eed53f34d6f54d41a6553df69ffe0546becf0101.png)

从部署角度看，TradingAgents 的门槛并不算高。准备好 Docker、模型 API 和数据源之后，**几条命令就可以启动** 。

真正值得花时间的部分，在于理解它的运行逻辑：哪些数据被采集，哪些角色参与分析，多空观点如何形成，最终决策又是如何被风险管理团队审核。

当大模型开始从**“回答问题”转向“分工协作”** ，TradingAgents 提供了一个相对直观的观察样本。

跑通不难，理解它怎么思考才费时间。

该框架仅供研究，输出不构成任何投资建议。对 A 股标的的数据覆盖有限，结论仅供参考。投资需谨慎，AI 时代最重要的是自己的判断力。

项目官方仓库：**https://github.com/TauricResearch/TradingAgents**

研究论文：TradingAgents: Multi-Agents LLM Financial Trading Framework

本文由人人都是产品经理作者【AI李子】，微信公众号：【AI李子】，原创/授权 发布于人人都是产品经理，未经许可，禁止转载

题图来自Unsplash，基于 CC0 协议


---
> 原文链接: https://www.woshipm.com/ai/6468328.html