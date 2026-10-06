# WFM01 · FP1 Further Pure Mathematics 1：考纲摘要

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019；文本版 `registry/src/fb/fb.txt`。页码同样是印刷页码。
- 公式、上下标、不等号都对照渲染页图核过（`registry/work/fm-spec/pg-*.png`、`fb-*.png`），因为纯文本抽取会丢掉 ≤、≥、√ 和上标。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WFM01/01**。另有区域卷 **WFM01/01A**：考纲里没有这个代码，英国文化协会中国区 2026 年 1 月和 6 月以 WFM01A 报名。/01A 有自己的试卷和评分方案，题目与 /01 不同 | SPEC p.7、p.78 Appendix 1；versions.md §1.6 |
| 单元名称 | Unit FP1: Further Pure Mathematics 1。p.67 的表里写作 “FP1: Further Mathematics 1”，是同一单元，属考纲自身用词不一致 | SPEC p.30、p.67 |
| AS/A2 定位 | 单元页：“Compulsory unit for IAS Further Mathematics and Pure Mathematics”，“Compulsory unit for IAL Further Mathematics and Pure Mathematics”。p.67 “IAS or IA2” 一栏为 **IAS**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.30、p.67、p.7 |
| 资格结构 | IAS Further Mathematics：FP1 必考，另从 FP2, FP3, M1–M3, S1–S3, D1 中选。IAL Further Mathematics：FP1 加 FP2 或 FP3 二选一为必考。IAS Pure Mathematics：P1, P2, FP1。IAL Pure Mathematics：P1–P4, FP1，再加 FP2 或 FP3 | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.30 |
| 题量（参考） | 2025 年 6 月卷封面：“There are 9 questions”，总分 75。这只是该卷的情况，考纲没有固定题量 | `registry/src/WFM01/2025-06_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra、symbolic differentiation or integration 功能的计算器，计算器里也不得存有可调出的公式 | SPEC p.30；Appendix 6，p.86 |
| 卷面要求（试卷封面，不是考纲） | “show sufficient working to make your methods clear. Answers without working may not gain full credit.”非精确答案默认保留 3 位有效数字 | 2025-06 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。FP1 部分在 FB p.6；考生还可能要用 P1、P2 的公式（FB p.6 原话：“may also require those formulae listed under Pure Mathematics P1 and P2”） | SPEC p.30；FB p.6 |
| 开考季 | **January and June**。p.70 注：“From June 2020, all units will be assessed in January and June and just units P1, P2, P3, P4, M1, M2, S1 and S2 in October” | SPEC p.7、p.70 |
| 特殊考季 | 2020 年 6 月整季取消。2020 年 10 月和 2021 年 10 月例外地开考了 FP1。2021 年 6 月发布了试卷和评分方案，但考试取消，改用教师评估成绩，没有考官报告 | versions.md §1.5 |
| 2018 版首考 | **“First assessment: June 2019.”** 2018 版考纲下实际开考的考季：2019 年 6 月、2020 年 1 月，之后每年 1 月和 6 月 | SPEC p.30、p.7、p.70；versions.md §1.4 |
| 旧考纲同代码 | WFM01 这个代码 2013 版旧考纲也用过，旧版最后一次是 **2019 年 1 月**，不算本考纲的真题。p.1 说 “The Further, Mechanics and Statistics units have not changed”，所以旧卷内容兼容，可作额外练习。另外，Pearson 官网把 2019 年 6 月和 2020 年 1 月的 WFM01 放在 2013 文件夹里，但按首考日期它们属于 2018 版 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specification for P1 and P2, their prerequisites and associated formulae, is assumed and may be tested.”另须：① 知道在 f(x) **连续**的区间上，可以通过 f(x) 变号来定位 f(x)=0 的根（印刷时这一点被拆成两个项目符号，实为一句）；② 知道把图形绕 (0, 0) 旋转任意角；③ 会用二次多项式除三次多项式；④ 会用二次多项式除四次多项式 | SPEC p.30 |
| 评估目标分配（75 分中） | AO1 25–30；AO2 25–30；AO3 0–5；AO4 5–10；AO5 5–10。各 AO 定义见 p.68：AO2 是严谨论证与证明，AO5 是计算器与公式册的使用和答案精度 | SPEC p.68–69 |
| 须背公式（不在 FB 里） | 考纲列出，原文：“expected to remember and which will not be included in formulae booklets”。① 对 ax²+bx+c=0，α+β = −b/a，αβ = c/a；② Σ_{r=1}^{n} r = ½n(n+1) | SPEC p.31 |
| 记号 | 见 Appendix 7。复数记号在 p.90，规定 arg z 的主值范围为 −π < θ ≤ π（原文误把 θ 印成 x）。矩阵记号在 p.91：M⁻¹、Mᵀ、det M 或 \|M\| | SPEC pp.87–92 |
| 单元概述 | “Complex numbers; roots of quadratic equations; numerical solution of equations; coordinate systems; matrix algebra; transformations using matrices; series; proof.” | SPEC p.30 |

---

## 2. 规格条目逐条（FP1.3 Unit content）

### 主题 1 Complex numbers（p.32）

**1.1 Definition of complex numbers in the form a + ib and r cos θ + i r sin θ**（p.32）
- 要求：掌握复数的代数式 a + ib 与模–辐角式 r cos θ + i r sin θ。考纲点名必须知道这些概念的含义：**conjugate, modulus, argument, real part, imaginary part** 以及 **equality of complex numbers**。
- 公式：FB 的 FP1 部分没有复数公式。记号见 p.90：|z| = √(x²+y²)，主辐角 −π < θ ≤ π，共轭记作 z*。

**1.2 Sum, product and quotient of complex numbers**（p.32）
- 要求：会做复数的加、乘、除，指导栏给出 **|z₁z₂| = |z₁||z₂|**。
- 排除：“Knowledge of the result arg(z₁z₂) = arg z₁ + arg z₂ is **not required**.”

**1.3 Geometrical representation of complex numbers in the Argand diagram. Geometrical representation of sums, products and quotients of complex numbers**（p.32）
- 要求：在 **Argand diagram** 上表示复数，并能用几何方式表示和、积、商。指导栏为空。

**1.4 Complex solutions of quadratic equations with real coefficients**（p.32）
- 要求：解实系数一元二次方程的复数根。指导栏为空。

**1.5 Finding conjugate complex roots and a real root of a cubic equation with integer coefficients**（p.32）
- 要求：求**整系数三次方程**的一对共轭复根和一个实根。须知道：若 z₁ 是 f(z)=0 的根，则 z₁* 也是根。
- 相关先修：用二次式除三次式（p.30）。

**1.6 Finding conjugate complex roots and/or real roots of a quartic equation with real coefficients**（p.32）
- 要求：求**实系数四次方程**的共轭复根和/或实根。考纲举了两个例子：(i) 已知一个复根 x = 2 + i，用代数方法求其余三根；(ii) 已知 g(1)=0、g(−2)=0，用代数方法把 g(x)=0 完全解出。关键词是 “use algebra”。
- 相关先修：用二次式除四次式（p.30）。

### 主题 2 Roots of quadratic equations（p.33）

**2.1 Sum of roots and product of roots of a quadratic equation**（p.33）
- 要求：对 ax²+bx+c=0（两根 α、β），α+β = −b/a，αβ = c/a。
- 公式：**须背**，不在 FB 里（p.31）。

**2.2 Manipulation of expressions involving the sum of roots and product of roots**（p.33）
- 要求：把含 α、β 的对称式用 α+β 和 αβ 表示。考纲点名须知恒等式 **α³+β³ ≡ (α+β)³ − 3αβ(α+β)**。
- 公式：这条恒等式不在 FB 里，须掌握。

**2.3 Forming quadratic equations with new roots**（p.33）
- 要求：给定以 α、β 表示的新根，构造新的二次方程。考纲举的新根有 α³, β³；1/α, 1/β；1/α², 1/β²；α + 2/β, β + 2/α，并写 “etc.”。

### 主题 3 Numerical solution of equations（p.33）

**3.1 Equations of the form f(x) = 0 solved numerically by: (i) interval bisection, (ii) linear interpolation, (iii) the Newton-Raphson process**（p.33）
- 要求：用三种方法数值求解 f(x)=0：区间二分法、线性插值法、Newton-Raphson 法。
- 限制：“f(x) will involve **only functions used in P1 and P2**.”Newton-Raphson 中所需的求导 “only … as defined in unit P1 and P2”，即只涉及 P1/P2 范围内的求导。
- 公式：Newton-Raphson 迭代式 x_{n+1} = x_n − f(x_n)/f′(x_n) 在 **FB p.6** 中给出。区间二分法和线性插值法 FB 不给公式。
- 先修：用变号法定位根（p.30 Prerequisites）。

### 主题 4 Coordinate systems（p.33）

**4.1 Cartesian equations for the parabola and rectangular hyperbola**（p.33）
- 要求：熟悉 **y² = 4ax** 及参数式 x = at², y = 2at；熟悉 **xy = c²** 及参数式 x = ct, y = c/t。
- 公式：两种标准式和两种参数式都在 **FB p.6**（Conics 表）。

**4.2 Idea of parametric equation for parabola and rectangular hyperbola**（p.33）
- 要求与排除：“The idea of (at², 2at) as a general point on the parabola is **all that is required**.”即只要求把 (at², 2at) 当作抛物线上的一般点来用。

**4.3 The focus-directrix property of the parabola**（p.33）
- 要求：理解焦点（focus）与准线（directrix）的概念，知道抛物线是到焦点和到准线距离相等的点的轨迹（locus of points equidistant from focus and directrix）。
- 公式：FB p.6 给出抛物线焦点 (a, 0)、准线 x = −a。直角双曲线的焦点和准线在 FB 中标为 “**Not required**”。

**4.4 Tangents and normals to these curves**（p.33）
- 要求：求抛物线和直角双曲线的切线（tangent）与法线（normal）。求导方式是把曲线写成 y = 2a^{1/2}x^{1/2}、y = c²/x 后直接求导。
- 排除：“**Parametric differentiation is not required.**”

### 主题 5 Matrix algebra（p.34）
注意：Issue 3 原文这一主题的标题印作 “5. Matrix algebra integration”，已对照渲染页图确认。“integration” 是多余词，本单元不含积分内容。

**5.1 Addition and subtraction of matrices**（p.34）：矩阵加减。指导栏为空。

**5.2 Multiplication of a matrix by a scalar**（p.34）：矩阵数乘。指导栏为空。

**5.3 Products of matrices**（p.34）：矩阵乘法。指导栏为空。

**5.4 Evaluation of 2 × 2 determinants**（p.34）
- 要求：计算 2×2 行列式，并理解 **singular and non-singular matrices**（奇异与非奇异矩阵）。
- 公式：行列式和逆矩阵公式都不在 FB 里。

**5.5 Inverse of 2 × 2 matrices**（p.34）
- 要求：求 2×2 逆矩阵，会用 **(AB)⁻¹ = B⁻¹A⁻¹**。

### 主题 6 Transformations using matrices（p.34）

**6.1 Linear transformations of column vectors in two dimensions and their matrix representation**（p.34）
- 要求：二维列向量的线性变换及其矩阵表示。考纲强调：AB 表示的变换是**先做 B、再做 A**（“B followed by … A”）。

**6.2 Applications of 2 × 2 matrices to represent geometrical transformations**（p.34）
- 要求：能识别并使用下列**单一变换**的矩阵：关于坐标轴和直线 y = ±x 的反射；绕 (0, 0) **任意角**的旋转（rotation through any angle）；平行于 x 轴、y 轴的伸缩（stretches）；以 (0, 0) 为中心、比例因子为 k 的放大（enlargement，k ≠ 0，k ∈ ℝ）。
- 公式：FB p.6 给出两个矩阵：绕 O 逆时针旋转 θ 的矩阵 (cos θ, −sin θ; sin θ, cos θ)，以及关于直线 y = (tan θ)x 反射的矩阵 (cos 2θ, sin 2θ; sin 2θ, −cos 2θ)。伸缩和放大矩阵 FB 不给。
- 版本注意：FB Issue 2 删去了旧版中 “In FP1, θ will be a multiple of 45°” 一句，理由是这句只适用于反射、不适用于旋转（FB PDF p.3 变更说明）。所以旋转角可以是任意角，这与考纲 “rotation through any angle” 一致。

**6.3 Combinations of transformations**（p.34）
- 要求：能识别并使用**复合变换**的矩阵表示。

**6.4 The inverse (when it exists) of a given transformation or combination of transformations**（p.34）
- 要求：求单一变换或复合变换的逆变换（存在时）。理解 **determinant as an area scale factor**，即行列式是变换的面积比例因子。

### 主题 7 Series（p.34）

**7.1 Summation of simple finite series**（p.34）
- 要求：能求 Σr、Σr²、Σr(r²+2) 这类有限和（考纲例子均为 r = 1 到 n），即用标准求和公式代入并化简。
- 排除：“**The method of differences is not required.**”（差分法属于 FP2 2.1。）
- 公式：Σr = ½n(n+1) **须背**（p.31）。Σr² = (1/6)n(n+1)(2n+1) 和 Σr³ = ¼n²(n+1)² 在 **FB p.6**。

### 主题 8 Proof（p.35）

**8.1 Proof by mathematical induction**（p.35）
- 要求：数学归纳法证明，考纲列了四类：
  - (i) **summation of series**，例：Σr³ = ¼n²(n+1)²，或 Σr(r+1) = n(n+1)(n+2)/3；
  - (ii) **divisibility**，例：3^{2n} + 11 能被 4 整除；
  - (iii) **finding general terms in a sequence**，例：u_{n+1} = 3u_n + 4、u₁ = 1，证明 u_n = 3^n − 2；
  - (iv) **matrix products**，例：(−2 −1; 9 4)^n = (1−3n, −n; 9n, 3n+1)。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| α+β = −b/a，αβ = c/a | **须背**（考纲明列） | SPEC p.31 |
| Σr = ½n(n+1) | **须背**（考纲明列） | SPEC p.31 |
| Σr²、Σr³ | FB 给出 | FB p.6 |
| Newton-Raphson 迭代式 | FB 给出 | FB p.6 |
| 抛物线 y²=4ax、(at², 2at)、焦点 (a,0)、准线 x=−a | FB 给出 | FB p.6 |
| 直角双曲线 xy=c²、(ct, c/t)；焦点/准线 “Not required” | FB 给出 | FB p.6 |
| 旋转矩阵、关于 y=(tan θ)x 的反射矩阵 | FB 给出 | FB p.6 |
| α³+β³ 恒等式、2×2 行列式与逆矩阵、(AB)⁻¹ = B⁻¹A⁻¹、伸缩/放大/坐标轴反射矩阵、二分法与线性插值的做法 | FB **未给**。考纲要求掌握，但未列入 p.31 须背清单 | SPEC pp.33–34；FB p.6（已核对没有这些） |
| P1、P2 的公式（余弦定理、等差/等比数列、二项式、梯形法则等） | FB 给出，FP1 可能用到 | FB p.3 |

---

## 4. 与相邻单元的界线

- **P1/P2（先修，可直接考）**：FP1 默认学过 P1、P2 及其公式（p.30）。FP1 中的函数和求导都限定在 P1/P2 范围（3.1）。P1 求导不含链式法则（P1 4.1 指导栏：“Knowledge of the chain rule is not required”，p.16）。与此一致，4.4 指导栏要求的是对 y = 2a^{1/2}x^{1/2}、y = c²/x 直接求导，并排除参数求导。
- **P3（FP1 不以它为先修）**：P3 6.1 用变号法定位根、6.2 用 x_{n+1} = f(x_n) 迭代求近似解（p.25），这两种方法属于 P3。区间二分法、线性插值法、**Newton-Raphson** 都在 FP1 3.1，IAL 2018 版的 P3 里没有 Newton-Raphson。FP1 先修里单独列出 “变号定位根”，正是因为 FP1 不以 P3 为先修。P3 的链式、积、商法则和 e^x、ln x、三角函数求导不属于 FP1 范围。
- **P4（FP1 不以它为先修）**：参数求导在 P4 5.1（p.27），FP1 4.4 明确排除。参数方程与直角坐标互化在 P4 3.1。反证法（proof by contradiction）在 P4 1.1；FP1 只考数学归纳法。
- **FP2（以 FP1 为先修）**：
  - 差分法求和 → FP2 2.1，FP1 7.1 明确排除；
  - Euler 关系、De Moivre 定理、复数的 n 次根、Argand 图上的轨迹与区域、z 平面到 w 平面的变换 → FP2 主题 3。FP1 只到复数运算、Argand 图表示和多项式方程的根，不要求 arg(z₁z₂) = arg z₁ + arg z₂。
- **FP3（以 FP1 为先修）**：
  - 椭圆和双曲线（含离心率、焦点–准线性质、y = mx + c 的相切条件）→ FP3 主题 2，FP3 2.1 写明 “Extension of work from FP1”；
  - 3×3 矩阵、转置、三维变换、特征值与特征向量、对角化 → FP3 主题 6，6.1 写明 “Extension of work from FP1 to 3 dimensions”。FP1 只到 2×2。

---

## 5. 印刷问题与缺口
- 主题 5 标题印作 “Matrix algebra integration”（p.34），多了 “integration”，按 Matrix algebra 理解。
- p.67 把单元名写成 “FP1: Further Mathematics 1”，单元页写 “Further Pure Mathematics 1”。
- Appendix 7 第 7.6 条把主辐角范围印作 “−π < x ≤ π”（p.90），x 应为 θ。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 往届真题

2018 考纲下 WFM01 的试卷、MS、ER 收集情况见 `../../inventory/fm-mech.json` 与 `../../inventory/fm-mech-gaps.md`。注意：这两个文件仍把 2020-10 至 2022-06 的 QP 记为 “text only (Finder)”、MS 记为缺失；这 12 个 PDF 后来在 GitHub `RayZ3R0/papernexus-finder`（@921bdf4f）找到，已放在 `registry/src/WFM01/`（见 `WFM01.coverage.part1.md` “New sources found in this pass”）。inventory 本次没有改动，应由其维护者更新。

逐题索引（合并版）：`WFM01.questions.json`（同一文件夹；由 `WFM01.questions.part1.json` 与 `part2.json` 合并、去重、排序，2026-10-06 审核，改正同步写回两个 part 文件）。各卷来源与缺失文件见第 7 节、`WFM01.coverage.part1.md`、`WFM01.coverage.part2.md`。

## 7. 审核记录（2026-10-06）

本节与第 8 节中的路径都相对于 `registry/`。脚本在 `work/wfm01audit/scripts/`，改正清单在 `work/wfm01audit/fixes.json`（每条写明改了什么和理由），改动前的 part 文件与本文件备份在 `work/wfm01audit/backup/`。

- **合并**：`WFM01.questions.json` = part1（70 题，2019-06 至 2022-06，8 份卷）+ part2（55 题，2023-01 至 2025-06，6 份卷），按 id 去重（没有重复），按考季、卷别、题号排序，共 125 题、355 个小问、1050 分。`merge_validate.py` 检查：字段齐全；各小问分值之和等于题目总分；spec id 都在 `spec-items.fm.json` → WFM01 中；series 符合 YYYY-MM；id 与 paper 一致；每份卷 75 分且题号连续；引号内原文不超过 25 词。改正后 0 个问题（合并时有 1 个：O21 Q9(i) 的 27 词“引文”，见改正 F02）。
- **自动比对**（`checks.py`、`pagecmd.py`，结果在 `work/wfm01audit/checks.txt`）：
  - 12 份有 PDF 的卷：每题总分、各小问分值与 QP 文本印刷的 “(Total …)” 和 (n) 一致；QP 把几个小问合印一个分值、索引按 MS 拆开的共 7 处，都已在 coverage 文件中说明（J21 Q6(c)、O21 Q2(b)、J23 Q4(a)、S23 Q7(c)、S24 Q1(ii)、S24 Q5(a)、S24 Q6(b)）。S19、J20 只有 Finder 文本，分值已在 part 1 对照 Finder 文本核过。
  - `final_form` 里的数值答案（小数和两位以上整数）都能在该卷 MS 文本中找到。
  - 461 处 “(MS p.n)”“(ER p.n)” 引用：所指页面都是该题（16 处自动匹配不到题号，逐页看过，都是同一题的续页）。
  - 命令词都出现在该题 QP 文本中；唯一的归一化是 “Give a full description” 记作 “Describe fully”（S21 Q3(e)、J22 Q5(a)）。
  - 所有 `ms`、`er` 字段里加引号的短语，逐条与 MS、ER 原文比对，凡不是原话的都已改写（F02、F04–F16）。
- **完整性**：`versions.json` 的预期考季为 2019-06 至 2026-06 共 16 季（FP1 只有 1 月、6 月，另加 2020-10、2021-10 两个疫情秋季考季）。索引了 14 份卷，即所有能拿到 QP 文本的卷（12 份 PDF + S19、J20 两份 Finder 文本），没有漏卷。SAM（S59759A）不是考季，不收；2019-01 及以前的 WFM01 属 2013 考纲，不收。
  - **所有来源都拿不到的卷**：2026-01 /01 与 /01A、2026-06 /01 与 /01A（QP、MS、ER 全缺）。2025-06 /01A 是否存在无法确认（同季 Drive 上只有 WFM02、WME02 的 /01A）。（critic 2026-10-06：grademax 的 Pearson 链接索引 `finder/gh/grademax_maths_index.json` 里 2025 年 6 月只有 WMA11–WMA14、WFM02、WME02 有 /01A，本单元没有，所以这份卷很可能没有出过；属中等可信的指针，不是缺口。）
  - **缺 MS**：S19（`WFM01_01_rms_20190815.pdf`）、J20（`WFM01_01_rms_20200305.pdf`），这两份卷 18 题的 `ms` 为空，也没有自行推算答案。
  - **缺 ER**：S19、J20、O20、J21、O21、J22、S22、S24、J25、S25（S21 本来没有 ER）。新线索：WebSearch 结果列出 Pearson 链接 `…/International-Advanced-Level/Mathematics/2018/Exam-materials/wfm01-01-pef-20250814.pdf`，说明 S25 的 ER 已发布（pointer，官网 403，未取得）。
  - 2026-10-06 复查：Drive 标题检索（`WFM01A`、`F1A`、`FP1A`；2025-07-01 以后修改、标题含 `FP1`／`WFM01`／`Further Pure`），没有新的 FP1 试卷（检索到的学生作业只看了标题，没有打开）；examsolutions S3 镜像按 7 个缺失文件名探测，全部无对象（403）。
- **准确性**：对照 QP、MS、ER 原文逐条复核了 24 条，覆盖全部 14 份卷和全部 8 个主题：S19 Q6、J20 Q6、O20 Q4、O20 Q6、O20 Q7、J21 Q6、S21 Q3、O21 Q2、O21 Q9、J22 Q8、S22 Q6、J23 Q4、J23 Q7、S23 Q5、S23 Q7、S23 Q9、J24 Q2、J24 Q9、S24 Q5、S24 Q9、J25 Q4、J25 Q8、S25 Q3、S25 Q8（S25 Q8 另看了渲染图，确认 (b) 印的是 n ∈ ℕ）。逐条核了分值、spec 映射、终点形式和答案（重新计算）、MS 要点、ER 要点。错误分散在 O20、O21、S23、J25 四份卷，没有集中在某一个 part；引文问题集中在归纳法结论一类，已对全部 355 个小问做了引文全量比对。
- **改正**（合并文件和两个 part 文件同步修改）：
  1. F01 O20 Q4(b)：原 `ms` 暗示把 200 和 500 当上下限就丢 M 分。MS p.12 原意：这是常见错误，但若用了 199（即 S(500) − S(199) 的写法）M1 仍得分。已改。
  2. F03 S23 Q5(b)：原 `ms` 与 `final_form` 说必须写出带 “= 0” 的方程。该卷 MS p.11 明写 “Allow e.g., p = 40, q = –24, r = 3”。已改，并注明 (a) 的工作只出现在 (b) 中时 (a) 不给分。
  3. F02、F04–F16：14 处把转述放进引号、或引文与原文不符（O21 Q9(i)、J25 Q8(i)、S22 Q9(i)、J23 Q4(a)(ii) ER、J23 Q7(i)(a)、S23 Q9、J23 Q9、J24 Q4(a) ER、J24 Q7(a) ER、J24 Q10(i) ER、J25 Q1(b)、S25 Q3(i)、S25 Q8(b)、S24 Q8）。原话改为原文，转述去掉引号。
  4. 补充（不算错误）：E01 S19 Q6(c) 注明 Finder 文本无法确定立方的位置，(α + 1/β)³ 的读法不能排除；E02 J22 Q8(a) 注明 QP 表中印的 f(5) = 0.5834 与 MS 表和函数值 0.5840 不一致；E03、E04 S24 Q5(b)、S25 Q6(d) 补上 MS 对“只写系数”的条件；E05 S22 Q7(b) 把泛泛的终点改为 MS 答案（顺时针 60°，即逆时针 300°，绕 O）。
- **抽查中没有发现**分值、题目总分、spec 映射、数值答案、MS 页码的错误。
- **保留未改的差异**：`coverage.part2.md` §4 第 9 条把 “= 0” 写成所有卷的硬性要求；实际上 S23 的 MS 接受只写 p、q、r，S24、S25 在写出 ax² + bx + c = 0 形式时接受只写系数（见第 8.4 节第 5 条）。coverage 文件是构建记录，没有改动，以本节和索引为准。

## 8. 真题需求概览

**数据范围**：2018 考纲下能拿到题面的全部 14 份卷（S19、J20、O20、J21、S21、O21、J22、S22、J23、S23、J24、S24、J25、S25，均为 /01），共 125 题、355 个小问、1050 分。12 份有 MS（S19、J20 没有）；有 ER 的只有 J23、S23、J24 三份。S19、J20 的题面来自 Finder 文本，部分式子读不全（索引 `ask` 已标明）。缺的卷见第 7 节。下面的数字由 `work/wfm01audit/scripts/stats.py` 从索引统计（结果在 `work/wfm01audit/stats.json`）；“问法、终点、评分”来自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 7 节抽查过。

**引用写法**：J = January，S = June（5 月考的夏季卷），O = October，后接两位年份；题号与小问照试卷印刷。MS、ER 页码在索引条目 `ms`、`er` 字段末尾的 “(MS p.n)” “(ER p.n)”。

### 8.1 卷面结构

- 每卷 75 分、8–10 题（9 题 11 份，8 题 O20、S21 两份，10 题 J24 一份），单题 4–16 分，最常见 7–10 分。命令词（355 个小问）：Determine 135，Show that 54，Find 43，Write down 34，Prove 24，Show 14（多为画 Argand 图），Use 12，Describe fully／Describe 12，其余各 1–5 次。除 S19（全用 Find）和 S21（Find 8 次、Determine 0 次）外，“Determine” 是主要的求解命令词。
- **每份卷都有**：一道数值解法题（3.1，14/14）；一道复数多项式求根题（三次 1.5 七份、四次 1.6 七份，合起来 14/14）；至少一道圆锥曲线题（4.4，14/14；抛物线 13 份，只缺 J20；直角双曲线 12 份，缺 S19、S22）；一道求和题（7.1，14/14）；归纳法证明（8.1，14/14，其中 9 份卷有两个各 4–6 分的证明）；矩阵或变换题（主题 5、6，14/14）。二次方程根与系数题（主题 2）13/14，只有 S21 没有。
- 按小问的第一个 spec 计分值：复数 193（18%），圆锥曲线 221（21%），归纳法 124（12%），变换 119（11%），数值解法 118（11%），根与系数 117（11%），求和 100（10%），矩阵代数 58（6%）。
- **题面限制语**（按 QP 文本统计）：“Use calculus” 出现在多数圆锥曲线题（S19、J20、O20、O21 两题、J22 Q7（“using calculus”）、S22、S23、J24、S24、J25 两题、S25）；“Without solving the equation” 出现在主题 2 的多数题；“Solutions relying (entirely) on calculator technology are not acceptable／show all stages／detailed reasoning” 的题：2021–2022 年只有 J21 Q6、J22 Q7；2023 年以后 J23 3 题（Q2、Q3、Q6）、S23 2 题（Q2、Q6）、S24 2 题（Q2、Q4）、S25 2 题（Q3、Q8），J24、J25 没有。另有 “without using your calculator／a calculator” 的小问（J22 Q2(b)，S25 Q7(d)）。

### 8.2 每个考纲条目怎么考

“卷数／题数／小问／涉及分值”：一个小问可以带几个条目标签，所以各行相加大于 125 题、1050 分。“典型分值”是带该标签的小问最常见的分值。

| 条目 | 卷数／题数／小问／涉及分值 | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 复数的定义、模、辐角、共轭 | 11／11／22／51（缺 O20、O21、J25） | Determine 13，Find 6 | 求给定复数的模、辐角（弧度）；由模或辐角条件求参数：\|z\| = 5 求 λ（J21 Q6(a)）、arg z = π/4 求 λ（J24 Q9(b)）、\|z₂z₃/z₁\| = 2√5 求 p（S21 Q2(b)）、z₁ + z₂ 为实数求 z₂（S25 Q5(b)）；模–辐角式只出现 1 次（S25 Q5(a) 给出 r(cos 7π/6 + i sin 7π/6) 求 r） | 弧度按指定精度（1 d.p.、2 d.p.、3 s.f.、4 s.f. 都出过）；精确根式；要舍去不合条件的值；多为 2 分 | J21 Q6(b)，J22 Q2(c)，S23 Q6(d)，J24 Q9(b)，S24 Q4(c)，S25 Q5(b) |
| 1.2 复数的加、乘、除 | 10／11／19／56（缺 O20、O21、J23、J25） | Determine 11，Express 4，Find 3 | 商化成 a + bi，常注明不用计算器或要 detailed reasoning（J21 Q6(c)，J22 Q2(b)）；含参数的商（S21 Q2(a)，S23 Q6(b)，J24 Q9(a)）；用 \|z₁z₂\| = \|z₁\|\|z₂\|（S22 Q1(a)，S25 Q5(a)）；z 与 z* 的方程（S19 Q3(i)）；\|z² − 3\|（S24 Q4(a)）；50/z* = kz（S24 Q4(b)） | a + bi，分数化简；含参数时分开写实部、虚部；多为 3 分 | J21 Q6(c)，S21 Q2，J22 Q2(b)，S23 Q6，J24 Q9(a)，S24 Q4 |
| 1.3 Argand 图 | 13／13／14／27（缺 J20） | Show 11 | 几乎都是“把所有根画在同一张 Argand 图上”，接在多项式求根之后；画给定的复数（J22 Q2(a)，S22 Q1(c)，S25 Q5(c)）；根构成的三角形面积（J24 Q2(d)）、四边形周长（S24 Q2(d)）。考纲里“和、积、商的几何表示”从未单独考过 | 标注点名或坐标，共轭对关于实轴对称，相对距离正确；多为 2 分 | J21 Q6(d)，J23 Q3(d)，J24 Q2(d)，S24 Q2(c)(d)，J25 Q4(c) |
| 1.4 实系数二次方程的复数根 | 2／2／3／7（只有 S21 Q5、S25 Q7(d)） | Find，Express，Determine | 单独考只有 S21 Q5（含参数 d 的四个根）；但每道三次、四次求根题都要解二次因式，实际每卷都用到 | a + ib，最简形式；2–3 分 | S21 Q5，S25 Q7(d) |
| 1.5 整系数三次方程的共轭复根与实根 | 7／7／15／41（J20、J21、O21、J23、J24、S24、J25） | Determine 7，Write down 4，Solve 2 | 写出共轭根（1 分）；由共轭对得二次因式，再求实根或系数（4–5 分）；已知实根先求参数（J23 Q3(a)，S24 Q2(a)，J20 Q2(a)）；“Solve completely”（J23 Q3(b)，J24 Q2(b)） | 三个根都要列出，实根要在本问写出；系数为整数；1 分 + 4–5 分 | O21 Q4，J23 Q3，J24 Q2，S24 Q2，J25 Q4 |
| 1.6 实系数四次方程 | 7／7／18／48（S19、O20、S21、J22、S22、S23、S25） | Determine 8，Write down 6 | 给一个复根，求其余三个根；给两个复根，写出另两个再求全部系数（O20 Q3）；有重复正实根（J22 Q4）；求系数 A、B 或 P、Q（J22 Q4(d)，S22 Q4(c)，S25 Q7(c)）；“Use algebra”（S23 Q2(b)） | 四个根全部写出，含 i 的精确形式；写共轭根 1 分；其余小问 2–6 分，2 分最多 | O20 Q3，J22 Q4，S22 Q4，S23 Q2，S25 Q7 |
| 2.1 两根之和与积 | 13／13／16／30（缺 S21） | Write down 8，Determine 5 | 写出 α + β、αβ（1 分，常含参数 A、k）；反过来已知根为 1/p、1/q 求 pq、p + q（S24 Q5(a)）；由 α + β = 9αβ 求 k（S25 Q6(b)） | 分数；1 分为主 | O21 Q3(a)，J23 Q5(a)，S24 Q5(a)，S25 Q6(a)(b) |
| 2.2 对称式的计算 | 13／13／26／98（缺 S21） | Determine 16，Find 7 | α² + β²、α³ + β³ 成对出现（4 分，S19、O20、O21、S22）；单独 α² + β²（J24、J25）、α³ + β³（J21）；其他对称式：α/β² + β/α²（J23）、(α² + 1)(β² + 1)（S23）；证明 α³ + β³ 恒等式（S25 Q6(c)）；更多是嵌在 2.3 里求新根之和与积 | 最简分数；对称式 2–4 分 | O20 Q2(b)，O21 Q3(b)，J23 Q5(b)，S23 Q5(a)，S25 Q6(c) |
| 2.3 构造以新根为根的二次方程 | 13／13／14／60（缺 S21） | Find 6，Determine 6 | 新根全是 α、β 的组合：α + β²（O20）、α²/β（J21）、1/(α² + β)（O21）、α − 3/β（J22，反求系数 A、B）、α³ − β（S22）、α/β²（J23，含参数 k）、α/(α² + 1)（S23）、α − 1/β²（J24）、p/(p² + 1)（S24，根为 1/p、1/q）、α + 1/α（J25）、α² + β（S25） | 整数系数方程，“= 0”（个别卷的 MS 接受只写系数，见 8.4 第 5 条）；4–6 分 | O20 Q2(c)，O21 Q3(c)，S23 Q5(b)，J24 Q5(c)，S24 Q5(b)，S25 Q6(d) |
| 3.1 数值解法（二分、线性插值、Newton–Raphson） | 14／14／50／118 | Show that 12，Use 12，Determine 10，Find 7 | 先用变号定根（11 份卷）；Newton–Raphson 11 份卷（缺 J21、J22、S25），前一问多为求 f′(x)（9 次），S21 要迭代两次；线性插值 11 份卷（缺 J20、O20、J21）；二分 4 次（J21、J22、S23、S25）。函数以分数、负指数幂为主，三角函数（弧度）4 次（J21、S21、J24、S25），8^(5x) 1 次（S25）。另有：说明为何某端点不能作初值（J23 Q4(a)(ii)，f′ = 0）、验证 2 d.p. 精度（J20 Q5(c)）、补全函数值表（J22 Q8(a)） | 3 d.p. 为主，也有 2 d.p.（S19、J20、J24）、3 s.f.（J22）、4 s.f.（S25）；区间写成 [a, b]；多为 2 分 | O21 Q2，J22 Q8，J23 Q4，S23 Q7，J24 Q6，S25 Q3 |
| 4.1 抛物线与直角双曲线的直角坐标方程 | 13／19／26／98（主标签只有 5 次） | Determine 13，Show that 10 | 主要作为副标签：与曲线联立求交点（O20 Q7(b)，J21 Q8(a)(c)）、求另一交点、轨迹方程（O21 Q8(d) 2x² + y² = 10x，J25 Q9(b) y² = αx + β） | 精确坐标、成对；轨迹给定形式 | J21 Q8，O21 Q8(d)，J25 Q9(b) |
| 4.2 一般点 (at², 2at)、(ct, c/t) | 10／11／15／64（主标签 2 次） | Show that 9，Determine 4 | 题目给出参数形式的一般点 P；单独考：由一般点求常数 a（J23 Q6(a)）、验证另一点在曲线上（S23 Q8(a)） | 1 分 | J23 Q6(a)，S23 Q8(a) |
| 4.3 抛物线的焦点–准线性质 | 9／9／12／39（缺 J20、J21、S21、J24、J25） | Determine 6，Show that 3，Write down 2 | 写出焦点（1 分）；用“到焦点距离 = 到准线距离”求点或长度（J22 Q3(b)，J23 Q8(a)，S25 Q9）；含焦点、准线交点的三角形面积（S19 Q9(b)，O20 Q7(c)，S22 Q6(c)）；证明弦过焦点（S23 Q8(b)）；线段 QS 长（S24 Q9(c)） | 精确值或最简根式；3–5 分 | O20 Q7(c)，J22 Q3，J23 Q8，S24 Q9(c)，S25 Q9 |
| 4.4 切线与法线 | 14／20／42／164 | Show that 17，Determine 16，Find 7 | **求 P 处切线或法线方程**（16 次，其中 13 次给出答案要 “show that”，多数写明 “use calculus”；3–5 分）；之后：法线与曲线的另一交点（J20、O20、J21、J22、J23、S23、J24、S24）；两切线或两法线的交点（S21 Q4(b)、Q6(c)，S23 Q8(c)）；与坐标轴的交点和三角形面积（O21 Q6，J24 Q3，J25 Q6(b)，S25 Q4）；过已知点的法线（S22 Q6(b)）；直线为切线的条件（O20 Q7(a)，判别式为 0）；轨迹（S21 Q6(d)，O21 Q8(d)，J25 Q9(b)） | 给定方程要有中间步骤；精确坐标、要舍去不合条件的点；4 分最常见（17 次） | O20 Q5，S21 Q6，J23 Q6，S23 Q8，J24 Q7，S24 Q9，J25 Q9，S25 Q4 |
| 5.1、5.2 矩阵加减、数乘 | 各 2／2／2／6 | Determine | 只作为副标签出现在方程里：A + A⁻¹ = I（O21 Q1(b)）、M⁻¹ = 2M + 8I（S25 Q1(b)）、3R 的逆（J22 Q5(d)） | 3 分 | O21 Q1(b)，S25 Q1(b) |
| 5.3 矩阵乘法 | 10／14／18／50（主标签 3 次） | Determine 12，Prove 3 | 主要作为副标签：复合变换、归纳法中的矩阵幂；单独考：A²（S22 Q7(a)）、2×3 乘 3×2（J23 Q1(a)）、整数元素的矩阵四次幂（S24 Q6(b)(i)） | 1–2 分 | S22 Q7(a)，J23 Q1(a)，S24 Q6(b) |
| 5.4 2×2 行列式、奇异与非奇异 | 13／18／20／56（缺 S21） | Determine 14，Find 3 | 求使矩阵奇异的参数（J21、S24；J20 Q1(a) 题面不全）；det 化成最简式（O21、J25）；证明对所有实数 k 非奇异：配方或判别式（J24 Q1(a)，J25 Q1(b)）；det 为正的 x 的范围（J22 Q1）；det(AB) = 0（J23 Q1(b)）；更多作为面积因子的副标签 | 参数值、二次式；证明要写出理由和 “non-singular”；2–3 分 | J22 Q1，J23 Q1(b)，J24 Q1(a)，S24 Q1(i)(a)，J25 Q1 |
| 5.5 2×2 逆矩阵 | 11／12／15／40（缺 O20、S21、J23） | Determine 13 | 含参数的逆矩阵（2 分，11 份卷）；由 A + A⁻¹ = I、M⁻¹ = 2M + 8I 求参数；(MN)⁻¹ = N⁻¹M⁻¹（S22 Q3(b)）；由 BC 求 C，需先求 B⁻¹（S23 Q4(ii)） | (1/det)(…) 形式，最简；2–3 分 | O21 Q1，S22 Q3，S23 Q4(ii)，S25 Q1 |
| 6.1 线性变换与矩阵表示 | 7／7／8／20 | Determine 5 | 求点的像；由像点反求参数（J20 Q6(a)，J21 Q7(b)，J25 Q7(ii)(a)）；证明存在 λ 使 (λ, 1) 映到 (4λ, 4)（J23 Q7(ii)，两个方程都要验证） | 坐标或参数值，舍去多余值；2–5 分 | S21 Q3(a)，J23 Q7(ii)，J25 Q7(ii)(a) |
| 6.2 几何变换的矩阵 | 12／12／26／41（缺 J20、S23） | Write down 10，Describe (fully) 12 | 描述矩阵代表的单一变换：旋转 7 次（90° 顺时针、60°、240°、300° 等），伸缩 2 次，反射 2 次（y = x，y = −x），放大 1 次；写出矩阵：旋转 45°、210°（两次），伸缩，关于 y = −x、x 轴、y 轴的反射，比例因子 −2 的放大；Aⁿ = I 的最小 n（S22 Q7(c)） | 旋转写角度、方向、中心；伸缩写比例因子和方向；矩阵元素用精确值；1–2 分 | J22 Q5(a)，S22 Q7，J23 Q7(i)，J25 Q7(i)，S25 Q2 |
| 6.3 复合变换 | 12／12／16／33（缺 J20、S23） | Determine 11，Find 3 | “A followed by B is represented by C”，求复合矩阵，后做的变换的矩阵写在左边（9 次，如 C = BA、RQ、NM）；反求一个因子：C = B⁻¹A（S19 Q5(c)），C = BA⁻¹（J21 Q7(d)） | 矩阵，乘法顺序正确；2 分为主 | O20 Q6(i)(c)，J22 Q5(c)，J23 Q7(i)(c)，J24 Q4(c)，S24 Q6(b)(ii) |
| 6.4 逆变换；行列式是面积因子 | 12／12／14／39（缺 S21、J23） | Determine 12 | 已知面积求像的面积或原面积（J20、J21、S22、J24、S24、J25）；已知两面积求参数，\|det\| 给出两个值（S19 Q2，O20 Q6(ii)，O21 Q7(ii)(b)，S23 Q4(i)）；逆变换的矩阵（J22 Q5(d)）；由像点求原像（S25 Q2(e)） | 面积数值、参数值（常为两个）；2–5 分 | O20 Q6(ii)，O21 Q7(ii)，S23 Q4(i)，J24 Q4(d)，J25 Q7(ii)(b) |
| 7.1 有限级数求和 | 14／14／28／110 | Show that 17，Determine 5，Find 3 | 用标准公式证明 Σ 等于给定的因式分解形式，或求其中的整数常数（4–6 分）；“hence” 求从 r = n + 1 到 2n 的和（J21、O21、J24）或给定上下限的数值和（J20、O20、S21、S22、J25，含写成展开式的 10×11 + … + 100×101、20×21×25 + …）；关于 n 的方程（J22 Q9(c)，S24 Q7(b)，S25 Q8(c)）；从 r = 0 开始的和（S22 Q8(a)）；上限为 2n（S25 Q8(a)） | 给定形式或整数常数；数值和为整数；n 要舍去非正整数解；4–5 分为主 | O20 Q4，J22 Q9，J24 Q8，S24 Q7，J25 Q5，S25 Q8 |
| 8.1 数学归纳法 | 14／16／23／124 | Prove 23 | 整除 10 次（S19、J20、O20、J21、S21、O21、S22、S23、J24、S24），通项 5 次（一阶 J21、S22；二阶 J20、O21、J25），求和 5 次（O20 分式和、S21 Σr²、J22 Σr³、J23 对数和、S25），矩阵幂 3 次（J24、S24、J25）；S23 从 n = 2 开始 | 基础情形、假设、推到 k + 1、结论四要素齐全；5 分 12 次，6 分 10 次 | O21 Q9，J23 Q9，S23 Q9，J24 Q10，J25 Q8，S25 Q8(b) |

### 8.3 考纲写了、真题还没考过（或极少考）的点

依据：14 份卷的索引检索。每个编号条目至少出现过 2 次，没有完全没考过的条目；下面是条目内的细项。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 r(cos θ + i sin θ) 形式 | 只有 S25 Q5(a) 出现（给出模–辐角式求 r）；从未要求把复数化成模–辐角式 | 一张互化卡即可 |
| 1.2 \|z₁z₂\| = \|z₁\|\|z₂\| | S22 Q1(a)、S25 Q5(a) 两次 | 一张卡；同时提醒 arg(z₁z₂) = arg z₁ + arg z₂ 不要求，S24 Q4(c) 的 MS 写明把 arg 2z 换成 2 arg z 得 M0 |
| 1.3 和、积、商在 Argand 图上的几何表示 | 从未单独考；Argand 题都是描点 | 不必单独做卡，重点练描点规则（对称、相对距离、标注） |
| 1.4 二次方程的复数根 | 单独只考过 S21 Q5 | 并入三次、四次求根卡 |
| 2.3 考纲例子中的 α³, β³；1/α², 1/β² | 原样从未出现；真题的新根都是两种运算的组合（见 8.2） | 练“新根之和、新根之积分别化成 α + β、αβ”的通法 |
| 3.1 二分法 | 14 份卷只有 4 次 | 一张步骤卡（取中点、看符号、写出区间） |
| 4.2 参数求导 | 考纲排除；所有 “use calculus” 都可用 y = 2a^½x^½、y = c²/x 直接求导，MS 也接受参数求导、隐函数求导 | 讲直接求导一种即可 |
| 4.3 直角双曲线的焦点、准线 | 公式册注明 “Not required”，从未出现 | 不做 |
| 5.1、5.2 矩阵加减、数乘 | 只作为方程的一部分出现（O21 Q1(b)，S25 Q1(b)，J22 Q5(d)） | 并入逆矩阵方程卡 |
| 5.3 非方阵相乘 | 只有 J23 Q1(a)（2×3 乘 3×2） | 一张卡 |
| 6.2 关于 y = (tan θ)x（θ 非 45° 的倍数）的反射 | 从未出现；反射只考过坐标轴和 y = ±x | 公式册有矩阵，会查即可 |
| 6.2 平行于 x 轴的伸缩 | S22 Q7(d)、J25 Q7(i)(b) 两次（写矩阵）；描述题只考过平行于 y 轴 | 两个方向各一张 |
| 8.1 不等式归纳 | 考纲不含，从未出现 | 不做 |
| 8.1 二阶递推 | 考纲例子没有，却考了 3 次（J20 Q9(ii)，O21 Q9(i)，J25 Q8(ii)） | 必须做卡：两个基础情形，假设 n = k 与 k + 1，推到 k + 2 |

### 8.4 反复出现的评分惯例与考官提醒

ER 只有 J23、S23、J24 三份；没有标 ER 的条目来自 MS 的评分说明。页码见各条目 `ms`、`er` 字段，以及 `WFM01.coverage.part1.md` “Recurring mark-scheme warnings”、`WFM01.coverage.part2.md` §4。下面的 MS、ER 原文在本次审核中核对过。

1. **变号定根要四样东西**：两个函数值、变号、连续、结论。S25 Q3(ii)(a) MS（“be generous” 但必须有 continuous 的字样）；S23 Q7(a) ER（结论常不充分，常漏 continuous）；J24 Q6(i)(a) ER。只有 O20 Q1(a) 的 MS 写明 “Mention of ‘continuous’ is not required”，所以一律写上最稳。J22 Q8(b) 用 x = 5/3 处不连续排除区间 [1, 2]。
2. **弧度**：J21 Q1(a) MS 列出计算器在角度模式下的错误值；J24 Q6(i)(a) ER（不少人先用了角度模式）；S25 Q3(ii)(a) 要用弧度值。
3. **Newton–Raphson**：答案的 A 分要求导数正确（O21 Q2(b)(ii) “cao following a correct derivative”，J23 Q4(a)(iii) A1cso）；O20 Q1 的 MS 点名常见错误：把 f′(x) 中的 −4x⁻² 写成 +4x⁻²，(c) 得 1.430 而不是 1.442；只写答案不给分，除非精确到 1.379592（S23 Q7(c)(ii)）；f′(x₀) = 0 时不能用这个初值（J23 Q4(a)(ii)，ER：很多人答不出，误以为“上端点不能作初值”）。
4. **线性插值**：比例式的正负号要对，常见错误是正比例等于负比例（J23 Q4(b) ER，S23 Q7(d) ER，J24 Q6(i)(b) ER）；S25 Q3(ii)(b) MS 点名不改 g(5) 符号得 5.265，且用计算器解出的真实根 4.8245… 不算插值；建议画草图（J23 ER，J24 ER）。
5. **二次方程新根**：题目说 “without solving” 时，解出根再算的做法有封顶（S24 Q5 最多 0010 11010，J25 Q3 最多 0000010，S25 Q6(d) 最多 101010）。最后一步要整数系数、写成方程并带 “= 0”：O20 Q2(c)（MS：Not just p = 125, q = 80, r = 38）、J21 Q4(b)、O21 Q3(c)、J23 Q5(c)、J24 Q5(c)、J25 Q3(c)；但 S23 Q5(b) 的 MS 接受只写 p = 40, q = −24, r = 3，S24 Q5(b)、S25 Q6(d) 在写出 ax² + bx + c = 0 时接受只写系数。ER：忘记分母 (αβ)²（J23 Q5(b)），两边乘 αβ 导致错误（J24 Q5(c)），α + β 的符号错（S23 Q5(a)），没有化成整数系数（S23 Q5(b)）。
6. **多项式的复数根**：共轭根在 (a) 写出；实根要在 (b) 写出，在后面才写不给分（J24 Q2(b) ER，z = 1/2）；用比较系数而不是长除法，长除法错误多（J23 Q3(b) ER，J24 Q2(b)(c) ER）；只靠计算器求根再凑因式会被扣分（S23 Q2(b) ER，J23 Q3(b) ER）；“Use algebra” 必须写出代数过程（S23 Q2(b)，S24 Q2(b)）。
7. **Argand 图**：点要标注（字母、坐标或刻度），共轭对关于实轴对称，相对距离正确；没有标注但位置正确得 M1A0（J22 Q2(a) MS）；实根画在正半轴、或共轭对关于虚轴对称都是常见错误（J23 Q3(d) ER）；坐标轴画反 B0（J25 Q4(c) MS）；根组成的三角形面积以实根为顶点，不是原点，写成 “18i” 不给分（J24 Q2(d) ER）。
8. **模与辐角**：\|z₁ + z₂\| 不能写成 \|z₁\| + \|z₂\|（S23 Q6(a) ER）；辐角要弧度、象限正确、按要求的精度（J21 Q6(b)，S23 Q6(d)）；S24 Q4(c) MS：留着 “π − 0.927” 不算出得 A0，arg 2z 换成 2 arg z 得 M0；arg z = π/4 要求实部、虚部都为正，舍去负根，ER 说几乎所有人都丢了这一分（J24 Q9(b)）。
9. **矩阵**：“A followed by B” 是 BA（O20 Q6(i)(c) “BA, not AB”，J22 Q5(c)，S22 Q7(e)，J23 Q7(i)(c) ER，J24 Q4(c) ER，S24 Q6(b)(ii) NM）；S23 Q4(ii) 求 C 时 B⁻¹ 乘的顺序错，即使结果对也是 M0；面积因子是 \|det\|，已知面积求参数要取 det = ± 值，得两个答案（O21 Q7(ii)(b) k = 3, 15；S23 Q4(i) ER：常只令 det = 3）；用面积除以行列式 M0（J21 Q7(a)）；“非奇异”要写理由和这个词，只写 “shown” 不给分（J25 Q1(b) MS，接受 “has inverse”；J24 Q1(a) ER）。
10. **描述变换**：旋转要写类型、角度和方向、中心，不写方向默认逆时针，逆时针旋转写成 “60° clockwise” 算错（J22 Q5(a)，S21 Q3(b)，S22 Q7(b)）；伸缩要用 stretch 这个词，写 “enlargement … y-axis” 得 M1A0（J24 Q4(a) MS），ER 列出 “sketch”“strength”“Enlargement” 等错词，“about O” 对伸缩没有意义（J24 Q4(a) ER）；放大写成 “stretch” 得 M0（S25 Q2(b)）；要求单一变换却写两个变换不给分，y = x 与 y = −x 常混（J23 Q7(i)(a) ER）。
11. **求和**：Σ1 = n（上限 2n 时为 2n），写成 1 丢分（O20 Q4(a)，J21 Q5(a)，S25 Q8(a) B1）；show that 要先提公因式、写出因式分解前的二次式，从四次式直接跳到答案丢分（S22 Q8(a)，J24 Q8(a) ER）；求部分和用 S(上限) − S(下限 − 1)（O20 Q4(b)，S21 Q7(c)，J24 Q8(b) ER，J25 Q5(b)）；题目要求用标准公式时，用归纳法或代两个 n 值都不给分（J24 Q8(a)，S25 Q8(a)）；“hence” 必须用上一问，计算器直接算出 M0A0（S21 Q7(c)）。
12. **归纳法**：基础情形两边都要有代入过程，只写 “both = 1” 得 B0（S25 Q8(b)），只写 “u₁ = 1, u₂ = 4” 最多 01110（J25 Q8(ii)），J23 Q9 的两边是 log 1 = 0 而不是 1（ER）；从题目给的 n 开始，S23 Q9 是 n ≥ 2，评论 f(1) 的整除性扣最后一分；整除题要把 f(k + 1) 写成 f(k) 的倍数加上除数的倍数，每一项都看得出因子（S23 Q9 ER，J24 Q10(ii) ER），f(1) 要显示为除数的倍数（S24 Q8：513 = 9 × 57；出现 114 时要说明 114 是 57 的倍数）；矩阵幂要由乘积推出 k + 1 的矩阵，不能直接写出（J24 Q10(i) ER）；结论要写蕴含关系“若 n = k 成立则 n = k + 1 成立”，写成 “true for n = k and n = k + 1” 不够（J24 Q10 ER），四个要素要在结论里一起出现，不能散在过程中（J22 Q9(a) MS）；二阶递推要假设 n = k 与 n = k + 1，推到 n = k + 2（O21 Q9(i)，J25 Q8(ii)）。
13. **圆锥曲线**：题目写 “use calculus” 时要写出求导并化成 t 的式子，背出来的斜率最多得一分（J24 Q7(a) ER），各卷封顶不同（S24 Q9(a) 从 dy/dx = −1/t² 开始最多 0110、从 m_N = t² 开始最多 0010；J25 Q6(a)、S25 Q4(a) 从 m_N = t² 开始最多 0110）；dy/dx = 1/t 没有过程得 B0（S22 Q6(a)）；法线用垂直斜率（S21 Q6(a)，J22 Q7(a)），用 y = mx + c 时要算出 c（S22 Q6(a)）；给定答案前至少一行中间步骤（S24 Q9(a)，J25 Q6(a)，J23 Q8(a) ER）；用焦点–准线性质 PS = x + a 比用距离公式简单，但很少人想到（J23 Q8(a) ER，S25 Q9）；面积法中焦点横坐标没有加倍得 M0（S22 Q6(c)）；多余的点要舍去（S24 Q9(b)：没有舍去 (6, −6) 得 A0；J25 Q6(b)）；坐标顺序写反、标错（J24 Q3(a)、Q7(b) ER）。
14. **精确值与过程**：根式要化成最简（J22 Q3(b)，J24 Q3(b)）；坐标要精确并正确配对，x = 15 ± 10√2, y = 15 ± 10√2 不配对得 A1A0（J21 Q8(c)）；“without using your calculator” 时精确答案必须出现（J22 Q2(b)）；ER 多次批评过度依赖计算器、不写过程（J24 General，S23 Q6(c)），字迹和版面混乱也会丢分（J23 Overview）。
