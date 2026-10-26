---
title: "Firecracker"
type: entity
tags: [工具, 虚拟化, 沙箱, 基础设施, AWS]
sources:
  - raw/09-archive/2026-10-21-斯坦福新课直接讲 personal agent，Grok Bot 工程师分享如何打造出 always-on agent.md
last_updated: 2026-10-21
---

## 定义

AWS 推出的轻量级虚拟化方案（KVM microVM），在 always-on agent 架构中被用作**agent 专属的那台云端 Linux 电脑**的承载技术。

## 关键信息

### 为什么选它
Lee Robinson 提到的那台电脑跑的就是 Firecracker 虚拟机，好处是：
- **很容易把整台机器的状态做成快照**，关掉再起来
- 可以连上去看它的实时画面，必要时亲自接管
- 有文件、能跑命令、有 Chrome，而且可以有虚拟桌面——**同时跑五个、十个 bot，每个都能有自己的屏幕**

### 关键的设计意图
> 你不想把这些命令放在自己的笔记本上，而是放在一个被锁定、与你隔离的环境里。**Agent 在那里怎么折腾，都不会弄脏你的电脑。**

这与 [[ThinClientThickServer]] 的架构取向配套——所有重活（shell、录屏、演示、桌面操作）都在服务端这台隔离机器上完成。

### 与「可独立重建」的关联
因为 agent 的循环就跑在虚拟机里，运维可以独立地关掉那台虚拟机（比如打紧急的 Linux 零日补丁时直接重建虚拟机），而不会把整个 agent 循环一起清掉、让应用停机。

## 关联连接

- [[LeeRobinson]] — 分享中提及该技术的工程师
- [[ThinClientThickServer]] — 配套的架构取向
- [[常驻智能体]] — 所属场景
- [[沙箱]] — 隔离职责
- [[摘要-always-on-agent-斯坦福分享]] — 来源
