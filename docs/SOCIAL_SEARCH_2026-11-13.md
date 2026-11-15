# X / 中文平台检索（2026-11-13）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询与线索台账](../data/social-search-2026-11-13.json) · [同日 arXiv 第 14 轮](ARXIV_SEARCH_2026-11-13.md)

检索窗口：**2026-11-11 至 2026-11-13**（自 11-12 第 13 轮以来的空档日），另加无日期补充查询与 [Jev Daily](https://jevdaily.com) 逐期直达。论文首次提交日期以 arXiv 记录为准，与帖子/文章日期分开处理。

**本轮社媒线索独立新增 0 篇。** 四平台全部论文形线索均解析到已收录记录：知乎宽查询提及的 REFLEX（2609.26532）与 StartLux（2610.17309，见 36氪报道）均在目录；X 交叉检索surfaced 的 2610.32955（Measure Before You Train，报告 v2.1）目录按方法学钉定已核版本 v1（updated 2026-11-06）；OpenReview 上流传的《Can Jev Be Your Q or Policy in Reinforcement Learning?》解析为 arXiv 2610.11692（首发 10-08），已收录；JEV-27B-VL 线索顺带复查的 DecisionRobust（2610.19118）也已收录。

## 本轮社媒新增

无。检索与结果全部记录在 [JSON 台账](../data/social-search-2026-11-13.json)。

| 平台 | 检索与读取 | 结果与限制 |
| --- | --- | --- |
| 微信公众号 | `site:mp.weixin.qq.com` 带日期查询与更宽的「微信公众号 Jev 决策模型 论文 11月」。 | 带日期查询 0 命中（微信文章索引不全，不能据此断言无新内容）。宽查询命中的是知乎/腾讯云/开源中国/博客园的科普与转载（RLCD 解读、API 逆推拆解等）；论文形线索（REFLEX、StartLux）均已收录。新非论文线索：StartLux v1.1 发布报道（见下）。 |
| 知乎 | `site:zhihu.com Jev 决策模型 System One`（带 11 月日期）与「知乎专栏 … 新论文」复查。 | 专栏仍集中于 2026 年 9-10 月；11 月日期查询与「新论文」查询均无命中；引用论文均已收录。 |
| 新浪微博 | `site:weibo.com Jev 决策模型 论文`。 | 科普长文与融资新闻（估值暴涨）无变化；无新论文线索。 |
| X / Twitter（交叉） | `Jev decision model arxiv new paper November 11 12 13 2026`、`twitter X Jev System One typed decision model paper arxiv 2611.10 OR 2611.11 OR 2611.12`。 | 无台账外记录；生态项（Cloudflare clef、Laya、社区 awesome-jev 仓库、Barrow/Pachaar/mvanhorn 帖）均为已知内容。X 原生搜索不可达，依赖网页索引，无命中不等于无讨论。 |
| Jev Daily（聚合站） | 直达 `issues/2026-11-12`（已发布）、`/2026-11-13`（404）。 | 11-12 期**无论文**：Google **Gemini Decisions API**（Gemini Decision 1，$0.10/百万输入 token、最多 1,000 道闭集问题，对比 Jev 1.14 的 $0.042 约 2.4 倍）、Mike Taylor 采用 Every「cut」剪辑软件（Jev 场景检测）、Theo 的 Gemini 延迟批评（~11 秒首响应，未公布测试脚手架）。11-13 期抓取时未发布。 |

## 新增非论文线索

| 线索 | 来源与时间 | 处理理由 |
| --- | --- | --- |
| **Google Gemini Decisions API / Gemini Decision 1** | Jev Daily 11-12 期 + aihubmix 对比（11-12） | 厂商产品发布，无技术报告；与 Prism、Vega、JEV-27B-VL 同列为观察线索，出现 arXiv 技术报告后再评估。 |
| **Jev 1.14 正式稳定版**（遗留线索收束） | docs.typesafe.ai 模型页、OpenRouter、shattered.io 报道 | `jev-latest` 已指向 `jev-1.14.0`、`jev-1.13.0` 随之弃用——第 9-13 轮「11 月中旬正式版」观察线索就此收束；仍无官方技术报告，属产品动态。 |
| **StartLux-Decision v1.1** | Pandaily（X）、decision.startlux.com | 自跑分 73.37（27B AutoThink，Decision Index 0.3.2）；论文 2610.17309 已按 v1 收录，v1.1 为模型/榜单动态。 |
| DoltHub: Working with Jev | dolthub.com 博客（11-12） | 工程实录（Jev 1.14.0 类型化回答 <200ms），非论文。 |

遗留观察线索（Sarvam Prism、Vega、JEV-27B-VL、Smaug-Audio-Decisions、alphaXiv 4B、ResearchGate Ahn 预印本、屠荒者微信文）本轮均未解析到新 arXiv 记录，继续保留。

## 覆盖与来源限制 / Coverage

- 三条中文平台与 X 均无法登录检索，使用网页搜索 `site:` 查询与聚合站直达；查询与结果全部记录在 [JSON 台账](../data/social-search-2026-11-13.json)。
- X 帖提及的社区 [awesome-jev](https://github.com/Promethe-us/awesome-jev) 清单做了直接抓取比对：29 条 arXiv 引用中 25 条已收录，3 条窗口前背景（RLCD/LLaDA/SalesRLAgent）不入台账，1 条窗口内 iLLaDA（2606.25331）经摘要核验按方法学排除——详见[同日 arXiv 第 14 轮](ARXIV_SEARCH_2026-11-13.md)的排除表。
- Jev Daily 11-12 期为人工读取，11-13 期未发布；聚合站缺论不等于当日无论文——当日新论文以 [arXiv 第 14 轮](ARXIV_SEARCH_2026-11-13.md)的 API 扫描为准。
- 本轮没有建立任何论文的社媒原帖证据链；0 独立新增指社媒渠道的收录归功，不代表当日没有新论文。
