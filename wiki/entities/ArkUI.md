---
title: "ArkUI"
type: entity
tags: [UI框架, HarmonyOS, 鸿蒙, 方舟]
sources: [raw/09-archive/2026-09-08-一文读懂 HarmonyOS 7.0 带来的十大重要升级（一）.md]
last_updated: 2026-09-09
---

## 定义
HarmonyOS 的方舟 UI 框架，提供声明式界面构建能力，Text 组件是其中用于文本显示的基础组件。

## 关键信息
- **TextController**：Text 组件专用的文本控制器，在 Text 组件构造接口中传入即可
- **HarmonyOS 7.0 新特性**：新增 setTextSelection 方法，可设置文本选择区域并高亮显示
- **两种失效场景**：copyOption 设置为 CopyOptions.None 时不生效；textOverflow 设置为 TextOverflow.MARQUEE 时不生效
- **引入动机**：原先只有长按 Text 组件才会弹出文本选择菜单，再选中并复制/全选；新特性拓宽场景，无需长按即可通过其他途径调用 setTextSelection 灵活选中并复制目标文本
- **验证方式**：按《鸿蒙 HarmonyOS 6 应用开发》"4.1 文本显示"小节搭建 Text 组件，在构造接口中输入 TextController 对象，通过点击按钮触发 setTextSelection 观察效果

## 关联连接
- [[HarmonyOS]] — 所属操作系统
- [[ArkWeb]] — 同属方舟体系的 Web 框架
- [[摘要-harmonyos-7十大升级一]] — 来源
