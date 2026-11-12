# X / 中文平台检索（2026-11-12）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询与线索台账](../data/social-search-2026-11-12.json) · [同日 arXiv 第 13 轮](ARXIV_SEARCH_2026-11-12.md)

检索窗口：**2026-11-07 至 2026-11-12**（自 11-09 第 12 轮以来的空档日），另加无日期补充查询与 [Jev Daily](https://jevdaily.com) 逐期直达。论文首次提交日期以 arXiv 记录为准，与帖子/文章日期分开处理。

**本轮社媒线索独立新增 1 篇（EarthJev），另先于 API 扫描发现 2 条新记录。** X/Twitter 交叉检索在 arXiv 扫描完成前 surfaced 三条台账外记录：[2611.11480](https://arxiv.org/abs/2611.11480)（Beyond Ranking）与 [2611.10802](https://arxiv.org/abs/2611.10802)（Evaluating Jev on Arabic），两篇随后也被第 13 轮 [arXiv API 扫描](ARXIV_SEARCH_2026-11-12.md)独立命中并按其流程收录；以及 [2611.10005](https://arxiv.org/abs/2611.10005)（**EarthJev**，UHR 遥感证据获取）——这篇**任何常设/变体 API 查询都无法命中**：未加连字符的复合名 "EarthJev" 不会按 `all:"Jev"` 分词，摘要中也没有其他常设词元。经 id_list 定向补录（首发 11-04，在窗口内）后作为本轮社媒渠道自己的贡献收录（related / applications）。微信、知乎、微博的全部论文线索均已在目录。

## 本轮社媒新增

| 论文 | 首次提交 / 版本 | 分类与理由 | 证据边界 |
| --- | --- | --- | --- |
| [EarthJev](https://arxiv.org/abs/2611.10005v1) | 2026-11-04 / v1 | applications / related。RIKEN AIP/武汉大学/东京大学。UHR 遥感 VQA 的证据获取去生成化：空间指针校验、轻量头批量为候选视图打分、格式特定置信校准；五个基准平均 53.06%（超 ZoomSearch 2.33-14.73pp），延迟 11.30→1.67 秒。 | 名称中的 Jev 为 Jev 式打分思想，托管 Jev 仅被引用（TypeSafe 博客）未调用；决策模块按回答模型逐一拟合。代码已核实（Da1daidaidai/EarthJev）。 |

**方法论备注**：未加连字符的「…Jev」复合名（EarthJev 这类）是 API 查询的盲区（MedJev/JevBench 已有专设变体，NuJEV/TrialJev 靠摘要中的独立 "Jev" 词元命中）。后续轮次除社媒交叉检索外，可考虑为新出现的复合名补设变体查询。

| 平台 | 检索与读取 | 结果与限制 |
| --- | --- | --- |
| 微信公众号 | `site:mp.weixin.qq.com` 带日期查询与更宽的「公众号 Jev 决策模型 论文 11月」。 | 带日期查询 0 命中（微信文章索引不全，不能据此断言无新内容）。更宽查询命中 datawhale jev-cookbook 与魔搭社区对 **JEV-27B-VL** 的转载（autotrust 开源 27B 多模态决策模型，Apache 2.0，VL-RewardBench 78.3%、Jev Decision Index 0.3 视觉榜第一）——**无专门 arXiv 记录**，列为观察线索；其余引用论文（2610.29052、2609.37647、2610.18610 等）均已收录。 |
| 知乎 | `site:zhihu.com Jev 决策模型 System One`（带与不带 11 月日期）。 | 专栏集中于 2026 年 9-10 月（「Jev 与 System One 原理边界」「引爆决策模型」「JEV 工程学」「385ms 接入实测」等），引用论文均已收录；未发现 11 月新专栏。 |
| 新浪微博 | `site:weibo.com Jev 决策模型 论文`。 | 科普长文、RLCD 训练解读与融资新闻（「不到 1 个月估值暴涨 100 亿美元」）；无新论文线索。 |
| X / Twitter（交叉） | `Jev decision model arxiv new paper November 10 11 12 2026`、`twitter X Jev System One typed decision model paper arxiv 2611.09 OR 2611.10 OR 2611.11`。 | 第一条先于扫描发现 2611.11480 与 2611.10802；第二条发现 2611.10005（EarthJev，用 Jev 式打分接口，另引 NanoJev）并确认 JevBreak/XDecideBench/Drex/Policy Gates/2611.00428/2609.28940 均已收录。X 原生搜索不可达，依赖网页索引，无命中不等于无讨论。 |
| Jev Daily（聚合站） | 直达 `issues/2026-11-09`（404）、`/2026-11-10`、`/2026-11-11`、`/2026-11-12`（404）。 | 11-10、11-11 两期**无论文**：Browser Use 1.0.0 发布、Jev 语音点单演示（每个词后约 200ms 渲染）、Sextant 关键词判定成本报告（2.01 亿 token 花 8.04 美元）等非论文线索；11-09 与 11-12 期抓取时未发布（404）。 |

## 新增非论文线索

| 线索 | 来源与时间 | 处理理由 |
| --- | --- | --- |
| **autotrust JEV-27B-VL**（Qwen3.8-27B 上 Apache 2.0 LoRA，27B 多模态决策模型，VL-RewardBench 78.3%） | [Hugging Face 模型卡](https://huggingface.co/autotrust/JEV-27B-VL) + 魔搭/微信转载 | 与 Prism、Vega 同等对待：权重 + 模型卡，无专门 arXiv 记录；列为观察线索，出现技术报告后再评估。 |
| Sarvam Prism（遗留） | 官方博客 + Unite.AI/ET CIO 报道（11-03） | 仍无 arXiv 记录；报道称内部测试对比 Jev 1.14 与 Microsoft-Decision-1；继续观察。 |
| TypeSafe Jev 1.14 正式版 | 11-09 轮遗留 | 据报道 11 月中旬发布；产品动态，发布后若出现官方技术报告再行收录。 |

遗留观察线索（Vega、Smaug-Audio-Decisions、alphaXiv 4B、ResearchGate Ahn 预印本、屠荒者微信文、Sarvam Prism）本轮均未解析到新 arXiv 记录，继续保留。

## 覆盖与来源限制 / Coverage

- 三条中文平台与 X 均无法登录检索，使用网页搜索 `site:` 查询与聚合站直达；查询与结果全部记录在 [JSON 台账](../data/social-search-2026-11-12.json)。
- Jev Daily 11-10/11-11 期为人工读取，11-09 与 11-12 期未发布；聚合站缺论不等于当日无论文——当日新论文以 [arXiv 第 13 轮](ARXIV_SEARCH_2026-11-12.md)的 API 扫描为准。
- 本轮没有建立任何论文的社媒原帖证据链；0 独立新增指社媒渠道的收录归功，不代表当日没有新论文。
