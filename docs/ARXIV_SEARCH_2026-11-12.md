# arXiv 第 13 轮检索（2026-11-12）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-12.md)

周三上午执行（01:44 UTC 起）：探针显示索引已到首次提交 **11-10**。新窗口（11-07 至 11-12，补上第 12 轮标记的缺口）用四条常设查询加五个 token 变体，另将**常设查询与变体全部全窗口重扫**（2026-09-15 起，Jev/decision model 单数各取最新 200 条）。382 条去重记录，**24 条新候选：19 篇收录（11 direct、8 related），5 篇排除**。

**迟索引再次命中**：11-06 首发的 5 篇（2611.089xx-101xx，含 TrialJev、Laya 顺序敏感、数字助推、文风审计等）在周一第 12 轮全窗重扫后才公告入库，本轮全窗重扫一次捞回；加上 11-07 至 11-10 新窗口命中的记录（含一条 11-03 迟索引与一条 10-12 的 v3 更新）。API 扫描收录 19 篇；另有 [EarthJev](SOCIAL_SEARCH_2026-11-12.md)（2611.10005，首发 11-04）任何常设/变体查询都不可见（未加连字符复合名不按 `all:"Jev"` 分词），由[同日社媒检索](SOCIAL_SEARCH_2026-11-12.md)发现并定向补录，合计 **20 篇（11 direct、9 related）**。目录由 336 增至 **356 篇：225 direct、127 related、4 foundations，131 篇有已核实代码**。台账 495 → **520 条：356 收录、162 排除、2 待核实**。主窗口首次提交范围延至 **2026-11-10**。

## 新增与阅读优先级

| 论文 | 首次提交 / 版本 | 分类与推荐理由 | 证据边界 |
| --- | --- | --- | --- |
| [MMDM: Measuring Massive Multitask Decision Making](https://arxiv.org/abs/2611.14309v1) | 2026-11-10 / v1 | **优先阅读；evaluation / direct**。港中文/HKUST/Lightspeed。5,448 题、16 个新构任务类别的多任务决策基准（单选/多选/软标签，选项 2-1,024、输入至 64,817 token），28 个决策模型同台：Jev 1.14.0 硬单选 67.17，落后 WeMM-JEV 27B（76.00）与 Liquid-d1-Ultra（73.32）；选项逻辑/约束规划/多选全体失准（最佳多选仅 36.81%）。 | 标签与软目标出自作者自建流程；各 API 版本以测试时固定为准。代码已核实（mmdm-benchmark/mmdm）。 |
| [LEASH: Stay Safe in Agentic Robotics](https://arxiv.org/abs/2611.14115v1) | 2026-11-10 / v1 | **优先阅读；security / direct**。西浦/昆山杜克/利物浦/NUS/CNRS。RoboRisk 基准（92 仿真+13 实机任务，五类风险全闭环）+ LEASH 护栏：任务/动作/提交三道门经托管 Jev（或 OpenAI Decisions API）审查，六个基础模型伤害率全线下降而完成率大体保留。 | 共享安全策略为作者自设而非独立标准；效果按规划器-环境对报告。 |
| [Can the Confidence and Decisions of System 1 Models Be Trusted?](https://arxiv.org/abs/2611.12521v1) | 2026-11-09 / v1 | calibration / related。独立研究者。开放确定性审计基准：保标签扰动校准、捆绑请求跨问题干扰、事后归因忠实度；证明提供方"置信度"是闭式离散度变换而非经验准确率；≥4B 模型校准与注入防御均强于 logprob/JSON 基线。 | 受测为五个开放权重模型（Tev1/Clef 等），托管 Jev 仅作背景；单作者项目。代码已核实（j2launay/jev-decision-models-xai）。 |
| [Beyond Ranking: Are Decision Models Calibrated Relevance Scorers?](https://arxiv.org/abs/2611.11480v1) | 2026-11-08 / v1 | **优先阅读；calibration / direct**。Keenable/滑铁卢。首个对照 TREC 人工判定校验 Jev 原生相关性的工作：DL21 上 Jev 打分>0.9 的配对仅 66% 相关，两参数校准（DL19 拟合）迁移后 Brier 反超 FLAN-UL2 与交叉编码器，期望 F1 截断免调参。 | 校准为集合特定；八个 BEIR 库、TREC 标签。 |
| [Evaluating Jev on Arabic](https://arxiv.org/abs/2611.10802v1) | 2026-11-07 / v1 | evaluation / direct。Fraunhofer IAIS/Bonn/Lamarr。67 系统（47 决策模型）、43 项阿拉伯语任务统一零样本评测：Jev 1.14.0 平均 69.24（1.13.0 为 68.77，Gemma-4-31B 71.81）；方言-标准语差距 -7.94 至 -0.35pp，巴勒斯坦银行语料损失大于 LLM。 | 全部为描述性结果，不做一般排序或因果解释；SIB-200 区间含零。 |
| [AbductionBench](https://arxiv.org/abs/2611.10705v1) | 2026-11-07 / v1 | evaluation / direct。Sharif/德黑兰/Tarbiat Modares。溯因推理统一基准（27 数据集/10 领域）：Jev 作为非 LLM System One 决策系统参评单选任务，紧凑证据上追平小 LLM、长案例明显落后。 | Jev 仅覆盖单选子集；轨迹按可观察输出分析。 |
| [Track or Follow?](https://arxiv.org/abs/2611.10414v1) | 2026-11-07 / v1 | applications / direct。NTU/武大/UCL CBT。多 agent 交易系统全 agent 走 Jev 接口（含托管 jev-1.13.0）：判断与公告窗口异常收益相关（Spearman 0.119、AUC 0.833），但 72% 财报新闻晚于公告，从发布后首笔交易起算关联塌缩至 0.023。 | 确证性周度检验未发现超出纯代码特征的信息；Jev 部分为描述性。代码已核实（yebof/track-or-follow）。 |
| [TrialJev](https://arxiv.org/abs/2611.10145v1) | 2026-11-06 / v1 | applications / direct。UHN/多伦多大学/Vector。开放权重单遍入组打分器：27B 两版 80.99-81.88%，托管 Jev API 81.28%，配对区间含零；本地 178ms/对，生成式判决慢 2.45-2.70 倍。 | 仅 TREC 合成病人、临床未验证；托管延迟为 API 上报。代码已核实（oibrahi1/TrialJev）。 |
| [Peptide ICL 系统比较](https://arxiv.org/abs/2611.09994v1) | 2026-11-03 / v1 | applications / direct。Radboud。多肽性质低数据预测中把托管 Jev 1.14 与 GPT-6 Luna Decisions 作为 TDM 预测器与 LLM/表格模型/XGBoost 系统对比：Jev 五任务平均 macro-F1 超 DeepSeek-V4.1 Flash 与 Gemma-4 31B，附成本对比。 | 数据集小、差异检验功效有限；Jev 为单一多肽套件上的零样本调用。代码已核实（BigChemistry-RobotLab/icl-benchmark）。 |
| [Nudging Decision Models](https://arxiv.org/abs/2611.09264v1) | 2026-11-06 / v1 | security / direct。帕德博恩大学。数字助推 × 三决策模型（Jev/Decision-1/d1）各 600 次：默认助推使预设商品选择率 47-49%→97.5-99.9%，且自动助推强于社交助推——与推理型 LLM agent 相反，符合 System 1 标签。 | 单一模拟商店；人类/LLM 对比沿用早前实验。 |
| [Same Facts, Different Remedy](https://arxiv.org/abs/2611.08995v1) | 2026-11-06 / v1 | security / direct。UNSW。预注册文风审计：GPT-4o-mini/GPT-5-mini 与 Jev 1.13.0 三系统群体差距全部 ≤0.5pp，但同一投诉两种文风 2.6-6.3% 得到不同货币决定；Jev 同文本重评 TV 距离 0.021、档位翻转 2.5%；统一文风反转 Jev 两个差距。 | 事实敏感度为文风差距的 49-387 倍（阳性对照）；LLM 审计员在 3.3-11.7% 改写中标记事实变化。 |
| [DM-Call](https://arxiv.org/abs/2611.10977v1) | 2026-11-07 / v1 | agents / direct。Enhans/UCL。函数调用加决策模型验证器（托管 Jev jev-1.13.0 或开放 PPLX Decider）：验证概率+二元判断+schema 错误累积回传免执行修正，BFCL/API-Bank 准确率提升、两种验证器接近。 | 仅两个函数调用套件；被验调用来自同一生成流水线。代码已核实（gogoymh/decision-model-guided-function-calling）。 |
| [PolyRoute](https://arxiv.org/abs/2611.13843v1) | 2026-11-10 / v1 | evaluation / related。Intel。12 语言+混合语类型化决策路由基准（322 原生消息+156 混合语），Laya 家族 61.2%→96.6%，TF-IDF+LR 达 91.9%；划分仅能分辨 >4pp 差异。 | 全部文本与标签 LLM 生成；托管 Jev 未参评。 |
| [Omni-JEV](https://arxiv.org/abs/2611.13777v1) | 2026-11-10 / v1 | architecture / related。Merit Interactive。全双工语音对话五动作决策：对齐语音骨干双流编码+文本共享读出，交叉熵微调+RLCD；Gaussian 版音频 84.08%/文本 96.55%。 | 五类动作为自定义体系；托管 Jev 仅接口引用。 |
| [ZeroPoint](https://arxiv.org/abs/2611.12992v1) | 2026-11-08 / v1 | architecture / related。未署单位。能量决策模型的"空答案零能态"：弃权并入普通推理，同分布同 NLL 训练，优于学习型拒绝类与阈值 softmax。 | 对比用开放 Laya 与基线，未评测托管 Jev。代码已核实（Javihaus/zeropoint，作者自引）。 |
| [NuJEV](https://arxiv.org/abs/2611.11359v1) | 2026-11-08 / v1 | applications / related。复旦。Jev 结构化决策思想用于 PanNuke 细胞核计数/分型：视觉 LoRA+并行头单遍预测，五查询 MAE 1.844（致密 5.268），语言请求 MAE 降 76.2%。 | 仅 PanNuke 族；代码承诺未发布。 |
| [LoMASA](https://arxiv.org/abs/2611.11234v1) | 2026-11-08 / v1 | applications / related。西安外国语/北大-北海道。全本地双模型 B2B 报价助手：35B MoE 作 System 1 从选项概率读置信，硬规则上报 42.5%、人工仅决 19.5%，自动裁定追平规则基线 0.894。 | 模拟情境；选项概率免训练校准但 27B System 2 很少改变决策。 |
| [Deterministic Split-K](https://arxiv.org/abs/2611.10334v1) | 2026-11-07 / v1 | applications / related。JPMorgan Chase。vLLM Split-K 原子归约使 LoRA 推理不确定：Jev 式结构化决策概率在 81.47% 原子对比中变化并翻转；确定性 Triton 实现仅多 1.02-2.62% 延迟。 | 决策模型为三个负载之一；确定性限于同输入重放。 |
| [Maya a1](https://arxiv.org/abs/2611.09803v1) | 2026-11-06 / v1 | security / related。Intel。开放 Laya 检查点全循环旋转测试：25.8% 题目答案随选项位置改变（金标首/末差 10.1pp），乱序微调降至 7.2%，并行布局微调达 0.5%。 | 标签 LLM 制+教师过滤；结论限于 Laya 而非托管 Jev。 |
| [EarthJev](https://arxiv.org/abs/2611.10005v1) ※社媒补录 | 2026-11-04 / v1 | applications / related。RIKEN AIP/武大/东大。UHR 遥感 VQA 证据获取去生成化：轻量头批量打分候选视图+格式特定校准，五基准平均 53.06%（超 ZoomSearch 2.33-14.73pp）、延迟 11.30→1.67 秒。 | 托管 Jev 仅被引用未调用；决策模块按回答模型逐一拟合。代码已核实（Da1daidaidai/EarthJev）。非 API 命中，见[社媒检索](SOCIAL_SEARCH_2026-11-12.md)。 |

质量判断与相关性分数分开：20 篇（API 19 + 社媒补录 1）均满足明确模型关系与实质贡献的收录门槛；相关性分不代表质量认证，实验未复现。

## 排除与去重

| 候选 | 处理理由 |
| --- | --- |
| [Categorical RMT](https://arxiv.org/abs/2611.13093v1) | 量子物理随机矩阵理论；"System One" 词元命中为误报。 |
| [A Life of Its Own](https://arxiv.org/abs/2611.12076v1) | AI 伴侣 HCI 研究；"System One" 命中与决策模型无关。 |
| [DASH](https://arxiv.org/abs/2611.11854v1) | 人形机器人 VLA 系统，System 1/2 仅作架构隐喻，无类型化决策接口。 |
| [Thinking Twice](https://arxiv.org/abs/2611.09269v1) | 人类使用 GenAI 的双过程研究；未评测任何决策模型。 |
| [Where Polanyi Meets Galois](https://arxiv.org/abs/2610.16102v3) | 默会知识哲学论述，System 1/2 仅为隐喻；v3 更新（11-10）触发全窗命中。 |

既有目录条目（JevBreak、XDecideBench、Drex、Policy Gates、2611.00428、2609.28940 等在全窗重扫中再次出现）未重复添加。

## 检索覆盖与可复核性

1. Atom API 正常；探针 `all:"language model"` 限定新窗口返回 50 条，最高 published 日期 11-10——11-11 起投稿尚未公告，**下一轮须从 11-11 重扫**。
2. 四条常设查询（`Jev`/`System One`/`typed decision`/`decision model`）扫新窗口并全窗重扫（Jev 与 decision model 单数各取最新 200 条）；五个变体（MedJev/System-One/System 1/decision models/JevBench）同样双窗口。全部 19 条查询与命中数记录在 [search-log.json](../data/search-log.json)。
3. 19 篇收录条目的证据引用逐条与摘要或 PDF 全文（本地提取）断言一致后才写入；七个 GitHub 仓库经 API 核实公开（colinpriest/llm-jev-linguistic-profiling 虽见于 arXiv 评论但 API 返回 404，未记代码）。排除条目仅记台账不改目录。
4. 社媒渠道（微信/知乎/微博/X）在扫描前先行检索，X 交叉检索先于 API 扫描发现 3 条新记录：2611.11480 与 2611.10802 也被 API 扫描独立命中（归入 API 筛选），**EarthJev（2611.10005）则任何 API 查询都不可见**——未加连字符复合名不按 `all:"Jev"` 分词且摘要无其他常设词元，经 id_list 定向补录收录；详见[同日社媒检索](SOCIAL_SEARCH_2026-11-12.md)。

## English summary

Mid-week sweep with the four standing queries (fresh window 11-07..11-12, index reached 11-10) plus whole-window standing and variant re-runs since 09-15: 382 unique records, 24 fresh candidates, 19 added from the API sweep (11 direct — MMDM, LEASH, Beyond Ranking, DM-Call, Arabic Jev, AbductionBench, Track or Follow, TrialJev, peptide ICL, Nudging, Same Facts; 8 related — PolyRoute, Omni-JEV, ZeroPoint, the Jev-style XAI audit, NuJEV, LoMASA, deterministic Split-K, Maya a1), 5 excluded. The whole-window re-run again earned its keep: five 11-06 first submissions were announced only after Monday's round-12 re-run and were caught here. One further paper, EarthJev (2611.10005, first submitted 11-04), was invisible to every standing and variant query (unhyphenated compound name) and was added from the same-day social round's targeted id_list follow-up, bringing the round to 20 additions and the catalogue to 356. Eight GitHub repositories verified via API (code count 123→131; colinpriest/llm-jev-linguistic-profiling from one arXiv comment returns 404 and was not recorded). Submissions from 11-11 onward were not yet announced at run time and must be re-covered next round.
