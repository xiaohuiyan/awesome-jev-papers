# Search snapshot / 检索记录

**Broad-search snapshot:** 2026-10-16, Asia/Shanghai. **Window:** 2025-10-16–2026-10-16, plus four marked foundations. **Latest targeted addition:** 2026-10-17.

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

## Current outcomes (2026-10-17)

| Outcome | Count |
| --- | ---: |
| Unique candidates | 284 |
| Included | 173 |
| Direct Jev | 117 |
| Related models / methods | 52 |
| Earlier foundations | 4 |
| Excluded | 109 |
| Pending further evidence | 2 |
| Papers with verified author-linked GitHub code | 52 |

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

原始检索合并站内检索、官方 API 查询和参考文献扩展。2026-10-17 根据用户提供的链接补充 StartLux-Decision，核实元数据、正文中的 Jev 对比及作者代码；此次单篇补充不代表重新检索或复核整个目录。累计 **284 个去重候选**，正式收录 **173 篇**，排除 **109 篇**，另有 **2 篇待核实**。正式目录分为 **117 篇 Jev 直接相关、52 篇同类模型与方法、4 篇基础背景**；**52 篇**有已核实可访问的作者 GitHub 代码链接。

目录覆盖本次检索中截至 10 月 15 日提交的论文，不代表 10 月 16 日所有投稿均已公开或被索引。摘要中没有明确关系的论文，必要时查询正文；同名模型、通用双系统研究及仅在 URL 中出现 Jev 的结果不会直接收录。
