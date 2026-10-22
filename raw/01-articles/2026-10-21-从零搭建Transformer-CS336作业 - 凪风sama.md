---
title: "从零搭建Transformer-CS336作业 - 凪风sama"
source: "博客园"
url: "https://www.cnblogs.com/CrescentWind/p/23391357"
date: "2026-10-21T11:21:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 从零搭建Transformer-CS336作业 - 凪风sama

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/CrescentWind/p/23391357  
> **抓取日期**: 2026-10-21  
> **相关性评分**: 0.6

# cs336 Assignment 1

## Linear

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261019212532193-1599386676.png)

线性层的定义如上图所示，其输入为一个\\((batchsize, sequence_length, d_in)\\)维度的张量，其中：

  * \\(batchsize\\)表示一个batch中样本的数量
  * \\(sequence\\_length\\)表示每个样本的序列长度
  * \\(d\\_in\\)表示每个样本的特征维度(即`dimension input`)



比如在一个情感分类任务中，假设一个 batch 中有两条评论，每条评论分为 3 个词，每个词用一个 4 维向量表示：

  * 评论 1：“这部 / 电影 / 好看”
  * 评论 2：“剧情 / 非常 / 无聊”



那么输入张量的维度为 \\((2, 3, 4)\\)，其中：

  * \\(batchsize=2\\)，表示有两条评论
  * \\(sequence\\_length=3\\)，表示每条评论有三个词
  * \\(d\\_in=4\\)，表示每个词用一个 4 维向量表示



在线性层中，我们使用W和b来表示权重和偏置，其中：

  * W的维度为 \\((d\\_in, d\\_out)\\)，表示输入特征维度到输出特征维度的映射关系
  * b的维度为 \\((d\\_out)\\)，表示输出特征维度的偏置



则对于输入张量 \\(X\\)，线性层的输出张量 \\(Y\\) 的计算公式为：

\\[y = XW + b \\]

不难看出，在运算时，实际上是`batch`中的每个样本与`W`进行矩阵乘法，然后加上偏置`b`，最终得到输出张量`y`。而由于这两者的维度其实是不一致的：

  * X：`（batchsize, sequence_length, d_in）`
  * W：`（d_in, d_out）`
  * Y：`（batchsize, sequence_length, d_out）`



我们不妨从`y=wx+b`这个一元一次函数开始看待这个操作。

当输入输出仅有一个时，当然可以使用`y=wx+b`去描述这个线性关系。当输入有多个时，此时输入为\\(\hat{x} = [x_1\quad x_2 \quad x_3]\\)时，我们就需要三个权重去描述输出：

\\[y = w_1x_1 + w_2x_2 + w_3x_3 + b \\\ 这等价于 \\\ y = \hat{x}W + b, \qquad其中\quad W = \begin{bmatrix} w_1\\\ w_2\\\ w_3\\\ \end{bmatrix} \\]

同时，当我们有多个输出的时候，即此时输出为\\(\hat{y} = [y_1\quad y_2]\\)时, 则还需要一组权重去描述输出，那么此时的输出可以这样描述：

\\[y_1 = w_{11}x_1 + w_{12}x_2 + w_{13}x_3 + b_1 \\\ y_2 = w_{21}x_1 + w_{22}x_2 + w_{23}x_3 + b_2 \\\ 则写成矩阵形式，即为 \\\ \hat{y} = \hat{x}W + b, \qquad其中\quad W = \begin{bmatrix} w_{11} & w_{21}\\\ w_{12} & w_{22}\\\ w_{13} & w_{23}\\\ \end{bmatrix}, \quad \\]

也就是说有

\\[\begin{bmatrix} y_1\\\ y_2 \end{bmatrix} = \begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} \begin{bmatrix} w_{11} & w_{21}\\\ w_{12} & w_{22}\\\ w_{13} & w_{23}\\\ \end{bmatrix} \+ \begin{bmatrix} b_1\\\ b_2 \end{bmatrix} \\]

但是一般来说，该权重矩阵的维度并非为`输入特征维度 * 输出特征维度`，而是`输入特征维度 * 输出特征维度`，即权重矩阵的每一行为对应输入需要乘上的权重，不像上述描述的每一列为对应输出需要乘上的权重。因此此时的运算就从\\(\hat{y} = \hat{x}W + b\\)变成了\\(\hat{y} = \hat{x}W^T + b\\)，也就是变成了乘上权重矩阵的转置。

我们再回到开始的图片:

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261019212532881-694558563.png)

在上述图片中，每条连接线都代表着权重，而第一层的每个节点都代表着一个输入\\(x_i\\)，第二层的输出记作\\(v_j\\)，在不考虑偏置的情况下，那么则有：

\\[v_j = x_iW_{0}^{T} \\]

而对于最后一层的输出，不妨记作\\(y_k\\)，那么则有：

\\[y_k = v_jW_{1}^{T} \\\ 即\\\ y_k = x_iW_{0}^{T}W_{1}^{T} \\]

可以看出，这样一个网络结构的实现实际上是由两层线性层实现的。而且线性层的作用也很明确了：

> 线性层的作用，是把输入特征进行加权组合，生成新的特征。 它既可以改变特征维度，也可以在维度不变时重新组合信息。

比如在一个回归任务中，

\\[价格 = w_1 * 面积 + w_2 * 房龄 + w_3 * 楼层 \\]

通过不断学习权重\\(w_1, w_2, w_3\\)，线性层可以学习到不同特征对价格的影响程度，从而预测出更准确的房价。

同时线性层亦改变特征的维度，将其升维或者降维。

### Linear Python Torch 实现

其实现代码如下：
    
    
    import torch
    import torch.nn as nn
    from einops import einsum, rearrange
    
    # nn.Module是torch中的模块类，继承后可以使用模块的一些特性
    # 必须重载(override)构造函数(__init__())以及前向传播(forward())
    class Linear(torch.nn.Module):
        def __init__(self, in_features, out_features, device=None, dtype=None):
            super().__init__() # 初始化父类
    
            '''parameters
            in_features: int 输入特征维度
            out_features: int 输出特征维度
            device: torch.device | None = None 参数放在哪个设备上
            dtype: torch.dtype | None = None 参数的数据类型
            '''
            # 创建一个torch参数类型，使用nn.Parameter定义的张量参数在应用是，会自动开启梯度计算
            # 即这样定义的参数能直接融入torch体系
            self.w = nn.Parameter(torch.empty(out_features, in_features, device=device, dtype=dtype))
    
            # mean：均值
            # std：标准差
            mean, std = 0, (2/(in_features+out_features)) ** 0.5
    
            # trunc_normal：截断正态分布，其均值与标准差即为上面的mean与std
            # 该函数在正态分布范围内抽取随机数然后填入W中，初始化它。
            # 之所以是截断正态分布，当抽取的随机数不在区间[-3*std, 3*std](即a与b参数正是这里的左右边界)
            # 那么该参数则会重新抽取
            nn.init.trunc_normal_(self.w, mean=mean, std=std, a=-3*std, b=3*std)
            # 这样给权重一个随机、大小适中，同时避免极端值的起点，让训练更容易稳定进行。
    
    
        # 前向传播
        def forward(self, x: torch.Tensor) -> torch.Tensor:
    
            # 使用爱因斯坦求和约定即(einsum)去进行不同维度的张量运算
            y = einsum(x, self.w, "... d_in, d_out d_in -> ... d_out")
            return y
    

其中，在矩阵乘法时，使用了einsum即爱因斯坦求和约定去做，关于爱因斯坦求和约定，可见[这里](<https://www.cnblogs.com/CrescentWind/p/23305178>)。

## Embedding

对于一个`decoder=only`的现代transformer模型来说，对于其输入的语言，在进行各种操作之前，我们需要对其进行：

  * Tokenization：将语言分割成一个个token，也称为分词
  * Embedding：将每个token映射到一个向量空间中，即词嵌入
  * 


![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261019212533347-1711447111.png)

在第一步，我们会将一个句子通过某种规则去将其分为一个又一个的`token`,下面是一个例子：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261019212533733-575041453.png)

这里将`"Hello, ! 你好!"`通过分词得到了一个又一个的token，然后这些token通过对照着已有的词表，词表中存储的是tokens与其各自对应的编码，将每个token转换成对应的编码。

因此通过`tokenization`，我们将语言转化为一个个token的编码。

我们使用压缩比去描述tokenization的效果，压缩比的计算如下：

\\[压缩比 = 输入的字节数 / 输出的token数 \\]

在上面的例子中，输入的句子所占字节数如下：

内容 | 字节数  
---|---  
`Hello` | 5  
`,` | 1  
空格 | 1  
`` | 4  
`!`（半角感叹号） | 1  
空格 | 1  
`你` | 3  
`好` | 3  
`!`（半角感叹号） | 1  
**合计** | **20**  
  
而输出的token编码占用了 8 个Byte，因此压缩比为：`20 / 8 = 2.5`。当压缩比越大时，说明一个句子可以通过`tokenization`被压缩成更少的token数，这样在后续的模型中处理时，计算量也会更小。

当然，对于一个分词器，其一定能满足对于分词前后的语义保持一致性，即分词前后语义不变，也就是说分词前的句子与分词后的token编码可以随时的互相转换。否则这是一个问题。

当我们分词过程结束后，下一步就是将分好的词进行词嵌入，即Embedding。  
在分词结束后所得到的token编码是一个个整数，显然这些整数实质上与原先的词汇一样，计算机无法仅仅通过简单的编码去理解或者用数值的方法去衡量每个token之间的一些量化关系，如两个token之间的相似程度。Embedding就是来解决这个问题的。

> 一个粗糙的示例如下，这仅仅是用来演示embedding的作用，实际中embedding的维度会更高，通常为几十维甚至上百维。

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191815914-485505660.png)
    
    
    可以看到，词汇"Man"所对应的向量与词汇"royal"所对应的向量做向量加法，其结果为"King"，也就是"皇室男人" = "国王"。同理，图中有"Woman" + "royal" = "Queen"，也就是"皇室女人" = "女王"。而"Woman" - "Man" + "King" = "Queen"，也就是"女人" - "男人" + "国王" = "女王"。这说明了词嵌入的向量空间中，词汇之间的关系可以通过向量运算来表达。
    

> Embedding所做的事情是将token去映射到一个可以表达他们之间关系的向量空间中，即将每个token映射到一个向量中，这样就可以通过向量之间的距离去衡量token之间的相似程度。

当然，这个映射不是凭空产生的，也不是通过精确的数学公式直接去实现的，这部分映射如同神经网络一样，也是通过样本以及损失函数去学习的，当学习完毕后，之后我们只需要使用`token_id`也就是token编码去做查表操作即可得到这个token对应的向量表示。即

\\[\text{Embedding}[token\\_id] = \text{该token的向量表示} \\]

### Embedding Python Torch 实现

一个embedding层的实现代码如下：
    
    
    import torch
    
    class Embedding(torch.nn.Module):
        def __init__(self, num_embeddings: int, embedding_dim: int, device=None, dtype=None):
            super().__init__()
    
            '''
            num_embeddings: int 词表大小，取值范围为[0, num_embeddings-1]
            embedding_dim: int 词向量的维度，也即模型的特征维度 d_model
            device: torch.device | None = None 参数存放在那个设备上
            dtype: torch.dtype | None = None 参数的数据类型
            '''
    
            self.embed = torch.nn.Parameter(torch.empty(num_embeddings, embedding_dim, device=device, dtype=dtype))
    
            # 截断正态初始化，均值为0，标准差为0，截断区间为[-3, 3]
            torch.nn.init.trunc_normal_(self, self.embed, mean=0, std=1, a=-3, b=3)
    
    
        def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
    
            '''
            根据 token_ids 查表取向量
    
            token_ids: [batch_size, seq_len]
            return: [batch_size, seq_len, embed_dim]
            '''
    
            return self.embed[token_ids]
    

同上面的线性层一样，使用torch所提供一些基类，让这个词嵌入层能够兼容torch所提供的一些特性。对于一个词向量表，其维度可以很大，参考`HuggingFace`所提供的一些主流开源模型的参数：

模型 | 每个 token 的 embedding 维度 | 词表大小 | 官方来源  
---|---|---|---  
**DeepSeek-V4.1-Flash** | **5120** | 129,280 | [配置](<https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/config.json>)  
DeepSeek-V4-Flash | 4096 | 129,280 | [配置](<https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/config.json>)  
DeepSeek-V4-Pro | 7168 | 129,280 | [配置](<https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/config.json>)  
DeepSeek-V3.1 | 7168 | 129,280 | [配置](<https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/config.json>)  
Qwen3-8B | 4096 | 151,936 | [配置](<https://huggingface.co/Qwen/Qwen3-8B/blob/main/config.json>)  
Qwen3-32B | 5120 | 151,936 | [配置](<https://huggingface.co/Qwen/Qwen3-32B/blob/main/config.json>)  
  
以`DeepSeek-V4.1-Flash`为例，其词表大小为129,280，每个token的embedding维度为5120，那么其embedding表可以用这样一个矩阵表示：

\\[\mathbf{E} \in \mathbb{R}^{129280 \times 5120} \\\ E:Embedding表 \qquad \mathbb{R}^{129280 \times 5120}: 词表大小为129280，每个token的embedding维度为5120 \\]

即代表该模型的词嵌入矩阵E是属于一个129,280行，5120列的这个规模的矩阵。

其中，\\(E_{i}\\)表示词表中第i个token的向量表示，\\(E_{i} \in \mathbb{R}^{5120}\\)，即该token的向量表示是一个5120维的向量。

当然让我们看向最后这一行的实现：
    
    
     return self.embed[token_ids]
    

其中embed是一个这样的矩阵

\\[\mathbb{R}^{num\\_embeddings \times embedding\\_dim} \\]

也就是它的每一行对应着一个token的向量表示，而token_ids是一个二维矩阵，如\\([1, 2, 3]\\)。此时使用`embed[token_ids]`，所作的操作是将token_ids中的每个token_id作为索引去查找embed矩阵中对应的行，从而得到该token的向量表示。最终返回的结果是一个三维张量，其维度为`(batch_size, seq_len, embedding_dim)`，即每个样本中的每个token都被映射到了一个向量空间中。下面是一个例子：
    
    
    self.embed.shape == [10000, 4]  # 10000 个 token，每个向量 4 维
    
    token_ids = torch.tensor([
        [2, 5, 1],
        [0, 2, 8],
    ])  # shape: [2, 3]
    

则`self.embed[token_ids]`的结果为：
    
    
    [
        [embed[2], embed[5], embed[1]],
        [embed[0], embed[2], embed[8]]
    ]
    
    # 每个数字都被替换为了对应的向量表示，最终结果的维度为 [2, 3, 4]，即 batch_size=2, seq_len=3, embedding_dim=4
    

## Normalization

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191817561-590108692.png)

在将上面转换为Embedding之后的向量表示，输入到网络中前，其需要先进行一次归一化(Normalization)，当然，这个操作也称作标准化，但是归一化更能够体现这个操作的作用：

> 归一化的作用是将输入数据的分布调整到一个标准范围内，使得数据具有零均值和单位方差(\\(\mu=0, \sigma=1\\))，从而加快模型的收敛速度，提高训练的稳定性。

即对于一个输入向量\\(x\\)，其中有的数值可能很大，有的数值可能很小，在此后如果不做归一化处理，则很大的数值可能会主导模型的训练过程，而较小的数值则可能被忽略，从而导致模型无法有效地学习到所有特征的信息。通过归一化处理，我们可以将所有特征的数值调整到一个相对统一的范围内，使得每个特征都能在训练过程中发挥作用。

常见的归一化操作有：

  * Layer Normalization：层归一化，
  * Batch Normalization：批归一化，
  * RMS Normalization：均方根归一化。



我们定义如下：

  * B: batch_size，批大小或者说样本数，每一行为一个样本
  * d：特征维度，或者说每个样本的特征数，每一列为一个特征



即对于一个输入矩阵\\(X \in \mathbb{R}^{B \times d}\\)，他的每一行是一个样本向量，而每一列代表着一个特征维度的所有取值。当然我们可以用一个简单表格去演示这个输入：

Batch_Num | 姓名 | 性别  
---|---|---  
1 | Ruby Rose | 女  
2 | Weiss Schnee | 女  
3 | Blake Belladonna | 女  
4 | Yang Xiao Long | 女  
  
让我们忽略最左侧的Batch_Num列，这仅用来提示该行是第几个样本，而我们只看中间。可以看到每一行包含着一个人的所有信息，即`姓名`和`性别`，而每一列则包含着所有人的同一特征信息，即第一列是所有人的姓名，第二列是所有人的性别。因此这个表格可以按照上述的表述记作：

\\[X \in \mathbb{R}^{4 \times 2} \\]

  * 层归一化，Layer Normalization



\\[\mu_b=\frac{1}{d} \sum_{j=1}^{d}x_{b,j} \\\ \qquad \\\ \sigma_b^2=\frac{1}{d}\sum_{j=1}^{d}(x_{b,j}-\mu_b)^2 \\\ \qquad \\\ y_{b,j} =\gamma_j\frac{x_{b,j}-\mu_b}{\sqrt{\sigma_b^2+\epsilon}}+\beta_j \\]

对于上述的公式，实际上就是对于随机样本的进行均值以及方差的归一化，这部分需要一丁点概率论的知识。经过上述归一化后的样本，其分布将会变成均值为0，方差为1分布，即样本的数值会围绕着1上下波动，不会出现较大较小的数值。

其中

  * \\(\mu_b\\): 表示第b个样本的均值，计算方式为对该样本的所有特征求平均值
  * \\(\sigma_b^2\\): 表示第b个样本的方差，计算方式为对该样本的所有特征求方差
  * \\(\gamma_j\\): 表示第j个特征的缩放参数，学习得到的参数
  * \\(\beta_j\\): 表示第j个特征的偏移参数，学习得到的参数
  * \\(\epsilon\\): 表示一个很小的数值，防止除以零的情况发生
  * \\(y_{b,j}\\): 表示第b个样本的第j个特征归一化后的值



即整个的输出\\(Y\\)如下：

\\[Y = \begin{bmatrix} y_{1,1} & y_{1,2} & \cdots & y_{1,d} \\\ y_{2,1} & y_{2,2} & \cdots & y_{2,d} \\\ \vdots & \vdots & \ddots & \vdots \\\ y_{B,1} & y_{B,2} & \cdots & y_{B,d} \end{bmatrix} \\]

这是一个与\\(X\\)同维度的矩阵。

不难看出，层归一化时，我们横着去将**同一样本** 的所有特征值相加，然后求平均值，得到该样本的均值\\(\mu_b\\)，这些操作都是针对同一样本的特征。

> 其中，\\(\gamma_j\\)以及\\(\beta_j\\)是两个可学习的参数，也就是其数值是通过网络学习得到的，前者将归一化的结果进行缩放，后者将归一化的结果进行偏移。通过这两个参数，我们可以让网络在归一化的基础上，学习到更适合当前任务的特征分布，从而提高模型的表达能力。不难看出，这两个参数是针对每个特征，即对于不同的特征，都对应的一组\\(\gamma_j\\)以及\\(\beta_j\\)，而不是针对每个样本。

> 至于\\(\epsilon\\)，如果样本的标准差非常小或者为零，那么在归一化的过程中就会出现除以零的情况，从而导致计算结果为无穷大或者NaN。为了避免这种情况的发生，我们在计算标准差时，通常会加上一个很小的数值\\(\epsilon\\)，从而保证计算结果的稳定性。

  * 批归一化，Batch Normalization



\\[\mu_j=\frac{1}{B}\sum_{b=1}^{B}x_{b,j} \\\ \qquad \\\ \sigma_j^2=\frac{1}{B}\sum_{b=1}^{B}(x_{b,j}-\mu_j)^2 \\\ \qquad \\\ y_{b,j} =\gamma_j\frac{x_{b,j}-\mu_j}{\sqrt{\sigma_j^2+\epsilon}}+\beta_j \\]

上述公式的含义与层归一化类似，只是计算均值和方差的方式不同，批归一化是对**同一特征** 的所有样本进行归一化，即对每一列的特征值求均值和方差，然后对每个样本的该特征值进行归一化。可以看到我们公式中在变的下表不再是`b`，即代表样本数，而是`j`，即代表特征维度。当归一化的时候，同意特征的所有样本去减去矩阵的均值，然后除以标准差，这个过程在二维上即是竖着来的。

  * 均方根归一化，RMS Normalization



\\[\mathrm{RMS}(x_b) =\sqrt{\frac{1}{d}\sum_{j=1}^{d}x_{b,j}^{2}} \\\ \qquad \\\ \ y_{b,j} =\gamma_j \frac{x_{b,j}} {\sqrt{\frac{1}{d}\sum_{k=1}^{d}x_{b,k}^{2}+\epsilon}} \\]

> 均方根(Root Mean Square)，正如其名称，是先求平方，再求平均，最后开方。在实现的方向上，`RMS Normalization`与`Layer Normalization`类似，都是对同一行的所有特征进行归一化，只是计算均值和方差的方式不同。`RMS Normalization`并不去计算均值与方差，而是去计算均方根，然后每个向量去除以均方根，从而得到归一化的结果。`RMS Normalization`的计算量更小，速度更快，且在某些任务中表现更好。

相较于上面的两种归一化，`RMS Normalization`并不去调整各维度相对于零点的位置，他仅仅去控制向量的整体大小。比如一个向量整体放大十倍，即

\\[x => 10x \\\ \text{且有定律：} RMS(10x) = 10 RMS(x) \\]

因此

\\[\frac{10x}{\mathrm{RMS}(10x)} =\frac{x}{\mathrm{RMS}(x)} \\]

这抵消了整体放大十倍的影响，从而使得归一化后的向量大小不受整体放大影响。同时由于均方根归一化在计算的时候并不用去计算均值，而且在归一化时也不用去减去均值，以及不用考虑可学习的偏移参数\\(\beta\\)，因此其计算量更小，速度更快。

一个展示三种归一化特点的图像如下：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191818263-2064523174.png)

下面给出几个例子。  
取一个 **\\(2\times3\\) 的矩阵**，每行是一个样本，每列是一个特征：

\\[X= \begin{bmatrix} 1&2&3\\\ 4&5&6 \end{bmatrix} \\]

下面**不考虑 \\(\gamma,\beta\\)，也忽略 \\(\epsilon\\)**。

### ① LayerNorm：按行归一化

每行减去该行均值，再除以该行标准差。

两行的均值分别为 \\(2\\)、\\(5\\)，标准差都是 \\(\sqrt{2/3}\\)：

\\[[1,2,3]\rightarrow \frac{[1,2,3] - [2,2,2] = [-1,0,1]}{\sqrt{2/3}} \\]

\\[[4,5,6]\rightarrow \frac{[4,5,6] - [5,5,5] = [-1,0,1]}{\sqrt{2/3}} \\]

因此：

\\[\boxed{ \mathrm{LayerNorm}(X)\approx \begin{bmatrix} -1.225&0&1.225\\\ -1.225&0&1.225 \end{bmatrix} } \\]

**每一行的均值为 \\(0\\)，方差为 \\(1\\)。**

第二行只是第一行整体加了 \\(3\\)，减均值后，这个差异被消除了。

* * *

### ② BatchNorm：按列归一化

每列减去该列均值，再除以该列标准差。

三列分别是：

\\[\begin{bmatrix}1\\\4\end{bmatrix},\qquad \begin{bmatrix}2\\\5\end{bmatrix},\qquad \begin{bmatrix}3\\\6\end{bmatrix} \\]

它们的均值分别为 \\(2.5\\)、\\(3.5\\)、\\(4.5\\)，标准差都是 \\(1.5\\)。

例如第一列：

\\[\frac{ \begin{bmatrix}1\\\4\end{bmatrix} \- \begin{bmatrix}2.5\\\2.5\end{bmatrix} }{1.5} = \begin{bmatrix}-1\\\1\end{bmatrix} \\]

其余两列同理，所以：

\\[\boxed{ \mathrm{BatchNorm}(X)= \begin{bmatrix} -1&-1&-1\\\ 1&1&1 \end{bmatrix} } \\]

**每一列的均值为 \\(0\\)，方差为 \\(1\\)。**

这里展示的是使用当前批次统计量的训练阶段计算。

* * *

### ③ RMSNorm：按行除以均方根

每行直接除以该行均方根，**不减均值** 。

第一行的均方根：

\\[r_1=\sqrt{\frac{1^2+2^2+3^2}{3}} =\sqrt{\frac{14}{3}} \\]

第二行的均方根：

\\[r_2=\sqrt{\frac{4^2+5^2+6^2}{3}} =\sqrt{\frac{77}{3}} \\]

因此：

\\[\boxed{ \mathrm{RMSNorm}(X)= \begin{bmatrix} \frac1{\sqrt{14/3}}&\frac2{\sqrt{14/3}}&\frac3{\sqrt{14/3}}\\\\[6pt] \frac4{\sqrt{77/3}}&\frac5{\sqrt{77/3}}&\frac6{\sqrt{77/3}} \end{bmatrix} \approx \begin{bmatrix} 0.463&0.926&1.389\\\ 0.790&0.987&1.184 \end{bmatrix} } \\]

* * *

方法 | 操作方向 | 操作  
---|---|---  
LayerNorm | 横着，每一行 | 减行均值，除以行标准差  
BatchNorm | 竖着，每一列 | 减列均值，除以列标准差  
RMSNorm | 横着，每一行 | 直接除以行均方根  
  
### RMS Normaliztion Python Torch 实现

使用python实现的RMS Normalization层如下：
    
    
    import torch
    import torch.nn as nn
    
    
    class RMSNorm(torch.nn.Module):
        def __init__(self, d_model: int, eps: float = 1e-5, device=None, dtype=None):
            super().__init__()
    
            '''
            d_model: int 模型隐藏层的特征维度
            eps: float = 1e-5 数值稳定性的极小值，即epsilion
            device: torch.device | None = None 参数存放的设备
            dtype：torch.dtype | None = None 参数存储类型
            '''
            self.d_model = d_model
    
            # 可学习参数g(gamma)，初始化全为1，维度为1 * 特征数量，即为一个向量
            self.g = nn.Parameter(torch.ones(d_model, device=device, dtype=dtype))
            self.eps = eps
    
    
    
        def forward(self, x : torch.Tensor) -> torch.Tensor:
    
            '''
            输入形状: [..., d_model] 支持任意前置维度如(batch_size, seq_len), 最后一维为特征维度
            输出形状: [..., d_model] 与输入形状一致
            '''
            # 记录原始精度，计算式提升到float32保持稳定， 输出时还原精度
            in_dtype = x.dtype
            x = x.to(torch.float32)
    
            # 计算
    
            # 求均方根
    
            #(..., d_model) -> (..., 1)
            rms = ((x.square().sum(dim=1, keepdim=True)) / self.d_model + self.eps) ** 0.5
    
            # (..., d_model) / (..., 1) -> (..., d_model)
            # (..., d_model) * (d_model) -> (..., d_model)
            result  = x /rms * self.g
    
            return result.to(in_dtype)
    

在操作时，我们不难看到，代码中在前向传播的时候，有：
    
    
    x = x.to(torch.float32) # 将输入张量提升到float32精度，保证计算稳定性
    # then
    return result.to(in_dtype) # 最后将结果还原为输入张量的精度
    

这样操作可以使得在计算均方根归一化的时候，计算时的精度更高，减少数值误差，因为计算的时候会涉及`平方`，`求平均`，`开方`等操作，这些操作在低精度下可能会引入较大的数值误差，从而影响归一化的结果。通过将输入张量提升到float32精度，可以减少这些误差，提高计算的稳定性和准确性。

同时，我们初始化\\(\hat{\gamma}\\)这个向量为全1，这样的话，即：

\\[y_{b,j} =\gamma_j \frac{x_{b,j}} {\sqrt{\frac{1}{d}\sum_{k=1}^{d}x_{b,k}^{2}+\epsilon}}\qquad where\quad \gamma_j = 1 \\\ \qquad \\\ \qquad 即有 \\\ \qquad \\\ y_{b,j} = \frac{x_{b,j}} {\sqrt{\frac{1}{d}\sum_{k=1}^{d}x_{b,k}^{2}+\epsilon}} \\]

也就是最开始的\\(\hat{\gamma}\\)不会对归一化的结果产生任何影响。

在最后计算的时候，实际上使用了`torch`的广播机制，即：

  * `x / rms`，其中`x`的形状为`(..., d_model)`，而`rms`的形状为`(..., 1)`，在进行除法操作时，`rms`会自动广播到与`x`相同的形状，然后所作的操作即为按元素除法，从而实现了均方根归一化的操作。
  * `result = x / rms * self.g`，其中`self.g`的形状为`(d_model,)`，在进行乘法操作时，`self.g`会自动广播到与`x / rms`相同的形状，即`(..., d_model)`，然后所作的操作即为按元素乘法，从而实现了缩放操作。



## Postional Encoding

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191818759-1416149378.png)

在`transformer`架构中，上面那个一个像`太极`的一样的符号表示的是给当前的输入序列添加位置信息，即`Positional Encoding`。总所周知，在注意力机制计算`Q，K，V`时，计算的过程实际上与每个token的位置信息毫无关系，因此之后输入到网络中的张量是没有位置信息的。但是词语之间的位置信息实际上是一个很重要的特征，比如：
    
    
    - 小猫追小狗：小猫是追赶者，小狗是被追赶者
    - 小狗追小猫：小狗是追赶者，小猫是被追赶者
    

这两句话中包含着完全相同的词，但是正是由于这些词之间的位置不同，表达出了截然相反的意思。不难看出，词语之间的位置信息这一特征对于网络理解语言的语义是非常重要的，因此我们需要在输入到网络之前，将位置信息添加到输入的张量中，从而让网络能够理解词语之间的相对位置关系。

位置编码的方式大体分两种：

  * 绝对位置编码(Absolute Positional Encoding)
  * 相对位置编码(Relative Positional Encoding)



### Absolute Positional Encoding

一个很简单想法，对于一个长度为`seq_len`的序列，那么我们可以对每一个位置找到一个唯一的向量表示，然后将这个向量表示与该位置的token的向量表示进行相加，从而让网络能够理解每个token的位置。

flowchart TB subgraph A["位置 0：我"] direction LR X0["内容向量 x₀<br/>[0.20, 0.60]"] --> S0(("＋")) P0["位置向量 p₀<br/>[0.00, 1.00]"] --> S0 S0 --> H0["相加结果 h₀<br/>[0.20, 1.60]"] end subgraph B["位置 1：喜欢"] direction LR X1["内容向量 x₁<br/>[0.80, 0.10]"] --> S1(("＋")) P1["位置向量 p₁<br/>[0.84, 0.54]"] --> S1 S1 --> H1["相加结果 h₁<br/>[1.64, 0.64]"] end subgraph C["位置 2：猫"] direction LR X2["内容向量 x₂<br/>[0.40, 0.70]"] --> S2(("＋")) P2["位置向量 p₂<br/>[0.91, −0.42]"] --> S2 S2 --> H2["相加结果 h₂<br/>[1.31, 0.28]"] end H0 --> T["按顺序组成输入序列<br/>送入 Transformer"] H1 --> T H2 --> T 

注意位置向量与词嵌入向量之间并没有什么关系，位置向量通常是通过固定公式，使用位置索引去计算得到的。比如在原始版本的`transformer`中，使用了如下的公式去计算位置编码向量：

\\[ \begin{aligned} p_{i,2j}&=\sin\left(\frac{i}{10000^{2j/d}}\right)\\\ p_{i,2j+1}&=\cos\left(\frac{i}{10000^{2j/d}}\right) \end{aligned} \\]

其中

  * \\(p_{i,j}\\) 表示第 \\(i\\) 个位置的第 \\(j\\) 个维度的编码值，即对于一个使用四维向量进行`embedding`的模型，\\(p_{i} = [p_{i,0}\quad p_{i,1}\quad p_{i,2}\quad p_{i,3}]\\)
  * \\(p_{i,2j}\\) 以及 \\(p_{i,2j+1}\\) 分别表示第 \\(i\\) 个位置的偶数维度(即\\(0,2,4,...,2j\\))以及奇数维度(即\\(1,3,5,...,2j+1\\))的编码值
  * \\(d\\) 表示位置编码向量的维度，这个维度与词嵌入向量所选择的维度相同



比如还是使用四维向量进行`embedding`，那么对于第 \\(i\\) 个位置的编码向量为：

\\[p_{i} = [p_{i,0}\quad p_{i,1}\quad p_{i,2}\quad p_{i,3}] = [\sin(\frac{i}{10000^{0/4}})\quad \cos(\frac{i}{10000^{0/4}})\quad \sin(\frac{i}{10000^{2/4}})\quad \cos(\frac{i}{10000^{2/4}})] \\\ \qquad \\\ \qquad即为 \\\ \qquad \\\ p_i= \left[ \sin i,\ \cos i,\ \sin\frac{i}{100},\ \cos\frac{i}{100} \right] \\]

不难看出，该位置编码在计算时，实际上是使用两两组合的方式去进行计算的。每一个偶数位置与其下一个奇数位置相匹配，分别用一个正弦函数与一个余弦函数去计算，且每一对正弦余弦函数的频率都是不同的，随着位置索引的增大，频率会越来越小。即

\\[p_i= \left[ (\sin i,\ \cos i),\ (\sin\frac{i}{100},\ \cos\frac{i}{100}) \right] \\]

根据三角函数的知识我们不难知道，在坐标系的单位圆中，我们可以使用正弦函数sin去描述纵坐标，而使用余弦函数cos去描述横坐标。而同时亦可以使用正余弦函数的两个值描述一个点的旋转角度。而在这里，不同的位置索引\\(i\\)，会对应着不同的旋转角度，从而表现出位置的不同。

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191819251-306764321.png)

不难看出，在计算位置编码的公式中，随着特征维度增大，分母的指数会越来越大，从而使得分母的值越来越大，也就是随着特征维度的增大，该维度上三角函数的周期会变得更大，在角度表示的视角上，体现为前面的维度旋转角度变化较快，而后面的维度旋转角度变化较慢。这是非常合理的。因为若仅仅使用一种频率去描述位置，总是会有转过一圈的情况，这时候的位置编码就会出现重复的情况，而使用多种不同频率的正余弦函数去描述位置编码，则可以避免这种情况的发生。可以见下面的图片来理解一下这种所谓的`旋转`：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191820028-1370011187.png)

当然，最后我们的操作是将位置编码向量与词嵌入向量进行相加，从而得到最终的输入向量：

\\[h_i = x_i + p_i \\]

  * \\(x_i\\): 表示第 i 个位置的词嵌入向量
  * \\(p_i\\): 表示第 i 个位置的位置信息向量
  * \\(h_i\\): 表示第 i 个位置的最终输入向量，即将词嵌入向量与位置信息向量相加得到的结果



注意，自始至终，我们并没有去关注每个向量之间的相对位置关系，而是仅仅依据每个向量的绝对位置\\(i\\)去带入公式得到其位置编码向量\\(p_i\\)，然后与词嵌入向量\\(x_i\\)相加得到最终的输入向量\\(h_i\\)。因此这种方式被称为绝对位置编码(Absolute Positional Encoding)。

当然，词嵌入向量与位置向量相加，看起来是信息糅合起来了，这并不意味着信息丢失了，比如我们还是使用`小猫追小狗，小狗追小猫`为例子，假设编码的两个`小猫`分别为\\(x_1\\)以及\\(x_2\\)，显然他们的词嵌入向量是相同的，然后假设他们对应的位置编码向量分别为\\(p_1\\)以及\\(p_2\\)，则有：

\\[h_1 = x_1 + p_1 \\\ h_2 = x_2 + p_2 \\\ 且 x_1 = x_2 \\\ \\]

我们做

\\[h_1 - h_2 = (x_1 + p_1) - (x_2 + p_2) = p_1 - p_2 \\]

可以看出位置信息是可以被保留下来的。当然上面实际上只是一个演示，实际上还是将上面的东西塞入到网络中去训练，网络会学习到如何去理解这些信息，从而在后续的任务中做出正确的判断。网络真NB。

### Relative Positional Encoding

区别于绝对位置编码，`相对位置编码(Relative Positional Encoding)`更关注于每个嵌入向量之间的相对位置关系，而不是每个嵌入向量的绝对位置。也就是说，`相对位置编码`关注的是两个token之间的距离，而不是一个token到底在这个sequence的哪个位置。下面我们介绍一种相对位置编码的实现：`旋转位置编码(Rotary Positional Encoding)`，简称`RoPE`。

> RoPE的核心思想是：`旋转角度`能够表示一个token的绝对位置信息，而  
>  `旋转角度差`能够表示两个token之间的相对位置信息。前者看起来和绝对位置编码有点类似，但是后者则是绝对位置编码所不具备的。

不同于上面的绝对位置编码在输入进入到网络之前，将位置编码向量与词嵌入向量相加，`RoPE`是在计算注意力分数时，将位置编码信息融入到查询向量`Q`和键向量`V`中。其示意图如下：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191820686-734516669.png)

可以看到`Q K`向量的旁边有一个也是像太极一样的符号，这个符号表示的是将位置编码信息融入到`Q K`向量中，从而在计算注意力分数时，能够考虑到token之间的相对位置关系。

对于一系列输入\\([x_1, x_2, x_3, ..., x_n]\\)，我们取其中两个`x_m`以及`x_n`，同时他们分别对应的查询向量以及键向量为\\(q_m\\)以及\\(k_n\\)，则他们的注意力分数为：

\\[\alpha_{m,n} = q_m \cdot k_n = q_m^T k_n \\\ 同时有 \\\ q_m = W_q x_m \qquad k_n = W_k x_n \\]

然后记RoPE旋转的单位角度值为\\(\theta\\)，同时我们补充一个概念，记\\(R(\alpha)\\)为旋转矩阵，其定义如下：

\\[R(\alpha) = \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\\ \sin(\alpha) & \cos(\alpha) \end{bmatrix} \\\ 对于上述的矩阵，有 \\\ \begin{bmatrix} a\prime \\\ b\prime \end{bmatrix} = R(\alpha) \begin{bmatrix} a \\\ b \end{bmatrix} \\\ \qquad \\\ 且有 \\\ R(\alpha)^{-1} = R(-\alpha) \\\ R(\alpha)^\top = R(-\alpha) \\\ 即R为正交矩阵 \\]

其中\\(a\prime\\)和\\(b\prime\\)分别表示逆时针旋转\\(\alpha\\)角度后的新坐标，而\\(a\\)和\\(b\\)分别表示旋转前的原始坐标。同时逆时针旋转时，角度\\(\alpha\\)为正值，而顺时针旋转时，角度\\(\alpha\\)为负值。这个公式的推导十分简单，你只需要在复数域中表述旋转，然后使用欧拉公式展开整理即可。

那么所谓的`RoPE`旋转位置编码，可以对于二维向量下的\\(q_m\\)和\\(k_n\\)进行如下表述：

\\[ \tilde q_m=R(m\theta)q,\qquad \tilde k_n=R(n\theta)k \\]

此时我们带着旋转后的向量去计算注意力分数，则有：

\\[ \begin{aligned} \tilde q_m^\top\tilde k_n &=(R(m\theta)q)^\top(R(n\theta)k)\\\ &=q^\top R(m\theta)^\top R(n\theta)k\\\ &=q^\top R(-m\theta)R(n\theta)k\\\ &=q^\top R((n-m)\theta)k \end{aligned} \\]

因此，在最后的结果中，我们可以看到，注意力分数\\(\tilde q_m^\top\tilde k_n\\)的结果中除了原先的\\(q_m^\top k_n\\)之外，还参与了由旋转矩阵带来的相对位置信息，即\\(R((n-m)\theta)\\)，注意，这里的`n-m`表示的是两个token之间的相对位置关系。  
![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191821625-1768591509.png)

但是，实际上我们并不会仅仅使用一个二维向量去表示一个token的查询向量或者键向量，而是使用一个高维向量去表示一个token的查询向量或者键向量。对于高维且为偶数维的向量，进行旋转位置编码的策略为：

  * 将高维向量划分为若干个二维向量的组合，即每个向量按照奇偶分组
  * 对于每个组内的二维向量，使用上述的旋转矩阵进行旋转位置编码



\\[ f_{\\{q,k\\}}(\mathbf{x}_m,m) = \mathbf{R}_{\Theta,m}^{d} \mathbf{W}_{\\{q,k\\}} \mathbf{x}_m \\]

\\[\mathbf{R}_{\Theta,m}^{d} = \underbrace{ \begin{pmatrix} \cos(m\theta_0) & -\sin(m\theta_0) & 0 & 0 & \cdots & 0 & 0 \\\ \sin(m\theta_0) & \cos(m\theta_0) & 0 & 0 & \cdots & 0 & 0 \\\ 0 & 0 & \cos(m\theta_1) & -\sin(m\theta_1) & \cdots & 0 & 0 \\\ 0 & 0 & \sin(m\theta_1) & \cos(m\theta_1) & \cdots & 0 & 0 \\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\\ 0 & 0 & 0 & 0 & \cdots & \cos(m\theta_{d/2-1}) & -\sin(m\theta_{d/2-1}) \\\ 0 & 0 & 0 & 0 & \cdots & \sin(m\theta_{d/2-1}) & \cos(m\theta_{d/2-1}) \end{pmatrix} }_{W_m} \\\ \Theta = \left\\{ \theta_i = 10000^{-2(i-1)/d}, \quad i \in [0,1,\ldots,d/2-1] \right\\} \\]

其中：

  * \\(W_{\\{q,k\\}}\\)：查询和键的权重矩阵，则\\({\\{q_m,k_m\\}}=W_{\\{q,k\\}} x_m\\)
  * \\(\mathbf{R}_{\Theta,m}^{d}\\)：旋转矩阵，\\(d\\)表示`q/k`向量的维度，\\(m\\)表示位置索引，\\(\Theta\\)表示旋转角度的集合
  * \\(\theta_i\\)：旋转角度的计算公式，随着维度的增加，旋转角度会越来越小



我们不妨将矩阵与对应向量展开看：

\\[ \underbrace{ \begin{pmatrix} \cos(m\theta_0) & -\sin(m\theta_0) & 0 & 0 & \cdots & 0 & 0 \\\ \sin(m\theta_0) & \cos(m\theta_0) & 0 & 0 & \cdots & 0 & 0 \\\ 0 & 0 & \cos(m\theta_1) & -\sin(m\theta_1) & \cdots & 0 & 0 \\\ 0 & 0 & \sin(m\theta_1) & \cos(m\theta_1) & \cdots & 0 & 0 \\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\\ 0 & 0 & 0 & 0 & \cdots & \cos(m\theta_{d/2-1}) & -\sin(m\theta_{d/2-1}) \\\ 0 & 0 & 0 & 0 & \cdots & \sin(m\theta_{d/2-1}) & \cos(m\theta_{d/2-1}) \end{pmatrix} }_{\mathbf{R}_{\Theta,m}^{d}} \underbrace{ \begin{pmatrix} q_{m,0} \\\ q_{m,1} \\\ q_{m,2} \\\ q_{m,3} \\\ \vdots \\\ q_{m,d-2} \\\ q_{m,d-1} \end{pmatrix} }_{\mathbf{q}_m} = \underbrace{ \begin{pmatrix} q_{m,0}\cos(m\theta_0)-q_{m,1}\sin(m\theta_0) \\\ q_{m,0}\sin(m\theta_0)+q_{m,1}\cos(m\theta_0) \\\ q_{m,2}\cos(m\theta_1)-q_{m,3}\sin(m\theta_1) \\\ q_{m,2}\sin(m\theta_1)+q_{m,3}\cos(m\theta_1) \\\ \vdots \\\ q_{m,d-2}\cos(m\theta_{d/2-1}) -q_{m,d-1}\sin(m\theta_{d/2-1}) \\\ q_{m,d-2}\sin(m\theta_{d/2-1}) +q_{m,d-1}\cos(m\theta_{d/2-1}) \end{pmatrix} }_{\tilde{\mathbf{q}}_m} \\]

我们对其进一步，将每一对都写成旋转矩阵与对应向量相乘的形式：

\\[ \tilde{\mathbf{q}}_m = \begin{pmatrix} \begin{pmatrix} \cos(m\theta_0) & -\sin(m\theta_0) \\\ \sin(m\theta_0) & \cos(m\theta_0) \end{pmatrix} \begin{pmatrix} q_{m,0} \\\ q_{m,1} \end{pmatrix} \\\\[1.5em] \begin{pmatrix} \cos(m\theta_1) & -\sin(m\theta_1) \\\ \sin(m\theta_1) & \cos(m\theta_1) \end{pmatrix} \begin{pmatrix} q_{m,2} \\\ q_{m,3} \end{pmatrix} \\\\[1.5em] \vdots \\\\[1.5em] \begin{pmatrix} \cos(m\theta_{d/2-1}) & -\sin(m\theta_{d/2-1}) \\\ \sin(m\theta_{d/2-1}) & \cos(m\theta_{d/2-1}) \end{pmatrix} \begin{pmatrix} q_{m,d-2} \\\ q_{m,d-1} \end{pmatrix} \end{pmatrix} = \begin{pmatrix} R(m\theta_0) \begin{pmatrix}q_{m,0}\\\q_{m,1}\end{pmatrix} \\\\[1em] R(m\theta_1) \begin{pmatrix}q_{m,2}\\\q_{m,3}\end{pmatrix} \\\\[1em] \vdots \\\\[1em] R(m\theta_{d/2-1}) \begin{pmatrix}q_{m,d-2}\\\q_{m,d-1}\end{pmatrix} \end{pmatrix} \\]

不难看出，上面每一块都是一个二维向量与旋转矩阵相乘的形式，但是随着维度的增加，旋转角度会越来越小。（当然，如果你的下标从1开始，那么就有：

\\[\Theta = \left\\{ \theta_i = 10000^{-2(i-1)/d}, \quad i \in [1,2,\ldots,d/2] \right\\} \\]

不过这无伤大雅，经过计算后列表生成的对应数值是一样的。

### RoPE Python Torch 实现

不难看出，`RoPE`在实现时，实际上就是对一个词嵌入向量，我们知道其位置`m`，同时设定好旋转的单位角度\\(\theta\\)，然后将该向量按照奇偶分组，每一组都是一个二维向量，然后对每一组的二维向量进行旋转操作，旋转的角度为\\(m * \theta\\)，即

\\[\tilde{p_{m}} = R(m \Theta) p_m \\]

为了方便代码的数值计算，不妨将他们都拆开，且假定\\(p_m\\)为四维向量，那么此时：

  * d = 4
  * \\(\Theta = \\{\theta = 10000^{-2(i-1)/d}, i \in [1,2]\\}\\) 即 \\(\Theta = \\{\theta_1, \theta_2\\}\\)，也就是有两个子旋转矩阵



一般在矩阵中，每一行代表着一个token，则展开后

\\[p_m = [p_{m,0}, p_{m,1}, p_{m,2}, p_{m,3}] \qquad 维度为(4,) \\\ \qquad \\\ R(m\theta) = \begin{bmatrix} \cos{m\theta} \qquad \sin{m\theta}\\\ -\sin{m\theta} \qquad \cos{m\theta} \end{bmatrix} \\]

我们将\\(p_m\\)进行分组，变一下维数：

\\[p_m = \begin {bmatrix} \begin{bmatrix} p_{m, 0} \quad p_{m, 1} \end{bmatrix} \begin {bmatrix} p_{m,2} \quad p_{m,3} \end {bmatrix} \end {bmatrix} \qquad 维度为(2, 2) \\]

对于每一个奇偶分组，我们以第一组为例，记\\(p_{m,01} = [p_{m,0}, p_{m,1}]\\)

\\[\tilde{p_{m,01}}^T = R(m\theta_1) p_{m,01}^T = \begin{bmatrix} \cos(m\theta_1) & -\sin(m\theta_1) \\\ \sin(m\theta_1) & \cos(m\theta_1) \end{bmatrix} \begin{bmatrix} p_{m,0} \\\ p_{m,1} \end{bmatrix} = \begin{bmatrix} p_{m,0}\cos(m\theta_1) - p_{m,1}\sin(m\theta_1) \\\ p_{m,0}\sin(m\theta_1) + p_{m,1}\cos(m\theta_1) \end{bmatrix} \\\ \qquad \\\ 也就是说 \\\ \qquad \\\ \tilde{p_{m,01}}=[ p_{m,0}\cos(m\theta_1) - p_{m,1}\sin(m\theta_1),\quad p_{m,0}\sin(m\theta_1) + p_{m,1}\cos(m\theta_1)] \\]

也就是说，分别对于奇数的\\(p_{m,0}\\)和偶数的\\(p_{m,1}\\)，有

\\[\tilde{p_{m,0}} = p_{m,0}\cos(m\theta_1) - p_{m,1}\sin(m\theta_1) \\\ \qquad \\\ \\]

\\[\tilde{p_{m,1}} = p_{m,0}\sin(m\theta_1) + p_{m,1}\cos(m\theta_1) \\]

同理，对于第二组的\\(p_{m,2}\\)和\\(p_{m,3}\\)，有

\\[\tilde{p_{m,2}} = p_{m,2}\cos(m\theta_2) - p_{m,3}\sin(m\theta_2) \\\ \qquad \\\ \\]

\\[\tilde{p_{m,3}} = p_{m,2}\sin(m\theta_2) + p_{m,3}\cos(m\theta_2) \\]

最后的结果即为

\\[\tilde{p_m} = [ p_{m,0}\cos(m\theta_1) - p_{m,1}\sin(m\theta_1),\quad p_{m,0}\sin(m\theta_1) + p_{m,1}\cos(m\theta_1),\quad p_{m,2}\cos(m\theta_2) - p_{m,3}\sin(m\theta_2),\quad p_{m,2}\sin(m\theta_2) + p_{m,3}\cos(m\theta_2)] \\]

不难看出，上面的乘法中，偶数位置的特征值实际上仅会与cos函数相乘，而奇数位置的特征值实际上仅会与sin函数相乘。也就是说，奇数位置的特征值与偶数位置的特征值是分开计算的。我们完全可以使用这一特性去分组分别计算奇偶位置上的结果，最后再合并即可。

此时我们做如下分组：

\\[\cos(\Theta) = [\cos(\theta_1), \cos(\theta_2)] \\\ \sin(\Theta) = [\sin(\theta_1), \sin(\theta_2)] \\\ p_{m, 偶数} = [p_{m, 0}, p_{m, 2}]\\\ p_{m, 奇数} = [p_{m, 1}, p_{m, 3}] \\]

且此时

\\[p_{m, 偶数} \odot \cos(\Theta) = [p_{m, 0}\cos(\theta_1), p_{m, 2}\cos(\theta_2)] \qquad(1) \\\ p_{m, 奇数} \odot \sin(\Theta) = [p_{m, 1}\sin(\theta_1), p_{m, 3}\sin(\theta_2)] \qquad(2) \\]

则  
(1) + (2)

\\[[p_{m, 0}\cos(\theta_1) + p_{m, 1}\sin(\theta_1),\quad p_{m, 2}\cos(\theta_2) + p_{m, 3}\sin(\theta_2)] \\]

(1) - (2)

\\[[p_{m, 0}\cos(\theta_1) - p_{m, 1}\sin(\theta_1),\quad p_{m, 2}\cos(\theta_2) - p_{m, 3}\sin(\theta_2)] \\]

我们将上述得出的结果进行合并

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191822476-952314107.png)

结果即为：

\\[[p_{m,0}\cos(m\theta_1) - p_{m,1}\sin(m\theta_1),\quad p_{m,0}\sin(m\theta_1) + p_{m,1}\cos(m\theta_1),\quad p_{m,2}\cos(m\theta_2) - p_{m,3}\sin(m\theta_2),\quad p_{m,2}\sin(m\theta_2) + p_{m,3}\cos(m\theta_2)] \\]

这与我们之前得出的\\(\tilde{p_m}\\)的结果一模一样。因此，我们不需要去执行矩阵乘法去实现`RoPE`，我们仅需要进行下面的步骤：

  1. 将输入的特征矩阵奇偶分组，注意这里是特征矩阵，是很多个token的特征向量组成的矩阵，而不是单个token的特征向量



如

\\[X = \begin{bmatrix} x_{00} & x_{01} & x_{02} & x_{03} \\\ x_{10} & x_{11} & x_{12} & x_{13} \\\ x_{20} & x_{21} & x_{22} & x_{23} \\\ x_{30} & x_{31} & x_{32} & x_{33} \end{bmatrix} \\]

其中每一行表示一个token的特征向量，每一列表示一个特征维度，则奇偶分组后为：

\\[X_0 = \begin{bmatrix} x_{00} & x_{02} \\\ x_{10} & x_{12} \\\ x_{20} & x_{22} \\\ x_{30} & x_{32} \end{bmatrix} \\]

\\[X_1 = \begin{bmatrix} x_{01} & x_{03} \\\ x_{11} & x_{13} \\\ x_{21} & x_{23} \\\ x_{31} & x_{33} \end{bmatrix} \\]

  2. 根据特征矩阵的特征维度d，提前计算出每组的转角列表



即上面公式中的

\\[\Theta = \left\\{ \theta_i = 10000^{-2(i-1)/d}, \quad i = 1, 2, \ldots, d/2 \right\\} \\]

  3. 根据转角列表，分别提前计算出对应角度的sin 和 cos 列表



也就是计算

\\[\cos{\Theta} = [\cos(\theta_1), \cos(\theta_2), \ldots, \cos(\theta_{d/2})] \\\ \sin{\Theta} = [\sin(\theta_1), \sin(\theta_2), \ldots, \sin(\theta_{d/2})] \\]

  4. 将奇元素矩阵与 sin 列表进行按元素相乘(即哈达玛积)，将偶元素矩阵与 cos 列表进行按元素相乘，并将奇偶元素矩阵进行线性组合，并进行合并，得到最终的旋转位置编码后的特征矩阵



对于上述的4*4矩阵X，\\(\cos{\Theta} = [\cos(\theta_1), \cos(\theta_2)]\\)，\\(\sin{\Theta} = [\sin(\theta_1), \sin(\theta_2)]\\)

我们做如下操作：

\\[X_0 \odot \cos{\Theta} - X_1 \odot \sin{\Theta} \\\ X_0 \odot \cos{\Theta} + X_1 \odot \sin{\Theta} \\]

当然，这一步操作在实际上是不可以的，因为\\(X_0\\)和\\(X_1\\)的形状是(4,2)，而\\(\cos{\Theta}\\)和\\(\sin{\Theta}\\)的形状是(2,)，虽然在数学公式上不适用，但是在支持张量广播机制(可以看[Torch中的广播机制](<https://www.cnblogs.com/CrescentWind/p/23320347>))的python中是可以使用广播机制完成这个工作的，此时cos与sin都会自动从`(2,)`广播到`(4,2)`，然后进行按元素相乘即可:
    
    
    X_0 * cos
    
    # x_0: [[x00, x02],
    #       [x10, x12],
    #       [x20, x22],
    #       [x30, x32]]
    
    
    # cos [cos1, cos2]
    # -> 广播
    # cos [[cos1, cos2],
    #      [cos1, cos2],
    #      [cos1, cos2],
    #      [cos1, cos2]]
    

结果即为

\\[X_0 \odot \cos{\Theta} - X_1 \odot \sin{\Theta} = \begin{bmatrix} x_{00}\cos{\theta_1} - x_{01}\sin{\theta_1} & x_{02}\cos{\theta_2} - x_{03}\sin{\theta_2} \\\ x_{10}\cos{\theta_1} - x_{11}\sin{\theta_1} & x_{12}\cos{\theta_2} - x_{13}\sin{\theta_2} \\\ x_{20}\cos{\theta_1} - x_{21}\sin{\theta_1} & x_{22}\cos{\theta_2} - x_{23}\sin{\theta_2} \\\ x_{30}\cos{\theta_1} - x_{31}\sin{\theta_1} & x_{32}\cos{\theta_2} - x_{33}\sin{\theta_2} \end{bmatrix}_{4 \times 2} \\\ \quad \\\ X_0 \odot \cos{\Theta} + X_1 \odot \sin{\Theta} = \begin{bmatrix} x_{00}\cos{\theta_1} + x_{01}\sin{\theta_1} & x_{02}\cos{\theta_2} + x_{03}\sin{\theta_2} \\\ x_{10}\cos{\theta_1} + x_{11}\sin{\theta_1} & x_{12}\cos{\theta_2} + x_{13}\sin{\theta_2} \\\ x_{20}\cos{\theta_1} + x_{21}\sin{\theta_1} & x_{22}\cos{\theta_2} + x_{23}\sin{\theta_2} \\\ x_{30}\cos{\theta_1} + x_{31}\sin{\theta_1} & x_{32}\cos{\theta_2} + x_{33}\sin{\theta_2} \end{bmatrix}_{4 \times 2} \\]

我们对上述矩阵做刚才对一个token的合并操作：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191823812-176065787.png)

且记

\\[\tilde{X_{00}} = [x_{00}\cos{\theta_1} + x_{01}\sin{\theta_1}] \\\ \tilde{X_{01}} = [x_{00}\cos{\theta_1} - x_{01}\sin{\theta_1}] \\]

以此类推，上述矩阵即为

\\[\begin{aligned} X_0 \odot \cos{\Theta} - X_1 \odot \sin{\Theta} &= \begin{bmatrix} \tilde{X}_{01} & \tilde{X}_{03} \\\ \tilde{X}_{11} & \tilde{X}_{13} \\\ \tilde{X}_{21} & \tilde{X}_{23} \\\ \tilde{X}_{31} & \tilde{X}_{33} \end{bmatrix}_{4 \times 2} \\\\[1em] X_0 \odot \cos{\Theta} + X_1 \odot \sin{\Theta} &= \begin{bmatrix} \tilde{X}_{00} & \tilde{X}_{02} \\\ \tilde{X}_{10} & \tilde{X}_{12} \\\ \tilde{X}_{20} & \tilde{X}_{22} \\\ \tilde{X}_{30} & \tilde{X}_{32} \end{bmatrix}_{4 \times 2}. \end{aligned} \\]

合并，有：

\\[\tilde{X} = \begin{bmatrix} \tilde{X}_{00} & \tilde{X}_{01} & \tilde{X}_{02} & \tilde{X}_{03} \\\ \tilde{X}_{10} & \tilde{X}_{11} & \tilde{X}_{12} & \tilde{X}_{13} \\\ \tilde{X}_{20} & \tilde{X}_{21} & \tilde{X}_{22} & \tilde{X}_{23} \\\ \tilde{X}_{30} & \tilde{X}_{31} & \tilde{X}_{32} & \tilde{X}_{33} \end{bmatrix}_{4 \times 4} \\]

最后贴出代码实现：
    
    
    import torch 
    import torch.nn as nn
    from einops import rearrange
    
    class RotrayPositionalEmbedding(torch.nn.Module):
        def __init__(self, theta: float, d_k: int, max_seq_len: int, device=None, dtype=None):
            super().__init__()
            '''
            theta: float RoPE的角度值
            d_k:int 代编码的向量维度(一般指多头注意力层中的query以及key向量的维度)
            max_seq_len:int 输入的最大序列长度
            device: torch.device | None = None 存储 buffer 的设备
            '''
    
            assert d_k % 2 == 0, "RoPE要求向量维度d_k必须是偶数"
            # assert 表达式，错误信息，当捕捉到表达式的错误是会结束并返回错误信息
    
            positions = torch.arange(max_seq_len, device=device)
            # arange(max_seq_len)生成一个从0到max_seq_len-1编号的张量，即[0, 1, 2, ..., max_seq_len-1],这即为位置下标i
            # positions: (max_seq_len,)
    
            dim_indices = torch.arange(0, d_k, 2, device=device) 
            # arange(start起始, end终止, step步长)，则dim_indices = [0, 2, 4, ..., d_k - 2],这是偶数位置下标
            # dim_indices: (d_k/2,)
    
            freqs = theta ** (-(dim_indices / d_k))
            # 频率，也是旋转角度的分母
            # freqs: (d_k/2,)
    
            angle = positions[:, None] * freqs[None, :]
            # positions[:, None]，将positions使用切片操作插入新维度，前面的[:,]是取原来的所有元素，后面的None是第二个维度
            # 此时positions是(max_seq_len, 1)
            # 同理，freqs是(1, d_k/2)
            # 这样两者点积就是(max_seq_len, 1) * (1, d_k/2) = (max_seq_len, d_k/2)
            
    
            cos_table = torch.cos(angle)
            sin_table = torch.sin(angle)
            # 根据角度计算cos与sin, cos/sin_table: (max_seq_len, d_k/2)
    
            self.register_buffer("cos_table", cos_table)
            self.register_buffer("sin_table", sin_table)
            # 注册到buffer中。注册后
            # 1. 参数会跟随模型迁移到device中
            # 2. 默认随着模型保存与加载
            # 3. 不属于模型内部的参数(即nn.Parameter),仅用来查表
    
        def forward(self, x:torch.Tensor, token_positions: torch.Tensor) -> torch.Tensor:
            '''
    
            x:(..., seq_len, d_k) 输入张量，支持任意批维度
            token_posiotions: (..., seq_len) 存储每个token的位置下标
            return: (..., seq_len, d_k) 旋转位置编码后的向量，与输入形状完全一致
            '''
            cos = self.cos_table[token_positions]
            sin = self.sin_table[token_positions]
            # 查表取出对应的cos与sin，注意当使用张量查表时，相当于将原先最低维度的每个元素作为索引，将该元素换成查表得到的元素，即为输出
            # 因此此时cos:(..., seq_len, d_k/2)
    
            x1, x2 = rearrange(x, "... (half_d xy) -> ... half_d xy", xy=2).unbind(dim=-1)
            # 对输入向量重整，x1为偶数位置特征，x2为奇数位置特征
    
            x1_rot = x1 * cos - x2 * sin
            x2_rot = x1 * sin + x2 * cos
    
            x_rot = torch.stack([x1_rot, x2_rot], dim=-1)
            x_rot = rearrange(x_rot, "... half_d xy -> ... (half_d xy)")
            # 合并
            return x_rot
    

其中，`rearrange`是`einops`库中的一个函数，主要用于对张量进行重整形操作，类似于`reshape`，但是更加灵活和直观。其使用方法见[einops.rearrange的用法](<https://www.cnblogs.com/CrescentWind/p/23341206>)

这里使用`"... (half_d xy) -> ... half_d xy"`的方式将输入张量的最后一个维度拆分为两个维度，其中`half_d`表示拆分后的第一个维度，`xy`表示拆分后的第二个维度，并且指定了xy这个维度大小为2。

我们知道对于输入x，其维度一般为`{batch_size, seq_len, d_k}`，即`{样本批大小，单个样本的序列长度即token数量，每个token的特征向量维度}`，因此此时`(half_d xy) = d_k`，而指定`xy=2`，则`half_d = d_k / 2`。因此我们将X的最后一个维度的每一行的嵌入向量变成了两两分组的形式，即单看最后一维，有

\\[[x_{0}, x_{1}, x_{2}, x_{3}, ..., x_{d_k-2}, x_{d_k-1}]_{1\times d_k} \to [[x_{0}, x_{1}], [x_{2}, x_{3}], ..., [x_{d_k-2}, x_{d_k-1}]]_{(d_k/2) \times 2} \\]

最后，使用unbind函数将其沿着最后一个维度(`dim = -1`)，将X拆成两个矩阵
    
    
    (..., d_k/2, 2) -> (..., d_k/2) + (..., d_k/2)
    

其中第一个矩阵中，存放的全是每个最低维度元素中的第一个元素，第二个矩阵中，存放的是每个最低维度元素中的第二个元素。也就是我们上面所说的奇偶分组。

接着我们计算旋转后的奇偶分组特征向量
    
    
     x1_rot = x1 * cos - x2 * sin # x1_rot:(..., seq_len, d_k/2)
     x2_rot = x1 * sin + x2 * cos # x2_rot:(..., seq_len, d_k/2)
    

最后将其合并，unbind的逆操作可以使用stack函数，指定`dim=-1`，将两个矩阵沿着最后一个维度进行堆叠，得到一个新的张量，其形状为`(..., d_k/2, 2)`，然后再使用rearrange函数将其重整形为`(..., d_k)`，即恢复到原来的形状。
    
    
    x_rot = torch.stack([x1_rot, x2_rot], dim=-1)
    x_rot = rearrange(x_rot, "... half_d xy -> ... (half_d xy)")
    

这样，我们就完成了`RoPE`旋转位置编码的实现。

## MHA

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191825640-324826521.png)

MHA(Multi-Head Attention)，即多头注意力机制，是Transformer中最核心的模块之一。其主要思想是将输入的特征向量进行多次线性变换，得到多个不同的查询、键、值向量，然后分别计算注意力分数，最后将这些注意力分数加权求和，得到最终的输出向量。通过这种方式，模型可以在不同的子空间中学习到不同的特征表示，从而提高模型的表达能力。

在实现MHA之前，我们先看其最基本的形态：

`缩放点积注意力机制(Scaled Dot-Product Attention)`

众所周知，在原版的Transformer中，注意力机制的目的是通过一系列操作，对于一个输入的token，找出既含有其自身信息，又含有其他token信息的特征向量，然后用该向量代表该token进入后续的网络层进行处理。在这过程中，有着：

  * q : query，查询向量
  * k : key，键向量
  * v : value，值向量
  * \\(\alpha\\) :注意力分数，表示当前token与其他token的相关性，\\(\alpha = softmax(\frac{qk^T}{\sqrt{d_k}})\\)
  * dk : 特征维度的数量
  * o : 输出的最终向量



其公式为：

\\[ \operatorname{Attention}(Q,K,V) = \operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V \\]

此时，所谓的`缩放`，就是分母下的\\(\sqrt{d_k}\\)，而所谓的`点积`指的是分子中的\\(QK^\top\\)，即查询向量与键向量的点积。因为对于单纯的两个长度相同的一维向量来说，其点积可以用  
\\( \\\ \vec{a}\vec{b}^T = \sum_{i=1}^{n} a_i b_i \\)  
来表示，即一个向量与另一个向量的转置做矩阵乘法，最终的结果为一个标量。而\\(QK^\top\\)就是将查询矩阵\\(Q\\)与键矩阵\\(K\\)的转置做矩阵乘法：

\\[Q = \begin{bmatrix} q_1 \\\ q_2 \\\ \vdots \\\ q_n \end{bmatrix}, \quad K = \begin{bmatrix} k_1 \\\ k_2 \\\ \vdots \\\ k_n \end{bmatrix} \qquad where \quad q\in \mathbb{R}^{1 \times d_k}, k\in \mathbb{R}^{1 \times d_k} \\]

因此\\(QK^\top\\)为：

\\[QK^\top = \begin{bmatrix} q_1 k_1 & q_1 k_2 & \cdots & q_1 k_n \\\ q_2 k_1 & q_2 k_2 & \cdots & q_2 k_n \\\ \vdots & \vdots & \ddots & \vdots \\\ q_n k_1 & q_n k_2 & \cdots & q_n k_n \end{bmatrix} \\]

而注意力分数\\(\alpha_{i,j}\\)表示第i个token与第j个token的相关性，即\\(\alpha_{i,j} =softmax(\frac{q_i k_j}{\sqrt{d_k}})\\)，因此此时的注意力分数矩阵\\(A\\)为：

\\[A = \begin{bmatrix} \alpha_{1,1} & \alpha_{1,2} & \cdots & \alpha_{1,n} \\\ \alpha_{2,1} & \alpha_{2,2} & \cdots & \alpha_{2,n} \\\ \vdots & \vdots & \ddots & \vdots \\\ \alpha_{n,1} & \alpha_{n,2} & \cdots & \alpha_{n,n} \end{bmatrix} \qquad where \quad \alpha_{i,j} = softmax(\frac{q_i k_j}{\sqrt{d_k}}) \\]

那么对于值矩阵\\(V\\):

\\[V = \begin{bmatrix} v_1 \\\ v_2 \\\ \vdots \\\ v_n \end{bmatrix} \\]

且对于最后的输出向量\\(o\\)，有\\(o_i = \sum_{j=1}^n \alpha_{i,j} v_j\\)，故：

\\[O = AV = \begin{bmatrix} \alpha_{1,1} & \alpha_{1,2} & \cdots & \alpha_{1,n} \\\ \alpha_{2,1} & \alpha_{2,2} & \cdots & \alpha_{2,n} \\\ \vdots & \vdots & \ddots & \vdots \\\ \alpha_{n,1} & \alpha_{n,2} & \cdots & \alpha_{n,n} \end{bmatrix} \begin{bmatrix} v_1 \\\ v_2 \\\ \vdots \\\ v_n \end{bmatrix} = \begin{bmatrix} \alpha_{1,1}v_1 + \alpha_{1,2}v_2 + \cdots + \alpha_{1,n}v_n \\\ \alpha_{2,1}v_1 + \alpha_{2,2}v_2 + \cdots + \alpha_{2,n}v_n \\\ \vdots \\\ \alpha_{n,1}v_1 + \alpha_{n,2}v_2 + \cdots + \alpha_{n,n}v_n \end{bmatrix} = \begin{bmatrix} o_1 \\\ o_2 \\\ \vdots \\\ o_n \end{bmatrix} \qquad where \quad o_i \in \mathbb{R}^{1 \times d_v} \\]

当然，如果你要问我`q,k,v,o`是怎么来的，可以参考下面的图片：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191826869-1792689236.png)

其中，\\(W_q\\)、\\(W_k\\)、\\(W_v\\) 都是可学习的权重矩阵，也就是说它长什么样是由模型通过数据学习出来的。

以及推荐这个视频[从Transformer到大模型](<https://www.bilibili.com/video/BV15z4C6SEHT/?spm_id_from=333.788.recommend_more_video.0&trackid=web_related_0.router-related-2479604-fjzqj.1792242034786.377&vd_source=41b4153bd728e4cb4d0daa4b56eb0786>)

这里的\\(Attention(Q,K,V)\\)即为输出最终的矩阵\\(O\\)。因此，为了实现注意力机制层我们仅需要：

  * 计算对整个输入的查询矩阵Q，键矩阵K，值矩阵V
  * 实现一个softmax函数
  * 计算注意力分数\\(A = softmax(\frac{QK^T}{\sqrt{d_k}})\\)
  * 计算输出向量\\(O = AV\\)



## softmax

softmax的公式为：

\\[对\mathbf{x} = [x_1, x_2, \ldots, x_n] \in \mathbb{R}^n，softmax函数将其映射到一个概率分布上，即： \\\ \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}} \quad where \quad i=1, 2, \ldots, n \\]

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191827323-959498138.png)

不难看出\\(\sum_{i=1}^n \text{softmax}(x_i) = 1\\)，也就是经过这一操作，这个我们将这个向量的所有分量都映射到了0到1之间，并且所有分量的和为1，同时，保留了原向量中各分量的相对大小关系。

还有一个现象，就是对于  
\\(x = [x_1, x_2, \ldots, x_n] \in \mathbb{R}^n\\)，softmax函数具有平移不变性，即对于\\(c\in \mathbb{R}\\)，有

\\[{softmax}(x + c) = {softmax}(x) \\\ 即 \\\ {softmax}(x_i + c) = \frac{e^{x_i+c}}{\sum_{j=1}^n e^{x_j+c}} = \frac{e^{x_i}e^c}{\sum_{j=1}^n e^{x_j}e^c} = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}} = softmax(x_i) \\]

而若\\(\mathbf{x}\\)有比较大的分量，那么在计算\\(e^{x_i}\\)时，由于指数函数的增长性比较大，因此可能会出现数值非常大而溢出的结果。如\\(\mathbb{x} = [1, 5, 100, 10000]\\)。显然我们需要去计算\\(e^{10000}\\)，但是这是一个十分巨大的数。解决方法就是在计算softmax时，先将输入向量减去其最大值，即

\\[\text{softmax}(x - \max(x)) = \text{softmax}(x) \\]

即对于上面的向量，就有\\(\hat{x} = x-10000 = [-9999, -9995, -9900, 0]\\) 此时再去计算指数时，最大指数项为\\(e^0 = 1\\)。不会再出现数值溢出的问题

下面给出softmax函数的python实现：
    
    
    import torch
    import torch.nn as nn
    
    def softmax(x:torch.Tensor, i:int) -> torch.Tensor:
        '''
        x: 输入张量，支持任意维度
        i: int 待计算的 softmax 的维度编号
        返回形状：与x形状完全一致
        '''
        x -= x.max(dim=-1, keepdim=True)[0]
        # dim=-1：对每组最后一维的元素取最大值
        # keepdim=True：保留最后一个维度，但将其长度变为1，方便广播相减
        # [0]：max 返回“最大值、最大值的索引”，这里取最大值
        # 最终效果：每组最后一维的元素，都减去该组的最大值
    
    
        return torch.exp(x) / torch.exp(x).sum(dim=i, keepdim=True)
        # torch.exp(x)，对于每个元素计算指数
        # .sum(dim=i, keepdim=True)，对指定维度i的元素求和，并保留该维度，方便广播相除
        # 最后一步是广播相除
    

## Scaled Dot-Product Attention

\\[ \operatorname{Attention}(Q,K,V) = \operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V \\]

回到这个计算公式，我们再次看向\\(QK^\top\\)：

\\[QK^\top = \begin{bmatrix} q_1 k_1 & q_1 k_2 & \cdots & q_1 k_n \\\ q_2 k_1 & q_2 k_2 & \cdots & q_2 k_n \\\ \vdots & \vdots & \ddots & \vdots \\\ q_n k_1 & q_n k_2 & \cdots & q_n k_n \end{bmatrix} \\]

对于这个方阵，我们可以使用一个同样规格的表格去描述一些东西，

| Key0 | Key1 | Key2 | ... | Key_N  
---|---|---|---|---|---  
Query0 | \\(q_1k_1\\) | \\(q_1k_2\\) | \\(q_1k_3\\) | ... | \\(q_1k_n\\)  
Query1 | \\(q_2k_1\\) | \\(q_2k_2\\) | \\(q_2k_3\\) | ... | \\(q_2k_n\\)  
Query2 | \\(q_3k_1\\) | \\(q_3k_2\\) | \\(q_3k_3\\) | ... | \\(q_3k_n\\)  
  
每一行都表示一个查询向量与所有键向量的点积结果，这也对应着他们的名称`Query`就是用来查询自身与其他token的相关性的，而查询这一操作需要使用键`Key`去进行查询。

此时我们引入一个概念，因果性：

> 在自然语言处理中，因果性指的是模型在生成输出时，只能依赖于当前和过去的输入，而不能依赖于未来的输入。

也就是在attention的计算中，当前的token只能获取到当前token以及之前token的信息，而不能获取到之后token的信息。转换到`q, k, v`的计算上，即为当前的查询向量q仅可以计算与自身的注意力分数以及自身之前的注意力分数：

\\[\alpha_{m} = \text{softmax}\left(\frac{q_m \cdot k_n}{\sqrt{d_k}}\right) \qquad where \quad n \leq m \\]

要实现这个功能，我们只需要让对应位置的注意力分数为0即可，即：

\\[A = \begin{bmatrix} \alpha_{1,1} & 0 & 0 & \cdots & 0 \\\ \alpha_{2,1} & \alpha_{2,2} & 0 & \cdots & 0 \\\ \alpha_{3,1} & \alpha_{3,2} & \alpha_{3,3} & \cdots & 0 \\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\ \alpha_{n,1} & \alpha_{n,2} & \alpha_{n,3} & \cdots & \alpha_{n,n} \end{bmatrix}\qquad \\]

这其实是一个下三角矩阵，其上三角部分全部为0。如何让原来有值的地方变成0呢？

我们先来看softmax函数的计算公式：

\\[\mathbf{x} = [x_1, x_2, \ldots, x_n] \in \mathbb{R}^n \\\ \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}} \\]

对于\\(e^x\\)函数，我们知道它的函数图像如下：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191827706-596950918.png)

当\\(x_i \rightarrow -\infty\\)时，有\\(e^{x_i} \rightarrow 0\\)，此时其\\(softmax\\)的结果为

\\[\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}} \rightarrow 0 \\]

因此为了使得某个注意力分数为0，我们只需要在想让其为0的位置，对原先的元素加上一个负无穷大的数即可，即

\\[A = \operatorname{softmax}(S + M) \\]

\\[S + M = \underbrace{ \begin{bmatrix} q_1 k_1 & q_1 k_2 & q_1 k_3 & \cdots & q_1 k_n \\\ q_2 k_1 & q_2 k_2 & q_2 k_3 & \cdots & q_2 k_n \\\ q_3 k_1 & q_3 k_2 & q_3 k_3 & \cdots & q_3 k_n \\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\ q_n k_1 & q_n k_2 & q_n k_3 & \cdots & q_n k_n \end{bmatrix} }_{\text{QK}^T} \+ \underbrace{ \begin{bmatrix} 0 & -\infty & -\infty & \cdots & -\infty \\\ 0 & 0 & -\infty & \cdots & -\infty \\\ 0 & 0 & 0 & \cdots & -\infty \\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\ 0 & 0 & 0 & \cdots & 0 \end{bmatrix} }_{\text{因果遮罩}} = \begin{bmatrix} q_1 k_1 & -\infty & -\infty & \cdots & -\infty \\\ q_2 k_1 & q_2 k_2 & -\infty & \cdots & -\infty \\\ q_3 k_1 & q_3 k_2 & q_3 k_3 & \cdots & -\infty \\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\ q_n k_1 & q_n k_2 & q_n k_3 & \cdots & q_n k_n \end{bmatrix} \\]

这样的话，经过softmax函数后，所有上三角部分的注意力分数就会变为0。实现了因果的注意力机制。当然，上面只是演示，实际上+M这一步操作是在\\(\frac{QK^\top}{\sqrt{d_k}}\\)之后进行的。

最后的公式就变成了：

\\[\operatorname{Attention}(Q,K,V) = softmax(\frac{QK^\top}{\sqrt{d_k}} + M)V \\]

使用python代码实现如下：
    
    
    def scaled_dot_product_attention(
            q: torch.Tensor,
            k: torch.Tensor,
            v: torch.Tensor,
            mask : torch.Tensor = None
    ) -> torch.Tensor:
        '''
        q,k : (batch_size, ..., seq_len, d_k)
        v: (batch_size, ..., seq_len, d_v)
        mask: 可选布尔张量 (seq_len, seq_len)
         mask = True 代表该位置允许参与注意力权重计算,False 权重置零
        return: (batch_size, ..., seq_len, d_v)
        '''
        # scores = q @ k^T
        scores = einsum(q, k, "... seq_len1 d, ... seq_len2 d -> ... seq_len1 seq_len2")
        # 等价 scores = q @ k.T
        
        scores /= (q.shape[-1] ** 0.5)
        # q.shape = (batch_size, ..., seq_len, d_k), q.shape[-1] = d_k
    
        if mask is not None:
            scores = scores.masked_fill(mask == False, -torch.inf)
            # 对 False所对应的位置填充上负无穷
        scores = softmax(scores, -1) # 在最最后一个维度上做softmax
    
        y = einsum(scores, v, "... seq_len1 seq_len2, ... seq_len2 d -> ... seq_len1 d")
        # y = scores @ v
    
        return y
    

## Multi-Head Attention

在实现多头注意力机制之前，我们回顾一下`Embedding`层。

假设我们需要区分 A、B 两类样本，最初只使用身高作为特征：

样本 | 身高（cm） | 类别  
---|---|---  
1 | 160 | A  
2 | 170 | A  
3 | 180 | A  
4 | 160 | B  
5 | 170 | B  
6 | 180 | B  
  
![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191828094-963152291.png)

可以看出，此时实际上无法通过一个明显的阈值将A、B两类样本区分开来，也看不出来样本之间的关系或者说样本之间不同程度与相似程度。此时如果我们再加入一个特征，比如体重，如：

样本 | 身高（cm） | 体重（kg） | 类别  
---|---|---|---  
1 | 160 | 45 | A  
2 | 170 | 55 | A  
3 | 180 | 65 | A  
4 | 160 | 65 | B  
5 | 170 | 75 | B  
6 | 180 | 85 | B  
  
将这些点绘制在平面直角坐标上，有：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191828538-20848202.png)

不难看出，加入了体重这个特征后，A、B两类样本就可以明显区分开来。因此，当在低维空间中无法区分的样本，当我们将其映射到高维空间中，增加其特征维度后，就有更大的可能性将其区分开来。这部分有点类似于机器学习中的`sVM`所采用的策略。

显然，我们使用经过训练学习的`Embedding`将输入的`token`的`token_id`映射到一个高维空间中，增加了其特征维度后，`token`与`token`之间的关系就会更加明显，模型也更容易学习到这些关系。至于这些维度的特征到底是什么，实际上并不像我们之前举例的`身高、体重`一样明晰能让人看懂，实际上这些维度是`Embedding`层通过训练学习到的特征维度，可能是某种语义上的特征，也可能是某种语法上的特征，甚至可能是某种我们无法理解的特征，但是他认为这些特征可以很好的描述token之间的关系。

在之前的`缩放点积注意力`中，我们所使用的公式如下：

\\[Attention(Q,K,V) = softmax(\frac{QK^\top}{\sqrt{d_k}} + M)V \\]

其中，`QK^T`是一个`n*n`的矩阵，表示每个token与其他token的相关性。不难看出，我们所做的就是在高维空间中，计算\\(q_i\\)与\\(k_j\\)的点积，来衡量第i个token与第j个token的相关性。在计算的时候，我们其实是去考虑了所有特征维度上的相关性。

但是，为了让模型对不同的特征维度有不同的关注度，我们对\\(q_{1\times d_k}\\)与\\(k_{1\times d_k}\\)做如下操作

  * 将特征维度大小为\\(d_k\\)的向量分成h个子向量，每个子向量的维度为\\(d_k/h\\)
  * 对于每个子向量，我们记作\\(q_{i}^{(h)}\\) , \\(k_{j}^{(h)}\\) 与 \\(v_{l}^{(h)}\\)
  * 对于每个头的子向量拼接成矩阵，我们记作\\(Q^{(h)}\\)、\\(K^{(h)}\\)、\\(V^{(h)}\\)
  * 计算每个子向量的点积，得到每个头内的注意力分数矩阵\\(A^{(h)} = softmax(\frac{Q^{(h)}K^{(h)^\top}}{\sqrt{d_k/h}} + M)\\)
  * 对于每个\\(head\\)，我们去计算其对应的输出向量\\(O^{(h)} = A^{(h)}V^{(h)}\\)
  * 则暂时的输出向量为：



\\[O\prime = [O^{1}, O^{2}, \dots, O^{h}] \\]

  * 最终让其经过一个输出矩阵，将各个头的信息融合一下，得到最后的输出：



\\[O = O\prime W_{o} \\]

经过这样一番折腾，我们就实现了多头注意力机制。不难看出，采用这种`将整个特征维度分组，然后分组学习不同token之间的特定维度之间的关系`的策略，相较于原本直接计算整个特征维度的相关性，显然可以让模型学习到更细致的不同`token`之间`不同特征维度`之间的关系，从而提高模型的表达能力。

当然，在运算过程中，我们还会对每个头的\\(Q^{(h)}\\)和\\(K^{(h)}\\)进行旋转位置编码，以便模型能够捕捉到序列中token之间的相对位置信息。那么公式变为：

\\[A^{(h)} = softmax(\frac{RoPE(Q^{(h)})RoPE(K^{(h)^\top})}{\sqrt{d_k/h}} + M) \\]

一个简单演示流程如下：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191829167-2028947067.png)

其中：

  * n: token数，也就是序列长度(seq_len)
  * \\(d_{head}\\): 每个头下，维度的长度，\\(d_head\\) = \\(d_{model} / h\\)，即模型维度/头数
  * \\(d_k / h\\): 等于\\(d_{head}\\)



下面给出多头注意力机制的python实现：
    
    
    class MultiHeadSelfAttention(nn.Module):
        def __init__(self, d_model: int, num_heads: int, max_seq_len: int, rope_theta: float) -> None:
            super().__init__()
            '''
    
            d_model: int Transformer 块输入维度
            num_heads: int 注意力头数
            max_seq_len: int RoPE最大序列长度
            rope_theta: float RoPE基数频率
            '''
    
            self.d_model = d_model # 模型的特征维度
            self.d_head = d_model // num_heads # 计算每个头的向量维度
            self.num_heads = num_heads # 模型的注意力头数
    
            self.w_qkv = Linear(d_model, 3 * d_model) # 将所有头的qkv矩阵合成一个大矩阵，输出维度为out_dim = num_heads * d_head * 3
    
            self.rope = RotrayPositionalEmbedding(theta=rope_theta, d_k=self.d_head, max_seq_len=max_seq_len) if rope_theta > 0 else None
            # if theta > 0 ,才有self.rope = RotrayPositionalEmbedding(theta=rope_theta, d_k=self.d_head, max_seq_len=max_seq_len)，否则为None
            self.w_output = Linear(d_model, d_model) # 输出投影矩阵
            # 输入的是
    
        def forward(self, x: torch.Tensor, token_positions: torch.Tensor=None) -> torch.Tensor:
    
            '''
    
            : param x :输入张量，(batch_size, seq_len, d_model)
            : param token_positions: 每个token的位置下标 (batch_size, seq_len), 为None自动生成0-seq_len-1
            : return: (batch_size, seq_len, d_model)
            '''
    
            qkv = self.w_qkv(x) # (B, S, d_model)@(d_model, 3 * d_model) -> (B, S, 3 * d_model)
                                # 其中，q\k\v分别：(B, S, d_model)
            q, k ,v = torch.split(qkv, self.d_model, dim=-1)
            # 沿着最后一个维度切分，且每一个块的长度为d_model
            # 此时(B, S, 3*d_model) - > q/k/v : (B, S, d_model)
    
            # 拆分多头：
            # (batch_size, seq_len, d_model)->(batch_size, seq_len, num_heads d_head)
            # (batch_size, seq_len, num_heads d_head)->(batch_size, num_heads seq_len d_head)
            # 此时固定前两个维度，我们就可以找到对应的两个Q^i, K^j, V^k，计算其分头的注意力分数
            q = rearrange(q, "... seq (num_heads d_head) -> ... num_heads seq d_head", num_heads=self.num_heads, d_head=self.d_head)
            k = rearrange(k, "... seq (num_heads d_head) -> ... num_heads seq d_head", num_heads=self.num_heads, d_head=self.d_head)
            v = rearrange(v, "... seq (num_heads d_head) -> ... num_heads seq d_head", num_heads=self.num_heads, d_head=self.d_head)
    
            seq_len = x.shape[1]
            # x.shape -> (batch_size, seq_len, d_model)
            # x.shape[1] = seq_len
    
    
            # 对 Q、K 应用旋转位置编码
            # 初始化 RoPE 时传入 d_head，即每个注意力头的特征维度
            # 此时 Q、K 的形状为 (batch_size, num_heads, seq_len, d_head)
            #
            # RoPE 根据每个 token 的位置，对其最后一维中的特征对进行旋转
            # batch_size 和 num_heads 维度保持不变
            # 位置对应的 cos、sin 通过广播应用到各个 batch 和各个头上
            # 同一位置在不同头中使用相同的旋转角度，旋转各头自己的向量
            if self.rope is not None:
                if token_positions is None:
                        token_positions = torch.arange(seq_len, device=x.device)
                q = self.rope(q, token_positions)
                k = self.rope(k, token_positions)
            
            # 使用torch.tril构造下三角矩阵
            mask = torch.tril(torch.ones((seq_len, seq_len), device=q.device)).bool()
    
            # 去计算缩放点积注意力，其广播机制同上
            # 结果为[O^1, O^2, ..., O^h]
            output_head = scaled_dot_product_attention(q, k, v, mask)
    
            # 还原原始输入矩阵维度
            output_head = rearrange(output_head, "... num_heads seq d_head -> ... seq (num_heads d_head)")
            # 经过输出矩阵Wo
            output = self.w_output(output_head)
    
            return output
    

## FFN

在经过多头注意力机制后的输出，最后还需要经过一个前馈神经网络(Feed Forward Network, FFN)进行处理。

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191829686-1345471879.png)

在这一层中，我们所做的就是将每个token的特征向量，经过数个全连接层以及激活函数的处理，得到一个新的特征向量。注意，在`FFN`中，我们并没有做任何操作去融合各个token之间的信息，而是针对**一个** token中的不同维度进行信息的加权处理。当然，线性层的本质上就是一个巨大的加权矩阵。

当然，类比于前文中的介绍，`FFN`将较低维度下的特征向量映射到高维空间中，增加了其特征维度后，原本维度下可能混杂的特征，在高维空间中就**可能** 会更加的清晰，然后再对这些高维空间下的特征向量进行加权处理并学习，模型就能学到更多的特征信息。

在原版`Transformer`中，`FFN`的结构为：

graph TD A[输入向量] --> B[线性变换 W1] B --> C[激活函数 ReLU] C --> D[线性变换 W2] D --> E[输出向量] 

使用公式即为：

\\[\operatorname{FFN}(x)=ReLU(xW_1+b_1)W_2+b_2 \\]

其中输入的向量经过第一个线性层进行升维，升维的大小一般是输入向量的倍数扩展。在原版`Transformer`中，升维的大小是输入向量的4倍，我们使用\\(d_{ffn}\\)表示FFN的隐藏层的维度，使用\\(d_{model}\\)表示输入向量的维度，因此有\\(d_{ffn} = 4d_{model}\\)， 我们定义\\(r = \frac{d_{ffn}}{d_{model}}\\)，这反映了FFN的升维比例，同时也可以反映出FFN中参数的规模。在实现中，取\\(d_{model} = 512\\)，则\\(d_{ffn} = 2048\\)。升维之后，经过激活函数ReLU进行非线性变换，最后再经过一个线性层将其降维回原来的维度\\(d_{model}\\)，得到输出向量。这里我们仅仅是对一个token的特征向量进行处理，实际上在运算的时候所有token的特征向量会拼成矩阵，批量的及行并行的运算。

在后续的改进中，在零点处不可导的`ReLU`被`SiLU`所替代，`SiLU`的公式为：

\\[\operatorname{SiLU}(x) = x \cdot \sigma(x) \qquad where \quad \sigma(x) = \frac{1}{1 + e^{-x}} \\]

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191830118-789017787.png)

同时，`FFN`的结构也不再是单纯的两层线性层，而是引入了门控的机制，也就是通过一个门控(Gate)函数来控制另一条路径的输出，我们期待门控的分支去学习对于不同的特征，该如何调整他的最终权重；同时其他另一条分支去学习如何提取融合`同一token中`的不同维度信息。

在门控机制下，使用上面的`SiLU`作为激活函数，产生的结构叫做`Swish-Gated Linear Unit`，简称`SwiGLU`，使用`SwiGLU`的FFN层的数学公式表达如下：

\\[ \operatorname{FFN}_{\mathrm{SwiGLU}}(x) =\bigl[\operatorname{SiLU}(xW_1)\odot(xV)\bigr]W_2 \\]

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191830488-633267334.png)

不难看出，`SwiGLU`的FFN层中，使用了三个线性层，分别是\\(W_1\\)、\\(V\\)、\\(W_2\\)，这也意味着相较于原版的\\(W_1\\)和\\(W_2\\)，模型的参数量会增加一倍。相较于原先的\\(r = d_{ffn}/d_{model} = 4\\)，为了使得模型的参数量不会过大，考虑参数量的平衡：

\\[\begin{aligned} &\text{原版 FFN：}\\\ &W_1 \in \mathbb{R}^{d_{model}\times d_{ffn}} = \mathbb{R}^{d_{model}\times 4d_{model}}\\\ &W_2 \in \mathbb{R}^{d_{ffn}\times d_{model}} = \mathbb{R}^{4d_{model}\times d_{model}}\\\\[6pt] &\text{忽略偏置，参数量为：}\\\ &P_{\text{FFN}} = d_{model}\times 4d_{model} \+ 4d_{model}\times d_{model} = 8d_{model}^{2}\\\\[10pt] &\text{使用 SwiGLU：}\\\ &W_1,V \in \mathbb{R}^{d_{model}\times d_{ffn}}, \qquad W_2 \in \mathbb{R}^{d_{ffn}\times d_{model}}\\\\[6pt] &\text{参数量为：}\\\ &P_{\text{SwiGLU}} = d_{model}\times d_{ffn} \+ d_{model}\times d_{ffn} \+ d_{ffn}\times d_{model} = 3d_{model}d_{ffn}\\\\[10pt] &\text{若保持参数量不变，则：}\\\ &3d_{model}d_{ffn}=8d_{model}^{2} \quad\Rightarrow\quad d_{ffn}=\frac{8}{3}d_{model}\\\\[6pt] &\text{因此，扩展比率为：}\\\ &r=\frac{d_{ffn}}{d_{model}} =\frac{8}{3}\approx 2.67 \end{aligned} \\]

因此对于`SwiGLU`的FFN层，我们将其升维比例从原先的4倍降低为\\(\frac{8}{3}\\)倍，来保证模型的参数量不会过大。当然，为了方便GPU并行计算，\\(d_{ffn}\\)通常会在此基础上近似到64的倍数。

下面是不同版本的FFN层的结构图：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191830932-764618572.png)

下面我们给出`SwiGLU`的FFN层的python实现：
    
    
    import torch
    import torch.nn as nn
    from module1_Linear import Linear
    
    class FFN(torch.nn.Module):
        def __init__(self, d_model: int, d_ff: int=512, device=None, dtype=None):
            super().__init__()
            '''
            d_model: int 模型隐藏层/词向量的维度
            d_ff: int 前馈网络中间层的维度
            device: torch.device | None = None 参数存放设备
            dtype: torch.dtype | None = None 参数的数据类型
            '''
    
            self.d_ff = 64 * (8 * d_model // 3 // 64)
            # // : 向下取整的除法
            # 向下取整到64的倍数：d_model * 8 //3 // 64 计算的是向下取整的8/3 * d_model然后求其有多少个64并再次向下取整
            # 最后用这个系数乘以64，保证结果是64的倍数
            self.w1, self.v = Linear(d_model, self.d_ff, device=device, dtype=dtype), Linear(d_model, self.d_ff, device=device, dtype=dtype)
            # w1 ,v (d_model, d_ff)
            self.w2 = Linear(self.d_ff, d_model, device=device, dtype=dtype)
            # w2 (d_ff, d_model)
    
        def forward(self, x: torch.Tensor) -> torch.Tensor:
    
            '''
            FFN(x) = W2(SiLU(W1*X) hadama积 (V*X))
            x: (batch_size, seq_len, d_model)
            return: (batch_size, seq_len, d_model)
            '''
    
            y1 = self.w1(x)
            # sigmoid = 1/(1+e^(-x))
            # y1 * torch.sigmoid(y1) = SiLU(x w1)
            y13 = y1 * torch.sigmoid(y1) * self.v(x)
            # SiLU(x*w1) hardama v*x
    
            # w2(SiLU(x*w1) hardama v*x)
            return self.w2(y13)
    

## Transformer Block

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191834790-1621912482.png)

回到上面的这张图，我们可以使用之前的所有组件去搭建`Transformer Block`了。

代码如下:
    
    
    import torch
    import torch.nn as nn
    from module2_embedding import Embedding
    from module3_RMSNormalization import RMSNorm
    from module4_RoPE import RotrayPositionalEmbedding
    from module5_MHA import MultiHeadSelfAttention
    from module6_FFN import FFN
    
    class TransformerBlock(nn.Module):
        def __init__(self, d_model: int, num_heads: int, d_ff: int, max_seq_len: int, rope_theta: float) -> None:
            super().__init__()
    
            # 因果注意力加残差连接
    
            self.mha = MultiHeadSelfAttention(d_model, num_heads, max_seq_len, rope_theta)
            self.pre_norm1 = RMSNorm(d_model) # 子层1的前置归一化
    
            # FFN加残差连接
    
            self.ffn = FFN(d_model, d_ff)
            self.pre_norm2 = RMSNorm(d_model)# 子层2的前置归一化
    
    
    
        def forward(self, x: torch.Tensor) -> torch.Tensor:
    
            '''
            input: (batch_size, seq_len, d_model)
            output: (batch_size, seq_len, d_model)
            '''
    
            x = x + self.mha(self.pre_norm1(x))
            # 前置归一化 -》 MHA -》残差连接
            y = x + self.ffn(self.pre_norm2(x))
            # 前置归一化 -》 FFN -》残差连接
    
            return y
    

### 补充：残差连接

对于神经网络来说，一个简单的直觉是：网络的层数越深，参数越多，模型能够学习到的特征就越多，能够拟合的函数就越复杂，模型的表达能力就越强。然而，实际情况却并非如此。随着网络层数的增加，模型的训练误差反而会增大，模型的性能反而会下降。这种现象被称为退化问题。

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191835309-161775211.png)

在2015年，何恺明等人为解决深度神经网络的退化问题，在论文《Deep Residual Learning for Image Recognition》中提出了残差网络(ResNet)的概念，同时引入了残差连接这一结构。

残差连接(Residual Connection)通过跨层连接将输入直接传递到输出，从而使得网络能够学习到残差函数，而不是直接学习原始函数。可以用下面的图片来描述一个简单的残差连接结构：

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191835756-153236309.png)

\\[y = x + F(x) \\]

普通网络模块直接学习从输入 \\(x\\) 到输出 \\(y\\) 的目标映射 \\(H(x)\\)：

\\[ y=H(x) \\\ 残差连接则将这个映射改写为：\\\ y=H(x)=x+F(x)\\\ 因此，需要学习的部分变为：\\\ F(x)=H(x)-x \quad or \quad F(x)= y - x \\]

在统计学中，残差通常指观测值与预测值之差。残差网络借用了这种“差值”的思想：以恒等映射 \\((x)\\) 为基准，让网络学习目标输出相对于输入的修正量 \\((F(x))\\)，最后将修正量加回输入，得到输出。

恒等映射，即存在一个线性映射\\(\mathcal{A}\\)使得\\(\mathcal{A}(x) = x\\)，即映射恒为自身，那么这就是一个恒等映射。说白了就是这层网络的作用就是去将上一层网络给塞进来的输入直接输出出去，因为有时候某些层其实对任务是无贡献的。

对于普通的网络来说，通过\\(y = H(x)\\)去拟合一个恒等映射是非常困难的，通常还不如直接输出\\(x\\)，而残差连接则通过\\(y = x + F(x)\\)的形式，将学习恒等映射的问题转化为学习一个零映射的问题，即\\(F(x) = 0\\)，此时即使最坏的输出也不会比输入差多少，模型的性能也不会下降太多。

同时，在反向传播的时候，有：

\\[\frac{\partial y}{\partial x} = \frac{\partial F(x)}{\partial x} \+ 1 \\]

也就是其梯度的导数中有一个恒定的梯度1，这样就可以缓解梯度消失的问题。

## Transformer Model

最后，将之前所有的组件组合起来，就可以搭建一个完整的`Transformer`模型了。

![alt text](https://img2024.cnblogs.com/blog/3147612/202610/3147612-20261021191825640-324826521.png)

代码如下：
    
    
    import torch
    import torch.nn as nn
    from module1_Linear import Linear
    from module2_embedding import Embedding
    from module3_RMSNormalization import RMSNorm
    from module4_RoPE import RotrayPositionalEmbedding
    from module5_MHA import MultiHeadSelfAttention
    from module6_FFN import FFN
    from module7_transformer_block import TransformerBlock
    
    
    class TransformerLM(nn.Module):
        def __init__(
            self,
            d_model: int,
            num_heads: int,
            d_ff: int,
            vocab_size: int,
            context_length: int,
            num_layers: int,
            rope_theta: float
        ) -> None:
            super().__init__()
            '''
    
            d_model: Transformer块的输入维度
            num_heads: 多头自注意力头数
            d_ff: 前馈网络中间层维度
            vocab_size: 词表大小，决定词元嵌入矩阵维度
            context_length: 最大上下文长度,决定RoPE的缓存长度
            num_layers: Transformer 块的堆叠层数
            rope_theta: RoPE 基数频率
            '''
    
            self.embed = Embedding(vocab_size, d_model)
            self.transformerBlocks = nn.Sequential(
                *[TransformerBlock(d_model, num_layers, d_ff, context_length, rope_theta=rope_theta) for _ in range(num_layers)]
            )
            # 列表推导式：[元素 for _ in range(2)] = [元素, 元素]
            # nn.Sequential:将多个层打包，并按顺序依次执行，前层输出给到后层输入
            # *[]参数解包，print(*[1 1 1 1]) = print(1, 1, 1, 1)
    
            self.final_norm = RMSNorm(d_model) # 最终归一化
            self.llm_head = Linear(d_model, vocab_size) # 输出投影
    
        def forward(self, tokens: torch.Tensor) -> torch.Tensor:
            '''
            input: (batch_size, seq_len), 整数token IDs
            output: (batch_size, seq_len, vocab_size) 下一个token 的logits  
            '''
            x_embed = self.embed(tokens) # 词嵌入，(B, S) -> (B, S, d_model)
            x_blocks =self.transformerBlocks(x_embed) # (B, S, d_model) -> (B, S, d_model)
            llm_output = self.llm_head(self.final_norm(x_blocks)) # (B, S, d_model) -> (B, S, vocab_size)
            return llm_output
    
    # test code，测试以下输入输出维度是否匹配
    batch_size, seq_len = 2, 16
    d_model, num_heads, d_ff = 128, 8, 512
    vocab_size, context_length, num_layers = 10000, 128, 4
    rope_theta = 10000.0
    
    model = TransformerLM(
        d_model=d_model,
        num_heads=num_heads,
        d_ff=d_ff,
        vocab_size=vocab_size,
        context_length=context_length,
        num_layers=num_layers,
        rope_theta=rope_theta
    )
    
    tokens = torch.randint(0, vocab_size,(batch_size, seq_len))
    logits = model(tokens)
    print(f"输入形状:{tokens.shape}, 输出形状{logits.shape}")
    

此时，模型的输出是形状为(batch_size, seq_len, vocab_size)的张量，表示对于输入的token序列，模型预测的下一个token的logits。即模型会对词表中每个位置上的token的概率进行打分，这个输出经过一层softmax后，就可以得到每个token的概率分布。

> **参考资料**
> 
>   * [跟着Stanford动手学大模型blog](<https://ncnwr8o2w69j.feishu.cn/wiki/UqOfwSeryigq9fkfXFqc7ZLGnKd>)
>   * [跟着Stanford动手学大模型b站](<https://www.bilibili.com/video/BV1NV8t6AE4T/?spm_id_from=333.788.videopod.episodes&vd_source=41b4153bd728e4cb4d0daa4b56eb0786&p=5>)
>   * [台大李宏毅自注意力机制和Transformer详解](<https://www.bilibili.com/video/BV1v3411r78R/?share_source=copy_web&vd_source=854bd73c3d7409be42d762a08bc81361>)
>   * [十分钟读懂旋转位置编码RoPE](<https://zhuanlan.zhihu.com/p/647109286>)
>   * [transformer 的多头注意力计算说明](<https://blog.csdn.net/rstroller/article/details/149945244>)
>   * [多头注意力 MultiHeadAttention 是什么](<https://www.bilibili.com/video/BV1of6cBAEuJ/?share_source=copy_web&vd_source=854bd73c3d7409be42d762a08bc81361>)
>   * [探秘Transformer系列之（13）--- FFN](<https://www.cnblogs.com/rossiXYZ/p/18765884>)
>   * [大模型回归基本功之6——FFN / MoE](<https://zhuanlan.zhihu.com/p/2016209652937942819>)
>   * [残差连接（Residual Connection）：从直觉困境到现代神经网络的核心结构](<https://kingson4wu.github.io/zh/posts/20260130-residual-connection/>)
>   * [残差链接（Residual Connection）](<https://zhuanlan.zhihu.com/p/1992918095468188119>)
>   * [【闪客】一小时从 Transformer 到大模型！](<https://www.bilibili.com/video/BV15z4C6SEHT/?share_source=copy_web&vd_source=854bd73c3d7409be42d762a08bc81361>)
>   * [Attention Is All You Need](<https://arxiv.org/pdf/1706.03762>)
>   * [GLU Variants Improve Transformer](<https://arxiv.org/pdf/2002.05202>)
>   * [Deep Residual Learning for Image Recognition](<https://arxiv.org/pdf/1512.03385>)
> 



---
> 原文链接: https://www.cnblogs.com/CrescentWind/p/23391357