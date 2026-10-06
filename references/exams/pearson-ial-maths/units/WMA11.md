# WMA11 Pure Mathematics 1（P1）考纲条目登记

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WMA11.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WMA11 --gaps` 输出为准（快照 2026-10-06）**。

**来源**：Pearson Edexcel IAL Mathematics, Further Mathematics and Pure Mathematics Specification，**Issue 3 – April 2019**（ISBN 978 1 446 94981 8；本地 `research/dl/ial-maths-spec.pdf`，md5 06d01a11…；与 `registry/versions.md` §1.1 一致）。P1 位于印刷页 **pp.12–16**（PDF 页 = 印刷页 + 6）。公式册：*Mathematical Formulae and Statistical Tables* **Issue 2 – January 2021**（P59773RA；Pure Mathematics P1 一节在公式册印刷 **p.3**）。逐页核对：条目编号与页码已用脚本对照逐页文本（77 个纯数条目 0 处不符），含公式的格子另用渲染图核对。登记日期 2026-10-06。

共用部分（资格结构、cash-in、AO、记号附录、计算器规则、各单元公式对照）见 `../specification.md`。

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WMA11/01**（区域卷 WMA11/01A 另有试卷与 MS，考纲未列；2024 年 6 月另有 /01R，见 `inventory/pure-gaps.md`） | 印刷 p.78 Appendix 1；`versions.md` §1.6 |
| 名称 | Unit P1: Pure Mathematics 1 | p.12 |
| 角色 | **IAS 单元**（p.67 表）。Compulsory unit for IAS Mathematics and Pure Mathematics；Compulsory unit for IAL Mathematics and Pure Mathematics。不能计入 Further Mathematics（FM 的必修与选修清单都不含 P1–P4，p.10） | p.12；p.10；p.67 |
| 权重 | IAS 33⅓%，IAL 16⅔% | p.7 |
| 时长与分值 | 外部笔试 1 h 30 min，75 分，Students must answer all questions；可用计算器；提供公式册 | p.12（P1.2） |
| 考季 | January、June、October | p.7；p.70 |
| 2018 考纲首考 | **January 2019**（实际首考同） | p.12 P1.2；p.7；`versions.md` §1.4 |
| 先修 | P1.2 **没有** Prerequisites 一栏（P2–P4 都有）。资格层面：“There are no prior learning or other requirements”，最适合已有 Level 2 资格如 International GCSE in Mathematics 的学生 | p.12；p.75 |
| AO 分值区间（满分 75） | AO1 30–35，AO2 25–30，AO3 5–15，AO4 5–10，AO5 1–5 | p.69 |
| 单元描述 | Algebra and functions; coordinate geometry in the (x, y) [plane]; trigonometry; differentiation; integration（p.12 原文漏印 “plane”，p.7 写作 “coordinate geometry in the (x, y)”） | p.12；p.7 |
| 记号 | Students will be expected to understand the symbols outlined in Appendix 7: Notation；题目使用 SI 单位及常用单位 | p.12 |

## 2. 公式：须记住 vs 公式册给出

**考纲列为须记住、公式册不印**（P1.2 “Notation and formulae”，pp.12–13）：

- Quadratic equations：ax² + bx + c = 0 的根为 x = (−b ± √(b² − 4ac)) / 2a
- Trigonometry：sine rule a/sin A = b/sin B = c/sin C；area = ½ab sin C；arc length = rθ；area of sector = ½r²θ
- Differentiation：xⁿ → nxⁿ⁻¹
- Integration：∫xⁿ dx = xⁿ⁺¹/(n + 1) + c，n ≠ −1

**公式册 P1 节给出**（公式册 p.3）：Mensuration — surface area of sphere = 4πr²；area of curved surface of cone = πr × slant height；Cosine rule a² = b² + c² − 2bc cos A。

注意：
- 余弦定理在公式册里，**正弦定理不在**，要背。
- 球面积与圆锥侧面积印在 P1 节，但 P1 考纲条目没有单列 mensuration；它们供应用题（如 P2 7.1 实际情境的最值题）使用。这是对公式册与考纲的对照观察，不是考纲原文。
- 后续单元都可能用到 P1 公式（公式册 Introduction：“A candidate sitting a unit may be required to use formulae that were introduced in a preceding unit”，公式册 p.1）。
- 评分惯例（WMA14 January 2024 MS，PDF p.6，General Principles for Pure Mathematics Marking 的 “Use of a formula”；本地 `research/dl/wma14-jan24-ms.pdf`）：用学过的公式时先写出公式；不写公式时，方法分只能从正确代入的过程中推断得到，过程一有错就可能失去方法分。

## 3. 考纲条目（P1.3 Unit content）

条目号即考纲编号；“要求”一栏紧贴原文意译，关键术语保留英文原词；页码为印刷页。

### 1. Algebra and functions

**1.1 Laws of indices for all rational exponents** — p.14
- 要求：对所有有理指数使用指数律 aᵐ × aⁿ = aᵐ⁺ⁿ，aᵐ ÷ aⁿ = aᵐ⁻ⁿ，(aᵐ)ⁿ = aᵐⁿ；“The equivalence of a^(m/n) and ⁿ√(aᵐ) should be known.”
- 公式：指数律考纲未列入“须记”清单，也不在公式册里，实际上必须会用。

**1.2 Use and manipulation of surds** — p.14
- 要求：surd 的运算与化简；“Students should be able to **rationalise denominators**.”

**1.3 Quadratic functions and their graphs** — p.14
- 要求：二次函数及其图像（guidance 栏空白）。

**1.4 The discriminant of a quadratic function** — p.14
- 要求：“Need to know and to use” b² − 4ac > 0、b² − 4ac = 0、b² − 4ac < 0 三种情形（两个不同实根／重根／无实根）。

**1.5 Completing the square. Solution of quadratic equations** — p.14
- 要求：用 factorisation、use of the formula、use of a calculator、completing the square 四种方法解二次方程；配方形式 ax² + bx + c = a(x + b/2a)² + (c − b²/4a)。
- 公式：求根公式须记住（p.12）。

**1.6 Solve simultaneous equations; analytical solution by substitution** — p.14
- 要求：解联立方程，用代入法求解析解（一次与二次联立属本条）。

**1.7 Interpret linear and quadratic inequalities graphically** — p.14
- 要求：用图像解释不等式，例如 ax + b > cx + d，px² + qx + r ≥ 0，px² + qx + r < ax + b；把第三式理解为“曲线 y = px² + qx + r 位于直线 y = ax + b 下方”的 x 范围。“Including inequalities with brackets and fractions”，这些可化为一次或二次不等式，例：a/x < b 化为 ax < bx²，x ≠ 0。

**1.8 Represent linear and quadratic inequalities graphically** — p.14
- 要求：在图上表示 y > x + r、y > ax² + bx + c 这类不等式区域；“**Shading and use of dotted and solid line convention is required.**”（这一约定的通常含义是：严格不等号的边界画虚线，含等号的边界画实线；考纲原文只写到 “convention”，阴影画在满足区域还是排除区域以题目要求为准。）

**1.9 Solutions of linear and quadratic inequalities** — p.14
- 要求：代数求解 ax + b > cx + d，px² + qx + r ≥ 0，px² + qx + r < ax + b 等。

**1.10 Algebraic manipulation of polynomials, including expanding brackets and collecting like terms, factorisation** — p.14
- 要求：会用括号；对次数 n ≤ 3 的多项式因式分解，例 x³ + 4x² + 3x；可使用记号 f(x)。
- 范围：P1 的因式分解到三次为止，且例子是可先提公因式的三次式；用 Factor Theorem 分解三次式属 P2 2.1。

**1.11 Graphs of functions; sketching curves defined by simple equations. Geometrical interpretation of algebraic solution of equations. Use of intersection points of graphs of functions to solve equations** — p.15
- 要求：函数包括 simple cubic functions 与 reciprocal functions y = k/x、y = k/x²（x ≠ 0）；“Knowledge of the term **asymptote** is expected.” 也包括 trigonometric graphs。会用图像交点解方程，并从几何上解释代数解。

**1.12 Knowledge of the effect of simple transformations on the graph of y = f(x) as represented by y = af(x), y = f(x) + a, y = f(x + a), y = f(ax)** — p.15
- 要求：能把**其中一种**变换作用于上述任一函数（quadratics, cubics, reciprocals, sine, cosine, tangent）并画出结果；给出任一 y = f(x) 的图像，能画出经其中一种变换后的图像。
- 范围：P1 只做单一变换；多种变换的组合属 P3 1.4。

### 2. Coordinate geometry in the (x, y) plane

**2.1 Equation of a straight line, including the forms y − y₁ = m(x − x₁) and ax + by + c = 0** — p.15
- 要求：To include (i) 过两已知点的直线方程；(ii) 过已知点且与已知直线 parallel（或 perpendicular）的直线方程。例：过 (2, 3) 且垂直于 3x + 4y = 18 的直线为 y − 3 = 4/3 (x − 2)。

**2.2 Conditions for two straight lines to be parallel or perpendicular to each other** — p.15
- 要求：两直线平行或垂直的条件（平行：斜率相等；垂直：斜率乘积为 −1。考纲此格的 guidance 栏空白，括号内为通用表述）。

### 3. Trigonometry

**3.1 The sine and cosine rules, and the area of a triangle in the form ½ab sin C** — p.15
- 要求：正弦、余弦定理与三角形面积 ½ab sin C；“Including the **ambiguous case** of the sine rule.”
- 公式：sine rule 与 ½ab sin C 须记住（p.12）；cosine rule 在公式册 P1 节（公式册 p.3）。

**3.2 Radian measure, including use for arc length and area of sector** — p.15
- 要求：弧度制；使用 s = rθ 与 A = ½r²θ。
- 公式：两式都须记住（p.12）。

**3.3 Sine, cosine and tangent functions. Their graphs, symmetries and periodicity** — p.15
- 要求：知道 y = 3 sin x、y = sin(x + π/6)、y = sin 2x 这类曲线的图像（含对称性与周期性）。
- 范围：P1 不要求解三角方程（属 P2 6.2）。

### 4. Differentiation

**4.1 The derivative of f(x) as the gradient of the tangent to the graph of y = f(x) at a point; the gradient of the tangent as a limit; interpretation as a rate of change; second order derivatives** — p.16
- 要求：例如知道 dy/dx 是 y 关于 x 的 rate of change；可使用记号 f′(x)、f″(x)。
- 排除：“**Knowledge of the chain rule is not required.**”（chain rule 属 P3 4.2）

**4.2 Differentiation of xⁿ, and related sums, differences and constant multiples** — p.16
- 要求：会对 (2x + 5)(x − 1)、(x² + 5x − 3)/(3√x) 这类表达式求导（先展开或拆成幂再逐项求导）。
- 公式：xⁿ → nxⁿ⁻¹ 须记住（p.13）。

**4.3 Applications of differentiation to gradients, tangents and normals** — p.16
- 要求：用求导求曲线上指定点处的 tangent 与 normal 方程。
- 范围：stationary points、增减性属 P2 7.1。

### 5. Integration

**5.1 Indefinite integration as the reverse of differentiation** — p.16
- 要求：“Students should know that a **constant of integration** is required.”

**5.2 Integration of xⁿ and related sums, differences and constant multiples** — p.16
- 要求：会积分 ½x² − 3x^(−1/2)、(x + 2)²/√x 这类表达式；给出 f′(x) 和曲线上一点，求曲线方程 y = f(x)。
- 排除：“(Excluding n = −1 and related sums, differences and multiples).”（∫1/x dx = ln|x| + c 属 P3 5.1。）
- 公式：∫xⁿ dx = xⁿ⁺¹/(n + 1) + c，n ≠ −1，须记住（p.13）。
- 范围：P1 只有不定积分；定积分与面积属 P2 8.1–8.2。

## 4. 与相邻单元的界线

| 内容 | P1 做到哪里 | 属于哪个单元（考纲出处） |
|---|---|---|
| 多项式 | 展开、合并、≤ 三次的因式分解（1.10） | algebraic division、Factor／Remainder Theorem → **P2 2.1**（p.18）；有理式化简、代数除法 → **P3 1.1**（p.23）；部分分式 → **P4 2.1**（p.27） |
| 二次方程的根 | discriminant 判别根的个数（1.4） | 根与系数关系 α + β、αβ → **FP1 2.1**（p.33）；复数根 → **FP1 1.4**（p.32） |
| 不等式 | 一次、二次（含括号与分式、可化为一次或二次的）不等式及其图示（1.7–1.9） | 含 modulus 的不等式、分式不等式 1/(x − a) > x/(x − b) → **FP2 1.1**（p.37）；用图像解 \|2x − 1\| > x + 5 → **P3 1.3**（p.23） |
| 图像变换 | 单一变换（1.12） | 两种以上变换组合 → **P3 1.4**；y = \|f(x)\|、y = f(\|x\|) → **P3 1.3**（p.23） |
| 坐标几何 | 直线（2.1–2.2） | 圆 → **P2 3.1**（p.18）；参数方程 → **P4 3.1**（p.27）；抛物线、直角双曲线 → **FP1 4**（p.33）；椭圆、双曲线 → **FP3 2**（p.41） |
| 三角 | 正余弦定理、弧度、sin/cos/tan 的图像（3.1–3.3） | tan θ = sin θ/cos θ、sin²θ + cos²θ = 1 与解三角方程 → **P2 6.1–6.2**（p.20）；sec/cosec/cot、复角与倍角公式 → **P3 2**（pp.23–24） |
| 求导 | xⁿ 及其和差倍；切线与法线；二阶导数（4.1–4.3） | 驻点与增减性 → **P2 7.1**（p.20）；e^kx、ln、三角函数求导与 product／quotient／chain rule → **P3 4.1–4.2**（p.24）；隐函数与参数求导 → **P4 5.1**（p.27） |
| 积分 | xⁿ（n ≠ −1）的不定积分，由 f′(x) 与一点求曲线（5.1–5.2） | 定积分与面积、trapezium rule → **P2 8.1–8.3**（p.20）；1/x、e^kx、三角函数的积分 → **P3 5.1**（p.25） |
| 被其他单元依赖 | — | M1 先修：“A knowledge of P1 and P2 and associated formulae and of vectors in two dimensions”（p.44）；S1 公式册注明可能用到 P1、P2 公式（公式册 p.14）；FP1 先修 P1 与 P2（p.30） |

## 5. 往届真题

2018 考纲下 WMA11 的试卷、MS、ER 收集情况与缺口以 `python scripts/exam_index.py WMA11 --gaps` 输出为准（快照 2026-10-06）；构建时的清单 `inventory/pure.json`、`pure-gaps.md` 是构建溯源，不随包发布。

逐题索引（24 份卷、240 题，含每小问的考纲条目、命令词、答案形式、MS 与 ER 要点）见同目录 `WMA11.questions.json`；各卷来源、缺失文件与审计记录见 `WMA11.coverage.part1.md`、`WMA11.coverage.part2.md`。下面第 6 节是据此汇总的考法概览。

## 6. 真题需求概览

**数据与口径**。依据同目录 `WMA11.questions.json`（2026-10-06 合并并审计）：24 份卷 = WMA11/01 的 22 个考季（2019-01 至 2026-06；2020-06 取消，无卷）+ 2024-06 /01R + 2025-06 /01A，共 240 题、590 小问、1800 分。MS 有 22 份卷（2019-01 至 2025-10 全部，含 /01R、/01A；只有 2026-01、2026-06 没有，共 47 个小问 `ms` 为空），ER 只有 5 份（2022-10 至 2024-01），所以评分惯例取自 22 份 MS，考官提醒只能从这 5 份 ER 里取。2019-01 至 2022-06 的 10 份 MS 是 2026-10-06 补入的，2019-01、2019-06 的题面同日改为依据 QP PDF 核对（见下方注）；2026-06 只有第三方逐题截图（看不到封面和 P 号，见 `WMA11.coverage.part2.md` 第 8 节 Audit note）。

> **Critic 2026-10-06（已补完，同日）**：2019-01 至 2022-06 的 10 份 Pearson 官方 MS 取自 GitHub `RayZ3R0/papernexus-finder@921bdf4f` 的 `papers/mathematics/ms/pure1/`（封面 Publications Code `WMA11_01_1901_MS` … `WMA11_01_2206_MS`；2021-06 起的 Log Number 与本索引 P 号一致），本地副本 `registry/src/WMA11/<series>_01_ms.pdf`。这 10 份卷共 101 题（2019-01 至 2020-10 有 53 题，2021-01 至 2022-06 有 48 题）、232 个小问的 `ms` 已全部填写，`sources.ms` 指向上述文件。2019-01、2019-06 的题面已改为依据 QP PDF（`2019-01_01_qp.pdf`、`2019-06_01_qp.pdf`，P60791A、P61837A）逐题核对：改写 14 个小问的 `ask`，按 MS 补准 14 个 `final_form`，2019-06 Q2(b) 的 spec 去掉 1.6（这是含根式的一次方程，不是联立方程；所以 6.2 里 1.6 的题数、小问数各少 1）。审核：按 MS 原文逐项复核了 15 题（2019-01 Q4、Q8，2019-06 Q2、Q7，2019-10 Q3、Q10，2020-01 Q4、Q11，2020-10 Q7，2021-01 Q6，2021-06 Q7，2021-10 Q4，2022-01 Q8，2022-06 Q7、Q10），另用脚本核对了 184 个小数是否出现在所引 MS 页（未出现的 5 个都是正确的派生值或等价写法）。改正 2 处：2022-06 Q7(b) 常数 c 的 follow-through 式子符号写反，应为 A/12 − 36；2019-01 Q4 的下界条件按 MS 改为“a ≤ x，a ≤ 12”。2026-01、2026-06 仍无 MS（缺口以 `python scripts/exam_index.py WMA11 --gaps` 为准）。

引用写法：`2023-01 Q5(b)` 指 2023 年 1 月 WMA11/01 第 5 题 (b)；`2024-06R` 指 /01R 卷，`2025-06A` 指 /01A 卷。一个小问可以挂多个条目，各条目分别计数。“主考”指该小问 spec 列表里排第一的条目；“分值中位”按挂了该条目的小问计；“卷”指 24 份卷中出现该条目的份数。

### 6.1 卷面结构

- 每卷 9–12 题，75 分，全部必答，单题最高 10–14 分。
- 第 1 题在 18/24 份卷里是“幂函数和”的求导或积分（3–8 分）：积分 10 次（如 2020-01 Q1、2024-06 Q1、2026-06 Q1），求导 8 次（如 2021-06 Q1、2025-10 Q1、2026-01 Q1）。其余 6 份的第 1 题考扇形（2019-10）、指数（2020-10、2025-06）、二次不等式（2023-06）、直线（2024-10）或图像变换（2025-06A）。
- 不许依赖计算器的题（题首加粗 banner：show all stages of your working / solutions relying on calculator technology are not acceptable，或小问括注）逐年增多：2019-01 至 2020-10 每卷 1 题；2021-01 至 2022-10 每卷 2–3 题；2023-01 起每卷 2–6 题，中位 4 题（2025-01 有 6 题）。这类题的 MS 规则见 6.4 第 1 条。
- 24 份卷每份都有：一道扇形或弧长题（3.2）；一道三角形求边、角或面积的题（3.1，常与扇形合成一题）；一道“由 f′(x) 和一点求 f(x)”的题（5.1、5.2）；至少一题切线或法线（4.3）。

### 6.2 各条目怎么考

**1.1 Laws of indices**（24/24 卷；79 题 113 小问，主考 42；小问分值中位 4，范围 1–8）
- 命令词：Find 68，Express 13，Solve 8，Show that 7，Hence find／Hence solve 各 5。
- 考法：几乎每道微积分题都要先把根式、分式改写成 xⁿ 再求导或积分（与 4.2、5.2 同挂）；单独写成 kxⁿ 的题见 2023-10 Q2、2025-06 Q1；指数方程，化成同底后比较指数或换元成二次，见 2020-01 Q2、2024-01 Q4、2025-06A Q4(i)、2025-10 Q4(i)；分数指数下的隐藏二次见 2022-10 Q4(b)、2026-06 Q4(b)。
- 答案形式：simplest form（k、n 都化简），精确值。

**1.2 Surds**（22/24 卷；32 题 45 小问，主考 16；中位 4，范围 2–6）
- 命令词：Find 15，Solve 6，Show that 4。
- 考法：有理化分母（2022-01 Q3(ii)、2022-06 Q3(ii)、2025-01 Q2(a)）；把答案写成 a + b√c（2019-06 Q2、2021-06 Q3(c)、2026-06 Q7(b)）；精确长度与面积（2022-10 Q8(b)、2024-01 Q5(c)）；隐藏二次的精确根（2025-10 Q4(ii)、2025-10 Q10(b)）。
- 答案形式：精确 surd，写成题目指定的 a + b√c 形式。

**1.3 Quadratic functions and their graphs**（16/24 卷；17 题 22 小问，主考 11；中位 2，范围 1–5）
- 命令词：Find 9，State 3，Deduce 3，Sketch 2。
- 考法：由顶点和一个根求二次式（2022-06 Q5(a)、2023-01 Q8(b)(c)、2024-01 Q9(b)、2024-10 Q4(a)）；过三点求二次式（2025-06A Q8(b)）；带顶点和截距的草图（2023-06 Q3(b)、2024-01 Q9(a)）；对称轴（2022-01 Q2(c)）；二次模型在情境中的解释与局限（2021-06 Q5(a)(d)）。

**1.4 The discriminant**（19/24 卷；20 题 20 小问，主考 19；中位 5，范围 3–7）
- 命令词：Find 12，Show that 5，Hence find 2。
- 考法：都是“直线与曲线（或方程）根的个数”转成判别式条件：不相交（2020-01 Q8、2021-01 Q6(c)、2024-01 Q7(b)），两个不同交点（2020-10 Q7(b)、2025-01 Q7(b)），至少一个交点（2024-10 Q6(b)、2025-06A Q7(b)(i)、2025-10 Q6(b)），相切或只有一个公共点（2019-06 Q6(a)、2019-10 Q6(b)、2024-06 Q4(a)、2026-06 Q10(b)），方程无实根（2019-01 Q9、2023-01 Q4、2025-06 Q10(b)），关于 x² 的二次式有 4 个不同交点（2022-01 Q10(b)、2024-06 Q8(c)）。曲线常是倒数函数 k/(x − a)，要先乘过去化成二次式。
- 答案形式：参数的不等式区间（14/20），或 show that 一个给定的二次式／不等式。

**1.5 Completing the square; solving quadratics**（24/24 卷；61 题 76 小问，主考 40；中位 3，范围 1–7）
- 命令词：Find 20，Hence find 8，Show that 7，Find, using algebra 6，Solve 5，Express 5。
- 考法：写成 a(x + b)² + c（a 常为负数或不为 1，如 2020-10 Q2(a)、2022-01 Q2(a)、2025-10 Q5(a)、2026-06 Q5(a)），再读出顶点或最值；在 banner 下解隐藏二次，变量是 √x、x²、x^(2/3) 或 3ˣ（2021-01 Q7(a)、2022-06 Q6(b)、2023-10 Q8、2025-06 Q10、2026-06 Q4(b)）；求交点、扇形 r 等时出现的二次方程。
- 答案形式：精确根（常要舍去一个根并说明理由）、配方式、顶点坐标。

**1.6 Simultaneous equations by substitution**（24/24 卷；55 题 65 小问，主考 34；中位 4，范围 1–7）
- 命令词：Find 29，Show that 11，Find, using algebra 6，Use algebra to find 6。
- 考法：直线与二次、三次或倒数曲线求交点（2022-01 Q4(a)、2024-06 Q6(a)、2025-06 Q7(c)、2026-06 Q6(b)）；先 show that 消元后的方程，再 hence solve（2022-06 Q6、2023-10 Q8、2024-06R Q4(a)、2026-01 Q2(a)）；用两组数据拟合模型的常数（2019-10 Q2(a)、2021-01 Q2(a)、2022-10 Q3(a)、2025-01 Q3(a)、2025-06A Q2(a)）；扇形面积与周长联立求 r、θ（2026-06 Q7(b)）。
- 答案形式：坐标成对给出，常要求精确值；show that 要写出消元的中间一步。

**1.7 Interpret inequalities graphically**（11/24 卷；11 题 12 小问，主考 4；中位 3，范围 1–5）
- 考法：从给定草图读出 f(x) > 0、f(x) ≤ 0 或 f(x) < 6 的 x 范围（2019-10 Q10(a)、2021-01 Q8(a)、2022-10 Q7(a)）；带 x 在分母的不等式（2021-10 Q3(i) 解 3/x > 4，与 1.9 同挂）；其余小问是与 1.8 同挂的区域题。
- 答案形式：x 的不等式，“中间段”写成一个连写不等式，两段要分开写。

**1.8 Represent inequalities graphically (regions)**（16/24 卷；16 题 17 小问，主考 16；中位 3，范围 2–5）
- 命令词：Use inequalities (to define／to fully define) 11，Define 2，Identify 2，Find 1，Represent 1。
- 考法：17 小问里有 15 问是反向的：给出阴影区域 R，用不等式写出 R（2019-10 Q3(c)、2022-10 Q9(d)、2023-10 Q11(d)、2025-10 Q5(c)、2026-06 Q5(c)）；2023-06 Q7(a) 由区域面积反求常数。只有 2026-01 Q3(ii) 是正向的：在给定网格上标出满足 x + 5 ≤ y ≤ x(x − 3) 的区域（这份卷没有 MS）。
- 答案形式：一组含 x 和 y 的不等式，边界（曲线、直线、坐标轴）都要写到。

**1.9 Solving linear and quadratic inequalities**（20/24 卷；23 题 27 小问，主考 13；中位 4，范围 1–7）
- 命令词：Find 12，Hence find 4，Solve 3。
- 考法：二次不等式要取“外侧”或“内侧”区域（2023-06 Q1、2024-06R Q2(b)）；一次不等式（2024-06R Q2(a)，情境中的 2019-06 Q3(a)）；两个不等式求交集（2019-06 Q3(c)、2024-06R Q2(c)）；判别式之后求参数区间（见 1.4）；分式不等式（2026-01 Q3(i) 解 4/z < 8）；情境中的时间区间（2021-06 Q5(c)）。
- 答案形式：区间写法要合规，见 6.4 第 6 条。

**1.10 Polynomials: expand, factorise**（22/24 卷；41 题 54 小问，主考 27；中位 3，范围 2–6）
- 命令词：Find 23，Show that 6，Use algebra to find 5，Expand 3。
- 考法：展开三个括号的乘积（2019-10 Q10(b)、2023-01 Q10(b)），常为随后求导或积分做准备（2024-01 Q1、2025-10 Q2）；完全因式分解三次式（2023-10 Q4(b)、2024-06R Q5(a)）；用代数解三次方程（2019-06 Q5(a)、2022-10 Q4(a)）；由草图上的根、重根和截距写出三次式（2024-10 Q4(b)、2025-06 Q7(a)、2026-01 Q6(b)、2026-06 Q6(a)）。

**1.11 Graphs of functions; sketching; intersections**（23/24 卷；49 题 64 小问，主考 34；中位 3，范围 1–5）
- 命令词：Sketch 24，State 13，Find 9，Deduce 4。
- 考法：画含重根的三次曲线（2020-01 Q10(a)、2021-10 Q6(a)、2022-10 Q6(a)(i)）；画倒数曲线 k/x、k/(x − a)、k/x + c，截距和渐近线用参数 k 表示（2019-10 Q6(a)、2024-01 Q7(a)、2025-01 Q7(a)、2025-10 Q6(a)、2026-06 Q10(a)）；由两条曲线的交点个数说出方程根的个数并给出理由（2021-06 Q9(b)、2022-10 Q6(b)、2023-10 Q4(d)）。
- 答案形式：草图标出与坐标轴的全部交点（含参数），渐近线写成方程；“根的个数”要给出基于图像交点的理由。

**1.12 Single transformations**（24/24 卷；41 题 59 小问，主考 33；中位 2，范围 1–6）
- 命令词：State 19，Sketch 19，Find 11，Write down 5，Describe fully／Fully describe 2。
- 考法：最常见的是 f(x + a)（11 份卷）；f(−x)、f(ax)（2019-01 Q8(b)、2022-06 Q4(ii)、2024-06 Q3(b) 的 f(−3x)、2024-06R Q8(c)）；求点的像（2024-10 Q9(d)、2025-06A Q1(a)、2025-10 Q9(b)）；求常数使变换后的曲线过原点或给定点（2019-06 Q10(d)、2022-01 Q7(a)(b)）；三角函数 A sin x + k、A cos x + k 的最值点（2020-01 Q7(b)、2021-01 Q3(b)、2024-06 Q11(b)、2024-10 Q7(b)）；用文字描述变换（2023-01 Q7(b)、2025-06 Q9(a)）。
- 答案形式：像点坐标；草图标出关键点和渐近线；描述变换要写全类型、方向和比例因子或平移向量。

**2.1 Equation of a straight line**（24/24 卷；61 题 89 小问，主考 36；中位 3，范围 1–6）
- 命令词：Find 69。
- 考法：过两点或过一点且已知斜率的直线；中点、距离、由坐标求三角形面积（11 小问，9 份卷，如 2024-01 Q5(c)、2024-06 Q9(c)、2026-06 Q2(b)）。考纲 2.1 正文没有单列距离、中点和面积，但这些几乎每年都考；线性模型也归在这一条（2019-10 Q2、2022-10 Q3）。
- 答案形式：题目指定 y = mx + c 的有 21 小问，指定 ax + by + c = 0 且 a、b、c 为整数的有 13 小问，“任意正确形式”的有 12 小问。

**2.2 Parallel and perpendicular lines**（24/24 卷；37 题 43 小问，主考 15；中位 3）
- 考法：用斜率乘积为 −1 求法线或垂线；平行直线、平行切线（2024-06R Q10(b)、2024-10 Q9(c)、2025-10 Q10(b)）；用斜率乘积证明直角，再补出矩形的第四个顶点（2023-01 Q2）。

**3.1 Sine rule, cosine rule, ½ab sin C**（24/24 卷，每卷 1 题；54 小问，主考 47；中位 3，范围 1–8）
- 命令词：Find 35，Show that 10，Hence find 5。
- 考法：通常与扇形合成一个实物平面图（花园、标志、池塘、徽章）；正弦定理的钝角情形（9 份卷：2019-01 Q7(a)、2019-06 Q7(b)、2019-10 Q4(a)、2021-01 Q5(a)、2022-06 Q2(b)、2024-01 Q2(b)、2025-01 Q8(a)、2025-10 Q3(a)、2026-06 Q3(b)）；用 ½ab sin C 反求角或边（2025-10 Q3(b)、2026-06 Q3(a)）。
- 答案形式：指定 d.p.（28 小问）或 s.f.（14 小问）；show that 要从更精确的值得出给定值。

**3.2 Radians, arc length, sector area**（24/24 卷，每卷 1 题；63 小问，主考 40；中位 3，范围 1–8）
- 命令词：Find 34，Show that 16，Hence find 6。
- 考法：组合图形的周长与面积，要用到优弧扇形的反射角 2π − θ（2024-01 Q8、2025-10 Q7），以及“周长 = 弧长 + 两条半径”；弓形（弦与弧围成）面积（2022-01 Q5(b)）；由面积和周长联立求 r 与 θ（2019-01 Q10、2026-06 Q7）。
- 答案形式：d.p.／s.f.／精确（含 π）；show that 常要给 3 或 4 位有效数字。

**3.3 Trig graphs, symmetry, periodicity**（23/24 卷；23 题 60 小问，主考 52；中位 2，范围 1–4；只有 2022-10 没考）
- 命令词：State 30，Find 10，Write down 9，Sketch 6。
- 考法：读出 A sin(x + c)、A cos(bx) 的最值点、截距和周期（角度制与弧度制都有）；看图写出函数式（2023-06 Q9(i)(a)(ii)(a)、2025-06A Q3(a)、2025-10 Q9(a)、2026-01 Q9(a)）；在很长的区间上数解的个数（2019-01 Q5(c)、2023-01 Q9(b)、2025-06 Q4(c)、2026-06 Q9(b)）；tan 的周期与渐近线（2021-06 Q9、2023-01 Q9、2024-06R Q9、2026-01 Q9(c)）；用对称性写 sin(180° − α) 一类的值（2022-06 Q9(a)）。
- 答案形式：坐标（弧度制要精确，含 π），解的个数。

**4.1 Derivative as gradient; second derivative**（18/24 卷；25 题 30 小问，主考 20；中位 3）
- 考法：给出 f″(x) = 0 或 f″ 的值，求常数或 x（2021-10 Q10(a)、2022-06 Q7(a)、2024-01 Q10(a)、2024-06R Q3(b)、2026-06 Q4(b)）；求某点的斜率；弦 PQ 的斜率（含 h）及其极限，只在 2019-10 Q7、2020-01 Q3 考过。

**4.2 Differentiating xⁿ**（24/24 卷；38 题 42 小问，主考 22；中位 3）
- 考法：先把分式拆项、根式写成幂、括号展开，再逐项求导；常作为第 1 题，或作为切线、法线、驻点类题目的第一步。
- 答案形式：simplest form；导数后面不能加 + c（6.4 第 3 条）。

**4.3 Tangents and normals**（24/24 卷；36 题 45 小问，主考 38；中位 4，范围 2–6）
- 命令词：Find 30，Show that 5，Find, using algebra 4。
- 考法：求切线或法线方程；法线与曲线的第二个交点（2025-10 Q10(a)），或法线同时是曲线另一点的切线（2022-06 Q10(b)）；已知切线方程，反求常数 k 或切点（2025-10 Q8(a)、2026-01 Q8(a)、2026-06 Q8(a)）；两条平行切线（见 2.2）。
- 答案形式：按题目指定的直线形式（见 2.1），常要求整数系数或精确值。

**5.1 / 5.2 Indefinite integration of xⁿ**（两条都是 24/24 卷；43 题 44 小问；中位 5，范围 3–8）
- 命令词：Find 40，Hence find 3。
- 考法：一类是单独积分（常在第 1–3 题），先展开或拆项（2024-01 Q1、2025-06 Q3、2026-06 Q1）；另一类每卷必考：由 f′(x) 和曲线上一点求 f(x)。f′(x) 常含未知常数，要先用 f″ = 0 或已知斜率求出（2021-10 Q10、2022-06 Q7、2024-01 Q10）；从 f″(x) 开始积分两次的只有 2019-10 Q11、2020-01 Q11、2023-01 Q11(b)。
- 答案形式：simplest form，带 + c；求 f(x) 的题要算出常数，最后写出完整的 f(x)。

### 6.3 尚未考过或极少考的考纲内容

22 个条目都至少考过一次。以下是条目 guidance 中写明、但在 24 份卷里没考或只考过一两次的点：

- **4.1 interpretation as a rate of change**：没有出现过情境中的“变化率”解释题（0/24）。
- **4.1 the gradient of the tangent as a limit**：只在 2019-10 Q7、2020-01 Q3 出现过（弦 PQ 斜率含 h，再说明 h → 0 时的极限），2020-01 之后 22 份卷都没有。
- **1.8 shading and dotted/solid line convention**：正向画区域只有 2026-01 Q3(ii)（无 MS）。22 份 MS 里只有 2019-01 Q4 写了虚线／实线约定：虚线边界用 < 或 >、实线边界用 ≤ 或 ≥，两者对调但前后一致也给分。其他区域题的 MS 对严格与非严格多半不作要求（2019-10 Q3(c)、2022-01 Q4(b)、2022-06 Q5(c)）。
- **1.11 y = k/x²**：只画过两次（2022-01 Q10(a)、2022-10 Q6(a)(ii)）。
- **1.7 含分式的不等式（a/x < b 化为 ax < bx²）**：只有 2021-10 Q3(i) 和 2026-01 Q3(i)。
- **1.12 y = af(x)**：从未要求对一般曲线画 af(x)，只问过像点坐标（2024-10 Q9(d)、2025-06A Q1(a)(ii)、2025-10 Q9(b)(ii)）或三角函数的振幅。
- **公式册 P1 节的 mensuration（球面积、圆锥侧面积）**：24 份卷都没有用到。

### 6.4 反复出现的评分惯例

以下来自 22 份 MS 和 5 份 ER，引用格式为“卷 题号”。2019-01 至 2022-06 的 10 份 MS 是后来补入的，补入后各条惯例都没有变，只在第 1、6、7、9 条加了早年的例子。

1. **不许依赖计算器的题，只写答案得 0 分。** 二次方程或隐藏二次必须写出因式分解、求根公式或配方，而且因式要和方程对得上；因式对不上会被当作计算器作答，丢掉解方程的 M 分（2025-10 Q5(b)、2025-01 Q5(c)、2025-06A Q5(b)(ii)）。MS 写明 “Correct answer with no working scores no marks”（2025-10 Q4(i)）。ER 一再批评直接抄计算器根：2023-01 Q5(b)、2023-10 Q6(b)、2024-01 Q4(b)。早年的 MS 规则相同：只写答案 0 分（2021-01 Q7(a)、2022-01 Q4(a)），只写计算器根的三次方程 0 分（2019-06 Q5(a)），解二次方程不写过程丢 dM 和最后的 A（2020-10 Q4）。
2. **先写公式。** MS 通则 “Use of a formula” 要求先写出所用公式；不写公式时，方法分只能从正确代入中推断，“may be lost if there is any mistake in the working”（2022-10、2025-10 MS 通则）。
3. **精确值与 + c。** 题目要求 exact 或明显要用 surd 时，“marks will normally be lost if the candidate resorts to using rounded decimals”（MS 通则；实例 2022-10 Q8(a)、2023-01 Q1(b)、2025-10 Q4(ii)）。积分漏写 + c 扣最后的 A 分（2024-06 Q1、2025-10 Q2；ER 2024-01 通则 “failing to add + c when integrating will lead to the loss of a mark”）。反过来，导数后面加 + c 也判 A0（2023-06 Q4(b)、2025-10 Q1(a)）。
4. **Show that（A1\*）。** 要写出至少一个中间步骤和结论，不能只把给定答案重写一遍。例如 2022-10 Q8(c) 要看到 AB² = 27；2025-06A Q7(b)(i) 要看到 (6m − 4)² + 100m ≥ 0；2025-10 Q7(a) 要从 r = 6.03… 得出 8.83。ER 原话：“it is the steps leading to the answer where the marks will be awarded”（2022-10 Q8）。
5. **方法错但答案碰巧对，不给分。** 例如 2024-10 Q5(c) 误用 ½·5·OP·1.2 也能得 4.7 km，最多 M0A0M1A0；2023-01 Q6(d)、2025-06A Q9(c) 的扇形题也写了同类警告。
6. **不等式的写法。** “或”的两段要分开写，“且”的中间段要写成连写不等式。下列写法判 A0：“18 > k > 2”和用 “and” 连接两段（2025-01 Q7(b)）；“A > 0 or A < 4” 和 “A > 0, A < 4”（2024-06 Q8(c)）；−1/4 ≥ x ≥ 2 一类的写法（2023-06 Q1）；早年同样：用 “and” 连接两段或写成 −12 > k > −4（2020-10 Q7(c)），中间段用 “or”、逗号或 ∪ 连接（2021-01 Q6(c)、2022-01 Q10(b)）。如果题目给了 k > 0，下限必须写对。ER 还提到用 R 代替 y、漏写 y ≥ 0 等问题（2023-10 Q11(d)、2022-10 Q9(d)）。
7. **草图。** 不画图就没有分（2025-10 Q6(a)、2025-06A Q7(a)、2023-06 Q3(b)、2020-10 Q5(i)、2020-10 Q7(a)）。渐近线要写成方程，不能只在轴上标一个数（2025-01 Q7(a)、2025-10 Q6(a)）；写 “x-axis” 也不给分（2020-10 Q7(a)）。重根处曲线要“相切”而不是穿过 x 轴（2023-10 Q4(c)）。“根的个数”必须用图像交点说明理由，用代数或判别式说明不得分（2023-10 Q4(d)）。
8. **变换的用词。** 要说 stretch／translation，并写出方向、比例因子或平移向量。“compression by factor 2”判 A0，“multiply each x value by 2”“add 12 to each y value”都不给分（2025-06 Q9(a)）。ER 也批评过用 shift／move 代替 translation（2023-01 Q7(b)）。
9. **钝角与弧度。** 正弦定理在钝角情形要取补角：2024-01 Q2(b) 有人用 32.2° 代替 147.8°；2025-01 Q8(a) 要把 1.11 转成 2.034。角度制的题写成弧度，或坐标不加括号，第一次出现时扣 1 分（2024-01 Q6、2020-01 Q7(a)、2021-10 Q4(a)）。
10. **切线与法线。** 法线斜率要取负倒数；用错曲线上的点或把切线与法线搞混，后面的分基本全丢（ER 2023-01 Q11(a)、2023-10 Q7(a)(ii)、2024-01 Q3(b)）。从 f″ 积分得到 f′ 时，第一个常数要用 f′(a) = 已知斜率来求，不能代入点的坐标（ER 2023-01 Q11(b)）。
11. **扇形组合图形。** 常见错误：用 2π − θ 代替 π − θ（2022-10 Q8(d)、2023-01 Q6）、漏掉小扇形或一段弧（2023-10 Q9）、周长漏加两条半径（2022-10 Q8(a)(ii)）、中间步骤过早四舍五入（2023-10 Q5(b)、2024-01 Q8(b) 把 55.98 写成 56.1）。
12. **复合题的最后一分常要求“只给符合条件的值”。** 例如 x > 0 或 y > 0 时要舍根（2022-10 Q4(b)）；2025-10 Q10(a) 只要 x = −5/4，2025-10 Q5(b) 只要 x = 25/4；2023-06 Q2(c) 要按 x > y 配对。反过来，舍掉合法的根也扣分：2024-01 Q4(b) 舍去 x = −2 判 A0。
