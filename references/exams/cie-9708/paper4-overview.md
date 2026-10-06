# CIE 9708 Paper 4（A Level Data Response and Essays）：真题索引总览

登记日期 2026-10-06（审核轮）。数据文件：同目录 `9708-P4.questions.json`；考纲条目：`spec-items.json`（键 `9708`）与 `syllabus-a-level.md`；分卷说明：`9708-P4.coverage.part1.md`（2023–2024，审核前写成）与 `9708-P4.coverage.part2.md`（2025）。本文件的统计与表格由 `work/p4audit/scripts/overview.py` 生成，审核脚本与新下载文件见 `work/p4audit/`。

## 0. 收录范围与缺口

**收录**：2023 年新考纲首考（F/M 2023）至 O/N 2025 的全部 Paper 4 卷号，共 23 个卷号、115 条题目记录、185 个小问行。其中 3 个卷号与同季 /41 完全相同（2023-06 /43、2024-06 /43、2025-06 /43：QP、MS 文本逐词比对一致，PER 两节也逐词一致），记录照抄 /41 内容、出处写各自文件。下面的统计把同卷只算一次：**20 份不同试卷、100 道题、161 个小问行**。

| 考季 | 卷号 | QP | MS | 考官报告（PER） |
|---|---|---|---|---|
| 2023-03 | 42 | Drive | Drive | 有，pp.8–10 |
| 2023-06 | 41 | GitHub 镜像（本轮新增） | GitHub 镜像（本轮新增） | 有，pp.21–22 |
| 2023-06 | 42 | Drive | Drive | 有，pp.23–24；另有 ECR |
| 2023-06 | 43 | GitHub 镜像（本轮新增，=/41） | GitHub 镜像（本轮新增，=/41） | 有，pp.25–26（=/41） |
| 2023-11 | 41 | GitHub 镜像（本轮新增） | GitHub 镜像（本轮新增） | 有，pp.23–24 |
| 2023-11 | 42 | Drive（文章正文因版权删除） | Drive | 有，pp.25–26 |
| 2023-11 | 43 | GitHub 镜像（本轮新增） | GitHub 镜像（本轮新增） | 有，pp.27–29 |
| 2024-03 | 42 | Drive | Drive | **缺** |
| 2024-06 | 41 | GitHub 镜像（本轮补 QP） | Drive | 有，pp.24–25 |
| 2024-06 | 42 | Drive | Drive | 有，pp.26–28 |
| 2024-06 | 43 | GitHub 镜像（本轮新增，=/41） | GitHub 镜像（本轮新增，=/41） | 有，pp.29–30（=/41） |
| 2024-11 | 41 | Drive | Drive | **缺** |
| 2024-11 | 42 | GitHub 镜像（本轮补 QP） | Drive | **缺** |
| 2024-11 | 43 | GitHub 镜像（本轮新增） | GitHub 镜像（本轮新增） | **缺** |
| 2025-03 | 42 | Drive（文章大部分因版权删除） | Drive | 有，pp.8–10 |
| 2025-06 | 41–44 | Drive（/41、/43、/42 文章部分删除） | Drive | **缺** |
| 2025-11 | 41–44 | Drive | Drive | **缺** |

考季的卷号清单有官方依据：grade thresholds 2023-03（12/22/32/42）、2023-06、2023-11、2024-03（12/22/32/42，本轮从 GitHub 镜像取得，原先“未核实”的 2024-03 只有 /42 由此证实）、2024-06（41/42/43，/41 与 /43 分数线相同）、2024-11、2025-03、2025-06、2025-11，副本在 `src/9708-ER/gt/`。

**本轮新增来源**：公开 GitHub 仓库 `Upppllld/OpenPastPapers`（commit `6db0095`，HEAD 在 2026-10-06 仍是这一提交），路径 `as-and-a-level-economics-9708/9708_<季>_<qp|ms|gt>_<卷>.pdf`，经 raw.githubusercontent.com 下载。该仓库此前的 finder 轮已记入 `inventory/github-candidates.json`，但两轮 Paper 4 建索引都没有用到。每个文件都核对了封面卷号与考季、页脚（如 `9708/43/O/N/23`），文本用 `pdftotext -layout` 抽取；14 份 QP/MS 与 4 份 grade thresholds 复制到 `src/9708-P4/` 与 `src/9708-ER/gt/`，md5 前缀记在 `work/p4audit/provenance.md`。

**仍然缺的（所有可达来源都没有）**：

- **2026-03 9708/42、2026-06 9708/41–44**：已发布。WebSearch 可见 pastpapers.co 的 2026 March 页面与 `9708 Economics June 2026 Mark Scheme 42.pdf` 等链接，但该站经代理返回 `CONNECT tunnel failed, response 403`；physicsandmathstutor 同样被拦；Drive（标题 `m26`/`s26`、全文 `9708/4x/F/M/26`、`9708/4x/M/J/26` 等）没有；OpenPastPapers 只到 2025-11。用之前先补这两季。2026-11 尚未开考。
- **PER**：2024-03、2024-11、2025-06、2025-11（以及 2026 年各季）缺。Drive 上的 `9708_s24_er.pdf`、`9708_w24_er.pdf`、`9708_s25_er.pdf` 是 PapaCambridge 网页存档，不是报告；OpenPastPapers 也没有这几份。这些考季的 `er` 字段为空（共 60 条记录）。
- **Specimen Paper 4（9708/04，2023 起）的 QP**：只有 specimen MS 与 Specimen Paper Answers（`src/9708-P4/2023-SP_*`），不属于正式考季，未入索引。

**审核记录（本轮）**：

1. 合并 part1（40 条）与 part2（45 条）为 85 条，无重复 id；字段、id 格式、考季格式、每题 20 分、小问分值之和、spec id 均通过脚本校验（`merge_validate.py`）。
2. 独立复核：脚本逐份比对 Section A 各小问分值与 QP 方括号分值、MS 表头分值（全部一致）；核对每条记录所引 QP/MS 页确实含该题（`page_check.py`）；核对每条 `er` 所引 PER 页落在对应卷号的章节内并提到该题（`er_check.py`，88 处引用）；所有单引号引文在 MS/PER/QP 原文中逐字找到且不超过 25 词（`quotes.py`，150 处）；essay 命令词与 MS 题干一致。
3. 人工逐条对原文复核 25 条（覆盖 2023-03 至 2025-11 每个考季、Section A 与 essay、part1 与 part2）：2023-03/42 Q1、Q3；2023-06/42 Q1、Q4；2023-11/42 Q1、Q2、Q4；2024-03/42 Q1、Q5；2024-06/41 Q1；2024-06/42 Q3；2024-11/41 Q1；2024-11/42 Q1、Q4；2025-03/42 Q1；2025-06/41 Q1、Q2；2025-06/42 Q1、Q3、Q4；2025-06/44 Q1；2025-11/41 Q1、Q4；2025-11/42 Q1；2025-11/43 Q1；2025-11/44 Q1。分值、MS 要点、ER 转述、终点要求均与原文相符，图形读数（2023-03 Fig. 1、2024-11/41 Fig. 1.1）与渲染图一致，2025-06/44 1(d) 的 MS 算术错误已在记录中注明。没有发现成片错误。
4. 修正 4 处考纲映射：2023-06/42 Q4 主考点由 AS 6.4.5 改为 11.2.5（6.4.5 保留为次要）；2024-11/42 1(b) 主考点由 AS 1.5.3 改为 9.2.1（问的是生产潜力）；2025-11/42 Q2 主考点由 7.3.1 改为 8.1.1（题目要评价两项政府政策）；2023-11/42 1(d) 增加 8.1.1（政府直接提供）。
5. 完整性：发现 6 个卷号（2023-06 /41、/43，2023-11 /41、/43，2024-06 /43，2024-11 /43）与 2 份 QP（2024-06/41、2024-11/42）可从 GitHub 镜像取得却未收录。已全部补入：新写 20 条（2023-06/41、2023-11/41、2023-11/43、2024-11/43），照抄生成 10 条（2023-06/43、2024-06/43），并用新 QP 重写 2024-06/41 与 2024-11/42 第 1 题的材料摘要、更新 10 条记录的 `sources.qp`。`inventory/9708-gaps.md`、`9708-P4.coverage.part1.md` 中“缺失”的说法已过时，以本节为准。

## 1. 真题需求概览

### 1.1 卷面结构与分值惯例

- **Section A**（第 1 题，20 分，数据题）：一篇 1–2 页的新闻材料加表或图，4 个小问（有时带 (i)(ii)，2025-11/44 为 5 行）。分值大体递增，最后一问的分值分布：5 分×1 份；6 分×1 份；7 分×4 份；8 分×13 份；10 分×1 份。出现过的分值组合：2/4/6/8×3；3/3/6/8×3；4/4/4/8×2；2/5/6/7×2；3/5/6/6×1；3/6/6/5×1；3/5/5/7×1；5/4/3/8×1；4/2/6/8×1；3/6/3/8×1；2/4/4/10×1；3/4/6/7×1；5/2/5/8×1；4/2/1/5/8×1。
- **Section B**（第 2、3 题选一）微观，**Section C**（第 4、5 题选一）宏观，每题 20 分、不分小问：AO1 知识与理解＋AO2 分析共 14 分（Table A：L1 1–5、L2 6–10、L3 11–14），AO3 评价 6 分（Table B：L1 1–3、L2 4–6），见 1.5 C1。按主考点所在 topic 计：第 2 题 topic 7×11、topic 8×9；第 3 题 topic 7×12、topic 8×8；第 4 题 topic 9×9、topic 10×5、topic 11×6；第 5 题 topic 9×3、topic 10×1、topic 11×16。
- **命令词**：Section A 小问 Explain 26、Consider 12、Assess 10、Analyse 8、Evaluate 5、Identify 5、Describe 4、Distinguish 4、Define 2、Discuss 2、State 1、Is there evidence 1、Comment 1；essay Evaluate 54、Assess 17、Consider 5、To what extent 3、Explain 1。80 篇 essay 中 24 篇的题干含 always／only／automatically／equally／all／fully／ideal／most effective 一类绝对化用词，评价就是检验这个词。
- **图**：essay 题干要求图的，2023-11 起的 MS 几乎都印了 AO1/AO2 封顶（见 1.5 C2）；2023-03、2023-06/42 的 MS 没印封顶，但 PER 同样说无图不能进 L3（见 1.6 W2）。Section A 要求图的小问，图本身通常占 2–3 分（标注与坐标轴、曲线、移动或均衡点）。

### 1.2 按考纲条目：考频与问法

计数口径：20 份不同试卷。“主考点”＝该小问 `spec` 的第一个 id；“涉及行数”＝出现在任一位置的次数（一个 essay 算一行）。命令词取小问的第一个命令词。AS 条目（topics 1–6）在 Paper 4 中只作“已知前提”，列在本节末尾。

#### 7.1 边际效用

边际效用理论只以 essay 出现：问它能否“完全解释”价格与需求量的关系（2024-11/42 Q2）或能否解释“所有商品”的市场需求曲线（2025-11/44 Q2，要图）。终点：由 MU=P／等边际原则推出个人需求曲线、再加总成市场需求曲线，评价落在理性与效用可度量的假设上（7.1.5）。题目点名 indifference curve 时改写边际效用会被限在 Level 1（PER 2023-11 p.26，2023-11/42 Q2）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.1.1** definition and calculation of total utility and marginal utility | 1／1 | – | 1 | Evaluate 1 | 2025-11/44 Q2 |
| **7.1.2** diminishing marginal utility | 0／2 | – | 2 | Evaluate 2 | – |
| **7.1.3** equi-marginal principle | 0／2 | – | 2 | Evaluate 2 | – |
| **7.1.4** derivation of an individual demand curve | 1／3 | – | 3 | Evaluate 3 | 2024-11/42 Q2 |
| **7.1.5** limitations of marginal utility theory and its assumptions of ratio... | 0／2 | – | 2 | Evaluate 2 | – |

#### 7.2 无差异曲线

无差异曲线三季三考，全是 Section B essay：推导正常品与劣等品的需求曲线（2023-11/42 Q2）、价格上涨对正常品与 Giffen 品需求的不同影响（2024-06/41 Q3，题目要求 IC 图）、价格变化如何改变个人需求（2025-06/41 Q2）。终点：IC＋预算线图，价格效应分解为替代效应与收入效应；2025-06/41 MS 写明两种效应都要分析才能进 Level 3，无图最高 L2（8 分）。评价点：理性假设、两商品世界、偏好会变、静态分析。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.2.1** meaning of an indifference curve and a budget line | 1／3 | – | 3 | Evaluate 2、Assess 1 | 2025-06/41 Q2 |
| **7.2.2** causes of a shift in the budget line | 0／3 | – | 3 | Evaluate 2、Assess 1 | – |
| **7.2.3** income, substitution and price effects for normal, inferior and Gif... | 2／5 | – | 5 | Evaluate 4、Assess 1 | 2023-11/42 Q2；2024-06/41 Q3 |
| **7.2.4** limitations of the model of indifference curves | 0／3 | – | 3 | Evaluate 2、Assess 1 | – |

#### 7.3 效率与市场失灵

效率定义多在 Section A 拿分：2025-11/44 1(a) 4 分（allocative：生产消费者想要的、P=MC；productive：最少资源、AC 最低点；也收“在 PPC 上”）；2023-06/41 1(d) 两个定义各 2 分＋垄断图 3 分＋结论 1 分。essay 里它是评价尺度：完全竞争是否“理想”（2023-11/42 Q3）、无政府干预能否达到效率（2025-06/44 Q2，无图 L2 8）、长期均衡为何代表效率与什么阻碍效率（2024-06/41 Q2）。dynamic efficiency（7.3.4）从未单独设问，但 11 次作为替垄断/合并辩护的评价点出现。market failure 定义：2024-03/42 1(a) 2 分定义（价格机制没计入全部成本收益→配置无效率）＋1 分判断文章是否显示市场失灵；essay：“market failure exists in all economies”（2024-06/42 Q2）、“政府干预是唯一办法”（2025-11/41 Q2）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.3.1** definitions of productive efficiency and allocative efficiency | 3／16 | 5（8、4、10、4、8） | 11 | Evaluate 8、Assess 2、Explain 2、Consider 2、Is there evidence 1、Discuss 1 | 2024-03/42 Q1(b)；2025-06/44 Q2；2025-11/44 Q1(a) |
| **7.3.2** conditions for productive efficiency and allocative efficiency | 0／11 | 3（8、10、4） | 8 | Evaluate 4、Assess 3、Explain 2、Discuss 1、Consider 1 | – |
| **7.3.3** Pareto optimality | **未考** | – | – | – |  |
| **7.3.4** definition of dynamic efficiency | 0／11 | 4（8、4、8、8） | 7 | Evaluate 6、Assess 2、Consider 2、Is there evidence 1 | – |
| **7.3.5** definition of market failure | 3／6 | 1（5） | 5 | Assess 2、Evaluate 2、Identify 1、Consider 1 | 2024-03/42 Q1(a)；2024-06/42 Q2；2025-11/41 Q2 |
| **7.3.6** reasons for market failure | 0／7 | 2（5、5） | 5 | Assess 2、Evaluate 2、Identify 1、Explain 1、Consider 1 | – |

#### 7.4 外部性

外部性是 Section A 最常考的图题，也是 Section B 政府干预 essay 的底座。定义题 2–4 分：“由第三方承担的成本”（2025-11/44 1(b)(i)；2023-06/41 1(b) 要求举生产外部性的例子，只写消费外部性最高 3 分）。图题 5–10 分：MPC／MSC／MPB(=MSB) 正确标注、外部性或福利损失、Q* 与 Q（2025-06/42 1(d) 10 分逐点给分；2025-11/44 1(b)(iii) 5 分要说出产量由 Q 降到 Q1、价格由 P 升到 P1；2023-11/42 1(b) 6 分图要说明过度消费）。生产外部性与消费外部性的图要分清：航空是消费外部性，画成生产外部性导致图与分析都不准（PER 2023-03 p.9，2023-03/42 Q2）。7.4.6（信息不对称、道德风险）与 7.4.7（成本收益分析）至今未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.4.1** definition and calculation of social costs (SC) as the sum of priva... | 1／5 | 5（4、6、10、2、5） | – | Explain 4、Discuss 1 | 2025-06/42 Q1(d) |
| **7.4.2** definition and calculation of social benefits (SB) as the sum of pr... | 0／1 | 1（10） | – | Discuss 1 | – |
| **7.4.3** definition of positive externality and negative externality | 3／4 | 3（4、6、2） | 1 | Explain 3、Assess 1 | 2023-06/41 Q1(b)；2023-11/42 Q1(b)；2025-11/44 Q1(b(i)) |
| **7.4.4** positive and negative externalities of both consumption and production | 1／17 | 7（4、6、4、10、8、7、1） | 10 | Evaluate 7、Assess 5、Explain 2、Comment 1、Discuss 1、Identify 1 | 2025-11/44 Q1(b(ii)) |
| **7.4.5** deadweight welfare losses arising from positive and negative extern... | 1／13 | 3（6、10、5） | 10 | Evaluate 6、Assess 4、Explain 2、Discuss 1 | 2025-11/44 Q1(b(iii)) |
| **7.4.6** asymmetric information and moral hazard | **未考** | – | – | – |  |
| **7.4.7** use of costs and benefits in analysing decisions (knowledge of net ... | **未考** | – | – | – |  |

#### 7.5 成本、收益与利润

成本收益条目多是辅助：internal economies of scale 定义 3 分须含 long run 与 average cost（PER 2024-06 p.26，2024-06/42 1(a)）；minimum efficient scale 的含义与是否达到（2024-06/42 1(b)，“very few had a clear idea”）及 essay“总需求与 MES 如何决定市场结构”（2023-06/42 Q3）；分工如何降低平均成本 3 分（2025-06/44 1(b)）。利润类型：超额利润是否“总是”企业存续所必需（2024-06/42 Q3）、超额／亏损利润是否只出现在短期且只在完全竞争（2025-11/44 Q3）、垄断竞争长期只有正常利润（2025-06/44 1(c)，图 3 分）。收入与利润的计算（7.5.8、7.5.10）、短期成本函数与长期生产函数（7.5.2、7.5.3）在 Paper 4 未出现。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.5.1** short-run production function | 0／1 | 1（3） | – | Explain 1 | – |
| **7.5.2** short-run cost function | **未考** | – | – | – |  |
| **7.5.3** long-run production function | **未考** | – | – | – |  |
| **7.5.4** long-run cost function | 2／2 | 1（3） | 1 | Evaluate 1、Consider 1 | 2023-06/42 Q3；2024-06/42 Q1(b) |
| **7.5.5** relationship between economies of scale and decreasing average costs | 0／4 | 2（3、3） | 2 | Evaluate 2、Explain 2 | – |
| **7.5.6** internal and external economies of scale | 1／8 | 4（3、8、3、8） | 4 | Evaluate 4、Explain 2、Consider 2 | 2024-06/42 Q1(a) |
| **7.5.7** internal and external diseconomies of scale | 0／1 | – | 1 | Evaluate 1 | – |
| **7.5.8** definition and calculation of revenue: total, average and marginal ... | **未考** | – | – | – |  |
| **7.5.9** definition of normal, subnormal and supernormal profit | 2／3 | 1（6） | 2 | Evaluate 2、Consider 1 | 2024-06/42 Q3；2025-11/44 Q3 |
| **7.5.10** calculation of supernormal and subnormal profit | **未考** | – | – | – |  |

#### 7.6 市场结构

7.6.4（不同市场结构下企业的表现）是 Paper 4 微观主考点第一：11 次作主考点，2023–2025 的 9 个考季中有 8 个考到（只有 2024-03 没有）。essay 常见句式是给一个绝对化判断让考生评价：寡头合谋导致高价低效（2023-03/42 Q3）、完全竞争最理想（2023-11/42 Q3）、垄断竞争“总是”价更低更有效率（2023-11/43 Q3）、寡头能否避免价格竞争且长期保有超额利润（2025-03/42 Q2，折弯需求曲线、博弈论、价格领导）、政府应否干预垄断（2025-06/42 Q2，无垄断图最高 L2 8）、可竞争性提高对消费者与生产者的影响（2025-11/43 Q2）、竞争程度是否“只”由进入壁垒决定（2025-11/41 Q3，至少两种结构且要图）。Section A：识别市场结构并画长期图（2025-06/44 1(c)，分析对但市场结构判错最多 5 分）、描述农户与贸易商两种结构的差异（2025-11/42 1(c)，结构判错则特征分不给）、垄断是否有效率（2023-06/41 1(d)，8 分）。图的硬性要求：MC 穿过 AC 最低点、利润最大化在 MR=MC（PER 2023-06 p.21；PER 2024-06 p.27）。concentration ratio 只考过一次：含义 2 分＋算法 2 分（2023-06/41 1(a)）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.6.1** perfect competition and imperfect competition: monopoly, monopolist... | 3／10 | 3（4、6、6） | 7 | Evaluate 6、Explain 1、Assess 1、Consider 1、Describe 1 | 2025-06/44 Q1(c)；2025-11/41 Q3；2025-11/42 Q1(c) |
| **7.6.2** structure of the listed markets as explained by number of buyers an... | 0／5 | 2（6、6） | 3 | Evaluate 3、Consider 1、Describe 1 | – |
| **7.6.3** barriers to entry and exit | 0／5 | 1（4） | 4 | Evaluate 4、Distinguish 1 | – |
| **7.6.4** performance of firms in different market structures | 11／20 | 6（4、8、4、8、6、8） | 14 | Evaluate 11、Assess 3、Consider 3、Describe 1、Is there evidence 1、Explain 1 | 2023-03/42 Q3；2023-06/41 Q1(c)；2023-06/41 Q1(d)；2023-11/42 Q3；2023-11/43 Q3；2024-06/41 Q2；2024-11/43 Q1(c)；2025-03/42 Q2；2025-06/42 Q2；2025-11/43 Q2；2025-11/44 Q1(c) |
| **7.6.5** definition and calculation of the concentration ratio | 1／1 | 1（4） | – | Explain 1 | 2023-06/41 Q1(a) |

#### 7.7 企业增长

企业增长：合并 essay（政府允许同业两家大企业合并，2023-11/41 Q3：须认出 horizontal integration→垄断，无相关图限 L2）、收购是否可取（2025-06/41 Q3）；Section A 横向与纵向一体化各给一个好处，定义 1＋好处 1（2025-11/42 1(b)）。卡特尔与委托代理只作 essay 次要点。7.7.2（内部增长：有机增长与多元化）未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.7.1** reasons for different sizes of firms | 0／1 | 1（8） | – | Consider 1 | – |
| **7.7.2** internal growth of firms: organic growth and diversification | **未考** | – | – | – |  |
| **7.7.3** external growth of firms – integration (mergers and takeovers) | 3／3 | 1（4） | 2 | Evaluate 2、Explain 1 | 2023-11/41 Q3；2025-06/41 Q3；2025-11/42 Q1(b) |
| **7.7.4** cartels | 0／2 | – | 2 | Evaluate 2 | – |
| **7.7.5** principal–agent problem arising from differing objectives of shareh... | 0／1 | – | 1 | Evaluate 1 | – |

#### 7.8 企业目标与定价

定价与企业目标：价格歧视 essay（2023-06/41 Q3，“总是”有利于生产者而损害消费者与社会？须写条件、至少一个模型，多用三级价格歧视）；由利润最大化改为销售最大化对价格与产量的影响（2024-11/41 Q3）；limit pricing 与 predatory pricing 的区别 4 分及文中证据 2 分（2024-11/43 1(a)）；折弯需求与 PED 和收益的关系作 essay 次要点（2025-03/42 Q2）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **7.8.1** traditional profit-maximising objective of firms | 0／3 | – | 3 | Assess 2、Evaluate 1 | – |
| **7.8.2** an understanding of other objectives of firms | 1／3 | 1（4） | 2 | Evaluate 2、Describe 1 | 2024-11/41 Q3 |
| **7.8.3** price discrimination – first, second and third degree | 1／1 | – | 1 | Assess 1 | 2023-06/41 Q3 |
| **7.8.4** other pricing policies | 2／3 | 2（4、2） | 1 | Distinguish 1、Explain 1、Evaluate 1 | 2024-11/43 Q1(a(i))；2024-11/43 Q1(a(ii)) |
| **7.8.5** relationship between price elasticity of demand and a firm’s revenue | 0／1 | – | 1 | Evaluate 1 | – |

#### 8.1 政府对市场失灵的干预

8.1.1 是 Section B 的固定题型：20 份试卷里 11 次作主考点（10 篇 essay＋2023-11/42 1(c)），2024-06、2025-03、2025-06 以外每季都有“用图评价政府用某政策纠正某市场失灵”：航空外部性（2023-03/42 Q2）、电动车两项政策（2023-06/42 Q2）、撤销教育补贴（2023-06/41 Q2）、医疗全部私营（2023-11/41 Q2）、污染该多大程度依赖市场力量（2023-11/43 Q2）、用价格机制应对气候变化（2024-03/42 Q2）、两项减外部性政策（2024-11/41 Q2）、间接税（2024-11/43 Q2）、IMF/世界银行要求的私有化（2024-11/42 Q3）、交通拥堵两项政策（2025-11/42 Q2）；Section A 也考过新加坡配额与 ERP 哪个更有效（2023-11/42 1(c)，“两者各有优点”拿不到最后 1 分）。终点：外部性／税／补贴图，逐项政策分析，再逐项评价（PED、税额难定、监管成本、累退性、时滞），以结论比较各方案。8.1.2（政府失灵）从未作主考点，但 10 次作为评价点。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **8.1.1** application and effectiveness of measures to tackle different forms... | 11／22 | 5（6、5、4、8、5） | 17 | Evaluate 10、Assess 6、Consider 3、Explain 2、Is there evidence 1 | 2023-03/42 Q2；2023-06/41 Q2；2023-06/42 Q2；2023-11/41 Q2；2023-11/42 Q1(c)；2023-11/43 Q2；2024-03/42 Q2；2024-11/41 Q2；2024-11/42 Q3；2024-11/43 Q2；2025-11/42 Q2 |
| **8.1.2** government failure in microeconomic intervention | 0／10 | – | 10 | Assess 4、Evaluate 4、Explain 1、Consider 1 | – |

#### 8.2 公平、效率与贫困

公平与贫困全在 Section A：equity 与 equality 的定义或区分 2–3 分（2023-11/42 1(a)、2023-11/43 1(a)、2024-03/42 1(c)(i)、2025-11/43 1(b)(i)），equity＝fairness 是必拿点（PER 2023-11 p.25：约一半考生不知道）；应用题 8 分要对消费者和生产者分别判断 equity 与 equality（2024-03/42 1(c)(ii)）。absolute 与 relative poverty 3 分（2024-06/41 1(b)，可用 poverty line 或世界银行定义）、2 分（2025-11/41 1(a)，MS 写明“Do not credit minimum wage”）。再分配政策 8 分：一项供给侧＋一项财政政策，各 1 例＋2 发展＋1 联系到收入分配（2024-06/41 1(d)）。8.2.2（公平与效率）与 8.2.4（贫困陷阱）未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **8.2.1** difference between equity and equality | 5／6 | 6（3、3、3、8、8、2） | – | Distinguish 2、Consider 2、Explain 1、Describe 1 | 2023-11/42 Q1(a)；2023-11/43 Q1(a)；2024-03/42 Q1(c(i))；2024-03/42 Q1(c(ii))；2025-11/43 Q1(b(i)) |
| **8.2.2** difference between equity and efficiency | **未考** | – | – | – |  |
| **8.2.3** distinction between absolute poverty and relative poverty | 2／3 | 3（3、6、2） | – | Distinguish 1、Consider 1、Explain 1 | 2024-06/41 Q1(b)；2025-11/41 Q1(a) |
| **8.2.4** the poverty trap | **未考** | – | – | – |  |
| **8.2.5** policies towards equity and equality, for example | 1／2 | 2（8、8） | – | Consider 1、Assess 1 | 2024-06/41 Q1(d) |

#### 8.3 劳动市场

劳动市场是 Section B 的第二大题型（2024 年起除 2024-06 外每季至少一篇 essay）：工会进入完全竞争劳动市场是否“总是”提高工资并增加失业（2024-03/42 Q3）、买方垄断劳动市场的有效最低工资（2025-03/42 Q3）、完全竞争工资是否“总是”高于买方垄断（2024-11/43 Q3）、劳动生产率上升在两种市场的影响（2025-06/42 Q3，没分析 productivity 最高 L2 10，只写一种市场或无图最高 L2 8）、MRP 理论能否“总是”解释工资差异（2025-06/44 Q3）、CEO 工资为员工 100 倍（2025-11/42 Q3）、劳动供给在完全竞争与买方垄断中的重要性（2025-11/43 Q3，两种市场都要写才进 L3）。Section A：劳动市场供求图（2024-06/42 1(c) EV 转型对内燃机车工人；2025-11/41 1(b) 移民流出→劳动供给左移→工资上升，无图最多 3 分）、工资差异（2024-11/42 1(c)，MPP/MRP 与供给弹性）。终点：买方垄断图（MCL 在 ACL/S 之上，MRP=MCL 定雇佣量，工资读在供给曲线上）；把买方垄断题画成完全竞争图“invariably led to weak analysis”（PER 2025-03 p.9）。transfer earnings 与 economic rent（8.3.10）只作次要点一次。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **8.3.1** demand for labour as a derived demand | 0／1 | 1（6） | – | Analyse 1 | – |
| **8.3.2** factors affecting demand for labour in a firm or an occupation | 0／3 | – | 3 | Evaluate 2、Assess 1 | – |
| **8.3.3** causes of shifts in and movement along the demand curve for labour ... | 2／2 | 1（6） | 1 | Analyse 1、Assess 1 | 2024-06/42 Q1(c)；2025-06/42 Q3 |
| **8.3.4** marginal revenue product (MRP) theory | 2／7 | 1（6） | 6 | Evaluate 3、Assess 3、Analyse 1 | 2025-06/44 Q3；2025-11/42 Q3 |
| **8.3.5** factors affecting the supply of labour to a firm or to an occupation | 1／7 | 1（6） | 6 | Evaluate 4、Assess 2、Analyse 1 | 2025-11/43 Q3 |
| **8.3.6** causes of shifts in and movement along the supply curve of labour t... | 1／4 | 3（6、5、7） | 1 | Analyse 1、Explain 1、Consider 1、Assess 1 | 2025-11/41 Q1(b) |
| **8.3.7** wage determination in perfect markets | 0／6 | 1（5） | 5 | Assess 3、Evaluate 2、Explain 1 | – |
| **8.3.8** wage determination in imperfect markets | 3／8 | 1（4） | 7 | Evaluate 4、Assess 3、Describe 1 | 2024-03/42 Q3；2024-11/43 Q3；2025-03/42 Q3 |
| **8.3.9** determination of wage differentials by labour market forces | 1／3 | 1（6） | 2 | Analyse 1、Evaluate 1、Assess 1 | 2024-11/42 Q1(c) |
| **8.3.10** transfer earnings and economic rent | 0／1 | – | 1 | Assess 1 | – |

#### 9.1 国民收入与乘数

乘数：Section A 4–5 分，乘数理论 2 分＋结合材料 2 分（2024-11/41 1(b)）、政府借债增支→收入、产出、就业、乘数（2023-03/42 1(b)）；essay 要求注入—漏出（J/W）图分析降息对就业（2025-06/42 Q4：无 J/W 图最高 L2 8，泛泛谈货币政策也是 L2 8，写财政或供给侧不给分）。AD 构成多在 Section A 宏观影响题里（2024-06/42 1(d) 对两国分别判断）。充分就业均衡只在 essay 次要点出现（2025-11/41 Q5“增长只能在低于充分就业时发生”）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **9.1.1** the multiplier process | 3／12 | 5（5、8、4、8、6） | 7 | Evaluate 5、Assess 3、Analyse 1、Consider 1、To what extent 1、Explain 1 | 2023-03/42 Q1(b)；2024-11/41 Q1(b)；2025-06/42 Q4 |
| **9.1.2** components of Aggregate Demand (AD) and their determinants | 1／7 | 6（6、8、8、6、6、7） | 1 | Consider 2、Analyse 2、Assess 2、Evaluate 1 | 2024-06/42 Q1(d) |
| **9.1.3** full employment level of national income and equilibrium level of n... | 0／3 | – | 3 | Evaluate 2、Assess 1 | – |

#### 9.2 增长

9.2.1 涉及次数全卷第一（23 行）：PPC 图区分实际增长与潜在增长（2023-06/42 1(b)：实际＝PPC 内一点移向边界，潜在＝PPC 外移；图不准确最多 3 分）、资源开发对潜在增长（2024-11/41 1(a)，PPC 或 LRAS 外移）、移民停止与退休对生产潜力（2024-11/42 1(b)，MS：移民停止 PPC 不变，退休 PPC 内移）、实际增长定义＝实际 GDP 在一段时间内的百分比变化（2023-11/43 1(b)）；essay：如何提高潜在增长（2025-06/44 Q5）、增长是否只能在低于充分就业时发生（2025-11/41 Q5）。产出缺口：财政政策填补负产出缺口（2023-11/43 Q4，要图）、滞胀（2025-06/41 Q4，无图最多 8 分）。衰退定义 3 分：与 GDP 相关、负增长、连续两个季度，缺一扣一（2023-03/42 1(a)；PER 2023-03 p.8）。可持续增长定义 2 分：“不损害后代满足其需要的能力”＋材料中的例子（2025-06/42 1(a)）。inclusive growth 只作次要点一次。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **9.2.1** actual growth versus potential growth in national output | 7／23 | 13（4、8、6、5、5、7、4、4、8、6、6、7、7） | 10 | Evaluate 10、Consider 4、Explain 3、To what extent 2、Assess 2、Define 1、Analyse 1 | 2023-06/42 Q1(b)；2023-11/43 Q1(b)；2023-11/43 Q1(c)；2024-11/41 Q1(a)；2024-11/42 Q1(b)；2025-06/44 Q5；2025-11/41 Q5 |
| **9.2.2** positive and negative output gaps | 1／4 | 1（5） | 3 | Assess 2、Evaluate 2 | 2023-11/43 Q4 |
| **9.2.3** business (trade) cycle | 2／2 | 2（3、6） | – | State 1、Consider 1 | 2023-03/42 Q1(a)；2023-11/41 Q1(c) |
| **9.2.4** policies to promote economic growth and their effectiveness | 2／7 | 3（8、7、7） | 4 | Evaluate 4、Analyse 1、To what extent 1、Consider 1 | 2023-11/43 Q1(d)；2024-06/41 Q4 |
| **9.2.5** inclusive economic growth | 0／1 | 1（8） | – | Assess 1 | – |
| **9.2.6** sustainable economic growth | 4／10 | 7（8、8、3、2、4、4、7） | 3 | Evaluate 4、Assess 2、Explain 1、Define 1、Comment 1、Discuss 1 | 2025-06/41 Q1(c)；2025-06/42 Q1(a)；2025-06/42 Q1(b)；2025-06/42 Q1(c) |

#### 9.3 就业与失业

失业条目大多是次要点：structural unemployment 与 natural rate 是否相同（2025-06/41 1(a) 3 分：自然失业率包括结构性与摩擦性，所以不同）；货币政策能否有效解决失业（2023-11/41 Q4，最适合周期性失业）；财政政策影响失业率（2025-06/41 1(b)）；增长与失业的关系看趋势不看单点（2023-11/43 1(b)；PER 2023-11 p.27）。9.3.3（自愿与非自愿失业）未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **9.3.1** definition of full employment | 0／1 | – | 1 | Evaluate 1 | – |
| **9.3.2** equilibrium and disequilibrium unemployment (including hysteresis) | 0／1 | 1（3） | – | Explain 1 | – |
| **9.3.3** voluntary and involuntary unemployment | **未考** | – | – | – |  |
| **9.3.4** natural rate of unemployment | 1／2 | 1（3） | 1 | Evaluate 1、Explain 1 | 2025-06/41 Q1(a) |
| **9.3.5** patterns and trends in (un)employment | 1／2 | 2（5、2） | – | Define 1、Identify 1 | 2024-11/42 Q1(a) |
| **9.3.6** mobility of labour | 0／3 | 2（6、2） | 1 | Analyse 1、Identify 1、Evaluate 1 | – |
| **9.3.7** policies to reduce unemployment and their effectiveness | 2／5 | 3（7、6、8） | 2 | Assess 3、Evaluate 1、Analyse 1 | 2023-11/41 Q4；2025-06/41 Q1(b) |

#### 9.4 货币与通胀

9.4.6（降低通胀的政策及其有效性）是 Section C 的高频 essay：货币政策降通胀及其对其他宏观目标的影响（2023-06/42 Q5）、成本推动型通胀的政策（2024-03/42 Q4：无准确图 L2，不涉及供给侧政策进不了 L3）、供给冲击下的减税与加息（2024-06/42 Q4，要抓住成本推动的语境，PER 2024-06 p.27）、央行能否靠控制货币供应控制通胀（2024-11/43 Q4，公开市场操作、MV=PT、货币供应难定义）、需求拉动型通胀（2025-03/42 Q4：微观图代替 AD/AS 拿不到 L3，PER 2025-03 p.10）、关税加限制移民对通胀（2025-11/44 Q4）。MV=PT、流动性偏好、利率决定只作次要点；9.4.1（货币的定义与职能）未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **9.4.1** definition, functions and characteristics of money | **未考** | – | – | – |  |
| **9.4.2** definition of money supply | 0／1 | – | 1 | Evaluate 1 | – |
| **9.4.3** quantity theory of money (MV = PT) | 0／2 | – | 2 | Evaluate 1、Assess 1 | – |
| **9.4.4** functions of commercial banks | 0／1 | – | 1 | Evaluate 1 | – |
| **9.4.5** causes of changes in the money supply in an open economy | 0／3 | – | 3 | Evaluate 2、Assess 1 | – |
| **9.4.6** policies to reduce inflation and their effectiveness | 6／7 | 1（8） | 6 | Evaluate 4、Assess 3 | 2023-06/42 Q5；2024-03/42 Q4；2024-06/42 Q4；2024-11/43 Q4；2025-03/42 Q4；2025-11/44 Q4 |
| **9.4.7** demand for money: liquidity preference theory | 0／1 | – | 1 | Evaluate 1 | – |
| **9.4.8** interest rate determination: loanable funds theory and Keynesian th... | 0／2 | 1（6） | 1 | Consider 1、Evaluate 1 | – |

#### 10.1 宏观目标

宏观目标：大企业扩张对宏观的三项正面影响，每项 2 分，写微观影响不给分（2024-11/43 1(b)）；汇率升／降对宏观目标的影响（2025-11/41 Q4 的 MS 写 'Minimum of 2 aims developed for L3'；2025-11/42 Q4 的 MS 要求指出至少两个宏观目标）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **10.1.1** objectives in terms of inflation, balance of payments, unemployment... | 1／4 | 2（8、6） | 2 | Evaluate 3、Assess 1 | 2024-11/43 Q1(b) |

#### 10.2 目标之间的关系

目标间关系（10.2.1–10.2.5）只作次要点，唯一主考是预期通胀与 Phillips 曲线（2024-11/41 Q4）。考点出现方式是 essay 评价里的“政策 A 达成目标 X 却损害目标 Y”。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **10.2.1** relationship between the internal value of money and the external v... | 0／1 | – | 1 | Evaluate 1 | – |
| **10.2.2** relationship between the balance of payments and inflation | 0／1 | – | 1 | Evaluate 1 | – |
| **10.2.3** relationship between growth and inflation | 0／3 | – | 3 | Evaluate 2、To what extent 1 | – |
| **10.2.4** relationship between growth and the balance of payments | 0／4 | 2（8、4） | 2 | Consider 1、To what extent 1、Evaluate 1、Explain 1 | – |
| **10.2.5** relationship between inflation and unemployment | 1／5 | – | 5 | Evaluate 5 | 2024-11/41 Q4 |

#### 10.3 政策有效性

10.3.1 是 Section C 与 Section A 末题的主力（主考 9 次，涉及 22 行）：政府大量借债是否有效、crowding out 的过程链（2023-03/42 1(c)(d)）、预算盈余对失业与经常账户（2023-06/41 Q4）、日本低利率的理论 4 分＋数据评价 4 分（2023-11/41 1(d)）、文章是否足以证明“政府干预作用不大”（2025-06/41 1(d)）、滞胀下的财政政策（2025-06/41 Q4）、出口需求下降时“只靠货币政策”能否解决（2025-06/44 Q4）、货币政策促增长（2025-11/43 Q4）、预算赤字是否“总是”带来增长（2025-11/44 Q5）。10.3.2（政策冲突）12 次作评价点；10.3.3 宏观政策中的政府失灵只作次要点一次。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **10.3.1** effectiveness of different policies in relation to different macroe... | 9／22 | 6（5、6、6、8、6、8） | 16 | Evaluate 9、Assess 7、Analyse 3、Consider 2、To what extent 1 | 2023-03/42 Q1(c)；2023-03/42 Q1(d)；2023-06/41 Q4；2023-11/41 Q1(d)；2025-06/41 Q1(d)；2025-06/41 Q4；2025-06/44 Q4；2025-11/43 Q4；2025-11/44 Q5 |
| **10.3.2** problems and conflicts arising from the outcome of these policies | 0／12 | 3（6、3、4） | 9 | Evaluate 6、Assess 4、Explain 1、Discuss 1 | – |
| **10.3.3** existence of government failure in macroeconomic policies | 0／1 | 1（8） | – | Assess 1 | – |

#### 11.1 国际收支

国际收支：expenditure-reducing 政策减少赤字但造成失业（2023-03/42 Q4：分析政策本身不等于评价，PER 2023-03 p.10）、expenditure-switching 政策减少经常账户赤字（2025-03/42 Q5：L3 需至少两项政策加相关图，关税图最常用，PER 2025-03 p.10）、关税是否最有效（2025-11/43 Q5，微观图不接受）；Section A：贸易赤字的成因 4 分，每个原因识别 1＋解释 1，只列四个原因得 2 分（2023-11/41 1(b)；PER 2023-11 p.23）、侨汇作为二次收入进入经常账户→(X−M)→AD（2025-11/41 1(c)）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.1.1** components of the balance of payments accounts: current account, fi... | 1／4 | 3（4、8、6） | 1 | Evaluate 2、Explain 1、Analyse 1 | 2025-11/41 Q1(c) |
| **11.1.2** effect of fiscal, monetary, supply-side, protectionist and exchange... | 2／6 | – | 6 | Evaluate 5、Consider 1 | 2025-03/42 Q5；2025-11/43 Q5 |
| **11.1.3** difference between expenditure-switching and expenditure-reducing p... | 1／5 | – | 5 | Evaluate 4、Consider 1 | 2023-03/42 Q4 |

#### 11.2 汇率

汇率：贬值对低收入国增长的贡献（2023-06/42 Q4，X、M 价格→(X−M)→AD/AS→增长；评价供给能否反应、初级产品供给弹性、外债币种）；汇率上升／下降对宏观目标（2025-11/41 Q4、2025-11/42 Q4）；出口下滑时货币政策（2025-06/44 Q4）；Marshall-Lerner 与 J 曲线是这些题的高分评价（PER 2025-03 p.10，Q4、Q5）。11.2.1（汇率的度量）与 11.2.2（固定与管理汇率的决定）未考。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.2.1** measurement of exchange rates | **未考** | – | – | – |  |
| **11.2.2** determination of exchange rates under fixed and managed systems | **未考** | – | – | – |  |
| **11.2.3** distinction between revaluation and devaluation of a fixed exchange... | 0／2 | – | 2 | Evaluate 1、Consider 1 | – |
| **11.2.4** changes in the exchange rate under different exchange rate systems | 2／3 | – | 3 | Evaluate 2、Consider 1 | 2025-11/41 Q4；2025-11/42 Q4 |
| **11.2.5** the effects of changing exchange rates on the external economy usin... | 1／6 | – | 6 | Evaluate 3、Consider 2、Assess 1 | 2023-06/42 Q4 |

#### 11.3 发展与生活水平

生活水平是 Section A 末题的常客（主考 10 次）：PPP 的含义 2 分（同一篮子商品本币价格与他币价格之比，2023-06/42 1(a)）、HDI 三项（2025-06/44 1(a)）、用表格评价生活水平变化（2023-06/42 1(c)、2024-11/41 1(d)、2025-06/44 1(d)、2025-11/42 1(d)）。终点的固定格式：先定义 SoL 并分 material 与 non-material，用数据两边论证（算出变化幅度），指出缺失的数据（收入分配、健康、教育、住房、污染、工时），结论通常是“数据不足以下定论”，单边论证有封顶（2024-11/41 1(d) 单边最多 4，罗列最多 4）。essay：GNI 与 MPI 的相对优劣（2023-11/42 Q5）、国民收入统计比较高低收入国（2024-06/41 Q5）、给定墨西哥 2020 数据评价其用于判断生活水平（2024-11/42 Q4：名义工资 2.8% 低于通胀 3.4%，实际收入下降）、生产率提高是否带来更高生活水平（2023-06/41 Q5，生产与生产率常被混淆，PER 2023-06 p.22）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.3.1** classification of economies in terms of their level of development | 0／6 | – | 6 | To what extent 2、Evaluate 2、Assess 1、Consider 1 | – |
| **11.3.2** classification of economies in terms of their level of national income | 0／1 | – | 1 | Consider 1 | – |
| **11.3.3** indicators of living standards and economic development | 10／19 | 8（2、6、6、8、3、8、7、8） | 11 | Evaluate 6、Assess 5、Consider 4、To what extent 2、Explain 1、Identify 1 | 2023-06/41 Q5；2023-06/42 Q1(a)；2023-06/42 Q1(c)；2023-11/42 Q5；2024-06/41 Q5；2024-11/41 Q1(d)；2024-11/42 Q4；2025-06/44 Q1(a)；2025-06/44 Q1(d)；2025-11/42 Q1(d) |
| **11.3.4** comparison of economic growth rates and living standards | 0／10 | 6（6、8、8、3、7、5） | 4 | Consider 3、Evaluate 3、Assess 2、Explain 1、Analyse 1 | – |

#### 11.4 人口、分配与经济结构

人口与收入分配全在 Section A：2025-03/42 Q1 四问都考人口（optimum population 2 分须有“人均收入最高”与“给定资源和技术”两要素；人口 structure 而非 size；两种人口变化对 GDP 的影响须写到最终影响；中国政府自己的政策是独生与二孩，延迟退休不给分）；移民对东道国是否只有好处（2025-11/41 1(d)）、回到 2019 年前移民水平的宏观影响（2024-11/42 1(d)）。Gini 与 Lorenz：Gini 的含义与取值 3 分（2024-06/41 1(a)，三点缺一不可）、两者的联系须画 Lorenz 曲线 5 分（2025-11/43 1(a)）、表格是否支持“不平等与识字率、贫困有关”（2024-06/41 1(c)，结论错也可拿 2 分数据分）。Dutch disease（11.4.3）：资源出口→汇率升值→制成品出口更贵→制造业萎缩，再用图判断程度（2024-11/41 1(c)）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.4.1** population growth and structure | 6／8 | 8（4、8、2、5、6、7、5、7） | – | Explain 4、Consider 2、Evaluate 1、Analyse 1 | 2024-11/42 Q1(d)；2025-03/42 Q1(a)；2025-03/42 Q1(b)；2025-03/42 Q1(c)；2025-03/42 Q1(d)；2025-11/41 Q1(d) |
| **11.4.2** income distribution | 4／5 | 5（6、3、6、5、5） | – | Consider 2、Describe 1、Explain 1、Analyse 1 | 2024-06/41 Q1(a)；2024-06/41 Q1(c)；2025-11/43 Q1(a)；2025-11/43 Q1(b(ii)) |
| **11.4.3** economic structure | 1／4 | 3（8、4、8） | 1 | Assess 2、Evaluate 1、Explain 1 | 2024-11/41 Q1(c) |

#### 11.5 援助、贸易投资、MNC、外债、IMF/世界银行

发展问题：MNC 是否“总是”促进增长／有益（2023-11/42 Q4、2025-11/42 Q5）、国际援助对生活水平（2023-11/43 Q5：援助类型几乎没人分清，停在 L2，PER 2023-11 p.29）、低利率时期向外国借款促长期增长（2024-11/42 Q5）、一带一路对巴基斯坦与中国的长期影响（2023-06/42 1(d)，只写一国最多 5、两边论证最多 7、判断 1）。FDI 9 次全作次要点。IMF 与世界银行只在私有化 essay 中出现（2024-11/42 Q3）。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.5.1** international aid | 1／2 | – | 2 | Assess 1、Evaluate 1 | 2023-11/43 Q5 |
| **11.5.2** trade and investment | 1／5 | 1（8） | 4 | Evaluate 4、To what extent 1 | 2023-06/42 Q1(d) |
| **11.5.3** role of multinational companies (MNCs) | 2／5 | 1（8） | 4 | Evaluate 3、Assess 2 | 2023-11/42 Q4；2025-11/42 Q5 |
| **11.5.4** Foreign Direct Investment (FDI) | 0／9 | 3（8、7、8） | 6 | Evaluate 7、To what extent 1、Assess 1 | – |
| **11.5.5** external debt | 1／3 | 1（8） | 2 | Evaluate 2、Assess 1 | 2024-11/42 Q5 |
| **11.5.6** role of the International Monetary Fund (IMF) | 0／1 | – | 1 | Evaluate 1 | – |
| **11.5.7** role of the World Bank | 0／1 | – | 1 | Evaluate 1 | – |

#### 11.6 全球化与经济一体化

全球化是 Section C 第 5 题最常见的主题（20 份中 6 份的第 5 题，加上 Section A 一次，共主考 7 次）：对低收入国生活水平（2023-03/42 Q5、2024-06/42 Q5）、高收入国以低收入国为代价获益？（2023-11/41 Q5）、高收入国增长并“自动”提高生活水平（2024-03/42 Q5）、高收入国用高关税应对全球化负面影响（2024-11/43 Q5，要图）、对高低收入国“同等”有益？（2025-06/42 Q5，只写一类国家最高 L2 10）；Section A 也问过文章是否足以证明全球化对所有人净有益（2025-11/43 1(c)，定义 2 分）。自由贸易区：是否“总是”有益（2024-11/41 Q5）、FTA 能否既得关税同盟好处又免其代价（2025-06/41 Q5），贸易创造与转移是分析工具。

| 条目 | 主考点次数／涉及行数 | Section A 小问（分值） | essay | 命令词 | 作为主考点的出处 |
|---|---|---|---|---|---|
| **11.6.1** meaning of globalisation and its causes and consequences | 7／9 | 1（8） | 8 | Evaluate 6、Assess 2、To what extent 1 | 2023-03/42 Q5；2023-11/41 Q5；2024-03/42 Q5；2024-06/42 Q5；2024-11/43 Q5；2025-06/42 Q5；2025-11/43 Q1(c) |
| **11.6.2** distinction between a free trade area, a customs union, a monetary ... | 2／2 | – | 2 | Evaluate 2 | 2024-11/41 Q5；2025-06/41 Q5 |
| **11.6.3** trade creation and trade diversion | 0／3 | – | 3 | Evaluate 3 | – |

#### AS 条目在 Paper 4 中的出现

Paper 4 把 AS 内容当作已知前提，下列 AS 条目以定义或分析工具的身份出现（括号内为涉及行数／主考点次数）：1.3.4 division of labour and specialisation（1／1）；1.5.3 causes and consequences of shifts in a PPC（3／0）；1.6.2 nature and definition of public goods（1／1）；1.6.3 nature and definition of merit goods: under-consumption as…（2／0）；2.4.2 effects of shifts in demand and supply curves on…（1／0）；2.4.4 functions of price in resource allocation; rationing,…（1／0）；3.1.1 addressing the non-provision of public goods（1／0）；3.3.2 measuring income and wealth inequality（2／0）；3.3.4 policies to redistribute income and wealth（1／0）；4.1.1 meaning of national income（1／0）；4.2.2 injections and leakages (multiplier not required)（1／0）；4.3.5 causes of a shift in the AD curve（1／0）；4.3.9 causes of a shift in the AS curve in the short run (SRAS)…（1／0）；4.3.12 effects of shifts in the AD curve and the AS curve on the…（1／0）；4.4.1 meaning of economic growth（1／0）；4.4.2 measurement of economic growth（1／0）；4.4.3 distinction between growth in nominal GDP and real GDP（1／1）；4.4.4 causes of economic growth（4／0）；4.5.3 causes and types of unemployment: frictional, structural,…（4／0）；4.6.3 distinction between money values (nominal) and real data（2／0）；4.6.4 causes of inflation: cost-push and demand-pull inflation（5／0）；5.2.2 distinction between a government budget deficit and a…（2／0）；5.2.3 meaning and significance of the national debt（3／1）；5.2.4 taxation（1／0）；5.2.7 AD/AS analysis of the impact of expansionary and…（5／0）；5.3.2 tools of monetary policy: interest rates, money supply and…（1／0）；5.3.4 AD/AS analysis of the impact of expansionary and…（7／0）；5.4.3 tools of supply-side policy, for example training,…（3／0）；5.4.4 AD/AS analysis of the impact of supply-side policy on the…（1／0）；6.2.2 different tools of protection and their impact（5／0）；6.3.1 components of the current account of the balance of payments（1／0）；6.3.3 causes of imbalances in the current account of the balance…（3／1）；6.4.4 causes of changes in a floating exchange rate: demand and…（1／0）；6.4.5 AD/AS analysis of the impact of exchange rate changes on…（3／0）。作主考点的 5 次：national debt 读表（2023-11/41 1(a)）、贸易赤字成因（2023-11/41 1(b)）、public good 定义与应用（2023-11/42 1(d)）、分工与平均成本（2025-06/44 1(b)）、按不变价格计算 GDP 的意义（2025-11/42 1(a)）。

### 1.3 至今未考的条目

20 份试卷中从未被标注的 A Level 条目（14 条）：**7.3.3** Pareto optimality；**7.4.6** asymmetric information and moral hazard；**7.4.7** use of costs and benefits in analysing decisions (knowledge of net present value is not required)；**7.5.2** short-run cost function；**7.5.3** long-run production function；**7.5.8** definition and calculation of revenue: total, average and marginal revenue (TR, AR, MR)；**7.5.10** calculation of supernormal and subnormal profit；**7.7.2** internal growth of firms: organic growth and diversification；**8.2.2** difference between equity and efficiency；**8.2.4** the poverty trap；**9.3.3** voluntary and involuntary unemployment；**9.4.1** definition, functions and characteristics of money；**11.2.1** measurement of exchange rates；**11.2.2** determination of exchange rates under fixed and managed systems。

只作次要点、从未作主考点的 A Level 条目（49 条）：7.1.2、7.1.3、7.1.5、7.2.2、7.2.4、7.3.2、7.3.4、7.3.6、7.4.2、7.5.1、7.5.5、7.5.7、7.6.2、7.6.3、7.7.1、7.7.4、7.7.5、7.8.1、7.8.5、8.1.2、8.3.1、8.3.2、8.3.7、8.3.10、9.1.3、9.2.5、9.3.1、9.3.2、9.3.6、9.4.2、9.4.3、9.4.4、9.4.5、9.4.7、9.4.8、10.2.1、10.2.2、10.2.3、10.2.4、10.3.2、10.3.3、11.2.3、11.3.1、11.3.2、11.3.4、11.5.4、11.5.6、11.5.7、11.6.3。其中 8.1.2（政府失灵，10 次）、10.3.2（政策冲突，12 次）、7.3.2／7.3.4（效率条件、动态效率，各 11 次）、11.3.4（增长与生活水平比较，10 次）、11.5.4（FDI，9 次）是 essay 评价段的常用材料，不能因为没单独设问就不准备。

提醒：未考≠不会考。Paper 3（选择题）覆盖面更广，见 `9708-P3.questions.json`；2026 年两季的 Paper 4 尚未读到。

### 1.4 典型终点（final form）

- **定义题（2–4 分）**：MS 把定义拆成要素逐个给分，缺一个要素扣一分；用同义词改写术语不给分（optimum 写成 best／ideal 得 0 分，PER 2025-03 p.8）。例：recession＝GDP＋负增长＋连续两个季度（2023-03/42 1(a)）；Gini＝收入不平等的度量＋0–1＋0 为完全平等、1 为完全不平等（2024-06/41 1(a)）；optimum population＝人均收入最高＋给定资源与技术（2025-03/42 1(a)）；concentration ratio＝含义 2 分＋算法 2 分（2023-06/41 1(a)）；PPP＝同一篮子在两种货币下的价格之比，可举例算出汇率（2023-06/42 1(a)）。
- **“解释/分析”题（4–6 分）**：按因果链逐环给分，最后一环必须落到题目问的变量上（2025-03/42 1(c) 必须写到对 GDP 的最终影响；2023-03/42 1(c) crowding out：卖债券→利率上升→私人借贷变贵→私人投资与消费被挤出）。理论与材料常各占一半（2024-11/41 1(b) 2＋2；2023-11/41 1(d) 4＋4）。
- **Section A 末题**：两边用材料论证＋指出缺失的数据＋保留 1 分给结论。20 份中 6 份的末题直接问“文章／证据是否足以支持某结论”（2023-03/42、2024-11/43、2025-06/41、2025-06/44、2025-11/41、2025-11/43）。
- **Essay**：先界定题干术语（低收入国、MNC、output gap……），画题目要求的图并在文中引用，分析成链，评价逐条展开（说明“为什么取决于”而不只说“取决于”），结论回到题干的绝对化用词（always、only、automatically、equally）。

### 1.5 反复出现的 MS 惯例（附出处）

- **C1 统一的 essay 评分**：每篇 essay 的 MS 都写明 'AO1 and AO2 out of 14 marks. AO3 out of 6 marks.'，分别按 Table A、Table B 给等级；Table A/B 的文字在 2023-06/41（=/43）的 MS 文本层里抽不出来，其余 18 份可见且一致。
- **C2 要图而无图（或图错）→ AO1/AO2 封顶 L2**：'Where no diagram – max marks top L2'（2023-06/41 Q2）；'Limit of Level 2 if no relevant diagram'（2023-11/41 Q3）；'L2 maximum if no accurate diagram provided'（2024-03/42 Q2、Q3、Q4）；'Up to Level 2 only if no diagram'（2024-06/41 Q3）；'Maximum L2 if no diagram'（2024-11/41 Q2、Q4、Q5）；'L2 max if no or incorrect diagram provided'（2024-11/43 Q2、Q3、Q5）；'L2 Max if no relevant diagram provided'（2025-03/42 Q3、Q4，Q5 同义）；'No diagram-highest mark is L2 – 8'（2025-06/41 Q2）；'Maximum 8 marks if no relevant diagram'（2025-06/41 Q4）；无垄断图／无图／无 J/W 图 L2 8（2025-06/42 Q2、Q3、Q4）；'No Diagram Max L2 8'（2025-06/44 Q2）；'Max L2 if no diagram'（2025-11/41 Q3）；'No diagram L2 Max'（2025-11/43 Q2、Q3）。2025-11/43 Q4、Q5 写成 'No diagram Max L3'，与其余写法不一致，按 L2 理解更稳妥（见 1.7）。Section A：图不准确最多 3 分（2023-06/42 1(b)）、'Maximum 3 marks if no diagram'（2025-11/41 1(b)）。
- **C3 题目有两个对象，只写一个封顶 L2**：只写一种市场 L2 8（2025-06/42 Q3）、只写一类收入国家 L2 10（2025-06/42 Q5）、只写一种市场结构 L2（2025-11/41 Q3）、两个市场都要写才进 L3（2025-11/43 Q3）、至少展开两个宏观目标才进 L3（2025-11/41 Q4）、不涉及供给侧政策进不了 L3（2024-03/42 Q4）、只写一国 Section A 最多 5 分（2023-06/42 1(d)）。
- **C4 偏离题目的内容不给分**：'No credit for alternative policies eg supply side/fiscal policy'（2025-06/42 Q4）；'Micro diagram not acceptable'（2025-11/43 Q5）；'Must assess effects on macro economy not micro economy'（2024-11/43 1(b)）；不是中国政府的政策（延迟退休）不给分（PER 2025-03 p.9，2025-03/42 1(d)）；市场结构判错则特征分全失（2025-11/42 1(c)）。
- **C5 Section A 末题的结构分**：保留结论分——'reserve a mark for the conclusion'（2023-03/42 1(d)）、'Reserve a mark for conclusion.'（2025-06/41 1(d)）、结论 1 分（2023-06/41 1(d)、2023-06/42 1(d)、2024-11/41 1(d)、2024-11/42 1(d)、2024-11/43 1(c)、2025-11/44 1(c) 等）；单边论证与罗列封顶——单边最多 4、罗列最多 4（2024-11/41 1(d)）、两边最多 7＋判断 1（2023-06/42 1(d)）、论证最多 7＋结论 1（2024-11/42 1(d)、2025-11/44 1(c)）。
- **C6 数据分独立于结论**：结论错也可拿“正确使用数据”的 2 分（2024-06/41 1(c)）；算出变化幅度给分（2023-06/42 1(c) 人均 GDP 中国 +28%、巴基斯坦 +14%；2025-11/42 1(d) GDP +0.7 万亿美元、人均 +1459 美元）；点出材料里没有的数据也给分（2023-06/42 1(c)、2024-11/41 1(d)、2025-06/44 1(d)、2025-11/42 1(d)）。
- **C7 “识别＋发展”配对给分**：每个原因／影响 1 分识别、1 分解释（2023-06/41 1(c)、2023-11/41 1(b)、2024-11/43 1(b)）；只列不解释只拿一半（PER 2023-11 p.23）。
- **C8 Section A 用 MS 的固定措辞的地方**：equity＝fairness／justice（2023-11/42 1(a)、2023-11/43 1(a)、2024-03/42 1(c)(i)）；“Do not credit minimum wage”作为绝对贫困的定义（2025-11/41 1(a)）；可持续性＝不损害后代满足其需要的能力（2025-06/42 1(a)）。

### 1.6 考官反复警告（附出处）

- **W1 没回答题目真正问的东西**：PER 2025-03 p.8 说这一失误 'has been ‘flagged up’ many times'；population structure 写成 size（2025-03/42 1(b)，p.8）；用别人的建议代替政府政策（2025-03/42 1(d)，p.9）；微观题写宏观（2025-03/42 Q3，p.9）；用边际效用代替无差异曲线被限 L1（2023-11/42 Q2，PER 2023-11 p.26）；把增长题写成生活水平（2023-11/42 Q4，p.26）；没把教育认作 merit good、把 productivity 写成 GDP（2023-06/41 Q2、Q5，PER 2023-06 p.21）；没认出 horizontal integration（2023-11/41 Q3，PER 2023-11 p.23）；背好的答案不对题（PER 2023-06 p.23；PER 2024-06 p.26）；essay 不分小问后更要通读题干（PER 2023-06 p.23；PER 2023-11 p.25；PER 2024-06 p.26）。
- **W2 图的问题**：题目要图而没有相关的、标注正确的图，不能超过 Level 2（PER 2023-06 p.21；PER 2023-11 p.23；PER 2024-06 p.24；PER 2025-03 p.10）；图的类型错——航空画成生产外部性（2023-03/42 Q2，PER 2023-03 p.9）、买方垄断题画成完全竞争劳动市场（2025-03/42 Q3，p.9）、AD/AS 题画微观图（2025-03/42 Q4，p.10）、劳动市场图标成 AS/AD（2024-06/42 1(c)，PER 2024-06 p.26）；作图精度——MC 必须过 AC 最低点、利润最大化在 MR=MC（2023-06/41 1(d)，PER 2023-06 p.21；2024-06/42 Q3，PER 2024-06 p.27）；画了图却不在文中引用（PER 2023-06 p.23；PER 2024-06 p.26）。题目没要求图时也应画相关图（PER 2023-06 p.21；PER 2023-11 p.23；PER 2024-06 p.24）。
- **W3 评价不足**：分析政策本身不算评价（2023-03/42 Q4，PER 2023-03 p.10）；“evaluate”要质疑题干断言的有效性（PER 2023-03 p.10）；只说“取决于 PED”是 E1，解释 PED 如何改变结果才是 E2（2024-06/42 Q2，PER 2024-06 p.27）；题目没写 evaluate 也要评价（PER 2023-11 p.23）；充分展开的结论本身可拿至少 4/6（2023-03/42 Q2，PER 2023-03 p.9；2023-11/43 Q2，PER 2023-11 p.28）；一句话的评价停在 L1（2025-03/42 Q4，PER 2025-03 p.10）；结论不要只是复述（2025-03/42 Q5，PER 2025-03 p.10）。
- **W4 Section A 的用法**：不基于文章的评论不给分（2023-03/42 1(d)，PER 2023-03 p.9）；数据题要看趋势而不是读单点（2023-11/43 1(b)，PER 2023-11 p.27）；要评论证据是否充分（2023-11/41 1(c)，PER 2023-11 p.23）；结论分常被漏掉（2023-06/41 1(d)，PER 2023-06 p.21；2023-11/43 1(c)，PER 2023-11 pp.27–28；2025-03/42 1(d)，PER 2025-03 p.9）；“两者各有优点”拿不到判断分（2023-11/42 1(c)，PER 2023-11 p.25）；四个原因只列不解释只得 2 分（2023-11/41 1(b)，PER 2023-11 p.23）；按分值控制长度、发展材料而非抄写（ECR 2023-06 p.14）。
- **W5 定义要素不全**：recession（2023-03/42 1(a)，PER 2023-03 p.8）、PPP（2023-06/42 1(a)，PER 2023-06 p.23）、concentration ratio（2023-06/41 1(a)，PER 2023-06 p.21）、负外部性是第三方承担的成本（2023-06/41 1(b)，PER 2023-06 p.21）、equity（2023-11/42 1(a)，PER 2023-11 p.25）、Gini 的两端（2024-06/41 1(a)，PER 2024-06 p.24）、internal economies of scale 漏 long term／average costs（2024-06/42 1(a)，PER 2024-06 p.26）、minimum efficient scale（2024-06/42 1(b)，p.26）、optimum population（2025-03/42 1(a)，PER 2025-03 p.8）。
- **W6 语境与绝对化用词**：“always”要正面检验（2023-11/43 Q3，PER 2023-11 p.28）；成本推动型通胀的语境下减税加息针对的是 AD（2024-06/42 Q4，PER 2024-06 p.27）；低收入国这一限定不能丢（2023-06/42 Q4，PER 2023-06 p.24）；紧缩性货币政策题写成扩张性政策是弱答案（2023-06/42 Q5，PER 2023-06 p.24）；国际收支常见误解——以为政府从出口取得收入（2023-06/41 Q4，PER 2023-06 p.22）；援助要分类型讨论（2023-11/43 Q5，PER 2023-11 p.29）。

### 1.7 MS 本身的问题（制卡前核对）

- 2023-06/41 Q3：MS 写“低 PED 市场价格较低”，与三级价格歧视的标准结论（弹性大的市场定低价）相反。
- 2023-06/41 Q5：MS 只印了 AO3，且部分要点写的是 FDI 题；2023-11/41 Q5 的 MS 里夹着一道 FDI 与生活水平题的指示内容；2023-11/43 Q4 的 AO3 后半段讲贬值，属于别的题；2023-06/41 Q2、2023-11/41 Q2 的 AO3 夹着负外部性与广告的通用条目。这些段落按题意取舍。
- 2023-11/43 Q3：MS 称垄断竞争企业长期实现 productive efficiency；标准理论下长期切点在 AC 最低点左侧（过剩产能），不宜照搬。
- 2023-11/43 1(b)：MS 写“employment fluctuates but there is a general rising trend”，按图应为 unemployment。
- 2025-03/42 1(d)：MS 要点列了延迟退休，PER 说它不是中国政府的政策、不给分（PER 2025-03 p.9），以 PER 为准。
- 2025-06/44 1(d)：MS 把 GNI 增量写成 2481 美元／143%，按材料（2342→5823）应为 3481 美元、约 149%。
- 2025-11/42 1(c)：MS 把 price maker 也列为农户（垄断竞争）的特征。2025-11/41 Q2 部分要点按正外部性写，题目是气候变化（负外部性）。2025-11/43 Q4、Q5 写 'No diagram Max L3'，与其他题的 L2 封顶不一致。
- 2024-11/43 1(c)：QP 问 “supported by the article and by economic theory”，MS 题干写 “or”。

## 2. 复现

- `work/p4audit/scripts/merge_validate.py <cie-9708>`：合并两个 part 文件并校验；`--no-merge` 只校验。
- `work/p4audit/scripts/apply.py <cie-9708>`：在合并结果上做本轮修改（考纲映射修正、新卷号、/43 照抄、QP 补全），新条目写在 `new_entries.py`。
- `marks_check.py`、`page_check.py`、`er_check.py`、`quotes.py`（参数都是 `registry` 目录）：分值、页码、PER 引用、引文核对。
- `stats.py`、`overview.py`：统计与本文件。
- `work/p4audit/provenance.md`：本轮下载文件的来源与校验。
