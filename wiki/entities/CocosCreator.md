---
title: "CocosCreator"
type: entity
tags: [游戏引擎, H5游戏]
sources: [raw/09-archive/程序汪4万20天接的肉鸽类小游戏，二期项目.md]
last_updated: 2026-07-24
---

## 定义

开源跨平台游戏引擎，专注于H5游戏开发，支持发布到Web Mobile、原生移动平台和小游戏平台。Cocos Creator 3.x系列基于TypeScript，提供可视化编辑器与Asset Bundle按需加载机制。

## 关键信息

- **版本选型**：3.8 LTS为经过兼容测试的稳定版本，支持Web Mobile发布
- **构建目标**：Web Mobile，竖屏/横屏在产品确认后固定，不在战斗中动态旋转
- **渲染后端**：移动端WebView以WebGL兼容性为准，WebGPU仅限Web Desktop，不作为移动端生产依赖
- **Asset Bundle拆分**：支持按需加载、远程Bundle、预加载和版本Hash，典型拆分策略为boot/common/gameplay/season_x
- **编辑器工程化管理**：编辑器版本、构建扩展、npm依赖、资源导入参数全部纳入版本控制和CI
- **性能优化手段**：图集与DrawCall合并、对象池、弹幕和伤害数字上限、分帧生成、纹理分档、音频懒加载、运行时大对象和JSON解析控制、场景退出时释放对应Bundle

## 关联连接

- [[摘要-程序汪-肉鸽小游戏二期]] — 来源
- [[roguelike-game]] — 使用Cocos开发的游戏类型
- [[jsbridge]] — H5业务壳与Cocos画布分工
