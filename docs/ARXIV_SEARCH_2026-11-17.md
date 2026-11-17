# arXiv 第 17 轮检索（2026-11-17）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-17.md)

周二凌晨执行（01:43 UTC 起）：探针显示新窗口已见 **11-13 首发批次**（11-14 及之后尚未公告）。第 15 轮收尾时标注「11-13 起首发须下轮补扫」；11-16 尝试的第 16 轮在两条查询后被中断、从未提交，本轮一并接管。按协议双窗口执行：新窗口（11-13 至 11-17）四条常设查询加五个变体；**常设查询与变体全窗口重扫**（2026-09-15 起）共得 **399 条**去重记录，**4 条台账外**（Marimba、UltraBERT-JEV、LuthorSQL、S1Pert，均为 11-13 首发 v1）。另首次跑通**四份外部 awesome 清单对照**与 X 交叉核查，再得 2 个候选。合计 **6 个新候选：5 收录（均为相关方法）、1 排除**。目录 371 → **376 篇**（231 直接、141 相关、4 奠基）；台账 540 → **546 条**（376 收录、168 排除、2 待核实）；主窗口右界延伸至 **2026-11-13**。

**本轮最大收获来自外部清单对照**（第 14 轮只对照过 awesome-jev 一份）：[awesome-jev-security](https://github.com/Sarim-MBZUAI/awesome-jev-security) 带出 [VX-One（2610.30090）](https://arxiv.org/abs/2610.30090v2)——10-21 首发窗口内、v2（10-24）明确以「TypeSafe Jev; Microsoft Decision-1」的商业 System One 原语三元组为动机，但标题「Typed, Calibrated Decision Heads」把 `all:"typed decision"` 短语查询拆散，`/recent` 列表检查也因 10-21 早于五天回看窗口而不可见——**这是短语级盲区的又一实例（EarthJev 教训的变体），四份清单对照从本轮起列入常设动作**。同清单对照还排除 in-window 的 [LLMRouterBench（2601.07206）](https://arxiv.org/abs/2601.07206v1)（通用 LLM 路由基准，早于 Jev、无类型化决策接口）；awesome-jev 缺失的 3 条（RLCD、LLaDA、SalesRLAgent）与 awesome-system-one 的 7 条（System 2 Attention、RouterBench、Distilling S2 into S1、BRIGHT、System-1.x、Talker-Reasoner、RouterEval）均为窗口前背景，沿用第 14 轮处置不入台账；awesome-decision-models 干净。X 交叉核查带出的 MMDM（2611.14309）与 LEASH（2611.14115）经查**已于第 13 轮收录**（11-10 首发）——值得记录的是，本轮全窗口 token 查询依然够不到这两条 11-10 首发记录（各查询只取最新 100/200 条），跨清单与社媒交叉仍是必要防线；另顺带发现 2611.15592 已出 v2（记录仍钉在 v1）。

**列表级盲区补查**（37 个目录分类 `/recent`，分页至各分类尽头，共 **5,031 条**，覆盖首发至 11-17 的公告批次）：36 条命中 = **27 条已收录** + **3 条本轮新增**（与 API 扫描重合）+ **6 条误报**——第 16 轮未提交运行中已核验的 5 条（Merkurjev×2、Jevgenija、Ahijevych、DOI `YIJEVR`）加上新一条 [2611.17666](https://arxiv.org/abs/2611.17666v1)（SNN 波束选择，作者名 Timotijevic 触发），全部经摘要级核验无 Jev/System One/类型化决策内容，按第 14 轮先例记档不入台账。**本轮列表检查未发现独立盲区**——盲区由清单对照捕获。

## 新增与阅读优先级

相关方法（5 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [Marimba](https://arxiv.org/abs/2611.18330v1)（applications） | charcot.ai | 类型化语音决策接口：冻结 Qwen3-ASR 0.6B 上词面零样本打分 + 问题条件头 + 第 18 层回合结束读出；Speech Commands 0.93、词面 ECE ≤0.08、说话人切换 AUROC 0.966–0.980 超 ECAPA；明言 Jev 不接受音频，接口自建。 |
| [LuthorSQL](https://arxiv.org/abs/2611.17780v1)（agents） | UC Irvine；独立研究者 | 受 TypeSafe Jev 启发的非自回归 7B text-to-SQL「System 1 门」：一次前向预测有界文法槽位分数、至多 32 个候选计划；BIRD 隐藏集 68.03%@0.84s，与 Claude Opus 5.5 级联省 33.3% API 成本且准确率不降。 |
| [S1Pert](https://arxiv.org/abs/2611.17705v1)（applications） | 华南理工大学 | System-One 基因扰动响应预测：冻结 Jev 式编码器（开源 DECIDER-4B）+ 多级地标缓存 + 层次交叉注意力，方向性 Welch/等价检验区分有支持响应与不确定标签，摆脱基因级频率记忆。 |
| [UltraBERT-JEV](https://arxiv.org/abs/2611.17867v1)（architecture） | 独立研究者 | 编码器做 System One：UltraBERT-380M 每选项一掩码的四种微调配方对比，「yes 减 no」打分 +1.6 点、sigmoid 归一化 +0.8 点；A100 每决策 29ms 对解码器 68ms；辅助头同次前向预测支持句。 |
| [VX-One](https://arxiv.org/abs/2610.30090v2)（security） | 独立研究 | 把 Jev/MS Decision-1 的商业原语三元组（门/闭集选择/序数分）实现为 100K–10M 参数多头网络做边界分诊，逐头温度校准 0.7–1.7ms；结果刻意两面：时序 CIC 胜出但多类归因落败，漂移下所有方法 ECE 0.04→0.40。 |

排除（1 条）：LLMRouterBench（2601.07206）——40 万实例的 LLM 路由基准与统一框架，路由属模型选择基础设施、早于 Jev 且无类型化决策接口与托管 Jev 使用；由 awesome-system-one 清单对照带出，入台账备查。

## 核验与代码

- 全部 5 篇新增均完成 Atom 元数据、摘要与定向全文核验；证据引文写入前逐条断言于源文本（≤80 字符、合计 ≤25 词）。5 篇均署名单位（独立研究者 ×3、charcot.ai、华南理工；全库无署名单位论文维持 21 篇）。
- 新增 2 个作者仓库（IAMIbrahimmemon/luthorsql、liujiawen-jpg/S1Pert，GitHub API 确认公开）；**回填 1 个**：LEASH（2611.14115）第 13 轮收录时项目页尚无 GitHub 链接（仓库 11-12 才推送），本轮验证 zhuqinfeng1999/LEASH 公开后补记。VX-One 声明的 vectrayx/vx-one 返回 404，按先例不记。代码库计数 136 → **139**。
- 限制：本轮探针仅见 11-13 批次，11-14 起首发须下轮补扫；MMDM/LEASH 类「token 查询够不到」的窗口内旧记录仍依赖交叉核查兜底；社媒平台原生搜索不可达，依赖网页索引（见同日社媒报告）。
