---
title: "摘要-ollite-rt-旧手机ai服务器"
type: source
tags: [来源, 原始文件, 端侧推理, 开源项目, OlliteRT]
sources: ["raw/09-archive/2026-10-04 - 夯爆了！这个开源项目，让旧手机变成24小时跑的AI服务器！.md"]
last_updated: 2026-10-08
---

## 核心摘要
OlliteRT 是把闲置安卓手机变成本地模型服务器的开源项目（Apache-2.0，基于谷歌 AI Edge Gallery 改造，底层用谷歌 LiteRT-LM 运行时直接调手机 GPU/CPU），对标 Ollama 体验：手机上跑模型并暴露兼容 OpenAI 的 HTTP 接口（chat/completions、completions、responses、音频转写甚至 Anthropic messages 全支持，流式非流式均可），局域网其他设备改个 base_url 即可调用，模型下载后断网可用、数据全本地处理。内置 7 个模型：Gemma 4 E2B（2.4GB/需 8GB 内存/32K 上下文，文本+图片+音频+思考+工具+MTP）、Gemma 4 E4B（3.4GB/需 12GB）、Gemma 3n E2B/E4B、Gemma 3 1B、Qwen 2.5 1.5B、DeepSeek-R1 1.5B——"6GB 能跑"只是最低门槛（仅最小三个），官方推荐的多模态 E2B 实际要 8GB。运维配套齐全：状态页（运行时长/请求数/token/出字速度/首字延迟/成功率）、可过滤日志、29 个 Prometheus 指标（/metrics 接 Grafana）、内置 Benchmark、悬浮窗；常驻三开关为闲置自动卸载、开机自启（需关电池优化）、常驻通知。硬限制：一次只能加载一个模型且请求排队、只认 .litertlm 格式（不支持 GGUF/Ollama 模型）、token 按字符数÷4 估算不可用于计费；官方强调不要端口映射暴露公网（无 HTTPS、token 仅基础防护）。适用场景是任务碎、量小、不想开电脑、数据不想外传的局域网常驻服务，替代正经推理机器不现实。

## 关联连接
- [[OlliteRT]] — 本文主角
- [[Ollama]] — 对标体验的参照物
- [[本地Agent工作站]] — 同属本地推理路线的上位方案
- [[OpenAI]] — 其接口兼容对象
