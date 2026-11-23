# X / 中文平台检索（2026-11-23）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询与线索台账](../data/social-search-2026-11-23.json) · [同日 arXiv 第 20 轮](ARXIV_SEARCH_2026-11-23.md)

检索窗口：**2026-11-19 至 2026-11-23**（自 11-19 第 19 轮以来的空档日），另加无日期补充查询、观察线索定向核查、四个外部 awesome 清单对照与 [Jev Daily](https://jevdaily.com) 逐期直达。论文首次提交日期以 arXiv 记录为准，与帖子/文章日期分开处理。

**本轮社媒线索独立新增 0 篇。** X 交叉检索给出六个 arXiv ID——[钓鱼邮件对比](https://arxiv.org/abs/2611.23683v1)（2611.23683）、[AnyS1](https://arxiv.org/abs/2611.23751v1)（2611.23751）、[Jeveration](https://arxiv.org/abs/2611.24738v1)（2611.24738）、[LLM 置信度分类研究](https://arxiv.org/abs/2611.25289v1)（2611.25289）、[LoopRoute](https://arxiv.org/abs/2611.25363v1)（2611.25363）、[VisualJevBench](https://arxiv.org/abs/2611.25435v1)（2611.25435）——逐条经 id_list 标题核验后，**全部已在同日 arXiv API 扫描池内**，并随[第 20 轮](ARXIV_SEARCH_2026-11-23.md)收录；X 检索另提到已收录的 JevRSI（2611.22432）与 Small Heads（2611.15592）出现了新版本，目录条目仍固定在已核验版本。**Jev Daily 连续出刊**（11-19、11-20、11-21、11-22 四期，11-23 尚未发布），均为生态新闻，无任何 arXiv ID。**新观察线索一条**：HeyGen Decision 1（11-13 上线 HeyGen API 与 OpenRouter，单次请求最多 400 个问题、覆盖文本/JSON/图像/视频帧，每个答案返回校准概率），未见 arXiv 报告。

## 本轮社媒新增

无。检索与结果全部记录在 [JSON 台账](../data/social-search-2026-11-23.json)。

| 平台 | 检索与读取 | 结果与限制 |
| --- | --- | --- |
| 微信公众号 | `site:mp.weixin.qq.com Jev 决策模型 System One 2026年11月`。 | 没有任何 mp.weixin.qq.com 结果（微信文章索引不全，不能据此断言无新内容）；返回的是 9–10 月发布期的解读（Eigent 博客、百度 AI Studio、科学网新闻），无新论文线索。 |
| 知乎 | `site:zhihu.com Jev 决策模型 System One TypeSafe 2026年11月`。 | 只命中已知的专栏《Jev：全球首款System One 决策模型》，其余为 9–10 月科普文的站外转载；无新专栏、无新论文线索。 |
| 新浪微博 | `site:weibo.com Jev 决策模型 论文 TypeSafe`。 | 没有任何 weibo.com 结果；腾讯云开发者社区（09-23）、36氪与 PANews 的发布期报道而已；无新论文线索。 |
| X / Twitter（交叉） | `Jev TypeSafe decision model arxiv new paper November 20 21 22 23 2026`；`site:x.com OR site:twitter.com Jev TypeSafe "System One" arxiv paper November 2026`；另做两条标题定向检索。 | 六个 arXiv ID 全部已在扫描池内（见上）。其余为 Jev-Mem 发布帖（已收录 2609.23986）、TypeSafe 融资报道、OpenRouter 路由讨论，以及指向已收录的 2611.15592 的推文。X 原生搜索不可达，依赖网页索引。 |
| Jev Daily（聚合站） | 直达 `issues/2026-11-19`、`/2026-11-20`、`/2026-11-21`、`/2026-11-22`（均 200，已通读全文）、`/2026-11-23`（404，未出刊）。 | 四期均为生态新闻：Rivet 把一个 Jev 严重度问题拆成三个是非题、PostHog 的「便宜 444.6 倍」说法、HeyGen Decision 1 上线 OpenRouter（中位 93 ms）、TypeSafe 与 Strala 的保险案例、Colgate 的 LLM 合成消费者研究、Raindrop 的 11 个决策模型对比、Nathan Flurry 的「是否回复」门控代码。无 arXiv ID、无论文线索。 |
| 外部清单对照 | awesome-jev / awesome-system-one / awesome-decision-models / awesome-jev-security 四清单 raw README 拉取比对。 | **本轮不再全净**：awesome-jev-security 新列的三个 ID（2611.23683、2611.23947、2611.25435）均已在扫描池内；awesome-system-one 新增 2605.19099（「DecisionBench (delegation)」，实为 LLM 委派基准）并在正文把 2609.14973 标为 AutoTrust Decider-Pro 的论文（实际解析为 PhysBrain 1.5），两条均经核验后排除；awesome-jev 的三个窗口前 ID 与 awesome-decision-models 维持既定处置。 |

## 线索处置

- **HeyGen Decision 1**：新增观察线索。据网页检索摘要与 Jev Daily 11-21（未对照一手来源）：11-13 上线 HeyGen API（模型 ID `heygen-decision-1`，接口 `POST /v3/models/decisions`），另上 OpenRouter；单次请求最多 400 个问题，覆盖文本/JSON/图像/视频帧，返回是非校验分、多选项分与有序排序。未见 arXiv 技术报告。
- **Raindrop 决策模型对比**：博客《A practical guide to choosing decision models》加 GitHub 仓库 raindrop-ai/choosing-decision-models（1,005 个决策 × 11 个决策模型 + 2 个 LLM 基线），非论文，不收录。
- **Colgate 合成消费者研究**：Colgate-Palmolive 与 PyMC Labs 的 LLM 角色扮演购物者研究（Semantic Similarity Rating），不涉及类型化决策模型，超出范围，不处置。
- **既有观察线索**：Sarvam Prism（博客 + 开放权重，71.8 @ 44 ms 为厂商口径）、书生·明决 / Intern-Decision、Gemini Decisions、Microsoft-Decision-1.1 均无变化；本轮收录的论文中，Microsoft Decision 1、Liquid D1-Ultra、Mercury Decide、PPLX Decider 以被评测的商用决策模型身份出现，但均未见自家 arXiv 报告。
