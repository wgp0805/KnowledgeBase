---
title: "OlliteRT"
type: entity
tags: [开源项目, 端侧推理, 安卓, 本地模型, AI服务器]
sources: ["raw/09-archive/2026-10-04 - 夯爆了！这个开源项目，让旧手机变成24小时跑的AI服务器！.md"]
last_updated: 2026-10-08
---

## 定义
OlliteRT（github.com/NightMean/OlliteRT）是把闲置安卓手机变成本地模型服务器的开源项目（Apache-2.0），基于谷歌 AI Edge Gallery 改造，底层用谷歌 LiteRT-LM 运行时直接调用手机 GPU/CPU 推理，暴露兼容 OpenAI 的 HTTP 接口，局域网内其他设备填个地址即可调用——对标 Ollama 的体验。

## 关键信息
- **接口兼容**：OpenAI 的 chat/completions、completions、responses 全支持，含音频转写接口，连 Anthropic messages 接口都兼容，流式/非流式均可；模型列表与健康检查端点齐全——OpenAI 官方 SDK、curl、Open WebUI 基本改个 base_url 就能用
- **模型来源三种**：应用内置清单直下（托管在 HuggingFace 的 LiteRT 社区）、导入本地 .litertlm 文件、自定义 JSON/URL 模型源（约每 24 小时刷新）
- **内置 7 模型**：Gemma 4 E2B（2.4GB，最低 8GB 内存，32K 上下文，文本/图片/音频/思考/工具/MTP）、Gemma 4 E4B（3.4GB，12GB）、Gemma 3n E2B（3.4GB，8GB）、Gemma 3n E4B（4.6GB，12GB）、Gemma 3 1B（0.5GB，6GB）、Qwen 2.5 1.5B（1.5GB，6GB）、DeepSeek-R1 1.5B（1.7GB，6GB）——"6GB 能跑"只是最低门槛且仅限最小三个，官方推荐的多模态 Gemma 4 E2B 实际要 8GB；Gemma 4 的 MTP（一次预测多个词）可手动开启提速
- **监控与运维**：状态页（运行时长/请求数/输入输出 token/出字速度与峰值/首字延迟/成功率）、可拖悬浮窗、日志页（按方法/状态码过滤、JSON 高亮、标注耗时/流式/思考/上下文占比）、`/metrics` 输出 29 个 Prometheus 指标可接 Grafana、内置 Benchmark 同机横测多模型
- **常驻三开关**：闲置自动卸载（如 5 分钟无请求卸模型还内存，下次请求自动重载）、开机自启（需关闭电池优化防安卓杀进程）、常驻通知（前台通知保后台）
- **硬限制**：一次只能加载一个模型、请求排队（不适合多人共用）；只支持 .litertlm 格式，不认 GGUF/llama.cpp/Ollama 模型；token 按字符数÷4 估算（代码和多语言会偏，不能用于计费）；本地导入会复制文件占双倍空间；无 logprobs、语法约束输出、重复惩罚、LoRA
- **安全**：数据全本地、断网可用、代码无统计逻辑；支持 bearer token（无 token 返回 401）与客户端 IP 白名单；**官方强调不要端口映射暴露公网**（无 HTTPS，token 仅基础防护），适用场景是局域网
- **硬件要求**：安卓 12+、arm64（2017 年后安卓机基本满足）、内存最低 6GB（多模态建议 8GB+），x86/模拟器不支持；当前为 beta（v0.9.7-beta.1，安装包 30 余 MB）
- **定位**：任务碎、量小、不想开电脑、数据不想外传时的常驻服务；替代正经推理机器不现实

## 关联连接
- [[摘要-ollite-rt-旧手机ai服务器]] — 来源
- [[Ollama]] — 对标体验的参照物
- [[本地Agent工作站]] — 同属本地推理路线的上位方案
- [[DeepSeek]] — 内置模型之一的来源方
- [[OpenAI]] — 其接口兼容对象
