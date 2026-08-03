---
title: "12.7K Star，这个开源项目把整本书炼成 Skill"
source: "https://mp.weixin.qq.com/s/xV05fvt2Spv3YdGIKZsxqQ"
---
程序员追风 *2026年8月2日 22:00*

**导读：** 买过的技术书，最可惜的往往是读完三个月后，连某个方法在哪一章都想不起来。把整本 PDF 临时扔给 Agent，又要重新翻目录、找章节、压缩上下文。book-to-skill 换了个思路：先把书“编译”成结构化 Skill，以后遇到问题，只加载真正相关的那一章。

GitHub： [https://github.com/virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)

它把“让 Agent 读一次书”，变成了“一本书以后都能在工作里被调用”。

## 它给知识做了一次重新编排

普通的 PDF 问答，流程通常是这样的：把文档塞进上下文，问一个问题，Agent 再去找目录、翻页、回头补定义。

这招临时查一次没问题。可如果一本书要反复用，每次都重新找路，成本和结果都不稳定。

book-to-skill 做的是一次“预编译”。

它先从 PDF、EPUB、DOCX、Markdown、HTML、RTF 等文件中提取正文，再让 Agent 把内容整理成一套可安装的 Skill。输入也不只是一份书，可以是一个文档目录、一组论文，或者匹配某类文件的 glob。

截至 2026 年 7 月 30 日，这个项目在 GitHub 上有 12,739 Star、1,416 Fork。仓库 5 月初创建，7 月 27 日仍有提交，更新速度很快。

book-to-skill GitHub 仓库与当前数据

![图片](assets/%E5%B0%B1%E4%B8%80%E4%B8%AAskill%EF%BC%8C%E5%87%AD%E5%95%A56wstar%EF%BC%9F/944c67f921fca7220ca1748b2d1e1a2c_MD5.webp)

## 生成出来的 Skill，长什么样

它不会只交付一篇长摘要。

生成目录里有一个主 `              SKILL.md            ` ，放核心心智模型和章节索引；每个章节单独生成 Markdown 文件，需要时再加载。旁边还有术语表、方法与模式清单，以及一份偏决策规则的速查表。

大致会得到这套结构：

```
your-book-skill/ ├── 
            SKILL.md
           ├── chapters/ │   ├── ch01-*.md │   ├── ch02-*.md │   └── ... ├── 
            glossary.md
           ├── 
            patterns.md
           └── 
            cheatsheet.md
```

其中比较关键的是 `chapters/` 。

主 Skill 只保留最常用的框架和索引。你问到某个概念时，Agent 再去读对应章节，没必要每轮对话都背着整本书跑。

项目生成的文件结构与用途

![图片](assets/%E5%B0%B1%E4%B8%80%E4%B8%AAskill%EF%BC%8C%E5%87%AD%E5%95%A56wstar%EF%BC%9F/cce2ae42bb065069a132b3bc8f719ead_MD5.png)

这也是它和普通 RAG 最明显的区别。

RAG 擅长在一堆文档里找“和问题最像的片段”；book-to-skill 更像提前做了一次知识编辑，把框架、判断规则、反模式和章节关系整理好。一个适合广而浅地搜资料，一个适合把少量高价值材料反复用深。

## 为什么按章节加载，比整本塞进去更划算

项目作者把反复翻目录、定位章节、回头补上下文的成本叫作 “Discovery Loop Tax”，也就是发现循环税。

README 给了三本真实书的测算。针对一个具体问题，book-to-skill 运行时大约加载 4,000 token 的核心 Skill，再加约 1,000 token 的相关章节。和整本书直接进入上下文相比，输入 token 少 24～51 倍。

项目对 Discovery Loop Tax 的测算与限制说明

![图片](assets/%E5%B0%B1%E4%B8%80%E4%B8%AAskill%EF%BC%8C%E5%87%AD%E5%95%A56wstar%EF%BC%9F/868b23c1174435c4cc6a5336aa50cdf2_MD5.png)

这个数字不能理解成“所有场景都快 51 倍”。

作者也写了限制：和一次性的发现循环相比，测算优势是 2.4～15.6 倍，而且发现循环本身是一个模型；如果只是临时读一次 PDF，直接让 Agent 读可能更省事。book-to-skill 真正占便宜的场景，是同一本书、同一套内部文档会被反复查阅。

## 它怎么把一本书变成 Skill

整个流程可以拆成两段。

第一段是本地提取。对于以文字为主的 PDF，它优先尝试 `pdftotext` ，也可以回退到 `pypdf` 或 `              pdfminer.six            ` ；技术书如果有大量代码、表格和公式，可以选 Docling，速度慢一些，但能保住更多结构。

第二段才是 Agent 整理。它会识别书名、作者、目录和章节，为每章提炼框架、方法、反模式和例子，再生成总索引、术语表、模式清单与速查表。

项目还设计了更新模式。以后有新论文、新章节或内部文档，可以 fold-in 到现有 Skill，原来的内容不用全部推倒重做。

提取脚本虽然在本机运行，后续如果 Agent 使用云端模型，发送给模型的文本仍受相应服务商的数据条款约束。公司内部材料别因为“本地提取”四个字就放松权限判断。

## 怎么安装，别把两条路线混在一起

如果你想在 Claude Code 中直接使用 `/book-to-skill` ，需要把完整仓库克隆到 Skill 目录：

```
git clone 
            https://github.com/virgiliojr94/book-to-skill.git
           \   ~/.claude/skills/book-to-skill
```

然后在 Agent 会话中调用：

```
/book-to-skill ~/path/to/
            your-book.pdf
```

GitHub Copilot CLI 可以安装到 `~/.copilot/skills/book-to-skill` ，也可以使用 `~/.agents/skills/book-to-skill` 这条跨 Agent 路径。项目当前明确列出的宿主是 GitHub Copilot CLI、Amp 和 Claude Code。

另一条路线是安装 Python 包：

```
pip install "book-to-skill[pdf,epub,docx]" book-to-skill --check
```

==但 `pip install` 只会安装文字提取 CLI，不会注册 `/book-to-skill` 这个 Agent Skill。== 想要完整的“书转 Skill”流程，仍要按上面的方式克隆仓库。

Agent Skill 与独立提取 CLI 的安装方式

![图片](assets/%E5%B0%B1%E4%B8%80%E4%B8%AAskill%EF%BC%8C%E5%87%AD%E5%95%A56wstar%EF%BC%9F/2f1fb016d401c60aa514355a011e2416_MD5.png)

## 我实际检查了什么

我在 macOS 上直接跑了仓库里的依赖检查和 Markdown 提取。

`              README.md            ` 被识别为约 4,424 token，提取成功，并检测出 14 个章节级标题。仓库的测试套件也完整跑了一遍，163 项测试全部通过。

这能说明它的提取入口、章节检测和当前代码测试是通的，但不等于我已经用一本数百页技术书完成了整套云端生成。后半段的速度、费用和成品质量，仍会受到书的排版、所选提取器、模型和提示过程影响。

## 上手前还要知道几件事

章节标题越规范，自动切分越稳。只有章节名、罗马数字或复杂排版的书，仍可能需要手动检查；技术 PDF 如果用快速文本模式，表格和代码结构也可能被打散。

版权边界同样不能跳过。这个项目本身不附带任何书籍内容，但你生成的 Skill 是对原书的结构化整理。自己学习、处理自有文档是一回事，把受版权保护的书转成 Skill 后公开分发，是另一回事。

任何把外部文档转成 Agent 指令的流程，都要防提示注入。当前 master 分支已经加入生成 Skill 的安全扫描，但它是提示性检查，不是绝对保证。内部文档、陌生电子书和网上下载的文件，依旧要先确认来源。

## 写在最后

我喜欢这个项目的一点，是它没有把“大上下文”当成唯一答案。

上下文能装下整本书，不代表每次回答都应该把整本书重新读一遍。对于经常要查的技术书、研究资料、品牌手册、架构文档，先整理成按需加载的 Skill，确实更像一套能长期使用的工作流。

如果你只想临时问一本 PDF，没必要折腾。可如果某份材料你已经打开过三次，还会继续打开第四次，book-to-skill 值得收藏。

GitHub 项目地址： [https://github.com/virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)

 **![图片](assets/%E5%B0%B1%E4%B8%80%E4%B8%AAskill%EF%BC%8C%E5%87%AD%E5%95%A56wstar%EF%BC%9F/000659fdef65615a176821139f9416c4_MD5.webp)**你在看吗****