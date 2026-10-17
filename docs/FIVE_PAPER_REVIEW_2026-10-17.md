# Five-paper source check / 五篇论文原文复核

Reviewed on **2026-10-17** against current arXiv abstract pages and official Atom metadata; targeted full-text checks for the first three papers. All five were already included at the latest observed versions. **No new papers or version upgrades; the catalogue remains at 174.** Bilingual annotations and review dates were refined. This is a source check, not experimental replication.

本轮复核五篇已有论文，当前版本均与目录一致；未新增或升级版本，总数仍为 **174 篇**。更新中英文简介、关联说明与核实日期，不代表实验复现。

| Paper | Current version / revision date | Source-grounded clarification |
| --- | --- | --- |
| [Are AI Decision Models Biased? A Case Study of Jev](https://arxiv.org/abs/2610.19619v1) | v1 · 2026-10-14 | 41,500 initial responses plus 15,000 additional conjunction responses. Familiar answer-level bias tests often look favorable; irrelevant numbers, answer order and probability changes reveal vulnerabilities. The expanded conjunction test has approximately 54% rule violations. The paper does not establish a general calibration advantage over zero-shot autoregressive LLMs. |
| [Jev-ToM: Evaluating Theory of Mind in Typed Decision Models](https://arxiv.org/abs/2610.18610v1) | v1 · 2026-10-13 | Five typed models and seven primary generative baselines, 11,117 English questions, nine benchmarks and six capability groups. Jev’s 73.2% source-balanced accuracy includes native controls. Section 3.4 does not list Claude among the seven primary baselines; limitations explicitly exclude complete interactive-assistant evaluation. |
| [Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences](https://arxiv.org/abs/2609.24965v3) | v3 · 2026-10-15 | Ten cases, twenty Choices, five repetitions: 50 planned requests and 100 semantic answers per configuration. Table I and Section III-C report a successful-request median of 0.335 s and p95 of 0.442 s. Jev ties five configurations on complete semantic correctness; GPT-5.6 Luna is not one of those ties. |
| [LLM-as-Jev: LLMs Are Already Jev-Style Decision Models -- When and How to Fine-Tune Them](https://arxiv.org/abs/2610.02076v3) | v3 · 2026-10-13 | The full title includes the fine-tuning subtitle. The current abstract covers training-free inference, KL-anchored fine-tuning and budgeted Thinking Jev, beyond merely a constrained output interface. Proprietary Jev internals are not disclosed. |
| [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160v1) | v1 · 2026-09-26 | The full title ends in “Checklist”. It reviews 28 papers posted September 19–24 and derives a 14-item checklist. It is an early evidence map, not a settled architecture survey or a disclosure of TypeSafe’s RLCD training recipe. |

## 中文核对说明

- **偏差研究：** 不能概括为“普遍复现人类经典偏差”。原文先报告若干熟悉测试上的良好表现，再指出改写情境、无关数字、选项顺序及返回概率中的脆弱性。追加合取实验的约 54% 违规率有独立的 15,000 次响应样本范围。详见[正文](https://arxiv.org/html/2610.19619v1)。
- **心智理论：** 主要对照确为五个类型化模型、七个生成式模型，但七个主要生成式基线不含 Claude；论文未验证完整助手的多轮交互成功率，因此不能将结论写成已证实的长程上下文瓶颈。详见[第 3.4 节与 Limitations](https://arxiv.org/html/2610.18610v1)。
- **科研决策：** “100”是重复后的语义答案数，不是 100 个独立任务；实验中的成功请求中位延迟为 **335 ms**，而非 70–250 ms。与 Jev 同为语义全对的配置是 GPT-5.6 Sol、GPT-6 Astra、Claude Sonnet 5、Claude Opus 5 和 Kimi K3；不能笼统写成所有 GPT-5.6 配置持平。详见[表 I、第 II-C 与 III-C 节](https://arxiv.org/html/2609.24965v3)。
- **方法与综述：** 保留两篇的完整最新标题，并区分开放方法、早期证据审计与尚未公开的 Jev 内部训练配方。

All numerical statements above retain their paper-specific setup. The list is not a cross-paper leaderboard, and no popularity claim was verified.

所有数字均保留论文内的实验条件，不合并为跨论文排行榜；本轮也未核实“关注度较高”的传播指标。
