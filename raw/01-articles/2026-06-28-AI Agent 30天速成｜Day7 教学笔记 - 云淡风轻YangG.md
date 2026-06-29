---
title: "AI Agent 30天速成｜Day7 教学笔记 - 云淡风轻YangG"
source: "博客园"
url: "https://www.cnblogs.com/ylxin/p/20899792"
date: "2026-06-28T13:49:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# AI Agent 30天速成｜Day7 教学笔记 - 云淡风轻YangG

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/ylxin/p/20899792  
> **抓取日期**: 2026-06-28  
> **相关性评分**: 0.6

# AI Agent 全日制30天速成｜Day7 教学笔记

## 今日总学习目标

  1. 替换Day3内存FAISS，掌握**Chroma持久化向量库** （本地磁盘落地、支持元数据过滤、MMR去重检索）
  2. 搭建**多模态RAG** ：图文统一向量空间、SigLIP图文嵌入、图片+文本混合知识库检索
  3. 扩展统一工具网关，新增「图文检索工具」，接入Day6 ReAct动态Agent
  4. 打通完整多模态智能体链路：文本对话+图片检索+计算器+分层Redis记忆  
每日时长分配（全天8h）


  * 理论笔记阅读：2.5h
  * 代码编写调试：4h
  * 复盘面试背诵：1.5h



## 一、核心理论教学笔记

### 1\. Chroma向量库全解析（替代FAISS）

#### 1.1 FAISS痛点 & Chroma优势

Day3 FAISS仅内存存储，重启丢失向量、无元数据、不支持过滤、无内置去重逻辑；  
Chroma专为LLM RAG设计，核心优势：

  1. **持久化本地磁盘** ：程序重启向量不丢失，开箱即用无需部署服务
  2. 内置三层客户端：内存临时、本地持久、远程服务异步客户端
  3. 原生支持**元数据过滤** ：按文档来源、类型、上传时间筛选检索
  4. MMR最大边际相关性检索：避免返回高度重复片段，提升多样性
  5. 统一Collection集合隔离：文本库、图片库分开存储互不干扰
  6. 同步/异步双API，完美适配项目全异步架构



#### 1.2 Chroma三大客户端模式

客户端类型 | 存储位置 | 适用场景  
---|---|---  
EphemeralClient | 内存 | 单元测试、临时调试  
PersistentClient | 本地文件夹磁盘 | 单机本地知识库、学习项目  
AsyncHttpClient | 远程Chroma服务 | 多实例分布式线上服务  
  
#### 1.3 核心检索能力

  1. 基础相似度检索：返回文本/图片片段+距离分数
  2. Metadata条件过滤：`filter={"type":"image","source":"产品手册"}`
  3. MMR去重检索：平衡相似度与多样性，适合长文档问答
  4. 批量增删改查：支持文档/图片批量入库、指定ID删除



### 2\. 多模态RAG基础（MM-RAG）

#### 2.1 跨模态嵌入核心原理（SigLIP）

传统文本Embedding只能编码文字；SigLIP/CLIP构建**统一共享向量空间** ：

  * 图片输入 → 视觉编码器 → 图片向量
  * 文字描述/用户提问 → 文本编码器 → 文本向量  
语义相近的图文向量距离更近，实现**以文搜图、以图搜文** 双向检索



#### 2.2 多模态RAG完整流程

  1. 知识库预处理：文本分块、图片提取SigLIP向量，存入同一Chroma集合，附加`type=text/image`元数据
  2. 用户输入（文字/图片）生成多模态向量
  3. Chroma跨模态相似度召回，可过滤只返回图片或文本
  4. 图文检索结果统一拼接进Prompt，交由大模型结合图文信息回答



#### 2.3 多模态RAG解决的业务痛点

  1. 手册截图、流程图、产品配图无法被纯文本RAG检索
  2. 用户描述图片内容，无法匹配对应图文资料
  3. 图文混合知识库统一存储、统一检索，不用两套向量库



### 3\. 多模态工具网关扩展

在Day6网关基础上新增`multimodal_search`工具，标准化输入：

  * query：文字检索词（图文通用）
  * search_type：all/text/image 三种检索模式
  * top_k：返回片段数量
  * use_mmr：是否开启去重检索



网关统一封装SigLIP向量化、Chroma检索、元数据过滤逻辑，上层ReAct Agent无需关心图文底层差异。

### 4\. 今日完整串联链路（整合前6天全部能力）

用户提问（支持图文描述）

  1. Redis读取分层记忆，自动滑动窗口+摘要压缩
  2. ReAct循环Thought-Action-Observation： 
     * Thought判断是否需要检索图文知识库/数学计算
     * Action调用统一工具网关（计算器/多模态检索）
     * 网关执行Chroma图文检索或计算，返回Observation
     * 自我反思判断信息是否充足，循环迭代
  3. 汇总所有工具结果输出最终回答
  4. 对话持久化存入Redis记忆



## 二、今日学习重点

  1. Chroma持久化向量库增删改查、元数据过滤、MMR去重检索
  2. SigLIP本地图文嵌入模型调用，实现跨模态向量生成
  3. 扩展工具网关，封装统一图文检索工具
  4. 改造ReAct Agent，支持自动调用多模态知识库
  5. 对比FAISS与Chroma落地差异，掌握生产级本地向量库选型



## 三、今日难点 & 解决方案

### 难点1：SigLIP本地模型下载慢、CPU推理卡顿

解决方案：

  1. 提前缓存模型权重到本地，离线加载
  2. 推理开启`torch.no_grad()`关闭梯度，大幅提速
  3. 学习阶段缩小图片尺寸，降低算力消耗



### 难点2：图文向量混在一起，检索大量无关图片/文本

解决方案：

  1. 入库时添加`type`元数据区分图文
  2. 工具支持`search_type`过滤，按需只查文本/图片
  3. 设置相似度分数阈值，过滤低相关结果



### 难点3：Chroma持久化后向量膨胀、查询变慢

解决方案：

  1. 按业务拆分多个Collection（文本库、图片库分离）
  2. 定期清理过期无用文档，释放向量存储
  3. 检索开启MMR减少重复冗余片段



### 难点4：ReAct分不清何时该查文本、何时查图片

解决方案：

  1. System提示词明确规则：描述图表/截图/产品配图调用image检索；理论知识调用text检索
  2. Few-shot示例演示图文区分调用逻辑
  3. 工具返回时区分图文来源，模型下一轮可精准判断



## 四、完整练习代码（基于Day1~Day6扩展）

### 新增依赖安装
    
    
    pip install chromadb torch transformers pillow scikit-learn
    

### 1\. 多模态向量库 chroma_mm_store.py
    
    
    import asyncio
    import chromadb
    from chromadb.utils.embedding_functions import create_langchain_embedding
    import torch
    from PIL import Image
    from transformers import AutoProcessor, AutoModel
    import numpy as np
    from typing import List, Dict, Optional
    
    # ========== 1. SigLIP多模态嵌入本地模型 ==========
    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = AutoProcessor.from_pretrained("google/siglip-so400m-patch14-384")
    siglip_model = AutoModel.from_pretrained("google/siglip-so400m-patch14-384").to(device).eval()
    
    def text_to_vector(text: str) -> List[float]:
        """文本转多模态向量"""
        with torch.no_grad():
            inputs = processor(text=text, return_tensors="pt").to(device)
            vec = siglip_model.get_text_embedding(**inputs)
            return vec.squeeze().cpu().numpy().tolist()
    
    def image_to_vector(img_path: str) -> List[float]:
        """图片转多模态向量"""
        img = Image.open(img_path).convert("RGB")
        with torch.no_grad():
            inputs = processor(images=img, return_tensors="pt").to(device)
            vec = siglip_model.get_image_embedding(**inputs)
            return vec.squeeze().cpu().numpy().tolist()
    
    # ========== 2. 持久化Chroma多模态向量库封装 ==========
    class MultiModalChromaStore:
        def __init__(self, persist_path="./chroma_mm_db", coll_name="mm_kb"):
            # 本地持久化客户端
            self.client = chromadb.PersistentClient(path=persist_path)
            self.collection = self.client.get_or_create_collection(
                name=coll_name,
                metadata={"hnsw:space": "cosine"}  # 使用余弦相似度
            )
    
        # 批量插入文本
        async def add_text(self, text_list: List[str], source: str = "文档"):
            ids = [f"txt_{i}" for i in range(len(text_list))]
            vecs = [text_to_vector(t) for t in text_list]
            metas = [{"type": "text", "source": source} for _ in text_list]
            self.collection.add(
                embeddings=vecs,
                documents=text_list,
                metadatas=metas,
                ids=ids
            )
    
        # 插入单张图片
        async def add_image(self, img_path: str, desc: str, source: str = "图片库"):
            vec = image_to_vector(img_path)
            self.collection.add(
                embeddings=[vec],
                documents=[desc],
                metadatas=[{"type": "image", "source": source, "img_path": img_path}],
                ids=[f"img_{img_path.replace('/','_')}"]
            )
    
        # 多模态检索
        async def search(self, query: str, search_type: str = "all", top_k=3, use_mmr=False):
            query_vec = text_to_vector(query)
            where_filter = {}
            if search_type == "text":
                where_filter = {"type": "text"}
            elif search_type == "image":
                where_filter = {"type": "image"}
    
            if use_mmr:
                res = self.collection.max_marginal_relevance_search(
                    query_embeddings=[query_vec],
                    n_results=top_k,
                    where=where_filter
                )
            else:
                res = self.collection.query(
                    query_embeddings=[query_vec],
                    n_results=top_k,
                    where=where_filter
                )
            output = []
            for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
                output.append({
                    "content": doc,
                    "meta": meta,
                    "distance": round(float(dist), 4)
                })
            return output
    
    # 测试多模态库
    async def test_chroma_mm():
        mm_store = MultiModalChromaStore()
        # 写入文本知识库
        await mm_store.add_text([
            "多模态RAG使用SigLIP实现图文统一向量检索",
            "Chroma支持本地持久化，重启不丢失向量数据",
            "ReAct Agent可以自主调用图文检索工具"
        ], source="Day7学习文档")
        # 文字检索全部内容
        ret = await mm_store.search("什么是多模态RAG", search_type="all")
        print("检索结果：", ret)
    
    if __name__ == "__main__":
        asyncio.run(test_chroma_mm())
    

### 2\. 扩展工具网关 tool_gateway_mm.py（复用Day6网关）
    
    
    import asyncio
    from pydantic import BaseModel, Field
    from tool_gateway import gateway, ToolMeta
    from chroma_mm_store import MultiModalChromaStore
    
    # 全局多模态向量库实例
    mm_chroma = MultiModalChromaStore()
    
    # 多模态检索参数模型
    class MultiModalSearchParams(BaseModel):
        query: str = Field(description="检索关键词/图片描述")
        search_type: str = Field(description="检索类型 all/text/image")
        top_k: int = Field(default=2, description="返回条数")
        use_mmr: bool = Field(default=False, description="是否开启去重检索")
    
    # 新增图文检索异步工具
    async def multimodal_search(query: str, search_type: str, top_k: int, use_mmr: bool):
        res = await mm_chroma.search(query, search_type, top_k, use_mmr)
        if not res:
            return "未检索到相关图文资料"
        out_text = ""
        for item in res:
            t = item["meta"]["type"]
            src = item["meta"]["source"]
            out_text += f"【{t}|{src}】相似度距离：{item['distance']}\n内容：{item['content']}\n\n"
        return out_text
    
    # 注册新工具到网关
    gateway.register_tool(ToolMeta(
        name="multimodal_search",
        description="多模态知识库检索，可查询文本资料、产品截图、流程图等图片信息；描述图表/图片使用image类型，查询理论知识使用text类型",
        params_model=MultiModalSearchParams,
        run_func=multimodal_search
    ))
    

### 3\. 多模态ReAct智能体 react_mm_agent.py
    
    
    import asyncio
    from react_agent import ReActAgent
    from tool_gateway_mm import gateway
    
    class MultiModalReActAgent(ReActAgent):
        def __init__(self, model_name="qwen-turbo"):
            super().__init__(model_name)
            # 更新系统提示词，新增多模态工具规则
            self.system_prompt = """
    你是多模态ReAct智能体，遵循Thought -> Action -> Observation循环。
    可用工具：
    1. calculator：数学加减乘除运算
    2. multimodal_search：图文混合知识库检索
       - 查询理论、课程文字资料：search_type="text"
       - 查询流程图、产品截图、图表描述：search_type="image"
       - 全部资料一起查：search_type="all"
    规则：
    1. 涉及图片、图表类问题必须调用multimodal_search并指定image类型
    2. 数学计算禁止心算，必须调用calculator
    3. 知识库无内容禁止编造信息
    4. 每轮执行工具后自动反思信息是否充足
    """
            self.tools_schema = gateway.get_openai_tools_schema()
    
    # 测试多模态Agent
    async def test_mm_agent():
        agent = MultiModalReActAgent()
        await agent.init_memory()
        # 写入测试图文知识库
        from chroma_mm_store import mm_chroma
        await mm_chroma.add_text(["SigLIP是跨模态图文嵌入模型，用于多模态RAG检索"], source="AI知识库")
        # 复合型问题：先计算，再查询多模态RAG知识
        query = "计算 (50+10)*3，再介绍多模态RAG和SigLIP作用"
        res = await agent.chat(session_id="mm_test_001", user_query=query)
        print("最终回答：\n", res["answer"])
        await agent.close_memory()
    
    if __name__ == "__main__":
        asyncio.run(test_mm_agent())
    

### 4\. FastAPI多模态接口 main_mm_react.py
    
    
    from fastapi import FastAPI, Query
    import asyncio
    from react_mm_agent import MultiModalReActAgent
    
    app = FastAPI(title="Day7 多模态ReAct Agent｜Chroma图文知识库")
    agent = MultiModalReActAgent()
    
    @app.on_event("startup")
    async def startup():
        await agent.init_memory()
    
    @app.on_event("shutdown")
    async def shutdown():
        await agent.close_memory()
    
    @app.get("/agent/mm_chat")
    async def mm_chat(
        session_id: str = Query(..., description="会话ID"),
        prompt: str = Query(..., description="用户提问，可描述图片、数学、理论知识")
    ):
        result = await agent.chat(session_id, prompt)
        return result
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run("main_mm_react:app", reload=True)
    

## 五、今日必做练习任务

  1. 运行`chroma_mm_store.py`，测试文本入库、跨模态检索、元数据过滤功能，重启程序验证向量持久化
  2. 新增本地图片，调用`add_image`存入向量库，用文字描述实现以文搜图
  3. 修改`search_type`分别为text/image/all，对比检索返回内容差异
  4. 运行多模态ReAct Agent，提交「计算+图文知识库」复合问题，观察自动调用multimodal_search工具
  5. 开启MMR去重检索，对比普通检索返回片段重复度差异
  6. 对比Day3 FAISS代码，总结Chroma持久化、过滤、去重优势



## 六、今日配套面试题（RAG进阶/多模态Agent必考）

### 基础问答

  1. FAISS和Chroma核心区别，分别适合什么场景？
  2. 什么是SigLIP跨模态嵌入？如何实现以文搜图？
  3. Chroma三种客户端模式各自作用？
  4. MMR检索是什么，解决什么问题？
  5. 多模态RAG和纯文本RAG相比新增哪些能力？



### 工程实操题

  1. 检索时混杂大量无关图片/文本，如何通过元数据过滤精准筛选？
  2. Chroma向量数据磁盘膨胀，如何优化存储与查询速度？
  3. SigLIP本地模型推理速度慢，有哪些优化手段？
  4. ReAct Agent如何区分该检索图片库还是文本库？



### 拓展思考题

  1. 百万级图文知识库，单机Chroma性能不足有哪些替代向量库？
  2. 如何实现图片OCR+多模态向量双重检索（混合检索）？
  3. 多模态记忆如何存入Redis，实现图文对话持久化？



## 面试题参考答案

### 基础问答

  1. **FAISS vs Chroma**  
FAISS仅内存存储、无元数据、无过滤、无MMR；适合临时测试小批量向量。  
Chroma支持磁盘持久化、元数据过滤、MMR去重、异步客户端、多集合隔离；适合单机本地RAG学习/小型业务落地。

  2. **SigLIP跨模态嵌入**  
统一图文共享向量空间，图片与文字编码到相同维度向量；语义相近图文向量距离近，因此输入文字描述可检索匹配图片。

  3. **Chroma客户端**  
Ephemeral内存临时；Persistent本地磁盘持久单机；AsyncHttpClient连接远程Chroma服务，分布式多实例使用。

  4. **MMR最大边际相关性**  
平衡相似度与结果多样性，过滤高度重复的知识库片段，避免检索返回内容高度雷同，提升问答信息丰富度。

  5. **多模态RAG新增能力**  
支持图片、图文混合知识库存储检索；可通过文字描述查找图片资料；适配手册截图、流程图、图表类私有资料。




### 工程实操题

  1. **元数据过滤**  
入库时给每条数据添加`type`字段区分text/image；检索传入where过滤条件，按需只返回文本或图片片段。

  2. **Chroma存储优化**  
拆分多Collection隔离图文；定期清理无用过期向量；检索使用MMR减少冗余结果；单机大数据切换Milvus/Qdrant。

  3. **SigLIP推理优化**  
使用GPU加速；关闭梯度计算`torch.no_grad()`；压缩输入图片分辨率；提前缓存模型本地离线加载。

  4. **ReAct区分图文检索**  
System提示词明确规则，图表/截图描述调用image检索；理论文字使用text检索；搭配Few-shot示例规范工具入参。




### 拓展思考题

  1. **大规模向量库选型**  
开源分布式：Milvus、Qdrant；云托管向量库：阿里云DashVector、Pinecone；Chroma仅适合单机小规模场景。

  2. **OCR+向量混合检索**  
图片先用OCR提取文字存入文本向量库；原图SigLIP存入多模态库；检索同时召回OCR文本与图片向量，合并结果重排。

  3. **多模态会话持久化**  
Redis存储对话文字；图片路径、图片描述存入消息元数据；用户再次提问时，根据历史图片描述向量召回对应图片知识库。




## 学习总结

Day7完成向量库生产级升级（Chroma替代FAISS）与多模态RAG完整落地，打通图文混合知识库检索能力。整合前六天异步LLM、SSE、Function Calling、统一工具网关、ReAct动态反思、Redis分层记忆全套底层体系，实现能处理图文、数学、私有文档的全能本地智能体。  
下一日学习：Agent工作流编排、多智能体协作、工具链批量自动化任务。


---
> 原文链接: https://www.cnblogs.com/ylxin/p/20899792