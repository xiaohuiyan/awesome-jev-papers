# Selection and review methodology / 收录方法

[English catalogue](../README.md) · [中文目录](../README.zh-CN.md) · [Search record](SEARCH_LOG.md)

## Scope

The main corpus covers first submissions from **2025-10-16 through 2026-10-16**, using the latest arXiv version verified on the snapshot date. A paper first submitted before the window is included only as an explicitly marked foundation. A revision inside the window does not reset the first-submission date.

**Jev** refers to the hosted model from TypeSafe. The broader topic is models and interfaces that return decisions or distributions over caller-supplied choices, binary questions or ordered scores. A common name, a System 1 metaphor or a repository URL containing “jev” does not establish technical relevance or shared model lineage.

## Relation levels

| Level | Requirement | Interpretation |
| --- | --- | --- |
| `direct` | The abstract or inspected body establishes use, evaluation, or substantive review of hosted Jev. | May include another model whose paper empirically compares it with Jev. It does not imply derivation from Jev. |
| `related` | A concrete contribution to closely related typed-decision models, readouts, calibration, control, or interfaces. | Hosted-Jev evaluation is not required. Reproduction of proprietary internals is not inferred. |
| `background` | A small, explicitly selected set of earlier foundations needed to interpret the field. | Not counted as direct Jev evidence. |

The six primary categories are architecture/training, evaluation, calibration/reliability, agents, security/robustness, and domain applications/efficiency. Each paper appears in exactly one category; tags represent overlapping themes. Foundations are presented separately even though they retain a category in the data.

## Evidence rubric

The author of the catalogue screens the accumulated candidate pool; no external model-based judge is used. Two criteria determine **relevance, not quality**:

| Criterion | Weight | Evidence |
| --- | ---: | --- |
| Topic fit | 0.60 | A short exact excerpt connecting the paper to hosted Jev or the defined decision-model problem. Direct relation scores 1; a close method connection scores 0.75; a foundation scores 0.5. |
| Substantive contribution | 0.40 | An excerpt supporting a proposed method, empirical evaluation, analysis, benchmark, or substantive review. Verified contributions score 1; unsupported criteria score 0. |

The total is calculated from these values. Main-corpus entries must score at least 0.70 and meet the explicit relation-level rule. Scores do not measure experimental rigor, novelty, peer-review status or model performance. Citation counts were not collected. The recommended ten-paper reading path is an editorial selection of eligible papers across topics, not a ranking by model accuracy.

Each evidence excerpt is at most 80 characters; the combined excerpts from a paper are at most 25 words. Sources are pinned to the version inspected. The full abstract is not republished. Full-text checking is targeted, not a claim that every paper has received a complete methodological review.

## Exclusion and pending decisions

Exclude lexical false positives, unrelated scientific meanings of “system one,” general decision theory, ordinary fixed-taxonomy classifiers without a close connection, and generic dual-process work lacking the relevant decision interface. A model name alone does not suffice.

If the available passages leave technical scope or model identity unresolved, record the candidate as **pending**, outside the formal catalogue. Keep its source and the unresolved question in the screening ledger. Excluded and pending items can be reconsidered when new evidence arrives.

## Source and version handling

- arXiv Atom metadata supplies exact titles, full author lists, first-submission dates, update dates, subjects and version IDs. The indexed web search is a discovery aid, not the final authority.
- The versioned abstract is the citation target. The unversioned arXiv link also appears so readers can check later revisions.
- `publication_status` records “arXiv manuscript.” A missing journal reference does not prove that a paper is unpublished. No conference acceptance is inferred from a title or search snippet.
- Only code repositories linked by authors in an abstract, comments, or inspected full text are shown. GitHub API access confirms that the repository is public and reachable. It does not prove that the code is complete, reproducible, licensed for a particular use or equivalent to the paper's experiments.
- No code link means **not verified**, not “no code exists.” Anonymous repositories, model hubs and project pages may remain discoverable through the paper but are not relabelled as verified GitHub code.
- The catalogue paraphrases research contributions. Numerical results are not compared across incompatible datasets, hardware, model versions, inference protocols or prices.

## Data interface

`data/papers.json` is the source of truth (schema version 1). Its top level contains the date window, categories, relevance weights, recommended IDs and `papers`. Each paper has:

- Stable `arxiv_id`, exact `title`, complete `authors`, first-submission/update dates and reviewed `version`.
- Primary category, relation level, cross-topic tags, bilingual `summary` and `relation`.
- Versioned source URLs, short criterion evidence, calculated relevance and review depth.
- Author-linked code URLs with provenance and verification date.
- An abstract fingerprint for checking metadata against the pinned arXiv record without redistributing the abstract.

`data/screening.json` records every unique candidate and its decision. `data/search-log.json` records queries and coverage. `data/code-checks.json` records the GitHub link checks. Generated README files, the evidence ledger and BibTeX are derived from the same dataset.

## 中文说明

主目录按首次提交日期覆盖近一年，使用截至 2026-10-16 核实的最新版本；早期基础论文单列。直接相关必须有使用、评测或实质综述托管 Jev 的证据。同类方法可以采用相似接口，但不能仅凭名称推断继承关系或复现了专有架构。

每篇仅归入一个主分类，并使用交叉标签。筛选依据是主题相关性与实质贡献，分数不是论文质量或模型性能评分。大多数条目依据摘要筛选，必要时核查正文；不声称逐篇完成完整实验审计。无法确定的候选留在待核实台账中。

代码链接必须由论文作者提供并确认公开可访问；没有展示链接仅代表本次未核实。标题、作者、日期和版本以 arXiv 为准，不从搜索摘要推断发表状态。跨论文的数字结果不直接比较，也不将作者报告等同于独立复现。
