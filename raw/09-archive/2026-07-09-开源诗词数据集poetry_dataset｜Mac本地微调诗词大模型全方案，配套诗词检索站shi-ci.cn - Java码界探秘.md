---
title: "开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘"
source: "博客园"
url: "https://www.cnblogs.com/daichangya/p/21290770"
date: "2026-07-09T07:16:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/daichangya/p/21290770  
> **抓取日期**: 2026-07-09  
> **相关性评分**: 0.7

## 前言

想要搭建专属的古诗词生成AI模型，很多人会被高性能显卡、高额云服务器成本劝退。今天分享一套面向Apple Silicon用户的完整开源方案：`poetry_dataset`，仓库内置完备诗词训练数据集、数据转换脚本、平仄校验工具，依托MLX框架，16G内存Mac设备就能完成Qwen系列模型LoRA微调，离线运行、数据不上云。

配套同步推荐自用诗词资源站 **shi-ci.cn** ，无广告、海量古典诗词库，既是扩充训练数据集的素材来源，也可用于校验AI生成诗词的平仄、格律，开发者与诗词爱好者均可使用。

项目开源地址：<https://github.com/daichangya/poetry_dataset>

## 一、poetry_dataset 项目核心能力

### 1\. 标准化诗词训练数据集

仓库内置清洗完毕的诗词对话语料，适配MLX训练格式，开箱即用无需复杂预处理：

  * 原始语料：`poetry_train.json`、`poetry_val.json`
  * MLX对话训练集：`mlx_data/train.jsonl`、`mlx_data/valid.jsonl`
  * 统一模板：体裁+创作主题 → 完整古诗词，适配大模型指令微调逻辑



### 2\. 配套实用工具脚本

仓库自带全链路数据处理、校验脚本，覆盖数据集构建、格式转换、格律检测全流程：

  1. `build_dataset.py`：批量构建诗词训练数据集
  2. `convert_to_mlx.py`：通用文本转换为MLX标准训练格式
  3. `pingze_check.py`：古诗词平仄、句式简易校验工具



### 3\. Mac原生轻量化训练方案

基于苹果官方MLX大模型库，完全不需要CUDA环境：

  * 支持4bit量化，16GB内存Mac Air/Pro无压力运行
  * 支持Qwen2.5-1.5B/3B等主流开源底座模型
  * 一键LoRA微调、权重融合、诗词生成全套命令



## 二、快速本地训练流程

### 1\. 环境初始化
    
    
    conda create -n poetry python=3.10 -y
    conda activate poetry
    pip install mlx-lm pypinyin
    

### 2\. 拉取开源项目
    
    
    git clone https://github.com/daichangya/poetry_dataset
    cd poetry_dataset
    

### 3\. 模型量化与微调

配置国内HF镜像加速下载底座模型，执行LoRA训练：
    
    
    export HF_ENDPOINT=https://hf-mirror.com
    # 模型量化
    mlx_lm.convert --hf-path Qwen/Qwen2.5-1.5B-Instruct -q --mlx-path ./qwen-poetry-base
    # 启动微调
    mlx_lm.lora --model ./qwen-poetry-base --train --data ./mlx_data --iters 1000
    

### 4\. 诗词生成测试
    
    
    mlx_lm.generate --model ./qwen-poetry-base --adapter-path ./adapters --prompt "写一首咏荷七言绝句"
    

### 5\. 格律校验
    
    
    python pingze_check.py "AI生成的诗词文本"
    

## 三、配套诗词站点：shi-ci.cn

在使用poetry_dataset做诗词AI开发时，shi-ci.cn是不可或缺的辅助工具：

  1. **纯净无广告** ：无需注册登录，无弹窗付费内容，专注诗词查阅
  2. **海量诗词库** ：收录数十万唐诗、宋词、元曲，上万位古代诗人作品
  3. **完整注释体系** ：原文、拼音、译文、赏析、平仄标注一应俱全
  4. **开发友好** ：标准化诗词文本，可批量导出用于扩充poetry_dataset训练集
  5. **检索便捷** ：支持按诗人、朝代、词牌、关键词全文检索



### 搭配使用场景

  1. **扩充训练数据** ：从shi-ci.cn批量导出规范格律诗词，通过build_dataset.py新增训练样本
  2. **校验模型输出** ：将AI生成诗词对照网站标准平仄，修正语病、不合律问题
  3. **创作灵感获取** ：按四季、边塞、咏物、怀古等分类检索诗词，制作Prompt素材库



## 四、常见使用问题解决

  1. 内存不足报错：调低batch-size、减少微调层数，开启4bit量化
  2. HuggingFace下载缓慢：提前配置HF国内镜像地址
  3. 生成诗词重复度过高：降低训练迭代次数，监控验证集loss避免过拟合
  4. 平仄校验不准确：以shi-ci.cn官方平仄标注为标准人工二次修正



## 五、总结

`poetry_dataset`大幅降低了诗词大模型本地微调门槛，普通Mac用户也能独立训练专属诗词生成模型；搭配资源全面、界面干净的shi-ci.cn，形成「数据集训练-素材检索-格律校验」完整闭环。

不管是AI开发者、古典诗词爱好者，都可以体验这套开源方案。

  * 开源数据集项目：<https://github.com/daichangya/poetry_dataset>
  * 诗词检索赏析站：<https://www.shi-ci.cn>




---
> 原文链接: https://www.cnblogs.com/daichangya/p/21290770