# Social-platform paper discovery / 社交平台论文检索（2026-11-04）

**Reviewed / 核实日期:** 2026-11-04 (Asia/Shanghai). [Query and lead ledger / 查询与线索记录](../data/social-search-2026-11-04.json).

## Result / 结果

This social round contributed **no new records of its own** — every arXiv ID it surfaced was already catalogued, and no platform-only lead resolved to an arXiv record. The day's 52 additions all came from the arXiv API sweeps, including the whole-window variant backfill (2026-09-15 forward) that the 2026-11-02 round's blind-spot findings motivated; the social round served as the cross-check that the sweeps had indeed caught everything visible. Notable resolutions: two independent [Jev-X](https://jev-x.com/) posts (11/02, 11/03) on the **DecisionRAG** paper both resolve to the already-included [2610.35868](https://arxiv.org/abs/2610.35868v1); the vendor citation index ([jevmodel.ai/citations](https://jevmodel.ai/citations), header now 2026-11-03) added [2609.37647](https://arxiv.org/abs/2609.37647), also already catalogued. The catalogue now stands at **309 papers**: 200 direct Jev, 105 related methods, four foundations, with 113 papers carrying verified author-linked code.

本轮社媒检索**没有独立贡献新记录**——它带出的每个 arXiv 编号均已在目录中,平台独有的线索也未解析到任何 arXiv 记录。当日新增的 52 篇全部来自 arXiv API 扫描,包括由 11-02 轮盲区发现所推动的全窗口变体重扫(2026-09-15 起);社媒轮充当了交叉核验,确认扫描已覆盖所有可见内容。值得记录的解析:[Jev-X](https://jev-x.com/) 两条独立帖子(11/02、11/03)讨论的 **DecisionRAG** 均解析到已收录的 [2610.35868](https://arxiv.org/abs/2610.35868v1);厂商引用索引([jevmodel.ai/citations](https://jevmodel.ai/citations),页头已更新至 2026-11-03)新增 [2609.37647](https://arxiv.org/abs/2609.37647),同样已收录。目录现共 **309 篇**:200 篇 Jev 直接相关、105 篇同类方法、4 篇基础背景;113 篇有已核实作者代码。

## Platform coverage / 平台覆盖

| Platform | What was searched or read | Result and limitation |
| --- | --- | --- |
| 微信公众号 | Web searches for 公众号 Jev articles dated 11-01 through 11-04. | All surfaced IDs already catalogued; commentary is explainer/product news (Jev Chat Jarvis, aigc.bar 解析, JEV 融资回顾); the 电车难题 lead (屠荒者) still has no arXiv record. |
| 知乎 | `site:zhihu.com` search (10 results read) plus an exact follow-up on the 30-day survey post (2026-10-16, 从Jev 到 OpenAI Decisions). | The survey post and the MedJev / Chinese-Jev / Jev-Mem roundups reference already-catalogued papers; 2606.12372 was excluded on 2026-11-01; no new records. |
| 新浪微博 | `site:weibo.com` search. | One product-explainer post (只会涂答题卡的AI Jev); no arXiv records. |
| X / Twitter | Web searches; [Jev-X](https://jev-x.com/) posts through 11/03; follow-ups on DecisionRAG and Smaug-Audio-Decisions. | DecisionRAG resolves to already-included 2610.35868. **Smaug-Audio-Decisions-0.7B** (Abacus.AI, Bindu Reddy, 11/03) is a Hugging Face model card — a fine-tune of EmbeddingGemma for 10 ms audio decisions — with **no arXiv paper**; product-only item. Remaining posts are Claude-Code + Jev routing tutorials and product use cases (spam-reply ranking, Solana pair vetting). |
| 厂商索引 | [jevmodel.ai/citations](https://jevmodel.ai/citations) (header 2026-11-03). | Updated since 10-31: newly added 2609.37647, already catalogued; earlier citations unchanged. The summarizing fetch truncated at card 126 of 234, so any later additions were not visible. |

## Unresolved leads / 待核实线索

| Lead | Disposition |
| --- | --- |
| ResearchGate publication *Referring uncertain answers by decision-model confidence: Jev, OpenAI Decisions and Clef on Korean and US medical licensing examination questions*, carried over from 2026-10-30. | Still ResearchGate-only (dated 2026-10-14); no arXiv record; carried over again. |
| WeChat article *Jev 决策模型遇上电车难题* (account 屠荒者), carried over from 2026-10-27. | Still no arXiv record located; carried over again. |
| alphaXiv (@askalphaxiv) 4B decision model trained with OpenResearch on 117k+ decision examples, carried over from 2026-11-02. | Still an X post only; no arXiv record or technical report. |
| **Smaug-Audio-Decisions-0.7B** (Abacus.AI / Bindu Reddy, new this round). | Hugging Face model card only (audio-decision fine-tune of EmbeddingGemma); watch for a technical report. |
| Product/leaderboard news: MiniCPM-OCR Jev verification model, OpenDecider, Decision-3.0, NeoHorse-Jev-4B, jev-router cost tests. | Product, leaderboard and tooling news without arXiv records; keep watching for accompanying papers. |

Social summaries supplied only discovery leads; the formal evidence for every added paper comes from the original arXiv metadata, abstracts and inspected full text. Discovery dates are not paper submission dates.
