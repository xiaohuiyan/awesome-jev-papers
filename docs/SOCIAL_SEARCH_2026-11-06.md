# Weekly X/Twitter discovery / 本周 X 论文检索（2026-11-06）

检索窗口：**2026-10-31 至 2026-11-06**，Asia/Shanghai，截至执行时。最初的日期查询额外覆盖 10-30，作为边界缓冲；无日期查询用于补充发现。论文首次提交日期、聚合站发布日期和原帖日期分别处理。[查询与线索台账](../data/social-search-2026-11-06.json) · [中文目录](../README.zh-CN.md) · [English catalogue](../README.md)

**本轮新增正式论文 0 篇；目录仍为 316 篇（直接相关 204、同类方法 108、基础背景 4，115 篇有已核实代码）。** 找到的相关论文线索已在目录。以下补充本周阅读精选与未收录线索，不重复创建条目。没有核实到新论文，不等于 X 上没有新论文。

后续更新：同日的独立 [arXiv 站内补漏](ARXIV_SEARCH_2026-11-06.md)新增 2 篇，目录增至 318 篇；再后的[同日中文平台补充轮](#cn-platforms)与 [arXiv 第二轮](ARXIV_SEARCH_2026-11-06.md#round11)合计使目录增至 **325 篇**。上面的 316 篇是 X 轮结束时的历史快照。

<a id="cn-platforms"></a>
## 同日补充：微信公众号、知乎、微博

在上午 X 轮之后执行，检索窗口同为 10-31 至 11-06，另加无日期查询。三条平台的公开索引均无法直接登录检索，使用网页搜索的 `site:` 查询与关键词组合；查询与结果已并入 [JSON 台账](../data/social-search-2026-11-06.json)。

| 平台 | 检索与读取 | 结果与限制 |
| --- | --- | --- |
| 微信公众号 | `site:mp.weixin.qq.com` 的 Jev/决策模型查询（带与不带 11 月日期）。 | 带日期查询 0 命中；无日期查询返回 Datawhale jev-cookbook 存档、智源社区/掘金/puppyone 科普文，引用论文均在目录。微信文章不被搜索引擎完整收录，不能据此断言公众号无新内容。 |
| 知乎 | `site:zhihu.com Jev 决策模型 System One` 等 2 组查询，读约 10 篇专栏。 | 「一周 13 篇论文」「10-23 cs.AI 汇总」等摘要文引用的 Jev-DLC（2610.31521）、RetiJev、LLM-as-Jev（2610.02076，v1 名 LLM2Jev）、General Decision Models（2610.03935）均已在目录；无新记录。 |
| 新浪微博 | `site:weibo.com Jev 决策模型`。 | ttarticle 科普与产品稿：蚂蚁 27B 解析为 SII-Decision-27B（2610.03935，已收录）；「0.6B 开源多模态」解析为 StartLux（2610.17309，已收录）或社区工具；「Jev 上新会看图」为厂商产品动态，无论文。 |
| X / Twitter（交叉） | 上午 X 轮之后的数小时增量网页查询。 | 汇总页列出的 2611 系列论文中 6/7 已在目录，唯 [EarthJev](https://arxiv.org/abs/2611.02096v1)（首发 11-01）不在——其 Jev token 仅以融合形式出现，从未被 API 查询命中。该发现链移交同日 arXiv 第二轮，经摘要页与正文核实后收录。 |

**本轮平台线索 0 篇独立新增；但 EarthJev 的发现链源自本轮社媒交叉检索**，正式收录证据来自 arXiv 摘要页、提交历史与 PDF 正文（见 [arXiv 第二轮记录](ARXIV_SEARCH_2026-11-06.md#round11)）。

| 新增非论文线索 | 来源与时间 | 处理理由 |
| --- | --- | --- |
| Vega（800M，Laya 作者） | [HF 模型卡](https://huggingface.co/nandakishorm/vega-08b-public-intents)、LinkedIn/Reddit 公告 | 物理类 typed decision model，仅模型卡无 arXiv 记录；与 Smaug-Audio-Decisions 同样列为观察线索，出现技术报告后再评估。 |
| Decision 3.0 / d3-ultra、Jev 多模态上新 | 产品新闻 | 无论文；延续既有观察线索。 |

遗留线索（ResearchGate Ahn 预印本、屠荒者微信文、alphaXiv 4B、Smaug-Audio-Decisions）本轮均未解析到 arXiv 记录，继续保留。

## 覆盖与来源限制 / Coverage

- 连接器搜索发生传输错误，改用网页搜索。使用 X/Twitter 域名、Jev、System One / System 1、typed decision、decision model(s)、arXiv 与日期变体。
- X 原生搜索及抽查的两条原帖返回 **403**，未读取登录后的时间线。Jev Daily 可访问，保留其原帖链接及二手来源身份；没有将聚合站的说法写成原帖独立核验结果。
- Jev-X 首次读取仅取得标注 11/06 UTC 的页面头部，后续请求超时，未完成其信息流审阅。arXiv API 请求也失败，本轮**不是一次完成的 API 全量扫描**。
- arXiv 摘要和部分 HTML 正文可读，用于筛选下面的论文。它们的近期首发日期可核实，但**尚未建立每篇论文在本周被 X 分享的原帖证据链**。

This was a coverage-limited discovery attempt, not an exhaustive X collection. Primary paper pages support the reading selections below; a weekly X post has not been verified for them. Existing metadata verification dates are preserved.

## 本周优先阅读 / Reading shortlist

选择理由是与概率决策接口的关系、对照与评测设计、限制说明。它们是编辑性阅读推荐，不是引用量排名，也不是独立复现后的质量认证；仓库 relevance 分数仅表示相关性。

| 论文 / Paper | 首次提交 | 推荐理由 | 阅读时应关注的限制 | 本轮处理 |
| --- | --- | --- | --- | --- |
| [TandemBench](https://arxiv.org/html/2611.05827v1) | 11-04 | 1,200 道协作决策题，以执行与精确搜索建立答案；比较 40 个原生决策模型和 10 个 LLM，配对移除最优选项，区分“选得对”和“知道候选不完整”。适合评估 System 1 在 agent 中的能力边界。 | 完全可见状态的做饭场景，不能直接代表开放环境；最优性验证接近随机。分类沿用 related，不据此认定评测了托管 Jev。 | 已收录；优先阅读 |
| [Honest Small Decision Models for Finance](https://arxiv.org/html/2611.03755v1) | 11-02 | 同一 LoRA 配方覆盖两个模型家族与九档规模，研究领域微调损伤、混合语料修复、概率校准；区分规则标签与现实结果标签，报告无可检测预测优势的负结果。适合研究小型决策模型训练。 | 材料需向作者索取，封存的 2026 测试集尚未评测；结论限定于所用特征与协议，不代表获得交易优势。 | 已收录；优先阅读 |
| [Decision Models as Scalable Economic Surrogates](https://arxiv.org/abs/2611.05553v1) | 11-03 | 10 个决策模型与 8 个 LLM 在三个经济情境比较，将人类回答分布的差异纳入评估，适合理解概率输出的用途。 | 分布相似不等于逐人预测正确；经济博弈中众数回答拟合不如 LLM，速度及成本结论取决于所测配置。本轮核查摘要，未完成实验复现。 | 已收录；优先阅读 |

Read TandemBench for candidate-set coverage, the finance study for specialization and calibration, and economic surrogates for distribution-valued decisions. The selection favors informative evaluation designs and explicit limitations rather than uniformly positive results.

## 其他论文线索 / Other paper leads

- [Structured Clinical Memory](https://arxiv.org/abs/2611.04101)：已收录。仅 30 个合成病例、120 个问题；配对准确率差异未达显著（p=0.219），且记忆是理想化上界。保留为探索性试验，未列入本轮优先阅读。网页搜索的发现链来自 Bluesky 聚合内容，不能标作 X 发现。
- [VerdictAD](https://arxiv.org/abs/2611.02654)：已收录。通过作者提交的 [JevList 项目说明](https://jevlist.ai/projects/verdictad) 再次发现；其明确说明使用开放 Clef-Flash，而非托管 Jev。该说明的审阅日期不是论文首发或 X 原帖日期。

## 未作为论文收录 / Non-paper leads

| 线索 | 来源与时间 | 处理理由 |
| --- | --- | --- |
| Decision models against small LLMs | [作者博客](https://pournasserian.com/writing/decision-models-vs-small-llms-2026)，11-05 | 对 6,662 次决策的对照评测，值得后续关注；目前核实为博客，未找到对应 arXiv 论文，X 来源未核实。保留待跟进，不计入正式论文或 arXiv pending 数。不同模型任务覆盖与并发配置不完全一致，不能直接套用总体排名。 |
| 模拟购物者与广告选择 | [X 原帖](https://x.com/TheMattBerman/status/2116574903713358097)；[二手摘要](https://jevdaily.com/issues/2026-11-01)标注原帖 10-31 | 原帖 403；二手描述是个人演示，未定位论文，不作为研究结论收录。 |
| Jev-as-a-judge 位置偏差警告 | [X 原帖](https://x.com/hammer_mt/status/2116234738990223645)；[二手摘要](https://jevdaily.com/issues/2026-10-31)标注原帖 10-30 | 聚合站在窗口内发文，但原帖在窗口外；原帖 403，未定位论文。 |
| Prism 邮件小样本比较、垃圾邮件排序部署 | [11-04 摘要](https://jevdaily.com/issues/2026-11-04)、[11-03 摘要](https://jevdaily.com/issues/2026-11-03) | 社区实验与产品集成线索，未定位论文；聚合日期不作为原帖日期。 |

上述非论文线索单独保存在本轮 JSON 台账；既有 arXiv 筛选台账没有新增 ID，计数保持一致。后续只有定位到正式研究文本、核实模型身份及方法证据后，才考虑转入论文目录。
