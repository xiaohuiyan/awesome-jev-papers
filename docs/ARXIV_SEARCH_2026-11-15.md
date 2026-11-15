# arXiv 第 15 轮检索（2026-11-15）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-15.md)

周日上午执行（01:43 UTC 起）：探针显示新窗口已见 **11-12 首发批次**——第 14 轮（11-13）迟到的 11-11 批次本次已入索引，补扫义务履行完毕。按协议双窗口执行：新窗口（11-11 至 11-15）四条常设查询加五个变体；**常设查询与变体全窗口重扫**（2026-09-15 起）共得 395 条去重记录，**17 条台账外 + 1 条社媒线索 = 19 个新候选：15 收录（6 直接 Jev、9 相关方法）、4 排除**。目录 356 → **371 篇**；台账 521 → **540 条**（371 收录、167 排除、2 待核实）；主窗口右界延伸至 **2026-11-12**。

**盲区补查（第 14 轮引入的动作，本次为第二次运行）**：对 37 个目录分类的 `/recent` 列表页（分页至各分类尽头，共 **5,233 条**，覆盖首发至 11-14 的公告批次）做标题/条目级 grep。38 条命中 = **32 条已收录** + **5 条误报**（2611.11274 媒体日记、2611.11918 气象协方差、2611.12544 非精确交替极小化、2611.13337 几何 ML VC 维、2611.13448 Fermat ProbCover——均系第 14 轮已做摘要级词元核验的误报复现）+ **1 条真盲区：[2611.15572](https://arxiv.org/abs/2611.15572v1)**。后者题为「Learning a calibrated decision head from logged bandit feedback」，标题与摘要只有「decision head」措辞、不含任何常设/变体词元，与 EarthJev 同属分词不可见模式——经摘要与全文核验为类型化决策内容（决策头 + bandit 反馈校准），按相关方法收录（calibration 类）。**列表级盲区检查第二次挣得车票。**

## 新增与阅读优先级

直接 Jev（6 篇，均 11-11/11-12 首发 v1）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [Actor, Judge, or Teacher?](https://arxiv.org/abs/2611.17167v1)（agents） | 浙大；百度 | JEV 自己做执行者只完成 42.9% 任务，但当 GRPO 老师把 Qwen2.5-1.5B 从 72.8% 提到 82.9%（ALFWorld）、56.8% 到 71.4%（WebShop）——差的执行者可以是好老师，提问措辞是关键。 |
| [SO-Arena](https://arxiv.org/abs/2611.15777v1)（evaluation） | 未署名 | 11 领域、5 能力族、21 个 System One 模型（含 Jev API 1.14，得分 60.4）；最可靠的两个模型（JevAny-27B 与 Jev API 1.14）在性能榜只排第 8/第 6——性能≠可靠。 |
| [Is Jev a Good Multilingual Judge?](https://arxiv.org/abs/2611.14861v1)（evaluation） | HITS；独立研究者 | 47 个语言变体上 Jev 约为 GPT-6.1 成本的 1/31–1/61，多数任务具竞争力，但低资源语言更易接受错误答案；概率输出有助识别错误。 |
| [S1-Evo](https://arxiv.org/abs/2611.16937v1)（security） | 未署名 | 面向 S1 接口的自进化攻击：jev-1.14 上平均 ASR 71.99%、高置信 57.47%，双系统工作流端到端违规至多 24.00%，攻击 token 省三到六成。 |
| [The Value of Thinking / HDM](https://arxiv.org/abs/2611.16961v1)（architecture） | 华为诺亚方舟实验室；利物浦大学；UCL | 零或 T 思考的混合决策模型：JevBench 上 HDM-4B 0.857 对 Jev 1.13.0 的 0.851，中位延迟省 72.5%；MiniWoB token 成本省 80.1%。 |
| [Survey simulation 审计](https://arxiv.org/abs/2611.15576v1)（applications） | 大阪大学；名古屋大学 | jev-1.14.0 概率做调查模拟：预测分数可升而关联仍失真（传统价值观男性例 16% 对 56%），颠倒提问顺序改变联合分布。 |

相关方法（9 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [Small Heads, Strong Decisions](https://arxiv.org/abs/2611.15592v1)（architecture） | 未署名 | 五种读出头统一协议重训：头的复杂度不影响准确率（0.5M 余弦头追平 27M 联合头），骨干规模才是主导（+4/+11 分）。 |
| [NESTONE](https://arxiv.org/abs/2611.16321v1)（architecture） | 南洋理工大学 | 决策信息集中在中间层、末六层可删；前缀子模型共享尾部与决策头 + 出口门控，每个深度都追平独立训练模型。 |
| [Look Here, Then Decide](https://arxiv.org/abs/2611.16565v1)（applications） | Cyrex；Deus Rex | Intern-Decision-4B 进漏洞挖掘流水线：单模型弱（AUC 0.73）但排序有用，确认 187 个内存安全发现（12 危急、148 高危）。 |
| [CURATOR](https://arxiv.org/abs/2611.16366v1)（agents） | AWS AI Labs | 预训练决策模型一次评多片段会退化；微调后能从大候选池稳定选证据片段，提升下游 RAG（上下文受限时尤甚）。 |
| [Recalibrating Laya](https://arxiv.org/abs/2611.16499v1)（calibration） | Intel | 130 行 numpy 五步再校准教程：池化 ECE 0.073 掩盖桶宏 0.143（12 选项桶 +0.22 过度自信），按桶温度才有效。 |
| [The Noise Floor of a Quantization Comparison](https://arxiv.org/abs/2611.15671v1)（applications） | Level5 | Clef-flash/Clef 2,400 条决策：引擎/重启/批处理/内核漂移移动 0–0.92% 决策，而 4-bit 区间与之完全分离；准确率掩盖 436 条变差。 |
| [JEV-VAD](https://arxiv.org/abs/2611.15362v1)（applications） | 天津大学；天津师范大学；上海深奇纪元 | 语音端点检测退化为标量停止决策：Qwen3-ASR-0.6B 冻结骨干 + 标量头 + 解码器前缀剪枝，EOT-bench 跨语言迁移。 |
| [Browser Immune System](https://arxiv.org/abs/2611.15302v1)（applications） | Alias Robotics；独立研究者 | 4-bit 4B 网络安全 Transformer 在浏览器内跑完整类型化决策模式（指针头），150ms 作答；BISBENCH-8 7/8，真实网页特异性仍是开放问题。 |
| [Learning a calibrated decision head from logged bandit feedback](https://arxiv.org/abs/2611.15572v1)（calibration，盲区捕获） | 独立研究者 | 仅凭日志化 bandit 反馈校准决策头：采样动作自身分数不能当 REINFORCE 奖励；CAPS 胜过只在确认答案上微调（Banking77 +2.6 分）。 |

## 排除与去重

| 候选 | 处理理由 |
| --- | --- |
| [2611.16778](https://arxiv.org/abs/2611.16778v1)（库存与广告鲁棒优化） | 运筹学随机优化，「decision model」指优化模型本身；无 Jev/System One/类型化决策内容。 |
| [2611.16655](https://arxiv.org/abs/2611.16655v1)（MuViRL 视觉语音表征） | 自监督多模态表征学习；内部「multimodal decision model」只是视图加权模块，非类型化决策接口。 |
| [2611.14652](https://arxiv.org/abs/2611.14652v1)（量子态制备内存成本） | 量子资源理论；「systems one at a time」短语误中 `System One` 词元。首发 11-10 但公告晚于第 13 轮全窗重扫，本次补获后排除。 |
| [2611.13015](https://arxiv.org/abs/2611.13015v1)（Ask2Decide） | LLM 智能体向人索取决策信息的澄清基准；标题的 Decisions 指人类规划决策，无类型化决策内容。社媒线索，经 id_list 定向拉取后排除。 |

另：5 条列表页误报系第 14 轮已核验条目的复现（见上），不再入台账。

## 检索覆盖与可复核性

1. Atom API 正常；探针 `all:"language model"` 限定新窗口（11-11..11-15）返回 50 条，published 最新到 **11-12**——11-11/11-12 批次已入索引（对比第 14 轮同一时刻为空）。11-13/11-14 首发尚未公告，**下一轮须从 11-13 重扫**。
2. 四条常设查询（`Jev`/`System One`/`typed decision`/`decision model`）扫新窗口并全窗重扫（Jev 与 decision model 单数各取最新 200 条）；五个变体（MedJev/System-One/System 1/decision models/JevBench）同样双窗口。全部 21 条查询与命中数记录在 [search-log.json](../data/search-log.json)（新窗口：Jev 7、System One 3、typed decision 3、decision model 13、MedJev 0、System-One 3、System 1 2、decision models 13、JevBench 1；全窗：Jev 235、System One 102、typed decision 79、decision model 237、MedJev 1、System-One 102、System 1 56、decision models 238、JevBench 8）。
3. 盲区补查：37 分类 `/recent` 列表页分页至各分类尽头（5,233 条、38 命中），1 条新捕获（2611.15572）以 `id_list` 摘要级核验后收录；5 条误报为第 14 轮已核验条目复现。
4. 社媒渠道（微信/知乎/微博/X）同日先行检索，X 交叉核出的 4 个新 ID 与 API 扫描重合（收录归扫描轮），社媒自身贡献 1 条排除（Ask2Decide）；详见[同日社媒检索](SOCIAL_SEARCH_2026-11-15.md)。
5. 代码核验：新增 **5 个作者仓库**（ZJU-REAL/decision-agents、wuzengqing001225/jev-survey-distributions、holdrain/SO-Arena、Level5Tech/clef-quant-bench、yuan-phd/jevmark；GitHub API 确认公开；代码计数 131 → **136**）。2611.16961 与 2611.15592 论文声明的仓库（zhengxuyu/HDM；Ritvik19/DecideAnything，后者用将来时「will be open sourced」）验证时 404，按第 13 轮先例不录入。
6. 21 篇论文未署名单位（新增 3 篇：2611.16937、2611.15777、2611.15592——PDF 与 HTML 首页均无单位行）。

## English summary

Sunday sweep (01:43 UTC) over both windows: the probe saw the 11-12 first-submission batch, so the batches round 14 missed had reached the index. The fresh window (11-11..11-15) with four standing queries plus five variants and the whole-window re-runs since 09-15 pooled 395 unique records; 17 outside the ledger plus one social lead gave 19 fresh candidates - **15 added (6 direct Jev, 9 related methods), 4 excluded** (an OR inventory-planning token match, a visual-speech view-weighting token match, a quantum 'systems one at a time' token match, and the Ask2Decide social lead with no typed-decision content). Direct: Actor/Judge/Teacher (JEV as GRPO teacher, 72.8 to 82.9 ALFWorld), SO-Arena (21 System One models, reliability lags performance), Jev as multilingual judge (47 varieties at 1/31-1/61 of GPT-6.1 cost), S1-Evo attacks (71.99% mean ASR on jev-1.14), HDM (0.857 vs Jev 0.851 on JevBench at -72.5% latency) and the Jev survey-simulation audit. Related: the readout ablation, NESTONE adaptive depth, the Intern-Decision-4B vulnerability harness, CURATOR evidence selection, the Laya recalibration recipe, the Clef quantization noise floor, JEV-VAD endpointing, the in-browser Browser Immune System, and the CAPS bandit-feedback calibration paper - the last one caught only by the fused-name listing blind-spot check (no standing token anywhere: 'decision head' wording), the check's second earn. Catalogue 356 -> 371; ledger 521 -> 540 (371 included / 167 excluded / 2 pending); window extended to 2026-11-12; five author repos verified (131 -> 136 with code); two stated-but-404 repos not recorded. Submissions from 11-13 onward were not yet announced and must be re-covered next round.
