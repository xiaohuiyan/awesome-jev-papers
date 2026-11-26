# arXiv 第 22 轮检索（2026-11-26）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-26.md)

周四凌晨执行（01:42 UTC 起）：探针显示**搜索索引已达 11-24**（第 21 轮结束时仅部分入索引的 11-21 批次已完整可见，且 11-22..11-24 三个首发批次全部落地），新窗口 11-21..11-26 的四条常设查询加五个变体直接命中 **36 条**去重记录；全窗口重扫（2026-09-15 起，全部不设取回上限）再收 6 条此前各轮漏网的迟索引尾巴。共得 **531 条**去重记录，**33 条台账外**；API 侧 37 分类列举网（11-21..11-26，**2,546 条**，其中 11-25/11-26 尚无记录——周四查询时这两个首发日还未公告）又补 **2 个候选**（PixelOne 经标题 VideoJEV 融合名、Clinical3D-Bench 经摘要 JEV token——融合名盲区类，与 EarthJev/EEGJev 同类）。首过合计 **35 个新候选：31 收录（12 直接、19 相关）、4 排除**；收尾复核再补 **3 收录（2 直接、1 相关）**（见文末）——全天 **38 个候选：34 收录（14 直接、20 相关）、4 排除**，第 20 轮（35 篇）以来最大单轮。目录 440 → **474 篇**（281 直接、189 相关、4 奠基）；台账 625 → **663 条**（474 收录、187 排除、2 待核实）；主窗口右界延伸至 **2026-11-24**。

**全窗口计数与上轮收尾对比**：`all:"Jev"` 273（+13）、`all:"decision model"` 311（+23）、`all:"decision models"` 312（+23）、`all:"System One"` 130（+8）、`all:"System-One"` 130（+8）、`all:"typed decision"` 91（+5）、`all:"System 1"` 73（+4）、`all:JevBench` 10（+2）、`all:MedJev` 2（持平）——增量全部来自 11-22..11-24 批次与迟索引尾巴，无更名/掉 token 记录。收尾复核时索引继续移动：`all:"Jev"` 273→**274**、`all:"decision model"` 311→**314**、`all:"decision models"` 312→**315**（其余不变）。

**收录十二条（直接，均经全文核验使用或评测了托管 Jev）**：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [OmniDecisionBench](https://arxiv.org/abs/2611.28924v1)（evaluation） | 吉林大学 | 45 个数据集（192,975 条）、五能力族十二角度的多模态 System One 全景基准：托管 Jev 1.14（80.14% 准确率、4.50% ECE15）对比 JEV-27B-VL、d3-27B 与两款通用 VLM；仅渲染选项就把 Jev 1.14 选择性风险放大近三倍，供体数据集估的风险阈值难迁移。 |
| [Decision Models: An Introduction and Capability Evaluation](https://arxiv.org/abs/2611.32368v1)（evaluation） | 北京航空航天大学 | 类型化决策服务入门评测：11 种配置（含托管 JEV jev-1.14.0、StartLux Instant）在 9 套任务、1,000 条中英文案例上测准确率/有效性/延迟；StartLux Instant 95.3% 总体、0.084 秒中位延迟，最高配置 97.1%。 |
| [Triage Accuracy of Jev](https://arxiv.org/abs/2611.31012v1)（evaluation） | DOCYET；夏里特医学院；帝国理工；莱普哈纳大学 | 16 个决策模型（14 开放权重 + gpt-6-luna-decisions 与 jev-1.14，经 OpenRouter 调用）在 233 合成 + 10,000 真实症状案例上共 163,728 次评估：最佳模型合成分诊 72.1%、与既有算法一致率 56.1%，早期急症识别 AUROC 0.87。 |
| [Reducing Order Sensitivity](https://arxiv.org/abs/2611.31174v1)（architecture） | 康奈尔大学 | 十个开闭源决策模型（明确含 TypeSafe Jev 与 OpenAI Decisions API）上顺序敏感性普遍、随选项数放大并在多步决策中级联；系统对比八种缓解方法，树形注意力（选项作共享上下文并行分支）出奇有效且推理低廉。 |
| [Seeing Is Locating / GeoDecisions](https://arxiv.org/abs/2611.30564v1)（evaluation） | 新南威尔士大学；港科大（广州） | 决策模型的空间感知与地理偏见基准：六个决策模型（对比表含 Jev-1.14）对日常照片与卫星图像——空间感知离不开视觉、纯文本坐标不够；决策模型 + 地点先验的训练无关方法改善感知而不明显加重偏见。 |
| [The Control-Flow Tax](https://arxiv.org/abs/2611.32365v1)（agents） | Talkdesk | 智能体「决定做什么」占基线成本 42.5%：托管 Jev 控制有限动作、Sol 生成文档的异构架构在四任务 480 次运行上全面最低成本与耗时，初始任务成本降 49.6%、耗时降 33.2%。 |
| [SOARS](https://arxiv.org/abs/2611.32917v1)（agents） | 滑铁卢大学；汤森路透实验室；圭尔夫大学 | 深度搜索智能体每步用托管 Jev 做快速校准重排（$0.042/百万输入 token、输出免费）：六个 LLM 底座上持续提升准确率与证据召回、减少搜索调用与端到端延迟，BrowseComp-Plus 上把 GPT-5.4 Mini 从 73.9% 提到 84.7%。 |
| [DKnown-Jev-2](https://arxiv.org/abs/2611.31056v1)（applications） | 北京财智科技 | 文章级「答案-证据」分类器，一次前向跨全段落预测：972 条人工标注测试集上 91.77% 准确率、91.28% 宏 F1，表格实测超托管 Jev 2.16/2.37 个百分点（Jev 89.61%/88.92%）、领先 OpenAI Decision 约 8 个点。 |
| [GitHub Actions Workflow Smell Detection](https://arxiv.org/abs/2611.31421v1)（applications） | 北卡州立；巴西三所联邦大学 | 定义驱动的工作流坏味检测：Jev 1.13 与 GPT Decisions（闭源）、Tev1 4B（开放）按自然语言坏味定义打分，1,710 对验证样本上 Jev 1.13 阈值 0.5 时 79.69% micro-F1、选阈值后 85.43%；0.675 秒延迟、全基准 $0.22 API 费。 |
| [Disclosure Bias in AI Reviewers](https://arxiv.org/abs/2611.30410v1)（evaluation） | （无单位行） | 只改 150 篇 ICLR 2027 投稿的 AI 使用声明（最多九版），六位 AI 审稿人（Jev 1.13.0 + 五个 LLM）共 23,652 份评审：声明「AI 做全部工作」时全员降分；「AI 研究智能体」对 Jev、Sonnet、Argon 显著降分，Jev 细粒度期望评分下多拒 77%。 |
| [UUBench](https://arxiv.org/abs/2611.30157v1)（evaluation） | 大湾区大学、港科大（广州）等 15 家 | 全双工多模态交互的「未说出口意图」基准：面向过程的评分把意图满足锚定在可听可见线索上，**托管 Jev 作评分器**按固定原语标签逐项打分，九个系统 216 共享输入对比；定位 v0.1 预览版。 |
| [Don't Sleep, Keep Watch / NightWatch](https://arxiv.org/abs/2611.28947v1)（agents） | 新加坡国立；A*STAR CFAR；商汤；香港浸会大学 | 计算机操作智能体的连续感知：0.8B System-1 监视器流式盯屏（0.25 秒/次），基线含像素规则与 Jev API 监视器（0.59 秒/次）、远比 D3-27B（7.6 秒）便宜；代码/模型/数据开源。 |

**收录十九条（相关方法，均经全文核验未使用托管 Jev）**：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [DeciForm](https://arxiv.org/abs/2611.29340v1)（architecture） | 东南大学；北京中关村学院；昆山杜克大学 | 把答案空间结构做进决策模型：无候选查询 + 隔离候选分支保重排一致，log-spherical 目标 + 十进制前缀读出统一选择/判断/打分，Qwen 与 ModernBERT 双底座三类指标齐升。 |
| [EEGJev](https://arxiv.org/abs/2611.32100v1)（applications） | 东北大学（日本） | 脑电版「换问题换任务」：一次前向为候选答案打分，19 个公开 EEG 源六种问题类型；固定记录换属性问题，13 个测试源标签选择 99.70%（均匀 49.20%），95 分位响应快于 NeuroLM。 |
| [EEG-Jev](https://arxiv.org/abs/2611.31875v1)（applications） | 中科院深圳先进院；东南大学；哈工大；深理工等 | CHOICE/NOUL/SCORE 三类 typed 读出的统一脑电单次前向模型，一个检查点联合训练、35 个公开源留出评估（运动想象 54.08%、睡眠分期 70.45%、癫痫检测 AUROC 0.825、疼痛评分 MAE 1.700）。 |
| [MolReJev](https://arxiv.org/abs/2611.28965v1)（applications） | 新加坡国立大学 | Jev 式候选打分 + 上下文学习的分子预测：检索相似标注示例、一次前向联合打分，对 Kev 检查点与自训模型都有增益，覆盖留出任务与训练外分子。 |
| [AdaptRouter](https://arxiv.org/abs/2611.30162v1)（architecture） | 北航；北京中关村学院；东北大学；北理工 | 策略学习训练的自适应路由器：紧凑多模态决策模型（StartLux/JevAny 式，均 0.8B）读专家卡片按原生反馈选冻结专家，新任务免回放、新专家以卡片接入，质量优先优势可证不让成本压倒质量。 |
| [Voyag](https://arxiv.org/abs/2611.30253v1)（applications） | 零束科技 | 车载语音的单次前向决策模型：mmBERT 编码器 + 逐槽 typed 选择头 + 轻量关系头，联合预测十个意图槽与共现意图对的三值执行关系（并行/顺序/互斥）。 |
| [JevBench（Feng）](https://arxiv.org/abs/2611.31533v1)（evaluation） | （无单位行） | 无金标签的概率自洽测试：50 条蜕变关系覆盖改写/取反/合并/换选项/换批次五个维度，12,000 项测试；21 个自托管开放 Jev 兼容模型（48M–9.7B）自洽分 56.5–83.9，可加性违例常见；托管 Jev 不在受测之列。 |
| [Taxi](https://arxiv.org/abs/2611.31457v1)（applications） | Rival Research | 百万步级智能体调试/聚类/监控系统：聚类生成分类法 + SQL 问答 + 编码智能体混合流水线，实验性接入 Jev 式决策模型做低成本语义路由与评估（明言指接口而非仅 TypeSafe 原版）。 |
| [Needwise](https://arxiv.org/abs/2611.31175v1)（applications） | Adobe | 零生成的对话推荐：每轮一次类型化请求把消息映射到目录字段并更新既有需求，按「必须优先」分层排序，每个分数分解为具名需求判定（支持/矛盾/未知）。 |
| [S1Arena-MM](https://arxiv.org/abs/2611.29773v1)（evaluation） | 得克萨斯大学奥斯汀分校 | 51,060 道多模态决策题 + 102 个截图闭环游戏（实时模式下游戏不等模型）：33 个开放模型（OneJev、Jev-Omni、d3、Clef 等 System-1 家族对 MLLM 底座）同题同概率评分，思考反而抬高多数 MLLM 的 Brier 分。 |
| [CORE](https://arxiv.org/abs/2611.30096v1)（calibration） | 高丽大学 | 「A 或 B」平均比 A+B 少 11.5 个点：视觉决策模型次可加性在 0.85B–26B 全规模出现且标签微调不消；一致重分组训练把总变差距离从 14.8 降到 5.8 点（最佳基线 9.4）。 |
| [Layer-Level Control](https://arxiv.org/abs/2611.29519v1)（architecture） | 华为（经通讯邮箱域名推断） | 把中间状态与层级执行控制暴露给智能体运行时：调度器选「全词表下一 token 与全深度预测一致」的最省算力动作（继续/退出/拼接），5,000 条类型化决策项训练、公开 JevBench v1.2 子集评估。 |
| [Legal Is Not Good / hexfolk](https://arxiv.org/abs/2611.28713v1)（evaluation） | 独立研究者（特伦托） | 预注册协议下低成本智能体玩全新极简 4X 游戏：确定性引擎、不纠错的裁判、逐决策日志；8B/3B 开放语言模型全败给几行规则玩家，低成本决策模型同样不佳；引擎/协议开源。 |
| [JevNavAgent](https://arxiv.org/abs/2611.28766v1)（agents） | 复旦大学 | 千兆病理切片的 Jev 范式导航：2B 参数、因子化停止/候选/确认头一次前向出分布，确定性代码执行导航，轨迹级 RL 在线训练；Clean Visual WSI-VQA 多尺度 51.57%。 |
| [NavDecision](https://arxiv.org/abs/2611.28796v1)（agents） | 中科院自动化所；北京科技大学；北邮 | 视觉-语言导航的并行多步动作预测（PMAP）+ 记忆增强自参照策略优化（M-SRPO）：共享视觉-语言状态一次出多步动作分布，OmniJev/Qwen3.5-4B 底座，更低延迟报告领先结果。 |
| [Antares-Smaug](https://arxiv.org/abs/2611.31347v1)（security） | 英特尔 | 对六个开放 Laya 决策模型的黑箱攻击目录（81 种程序化改写 × 566 条）：未见过的攻击措辞在已发布模型上赢 59% 条目，点名选项的句子被否定仍能带偏（32%）；净化器漏掉未见泛化。 |
| [Training decision models for simulating human respondents](https://arxiv.org/abs/2611.31613v1)（applications） | 麦吉尔大学 | 硅基抽样校正：KEV 决策模型在历史受访者级选择微数据上做事前选择训练（条件极大似然、不碰目标研究数据），四个留出研究处理效应误差降 22–89%，小模型胜过大 LLM。 |
| [Clinical3D-Bench](https://arxiv.org/abs/2611.32094v1)（evaluation） | 中国科学技术大学；A*STAR；温州医科大学 | 医院空间推理基准（373 间病房、3,368 题、答案由 3D 场景计算、十位医师审核）：35 个 MLLM 最佳仅 45.7%/53.6%（医师 79.0%）；在 Clinical3D-45K 上微调开放 VideoJev-4B 达 73.9%。 |
| [PixelOne](https://arxiv.org/abs/2611.30235v2)（architecture） | 复旦大学；京东；上海创新研究院 | GUI 定位单次前向原生分辨率点击：搜索教师用 VideoJEV 文本-选项打分器选行选列逐步放大，学生继承参数经空间蒸馏 + 框监督，推理时决策头选 token、像素头在其内定点。 |

**排除四条（均逐字核验触发短语后入台账）**：2611.31955（矩阵-向量复杂度理论；摘要相邻词「solving linear **systems, one**-sided methods」——已知逗号式相邻词类）；2611.31462（生成音乐分布分析；摘要相邻词「these **systems one** prompt at a time」——无标点变体，新记录一例）；2611.31319（GBDT 反事实追索；arXiv 词干把「automated decision models」匹配给 `all:"decision model"`）；2611.30188（WAM 置信校准/System 2 接管框架；「decision step」为机器人控制通用语，全文 0 个 Jev/类型化决策 token，同 2609.32591/2609.24170 先例）。

**作者子串误报（记日志不入台账）**：2611.28986（CLASP）与 2611.32823（FORA）均因作者 Teodora **Spasojevic** 触发融合名检查，经 id_list 摘要核实无任何 Jev/System One/决策模型 token——Stanojev、Gligorijevic 之后又一姓氏类（-jevic 结尾），该检查的已知第五、六例。

**代码仓库**：7 个作者链接经 GitHub API 验证收录（NightWatch、DeciForm、S1Arena-MM、GeoDecisions、EEGJev、EEG-Jev、hexfolk；EEG-Jev 经项目页 neuroimglab.github.io/EEG-Jev/ 映射，canonical 大小写 NeuroImgLab/EEG-Jev 以 API 为准）。两个声称仓库审阅时 404 按先例不记录：OmniDecisionBench 的 Glax147/OmniDecisionBench（「will be available」）、Control-Flow Tax 的 Czk0712/Workflow_routing（「upon publication」）；CORE 项目页标注「Code soon」亦无仓库。

**版本漂移**：57 条已编目论文在本轮池中以比 pin 版本更新的 arXiv 版本重新出现（第 21 轮为 53 条），按既定政策条目保持 pin 至逐条复审。

**覆盖说明**：周四查询时 11-25/11-26 首发日尚未公告（列举网亦无记录），下一轮须自 11-25 起重复覆盖。

## 收尾补录（索引继续更新后）

首次渲染完成后按第 20/21 轮流程重跑九条常设+变体查询（不设上限、新缓存目录），与扫描池、目录、台账三方比对，发现索引在本轮执行期间继续移动（与第 20/21 轮同型的 ~2 小时滞后），新增 **3 条台账外记录，全部收录**——赶在首次 push 之前处置，保住单次提交：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [General-Purpose Decision Models for AI Configuration Tuning](https://arxiv.org/abs/2611.33190v1)（applications） | 伦敦国王学院 | 托管 Jev 在八个 AI 调优任务上充当优化器/性能预测器/区域引导器：前两种角色不敌传统方法（8 比 6、7 任务），但区域引导找到比原生调优器困惑度更低的配置——首次提交 11-15、索引迟至本轮的又一条 straggler。 |
| [Searching Ultra-Long Videos with Decision Models / DeLoVi](https://arxiv.org/abs/2611.33368v1)（agents） | 北卡罗来纳大学教堂山分校 | 预训练决策模型从超长视频检索证据：像 LLM 一样把问题与候选证据一起读、但零文本生成直接出相关性分；默认打分器即托管 Jev，消融换 Decider/Drex Max/OpenJev（57.4/57.5/57.6/51.4）；代码 CeeZh/DeLoVi 已验证收录。 |
| [Lost in Translation, Not in Confidence](https://arxiv.org/abs/2611.33307v1)（evaluation） | 南洋理工；新加坡国立；VinUniversity | 25 个开放权重决策模型在 14 种语言、17 个任务上对英语平行对比：全员掉点（高资源 ~2 点、泰米尔语 8 点）而置信度只掉一半；损失由语言与底座决定、与榜单排名无关，81 组微调也关不上缺口。 |

收尾计数：目录 **474 篇**（281 直接、189 相关、4 奠基）；代码仓库 167 → **168**；台账 **663 条**（474 收录、187 排除、2 待核实）。
