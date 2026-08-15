---
title: "Deepseek Harness 接glm/minimax等其他模型 - 九里九里"
source: "博客园"
url: "https://www.cnblogs.com/polipolu/p/22485471"
date: "2026-08-14T23:49:00Z"
score: 0.9
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Deepseek Harness 接glm/minimax等其他模型 - 九里九里

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/polipolu/p/22485471  
> **抓取日期**: 2026-08-15  
> **相关性评分**: 0.9

项目https://github.com/lo2589/deepseek-harness-provider.git

## 

DeepSeek Harness 默认只接 DeepSeek 官方模型。装上这个插件之后，发送键旁边会多一个 **+** ，点开就能可视化添加其他模型厂商——不用改任何配置文件，界面点几下就完事。

## 一、安装（一次性，重启不丢）

**正式安装（推荐）** ：把插件装进你的 `web` profile，之后重启 dsh 也一直在。
    
    
    # 1. 拿到插件包（仓库里自带 dsh-provider-quick-config-0.1.2.tgz）
    # 2. 装进 profile
    dsh plugin --profile web add file:/path/to/dsh-provider-quick-config-0.1.2.tgz
    
    # 3. 重启 dsh web 生效
    deepseek restart

**想先试试** ：在 dsh 会话里用 `cordis_define` 挂载动态版（源码在仓库 `plugin/` 目录），刷新页面即可，但进程重启后会消失——所以长期用还是正式安装。

**验证装上了没有** ：刷新页面，发送键旁边出现 **+** 就是成功；或者检查 `~/.dsh/profiles/web/package.json`，`dsh.profile.bundles` 里应该能看到 `dsh-provider-quick-config`。

## 二、第一次用（5 步）

  1. **点发送键旁边的 +** ，弹出 Provider 配置面板；

  2. 点 **添加 Provider** ，选一个厂商——**智谱 GLM / MiniMax / OpenAI GPT / Anthropic Claude / 本地模型 (Ollama)** ，端点、协议、推理格式、模型列表全都预填好了；

  3. 填 **API 密钥** （比如智谱填你的 GLM key，MiniMax 填 MiniMax key）；

  4. 点 **保存** ；

  5. 完事——模型立刻出现在发送框旁边的模型下拉框里，直接选就能用。




## 三、日常操作

**加第二个厂商** ：重复上面流程，选另一个厂商即可。所有厂商平级显示在下拉框里。

**一个厂商开多个号** ：再点同一个厂商，插件会自动排号（`glm` → `glm2` → `glm3`…），显示名自动带"号N"，各自配自己的密钥。适合一个平台有多个账号/额度的情况。

**换模型** ：点厂商行右边的 **编辑** ，模型区有"快捷模型"一排标签，点一下选中、再点取消（比如 MiniMax 想用 M3，点 `MiniMax-M3` 就行）；也能手动加任意模型 id 并填上下文窗口、最大输出。

**自动获取模型** ：编辑表单里有"自动获取模型"按钮，一键拉取端点真实支持的模型列表，省得自己猜名字。

**改密钥** ：编辑对应厂商，在密钥框里填新值保存即可。

**删除** ：点"删除"两次确认，路由和它的模型立即从下拉框消失。

## 四、本地模型自动同步

给 Ollama 添加时插件默认开启"自动同步"（面板里能看到"自动同步"标记）。之后**每 60 秒** 自动对比一次本机 Ollama 的模型列表：

  * 在 Ollama 里 `ollama pull` 了新模型 → 最多一分钟自动出现在下拉框，不用手动加；

  * 删掉的模型也会自动移除。




其他厂商的路由也可以在编辑表单里勾选"自动同步模型"，端点模型有变化时同样自动跟进。

## 五、自定义 OpenAI 兼容

自建网关、公司内网端点、或者上面预设里没有的厂商，选 **"自定义 OpenAI 兼容"** ，填四项：

  * **BaseURL** （端点地址，如 `https://网关地址/v1`）

  * **API 协议** （openai-completions / openai-responses / anthropic-messages）

  * **API 密钥**

  * **模型列表** （手动填，或点"自动获取模型"让它拉）




保存前插件会先向端点校验一遍模型名，**打错名字会当场红字拦下** ，不会把错误配置存进去。

## 六、更多

  * 完整源码、安装文档、踩坑记录都在仓库：**lo2589/deepseek-harness-provider** ；

  * 插件面板里所有操作都是热生效的——保存完下一次请求就能用，不用重启服务；

  * 官方自带的 **设置 → 模型** 页面也仍然可用，两者不冲突。




装好之后，GLM、MiniMax、GPT、Claude、本地 Ollama 就能在一个下拉框里随意切换了。


---
> 原文链接: https://www.cnblogs.com/polipolu/p/22485471