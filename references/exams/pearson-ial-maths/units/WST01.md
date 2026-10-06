# WST01 · S1 Statistics 1：考纲摘要

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文关键词照抄考纲。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。S1 在印刷 pp.53–56（PDF pp.59–62）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。页码写印刷页码（FB 印刷页 = PDF 页 − 6）。
- 公式、上下标和 ≤ 号都对照渲染页图核过（`registry/work/stat-spec/pg-59.png`–`pg-62.png`），因为纯文本抽取会丢掉 ≤ 号和上标。版面文本：`registry/work/stat-spec/lay_p059.txt`–`lay_p062.txt`。
- 试卷封面只用来补充考场要求，不是考纲：`registry/src/WST01/2026-01_01_qp.txt`（WST01/01，Wednesday 14 January 2026，P78914A）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WST01/01**。另有区域卷 **WST01/01A**，考纲里没有这个代码。英国文化协会中国区 2025 年 10 月、2026 年 10 月以及 2026 年 1 月、6 月都以 WST01A 报名。已见到 2025 年 10 月（Friday 17 October 2025，P87446A）和 2026 年 1 月（P87600A）的 /01A 试卷和评分方案，两份都是题目卷加单独寄送的答题册（“Answer book (sent separately)”） | SPEC p.8、p.78；versions.md §1.6；`inventory/stat-gaps.md`；`registry/src/WST01/2025-10_01A_qp.txt`、`2026-01_01A_qp.txt` 封面 |
| 单元名称 | Unit S1: Statistics 1；p.67 表中写作 “S1: Statistics 1” | SPEC p.53、p.67 |
| AS/A2 定位 | 单元页原文：“Optional unit for IAS Mathematics and Further Mathematics”，“Optional unit for IAL Mathematics and Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IAS**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.53、p.67、p.8 |
| 资格结构 | IAS Mathematics：P1、P2 必考，再从 M1、S1、D1 中选一门。IAL Mathematics：P1–P4 必考，选修组合五选一，其中含 S1 的是 “M1 and S1”“S1 and D1”“S1 and S2”。IAS/IAL Further Mathematics 都可选 S1 | SPEC p.10 |
| 时长与分值 | 1 hour and 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.53 |
| 题量（参考） | 2026 年 1 月卷封面写 “There are 7 questions”，总分 75。这只是该卷的情况，考纲没有固定题量 | `registry/src/WST01/2026-01_01_qp.txt` |
| 计算器 | 允许使用，规则见 Appendix 6：不得带 symbolic algebra、symbolic differentiation or integration 功能，计算器里不得存有可调出的公式 | SPEC p.53；p.86 |
| 卷面要求（试卷封面，不是考纲） | 统计表查出的值要 “quoted in full”；用计算器代替查表时，结果要保留到相当的精度。非精确答案默认保留 3 位有效数字 | 2026-01 QP 封面 |
| 公式册 | 考试提供 FB（试卷封面：“Mathematical Formulae and Statistical Tables (Yellow), calculator”）。S1 部分在 FB pp.14–17。FB p.14 原话：“Candidates sitting S1 may also require those formulae listed under Pure Mathematics P1 and P2.”这句是 Issue 2 新加的 | SPEC p.53；FB p.14；FB PDF p.3 变更说明 |
| 开考季 | **January, June and October**。p.70 注：从 2020 年 6 月起，October 只考 P1–P4、M1、M2、S1、S2。2020 年 6 月以前，S1 在 2019 年 6 月、2019 年 10 月、2020 年 1 月开考 | SPEC p.8、p.70；versions.md §1.4 |
| 特殊考季 | 2020 年 6 月整季取消。2021 年 6 月发布了试卷和评分方案，但考试取消，改用教师评估成绩，没有考官报告 | versions.md §1.5 |
| 2018 版首考 | **“First assessment: June 2019.”** 实际第一次开考就是 2019 年 6 月 | SPEC p.53；versions.md §1.4 |
| 旧考纲同代码 | 2013 版旧考纲也用 WST01，最后一次是 **2019 年 1 月**，不算本考纲的真题。p.1 说 “The Further, Mechanics and Statistics units have not changed”，所以旧卷内容兼容，可作额外练习。Pearson 官网把 2019 年 6 月、2019 年 10 月、2020 年 1 月的 WST01 放在 2013 文件夹里，但按首考日期它们属于 2018 版 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | **S1.2 没有 “Prerequisites” 这一条**，直接从 “1. Examination” 开始。S2、S3 都有这一条（p.57、p.60）。考纲里与先修最接近的说法只有 FB p.14 那句：可能用到 P1、P2 的公式 | SPEC p.53；FB p.14 |
| 评估目标分配（75 分中） | AO1 20–25；AO2 20–25；**AO3 15–20**（建模，S2、S3 只有 10–15）；AO4 5–10；AO5 5–10 | SPEC p.69 |
| 须背公式（不在 FB 里） | 考纲原文：“Formulae that students are expected to know are given below and will **not** appear in the booklet”。清单见本文件 §3 | SPEC pp.53–54 |
| 单位 | “Questions will be set in SI units and other units in common usage.” | SPEC p.53 |
| 记号 | Appendix 7 第 10 节 Probability and statistics（pp.91–92）：A′ 表示补事件，P(A \| B) 表示条件概率，p(x) = P(X = x)，F(x) 表示 P(X ≤ x)，x̄ 表示样本均值，r 表示样本的 product moment correlation coefficient，Φ 表示标准正态的累积分布函数等 | SPEC pp.91–92 |
| 单元概述 | “Mathematical models in probability and statistics; representation and summary of data; probability; correlation and regression; discrete random variables; discrete distributions; the Normal distribution.” | SPEC p.53 |

---

## 2. 规格条目逐条（S1.3 Unit content）

### 主题 1 Mathematical models in probability and statistics（p.55）

**1.1 The basic ideas of mathematical modelling as applied in probability and statistics**（p.55）
- 要求：理解概率统计中的数学建模思想。指导栏为空，考纲没有进一步说明考法。
- 相关：S1 的 AO3（建模）占 15–20 分，是 S 系列里最高的（p.69）。

### 主题 2 Representation and summary of data（p.55）

**2.1 Histograms, stem and leaf diagrams, box plots**（p.55）
- 要求：用 histograms、stem and leaf diagrams、box plots **比较分布**（“to compare distributions”）。可能考 **back-to-back stem and leaf diagrams**。
- 排除：“Drawing of histograms, stem and leaf diagrams or box plots will not be the direct focus of examination questions.”（画图本身不是直接考点；2.4 例外，可能要求在箱线图上标出 outliers。）

**2.2 Measures of location – mean, median, mode**（p.55）
- 要求：对集中趋势与离散程度的度量 “draw simple inferences and give interpretations”。数据可以是 “discrete, continuous, grouped or ungrouped”。要求 **“Understanding and use of coding.”**
- 排除：“Calculation of mean, mode and median, range and interquartile range will not be the direct focus of examination questions.” “Significance tests will not be expected.”

**2.3 Measures of dispersion – variance, standard deviation, range and interpercentile ranges**（p.55）
- 要求：方差、标准差、极差、**interpercentile ranges**。指导栏：“Simple interpolation may be required. Interpretation of measures of location and dispersion.”
- 公式：标准差 = √(variance)、IQR = Q₃ − Q₁ 须背（p.53）；数据方差的计算式不在 FB 里，也不在须背清单里（见 §3）。

**2.4 Skewness. Concepts of outliers**（p.55）
- 要求：偏态（skewness）与异常值（outliers）概念。可能要求在 box plot 上标出 outliers 的位置。
- 关键限制：“Any rule to identify outliers will be specified in the question.”（判定异常值的规则由题目给出，不需要背某个固定规则。）

### 主题 3 Probability（p.55）

**3.1 Elementary probability**（p.55）
- 要求：基础概率。指导栏为空。

**3.2 Sample space. Exclusive and complementary events. Conditional probability**（p.55）
- 要求：样本空间，互斥事件与对立事件，条件概率。会理解并使用 P(A′) = 1 − P(A)、P(A ∪ B) = P(A) + P(B) − P(A ∩ B)、P(A ∩ B) = P(A) P(B | A)。
- 公式：P(A′) = 1 − P(A) 须背（p.53）；后两式在 FB p.14。

**3.3 Independence of two events**（p.55）
- 要求：两事件独立：P(B | A) = P(B)，P(A | B) = P(A)，P(A ∩ B) = P(A) P(B)。
- 公式：这三式都在须背清单里（p.53），FB 不给。

**3.4 Sum and product laws**（p.55）
- 要求：加法与乘法法则；使用 **tree diagrams** 和 **Venn diagrams**；“Sampling with and without replacement.”

### 主题 4 Correlation and regression（p.56）

**4.1 Scatter diagrams. Linear regression**（p.56）
- 要求：用 **method of least squares** 计算线性回归直线方程；可能要求把回归直线画在散点图上。
- 公式：Sxx、Syy、Sxy、b = Sxy/Sxx、a = ȳ − b x̄ 都在 FB p.15。

**4.2 Explanatory (independent) and response (dependent) variables. Applications and interpretations**（p.56）
- 要求：区分 explanatory (independent) 与 response (dependent) variables。用回归直线在**解释变量的取值范围内**做预测，并认识 “the dangers of extrapolation”。变量名可以不是 x、y。“Linear change of variable may be required.”（即回归中的编码换元。）
- 排除：“Derivations will not be required.”

**4.3 The product moment correlation coefficient, its use, interpretation and limitations**（p.56）
- 要求：product moment correlation coefficient（r）的计算、使用、解释与局限。
- 排除：“Derivations and tests of significance will not be required.”（相关系数的显著性检验在 S3 5.2。）
- 公式：r 的公式在 FB p.15（Issue 2 更正过该式，见 §5）。

### 主题 5 Discrete random variables（p.56）

**5.1 The concept of a discrete random variable**（p.56）
- 要求：离散随机变量的概念。指导栏为空。

**5.2 The probability function and the cumulative distribution function for a discrete random variable**（p.56）
- 要求：简单使用概率函数 p(x)，其中 p(x) = P(X = x)；使用累积分布函数 F(x₀) = P(X ≤ x₀) = Σ_{x ≤ x₀} p(x)。
- 公式：F(x₀) 的定义式须背（p.54）。

**5.3 Mean and variance of a discrete random variable**（p.56）
- 要求：用 E(X) 和 E(X²) 计算 X 的方差。“Knowledge and use of” E(aX + b) = aE(X) + b，Var(aX + b) = a² Var(X)。
- 公式：E(X)、Var(X)、E(g(X)) 在 FB p.14；E(aX + b)、Var(aX + b) 须背（p.53）。

**5.4 The discrete uniform distribution**（p.56）
- 要求：离散均匀分布，以及 “The mean and variance of this distribution”。
- 公式：FB 没有离散均匀分布的均值和方差（S1、S2 两节都核过，FB 只给了连续均匀分布，在 S2 节 p.18），须背清单里也没有。对取值 1, 2, …, n 的离散均匀分布，均值 (n + 1)/2、方差 (n² − 1)/12。这是数学事实，不是考纲原文；考纲也没说是否要求推导。

### 主题 6 The Normal distribution（p.56）

**6.1（考纲印作 “5.1”）The Normal distribution including the mean, variance and use of tables of the cumulative distribution function**（p.56）
- 编号：考纲在 “6. The Normal distribution” 标题下把这一条印成 “5.1”，与主题 5 的 5.1 重号（已在渲染页 pg-62.png 上核对）。目录 `spec-items.stat.json` 中键名为 `"5.1#2"`，做法与 `spec-items.fm.json` 中 WFM02 的 `"7.1#2"` 一致。
- 要求：正态分布的均值、方差，使用累积分布函数表。必须知道分布的**形状和对称性**（“Knowledge of the shape and the symmetry of the distribution is required”）。“Questions may involve the solution of simultaneous equations.”（例如由两个概率反求 μ 和 σ。）
- 排除：“Knowledge of the probability density function is not required.” 均值、方差、累积分布函数的推导都不要求。“Interpolation is not necessary.”（查 Φ 表不需要插值。）
- 公式：标准化 Z = (X − μ)/σ（X ∼ N(μ, σ²)）须背（p.54）。FB 给出 Φ(z) 表（p.16，z 从 0.00 到 4.00）和 Percentage Points Of The Normal Distribution 表（p.17，p = 0.5000 到 0.0005），正态的概率密度函数也印在 FB p.14，但考纲说不要求掌握。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| Mean = x̄ = Σx/n 或 Σfx/Σf | **须背**（考纲明列） | SPEC p.53 |
| Standard deviation = √(variance) | **须背** | SPEC p.53 |
| Interquartile range = IQR = Q₃ − Q₁ | **须背** | SPEC p.53 |
| P(A′) = 1 − P(A) | **须背** | SPEC p.53 |
| 独立事件：P(B \| A) = P(B)，P(A \| B) = P(A)，P(A ∩ B) = P(A) P(B) | **须背** | SPEC p.53 |
| E(aX + b) = aE(X) + b，Var(aX + b) = a² Var(X) | **须背** | SPEC p.53 |
| F(x₀) = P(X ≤ x₀) = Σ_{x ≤ x₀} p(x) | **须背** | SPEC p.54 |
| Z = (X − μ)/σ，X ∼ N(μ, σ²) | **须背** | SPEC p.54 |
| P(A ∪ B) = P(A) + P(B) − P(A ∩ B)；P(A ∩ B) = P(A)P(B \| A)；P(A \| B) = P(B \| A)P(A) / [P(B \| A)P(A) + P(B \| A′)P(A′)] | FB 给出 | FB p.14 |
| E(X) = Σxᵢ P(X = xᵢ)；Var(X) = Σ(xᵢ − μ)² P(X = xᵢ) = Σxᵢ² P(X = xᵢ) − μ²；E(g(X)) = Σg(xᵢ) P(X = xᵢ) | FB 给出 | FB p.14 |
| 正态分布 N(μ, σ²) 的 P.D.F.、均值 μ、方差 σ² | FB 给出（考纲说不要求掌握 pdf） | FB p.14；SPEC p.56 |
| Sxx、Syy、Sxy；r = Sxy/√(SxxSyy) 及其展开式；b = Sxy/Sxx；y = a + bx，a = ȳ − b x̄ | FB 给出 | FB p.15 |
| Φ(z) 表；正态分布百分点表 | FB 给出 | FB pp.16–17 |
| 数据的方差计算式（如 Σx²/n − x̄²、Σfx²/Σf − x̄²）；编码（coding）对均值和标准差的影响；分组数据用插值求中位数和四分位数；离散均匀分布的均值与方差 | FB **未给**，须背清单也**没有**；但 2.2、2.3、5.4 要求会用 | SPEC pp.53–56；FB pp.14–17（已核对没有） |
| P1、P2 的公式 | FB 给出，S1 可能用到 | FB p.14 那句说明；FB p.3 |

---

## 4. 与相邻单元的界线

- **P1/P2**：S1 的单元页没有先修条目，但 FB p.14 写明可能用到 P1、P2 的公式。考纲在 6.1 写明可能要解联立方程。
- **S2（以 S1 为先修）**：
  - **binomial 和 Poisson 分布不在 S1**。S1 5.4 只点名了离散均匀分布，B(n, p) 和 Po(λ) 在 S2 1.1（p.58）。S1 3.4 的 “Sampling with and without replacement” 与树形图、Venn 图写在同一条指导里，考纲没有在 S1 提二项分布。
  - 连续随机变量、概率密度函数、连续均匀分布 → S2 主题 2、3.1。S1 6.1 明确不要求正态的 pdf。
  - 用正态分布近似二项分布和 Poisson 分布、continuity correction → S2 3.2。S1 只用正态表，不做近似。
  - 假设检验（critical region、单尾/双尾）→ S2 主题 4。S1 2.2 写明 “Significance tests will not be expected”，4.3 写明相关系数不考显著性检验。
  - population、census、sampling frame 等抽样概念 → S2 4.1–4.2。
- **S3（以 S1、S2 为先修）**：
  - 相关系数为零的假设检验（product moment 和 Spearman）→ S3 5.1–5.2（p.62）。S1 4.3 只算和解释 r。
  - 独立正态随机变量的线性组合，如 X₁ + X₂、aX ± bY → S3 1.1。S1 只到 E(aX + b)、Var(aX + b)。
  - 样本均值的分布、置信区间、无偏估计 s² → S3 主题 3。
  - 抽样方法（simple random、stratified、systematic、quota）→ S3 2.1–2.2。

---

## 5. 印刷问题与缺口

- **6.1 重号**：主题 6 唯一一条被印成 “5.1”（p.56，已在渲染页核对）。目录键为 `"5.1#2"`，附 note。
- **Appendix 7 编号跳号**：第 10 节从 10.9 直接跳到 10.11，没有 10.10（p.91，渲染页 `registry/work/stat-spec/pg-97.png` 核对）。不影响内容。
- **FB Issue 2 更正了 r 的公式**（FB p.15；变更说明在 FB PDF p.4，已放大渲染核对，`registry/work/stat-spec/fb-pdf4-r.png`）：第三种写法（展开式）的根号，旧版只盖住分母里的第一个括号，Issue 2 改为盖住两个括号的乘积。用旧版公式册（Issue 1）的学生要注意。
- 考纲对 2.3 的 “interpercentile ranges”、1.1 的建模思想都没有给出具体考法，要从真题和评分方案里确认。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否另有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 逐题索引与审核（2026-10-06）

**索引文件**：同目录 `WST01.questions.json`。它由 `WST01.questions.part1.json`（2019-06 至 2022-10，10 份卷，63 题）和 `WST01.questions.part2.json`（2023-01 至 2026-01，12 份卷，84 题）合并而成。按 id 去重（没有重复 id），再按考季、卷号（同一考季 /01 在 /01A 前）、题号排序。注意 part 2 文件里 2025-10、2026-01 两季是 /01 与 /01A 按题号交替排列的，合并文件改成了先 /01 后 /01A。构建记录见 `WST01.coverage.part1.md`、`WST01.coverage.part2.md`。

审核脚本和输出都在 `registry/work/wst01audit/`：
- 脚本：`scripts/merge_validate.py`（合并与格式校验）、`completeness.py`（与清单比对）、`checks.py`（小问分值、评分代码、MS 页码与数值、引文、命令词）、`labelcheck.py`（所引 MS 页是否有该小问的标号）、`er_span.py`（所引 ER 页是否落在该题的评论范围内）、`pua.py`（QP 文本层丢失的私用区字形，如 ⩽ ⩾）、`show.py`、`qtext.py`、`page.py`、`dump.py`（逐题调出索引、QP、所引 MS 页和 ER 页）、`apply_fixes.py`、`stats.py`、`shapes.py`。
- 输出：`validate.txt`、`completeness.txt`、`checks.txt`、`pua.txt`、`stats.txt`、`byitem.txt`（按主条目列出全部小问）、`shapes_rough.txt`（关键词粗筛，有误报，第 7 节的题型计数以人工核对为准）。
- 改动清单：`fixes.json`（16 条）；改动前的两个 part 文件和本文件备份在 `backup/`。渲染核对图在 `img/`。

**收录范围**：22 份卷，147 题，645 个小问，1650 分。

| 考季 | 卷 | 题数 | QP、MS 来源 | ER |
|---|---|---|---|---|
| 2019-06（2018 考纲首考） | /01 | 6 | GitHub `RayZ3R0/papernexus-finder`（PMT 戳记的 Pearson PDF），本地 `src/WST01/` | 缺 |
| 2019-10 | /01 | 7 | **只有 Edexcel-Finder 文本**（igexams 水印，小写化，部分符号被替换）；MS 缺 | 缺 |
| 2020-01 | /01 | 6 | **只有 Edexcel-Finder 文本**（原始 JSON 干净，数值可核）；MS 缺 | 缺 |
| 2020-10（封面 Thursday 4 June 2020，10 月实考） | /01 | 6 | papernexus | 缺 |
| 2021-01 | /01 | 6 | papernexus | 缺 |
| 2021-06（考试取消，只发布了试卷和 MS） | /01 | 6 | papernexus | 本季没有 ER |
| 2021-10 | /01 | 6 | papernexus | 缺 |
| 2022-01 | /01 | 7 | papernexus | 缺 |
| 2022-06 | /01 | 6 | papernexus | 缺 |
| 2022-10 | /01 | 7 | examsolutions S3 镜像（Pearson 原文件名） | 有 |
| 2023-01 | /01 | 6 | S3 镜像；Drive 有同尺寸副本 | 有 |
| 2023-06 | /01 | 7 | S3 镜像；Drive 有 MS 重存版 | 有 |
| 2023-10 | /01 | 6 | S3 镜像；Drive 有 MS 重存版 | 有 |
| 2024-01 | /01 | 8 | S3 镜像；Drive 有 QP、MS 重存版 | 有 |
| 2024-06（P75720RA） | /01 | 6 | Drive | 缺 |
| 2024-10 | /01 | 8 | Drive | 缺 |
| 2025-01 | /01 | 7 | Drive（MS 用 Results 版，Final 版在 `src/WST01/alt/`） | 缺 |
| 2025-06 | /01 | 7 | Drive | 缺 |
| 2025-10 | /01 | 8 | Drive | 缺 |
| 2025-10 | /01A | 7 | Drive（P87446A，第一份 S1 区域卷；PDF 后半是答题册） | 缺 |
| 2026-01 | /01 | 7 | Drive（只找到 MS Final 版） | 缺 |
| 2026-01 | /01A | 7 | Drive（P87600A；只找到 MS Final 版） | 缺 |

**格式校验**（`merge_validate.py`，结果 0 个问题，`validate.txt`）
- 每条记录字段齐全；各小问分值之和等于题目总分；每卷 75 分，题号连续。
- 所有 spec id 都在 `spec-items.stat.json` → `WST01` 中（`"5.1#2"` 是考纲第 6 主题被印成 “5.1” 的正态分布条目，见 §2）；series 都是 YYYY-MM，月份只有 01、06、10；id 与考季、卷号、题号一致。
- 引号内文字都不超过 25 词。有 MS 的 20 份卷全部 586 个小问都有 MS 要点；`er` 恰好在有 ER 的 5 季（O22、J23、S23、O23、J24，34 题、137 个小问）填写；2019-10、2020-01 两份没有 MS，`ms` 为空，`final_form` 只写题目要求的形式，没有自行计算答案。

**自动比对**（`checks.txt`）
- **小问分值**：从 QP 文本（2019-10、2020-01 用 Finder 文本）逐题读出印刷的 "(n)" 和 "Total for Question n"，147 题的小问分值顺序和总分全部一致。
- **评分代码求和**：把 `ms` 中的 B1、M1、A1、dM1、A1ft 等按小问求和。余下 18 处标记都已逐条看过，全是脚本误报：代码写在被去掉的括号里（如 "M1 P(…)/P(…)"），或说明里的 "M1M0A0" 一类特例，或 "B1 each value"。
- **MS 页码**：每个小问都引了 MS 页，页面都存在且有该题的评分行（`labelcheck.py` 还要求所引页上有该小问的标号）。`final_form` 中 478 个小数逐个在所引 MS 页上查找，找不到的 6 个都核对过：S23 Q6(c) 的 0.07、0.06 在 MS 的 Venn 图图片里；O23 Q3(i)(c) 的 0.786 是 MS 的 0.7857…；O24 Q3 的 0.07、0.59、0.3125 是 MS 分数 14/200、118/200、25/80 的小数。
- **ER 页码**：137 个 `er` 字段所引页码都落在该题的评论范围内（`er_span.py`）。
- **引文**：47 处加引号的短语，46 处逐字在原文找到；剩下的 O25 Q3(b) 'normal uniform' 是文本层把一行拆开，渲染 MS p.9 核对无误（`img/ms2510p9-09.png`）。
- **丢失符号**：QP 文本层把 ⩽、⩾ 丢成私用区字形（U+F084、U+F085），`pua.py` 列出全部出现位置（`pua.txt`）。除组距表外，涉及答案的只有 J22 Q4(a) P(2 ⩽ W < 3.5)、O22 Q5 的分级表、J23 Q6 的 10 ⩽ x ⩽ 80、S23 Q3(c) 的 4600 < w ⩽ 7700、S23 Q5(b) P(1 < Y ⩽ 4)、S23 Q5(d) P(Y ⩾ X)、J25 Q1(e) P(R + B ⩽ 5)，逐一对照索引：只有 S23 Q5(d) 读错（改正 F1–F2）。
- **命令词**：58 处标记都看过，都不是错误：共用题干的 "Find the exact value of (b)… (c)…"、合并小问写成 "Find; Show that"，以及 2020-01 全卷（part 1 的清洗文件 `work/wst01p1/clean/2020-01_finder.txt` 把题号和小问标号错误地做了字形替换，如 "NK&" 代表 "1."，脚本定位不到小问；原始 JSON `2020-01_finder_raw.txt` 是干净的）。

**完整性**（`completeness.txt`）
- **预期考季**：据 `versions.json` 和 `src/expected_series.json`，2018 考纲下 WST01 到 2026-06 共 21 季：2019-06、2019-10、2020-01，2020-10 起每年 1、6、10 月。2020-06 整季取消（试卷改在 2020-10 使用）。
- **收录情况**：有 QP 文本的 20 季 22 份卷全部收录，没有漏卷。`inventory/stat.json` 的 WST01 条目、`finder/finder-inventory.tsv` 中 17 份 2018 考纲卷（2019-06 至 2025-01）都在索引内。
- **不收**：Finder 的 SAM（S59767A）是样卷；2014-01 至 2019-01 的 13 份同代码卷属于 2013 旧考纲（S1 内容未变，可作额外练习）；`src/WST01/2026-04_01A_specimen-ab.pdf` 是区域卷答题册样本，没有题目；Drive 上的 `26数学大考IAL-S1预测卷.pdf` 是第三方预测卷。
- **所有来源都拿不到的卷**：2026-06 WST01/01 与 WST01/01A（QP、MS、ER 全缺；英国文化协会中国区本季有 WST01A 报名，所以 /01A 应当存在）。2025-06 是否有 /01A 卷不明。（critic 2026-10-06：grademax 的 Pearson 链接索引 `finder/gh/grademax_maths_index.json` 里 2025 年 6 月只有 WMA11–WMA14、WFM02、WME02 有 /01A，本单元没有，所以这份卷很可能没有出过；属中等可信的指针，不是缺口。）2026-10-06 审核时再查 Drive（标题含 S1/WST01/wst01/Statistics、2026-05-15 以后修改的文件），只找到笔记、S2 材料和已收录文件。
- **缺 MS**：2019-10、2020-01（Pearson 文件名见 `inventory/stat-gaps.md`）。2026-01 两份只有 Final 版，页码按 Final 版。
- **缺 ER**：除 O22、J23、S23、O23、J24 外的全部考季（2021-06 本来没有 ER；/01A 卷是否另出 ER 不明）。

**准确性抽查**
- **抽查范围**：对照 QP、MS、ER 原文逐条复核 97 题，覆盖全部 22 份卷和全部 17 个条目。
  - part 1（10 份卷）抽 13 题，每份卷至少 1 题：S19 Q1、Q4；O19 Q3；J20 Q5；O20 Q2；J21 Q2；S21 Q5；O21 Q4；J22 Q1、Q4；S22 Q2；O22 Q5、Q6。O19、J20 没有 MS，只核对题意、分值和形式。13 题没有发现错误。
  - part 2 先抽 10 题时查出 4 处错误（S23 Q5、J24 Q4、J25 Q1、J25 Q4），错误集中在 part 2，于是把 **part 2 全部 84 题逐题复核**：每题都调出 QP 文本、所引 MS 页和 ER 页（`dump.py`），不看 MS 独立重算终点值后再与 MS 对照。
- **核对内容**：分值、spec 映射、命令词、题干数值（文本层丢失的分数、负号、⩽ ⩾ 都对照 MS 或渲染页）、终点形式、MS 要点（代码顺序、接受与不接受的答案、特例）、ER 要点。重算并与索引一致的终点值有 300 多个，例如 J23 Q6(d) 由回归线反推 Σx = 479.6、r = 0.988；S23 Q7(c) k = 42.2、r = 476；O23 Q6 交点 (25/12, 53/12) 与 r = √0.28；J24 Q8(b) μ = 6、σ = 2；O24 Q1 的众数 137 与四分位数 106、129、126；S25 Q6(d) k = 505；O25 Q8(c) 6/13、9/52、19/52；J26 Q3(b) 的 Venn 区域 36、4、21、16；J26A Q5(c) 均值 1.4125、标准差 0.347。

**改正**（合并文件和对应 part 文件同步修改，清单见 `work/wst01audit/fixes.json`）
1. **错误（6 处，改 8 个字段）**
   - F1–F2 S23 Q5(d)：QP 原文是 P(Y ⩾ X)（渲染 `img/qp2306p16_top.png`），索引写成 P(Y > X)，MS 要点也写成 "Y > 15 − 2Y"。按 > 计算答案会是 1/30，而不是 3/5。已改为 ⩾（MS p.10，`img/ms2306p10_d.png`）。
   - F5 J25 Q1(d)：MS 规则写反了。索引原写 "21 stated alone is M0"；MS p.6 是 E(B²) = 21 可推出 M1，**21/4 才是 M0**。
   - F6–F8 J25 Q4(b)、(c)(i)、(c)(ii)：引 MS p.12，实际评分在 p.11（p.12 是 Q5），已改。
   - F9 J24 Q4(e)：引 MS p.10，实际在 p.9，已改。
2. **遗漏（2 处）**：F3–F4 S23 Q5(b)(c) 题目要 "exact value"，但 MS p.10 也接受 awrt 0.333、awrt 4.33，补进 `final_form`。
3. **页码精度（1 处）**：F10 J26A Q3(f) 的评分行在 MS p.10、注释在 p.11，改为 "MS pp.10-11"。
4. **引文（6 处）**：F11 J23 Q6(a) 改为 ER 原话 'as x increases then y increases'；F12 S23 Q2(e) 改为 'the weight would be negative'；F13 O22 Q1(d)、F14 J23 Q6(c)、F15 J25 Q6(b)、F16 J26A Q2(c) 把引号内的转述改回 MS 原文措辞。
5. **错误分布**：6 处实质错误全在 part 2（S23、J24、J25 两题），已对 part 2 全卷复核；页码类错误又用 `labelcheck.py` 对全部 645 个小问扫过；符号丢失类错误用 `pua.py` 对全部 QP 扫过。part 1 抽查和全索引扫描都没有发现同类错误。

**保留未改的差异**（coverage 文件是构建记录，没有改动，以本节和索引为准）
- `inventory/stat.json` 和 `stat-gaps.md` 仍把 2019-06 至 2022-06 的 QP、MS 记为缺失；part 1 已从 papernexus 补齐 PDF（`WST01.coverage.part1.md` "New sources found in this pass"）。
- O19 的几处读法没有 PDF 可核：Q1 编码的除数、Q5 的撇号、Q6(a) 的不等号、Q7 的 Y 分布，Q2、Q4 的图无法恢复（见 coverage part 1）。这些小问的 `final_form` 只写形式。
- part 1 的工作文件 `work/wst01p1/clean/2020-01_finder.txt` 有上面说的标号替换，但索引是按干净的原始 JSON 写的，J20 的题意、数值和分值都不受影响（J20 Q5 已对照原始文本核对）。

---

## 7. 真题需求概览

**数据范围**
- 本节统计第 6 节收录的 22 份卷：S19、O19、J20、O20、J21、S21、O21、J22、S22、O22、J23、S23、O23、J24、S24、O24、J25、S25、O25、O25A、J26、J26A。共 147 题、645 个小问、1650 分。
- 20 份卷有 MS（O19、J20 没有）；有 ER 的只有 O22、J23、S23、O23、J24 五份。
- 拿不到的卷见第 6 节"完整性"。

**统计方法**
- 数字由 `work/wst01audit/scripts/stats.py` 从索引算出，结果存于 `stats.txt`；题型计数由 `byitem.txt`（按主条目列出全部小问）和 `shapes_rough.txt` 人工核对得出。
- "问法、终点、评分"取自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节核对过（part 2 全部、part 1 抽查）。

**引用写法**
- J = January，S = June，O = October，后接两位年份；O25A、J26A 是 WST01/01A 区域卷。
- O20 用的是原定 2020 年 6 月的试卷；S21 的考试取消，但试卷和 MS 已发布。O19、J20 只有题目文本。
- 题号和小问按试卷印刷。MS、ER 页码见索引条目 `ms`、`er` 字段末尾的 "(MS p.n)"、"(ER p.n)"，下文只在需要时注出。

### 7.1 卷面结构

**题量与分值**
- 每卷 75 分、90 分钟。6 题的 10 份（S19、J20、O20、J21、S21、O21、S22、J23、O23、S24），7 题的 9 份（O19、J22、O22、S23、J25、S25、O25A、J26、J26A），8 题的 3 份（J24、O24、O25）。2024 年以后题数略增。
- 单题 4–17 分，最常见 13 分（26 题），其次 12 分（18 题）、14 分（18 题）、9 分（17 题）。每题 1–10 个小问，4 个小问最常见（45 题）。

**命令词**（645 个小问；复合小问的每个动词各计一次）

| 命令词 | 次数 |
|---|---|
| Find | 317 |
| Show that（另有 Show 1、Verify 1） | 65 |
| Calculate | 49 |
| Estimate | 39 |
| State | 33 |
| Write down | 25 |
| Complete（树形图、Venn 图、频数表） | 19 |
| Draw（箱线图、Venn 图、回归线） | 15 |
| Comment | 13 |
| Describe（几乎都是偏态） | 12 |
| Interpret / Give an interpretation | 12 / 9 |
| Determine、Explain | 各 8 |
| Use linear interpolation、Give、Hence find | 各 5 |
| Identify | 3 |
| Define（用文字描述事件） | 2 |
| Redraw、Plot、Work out、Discuss、Compare、Evaluate、Specify | 各 1 |

- 给定结果的小问（Show that、Show、Verify）共 66 个、158 分，约占 10%。按主条目分：4.1（印出回归线）11 个，正态 9 个，5.3 8 个，2.4（证明有几个异常值）7 个，5.2 6 个，3.2、3.4 各 5 个。
- "Describe / Comment / Interpret / Explain / State with a reason" 这类文字作答的小问每卷都有，集中在偏态、相关系数与斜率的解释、可靠性和模型适用性（见 7.4）。

**各主题分值**（按每个小问的第一个 spec 计）

| 主题 | 分值 | 占比 | 每卷分值范围 |
|---|---|---|---|
| 3 概率（Venn、树形图、条件概率、独立） | 392 | 24% | 10–28 |
| 2 数据的表示与概括 | 367 | 22% | 8–27 |
| 5 离散随机变量 | 313 | 19% | 7–27 |
| 4 相关与回归 | 301 | 18% | 11–19 |
| 6 正态分布（条目 `5.1#2`） | 275 | 17% | 7–18 |
| 1 建模 | 2 | 0% | 0–2 |

**每卷固定出现的题型**
- **22/22 份卷都有**：
  - 一道数据题（茎叶图 13 份、直方图 13 份、箱线图 12 份，常两种合在一题）：求中位数、四分位数、IQR，用题目给的规则判断异常值，描述偏态，比较两组分布。
  - 一道相关与回归题：由汇总统计量求 S_xy、S_xx、S_yy，算 r，求或证明回归线，解释斜率，判断估计是否可靠。只有 O23 Q6 换成由两条回归线求均值、S_xy 和 r。
  - 一道概率题，必有条件概率（46 个小问）：Venn 图 17 份，树形图 13 份，两者都没有的只有 O25A（用放回与不放回取球的乘积）。
  - 一道离散随机变量题：E(X)、Var(X)，多数还有 Var(aX + b) 或由 Σp = 1 与 E(X) 解未知概率。
  - 一道正态分布题（第 3–8 题都出现过，多在后半卷），每题 5–17 分。
- **常见组合**：
  - 正态 + 条件概率（"在合格／未被排除的产品中……"）：13 份（S19、O19、O20、J21、S21、S22、O22、J23、J24、S24、O25、O25A、J26）。
  - 正态 + 由两个概率解 μ 和 σ（联立方程）：8 份（O19、S23、O23、J24、O24、J25、O25、J26A）；只解一个未知数（σ、μ 或 k）的又有 J20、J22、O23、J24、S24、S25、J26。
  - 正态 + 独立重复（"5 袋都少于……"、"3 次试跳内合格"、"4 袋中恰有 2 袋"）：8 份（S19、O19、J21、J22、S23、J24、S25、O25A）。
  - 正态 + 用四分位数定义的异常值：4 份（O19、J23、O24、J25）。
  - 离散随机变量 + 累积分布函数 F(x)（由 F 求概率分布或反过来）：13 份。
  - 回归 + 编码（线性变换后 r 不变、回归线还原）：O19、S23、J24、J25、S25、J26A。
  - 数据 + 编码求均值、方差：J22、S22、O22、S23、J24、S24、O25。

**题面限制语**
- "Using standardisation"（必须写出标准化）：2023 年起几乎每卷都有，共 10 题：J23 Q5(d)、S23 Q7、J24 Q5(a)、S24 Q5、J25 Q5(a)、S25 Q6(a)、O25 Q7(a)、O25A Q4、J26 Q7、J26A Q6(a)。
- "Solutions relying (entirely) on calculator technology are not acceptable"：O24 Q4、O24 Q6(c)。"You must show your working (clearly)"：J22 Q6、J24 Q4、J24 Q6、O23 Q5、O24 Q6、O24 Q7、S24 Q1、S25 Q5、S25 Q7、O25 Q4、O25 Q7、O25A Q4、J26 Q6，共 13 题。
- 题目给出公式或规则：异常值规则每次都写在题里（多为 1.5 × IQR，S22 Q1(b) 用 1.0 × IQR，J25 Q7(d) 用"均值以上 2 个标准差"）；偏态系数也由题目给出（J20 Q4(e) 3(均值 − 中位数)/标准差，S22 Q1(d)、O22 Q1(d) 两种四分位数公式，O24 Q1(d) (均值 − 众数)/标准差）。
- 默认答案保留 3 位有效数字；题目另行指定精度的有 29 个小问（如 O22 Q5(b)(c) 1 位小数、O25A Q4(b) 4 位有效数字、J22 Q5(b) 2 位小数）。

### 7.2 每个考纲条目怎么考

- "卷数／题数／小问／涉及分值"按标签出现的任何位置统计。一个小问可以带几个标签，所以各行相加会超过 147 题、1650 分。
- 括号内的"主"表示该条目作为第一个标签时的小问数和分值。

| 条目 | 卷数／题数／小问／涉及分值 | 常见命令词（主） | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 建模思想 | 12／16／20／50（主 2／2） | Give 1，Comment 1 | 直接问只有一次："统计模型便宜快捷，再给一个使用模型的理由"（S25 Q3(a)）。其余都是附在别的条目上的模型判断：正态模型是否合适、用期望判断是否值得玩、模型能否用于决策 | 一句话；1–2 分 | S25 Q3(a)；S25 Q5(f)；S19 Q5(e) |
| 2.1 直方图、茎叶图、箱线图 | 22／29／57／148（主 37／103） | Draw 10，Calculate 6，Find 6，Estimate 6，Complete 3，Give 2 | **画箱线图并标出异常值**（10 份卷 11 次：S19、O20 两次、J21、O21、S22、O23、S24、O25、O25A、J26），常画在给出另一组箱线图的同一坐标上。**直方图**：已知一根柱的宽和高（或面积），求另一根柱的宽和高（8 份）；由直方图补频数表或估计某区间人数（5 份）；"为什么用直方图"答"数据连续"（O24 Q5(a)、J26A Q5(b)）。**茎叶图**：读出缺失的叶子（S22 Q1(a)、S24 Q1(a)），由四分位数反求未知值（J22 Q3(a)、J25 Q2(c)、S24 Q1(f)） | 箱线图 3–5 分（须两根须、半格精度）；柱宽柱高 2–3 分；区间人数取整 | O22 Q1(a)(b)；S25 Q5(a)(b)；J26 Q1(b) |
| 2.2 均值、中位数、众数 | 22／38／72／175（主 56／134） | Find 22，Estimate 10，State 6，Calculate 5，Use linear interpolation 4，Show that 4 | **茎叶图上读中位数或四分位数**（13 份）；**线性插值求中位数或四分位数**（12 份）；**分组数据的均值**（用组中值）；**编码数据还原均值**（J22、S22、O22、S23、S24、O25）；**合并两组**求总均值或反求一组均值（J21 Q6(c)、S25 Q2(a)、J25 Q2(e)）；**不计算说明增减**：加入等于均值或对称的两个值、改正记错的值（S19 Q1(c)、J20 Q4(f)、S24 Q3(e)、S25 Q2(c)、O25A Q7(c)、J26A Q5(f)）；用统计量比较两组并结合语境（O21 Q3(e)、O23 Q2(d)、S24 Q1(e)、O24 Q1(e)） | 插值中位数 awrt 3 s.f.，n 与 n + 1 都接受；比较须写出统计量名和两个数值；说明题要"结论 + 理由" | J23 Q1(c)；S23 Q1(b)；O24 Q1(e) |
| 2.3 方差、标准差、极差、百分位距 | 22／37／68／184（主 28／65） | Find 15，Estimate 4，Calculate 4，Show that 3 | 由 Σx、Σx² 求方差或标准差（默认除以 n，s 也接受）；编码后的方差、标准差（乘数平方、平移不变）；分组数据的标准差；四分位数与 IQR；由合并组的均值和标准差反求 Σy²（J25 Q2(e)）；不计算判断标准差增减（S19 Q1(c)、S24 Q3(e)、O25A Q7(d)）。**百分位距（如 10–90）从未出现** | 标准差 3 s.f.；show-that 要写出比印刷值更精确的中间值 | J24 Q2(a)；O25 Q5(c)；J25 Q2(d)(e) |
| 2.4 偏态、异常值 | 21／26／46／130（主 27／65） | Describe 11，Show that 7，Find 3，Determine 2 | **按题目给的规则求异常值界限并指出异常值**（17 份卷）：show-that 型"证明恰有 1 个／2 个／没有异常值"最多；**描述偏态**：用四分位数比较 Q3 − Q2 与 Q2 − Q1（多数），或用均值与中位数，或按题目给的偏态系数计算（4 种公式）；改动数据后说明箱线图怎样变（J26 Q1(c)） | 界限值 + 结论；偏态方向 + 数值理由；1–4 分 | J21 Q2(c)；O23 Q2(b)；J26A Q2(c) |
| 3.1 初等概率 | 10／11／18／38（主 3／9） | Show that、Explain、Estimate 各 1 | 几乎不单独考。主标签只有 J21 Q6（圆片落在网格上的几何概率，再由实验频率估计 π）和 S24 Q6(e)（用 Venn 图概率估计人数）。作为副标签多是"由 Venn 图读概率" | — | J21 Q6 |
| 3.2 样本空间、互斥、对立、条件概率 | 22／51／89／250（主 64／147） | Find 50，State 4，Show that 4，Write down 3，Define 2 | **条件概率**每卷都有：由树形图（"已知后一个是红球，求前一个是黑球"）、由 Venn 图、由公式 P(A \| B) 反求未知概率。**加法公式**解未知数（S23 Q6(b)、J24 Q6(a)、S25 Q4）；**互斥**：指出哪两事件互斥、互斥时 P(A ∪ C) = P(A) + P(C)、用 P(C) + P(D) > 1 证明不可能互斥（J23 Q4(ii)）；用文字描述事件（O19 Q5(e)） | 精确分数或 3 s.f.；比值形式（分子 < 分母）；2–7 分 | J23 Q2(d)；S23 Q4(d)；J26A Q7(a)(b) |
| 3.3 两事件独立 | 19／27／36／114（主 22／60） | Find 15，Determine 5，Show that 2 | **检验是否独立**：写出所需概率并比较 P(A)P(B) 与 P(A ∩ B)（或 P(A \| B) 与 P(A)），给结论（O19、J20、O21、O23、J24、J25）；**已知独立求 Venn 图中的未知概率**（O20、S21、O21、S22、S24、O25、J26A）；独立重复的乘积（"5 件中恰 4 件……"、"至少一个"） | 数值比较 + 结论句；2–6 分 | J24 Q6(c)；O25 Q6(a)；S21 Q2(c) |
| 3.4 加法与乘法法则、树形图、Venn 图、放回与不放回 | 22／52／99／279（主 68／176） | Find 35，Complete 16，Show that 5，Draw 4，Calculate 3 | **补全树形图**（13 份，含"两次不放回""从一袋移球到另一袋""最多三局"）、**补全或画 Venn 图**（17 份，三圆，常有互斥或独立条件）；用乘法、加法求概率；**含参数的树形图**：n 个红球、n + 1 个黑球（O24 Q7），7x 个计数器（J26 Q5），比例 4 : 3 : 1 得二次方程（S25 Q7(e)） | Venn 图要外框、标签、所有区域（零写 0）；树形图每组分支和为 1；1–5 分 | S23 Q6(c)；O24 Q7；J26 Q5 |
| 4.1 散点图、最小二乘回归线 | 22／24／57／155（主 38／106） | Find 16，Show that 12，Calculate 4 | **求回归线**（13 份）或**证明印出的回归线**（8 份）；由原始和求 S_xy 等；特殊变化：加入一个位于均值处的点后 S_xy 不变（O20 Q5(d)），改正记错的数据后重算（J22 Q6(f)），由两条回归线的交点求均值（O23 Q6），在散点图上画线或圈出某点（S19 Q6(f)(g)、J21 Q5(g)(h)） | y = a + bx，a、b 3 s.f.，用题目的变量名，多数 MS 不收分数；证明题要写出 b、a 的更精确值；3–6 分 | S23 Q2(c)；O25 Q1(c)；J26A Q3(d) |
| 4.2 解释变量与响应变量；应用与解释 | 21／21／56／98（主 51／88） | Estimate 13，Find 8，Interpret 7，Comment 7，Give an interpretation 7，State 6 | **解释斜率**（13 份："x 每增加 1 单位，y 平均增加 b 单位"）；**用回归线估计**并**判断可靠性**（内插／外推，10 份）；**编码换元**后写出原变量的回归线（S23 Q2(g)、S25 Q3(g)、J26A Q3(e)）或说明编码对斜率、截距的影响（J25 Q6(e)）；由回归线求使某关系成立的范围（J22 Q6(e)、O22 Q2(f)）；某变化量对应的 x（S22 Q2(f)、S24 Q4(f)）；比较两条线的斜率作决策（J26A Q3(f)）。**指出响应变量**只考过一次（J26 Q2(b)） | 语境 + 数值 + 单位；可靠性要引用解释变量的取值范围；1–3 分 | J24 Q4(c)(e)；S22 Q2(e)；J26A Q3(e)(f) |
| 4.3 积矩相关系数 | 22／23／57／123（主 51／107） | Calculate 16，State 10，Find 10，Interpret 5，Show that 4，Write down 3 | **算 r**（每卷）；**在语境中解释 r**（7 份）；**判断是否支持线性模型**（r 接近 ±1，7 份）；**线性编码后 r 不变**（S23 Q2(f)、J24 Q2(d)、J25 Q6(e)）；w = 50 − p 时 r = −1（J22 Q2(b)）；由回归线和部分和反推 r（J23 Q6(d)，7 分）；由给出的 r 判断说法（S19 Q2(d)）；看散点图选 r（O19 Q4(a)） | r 3 s.f.（题目有时要求 3 d.p.）；解释要写变量名，不能只写"强正相关"；1–7 分 | S25 Q3(d)(e)；O25A Q1(b)–(d)；J23 Q6(d) |
| 5.1 离散随机变量的概念 | 2／2／2／5（主 1／1） | Write down 1 | 从未单独考定义。只有 J26A Q4(a) 写出 P(S = 1) = 0（"取到两只蓝袜为止"的取袜次数）和 O25A Q6(d) Y = 1 − X 的概率 | — | J26A Q4(a) |
| 5.2 概率函数与累积分布函数 | 22／31／63／180（主 45／126） | Find 29，Show that 6，Write down 6 | **由 Σp = 1 与 E(X)（或 Var(X)）解未知概率**（11 份）；**由 F(x) 求概率分布或反过来**（13 份），含 F 中带参数（J24 Q7、O24 Q6、J26 Q4）、F 由公式给出（O22 Q4）；**由实验构造分布**：不放回取球、游戏规则、两个数的乘积、取到第二只蓝袜为止（O21 Q4(d)、O21 Q5(d)、O22 Q7(f)、J22 Q7、J26A Q4）；不等式型概率 P(2X − 3 > 5)、P(4X² > Y)、P(Y ⩾ X) | 表格（x 与概率对应）；精确分数；1–6 分 | J24 Q7；J22 Q7；J26A Q4 |
| 5.3 离散随机变量的均值与方差 | 22／30／68／208（主 57／169） | Find 42，Show that 8，Calculate 4，Write down 3 | **E(X)、E(X²)、Var(X)**（每卷）；**Var(aX + b)、E(aX + b)**（13 份），含由 E(aX + b)、Var(aX + b) 反求 a、b（J21 Q4(d)、S24 Q2(c)、J26 Q6(c)）；E(1/X)、Var(1/X)（O23 Q4）；由 Var(X) 解未知概率（S19、S21、O21、J23 二次方程、O25A）；E(X) 的可能范围（J23 Q3(b)）；期望利润或罚款（O19 Q7(c)、J20 Q6(c)(f)、J26A Q6(b)） | 精确值或 3 s.f.；show-that 要写出全部乘积；2–6 分 | J24 Q7(d)；J23 Q3(c)；O25 Q4(d) |
| 5.4 离散均匀分布 | 6／6／17／32（主 12／17） | Find 6，Write down 3，State 3 | 说出分布名称"discrete uniform"（O20、J21、J25、O25）；写出概率函数（O25 Q3(a)）；求 E、Var 或线性变换的期望（J21 Q4(b)、J25 Q1(c)(d)、O25 Q3(c)、J26 Q6(c)）；不等式概率（J22 Q4、J26 Q6(a)） | 名称要写全两个词；1–3 分 | J25 Q1；O25 Q3；J26 Q6 |
| 6.1（`5.1#2`）正态分布 | 22／30／88／290（主 83／275） | Find 60，Show that 9，Calculate 6，Estimate 2，Hence find 2 | **直接求概率**（每卷，常要"Using standardisation"）；**反查百分位点**求临界值（几乎每卷）；**解 μ、σ**（8 份联立，另有单个未知数）；**条件概率**（13 份）；**独立重复**（8 份）；**正态四分位数与异常值**（4 份）；对称区间 P(μ − k < X < μ + k)（J20、O23、J24、S24、S25）；期望数量或金额（S22 Q6(b)、J26A Q6(b)）；**判断正态模型是否合适**（O24 Q5(d)、J25 Q7(c)、S25 Q5(f)、J26A Q2(d)） | 概率 4 位小数或 3 s.f.；z 值用表中 4 位小数；μ、σ 按题目精度；2–7 分 | J23 Q5；S23 Q7(c)；J24 Q8 |

**正态题的几种结构**（30 题）
- 先直接求概率，再反查（临界值或参数），最后条件概率等：S19 Q4、J21 Q3、O22 Q5、J23 Q5、O23 Q5、S24 Q5、O25 Q7、O25A Q4、J26 Q7。
- 以解参数为主：O19 Q6(a)、S23 Q7(c)、J24 Q8、O24 Q8(a)、J25 Q5(b)、J26A Q6(a)。J24 Q8(b) 还要用 2μ = 3σ²，σ 必须舍去其他根。
- 与其他主题连用：概率树（"3 次试跳内合格"O19 Q3、J24 Q5）、乘积与组合数（S25 Q6(b) 中 4 袋恰 2 袋，系数 6）、二次不等式（J20 Q5(c) 矩形面积 > 40）、利润期望（J26A Q6(b)）、异常值规则（O24 Q8(b)、J25 Q7）。

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据是 22 份卷的索引检索。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 建模思想 | 直接问只有 S25 Q3(a)（1 分）；其余都附在正态模型适用性、期望决策等小问里 | 一张"为什么用模型、模型的局限"短答卡；一张"正态模型适用的条件"卡 |
| 2.1 画直方图、茎叶图 | 从未要求画（考纲已排除）；只考柱宽柱高、读频数 | 不做画图卡；做"频数 = 面积"的计算卡 |
| 2.1 画箱线图 | 虽然考纲说画图不是直接考点，实际 10 份卷要求在网格上画带异常值的箱线图 | 一张流程卡：界限 → 须端到界内最远数据（或界限）→ 异常值单独标出 |
| 2.2 众数 | 只有 O24 Q1(a)（茎叶图）、J24 Q7(c)（离散分布的众数）和 O24 Q1(d) 的偏态系数 | 与偏态系数卡合并 |
| 2.3 百分位距（interpercentile ranges） | 从未出现；数据题只考四分位数与 IQR。唯一的百分位是正态的第 85 百分位（S25 Q6(c)） | 一张定义卡即可 |
| 3.1 初等概率（几何概率） | 只有 J21 Q6 | 不单独做卡，并入 Venn 图卡 |
| 4.1 在散点图上画回归线 | 只有 S19 Q6(f)、J21 Q5(g)（2021 年以后没有） | 一张卡：线必须过 (x̄, ȳ) |
| 4.2 指出解释变量与响应变量 | 只有 J26 Q2(b)（2026 年 1 月才首次出现） | 一张术语卡："响应变量依赖于解释变量／解释变量是受控的那个" |
| 5.1 离散随机变量的概念 | 从未问定义；只有 J26A Q4(a) 写出 P(S = 1) = 0 | 不单独做卡 |
| 5.4 离散均匀分布的均值、方差公式 | 公式册不给，也不在须背清单；真题多用逐项计算，J26 Q6(c) 的 MS 列出 (n² − 1)/12 作替代方法 | 一张公式卡（1 到 n 时均值 (n + 1)/2、方差 (n² − 1)/12），注明只适用于 1, 2, …, n |
| 二项分布 | 不在 S1（在 S2 1.1），但"n 次中恰 k 次"已出现多次（S19 Q4(d)、J21 Q3(d)、S25 Q6(b)）；MS 按"乘积 × 排列数"给分 | 一张卡：p^k(1 − p)^(n−k) × 排列数，不提二项分布名称 |
| 正态的概率密度函数、表中插值、显著性检验 | 考纲排除，22 份卷中没有出现 | 不做 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 O22、J23、S23、O23、J24 五份；没有标 ER 的条目都来自 MS 的评分说明。

1. **正态：z 值用百分位表的 4 位小数**
   - B 分只给 1.0364、1.6449、0.8416、2.3263、2.5758 等"或更精确"的值：O22 Q5(b)（MS p.12："awrt 88.3 implies 1st B1 and M1 but not the 2nd B1"）；S19 Q4(b)（584 只得 M1B0A1）；J23 Q5(b)（z 在 0.67–0.675 才得 B1）；S23 Q7(c)、J26A Q6(a)（不准确 z 值得出的答案扣 A）。
   - ER：用主表读出的 1.04 是最常见错误，百分位表才有"the four decimal place accuracy that is expected"（O22 ER p.5）；O23 Q5(d)(e) 用 −1.04、σ 写成 14.7 都失分（ER p.6）；J23 Q5(b) 常见错值 0.68（ER p.5）。
   - 可以用计算器求 z，但精度不能低于表值（S23 ER p.7）。
2. **"Using standardisation"：标准化式必须写出**
   - 没写标准化，答案对也不给分：J23 Q5(d) 很多人因此丢掉全部 3 分（ER p.5）；O24 Q4（MS p.9："correct answers with no working scores no marks"）；J25 Q5(a)(i)（只写答案 M0A0）；O25 Q7(a)（无过程的正确答案得 0）；J26 Q7(a)、O25A Q4(a)(b)（"Must show the standardisation"）。
   - 证明题写完标准化后还要再写一步：S23 Q7(a)(i)（ER p.6）；J24 Q5(a) 要见到 1 − 0.6179。
3. **正态：先画草图，符号要相容，除以标准差**
   - 不要习惯性地"用 1 减"：O22 Q5(a)（MS p.12："do not ISW so an answer of 0.1056 is A0"；ER p.5 说考生像是"programmed"去减）；J23 Q5(a) 相反，不减而失 2 分（ER p.5）。
   - 符号写反：S23 Q7(a)(ii)、(c)（ER pp.6–7，"a sketch"能避免）；O25A Q6(a) 两个方程符号都反导致 σ = −4.27，A0A0（MS p.16）。
   - 除以方差而不是标准差：J24 Q8(a)（ER p.7）；O25 Q7(a) 用 1.7² 得 M0。
4. **条件概率：分子是交事件，分母是已知事件**
   - MS 统一要求"a correct ratio of probability expressions"，分子小于分母（S19 Q4(c) MS p.9；S25 Q7(d)；J26 Q5(c)）。
   - 分子常见错误：用 0.25 而不是 0.25 × 0.06（S23 Q4(d)，ER p.5）；用 0.4 而不是 0.4 × 7/8（J24 Q3(d)，ER p.4）；用 P(L > 5) 而不是 P(5 < L < 5.58)（J23 Q5(e)，ER p.5）；把 (b) 的答案当分子（O23 Q1(e)，ER p.3）。
   - 分母常见错误：把 0.02 + 0.04 + 0.06 = 0.12 当 P(红)（S23 Q4(d)）；"合格"的概率是 1 − 0.3821³，不是 1 − 0.3821（J24 Q5(b)，ER p.5）。
   - 当作独立直接相乘一律 M0：J25 Q4(c)(ii)、S25 Q7(d)、O25 Q7(b)。
   - 不少考生没认出题目要条件概率：J23 Q2(d)、Q5(e)（ER pp.4–5）；O22 Q5(c) 只有最好的考生做下去（ER p.5）。
5. **独立与互斥：分清两者，检验要标注每个概率并下结论**
   - 互斥时 P(A ∪ C) = P(A) + P(C)，有人去乘（S23 Q6(a)，ER p.6）；独立时 P(F ∩ G) = P(F)P(G)，有人写成 0 或相加（O23 Q3(ii)(b)，ER p.4）；没有独立条件却写 xy（J24 Q6(a)，ER p.6，MS M0）。
   - 独立性检验：每个概率要标明是什么，P(A ∩ B) 要写出算法（J24 Q6(c)，ER p.6："union instead of intersection"也扣分；J25 Q4(b)，MS p.11）；show-that 型要写足细节（O23 Q3(i)(c)，ER p.4）。
6. **Venn 图与树形图的画法**
   - Venn 图：互斥的圆分开、独立的交集算出来、所有区域都填数（零写 0）、外框和标签要有。S23 Q6(c)（MS p.11："Do not accept blank or dash instead of 0"，ER p.6 最常见错误是三圆不相交或漏写外部概率）；J26A Q7(d)（MS p.18：一个圆完全在另一个圆内或完全分开得 M0，空白不当 0）；J25 Q4(a)（空白不能当 0 跟进）。例外：O24 Q3(a) 的 MS 写明"Treat blanks on the diagram as zero"，各卷不一致，制卡按"写 0"教。
   - 树形图：每组分支和为 1，位置不能对调（S23 Q4(a) 的 0.3 − 0.02 = 0.28，ER p.5；J23 Q2(a) 把给出的 4/8 抄到另一支，ER p.3；O23 Q1(a) 第三层分支出错，ER p.3）。
7. **直方图：频数 = 面积**
   - 把柱高当频数（J23 Q1(a) 得到 25 和 5，ER p.3）；求了面积不换算（S23 Q1(a)，ER p.3）。
   - S25 Q5(a)：第三根柱的频数密度也是 6，所以只写 60 ÷ 10 = 6 得 M1M0A0（MS p.10）；只写答案 M1M0A0。
   - 由直方图估计人数、取到整数（S25 Q5(b) 只收 45 或 46）。
8. **分组数据与插值**
   - 用组中值，不用组宽，不要除以组数（J23 Q1(c)，ER p.3）；标准差公式写对（J23 Q1(d)，ER p.3）。
   - 中位数、四分位数用 n 或 n + 1 都接受（O22 Q1(c) MS p.7，S21 Q3(b) MS p.9，J23 Q1(e)，S24 Q3(b)，O24 Q5(c)，S25 Q5(c)，O25 Q5(b)，J26A Q5(d)）；用 n 的考生更成功（J23 ER p.3）；求到下四分位数就停、没算 IQR（J23 Q1(e)，ER p.3）；找到中位数所在组却不插值（S23 Q1(b)，ER p.3）；四分位数要落在数据范围内（O22 ER p.3）。
   - 标准差默认除以 n，除以 n − 1 的 s 也接受：S19 Q1(a)(b)，J23 Q1(d)，O24 Q1(c)，S25 Q2(b)，O25A Q7(a)，J26A Q5(c)。
9. **编码**
   - 加减常数不改变离散程度，乘数只乘标准差（方差乘平方）：O22 Q3(b)（MS p.10："adding 21 is M0"；ER p.4 说不到 30% 的考生用对公式，常忘记乘 2 或乘 4）；J24 Q2(c)（从标准差里减 32、把 5/9 平方，ER p.4）；O25 Q5(c)(ii)（2 × 100 + 200 = 400 是 M0A0）；S25 Q2(c)(i)（只写"not affected by coding"是 B0）。
   - 还原后的量要标明：S23 Q3(b) 要写 Var(L)（ER p.4）。
   - r 不受线性编码影响，并要说明理由：J24 Q2(d)（ER p.4）；S23 Q2(f) 很多人重算或把编码套在 r 上（ER p.4）。
   - 回归线换回原变量：S23 Q2(g) 常把 y = w/2 − 5 反解成 w = 2y + 5（ER p.4）；J26A Q3(e)、S25 Q3(g) 不必化简。
10. **回归线**
    - 证明印出的回归线：要写出比印刷值更精确的 b 或 a（S23 Q2(c) 要见到 4.771 或 −16.66，ER p.4；S24 Q4(c) 要见到 0.7218 或 −42.29；O22 Q2(d) MS p.9、ER p.4）；把 45.85 凑成 46.0、写成 "w = 46 + 3.27h" 都不给（O25 Q1(c)，MS p.7）；过早取整 b、用错 n（J24 Q4(b)，ER p.5）。
    - 最终方程用题目的变量名（J24 Q4(b) 写成 x、y 失分，ER p.5；S22 Q2(c)、J26 Q2(e)）；多数 MS 不收分数（S19 Q6(d)、J21 Q5(e)、S22 Q2(c)、J25 Q6(c)、O25A Q1(e)），但 J26 Q2(e) 的 MS 接受精确分数 4023/10906、240/5453。
11. **解释斜率与 r：要有语境、数值和单位**
    - 斜率："x 每增加 1 单位，y 平均变化 b 单位"，写出 b 和单位：S22 Q2(d)（MS p.8）；J23 Q6(a)（ER p.6：只写 'as x increases then y increases' 或单位混乱）；S23 Q2(d)（漏单位或两个量都写 cm，ER p.4）；J24 Q4(c)（漏 'marks'、方向反了、把 −5.72 也写进去，ER p.5）；J26 Q2(f)（单位"米"必须有；截距解释成"在海面"）。
    - r：要写出两个变量的关系，只写"strong positive correlation"得 0 分：S22 Q2(b)（MS p.8）；O22 Q2(c)（ER p.3："Non contextual responses, scoring zero, were extremely common"）；O24 Q2(b)；O25A Q1(c)（必须提到年龄和血量）。
    - 散点图特征：要说"点接近一条直线"和"负斜率"，"negative correlation/negative trend/negative relationship"不收（J25 Q6(b)，MS p.13）。
12. **可靠性：围绕解释变量的取值范围**
    - 只写"extrapolation so unreliable"是 B0，提到响应变量超范围也是 B0（S22 Q2(e)(ii)，MS p.8）；只说"larger"不够（O20 Q5(f)，MS p.9）。
    - 不能说"396 超出范围"，也不要用 'it'（J23 Q6(c)，MS p.12、ER p.6）；要说法语成绩的范围，不能说西班牙语成绩的范围，也不能说"离中位数近"（J24 Q4(e)，MS p.9、ER p.5）；不能引用体重（O25 Q1(f)）；不能说"72 在数据范围内"（O25A Q1(f)）。
    - 用计算支持"不能用"：得到负体重 −7.16 g（S23 Q2(e)，ER p.4），负周长 −6.2 cm（S24 Q4(e)，代入 0.5 而不是 50 不给分）。
    - y 对 x 的回归线不能用来估计 x（S21 Q6(g)）。
13. **箱线图与异常值**
    - 先排序再找四分位数（J24 Q4(a)：直接取未排序的第三个数得 Q1 = 24，ER p.5）。
    - 界限必须写出来：只说出异常值是 43 而没有界限，M0A0A0（J21 Q2(c)，MS p.6）；只写答案 M0A0（S22 Q1(b)，MS p.7）；要明确比较两端数据与界限并下结论（S23 Q3(d)，MS p.8）；找到界限后还要指出是哪两个值（O23 Q2(b)，ER p.4）。
    - 画图：每端只能一根须（S22 Q1(c)，MS p.7："award A0 if there is more than one whisker at either end"）；须端在界内最远的数据或界限，不能画到 13 这种界限以外的位置（J26 Q1(c)，MS p.6）；半格精度（J21 Q2(d)）；没有刻度最多 M1B1B0A0（O25A Q3(c)）；漏画已找出的异常值（O23 Q2(c)，ER p.4）。
14. **偏态的描述**
    - 用题目指定的量；算了要描述，描述要有数值依据（O22 Q1(d)，ER p.3）。
    - 比较要用"更近／更大"，"中位数接近下四分位数"不是比较（J26A Q2(c)，MS p.9）；"even skew""normal"不收（O25A Q3(d)）；"positive correlation"代替 positive skew 得 M0（O25 Q2(d)）。
    - "left skew"在 S19 Q2(b) 得 A0（MS p.7），但 J26A Q2(c) 的 MS 接受 right/left skew；制卡统一用 positive/negative skew。
    - 只说偏态不足以说明为什么选均值而不是中位数（S22 Q1(e)，MS p.7）。
15. **正态模型是否合适**
    - 要"对称"和"连续"两方面：J26A Q2(d)（MS p.9：discrete 可以代替 not continuous；"insufficient data points"不收；均值≠中位数只有在均值或众数算对时才收）。
    - "mean = median"单独不足以说明对称（J25 Q7(c)，MS p.14）；O24 Q5(d) 以均值与中位数接近为依据，直方图形状的说法不计分。
16. **离散随机变量**
    - Var(X) = E(X²) − [E(X)]²：忘记平方（O22 Q7(c)，ER p.5；J23 Q3(c)，ER p.4；J24 Q7(d)，ER p.7）；把 Var 写成 E(X²) − E(X)（S23 Q5(e)，ER p.6）；停在 E(1/X²)、或把整项平方（O23 Q4(b)，ER p.5）。
    - Var(aX + b) = a² Var(X)：不平方 −3、加上 4、乘 4²（O22 Q7(d)，ER p.5）；乘 13 而不是 169（J24 Q7(d)，ER p.7）；5 + 4Var(Y) 不收（O24 Q6(e)，MS p.11）。
    - 求 E(X) 时除以值的个数是 M0（S25 Q1(c)，J26A Q1(b)(c)）。
    - 由 F(x) 求概率：只减前一个 F 值（J24 Q7(b)，ER p.6）；直接把累积值当概率是最常见错误（O22 Q4，ER p.4）；F 的最后一个值是 1，不是各 F 之和（J24 Q7(a)，ER p.6）。
    - 参数的约束决定 E(X) 的范围：0 < a < 0.6 而不是 0 < a < 1（J23 Q3(b)，ER p.4）。
    - 众数写 x 的值，不写概率（J24 Q7(c)，ER p.6）。
    - 只写答案：J25 Q1(g) 0/3（MS p.7）；J25 Q1(d) 无过程的 5 送复核；E(B²) = 21/4 是 M0（MS p.6）。
17. **Show that：步骤写全，中间值比印刷值更精确**
    - 通则：O22 ER p.3、J23 ER p.3（"a full method should be given for 'show that' questions"）。
    - 例：S23 Q6(b) 必须写出 0.3 × 0.1 = 0.03（ER p.6）；J24 Q2(a)(ii) 用 71.8 或 71.83 作均值一律 M1A0（MS p.7）；J25 Q2(d) 用 0.505² 的不精确算式 M1A0（MS p.8）；S25 Q1(d) 只写 6.65 − 2.35² = 1.1275 得 M0M1A0（MS p.6）；J23 Q4(i)(a) 只写出答案丢 A（ER p.4）。
    - 用给定答案去验证：S23 Q5(a)、S25 Q2(a) 都是 M1A0；S22 Q4(a) 最多 M1M1A0A0。
    - 题目禁止计算器解方程时要写出消元的一行（O24 Q6(c)，MS p.11）。
18. **精度、精确值和单位**
    - 默认 3 s.f.：J24 Q2(b) 写 0.85 失分（ER p.4）；S23 Q2(b) 写 2 位小数失分（ER p.3–4）；O22 Q2(b)（ER p.3）。
    - 题目要精确值时按要求：O22 Q2(a) 的 S_tt、S_ct（ER p.3）；S24 Q4(a)（只有 awrt 12100、9090 时 SC M1A0A1）；S21 Q1(b)（只写 awrt 0.476 得 M1M1A0）。但 S23 Q5(b)(c) 写着 "exact value"，MS 仍接受 awrt 0.333、4.33。
    - 语境答案要带单位：O22 Q2(e)（"£82 million (must include units)"，ER p.4 说很多人因此失分）；O20 Q5(a)（"Must have some units"）；S21 Q3(e)（"this must have units"）。
19. **读题，答所问**
    - 两株都要（J24 Q1(d)，ER p.3）；代 90 而不是 80 或 100（J23 Q6(b)，ER p.6）；计数题答整数（S23 Q3(c) 写 40.5 错，ER p.4）。
    - 答案要写在对应小问里：O24 Q1(a)、S25 Q1(a)、O25 Q3(a) 的 MS 都注明答案必须出现在 (a) 里（"Must be seen in part (a)" 或同义）。
