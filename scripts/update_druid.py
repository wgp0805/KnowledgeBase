#!/usr/bin/env python3
"""Update Druid.md with optimization details"""
import re

with open('wiki/entities/Druid.md', 'r', encoding='utf-8') as f:
    content = f.read()

new_key_info = """## 关键信息
- **性能监控**：实时统计 SQL 执行次数、耗时、慢查询
- **SQL 防火墙**：WallFilter 防 SQL 注入攻击
- **内置 Web 监控页面**：可视化查看连接池和 SQL 状态
- **配置**：通过 druid-spring-boot-starter 整合

### 核心参数调优
- **initialSize**：初始连接数，建议 CPU 核心数/2
- **minIdle**：最小空闲连接数，建议 CPU 核心数 x 1.5
- **maxActive**：最大活跃连接数，经验公式为数据库单连接 QPS x 1.2
- **maxWait**：获取连接最大等待时间，建议 3000ms
- **timeBetweenEvictionRunsMillis**：后台检测间隔，建议 10000ms
- **minEvictableIdleTimeMillis**：最小空闲时间，建议 60000ms（短连接场景）
- **validationQuery**：连接有效性校验 SQL（MySQL: SELECT 1）
- **testWhileIdle=true**：推荐空闲时校验，借用/归还时不校验

### 监控体系
- **StatFilter**：SQL 统计，慢 SQL 阈值 2000ms
- **Web 监控**：/druid/statView.html 页面，需设置登录用户名和密码
- **日志集成**：支持 ELK（Logstash）和 Prometheus+Grafana 方案

### 安全增强
- **WallFilter**：拦截 DELETE/UPDATE 无 WHERE 条件的 SQL，禁止存储过程
- **密码加密**：支持 AES 或 SHA-256 加密数据库密码
- **CC 攻击防御**：限制单个 IP 的 SQL 执行频率

### 连接泄漏检测
- **removeAbandoned=true**：开启强制回收
- **removeAbandonedTimeout=300**：超时时间（秒）
- **logAbandoned=true**：记录泄漏堆栈

### 高级优化
- **动态调整**：通过 JMX 或编程方式运行时调整连接池参数
- **连接预热**：启动时预创建连接，initial-size 参数
- **事务隔离级别**：支持配置默认事务隔离级别（默认 READ_COMMITTED）"""

old_key_info = re.search(r'## 关键信息\n.*?(?=\n## 关联连接)', content, re.DOTALL)
if old_key_info:
    content = content[:old_key_info.start()] + new_key_info + content[old_key_info.end():]

content = content.replace('sources: []', 'sources: [raw/01-articles/Druid 崩了，线上直接炸锅！.md]')
content = content.replace('last_updated: 2026-05-29', 'last_updated: 2026-07-27')
content = content.replace('tags: [连接池, Java, 数据库, 监控]', 'tags: [连接池, Java, 数据库, 监控, 优化, 安全]')

old_links = """## 关联连接
- [[Hikari]] — 竞品连接池（性能优先）
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 常配合使用
- [[摘要-springboot整合mybatisPlus]] — Spring Boot 整合 MyBatis-Plus 的完…"""

new_links = """## 关联连接
- [[Hikari]] — 竞品连接池（性能优先）
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 常配合使用
- [[摘要-druid-连接池极致优化]] — Druid 连接池极致优化策略
- [[摘要-springboot整合mybatisPlus]] — Spring Boot 整合 MyBatis-Plus"""

content = content.replace(old_links, new_links)

with open('wiki/entities/Druid.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Druid.md updated successfully')