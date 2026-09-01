---
title: "LangChain、LangGraph和LlamaIndex 傻傻分不清楚？"
source: "https://mp.weixin.qq.com/s/1UEjlbouW8ylQ4BBI3X8jA"
---
苏三 苏三说技术 *2026年8月28日 08:21*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

最近这段时间，我们可能会经常听到：LangChain、LangGraph、LlamaIndex，但它们有什么区别呢？

这三个框架确实容易搞混——它们都跟大模型相关，都来自Python生态，而且名字还都挺像。

但如果你把它们的 **核心定位** 搞清楚，事情就简单多了。

今天这篇文章，就专门跟大家一起聊聊这个话题，希望对你会有所帮助。

最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/120fc0032d790118e773ec1a67b88378_MD5.webp)

## 一、一张图看懂三个框架的本质区别

在深入细节之前，先上一张全景图：

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/6f66eac67a5edb52bac87b13024cdb9c_MD5.webp)

这张图展示的是三个框架各自要解决的核心问题：

- **LangChain** 解决“怎么调用模型、怎么管理Prompt、怎么让模型用工具”
- **LlamaIndex** 解决“怎么加载文档、怎么建索引、怎么精准检索”
- **LangGraph** 解决“怎么管理状态、怎么处理循环、怎么恢复故障”

**三个框架各管一摊，谁也不是谁的替代品。**

下面我逐一拆解。

## 二、LangChain

它是AI应用的“乐高积木盒”。

### 2.1 它是什么？

LangChain是 **出现最早的基于LLM应用的框架** ，主打链式（Chain）结构，提供了模型调用、工具调用、智能体创建、中间件等基础能力。

它的核心定位是 **业界首个标准化大模型应用开发基础框架** 。

截至2026年，LangChain在GitHub上拥有 **95K+ Star** ，生态中集成了上百个LLM、向量数据库和工具。

**一句话说清：LangChain是一套“AI应用开发的标准零件库”——不管你做什么AI应用，大概率都能从里面找到现成的组件。**

### 2.2 LangChain的核心架构

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/e468483442839ea716213872fa69daf0_MD5.jpg)

### 2.3 代码示例

一个最简单的LangChain应用——让模型回答问题：

```
from 
            langchain.chat_models
           import ChatOpenAI
from 
            langchain.schema
           import HumanMessage

model = ChatOpenAI(model="gpt-4")
response = 
            model.invoke([HumanMessage(content=
          "什么是微服务架构？")])
print(
            response.content)
```

加上RAG检索：

```
from 
            langchain.document_loaders
           import TextLoader
from 
            langchain.text_splitter
           import CharacterTextSplitter
from 
            langchain.vectorstores
           import FAISS
from 
            langchain.embeddings
           import OpenAIEmbeddings

loader = TextLoader("
            knowledge.txt"
          )
documents = 
            loader.load()
          
text_splitter = CharacterTextSplitter(chunk_size=1000)
docs = 
            text_splitter.split_documents(documents)
          

embeddings = OpenAIEmbeddings()
vectorstore = 
            FAISS.from_documents(docs,
           embeddings)

retriever = 
            vectorstore.as_retriever()
          
docs = 
            retriever.get_relevant_documents(
          "什么是微服务？")
```

### 2.4 优缺点

**优点：**

- **生态最完善** ，集成了上百个LLM、向量数据库和工具
- **模块化设计** ，像搭乐高一样组合各种能力
- **降低入门门槛** ，让“搭一个Demo”变得极其简单

**缺点：**

- **学习曲线陡峭** ——概念太多，初学者容易迷失
- **性能开销** ——封装层多，相比原生调用有额外延迟
- **版本迭代快** ，早期版本不稳定导致一些开发者有阴影

### 2.5 适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **快速原型验证** | ✅✅✅ | 模块化设计，几天就能跑通一个Demo |
| **多模型切换/A/B测试** | ✅✅✅ | 统一接口，换模型改一行配置 |
| **需要丰富集成的项目** | ✅✅✅ | 生态最全，工具最多 |
| **生产级高性能场景** | ⚠️ 需评估 | 封装层有性能开销 |

## 三、LangGraph

它是Agent的“生产流水线”。

### 3.1 它是什么？

LangGraph是由LangChain团队开发的 **有状态循环图编排运行时** ，专为复杂LLM Agent应用而生。

它解决了一个LangChain没解决的问题： **当Agent需要循环推理、条件分支、多步工具调用时，怎么让流程既可控又可观测？**

**一句话说清：LangChain是“零件”，LangGraph是“把这些零件组装成一条可调试、可恢复的生产流水线”。**

截至2026年，LangGraph已成为LangChain生态中 **构建有状态Agent的推荐方式** ，在生产环境中被广泛采用。

### 3.2 LangGraph的工作流程

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/e8cb56e95d636c520b3edaa4eee27f70_MD5.jpg)

**关键设计：检查点（Checkpointer）机制**

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/1cdd82083b74fb1038fcaa8f6b195407_MD5.jpg)

LangGraph的检查点机制会自动保存每一步执行后的状态。

如果Agent在执行到第5步时崩溃了，重启后可以从第5步继续，而不是从头开始。

这让Agent能够运行数小时甚至数天而不丢失进度。

### 3.3 代码示例

```
from 
            langgraph.graph
           import StateGraph, END
from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[dict]
    tool_results: List[str]
    done: bool

def llm_node(state: AgentState) -> AgentState:
    # 调用LLM，决定是否需要工具
    return state

def tool_node(state: AgentState) -> AgentState:
    # 执行工具调用
    return state

def should_continue(state: AgentState) -> str:
    if state["done"]:
        return "end"
    return "tool"

graph = StateGraph(AgentState)

            graph.add_node(
          "llm", llm_node)

            graph.add_node(
          "tool", tool_node)

            graph.set_entry_point(
          "llm")

            graph.add_conditional_edges(
          "llm", should_continue, {
    "tool": "tool",
    "end": END
})

            graph.add_edge(
          "tool", "llm")  # 循环！

app = 
            graph.compile()
          
result = 
            app.invoke({
          "messages": [{"role": "user", "content": "查一下北京天气"}]})
```

### 3.4 优缺点

**优点：**

- **状态驱动** ：所有决策基于明确定义的状态，可追溯、可审计
- **检查点+中断模型** ：让生产级的长运行Agent变得可行
- **混合确定性+Agent步骤** ：手写逻辑和LLM决策可以在同一张图中混合

**缺点：**

- **学习曲线陡峭**
- **图模型有局限** ：不是所有流程都适合用图表示

### 3.5 适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **复杂Agent工作流（10+步骤）** | ✅✅✅ | 图结构天然支持复杂流程 |
| **需要审计追踪的金融/医疗场景** | ✅✅✅ | 状态可追溯、可审计 |
| **需要错误恢复和重试的系统** | ✅✅✅ | 检查点机制 |

## 四、LlamaIndex

它是RAG的“数据仓库管理员”。

### 4.1 它是什么？

LlamaIndex（原名GPT Index）是一个 **专门为RAG（检索增强生成）设计的数据框架** 。

它的核心使命是： **把非结构化数据与LLM无缝连接** 。

截至2026年，LlamaIndex在GitHub上拥有 **44K+ Star** ，通过LlamaHub提供了 **300+个数据连接器** ，覆盖Notion、Google Drive、Slack、PDF、数据库等数据源。

**一句话说清：如果LangChain是“工具箱”，LlamaIndex就是“专门管数据怎么存、怎么查的工具箱”。**

### 4.2 LlamaIndex的RAG全链路

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/c1bcd27c658f4c979e82e87596798fed_MD5.jpg)

### 4.3 代码示例

```
from 
            llama_index.core
           import SimpleDirectoryReader, VectorStoreIndex
from llama_parse import LlamaParse

# 简单版本
documents = SimpleDirectoryReader("./data").load_data()
index = 
            VectorStoreIndex.from_documents(documents)
          
query_engine = 
            index.as_query_engine()
          
response = 
            query_engine.query(
          "公司的请假流程是什么？")

# 复杂PDF使用LlamaParse
parser = LlamaParse(result_type="markdown")
documents = 
            parser.load_data(
          "./
            complex_report.pdf"
          )
index = 
            VectorStoreIndex.from_documents(documents)
```

### 4.4 优缺点

**优点：**

- **RAG领域的天花板** ，数据摄取和检索能力极强
- **开箱即用** ，几行代码就能跑通一个企业知识库
- 支持 **混合搜索、重排序** 等高级功能

**缺点：**

- **定位聚焦** ，主要解决RAG问题，通用Agent编排能力不如LangChain

### 4.5 适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **企业内部知识库** | ✅✅✅ | 90%的企业需求，LlamaIndex是王者 |
| **几百份财务报告PDF解析** | ✅✅✅ | 自动分块+多种索引 |
| **需要混合检索/重排序** | ✅✅✅ | 开箱即用 |

## 五、三个框架组合使用的最佳实践

三个框架最优雅的方案从来不是“三选一”，而是 **组合使用** ：

![图片](assets/LangChain%E3%80%81LangGraph%E5%92%8CLlamaIndex%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A%EF%BC%9F/05de76cd458c69301b74860ffbf30fa1_MD5.jpg)

**组合方案的优势：**

- **LlamaIndex做数据层** ：从各种数据源摄取文档、建立多类型索引
- **LangGraph做编排层** ：定义Agent的状态图、处理多轮推理和工具调用
- **LangChain做基础层** ：提供模型调用、工具定义、Prompt管理

## 六、详细对比总表

| 对比维度 | LangChain | LangGraph | LlamaIndex |
| --- | --- | --- | --- |
| **核心定位** | 通用LLM应用框架 | 有状态Agent编排运行时 | RAG数据框架 |
| **核心抽象** | Chain / Agent | StateGraph（状态图） | Index / Query Engine |
| **GitHub Stars** | 95K+ | 15K+ | 44K+ |
| **生态规模** | 100+集成 | LangChain生态内 | 300+数据连接器 |
| **主要优势** | 生态最全、入门快 | 状态管理、可观测性 | RAG能力最强 |
| **主要劣势** | 性能开销、学习曲线 | 学习曲线陡 | 定位聚焦 |
| **最适合** | 快速原型、多模型集成 | 生产级复杂Agent | 企业知识库、RAG |
| **开源协议** | MIT | MIT | MIT |

## 七、写在最后

回到最初的问题： **LangChain、LangGraph、LlamaIndex到底有什么区别？**

**LangChain是“零件箱”** ——提供所有基础零件，让你能快速组装AI应用。它的优势是生态全、入门快。

**LangGraph是“流水线图纸”** ——把零件组装成一条可调试、可恢复的生产流水线。它的优势是状态管理、可观测性、支持长运行Agent。

**LlamaIndex是“数据仓库管理员”** ——专门管数据怎么存、怎么查。它的优势是RAG能力最强、数据连接器最多。

这三个框架在2026年已经形成了非常清晰的分工。

**LangChain提供零件，LangGraph负责组装成流水线，LlamaIndex专门解决数据问题** 。

它们不是“三选一”的竞争关系，而是可以组合使用的互补关系。

开源地址：

- **LangChain** ： [https://github.com/langchain-ai/langchain（95K+](https://github.com/langchain-ai/langchain%EF%BC%8895K+) Star）
- **LangGraph** ： [https://github.com/langchain-ai/langgraph（15K+](https://github.com/langchain-ai/langgraph%EF%BC%8815K+) Star）
- **LlamaIndex** ： [https://github.com/run-llama/llama\_index（44K+](https://github.com/run-llama/llama_index%EF%BC%8844K+) Star）

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)