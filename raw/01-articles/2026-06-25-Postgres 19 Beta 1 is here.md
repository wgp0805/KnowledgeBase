---
title: "Postgres 19 Beta 1 is here"
source: "PostgreSQL Weekly"
url: "https://postgresweekly.com/issues/652"
date: "Wed, 10 Jun 2026 00:00:00 +0000"
score: 1.0
tags: ["PostgreSQL", "数据库", "SQL"]
auto_captured: true
---

# Postgres 19 Beta 1 is here

> **来源**: PostgreSQL Weekly  
> **链接**: https://postgresweekly.com/issues/652  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

| #​652 — June 10, 2026 | [Web Version](<https://postgresweekly.com/link/186354/rss>)  
---|---  
---  
Postgres Weekly  
---  
[![](assets/2026-06-25-Postgres%2019%20Beta%201%20is%20here/ef90637fbadd6ef7b41eeb91dc6716aa_MD5.jpg)](<https://postgresweekly.com/link/186319/rss>)  
---  
[PostgreSQL 19 Beta 1 Released](<https://postgresweekly.com/link/186319/rss> "www.postgresql.org") — One of the more exciting major releases of Postgres is a step closer with graph queries, faster inserts, [pg_plan_advice](<https://postgresweekly.com/link/186320/rss>), parallel-worker autovacuuming, [online toggling of data checksums](<https://postgresweekly.com/link/186322/rss>), and more, all ready to try now. Final release will be around late September/early October. PostgreSQL Global Development Group   
---  
💡 Ready to give Postgres 19 a spin? Here's [how to get it running in Docker](<https://postgresweekly.com/link/186323/rss>) or [on a Kubernetes cluster](<https://postgresweekly.com/link/186324/rss>).  
---  
[![](assets/2026-06-25-Postgres%2019%20Beta%201%20is%20here/16e9921b0742286dbaf0289fc0d3867e_MD5.png)](<https://postgresweekly.com/link/186318/rss>) [Come for Great PostgreSQL Talks, and Yes, There’s Swag](<https://postgresweekly.com/link/186318/rss> "posetteconf.com") — POSETTE: An Event for Postgres is around the corner (16-18 Jun). Pick & attend your must-sees. Join the Hallway Track on Discord for limited, exclusive event swag for attendees to the live event from anywhere in your slippers. Last call: [Register now](<https://postgresweekly.com/link/186318/rss>). Microsoft | AMD sponsor  
---  
**IN BRIEF:**

  * 📘 The [official Postgres 19 documentation](<https://postgresweekly.com/link/186326/rss>) is now taking shape, such as [this page on property graphs](<https://postgresweekly.com/link/186327/rss>) and [the draft release notes](<https://postgresweekly.com/link/186329/rss>).
  * 💰 [Supabase has raised a $500m Series F round](<https://postgresweekly.com/link/186330/rss>) at a valuation of $10bn.
  * Spectral Core has [unveiled SQL Tran](<https://postgresweekly.com/link/186331/rss>), a (commercial) tool for automating Oracle to Postgres migrations.

  
---  
⚾ [Comparing the Graph Capabilities of Postgres, DuckDB, and LadybugDB](<https://postgresweekly.com/link/186332/rss> "theconsensus.dev") — A baseball-oriented comparison of how three databases fare (both in terms of developer experience and raw performance) with making graph-style queries across millions of rows of player, venue, and game data. John Nevin   
---  
[`EXPLAIN` Prettier (or Post-Processing Query Plans)](<https://postgresweekly.com/link/186333/rss> "www.pgedge.com") — `EXPLAIN` output can be tricky to read at the best of times and it can also change subtly between machines and versions. Andrei shows off [explain_prettier](<https://postgresweekly.com/link/186334/rss>), which makes `EXPLAIN` output cleaner and simpler by stripping away unnecessary info. Andrei Lepikhov   
---  
📄 [The Postgres Developer's Guide to Vector Index Tradeoffs](<https://postgresweekly.com/link/186335/rss>) – Find out what HNSW, IVFFlat, DiskANN, and SPFresh indexes are and when to pick each of them. Hien Phan (Tiger Data) 📄 [SQL’s `ORDER BY` Has Come a Long Way](<https://postgresweekly.com/link/186337/rss>) – A feature tour from the 80s through to the ISO-specified SQL:2023 present. Markus Winand 📄 [Does pgBackRest Work with `pg_tde`?](<https://postgresweekly.com/link/186338/rss>) – Can pgBackRest handle encrypted WAL segments transparently? Mostly, yes! Stefan Fercot 📄 [File Descriptors: The OS Limit That Takes Down Postgres](<https://postgresweekly.com/link/186339/rss>) Warda Bibi  
---  
---  
|   
---  
📰 Classifieds  
---  
🧮 [Build a full RAG stack inside Postgres](<https://postgresweekly.com/link/186340/rss>). Docloader, Vectorizer, RAG, & MCP. [100% open source](<https://postgresweekly.com/link/186340/rss>). 🐘 AI wrote the migration. Who reviews it? Open-source multi-agent PR review - a custom review lens per PR, cents per run. [Star & deploy →](<https://postgresweekly.com/link/186341/rss>)  
---  
---  
---  
**RELEASES AND CODE:**  
---  
[Absurd: A Postgres-Native Durable Workflow System](<https://postgresweekly.com/link/186342/rss> "earendil-works.github.io") — Described as _“the simplest durable execution workflow system you can think of”_ , Absurd is [an SQL file](<https://postgresweekly.com/link/186343/rss>) that implements a multi-step task/queue/worker system on regular Postgres. There are [SDKs](<https://postgresweekly.com/link/186344/rss>) to make it easy to use from TypeScript, Python, and Go. Armin Ronacher (Earendil)   
---  
[Multigres v0.1 Alpha: An 'Operating System' for Postgres](<https://postgresweekly.com/link/186345/rss> "supabase.com") — A year ago, [Supabase announced](<https://postgresweekly.com/link/186346/rss>) it was hiring the co-creator of Vitess to work on a Vitess-like horizontally-scaling database clustering system but for Postgres. This alpha is an early public look at what they’re building. Sugu Sougoumarane   
---  
  
  * [TimescaleDB 2.27](<https://postgresweekly.com/link/186347/rss>) – Tiger Data's time series extension continues its focus on performance with more efficient operations on compressed data in particular.
  * [pg_clickhouse 0.3](<https://postgresweekly.com/link/186348/rss>) – FDW for querying ClickHouse databases from Postgres. The underlying C++ library gets switched out for a faster, more robust C alternative.
  * [pg_background 2.0](<https://postgresweekly.com/link/186349/rss>) – Run SQL in background workers. Now works with Postgres 19.
  * [Kanel 4.0](<https://postgresweekly.com/link/186350/rss>) – Generate TypeScript types from a live Postgres database.
  * [pgrls](<https://postgresweekly.com/link/186351/rss>) – Static analyzer for RLS (Row-Level Security) to catch common policy bugs.
  * [NeonD](<https://postgresweekly.com/link/186352/rss>) – Open-source Neon-based control plane daemon for Postgres that runs as a single Docker container.
  * [pgcheck](<https://postgresweekly.com/link/186353/rss>) – A lightweight Postgres health-check CLI written in Go.

  
---  
---  
  
![](assets/2026-06-25-Postgres%2019%20Beta%201%20is%20here/7c0468a65b11fa22737726364a0ece63_MD5.gif)


---
> 原文链接: https://postgresweekly.com/issues/652