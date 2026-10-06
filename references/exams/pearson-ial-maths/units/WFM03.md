# WFM03 · FP3 Further Pure Mathematics 3：考纲摘要

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述。

**来源**
- **SPEC**：Pearson Edexcel IAS/IAL Mathematics, Further Mathematics and Pure Mathematics Specification，**Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。页码为印刷页码。
- 公式中的根号、上下标、不等号都已对照渲染页图核过（`registry/work/fm-spec/pg-47.png`、`pg-48.png`、`pg-49.png`，以及 `fb-14.png` 到 `fb-17.png`）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WFM03/01**。另有区域卷 **WFM03/01A**，考纲里没有这个代码。英国文化协会中国区 2026 年 1 月和 6 月以 WFM03A 报名 | SPEC p.8、p.78；versions.md §1.6 |
| 单元名称 | Unit FP3: Further Pure Mathematics 3。p.67 的表里写作 “FP3: Further Mathematics 3” | SPEC p.40、p.67 |
| AS/A2 定位 | 单元页：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Further Mathematics and Pure Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.40、p.67、p.8 |
| 资格结构 | IAL Further Mathematics 的必考单元是 “FP1 and either FP2 or FP3”。IAL Pure Mathematics 是 P1–P4 加 FP1 必考，再从 FP2、FP3 中选一门 | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.40 |
| 题量（参考） | 2025 年 6 月卷封面：“There are 9 questions”，总分 75。考纲不固定题量 | `registry/src/WFM03/2025-06_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra、symbolic differentiation or integration 功能的计算器，也不得存有可调出的公式 | SPEC p.40；Appendix 6，p.86 |
| 公式册 | 考试提供 FB。FP3 部分在 FB pp.8–11：p.8 向量，p.9 双曲函数与圆锥曲线，p.10 求导与积分，p.11 弧长与旋转曲面面积。考生还可能要用 “Further Pure Mathematics FP1, and Pure Mathematics P1, P2, P3 and P4” 的公式 | SPEC p.40；FB p.8 |
| 开考季 | **January and June**。从 2020 年 6 月起，October 考季不开 FP3 | SPEC p.8、p.70 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**。2021 年 10 月也例外开考。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.40；versions.md §1.4–1.5 |
| 旧考纲同代码 | 2013 版旧考纲也用 WFM03 这个代码，最后一次是 **2019 年 6 月**，不算本考纲真题。p.1 说 Further 各单元内容 “have not changed”，所以旧卷可作兼容练习 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specifications for P1, P2, P3, P4 and FP1, their prerequisites and associated formulae, is assumed and may be tested.”注意 **FP2 不是先修** | SPEC p.40 |
| 评估目标分配（75 分中） | AO1 25–30；AO2 25–30；AO3 0–5；**AO4 7–12**；AO5 5–10 | SPEC p.69 |
| 须背公式清单 | FP3 单元页只有 “3. Notation”，**没有**列出须背公式。须掌握但 FB 不给的内容，见第 3 节 | SPEC p.40 |
| 记号 | 见 Appendix 7。双曲函数及反双曲函数在 p.90：sinh、cosh、tanh、cosech、sech、coth，以及 arsinh、arcosh、artanh 等，用 “ar-” 前缀而不是 “arc-”。矩阵在 p.91：Mᵀ 表示转置，det M 或 \|M\| 表示行列式。向量在 p.91：a×b 表示 vector product | SPEC pp.90–91 |
| 单元概述 | “Hyperbolic functions; further coordinate systems; differentiation; integration; vectors; further matrix algebra.” | SPEC p.40 |

---

## 2. 规格条目逐条（FP3.3 Unit content）

### 主题 1 Hyperbolic functions（p.41）

**1.1 Definition of the six hyperbolic functions in terms of exponentials. Graphs and properties of the hyperbolic functions**（p.41）
- 要求：
  - 用指数函数定义六个双曲函数，例如 cosh x = ½(eˣ + e⁻ˣ)，sech x = 1/cosh x = 2/(eˣ + e⁻ˣ)；
  - 掌握它们的图像与性质；
  - 会推导并使用简单恒等式，例如 **cosh²x − sinh²x ≡ 1**、**cosh²x + sinh²x ≡ cosh 2x**；
  - 会解 **a cosh x + b sinh x = c** 这类方程。
- 公式：FB p.9 给出 cosh²x − sinh²x ≡ 1、sinh 2x ≡ 2 sinh x cosh x、cosh 2x ≡ cosh²x + sinh²x。双曲函数的**指数定义 FB 不给**，须记住。考纲又要求能推导这些恒等式，所以即使 FB 印了，也可能要求证明。

**1.2 Inverse hyperbolic functions, their graphs, properties and logarithmic equivalents**（p.41）
- 要求：反双曲函数的图像、性质及其对数形式（logarithmic equivalents），例如 arsinh x = ln[x + √(1 + x²)]。考纲写明 “Students may be required to **prove** this and similar results”。
- 公式：FB p.9 给出 arcosh x ≡ ln{x + √(x² − 1)}（x ≥ 1）、arsinh x ≡ ln{x + √(x² + 1)}、artanh x ≡ ½ ln((1 + x)/(1 − x))（|x| < 1）。这些结果可能要求证明，不能只抄 FB。

### 主题 2 Further coordinate systems（p.41）

**2.1 Cartesian and parametric equations for the ellipse and hyperbola**（p.41）
- 要求：“Extension of work from FP1.”熟悉以下方程：
  - 椭圆 x²/a² + y²/b² = 1，参数式 x = a cos t, y = b sin t；
  - 双曲线 x²/a² − y²/b² = 1，参数式 x = a sec t, y = b tan t，或 x = a cosh t, y = b sinh t。
- 公式：FB p.9 Conics 表全部给出。FB 中双曲线的双曲参数式写作 (±a cosh θ, b sinh θ)。

**2.2 The focus-directrix properties of the ellipse and hyperbola, including the eccentricity**（p.41）
- 要求：椭圆和双曲线的焦点–准线性质及离心率（eccentricity）。考纲以椭圆为例，学生应知道 **b² = a²(1 − e²)**，焦点为 (ae, 0) 和 (−ae, 0)，准线为 x = a/e 和 x = −a/e。
- 公式：FB p.9 给出四种曲线的离心率、焦点、准线和渐近线：
  - 椭圆：e < 1，b² = a²(1 − e²)，焦点 (±ae, 0)，准线 x = ±a/e；
  - 双曲线：e > 1，b² = a²(e² − 1)，渐近线 x/a = ±y/b；
  - 直角双曲线：e = √2，焦点 (±√2c, ±√2c)，准线 x + y = ±√2c。
  - 考纲说 “should know”，但 FB 也印了这些。

**2.3 Tangents and normals to these curves**（p.41）
- 要求：求椭圆和双曲线的切线与法线。“The condition for **y = mx + c to be a tangent** to these curves is expected to be known.”
- 公式：相切条件 **FB 不给**，须记住。

**2.4 Simple loci problems**（p.41）：简单轨迹问题。指导栏为空。

### 主题 3 Differentiation（p.41）

**3.1 Differentiation of hyperbolic functions and expressions involving them**（p.41）
- 要求：对双曲函数及含双曲函数的表达式求导，例如 tanh 3x、x sinh²x、cosh 2x/√(x + 1)。
- 公式：FB p.10 给出 sinh、cosh、tanh 的导数。sech、cosech、coth 的导数 FB 不给。

**3.2 Differentiation of inverse functions, including trigonometric and hyperbolic functions**（p.41）
- 要求：对反函数求导，包括反三角函数和反双曲函数，例如 arcsin x + x√(1 − x²)、½ artanh x²。
- 公式：FB p.10 给出 arcsin、arccos、arctan、arsinh、arcosh、artanh 的导数。

### 主题 4 Integration（p.42）

**4.1 Integration of hyperbolic functions and expressions involving them**（p.42）
- 要求：对双曲函数及含双曲函数的表达式积分。指导栏为空。
- 公式：FB p.10 给出 ∫sinh x、∫cosh x、∫tanh x = ln cosh x。

**4.2 Integration of inverse trigonometric and hyperbolic functions**（p.42）
- 要求：对反三角函数和反双曲函数积分，例如 ∫arsinh x dx、∫arctan x dx。
- 公式：这类积分 FB 不给结果。分部积分公式在 FB 的 P4 部分（p.5）。

**4.3 Integration using hyperbolic and trigonometric substitutions**（p.42）
- 要求：用双曲代换和三角代换积分。考纲写明 “To include the integrals of”：1/(a² + x²)、1/√(a² − x²)、1/√(a² + x²)、1/√(x² − a²)。
- 公式：这四个积分的结果都在 FB p.10（arctan、arcsin、arsinh、arcosh 形式以及对应的 ln 形式）。另有 1/(a² − x²)、1/(x² − a²) 的 ln/artanh 形式。本条考的是代换方法本身。

**4.4 Use of substitution for integrals involving quadratic surds**（p.42）
- 要求：对含二次根式（quadratic surds）的积分用代换法求解。“In more complicated cases, **substitutions will be given**.”即复杂情形题目会给出代换。

**4.5 The derivation and use of simple reduction formulae**（p.42）
- 要求：推导并使用简单的递推公式（reduction formulae）。考纲举了两例：
  - I_n = ∫₀^{π/2} sinⁿx dx 满足 nI_n = (n − 1)I_{n−2}，n ≥ 2；
  - I_n = ∫ (sin nx / sin x) dx 满足 I_{n+2} = 2 sin(n + 1)x/(n + 1) + I_n，n > 0。
- 公式：FB 不给任何递推公式。

**4.6 The calculation of arc length and the area of a surface of revolution**（p.42）
- 要求：计算弧长和旋转曲面面积。曲线可以以 **cartesian or parametric** 形式给出。
- 排除：“**Equations in polar form will not be set.**”
- 公式：FB p.11 给出弧长公式（直角坐标式和参数式），以及绕 x 轴的旋转曲面面积 S_x = 2π∫y ds（直角坐标式和参数式）。FB 只印了 S_x，**没有**印绕 y 轴的公式。

### 主题 5 Vectors（p.42）

**5.1 The vector product a × b and the triple scalar product a . b × c**（p.42）
- 要求：向量积和三重标量积，并会解释它们的几何意义：|a × b| 是面积，a . b × c 是体积。
- 公式：FB p.8 给出 a × b = |a||b| sin θ n̂ 及其行列式和分量形式；a.(b × c) 的行列式形式，以及 = b.(c × a) = c.(a × b)。

**5.2 Use of vectors in problems involving points, lines and planes. The equation of a line in the form (r − a) × b = 0**（p.42）
- 要求：用向量解点、线、面问题，包括直线的 **(r − a) × b = 0** 形式。可能要求使用等价的直角坐标形式（equivalent cartesian forms）。应用包括：
  - (i) 点到平面的距离（distance from a point to a plane）；
  - (ii) 两平面的交线（line of intersection of two planes）；
  - (iii) 两条异面直线之间的最短距离（shortest distance between two skew lines）。
- 公式：FB p.8 给出直线的直角坐标方程 (x − a₁)/b₁ = (y − a₂)/b₂ = (z − a₃)/b₃，以及点 (α, β, γ) 到平面 n₁x + n₂y + n₃z + d = 0 的距离公式 |n₁α + n₂β + n₃γ + d|/√(n₁² + n₂² + n₃²)。异面直线最短距离的公式 FB 不给。另外，FB 还给出 a 在 b 方向上的分量 a.b/|b|，以及按 λ : μ 分 AB 的点 (μa + λb)/(λ + μ)。

**5.3 The equation of a plane in the forms r.n = p, r = a + sb + tc**（p.42）
- 要求：掌握平面的两种向量方程 **r.n = p** 和 **r = a + sb + tc**，也可能要求使用等价的直角坐标形式。
- 公式：FB p.8 给出 n₁x + n₂y + n₃z + d = 0（d = −a.n）；过三点 A、B、C 的平面 r = a + λ(b − a) + μ(c − a)；过 a 且平行于 b、c 的平面 r = a + sb + tc。

### 主题 6 Further matrix algebra（p.43）

**6.1 Linear transformations of column vectors in two and three dimensions and their matrix representation**（p.43）
- 要求：二维和三维列向量的线性变换及其矩阵表示。“Extension of work from FP1 to 3 dimensions.”

**6.2 Combination of transformations. Products of matrices**（p.43）
- 要求：复合变换和矩阵乘法。AB 表示**先做 B、再做 A**。

**6.3 Transpose of a matrix**（p.43）
- 要求：矩阵转置（transpose），会用 **(AB)ᵀ = BᵀAᵀ**。

**6.4 Evaluation of 3 × 3 determinants**（p.43）
- 要求：计算 3×3 行列式，并理解 singular and non-singular matrices。

**6.5 Inverse of 3 × 3 matrices**（p.43）
- 要求：求 3×3 逆矩阵，会用 **(AB)⁻¹ = B⁻¹A⁻¹**。

**6.6 The inverse (when it exists) of a given transformation or combination of transformations**（p.43）
- 要求：求单一变换或复合变换的逆变换（存在时）。指导栏为空。

**6.7 Eigenvalues and eigenvectors of 2 × 2 and 3 × 3 matrices**（p.43）
- 要求：求 2×2 和 3×3 矩阵的特征值与特征向量（eigenvalues and eigenvectors）。“**Normalised vectors** may be required”，即可能要求单位化的特征向量。

**6.8 Reduction of symmetric matrices to diagonal form**（p.43）
- 要求：把对称矩阵化为对角形，会求 **orthogonal matrix P**，使 **PᵀAP** 为对角矩阵。
- 公式：主题 6 的所有内容，FB 都**不给**公式。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| 双曲恒等式（cosh² − sinh²、sinh 2x、cosh 2x）；arcosh、arsinh、artanh 的对数形式 | FB 给出。但可能要求推导或证明（1.1、1.2） | FB p.9；SPEC p.41 |
| 六个双曲函数的**指数定义** | FB **未给** | SPEC p.41 |
| 椭圆、抛物线、双曲线、直角双曲线的标准式、参数式、离心率、焦点、准线、渐近线 | FB 给出 | FB p.9 |
| y = mx + c 与曲线相切的条件 | FB **未给**，考纲要求 “expected to be known” | SPEC p.41 |
| arcsin、arccos、arctan、sinh、cosh、tanh、arsinh、arcosh、artanh 的导数 | FB 给出 | FB p.10 |
| sech、cosech、coth 的导数与相关积分 | FB **未给** | FB p.10（已核对没有） |
| ∫sinh、∫cosh、∫tanh；四个标准代换积分及 1/(a² ± x²) 型积分 | FB 给出 | FB p.10 |
| 递推公式 | FB **未给**，须推导 | SPEC p.42 |
| 弧长（直角坐标式、参数式）；S_x 旋转曲面面积 | FB 给出（只有绕 x 轴的） | FB p.11 |
| 向量积、三重积、直线和平面方程、点到平面距离、分量投影、定比分点 | FB 给出 | FB p.8 |
| 异面直线最短距离、两平面交线的求法 | FB **未给** | SPEC p.42 |
| 3×3 行列式与逆矩阵、转置、特征值和特征向量、正交对角化 | FB **未给** | SPEC p.43 |
| FP1、P1–P4 的公式（例如 P3 的三角恒等式和求导表、P4 的分部积分公式） | FB 给出，FP3 可能用到 | FB pp.3–6 |

---

## 4. 与相邻单元的界线

- **P3（先修）**：反三角函数 arcsin、arccos、arctan 的定义、图像和定义域限制在 P3 2.1（p.23）。链式、积、商法则在 P3 4.2，dy/dx = 1/(dx/dy) 在 P3 4.3（均在 p.24）。eˣ 和 ln x 在 P3 主题 3（p.24）。FP3 在此基础上加入反函数求导（3.2）和双曲函数。P3 的 a cos θ + b sin θ = c 对应 FP3 1.1 的 a cosh x + b sinh x = c。
- **P4（先修）**：
  - 简单的换元积分和分部积分在 P4 6.2，用部分分式积分在 P4 6.3（p.28）；FP3 4.3–4.5 在此之上增加双曲/三角代换、二次根式代换和递推公式；
  - 旋转**体积**在 P4 6.1（p.28），FP3 4.6 考的是旋转**曲面面积**和弧长；
  - 参数求导在 P4 5.1（p.27）；
  - 三维向量的基础在 P4 主题 7（pp.28–29）：模、位置向量、两点距离、直线 r = a + tb、平行/相交/异面的判定（7.6）、数量积与夹角（7.7）。FP3 主题 5 新增向量积、三重积、直线的 (r − a) × b = 0 形式、平面方程、点到平面距离、两平面交线、异面直线最短距离。
- **FP1（先修）**：
  - 抛物线和直角双曲线（标准式、参数式、抛物线的焦点–准线、切线法线）在 FP1 主题 4。FP3 2.1 写明 “Extension of work from FP1”，加入椭圆、双曲线、离心率，以及 y = mx + c 的相切条件；
  - 2×2 矩阵、行列式、逆矩阵、二维变换（含 AB = 先 B 后 A）在 FP1 主题 5–6。FP3 6.1 写明 “Extension of work from FP1 to 3 dimensions”，新增转置、3×3 行列式与逆矩阵、特征值和特征向量、对称矩阵的正交对角化。
- **FP2（不是 FP3 的先修，两者平行）**：FP3 不能默认学生会 FP2 的内容，包括 De Moivre 和复指数、Maclaurin/Taylor 级数、极坐标、微分方程。FP2 也不默认学生会双曲函数。极坐标曲线的面积在 FP2 主题 7；FP3 4.6 写明极坐标形式的弧长和曲面面积 “will not be set”。

---

## 5. 印刷问题与缺口
- 1.2 的例子在考纲中印作 ln[x + √(1 + x²)]，FB 印作 ln{x + √(x² + 1)}，两者等价。
- 2.2 的指导栏把准线写成 “x = +a/e and x = −a/e”，FB 写成 x = ±a/e，两者一致。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误。

---

## 6. 逐题索引与审核（2026-10-06）

**索引文件**：同目录 `WFM03.questions.json`。它由 `WFM03.questions.part1.json`（2020-10 至 2022-06）和 `WFM03.questions.part2.json`（2023-01 至 2025-06）合并而成，按 id 去重（没有重复）并按考季、题号排序。构建记录见 `WFM03.coverage.part1.md`、`WFM03.coverage.part2.md`。审核脚本和输出在 `registry/work/wfm03audit/`：
- 脚本：`scripts/merge_validate.py`、`qpblocks.py`、`checks.py`、`pagerange.py`、`quotecheck.py`、`codesum.py`、`numcheck.py`、`matcheck.py`、`stats.py`、`stats2.py`；
- 改动清单：`fixes.json`；改动前的备份：`backup/`。

**收录范围**：12 份卷，101 题，249 个小问，900 分，全部是 /01 卷。

| 考季 | 题数 | QP、MS 来源 | ER |
|---|---|---|---|
| 2020-10（封面日期 8 June 2020，10 月实考） | 8 | GitHub papernexus（PMT 戳记的 Pearson PDF），本地副本 `src/WFM03/` | 缺 |
| 2021-01 | 9 | 同上 | 缺 |
| 2021-06（考试取消，只发布了试卷和最终版 MS） | 8 | 同上 | 本季没有 ER |
| 2021-10 | 8 | 同上 | 缺 |
| 2022-01 | 8 | 同上 | 缺 |
| 2022-06 | 9 | 同上 | 缺 |
| 2023-01（索引用重发版，实考版的 Q5 不同） | 9 | examsolutions S3 镜像；实考版在 `src/WFM03/alt/` | 有 |
| 2023-06 | 8 | S3 镜像，Drive 上有同一文件 | 有 |
| 2024-01 | 8 | S3 镜像，Drive 上有同一文件 | 有 |
| 2024-06 | 9 | Drive | 缺 |
| 2025-01 | 8 | Drive | 缺 |
| 2025-06 | 9 | Drive | 缺 |

**格式校验**（`merge_validate.py`，结果 0 个问题）
- 每条记录字段齐全；各小问分值之和等于题目总分；每卷 75 分，题号连续。
- 所有 spec id 都在 `spec-items.fm.json` → `WFM03` 中；series 都是 YYYY-MM 格式；id 与考季、卷号一致；引号内的文字都不超过 25 词。
- `qpblocks.py` 把每题总分与 QP 文本印的 "Total" 逐题核对，全部一致。
- 小问分值与 QP 印的 (n) 不一致的只有 4 题：J23 Q2(b)、J23 Q5(b)、J23 Q9(a)、J24 Q3(a)(b)。原因都是 QP 把几个小问合印一个分值，而索引按 MS 拆开，coverage part 2 §1 已说明。

**自动比对**
- **命令词**：249 个小问的命令词，逐词都能在该题 QP 文本中找到。整句比对时有 5 处是缩写，例如 J22 Q8(b) 原文 "Hence, for this ellipse, determine" 记作 "Hence determine"。这不算错。
- **引文**：`ms`、`er` 中共有 33 处加引号的短语，逐条在 MS、ER 文本中找到。其中 2 处（J23 Q8(c)、J23 Q9(a)(ii)）因分式排版，脚本匹配不上，人工核对后确认是原文。
- **页码**：所有 "(MS p.n)"、"(ER p.n)" 指向的页面都存在。脚本按题号定出每题在 MS、ER 中的页码范围，超出范围的 9 处逐页看过，都没问题。它们是：同一题的续页；2021-06 MS p.7 的 "Summary of changes" 页；ER 总述页（J24 ER p.3 谈到了 Q7）。
- **评分代码**：把 `ms` 中列出的 B1、M1、A1 等代码按小问求和，与小问分值一致。脚本报了 14 处差异，人工逐条看过，都是把 "A1A0" 一类特例说明也算进去了，不是错误。
- **答案重算**：不看 MS，独立重算了 54 个终点值，结果与 `final_form` 全部一致。方法如下：
  - 积分用 Simpson 法数值计算；
  - 矩阵用分数做精确计算：逆矩阵取 2–3 个参数值检验 A·A⁻¹ = I，特征向量检验 Mv = λv；
  - 向量的距离、角度、体积直接计算。

**完整性**
- **预期考季**：据 `versions.json` 和 `src/expected_series.json`，2018 考纲下 WFM03 共有 14 个预期考季。从 2020-10 起，每年 1 月、6 月各一季，另加 2020-10、2021-10 两个疫情期间的秋季考季。2020-06 整季取消，没有试卷。
- **收录情况**：有 QP 文本的 12 季全部收录，没有漏卷。
- **比对过的来源**：
  - `inventory/fm-mech.json` 和 `fm-mech-gaps.md`。这两个文件仍把 2020-10 至 2022-06 的 QP 记为"只有 Finder 文本"、MS 记为缺失；part 1 已从 GitHub papernexus 补齐 PDF。
  - `finder/finder-inventory.tsv`。其中 2018 考纲的 WFM03 共 11 季加 SAM，全部在索引内。2014-06 至 2019-06 的 5 份属于 2013 考纲，不收。
- **所有来源都拿不到的卷**：2026-01 WFM03/01 与 /01A、2026-06 WFM03/01 与 /01A，QP、MS、ER 全缺。它们的文件名只出现在 grademax 清单中（见 coverage part 2 §3）。2026-10-06 再次检索 Drive，只找到已收录的 2023–2025 文件。检索条件为：标题含 WFM03、FP3 或 F3A 且 2025-09 以后修改；fullText 含 WFM03 且 2025-07 以后创建。
- **缺 ER**：2020-10、2021-01、2021-10、2022-01、2022-06、2024-06、2025-01、2025-06。2021-06 本来就没有 ER。有 ER 的只有 J23、S23、J24 三季。
- **/01A**：已知的 FP3 卷中没有 2026 年以前的 /01A 卷。

**准确性抽查**
- **抽查范围**：对照 QP、MS 和 ER 原文，逐条复核了 27 题，覆盖全部 12 份卷和全部 6 个主题：
  - 2020–2021：O20 Q4、O20 Q6、J21 Q5、J21 Q9、S21 Q2、S21 Q6、O21 Q7；
  - 2022：J22 Q2、J22 Q5、S22 Q4、S22 Q7、S22 Q9；
  - 2023：J23 Q2、J23 Q5、J23 Q6、J23 Q8、J23 Q9、S23 Q5；
  - 2024：J24 Q3、J24 Q5、S24 Q6、S24 Q8；
  - 2025：J25 Q4、J25 Q7、J25 Q8、S25 Q3、S25 Q9。
  - 另外，S23 全卷的 `er` 字段逐条与 ER 原文对照过。
- **核对内容**：分值、spec 映射、命令词、终点形式（并重算答案）、MS 要点、ER 要点。
- **结果**：分值、终点、MS 页码都没有发现错误，错误全部在 spec 映射。随后对全部 249 个小问的 spec 标签按条目检查了一遍，即列出每个条目下所有小问的题面逐一判断，重点查 3.1、4.1、4.3、4.4、1.2 的副标签。

**改正**（合并文件和两个 part 文件同步修改，清单见 `work/wfm03audit/fixes.json`）
1. **F01 J22 Q2**：spec 由 [4.6, 3.1] 改为 [4.6]。本题 dx/dθ 是 ln(sec θ + tan θ) − sin θ 的导数，不涉及双曲函数，3.1 不适用。
2. **F02 J25 Q3(i)**：spec 由 [4.3, 4.4] 改为 [4.3]。∫1/(4x² + 12x + 25) dx 不含二次根式，同类积分（O20 Q2(i)、S21 Q7(i)）也只标 4.3。
3. **F03–F05 O20 Q2(ii)、J22 Q5(i)、J22 Q5(ii)**：spec 由 [4.3, 4.4] 改为 [4.4, 4.3]。
   - 这三题都要先在根号下配方。part 2 和 S22 Q2(i) 对这类积分都以 4.4 为主标签，part 1 这三处顺序相反。统一后，4.4 的主标签计数才能跨卷比较。
   - 题目已给定双曲或三角代换的（J21 Q4、O21 Q8(c)、S22 Q2(ii)），仍以 4.3 为主标签。
4. **补充**（不算错误，是把漏掉的 MS 要点补上）：
   - E01 J23 Q8(c)：补上 MS 的另一半规定。只写 "I₆ − I₈ = 5π/256" 得 3/3；在 (c) 中做的工作不给 (b) 记分。
   - E02 S25 Q9(a)：补上 "不接受 e = ±√113/8"。
   - E03 J21 Q5(a)：补上 "(a)、(b) 一起评分，但只出现在 (c) 中的 (a) 工作不给分"。
   - E04 O21 Q7(d)：补上 "用判别式时要代入数值，只写 b² − 4ac < 0 不够"。
5. **错误分布**：错误分散在两个 part，J22、J25 各一处，另有 part 1 的标签顺序约定，没有集中在某一卷。顺序问题已对 part 1 全部 4.3、4.4 标签复查过。

**保留未改的差异**（coverage 文件是构建记录，没有改动，以本节和索引为准）
- `WFM03.coverage.part2.md` §2 说每卷都有递推公式题（"Every paper has"），实际 J25 没有，4.5 只出现在 11/12 份卷。
- 同一处又说每卷都有 "a 3×3 determinant/inverse or a transformation question"，这也不对：
  - J25 只有特征值题，行列式只出现在特征方程里；
  - J23 Q5(a)（求使矩阵奇异的值）是重发版才加的，实考卷没有这一问。
- `WFM03.coverage.part1.md` 的 "Mapping notes" 中，4.3、4.4 的主标签计数是改正前的数字。
- `inventory/fm-mech.json` 和 `fm-mech-gaps.md` 仍把 2020-10 至 2022-06 的 PDF 记为缺失。

## 7. 真题需求概览

**数据范围**
- 本节统计 2018 考纲下能拿到题面的全部 12 份卷：O20、J21、S21、O21、J22、S22、J23、S23、J24、S24、J25、S25，全部是 /01 卷，共 101 题、249 个小问、900 分。
- 12 份卷都有 MS；有 ER 的只有 J23、S23、J24 三份。
- 拿不到的卷见第 6 节。

**统计方法**
- 数字由 `work/wfm03audit/scripts/stats.py`、`stats2.py` 从索引算出，结果存于 `work/wfm03audit/stats.txt`、`stats2.txt`。
- "问法、终点、评分"取自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节抽查过。

**引用写法**
- J = January，S = June，O = October，后接两位年份。
- S21 的考试取消了，但试卷和 MS 已发布。
- J23 用的是重发版。
- 题号和小问按试卷印刷。MS、ER 的页码见索引条目 `ms`、`er` 字段末尾的 "(MS p.n)"、"(ER p.n)"。

### 7.1 卷面结构

**题量与分值**
- 每卷 75 分。
- 题数：8 题的有 7 份（O20、S21、O21、J22、S23、J24、J25），9 题的有 5 份（J21、S22、J23、S24、S25）。
- 单题 3–14 分，最常见的是 9 分（20 题），其次是 6 分和 10 分（各 14 题）、8 分（13 题）。

**命令词**（249 个小问）

| 命令词 | 次数 |
|---|---|
| Determine | 98 |
| Show that | 56 |
| Hence determine | 17（另有 "Hence, determine" 2 次） |
| Find | 16 |
| Hence find | 8 |
| Hence show that | 8 |
| Write down | 8 |
| Prove | 7（另有 Prove by induction 1 次） |
| Using calculus, show that | 5 |
| Solve | 4 |
| Use | 3 |

- "Find" 只出现在 2020–2022 年，从 J23 起全部改用 "Determine"。
- 要求证明或得出给定结果的小问（Show that、Prove 等）共 83 个，约占三分之一。
- 以 "Hence" 开头的小问共 43 个。

**各主题分值**（按每个小问的第一个 spec 计）

| 主题 | 分值 | 占比 | 每卷分值范围 |
|---|---|---|---|
| 主题 4 积分 | 303 | 34% | 21–29（约占三分之一卷面） |
| 主题 2 圆锥曲线 | 169 | 19% | 10–20 |
| 主题 6 矩阵 | 160 | 18% | — |
| 主题 5 向量 | 137 | 15% | — |
| 主题 1 双曲函数 | 74 | 8% | — |
| 主题 3 求导 | 57 | 6% | — |

**每卷固定出现的题型**
- **12/12 份卷都有**：
  - 双曲函数题。除 O21 外，11 份卷都有要求用精确对数作答的双曲方程（J21 Q2(b)、J24 Q7(b) 是由导数条件得出的方程）；O21 Q2 改为证明 arcosh 的对数形式。8 份卷要求用指数定义作证明：7 次证恒等式，加上 O21 Q2。
  - 圆锥曲线题。椭圆出现在 9 份卷，双曲线出现在 7 份卷。
  - 弧长或旋转曲面面积题（4.6）。弧长 7 份，曲面面积 7 份，S21、J25 两样都考。
  - 向量题。每卷都有平面或直线的综合题。
  - 3×3 矩阵题。
- **11/12 份卷有**：
  - 递推公式题（4.5），只有 J25 没有。
  - 标准积分或配方积分（4.3/4.4），只有 S23 没有，那一卷改考 ∫arcosh 5x dx。
- **10/12 份卷有**：3×3 特征值、特征向量题（6.7），缺 S21、O21。
- **8/12 份卷有**：3×3 逆矩阵（6.5），缺 J22、J23、S24、J25。

**题面限制语**
- "Solutions relying (entirely) on calculator technology are not acceptable"、"show all stages of your working"、"all working must be shown" 一类的话：
  - 2020–2021 年没有出现；
  - 之后出现在 J22 Q3、S22 Q2、J23 Q6、S23 Q1–Q2、J24 Q1 与 Q8、S24 Q2 与 Q7、J25 Q1 与 Q3–Q5、S25 Q7。
- "Using calculus / Use calculus" 出现在 S21 Q2、Q7、Q8，O21 Q1、Q3，J22 Q2、Q8，S23 Q6，S24 Q6，J25 Q7，S25 Q9。

### 7.2 每个考纲条目怎么考

- "卷数／题数／小问／涉及分值"按标签出现的任何位置统计。一个小问可以带几个标签，所以各行相加会超过 101 题、900 分。
- 括号内的"主"表示该条目作为第一个标签时的小问数和分值。

| 条目 | 卷数／题数／小问／涉及分值 | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 双曲函数的指数定义、图像、性质；a cosh x + b sinh x = c | 12／16／24／96（主 16／61） | Show that 5，Solve 4，Prove 2，Hence determine 2 | **用指数定义证恒等式**，共 7 次，2–3 分：sinh 3x（O20）、1 − tanh²x ≡ sech²x（S21）、8cosh⁴x（J22）、cosh(A + B)（S22）、1 − sech²x ≡ tanh²x（J24）、sinh(A + B)（S24）、2cosh 5x cosh x（S25）。**解双曲方程**：先用 (a) 的恒等式或 cosh² − sinh² = 1 化成二次式，例如 cosh 4x − 17cosh 2x + 9 = 0（J22）、4tanh x − sech x = 1（J23）、7cosh x + 3sinh x = 2eˣ + 7（S23）、2sinh²x + 3cosh x = 7（J25）；或者化成 R sinh(x + α) 再解（S24 Q4） | 精确的自然对数，所有根都要写出、不能有多余的根；4–6 分 | J22 Q1，S22 Q1，J23 Q3，S23 Q1，S24 Q4，J25 Q1，S25 Q1 |
| 1.2 反双曲函数及其对数形式 | 12／17／18／83（主 4／13） | Prove，Hence solve，Hence determine | 主要作为收尾工具：方程、定积分、驻点的答案都要通过 arsinh、arcosh、artanh 的对数形式化成 ln。单独考证明只有 1 次：O21 Q2，用指数定义证明 y < 0 时 y = ln(x − √(x² − 1))，6 分 | ln(a + √b) 化简；要选对分支和符号 | O21 Q2，J23 Q4(b)，S24 Q4(c)，J25 Q3(ii)，S25 Q4(b) |
| 2.1 椭圆、双曲线的直角坐标方程和参数式 | 8／10／15／58（主 5／12） | Determine 3 | 多作为副标签，用于参数点 (a cos θ, b sin θ)、(a sec θ, b tan θ)。单独考的有：写渐近线（S21 Q8(a)）；直线代入椭圆得二次方程（S22 Q9(a)）；由焦点、准线写出双曲线方程 px² − qy² = r（S24 Q1(b)）；求点的坐标（J24 Q3(e)，J25 Q7(c)） | 整数系数方程或精确坐标；1–3 分 | S22 Q9(a)，S24 Q1(b)，J25 Q7(c) |
| 2.2 焦点–准线性质与离心率 | 9／10／28／67（主 26／59） | Determine 13，Show that 4，Write down 4 | 由 a、b 求 e（J22 Q8(a)；S25 Q9(a) 要 show e = √113/8）；用 e 表示焦点和准线（J24 Q3(a)）；由准线反求 a（J23 Q2(b)）、由焦点求 k（J25 Q2）、由焦点和准线求 e（S24 Q1(a)）；证明 PF₁ + PF₂ = 6（J23 Q9(b)）；证明 QF/PF = e（J21 Q9(c)）；由 PS² = e²PM² 推出 b² = 49(1 − e²)（J24 Q3(c)）；准线、渐近线、焦点构成的三角形面积（O21 Q7） | 焦点写成坐标 (±ae, 0)，准线写成方程 x = ±a/e，e 只取正值；每个小问 1–3 分 | O21 Q7，J22 Q8，J23 Q2，J23 Q9，J24 Q3，S24 Q1 |
| 2.3 切线与法线（含 y = mx + c 的相切条件） | 9／9／18／67（主 16／56） | Show that 7，Using calculus, show that 3，Write down 2 | **在参数点处求切线或法线**，答案印在题中，几乎都写明 "use calculus"。考法线 5 次（J21 Q9(a)，O21 Q3(a)，S23 Q6(b)，S24 Q6(a)，J25 Q7(a)），考切线 4 次（S21 Q8(c)，J22 Q8(c)，S23 Q6(a)，S25 Q9(b)）。相切条件只考过 1 次：O20 Q5 先证 25m² = 4 + c²，再求过点 (1, 2) 的切线和切点。与坐标轴的交点各 1 分（S25 Q9(c)(d)） | 给定方程，要写出中间步骤；3–5 分 | O20 Q5，J21 Q9(a)，S23 Q6，J25 Q7(a)，S25 Q9(b) |
| 2.4 简单轨迹 | 9／9／11／50（主 8／42） | Show that 4，Hence show that 2，Determine 2 | **中点轨迹**：O21 Q3(b) 得 16x² + 9y² = 49；S22 Q9(c) 是弦 y = kx − 3 的中点；J23 Q9(c) 中点轨迹是过原点的直线；S23 Q6(c) 得 x²(49 − 36y²) = 196。**交点轨迹**：S21 Q8(d) 的 S 在椭圆上；J22 Q8(e) 垂足满足 (x² + y²)² = 9x² + 4y²。**其他**：θ 变化时三角形面积的最大值（S24 Q6(b)，10/3）；以 QR 为直径的圆过两焦点（S25 Q9(e)） | 规定形式的整数系数方程，并写出结论（如"过原点""过焦点"）；5–7 分 | O21 Q3(b)，S22 Q9，J23 Q9(c)，S23 Q6(c)，S25 Q9(e) |
| 3.1 双曲函数及含双曲函数表达式的求导 | 7／7／8／37（主 3／16） | Show that，Prove by induction | 求 ln(tanh 2x) 的导数，化成 p cosech 4x（J21 Q2(a)）；求 arccos(sech x) + coth x 的驻点，要用 coth 的导数 −cosech²x，公式册不给（J24 Q7(b)）；用归纳法证明 e^(3x)cosh 2x 的 n 阶导数（J25 Q8，归纳法属 FP1）。此外作为递推公式证明（S23 Q7(a)）、弧长（S24 Q7(a)）中的步骤 | 给定形式或精确值；4–6 分 | J21 Q2，J24 Q7(b)，J25 Q8 |
| 3.2 反函数求导（反三角、反双曲） | 9／10／15／50（主 13／41） | Show that 5，Determine 4 | **乘积**：x arccos x（S21 Q4(i)），3x arcsin 2x（J23 Q1），x arcosh 5x（S23 Q8(a)）。**复合**：arccos(2√x)（O21 Q8(a)），arsech(x/2)（J22 Q3(a)），artanh((cos x + a)/(cos x − a))（S22 Q4），arccos(sech x)（J24 Q7(a)），arsinh√(x² − 1)（S24 Q3(a)），arsinh x + arsinh(1/x)（S25 Q4(a)）。**令 f′(x) = 0 解 x**：J22 Q3(b)，S24 Q3(b)，S25 Q4(b) | 给定形式，或求出 p、q、k；精确的 x 值，要舍去负值；2–5 分 | J22 Q3，J23 Q1，S24 Q3，S25 Q4 |
| 4.1 双曲函数的积分 | 5／6／8／41（主 1／4） | Hence show that | 几乎都只是中间步骤：∫cosh²（O20 Q7(c)，J24 Q8(b)，S25 Q7(b)）；∫tanh 3x = (1/3)ln cosh 3x（J24 Q5(c)）；coshⁿ2x 的递推（S23 Q7）。作为主标签只有 1 次：∫coth x = ln sinh x（S24 Q7(b)） | 精确的 ln 或指数式 | S24 Q7(b)，J24 Q5(c) |
| 4.2 反三角、反双曲函数的积分 | 4／4／5／23（主 4／18） | Determine，Show that，Hence, or otherwise, show that | 都用 1 × 反函数做分部积分：∫arccos(2√x) dx（O21 Q8(b)(d)），∫ from 1/4 to 3/5 of arcosh 5x dx（S23 Q8(b)，8 分），∫arcosh 3x dx（S25 Q2(ii)） | 带 ln 的精确值，或不定积分 + c | O21 Q8，S23 Q8(b)，S25 Q2(ii) |
| 4.3 双曲、三角代换积分（含四个标准积分） | 11／13／21／89（主 12／52） | Determine 5，"Use the substitution … to show that" 等 | **公式册标准式**：arctan 型（O20 Q2(i)，S21 Q7(i)，J24 Q1(i)，J25 Q3(i)），arcsin 型（J24 Q1(ii)），arsinh 型（J23 Q4）。**题目给定代换**：x = 4cosh θ（J21 Q4），√x = ½cos θ（O21 Q8(c)），x = 3sec θ（S22 Q2(ii)），y = 4sinh u（J24 Q8(b)），2sin 2x = sinh θ（S25 Q7(b)） | π 的倍数、ln 形式、A + B√3 等精确值；3–7 分 | J21 Q4，S22 Q2(ii)，J24 Q1，S25 Q7(b) |
| 4.4 含二次根式的积分（先配方） | 9／9／13／52（主 10／36） | Determine 6 | **根号内先配方，再化成 arcsin、arsinh 或 arcosh**：O20 Q2(ii)，J22 Q5(i)(ii)，S22 Q2(i)，J25 Q3(ii)，S25 Q2(i)。**拆成两个积分**：(8x + 5)/√(4x² + 4x + 17) 拆开后分别积分（S24 Q5）。**其他**：∫√(x² − 3)/x² dx（S21 Q7(ii)） | 写对反函数并加 + c；定积分化成 ln a；3–6 分 | J22 Q5，S22 Q2(i)，S24 Q5，J25 Q3(ii) |
| 4.5 递推公式 | 11／11／23／104（全为主标签） | Show that 9，Prove 3，Hence find 3，Hence determine 3，Use 2 | **固定两问**：(a) 用分部积分证明递推公式，4–6 分；(b) 用公式求具体值，3–5 分。**被积函数**：xⁿcos x（O20），xⁿ/√(x² + 3)（J21），secⁿx（S21），xⁿcos(x²)（O21，步长 4），eˣsinⁿx（J22），xⁿ/√(10 − x²)（S22），cosⁿx 并推出偶数 n 的乘积式（J23），coshⁿ2x（S23），tanhⁿ3x（J24，要用 1 − sech²），xⁿ(k − x)^½（S24，反求 k），xⁿ(3x − 2)^(−½)（S25） | (a) 是给定公式；(b) 是精确值，或 f(x)、g(x) 的系数；4 分的小问最常见（12 次） | J21 Q6，S21 Q5，J23 Q8，J24 Q5，S24 Q8，S25 Q5 |
| 4.6 弧长与旋转曲面面积 | 12／12／22／102（主 20／89） | Show that 10，Hence determine 3，Using calculus 4 | **固定两步**：先证被积式化简成给定形式，2–6 分；再求精确值，3–7 分。**弧长**：直角坐标 6 次（J21 y = 2 + ln(1 − x²)，S21 半圆，O21 y = ½arcosh 2x，S23 y = ½(tan x + cot x)，J24 抛物线、对 y 积分，S24 y = ln tanh(x/2)），参数式 1 次（J25）。**曲面面积**：直角坐标 2 次（S21，S25），参数式 5 次（O20，J22 含两端圆面的全表面积，S22，J23 摆线，J25） | 按题目给定形式写精确值，如 p√q、p + ln q、(π/2)(p + q√2)、kπ；4 分最常见 | O20 Q7，J22 Q2，J23 Q6，S23 Q3，J24 Q8，J25 Q5，S25 Q7 |
| 5.1 向量积与三重标量积 | 12／14／18／63（主 8／21） | Determine 8 | 求平面的法向量，或同时垂直于两直线的向量（O21 Q5(a)，J23 Q7(a)，J25 Q6(a)，S25 Q8(a)）；三角形面积（J21 Q1(a)）；四面体体积（J21 Q1(b)，S23 Q4(b)，J24 Q6(c)，O21 Q4(c) 结合行列式） | 向量或其倍数；体积 = (1/6)\|三重积\|，含参数时取 ±V，得两个解；1–5 分 | J21 Q1，S23 Q4(b)，J24 Q6(c) |
| 5.2 点、线、面问题；(r − a) × b = 0 | 12／15／26／106（主 22／90） | Determine 15，Find 4，Show that 2 | **两平面交线**：O20 Q8(a)，S21 Q6(c)，S23 Q4(a)（7 分），S24 Q9(b)，S25 Q8(c)（要求写成 (r − a) × b = 0）。**两直线最短距离**：O20 Q8(b) 平行线，O21 Q5(c)、S25 Q8(d) 异面直线。**点到平面距离**：J21 Q7(b)(c)，J23 Q7(c)，J24 Q6(b)，J25 Q6(c)。**夹角**：线面角（J22 Q7(b) 保留 1 位小数，J23 Q7(b) 精确到度，J25 Q6(b) 精确到度）、面面角（S21 Q6(d) 3 s.f.）。**其他**：直线与平面的交点（J22 Q7(a)，S22 Q8(a)），直线关于平面的反射（S22 Q8(c)），三平面的公共点（S24 Q9(c)） | 直线写成 "r = a + λb"；也可用直角坐标形式；距离写成精确根式且为正；角度按指定精度；3–5 分 | O20 Q8，O21 Q5，J22 Q7，S23 Q4(a)，S25 Q8 |
| 5.3 平面方程 r.n = p、r = a + sb + tc | 10／11／17／55（主 9／26） | Determine 5，Show that 2 | 过三点、或含两条直线、或含一点一线的平面，写成直角坐标式（J21 Q7(a)，S21 Q6(a)，S22 Q8(b)，J24 Q6(a)）；参数式化成直角坐标式（S24 Q9(a)）；两种向量形式互写（O21 Q5(b)，S25 Q8(b)） | 整数系数方程，常数项要由已知点算出；1–5 分 | J21 Q7(a)，O21 Q5(b)，S22 Q8(b)，S25 Q8(b) |
| 6.1 三维线性变换的矩阵表示 | 5／5／5／19（主 1／3） | Determine | 求直线在 M 下的像，写成 r × b = c（S24 Q2(b)）；其余都是副标签：变换后的体积（O21 Q4(c)），原像（O20 Q6(b)，J24 Q2(b)，S23 Q2(b)） | 直线方程 | S24 Q2(b) |
| 6.2 复合变换、矩阵乘积 | 1／1／1／4（主 0） | Determine | 只考过 1 次：由 TU = I 求三个未知元素（J24 Q2(a)） | 数值 | J24 Q2(a) |
| 6.3 转置，(AB)ᵀ = BᵀAᵀ | 0 | — | 从未作为考点，只在 PᵀMP = D 中隐含出现 | — | — |
| 6.4 3×3 行列式，奇异与非奇异 | 11／13／15／53（主 7／22） | Determine 4，Show that 2 | 求使矩阵奇异的参数（J21 Q3(a)，S21 Q3(a) 答案是根式，J23 Q5(a)，S25 Q6(a)）；证 det M = 5k − 10（O21 Q4(a)）；证对所有实数 x 都非奇异，要配方（S22 Q6(a)）；行列式作为体积比例因子（O21 Q4(c)）；其余是特征方程中的副标签 | 参数值；证明要写出理由和结论；2–4 分 | S21 Q3(a)，O21 Q4，S22 Q6(a)，S25 Q6(a) |
| 6.5 3×3 逆矩阵 | 8／8／9／36（主 8／32） | Find 4，Determine 4 | 含参数的逆矩阵（O20 Q6(a)，J21 Q3(b)，S21 Q3(b)，O21 Q4(b)，S22 Q6(b)，S25 Q6(b)）；数值矩阵要写出全部步骤（S23 Q2(a)）；由 TU = I 求未知元素（J24 Q2(a)） | (1/det) × 伴随矩阵，化简；4 分为主 | O20 Q6(a)，S22 Q6(b)，S23 Q2(a)，S25 Q6(b) |
| 6.6 逆变换 | 3／3／4／13（主 4／13） | Determine 3 | 由像直线求原直线（O20 Q6(b)；J24 Q2(b) 利用 U = T⁻¹，答案写成直角坐标式）；求平面在 M 下的像（S23 Q2(b)(c)，用 M⁻¹ 把 x、y、z 写成 u、v、w 的式子） | 直线或平面方程；2–4 分 | O20 Q6(b)，S23 Q2，J24 Q2(b) |
| 6.7 特征值与特征向量 | 10／10／28／88（主 25／75） | Determine 20，Find 2 | 全部是 3×3 矩阵，2×2 从未考过。**常见流程**：由给定的特征值或特征向量求出未知元素（O20 Q3(a)，J22 Q4(a)，J23 Q5(b)(i)，J25 Q4(a)(b)，S25 Q3(a)(b)）→ 由特征方程求其余特征值 → 求特征向量，并常要单位化（O20 Q3(c)，J22 Q4(c)，J23 Q5(c)，S24 Q2(a)，J25 Q4(d)）。**变体**：有重特征值时求 k，两种情形都要考虑（S23 Q5） | 特征值；特征向量可取任意倍数，单位化时写成 (1/√n)(…)；每小问 2–3 分，整题 7–14 分 | O20 Q3，J23 Q5，S23 Q5，J25 Q4，S25 Q3 |
| 6.8 对称矩阵对角化 | 4／4／4／15（主 4／15） | Hence determine 2 | 写出正交矩阵 P 和对角矩阵 D，使 PᵀMP = D（J21 Q5(c)，S22 Q3(c)，J24 Q4(c)，J25 Q4(e)）。J23 实考卷 Q5(c) 也是这一问，但因 A 不对称而作废 | P 的列是单位特征向量，顺序与 D 一致；2–5 分 | J21 Q5(c)，S22 Q3(c)，J24 Q4(c)，J25 Q4(e) |

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据是 12 份卷的索引检索。除 6.3 外，每个编号条目都出现过；下表列出条目内从未考过或极少考的细项。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 6.3 转置、(AB)ᵀ = BᵀAᵀ | 从未作为考点，只在 PᵀMP = D 中出现 | 一张定义卡，并与 6.8 合并 |
| 6.2 三维复合变换（AB 表示先 B 后 A） | 只有 J24 Q2(a) 的 TU = I，从未考过复合变换的顺序 | 一张卡，提醒乘法顺序（与 FP1 相同） |
| 6.6 复合变换的逆，(AB)⁻¹ = B⁻¹A⁻¹ | 从未考过，只考过单个 M⁻¹ 作用于直线或平面 | 一张性质卡 |
| 6.7 2×2 矩阵的特征值 | 从未考过，10 道特征值题全是 3×3 | 不单独做卡，只练 3×3 |
| 1.1 双曲函数的图像与性质 | 249 个小问中没有一个用 "Sketch"，图像从未考过；但定义域与值域会用于舍根，如 cosh x ≥ 1、\|tanh x\| < 1 | 做值域、定义域卡，服务于舍根 |
| 1.2 证明对数形式 | 只考过 1 次（O21 Q2，y < 0 时的 arcosh 对数形式，要说明取负号的理由）；arsinh、artanh 的对数形式从未要求证明 | arcosh、arsinh 的推导各做一张卡 |
| 2.3 y = mx + c 的相切条件 | 只考过 1 次（O20 Q5），公式册不给 | 一张推导卡（代入后令判别式为 0） |
| 2.1 双曲线的参数式 (a cosh t, b sinh t) | QP 里从未出现，双曲线上的点一律给成 (a sec θ, b tan θ) | 以 sec/tan 参数为主 |
| 2.2 直角双曲线的离心率 √2 等 | 未在 FP3 中出现，属于 FP1 内容 | 不做 |
| 4.2 ∫arsinh x、∫arctan x（考纲举的例子） | 从未出现，只考过 arccos(2√x) 和 arcosh kx | 用 1 × 反函数做分部积分的通法卡，各种反函数都练 |
| 4.5 ∫sin nx/sin x 型递推（考纲例子） | 从未出现；sinⁿ、cosⁿ 型只有 J23 一次 | 重点放在"分部积分 + 恒等式拆项"的通法 |
| 4.6 绕 y 轴旋转的曲面面积 | 从未出现，公式册也只印 S_x；极坐标形式考纲排除 | 不做 |
| 5.2 (r − a) × b = 0 形式 | 题面给出 1 次（O20 Q6(b)），要求作答 1 次（S25 Q8(c)），另有 r × b = c 1 次（S24 Q2(b)） | 一张互化卡 |
| 3.1 sech、cosech、coth 的导数 | 公式册不给，但考过：coth 的导数（J24 Q7(b)），sech 的导数（S21 Q4(ii) 推导中）；结果化成 cosech 的有 J21 Q2(a)、S24 Q7(a) | 必须做卡，并练符号 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 J23、S23、J24 三份；没有标 ER 的条目都来自 MS 的评分说明。

1. **"用指数定义"就必须出现指数式**
   - 用双曲恒等式证明不给分：J22 Q1(a) MS 原话 "No marks are available in (a) if exponentials are not used"；S24 Q4(a) MS，S25 Q1(a) MS，J24 Q5(a) 的 MS 和 ER 同此。
   - 分子、分母要因式分解才能得最后的 A1，只化到 e²ˣ、e⁻²ˣ 的分式得 B1M1A0（J24 Q5(a) MS）。
   - 两边同时化简（meet in the middle）要展开并写出结论（J22 Q1(a)，J24 Q5(a) ER）。
   - S25 Q1(a) 还要多写一行，把各项组合成 cosh 6x、cosh 4x。
   - O21 Q2 的定义式要写对变量：写成 cosh y = (eˣ + e⁻ˣ)/2 得 B0。
2. **双曲方程：精确对数、根要全、不能多**
   - 多出的根扣最后的 A：J22 Q1(b)；J22 Q3(b) 写 ± 得 A0；S24 Q4(b) 写 ±ln 3 得 A0；J25 Q1 两个根都要写且不能有别的根。
   - S21 Q1(b)：要舍去 tanh x = 1，并且 "no other answers"。
   - 两边平方求 sinh 或 cosh 会产生增根，不剔除得 M0A0（S22 Q1(b)）。
   - 只写答案 0/5（S23 Q1）。
   - O21 Q2 取负号要说明理由（y < 0，所以 eʸ < 1），这一分要以前面各分全对为前提。
3. **给定答案（A1*）至少要有一行中间步骤**
   - S25 Q9(a)：从公式直接跳到 e = √113/8 得 A0。
   - 同类要求见 S25 Q9(b)、J25 Q7(a)、S24 Q3(a)、S24 Q7(a)（"non-trivial step"）、J22 Q8(c)、O21 Q3(a)，以及 S23 Q6(a) ER。
   - S25 Q7(a)：把导数代入曲面面积公式的过程必须写出，否则 M0A0。
   - S23 Q3(a)：1 + y′² 展开后的式子必须写出；ER 指出很多人直接跳到给定答案。
4. **双曲与三角记号**
   - 漏写 "h"，或 sinh、cosh 写成 sin、cos，都得 A0：S25 Q1(a)；S25 Q2(i)（写成 arcsin 得 A0）；S24 Q4(a)；S24 Q7(a)。
   - S23 Q7(a) ER：cosh 写成 cos "no tolerance"。
   - 用错反函数得 M0：J23 Q1(a) 写成 arsinh 的导数；J23 Q4(a) 写成 arcsin 或 arsin；J22 Q5 要用 arsinh "but not arsin or arcsin"。
   - J24 Q1(i) ER：有人把 arctan 套用了 artanh 的对数形式。
5. **链式法则的系数是最常见的失分点**（建议求导检验积分结果，J23 Q4(a) ER）
   - arcsin 2x 的因子 2（J23 Q1(a) ER）。
   - arcosh 5x 的 5（S23 Q8(a) ER）。
   - ∫1/√(9x² + 16) dx 的 1/3（J23 Q4(a) ER）。
   - 多出一个 2，写成 2arcsin(2x/3)（J24 Q1(ii) ER）。
   - 递推证明里对 cos^(n−1)x、cosh^(n−1)2x 求导漏掉链式因子（J23 Q8(a) ER，S23 Q7(a) ER）。
6. **积分标准式**
   - 根号内的负二次项要先配方，改写成 −∫1/√(4x² − 4x − 63) dx 不给分（J22 Q5(ii)）。
   - 先把 arcosh 3x 改写成 ln 形式再积分得 0 分（S25 Q2(ii)）；S23 Q8(a) ER 也说先化成对数形式 "rarely" 是好办法。
   - 代入上下限的过程要看得见（J25 Q3(ii)）。
   - 换元时要换上下限并用弧度。S22 Q2(ii) 用角度上下限仍可得最后两分，但拿不到 B1。
   - 只给计算器答案得 0 分：S24 Q5(c)（1.477…），S23 Q3(b)（0.6311…，0/5）。
7. **递推公式**
   - **拆法要选对**：cos x·cos^(n−1)x、cosh 2x·cosh^(n−1)2x 可行（J23 Q8(a) ER，S23 Q7(a) ER）。tanhⁿ3x 直接分部积分 "invariably" 走不通，要拆成 tanh^(n−2)·tanh² 并用 1 − sech²（J24 Q5(b) ER）。
   - **边界项**：要写出代入上下限，并说明边界项为 0（O21 Q6(a) MS，S24 Q8(a) MS，J23 Q8(b) ER）。
   - **括号与 dx**：S22 Q7(a) 中漏括号、漏 dx 都算错误；J21 Q6(a) 偶尔漏 dx 可以容忍。
   - **(b) 必须用公式**：J21 Q6(b) 直接求 I₅ 不给分；S21 Q5(b) MS 原话 "the given reduction formula must be used at least once"，用计算器求 I₄ 不行；S24 Q8(b)、S25 Q5(b) 同此。
   - **初值单独算出**：O20 Q4(b) I₀ = sin x，O21 Q6(b) I₁ = ½，S21 Q5(b) I₂ = 1，S25 Q5(b) I₀ = 2，各占一个 B1。S23 Q7(b) ER 指出有人把 I₀ 当成 0，应为 x。
   - **"Hence"**：J23 Q8(c) 只写 "I = 5π/256" 得 0/3，写 I₆ − I₈ = 5π/256 得 3/3。
8. **弧长与曲面面积**
   - 2π 要保留（S22 Q5：用上下限的那一分要求 "2π now included"）。
   - "Total surface area" 要加两端圆面，不加通常 6/8（J22 Q2）；只求曲面面积时加了两端得 A0（J25 Q5(c)）。
   - 公式不能用错：弧长用了 y√(1 + y′²) 得 M0（S24 Q7(a)）；J24 Q8(a) ER 指出有人用了曲面面积公式。
   - O21 Q1：不积分直接写出正确答案按特例给 4/6。
   - J21 Q8(b)：假分式要先做除法，当真分式积分通常只得 B0M1A0M0A0。
   - 换元时 dy 要换成 4cosh u du，不能除；sinh(2arsinh 3) 要能精确算出（J24 Q8(b) ER）。
   - 摆线一类题卡在半角公式（J23 Q6 ER）。
9. **矩阵**
   - 伴随矩阵要除以"他们自己算出的"行列式。S22 Q6(b)：(a) 中把行列式除以 2 是可以的，但在 (b) 中用除过 2 的值得 dM0。
   - 余子式那一分通常要"2 行或 2 列正确"或"至少 6 个正确"（S22 Q6(b)，S23 Q2(a)，J21 Q3(b)）。
   - 数值矩阵也要写出求伴随矩阵的过程（S23 Q2(a)）。
   - (a) 的工作只在 (a) 中记分（S22 Q6(a)，J21 Q3(a)）。J21 Q5 的 (a)、(b) 一起评，但只出现在 (c) 中的 (a) 工作不给分。
   - "对所有 x 非奇异"要配方或用判别式，并写出结论（S22 Q6(a)）。
   - 要利用前一问：U 就是 T⁻¹（J24 Q2(b) ER，很多人重算出错）；M⁻¹ 已在 (a) 求出（S23 Q2(b) ER）。
10. **特征值与对角化**
    - 必须看到 det(M − λI) 的展开，只写因式分解后的三次式不行（J25 Q4(c)，S25 Q3(c)(i)）。
    - 求特征向量时 "making a variable equal to 0 is not a correct method"（S22 Q3(b)）；不写过程直接给出向量得 M0（J25 Q4(d)）。
    - P 的列要单位化，顺序与 D 中的特征值一一对应（J21 Q5(c)，S22 Q3(c)，J24 Q4(c) ER）。D 可以直接写出，不必计算 PᵀMP（J24 Q4(c) ER）。P、D 标签写反扣第二个 B（J25 Q4(e)）。
    - 有重特征值时，"常数项为 0"和"二次式判别式为 0"两种情形都要考虑（S23 Q5 ER）。
    - 参数的负根要舍去（J23 Q5(b)(i)）。
    - 只写答案也能得满分的个例：S25 Q3(a) 写出 3、J24 Q4(a) 写出 5 都得 2/2。
11. **向量**
    - 直线方程要以 "r =" 开头，写成 "l = …" 得 A0（O20 Q6(b)，J22 Q7(c)，S24 Q9(b)，S23 Q4(a) ER）。
    - 坐标可以写成列向量，但不能写成 i, j, k 形式（S22 Q8(a)）。
    - 线面角 = 90° − 直线与法向量的夹角。J23 Q7(b) ER：很多人答 66° 而不是 24°，建议画草图；J25 Q6(b) 同此。
    - 角度按最终答案评分，不适用 isw（J22 Q7(b)，S21 Q6(d)）；但 J25 Q6(b) 允许答对后再错误取整按 isw 处理。
    - 距离要为正（O21 Q5(c)）。
    - 四面体体积 = (1/6)|三重积|：漏 1/6 扣 2 分；体积给定时要取 V = ±12，得两个解（J24 Q6(c) ER）。
    - r.n = p 中的常数要由写明的点算出，不能凭空出现（J21 Q7(a)）。
    - 求两平面交线时，先观察出一个公共点、再叉乘两法向量，比代数消元成功率高得多（S23 Q4(a) ER）。
    - 要求直角坐标式时不能停在参数式（J24 Q2(b) ER）。
    - J24 Q6(b) ER：不必求出 E 点，求出反而更容易算错。
12. **圆锥曲线**
    - e 只取正值：J22 Q8(a) 写 e = ±√5/3 得 A0；J23 Q9(a) ER；J24 Q3(d) ER（不少人取了负值）；S24 Q1(a)。a 同理：J23 Q2(b)(i) 要 a = 2，不能写 ±2。
    - 焦点写坐标，准线写方程：
      - J21 Q9(b) 只要正半轴上的焦点，写 (±3, 0) 得 A0；
      - J23 Q9(a)(ii) 只写 "a/e = 9√2/4" 得 B0；
      - J24 Q3(a)(ii) ER；
      - J25 Q2(b) 写 ± 得 A0。
    - 写 "use calculus" 的题必须真的求导：
      - 用 y = mx + c 时要求出 c（S23 Q6，S24 Q6(a)，J25 Q7(a)，S25 Q9(b)）；
      - 背一个一般的法线公式再写出给定答案，不给分（J21 Q9(a)）；
      - 要求切线却求了法线得 M0（J22 Q8(c)）。
    - 焦半径和的证明要对任意 P 成立，只写 "2a = 6" 得 0/3（J23 Q9(b) MS 与 ER）。
    - 弦中点用二次方程的 −b/(2a)，即两根之和的一半；最后要写出"过原点"之类的结论（J23 Q9(c) ER）。
    - 要用题目指定的量，例如 PS² = e²PM²，不要照搬背过的推导（J24 Q3(c) ER）。
    - 椭圆、双曲线的离心率公式不要混用（J23 Q9(a) ER）。
    - 求面积最大值要说明理由，例如 sin 2θ 的最大值为 1；写出错误的不等式如 −1 < sin 2θ < 1 扣分（S24 Q6(b)）。
13. **计算器与过程**
    - O21 Q7(d)："just using a calculator to solve the cubic generally scores no marks"；用判别式时要代入数值。
    - 2022 年起越来越多题印有"不得只靠计算器"的说明（见 7.1）。这类题的 MS 普遍规定：只写答案或只写小数得 0 分。
    - J24 ER 总评：考生常常没意识到前一问是为后一问铺路（Q2、Q7）。
    - J24 ER 认为最难的是 Q5(b)、Q7、Q8；J23 ER 认为最难的是 Q9，Q6 是第一道有区分度的题。
