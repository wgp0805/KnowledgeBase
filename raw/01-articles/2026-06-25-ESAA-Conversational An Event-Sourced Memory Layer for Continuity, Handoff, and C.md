---
title: "ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents"
source: "arXiv SE"
url: "https://arxiv.org/abs/2606.23752"
date: "Wed, 24 Jun 2026 00:00:00 -0400"
score: 1.0
tags: ["软件工程", "论文", "研究"]
auto_captured: true
---

# ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents

> **来源**: arXiv SE  
> **链接**: https://arxiv.org/abs/2606.23752  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

arXiv:2606.23752v1 Announce Type: new Abstract: Software developers increasingly work with multiple LLM coding agents, switching among tools such as Codex, Grok, Claude Code, and other assistants as context windows fill, sessions end, or a particular agent becomes better suited to a subtask. Each agent, however, persists its conversation in a private and vendor-specific log. The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. This paper presents \emph{ESAA-Conversational}, a domain specialization of Event-Sourcing Agent Architecture (ESAA)~\cite{esaa} for shared conversational memory across heterogeneous agents. The method treats the visible conversation as a local event store: hooks and watchers capture visible turns, normalize them into an append-only \texttt{activity.jsonl}, and deterministically project read models such as \texttt{handoff.md}, \texttt{state.md}, \texttt{decisions.md}, and \texttt{tasks.json}. Mechanical capture does not require LLM inference; agents use judgment only for explicit curation, recording durable decisions and conversational tasks through domain commands. The public v1.1.0 release implements a PowerShell CLI with \texttt{init}, \texttt{enable-hooks}, \texttt{sync}, \texttt{project}, \texttt{verify}, \texttt{context}, \texttt{decide}, and \texttt{task}; includes \texttt{workspace\\_root} isolation and a write-path lockfile; and is distributed as a greenfield package with an empty public log. A self-referential case study with 570 development-lab events shows that heterogeneous agents can collaborate through a shared log without a direct agent-to-agent channel, while the public distribution preserves privacy by excluding the private conversational history.


---
> 原文链接: https://arxiv.org/abs/2606.23752