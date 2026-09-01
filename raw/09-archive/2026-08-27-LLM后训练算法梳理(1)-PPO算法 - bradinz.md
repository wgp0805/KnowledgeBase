---
title: "LLM后训练算法梳理(1)-PPO算法 - bradinz"
source: "博客园"
url: "https://www.cnblogs.com/zbohan/p/22727129"
date: "2026-08-27T14:11:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# LLM后训练算法梳理(1)-PPO算法 - bradinz

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/zbohan/p/22727129  
> **抓取日期**: 2026-08-27  
> **相关性评分**: 0.7

# LLM后训练算法梳理(1)-PPO算法

笔者最近在学习和梳理LLM post-training算法，本系列用于记录自己对LLM后训练中常见算法的思考和总结。目前初步打算梳理和总结的算法有:

  * 强化学习:PPO,GRPO,GRPO的热门变体，例如DAPO等。
  * 监督微调:重点梳理SFT，DFT，以及近期值得注意的其他实验性文章
  * PEFT:重点梳理Lora及其热门变体。
  * On policy Distillation: 关注OPD等开山之作，以及较为热门的OPSD，SDFT等自蒸馏变体。



个人随笔难免有纰漏之处，如有事实性错误或其他不足之处，还请不吝指正。

## 0.LLM的三个训练阶段

在介绍如何将RL方法引入LLM之前，我们首先需要知道LLM训练大致分为几个阶段，RL方法在什么阶段起到了作用？本小节就是在介绍这件事。总的来说，LLM的训练可以大致分为三个常见手段，他们大体上的先后顺序是：**预训练Pretrain** 、**监督微调SFT** 、**后训练Post-train** 。RL方法通常出现在后训练阶段，我们对这三个阶段分别做出解释:

  1. **Pre-training（预训练）**  
预训练阶段会采用巨量的，相对低质量的无标注数据，模型的训练任务是预测next token，也就是学会文本补充，在这一阶段训练出来的模型叫做**基座模型（Base Model）** ，

\\[\max_\theta \mathbb{E}_{x}\big[\log p_\theta(x)\big] \\]

目标是理解人类的语言模式和基础知识，这一阶段中，大模型开始逐渐展现出某种“正常有序”的行为模式，输出的内容越来越有意义。基础模型，是无监督训练的结果，它能够根据输入的内容预测下一个可能的词汇，尽可能保证它输出的是一段连贯、有意义的文本，因此它更擅长做“完形填空”，但并不能直接用来和人类进行自然语言的对话交互

  2. **SFT（Supervised Fine-Tuning）**  
和预训练阶段相比，这个阶段最大的变化就是训练数据由“量多质低”“变为“量少质高”，训练数据主要由人工进行筛选或生成，数据量一般在 10～100 万条，要比预训练阶段低几个数量级，同样大幅降低的还有算力资源消耗和训练时间。微调的“微”就体现在这里.此时使用的数据集是一条条包含“明确指令<->精确回答”的对话交互语料对，这可以看成一种“标签”型数据，因此是一种有监督的训练方式。

\\[\max_\theta \mathbb{E}_{(x,y^*)}\big[\log p_\theta(y^*\mid x)\big] \\]

这一阶段的训练目标是“听懂指令，学会模仿好答案”。

  3. **后训练阶段（Post-training）**  
希望模型**不只是模仿答案** ，而是满足一些更抽象的目标：例如安全性、符合人类偏好、代码正确、视觉检测 IoU 高等。这一步就会用到：

     * RLHF（符合人类偏好的强化学习）
     * RFT（强化微调，RL-based 的统称）
     * DPO（非 RL 的对齐方法）
     * 以及各种 RL 算法（PPO / GRPO 等）当优化器。



在这一阶段，模型学习和输出的内容发生了根本性的改变。前面的两个阶段，预训练和微调，模型的输出是符合预期的文本内容；奖励建模阶段的输出不仅包含预测内容，还包含奖励值或者说评分值，数值越高，意味着模型的预测结果越好。**这些奖励值或者评分是人类打出的，也就是说后训练阶段加入了人的因素。** ，此时模型的训练目标不存在硬标签这种明确的监督信号，而是通过奖励信号来引导模型学习更符合人类期望的行为模式。因此RL方法自然地被引入了这一阶段。

## 1\. RL变量在LLM语境下的基本定义

一个智能体（agent）在某个环境（environment）中采取动作（action）；这些动作由一个策略（policy）给出。在 LLM 的场景里，这个 **policy 就是我们要训练的大模型本身** 。

我们用参数 \\(\theta\\) 表示策略的参数（也就是 LLM 的参数）。在状态 \\(s_t\\) 下发生动作 \\(a_t\\) 的概率是 \\(\pi_\theta(a_t \mid s_t).\\) 动作发生后，环境将状态更新到下一步，写作“转移函数： \\(p(s_{t+1}\mid s_t, a_t).\\) 对于LLM决策而言，状态的更新规则就是“把新 token append 到上下文里”，是一种deterministic的转移。

最终，智能体会从环境中获得一个奖励（reward）。每个动作（\\(a_t\\)）、奖励（\\(r_t\\)）和状态（\\(s_t\\)）都与时间步 t 关联。组合在一起，就形成了一个T步的轨迹（trajectory. 记为

\\[\overbrace{\tau=\\{\overbrace{a_1,s_1,r_1}^{t=1},\overbrace{a_2,s_2,r_2}^{t=2}, \quad ···\overbrace{a_T,s_T,r_T}^{\text{Final Time Step (T)}}\\}}^{Trajectory} \\]

#### 总结一下，LLM的 state / action / transition 分别是

  * **Initial State（初始状态）** ：用户给定的prompt（输入问题）
  * **Action（动作）** ：LLM 在每一步输出的 token
  * **State（状态）** ：prompt + 已经生成的 token 们（即“当前上下文”）
  * **Reward（奖励）** ：由 reward model / rule-based verifier 给出
  * **Episode 终止** ：生成到 EOS / stop token 或达到最大长度



强化学习的训练目标是最大化“整条Trajectory上的累积奖励”。即对于每条轨迹 \\(\tau\\)，我们计算它的回报（return）\\(R(\tau)\\)，然后对所有可能的轨迹取期望. 轨迹的总回报（return）可以是 **non-discounted** 或 **discounted** ：

  * non-discounted return：\\(R(\tau) = \sum_{t=0}^{T-1} r_t\\)

  * discounted return：\\(R(\tau) = \sum_{t=0}^{T-1} \gamma^t r_t,\quad \gamma\in(0,1].\\)




最终的 RL 目标函数就是“回报的期望”，期望是对轨迹分布取的：

\\[J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]. \\]

把期望展开（离散写求和，连续写积分；这里写积分形式更通用）：

\\[J(\theta) = \int P(\tau\mid \theta)\, R(\tau)\, d\tau. \\]

## 2\. Policy Gradient

刚才我们讲到，RL 的目标函数是轨迹回报的期望，记作

\\[J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]. \\]

我们的目标是通过调整策略参数 \\(\theta\\)（也就是 LLM 参数）来最大化它：

\\[\theta^* = \arg\max_\theta J(\theta). \\]

那么什么叫 “policy gradient”？就是对目标函数关于参数的梯度：

\\[\nabla_\theta J(\theta). \\]

如果我们能算出这个梯度，就可以用gradient ascent：\\(\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta).\\)更新参数。问题是：**\\(\nabla_\theta J(\theta)\\) 怎么算？** 从定义出发：

\\[\nabla_\theta J(\theta) = \nabla_\theta \mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]. \\]

把期望展开成积分：

\\[\nabla_\theta J(\theta) = \nabla_\theta \int P(\tau\mid\theta)\,R(\tau)\,d\tau. \\]

将梯度移入积分号（在可交换条件下）：

\\[\nabla_\theta J(\theta) = \int \nabla_\theta P(\tau\mid\theta)\,R(\tau)\,d\tau. \\]

使用 log-derivative trick：

\\[\nabla_\theta P(\tau\mid\theta) = P(\tau\mid\theta)\nabla_\theta \log P(\tau\mid\theta), \\]

代回去：

\\[\nabla_\theta J(\theta) = \int P(\tau\mid\theta)\,\nabla_\theta \log P(\tau\mid\theta)\,R(\tau)\,d\tau = \mathbb{E}_{\tau\sim\pi_\theta}\big[\nabla_\theta \log P(\tau\mid\theta)\,R(\tau)\big]. \\]

接下来把轨迹概率分解。标准 episodic MDP 下，用条件概率公式可以轻易得到下式：

\\[P(\tau\mid\theta) = p(s_0)\prod_{t=0}^{T-1}\pi_\theta(a_t\mid s_t)\,p(s_{t+1}\mid s_t,a_t). \\]

\\[\log P(\tau\mid\theta) = \log p(s_0) + \sum_{t=0}^{T-1}\log \pi_\theta(a_t\mid s_t) \+ \sum_{t=0}^{T-1}\log p(s_{t+1}\mid s_t,a_t). \\]

由于 \\(p(s_0)\\) 与 \\(p(s_{t+1}\mid s_t,a_t)\\) 不依赖 \\(\theta\\)（策略参数只在 \\(\pi_\theta\\) 里），所以它们对 \\(\theta\\) 的梯度为 0，直接扔掉，原式子只保留

\\[\nabla_\theta \log P(\tau\mid\theta) = \sum_{t=0}^{T-1}\nabla_\theta \log \pi_\theta(a_t\mid s_t). \\]

代回 policy gradient：

\\[\nabla_\theta J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\left[ \left(\sum_{t=0}^{T-1}\nabla_\theta \log \pi_\theta(a_t\mid s_t)\right)R(\tau) \right]. \\]

这就是最基础的 Policy Gradient（REINFORCE）形式：**对每一步的 log-prob 梯度求和，再用整条轨迹的回报做加权。**

## 3\. PPO算法

在正式介绍 PPO 的裁剪目标之前，我们先说明它所依赖的几个基础概念，包括 credit assignment、优势函数以及 actor-critic 协同更新机制。

### credit assignment

策略梯度方法的目标是最大化策略在环境中的期望回报。对于策略 \\(\pi_\theta\\)，其目标函数记作 \\(J(\pi_\theta)\\)。在实践中，我们通常通过采样足够多的轨迹来估计这个期望。假设采样了 \\(N\\) 条轨迹，第 \\(n\\) 条轨迹长度为 \\(T_n\\)，则最原始的策略梯度可以写为

\\[\nabla J(\pi_\theta) = E_{\tau\sim \pi_\theta} \left[ \sum_{t=0}^{T-1} R(\tau)\nabla_\theta \log \pi_\theta(a_t|s_t) \right] \approx \frac{1}{N} \sum_{n=0}^{N-1} \sum_{t=0}^{T_n-1} R(\tau_n)\nabla_\theta \log \pi_\theta(a_t|s_t). \\]

这个公式的直观含义并不难理解：如果一条轨迹的回报 \\(R(\tau)\\) 很高，那么我们倾向于认为轨迹中出现过的动作总体上是“好的”，于是应该提升这些动作在对应状态下被采样到的概率；反之，如果轨迹回报很低，那么这些动作的概率就应被压低。

然而，这里立刻会产生一个很自然的问题：\\(R(\tau)\\) 是整条轨迹的总回报，而 \\(\pi_\theta(a_t|s_t)\\) 却是某一个时刻的单步决策。也就是说，我们是在用一整个序列的好坏来评价其中某一个动作的贡献。这种做法虽然简单，但 credit assignment 非常粗糙，方差也很大。以 LLM 为例，假设模型生成了一个很长的句子，前 99 个 token 都非常合理，只有最后 1 个 token 生成错误，导致整条序列得到较低奖励。那么按照上式，前面那些本来很好的 token 也会被整体地打上“低分”，它们对应的生成概率也会被一并压低。这正是基础 Policy Gradient 方法的核心缺陷之一。

因此，在衡量某一步动作的价值时，我们希望在“整条轨迹的整体结果”和“单步动作的局部贡献”之间找到更合理的平衡。为此，可以将上式中的 \\(R(\tau)\\) 替换为一个更一般的权重项 \\(\Psi_t\\)，于是策略梯度写成

\\[\nabla J(\pi_\theta) = E_{\tau\sim \pi_\theta} \left[ \sum_{t=0}^{T-1}\Psi_t \nabla_\theta \log \pi_\theta(a_t|s_t) \right] \approx \frac{1}{N} \sum_{n=0}^{N-1} \sum_{t=0}^{T_n-1} \Psi_t \nabla_\theta \log \pi_\theta(a_t|s_t). \\]

这里的 \\(\Psi_t\\) 可以有多种实现方式，它们对应着不同粒度的 credit assignment。

第一种方式是直接使用整条轨迹的总回报，即

\\[\Psi_t = R(\tau)=\sum_{t'=0}^{T-1}\gamma^{t'}r_{t'}. \\]

这是最原始的写法，优点是形式简单，但它对每一步都使用同一个标量回报，无法区分不同时间步动作的具体贡献，因此方差通常较大。

第二种方式是使用从当前时刻开始的累积折扣奖励，也称为 reward-to-go：

\\[\Psi_t = G_t=\sum_{t'=t}^{T-1}\gamma^{,t'-t}r_{t'}. \\]

相比整条轨迹总回报，\\(G_t\\) 只保留了从当前时刻开始的未来奖励。这样做的原因不是“过去和当前无关”，而是因为当前动作 \\(a_t\\) 不可能影响已经发生的过去奖励，因此用 reward-to-go 来评价 \\(a_t\\) 不会引入偏差，反而能显著降低方差。

第三种方式是在 reward-to-go 的基础上引入一个基线 \\(b(s_t)\\)，写成

\\[\Psi_t = G_t - b(s_t). \\]

这里的关键思想是：仅仅知道一个动作最终带来了多高的回报还不够，我们更关心的是它相对于“该状态下的一般水平”究竟好多少。因为一个高回报动作未必真的优秀，它也可能只是因为该状态本身就容易获得较高奖励。引入基线之后，我们衡量的是“超出平均水平的部分”，这能进一步降低梯度估计的方差。理论上，只要基线不依赖于当前动作 \\(a_t\\)，就不会改变策略梯度的无偏性。实践中，最常见的选择就是令基线取为状态价值函数 \\(V_\pi(s_t)\\)。

再往后，我们可以直接令 \\(\Psi_t\\) 取为一些更具语义的价值量，例如动作价值函数 \\(Q_\pi(s_t,a_t)\\)、优势函数 \\(A_\pi(s_t,a_t)\\)，或者用一步 TD residual 来构造对优势函数的近似估计。这几种写法之间有很紧密的联系，下面具体展开。

### 优势函数和协同更新

我们先定义某个时刻 \\(t\\) 开始的累积折扣回报：

\\[G_t = r_t+\gamma r_{t+1}+\gamma^2 r_{t+2}+\cdots+\gamma^{T-t-1}r_{T-1}. \\]

在此基础上，状态价值函数表示：如果当前位于状态 \\(s_t\\)，并继续按照策略 \\(\pi\\) 与环境交互，那么未来期望能够获得多少回报。它定义为

\\[V_\pi(s_t)=E_\pi(G_t\mid s_t). \\]

相应地，动作价值函数表示：如果当前位于状态 \\(s_t\\)，并首先执行动作 \\(a_t\\)，之后仍按照策略 \\(\pi\\) 行动，那么未来期望能够获得多少回报。它定义为

\\[Q_\pi(s_t,a_t)=E_\pi(G_t\mid s_t,a_t). \\]

两者之间满足关系

\\[V_\pi(s_t)=E_{a_t\sim \pi(\cdot\mid s_t)}[Q_\pi(s_t,a_t)] = \sum_{a_t\in\mathcal A}\pi(a_t\mid s_t)Q_\pi(s_t,a_t). \\]

因此，状态价值 \\(V_\pi(s_t)\\) 可以看作在状态 \\(s_t\\) 下，对所有可能动作的动作价值做策略加权平均后的结果。基于这一点，我们定义优势函数

\\[A_\pi(s_t,a_t)=Q_\pi(s_t,a_t)-V_\pi(s_t). \\]

它描述的是：在状态 \\(s_t\\) 下，执行动作 \\(a_t\\) 相对于该状态下“平均动作水平”究竟好多少。如果 \\(A_\pi(s_t,a_t)>0\\)，说明该动作优于平均水平；如果 \\(A_\pi(s_t,a_t)<0\\)，则说明它劣于平均水平。相比直接用原始回报更新策略，优势函数提供了更细粒度、也更稳定的 credit assignment。

进一步地，由 Bellman 关系可知

\\[Q_\pi(s_t,a_t)=E\big[r_t+\gamma V_\pi(s_{t+1})\mid s_t,a_t\big]. \\]

于是优势函数可以写成

\\[A_\pi(s_t,a_t) = E\big[r_t+\gamma V_\pi(s_{t+1})-V_\pi(s_t)\mid s_t,a_t\big]. \\]

这里需要特别注意：严格来说，优势函数并不直接等于

\\[r_t+\gamma V_\pi(s_{t+1})-V_\pi(s_t), \\]

而是等于这个量在条件 \\(s_t,a_t\\) 下的期望。单次采样时，我们通常用

\\[\delta_t = r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t) \\]

作为对优势函数的一步近似估计，这个 \\(\delta_t\\) 就是一阶 TD residual。换句话说，TD residual 是 advantage 的一种单步采样估计，而不是二者在严格意义上的完全恒等。

到这里可以看出，如果真实的状态价值函数 \\(V_\pi\\) 已知，那么我们就可以直接计算优势，从而用它来更新策略。但在实际问题中，\\(V_\pi\\) 通常未知，因此我们需要再引入一个参数化函数 \\(V_\phi\\) 来逼近它。此时，策略网络 \\(\pi_\theta\\) 与价值网络 \\(V_\phi\\) 就构成了经典的 actor-critic 框架：其中 actor 负责输出策略，critic 负责评估状态价值，并为 actor 提供更低方差的训练信号。

在这种框架下，actor 的更新目标可以写为一个 surrogate objective：

\\[L_{\text{actor}}(\theta) = E_t\big[\hat A_t \log \pi_\theta(a_t\mid s_t)\big], \\]

其中 $$\hat A_t$$ 是优势函数的估计值。若采用最简单的一步 TD 近似，则有

\\[\hat A_t \approx \delta_t = r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t). \\]

于是 actor 的目标可进一步写成

\\[L_{\text{actor}}(\theta) = E_t\Big[ \big(r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t)\big)\log \pi_\theta(a_t\mid s_t) \Big]. \\]

这意味着：如果某一步的优势估计为正，那么该动作在当前状态下的概率就应被提高；如果优势估计为负，则其概率应被压低。相比最原始的整轨迹回报更新，这种做法已经把 credit assignment 细化到了单步层面。

对于 critic 而言，它的任务是尽可能准确地逼近真实价值函数。若采用一步 TD 目标，那么可以最小化如下损失：

\\[L_{\text{critic}}(\phi) = E_t\Big[ \big(r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t)\big)^2 \Big]. \\]

这个目标的含义是：希望当前的价值估计满足 Bellman 一致性，即当前状态的价值应当接近“即时奖励加上下一个状态的折扣价值”。critic 训练得越准确，actor 所得到的优势估计就越可靠，策略更新的方差也就越小。

你可能会担心：critic 的目标是在让 TD residual 逼近 0，而 actor 的更新又恰好依赖于这个量。那么 critic 会不会把 actor 的训练信号“消掉”，导致 actor 无法继续更新？答案是否定的。确实，在理想最优状态下，如果价值估计已经非常准确，且当前策略也已接近最优，那么优势函数本来就应当趋近于 0，此时策略梯度自然也会变小。但这并不意味着训练过程出了问题，而恰恰说明策略已经接近稳定点。实际训练中，actor 和 critic 是一个动态耦合的过程：critic 持续提升对状态价值的估计精度，actor 则根据 critic 给出的优势信号不断调整策略，二者共同推动训练向更优的方向演化。

以上内容实际上构成了 PPO 的前置基础。PPO 真正的关键改进是在 actor 更新时，不再直接最大化上述策略梯度目标，而是进一步引入旧策略与新策略之间的概率比值，并通过 clip 机制限制单次更新幅度，从而在保证学习效率的同时提升训练稳定性。

### 重要性采样

观察这个梯度表达式

\\[arg \max_{\pi_{\theta}}J(\pi_{\theta}) = E_{t}[A_{\phi}(s_{t}, a_{t})log\pi_{\theta}(a_{t}|s_{t})] \\]

我们会发现如下问题：

问题1：每次执行这个梯度更新时，我们都需要对 \\(\pi_{\theta}\\) 进行若干次回合采样。我们知道智能体和环境交互的时间成本（fwd）比较高，也就是整个训练过程会比较慢。同时由于采样过程具有随机性，我们可能偶发采样到了一些方差特别大的样本，如果我们直接信任这些样本去做更新，就可能使得更新方向发生错误。

问题2：我们在前面说过，实际训练的过程中，用critic网络拟合出来 \\(V_{\pi}\\) 并不一定是能准确衡量 \\(\pi\\) 的那个价值函数，所以这里我们用TD error去估计优势其实是有偏的。为了降低这种偏差，我们需要对 \\(A_{\phi}(s_{t}, a_{t})\\) 进行改造，改造的方法之一就是GAE。

接下来我们就详细来看如何解决这两个问题。

### 解决采样效率问题：

在朴素的方法中，我们使用 \\(\pi_{\theta}\\) 和环境交互若干次，得到一批回合数据，然后我们用这个回合数据计算出来的奖励值去更新 \\(\pi_{\theta}\\)，此过程为on-policy的。PPO为了降低采样成本，提升训练效率，采取off policy的策略。

  * 假设某次更新完毕后，我们得到策略 \\(\pi_{old}\\)
  * 我们用 \\(\pi_{old}\\) 和环境交互，得到一批回合数据。
  * 我们将把这一批回合数据重复使用k次：即我们先把这批数据喂给 \\(\pi_{old}\\) 更新old得到 \\(\pi_{\theta_{0}}\\) ；
  * 我们再把这批数据喂给 \\(\pi_{\theta_{0}}\\) ，更新得到 \\(\pi_{\theta_{1}}\\) ；
  * 以此类推，做k次更新后，我们得到 \\(\pi_{\theta}\\) 。我们管这个过程叫off-policy（产出数据的策略和用这批数据做更新的策略不是同一个）。



在这k次更新后，我们令 \\(\pi_{old} = \pi_{\theta}\\) 。重复上面的过程，直到达到设定的停止条件为止。

更理论的角度来看待这个off-policy的过程：

假设有两个分布 \\(p(x), q(x)\\)  
最开始我想从 \\(p(x)\\) 中进行多次采样，然后求函数 \\(f(x)\\) 的期望。例如我想从 \\(\pi_{\theta}\\) 中进行采样，然后求累积奖励的期望，这个期望我们表示成 \\(E_{x \sim p(x)}[f(x)]\\)  
但是现在，因为某些原因，我们无法从 \\(p(x)\\) 中直接采样，只能从另一个分布 \\(q(x)\\) 中进行采样了，那么此时我们要怎么表示 \\(E_{x \sim p(x)}[f(x)]\\) ？  
为了解决这个问题，我们做如下变换：

\\[\begin{aligned} E_{x\sim p(x)}[f(x)] & = \int p(x)f(x)dx \\\ & = \int\frac{p(x)}{q(x)}q(x)f(x)dx\\\ & = E_{x \sim q(x)}[\frac{p(x)}{q(x)}f(x)] \end{aligned} \\]

也就是说，当我们从不同于 \\(p(x)\\) 的分布 \\(q(x)\\) 上采样x时，从数学上我们确实有办法改写 \\(E_{x \sim p(x)}[f(x)]\\) ，简单来说就是加上一个权重 \\(\frac{p(x)}{q(x)}\\) ，我们管上述的转换过程叫【重要性采样】。  
重要性采样前，策略的梯度是：

\\[\nabla J(\pi_{\theta}) = E_{t}[A_{\phi}(s_{t}, a_{t})\nabla log\pi_{\theta}(a_{t}|s_{t})] \\]

重要性采样后，策略的梯度是：

\\[\nabla J(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{old}(a_{t}|s_{t})}A_{\phi}(s_{t}, a_{t})\nabla log\pi_{\theta}(a_{t}|s_{t})] \\]

我们根据重要性采样构造了这个新的策略梯度，那么对应的新的actor优化目标就可以从这个策略梯度中反推出来：

\\[arg \max_{\pi_{\theta}}J(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{\theta_{old}}(a_{t}|s_{t})}A_{\phi}(s_{t}, a_{t})] \\]

特别注意 \\(\tau \sim \pi_{\theta_{old}}\\) ，它意味着我们这一波的训练数据是由old策略采集来的。

在假设 \\(V_{\pi}\\) 能正确评估策略 \\(\pi\\) 的价值的前提下，我们用TD_error作为优势函数的无偏估计：

\\[\begin{aligned} A_{\pi}(s_{t}, a_{t}) &= Q_{\pi}(s_t, a_t) - V_{\pi}(s_t)\\\ &= E_{s_{t+1}\sim P(.|s_{t}, a_{t})}[r_{t} + \gamma V_{\pi}(s_{t+1})] - E_{s_{t+1} \sim P(.|s_{t}, a_{t})}[V_{\pi}(s_{t})]\\\ &= E_{s_{t+1}\sim P(.|s_{t}, a_{t})}[r_{t} + \gamma V_{\pi}(s_{t+1}) - V_{\pi}(s_{t})]\\\ &= E_{s_{t+1}\sim P(.|s_{t}, a_{t})}[TD\\_error] \end{aligned} \\]

但是，在训练过程中，这个 \\(V_{\pi}\\) 往往无法完全正确评估出策略 \\(\pi\\) 的价值，所以上述这种估计是有偏的，也即如果我们使用TD error去近似优势函数，就会引发系统性偏差。为了解决因为 \\(V_{\pi}\\) 估计不准而引发的“高偏差”问题，直观上我们可以尽量少信任 \\(V_{\pi}\\) 的策略，即对于 \\(r_{t} + \gamma V_{\pi}(s_{t+1}) - V_{\pi}(s_{t})\\) ，我们可以把 \\(V_{\pi}(s_{t+1})\\) 做递归地展开，得到：

\\[-V_{\pi} (s_t) + \sum_{l=0}^{\infty}\gamma^{l}r_{t+l} \\]

其中， \\(r_{t}, r_{t+1}, r_{t+2}, ...\\) 都是我们某次采样得到的即时奖励数据。如果 \\(V_{\pi}\\) 不准，那么我就信任我的实际采样结果，这样至少不会让我对优势函数的估计出现偏差。

但采取这种做法又会引发一个新问题：我们知道 \\(r_{t}, r_{t+1}, r_{t+2}, ...\\) 它们都是随机变量，相比之前只用 \\(r_{t}\\) ，现在的做法带来的随机性更大了这意味着此时虽然偏差降低了，但你需要采样足够多的数据才能准确估计出优势函数，这样加重了实际训练中的采样负担。

此时你可能已自然而然想到：当 \\(V_{\pi}\\) 估计不准时，如果我能在 \\(r_{t} + \gamma V_{\pi}(s_{t+1}) - V_{\pi}(s_{t})\\) 和 \\(-V_{\pi} (s_t) + \sum_{l=0}^{\infty}\gamma^{l}r_{t+l}\\) 间取得一种平衡就好了，即我既不想完全信任 \\(V_{\pi}\\) ，又不想完全信任我全部的采样的结果 \\(r_{t}, r_{t+1}, r_{t+2}, ..\\) ，此时，GAE（Generalized Advantage Estimator）就登场了，它通过一个超参数 \\(\lambda\\) 控制了我们想要的方差-偏差间的平衡。

这里我们直接来看在GAE的修改下，最终的形式（具体的推导这里不再展开，大家可以看论文）：

\\[\Psi_{t} = \sum_{l=0}^{\infty}(\gamma \lambda)^{l}\delta_{t+l} \\]

\\[\delta_{t} = r_{t} + \gamma V_{\pi}(s_{t+1}) - V_{\pi}(s_{t}) \\]

\\(\gamma\\) ：超参，折扣因子  
\\(\lambda\\) ： 超参，即用于平衡方差-偏差的因子。  
当 \\(\lambda\\) 接近0时， \\(\Psi_{t}\\) 退化成 \\(r_{t} + \gamma V_{\pi}(s_{t+1}) - V_{\pi}(s_{t})\\) ，也即上图所绘制的高偏差情况  
当 \\(\lambda\\) 接近1时， \\(\Psi_{t}\\) 变成 \\(-V_{\pi} (s_t) + \sum_{l=0}^{\infty}\gamma^{l}r_{t+l}\\) ，也即上图所绘制的高方差-低偏差情况  
综上，\\(\lambda\\) 越小，方差越小，偏差越大。\\(\lambda\\) 越大，方差越大，偏差越小。

在接下来的表达中，我们记这种引入了GAE方法的单步优势为 \\(A_{\phi}^{GAE}(s_t, a_t)\\)

### 解决重要性采样中遗留的问题：

引入GAE解决单步优势的方差-偏差平衡问题后，我们的优化目标变成：

\\[arg \max_{\pi_{\theta}}J(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{\theta_{old}}(a_{t}|s_{t})}A_{\phi}^{GAE}(s_{t}, a_{t})] \\]

我们在之前使用了重要性采样，重要性采样理论上很优雅，但是实际中它的表现却不太好，因为当 \\(p(x)\\) 和 \\(q(x)\\) 这两个分布差异太大时，权重 \\(\frac{p(x)}{q(x)}\\) 的方差会变得非常大，这样就会导致我们对 \\(E_{x \sim p(x)}[f(x)]\\) 的估计不准确了，你需要采样足够多的数据才能得到一个准确的估计，这样就加重了实际训练中的采样负担。  
：如果 \\(\pi_{\theta}\\) 和 \\(\pi_{old}\\) 这两个分布差异太大，且我们采样的轨迹数量没有足够大时， \\(J(\pi_{\theta})\\) 的估计是不准确的。那要怎么办呢？

一种直观的解决办法是，把 \\(\pi_{\theta}\\) 和 \\(\pi_{old}\\) 的分布相似性作为 \\(J(\pi_{\theta})\\) 的constraint，这就是TRPO的做法，即我们有：

\\[\begin{matrix} arg \max_{\pi_{\theta}}J(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{old}(a_{t}|s_{t})}A_{\phi}^{GAE}(s_{t}, a_{t})]\\\ \\\ subject\; to \; E_{t}[KL(\pi_{\theta{old}}(.|s_{t}), \pi_{\theta}(.|s_{t}))] \le \delta \end{matrix} \\]

由于这种限制不直接加在 \\(J(\pi_{\theta})\\) 中，因此使得整体优化过程变得较为复杂，这就是TRPO的缺陷。

PPO的做法是把这个限制直接加在 \\(J(\pi_{\theta})\\) 中，形成一个新的优化目标.定义新旧策略比值为 \\(r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}.\\) ，新的优化目标可以写为:

\\[J^{CLIP}(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[min[r_{t}(\theta)A_{\phi}^{GAE}(s_t, a_t), \;\; clip(r_{t}(\theta), 1-\epsilon, 1+\epsilon)A_{\phi}^{GAE}(s_t, a_t)]] \\]

固定一批由 \\(\pi_{\theta_{\text{old}}}\\) rollout 得到的数据后，在若干个 PPO update epoch 中，actor 优化时通常把 \\(\theta_{\text{old}}\\) 和 \\(\hat A_t\\) 都视为常数，真正对 \\(\theta\\) 求导的只有比例值的分子部分

\\[r_t(\theta)=\frac{\pi_\theta(a_t|s_t)} {\pi_{\theta_{\text{old}}}(a_t|s_t)}. \\]

所以如果某个 sample 最终选择了 clipped branch，而且 clip 后恰好是常数 \\(1+\epsilon\\) 或 \\(1-\epsilon\\)，那么这个 sample 对 actor 的梯度就是 0。这正是 PPO-Clip 的设计目的。为了便于理解，我们可以对上述式子进行分类讨论，简写原式子为：

\\[L_t(\theta)= \min \left[ r_t A_t,\; \operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A_t \right] \\]

当 \\(A_t>0\\) 时，意味着当前动作带来正向收益，PPO希望提升这个新策略相较于旧策略采取这个动作的概率

  * 如果目前策略相比旧策略没那么偏好这个动作，即 \\(r_t<1+\epsilon\\)，那么就直接用 \\(r_t A_t\\) 作为优化目标；
  * 如果目前策略相比旧策略已经很偏好这个动作了，即 \\(r_t>1+\epsilon\\)。为了防止过度优化，PPO选择裁剪这个式子变成常数，不再提供梯度信号。于是我们有：



\\[L_t= \begin{cases} r_tA_t, & r_t\le 1+\epsilon,\\\ (1+\epsilon)A_t, & r_t>1+\epsilon. \end{cases} \\]

同理，当 \\(A_t<0\\) 时，意味着当前动作带来负向收益，PPO希望降低这个新策略相较于旧策略采取这个动作的概率

  * 如果目前策略相比旧策略没那么讨厌这个动作，即 \\(r_t>1-\epsilon\\)，那么就直接用 \\(r_t A_t\\) 作为优化目标；
  * 如果目前策略相比旧策略已经很讨厌这个动作了，即 \\(r_t<1-\epsilon\\)。为了防止过度优化，PPO选择裁剪这个式子变成常数，不再提供梯度信号。于是我们有：



\\[L_t= \begin{cases} r_tA_t, & r_t\ge 1-\epsilon,\\\ (1-\epsilon)A_t, & r_t<1-\epsilon. \end{cases} \\]

PPO 有意只让“方向正确但已经走太远”的 sample 丧失优化信号；如果方向走错，即使 ratio 已经越过另一侧 clipping boundary，也仍然保留梯度让它纠正回来。

* * *

除了PPO-Clip的方法外，我们还可以采用PPO-Penalty的方法来解决TRPO优化复杂的问题。PPO-Penalty做的事情就更直观了，直接把限制条件放进优化目标中，而这个限制条件就被称为“KL penalty"，PPO-Penalty的优化目标如下：

\\[arg \max_{\pi_{\theta}}J(\pi_{\theta}) = \underset{\tau \sim \pi_{\theta_{old}}}{E_{t}}[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{\theta_{old}}(a_{t}|s_{t})}A_{\phi}^{GAE}(s_{t}, a_{t}) - \beta KL(\pi_{\theta{old}}(.|s_{t}), \pi_{\theta}(.|s_{t}))] \\]

其中，超参 \\(\beta\\) 的调整策略如下：

首先，我们对KL散度一项也会设置threshold，我们分别记为 \\(KL_{max}, KL_{min}\\)  
当 \\(KL \ge KL_{max}\\) 时，说明当前策略已经偏离old策略较远了，这时我们应该增大 \\(\beta\\) ，把分布拉回来。  
当 \\(KL <= KL_{min}\\) 时，说明当前策略很可能找到了一条捷径，即它只优化KL散度一项，让自己和old更相近，而不去优化前面优势相关的项，所以这时我们应该减小 \\(\beta\\) ，降低KL散度一项的影响

## 4.PPO算法在LLM中的网络结构

在上述 PPO 算法中，我们实际上引入了两类需要训练参数的网络，即 actor 网络 \\(\pi_\theta(a_t|s_t)\\) 和 critic 网络 \\(V_\phi(s_t)\\)。

  * actor 网络的输入是当前状态 \\(s_t\\)，输出当前状态下执行各个动作的概率分布 \\(\pi_\theta(a_t|s_t)\\)。在 LLM 中，actor 就是语言模型本身：状态 \\(s_t\\) 对应 prompt 加已经生成的 token，动作 \\(a_t\\) 对应LLM生成的下一个 token。

  * critic 网络的输入同样是当前状态 \\(s_t\\)，输出是一个实数 \\(V_\phi(s_t)\\)，用于预测“从当前状态继续按照现有策略生成，未来期望能获得多少累计回报”。




要理解 critic 的网络结构，需要先更准确地看 LLM 的输出方式。假设当前输入序列token为为 \\(x_1,x_2,\ldots,x_T\\)，经过 Transformer 后，得到每个 token 位置对应的 hidden state：

\\[h_1,h_2,\ldots,h_T,\qquad h_t\in\mathbb R^{d_{\text{model}}}. \\]

其中 \\(h_t\\) 可以理解为模型已经看到 \\(x_1,\ldots,x_t\\) 后，对当前上下文的表示。

普通语言模型会把最后一个 hidden state 送入 LM Head：

\\[z_T=W_{\text{LM}}h_T+b_{\text{LM}}, \qquad z_T\in\mathbb R^{|\mathcal V|}, \\]

得到整个词表上的 logits，再通过 softmax 得到下一个 token 的概率：

\\[\pi_\theta(a_{T+1}|s_t)=\operatorname{softmax}(z_T). \\]

因此 actor 可以简单理解为

\\[\boxed{ \text{Transformer} \rightarrow h_t\in\mathbb R^{d_{\text{model}}} \rightarrow \text{LM Head} \rightarrow \mathbb R^{|\mathcal V|} } \\]

critic 的结构非常类似，只不过最后不再连接输出维度为词表大小的 LM Head，而是连接一个输出维度为 1 的 value head，执行回归任务。

\\[V_\phi(s_t)=w_V^\top h_t+b_V, \\]

其中 \\(w_V\in\mathbb R^{d_{\text{model}}}\\)。可以看到，在不同的 \\(h_t\\) 处，critic 会输出不同的 value，对应不同的状态价值。因此 critic 可以理解为

\\[\boxed{ \text{Transformer} \rightarrow h_t\in\mathbb R^{d_{\text{model}}} \rightarrow \text{Value Head} \rightarrow \mathbb R } \\]

需要特别注意，value head 输出的不是 reward，而是 value：

\\[V_\phi(s_t)\approx \mathbb E_{\pi_\theta}[G_t\mid s_t]. \\]

两者区别是：

  * reward \\(r_t\\)：环境、reward model 或 verifier 实际给出的反馈；

  * value \\(V_\phi(s_t)\\)：critic 根据当前前缀预测“从这里继续生成，未来大概还能拿到多少累计 reward”。




还有一个非常重要的实现细节：PPO 并不需要为了得到每个 \\(V(s_t)\\)，把每一个前缀分别 forward 一次。假设 rollout 得到

\\[x_1,x_2,\ldots,x_T, \\]

一次 Transformer forward 就会同时产生

\\[h_1,h_2,\ldots,h_T. \\]

然后对所有位置使用同一个 value head：

\\[V_\phi(s_t)=w_V^\top h_t+b_V, \\]

于是一次 forward 就可以得到整条序列所有位置的 value：

\\[V_\phi(s_1),V_\phi(s_2),\ldots,V_\phi(s_T). \\]

PPO 随后就可以利用相邻状态的 value 计算 TD residual：

\\[\delta_t = r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t), \\]

再进一步计算 GAE：

\\[\hat A_t = \delta_t+ \gamma\lambda\delta_{t+1} \+ (\gamma\lambda)^2\delta_{t+2} +\cdots. \\]

实际 PPO for LLM 中，actor 和 critic 又可以有两种组织方式。

第一种是两个独立 Transformer：

\\[\text{Actor} = \text{Transformer}_\theta+\text{LM Head}, \\]

\\[\text{Critic} = \text{Transformer}_\phi+\text{Value Head}. \\]

这种情况下 actor 和 critic 参数完全独立。优点是 value model 可以自由学习适合价值估计的 representation，缺点是基本又多了一整个 LLM 规模的网络，显存和计算成本都很高。

第二种是共享 Transformer backbone：

\\[h_t \rightarrow \begin{cases} \text{LM Head}\rightarrow\pi_\theta(a_t|s_t),\\\ \text{Value Head}\rightarrow V_\phi(s_t). \end{cases} \\]

这种方式更加节省显存，但 actor loss 和 critic loss 会共同更新 backbone，因此二者优化存在一定耦合。

所以从结构上看，可以把 LLM PPO 最核心的 actor-critic 关系记成：

\\[\boxed{ s_t \xrightarrow{\text{Transformer}} h_t \xrightarrow{\text{LM Head}} \pi_\theta(a_t|s_t) } \\]

以及

\\[\boxed{ s_t \xrightarrow{\text{Transformer}} h_t \xrightarrow{\text{Value Head}} V_\phi(s_t) } \\]

actor 回答的是：“当前前缀下，下一个 token 应该生成什么？”、critic 回答的是：“当前已经生成到这个前缀了，从这里继续生成，未来大概能拿到多少累计 reward？”

这个结构理解清楚以后，GRPO 为什么吸引人就非常直观了：PPO 需要维护一个 critic，为每个 token 状态估计 \\(V(s_t)\\)，再计算 GAE；GRPO 则直接利用同一个 prompt 下多条 rollout 的相对 reward 构造 advantage，因此把整个 critic/value model 删掉了。

# 重要参考文献

  * 大模型强化学习（1）- 万字长文解读PPO 的起源、直觉与代码实现：<https://zhuanlan.zhihu.com/p/1990178700575130664>
  * 猛猿：<https://zhuanlan.zhihu.com/p/7461863937>



诚挚的感谢几位博主给出的优秀分享！


---
> 原文链接: https://www.cnblogs.com/zbohan/p/22727129