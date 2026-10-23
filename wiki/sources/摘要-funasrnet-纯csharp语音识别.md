---
title: "摘要-funasrnet-纯csharp语音识别"
type: source
tags: [来源, FunAsrNet, CSharp, 语音识别, ASR, TTS, 张善友]
sources: [raw/09-archive/2026-10-22-有人用纯 C# 写了个语音识别引擎，README 比代码还好看 - 张善友.md]
last_updated: 2026-10-23
---

## 核心摘要
张善友（博客园，2026-10-22）介绍一个"很倔"的开源项目 FunAsrNet：用 .NET 10 和纯 C# 手写整个语音栈（基于 QwenAudio/Fun-ASR 固定版本架构的社区实现，围绕 F16 编码器、Qwen3 Q8_0 解码器、FSMN VAD、两个中文 VITS 验证），模型读取、特征提取、神经网络算子、解码、VAD、中文前端、TTS 全程不碰 Python、ONNX Runtime、ggml、sherpa-onnx，ONNX/GGUF 在这里只是文件格式，仓库甚至自带一个只实现目标算子的 ONNX 解释器。性能优化走 .NET 自己的路：SIMD、ARM64 NEON/SDOT 交错内核、池化缓冲、共享只读权重、有界队列，Vulkan 后端由 C# 调度嵌入的 SPIR-V。功能覆盖 WAV 转写、WebSocket+VAD 实时转写、175 发音人中文 TTS、浏览器 Demo、PCM16/G.711 电话音频。最出彩的是 README 的"反向基准"写法：多数项目只挑赢的指标发，它大量篇幅在讲"我们还差在哪"，仓库里引用原生 ORT 的工程只当测速对照的"陪练"，不进主解决方案。

## 关联连接
- [[张善友]] — 作者
- [[FunAsrNet]] — 项目本体
- [[语音AI]] — 所在领域
- [[本地部署]] — 推理本地化的技术路线
- 「反向基准」：主动公开自身劣势的评测文档写法（未单独立页，纯文本记录）
