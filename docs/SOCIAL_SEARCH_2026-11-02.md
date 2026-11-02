# Social-platform paper discovery / 社交平台论文检索（2026-11-02）

**Reviewed / 核实日期:** 2026-11-02 (Asia/Shanghai). [Query and lead ledger / 查询与线索记录](../data/social-search-2026-11-02.json).

## Result / 结果

This social round contributed **2 papers**, both of which every arXiv API sweep had missed because their abstracts never use the standing query tokens. A WeChat explainer syndicated by 新浪财经 on 2026-11-02 ("Lev：让决策模型学会「难题多想」") resolved to [arXiv 2610.20951](https://arxiv.org/abs/2610.20951v1), *LEV: Thinking Fast and Deep with Looped Decision Models* (Lehigh University / UBC / Vector Institute, first submitted 2026-10-14), which reports the closed Jev 1.13.0 as a production-API reference; its abstract says "decision models", "System 1" and "JevBench". The exact-title follow-up of the ResearchGate lead carried since 2026-10-30 returned [arXiv 2610.31315](https://arxiv.org/abs/2610.31315v2), which on fetching proved to be a *different* uncatalogued paper — *The Value of System 1 Models in Medicine* (Technical University of Munich, University of Crete, Charité and others), evaluating hosted Jev 1.14, GPT-6 Luna Decisions, Clef and Clef-flash on 86 clinical tasks and 179,111 cases, with Jev 1.14 the best model on 45 of 78 primary tasks. The Ahn ResearchGate preprint itself still has no arXiv record (confirmed by API title and author queries) and is carried over again. Together with the four additions from the arXiv re-sweep of 2026-10-29/30, the catalogue now stands at **257 papers**: 173 direct Jev, 80 related methods, four foundations, with 90 papers carrying verified author-linked code.

本轮社媒检索**贡献 2 篇**,且两篇都因摘要从未使用标准查询词而被此前所有 arXiv API 扫描漏掉。新浪财经 2026-11-02 转载的公众号解读《Lev：让决策模型学会「难题多想」》核实为 [arXiv 2610.20951](https://arxiv.org/abs/2610.20951v1)——*LEV: Thinking Fast and Deep with Looped Decision Models*(Lehigh 大学 / UBC / Vector 研究所,首投 2026-10-14),以经生产 API 测得的闭源 Jev 1.13.0 为参考;其摘要只写 "decision models"、"System 1" 与 "JevBench"。对 10-30 以来悬而未决的 ResearchGate 线索做精确标题检索,返回了 [arXiv 2610.31315](https://arxiv.org/abs/2610.31315v2),抓取后发现是另一篇未收录论文——*The Value of System 1 Models in Medicine*(慕尼黑工业大学、克里特大学、夏里特等),在 86 个临床任务、179,111 个病例上评测托管 Jev 1.14、GPT-6 Luna Decisions、Clef 与 Clef-flash,Jev 1.14 在 78 个主任务中的 45 个上最佳。Ahn 的 ResearchGate 预印本本身仍无 arXiv 记录(API 标题与作者查询确认),继续挂起。加上 10-29/30 arXiv 重扫的四篇,目录达到 **257 篇**:173 篇 Jev 直接相关、80 篇同类方法、4 篇基础背景;90 篇有已核实作者代码。

## Platform coverage / 平台覆盖

| Platform | What was searched or read | Result and limitation |
| --- | --- | --- |
| 微信公众号 | Web search for 公众号 Jev articles; a 新浪财经 syndication dated 2026-11-02. | The Lev explainer resolved to [2610.20951](https://arxiv.org/abs/2610.20951v1), included this round; roundup IDs 2610.02076, 2609.26550, 2609.24965, 2609.29283 and 2609.26532 were already catalogued; the 电车难题 lead (屠荒者) is mirrored by 向上研究所 but still has no arXiv record. |
| 知乎 | Web search with `site:zhihu.com` (10 results read). | StartLux (2610.17309) already included; 2510.01237 and 2606.12372 were both excluded on 2026-11-01; no new records. |
| 新浪微博 | Web search with `site:weibo.com` (10 results read). | Explainer and product posts only; no arXiv records. |
| X / Twitter | Web searches; [Jev-X](https://jev-x.com/) recent-post index (no posts dated 11-01 or 11-02 yet); [jevmodel.ai citations](https://jevmodel.ai/citations/) index (header still 2026-10-31). | Web results surfaced 2610.27746 and 2610.03935, both included. Jev-X repeats the IBM JevAct and Cornell/ASAPP leads resolved on 2026-11-01, and adds an alphaXiv post on a 4B decision model trained with OpenResearch on 117k+ decision examples — an X post with no arXiv record or technical report. The vendor citation index is unchanged. |

## Unresolved leads / 待核实线索

| Lead | Disposition |
| --- | --- |
| ResearchGate publication *Referring uncertain answers by decision-model confidence: Jev, OpenAI Decisions and Clef on Korean and US medical licensing examination questions*, carried over from 2026-10-30. | Still no arXiv record (title and author API queries return nothing); the web search for it instead surfaced the TUM System 1 paper included this round. |
| WeChat article *Jev 决策模型遇上电车难题* (account 屠荒者), carried over from 2026-10-27. | Still no arXiv record located. |
| alphaXiv (@askalphaxiv) 4B decision model trained with OpenResearch on 117k+ decision examples. | X post only; no arXiv record or technical report yet. |
| Product/leaderboard news: MiniCPM-OCR Jev verification model, OpenDecider, Decision-3.0, NeoHorse-Jev-4B, jev-router cost tests. | Product, leaderboard and tooling news without arXiv records; keep watching for accompanying papers. |

Social summaries supplied only discovery leads; the formal evidence for every added paper comes from the original arXiv metadata, abstracts and inspected full text. Discovery dates are not paper submission dates.

社媒内容仅用于发现线索；每篇新增论文的正式收录依据均来自 arXiv 原始元数据、摘要与抽查正文。发现日期不等于论文提交日期。
