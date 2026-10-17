# Changelog

## 2026-10-17

- Simplified every paper entry to four fields — published date, authors, problem addressed, and core contribution — in a uniform card layout headed by the title with PDF and verified-code links directly beneath it; entries carry no blank lines and are separated only by a horizontal rule. Removed the inline id/version line, tag list, relation note, verification dates and expandable details block from the READMEs. Added a bilingual `problem` statement to all 174 papers in `data/papers.json` (18 reuse their reading-guide question); author lists over four names are shown as the first three plus a count, with full lists still in the evidence ledger and BibTeX. Validation now requires the new field. Paper selection, reviewed versions, evidence and code links are unchanged.
- Refreshed both READMEs with a compact overview, a ten-paper reading path, question-led category navigation, and consistent paper entries with expandable author and provenance details. Added bilingual reading questions and clearer summaries for 18 featured papers; localized Chinese tags. This is an editorial update: the 174-paper selection, reviewed versions, evidence and verification dates are unchanged.
- Rechecked five user-supplied papers against current arXiv versions; all were already included. Refined bilingual notes on bias, ToM, scientific decisions, LLM-as-Jev and the early evidence audit; documented experiment sizes, latency and scope in [source-check notes](docs/FIVE_PAPER_REVIEW_2026-10-17.md). Paper count remains 174.
- Searched public X/Twitter, Sina Weibo, Xiaohongshu and WeChat sources; documented platform access limits and unresolved social leads in a separate audit.
- Added the missed v2 of *Evaluating Decision Models for Text Annotation in Computational Social Science* from a readable WeChat roundup, with original-paper evidence and author code. Catalogue now has 174 papers (118 direct, 52 related, four foundations), with verified code for 53 papers.
- Added StartLux-Decision (arXiv:2610.17309v1) under model architectures and training, with direct Jev relation established by full-text comparisons.
- Added bilingual notes, source evidence, BibTeX and the verified author-linked code repository for StartLux-Decision. Totals immediately after that addition were 173 papers, including 117 direct Jev papers, and 52 papers with verified author-linked code.
- Recorded this user-supplied addition separately from the original broad search; preserved each paper's verification date in BibTeX.

## 2026-10-16

- Initial bilingual arXiv catalogue: 172 papers across six categories; 116 direct Jev studies/reviews, 52 closely related models/methods, and four earlier foundations.
- Screened 283 unique candidates; documented 109 exclusions and two pending cases.
- Added 51 author-linked public GitHub repositories, verified for reachability.
- Pinned arXiv metadata and evidence to reviewed versions, including revised titles and full-text relation checks.
- Added JSON, BibTeX, an evidence ledger, contribution rules, deterministic rendering and offline CI validation.
- No scheduled paper collection is enabled.
