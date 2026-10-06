# WST02 · S2 Statistics 2：考纲摘要

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文关键词照抄考纲。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。S2 在印刷 pp.57–59（PDF pp.63–65）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。页码写印刷页码（FB 印刷页 = PDF 页 − 6）。
- 公式和 ≤ 号对照渲染页图核过（`registry/work/stat-spec/pg-63.png`–`pg-65.png`）。版面文本：`registry/work/stat-spec/lay_p063.txt`–`lay_p065.txt`。
- 试卷封面只用来补充考场要求，不是考纲：`registry/src/WST02/2025-10_01_qp.txt`（WST02/01，Friday 31 October 2025，P78847A）。
- 试卷用语的检索：Edexcel-Finder 题面数据（`registry/finder/repo/static/Data/Mathematics (2018)/WST02/`，14 份题面，2020 年 10 月至 2025 年 1 月），只用于 §5 的一条说明。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WST02/01**。另有区域卷 **WST02/01A**，考纲里没有这个代码。英国文化协会中国区 2025 年 10 月、2026 年 10 月以及 2026 年 1 月、6 月都以 WST02A 报名；本环境还没有找到任何一份 WST02/01A 试卷 | SPEC p.8、p.78；versions.md §1.6；`inventory/stat-gaps.md` |
| 单元名称 | Unit S2: Statistics 2；p.67 表中写作 “S2: Statistics 2” | SPEC p.57、p.67 |
| AS/A2 定位 | 单元页原文：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Mathematics and Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔%（可计入 IAS Further Mathematics，所以有 IAS 权重） | SPEC p.57、p.67、p.8 |
| 资格结构 | IAL Mathematics 里 S2 **只能以 “S1 and S2” 组合出现**（五组选修组合之一）。IAS/IAL Further Mathematics 可选。IAS Mathematics 不能选 S2 | SPEC p.10 |
| 时长与分值 | 1 hour and 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.57 |
| 题量（参考） | 2025 年 10 月卷封面写 “There are 7 questions”，总分 75。考纲没有固定题量 | `registry/src/WST02/2025-10_01_qp.txt` |
| 计算器 | 允许使用，规则见 Appendix 6 | SPEC p.57；p.86 |
| 卷面要求（试卷封面，不是考纲） | 统计表查出的值要 “quoted in full”；用计算器代替查表时，结果要保留到相当的精度。非精确答案默认保留 3 位有效数字 | 2025-10 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。S2 部分在 FB pp.18–24。FB p.18 原话：“Candidates sitting S2 may also require those formulae listed under Statistics S1, and also those listed under Pure Mathematics P1, P2, P3 and P4.” | SPEC p.57；FB p.18 |
| 开考季 | **January, June and October**（p.70 注：从 2020 年 6 月起 October 考季包括 S2）。2020 年 6 月以前，2018 版 S2 没有开考 | SPEC p.8、p.70；versions.md §1.4 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.57；versions.md §1.4–1.5 |
| 旧考纲同代码 | 2013 版旧考纲也用 WST02，最后一次是 **2020 年 1 月**，不算本考纲的真题。p.1 说 Statistics 各单元 “have not changed”，旧卷内容兼容，可作额外练习 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | 考纲要求已掌握：S1 的规格内容及其先修与公式；**多项式的微分和积分**；与二项分布有关的 **binomial coefficients**；**指数函数求值**（“the evaluation of the exponential function”）。原文结尾：“is assumed and may be tested” | SPEC p.57 |
| 评估目标分配（75 分中） | AO1 **25–30**；AO2 20–25；AO3 10–15；AO4 5–10；AO5 5–10 | SPEC p.69 |
| 须背公式（不在 FB 里） | 考纲原文：“This is a list of formulae that students are expected to remember and which will not be included in formulae booklets.”清单只有两条，见 §3 | SPEC p.57 |
| 记号 | Appendix 7 第 10 节（pp.91–92）：B(n, p)、f(x) 为概率密度函数值、F(x) 为 P(X ≤ x)、E(X)、Var(X) 等。考纲没有 Po(λ) 的记号条目，但 S2 1.1 指导栏用了 Po(λ) | SPEC pp.91–92、p.58 |
| 单元概述 | “The Binomial and Poisson distributions; continuous random variables; continuous distributions; samples; hypothesis tests.” | SPEC p.57 |

---

## 2. 规格条目逐条（S2.3 Unit content）

### 主题 1 The Binomial and Poisson distributions（p.58）

**1.1 The binomial and Poisson distributions**（p.58）
- 要求：用二项分布和 Poisson 分布 “model a real-world situation”，并 “comment critically on their appropriateness”（评论模型是否合适）。累积概率可以计算，也可以查表（“by calculation or by reference to tables”）。
- 要求：会用 Poisson 分布的 **additive property**。考纲的例子：每分钟事件数 ∼ Po(λ)，则每 5 分钟事件数 ∼ Po(5λ)。
- 公式：两个分布的 P(X = x)、均值、方差都在 FB p.18；二项累积分布表在 FB pp.19–23，Poisson 累积分布表在 FB p.24。

**1.2 The mean and variance of the binomial and Poisson distributions**（p.58）
- 要求：两个分布的均值和方差。
- 排除：“No derivations will be required.”

**1.3 The use of the Poisson distribution as an approximation to the binomial distribution**（p.58）
- 要求：用 Poisson 分布近似二项分布。指导栏为空：考纲**没有写**近似成立的条件（n 大、p 小的具体界限），FB 也没有。Pearson 接受什么样的条件表述，要从评分方案核对。

### 主题 2 Continuous random variables（p.58）

**2.1 The concept of a continuous random variable**（p.58）
- 要求：连续随机变量的概念。指导栏为空。

**2.2 The probability density function and the cumulative distribution function for a continuous random variable**（p.58）
- 要求：使用概率密度函数 f(x)，P(a < X ≤ b) = ∫ₐᵇ f(x) dx；使用累积分布函数 F(x₀) = P(X ≤ x₀) = ∫_{−∞}^{x₀} f(x) dx。
- 限制：“The formulae used in defining f(x) will be restricted to simple polynomials which may be expressed piecewise.”（f(x) 只用简单多项式，可以分段定义。）
- 公式：P(a < X ≤ b) 的积分式须背（p.57）；F(x₀) 的积分式在 FB p.18。

**2.3 Relationship between density and distribution functions**（p.58）
- 要求：f(x) = dF(x)/dx。
- 公式：须背（p.57）。

**2.4 Mean and variance of continuous random variables**（p.58）
- 要求：连续随机变量的均值与方差。指导栏为空。
- 公式：E(X) = ∫x f(x) dx，Var(X) = ∫x² f(x) dx − μ²，E(g(X)) = ∫g(x) f(x) dx 都在 FB p.18。

**2.5 Mode, median and quartiles of continuous random variables**（p.58）
- 要求：连续随机变量的众数、中位数、四分位数。指导栏为空。

### 主题 3 Continuous distributions（p.58）

**3.1 The continuous uniform (rectangular) distribution**（p.58）
- 要求：连续均匀（矩形）分布。指导栏：“Including the derivation of the mean, variance and cumulative distribution function.”（与 1.2 相反，这里**要求推导**均值、方差和累积分布函数。）
- 公式：pdf 1/(b − a)、均值 ½(a + b)、方差 (b − a)²/12 在 FB p.18；推导要自己会。

**3.2 Use of the Normal distribution as an approximation to the binomial distribution and the Poisson distribution, with the application of the continuity correction**（p.58）
- 要求：用正态分布近似二项分布和 Poisson 分布，并使用 **continuity correction**。指导栏为空；与 1.3 一样，考纲没有写近似条件。
- 相关：4.6 的二项检验也可能用正态近似计算概率。

### 主题 4 Hypothesis tests（p.59）

单元概述里的 “samples” 一项，在条目里放在 “4. Hypothesis tests” 标题下（4.1–4.2）。

**4.1 Population, census and sample. Sampling unit, sampling frame**（p.59）
- 要求：总体（population）、普查（census）、样本（sample）；抽样单位（sampling unit）、抽样框（sampling frame）。须知道 census 与 sample survey 各自的优缺点（“the advantages and disadvantages associated with a census and a sample survey”）。

**4.2 Concepts of a statistic and its sampling distribution**（p.59）
- 要求：统计量（statistic）的概念及其抽样分布（sampling distribution）。指导栏为空。

**4.3 Concept and interpretation of a hypothesis test. Null and alternative hypotheses**（p.59）
- 要求：假设检验的概念与解释，原假设与备择假设。指导栏：“Use of hypothesis tests for refinement of mathematical models.”

**4.4 Critical region**（p.59）
- 要求：拒绝域。指导栏：“Use of a statistic as a test statistic.”

**4.5 One-tailed and two-tailed tests**（p.59）
- 要求：单尾和双尾检验。指导栏为空。

**4.6 Hypothesis tests for the parameter p of a binomial distribution and for the mean of a Poisson distribution**（p.59）
- 要求：二项分布参数 p 的检验，Poisson 分布均值的检验。须会用表做检验（“know how to use tables to carry out these tests”）；“Questions may also be set not involving tabular values.”（也可能出不在表里的参数值，要直接计算。）
- 要求：二项分布参数 p 的检验 “may involve the use of a normal approximation to calculate probabilities”。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| P(a < X ≤ b) = ∫ₐᵇ f(x) dx | **须背**（考纲明列） | SPEC p.57 |
| f(x) = dF(x)/dx | **须背** | SPEC p.57 |
| 二项分布 B(n, p)：P(X = x) = C(n, x) pˣ(1 − p)ⁿ⁻ˣ，均值 np，方差 np(1 − p) | FB 给出 | FB p.18 |
| Poisson 分布 Po(λ)：P(X = x) = e^{−λ} λˣ / x!，均值 λ，方差 λ | FB 给出 | FB p.18 |
| 连续随机变量的 E(X)、Var(X)、E(g(X))；F(x₀) = P(X ≤ x₀) = ∫_{−∞}^{x₀} f(t) dt | FB 给出 | FB p.18 |
| 连续均匀分布 [a, b]：pdf 1/(b − a)，均值 ½(a + b)，方差 (b − a)²/12 | FB 给出（但 3.1 要求会推导） | FB p.18；SPEC p.58 |
| 二项累积分布表 P(X ≤ x)：n = 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 40, 50；p = 0.05 到 0.50，间隔 0.05 | FB 给出 | FB pp.19–23 |
| Poisson 累积分布表 P(X ≤ x)：λ = 0.5 到 10.0，间隔 0.5 | FB 给出 | FB p.24 |
| S1 的全部公式与表（含 Φ(z) 表、正态百分点表）；P1–P4 的公式 | FB 给出，S2 可能用到 | FB p.18 那句说明；FB pp.3–5、14–17 |
| Poisson 近似和正态近似的适用条件；continuity correction 的做法；Poisson 可加性的写法 | FB **未给**，须背清单也**没有**；考纲只写要会用 | SPEC pp.58–59；FB p.18（已核对没有） |

---

## 4. 与相邻单元的界线

- **S1（先修，可直接考）**：离散随机变量、E(X)、Var(X)、累积分布函数、正态分布查表与标准化都在 S1（主题 5、6，p.56），S2 默认会用。S1 2.2 是**数据**的中位数和四分位数，S2 2.5 是**连续随机变量**的中位数和四分位数。S1 只有离散均匀分布（5.4）；连续均匀分布在 S2 3.1。
- **P1–P4**：先修里写明多项式微积分、binomial coefficients、指数函数求值（p.57）。多项式微积分在 P1（WMA11 4.2、5.2）；二项展开在 P2（WMA12 4.5）；eˣ 在 P3（WMA13 3.1）。FB p.18 说可能用到 P1–P4 的全部公式，比考纲先修条目的范围宽。
- **S3（以 S1、S2 为先修）**：
  - 抽样**方法**（simple random sampling、random numbers、stratified、systematic、quota）→ S3 2.1–2.2（p.61）。S2 4.1 只到 population、census、sample、sampling unit、sampling frame 的概念。
  - 样本均值 X̄ 的分布、Central Limit theorem、无偏估计 → S3 3.1–3.2、3.6。S2 4.2 只是统计量和抽样分布的**概念**。
  - 正态总体均值的检验与置信区间 → S3 3.3–3.8。S2 的检验只针对二项分布的 p 和 Poisson 分布的均值。
  - χ² 拟合优度检验（可检验 binomial、Poisson、continuous uniform 等模型）→ S3 4.1。
  - 相关系数检验 → S3 5.2。
- **S2 没有的内容**：t 分布、两样本检验、正态均值检验都不在 S2；probability generating function 只出现在 Appendix 7 的记号表（10.19，p.92），任何单元的条目都没有提到它。

---

## 5. 印刷问题与缺口

- **FB 二项表的列标题印错**：n = 40 那一页（FB p.22）的列标题印成 “0.05 … 0.40 0.50 0.50”，第 9 列应为 0.45（其他二项表页都是 0.45；已放大渲染核对，`registry/work/stat-spec/fb-28-top.png`）。查 n = 40、p = 0.45 时要注意。
- **考纲用语与试卷用语**：S2 条目里没有出现 “significance level”“actual significance level”“p-value” 这些词（全文检索 `registry/work/stat-spec/spec_all_layout.txt`），但试卷里会出现。例如 Edexcel-Finder 收录的 14 份 WST02 题面中，有 3 份含 “actual significance level”，7 份含 “significance level”。这些词的接受答法要从评分方案和考官报告校准。
- **近似条件**：1.3、3.2 的近似条件考纲没写（见 §2），属于需要用评分方案补充的缺口。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否另有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 真题需求概览

### 6.1 数据范围、引用写法与本次审核

**数据范围**：`WST02.questions.json`（2026-10-06 由 `WST02.questions.part1.json` 与 `part2.json` 合并）。共 16 份卷，即 2020-10 至 2025-10 每一季的 WST02/01，合计 106 题、402 个小问、1200 分。
- S21（2021 年 6 月）的试卷和 MS 已发布，但考试取消，所以没有 ER。
- O20 卷封面印的是原定的 2020 年 6 月日期，实际在 10 月使用（见 `WST02.coverage.part1.md`）。
- 16 份卷都有 MS。J25 只找到 “Final” 版。
- ER 只有 O22、J23、S23、O23、J24 五份，覆盖 34 题。

下面的数字由 `work/wst02audit/scripts/stats.py` 和 `stats2.py` 从索引统计，结果在 `work/wst02audit/stats.json`、`stats2.txt`、`dump_by_spec.txt`。“问法、终点、评分”取自索引的 `ask`、`final_form`、`ms`、`er` 字段。

**缺失的卷**（所有来源都没有）：
- 2025-10 /01A。英国文化协会中国区报名了 WST02A，所以这份卷应当存在。
- 2026-01 的 /01 与 /01A。
- 2026-06 的 /01 与 /01A。
- 以上各卷的 QP、MS、ER 全缺。另外，S24、O24、J25、S25、O25 五季缺 ER。

本次审核在 Drive 重新检索了三类条件，没有发现新的 WST02 文件：
- 标题含 `S2A`、`QP_S2`、`MS_S2`、`WST02A`；
- 标题含 WST02 或 Statistics S2，且在 2025-11-15 以后修改；
- 全文含 `WST02/01A`。

唯一按 `_S2` 命名的文件 `24_10_MS_S2.pdf` 就是已收的 O24 MS（大小 542387 字节，相同）。

**引用写法**：
- J = January，S = June，O = October，后接两位年份，如 O24 = 2024 年 10 月。
- 题号和小问照试卷印刷。
- “MS”“ER”指该季的评分方案和考官报告，页码是 PDF 页（见索引条目的 `ms`、`er` 字段）。

**本次审核做了什么**（脚本和输出都在 `work/wst02audit/`）：

1. **合并与校验**。part1 有 45 条，part2 有 61 条，id 不重复，合并后共 106 条。`merge_validate.py` 检查了以下各项，问题数为 0（`validate.txt`）：
   - 每条的字段齐全；
   - 各小问分值之和等于题目总分；
   - spec id 都在 `spec-items.stat.json` 里；
   - series 的格式是 YYYY-MM；
   - 每卷合计 75 分，题号连续；
   - 有 MS 或 ER 来源的条目，`ms`、`er` 字段不为空；
   - 引文不超过 25 个词。
2. **独立核对分值**。`totals_check.py` 直接从 `src/WST02/*_qp.txt` 抽取印刷的 “(n)” 序列和 “(Total …)” 行。16 份卷的 402 个小问分值、106 个题目总分与索引逐一相符。
3. **评分码之和**。`mscodes.py` 把每个小问 `ms` 里的 M/A/B 码加起来，与该小问分值比较。402 个小问中有 14 个不一致，逐个查过，都是注释里的组合写法（如 “M1M0A0”）或 ALT 写法造成的，不是错误。
4. **命令词**。`cmdcheck.py` 检查每个命令词是否出现在该题的 QP 原文里，查出 1 处错误：J21 Q3(d) 原文是 “Using a suitable test … assess”，索引写成 “Use a suitable test”，已改为 “Assess”。
5. **逐条复核**。对照 QP、MS、ER 原文逐条重查了 24 题，每一季至少一题：
   - O20 Q4；J21 Q5；S21 Q1、Q2；O21 Q6；J22 Q6、Q7；S22 Q5；O22 Q5、Q7；J23 Q5；S23 Q2；O23 Q7；J24 Q3；S24 Q3、Q4、Q6；O24 Q3、Q7；J25 Q2；S25 Q6；O25 Q3、Q4、Q7。
   - 另外部分核对了 J22 Q2(d)、O22 Q3(a)、J23 Q2(d)、O23 Q6、O24 Q5。
   - 分值、终点、MS 要点和 ER 转述都相符。数值答案用 Python 独立重算（二项、Poisson 的尾概率，均匀分布与 pdf 的积分）。
   - 补了 2 处 MS 遗漏：S25 Q6(d) MS 接受 awrt 57.3，尽管题目要求 exact；O24 Q3(f) 只评论经理的说法不给分。
6. **集中出现的问题**：part1 的假设检验标签。part1 把 4.5 标在单尾检验上，完整检验又不标 4.3，与 part2 的规则不一致。因此把 part1 全部 164 个小问的 spec 重新看了一遍，统一采用下面的规则：
   - **4.3**：凡写假设、或解释检验结果（完整检验、只写假设、“根据拒绝域评论”）的小问都标；
   - **4.5**：只标在双尾检验上（含 O20 Q3(b) 的两侧临界值）；
   - **4.6**：建立或执行二项、Poisson 检验的小问都标；
   - **1.1**：Poisson 率需要换算到新区间时，作次要标签；
   - 由 f 积分得到 F 标 **2.2**；由 F 求导得到 f 标 **2.3**。

   按这套规则共改 19 处 spec：part1 14 处，part2 5 处（O23 Q5(d)、J25 Q3(d)、J25 Q5(c)、O24 Q5(a)、O24 Q5(b)）。连同上面的 1 处命令词和 2 处 MS 补充，一共 22 处修改，每处的证据写在 `fixes.json`，由 `apply_fixes.py` 同时写入合并文件和对应的 part 文件。
   - 这些修改只影响标签，没有改动分值、答案或 MS 要点。
   - 主条目分值的变化：4.6 减 2 分、4.3 加 2 分（J22 Q3(e)）；2.3 减 7 分、2.2 加 7 分（O24 Q5）。
   - 因此 `WST02.coverage.part1.md`、`part2.md` 里 “Spec coverage” 一节的计数已经过时，以本节为准。

### 6.2 卷面结构

- **每卷 75 分**。6 题的有 6 份（O20、J21、S21、O21、J23、S24），7 题的有 10 份。
  - 题目分值 4–18 分，最常见的是 10 分（24 题）、11 分（16 题）、9 分（13 题）、12 分（12 题）。
  - 4 分的两题都是普查与抽样的概念题（S23 Q2、O25 Q1）。
- **小问**：
  - 每题小问个数：3 个的 35 题、5 个的 27 题、4 个的 24 题、2 个的 11 题、6 个的 7 题、1 个的 2 题。
  - 小问分值：1 分 69 个、2 分 122 个、3 分 79 个、4 分 63 个、5 分 37 个、6 分 18 个、7 分 11 个、8 分 1 个、10 分 2 个。
  - 6–10 分的大问共 32 个，按类型分：
    - 抽样分布 11 个；
    - E 与 Var 的计算 7 个；
    - 带近似的完整检验 6 个；
    - 正态近似反求参数 5 个；
    - 完整的 cdf 2 个（J22 Q4(c)，S22 Q6(c)）；
    - 由二项概率反求 Poisson 参数 1 个（S22 Q5(b)）。
- **命令词**（402 个小问，归并同义词）：
  - Find／Calculate／Determine 240；
  - State／Write down／Give／Suggest／Identify／Specify 60；
  - Show that／Verify 49；
  - Test／Assess／Carry out a test 20；
  - Explain／Describe／Comment 17；
  - Sketch 10；
  - List 6。

  印刷了答案的小问（Show that、Verify）有 49 个，约占 12%，集中在 2.2（23 个）、2.4、2.5（各 8 个）。
- **终点形式**（自动粗分，仅供参考）：
  - 3 位有效数字的小数（awrt）约 103 个；
  - 精确分数或根式约 99 个；
  - 文字、模型、草图、列表、分布表约 93 个；
  - 印刷结果 49 个；
  - 检验结论 28 个；
  - 整数或参数值 26 个。
- **按主条目统计分值**（每个小问只算 `spec` 的第一个条目）：
  - 主题 1（二项与 Poisson）293 分（24.4%）；
  - 主题 2（连续随机变量）337 分（28.1%）；
  - 主题 3（均匀分布与正态近似）249 分（20.8%）；
  - 主题 4（抽样与假设检验）321 分（26.8%）。
- **每卷固定出现的题型**：
  - **至少一个假设检验**（4.6，16/16）。Poisson 检验 12 题，二项检验 13 题。O24、J25 两卷没有“一问做完”的检验，只有“假设 → 拒绝域 → 显著性水平 → 评论”的题组。
  - **恰好一题连续均匀分布**（3.1，16/16）。J22 有两题（Q2、Q7）。
  - **一题抽样分布**（4.2，16/16）。例外是 S23：只有 Q2(c) 判断哪个是 statistic 的 1 分，没有计算抽样分布。
  - **一到两题 pdf/cdf**（2.2，16/16；2.4，16/16）。
  - **至少一个正态近似小问**（3.2，16/16）。
  - **Q1 多半是二项或 Poisson 的直接概率**，16 份卷中有 12 份如此；S23 Q1 也以二项概率开头，再接正态近似。
- **检验格式**：
  - **完整检验**一问 4–7 分，评分结构为：B1 假设，M1 A1 概率或拒绝域，M1 比较，A1 语境结论。
  - **拒绝域题组**的结构为：写假设（1 分）→ 求拒绝域（3 分，双尾要写每侧概率）→ 求 actual significance level（1–2 分）→ 根据拒绝域评论（1–2 分）。出现在 J22 Q3、O22 Q3、J24 Q3、S24 Q3、O24 Q3、J25 Q5、S25 Q2。
  - 显著性水平：5% 为主；另有 1%（J21 Q3(d)，J23 Q3(c)）、10%（S25 Q7(e)，O25 Q5(d)），以及 3% 双尾（O24 Q3，S25 Q2）。
- **计算器限制**：
  - 题目里印了 “Solutions relying (entirely) on calculator technology are not acceptable” 的地方：J24 Q1(d)、Q4(c)；S24 Q6 整题；S25 Q5 整题；O25 Q5(c)、Q7(b)。
  - 题干或命令词要求 algebraic integration、calculus，或不能只靠计算器的小问，共 20 个，见 6.5 第 8 条。

### 6.3 每个考纲条目怎么考

“卷数／题数／小问／涉及分值（主）”：一个小问可以带几个条目标签，所以各行相加大于 106 题、1200 分；括号里是该条目作为第一标签时的分值。命令词已归并同义词。

| 条目 | 卷数／题数／小问／涉及分值（主） | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 二项与 Poisson 建模 | 16／48／107／313（241），主条目分值最多 | Find 79，State／Write down／Give／Suggest 18，Test 5 | ① 直接概率：B(n, p) 或 Po(λ) 的点概率、累积概率，常是一问两小问，用 “more than / at least / between … inclusive / fewer than” 表述（几乎每卷 Q1）。② 换算区间的 Poisson（可加性）：6 m²（S21 Q2(b)），80 m（J23 Q5(a)），2 m²（O24 Q1(a)），20 分钟（J25 Q5(a)），30 分钟（S24 Q1(b)，S25 Q2(a)）。③ 两段模型：Poisson、均匀分布或分位数给出概率 p，再进 B(n, p)（O20 Q2(f)，J21 Q2(b)，J22 Q1(c)，O22 Q1(b)，J23 Q5(b)，S23 Q7(b)，J24 Q1(e)，S24 Q1(b)，J25 Q4(ii)）。④ 反求：由累积概率求 x、k、r、n（J22 Q1(a)，S23 Q1(a)(iii)，S25 Q7(c)，O24 Q2(d)）；由两个 pmf 值求 λ（J25 Q1(e)）；由二项概率反求 Poisson 的区间长度 m（S22 Q5(b)）；“P(至少一次) > 0.95 的最小 n”（O20 Q6(c)，O23 Q1(b)(ii)，J24 Q6(b)，S24 Q4(c)，S25 Q4(b)，O25 Q5(b)）。⑤ 其他：条件 Poisson（O21 Q4(e)，S23 Q7(c)）；到下一事件的时间（O21 Q4(d)，S24 Q5(d)）；期望利润（S21 Q2(d)，O22 Q1(c)）；二项的线性函数（O21 Q1(c)，O24 Q2(b)–(c)）；两个独立变量比较 P(X₁ < W₁)（S22 Q1(d)）。⑥ 模型：写出分布并带参数；在语境中写假设（singly、independently、constant rate；独立、概率不变）；说明模型为何不成立（S24 Q1(d)：轮胎成对买） | 3 s.f. 小数（awrt），或照抄表值；整数 n、x、k；小问 1–4 分 | J23 Q1，S23 Q7，O21 Q4，S24 Q1，J25 Q1 |
| 1.2 二项与 Poisson 的均值、方差 | 8／10／13／41（21） | Find 7，Show 3，State 2 | 不考推导（考纲写 “No derivations”）。考法有：写出 Var（S22 Q1(a)）；由均值和方差反求 n、p（S25 Q3(a)，O23 Q7(b)，J25 Q6(a)）；样本均值与方差相近，说明 Poisson 合适（J24 Q1(a)–(b)，O25 Q2(a)；J24 Q1(b) 的 MS 要求先算出相容的数值）；期望个数（O23 Q1(b)(i)，S25 Q3(b)）；E(5X − 25)（O24 Q2(b)）；正态近似里的 np、np(1 − p)（S21 Q6，O23 Q7） | n、p 的值，或文字理由；1–3 分 | S25 Q3(a)，J24 Q1，O23 Q7(b) |
| 1.3 Poisson 近似二项 | 11／11／15／48（31） | Find 8，Test 3，State／Explain 4 | ① “Use a (suitable) Poisson approximation to find/estimate”：J22 Q5(c)，S23 Q4(b)，S24 Q5(b)，J25 Q1(b)，S25 Q3(c)(i)；多次重复中稀有事件的个数（O20 Q4(e) 200 块区域，J24 Q2(c) 200 组样本）。② 条件：n large、p small（J22 Q5(d)，S23 Q4(a)，J25 Q1(d)，S25 Q3(c)(ii)）。③ 百分误差（J25 Q1(c)）。④ 检验中先近似再查表：S21 Q1(d) 用 Po(5)，S22 Q4(b) 用 Po(6)，O22 Q3(c) 用 Po(7)。⑤ 反求最大的 n（J21 Q1(d)） | 3 s.f. 概率；条件用文字表述；1–4 分 | J25 Q1，S25 Q3(c)，O20 Q4(e) |
| 2.1 连续随机变量的概念 | 1／1／1／1（1） | Write down 1 | 只考过一次：P(X = 4) = 0（O25 Q4(b)） | 0；1 分 | O25 Q4(b) |
| 2.2 pdf 与 cdf | 16／32／70／198（159） | Find 34，Show that 23，Sketch 8 | ① 定常数：用 ∫f = 1 证明 k（O20 Q1(a)，J21 Q4(a)，J22 Q4(b)，O22 Q2(b)，S23 Q3(a)，S24 Q6(a)，O24 Q7(a)，J25 Q7(c)(i)，S25 Q5(a)）；cdf 里的常数由连接处连续、F(端点) = 0 或 1 定出（O21 Q3(a)–(b)，O22 Q5(a)，J23 Q6(a)，S23 Q5(a)–(b)，S24 Q2(a)，S25 Q1(a)，O25 Q4(a)）。② 分段写出完整 cdf：O20 Q5(b)，O21 Q6(c)–(d)，J22 Q4(c)（7 分），S22 Q6(c)（6 分），O24 Q5(a)–(b)，J25 Q3(d)。③ 用 F 求概率，包括条件概率（F 的差之比）：O21 Q6(f)，O22 Q5(c)，O23 Q6(a)，J24 Q4(b)，S24 Q2(b)；P(X > E(X))（J22 Q4(d)）。④ 画 pdf 或 cdf 草图：S21 Q3(a)，O21 Q6(a)，J22 Q4(a)，S22 Q3(c)，O22 Q2(a)，J24 Q4(a)，S24 Q6(c)，J25 Q7(a)。⑤ 由概率反求界值：S24 Q6(d)，P(X ≥ k) = 0.8 | 精确分数（83/90、133/192）或 3 s.f.；印刷的常数；分段函数连同区间；2 分最多（31 个），cdf 全式 4–7 分 | O21 Q6，J22 Q4，S22 Q6，O24 Q5，O25 Q4 |
| 2.3 f(x) = dF(x)/dx | 12／12／13／45（28） | Find 7，Specify 3，Show 2 | ① 由 cdf 求 pdf 并写全：O20 Q2(a)，S21 Q5(b)，J22 Q2(a)，S23 Q5(d)，S24 Q2(c)，O25 Q4(d)。② 由 cdf 求众数，要先求导：O21 Q3(d)，J24 Q7(a)，S25 Q1(d)。③ 求 E、Var 前先由 F 得到 f：J21 Q2(c)，J23 Q6(b)，O23 Q6(c) | 分段 pdf；2–6 分 | S24 Q2(c)，O25 Q4(d)，J24 Q7(a) |
| 2.4 连续随机变量的均值、方差 | 16／27／39／143（92） | Find 29，Show that 8 | ① 用代数积分求 E(X)、E(X²)、Var(X)：O20 Q5(a)，J21 Q2(c)，S21 Q3(c)–(d)，S22 Q2(a)，O22 Q2(c)，O23 Q6(c)，O24 Q7(c)，J25 Q4(i)，S25 Q5(b)–(c)。② Var(aX + b) 与 E(g(X))：Var(2Y − 3)（O21 Q6(b)），Var(1/Y) 和 Var(4 − 5/Y)（O25 Q7(b)–(c)），E(3X²)（J22 Q2(d)），用给定积分求 E(6Y − 5)（S23 Q5(e)），E(2H² + 3G + 3)（J24 Q4(c)），面积的期望（J23 Q4(d)，O25 Q6(a)）。③ 由 E、Var 列方程解常数：J21 Q4(b)，J23 Q6(b)–(d)，S24 Q6(b)。④ 以 µ ± σ、E(T) ± 2 为界的概率：O24 Q7(e)，O20 Q5(d) | 精确分数（19/6、66/7225）或 3 s.f.；印刷结果；2–6 分 | O24 Q7(c)，O25 Q7，J24 Q4(c) |
| 2.5 众数、中位数、四分位数 | 13／15／25／69（57） | Find 10，Show／Verify 8，State 4，Explain 2 | ① 众数：令 f′(x) = 0 并舍去另一个根（O20 Q1(b)，S21 Q3(b)，O21 Q3(d)，S25 Q1(d)）。但正二次函数的驻点是最小值，此时众数在端点（S23 Q3(d)–(e)，J25 Q7(b)）。也有由众数反求常数（J24 Q7(a)，O23 Q2(a)–(b)）。② 中位数、四分位数、百分位数：解 F(m) = 0.5（S25 Q1(c)，化成 m 的四次式）；第 30 百分位数（O21 Q6(e)）；P(Y ≥ y) = 0.9（S21 Q3(e)）；IQR（O22 Q2(d)）；上、下四分位数（O24 Q7(d)）。③ 用变号区间验证中位数或四分位数：J21 Q4(c)，J24 Q7(c)，J25 Q7(c)(ii)，O25 Q7(a)。④ 用已知概率判断四分位数在哪一侧：S23 Q3(c)。⑤ 由 mean、median、mode 的大小顺序判断偏态：J22 Q4(e)，S25 Q1(e)。⑥ 四分位数的概率进入二项分布：J25 Q4(ii) | 精确根式（2 − √6/3、√8）或 3 s.f.、指定小数位；“lies between” 型验证要写结论；1–5 分 | S23 Q3，S25 Q1，O24 Q7，O25 Q7(a) |
| 3.1 连续均匀分布 | 16／17／66／173（160） | Find 52，State／Write down 7，Show 5，Sketch 2 | 每卷恰好一题（J22 有两题）。① 由两个条件（概率加 E 或 Var）求 a、b：O21 Q2(i)，O22 Q7(i)，S23 Q6(b)，J24 Q5(a)，O24 Q4(i)，S25 Q6(a)（两组解都给分）。② 写 pdf、cdf，画图，套 E、Var 公式：O20 Q2(a)–(b)，J22 Q2，J23 Q4，O23 Q3，J25 Q3(a)–(d)；用 E(X²) = Var + E² 求 E(X²)：O22 Q7(ii)，S23 Q6(d)，S25 Q6(d)，J25 Q3(e)。③ 随机截断与几何：木头截成直角三角形的两边（J21 Q5），较短的一段（O21 Q2(ii)），电线分成三段（O22 Q7(iii)），木头围成长方形（J24 Q5(c)），电线弯成两个正方形（O24 Q4(ii)），周长固定的长方形（O25 Q6），面积服从均匀分布时求边长（J22 Q7），圆的面积（J23 Q4(d)）。④ 以 a + b 等参数写的不等式概率（O21 Q2(i)(b)，O22 Q7(i)，S25 Q6(e)）；条件概率（O20 Q2(e)）；截断到支撑区间（J25 Q3(f)，O23 Q3(d)，J24 Q5(b)(ii)）。⑤ 与 Poisson、二项组合：S21 Q5(d)，S24 Q5(d)，O20 Q2(f) | 精确分数为主（23/40、17/21、(√2 + 1)/6）；参数值；2 分最多（31 个） | O22 Q7，S25 Q6，J25 Q3，O25 Q6 |
| 3.2 正态近似（二项、Poisson），连续性修正 | 16／19／23／120（89） | Find 14，Show 5，Test 3 | 每卷都有。① 近似二项求概率：S22 Q2(c)，S23 Q1(b)(i)，O25 Q5(c)；近似 Poisson 求概率：O20 Q4(d)，J22 Q1(b)，J24 Q1(d)，O24 Q1(c)。② 反求（分值高）：求 n（J21 Q3(c)，O22 Q4(b)）；求 x（J23 Q5(c)，8 分，是 √x 的二次方程）；求 p（S21 Q6，10 分；J25 Q6(b)–(c)）；先求 µ、σ 再求 n、p（O23 Q7）；求 t（S25 Q7(d)）；求两侧临界值（O20 Q3(b)）。③ 检验中用正态近似：近似二项（O21 Q1(d)，J22 Q5(e)，S24 Q3(f)），近似 Poisson（O23 Q5(d)）。④ 适用条件：n large、p close to 0.5（S23 Q1(b)(ii)） | 3 s.f. 概率，或 n、x、p 的值；5 分（7 个）和 7 分（6 个）最多 | J23 Q5(c)，O23 Q7，S21 Q6，S24 Q3(f) |
| 4.1 总体、普查、样本、抽样框、抽样单位 | 4／4／11／14（14） | Suggest／Identify／Give／State 10，Explain 1 | 只在 J21 Q6(a)–(c)，S23 Q2(a)–(b)，S24 Q3(a)–(c)，O25 Q1(a)–(c) 出现：抽样框是全体成员（或店铺）的名单；抽样单位是一个成员（一家店）；样本相对普查的一个优点和一个缺点；什么样的总体适合普查（小、可接触） | 文字；每问 1 分，优缺点题 2 分 | S24 Q3(a)–(c)，O25 Q1 |
| 4.2 统计量与抽样分布 | 16／16／43／147（138） | Find 26，List 6，Show 4，State 4，Explain 3 | 每卷一题，例外是 S23，只有 1 分判断哪个是 statistic。① 定义 “sampling distribution of a statistic”（O20 Q6(a)，J22 Q6(a)，O25 Q3(a)）；判断某个量是不是统计量（S23 Q2(c)，J25 Q2(i)）。② 从只有两三种数值的大总体（或袋子）中抽 2–4 个，列出组合，求总和、均值、中位数、众数、极差或得分的抽样分布：O20 Q6 极差，S21 Q4 极差，O21 Q5 得分，J22 Q6 总数，S22 Q7 中位数，O22 Q6 极差，J23 Q2 均值与众数，O23 Q4 中位数，J24 Q6 总分，O24 Q6 总和与中位数，S25 Q4 总分，O25 Q3 均值与众数。③ 由已知概率反求比例 p（J21 Q6(d)，J23 Q2(c)，O25 Q3(d)），由比例反求个数 a（O22 Q6(a)）。④ 不放回抽样：S22 Q7，S24 Q4，J25 Q2(iii)。⑤ 后接“最小 n”：O20 Q6(c)，J24 Q6(b)，S24 Q4(c)，S25 Q4(b) | 概率分布表（值与概率配对，概率和为 1），精确分数；求整张表的一问常为 6–7 分 | O25 Q3，S24 Q4，J23 Q2，O23 Q4 |
| 4.3 假设检验的概念，H0 与 H1 | 16／24／35／135（15） | Test 20，Write down／State 8，Comment 5 | 作主条目只有两类：写假设（1 分：S21 Q1(c)，J22 Q3(b)，O24 Q3(c)，J25 Q5(b)，S25 Q2(c)），以及根据拒绝域评论（1–2 分：J22 Q3(e)，J24 Q3(d)，S24 Q3(e)，O24 Q3(f)，J25 Q5(d)，S25 Q2(f)）。其余是完整检验里写假设和写结论的部分。还考过“为什么这个检验不合适”：S23 Q4(c)(ii)–(d)，P(X = 0) 本身就大于 5%，H0 永远不能被拒绝 | H0: p = …，H1: p >、< 或 ≠ …（λ 用原来的率或换算后的率都可以，但要前后一致）；语境结论 | J24 Q3(d)，S23 Q4，O24 Q3 |
| 4.4 拒绝域 | 12／12／24／58（41） | Find 15，Comment 5，State 4 | ① 单侧或双侧拒绝域：双侧时每侧尽量接近 2.5%（3% 检验为 1.5%），并写出每侧概率。题目：O21 Q4(f)，J22 Q3(c)，O22 Q3(a)，J24 Q3(b)，S24 Q3(d)，O24 Q3(d)，J25 Q5(c)，S25 Q2(d)。② actual significance level，即两侧概率之和：J22 Q3(d)，O22 Q3(b)，J24 Q3(c)，O24 Q3(e)，S25 Q2(e)。③ 反求使 0 落入拒绝域的最小 n：S22 Q4(a)（0.93ⁿ），J23 Q3(c)（0.9ⁿ，1% 水平）。④ 用正态近似求临界值：O20 Q3(b) | 拒绝域写成 X ≤ c₁、X ≥ c₂，不能写成概率式；概率保留 4 位小数；2–3 分 | O24 Q3，J24 Q3，S25 Q2 |
| 4.5 单尾与双尾 | 8／9／12／42（0） | Find 7，Write down 3，Test 2 | 从未作主条目。双尾出现在：两侧临界值（O20 Q3(b)）；双尾 Poisson 拒绝域题组（J22 Q3，O24 Q3（3%），S25 Q2（3%））；双尾二项拒绝域（O22 Q3(a)，J24 Q3(b)，S24 Q3(d)）；双尾完整检验（J22 Q5(e) 用正态近似，S22 Q4(b) 用 Poisson 近似，都与 0.025 比较）。题干中的 “has changed / is not / increased or decreased” 是双尾的信号 | H1 用 ≠；每侧 α/2 | J22 Q3，S22 Q4(b)，O24 Q3 |
| 4.6 二项 p 与 Poisson 均值的检验 | 16／25／36／148（113） | Test 20，Find 11，Write down 5 | 每卷至少一个检验，见 6.2。先换算 Poisson 率再检验：O20 Q4(c)，S21 Q2(e)，O21 Q4(f)，O23 Q5(d)，S24 Q1(c)，J25 Q5(c)，O25 Q2(c)。用近似做检验：Poisson 近似（S21 Q1(d)，S22 Q4(b)，O22 Q3(c)）；正态近似（O21 Q1(d)，J22 Q5(e)，O23 Q5(d)，S24 Q3(f)）。考纲说的 “not involving tabular values” 只体现在反求最小 n 的题（S22 Q4(a) 的 p = 0.07 不在表里；J23 Q3(c)） | 概率值（与 α 或 α/2 比较）或拒绝域，加语境结论；5 分最多（13 个） | J24 Q3(e)，S24 Q1(c)，O23 Q5，O25 Q2(c) |

### 6.4 考纲写了、真题还没考过（或极少考）的点

依据：16 份卷的索引检索，加上 `src/WST02/*_qp.txt` 的关键词检索。16 个条目每个都至少出现过一次，下面列出很少考或从未考过的具体要点。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 2.1 连续随机变量的概念 | 只考过 O25 Q4(b)，1 分（P(X = 4) = 0） | 一张卡：连续型的单点概率为 0，所以求区间概率时 < 与 ≤ 结果相同 |
| 3.1 推导均匀分布的均值、方差和 cdf（考纲指导栏明确要求） | 16 份卷从未要求用积分证明 (a + b)/2 或 (b − a)²/12。J22 Q2(c) 要 “show Var(X) = 4k²/3”，MS p.7 接受直接套 (b − a)²/12，也接受积分。写出 cdf 只在 J25 Q3(d) 出现（4 分） | 考纲要求，所以保留一张推导卡；但练习重点放在应用：求 a、b，以及截断与几何题 |
| 1.2 均值、方差（“No derivations”） | 从未推导。考的是反求 n、p，以及用“均值 ≈ 方差”判断 Poisson 是否合适 | 公式卡加两种反求题型 |
| 4.1 普查、样本、抽样框、抽样单位 | 只在 4 份卷出现（J21、S23、S24、O25），合计 14 分。S21–J23、O23–J24、O24–S25 都没考 | 频率低但容易得分：做三张定义卡，措辞照 MS（list of **all** …；a single member） |
| 4.2 “statistic” 的定义 | 判断一个量是不是统计量只考过 2 次（S23 Q2(c)，J25 Q2(i)） | 一张卡：只用样本值算出、不含未知参数 |
| 4.3 “Use of hypothesis tests for refinement of mathematical models” | 从未以这种说法出现 | 不单独做卡 |
| 4.5 单尾与双尾 | 从未作主条目；双尾只在 8 份卷出现。“p-value”“critical value”这两个词从未出现在 QP 中；“actual significance level” 出现在 5 份卷（J22、O22、J24、O24、S25） | 练从题干判断单尾还是双尾，以及每侧 α/2；actual significance level 等于所选尾概率之和 |
| 4.6 “Questions may also be set not involving tabular values” | 只在反求最小 n 的题出现（S22 Q4(a)，J23 Q3(c)）。其余检验的参数都在表里，或经近似后在表里 | 练直接计算 (1 − p)ⁿ 和 e^(−λ)λˣ/x! |
| 3.2 用正态近似做 Poisson 均值的检验 | 只有 O23 Q5(d) 一次。近似条件只考过二项一侧（S23 Q1(b)(ii)）；“λ 大”这一条件从未要求写出 | 一张卡：Po(λ) ≈ N(λ, λ)，要用连续性修正 |
| 1.3 近似条件 | 已考 4 次，全部是 n large、p small。MS 接受的写法：n > 50 且 p < 0.2，或 “p close to 0”。不接受 “mean ≈ variance”（S25 Q3(c)(ii)，MS p.8）；只写 “np < 10” 也不接受（J25 Q1(d)，MS p.6） | 一张辨析卡：Poisson 近似要 n 大、p 小；正态近似要 n 大、p 接近 0.5 |
| 二项表 n = 40、p = 0.45（FB p.22 列标题印错，见 §5） | 真题没有用到这一组：n = 40 只配过 p = 0.2、0.3、0.35（S25 Q3(b)，S25 Q7，O22 Q3(a)，J24 Q3(e)） | 不影响备考，仅作提醒 |

**§2、§5 留下的待核实点已有答案**：
- **近似条件（1.3、3.2）**：Poisson 近似写 “n large and p small”；正态近似二项写 “n large and p close to 0.5”，写 “p is small” 是 S23 Q1(b)(ii) 最常见的错误（ER p.3）。
- **试卷用语**：“actual significance level” 在 5 份卷出现，“p-value” 从未出现。

### 6.5 反复出现的评分惯例与考官提醒

ER 只有 O22、J23、S23、O23、J24 五份；没有标 ER 的引用来自 MS 的评分说明。下列出处在 `WST02.coverage.part1.md`、`part2.md` 中整理，本次审核抽查了其中十余处原文（MS、ER 文本层），全部相符。

1. **不等式要准确换成累积概率**（ER 最常批评的一点）。
   - “more than 4” 是 1 − P(X ≤ 4)：J23 Q1(c)(i)、Q3(a)(i)（ER pp.3–4）。“at least 6” 是 1 − P(X ≤ 5)：O22 Q1(a)（ER p.3），O23 Q5(b)(ii)（ER p.5）。“at least 26” 是 1 − P(X ≤ 25)：S23 Q1(a)(ii)（ER p.3）。
   - 区间两端都容易差 1：O22 Q4(a)，P(5 ≤ X < 8) 写成 P(X ≤ 7) − P(X ≤ 5)（ER p.4）；J23 Q3(a)(ii)；S23 Q7(a)（ER p.7）；J24 Q1(c)(ii)（ER p.3）。
   - MS 对同样的错误扣分：O24 Q1(b) 写 1 − P(Y ≤ 5) 是 M0（MS p.6）。
   - 检验中也会出错：P(X ≥ 7) 写成 1 − P(X ≤ 7) 或 P(X = 7)（J23 Q1(d)，ER p.3）；P(X ≤ 8) 写成 P(X = 8)（J24 Q3(e)，ER p.5）。
2. **假设要用总体参数，写在 H0、H1 后面，而且必须写**。
   - 二项检验用 p 或 π，写 p(x) 不给分（S22 Q4(b)，MS p.8）。
   - Poisson 检验用 λ 或 µ，用 p 是 B0（J21 Q3(d)，MS p.7）。用 Poisson 近似做比例检验时，假设仍写 p：O22 Q3(c) 中不少人写成 λ = 7（ER p.4）。
   - 原来的率或换算后的率都接受，只要前后一致：O20 Q4(c) 的 4.5 或 9；S21 Q2(e) 的 0.9、3、0.75 或 9；O23 Q5(d) 的 6 或 36；J25 Q5(b) 的 15 或 7.5；O25 Q2(c) 的 2 或 10。
   - 没写假设，或方向写反，最后的语境 A 分为 0：J22 Q5(e)（MS p.12）；S21 Q1(d)（MS p.6）；O20 Q3(c)（MS p.7）；J23 Q3(b)（MS p.9）；O24 Q3(f)（MS p.8）；S25 Q2(f)（MS p.7）。
   - 题干里的“信念”通常是 H0：J24 Q3(d) 很多人把 Rowan 的信念当作 H1（ER p.4）。
3. **结论要放进语境，用关键词，前后不能矛盾**。
   - 只写不含语境的 “reject H0” 只得 dM1。A1 要求写出对象（proportion、rate 或 number of …）和方向（increased、decreased、changed），例如 O20 Q4(c)（MS p.8），O22 Q3(c)（MS p.10）。
   - Poisson 检验的结论要体现“率”的意思（每天、每 10 分钟的平均个数）：O24 Q3(f)、S25 Q2(f)、O25 Q2(c)（MS pp.7–8）。只评论“经理的说法”不给分（O24 Q3(f)）。
   - 二项检验写 “proportion”，不能只写 “number”（S24 Q3(f)，MS p.8）。J22 Q5(e) 的结论必须出现 “claim” 一词（MS p.12）。
   - 自相矛盾的非语境陈述会丢掉 M 分，几乎每个检验的 MS 都这样写，例如 O25 Q5(d)（MS p.13）。
4. **拒绝域是一组取值，不是概率式；双尾要写出每侧概率，actual significance level 是两侧之和**。
   - 写成概率式不给 A 分：O22 Q3(a)（MS p.10；ER p.4），J24 Q3(b)（MS p.8；ER p.4），S24 Q3(d)，O24 Q3(d)，S25 Q2(d)。
   - 每侧概率要写拒绝的概率：上侧写 0.0124，而不是 0.9876（J24 Q3(b)，ER p.4）。O22 Q3(a) 两侧 0.0303 与 0.0173 都要写出；把 X ≤ 7 当下侧是没读懂 “as close as possible to 2.5%”（ER p.4）。
   - actual significance level 跟着考生自己的拒绝域求和（J22 Q3(d)，O22 Q3(b)，J24 Q3(c)，O24 Q3(e)，S25 Q2(e)）。
   - 永远不能拒绝 H0 的检验不合适（S23 Q4(c)(ii)–(d)）。只写 “sample size is too small” 是 B0（MS p.9）。
5. **题目指定用哪种近似，就用哪种；用精确分布或用错近似会被封顶，甚至 0 分**。
   - 该用正态近似时用了精确二项：S22 Q2(c) 不得分（MS p.6）；O25 Q5(c) 0/5（MS p.13）；S24 Q3(f) 只得 B1（MS p.8）。
   - 该用正态近似时用了精确 Poisson：O24 Q1(c) 0/4（MS p.6）；O23 Q5(d) M0M0A0（MS p.10）。
   - 该用 Poisson 近似时用了精确二项：J21 Q1(d) B0M0A0（MS p.5）；S25 Q3(c)(i) M0M1A0（MS p.8）；J24 Q2(c) 用二项不得分，为了能查表改用 Po(7) 也丢分（ER p.4）。
   - 用错 Poisson 均值：Po(95) 是 M0A0（S21 Q1(d)，MS p.6）。
6. **连续性修正单独占一个 M 分，z 值要取表中 4 位小数**。
   - 连续性修正通常单独占一个 M 分，例如 J23 Q5(c)，O23 Q7(a)，J24 Q1(d)，S24 Q3(f)，O25 Q5(c)。较早的 O20 Q4(d) 则把 68.5、69.5、70.5 都算进标准化的 M 分（MS p.8）。ER 一再提到修正写错或漏写：O22 Q4(b)（ER p.4），S23 Q1(b)(i)（ER p.3），O23 Q5(d)、Q7(a)（ER pp.5–6），J24 Q1(d)（ER p.3）。
   - 变量本身就服从正态分布时不做修正：J24 Q2(a) 加了修正丢 2 分（ER p.4）。
   - z 值：写 1.6449，不写 1.645（J24 Q2(a)，ER p.4）；另见 O22 Q4(b) 的 1.98、J23 Q5(c) 的 ±0.1、J25 Q6(b) 的 1.87。
   - 没有过程的答案可能 0 分：O22 Q4(b) 只写 45 是 0/6（MS p.11）。
   - √x 的二次方程：先解再平方。很多人平方时当作 (a − b)² = a² − b²（J23 Q5(c)，ER p.5）。
7. **“Show that” 和印刷答案要写出每一步，印刷结果之前至少要有一行**。
   - O22 Q2(b)：解出二次方程后直接写 k = 1.25，丢最后 2 分（ER p.3）。
   - O23 Q7(a)：方程列对了，但没写出联立求解，丢 2 分（ER p.6）。
   - J24 Q1(d)：只写 0.29、没写出 0.2912，丢最后 1 分（ER p.3）。
   - 验证代替推导：不给分或封顶。J24 Q5(a) 写 “Do not allow verification”（MS p.11）；S25 Q5(a) 用验证最多 M1M1（MS p.11）。
   - 代入后直接跳到答案，代入的证据不足：J25 Q7(c)(i) 是 A0*（MS p.17）。
8. **“Use algebraic integration / use calculus” 要写出积分式和代入上下限的过程**。
   - 没有代数积分是 M0（O20 Q5(a)，MS p.9）；只写答案只能得 M1M0A0（S22 Q2(a)，MS p.6；J21 Q2(c)，MS p.6）。
   - 只用计算器积分丢 2 分（J24 Q4(c)，ER p.5）；不按题目要求的方法做，不得分（O23 Q2(b)，ER p.3）。
   - 把 F 当 f 用：积分 x F(x) 是 M0（J23 Q6(b)–(c)，MS pp.12–13；ER p.5）；O23 Q6(c)（ER p.5）；S23 Q5(e) 用了 (6y − 5)F(y)（ER p.6）。
9. **分段 cdf 或 pdf：每一行都要写区间，全程用同一个字母**。
   - “otherwise” 只能用在第一行或最后一行，不能两行都用：J22 Q4(c)（MS p.10），O20 Q5(b)（MS p.9），O24 Q5(b)（MS p.10）。
   - 字母不统一（f(x) 配 t 的区间）丢 A 分（O23 Q3(b)，ER p.4）。
   - 常数由连接处的 F 值或 F(上端) = 1 定出。不能把每一段都设成等于 1；也不能写 F(3) = 1（S23 Q5(a)–(b)，ER p.5）。
10. **草图按形状和标注给分**。
    - 跳跃处不能连起来（S21 Q3(a)，MS p.9；J24 Q4(a)，MS p.10，ER p.5）。
    - 曲线不能穿过 x 轴（O21 Q6(a)，MS p.13）。
    - 端点和高度要标出，例如 O22 Q2(a) 的 2k − 0.75 常被漏标（ER p.3）；S22 Q3(c) 要标 −5、19 和 1（MS p.7）。
11. **众数、中位数、四分位数**。
    - f′ = 0 求出的是驻点，可能是最小值，所以要检查端点：S23 Q3(d)–(e)（MS p.8；ER p.4）。
    - 已知 cdf 求众数，要求两次导：J24 Q7(a) 只求一次导或去积分都不对（ER p.6）。
    - 众数是 x 的值，不是高度 64a（O23 Q2(a)，ER p.3）。
    - 求四分位数要让正确那一段的 F 等于相应分数，不要重复用归一化的方程：O22 Q2(d)；IQR 是 Q3 − Q1，不是一个区间（ER p.3）。
    - 变号验证的结论要点名所求的量（median 或 upper quartile）：J24 Q7(c)（MS p.13；ER p.7），J25 Q7(c)(ii)（MS p.17），O25 Q7(a)（MS p.15）。
12. **期望与方差的代数**。
    - E(X²) = Var(X) + [E(X)]²，常见错误：0.48 − E(Y²)，或 E(Y) 忘了平方（O22 Q7(ii)，ER p.5）；12 没平方（J24 Q4(c)，ER p.5）；均值没平方（S23 Q6(d)，ER p.6）；把 E(X²) 当成 [E(X)]²（J23 Q4(d)，ER p.4）。
    - Var(aX + b) = a²Var(X)：O21 Q6(b)（MS p.11），O25 Q7(c)（MS p.16）。
    - 均匀分布的方差是 (b − a)²/12，不是除以 2（O23 Q3(c)，ER p.4）。
13. **均匀分布要注意支撑区间；随机截断题最难**。
    - 超出 [a, b] 的部分要截掉：O23 Q3(d) 写 (40 − 30)/15 不得分，因为模型只在 32 ≤ t ≤ 47 成立（ER p.4）；J25 Q3(f) 中 P(Y < 2k²) 应化为 P(−k < X < √2k)（MS p.11）。
    - O22 Q7(iii) 被 ER 称为 “by far the most difficult question”，并指出 “a sketch of a uniform distribution would have helped”（ER p.5）。J24 Q5(c) 只有较好的考生做出（ER p.6）。
    - 先写出所用的分布，例如 X ~ U[10, 20]（O22 Q7(iii)，ER p.5）。
14. **两段模型与“最小 n”**。
    - Poisson 或均匀分布的概率要再进入二项分布：O22 Q1(b) 有考生没意识到要用二项（ER p.3）；S23 Q7(b) 有人直接平方（ER p.7）；J23 Q5(b) 漏了系数 4（ER p.4）。
    - 条件 Poisson（4 个里分配到 15 分钟）是 S23 “the most discriminating part”，用 B(4, 0.25) 最省事（S23 Q7(c)，ER p.7）。
    - 用对数解 0.9ⁿ < 0.01 这类不等式时，除以负数要反号：J23 Q3(c) 因此得 43 而不是 44（ER p.4）；J24 Q6(b) 得 17 而不是 18（ER p.6）。
    - 答案要写成一个值，写 “n ≥ 51” 不给分（S24 Q4(c)，MS p.9）。
15. **抽样分布**。
    - 取值要全，不能有多余的值；不可能出现的值要写概率 0（O24 Q6，MS p.11）。
    - 二项系数不能漏：J23 Q2(d) 漏了 3（ER p.3）；J24 Q6(a) 把 6 写成 4（ER p.6）。
    - 看清问的是哪个统计量：J23 Q2(e) 问众数，有人去求中位数（ER p.3）；O23 Q4(b)–(c) 有人列了尺码而不是售价，或求了总和而不是中位数（ER p.4）。
    - 检查概率之和为 1：O22 Q6(b) 常漏 R = 0（ER p.5）；O23 Q4(c)（ER p.4）。
    - 不放回时，用放回的概率按特殊情况封顶（S24 Q4(b)，MS p.9）。
    - 定义要写出 “all the values of a statistic” 和 “associated probabilities”（J22 Q6(a)，MS p.13；O25 Q3(a)，MS p.9）。
16. **普查、抽样框、统计量、模型假设：措辞要准确**。
    - 抽样框是**全体**成员（或店铺）的名单。“list of all stocktaking systems” 是 B0（S24 Q3(a)，MS p.8）；S23 Q2(b)(i) 中 “all members” 很少有人写出（ER p.4）。
    - 抽样单位是一个成员，不是“成员的意见”（S23 Q2(b)(ii)，MS p.7；ER p.4）。
    - 统计量只由样本值算出，“because it is known” 不给分（J25 Q2(i)，MS p.8）。
    - 模型假设要放进语境：Poisson 写 singly、independently、constant rate，并提到投诉、顾客、销售等对象（J23 Q1(b)，ER p.3；O23 Q5(a)，ER p.5；O24 Q3(b)，MS p.8）。二项题已经给出 n 和两种结果时，只有“独立”和“概率不变”给分（J24 Q3(a)，ER p.4）。
17. **精度**。
    - 非精确答案保留 3 位有效数字：S23 Q1(a)(i) 写 0.026，应为 0.0259（ER p.3）；J24 Q2(b) 写 0.034，应为 0.0341（ER p.4）。
    - 要化成一个数：J23 Q4(a) 不能停在 9πk/20（ER p.4）。
    - 百分误差要写成百分数，不能写 0.037（J25 Q1(c)，MS p.6）。
