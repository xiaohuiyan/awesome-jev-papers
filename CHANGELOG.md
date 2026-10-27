# Changelog

## 2026-10-27

- Swept arXiv for first submissions from 2026-10-17 through 2026-10-26 with API queries on "Jev", "System One", "typed decision" and "decision model" (57 unique candidates) and added **48 papers**: 31 direct Jev (use, evaluation or substantive review of the hosted model, version-pinned where stated, e.g. jev-1.13.0 and Jev 1.14) and 17 closely related methods. Catalogue: **222 papers** (149 direct, 69 related, four foundations).
- Verified every added paper against arXiv metadata and abstracts; inspected targeted full text (LaTeXML HTML, PDF fallback for two papers) for relation decisions, author affiliations and author-linked code. Nine exclusions are logged in the screening ledger (unrelated acronyms, general decision theory, fixed-taxonomy classifiers, incidental mentions), plus the September crypto-accounting benchmark surfaced by the jevmodel.ai citation index.
- Added 22 verified author-linked GitHub repositories (GitHub API confirmed public; one printed code URL, Iris, was unreachable and stays unverified). 75 papers now have verified code. Screening ledger: 343 candidates (222 included, 119 excluded, 2 pending).
- Extended the main first-submission window to 2026-10-26 and recorded per-paper verification dates of 2026-10-27.
- Searched WeChat (Sogou index), Zhihu, Sina Weibo and X (Jev-X, jevmodel.ai); social channels produced no additional verifiable arXiv records — documented with platform limitations and unresolved leads in [the 2026-10-27 social-search audit](docs/SOCIAL_SEARCH_2026-10-27.md).

## 2026-10-17

- Rechecked user-supplied *Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges* (arXiv:2610.18122); arXiv still shows only v1 (2026-10-13) and the paper was already included as a direct-Jev entry under security with verified author code. No data changes needed; paper count remains 174.
- Added author affiliations to every entry that states them: 165 of 174 papers now show a 🏢 affiliations line between authors and problem. Values were collected from the version-pinned sources themselves — LaTeXML HTML full text (with a second pass over `<br>`-separated and broken frontmatter layouts), plus PDF first pages where HTML is missing or malformed — then cleaned (emails, footnotes, author-list leaks, place fragments, glued multi-institution lines) and spot-checked; common abbreviations in VideoJev were expanded. Nine papers state no affiliation anywhere in their text and omit the field; three of those inferences rely on the paper's own contact email domain (Microsoft ×2, Rice University) and one on the paper's own repository org. Lists longer than five institutions are truncated with a count.
- Simplified every paper entry to four fields — published date, authors, problem addressed, and core contribution — in a uniform card layout headed by the title with PDF and verified-code links inline after it; entries carry no blank lines and are separated only by a horizontal rule. Removed the inline id/version line, tag list, relation note, verification dates and expandable details block from the READMEs. Added a bilingual `problem` statement to all 174 papers in `data/papers.json` (18 reuse their reading-guide question); author lists over four names are shown as the first three plus a count, with full lists still in the evidence ledger and BibTeX. Validation now requires the new field. Paper selection, reviewed versions, evidence and code links are unchanged.
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
