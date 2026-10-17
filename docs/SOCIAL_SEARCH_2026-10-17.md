# Social-platform paper discovery / 社交平台论文检索

**Reviewed / 核实日期:** 2026-10-17 (Asia/Shanghai). [Query and lead ledger / 查询与线索记录](../data/social-search-2026-10-17.json).

## Result / 结果

Added **one previously missed paper**, bringing the catalogue to **174 papers**: 118 direct Jev, 52 related methods, and four foundations. There are now 53 papers with verified author-linked public GitHub code. This is a coverage correction: the added paper was first submitted in September, not newly submitted on the search date.

本轮新增 **1 篇此前遗漏的论文**，总计 **174 篇**：118 篇 Jev 直接相关、52 篇同类模型与方法、4 篇基础背景；53 篇有已核实作者代码。新增论文首次提交于 9 月，不能将本次发现日期写成论文发表日期。

### Added paper / 新增论文

[Evaluating Decision Models for Text Annotation in Computational Social Science](https://arxiv.org/abs/2609.24574v2) — Hazem Ibrahim and Yasir Zaki. First submitted 2026-09-21; reviewed **v2**, revised 2026-09-23.

- **Category / 分类:** Benchmarks and comparative evaluation / 基准测试与比较评估; direct Jev / Jev 直接相关.
- **Discovery / 发现来源:** [WeChat paper roundup](https://mp.weixin.qq.com/s/kK3du8zji4fa_9chnBl7Dw), located through the [Promethe-us community index](https://github.com/Promethe-us/awesome-jev/blob/main/README.md). The original WeChat article body was readable; its publication date was not independently extracted.
- **Verification / 核实:** Official arXiv metadata, abstract and targeted full text establish the Jev evaluation. The paper links the accessible [author replication repository](https://github.com/hazemibrahim97/decision-models-css). Experiments were not rerun.
- **Contribution / 贡献:** A matched zero-shot comparison across 18 social-science tasks and 7,977 items, examining annotation quality, confidence and escalation to LLMs. 在统一零样本设置中比较文本标注质量、置信度和向 LLM 升级的策略；结论受任务与协议限制。

The roundup supplies 13 arXiv identifiers. Twelve were already included; only this paper was added. All identifiers and their dispositions are in the JSON ledger. Social summaries supplied leads; the [formal evidence](EVIDENCE.md#evidence-2609-24574) comes from the original paper.

公众号盘点中的 13 个 arXiv 编号有 12 个已收录，仅新增上述一篇。正式收录依据来自论文原文，社交媒体只用于发现线索。

## Platform coverage / 平台覆盖

| Platform | What was searched or read | Result and limitation |
| --- | --- | --- |
| X / Twitter | Domain queries, [Jev-X](https://jev-x.com/) recent-post index, paper discussions in public profile mirrors, and [source notes](https://jevmodel.ai/citations/). | Existing-paper overlap and unresolved manuscript claims. Attempting the [Arize original post](https://x.com/arizeai/status/2107891481789022324) returned HTTP 403. Secondary-index content is explicitly labelled; it is not presented as verified original X content. |
| 新浪微博 | Public search-index snippets, including [宝玉xp's introduction](https://weibo.com/2/detail/5343782388109072), a [model overview](https://weibo.com/2/detail/5345122607694263), and [ecosystem commentary](https://weibo.com/2/detail/5344879783710295). | The accessible material concerns announcements and demonstrations. No new paper was verified from these posts; direct web access reported robots restrictions. |
| 小红书 | External search queries, a community index of note links, and the [public search page](https://www.xiaohongshu.com/search_result?keyword=Jev). | The search page requires login. Note text, authors and timestamps were not verified; no paper added from this platform. This is an access gap, not evidence that no relevant papers exist. |
| 微信公众号 | Domain queries, [Sogou WeChat search](https://weixin.sogou.com/weixin?type=2&query=Jev), and the readable original roundup linked above. | One verified addition and 12 duplicates from the roundup. Broader coverage remains incomplete; recent search snippets also included tutorials and already-covered judge work. |

公开搜索并不等于四个平台的完整站内搜索。小红书需登录；微博与部分 X 原文访问受限；微信公众号主要依靠搜狗公开索引及可读取原文。搜索工具偶尔返回域外或日期不符的结果，这些结果未被当作指定平台的已核实材料。

## Unresolved or insufficient leads / 待核实与证据不足的线索

These are social leads without established new arXiv records, separate from the two pending arXiv candidates in [PENDING.md](PENDING.md). They do not increase the formal paper count or enter BibTeX.

| Lead | Disposition |
| --- | --- |
| A support-routing post attributed to `@slash1sol`, displayed as 10/14 in [Jev-X](https://jev-x.com/), calls an item an October 12 arXiv paper. | Exact title, authors and scholarly identifier were not established. Keep unresolved; do not treat the quoted cost scenario as a verified paper result. |
| A trading post attributed to `@bl888m_eth`, displayed as 10/16 in [Jev-X](https://jev-x.com/), describes a tutorial as a research paper. | No verified manuscript identifier found. Keep unresolved until an accessible research manuscript can be checked. |
| [Sina repost of a TimePrism / From Samples to Scenarios article](https://finance.sina.com.cn/stock/t/2026-09-27/doc-inithqpy3279615.shtml), labelled as originating from 机器之心Pro. | A media analogy between probabilistic forecasting and Jev does not establish a direct model relationship. The original WeChat URL was not established; no addition under the focused scope. |

相对时间、热度、宣传中的性能数字及“论文”称呼均不作为收录依据。无法确定论文身份的线索单列保存，不编造 arXiv 编号、不纳入正式统计。检索日期更新也不代表既有 173 篇全部重新核实。
