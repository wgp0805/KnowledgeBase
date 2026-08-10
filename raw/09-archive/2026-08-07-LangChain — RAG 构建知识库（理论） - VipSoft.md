---
title: "LangChain — RAG 构建知识库（理论） - VipSoft"
source: "博客园"
url: "https://www.cnblogs.com/vipsoft/p/22316657"
date: "2026-08-07T09:11:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# LangChain — RAG 构建知识库（理论） - VipSoft

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/vipsoft/p/22316657  
> **抓取日期**: 2026-08-07  
> **相关性评分**: 0.7

目录

  * 构建知识库
    * 文档加载（Document Loaders）
      * TextLoader
      * WebBaseLoader
      * CSVLoader
      * PDF
    * 文本切分（Text Splitters）
      * 递归字符切分（推荐）
      * 固定长度切分
      * 结构感知切分
    * 向量化（Embeddings）
      * Ollama Embeddings
      * DashScope Embeddings（阿里云百炼）
    * 向量库
      * 初始化向量库-Chroma
      * 添加/删除文档
      * 检索文档
    * 检索器（Retriever）
      * VectorStore转Retriever
      * 其它Retriever
    * 总结



RAG（**R** etrieval-**A** ugmented **G** eneration，检索增强生成）是LangChain的核心应用场景之一。它通过从外部知识库检索相关信息来增强LLM的回答质量。

一个完整的RAG流程分为两大部分：

  * 知识库构建：加载文档 → 切分文本 → 向量化 → 存入向量库
  * 检索生成：用户提问 → 向量化 → 检索相关文档 → 拼接上下文 → 生成回答



[LangChain — RAG 构建知识库（实操）](<https://www.cnblogs.com/vipsoft/p/22065225>)

## 构建知识库

![image](assets/2026-08-07-LangChain%20%E2%80%94%20RAG%20%E6%9E%84%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93%EF%BC%88%E7%90%86%E8%AE%BA%EF%BC%89%20-%20VipSoft/d66d50df3047991712248e08e508d20f_MD5.png)

### 文档加载（Document Loaders）

LangChain提供了丰富的文档加载器（Document Loaders），支持从各种来源加载文档，例如：

  * Webpages: 将网页内容加载为Document，例如WebBaseLoader
  * PDFs: 将PDF文件加载为Document，例如PyPDF
  * CommonFiles: 各种常见文件类型加载为Document，例如TextLoader、CSVLoader
  * Social platforms: 从社交媒体加载文档，例如Twitter、Reddit
  * Messaging services: 从消息平台加载文档，例如Telegram、WhatsApp、Discord
  * Productivity tools: 从常用的生产力工具中加载文档，例如Figma、Github、Slack  
更多文档加载器参考LangChain官网：<https://docs.langchain.com/oss/python/integrations/document_loaders#all-document-loaders>



虽然加载器各不相同，但都实现了BaseLoader接口，因此都具有两个通用方法：

  * load() : 一次性加载所有文档
  * lazy_load() : 基于流式传输懒加载文档，适用于大数据集



所有加载器都将原始数据转换为统一的 Document 对象，包含：

  * page_content: 文档内容
  * metadata: 元数据（如来源、页码等）



#### TextLoader

TextLoader是社区提供的加载器，作用是加载普通的txt文件，这也是最常见的一种文本文件类型，格式简单，没什么好说的，直接看代码。
    
    
    # uv add langchain_community
    
    from pathlib import Path
    from langchain_community.document_loaders import TextLoader
    
    # 获取脚本所在目录，确保路径正确
    BASE_DIR = Path(__file__).parent
    resources_dir = BASE_DIR / "resources"
    resources_dir.mkdir(exist_ok=True)  # 自动创建目录（如果不存在）
    file_path = resources_dir / "sample.txt"
    
    
    # 创建示例文本文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("LangChain 像一条自动化的流水线，解决“自动化”问题。\n")
        f.write("LangGraph 不仅有记忆还懂得反复思考，能开会讨论的决策室。解决“自主化”问题。\n")
        f.write("LangSmith 是调试监控平台。\n")
    
    # 加载文本文件
    loader = TextLoader(str(file_path), encoding="utf-8")
    docs = loader.load()
    
    print(f"加载了 {len(docs)} 个文档")
    print(f"内容: {docs[0].page_content}")
    print(f"元数据: {docs[0].metadata}")
    

#### WebBaseLoader

WebBaseLoader同样是社区提供的加载器，只要给一个url地址，它就能自动读取网页内容，去掉无用的Html、CSS、JS元素，只保留普通文本数据。
    
    
    # uv add langchain_community
    # uv add beautifulsoup4
    from langchain_community.document_loaders import WebBaseLoader
    
    # 加载网页内容
    loader = WebBaseLoader(
        web_paths=["https://docs.langchain.com/oss/python/langchain/rag"],
    )
    docs = loader.load()
    
    print(f"加载了 {len(docs)} 个文档")
    print(f"来源: {docs[0].metadata.get('source', 'unknown')}")
    print(f"内容长度: {len(docs[0].page_content)} 字符")
    print(f"内容预览: {docs[0].page_content[:200]}...")
    

#### CSVLoader

CSVLoader也是社区提供的加载器，它可以加载csv格式的文件，示例代码：
    
    
    from langchain_community.document_loaders.csv_loader import CSVLoader
    
    # 创建示例CSV文件
    import csv
    with open("resources/sample.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "description", "category"])
        writer.writerow(["LangChain", "LLM应用开发框架", "AI框架"])
        writer.writerow(["LangGraph", "图结构编排库", "AI框架"])
        writer.writerow(["LangSmith", "调试监控平台", "AI工具"])
    
    # 加载CSV文件
    loader = CSVLoader(
        file_path="resources/sample.csv",
        source_column="name",  # 用name列作为source
        encoding="utf-8"
    )
    docs = loader.load()
    
    print(f"加载了 {len(docs)} 行数据")
    for doc in docs:
        print(f"  [{doc.metadata.get('source', '?')}] {doc.page_content[:100]}")
    

#### PDF

[MinerU](<https://www.cnblogs.com/vipsoft/p/20766758>) 是国人开发，可以本地部署使用，不管是处理速度还是精度都非常优秀。推荐使用。  
注册地址：<https://mineru.net/>  
MinerU - 入门使用：<https://www.cnblogs.com/vipsoft/p/20766758>  
*如何获取 Token： 访问 mineru.net → 注册 → 进入「API管理 → Token」→ 复制。MinerU官网提供了每日免费 2000 页高优先级额度。完整 API 参数请查阅 官方文档，本教程只在实战中用到时才展开。

  * SDK : 原生SDK，兼容性最好，可以自由的处理MinerU解析好的markdown、images、json
  * LangChain : 完美适配LangChain，但解析PDF时只能得到markdown，其它内容无法获取



对于扫描件类型的PDF，MinerU处理起来也毫不费力，只需要把OCR参数改为True即可：
    
    
    loader = MinerULoader(
        source="./resources/small_ocr.pdf",
        mode="precision",
        ocr= True
    )
    

MinerU不仅处理PDF是一把好手，它也能处理Html、ppt、pptx、doc、docx、xls、xlsx、图片等多种格式，理论上有这一种加载器就能满足90%的企业需求了。

### 文本切分（Text Splitters）

LLM的上下文窗口有限，不能将加载的整个文档扔进去，需要将文档切分成合适大小的块（chunk）  
这可不能随意，因为切分大小会直接影响检索质量：

  * 太大: 包含过多无关信息，检索精度下降
  * 太小: 丢失上下文，语义不完整  
常见的文档切分策略如下：

策略名称 | 核心原理 | ✅ 优点 | ❌ 缺点 | 适用场景  
---|---|---|---|---  
​固定长度切分​​​ | ​按预设字符数或Token数切分​​ | ​实现简单，速度快，可预测。​​ | ​易在句子中间截断，严重破坏语义完整性。​​ | ​日志、代码等结构不敏感文本；或作为性能基线。​​  
​递归切分​​ | ​按优先级分隔符（如段落\n\n > 句子。）逐级递归分割，直至满足大小要求。​​ | ​尊重文档结构，语义完整性好，能动态调整。​​ | ​对无标准分隔符的文本效果下降。​​ | ​通用首选，适用于报告、文章等大多数规范文档。​​  
​语义切分​​ | ​用嵌入模型计算相邻句子相似度，在低于阈值时切分，识别主题转折点。​​ | ​最大限度保持语义连贯性，分块质量高。​​ | ​计算成本高，依赖嵌入模型精度。​​ | ​对语义完整性要求极高的场景，如学术论文、法律文件。​​  
​结构感知切分​​ | ​利用文档元数据（如Markdown/HTML标题）识别逻辑区块进行切分。​​ | ​天然符合文档组织逻辑，结构清晰准确。​​ | ​需要格式良好的文档，灵活性受限。​​ | ​Markdown、网页等有清晰原生结构的文档。​​  
​滑动窗口切分​​ | ​固定窗口，通过高重叠率（如20%）滑动生成连续分块，保留上下文。​​ | ​上下文连接紧密，避免信息断裂。​​ | ​冗余度高，存储和计算开销大。​​ | ​可以与其它策略结合​​  
  
LangChain对常见的切分策略都有支持，并且提供了统一的接口：TextSplitter  
需要安装langchain-text-splitters依赖：
    
    
    uv add langchain-text-splitters
    

#### 递归字符切分（推荐）

LangChain中提供了一个RecursiveCharacterTextSplitter类，实现了递归字符切分。这是LangChain推荐的通用文本切分器，在不超过目标块大小的前提下，尽可能保持段落和句子的完整性。  
关键参数如下：

参数 | 作用 | 默认值 (通常情况)  
---|---|---  
​chunk_size​​ | ​目标块大小 (以字符/token计)。分割器努力让每个块的文本长度不超过这个值。​​ | ​4000​​  
​chunk_overlap​​ | ​块间重叠长度。为了让块与块之间保留一些共同上下文，避免在关键信息处被切断。​​ | ​200​​  
​separators​​ | ​自定义分隔符优先级列表。这是控制分割行为的核心，你可以根据文档格式（如代码、Markdown）调整顺序。​​ | ​["\n\n", "\n", " ", ""]​​  
​length_function​​ | ​长度计算函数。决定用何种方式测量文本长度（例如 len 计字符数，或 tiktoken 计token数）。​​ | ​len​​  
  
其切割流程如下：

  1. 输入：原始长文本 T，目标块大小 size，一个有序的字符列表 separators (例如：["\n\n", "\n", "。", " ", ""]，优先级从高到低)。
  2. 第一步（用最高级分隔符尝试）：使用当前优先级最高的分隔符（例如段落分隔符 \n\n）尝试将 T 分割成若干块。
  3. 检查与判断：


  * 遍历刚分割出的每一个块。
  * 如果这个块的长度小于等于 chunk_size，则将其保留为一个最终的文本块。
  * 如果这个块的长度大于 chunk_size，则不能接受它。


  4. 递归降级：对于所有大于 chunk_size 的“超大块”，放弃使用当前分隔符，改用下一个优先级更低的分隔符（例如换行符 \n）来对这个“超大块”再次进行分割。
  5. 重复：重复第 3 步和第 4 步，直到所有块都小于等于 chunk_size。
  6. 最终手段：如果尝试了所有分隔符，仍然有块大于 chunk_size，那么它会在最后一级分隔符（通常是空字符串 ""，即按字符切分）上，强制将文本按 chunk_size 的长度进行硬截断。


    
    
    from langchain_core.documents import Document
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    # 创建递归切分器
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        separators=["\n\n", "\n", "。"]  # 优先级从高到低
    )
    
    # 切分文档
    chunks = recursive_splitter.split_documents(docs)
    
    print(f"切分为 {len(chunks)} 个块:\n")
    for i, split in enumerate(chunks):
        print(f"--- Chunk {i+1} ({len(split.page_content)}字符) ---")
        print(split.page_content)
        print()
    

#### 固定长度切分

先看最简单的一种，就是固定长度切分，在LangChain里提供了两个实现：

  * 根据字符大小切分
  * 根据字节大小切分  
不管哪种都需要用到CharacterTextSplitter这个类。



**按字符切分**  
最简单的切分方式，属于固定长度切分策略的一种，常见的三个参数：

  * separator : 分隔符，以此作为分隔的基本单元
  * chunk_size : 块大小，如果超出则放到下个块
  * chunk_overlap : 下一块与上一块重叠的大小，也就是滑动窗口切分


    
    
    from langchain_text_splitters import CharacterTextSplitter
    
    # 准备一段较长的文本
    long_text = docs[0].page_content
    
    # 创建字符切分器
    text_splitter = CharacterTextSplitter(
        separator="\n",    # 以换行符作为分隔
        chunk_size=1000,     # 每块最大1000字符
        chunk_overlap=200,   # 块之间重叠200字符
    )
    
    
    # 切分文本
    chunks = text_splitter.split_text(long_text)
    
    print(f"原始文本长度: {len(long_text)} 字符")
    print(f"切分为 {len(chunks)} 个块:\n")
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ({len(chunk)}字符) ---")
        print(chunk)
        print()
    

按Token切分  
使用OpenAI开源的tiktoken计算token数量，按token数量切分，更精确地控制发送给LLM的token数。
    
    
    from langchain_text_splitters import CharacterTextSplitter
    
    # 使用from_tiktoken_encoder，LangChain自带，无需额外安装tiktoken
    token_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",    # token分词器编码名
        chunk_size=1000,                # 每块最多1000 token
        chunk_overlap=200,              # 块之间重叠200字符
    )
    
    chunks = token_splitter.split_text(long_text)
    
    print(f"原始文本长度: {len(long_text)} 字符")
    print(f"切分为 {len(chunks)} 个块:\n")
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ({len(chunk)}字符) ---")
        print(chunk)
        print()
    

#### 结构感知切分

利用文档元数据识别文档本身的逻辑区块进行切分。  
例如：markdown中的多级标题、JSON结构中的字段、Html中的标签等等。  
LangChain都提供了对应不同文档类型的结构感知切分器，例如：

  * MarkdownHeaderTextSplitter
  * RecursiveJsonSplitter
  * HTMLHeaderTextSplitter
  * RecursiveCharacterTextSplitter.from_language()
  * ...


    
    
    from langchain_text_splitters import MarkdownHeaderTextSplitter
    
    # markdown数据
    markdown_document = "# 1.Foo\n\n    ## 1.1.Bar\n\nHi this is Jim\n\nHi this is Joe\n\n ### 1.1.1.Boo \n\n Hi this is Lance \n\n ## 1.2.Baz\n\n Hi this is Molly"
    
    # 切分依据，这里是按照三级标题
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    
    # 创建切分器
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    
    # 切分文档
    chunks = markdown_splitter.split_text(markdown_document )
    
    for doc in chunks:
        print(doc.model_dump_json(indent=2))
    

没有绝对正确的文档切分方式，一定要根据具体文档来具体判断。  
如果你采用了MinerU这样的文本加载器，由于其输出的格式通常是Markdown，有严谨的文档结构，那我的建议切分方式是：

  * 优先采用Markdown的文档结构切分，不仅语义完整度高，而且还能记住自己所处的章节
  * 当基于文档结构切分的块太大时，可以对超过目标size的块采用递归字符切分，但要保留header到每一个分块



### 向量化（Embeddings）

文档切分成块后，下一步就是把文本向量化，向量化是将文本转换为高维向量的过程。语义相似的文本在向量空间中距离更近，这是语义检索的基础。  
目前比较常见的小规模、开源文本向量模型有：

模型 | 参数量 | 维度 | 最大长度 | 核心特点  
---|---|---|---|---  
​Qwen3-Embedding-0.6B​​ | ​0.6B​​ | ​1024​​ | ​32K​​ | ​MTEB多语言榜64.34分，支持MRL维度压缩，多语言能力强​​  
​jina-code-embeddings-0.5B​​ | ​0.5B​​ | ​896​​ | ​32K​​ | ​代码检索SOTA，MTEB Code平均78.72%，支持15+编程语言，Last-token池化​​  
​jina-embeddings-v5-omni-nano​​ | ​~1.0B​​ | ​768​​ | ​8K​​ | ​全模态(文本/图像/音频/视频/PDF)，冻结底座仅训练0.35%参数，支持MRL维度压缩​​  
​jina-embeddings-v5-omni-small​​ | ​~1.6B​​ | ​1024​​ | ​32K​​ | ​全模态四模态平均53.93分，文本侧与v5-text逐字节兼容，MMTEB文本67.0分​​  
​jina-code-embeddings-1.5B​​ | ​1.5B​​ | ​1536​​ | ​32K​​ | ​代码检索AVG 79.04%，匹配voyage-code-3闭源模型，支持GGUF量化​​  
​BGE-M3​​ | ​0.56B​​ | ​1024​​ | ​8K​​ | ​支持稠密+稀疏+多向量混合检索，MIT协议，多语言表现优异​​  
​all-MiniLM-L6-v2​​ | ​~0.08B​​ | ​384​​ | ​512​​ | ​纯英文优化，仅80M参数，推理速度比12层快50%，STS英文表现优​​  
  
其中的开源模型我们可以本地部署，也可以使用模型平台提供的服务。

LangChain支持多种Embedding模型平台，你可以自由选择：

模型 | 提供方  
---|---  
OpenAIEmbeddings | OpenAI  
DashScopeEmbeddings | 阿里云百炼  
HuggingFaceEmbeddings | 本地开源模型  
OllamaEmbeddings | 本地开源模型  
  
#### Ollama Embeddings

注意，ollama只是工具，关键是你基于ollama部署的模型是什么，这一点与Huggingface是类似的。  
比如，我们采用阿里提供的qwen3-embedding:0.6b这个模型，它在小模型中算是效果比较好的一个，不管是Huggingface还是Ollama都支持下载和部署这个模型。
    
    
    # 安装依赖
    uv add langchain-ollama
    
    
    
    from langchain_ollama import OllamaEmbeddings
    
    # 创建Embedding模型
    ollama_embeddings = OllamaEmbeddings(
        model="qwen3-embedding:0.6b",  # 性价比高的模型
        dimensions=1024  # 可选：减少维度以节省存储
    )
    
    # 向量化单条文本
    text = "我爱上班"
    vector = ollama_embeddings.embed_query(text)
    
    print(f"文本: {text}")
    print(f"向量维度: {len(vector)}")
    print(f"向量前5维: {vector[:5]}")
    
    # 批量向量化
    texts = ["我要躺平", "我爱工作", "拒绝加班"]
    vectors = ollama_embeddings.embed_documents(texts)
    print(f"\n批量向量化: {len(vectors)} 条, 维度: {len(vectors[0])}")
    

测试：自定义一个计算余弦相似度的函数
    
    
    import numpy as np
    
    def cosine_similarity(vec1, vec2):
        dot = np.dot(vec1, vec2)
        return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    # 比较向量相似度，值越大越相似
    for v in vectors:
        similarity = cosine_similarity(vector, v)
        print("Cosine Similarity:", similarity)
    

输出结果：
    
    
    # “我爱工作”与“我要上班”的相似度值是0.8738909040875059，相似度最高
    Cosine Similarity: 0.40952704102474247
    Cosine Similarity: 0.8738909040875059
    Cosine Similarity: 0.42264466004701556
    

#### DashScope Embeddings（阿里云百炼）

阿里云百炼平台也提供了很多文本向量化模型，比如qwen的text-embedding-v3、text-embedding-v4模型。只要注册并配置了阿里云保留的API_KEY，就都能使用
    
    
    # uv add dashscope
    
    # 使用阿里云百炼的Embedding服务
    import numpy as np
    import os
    from langchain_community.embeddings import DashScopeEmbeddings
    from dotenv import load_dotenv
    
    # 加载环境变量
    load_dotenv()
    
    api_key = os.getenv("DASHSCOPE_API_KEY")
    
    if not api_key:
        raise ValueError("未找到 DASHSCOPE_API_KEY，请设置环境变量或在代码中传入")
    
    dashscope_embeddings = DashScopeEmbeddings(
        model="text-embedding-v3",
        dashscope_api_key=api_key
    )
    
    # 向量化单条文本
    text = "我爱上班"
    vector = dashscope_embeddings.embed_query(text)
    
    print(f"文本: {text}")
    print(f"向量维度: {len(vector)}")
    print(f"向量前5维: {vector[:5]}")
    
    # 批量向量化
    texts = ["我要躺平", "我爱工作", "拒绝加班"]
    vectors = dashscope_embeddings.embed_documents(texts)
    print(f"\n批量向量化: {len(vectors)} 条, 维度: {len(vectors[0])}")
    
    def cosine_similarity(vec1, vec2):
        dot = np.dot(vec1, vec2)
        return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    
    for v in vectors:
        similarity = cosine_similarity(vector, v)
        print("Cosine Similarity:", similarity)
    
    

输出结果：
    
    
    Cosine Similarity: 0.5254144258464633
    Cosine Similarity: 0.9159621493477776  # 准确度比qwen3-embedding:0.6b要高一些。
    Cosine Similarity: 0.6147298238032792
    

### 向量库

向量库用于存储和检索向量化后的文档。LangChain支持多种向量库：<https://docs.langchain.com/oss/python/integrations/vectorstores>  
向量数据库对比（Vector Database）：<https://www.cnblogs.com/vipsoft/p/20396195>  
LangChain提供了统一的VectorStore接口，使你可以用统一的方式调用任意向量库：

  * add_documents: 添加文档到向量库（不用自己做文本向量化，只要提供好向量模型即可）
  * delete: 根据id删除某个文档
  * similarity_search: 基于相似度检索与用户问题有关的文档



#### 初始化向量库-Chroma

Chroma支持将向量数据持久化到磁盘，适合中小规模应用。
    
    
    # 安装依赖
    uv add langchain-chroma
    

创建Chroma库了，需要指定在本地存储的文件路径：
    
    
    from langchain_chroma import Chroma
    
    # 创建向量库
    vectorstore = Chroma(
        collection_name="example_collection",
        embedding_function=ollama_embeddings,
        persist_directory="./db/chroma_langchain_db",
    )
    

#### 添加/删除文档

添加和删除方法：

  * add_documents：接收list[Document]，可以批量添加文档
  * delete：接收list[str]，也就是id集合，可以根据id批量删除文档


    
    
    # 准备文档，我们用之前读取的Markdown文档来测试
    with open("./resources/output/r5.md", encoding="utf-8") as f:
        markdown_text = "\n".join(line for line in f.readlines())
    
    # 用递归切分器切分文档
    chunks = recursive_splitter.split_documents(
        [Document(page_content=markdown_text, metadata={"filename": "r5.md"})]
    )
    # 给文档生成id
    ids=[]
    for i,c in enumerate(chunks):
        c.id = f"doc_{i+1}"
        c.metadata['id'] = c.id
        ids.append(c.id)
    # 删除旧文档
    vectorstore.delete(ids)
    # 添加新文档
    vectorstore.add_documents(chunks)
    

#### 检索文档

VectorStore提供了多个检索文档的方法，例如：

  * search: 通用搜索方法，支持最多样化的参数
  * similarity_search: 基于相似度的搜索
  * similarity_search_with_relevance_scores: 基于相似度搜索，并且会返回相似度得分
  * ...



search方法实现文档检索，其核心参数包括：

  * query: 查询条件
  * search_type: 查询类型，有3个可选值， 
    * similarity:相似度检索，等同于similarity_search
    * similarity_score_threshold:会基于相似度分数阈值做过滤的检索，底层是similarity_search_with_relevance_scores，但不返回得分
    * mmr:先基于相似度检索，再把结果基于mmr算法筛选，提升结果的多样性  
其它参数(并不是所有向量库都支持):
  * k: 要返回的文档数量（默认值：4）
  * score_threshold: similarity_score的最小关联阈值，低于这个分值的文档会被丢弃
  * fetch_k: 传递给MMR算法的文档数量（默认：20）
  * lambda_mult: MMR返回结果的多样性；1表示最小分集，0表示最大分集。(默认值:0.5)
  * filter: 按文档元数据（metadata）筛选



**相似度检索**
    
    
    # 用户问题
    query = "茅台2025年的市盈率和市净率分别是多少"
    # 相似度检索
    results = vectorstore.search(
        query=query,
        search_type="similarity",
        k = 5,
    )
    
    print(f"查询: {query}\n")
    for i, doc in enumerate(results):
        print(f"结果 {i+1}: {doc.page_content}")
        print(f"  元数据: {doc.metadata}")
    

**基于metadata过滤**
    
    
    # 用户问题
    query = "茅台2025年的市盈率和市净率分别是多少"
    # 相似度检索
    results = vectorstore.search(
        query=query,
        search_type="similarity",
        k = 5,
        filter={"id": "doc_3"}
    )
    
    print(f"查询: {query}\n")
    for i, doc in enumerate(results):
        print(f"结果 {i+1}: {doc.page_content}")
        print(f"  元数据: {doc.metadata}")
    

**带相似度得分的检索**  
如果调用 VectorStore 的 similarity_search_with_score 方法，还可以在检索时返回相似度打分：
    
    
    # 用户问题
    query = "茅台2025年的市盈率和市净率分别是多少"
    # 相似度检索
    results = vectorstore.similarity_search_with_relevance_scores(
        query=query,
        # search_type="similarity_score_threshold", 不需要search_type了
        score_threshold=0.42,
        k = 5
    )
    
    print(f"查询: {query}\n")
    for doc, score in results:
        print(f"======文档: {doc.id}，得分：{score}=======")
        print(f"内容: {doc.page_content}")
        print(f"元数据: {doc.metadata}")
    

### 检索器（Retriever）

检索器（Retriever）是一种接口，能够根据非结构化查询返回文档。它的功能比向量存储更通用。检索器不需要具备存储文档的能力，只需能够返回文档即可。

检索器可以由向量存储构建，也可以由其他数据源构建，因此使用范围更广。

检索器接受字符串形式的查询作为输入，并返回一个由文档对象组成的列表作为输出

#### VectorStore转Retriever

需要注意的是，所有VectorStore都可以转换为检索器  
VectorStore提供as_retriever()方法将其转换为检索器，可以把调用VectorStore时的参数提前固化，简化后期的查询。  
例如，每次我们都要传入k=3作为参数，我们就可以将其固化，转vectorstore为一个固定每次最多查3条数据的retriever：
    
    
    retriever = vectorstore.as_retriever(
        search_type="similarity",  # 检索类型: similarity, mmr, similarity_score_threshold
        search_kwargs={"k": 3}     # 返回top-3结果
    )
    

以后每次查询就可以直接使用retriever了：
    
    
    # 使用检索器检索
    retrieved_docs = retriever.invoke(query)
    
    print(f"查询: {query}\n")
    for i, doc in enumerate(retrieved_docs):
        print(f"文档 {i+1}: {doc.page_content}")
    

当然，除了k以外，你也可以固化更多参数VectorStore支持的参数。但需要注意的是，retriever 是不会返回得分的。

#### 其它Retriever

<https://docs.langchain.com/oss/python/integrations/retrievers>

### 总结

知识库构建核心组件：

组件 | 作用 | 常用选择  
---|---|---  
​Document Loader​​ | ​加载原始文档​​ | ​MinerU, Docling​​  
​Text Splitter​​ | ​切分文档为chunk​​ | ​RecursiveCharacterTextSplitter​​  
​Embeddings​​ | ​文本转向量​​ | ​DashScopeEmbeddings , BGE-M3, qwen3-embedding:0.6b​​  
​Vector Store​​ | ​存储和检索向量​​ | ​InMemory(开发), Chroma(中小), Milvus(大规模)​​  
​Retriever​​ | ​标准检索接口​​ | ​vectorstore.as_retriever()​​  
  
关键参数建议：

  * chunk_size: 建议 200~1000，取决于文档类型和模型上下文长度
  * chunk_overlap: 建议 chunk_size 的 10%~20%
  * k (检索数量): 建议 3~10，太少可能遗漏，太多可能引入噪声




---
> 原文链接: https://www.cnblogs.com/vipsoft/p/22316657