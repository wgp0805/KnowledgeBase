---
title: "ConventionalCommits"
type: concept
tags: [Git, 提交规范, 语义化版本, 自动化]
sources: [raw/01-articles/一线大厂的Git规范.md]
last_updated: 2026-08-10
---

## 定义
Conventional Commits（约定式提交）是大厂普遍采用的 Commit Message 规范，格式为 `<type>(<scope>): <subject>`。规范的 commit message 可直接被工具解析自动生成 changelog、决定版本号，是 CI/CD 自动化的基石。

## 关键信息

### 格式与 type 类型
```
<type>(<scope>): <subject>
```
| type | 含义 | 示例 |
| --- | --- | --- |
| feat | 新增功能 | `feat(user): 添加用户登录功能` |
| fix | 修复 bug | `fix(api): 修复接口超时问题` |
| docs | 文档更新 | `docs(readme): 更新部署说明` |
| style | 不影响功能的格式 | `style: 统一缩进为4空格` |
| refactor | 代码重构 | `refactor(order): 优化订单查询逻辑` |
| perf | 性能优化 | `perf(cache): 优化缓存命中率` |
| test | 测试相关 | `test(auth): 增加登录单元测试` |
| chore | 构建/工具变动 | `chore: 升级Spring Boot版本` |

### subject 书写规则
- 一般现在时 + 祈使句（add vs added / I added）
- 首字母不小写、句尾不加句号
- 不超过 **50 个字符**

### 核心原则
- 每个提交只解决一个或一类问题
- 单次提交建议不超过 300 行；大厂 PR 不超过 500-800 行
- 提交前必须自测通过

### 自动化工具链
- **[[Commitlint]]**：git commit 时自动校验 message 格式（type-enum / subject-max-length / body-max-line-length）
- **[[Husky]]**：在 commit-msg 钩子中执行校验，不符合规范直接拒绝提交
- 校验规则示意：
```js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', ['feat','fix','docs','style','refactor','perf','test','chore','revert']],
    'subject-max-length': [2, 'always', 50],
    'body-max-line-length': [2, 'always', 72]
  }
};
```

## 关联连接
- [[Git]] — 所属工具
- [[语义化版本]] — commit 类型决定版本号
- [[Commitlint]] — 自动校验工具
- [[Husky]] — Git 钩子
- [[CI-CD]] — changelog 自动生成与门禁
- [[GitFlow]] — 配合的分支模型
- [[摘要-一线大厂Git规范]] — 来源