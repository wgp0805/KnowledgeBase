# ECC + OpenCode 完整使用指南

> 2026-06-26 · 随笔记

## 什么是 ECC？

ECC（Everything Claude Code）是一个开源的 **AI 编码智能体编排系统**，由 affaan-m 在 GitHub 上维护（222K+ Stars），MIT 协议，完全免费。

它原生支持 OpenCode、Claude Code、Cursor、Codex、Gemini 等多个 AI 编码工具，提供 **agents、commands、hooks、skills、rules、custom tools** 等一套完整的配置增强体系。

对于 OpenCode 用户，ECC 提供了：

- **26 个 agents**：`planner`、`architect`、`code-reviewer`、`security-reviewer`、`tdd-guide`、`python-reviewer`、`java-reviewer` 等
- **26 个 commands**：`/plan`、`/tdd`、`/code-review`、`/security`、`/build-fix`、`/orchestrate` 等
- **Plugin hooks**：文件变更钩子、安全审计、会话管理等
- **Custom tools**：`run-tests`、`check-coverage`、`security-audit`、`git-summary` 等
- **Skills**：TDD、安全审查、API 设计、前端/后端模式等 11+ 个技能

---

## 三种安装方式对比

安装 ECC 有三种方式，适用场景完全不同，**不要混用**。

| 方式 | 是否依赖 ECC 目录 | 功能完整度 | 适用场景 |
|------|-----------------|-----------|---------|
| npm 包 | ❌ 不需要 | ⚠️ 仅 plugin hooks + tools | 只想用安全审计、格式化等 hooks |
| 完整克隆 | ✅ 必须在 ECC 目录内运行 opencode | ✅ 全部功能 | 学习/调试 ECC 本身 |
| 选择性复制 | ❌ 不需要 | ✅ 可自选组合 | **日常多项目开发（推荐）** |

### 方式一：npm 包安装（功能有限）

```bash
npm install ecc-universal -g
```

在项目的 `opencode.json` 中加入：

```json
{
  "plugin": ["ecc-universal"]
}
```

**优点**：全局安装一次，各项目一行配置即可使用。
**缺点**：只加载 plugin hooks 和 custom tools，**不会自动注册 agents、commands 和 skills**。轻量，但功能不全。

### 方式二：完整克隆仓库（功能全但受限）

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
npm install
npm run build:opencode
opencode
```

**优点**：使用全部 26 个 agents、26 个 commands、hooks、tools。
**缺点**：必须在 ECC 仓库目录下运行 opencode，**无法在你自己项目里使用**。适合了解 ECC 整体架构，不适合日常开发。

### 方式三：选择性复制到项目（推荐）

```bash
# 1. 克隆 ECC（仅一次）
git clone https://github.com/affaan-m/ECC.git

# 2. 在项目里创建 .opencode 目录
mkdir 你的项目/.opencode

# 3. 按需复制你需要的功能
#    复制 commands
cp -Recurse ECC/.opencode/commands    你的项目/.opencode/commands/
#    复制 agents
cp -Recurse ECC/.opencode/prompts     你的项目/.opencode/prompts/
#    复制 instructions/skills
cp -Recurse ECC/.opencode/instructions 你的项目/.opencode/instructions/
#    复制 skills 目录
cp -Recurse ECC/skills                 你的项目/.opencode/skills/
#    复制 tools
cp -Recurse ECC/.opencode/tools        你的项目/.opencode/tools/
```

**优点**：
- 每个项目按需选择功能，不会把用不上的 agents/skills 都塞进来
- 不依赖 ECC 目录，在任意项目目录下直接使用
- 功能完整度完全由你控制

---

## 核心工作流速查

| 命令 | 用途 |
|------|------|
| `/plan "添加用户认证"` | 生成实现计划 |
| `/tdd` | TDD 工作流驱动 |
| `/code-review` | 代码审查 |
| `/security` | 安全审查 |
| `/build-fix` | 修复编译错误 |
| `/orchestrate` | 多 agent 协同工作 |
| `/learn` | 从当前会话提取模式 |
| `/verify` | 验证循环 |
| `/eval` | 评估指标 |

---

## 常见问题

**Q：npm 包安装后功能不全怎么办？**
A：npm 包只加载 plugin 层（hooks + custom tools）。如果需要 agents 和 commands，请改用"选择性复制"方式。

**Q：三种方式能混用吗？**
A：**不能。** 不要同时用 npm 包又克隆仓库又手动复制，会造成配置重复和冲突。选一种即可。

**Q：国内网络访问不了 GitHub 怎么办？**
A：可以使用 npm 包方式（npm 国内有镜像），或者通过代理/VPN 后克隆。npm 包虽然功能有限，但对网络要求最低。

**Q：一定要在 ECC 目录下才能用完整功能吗？**
A：不一定。选择性复制方式可以把完整功能复制到你自己的项目目录中，无需待在 ECC 目录下。

---

## 总结

- **想简单尝鲜** → 用 npm 包 `ecc-universal`
- **想研究 ECC 源码全文** → 完整克隆
- **日常多项目开发（推荐）** → 选择性复制，按需取用
