# arXiv 第 12 轮检索（2026-11-09）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-09.md)

周一上午执行（02:43 UTC 起）：探针显示索引已到首次提交 **11-06**。新窗口（11-06 至 11-09）用四条常设查询加五个 token 变体，另将**常设查询与变体全部全窗口重扫**（2026-09-15 起，Jev/decision model 单数各取最新 200 条）。371 条去重记录，**15 条新候选：11 篇收录（4 direct、7 related），4 篇排除**。

**迟索引再次命中**：11-05 首发的 9 篇（2611.077xx-084xx）周日 20:00 ET 才公告入库，上周五的第 11 轮全窗重扫全部错过——本轮全窗重扫一次捞回，加上 11-06 首发的 3 篇新窗口命中。目录由 325 增至 **336 篇：214 direct、118 related、4 foundations，123 篇有已核实代码**。台账 480 → **495 条：336 收录、157 排除、2 待核实**。

## 新增与阅读优先级

| 论文 | 首次提交 / 版本 | 分类与推荐理由 | 证据边界 |
| --- | --- | --- | --- |
| [Jev as an LLM Safety Guardrail](https://arxiv.org/abs/2611.08845v1) | 2026-11-06 / v1 | **优先阅读；security / direct**。南加州大学。托管 Jev（jev-latest）作为 Qwen2.5-1.5B 前置安全过滤器的端到端实测：有害回答 73.2%→2.4%、分层设计 5.6%/4.0%、宏 F1 0.9351→0.9512，是护栏方向少见的完整预算-拒答曲线。 | 仅三个英文安全集；等预算对比单门增益有限且留出集上不稳定。代码已核实（ANRGUSC/llm-safe-jev）。 |
| [Escalate or Close](https://arxiv.org/abs/2611.08229v1) | 2026-11-05 / v1 | **优先阅读；security / direct**。弗罗茨瓦夫理工大学。七攻击族逐族留出，监督检测器（ModernBERT）给留出族 37-60% 低危判定时，托管 Jev 与 Clef 在 5% 良性预算内每族至少上报 97.6%；对"快层悄悄关掉未见攻击"给出清晰测量设计。 | Jev 把 37% 良性孪生也上报；其训练数据可能含公开攻击族；Jev 引导搜索 300 查询内使 43% 留出攻击通过，且重问时答案漂移（60% 改为上报）。 |
| [Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854v1) | 2026-11-05 / v1 | **有条件推荐；architecture / direct**。Nace.AI 技术报告，四个开源决策模型（8B-27B，Max 基于 Kev 栈）+RLAF+一致性损失；Decision Index 0.4.1 上 Max 67.52 对托管 Jev 1.14.0 的 60.70，183 ms/请求。 | 厂商自报、自跑基准；托管 Jev 对比取决于测试时 API 版本；选项重排稳定性未经独立审计。代码已核实（nace-ai/drex-decision-models）。 |
| [Probabilistic Relevance Decisions for Semantic Retrieval](https://arxiv.org/abs/2611.08014v1) | 2026-11-05 / v1 | applications / direct。BEIR SciFact 上 BGE-M3 稠密检索 + Jev Noul（jev-1.13.0）/OpenAI Predicate 重排对照：深度 50 全库 nDCG@10 0.6413→0.7805（Jev 最高），并给出成本-延迟-缓存明细。 | 四个配对自助法深度区间均含零；OpenAI 大量精确零分带来并列随机化敏感性；探索性未校正分析，不宣称普遍优势或深度等价。 |
| [GeoJeV](https://arxiv.org/abs/2611.08879v1) | 2026-11-06 / v1 | applications / related。国防科大。超高分遥感证据获取去生成化：冻结的开放 metask-jev-4b-policy-mix1 输出区域概率分布，Region Rank/Sparse Branch/Depth Gate 共享同一分布控制搜索，Qwen3-VL-8B 平均 +5.32pp、提速 7.8 倍。 | 托管 Jev 仅引用未评测；每基准单骨干（备选仅 LLaVA-OV-7B）。 |
| [RELOAD（Extending Reasoning via Looping）](https://arxiv.org/abs/2611.07736v1) | 2026-11-05 / v1 | architecture / related。Lamarr/Fraunhofer IAIS/EPFL/Bonn。循环层须与决策模型共同训练才有收益（0.4B-4B 六模型，编码器在超训练推理链上最高 +23 点），控制器以 3/4 算力保留大部分增益。 | 未评测托管 Jev（解码器基于开源 Kev 重建）；结论限所用模型族与训练设置。 |
| [AffordJEV](https://arxiv.org/abs/2611.07896v1) | 2026-11-05 / v1 | applications / related。北京大学。可供性定位去思维链化：冻结分割器出候选、System One 判别器（Qwen3.5-4B LoRA）单次前向打分，层级互纠；仅训 InstructPart 即在 UMD/IIT-AFF 零样本超过 CoT 方法与 Valen/H2O/JevAny 判别器。 | 托管 Jev 仅出现在文献表；操作词对齐收益（14.22 对 6.39 gIoU）显示措辞敏感性与架构未分离。 |
| [DMGT（The Blindfolded Controller）](https://arxiv.org/abs/2611.07934v1) | 2026-11-05 / v1 | agents / related。考文垂大学。用开放 d3-turbo 以环境/任务描述初始化 RL 策略：七个稀疏奖励任务七胜纯 RL、五胜纯 DM。 | 托管 Jev 仅作为示例引用；增益限作者自建任务套件；描述指南与消融同源。 |
| [RouteAlign](https://arxiv.org/abs/2611.08162v1) | 2026-11-05 / v1 | agents / related。MemTensor/人大/上交。以任务需求组织 LLM 服务选择的证据积累，比最强开放 Jev 风格后端（Kev/Open-Jev/Decider/SemIf）高 5.22/6.44 分且生成成本低 9.7%。 | 未用托管 Jev；结果依赖作者自选服务池；打分器复用仅目录更新模拟验证。代码已核实（MemTensor/RouteAlign）。 |
| [Decision Models as Retrieval Gates](https://arxiv.org/abs/2611.08325v1) | 2026-11-05 / v1 | security / related。Google/UCSC。Kev-4B 门读 HTML 筛注入与污染：注入攻击成功率 27.9%→5.7%（76 ms/段）；污染台上伪造暴露 28%→0.5%、准确率保持 83%。全开源模型。 | 大模型裁判 AUROC 更高（0.99 对 0.94）但贵十倍；托管 Jev 仅引用；评测集为自建。 |
| [Ru-Jev 标签措辞增强](https://arxiv.org/abs/2611.08439v1) | 2026-11-05 / v1 | calibration / related。独立 307M 交叉编码器两个版本对照：标签多表面形式增强在常规/外来词表上全场景更准（最多 +0.24，14 项增益 11 项过 Holm 校正），缩写与不透明代码无增益。 | 全程未调用 Jev API（名字为致敬）；两个未见数据集准确率 -8.4/+5.6 点；单作者项目。代码已核实（beskvladimir-create/ru-jev）。 |

质量判断与相关性分数分开：11 篇均满足明确模型关系与实质贡献的收录门槛；相关性分不代表质量认证，实验未复现。

## 排除与去重

| 候选 | 处理理由 |
| --- | --- |
| [tok: a textual concrete syntax of BPMN and DMN](https://arxiv.org/abs/2611.07945v1) | "Decision Model" 指 OMG 的 DMN 流程标准记法，非 Jev 式类型化决策模型。 |
| [Hardness of integer linear feasibility with cyclic support](https://arxiv.org/abs/2611.08304v1) | 组合优化硬度证明；"System One" 词元命中与 Jev/类型化决策无关。 |
| [Efficient Spintronic Stochastic In-Sensor Computing Modules](https://arxiv.org/abs/2611.08715v1) | 自旋电子在传感器计算硬件；"System One" 命中为误报。 |
| [Toward LLM Self-Play Under Data Scarcity](https://arxiv.org/abs/2611.08908v1) | 立场文章，仅以 System 1/System 2 作隐喻，无 Jev 或类型化决策模型内容。 |

既有目录条目（TandemBench、Cyber-JEV、SAG2 等在全窗重扫中再次出现）未重复添加。

## 检索覆盖与可复核性

1. Atom API 正常；探针 `all:"language model"` 限定新窗口返回 17 条，最高 published 日期 11-06——11-07 起投稿尚未公告，**下一轮须从 11-07 重扫**。
2. 四条常设查询（`Jev`/`System One`/`typed decision`/`decision model`）扫新窗口并全窗重扫（Jev 与 decision model 单数各取最新 200 条，未读尾部为 10 月前旧记录，此前各轮已覆盖）；五个变体（MedJev/System-One/System 1/decision models/JevBench）同样双窗口。全部 19 条查询与命中数记录在 [search-log.json](../data/search-log.json)。
3. 11 篇收录条目的证据引用逐条与摘要或 PDF 全文（本地提取）断言一致后才写入；四个 GitHub 仓库经 API 核实公开。排除条目仅记台账不改目录。
4. 全部 11 篇来自 API 查询命中，无社媒/网页渠道独立发现；[同日社媒检索](SOCIAL_SEARCH_2026-11-09.md)新增 0 篇，其 Prism/Vega 观察线索不涉及 arXiv 记录。

## English summary

Monday-morning sweep with the four standing queries (fresh window 11-06..11-09, index reached 11-06) plus whole-window standing and variant re-runs since 09-15: 371 unique records, 15 fresh candidates, 11 added (4 direct — Jev as an LLM Safety Guardrail, Escalate or Close, Drex, Probabilistic Relevance Decisions; 7 related — GeoJeV, RELOAD, AffordJEV, DMGT, RouteAlign, Retrieval Gates, Ru-Jev), 4 excluded. The nine 11-05 first submissions were announced only Sunday 20:00 ET and were missed by Friday's round-11 whole-window re-run; the whole-window re-run again caught them. Four GitHub repositories verified via API (code count 119→123). Submissions from 11-07 onward were not yet announced at run time and must be re-covered next round.
