# arXiv 第 14 轮检索（2026-11-13）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-13.md)

周五上午执行（01:43 UTC 起）：探针显示新窗口（11-11 至 11-13）**尚无任何公告记录**——与昨日第 13 轮同一时刻已见 11-10 批次不同，11-11 投稿批次今日迟到（01:50、02:04、02:12 UTC 三次复查探针均为 0）。按协议照常双窗口执行：新窗口四条常设查询加五个变体全部 0 命中；**常设查询与变体全窗口重扫**（2026-09-15 起，Jev/decision model 单数各取最新 200 条）得 382 条去重记录，**0 条台账外记录：0 新候选、0 收录、0 排除**。目录维持 **356 篇**不变；另经第三方清单交叉核对补录 1 条排除（见下），台账 520 → **521 条**（356 收录、163 排除、2 待核实）。

**盲区补查（本轮新增动作）**：鉴于第 12/13 轮的 EarthJev 教训（未加连字符复合名不按 `all:"Jev"` 分词、摘要亦无常设词元，API 查询完全不可见），本轮对 arXiv `/recent` 列表页做标题级 grep（`jev` 子串、`System One`、`System 1`、`decision model`）。先扫 15 个主力分类，再扩展到目录 356 篇出现过的全部 36 个分类（38 分类查询去重后；`skip`/`show=100` 分页至分类尽头）：共 **4,793 条**列表记录——`/recent` 实际回溯多个公告日，覆盖面广于 11-11 周三公告批次（首发至 11-10）。命中 34 条 = **26 条已收录** + **8 条误报**（2611.05557 SVM/KL、2611.05643 推荐系统 scaling law、2611.06762 美国州级 K-12 AI 政策、2611.11274 媒体日记零替换、2611.11918 气象资料同化、2611.12544 非精确交替极小化、2611.13337 几何机器学习 VC 维、2611.13448 Fermat ProbCover 主动学习——经 `id_list` 摘要核验均无相关词元，为列表页作者名/评论所致的块级误匹配）。**已公告批次确认无复合名或其他盲区遗漏。**

## 新增与阅读优先级

无——本轮无新增。上一批新论文见[第 13 轮报告](ARXIV_SEARCH_2026-11-12.md)。

## 排除与去重

| 候选 | 处理理由 |
| --- | --- |
| [iLLaDA](https://arxiv.org/abs/2606.25331v1) | 掩码扩散语言模型架构论文（8B、双向注意力、12T token）；「基于置信度的多项选择打分」仅为评测协议，无托管 Jev 使用、无类型化决策接口贡献。由社区 [awesome-jev](https://github.com/Promethe-us/awesome-jev) 清单交叉核对带出（该清单自己也注明无 Jev 血统证据）；同清单的 RLCD（2307.12950）、LLaDA（2502.09992）、SalesRLAgent（2503.23303）均为窗口前背景，不入台账。 |

8 条列表页误报经摘要核验后不进入台账（词元级核验未命中常设/变体查询定义的主题，属块级误匹配而非「检索命中后排除」，与既有的排除记录性质不同）。

## 检索覆盖与可复核性

1. Atom API 正常；探针 `all:"language model"` 限定新窗口（11-11..11-13）返回 0 条，published 日期集为空——**11-11 起投稿尚未公告**；01:50、02:04、02:12 UTC 复查探针仍为 0，另以每 5 分钟一次的监视探针延续观察。**下一轮必须从 11-11 重扫。**
2. 四条常设查询（`Jev`/`System One`/`typed decision`/`decision model`）扫新窗口并全窗重扫（Jev 与 decision model 单数各取最新 200 条）；五个变体（MedJev/System-One/System 1/decision models/JevBench）同样双窗口。全部 19 条查询与命中数记录在 [search-log.json](../data/search-log.json)（全窗命中：Jev 229、System One 98、typed decision 76、decision model 223、MedJev 1、System-One 98、System 1 54、decision models 224、JevBench 7；新窗口全部 0）。
3. 盲区补查：38 分类 `/recent` 列表页（`skip`/`show=100` 分页至各分类尽头，共 4,793 条、34 命中）逐条对照目录与台账；8 条误报另以 `id_list` 拉取摘要做词元级复核。查询与结果记录在 [search-log.json](../data/search-log.json)。
4. 社媒渠道（微信/知乎/微博/X）同日先行检索，0 新记录；新非论文线索见[同日社媒检索](SOCIAL_SEARCH_2026-11-13.md)。

## English summary

Friday sweep (01:43 UTC) with the four standing queries plus five token variants over both windows: the fresh window (11-11..11-13) returned zero entries — the 11-11 announcement batch had not reached the API index at run time (unlike yesterday's round, which saw the 11-10 batch at the same hour; three re-probes through 02:12 UTC stayed empty) — and the whole-window re-runs since 09-15 pooled 382 unique records with **zero records outside the 520-entry screening ledger: 0 fresh candidates, 0 additions**. New this round, a fused-name blind-spot check modeled on the EarthJev lesson: the arXiv /recent listings for all 38 categories carrying catalogue papers (4,793 entries, paged to each category's end and spanning several announcement days back through first submissions of 11-10) grepped at title level for jev-compounds and standing tokens — 34 hits = 26 catalogued plus 8 false positives verified token-free at abstract level, so no blind-spot omissions in the announced batch. A third-party cross-check of the community awesome-jev list added one exclusion (iLLaDA 2606.25331: diffusion-LM architecture, multiple-choice scoring only as evaluation), taking the ledger to 521 (356 included / 163 excluded / 2 pending); the catalogue is unchanged at 356. Submissions from 11-11 onward were not yet announced at run time and must be re-covered next round.
