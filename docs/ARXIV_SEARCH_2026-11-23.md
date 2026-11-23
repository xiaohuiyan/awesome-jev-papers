# arXiv 第 20 轮检索（2026-11-23）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-23.md)

周一凌晨执行（01:44 UTC 起，arXiv API 当日频繁返回 429，全部重试成功）：探针显示新窗口已见 **11-19 首发批次**（11-20 及之后尚未入索引）。第 19 轮收尾时标注「11-18 起首发须下轮补扫」，本轮新窗口即取 11-18 至 11-23。按协议双窗口执行：新窗口四条常设查询加五个变体；**常设查询与变体全窗口重扫**（2026-09-15 起），并且**从本轮起常设查询不再设取回上限**（`all:"Jev"` 254 条、`all:"decision model"` 278 条全部取回）。共得 **482 条**去重记录，**29 条台账外**；列表检查与外部清单对照另贡献 3 个候选（EgoJev、2605.19099、2609.14973），合计 **32 个新候选：25 收录（15 直接、10 相关）、7 排除**。目录 400 → **425 篇**（258 直接、163 相关、4 奠基）；台账 576 → **608 条**（425 收录、181 排除、2 待核实）；主窗口右界延伸至 **2026-11-19**。这是自 11-04 全窗口回填以来单轮收录最多的一轮。

**全窗口重扫回收两条截断边缘漏网记录**（均为 9 月首发，此前各轮复数查询 `all:"decision models"` 只取最新 100 条，二者落在取回上限之外）：[Decision 1.0（2611.18629，09-22 首发）](https://arxiv.org/abs/2611.18629v1) 与 [决策模型的委托方偏置研究（2609.17989，09-16 首发，v4）](https://arxiv.org/abs/2609.17989v4)。第 18、19 轮分别回收过两条、一条同类记录，本轮改为不截断后一次回收两条，此后该类漏网在查询层面不再存在（仅余索引滞后）。

**直接关系核验要点**（均以全文版本串或明示的 API 调用为据）：[MM-SystemOneBias](https://arxiv.org/abs/2611.26557v1) 附录「TypeSafe Jev is evaluated through its hosted service using version jev-1.14.0」；[VisualJevBench](https://arxiv.org/abs/2611.25435v1) 摘要「Extensive experiments on jev-1.14.0」；[LoopRoute](https://arxiv.org/abs/2611.25363v1) 全程以 Jev-1.13.0 为默认策略；[Vanguard](https://arxiv.org/abs/2611.23917v1)「We use Jev [11] (release jev-1.13.0) as D」；[Keystone](https://arxiv.org/abs/2611.25530v1)「We use Jev [13] as released」且经供应商 API 调用；[AnyS1](https://arxiv.org/abs/2611.23751v1) 以商用 Jev（jev-1.14.0）为 System-1 基线；[Decision2Care](https://arxiv.org/abs/2611.23700v1) 主决策模型为 Jev 1.13.0；[LLM 置信度分类研究](https://arxiv.org/abs/2611.25289v1) 以 Jev 1.13.0 为参照；[钓鱼邮件对比](https://arxiv.org/abs/2611.23683v1) 评测 Jev 1.13；[论证框架研究](https://arxiv.org/abs/2611.25361v1) 的检索实验「Jev through TypeSafe's official API」；[信念分组后训练](https://arxiv.org/abs/2611.25168v1) 把 Jev 零样本结果列为外部参照；[Decision 1.0](https://arxiv.org/abs/2611.18629v1)「We compare the official Jev 1.13.0 service」；[委托方偏置研究](https://arxiv.org/abs/2609.17989v4) 的跨模型复现含 Jev 1.14（经 OpenRouter System-One Decisions API）；[GLiDE](https://arxiv.org/abs/2611.26509v1) 与 [Clover](https://arxiv.org/abs/2611.24636v1) 的对照表以托管 Jev 为参照——两篇的 Jev 数字来自榜单/基准维护方或公开基准口径而非作者重跑，简评中已如实注明。

**相关关系**（未使用托管 Jev）：RLCDR（FxAI-DM 作校准奖励，Jev 仅见于参考文献）、FinVeriQA（Laya 路由）、Jeveration（Jev 式决策范式用于单次前向生图）、Piccolo（类 Jev 接口的多模态决策模型家族，未评测 Jev）、UEmo-D1（情绪识别决策模型）、网络发现（Laya 决策门控）、医学选择题（冻结语言模型 + 投影头）、闭环 STEM 导航（Typed Decision）、System-One RSI（未具名的 27B 决策模型）、EgoJev（把 VLM 当决策模型读输出分布）。

**七条排除**：[2611.26423](https://arxiv.org/abs/2611.26423v1)（Seer，标题「Shared Decision Models」实为生成式工具响应模拟器 + HL-Gauss 价值估计器，无类型化决策接口）；[2611.25311](https://arxiv.org/abs/2611.25311v1)（贝叶斯序贯决策理论，"logistic decision models" 为统计含义）；[2611.24831](https://arxiv.org/abs/2611.24831v1) 与 [2611.24535](https://arxiv.org/abs/2611.24535v1)（卡尼曼 System 1/2 比喻，无决策模型）；[2611.24993](https://arxiv.org/abs/2611.24993v1)（语音合成与深度伪造检测教程报告，`all:"System One"` 命中为摘要相邻词伪短语「automated systems. One response to this threat」）；[2605.19099](https://arxiv.org/abs/2605.19099v1)（awesome-system-one 列出的「DecisionBench (delegation)」，实为 LLM 委派基准，同名无关）；[2609.14973](https://arxiv.org/abs/2609.14973v1)（awesome-system-one 在正文中把它标注为 AutoTrust Decider-Pro 的论文，实际解析为 PhysBrain 1.5 具身基础模型报告，属误引）。每条排除理由中的触发短语均先逐字核对于摘要或 PDF 原文。

**列表级盲区补查**（37 个目录分类 `/recent`，分页至各分类尽头，共 **4,979 条**，覆盖首发至 11-19 的公告批次）：39 条命中 = **22 条已收录** + **12 条与 API 扫描重合的本轮新增** + **5 条仅列表可见**——其中 [EgoJev（2611.24616）](https://arxiv.org/abs/2611.24616v1) 是融合式命名、对所有 API 查询不可见，**由列表检查独立发现并收录（相关）**；另 4 条为作者名含 "jev" 子串的误报（复现的 2611.17666 Timotijevic、2611.18998 Jevan Hutson、2611.19397 Stanojev，及新增的 2611.26531 Gligorijevic），经 id_list 摘要核实后只记日志不入台账。

**外部清单对照本轮不再全净**：awesome-jev-security 新列的三个 ID（2611.23683、2611.23947、2611.25435）均已在 API 扫描池内；awesome-system-one 新增 2605.19099 并在正文引用 2609.14973，两条均经核验后排除（见上）；awesome-jev 的三个窗口前 ID 与 awesome-decision-models 维持既定处置。

## 新增与阅读优先级

直接关系（15 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [MM-SystemOneBias](https://arxiv.org/abs/2611.26557v1)（security） | 吉林大学；KAUST；重庆大学 | 13 个多模态 System One 决策模型与骨干在六种成对干预下对比：七组匹配对中决策模型对选项标签、无关信息、评分量表全部更稳定，六组选项顺序翻转率更低；语义决策不变时概率仍移动 4.56–11.55 个点；托管 Jev（jev-1.14.0）为无匹配骨干的闭源参照。 |
| [VisualJevBench](https://arxiv.org/abs/2611.25435v1)（security） | 未署名单位 | 对 Visual Jev 的红队基准：800 张图像、3,200 道问题、四类攻击面；ABPS 借助类型化输出反馈搜索图像篡改，jev-1.14.0 上单图攻击成功率最高 69.6%，通用攻击在未见图像上平均 33.15%。 |
| [JEV vs. LLMs（钓鱼邮件）](https://arxiv.org/abs/2611.23683v1)（security） | 中央旁遮普大学；FAST；阿德莱德大学；扎耶德大学 | 1,500 封邮件上 Jev 1.13 对三个 LLM：准确率、精确率、召回率、F1 均最高，批处理时间、token、成本最低，Brier 与 ECE 最低；作者明言仍需进一步验证。 |
| [Whom Do AI Agents Serve?](https://arxiv.org/abs/2609.17989v4)（security） | 麦吉尔大学 Desautels 商学院 | 消费者委托的智能体惩罚赞助商品，把平台设为委托方即显著削弱该惩罚；跨模型复现含托管 Jev 1.14、Liquid D1-Ultra、Mercury Decide、Microsoft Decision 1、StartLux 27B；提示级缓解会过度修正，面向消费者的微调可消除偏置。 |
| [GLiDE](https://arxiv.org/abs/2611.26509v1)（architecture） | Fastino Labs | 0.4B–27B 单次前向决策模型：去掉因果掩码让上下文、问题、候选双向交互，多教师软标签蒸馏 + 参数无关的循环深度把推理压进一次前向；27B 版 Decision Index 73.37 分、ECE 2.1%。 |
| [What a Calibrated Probability Hides](https://arxiv.org/abs/2611.25168v1)（architecture） | MBZUAI；阿里巴巴；东北大学；南加州大学 | BGPO 让决策模型按「信念」分组预测选择分布并用贝叶斯法则分配奖励，区分群体间分歧与群体内不确定；四个基准上条件/最差组/总体 JS 散度最低。 |
| [Decision 1.0](https://arxiv.org/abs/2611.18629v1)（architecture） | vLLM Semantic Router 项目；AMD；微软；MBZUAI；麦吉尔大学 | 开放权重决策基础模型家族（六个模型，Choice/Noul/Score 接口）；Lux-9B 加权 77.22%，但 Jev 1.13.0 在总分、组合、阅读、迁移上领先且校准更好。 |
| [Clover-35B-A3B-Preview](https://arxiv.org/abs/2611.24636v1)（architecture） | DiffuSpace | 扩散语言模型技术报告中的决策模型一节：单次去噪联合回答至多八个相关问题，整组全对率 65.4% → 77.0%；以 Jev v1.13 为冻结 API 参照在 JevBench 与 Decision Index 上比较。 |
| [Keystone](https://arxiv.org/abs/2611.25530v1)（applications） | UIUC；NYU；CMU | 把文生图提示编译成类型化问题，让 Jev 1.14 在早期预览图上作答的免训练评判器；关键步搜索剪枝以不到一半计算量超过其他验证器的 best-of-8。 |
| [论证框架与 LLM 决策](https://arxiv.org/abs/2611.25361v1)（applications） | 中科院数学与系统科学研究院；中国科学院大学 | 四阶段论证框架流程在辩论决策与检索式事实核查上的设计研究；Qnt-Arg、Qlt-Arg 两个任务定制方法；决策模型（检索实验用 Jev）与生成模型的角色对比。 |
| [Auditable Clinical Support with Decision Agents](https://arxiv.org/abs/2611.23700v1)（applications） | 宾夕法尼亚大学；亚琛工业大学；德累斯顿工业大学；海德堡大学 | Decision2Care：Jev 1.13.0 为每个允许的 EHR 动作给概率、固定规则执行，全程不生成文本；546 份急诊记录诊断准确率 86.5%、单次检查 2.2 秒（对比 92–100 秒），每步可审计。 |
| [Stop Going in Circles（LoopRoute）](https://arxiv.org/abs/2611.25363v1)（agents） | 四川大学；华为 | Jev 默认执行、检测到状态—动作循环时由 LLM 短暂接管的免训练路由器；ALFWorld/MapReader/TextWorld 上较单独 Jev 平均提升 21.0%/60.1%/30.1%，成本远低于全程 LLM 控制。 |
| [Vanguard](https://arxiv.org/abs/2611.23917v1)（agents） | UIUC；CMU；NYU；东北大学 | 视觉语言智能体步级投机的免训练评判器：Jev（jev-1.13.0）看截图给每个候选步骤一次前向的正确概率；2B 起草模型至少与 8B 目标模型同样准。 |
| [Thinking Fast, Anywhere（AnyS1）](https://arxiv.org/abs/2611.23751v1)（agents） | 中国科学技术大学；南洋理工大学 | 把流程性技能变成通用决策点来源，训练单个校准 4B 指针 System-1；成本降 75–91%、模型调用时间降 63–92%，留出决策上超过商用 Jev（jev-1.14.0）且更省。 |
| [LLMs Are Already Confidence-Aware Zero-Shot Classifiers](https://arxiv.org/abs/2611.25289v1)（evaluation） | 谢菲尔德大学 | 11 个开源 LLM 上的置信度方法对比：logit 打分区分度最好（AUROC 0.74–0.77），「仅决策」打分减少 88–96% 解码步；最佳组合与参照 Jev 1.13.0 准确率、AUROC 相当，原始校准较差。 |

相关方法（10 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [Piccolo](https://arxiv.org/abs/2611.24651v1)（architecture） | 署名「Piccolo Team」，无单位行 | 0.8B–27B 多模态决策模型家族，模型与数据经递归自我改进共同演化；Piccolo-27B 登顶 Decision Index Vision Full（75.59）；骨干—配方协同适应重于骨干新旧，损失下降可能与决策准确率脱钩。 |
| [Jeveration](https://arxiv.org/abs/2611.24738v1)（architecture） | 新加坡国立大学 | System One 决策范式也能生成：冻结 Qwen3.5-4B，以共享随机状态协调并行预测，文生图/图生图/密集预测各一次前向，512×512 图像 78 ms。 |
| [Calibrated Decision Rewards（RLCDR）](https://arxiv.org/abs/2611.25135v1)（architecture） | FuturixAI Research | 把 LLM 变成决策模型作免参考的 RL 奖励：类型化问题、一次前向读概率、选项顺序去偏、百条标签校准；MATH500 从 72.2% 到 76.8%，追平用答案键训练。 |
| [EgoJev](https://arxiv.org/abs/2611.24616v1)（applications） | 哈佛大学 | 把 VLM 当作决策模型读其输出分布来选帧的免训练方法；QAEgo4D 准确率从均匀采样 51.2% 到 62.0%，单模型、可跑在手机上；融合式命名只被列表检查捕获。 |
| [Fast closed-loop STEM navigation](https://arxiv.org/abs/2611.23698v1)（applications） | 东京大学生产技术研究所 | 闭环电子显微镜导航的决策步：Typed Decision 直接读 VLM 候选标签概率，时延最短（0.13–0.21 秒）、导航成功率总体最高。 |
| [UEmo-D1](https://arxiv.org/abs/2611.24481v2)（applications） | 清华；江西财经大学；深圳北理莫斯科大学；光明实验室 | 首个多模态情绪识别决策模型，把多模态输入直接映射为候选分布；配套 97.7 万样本的 UEmo-Data，识别、时延、校准兼得。 |
| [A System 1 Decision Model for Medical MCQ](https://arxiv.org/abs/2611.23832v1)（applications） | Antz.ai | 冻结语言模型 + 两个投影头做医学选择题的单作者研究；最高 46.0%，作者明言只是廉价基线。 |
| [FinVeriQA](https://arxiv.org/abs/2611.25071v1)（applications） | 圣何塞州立大学 | 金融问答多智能体原型：Laya 路由、Python 算数、Mistral-7B 写作、代码校验器核对；校验必须独立于写作者看到的证据。 |
| [When Do Decision Models Help LLM-Driven Network Discovery?](https://arxiv.org/abs/2611.23947v1)（security） | 科奇大学；伊利诺伊高级研究中心（新加坡）；UIUC | Laya 决策门控把小网络端口召回率从 75.5% 提到 89.0% 并拦下蜜罐，但对前沿模型在早期增加时延。 |
| [System-One RSI](https://arxiv.org/abs/2611.26007v1)（agents） | 阿里巴巴 Token Foundry；中科院自动化所 | 27B 决策模型驱动 OODA 循环、推理智能体团队离线递归改进提示/决策树/参数；Snake 均分 1.30 → 7.35，《黑神话：悟空》进攻胜率 0% → 66.7%。 |

## 数据与核实

- 每条新增均经 Atom 元数据 + 摘要 + 定向全文核验；证据引文写入前逐条 assert 于摘要/PDF 原文，PDF 引文的章节位置按 LaTeXML 标题结构逐条定位核对。
- 代码核验：新增 9 个作者链接仓库（148 → **157**；GitHub API 确认公开）。RLCDR 声明的 rudransh2004/rlcdr 为将来时且核验时 404，不记录；医学选择题论文引用的 VizuaraAI/system-one-from-scratch 是参考文献而非论文发布的代码，不记录；Jeveration、BGPO、MM-SystemOneBias、Keystone、Vanguard、Decision 1.0 等论文内无作者代码链接。
- AnyS1 论文只印有项目页 middle-chunjie.github.io/AnyS1/，按既定先例映射到 github.com/middle-chunjie/AnyS1（API 确认公开且含代码包）。
- 未署名单位论文 22 → **24**：VisualJevBench（PDF 与 HTML 作者栏均无单位行）、Piccolo（署名仅「Piccolo Team」，正文只提到算力来自阿里 PPU 设备，项目页亦只写 AgentScope Team，均不构成单位声明，不予推断）。
- 版本：UEmo-D1 取最新 v2；委托方偏置研究取 v4（11-08 更新）。
- 待核实（pending）维持 2 条不变（2609.33609、2609.25498）。
- 11-20 及之后首发须下轮补扫（探针显示 11-20 批次尚未入索引）。
