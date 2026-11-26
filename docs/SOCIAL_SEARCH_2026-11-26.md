# 社媒与聚合器检索（2026-11-26，第 22 轮）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [同日 arXiv 检索](ARXIV_SEARCH_2026-11-26.md) · [数据](../data/social-search-2026-11-26.json)

与第 22 轮 arXiv 扫描同步执行的四平台社媒检索（微信公众号、知乎、新浪微博、X/Twitter）加 Jev Daily 聚合器与四个外部 awesome 清单对照；窗口 2026-11-21 至 11-26（含前一周遗留线索的解析）。**本轮社媒自有收录 0 条**——所有可解析线索均落在已编目论文上；本轮 31 条新增全部来自 API 扫描与列举网。

## 各平台结果

- **微信公众号**（`Jev 决策模型 论文 微信公众号 2026年11月` 等）：无 mp.weixin.qq.com 新结果；返回项均为 9–10 月已知的发布解读（腾讯云开发者、36 氪、开源中国 RLCD 解读、博客园 iTech 逆向拆解、「深蓝AI」系专栏），无论文线索。
- **知乎**（`site:zhuanlan.zhihu.com Jev 论文 2026年11月`）：两个 11 月专栏——《SO-Arena 用2919道题体检 System One 模型》（11-15，综述 11-13 Hugging Face Daily Papers 当日热文）解析为已编目的 [SO-Arena（2611.15777）](https://arxiv.org/abs/2611.15777)；《GPT 到 Jev：架构演进与训练部署》（11-03）为科普向，无论文线索；其余为已知旧专栏。
- **新浪微博**（`微博 Jev 决策模型 开源 论文 site:weibo.com`）：无 weibo.com 直达结果，热搜聚合页亦无 Jev 相关词条；生态梳理均为已知旧闻。
- **X / Twitter**（多组查询，含 `Jev decision model paper November 2026 arxiv new`、48 小时定向窗与 2611.28xxx/29xxx/30xxx ID 形态探针）：
  - @dair_ai 的「从 Jev 答案蒸馏开放 4B 决策模型」帖解析为已编目的蒸馏线论文（[Predicting What Answer Engines Cite（2610.38090）](https://arxiv.org/abs/2610.38090)、[From Probabilities to Decisions（2610.09188）](https://arxiv.org/abs/2610.09188)、[GLiDE（2611.26509）](https://arxiv.org/abs/2611.26509)）；
  - @barrowjoseph 的决策模型深潜长文与各 2611.x 周报帖（2611.25363、2611.22432、2611.27679、2611.28535、2611.26557、2611.28331）经逐条 id_list 核对全部在库；
  - Intern-Decision/书生·明决 的报道（ET CIO、Sarvam 博客等）解析为已编目的 [2610.22131](https://arxiv.org/abs/2610.22131) 与 [2611.16321](https://arxiv.org/abs/2611.16321)；
  - Paper Digest 列出的多语言情绪分类决策模型即已编目的 [2611.27721](https://arxiv.org/abs/2611.27721)。
- **Jev Daily**：issues/2026-11-24 已发布，生态-only（Hex 1.0.4 键盘端 Parakeet 转写、Matt Van Horn 的 PR 合并概率分类器、Guillermo Rauch 的个人评测——均无论文 ID）；**11-25 期至检索时未发布（404）**，与 11-16、11-23/11-24 的断更先例同型。
- **外部清单对照**（四清单 raw README diff）：**连续第三轮干净**——awesome-jev 3 个窗口外背景 ID（RLCD 2023、LLaDA 2025、SalesRLAgent 2025）；awesome-system-one 7 个窗口外背景 ID + 两个已知字符串（2609.14973 = PhysBrain 误引、4157.1124 = Science DOI 片段）；awesome-decision-models 与 awesome-jev-security 干净。**无窗口内新线索。**

## 线索处置

论文线索（paper_leads）与非论文线索（non_paper_leads）的逐条处置见 [数据文件](../data/social-search-2026-11-26.json)；watch leads 无变化（Sarvam Prism、书生·明决/Intern-Decision、Gemini Decisions/Gemini Decision 1、Microsoft-Decision-1.1、HeyGen Decision 1、autotrust JEV-27B-VL 均仍无 arXiv 报告）。
