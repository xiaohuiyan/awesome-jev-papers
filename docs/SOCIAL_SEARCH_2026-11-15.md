# X / 中文平台检索（2026-11-15）

[中文目录](../README.zh-CN.md) · [English catalogue](../README.md) · [查询与线索台账](../data/social-search-2026-11-15.json) · [同日 arXiv 第 15 轮](ARXIV_SEARCH_2026-11-15.md)

检索窗口：**2026-11-13 至 2026-11-15**（自 11-13 第 14 轮以来的空档日），另加无日期补充查询与 [Jev Daily](https://jevdaily.com) 逐期直达。论文首次提交日期以 arXiv 记录为准，与帖子/文章日期分开处理。

**本轮社媒线索独立新增 0 篇。** X 交叉检索 surfaced 四个新 ID——[2611.15576](https://arxiv.org/abs/2611.15576v1)（Jev 调查模拟）、[2611.15777](https://arxiv.org/abs/2611.15777v1)（SO-Arena）、[2611.16321](https://arxiv.org/abs/2611.16321v1)（自适应计算）与 [2611.17167](https://arxiv.org/abs/2611.17167v1)（决策模型三角色）——**四者均被同日 arXiv API 扫描独立捕获**，收录归功计入扫描轮（与第 13 轮 EarthJev 的处理相反，那次社媒先于 API 独立发现）。本轮社媒自身的台账贡献是 1 条排除：[Ask2Decide（2611.13015）](https://arxiv.org/abs/2611.13015v1)（LLM 智能体向人提问的澄清基准，无 Jev/System One/类型化决策内容，标题中的 Decisions 指人类规划决策）。

## 本轮社媒新增

无。检索与结果全部记录在 [JSON 台账](../data/social-search-2026-11-15.json)。

| 平台 | 检索与读取 | 结果与限制 |
| --- | --- | --- |
| 微信公众号 | `site:mp.weixin.qq.com` 带日期查询。 | 11 月日期查询 0 命中（微信文章索引不全，不能据此断言无新内容）。周边生态项：谷歌免费档决策模型、OpenAI 100ms「快脑」Decisions API（10-23）、上海AI实验室**书生·明决**（见下）。 |
| 知乎 | `site:zhihu.com Jev 决策模型 System One`（带 11 月日期）。 | 专栏仍集中于 2026 年 9-10 月，11 月无新专栏；新非论文项：JevLite（Qwen3-4B 复现帖，64.5ms/决策）与 Mobius/ONNX 本地部署教程。 |
| 新浪微博 | `site:weibo.com Jev 决策模型 论文`。 | 科普长文与融资新闻无变化；无新论文线索。 |
| X / Twitter（交叉） | `Jev decision model arxiv new paper November 13 14 15 2026`、AIM-Decision、SO-Arena、Actor-Judge-Teacher、Agentic RAG、Prism 等定向核查。 | 四个新 ID 均与 API 扫描重合；AIM-Decision 系 AIMultiple 分析师报告（非论文）；「Can Decision Models Speed Up Agentic RAG」解析为 Medium 工程文（49.73→18.67 秒）；Rohan Paul 对 2611.17167 的推文串与新闻稿「AI model that's bad at a task can still train another AI」为同一论文的报道。X 原生搜索不可达，依赖网页索引。 |
| Jev Daily（聚合站） | 直达 `issues/2026-11-13`（已发布）、`/2026-11-14`（已发布）。 | 两期**无论文**：11-13 期（100 智能体 gym 图谱、Slack 智能体用 Jev 做应答闸门、Ulmer 将 Gemini Decisions 加入 HotdogBench——Jev 仍领先）；11-14 期（Browser Use 1.0.4 降至 $0.45/任务、Allie the Icon 的 Jev 批量「预测性提问」模式）。 |

## 新增非论文线索

| 线索 | 来源与时间 | 处理理由 |
| --- | --- | --- |
| **书生·明决 / Intern-Decision**（上海AI实验室） | 微信生态报道 + shlab.org.cn 官方新闻（09-28 开源） | 0.8B/2B/4B 开源多模态决策模型，宣称性能超 Jev；**未找到 arXiv 技术报告**——与 Prism、Vega、JEV-27B-VL、Gemini Decisions 同列观察线索。注意 Intern-Decision-4B 已在本轮收录的两篇论文中被评测（[NESTONE](https://arxiv.org/abs/2611.16321v1)、[漏洞挖掘 harness](https://arxiv.org/abs/2611.16565v1)）。 |
| AIM-Decision（AIMultiple） | X 交叉检索；报告更新于 10-05 | 独立分析师基准「Jev vs Kev vs LLMs」（Jev 1.14 得 56.6，$0.036/千次决策）；非 arXiv 记录。社区 fork（Oscar-dzy/Awesome-jev-papers）收录了它。 |
| Corpus2Skill / DecisionRAG | Medium（generativeai.pub），约 11-13 | Jev 接入智能体 RAG 的端到端实测（200 问题、6,221 文档，平均延迟 49.73→18.67 秒）；工程博客非论文。 |
| JevLite / Mobius ONNX | 知乎专栏 | 社区复现与本地部署教程；非论文。 |

遗留观察线索（Sarvam Prism——11-03 发布、开源 105B 底座、25 模型测速第一，但仍无论文；Vega、JEV-27B-VL、Smaug-Audio-Decisions、alphaXiv 4B、Gemini Decisions）本轮均未解析到新 arXiv 记录，继续保留。

## 覆盖与来源限制 / Coverage

- 三条中文平台与 X 均无法登录检索，使用网页搜索 `site:` 查询与聚合站直达；查询与结果全部记录在 [JSON 台账](../data/social-search-2026-11-15.json)。
- 「From Questions to Decisions」检索出现 Sarvam Prism 假线索：聚合源把 2611.13563 当作 Prism 报告，实际是无关的边缘 NPU 基准论文；Prism 至今只有博客与权重。
- Jev Daily 11-13/11-14 期为人工读取；聚合站缺论不等于当日无论文——当日新论文以 [arXiv 第 15 轮](ARXIV_SEARCH_2026-11-15.md)的 API 扫描为准。
- 本轮没有建立任何论文的社媒原帖证据链；0 独立新增指社媒渠道的收录归功，不代表当日没有新论文。
