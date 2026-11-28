# 社媒与聚合器检索（2026-11-28，第 24 轮）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [同日 arXiv 检索](ARXIV_SEARCH_2026-11-28.md) · [数据](../data/social-search-2026-11-28.json)

与第 24 轮 arXiv 扫描同步执行的四平台社媒检索（微信公众号、知乎、新浪微博、X/Twitter）加 Jev Daily 聚合器与四个外部 awesome 清单对照；窗口 2026-11-22 至 11-28（含前两周遗留线索的解析）。**本轮社媒贡献了发现线索**：arxivdaily 交叉链接暴露的 [2611.16477](https://arxiv.org/abs/2611.16477v1) 揭示了一个系统性措辞缺口——Intel Laya 系列自称 "decision encoder"，任何常设查询与列举网 token 均未覆盖；据此新增常设变体 `all:"decision encoder"` 并全窗口不设上限运行，**5 条台账外记录全部收录（均相关）**。捕获动作本身由 API 侧变体执行，社媒轮占发现主。

## 各平台结果

- **微信公众号**（`Jev 决策模型 论文 微信公众号 2026年11月` 等）：无新的 mp.weixin.qq.com 十一月论文线索；返回项为 9–10 月已知发布解读、魔搭 ModelScope 的 JEV-27B-VL 帖（autotrust watch lead，已在跟踪）及其 datawhale jev-cookbook 镜像；arxivdaily 条目（Jev-LiteMAS [2610.21411](https://arxiv.org/abs/2610.21411)、Jev-DLC [2610.31521](https://arxiv.org/abs/2610.31521)）均已编目。
- **知乎**（`site:zhuanlan.zhihu.com Jev 论文 2026年11月`）：无十一月新专栏浮出；结果为 10 月已知解读（《一周13篇论文》《2170个项目生态分析》）、9 月发布解读及第 21–23 轮已知的十一月专栏；11-28 的《一个"不说话"的AI刷屏》为生态评论，无 arXiv ID。
- **新浪微博**（`微博 Jev 决策模型 开源 论文 site:weibo.com 2026年11月`）：无 weibo.com 十一月结果，仅九月旧文；无论文线索。
- **X / Twitter**（多组查询，含 48 小时定向窗与 watch-lead 探针）：
  - 论文线索全部在库：Jev for Scientific Decisions（[2609.24965](https://arxiv.org/abs/2609.24965)）、Replacing LLMs（[2609.22753](https://arxiv.org/abs/2609.22753)）、JevBreak（[2611.03759](https://arxiv.org/abs/2611.03759)）、LLM-as-Jev（[2610.02076](https://arxiv.org/abs/2610.02076)）、TypedBench（[2610.11392](https://arxiv.org/abs/2610.11392)）、MetaEncoder（[2610.11316](https://arxiv.org/abs/2610.11316)）、MM-SystemOneBias（[2611.26557](https://arxiv.org/abs/2611.26557)）、LoopRoute（[2611.25363](https://arxiv.org/abs/2611.25363)）、Thinking Fast, Trading Late（[2611.03985](https://arxiv.org/abs/2611.03985)）；
  - **arxivdaily 的 2611.16477 页面（交叉引用 MetaEncoder）是本轮关键线索**——该论文不在库亦不在台账，暴露 "decision encoder" 措辞缺口，经新增变体全窗口运行后与同系列另外四篇一并收录；
  - preprints.org 的《Jev-Like Models and Decision Systems: A Survey》（202611.2129）**不在 arXiv**，超出目录范围——记为 watch item，若日后落入窗口内成为候选。
- **Jev Daily**：issues/2026-11-27 自第 23 轮检查后已发布，生态-only——Simeon Griggs 的「Jev is not a decision model, you are」框架帖经 Diogo Almeida 放大（「逻辑应写在代码里而非提示词里」），无 arXiv ID、无准确率/延迟数字；**11-28 期至检索时（~02:30 UTC）未发布（404）**，发布时点晚于检索属正常时序。
- **外部清单对照**（四清单 raw README diff）：**连续第五轮干净**——awesome-jev 3 个窗口外背景 ID；awesome-system-one 7 个窗口外背景 ID + 两个已知字符串（2609.14973 = PhysBrain 误引、4157.1124 = Science DOI 片段）；awesome-decision-models 与 awesome-jev-security 干净。**无窗口内新线索。**

## 线索处置

论文线索（paper_leads）与非论文线索（non_paper_leads）的逐条处置见 [数据文件](../data/social-search-2026-11-28.json)。watch leads：原有各项（Sarvam Prism、书生·明决/Intern-Decision、Gemini Decisions/Gemini Decision 1、Microsoft-Decision-1.1、HeyGen Decision 1、autotrust JEV-27B-VL）均仍无 arXiv 报告；**新增一项**：preprints.org 的 Jev-Like Models survey（非 arXiv，暂不入库）。
