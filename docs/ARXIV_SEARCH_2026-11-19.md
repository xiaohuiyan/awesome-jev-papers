# arXiv 第 19 轮检索（2026-11-19）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-19.md)

周四凌晨执行（01:42 UTC 起）：探针显示新窗口已见 **11-17 首发批次**（11-18 及之后尚未公告）。第 18 轮收尾时标注「11-17 起首发须下轮补扫」，本轮新窗口即取 11-17 至 11-19。按协议双窗口执行：新窗口四条常设查询加五个变体；**常设查询与变体全窗口重扫**（2026-09-15 起）共得 **419 条**去重记录，**10 条台账外**。合计 **10 个新候选：7 收录（4 直接、3 相关）、3 排除**。目录 393 → **400 篇**（243 直接、153 相关、4 奠基）；台账 566 → **576 条**（400 收录、174 排除、2 待核实）；主窗口右界延伸至 **2026-11-17**。

**全窗口重扫再回收一条截断边缘漏网记录**：[Deciding Without Pointing（2611.21995，11-16 首发）](https://arxiv.org/abs/2611.21995v1) 仅被 whole:`all:"decision model"` 命中——第 18 轮该查询 251 条总量下取最新 200 条，此记录正处截断边缘之外，延续第 17/18 轮已记录的 MMDM/LEASH/Beveridge/AdaMenu 同类问题，再次实证「下轮重扫可回收」。另两条全窗口新面记录经核验排除（见下）。新窗口侧，11-17 首发批次贡献 7 条中的 6 条（含 4 条直接）。

**直接关系核验要点**：[RagHarnessDebugger](https://arxiv.org/abs/2611.22991v1) 全文明写「Jev is a new general-form classifier from TypeSafe AI」（修复 harness 的决策组件）；[客服中心研究](https://arxiv.org/abs/2611.22949v1) §4 明写评测「the API-based closed JEV 1.13 (TypeSafe AI, 2026)」；[交通研究](https://arxiv.org/abs/2611.22926v1) 摘要即「systematically evaluate TypeSafe Jev and GPT-6 Luna Decisions」；[JevRSI](https://arxiv.org/abs/2611.22432v1) §4.1 明写「The decision models are Jev-1.14 (TypeSafe AI, 2026) and StartLux」且「All decision-model calls are uniformly priced using the TypeSafe Jev API」。[SlideJev](https://arxiv.org/abs/2611.22879v1) 为 Jev 范式接口（并行候选打分、无选项位置标签、支持/拒绝对数似然差），TypeSafe 仅现于文档引用——记「相关」；[SpecSearch](https://arxiv.org/abs/2611.22296v1) 的「Jev-based predictor」是冻结 Qwen3-4B + LoRA 自建选择器，同样记「相关」。

**三条排除**：[2611.22660](https://arxiv.org/abs/2611.22660v1)（双星共振锁定，astro-ph.SR）与 [2611.21681](https://arxiv.org/abs/2611.21681v1)（量子弛豫备注，quant-ph）的 `all:"System One"` 命中均为「system. One / system, one」相邻词伪短语；[2611.21895](https://arxiv.org/abs/2611.21895v1)（鸟类运动多智能体 DQN）的 `all:"decision model"` 命中系 arXiv 词干化（"decision modeling"→"model"），且属无类型化决策接口的泛决策建模——按既定规则排除。

**列表级盲区补查**（37 个目录分类 `/recent`，分页至各分类尽头，共 **5,184 条**，覆盖首发至 11-17 的公告批次）：41 条命中 = **31 条已收录** + **6 条与 API 扫描重合的本轮新增** + **4 条复现误报**（2611.13337、17666 及第 18 轮已核验的 18998 Jevan Hutson、19397 Stanojev）——**本轮列表检查未发现独立盲区**。SpecSearch 标题与列表块均无 token，不在命中之列，但已被 API 摘要查询捕获，无遗漏。

## 新增与阅读优先级

直接关系（4 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [RagHarnessDebugger](https://arxiv.org/abs/2611.22991v1)（agents） | 哈佛；伊利诺伊理工芝加哥肯特法学院；布塞里乌斯法学院 CLTDS；新加坡管理大学；斯坦福 CodeX；Bommarito Consulting；MIT | Jev 引导的智能体 RAG 修复 harness 全程留痕并审计：轨迹完整性、校验-候选对应、接受规则可达性；暴露 77%/76% 可用而未实现的修复缺口，修订后比 BM25 基线高 3.6/3.7 分、比全文参考还高 1.1/2.4 分（ContractNLI + 复现集）。 |
| [Can Decision Models Replace LLMs in Real-World Contact Center…](https://arxiv.org/abs/2611.22949v1)（evaluation） | Dialpad | 九个决策模型（含 API 闭源 JEV 1.13、Gemini-Decision-1、OpenJev、Clef）对十三个 LLM，八个客服场景零样本：分类多可追平前沿 LLM 且 API 闭源单价最低、高置信更准可选择性路由；最大短板是几乎不弃答，小模型裁判质量骤降且位置偏置更重。 |
| [When Do Typed Decision Models Work in Transportation?](https://arxiv.org/abs/2611.22926v1)（applications） | 香港理工；约翰霍普金斯；港科大；京东 iCity/智能城市 | 决策模型首次进交通：TypeSafe Jev 与 GPT-6 Luna Decisions 上 Swissmetro 出行选择不及离散选择模型与最强对话基线、随输入表示与问法大幅波动；闭环信号控制若干部场景与成熟控制器相当但难路网下降级，时延与成本显著更低。 |
| [Think Once, Act Fast (JevRSI)](https://arxiv.org/abs/2611.22432v1)（agents） | 港科大（广州）AI Thrust；LIGHTSPEED | System-1/2 分工：托管 Jev-1.14（另评 StartLux）做低时延动作选择，异步 System-2 LLM 递归改由过程/状态记忆/世界模型组成的模块化 harness，效用驱动检索选模块；三个数据集多个设置追平或超过 LLM 智能体，System-2 干预随 harness 成熟递减、成本摊薄。 |

相关方法（3 篇）：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [SlideJev](https://arxiv.org/abs/2611.22879v1)（applications） | 西安交大；中国医学科学院医学信息研究所；剑桥 | 全切片病理 VQA 的 Jev 决策接口：候选答案并行单独打分（冻结原 LM 头支持-拒绝对数似然差、无选项位置标签），门控更新视觉 token 同分数端到端训练；三基准最高平均准确率、四种选项顺序一致率 100%、正确图像增益最大。 |
| [SpecSearch](https://arxiv.org/abs/2611.22296v1)（applications） | 伊利诺伊大学厄巴纳-香槟分校 | 硬件感知投机解码配置搜索：解析成本模型 + 多 GPU 校准；再训 Jev 式预测器（冻结 Qwen3-4B + LoRA + 线性修正）在新 GPU 上免现场校准选配置；四款 GPU 上全校准 2.01×AR/1.36×SD（vLLM），预测器 1.30×SD、保留全校准吞吐 97.36%。 |
| [Deciding Without Pointing](https://arxiv.org/abs/2611.21995v1)（evaluation） | 米兰理工 | 案例研究：决策模型判断出异常时知道在哪吗？Clef-flash 检测不均衡（MVTec AD 0.924 / MVTec AD 2 0.668），决策头路由注意力像素 AUROC 仅 0.391、遮住图像 token 检测不变；骨干注意力换问法即低于中心先验、去文本即低于随机；按区域提问/重训/读骨干可部分恢复定位，均不及专用少样本定位器。 |

## 数据与核实

- 每条新增均经 Atom 元数据 + 摘要 + 定向全文核验；证据引文写入前逐条 assert 于摘要/PDF 原文。
- 代码核验：新增 2 个作者链接仓库（usail-hkust/JevRSI、leowu-ai/SlideJev，GitHub API 确认公开，146 → **148**）；RagHarnessDebugger 声明仓库 rag-harness-debugger 核验时 404（"will become available"），按第 18 轮 TDM-Gauntlet 先例不记录。
- 未署名单位论文维持 22 篇（本轮 7 篇均有单位）。
- 待核实（pending）维持 2 条不变（2609.33609、2609.25498）。
- 11-18 及之后首发须下轮补扫（探针显示 11-18 批次尚未公告）。
