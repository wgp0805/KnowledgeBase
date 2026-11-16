---
title: "BISHENG"
type: entity
tags: [开源项目, Agent平台, 企业级, 私有化部署, AgentOps]
sources:
  - raw/09-archive/Coze 下线了，开源版 WorkBuddy 来了.md
last_updated: 2026-11-12
---

## 定义
BISHENG 是 BISHENG 团队维护的开源企业级 Agent 平台（GitHub 仓库 dataelement/bisheng，约 1.2 万 Star），支持私有化部署，企业可把模型、知识库、工作流放到自己管理的环境里围绕业务搭建 AI 应用；同时它也是开源 AgentOps，专攻办公效率场景。

## 关键信息
- **定位**：可私有化部署的开源企业级 Agent 平台，也是开源 AgentOps（办公效率场景），可视为"开源的 WorkBuddy 或豆包工作"，让企业把 AI 能力掌握在自己手中
- **部署方式**：通过 Docker Compose 运行，v3.0.0 版本官方安装脚本 `bash docker/install.sh`（准备配置、拉取镜像并启动服务）；手动部署或交给 AI 辅助安装底层都是同一套 Docker 服务；本机部署后访问 `http://127.0.0.1:3001/` 注册账号，第一个注册用户成为管理员
- **企业级模块（build/webui）**：文档知识库、测评、标注、权限、模型额度分配、审计等，类似 [[Coze]] 的企业版功能；内置应用模板可 build（如"文章助手"，每个节点可自定义，可用工具节点绘制 workflow 并运行，例如研读论文）
- **桌面端**：基于 [[DSHDesktop]] 改造，与 DSH Desktop 打通；需从平台下载。两种模式：
  - **Chat 模式**：简单问答、快速响应，网页端/桌面端/手机端三端数据同步
  - **Work 模式**：复杂任务，基于电脑本地文件持续工作，内置 Office 三件套模板能力（如用 Blue Professional 模板基于销售数据做 PPT）
- **托管 Vibe 应用**：可一键托管本地开发的 app 供员工使用，统一企业管理；用户可用熟悉工具或 Coding Agent 本地开发，提交后依次经过预检、密钥扫描、构建与发布审批
- **统一管理**：客户端模型权限按部门和角色分配；按部门/角色查看用量；积分设置按部门/角色分配限额；审计、审批与组织架构管理，自动审查员工调用模型时发送的内容、AI 返回结果及工具调用中的敏感/涉密信息；支持自建知识库、按知识库创建数据集、模型微调

## 关联连接
- [[摘要-coze下线开源workbuddy]] — 来源（苏三《Coze 下线了，开源版 WorkBuddy 来了》）
- [[DSHDesktop]] — BISHENG 桌面端的改造基础
- [[Coze]] — 企业版功能对标物
- [[WorkBuddy]] — 被类比的国产桌面 AI 应用（"开源版 WorkBuddy"）
- [[苏三]] — 文章作者
