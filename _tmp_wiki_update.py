# -*- coding: utf-8 -*-
"""增量更新 wiki 现有页面：雪花算法、sharding 补充双链；index.md 三区插入；log.md 顶部追加。"""
import sys

WIKI = r'D:\java\KnowledgeBase\wiki'

def read(path):
    with open(path, 'rb') as f:
        return f.read()

def write(path, raw):
    with open(path, 'wb') as f:
        f.write(raw)

def detect_eol(raw):
    return '\r\n' if b'\r\n' in raw else '\n'

def insert_after_line(path, anchor_substr, new_lines):
    """在最后一个包含 anchor_substr 的行之后插入 new_lines（列表），保留原 EOL。"""
    raw = read(path)
    eol = detect_eol(raw)
    text = raw.decode('utf-8')
    lines = text.split(eol)
    idx = None
    for i, line in enumerate(lines):
        if anchor_substr in line:
            idx = i  # 取最后一个匹配
    if idx is None:
        raise Exception("anchor not found in %s: %s" % (path, anchor_substr))
    lines = lines[:idx+1] + new_lines + lines[idx+1:]
    write(path, eol.join(lines).encode('utf-8'))
    print("OK insert_after: %s (after line %d)" % (path, idx+1))

def insert_at_top(path, new_text):
    raw = read(path)
    eol = detect_eol(raw)
    text = raw.decode('utf-8')
    new_full = new_text.rstrip(eol) + eol + eol + text
    write(path, new_full.encode('utf-8'))
    print("OK insert_top: %s" % path)

# 1. 雪花算法.md - 关联连接区追加 [[分布式发号器]] [[Leaf]]
insert_after_line(
    WIKI + r'\concepts\雪花算法.md',
    '摘要-分库分表六大痛点',
    ['- [[分布式发号器]] - 发号器场景下的应用',
     '- [[Leaf]] - 号段模式工程化组件']
)

# 2. sharding.md - 关联连接区追加 [[短链接系统]]
insert_after_line(
    WIKI + r'\concepts\sharding.md',
    '[[idempotency]]',
    ['- [[短链接系统]] - 短链按短码哈希分库分表的应用场景']
)

# 3. index.md - Sources 区追加（最后一项是 pi-agent-production-guide）
insert_after_line(
    WIKI + r'\index.md',
    '[[摘要-pi-agent-production-guide]]',
    ['- [[摘要-高并发短链接系统设计]] - 高并发短链接系统设计面试题：发号器+Base62、读多写少缓存架构、301/302 重定向']
)

# 4. index.md - Entities 区追加（最后一项是 markdown-it）
insert_after_line(
    WIKI + r'\index.md',
    '[[markdown-it]]',
    ['- [[Caffeine]] - Java 高性能本地缓存库，W-TinyLFU 算法',
     '- [[Leaf]] - 百度开源分布式 ID 生成组件，号段+雪花双模式']
)

# 5. index.md - Concepts 区追加（最后一项是 [[降级]]）
insert_after_line(
    WIKI + r'\index.md',
    '[[降级]] - 主流程不通时走兜底逻辑',
    ['- [[短链接系统]] - 长/短链映射服务，读多写少的高并发系统设计',
     '- [[分布式发号器]] - 分布式环境下生成全局唯一递增 ID 的组件',
     '- [[Base62编码]] - 62 字符进制编码，短链 ID 压缩为短码',
     '- [[布隆过滤器]] - 概率型数据结构，缓存穿透防护',
     '- [[哈希碰撞]] - 不同输入得到相同哈希值，MD5 短链方案核心缺陷',
     '- [[HTTP重定向]] - 3xx 状态码跳转机制，短链选 302 临时重定向',
     '- [[缓存雪崩]] - 大量缓存 key 集中过期压垮数据库，含穿透/击穿对比']
)

# 6. log.md - 顶部追加新条目
log_entry = (
    "## [2026-08-05] ingest | 摄入「面试经典：高并发短链接系统设计」\n"
    "- **变更**: 新增 source [[摘要-高并发短链接系统设计]]; "
    "新增 concepts [[短链接系统]], [[分布式发号器]], [[Base62编码]], "
    "[[布隆过滤器]], [[哈希碰撞]], [[HTTP重定向]], [[缓存雪崩]]; "
    "新增 entities [[Caffeine]], [[Leaf]]; "
    "增量更新 [[雪花算法]]（补充发号器场景与 Leaf 关联）、"
    "[[sharding]]（补充短链分库分表场景关联）; "
    "更新 [[index.md]]（1 source + 7 concepts + 2 entities）\n"
    "- **冲突**: 无\n"
    "- **归档**: raw/01-articles/面试经典：如何设计高并发短链接系统.md -> raw/09-archive/"
)
insert_at_top(WIKI + r'\log.md', log_entry)

print("ALL DONE")
