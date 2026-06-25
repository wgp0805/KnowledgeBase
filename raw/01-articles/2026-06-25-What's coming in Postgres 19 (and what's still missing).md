---
title: "What's coming in Postgres 19 (and what's still missing)"
source: "PostgreSQL Weekly"
url: "https://postgresweekly.com/issues/654"
date: "Wed, 24 Jun 2026 00:00:00 +0000"
score: 1.0
tags: ["PostgreSQL", "数据库", "SQL"]
auto_captured: true
---

# What's coming in Postgres 19 (and what's still missing)

> **来源**: PostgreSQL Weekly  
> **链接**: https://postgresweekly.com/issues/654  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

| #​654 — June 24, 2026 | [Web Version](<https://postgresweekly.com/link/186991/rss>)  
---|---  
---  
Postgres Weekly  
---  
[![](assets/2026-06-25-What's%20coming%20in%20Postgres%2019%20(and%20what's%20still%20missing)/8eebd9b65a034bead53388f8ef85c759_MD5.jpg)](<https://postgresweekly.com/link/186969/rss>)  
---  
[Looking Ahead to Postgres 19](<https://postgresweekly.com/link/186969/rss> "www.snowflake.com") — _“Postgres 19 feels like one of those releases that has a bit of everything,”_ says Craig, who focuses on quality of life improvements that day-to-day Postgres users will come to appreciate, both at the operational level (e.g. `REPACK` and partitioning improvements) and in SQL (e.g. SQL/PGQ and `GROUP BY ALL`). Craig Kerstiens   
---  
💡 Shaun Thomas [digs into Postgres 19's logical replication of sequences](<https://postgresweekly.com/link/186970/rss>).  
---  
[![](assets/2026-06-25-What's%20coming%20in%20Postgres%2019%20(and%20what's%20still%20missing)/16e9921b0742286dbaf0289fc0d3867e_MD5.png)](<https://postgresweekly.com/link/186968/rss>) [44 Recorded PostgreSQL Talks Are Now Available to Watch](<https://postgresweekly.com/link/186968/rss> "aka.ms") — POSETTE: An Event for Postgres 2026 is over, but the talks are here to stay. All sessions are now available on YouTube, so you can learn directly from Postgres experts at your own pace. [Access the full playlist of 44 talks](<https://postgresweekly.com/link/186968/rss>). Microsoft | AMD sponsor  
---  
▶ [What's Missing in Postgres?](<https://postgresweekly.com/link/186971/rss> "www.youtube.com") — We report on features Postgres is adding all the time, but what’s ‘missing’ and why? Bruce touches on a diverse range from sharding and connection pooling to columnar storage and transparent data encryption. _Can’t watch? Here are[the slides in PDF form.](<https://postgresweekly.com/link/186972/rss>)_ Bruce Momjian   
---  
[Postgres 18 Performance Enhancements](<https://postgresweekly.com/link/186973/rss> "aws.amazon.com") — Postgres 18 has many enhancements and performance tweaks worth reviewing. This tour covers skip scan optimization, Self-Join Elimination, autovacuum settings, and more. It takes an AWS perspective, but most of it applies to anyone on Postgres 18. Jafri, Bedi, Burman and Shaik (Amazon)   
---  
[pg_stats: How Postgres Internal Stats Work](<https://postgresweekly.com/link/186974/rss> "richyen.com") — Get a working understanding of what [`pg_stats`](<https://postgresweekly.com/link/186975/rss>) is, and how it shapes the query planner's decisions. Richard Yen   
---  
📄 [Optimizing Polymorphic Associations in Postgres](<https://postgresweekly.com/link/186976/rss>) Andrei Lepikhov 📄 [Shipping `psql` Without `psql`: A Pure-TypeScript Client in `neonctl`](<https://postgresweekly.com/link/186977/rss>) Vadim Kharitonov (Neon) 📄 [Looking Forward to Postgres 19: Query Hints](<https://postgresweekly.com/link/186978/rss>) Shaun Thomas  
---  
---  
|   
---  
📰 Classifieds  
---  
❄️ [ColdFront Beta](<https://postgresweekly.com/link/186979/rss>): Auto-tier old Postgres data to Iceberg on S3. Same table, same SQL. Cold data stays writable. [Open source](<https://postgresweekly.com/link/186979/rss>). Run AI agents like microservices — agents with auto-generated APIs, durable memory, policy-based orchestration. No glue code. Open source. [→ Star on GitHub](<https://postgresweekly.com/link/186980/rss>).  
---  
---  
---  
**RELEASES AND CODE:**  
---  
[![](assets/2026-06-25-What's%20coming%20in%20Postgres%2019%20(and%20what's%20still%20missing)/3003b2d5c721d506e959921a6361a6c9_MD5.jpg)](<https://postgresweekly.com/link/186981/rss>)  
---  
---  
[`pg_hardstorage` 1.0: A New Backup and Recovery Approach](<https://postgresweekly.com/link/186981/rss> "www.pghardstorage.org") — A streaming-first, host-access-free, chain-free backup tool in a single binary that streams the WAL over an ordinary replication connection for gap-free, byte-precise PITR. It includes pgBackRest and Barman shims so you can swap it in/try it out without rewriting your automation. Cybertec   
---  
🌐 [Datum: Local-First Spatial Syncing for PostGIS](<https://postgresweekly.com/link/186985/rss> "a-saed.github.io") — A local-first sync layer that mirrors Postgres/PostGIS tables into an in-browser PostGIS instance (via the WASM-based [PGlite](<https://postgresweekly.com/link/186986/rss>)) with real-time deltas over `NOTIFY`. Abdulrhman Elsaed   
---  
[Migration Autopilot: GitHub Action to Review DB Migration PRs](<https://postgresweekly.com/link/186982/rss> "migration.useautopilot.dev") — Looks at database migrations and detects the renaming or dropping of columns and tables, truncation, [and similar issues](<https://postgresweekly.com/link/186983/rss>). Isabelle Hue   
---  
  
  * [SPQR 3.0](<https://postgresweekly.com/link/186987/rss>) – _Stateless Postgres Query Router_ for horizontal scaling via sharding. v3.0 adds distributed query support, distributed and reference tables, and two-phase commit for DDL/migrations across shards.
  * [pgrx v0.19](<https://postgresweekly.com/link/186988/rss>) – Framework for building Postgres extensions in Rust. v0.19 adds Postgres 19 Beta support, updates dependencies, and includes tidy-ups.
  * [pgAdmin 4 9.16](<https://postgresweekly.com/link/186989/rss>) – Popular web-based Postgres management tool.
  * [pg_parse 0.15.0](<https://postgresweekly.com/link/186990/rss>) – Postgres SQL parser for Rust.

  
---  
---  
  
![](assets/2026-06-25-What's%20coming%20in%20Postgres%2019%20(and%20what's%20still%20missing)/7c0468a65b11fa22737726364a0ece63_MD5.gif)


---
> 原文链接: https://postgresweekly.com/issues/654