---
title: "FunAsrNet"
type: entity
tags: [开源项目, 语音识别, C#, .NET, TTS, FunAsrNet]
sources: [raw/09-archive/2026-10-22-有人用纯 C# 写了个语音识别引擎，README 比代码还好看 - 张善友.md]
last_updated: 2026-10-23
---

## 定义
FunAsrNet 是一个用 .NET 10 + 纯 C# 手写的语音推理引擎（开源，GitHub：hnlyf168/FunAsrNet，Apache-2.0），实现普通话 ASR、实时转写、中文 TTS、电话音频处理整条流水线，全程**不依赖任何原生推理库**（不碰 Python、ONNX Runtime、ggml、sherpa-onnx、RKNN）。

## 关键信息
- **不是封装，是手写**：模型读取、特征提取、神经网络算子、解码、VAD、中文前端、TTS 全部 C# 实现；ONNX/GGUF 在这里只是文件格式，仓库自带一个只支持目标模型算子的 ONNX 解释器
- **基于 QwenAudio/Fun-ASR 固定版本架构的社区实现**：F16 编码器、Qwen3 Q8_0 解码器、FSMN VAD、两个中文 VITS；作者明确声明不是官方 SDK、不兼容上游所有模型和语言
- **性能路线全走 .NET**：x64 SIMD、ARM64 NEON/SDOT 交错内核、池化缓冲、共享只读权重、有界队列；Vulkan 后端可选（C# 调度 GPU 驱动执行嵌入的 SPIR-V）
- **功能现状**：WAV 转写；WebSocket + VAD 切句实时转写；175 个中文发音人 TTS（Huayan 1 位 + AISHELL3 174 位）；浏览器 Demo（麦克风转写/上传/试听）；电话音频 PCM16、G.711 PCMA/PCMU、重采样
- **性能数据（作者实测，i7-12700 四线程）**：ASR 热态 C# CPU 已打平原版 C++（0.720s vs 0.773s）；RK3588 上 C# 比原版快 15%~27%；但 Vulkan 后端仍是原版 GPU 的 3.14~5.50 倍耗时——README 里"仍为同轮原版 GPU 的 3.14~5.50 倍耗时，尚未追平"的反向结果照写
- **README 是亮点**：大量篇幅讲"我们还差在哪"——"热态改善不等于启动改善""不能将差异解释为语言优劣""不宣称全链路零拷贝"，原始记录、哈希、P95、慢样本全留仓库，撤回的实验方案也有记录
- **上手须知**：模型权重不在仓库，需按清单自备并校验 SHA-256；未发 NuGet 包（引 csproj）；电话方向只做媒体层（SIP 信令/RTP 抖动缓冲/AEC 缺失）；Huayan 模型许可标注 Unknown
- **价值判断（张善友）**：纯比速度没得吹，但证明完整语音推理可用托管代码实现——对 .NET 团队意味着语音能力可成为解决方案里"能审计、能维护、部署不折腾"的普通一部分

## 关联连接
- [[摘要-funasrnet-纯csharp语音识别]] — 来源（张善友评述）
- [[张善友]] — 文章作者，.NET 生态长期观察者
- [[OpenClawNET]] — 同为 .NET 生态的 AI 实践（集成方向不同）
