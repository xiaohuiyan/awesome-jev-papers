# arXiv 第 21 轮检索（2026-11-24）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询记录](../data/search-log.json) · [筛选台账](../data/screening.json) · [同日社媒检索](SOCIAL_SEARCH_2026-11-24.md)

周二凌晨执行（01:43 UTC 起，arXiv API 一度连续 429/重定向循环，最后一个查询改走 https 直连后重试成功）：探针显示**搜索索引尚未到达 11-21**（新窗口 11-21..11-24 的四条常设查询加五个变体全部 0 命中，属合法空窗——第 15 轮记录的模式），但全窗口重扫（2026-09-15 起，常设查询不设取回上限）正常执行。共得 **493 条**去重记录，**1 条台账外**；API 侧 37 分类列举网（11-19..11-24，**1,762 条**）发现**分类浏览索引已包含 11-21 首发批次（151 条）**——两个索引更新不同步，列举网因此成为本轮唯一的「新鲜」入口，又贡献 **3 个候选**。合计 **4 个新候选：4 收录（均为相关方法）、0 排除**；收尾复核再补 1 收录（直接）、2 排除（见文末）。目录 435 → **440 篇**（267 直接、169 相关、4 奠基）；台账 618 → **625 条**（440 收录、183 排除、2 待核实）；主窗口右界延伸至 **2026-11-21**。

**全窗口计数与上轮收尾对比**：`all:"Jev"` 259（少 1：**已编目的 2609.30186 在 v2（11-20 更新）中改名**——"Jev-Mobile: Jev as an Executor for Mobile GUI Agents" → "ScopeAct: Scoping Decision Models for Reliable Multi-Step Execution in Mobile GUI Agents"，标题与摘要均不再含 Jev 字样，故不再被查询命中；按版本政策条目保持 pin 在已审阅的 v1，更名记入 CHANGELOG）；`all:"decision model"` 286（多 1）、`all:"decision models"` 287（多 1）——增量即下述 11-20 迟公告尾巴 2611.27910；`all:"System One"` 120、`all:"typed decision"` 86、`all:"System 1"` 67、`all:"System-One"` 120、`all:MedJev` 2、`all:JevBench` 8 均无台账外记录。

**收录四条（均经全文核验，未使用托管 Jev）**：

| 论文 | 单位 | 一句话 |
| --- | --- | --- |
| [Decision Columns as an Index](https://arxiv.org/abs/2611.27910v1)（applications） | 微软 | 用「决策列」构建可解释嵌入：每列存决策模型（微软 Decision 1）对一条自然语言问题的校准答案（是/否/未提及），相似度精确分解到每问、新问题只增坐标；WDC/STaRK 上统计追平稠密候选生成，小型 MLP 以约 1/200 成本回填语料。 |
| [Decision models for UAVBench](https://arxiv.org/abs/2611.28331v1)（evaluation） | InferLink Corporation | UAVBench 2,000 题上 Mac 评测 24 种配置：开放权重决策模型 H2O Lightning 4B 全场最高 77.65%（高于基准原作者托管测的 Gemini 2.5 Flash），但部署到 Qualcomm RB3 边缘板全部遇到转换/运行时限制；明言不评测商业 Jev。 |
| [Where the Image Sits](https://arxiv.org/abs/2611.28535v1)（security） | 中国科学院香港创新研究院 | Jev 式单次 prefill 读出对图文顺序敏感：本地 7 个开源 VLM 检查点上后缀放置翻转 41.0% 决策、降 18.6 个点，曲线单调非 U 形；P+Q 两次前向平均读出至少与前缀同准。全文未调用托管 Jev。 |
| [LoopSeek](https://arxiv.org/abs/2611.28635v1)（agents） | 弗吉尼亚理工；得克萨斯大学奥斯汀分校 | 长视频问答把证据搜索交给 System I（冻结 OneJev-4B + 三个 LoRA 适配器的四个角色智能体，纯概率输出、零文本生成）、System II（冻结 Qwen3-VL-8B）只答一次：五个基准平均准确率 53.5 → 63.9，GPU 时间比智能体式方法少 32–80%。 |

**相关关系依据**（逐篇全文核查）：Decision Columns 的应答模型是微软 Decision 1（MD1）与 gpt-6-luna，全文 0 处 Jev；UAVBench 论文原文明言「we do not evaluate the commercial Jev model itself」，评测对象为 GLiDE 0.4B/0.8B、Liquid d1 2B、H2O Lightning 4B；Where the Image Sits 在本地检查点（Qwen3-VL、Idefics3、LLaVA 系）上研究 Jev 式读出范式，Visual Jev/PixelJev 仅作引文；LoopSeek 的 System I 底座是 OmniJev 的开源 OneJev-4B，Jev 博文仅作范式出处。按既定边界（同 Laya 底座论文、SpecSearch、SlideJev）四条均记相关。

**列表级盲区补查**（API 侧，37 个目录分类，11-19..11-24，2 次不设限请求共 **1,762 条**：11-19 计 869、11-20 计 742、11-21 计 151）：19 条命中 = 14 条已编目/已入台账 + **3 个新候选**（上表后三条）+ **3 条作者子串误报**——2611.28356 Engram 与 2611.26531（作者名 Gligorijevic）、2611.26827（作者名 Stanojev，复现误报），经 id_list 摘要核实均无 Jev/System One/决策模型 token，只记日志不入台账。11-20 尾部两条（2611.28331、2611.28356）首发于 11-20 但公告滞后到本轮（ID 落在 2611.28xxx 段），第 20 轮当日的 480 条列举网因此未见过它们——迟公告尾巴与迟索引同属一个现象。

**版本漂移**：53 条已编目论文在本轮池中以比 pin 版本更新的 arXiv 版本重新出现（第 20 轮为 49 条；新增含 2609.30186 的 v2 改名）。按既定政策条目保持 pin 至逐条复审，其中 2609.30186 的更名已在本报告开头单独说明。

**收尾复核与同日补录**（见文末「收尾补录」）：本轮执行期间索引仍在移动（搜索索引追赶 11-21 批次），按第 20 轮流程在文档与渲染完成后重跑常设查询，又得 3 条台账外记录——1 篇收录（直接）、2 条排除。

首轮无排除条目；代码仓库零新增（Where the Image Sits 摘要声称公开的 Youzhi333/Visual_Tex_Order_Bias_Jev 审阅时 404，按 VX-One/TDM-Gauntlet 先例不记录）。

## 收尾补录（索引继续更新后）

首次渲染完成约两小时后复核，发现 arXiv 搜索索引在本轮执行期间已开始消化 **11-21 首发批次**（新窗口探针从 0 变为 `all:"Jev"` 1 条、`all:"decision model"` 2 条；全窗口 `all:"decision models"` 287→289、`all:"decision model"` 286→288、`all:"System One"` 120→122、`all:"System 1"` 67→69、`all:"Jev"` 259→260——`Jev` 的 +1 是本轮已收录的 2611.28535 进入搜索索引）。与扫描池、目录、台账比对后得到 **3 条台账外记录**：

- **[When to Test, Repair, or Regenerate: Decision-Guided Efficient RTL Generation](https://arxiv.org/abs/2611.28667v1)（11-21 首发，cs.AR）收录（直接）**：东南大学、港科大、谢菲尔德。RTL 生成流程把调度权交给专用决策模型——基础配置即托管 Jev（「The harness uses a specialized evaluator (Jev in our base configuration)」），并与 OpenAI Decisions API、通用 DeepSeek 裁判在选择性提前停止上对比；初始决策分数分配「修复 vs 重新生成」预算，Jev 缺陷假设打分（每类错误一个，示例 12 个）排序修复方向，最终选择按决策模型分数排列通过测试的候选；MAEDA 上的 Jev 式错误类别初评 macro-F1 86.01%。以 DeepSeek 为生成器，三个基准平均 Pass@1 +5.4–7.1 个点、估计总推理成本 −11.0–14.3%。项目页仓库 2002-Pan/Decision-Guided-RTL 经 GitHub API 验证（描述与标题吻合），代码记入（159→160）。
- **2611.28146 "Close the Loop on the Retrievability Gap"（11-19 迟公告，排除）**：`all:"System One"` 命中为相邻词伪短语——「picks the less retrievable of two systems one time in three」；全钢影像恢复/检索性研究，无类型化决策接口。
- **2611.28029 "Safety Systems Watch What the Model Says, Not What the Child Says"（10-06 首发、极迟入索引，排除）**：`all:"System 1"` 命中为相邻词伪短语——「10 attribute the relevant condition to the system, 1 to the user」；儿童安全分类学审计（NeurIPS 2026 workshop），无类型化决策内容。两条排除的触发短语均先逐字核实于摘要原文。

当日合计：**5 收录（1 直接、4 相关）、2 排除**。目录 435 → **440 篇**（267 直接、169 相关、4 奠基）；台账 618 → **625 条**（440 收录、183 排除、2 待核实）。11-21 批次在收尾复核时仅部分进入搜索索引（探针仍见大量空窗），**下轮必须从 11-21 起重扫**。
