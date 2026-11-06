# Weekly arXiv gap search / 近一周 arXiv 补漏（2026-11-06）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json)

目标窗口：**2026-10-31 至 2026-11-06**，按论文首次提交日期筛选，截至本次执行时。检索日期使用 Asia/Shanghai；论文提交时间保留 arXiv 原始记录。新增 **2 篇直接相关论文**，排除 2 篇范围不符候选。目录由 316 增至 **318 篇：206 direct、108 related、4 foundations，115 篇有已核实代码**。累计筛选台账为 473 条：318 收录、153 排除、2 待核实。

> **后续更新（同日第二轮，API 恢复）：** Atom API 恢复后执行的[第二轮扫描](#round11)新增 **7 篇**（4 direct、3 related，0 排除），目录增至 **325 篇（210 direct、111 related、4 foundations，119 篇有已核实代码）**，台账 480 条。上文 318 篇为第一轮结束时的历史快照。

## 新增与阅读优先级

| 论文 | 首次提交 / 版本 | 分类与推荐理由 | 证据边界 |
| --- | --- | --- | --- |
| [Presentation Sensitivity in Typed Decision Models for Subjective Text Evaluation](https://arxiv.org/abs/2611.06384v1) | 2026-11-04 / v1 | **优先阅读；security / direct**。受控呈现干预结合重复调用和多重比较校正，直接审计 Jev、Clef Flash、Perplexity Decider，有助于区分输出稳定与评测有效性。 | 仅三类英文主观任务；人类参考群体、措辞和评分量表影响结论。未独立复现实验。 |
| [Zuse: A Decision Model for European Languages](https://arxiv.org/abs/2611.06238v1) | 2026-11-04 / v1 | **有条件推荐；architecture / direct**。多语言指针头决策模型及任务间校准分析，适合作为训练设计案例；论文表 3 实质比较既有 Jev 结果。 | Jev 结果引自 Kev 项目，版本未知；没有欧洲任务上的 Jev 对照。选模与评测不独立，多数仅单种子，完整训练配方和数据不公开，不能据此认定性能领先或训练可复现。 |

质量判断与相关性分数分开：两篇均满足明确模型关系与实质贡献的收录门槛；相关性 1.0 不代表质量满分。没有将 Zuse 关于多语言评测“首次”的宣称写入目录结论。

针对性正文检查：[呈现敏感性全文](https://arxiv.org/html/2611.06384v1)的研究设计、结果、限制及附录 D；[Zuse 全文](https://arxiv.org/html/2611.06238v1)的架构、5.3 节选模、6.1 节与表 3、8 节限制。作者与单位来自摘要页及正文作者栏。没有核实到可加入目录的作者公开 GitHub 代码，故代码数量不变；这不等于断言不存在代码。

## 排除与去重

| 候选 | 处理理由 |
| --- | --- |
| [Permanent and Transient Representations for Continual Reinforcement Learning](https://arxiv.org/abs/2611.07327v1) | 持续强化学习中的互补表征；“systems: one”关键词命中不等于 System 1 类型化概率决策模型。摘要未建立托管 Jev 或所需接口关系。 |
| [Can Astra Solve RoboMME without Breaking the Bank?](https://arxiv.org/abs/2611.06184v1) | System 1 指低层视觉语言动作策略；摘要未建立 Jev 式概率选项接口或托管 Jev 评测关系。 |

TandemBench、Jev-AD、TACT、经济代理决策模型、Honest Small Decision Models、JevBreak、EO-Jev、VerdictAD、XDecideBench 等结果已收录，未重复添加。搜索摘要日期与版本页有时不一致，新增条目以版本页提交历史为准；没有批量改写既有日期。

## 检索覆盖与可复核性

1. 直接访问 arXiv 站内搜索，按最新公告排序，检索 `Jev`、`System One`、`System 1`、`typed decision`、`decision models`、`decision model`、`System-One`、`JevBench`、`MedJev`；查询 URL 写入 JSON 日志。检查关键词结果及候选原文，部分查询延伸到窗口前用于确认边界。
2. arXiv `/list/cs.AI/new` 当次返回的页面仍标注 11-05，不能用它断言 11-06 所有新稿均已覆盖。站内搜索的日期显示与单篇摘要页也有差异。
3. Atom API 与本地直接抓取超时或不可访问。本轮使用官方版本化摘要页、提交历史及 HTML 正文核实，**不是完成的 API 全量扫描**。站内结果截取、索引延迟、仅正文提及 Jev 及非标准命名都可能造成遗漏。
4. 两篇 `metadata_source` 指向实际读到的官方摘要页；记录 API 待交叉核验状态。摘要指纹来自该页空白归一化文本，恢复网页链接目标；不宣称已与 Atom 表示比对。既有条目的核实日期保留。
5. 本轮独立于同日 [X 检索](SOCIAL_SEARCH_2026-11-06.md)：社媒轮新增 0 篇，随后直接 arXiv 检索新增 2 篇。保留前一轮历史快照，避免混淆发现来源。

## English summary

A direct arXiv web follow-up added two papers missed by the preceding social search: a presentation-sensitivity audit and Zuse. Both first-submission dates are verified as November 4, 2026, with v1 reviewed. Zuse compares previously reported Jev results; its methodological and reproducibility limitations are explicit. Two neighboring papers were excluded for scope, not judged low quality. The catalogue contains 318 papers. API access failed, so provenance points to the official versioned web records and the Atom cross-check remains pending. This is a targeted gap search, not proof of exhaustive weekly coverage.

<a id="round11"></a>
## 同日第二轮：API 恢复后的全窗重扫

Atom API 恢复后（周五 02:50 UTC 起执行），先按常设四查询扫新窗口（首次提交 2026-11-05 至 11-06；探针显示索引最高到 11-05，11-06 投稿尚未入库），并把五个 token 变体再次全窗重扫（2026-09-15 起）。新窗口与变体重扫**均无新增**。随后把**常设四查询本身也全窗重扫**（此前只有变体做过全窗重扫），捞出 6 条迟索引漏网（首次提交 10-14 至 10-28）；另由微博/知乎线索与 X 交叉检索发现 [EarthJev](https://arxiv.org/abs/2611.02096v1)——其 "Jev" 仅以 "EarthJev"/"OneJev" 融合形式出现，任何查询都从未命中。**7 条候选全部收录（4 direct、3 related），0 排除**。四个 GitHub 仓库经 API 核实公开，代码数 115 → **119**。台账 473 → **480 条：325 收录、153 排除、2 待核实**。

| 论文 | 首次提交 / 版本 | 关系 / 分类 | 核实要点 |
| --- | --- | --- | --- |
| [CausalGrade](https://arxiv.org/abs/2610.40692v1) | 2026-10-28 / v1 | direct / applications | 正文固定 Jev version 1.13.0；500 个图选择任务最佳候选命中 54.4% 对自兼容 48.4%。候选图来自同一 CDFM 输出，稀疏化混淆部分增益；未见作者代码。 |
| [SAG2](https://arxiv.org/abs/2610.22588v1) | 2026-10-15 / v1 | direct / applications | 托管 typesafe/jev-1.13-20260917 经 OpenRouter Noul 接口；三基准最高 R@5/10。四跳完全证据覆盖仅 28.31%；基准代码仓库已核实。 |
| [城市出行生成式 agent](https://arxiv.org/abs/2610.22407v1) | 2026-10-14 / v1 | direct / applications | Jev-1.13（jev-1.13.0）为 15 个决策器之一，综合 3.65 落在拟合模型区间；逐次出行真实感全部未达标，事件检验仅单个 agent/单个事件；代码仓库已核实。 |
| [OneCodeReviewBench](https://arxiv.org/abs/2610.33389v1) | 2026-10-24 / v1 | direct / evaluation | 十套系统中 Jev 使用 jev-1.13.0；排名随答案类型改变。用例全为合成小场景；工件在 Zenodo（DOI 10.5281/zenodo.23604731）而非 GitHub，代码计数不变。 |
| [NIOCIS](https://arxiv.org/abs/2610.25985v1) | 2026-10-19 / v1 | related / agents | 本地 Laya 0.3.21 单次前向 10-19.5 ms 读出校准分布；未用托管 Jev。标签为约定推导弱标签，7.9% 目标在声明选项空间外；代码与语料仓库已核实。 |
| [One Confidence Threshold, Unequal Coverage](https://arxiv.org/abs/2610.37688v1) | 2026-10-17 / v1 | related / calibration | OpenAI/Microsoft/Perplexity 接口 51 语言对比，英文过阈值高 8.6-11.7 点；**未测试托管 Jev**，主证据限于 MASSIVE。无代码。 |
| [EarthJev](https://arxiv.org/abs/2611.02096v1) | 2026-11-01 / v1 | related / applications | 0.8B、开放 OneJev 配方、ECE 0.006、19.9 ms；**未使用或评测托管 Jev**。多模态基线仅见 RGB，数据限十个欧洲国家；代码与模型仓库已核实。 |

第二轮覆盖说明：两个宽查询（`all:"Jev"` 209 条、`all:"decision model"` 206 条）按提交日期降序各读最新 200 条，未读尾部为 10 月以前的记录，此前各轮已覆盖；站内搜索索引延迟、仅正文提及 Jev、融合命名（如 EarthJev）仍可能造成遗漏——本轮 EarthJev 即为融合命名的实例，靠社媒交叉链发现后以 `id_list` 补拉元数据。两个待核实条目（PENDING 台账）未变。

## English summary (round 11)

The recovered Atom API re-swept the fresh window (nothing new; index reached 11-05) and then, for the first time since round 8, re-ran the four standing queries over the whole window since 2026-09-15, surfacing six late-indexed submissions; a social/web cross-check added EarthJev, whose Jev token only appears fused inside "EarthJev"/"OneJev" so no query had matched it. All seven candidates were included (four direct papers pinning jev-1.13.0 or jev-1.13-20260917; three related: a Laya-based routing layer, a cross-language threshold-coverage study that does not test Jev, and EarthJev, which does not use hosted Jev). Four GitHub repositories were verified public; two related papers test no hosted Jev and are labelled accordingly. The two broad standing queries fetched their newest 200 of 206/209 records; the unread tails predate October and were covered by earlier rounds.
