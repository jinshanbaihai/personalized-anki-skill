# WST03 · S3 Statistics 3：考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WST03.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WST03 --gaps` 输出为准（快照 2026-10-06）**。

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文关键词照抄考纲。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。S3 在印刷 pp.60–62（PDF pp.66–68）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。页码写印刷页码（FB 印刷页 = PDF 页 − 6）。
- 公式、上下标对照渲染页图核过（`registry/work/stat-spec/pg-66.png`–`pg-68.png`），因为纯文本抽取会打乱分式和根号。版面文本：`registry/work/stat-spec/lay_p066.txt`–`lay_p068.txt`。
- 试卷封面只用来补充考场要求，不是考纲：`registry/src/WST03/2025-06_01_qp.txt`（WST03/01，Friday 13 June 2025，P76201A）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WST03/01**。另有区域卷 **WST03/01A**，考纲里没有这个代码。英国文化协会中国区 2026 年 1 月和 6 月以 WST03A 报名（10 月不开）；本环境还没有找到任何一份 WST03/01A 试卷 | SPEC p.8、p.78；versions.md §1.6；`inventory/stat-gaps.md` |
| 单元名称 | Unit S3: Statistics 3；p.67 表中写作 “S3: Statistics 3” | SPEC p.60、p.67 |
| AS/A2 定位 | 单元页原文：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.60、p.67、p.9 |
| 资格结构 | **只能计入 Further Mathematics**（IAS 或 IAL）。IAL Mathematics 的五组选修组合里没有 S3 | SPEC p.10 |
| 时长与分值 | 1 hour and 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.60 |
| 题量（参考） | 2025 年 6 月卷封面写 “There are 8 questions”，总分 75。考纲没有固定题量 | `registry/src/WST03/2025-06_01_qp.txt` |
| 计算器 | 允许使用，规则见 Appendix 6 | SPEC p.60；p.86 |
| 卷面要求（试卷封面，不是考纲） | 统计表查出的值要 “quoted in full”；用计算器代替查表时，结果要保留到相当的精度。非精确答案默认保留 3 位有效数字 | 2025-06 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。S3 部分在 FB pp.25–28。FB p.25 原话：“Candidates sitting S3 may also require those formulae listed under Statistics S1 and S2, and Pure Mathematics P1, P2, P3 and P4.”后半句是 Issue 2 加的 | SPEC p.60；FB p.25；FB PDF p.4 变更说明 |
| 开考季 | **January and June**。从 2020 年 6 月起 October 考季不开 S3；2020 年 6 月以前 2018 版 S3 没有开考 | SPEC p.9、p.70；versions.md §1.4 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**（该季例外地开了全部 14 个单元）。2021 年 10 月也例外开考。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.60；versions.md §1.4–1.5 |
| 旧考纲同代码 | 2013 版旧考纲也用 WST03，最后一次是 **2019 年 6 月**，不算本考纲的真题。p.1 说 Statistics 各单元 “have not changed”，旧卷内容兼容，可作额外练习 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specifications for S1 and S2, and their prerequisites and associated formulae, is assumed and may be tested.” | SPEC p.60 |
| 评估目标分配（75 分中） | AO1 25–30；AO2 20–25；AO3 10–15；AO4 5–10；AO5 5–10（与 S2 相同） | SPEC p.69 |
| 须背公式（不在 FB 里） | 只有一条：独立正态随机变量的线性组合，见 §3 | SPEC p.60 |
| 记号 | Appendix 7 第 10 节（pp.91–92）：μ、σ²、σ 为总体参数；x̄ 为样本均值；s² 为总体方差的无偏估计，s² = Σ(xᵢ − x̄)²/(n − 1)；ρ、r 分别为总体和样本的 product moment correlation coefficient | SPEC pp.91–92 |
| 单元概述 | “Combinations of random variables; sampling; estimation, confidence intervals and tests; goodness of fit and contingency tables; regression and correlation.” | SPEC p.60 |

---

## 2. 规格条目逐条（S3.3 Unit content）

### 主题 1 Combinations of random variables（p.61）

**1.1 Distribution of linear combinations of independent Normal random variables**（p.61）
- 要求：若 X ∼ N(μₓ, σₓ²)、Y ∼ N(μᵧ, σᵧ²) 且相互独立，则 aX ± bY ∼ N(aμₓ ± bμᵧ, a²σₓ² + b²σᵧ²)。
- 排除：“No proofs required.”
- 公式：这一结论须背（p.60）。FB p.25 的 “Expectation algebra” 给出更一般的结果：独立时 E(XY) = E(X)E(Y)，Var(aX ± bY) = a²Var(X) + b²Var(Y)。

### 主题 2 Sampling（p.61）

**2.1 Methods for collecting data. Simple random sampling. Use of random numbers for sampling**（p.61）
- 要求：收集数据的方法；简单随机抽样；用随机数抽样。指导栏为空。
- 表：FB p.28 有 Random Numbers 表。

**2.2 Other methods of sampling: stratified, systematic, quota**（p.61）
- 要求：分层（stratified）、系统（systematic）、配额（quota）抽样。须知道 “The circumstances in which they might be used. Their advantages and disadvantages.”

### 主题 3 Estimation, confidence intervals and tests（pp.61–62）

**3.1 Concepts of standard error, estimator, bias**（p.61）
- 要求：标准误、估计量、偏差的概念。样本均值 x̄ 和样本方差 s² = (1/(n − 1)) Σᵢ₌₁ⁿ (xᵢ − x̄)² 作为相应总体参数的**无偏估计**（“as unbiased estimates of the corresponding population parameters”）。
- 公式：S² 的无偏估计式在 FB p.25；s² 的定义也印在 Appendix 7 第 10.26 条。

**3.2 The distribution of the sample mean X̄**（p.61）
- 要求：X̄ 的均值为 μ、方差为 σ²/n。若 X ∼ N(μ, σ²)，则 X̄ ∼ N(μ, σ²/n)。
- 排除：“No proofs required.”
- 公式：“X̄ is an unbiased estimator of μ, with Var(X̄) = σ²/n” 在 FB p.25。

**3.3 Concept of a confidence interval and its interpretation**（p.61）
- 要求：置信区间的概念与解释。指导栏：“Link with hypothesis tests.”

**3.4 Confidence limits for a Normal mean, with variance known**（p.61）
- 要求：方差已知时正态均值的置信限。须会应用正态分布、使用标准误求均值的置信区间，“rather than be concerned with any theoretical derivations”（不要求理论推导）。
- 公式：置信区间的形式 x̄ ± z·σ/√n **不在 FB 里**，也不在须背清单里；z 值查 FB p.17 的正态百分点表。

**3.5 Hypothesis tests for the mean of a Normal distribution with variance known**（p.61）
- 要求：方差已知时正态均值的假设检验，使用 (X̄ − μ)/(σ/√n) ∼ N(0, 1)。
- 公式：FB p.25 给出。

**3.6 Use of Central Limit theorem to extend hypothesis tests and confidence intervals to samples from non-Normal distributions. Use of large sample results to extend to the case in which the variance is unknown**（p.61）
- 要求：用 **Central Limit theorem** 把检验和置信区间推广到非正态总体的样本；用大样本结果处理方差未知的情况：n 大时 (X̄ − μ)/(S/√n) 可当作 N(0, 1)。
- 排除：“A knowledge of the t-distribution is not required.”
- 公式：用 S 代替 σ 的这一式只在考纲指导栏里，FB 没有单独列出。

**3.7 Hypothesis test for the difference between the means of two Normal distributions with variances known**（p.62）
- 要求：方差已知时两个正态总体均值之差的检验，使用 [(X̄ − Ȳ) − (μₓ − μᵧ)] / √(σₓ²/nₓ + σᵧ²/nᵧ) ∼ N(0, 1)。
- 公式：FB p.25 给出（Issue 2 补上了 “∼ N(0, 1)”，见 §5）。

**3.8 Use of large sample results to extend to the case in which the population variances are unknown**（p.62）
- 要求：总体方差未知时用大样本结果，使用 [(X̄ − Ȳ) − (μₓ − μᵧ)] / √(Sₓ²/nₓ + Sᵧ²/nᵧ) ∼ N(0, 1)。
- 排除：“A knowledge of the t-distribution is not required.”
- 公式：用 Sₓ²、Sᵧ² 的这一式只在考纲指导栏里，FB 没有单独列出。

### 主题 4 Goodness of fit and contingency tables（p.62）

**4.1 The null and alternative hypotheses. The use of Σᵢ₌₁ⁿ (Oᵢ − Eᵢ)²/Eᵢ as an approximate χ² statistic**（p.62）
- 要求：写原假设和备择假设；把 Σ(Oᵢ − Eᵢ)²/Eᵢ 当作近似的 χ² 统计量。应用对象包括 **discrete uniform, binomial, Normal, Poisson and continuous uniform (rectangular)** 分布。
- 限制：“Lengthy calculations will not be required.”
- 说明：主题标题和单元概述都写了 **contingency tables**，但 4.1、4.2 两条正文没有单独写列联表，只写了拟合优度的应用对象。
- 公式：“Goodness-of-fit test and contingency tables: Σ(Oᵢ − Eᵢ)²/Eᵢ ∼ χ²_ν” 在 FB p.25；χ² 百分点表在 FB p.26。

**4.2 Degrees of freedom**（p.62）
- 要求：自由度。须会在 “one or more parameters are estimated from the data” 时确定自由度。“Cells should be combined when Eᵢ < 5.”
- 排除：“Yates’ correction is not required.”
- 公式：自由度的计算规则 FB 没有给。

### 主题 5 Regression and correlation（p.62）

主题标题叫 “Regression and correlation”，但两条正文都只讲相关；S3 没有新的回归条目（回归在 S1 4.1–4.2）。

**5.1 Spearman’s rank correlation coefficient, its use, interpretation and limitations**（p.62）
- 要求：Spearman 等级相关系数的计算、使用、解释和局限。
- 排除与限制：“Numerical questions involving ties will not be set.”但 “Some understanding of how to deal with ties will be expected.”（不出有并列等级的计算题，但要懂并列如何处理。）
- 公式：r_s = 1 − 6Σd² / (n(n² − 1)) 在 FB p.25。

**5.2 Testing the hypothesis that a correlation is zero**（p.62）
- 要求：检验相关系数为零的假设。“Use of tables for Spearman’s and product moment correlation coefficients.”
- 表：FB p.27 的 Critical Values For Correlation Coefficients。表头说明这些是 “on a one-tailed test” 的临界值。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| aX ± bY ∼ N(aμₓ ± bμᵧ, a²σₓ² + b²σᵧ²)，X、Y 独立，X ∼ N(μₓ, σₓ²)，Y ∼ N(μᵧ, σᵧ²) | **须背**（考纲明列） | SPEC p.60 |
| 独立时 E(XY) = E(X)E(Y)，Var(aX ± bY) = a²Var(X) + b²Var(Y) | FB 给出 | FB p.25 |
| X̄ 是 μ 的无偏估计，Var(X̄) = σ²/n；S² = Σ(Xᵢ − X̄)²/(n − 1) 是 σ² 的无偏估计 | FB 给出 | FB p.25 |
| 正态总体样本：(X̄ − μ)/(σ/√n) ∼ N(0, 1) | FB 给出 | FB p.25 |
| 两独立正态样本：[(X̄ − Ȳ) − (μₓ − μᵧ)] / √(σₓ²/nₓ + σᵧ²/nᵧ) ∼ N(0, 1) | FB 给出 | FB p.25 |
| Spearman：r_s = 1 − 6Σd² / (n(n² − 1)) | FB 给出 | FB p.25 |
| Σ(Oᵢ − Eᵢ)²/Eᵢ ∼ χ²_ν | FB 给出 | FB p.25 |
| χ² 百分点表：ν = 1–30；上尾概率 0.995、0.990、0.975、0.950、0.900、0.100、0.050、0.025、0.010、0.005 | FB 给出 | FB p.26 |
| 相关系数临界值表（单尾）：product moment 的水平 0.10、0.05、0.025、0.01、0.005；Spearman 的水平 0.05、0.025、0.01；样本量 4–30、40、50、60、70、80、90、100 | FB 给出 | FB p.27 |
| 随机数表 | FB 给出 | FB p.28 |
| S1、S2 的公式与表（Φ 表、正态百分点表、二项表、Poisson 表等）；P1–P4 的公式 | FB 给出，S3 可能用到 | FB p.25 那句说明 |
| 大样本时用 S 代替 σ 的两个统计量（3.6、3.8）；置信区间 x̄ ± z·σ/√n；自由度规则；Eᵢ < 5 合并单元格 | FB **未给**，须背清单也**没有**；考纲指导栏写了要会用 | SPEC pp.61–62；FB p.25（已核对没有） |

---

## 4. 与相邻单元的界线

- **S1（先修）**：product moment correlation coefficient 的计算与解释在 S1 4.3，但 S1 写明 “tests of significance will not be required”；显著性检验在 S3 5.2。回归直线在 S1 4.1–4.2，S3 不再加回归内容。E(aX + b)、Var(aX + b) 在 S1 5.3；两个随机变量的组合在 S3 1.1。
- **S2（先修）**：
  - 假设检验的框架（原假设、备择假设、critical region、单尾/双尾，S2 4.3–4.5）S3 直接沿用。
  - population、census、sampling unit、sampling frame（S2 4.1）是概念；抽样**方法**在 S3 2.1–2.2。
  - S2 4.2 只讲统计量及其抽样分布的概念；X̄ 的分布、Central Limit theorem、标准误在 S3 3.1–3.2、3.6。
  - 二项、Poisson、连续均匀分布本身在 S2；S3 4.1 把它们作为 χ² 拟合优度检验的模型。
- **P1–P4**：考纲先修只写 S1、S2 及其先修；FB p.25 说可能用到 P1–P4 的公式。
- **不在 S3 的内容**：t 分布（3.6、3.8 明确排除）、Yates’ correction（4.2 明确排除）、有并列等级的 Spearman 计算题（5.1）。probability generating function 和 Cov(X, Y) 只出现在 Appendix 7 的记号表（10.19、10.31，p.92），任何单元的条目都没有提到。

---

## 5. 印刷问题与缺口

- **FB Issue 2 的两处改动与 S3 有关**（变更说明在 FB PDF p.4，已渲染核对 `registry/work/stat-spec/fb-pdf4.png`）：(1) S3 节的说明从“可能用到 S1、S2 公式”扩为“S1、S2 和 P1–P4 公式”；(2) Sampling distributions 中两样本均值差的式子，旧版没有写 “∼ N(0, 1)”，Issue 2 补上。用旧版公式册的学生要注意。
- **主题 4、5 的标题与正文不完全对应**：contingency tables 只出现在标题和概述里；“Regression and correlation” 下没有回归条目（见 §2）。
- 缺口：考纲没有写置信区间、拟合优度和相关检验的书写格式与结论措辞，要从评分方案和考官报告校准。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否另有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 真题需求概览

### 6.1 数据范围、引用写法与本次审核（审核部分为构建溯源，不随包发布）

**数据范围**：`WST03.questions.json`（2026-10-06 由 `WST03.questions.part1.json` 的 46 题和 `part2.json` 的 43 题合并，id 没有重复）。共 13 份卷、89 题、273 个小问、975 分：
- 2020-10 至 2025-06 每一季的 WST03/01，共 12 份正式卷；
- 另加 2022 年 1 月的未启用卷 P71859A（id 后缀 `01U`）。这份卷 Pearson 发布了试卷和 “Mark Scheme (Unused)”，但从未开考。出题风格与正式卷相同，所以计入统计。只看正式卷时，过滤掉 `-01U-` 即可；各条目只在正式卷出现的卷数见 `work/wst03audit/stats.json` 的 `live_papers`。
- 13 份卷都有 MS。J25 只找到 “Mark Scheme (Final)”；grademax 的 Pearson 链接索引里有 Results 版 `wst03-01-rms-20250306.pdf`，在受限区，拿不到。
- ER 只有 J23、S23、J24 三份，覆盖 21 题、63 个小问。
  - S21 整季考试取消，没有 ER；U 卷没人考过，也没有 ER。
  - J24 Q2(c) 报告没有评论，`er` 字段如实写了“未评论”。

下面的数字由 `work/wst03audit/scripts/stats.py` 从索引统计，结果在 `work/wst03audit/stats.json` 和 `dump_by_spec.txt`。“问法、终点、评分”取自索引的 `ask`、`final_form`、`ms`、`er` 字段。

**缺失的卷**（所有来源都没有）：
- **2026-01 的 /01 与 /01A，2026-06 的 /01 与 /01A**，QP、MS、ER 全缺。这四份卷确实存在：grademax 的 2026 索引（`finder/gh/grademax_manifest/edexcel_2026.json`）列出了以下文件，都在 Pearson 受限区：
  - `wst03-01-que-20260123.pdf`、`wst03-01a-que-20260123.pdf`
  - `wst03-01-que-20260613.pdf`、`wst03-01a-que-20260613.pdf`
  - 以及各自的 rms 文件。
- **2025-06 /01A**：grademax 的 2025 索引里 S3 只有 /01，所以很可能不存在。
- **已收卷缺 ER 的 8 份**：O20、J21、O21、J22、S22、S24、J25、S25。

本次在以下来源重新查过，没有新的 WST03 文件：
- Drive 标题检索：含 `WST03`、`wst03`、`Statistics S3`、`S3A`、`_S3`，且 2025-09-01 以后修改的文件；
- Drive 标题检索：含 `2601`、`26_01`、`2606`、`26_06`、`January 2026`、`June 2026` 的 PDF，结果只有 P4、P4A、S1、S1A；
- Drive 全文检索：`WST03/01A`、`P76201A`，以及 `WST03` 加 `Principal Examiner`，结果只有已收的 MS 和考纲；
- `git ls-remote`：`RayZ3R0/papernexus-finder` 仍是 921bdf4f（S3 只到 2024 年 6 月，没有 ER），`anonymouslyanonymous1/Edexcel-Finder` 仍是 e3db7034。

**清单本身尚未更新**：`inventory/stat.json`、`stat-coverage.json`、`stat-gaps.md` 仍把 2020-10 至 2022-06（含 U 卷）的 QP、MS 记为缺失。这 14 个 PDF 已在 part 1 从 papernexus-finder 取得并核实（`WST03.coverage.part1.md` “Sources added in this pass”）。

**没有收的**（均有 Finder 文本）：
- 2018 年 Sample Assessment（S59770A），不是考季；PDF 在 `src/WST03/2018-09_01_specimen*.pdf`。
- 2014-06 至 2019-06 同代码的 2013 版旧卷。考纲 p.1 说统计单元内容没变，所以可作额外练习，但不算本考纲的真题。

**引用写法**：
- J = January，S = June，O = October，后接两位年份，如 S24 = 2024 年 6 月；U = 2022 年 1 月未启用卷（J22U）。
- 题号与小问照试卷印刷。
- “MS”“ER”指该卷的评分方案和考官报告，页码是 PDF 页（见索引条目的 `ms`、`er` 字段）。

**本次审核做了什么**（脚本和输出都在 `work/wst03audit/`；改动前的文件在 `backup/`）：

1. **合并与校验**。构建时的合并校验脚本检查了以下各项：
   - 每条的字段齐全，没有多余字段；
   - 各小问分值之和等于题目总分；
   - spec id 都在 `spec-items.stat.json` → WST03 里；
   - series 的格式是 YYYY-MM；
   - id、paper、series、题号互相一致；
   - 每卷合计 75 分，题号连续；
   - 有 MS 或 ER 来源的条目，`ms`、`er` 字段不为空；
   - 引号内的原文不超过 25 个词。

   首次运行有 1 个问题：J24 Q2(c) 有 ER 来源，但 `er` 为空。改正后为 0（`validate.txt`、`validate_after.txt`）。
2. **独立核对分值**。`totals_check.py` 从 `src/WST03/*_qp.txt` 抽取印刷的 “(n)” 序列和 “Total” 行，13 份卷的 273 个小问分值、89 个题目总分与索引逐一相符。
   - O20 有一个 “(8)” 后面紧跟页边文字，脚本没抓到；人工看过，相符。
3. **命令词**。`cmdcheck2.py` 检查每个命令词是否出现在该小问自己的 QP 原文段落里，0 处不符。
4. **评分码之和**。`mscodes.py` 把每个小问 `ms` 里的 M/A/B 码加起来，与该小问分值比较。273 个小问中有 15 个不一致，逐个查过，都不是错误，原因有三类：
   - 变量名被当成评分码，如 B1 − B2、C1；
   - 注释里的组合写法，如 “M1B0M1M1A1”；
   - “B1 each”这类写法。
5. **终点数值**。`ffcheck.py` 检查 `final_form` 里的 457 个数，确认都出现在所引的 MS 页上。只有 4 个不在页上，都是由 MS 数值四舍五入或相加得到的，已逐个核对，没有错：
   - 63.21（MS 是 63.2056）；
   - 20.78（MS 是 20.7768）；
   - 328.99（MS 是 328.986）；
   - 240（Σfx）。
6. **单尾与双尾**。34 个带 H1 的检验，H1 方向与所用临界值一一对得上。相关系数临界值也与 FB p.27 的 n 和水平相符。
7. **逐条复核**。对照 QP、MS、ER 原文重查了 38 题；分式、根号、不等号丢失的地方看了渲染图（`img/`）。
   - **计划抽查**：每份卷 2 题，共 26 题：O20 Q4、Q7；J21 Q3、Q5；S21 Q2、Q5；O21 Q3、Q6；J22 Q4、Q5；J22U Q5、Q6；S22 Q5、Q7；J23 Q1、Q4；S23 Q3、Q6；J24 Q6、Q7；S24 Q5、Q6；J25 Q2、Q4；S25 Q6、Q8。
   - **整卷复查**：S23、S24 两卷各查出 2 处问题，所以把这两卷其余各题也全部重查了：S23 Q1、Q2、Q4、Q5、Q7；S24 Q1、Q2、Q3、Q4、Q7。
   - **附带查看**：S21 Q4、J21 Q4。
   - 核对内容：分值、spec 映射、命令词、`final_form`（数值答案用 Python 独立重算：正态概率、二项概率、χ² 统计量、置信区间、n 的反求）、MS 要点及页码、ER 内容及页码。
   - 另外用 `cite_check.py` 核对了 6.5 节所引的 66 处 MS、ER 原文短语及其页码：62 处自动匹配；另 4 处因换行或符号丢失，人工核对。
   - 其中 1 处归类有误：`WST03.coverage.part2.md` 把 J25 Q5(c) 列为“结论可用 relationship／connection”，但 MS p.10 只写了不能用 correlation 代替 association。已在该文件和本节改正（`fixes.json` 第 7 条）。
8. **发现并改正的错误**：索引 6 处，加上第 7 项所说 coverage 注释 1 处。每处的原文、证据、改动写在 `fixes.json`，索引部分由 `apply_fixes.py` 同时写入合并文件和对应的 part 文件；改完后合并文件与两个 part 文件逐条一致。
   - **S24 Q5(a) `ms`（实质错误）**：特殊情况的不等号写反了。MS p.11 原文（看渲染图 `img/ms2406p11_notes.png`）是 “SC B0B1 for H0: μf − μp = 1 and H1: μf − μp > 1”，原条目写成了 “< 1”；“Use of t̄ is B0” 也被写成 “t is B0”。根源是 pdftotext 丢了符号。
   - **S21 Q5(d) `ms`**：MS p.10 的 M1 是 “Combining 0,1,2 or 5,6,7,8”，合并其中一组即可得分；原条目写成 “and”，像是两组都要合并。
   - **S23 Q3(a) `ms`**：MS p.8 原文是 “Allow σ is unknown (Do not allow σ is unknown variance)”，即不接受把 σ 说成方差。原条目转述成 “'unknown variance' alone not allowed”，意思走样了。
   - **S24 Q1(a) `ms`**：原条目把 “随机起点在 001–050” 写成了评分要求，MS p.6 并没有给范围。已注明“方案未给范围，001–050 是隐含的”。
   - **S23 Q5(c) `er`**：ER p.4 原文是 “regions in which the two confidence intervals overlapped”，举的错误是 P(x̄ − ȳ > 0) **或** P(x̄ − ȳ < 0)。原条目改写成 “non-overlap regions”，例子也只留了一半。现改为如实转述，并注明题目问的是“不重叠”。
   - **J24 Q2(c) `er`**：原为空，补成“报告第 2 题只评了 (a)(b)，未评论 (c)（ER p.3）”。
9. **没有改的判断**：
   - spec 映射逐条看过（`specdump.txt`），没有发现需要改的。S1、S2 的先修内容挂在 S3 条目上的规则，见两个 coverage 文件的 “Spec mapping notes”。
   - 因为 spec 没有改动，`WST03.coverage.part1.md`、`part2.md` 里的条目计数仍然有效。但那两处只统计各自的半段，全量统计以本节为准。

### 6.2 卷面结构

- **每卷 75 分、90 分钟**。9 份卷 7 题；J21、S21、J22 三份 6 题；S25 一份 8 题。
- **题目分值** 3–18 分，最常见的是 8 分（13 题）、10 分（12 题）、9 分和 12 分（各 11 题）、11 分和 14 分（各 9 题）。
- **小问**：
  - 每题小问个数：3 个 40 题、4 个 19 题、2 个 18 题、5 个 6 题、1 个 5 题、6 个 1 题。只有一问的 5 题是 S21 Q2、O21 Q1、O21 Q2、J22U Q4、J24 Q1，都是一问做完的完整检验。
  - 小问分值：1 分 48 个、2 分 54 个、3 分 47 个、4 分 51 个、5 分 21 个、6 分 14 个、7 分 24 个、8 分 11 个、9 分 1 个、10 分 2 个。
  - **7 分及以上的 38 个大问**：χ² 检验 20 个、两样本均值检验 11 个、线性组合 5 个（O20 Q7(c) 反求 n，J21 Q6(b)–(c)，O21 Q7(c)，S24 Q6(c)），另有 J24 Q6(c)（合并样本的标准误）、S23 Q5(c)（两区间不重叠的概率）各 1 个。
- **命令词**（273 个小问，归并同义词）：
  - Find／Calculate／Determine／Estimate 121；
  - Test／Carry out／Assess／“Use a suitable test” 55；
  - Explain／Describe／Comment／Advise 39；
  - State／Write down／Give 32；
  - Show that 19；
  - Complete 4（χ² 表或检验的后半段）；
  - Use 3。
- **终点形式**（自动粗分，仅供参考）：
  - awrt 小数，多为 3 位有效数字的概率、z 值或 χ² 统计量，约 97 个；
  - 检验结论（假设、临界值、语境结论），约 66 个；
  - 文字（抽样步骤、假设条件、解释），约 60 个；
  - 印刷结果 19 个；
  - 含参数的精确式（如 46μ/35、2a + 6、N(x + 2, 3/n)），约 12 个；
  - 整数或参数值（n、c、x、w），约 11 个；
  - 置信区间，约 8 个（另有若干归在 awrt 小数里）。
- **按主条目统计分值**（每个小问只算 `spec` 的第一个条目）：
  - 主题 1（独立正态的线性组合）182 分（18.7%）；
  - 主题 2（抽样）42 分（4.3%）；
  - 主题 3（估计、置信区间、均值检验）367 分（37.6%）；
  - 主题 4（χ² 拟合优度与列联表）253 分（25.9%）；
  - 主题 5（相关检验）131 分（13.4%）。
- **每卷固定出现的题型**：
  - **一题独立正态的线性组合**（1.1，13/13）。8–18 分，10 份卷是最后一题，例外是 J22（Q5）、S22（Q6）、S24（Q6）。
  - **χ²**（4.1，13/13）。13 份卷都有拟合优度检验，12 份有列联表，唯一例外是 S22。11 份卷两类各占一题；S24 两类合在 Q4 一题里；S22 只有 Q7（骰子）。
  - **Spearman 或 PMCC 的相关检验**（5.1/5.2，13/13）。
  - **两样本均值的 z 检验**（3.7/3.8，13/13）。J21 Q4(b) 是两个总体方差都已知（3.7）；其余 12 份都是大样本、方差用 s² 代替（3.8）。
  - **置信区间**（3.4，12/13）。S25 没有；O20 只在 Poisson 均值的区间里出现（Q6(b)）。
  - **估计量概念或无偏估计的计算**（3.1，12/13）。S21 没有。
  - **抽样方法**（2.1/2.2，10/13）。S22、J23、S23 没有。
- **显著性水平**：
  - 5% 为主。
  - 10%：χ² 的 O20 Q4，J21 Q5，S21 Q5(d)，J22U Q6(c)，J25 Q5(c)。
  - 1%：χ² 的 J23 Q3(b)、J25 Q2(d)；相关的 J22U Q3(b)、J23 Q2(b)(d)、J25 Q1(b)、S25 Q2(b)；两样本的 J22 Q2(a)、S22 Q2(b)（均为双尾）和 J23 Q5(a)。
- **z 临界值**：索引中出现 1.6449 的小问 29 个、1.96 的 16 个、2.5758 的 11 个、2.3263 的 7 个、1.2816 的 1 个（J22U Q7(d)）。MS 一律要 “or better”，见 6.5 第 1 条。
- **置信水平**：90%（S21 Q3(a)，S23 Q5(a)）、95%、98%（J21 Q4(a)，J23 Q6(a)，S24 Q3(b)）、99% 都考过。由区间宽度反求置信水平的考过两次，答案是非常规值：S22 Q3(c) 约 92%，J25 Q4(c) 约 89.3%。
- **ER 点名的难题**：
  - J23 最难的是 Q1，其次是 Q5、Q7；
  - S23 最难的是 Q5，其次是 Q3；
  - J24 最难的是 Q6(c)，其次是 Q7(c)；
  - 出处：各卷 ER p.3。

### 6.3 每个考纲条目怎么考

“卷数／题数／小问／涉及分值（主）”：一个小问可以带几个条目标签，所以各行相加大于 89 题、975 分；括号里是该条目作为第一标签时的分值。命令词已归并同义词。

| 条目 | 卷数／题数／小问／涉及分值（主） | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 独立正态的线性组合 | 13／15／41／193（182） | Find／Calculate 38，State／Explain 3 | ① n 个独立同分布的和（方差是 nσ²，不是 n²σ²）：O20 Q7(a)，J23 Q7(a)，S24 Q6(a)，J25 Q7(a)，S25 Q8(a)。② “差超过 d”，算 2 × P(D > d)：S21 Q6(b)，O21 Q7(a)，S24 Q6(b)，J25 Q7(b)，S25 Q8(b)。③ 与倍数或另一组合比较，化成单一正态：1.8 倍（J24 Q7(b)），110%（S21 Q6(a)），3 红砖 < 4 × 黄砖（J21 Q6(b)），4T > 100 + 3M（O21 Q7(c)），G < 2T + 20（S24 Q6(c)），T < 30P₁ + 190（S25 Q8(c)，托盘系数 29²），两颗西兰花 < 一颗卷心菜（J22U Q7(a)），按单价计费（J22U Q7(b)–(c)），两袋各含空袋重（S21 Q6(c)）。④ 反求：由概率解 n，要舍负根（O20 Q7(c)，J25 Q7(c)，Var 含 n²）；载重上限的最大人数 c（S22 Q6(b)）；σ（S23 Q7(b)）；分位数 t（J22 Q5(c)）；单价 w（J22U Q7(d)）；方差最小时的 a、b（J21 Q6(c)，要求极值）；写出 W ~ N(a, b)（J24 Q7(a)）。⑤ 第一个与均值之差 S₁ − S̄（J24 Q7(c)，S₁ 与 S̄ 不独立）。⑥ 假设：服务时间独立（J23 Q7(b)）；连续比赛不独立，所以 (a) 不能直接用于 (d)（J22 Q5(e)），(d) 本身是 B(6, p)。 | awrt 3 s.f. 的概率；整数 n、c 要按不等式方向取整；4 分最多（14 个），反求题 6–8 分 | O20 Q7，J24 Q7，S24 Q6，S25 Q8，J21 Q6 |
| 2.1 收集数据；简单随机抽样；随机数 | 5／5／8／15（6） | State／Explain 6，Find 1，Show 1 | 作主条目只有 3 问：用随机数表按指定列读两位数，跳过重复和超范围的数（J21 Q1(a)，表在 FB 上，但题目写 “page 27”，是旧版页码，Issue 2 在 p.28）；所选号码最大只到 42，所以年长的选手可能没有代表（J21 Q1(c)）；自制的一位随机数表不能直接用于 00–69 的简单随机抽样（O20 Q4(d)）。作次要条目：分层或系统抽样里的随机数步骤（J21 Q1(b)，J22U Q1(b)(i)，J24 Q2(b)），与简单随机抽样比较（J24 Q2(c)，J25 Q5(a)） | 号码列表或文字；1–2 分 | J21 Q1，O20 Q4(d) |
| 2.2 分层、系统、配额抽样 | 10／10／19／36（36） | Explain／Describe 12，State／Write down／Give 6 | ① 系统抽样：说明步骤（编号 → 在第一个区间随机起点 → 每隔 k 个取一个）：O20 Q4(a)（280 取 40），J22U Q1(a)（1200 取 60），J24 Q2(a)（800 取 80），S24 Q1(a)（400 取 8）；写出 k（S25 Q1(b)，x = 18）；“两个相邻编号或首尾编号同时入选”的概率是 0（S24 Q1(c)，S25 Q1(c)）；理由与缺点（J22U Q1(b)，S24 Q1(b)，S25 Q1(a)）。② 分层抽样：步骤加各层人数（S21 Q4(a) 28／42，O21 Q4(a) 20／80／60／40，J24 Q2(b) 54／31／15，J21 Q1(b) 用给定随机数分层）；为什么分层更好（J22U Q1(c)，Year 9 应有 10 人；J24 Q2(c)）。③ 配额抽样：描述做法（J22 Q4(a)）；一个优点、一个缺点（J25 Q5(a)） | 文字步骤，各层人数取整；1–3 分，评分多为“编号／随机／人数（或每隔 k 个）”各 1 分 | J24 Q2，J22U Q1，S24 Q1，S25 Q1 |
| 3.1 标准误、估计量、偏差；x̄、s² 无偏 | 12／18／34／90（88） | Find／Calculate 19，Show 8，Explain 4，Use 2 | ① 由 Σx、Σx² 求 x̄ 与 s²（几乎每卷）：O20 Q5(a)，J21 Q5(b)，O21 Q6(a)，J22 Q1(a)，J22U Q5(a)，S22 Q2(a)（给的是 Σ(x − x̄)²），S23 Q6(a)（求 s 而非 s²），J24 Q6(b)，J25 Q3(a)，S25 Q4(a)。变式：编码数据（J23 Q1(a)，Var(X + a) = Var(X)）；加入一个新观测值后重算 s²（S24 Q5(c)）；两个样本合并后的 s² 与标准误（J24 Q6(c)，7 分）。② 概念：为什么某个式子是或不是 statistic（S22 Q5(a)，S23 Q3(a)，S25 Q6(a)）；无偏的定义（S22 Q5(b)）；用期望证明有偏或无偏（O20 Q1(a)，S22 Q5(c)，S23 Q3(b)，J25 Q6(a)，S25 Q6(b)）；求偏差（S23 Q3(c)，J25 Q6(b)，S25 Q6(c)）；使估计量无偏的系数条件（S23 Q3(d)，J25 Q6(c)，S25 Q6(d) 联立）；估计量的方差与 “more efficient”（S22 Q5(d)，S23 Q3(e)）。③ 用估计量估参数：离散均匀的 α（O20 Q1(b)）；均匀分布的最大值（J25 Q6(d)）；用估计的正态求比例（J21 Q5(d)） | x̄ 精确、s² cao 或 awrt 3 s.f.；含 μ、a 的精确式；3 分最多（13 个） | S23 Q3，S25 Q6，J25 Q6，J24 Q6(c)，J23 Q1(a) |
| 3.2 X̄ 的分布 | 8／9／12／50（26） | Find 8，其余各 1 | 只考过一次直接求 P(X̄ < k)：J23 Q6(d)，ER 说很多人没看出问的是 X̄。其他考法：使 P(X̄ > 2) < 1% 的最小 n（O21 Q7(b)）；由两个关于 X̄ₙ 的概率列方程，证明 σ = 12√n，再求 μ 和新概率（S25 Q7）；X̄ − Ȳ 的分布（S23 Q5(c)）；S̄ 与 S₁ 的组合（J24 Q7(c)）；合并样本的标准误（J24 Q6(c)）；CLT 给出的 N(μ, σ²/n)（O20 Q6(a)，S22 Q4(c)，S24 Q7(a)） | awrt 3 s.f. 概率、整数 n 或印刷结果；5–7 分的大问 6 个 | S25 Q7，O21 Q7(b)，J23 Q6(d) |
| 3.3 置信区间的概念与解释 | 9／9／10／34（16） | Find 7，Explain 2，Test 1 | ① 若干个置信区间中含 μ 的个数服从二项分布：O20 Q6(c)（两个区间恰一个含 λ，2p(1 − p)），S21 Q3(b)，S24 Q3(c)。② 用区间判断说法：O21 Q5(b)（不含 3 kg，所以加量），J23 Q6(c)（22.5 在区间内，没有理由怀疑），J22 Q1(c)（取区间上端作均值，估“最少有多少比例低于 10.5 kg”）。③ 用区间做双尾检验，并写出显著性水平（S24 Q3(a)，考纲 “Link with hypothesis tests”）。④ 由宽度反求置信水平（S22 Q3(c)，J25 Q4(c)）。⑤ 两区间不重叠的概率（S23 Q5(c)） | 概率；百分数到 3 s.f.；文字判断；作主条目 1–3 分 | S24 Q3，O20 Q6(c)，J22 Q1(c) |
| 3.4 方差已知时正态均值的置信限 | 12／13／22／88（76） | Find／Calculate 19，Show 3 | ① 直接求区间：J21 Q4(a)（98%），O21 Q5(a)（99%），J22 Q1(b)，J22U Q2(a)，J23 Q6(a)，S23 Q5(a)–(b)。② 由一个区间反推 x̄ 与 σ（或标准误），再求另一水平的区间：S21 Q3(a)，S22 Q3(a)–(b)，J24 Q6(a)，S24 Q3(b)（明确不许只用计算器），J25 Q4(a)–(b)。③ 由宽度或界限求 n：最小 n 的有 J22U Q2(b)、S22 Q3(d)，最大 n 的有 O21 Q5(c)，S24 Q7(b) 由下界求 n。④ 由宽度求置信水平（S22 Q3(c)，J25 Q4(c)）。⑤ 用 CLT 求 Poisson 均值 λ 的区间（O20 Q6(b)，方差 λ/40） | (a, b) 区间按要求的小数位或 awrt；整数 n；3–6 分，4 分最多 | J24 Q6(a)，S24 Q3(b)，J25 Q4，S22 Q3 |
| 3.5 方差已知时正态均值的检验 | 4／4／6／19（16） | 各类 1–2 | 完整的单样本 z 检验只考过一次：O21 Q1（5 分，σ 已知，n = 80）。其他考法：双尾检验求 X̄ 的拒绝域，再判断 1008.47 是否落入（J23 Q1(b)–(d)）；反求最大的 μ，使两个样本都不显著（J21 Q4(c)）；用置信区间做检验（S24 Q3(a)） | 拒绝域写成 X̄ ≤ … 或 X̄ ≥ …；z awrt；语境结论 | J23 Q1，O21 Q1 |
| 3.6 CLT 与大样本 | 11／15／21／51（36） | Explain／State 14，Find 5 | ① 非正态总体的样本均值：Poisson（O20 Q6(a)–(b)），连续均匀（S22 Q4，等车时间 U[0, 7]；S24 Q7，U[x − 1, x + 5] 反求 n）。② 两样本检验里 CLT 的作用（S21 Q4(c)，O21 Q6(c)，J22 Q2(b)），大样本的两个用处（O20 Q5(c)，J25 Q3(c)）。③ 要不要假设总体正态：不需要，因为样本大、可用 CLT（J22U Q5(c)，S23 Q6(c)）；反过来，总体已是正态时不需要 CLT（J23 Q6(b)）。④ n 大，所以可用 σ² = s²（J23 Q1(e)）。⑤ 计算所需的假设（S22 Q4(d)） | 文字 1–2 分；N(…, …/n) 的分布式；概率 | S22 Q4，S24 Q7，O20 Q6，S23 Q6(c) |
| 3.7 两正态均值之差的检验（方差已知） | 13／13／14／92（6） | Test 13 | 作主条目只有 J21 Q4(b)：两镇方差都是全国的 σ = 18。其余 12 次都是大样本、方差未知，标签记作 3.8 为主、3.7 为次 | 见 3.8 | J21 Q4(b) |
| 3.8 两总体方差未知时的大样本检验 | 12／12／26／107（103） | Test 12，State 8，Explain／Comment／Advise 6 | ① 完整的两样本 z 检验，6–8 分，12 份卷都有（J21 除外）。原假设的差为 0 的 7 次：S21、O21、J22、S22、J23、S23、J25；差不为 0 的 5 次：O20（5 g）、J22U（20 kg）、J24（15 wpm）、S24（1 分钟，方向容易写反）、S25（200 g）。多为单尾；双尾只有 J22 Q2(a)、S22 Q2(b)，均为 1%。② 写假设条件：两组的 s² = σ²（S21 Q4(d)，J22U Q5(d)，S23 Q6(d)，S25 Q4(c)），为什么 σ² = s² 合理（S22 Q2(c)），写两个假设（O21 Q6(d)，J24 Q5(b)，S24 Q5(b)）。③ 后续：新 z 值不显著时如何评论（S21 Q4(e)–(f)）；按每株期望利润给建议（J23 Q5(b)） | z awrt 3 s.f.（偶有精确值，如 J22 Q2(a) 的 ±2√3）；临界值 1.6449、2.3263 或 2.5758；语境结论；7 分最多（10 个） | S24 Q5，J24 Q5，S25 Q4，O20 Q5 |
| 4.1 假设与 Σ(O − E)²/E | 13／24／55／247（244） | Test 22，Find 17，Show 7，Complete 4，State 4 | ① **列联表**（12 份卷）：2×2（S21 Q2），2×3（O21 Q4，J22 Q4，J22U Q4，J24 Q1，J25 Q5），3×2（J23 Q3），3×3（O20 Q2，S23 Q2，S25 Q3），3×4（J21 Q3，S24 Q4(b)–(c)）。多数只让你补几个 E，再与给定的部分和相加（O20 Q2，O21 Q4，J23 Q3，S23 Q2，J25 Q5，S25 Q3）；整题算完的有 S21 Q2（9 分）、J22 Q4(b)、J22U Q4（10 分）、J24 Q1。数据实为百分数、样本量翻倍时，统计量也翻倍（J22 Q4(c)）。② **拟合优度**（13 份卷）：离散均匀（O20 Q4，J21 Q3(a)，S22 Q7，S22 是含未知 x 的反求题）；给定比例或比值（O21 Q2，S24 Q4(a)）；二项（S21 Q5，J23 Q4 先给 p 再估 p，S25 Q5）；Poisson（J22U Q6，J24 Q4，J25 Q2，λ 都由样本估计）；正态（J21 Q5 先给参数再估参数，J22 Q6）；给定 pdf（S23 Q4，先证 P(a ≤ T < a + 1) = (2a + 1)/25）。③ 铺垫小问：证明样本均值（S21 Q5(b)，J22U Q6(a)，J24 Q4(a)，J25 Q2(a)）；补算缺失的 E（S21 Q5(c)，J22 Q6(a)，J22U Q6(b)，J24 Q4(b)–(c)，J25 Q2(b) 说明 r = 100 − 其余之和，S25 Q5(b)） | E 按要求的小数位；X² awrt 3 s.f.；ν；临界值；语境结论。完整检验 7–10 分，4 分以下的铺垫小问很多 | J22U Q6，J23 Q4，S24 Q4，J21 Q5，S25 Q3 |
| 4.2 自由度 | 13／24／33／198（9） | 作主条目时 Explain／State／Write down | 作主条目只有 5 问：说明为什么 ν = 4（J21 Q3(d)，有一格 E = 4.77 < 5，合并一列后成 3×3）；估计参数后临界值怎么变（J22 Q6(c)，ν = 8 − 3）；写出 ν（S24 Q4(c)，ν = 6）；为什么要合并格（J25 Q2(c)）；补完检验（J21 Q5(c)，ν = 5 − 3）。其余都是完整检验里的 B1（ν）和 B1ft（临界值）。估计参数后的 ν：二项 p 是 −1（S21 Q5(d) 4 − 2，J23 Q4(c) 3，S25 Q5(c) 6 − 1 − 1）；Poisson λ 是 −1（J22U Q6(c)，J24 Q4(d)，J25 Q2(d)）；正态 μ、σ 是 −2（J21 Q5(c)，J22 Q6(c)） | 整数 ν，或文字理由；1–3 分 | J21 Q3(d)，J22 Q6(c)，J25 Q2(c) |
| 5.1 Spearman 等级相关 | 13／13／19／60（60） | Find／Calculate 12，Explain 5，State 2 | ① 自己排等级、算 Σd² 和 rₛ（每卷一次，n = 5–11）。有时等级的方向要按题目指定，如 “rank 1 = highest price”（S24 Q2(a)）、“largest = 1”（S22 Q1(b)）、“fastest = 1”（J23 Q2(a)）；有时要先补全等级（J25 Q1(a)）。② 并列等级只考概念：用平均等级，再对等级算 PMCC（O20 Q3(c)，S22 Q1(a)）；改正一个价格后出现并列，记 1.5（S24 Q2(d)）。③ 什么时候用 Spearman 而不用 PMCC（S23 Q1(a)，O21 Q3(e)，S24 Q2(c)）；相关不等于因果（J21 Q2(c)） | rₛ 写成精确分数或 awrt 3 s.f.，并写出 Σd²；4–5 分 | S24 Q2，O20 Q3，S22 Q1 |
| 5.2 相关系数为零的检验 | 13／13／24／72（71） | Test 18，Find 4，State 2 | ① 每卷一个 ρ = 0 的检验，3–5 分，多为正相关单尾。双尾：O21 Q3(b)，J22 Q3(e)，S23 Q1(b)，J24 Q3(a)。负相关：S23 Q1(c)。1% 水平：J22U Q3(b)，J23 Q2(b)(d)，J25 Q1(b)，S25 Q2(b)。② 由 Sxx、Syy、Sxy 算 PMCC（S1 内容）再检验（O21 Q3(c)–(d)，J22 Q3(a)–(b)，J23 Q2(c)–(d)，J24 Q3(a)）。③ PMCC 检验需要正态假设（J22 Q3(c)）。④ 查表找能支持某说法的最大显著性水平（S22 Q1(d)） | H0、H1 用 ρ 写；临界值照 FB p.27 抄 4 位小数（如 0.7143、0.5494、0.6485、0.7455）；语境结论；4 分最多（9 个） | S23 Q1，J24 Q3，O21 Q3，J23 Q2 |

### 6.4 考纲写了、真题还没考过（或极少考）的点

依据：13 份卷的索引检索，加上 `src/WST03/*_qp.txt` 的关键词检索。15 个条目每个都至少作为次要标签出现过，下面列出很少考或从未考过的具体要点。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 4.1 以**连续均匀（rectangular）**分布为模型的拟合优度检验 | 13 份卷**从未**出过。已考过的模型：离散均匀 3 次、二项 3 次、Poisson 3 次、正态 2 次、给定比例 2 次、给定 pdf 1 次（S23 Q4） | 做一张卡：E = n × (区间长 / 总长)，没有估计参数时 ν = k − 1；端点若由数据估计，还要再减 |
| 3.7 两总体**方差已知**的两样本检验 | 作主条目只有 J21 Q4(b) 一次，其余都是大样本、s² 代替 σ² | 公式同 3.8（FB p.25 有），一张卡写清楚两者的区别即可 |
| 3.5 完整的单样本 z 检验 | 只有 O21 Q1 一次。其余是求拒绝域（J23 Q1）、反求 μ（J21 Q4(c)）、用置信区间检验（S24 Q3(a)） | 练“求 X̄ 的拒绝域”与“用区间判断”，这两种写法 ER 批评最多 |
| 2.1 “Methods for collecting data” | 除随机数抽样外从未单独考过。随机数表只在 J21 Q1 用过 | 不单独做卡；保留一张“读随机数表：两位一组，跳过重复和超范围”的卡 |
| 2.2 配额抽样 | 只考过 2 次（J22 Q4(a) 描述做法；J25 Q5(a) 优缺点）。系统抽样 5 卷、分层抽样 5 卷 | 一张卡：非随机选取，各组配额满即止。优点不能写 quick、cheap、easy（见 6.5 第 12 条） |
| 4.2 列联表中因 E < 5 而**合并格** | 只有 J21 Q3(d) 一次（4.77 < 5）。拟合优度里的合并更常见（S21 Q5，J22U Q6，J24 Q4，J25 Q2）。Yates 校正按考纲不考；2×2 表只出过 S21 Q2（ν = 1） | 一张卡：先合并，再按合并后的行列数或组数算 ν |
| 5.1 含并列等级的计算 | 按考纲不出数值题，真题也从未出过；只考并列的处理方法（O20 Q3(c)，S22 Q1(a)，S24 Q2(d)） | 一张卡：平均等级，然后对等级用 PMCC 公式，不是 1 − 6Σd²/(n(n² − 1)) |
| 3.6 单样本、方差未知的大样本检验 | 只在 J23 Q1 出现（n = 100，用 s² 代替 σ²）；其余大样本题都是两样本 | 与 3.8 合成一张卡：n 大时 s² ≈ σ²，并由 CLT 得 X̄ 近似正态 |
| 主题 5 “Regression” | 考纲 S3 没有回归条目，真题也没有回归计算；只在 O21、J22、J23、J24 用 Sxx、Syy、Sxy 算 PMCC（S1 内容） | 不做回归卡；PMCC 的计算放到先修复习 |
| t 分布 | 考纲明确不考（3.6、3.8），真题也没有 | 不做卡 |
| PMCC 检验的前提 | 只有 J22 Q3(c) 问过：两个变量都服从正态（bivariate normal） | 与“何时用 Spearman”合成一张对比卡 |

**`WST03.md` §5 的缺口有了答案**：考纲没写的书写格式，可由 MS 和 ER 校准，见下一节：
- 置信区间写成 (a, b)，按要求的小数位；
- 拟合优度检验的假设只写分布族，参数是给定的才写出；
- 相关检验的假设用 ρ（或 ρₛ）写，并挂在 H0、H1 上；
- 结论要写进语境。

### 6.5 反复出现的评分惯例与考官提醒

ER 只有 J23、S23、J24 三份；没有标 ER 的引用来自 MS 的评分说明。各条出处在 `WST03.coverage.part1.md`、`part2.md` 中整理。本次审核用 `cite_check.py` 核对了下文所引的 66 处原文（MS、ER 文本层，必要时看渲染图），除 J25 Q5(c) 一处归类已改正外，全部相符。S24 Q5(a) 和 S23 Q5(c) 两处已按原文改正（见 6.1）。

1. **临界值要照表写到 4 位小数，即 “or better”**。
   - MS 的写法：
     - “Use of 1.64 or 1.65 is B0”（S21 Q3(a)，MS p.8）；
     - B1 要求 1.6449 或更精确（S25 Q4(b)，MS p.9）；
     - show-that 里也必须用 2.5758（J25 Q4(a)，MS p.9）；
     - 用 2.576 的，B1 不给，但 A1 照给（S24 Q7(b)，MS p.15）；
     - z 值不够精确时得 M1B0M1M1A1（J24 Q6(a)，MS p.11）。
   - ER 点名的错误：
     - 写 2.32 或 2.33（J23 Q5(a)，ER p.4）；
     - 写 −1.645（S23 Q6(b)，ER p.4）；
     - 写 1.645（J24 Q5(a)，ER p.4）；
     - 写 2.576（J24 Q6(a)，ER p.5）；
     - “not round the required z values”（S23 Q5，ER p.4）。
   - 相关系数临界值照 FB p.27 抄全，如 0.7143、0.5494。
2. **假设必须用总体参数写，并挂在 H0、H1 上**。
   - 相关检验：
     - 要用 ρ，并写明是 H0、H1：S22 Q1(c)（MS p.7），J22U Q3(b)（MS p.8），O21 Q3(b)(d)（MS p.8）；
     - 不能用 r：S24 Q2(b)（MS p.7），S25 Q2(b)（MS p.7）；
     - 只用文字写假设不给分：J22 Q3(b)，原文 “Do not allow hypotheses in words on their own”（MS p.7）。
   - 均值检验：
     - 要用 μ，下标要说明是哪一组：S22 Q2(b)（MS p.8），J21 Q4(b)（MS p.7），O20 Q5(b)（MS p.9）；
     - 用 t̄ 是 B0（S24 Q5(a)，MS p.11）。
   - ER 点名的错误：
     - 假设写成文字，或不用 ρ（S23 Q1(b)，ER p.3；J24 Q3(a)，ER p.3）；
     - 用字母代表两组却不说明哪个是哪个（J24 Q5(a)，ER p.4）。
   - 没写假设或方向写反，最后的语境 A 分为 0：S22 Q1(c)（MS p.7），J22 Q4(b)、Q6(b)（MS pp.9, 11），S21 Q5(d)（MS p.10），S25 Q3(b)（MS p.8），J24 Q1（MS p.6），S23 Q2(b)、Q4(b)（MS pp.7, 9）。
3. **单尾还是双尾，要跟题意一致**。
   - 题目是单侧说法却用双尾 H1：S22 Q1(c) 最多得 B1B1dM1A0（MS p.7）；S25 Q2(b) 最多 B0B0M1A0（MS p.7）；J23 Q2(b) 为 B0B1M1A0（MS p.9）。
   - 题目问 “a relationship” 时必须双尾（O21 Q3(b)，MS p.8）。
   - 临界值跟着考生自己写的 H1 判分：S23 Q1(b) 写了单尾 H1 时，接受 −0.5636（MS p.6）。
   - ER：双尾检验却用了单尾临界值（S23 Q1(b)，ER p.3；J24 Q3(a)，ER pp.3–4）。
4. **χ² 的用语：说 association 或 independence，不能说 correlation**。
   - 假设里写 “relationship”“correlation”“connection”“link” 都是 B0（O20 Q2(b)，MS p.6；J23 Q3(b)，MS p.11；S21 Q2，MS p.7）。
   - 结论里可以容忍 “relationship”“connection”，不接受 “correlation”：O20 Q2(b)（MS p.6），S21 Q2（MS p.7），J22U Q4（MS p.9），S23 Q2(b)（MS p.7），S25 Q3(b)（MS p.8）。J25 Q5(c) 只写了不能用 correlation 代替 association，假设和结论都如此；允许用 dependent 代替 not independent（MS p.10）。
   - ER：列联表检验最常见的错误是 H0、H1 写反（J23 Q3，ER p.4；S23 Q2(b)，ER p.3；J24 Q1，ER p.3）；假设和结论漏了关键语境词，如 “making a claim” 和 “age”（J23 Q3，ER p.4）。
5. **拟合优度的假设：参数是给定的才写出，由数据估计的不写**。
   - 给定 p 时要写 B(4, 0.5)，漏写是最常见的错误（J23 Q4(a)，MS p.12；ER p.4）。
   - 参数由数据估计时只写分布族：
     - “mention of 1.75 is B0”（J24 Q4(d)，MS p.9；ER p.4）；
     - 不接受 “B(5, 0.488) is a suitable model”（S25 Q5(c)，MS p.10）；
     - “If parameters used then B0”（S21 Q5(d)，MS p.10）。
   - 给定比例时，假设里要写出比例或说“给定的比例”，只写 “manager's belief is correct” 不给分（S24 Q4(a)，MS p.9）。
6. **自由度：每估计一个参数减 1；E < 5 的格先合并**。
   - 估计参数后的 ν：
     - J22 Q6(c) 是 8 − 3（MS p.11），J21 Q5(c) 是 5 − 3（MS p.8）；
     - J22U Q6(c)、S25 Q5(c) 是 6 − 1 − 1（MS p.11；MS p.10）；
     - J24 Q4(d)、J25 Q2(d) 是 5 − 1 − 1（MS p.9；MS p.7）；
     - S21 Q5(d) 写明 “Only f.t. ν = r − 2”（MS p.10）；
     - p 是给定的就不减：J23 Q4(a) 的 ν = 4（MS p.12）。
   - 常见错误：ν 写成 4，从而用 9.488（S22 Q7，MS p.13）。
   - ER：估计 p 之后仍用原来的 ν 重做一遍（J23 Q4(c)，ER p.4）；列联表的 ν 写错（S23 Q2(b)，J24 Q1，ER p.3）。
   - 合并格：
     - J21 Q3(d) 要写出 4.77 < 5，再说明合并后成 3×3（MS p.6）；
     - S21 Q5(d) 合并 0–2 或 5–8 之一就得 M1（MS p.10）；
     - J22U Q6(c) 合并 0 和 1（MS p.11）；
     - J25 Q2(c) 合并的理由是 “all expected frequencies … greater than 5”（MS p.7）。
7. **题目要什么形式，就给什么形式**。
   - χ² 检验只给 p 值、不给临界值：S21 Q2 单独给 p 值是 B0B0（MS p.7）；O21 Q4(c) 得 M1M1B1B0A1（MS p.9）。
   - 正态均值的检验可以用 p 值：O21 Q1（MS p.6），J22 Q2(a)（MS p.6），J21 Q4(b)（MS p.7），S24 Q5(a)（p = 0.107，MS p.11）。
   - 题目要拒绝域却算 z 值或 p 值，要扣分；把拒绝域写成区间形式只得特殊分（J23 Q1(c)–(d)，ER p.3；MS pp.7–8）。
   - 印刷了 “Solutions relying entirely on calculator technology are not acceptable” 的：S24 Q3(b)；要求 “Using standardisation” 的：S25 Q8，其 A 分要求看得到标准化过程（MS p.14）。
8. **CLT 与大样本的说明：说的是样本均值，而且两个样本都要提到**。
   - 说 “Population means are normally distributed” 是 B0（J22 Q2(b)，MS p.6）。
   - 两个样本均值都要提到（S21 Q4(c)，MS p.9）。
   - 大样本有两个用处，各 1 分：CLT 使两个样本均值近似正态；两个样本方差可代替总体方差（O20 Q5(c)，MS p.9；J25 Q3(c)，MS p.8）。
   - σ² = s² 要 “imply for both samples”（S21 Q4(d)，MS p.9）。
   - 写成单数 “the sample is large enough” 不给分（S22 Q2(c)，MS p.8）。
   - “Samples are independent” 是 B0（S24 Q5(b)，MS p.12）。
   - 不能写成 sₓ = s_y 之类（S25 Q4(c)，MS p.9）。
   - ER 点名的错误：
     - 只写 s² = σ²，没说两组都如此；
     - 把“样本独立”当作假设；
     - 本该用 CLT，却假设总体正态。

     见 S23 Q6(c)–(d)（ER pp.4–5）、J24 Q5(b)（ER p.4）。
   - 总体本来就是正态时，不需要 CLT（J23 Q6(b)，ER p.5）。
   - 假设条件也要写进语境（J23、S23 总评，ER p.3）。
9. **相关检验的解释**。
   - 选 Spearman 的理由要说到点上：
     - 数据是等级（ordinal），或预期关系不是线性的（S23 Q1(a)，MS p.6）；
     - 数据已经排了等级，或不是正态（S24 Q2(c)，MS p.7）；
     - 判断给出的分数不是有意义的刻度（O21 Q3(e)，MS p.8），只写 “because it is ranked” 不给分。
   - ER：把“有并列等级”或“分布是正态”当作选 Spearman 的条件，是错的（S23 Q1(a)，ER p.3）。
   - 驳斥因果说法时，必须明确写出 “cause” 或 “causation”（J21 Q2(c)，MS p.5）。
   - 并列等级：
     - 用平均等级，再对等级算 PMCC（O20 Q3(c)，MS p.7）；
     - 不接受 “add 0.5 to both ranks”（S22 Q1(a)，MS p.7）；
     - 写出的并列等级必须是 1.5，并点名两个对象（S24 Q2(d)，MS p.7）。
   - PMCC 检验要假设两个变量都是正态（J22 Q3(c)，MS p.7）。
10. **估计量的定义按关键意思给分**。
    - “不是 statistic”：
      - 要说它含未知的总体参数（S22 Q5(a)，MS p.11）；
      - 接受 “σ is unknown”，不接受把 σ 说成 “unknown variance”（S23 Q3(a)，MS p.8）；
      - 只复述题干 “μ、σ² 未知”不得分（S23 Q3(a)，ER p.3）。
    - “是 statistic”：说 “because it is known” 太含糊（S25 Q6(a)，MS p.11）。
    - “无偏”：要说期望等于参数，“bias = 0” 是 B0（S22 Q5(b)，MS p.11）。
    - 证明有偏：
      - 必须写出 E(S) ≠ μ（S23 Q3(b)，ER p.3）；
      - 要用期望记号（S25 Q6(b)，MS p.11）；
      - 评分是 A1cso，写 “(1 + α)/2 ≠ α” 是 M0A0（O20 Q1(a)，MS p.5）。
    - 求无偏条件，要令 aE(X₁) + bE(X₂) = μ（S23 Q3(d)，ER p.4）。
    - 编码数据：
      - Var(X + a) = Var(X)，把方差加 1000 得 1064 是错的（J23 Q1(a)(ii)，ER p.3）；
      - 印刷结果要写明是 x̄ = 1008.47，不能标成 y（J23 Q1(a)(i)，ER p.3）。
11. **线性组合的方差陷阱**。
    - 方差总是相加，差也一样。“3 个之和”与“3 倍”要分清：
      - O20 Q7(a) 用 sd 3.75 要扣分（MS p.11）；
      - 4Y ~ N(48, 4² × 0.8²)（J21 Q6(b)，MS p.9）。
    - ER 点名的错误：
      - 用 Var(3P) 得 3600，应为 1200（J23 Q7(a)，ER p.5）；
      - 写 4 × 4.5²，应为 2 × 4.5²（J24 Q7(a)，ER p.5）；
      - 写 41 + σ²，应为 41 + 3σ²（S23 Q7(b)，ER p.5）；
      - 把 S₁ 与 S̄ 当作独立，Var 得 27，应为 13.5，评分 M0A0M1M0M1A0（J24 Q7(c)，ER p.5；MS p.12）。
    - 标准化要除以标准差，不是方差（J24 Q7(b)–(c)，ER p.5）。z 的符号要与标准化式一致，否则即使答案对也丢最后的 A（S23 Q7(b)，ER p.5）。
    - “differ by more than d” 要算 2 × P(D > d)：S21 Q6(b)（MS p.11），O21 Q7(a)（MS p.12），S24 Q6(b)（MS p.13），J25 Q7(b)（MS p.12），S25 Q8(b)（MS p.14）。S23 Q5(c)(ii) 的不重叠也有两个区域（ER p.4）。
    - 整数答案要按不等式方向取整；答案错时，解法要看得到：
      - n = 62（S22 Q3(d)），n = 43（J22U Q2(b)），最大 n = 54（O21 Q5(c)），n = 11（O21 Q7(b)），n = 80（S24 Q7(b)）；
      - c = 8（S22 Q6(b)，解法须可见），w = 2.23（J22U Q7(d)）；
      - 负根要舍去：O20 Q7(c) 的 −14，J25 Q7(c) 的 −101。
    - ER：很多人没看出问的是 X̄ 的分布，方差用错（J23 Q6(d)，ER p.5；S23 Q5(c)，ER p.4）。
12. **抽样题要写全每一步，理由要具体**。
    - 分层抽样：
      - 各层分别编号，在各层内用随机数抽取，并写出各层人数；
      - 只写 “simple random sample of 20 A, 80 B …”，没有随机数步骤，得 M0M1A1（O21 Q4(a)，MS p.9）；
      - 各层人数要取整：54、31、15，不能写 53.75、31.25（J24 Q2(b)，ER p.3）。
    - 系统抽样：
      - 在第一个区间内随机选起点，然后每隔 k 个取一个（O20 Q4(a)，MS p.8；J22U Q1(a)，MS p.6）；
      - 不是把总体分成 80 组、每组取一个（J24 Q2(a)，ER p.3）。
    - 配额抽样：要描述非随机的选取；写“编号”的不给分（J22 Q4(a)，MS p.8）。
    - 理由要针对情境：
      - 配额抽样的优点不能写 quick、cheap、easy（J25 Q5(a)，MS p.10）；
      - 系统抽样的理由不能写 “accurate”“fast” 这类样本相对普查的好处（S25 Q1(a)，MS p.6）；
      - 已有名单时，不能说“需要抽样框”（S24 Q1(b)，MS p.6）。
13. **结论要写进语境，点名变量或说法**。
    - MS 规定的必写词：
      - “rank” 和 “total tournaments”（S22 Q1(c)，MS p.7）；
      - “the officer or mean scores”（J22 Q2(a)，MS p.6）；
      - “mean”、“academic” 和 “vocational”（S21 Q4(b)，MS p.9）；
      - “apples” 或 “belief”（O21 Q2，MS p.7）；
      - “positive correlation”、“ranks” 和 “judges”（S25 Q2(b)，MS p.7）；
      - “rank”、“kettles” 和 “price”（S24 Q2(b)，MS p.7）；
      - brand A、lower fat content 和 brand B（S23 Q6(b)，MS p.11）。
    - ER 批评缺少语境的地方：J23 Q2(b)(d)、Q5(a)（ER p.4）；S23 Q2(b)、Q6(b)（ER pp.3–4）；J24 Q1、Q3、Q5(a)（ER pp.3–4）。
    - 用检验结果做决策时，要同口径比较：比的是每株的利润，不是 50 株 A 对 40 株 B（J23 Q5(b)，ER p.4）。
14. **印刷结果（show that）要有足够的中间步骤**。
    - A* 分要求写出中间一步：S25 Q7(a)（MS p.12），J25 Q4(a)（MS p.9）。
    - ER 要求 show-that 写出充分的步骤：S23 Q3(e)、Q4(a)（ER p.4）；J24 总评（ER p.3）。
