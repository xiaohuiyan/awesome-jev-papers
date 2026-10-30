# Search snapshot / 检索记录

**Broad-search snapshot:** 2026-10-16, Asia/Shanghai. **Window:** 2025-10-16–2026-10-16, plus four marked foundations. **Latest targeted addition:** 2026-10-30.

The complete machine-readable record is [search-log.json](../data/search-log.json); decisions for all candidates are in [screening.json](../data/screening.json).

## Discovery sequence

1. Resolve “Jev” through academic and web searches, beginning with Jev model evaluations and System One decision papers.
2. Search for typed decision models and architectures. Refine using calibration/risk control and named entities including AnyJev, FastJEV, Kev and Dyad. The broad combined-name query was low precision; subsequent queries separated model names.
3. Read the references and corpus appendix of [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/html/2609.32160v1). Use its early-paper corpus as leads and its calibration, rejection, cascading and classifier references to select four foundations. Independently verify included metadata.
4. Search [arXiv for Jev](https://arxiv.org/search/?query=Jev&searchtype=all&abstracts=show&order=-announced_date_first&size=200): **142 hits**. Fetch these records and additional verified seeds/foundations through the official Atom API: **153 unique records** in that request.
5. Fill terminology gaps with date-bounded Atom queries for `System One` (**151 results**) and `typed decision` (**49 results**). The query URLs and parameters are preserved in the JSON log. Each returned fewer than the 200-record request limit.
6. Merge by version-independent arXiv ID, screen title/abstract content, and inspect full-text passages where model identity or direct Jev involvement is ambiguous.

## Targeted additions

- **2026-10-17:** Added the user-supplied [StartLux-Decision](https://arxiv.org/abs/2610.17309v1), first submitted on 2026-10-12. Verified official Atom metadata, the abstract, full-text Jev comparisons (Table 4 and Figure 11), and the author-linked public code repository. Classified as direct Jev / architectures and training. This addition does not represent a new broad search or re-verification of existing entries.
- **2026-10-27:** Added three papers surfaced by a user-requested survey of shared-state, multi-question inference (Semantic Scholar keyword searches and the related-work section of [Verdict-MQ](https://arxiv.org/html/2610.20778v1)): [Chinese Decision](https://arxiv.org/abs/2610.23170v2) as direct Jev (Section 5.1 compares with reported hosted-Jev results), and [DuplexJev](https://arxiv.org/abs/2610.02638v1) and [VoxTurn](https://arxiv.org/abs/2610.21150v1) as related methods. Three neighbouring candidates from the same survey were excluded; see the screening ledger. Like the 2026-10-17 addition, this is not a new broad search.
- **2026-10-29:** Swept arXiv first submissions 2026-10-27 through 2026-10-29 with the four standing queries (six unique candidates) and added five papers: [Learning to Formalize](https://arxiv.org/abs/2610.36595v1), [Decision Models as Judges for Hallucination Detection](https://arxiv.org/abs/2610.37229v1) and [knowledge-conflict typing for RAG](https://arxiv.org/abs/2610.36915v1) as direct Jev, plus [JevRec](https://arxiv.org/abs/2610.36937v1) and [DFIP](https://arxiv.org/abs/2610.36804v1) as related methods; one LLM group-decision study excluded. A same-day [four-platform social round](SOCIAL_SEARCH_2026-10-29.md) surfaced no additional records — every ID it produced was already catalogued.
- **2026-10-30:** Swept arXiv first submissions 2026-10-27 through 2026-10-30 (nine fresh candidates after deduplication — several 10-27/10-28 first submissions had been indexed only after the previous sweep ran) and added nine papers: five direct Jev ([PrimaCons](https://arxiv.org/abs/2610.38623v1), [MedQA benchmark](https://arxiv.org/abs/2610.38448v1), [World Reward Models](https://arxiv.org/abs/2610.38439v1), [citation prediction](https://arxiv.org/abs/2610.38090v1), [SatOps-Decision](https://arxiv.org/abs/2610.38697v1)) and four related methods ([JevAct](https://arxiv.org/abs/2610.38620v1), [DecisionUnlearn-Bench](https://arxiv.org/abs/2610.38431v1), [DeFT-RAG](https://arxiv.org/abs/2610.37826v1), [ThinkJev](https://arxiv.org/abs/2610.37732v1)); no exclusions. The same-day [social round](SOCIAL_SEARCH_2026-10-30.md) added [MedJev](https://arxiv.org/abs/2610.36006v1), which the standing queries had missed because of its hyphenated "System-One" title.

## Current outcomes (2026-10-17)

The [four-platform social search](SOCIAL_SEARCH_2026-10-17.md) added the missed [computational social science evaluation](https://arxiv.org/abs/2609.24574v2) through a readable WeChat roundup. Twelve other papers in that roundup were duplicates. Platform access limits and unresolved non-arXiv leads are recorded separately; the original broad-search snapshot remains unchanged.

| Outcome | Count |
| --- | ---: |
| Unique candidates | 285 |
| Included | 174 |
| Direct Jev | 118 |
| Related models / methods | 52 |
| Earlier foundations | 4 |
| Excluded | 109 |
| Pending further evidence | 2 |
| Papers with verified author-linked GitHub code | 53 |

This snapshot contains papers submitted through 15 October 2026 in the retrieved corpus. The date boundary is the review cutoff, not a claim that every paper submitted on 16 October had already been announced or indexed.

## Important corrections made during review

- Use the current title and v2 of [the candidate-coverage study](https://arxiv.org/abs/2610.03387v2), which now explicitly studies rejection-policy transfer.
- Preserve the revised titles and expanded settings of studies such as [rubric judging](https://arxiv.org/abs/2609.29769v3) instead of copying older search summaries.
- Upgrade papers such as [SearchJev](https://arxiv.org/html/2610.05107v1), [Jeva](https://arxiv.org/html/2610.18773v1) and [TypedBench](https://arxiv.org/html/2610.11392v2) to direct relation only after checking their Jev comparisons in the body.
- Include [probabilistic sensing for authority contracts](https://arxiv.org/abs/2610.10978) after the body identifies Jev as an experimental sensor, despite its absence from the abstract.
- Exclude [Lychee-Reranker](https://arxiv.org/abs/2606.22807) from this focused list: the inspected abstract mentions Jev only in a model-collection URL.

## Coverage limits

This is an arXiv-focused curated snapshot, not a proof of exhaustive coverage. Full-text-only mentions, papers without indexed abstracts, non-arXiv reports, unpublished model cards and newly announced revisions may be missed. Most entries were screened using abstracts; full-text checks were targeted to ambiguity and provenance. Citation counts were not gathered and experiments were not rerun.

The phrase searches produce false positives outside AI, and broad terms such as “decision model” are not sufficient inclusion evidence. Some nearby work is intentionally excluded to keep the corpus centered on Jev and comparable interfaces. Two unresolved cases are documented in [PENDING.md](PENDING.md).

## 中文摘要

原始检索合并站内检索、官方 API 查询和参考文献扩展。2026-10-17 补充 StartLux-Decision，并通过四个平台的公开检索，从公众号盘点中补录一篇计算社会科学标注评测。逐篇核实元数据、正文中的 Jev 对比及作者代码，未重新核实整个目录。累计 **285 个去重候选**，正式收录 **174 篇**，排除 **109 篇**，另有 **2 篇待核实**。正式目录分为 **118 篇 Jev 直接相关、52 篇同类模型与方法、4 篇基础背景**；**53 篇**有已核实可访问的作者 GitHub 代码链接。没有确定 arXiv 编号的社交线索另见[平台检索记录](SOCIAL_SEARCH_2026-10-17.md)，不计入上述候选数。

目录覆盖本次检索中截至 10 月 15 日提交的论文，不代表 10 月 16 日所有投稿均已公开或被索引。摘要中没有明确关系的论文，必要时查询正文；同名模型、通用双系统研究及仅在 URL 中出现 Jev 的结果不会直接收录。
