---
title: orcale常用的查询资源的方法
tags:
  - orcale
categories:
  - orcale
date: 2023-06-13 09:31:06
---

{% note success %}
orcale查询慢sql
{% endnote %}

```sql
select *
 from (select sa.SQL_TEXT,
        sa.SQL_FULLTEXT,
        sa.EXECUTIONS "执行次数",
        round(sa.ELAPSED_TIME / 1000000, 2) "总执行时间",
        round(sa.ELAPSED_TIME / 1000000 / sa.EXECUTIONS, 2) "平均执行时间",
        sa.COMMAND_TYPE,
        sa.PARSING_USER_ID "用户ID",
        u.username "用户名",
        sa.HASH_VALUE
     from v$sqlarea sa
     left join all_users u
      on sa.PARSING_USER_ID = u.user_id
     where sa.EXECUTIONS > 0
     order by (sa.ELAPSED_TIME / sa.EXECUTIONS) desc)
 where rownum <= 50;
```

{% note success %}
查询次数最多的 sql
{% endnote %}

```sql
select *
 from (select s.SQL_TEXT,
        s.EXECUTIONS "执行次数",
        s.PARSING_USER_ID "用户名",
        rank() over(order by EXECUTIONS desc) EXEC_RANK
     from v$sql s
     left join all_users u
      on u.USER_ID = s.PARSING_USER_ID) t
 where exec_rank <= 100;
```

{% note success %}
查看表空间的名称及大小
{% endnote %}

```sql
SELECT t.tablespace_name, round(SUM(bytes / (1024 * 1024)), 0) ts_size
FROM dba_tablespaces t, dba_data_files d
WHERE t.tablespace_name = d.tablespace_name
GROUP BY t.tablespace_name;
```

{% note success %}
查看表空间物理文件的名称及大小
{% endnote %}

```
SELECT tablespace_name,
file_id,
file_name,
round(bytes / (1024 * 1024), 0) total_space
FROM dba_data_files
ORDER BY tablespace_name;
```

{% note success %}
查看回滚段名称及大小
{% endnote %}

```sql
SELECT segment_name,
tablespace_name,
r.status,
(initial_extent / 1024) initialextent,
(next_extent / 1024) nextextent,
max_extents,
v.curext curextent
FROM dba_rollback_segs r, v$rollstat v
WHERE r.segment_id = v.usn(+)
ORDER BY segment_name;
```

{% note success %}
查看控制文件
{% endnote %}

```sql
SELECT NAME FROM v$controlfile;
```

{% note success %}
查看日志文件
{% endnote %}

```sql
SELECT MEMBER FROM v$logfile;
```

{% note success %}
查看表空间的使用情况
{% endnote %}

```sql
SELECT SUM(bytes) / (1024 * 1024) AS free_space, tablespace_name
FROM dba_free_space
GROUP BY tablespace_name;
SELECT a.tablespace_name,
a.bytes total,
b.bytes used,
c.bytes free,
(b.bytes * 100) / a.bytes "% USED ",
(c.bytes * 100) / a.bytes "% FREE "
FROM sys.sm$ts_avail a, sys.sm$ts_used b, sys.sm$ts_free c
WHERE a.tablespace_name = b.tablespace_name
AND a.tablespace_name = c.tablespace_name;
```

{% note success %}
查看数据库库对象
{% endnote %}

```sql
SELECT owner, object_type, status, COUNT(*) count#
FROM all_objects
GROUP BY owner, object_type, status;
```

{% note success %}
查看数据库的版本　
{% endnote %}

```sql
SELECT version
FROM product_component_version
WHERE substr(product, 1, 6) = 'Oracle';
```

{% note success %}
查看数据库的创建日期和归档方式
{% endnote %}

```sql
SELECT created, log_mode, log_mode FROM v$database;
```

