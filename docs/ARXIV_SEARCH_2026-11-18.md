# arXiv 第 18 轮检索（2026-11-18）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-18.md)

周三凌晨执行（01:43 UTC 起）：探针显示新窗口已见 **11-16 首发批次**（11-17 及之后尚未公告）。第 17 轮收尾时标注「11-14 起首发须下轮补扫」，本轮新窗口即取 11-14 至 11-18。按协议双窗口执行：新窗口四条常设查询加五个变体；**常设查询与变体全窗口重扫**（2026-09-15 起）共得 **415 条**去重记录，**20 条台账外**。合计 **20 个新候选：17 收录（8 直接、9 相关）、3 排除**——单轮收录量为开库以来最高。目录 376 → **393 篇**（239 直接、150 相关、4 奠基）；台账 546 → **566 条**（393 收录、171 排除、2 待核实）；主窗口右界延伸至 **2026-11-16**。

**全窗口重扫首次捞出窗口内「漏网旧记录」**：[Beveridge（2611.18655，10-17 首发）](https://arxiv.org/abs/2611.18655v1) 与 [AdaMenu（2611.19005，11-13 首发）](https://arxiv.org/abs/2611.19005v1) 均为台账外——前者此前从未被任何一轮 token 查询命中（本轮 whole:`all:"Jev"` 243 条总量下浮出），后者正是第 17 轮 Jev 查询 200 条截断边缘外的 11-13 首发记录（第 17 轮已记录 MMDM/LEASH 同类问题，本轮实证「下轮重扫可回收」）。另两条 11-11 首发（[Frame First](https://arxiv.org/abs/2611.18761v1)、[Conv-Reluplex](https://arxiv.org/abs/2611.18753v1)）与一条 11-14 首发（[Program Distillation](https://arxiv.org/abs/2611.19461v1)）经全文核验排除。

**直接关系核验要点**：[Jev-as-a-Reward](https://arxiv.org/abs/2611.20955v1) 对两个版本的托管 Jev 做概率奖励校验；[S1Mal](https://arxiv.org/abs/2611.20699v1) **明言托管 Jev 因使用政策禁止恶意软件分析而未入评**——据此从「直接」降为「相关」，是本轮唯一因此改判的候选；[When Should Decision Models Compare Candidates?](https://arxiv.org/abs/2611.20335v1) 的 Jev 字样全部来自 Open-Jev/JevBench 基准名与文档引用，未用托管 API，同样记「相关」；[EditRec](https://arxiv.org/abs/2611.21155v1) 门控以 TypeSafe 文档实现的决策模型落地（§4.2），记「直接」；[BJAS](https://arxiv.org/abs/2611.19225v1) 明写 `jev-1.13.0` 批量选择；[AdaMenu](https://arxiv.org/abs/2611.19005v1) 对比 TypeSafe 官方束搜索基线；[Beveridge](https://arxiv.org/abs/2611.18655v1) 以相同请求经 API 评测托管 Jev（87.9% 对自家 93.0%）。

**列表级盲区补查**（37 个目录分类 `/recent`，分页至各分类尽头，共 **5,812 条**，覆盖首发至 11-18 的公告批次）：45 条命中 = **25 条已收录** + **10 条与 API 扫描重合的本轮新增** + **10 条误报**——其中 8 条为第 14/15/17 轮已核验的复现误报（2611.11274、11918、12544、13337、13448、17666 等，作者名/块级误匹配），新 2 条 [2611.18998](https://arxiv.org/abs/2611.18998v1)（作者名 Jevan Hutson）与 [2611.19397](https://arxiv.org/abs/2611.19397v1)（作者名 Stanojev）经 `id_list` 摘要核验同样为姓名子串误报，记档不入台账。**本轮列表检查未发现独立盲区。**

## 新增与阅读优先级

直接关系（8 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [TDM-Gauntlet](https://arxiv.org/abs/2611.20191v1)（evaluation） | 布拉迪斯拉发考门斯基大学；Kempelen 研究所；Cisco | 把 24 篇 ACL 论文的预测器换成托管 Jev（保留各自切分/标签/指标）得 46 个测试集：零样本直接替换 12/46；500 条标注下校准+GEPA 提示优化弥补差距中位 72%（每次 $1.66），LoRA 微调 97%——微调仍最准。 |
| [Jev-as-a-Reward](https://arxiv.org/abs/2611.20955v1)（security） | KT；成均馆大学；庆北大学 | RL 安全奖励校验协议：区分被自信放行伤害的份额与数量、裁判换版重校验；两个版本托管 Jev 作概率奖励时 11 次运行被放行伤害均收缩但集中盲区；加辅助项后 HarmBench 攻击成功率 0.287→≤0.033。 |
| [Beveridge](https://arxiv.org/abs/2611.18655v1)（architecture） | BDST（英国） | Apache 2.0 开源 System One 家族：ModernBERT-large+3.5M 决策网络，15 个类型化问题一次前向；运维文档基准 93.0% 胜五个 31B–675B LLM 之最（91.1%）与经 API 同题评测的托管 Jev（87.9%）；ECE 0.029 下 95% 准确率可自动交付 76% 决策，H200 单次 4.9ms。 |
| [AdaMenu](https://arxiv.org/abs/2611.19005v1)（applications） | 中国联通 | 大标签空间查询自适应候选菜单：检索构造紧凑菜单、单次决策模型调用；四个标签集（至多 1,016 标签）16 个模型×标签组全胜 TypeSafe 束搜索基线（+16.6~+34.3 分），输入 token 降 3.2–22.9 倍。 |
| [Jetriever](https://arxiv.org/abs/2611.21478v1)（agents） | 中国科学技术大学 | 记忆检索从相似度换成全池效用：托管 Jev 逐条给「对当前问题的有用性」决策分；InMind 125 间接问题金标对话 84.8% 排第一（BM25/MiniLM 1.6%/0.0%），MAB 四维分 55.4% 对 ReFind 44.3%，每题 $0.00834。 |
| [AgenticJevNav](https://arxiv.org/abs/2611.19912v1)（agents） | 未署名 | 目标搜索与导航：规划 Agent 持有目标，执行受阻/连续低进度时托管 Jev 审查版本化证据（版本/新鲜度/一次性检查），独立 RGB 反射可否决；仿真 60 试 73.33% SR、四足实机 30 试 70.0%。 |
| [EditRec](https://arxiv.org/abs/2611.21155v1)（agents） | NTT | WildChat-4.8M 构建 EditRecBench 检验「能否预判用户修改请求」，决策模型门控只展示高置信预测（§4.2 按 TypeSafe 文档实现）；训练门控胜现有决策模型，展示建议 pass@5 +12~25 分。 |
| [BJAS](https://arxiv.org/abs/2611.19225v1)（applications） | 谢菲尔德大学 | 卫星边缘计算预算化联合动作搜索：有界候选池 + 托管 Jev（jev-1.13.0）池内批量选择 + 数值验证后接受；对 LLM 生成卸载平均求解时间省 97.16%、时延持平且优于 GA/DDPG。 |

相关方法（9 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [FaceJev](https://arxiv.org/abs/2611.21604v1)（applications） | 中科院自动化所等 | 按 Jev 范式的人脸伪造检测：八个人脸部位问题共享图像编码、原生答案 logits 读异常概率、任一异常即判伪造；16 万张 PartForensics 部位级标注 + FS-GRPO 精确奖励对比，未见伪造类型超最强基线 7.25 分。 |
| [MedJev（模型）](https://arxiv.org/abs/2611.20992v1)（applications） | 港中文、清华、国大、同济、 squirrel 等 | 删去 Qwen3.5-4B VLM 上层语言与生成通路，决策头以预训练 query-key 匹配+MLP 残差单次多模态前向打分候选；四个医学分类/VQA 基准准确率 +7.93%、端到端加速 6.04 倍（与第 15 轮已收录的 MedJev 评估 2610.36006 同名不同文）。 |
| [A First Look: S1Mal](https://arxiv.org/abs/2611.20699v1)（security） | 尼科洛·库萨诺大学（罗马） | System One 决策模型首次进 Windows PE 恶意软件检测：Ghidra/capa 文本状态 + A0 单判定/A1 32 原子问题/A2 嵌入头三种读出；A0 AUROC 0.40–0.86、A1 平均 +54.61%、S1Mal 集成 0.9946@1.45% FPR；托管 Jev 因使用政策排除。 |
| [Cancer pathology](https://arxiv.org/abs/2611.20129v1)（applications） | 塔塔医学中心（加尔各答） | 决策模型首次上临床文本：Nimble 9B/Tev1 4B 从 1,113 份口腔癌病理报告抽 25 字段；Tev1 0.917 与 Qwen3.5 9B 持平且快 4 倍、ECE 0.022–0.026；概率 <0.94 升级 GLM-5.3-flash 达 0.982（38% 升级）；未评托管 Jev/Laya。 |
| [System 1 agents](https://arxiv.org/abs/2611.21053v1)（agents） | 克里特大学、卡罗林斯卡等 | 确定性编译器把工具 schema+请求编译成多选题，llama.cpp `/v1/systemone` 端点的原生 SystemOne 模型（OpenJev、Clef、pplx-decider）单次前向作答，全程零文本生成；157 个生物医学工具 97.0% 选对/正确拒绝，零捏造（LLM 5.5–19.7%）。 |
| [When Should Decision Models Compare Candidates?](https://arxiv.org/abs/2611.20335v1)（evaluation） | William & Mary、UCSD、斯坦福等 | 决策模型选动作的三种打分接口对比（Pointwise/Setwise/Candidate Attention），五个智能体基准（BFCL、MetaTool、Open-Jev、JevBench、Mind2Web）9,156 请求：Pointwise 仍具竞争力，Setwise 部分任务占优，候选注意力不稳定。 |
| [SuperGlance](https://arxiv.org/abs/2611.19138v1)（applications） | 清华 AIR、港科大广州等 | 驾驶版 System 1 读出：线性头从 VLM 首 token 前隐状态一次前向为固定 5,273 条候选轨迹打分，奖励离线化使监督目标可按奖励加权、RL 最大化精确期望奖励；84ms 规划比 Qwen-Drive-1.0 快六倍，多选题回答与基座解码相当。 |
| [Beyond Plain MCP](https://arxiv.org/abs/2611.19123v1)（agents） | 独立研究者 | 预注册评估 MCP 工具范式：code mode 对类型化工具桩写脚本 token 降 70–90%；返回形状提示影响至多 39.5 分大于加路由器；「决策层前置更好」的中心假设未获证实；开源测试台+微调 4B 工具选择模型。 |
| [Train After You Measure](https://arxiv.org/abs/2611.21393v1)（applications） | 独立研究者（特伦托） | 《Measure Before You Train》预注册后续：Tev1-0.8B/4B 在单用户 50–587 封邮件标注上 LoRA 微调对逻辑回归；消息类型 587 条时过线（+3.3）、动作开关全程落后（0.931 对 0.904/0.899），五假设证伪四个。 |

排除（3 条）：[Conv-Reluplex](https://arxiv.org/abs/2611.18753v1)（CNN 形式化验证，无相关词元，块级误匹配）；[Frame First, Decode Once](https://arxiv.org/abs/2611.18761v1)（单次前向几何基元坐标解码的「System-1」世界模型，无类型化决策接口，按通用双过程规则排除）；[Program Distillation](https://arxiv.org/abs/2611.19461v1)（System 2→System 0 程序蒸馏，贡献为可执行程序，Jev 类模型仅作基线 0.239，无托管 Jev 使用）。

## 核验与代码

- 全部 17 篇新增均完成 Atom 元数据、摘要与定向全文核验；证据引文写入前逐条断言于源文本（≤80 字符、合计 ≤25 词）。16 篇署名单位；[AgenticJevNav](https://arxiv.org/abs/2611.19912v1) 全文（PDF 与 arXiv HTML）均无作者单位信息，按「不臆造」原则记空（全库无署名单位论文 21 → 22 篇）。
- 新增 **7 个作者仓库**（GitHub API 确认公开）：imlrz/Jetriever、ntt-dkiku/llm-edit-recommendation、eltzanis/SystemOneAgents、zfkarl/MedJev、abhishek085/mcp-decision-layer、sathiskumarjothi0-oss/bev-decisions-pypi、federicolucca/foyer-measure。TDM-Gauntlet 声明的 NaiveNeuron/TDM-Gauntlet 返回 404（论文措辞为「将发布」），按 VX-One 先例不记。代码库计数 139 → **146**。
- 限制：本轮探针仅见 11-16 批次，11-17 起首发须下轮补扫；Jev Daily 自 11-15 期后未再发布（11-16/11-17/11-18 三期 404，下轮补查）；社媒平台原生搜索不可达，依赖网页索引（见同日社媒报告）。
