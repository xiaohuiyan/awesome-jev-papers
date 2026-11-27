# 社媒与聚合器检索（2026-11-27，第 23 轮）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [同日 arXiv 检索](ARXIV_SEARCH_2026-11-27.md) · [数据](../data/social-search-2026-11-27.json)

与第 23 轮 arXiv 扫描同步执行的四平台社媒检索（微信公众号、知乎、新浪微博、X/Twitter）加 Jev Daily 聚合器与四个外部 awesome 清单对照；窗口 2026-11-21 至 11-27（含前两周遗留线索的解析）。**本轮社媒自有收录 0 条**——所有可解析线索均落在已编目论文上（唯一例外 DecisionReplay 已被同日 API 扫描独立捕获）；本轮 2 条新增全部来自 API 扫描。

## 各平台结果

- **微信公众号**（`Jev 决策模型 论文 微信公众号 2026年11月` 等）：无 mp.weixin.qq.com 十一月结果；返回项均为 9–10 月已知的发布解读（腾讯云开发者、36 氪、开源中国 RLCD 解读、博客园 iTech 逆向拆解、「深蓝AI」系专栏），无论文线索。
- **知乎**（`site:zhuanlan.zhihu.com Jev 论文 2026年11月`）：
  - 机器之心 11-06 专栏《3.7万 token/s 实现千万级家庭仿真……发布 YN 决策模型》解析为已编目的 [S²-MAS（2610.27746）](https://arxiv.org/abs/2610.27746)（YN-mini 在其表中胜 Jev 1.13 九个点、吞吐 22.72× Jev API）；
  - 《【11-17】agentic 方式合成/清洗训练数据》速读中唯一 Jev 相关条目《Actor, Judge, or Teacher?》即已编目的 [2611.17167](https://arxiv.org/abs/2611.17167)（JEV 经 API 作冻结 GRPO 过程监督教师）；
  - SO-Arena 专栏（11-15）与《GPT 到 Jev 架构演进》（11-03）为第 21/22 轮已知项；其余为旧科普专栏。
- **新浪微博**（`微博 Jev 决策模型 开源 论文 site:weibo.com 2026年11月`）：无 weibo.com 十一月结果，仅九月旧文；无论文线索。
- **X / Twitter**（多组查询，含 48 小时定向窗与 watch-lead 探针）：
  - 论文线索全部在库：LEVER（[2611.27016](https://arxiv.org/abs/2611.27016)）、Replacing LLMs（[2609.22753](https://arxiv.org/abs/2609.22753)）、GDM（[2610.03935](https://arxiv.org/abs/2610.03935)）、LLM-as-Jev（[2610.02076](https://arxiv.org/abs/2610.02076)）；
  - Microsoft-Decision-1.1 的 Foundry GA 报道引出 [DecisionReplay（2611.34627）](https://arxiv.org/abs/2611.34627)——同日 API 扫描已独立捕获并收录，社媒轮确认不占主；
  - @typesafeai「~600 倍更低成本轨迹判分」帖与 Mario Martone 器具铭牌文章均为博客/演示，非论文；
  - Sarvam Prism 公告帖所引 arXiv 2607.23808 经 id_list 解析为 **Indic DiarBench**（七月 ASR 基准，与 Prism 无关）——又一例「聚合器引用的 ID 需逐个解析」，Prism 仍无 arXiv 报告。
- **Jev Daily**：issues/2026-11-26 已发布，生态-only（Harrison Chase 用 Jev 对存储的智能体轨迹做判分；Hamel Husain 称决策指数基准普遍过拟合——均无论文 ID）；**11-27 期至检索时（~03:00 UTC）未发布（404）**，发布时点晚于检索属正常时序。
- **外部清单对照**（四清单 raw README diff）：**连续第四轮干净**——awesome-jev 3 个窗口外背景 ID；awesome-system-one 7 个窗口外背景 ID + 两个已知字符串（2609.14973 = PhysBrain 误引、4157.1124 = Science DOI 片段）；awesome-decision-models 与 awesome-jev-security 干净。**无窗口内新线索。**

## 线索处置

论文线索（paper_leads）与非论文线索（non_paper_leads）的逐条处置见 [数据文件](../data/social-search-2026-11-27.json)；watch leads 无变化（Sarvam Prism、书生·明决/Intern-Decision、Gemini Decisions/Gemini Decision 1、Microsoft-Decision-1.1、HeyGen Decision 1、autotrust JEV-27B-VL 均仍无 arXiv 报告）。新记生态项：Paper Radar（Eliot5566/JEV-Paper-Radar，基于 Jev/Claude/Gemini Decision 1 的每日 arXiv 分诊开源工具，无自有论文）。
