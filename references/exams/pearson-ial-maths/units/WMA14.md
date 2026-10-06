# WMA14 Pure Mathematics 4（P4）考纲条目登记

**来源**：Pearson Edexcel IAL Mathematics, Further Mathematics and Pure Mathematics Specification，**Issue 3 – April 2019**（ISBN 978 1 446 94981 8；本地 `research/dl/ial-maths-spec.pdf`，md5 06d01a11…；与 `registry/versions.md` §1.1 一致）。P4 位于印刷页 **pp.26–29**（PDF 页 = 印刷页 + 6）。公式册 *Mathematical Formulae and Statistical Tables* **Issue 2 – January 2021**（P59773RA；Pure Mathematics P4 一节在公式册印刷 **p.5**）。条目编号与页码已用脚本逐页核对，所有页另用渲染图核对。登记日期 2026-10-06。

共用部分见 `../specification.md`。

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WMA14/01**（区域卷 WMA14/01A：June 2025 起已见，为合订册；January 2026、June 2026 的 /01A 为独立 question paper ＋ answer book） | p.78；`versions.md` §1.6 |
| 名称 | Unit P4: Pure Mathematics 4（p.11 目录误印 “Pue Mathematics 4”） | p.26 |
| 角色 | **IA2 单元**（p.67）。Compulsory unit for IAL Mathematics and Pure Mathematics；IAS 权重 N/A；不计入 Further Mathematics。IAL Mathematics 的 A* 要求 P3 + P4 合计 UMS ≥ 180/200（p.74） | p.26；p.7；p.74 |
| 权重 | IAS N/A，IAL 16⅔% | p.7 |
| 时长与分值 | 1 h 30 min，75 分，answer all questions；可用计算器；提供公式册 | p.26（P4.2） |
| 考季 | January、June、October | p.7；p.70 |
| 2018 考纲首考 | 考纲写 **June 2020**；该季全球取消，**实际首考 October 2020** | p.26；p.7；`versions.md` §1.4–1.5 |
| 先修 | “A knowledge of the specifications for P1, P2 and P3, their prerequisites and associated formulae, is assumed and may be tested.” | p.26 |
| AO 分值区间 | AO1 25–30，AO2 25–30，AO3 5–10，AO4 5–10，AO5 5–10 | p.69 |
| 单元描述 | Proof; algebra and functions; coordinate geometry in the (x, y) plane; binomial expansion; differentiation; integration; vectors | p.26 |
| Issue 3 的改动 | 新增 **6.5**（参数曲线下面积，不要求画参数曲线）。用 Issue 2 或更早版本的资料时注意这一条 | PDF p.3 “Issue 3 changes”；p.28 |

## 2. 公式：须记住 vs 公式册给出

**考纲列为须记住**（P4.2，p.26：“This is a list of formulae that students are expected to remember and which will not be included in formulae booklets.”）：
- Vectors：(x, y, z)·(a, b, c) = xa + yb + zc（列向量的 scalar product）
- 加上 P1–P3 的须记公式；7.5、7.7 的 guidance 另写明须知道距离公式与 cos∠AOB = a.b/(|a||b|)（见下）。

**公式册 P4 节给出**（公式册 p.5；“Candidates sitting Pure Mathematics P4 may also require those formulae listed under Pure Mathematics P1, P2 and P3.”）：
- Binomial series：(1 + x)ⁿ = 1 + nx + n(n − 1)x²/(1×2) + … + n(n − 1)…(n − r + 1)xʳ/(1×2×…×r) + …（|x| < 1，n ∈ ℝ）
- Integration (+ constant)：∫cosec x dx = −ln|cosec x + cot x|，或 ln|tan(½x)|；∫sec x dx = ln|sec x + tan x|，或 ln|tan(½x + ¼π)|
- Integration by parts：∫u (dv/dx) dx = uv − ∫v (du/dx) dx

注意：
- 公式册只给 (1 + x)ⁿ；考纲的 (ax + b)ⁿ 要先提出 bⁿ 化成 bⁿ(1 + (a/b)x)ⁿ 再套公式，有效范围由 |(a/b)x| < 1 得到（考纲 4.1 写作 |x| < b/a）。
- 分部积分公式在公式册；换元法、部分分式、可分离变量微分方程没有公式可查。
- 旋转体体积 V = π∫y² dx 不在公式册，也不在 P4 的须记清单里，但 6.1 写明 “is required”，实际必须会写。
- 评分惯例（WMA14 January 2024 MS，PDF p.6，General Principles for Pure Mathematics Marking）：用学过的公式时先写出公式；要求 exact 时改用小数通常失分。

## 3. 考纲条目（P4.3 Unit content）

### 1. Proof

**1.1 Proof by contradiction** — p.27
- 要求：“Including proof of the **irrationality of √2** and the **infinity of primes**, and application to **unfamiliar proofs**.”

### 2. Algebra and functions

**2.1 Decompose rational functions into partial fractions (denominators not more complicated than repeated linear terms)** — p.27
- 要求：分母可为 (ax + b)(cx + d)(ex + f) 与 (ax + b)(cx + d)²；“The degree of the numerator **may equal or exceed** the degree of the denominator.”（即 improper fraction，要先做除法）；应用于 integration、differentiation 与 series expansions。
- 排除：“Quadratic factors in the denominator such as (x² + a), a > 0, are **not** required.”

### 3. Coordinate geometry in the (x, y) plane

**3.1 Parametric equations of curves and conversion between cartesian and parametric forms** — p.27
- 要求：曲线的参数方程，参数式与 cartesian 式互化（guidance 空白）。

### 4. Binomial expansion

**4.1 Binomial series for any rational n** — p.27
- 要求：对 |x| < b/a，能求 (ax + b)ⁿ 的展开，以及通过 partial fractions 分解后展开有理函数。
- 公式：(1 + x)ⁿ（|x| < 1，n ∈ ℝ）在公式册（p.5）。

### 5. Differentiation

**5.1 Differentiation of simple functions defined implicitly or parametrically** — p.27
- 要求：“The finding of equations of **tangents and normals** to curves given parametrically or implicitly is required.”

**5.2 Formation of simple differential equations** — p.27
- 要求：“Questions involving **connected rates of change** may be set.”

### 6. Integration

**6.1 Evaluation of volume of revolution** — p.28
- 要求：“π∫y² dx is required, but **not** π∫x² dy.”（只考绕 x 轴旋转。）“Students should be able to find a volume of revolution, given **parametric equations**.”
- 排除：绕 y 轴的 π∫x² dy。

**6.2 Simple cases of integration by substitution and integration by parts. Understand these methods as the reverse processes of the chain and product rules respectively** — p.28
- 要求：能用换元求例如 ∫x√(x − 2) dx；“The substitution will be given in more complicated integrals.”；“The integral ∫ln x dx is required.”；“More than one application of integration by parts may be required”，例 ∫x²eˣ dx、∫eˣ sin x dx。
- 公式：分部积分公式在公式册（p.5）。

**6.3 Simple cases of integration using partial fractions** — p.28
- 要求：积分由部分分式产生的有理式，例 2/(3x + 5)、3/(x − 1)²；并注明其他有理式如 x/(x² + 5)、2/(2x − 1)⁴ 的积分 “is also required (see P3 section 5.2)”。

**6.4 Analytical solution of simple first order differential equations with separable variables** — p.28
- 要求：“**General and particular solutions** will be required.”

**6.5 Use integration to find the area under a curve given its parametric equations** — p.28（Issue 3 新增）
- 要求：能求参数方程给出的曲线下面积。
- 排除：“Students will **not** be expected to **sketch** a curve from its parametric equations.”

### 7. Vectors

**7.1 Vectors in two and three dimensions** — p.28
- 要求：二维与三维向量（guidance 空白）。

**7.2 Magnitude of a vector** — p.28
- 要求：能求 a 方向的 **unit vector**，熟悉 |a|。

**7.3 Algebraic operations of vector addition and multiplication by scalars, and their geometrical interpretations** — p.28
- 要求：向量加法、数乘及其几何意义（guidance 空白）。

**7.4 Position vectors** — p.28
- 要求：OB→ − OA→ = AB→ = b − a。

**7.5 The distance between two points** — p.29
- 要求：两点 (x₁, y₁, z₁)、(x₂, y₂, z₂) 的距离 d 满足 d² = (x₁ − x₂)² + (y₁ − y₂)² + (z₁ − z₂)²。
- 公式：不在公式册，须知道。

**7.6 Vector equations of lines** — p.29
- 要求：To include the forms **r = a + tb** and **r = c + t(d − c)**；“Conditions for two lines to be **parallel, intersecting or skew**.”

**7.7 The scalar product. Its use for calculating the angle between two lines** — p.29
- 要求：知道若 OA→ = a = a₁i + a₂j + a₃k，OB→ = b = b₁i + b₂j + b₃k，则 a.b = a₁b₁ + a₂b₂ + a₃b₃，且 cos∠AOB = a.b/(|a||b|)；知道若 a.b = 0 且 a、b 为非零向量，则 a 与 b **perpendicular**。
- 公式：scalar product 的分量式须记住（p.26）；夹角公式不在公式册，须知道。

## 4. 与相邻单元的界线

| 内容 | P4 做到哪里 | 属于哪个单元（考纲出处） |
|---|---|---|
| 证明 | proof by contradiction（1.1） | exhaustion 与 counter example 在 **P2 1.2–1.3**（p.18）；mathematical induction → **FP1 8.1**（p.35） |
| 部分分式 | 分母为不同一次因式或含重复一次因式，分子次数可 ≥ 分母（2.1）；不含二次因式 | 用部分分式做 method of differences 求和 → **FP2 2.1**（p.37） |
| 参数与曲线 | 一般参数方程、互化（3.1）、参数求导（5.1）、参数曲线下面积与体积（6.1、6.5）；不要求画参数曲线 | parabola (at², 2at)、rectangular hyperbola (ct, c/t) → **FP1 4.1–4.4**（p.33；FP1 4.4 写明 “Parametric differentiation is not required”）；ellipse、hyperbola → **FP3 2**（p.41） |
| 级数 | 任意有理 n 的 binomial series（4.1） | 正整数 n 在 **P2 4.5**；Maclaurin 与 Taylor series → **FP2 6**（p.38） |
| 求导 | implicit、parametric、connected rates of change（5.1–5.2） | dy/dx = 1/(dx/dy) 在 **P3 4.3**；hyperbolic 与反函数求导 → **FP3 3**（p.41） |
| 积分 | 换元（复杂情形给出代换）、分部（可多次）、部分分式、绕 x 轴的体积、参数面积（6.1–6.3、6.5） | 识别导数形式与三角恒等式变形在 **P3 5.2**；hyperbolic／三角换元、quadratic surds、reduction formulae、arc length、surface area of revolution → **FP3 4.3–4.6**（p.42） |
| 微分方程 | 建立简单微分方程（5.2）；可分离变量的一阶方程，通解与特解（6.4） | 进一步的可分离变量方程（含画解曲线族）、integrating factor 的一阶线性方程、二阶常系数方程、给定代换化简 → **FP2 4–5**（p.38） |
| 向量 | 二维与三维、模、单位向量、位置向量、两点距离、直线 r = a + tb、平行／相交／异面、scalar product 与夹角（7.1–7.7） | vector product、triple scalar product、直线 (r − a) × b = 0、平面 r.n = p 与 r = a + sb + tc、点到平面距离、两平面交线、异面直线最短距离 → **FP3 5.1–5.3**（p.42）；M1 只用二维向量（i、j，M1 2，p.45） |
| 被其他单元依赖 | — | FP2、FP3 先修 P1–P4 与 FP1（pp.36、40）；M2、M3 先修包括 P1–P4（pp.47、50），M2 1.3 用 P1–P4 的微积分处理变加速运动（p.48）；S2、S3 公式册注明可能用到 P1–P4 公式（公式册 pp.18、25） |

## 5. 往届真题

2018 考纲下 WMA14 的试卷、MS、ER 收集情况见 `../../inventory/pure.json` 与 `../../inventory/pure-gaps.md`。注意：`pure-gaps.md` 仍把 2020-10 至 2022-06 的 QP、MS 记为缺失，这 14 个文件后来在 GitHub `RayZ3R0/papernexus-finder` 找到，已放在 `registry/src/WMA14/`（见 `WMA14.coverage.part1.md` “New sources found in this pass”）。

逐题索引（合并版）：`WMA14.questions.json`（同一文件夹；由 `WMA14.questions.part1.json` 与 `part2.json` 合并、去重、排序，2026-10-06 审核，改正同步写回两个 part 文件）。各卷来源、缺失文件与审核记录见第 6 节、`WMA14.coverage.part1.md`、`WMA14.coverage.part2.md`。

## 6. 审核记录（2026-10-06）

本节与第 7 节中的路径都相对于 `registry/`。脚本在 `work/wma14audit/scripts/`，改正清单在 `work/wma14audit/fixes.json`（每条写明原值、证据和改动；改动前的 part 文件备份为 `work/wma14audit/part1.before.json`、`part2.before.json`）。

- **合并**：`WMA14.questions.json` = part1（76 题，2020-10 至 2022-10，含 2022-01 未用卷 `01U`）+ part2（120 题，2023-01 至 2026-06，含 /01A），按 id 去重（没有重复），按考季、卷别（01、01U、01A）、题号排序，共 196 题、425 个小问、1575 分。`merge_validate.py`：字段齐全、各小问分值之和等于题目总分、spec id 都在 `spec-items.pure.json` → WMA14 中、series 符合 YYYY-MM、id 与 paper 一致、每份卷 75 分且题号连续，0 个问题。`totals.py` 把每题总分和各小问分值与 QP 文本中印刷的 “(Total …)” 和 (n) 逐一比对（2026 年两份 /01A 的 PDF 后面附有答题册，只读到 “TOTAL FOR PAPER” 为止），21 份卷 0 个问题。`pagecheck.py`：条目中 264 处 “(MS p.n)”“(ER p.n)” 引用，所指页面都含该题。
- **完整性**：索引了 21 份卷，即所有能拿到 QP 文本的卷：`inventory/pure.json` 的 PDF 与 Edexcel-Finder 文本（2020-10 至 2025-01，含未用卷）、part 1 在 papernexus 补到的 2020-10 至 2022-06 的 14 个文件、Drive 上 2024-06 至 2026-06 的文件，对照 `versions.json` 的预期考季 2020-10 至 2026-06 没有漏卷。SAM 不是考季，按约定不收。**所有来源都拿不到的卷**：2025-10 /01A 和 2026-06 /01 的 QP 与 MS。这两份卷确实存在：第三方抓取的 Pearson 官方链接索引 `finder/gh/grademax_maths_index.json`（`ShariarAlamDipto/grademax` @9e091168）列出 `wma14-01a-que-20251029.pdf`、`wma14-01a-rms-20260122.pdf`、`wma14-01-que-20260610.pdf`、`wma14-01-rms-20260813.pdf`，都在 Pearson 的登录区。**缺 MS**：2026-01 /01、2026-01 /01A、2026-06 /01A（同一索引列出 `wma14-01-rms-20260305.pdf`、`wma14-01a-rms-20260305.pdf`、`wma14-01a-rms-20260813.pdf`），这 28 题的 `ms` 为空，也没有自行推算答案。**缺 ER**：2020-10、2021-01、2021-10、2022-01、2022-06，以及 2024-06 及以后的全部卷；2021-06 本来就没有 ER，未用卷没有考过。2026-10-06 复查：Drive 检索（2026 年以后创建、标题含 `WMA14`／`P4A`、全文含 `WMA14/01A` 或 `P78851A`；标题含 `26_06`、`25_10_QP`、`25_10_MS`、`26_01_MS`、`2606 WMA`、`2601 WMA`），没有新的 WMA14 文件（检索结果里的学生答卷只看了标题，没有打开）；`RayZ3R0/papernexus-finder` 的 HEAD 仍是 921bdf4f（2025-05-06），pure4 只到 2024 年 5 月。
- **准确性**：对照 QP、MS、ER 原文（文本层，加渲染图）逐条复核了 23 条，覆盖全部 21 份卷，题号和小问类型分散：O20 Q6、J21 Q9、S21 Q6、O21 Q10、J22 Q8、J22U Q4、S22 Q8、O22 Q7、J23 Q5、J23 Q8、S23 Q4、O23 Q3、J24 Q8、S24 Q5、O24 Q9、J25 Q6、S25 Q10、S25A Q3、O25 Q9、J26 Q5、J26A Q7、S26A Q4、S26A Q10。没有 MS 的三份 2026 卷文本层容易出错，在 J26A Q7 发现错误后，把 J26A 和 S26A 两份卷的全部 19 题与页面渲染图逐题对照过，没有别的错。另外按题意重新计算了 part 1 全部 8 份卷中约 100 个有数值或代数终点的小问，以及 part 2 中带根号、π 的约 25 个终点。在 J22 Q9(c) 发现错误后，J22 整份卷其余各题都重新算过，没有别的错。还做了三项全量检查：命令词是否出现在该题 QP 文本里（`cmdcheck.py`）、spec 映射的一致性、part 标签格式。
- **改正**（合并文件和两个 part 文件同步修改）：
  1. J22 Q9(c)：A 应为 √3/4，即 y = e^((√3/4)sec x − ½)。原条目写成 √3/2，是把 MS 中间一步 ln y = ½((√3/2)sec x − 1) 括号里的系数当成了最终答案。已用 MS p.24 渲染图和重新计算确认（代入 x = π/6 时 ln y = 0）。
  2. J26A Q7(c)：原 `ask` 说面积由法线下方的“三角形”加参数曲线下的面积组成。实际上法线 y = x + 7/2 与 y 轴交在 (0, 7/2)，0 ≤ x ≤ 1 这一段是梯形，面积 4，正是题目印的 “4 +”。已改为 trapezium。`WMA14.coverage.part2.md` §4 的相同说法也已改正。
  3. spec 映射：S23 Q8(d)、O23 Q8(d)、J26 Q9(a) 是参数方程的**体积**，原标 6.1 + 6.5。6.5 只管参数曲线下的**面积**，参数体积已写在 6.1 里（考纲 p.28）。改为 6.1 + 3.1，与 part 1 的 J21 Q9(a)、J22U Q9(a) 一致；`coverage.part2.md` §4 中 3.1、5.1、6.5 三行已重新统计。
  4. spec 映射：J24 Q8（证明曲线没有驻点）去掉 5.1。题中的求导是显函数求导（P3 内容），按 part 1 的映射规则归入它服务的 1.1。
  5. S22 Q8(c)：`final_form` 原写 “3 s.f. with units”。MS p.15 把单位放在括号里（awrt 3.99 (g/cm³)），即不强制写单位。
  6. 格式：O20 Q7、S21 Q9、O22 Q7 的 part 标签由 “(i)”“(ii)” 改为 “i”“ii”，与索引格式和其他单元一致。
  7. 命令词统一：J22 Q6、S22 Q9、J22U Q6 原为 “Use”，S25 Q10、S25A Q10 原为 “Prove”；这几题印的都是 “Use … to show that”，统一记为 “Show that”（part 2 本来就这样记）。J23 Q9(a) 印的是 “Show the calculations and statements…”，由 “Show that” 改为 “Show”，与 O22 Q8 一致。
- **抽查中没有发现**分值、题目总分、MS 页码或 ER 内容的错误。
- **保留未改的差异**：part 1 用 Unicode 记号（√、π、≤）并在 `ms` 后注 MS 页码；part 2 用 ASCII（sqrt、pi、<=），不注页码（按题号在 MS 中定位）。两种写法读者都能看懂，没有统一。P1–P3 的内容按它在题中服务的 P4 条目打标签（例如参数函数的值域记 3.1），见 `WMA14.coverage.part1.md` “Mapping notes”。`inventory/pure-gaps.md` 中关于 WMA14 2020-10 至 2022-06 的“missing”记录应由 inventory 的维护者更新，本次没有改动。

## 7. 真题需求概览

**数据范围**：2018 考纲下能拿到题面的全部 21 份卷：2020-10 至 2026-01 每个考季的 /01，加 2022-01 未用卷（J22U，Pearson 公布了 QP 与 MS，没有考过）、2025-06 /01A、2026-01 /01A、2026-06 /01A。共 196 题、425 个小问、1575 分。18 份有 MS（2026 年三份没有）；有 ER 的只有 O22、J23、S23、O23、J24 五份。缺的两份卷（2025-10 /01A、2026-06 /01）见第 6 节。下面的数字由脚本从索引统计（`work/wma14audit/scripts/stats.py`、`banners.py`，结果在 `work/wma14audit/stats.json`）。“问法、终点、评分”来自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节抽查过。

**引用写法**：J = January，S = June，O = October，后接两位年份；A = /01A，U = 2022-01 未用卷；题号与小问照试卷印刷。MS、ER 页码：part 1 的条目在 `ms`、`er` 字段末尾注明；part 2 的条目只注 ER 页码，MS 按题号定位。

### 7.1 卷面结构

- 每卷 75 分、8–11 题（9 题 11 份，10 题 7 份，8 题 2 份，11 题 1 份），单题 2–16 分，最常见 6–10 分。分值最大的题通常是参数曲线综合题：求导、切线或法线，再求面积或体积（O23 Q8 14 分，O25 Q9 15 分，J26A Q7 16 分）。
- **每份卷都有、且一般只有一题**：二项展开（4.1，13 份卷放在 Q1）、反证法（1.1，7 份卷放在最后一题）、旋转体体积（6.1）、可分离变量的微分方程（6.4，只有 O21 出了两题）、三维直线向量（7.6 与 7.7，每卷 1–2 题）。隐函数或参数求导（5.1）每卷约 2 题，积分方法（6.2）每卷约 2 题，它们分值最多：涉及 5.1 的小问合计 283 分，涉及 6.2 的 279 分，各约占全部分值的 18%。
- 命令词（425 个小问）：Find 242，Show that 94，Hence find 20，Prove 18，State 12，Use 6，Write down 5，Express 5，其余各 1–4 次。约四分之一的小问是 “Show that”，要给出到印刷结果为止的完整步骤。
- **禁用计算器的说明**（“Solutions relying (entirely) on calculator technology are not acceptable” 或 “show all stages of your working”，按 QP 文本统计）：2020–2022 年 8 份卷共 15 题（每卷 0–4 题），2023–2024 年 6 份卷共 9 题，2025–2026 年 7 份卷共 26 题（每卷 2–5 题）。近两年明显增多。

### 7.2 每个考纲条目怎么考

“卷数／题数／小问／涉及分值”：一个小问可以带几个条目标签，所以各行相加大于 196 题、1575 分。“典型分值”是带该标签的小问最常见的分值。

| 条目 | 卷数／题数／小问／涉及分值 | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 反证法 | 21／21／27／96 | Prove 16，Show that 5，Complete 2，Show 2 | 从来不考 √2 或质数无穷多的原文证明，题目都是新的命题：① 奇偶或整除（n³ 偶则 n 偶；n² 是 3 的倍数；n² − 2 不被 4 整除；n² − 4n + 5 偶则 n 奇）；② 无理数（∛2、∛3、√7）；③ 因式分解后列举因数对，证明没有整数解（3x² + 2xy − y² = 25；a² − 4b = 27；x² − 4y² = 27；4p² − q² = 46）；④ 不等式（9x/y + y/x ≥ 6；k + 9/k ≥ 6，再举反例）；⑤ 两条曲线不相交，曲线没有驻点；⑥ 补全学生写了一半的证明（4 次） | 假设（命题的否定）+ 推出矛盾的理由 + 结论，三者缺一不可；多为 4 分（15 次），补全证明 1–3 分 | O21 Q10，O22 Q8，J23 Q9，O23 Q4，J24 Q8，O24 Q2，J25 Q6，S25 Q10，O25 Q10，J26A Q8 |
| 2.1 部分分式 | 21／22／27／111 | Find 10，Express 5，Write 4，Show that 4 | 两个不同的一次因式最常见；三个一次因式（S25 Q4）；重复一次因式 3 次（J22U Q4，J24 Q2，S25A Q7(b)）；分子次数 ≥ 分母、要先除的 5 次（O20 Q7(ii)，O21 Q3，O24 Q7(a)，J26A Q4，S26A Q2）。之后接着积分（6.3），或解微分方程、求参数面积；用来求导（O21 Q3(b)）和展开成级数（J23 Q1(b)）各只 1 次 | 写出各常数或整个分式；单独考时 2–4 分（3 分最多） | J22U Q4(a)，J24 Q2(a)，O24 Q7(a)，S25 Q4(a)，S26A Q2(a) |
| 3.1 参数方程 | 21／26／42／135 | Find 17，Show that 17，State 4 | ① 化成指定形式的直角坐标方程，求整数常数：y = (ax + b)/(cx + d)（J21、O22、O25、S26A），y = √(ax + b)，y = a(x + b)² + c，直线（J23 Q2），x³ − 2xy³ − y⁴ = 0，不含三角函数的方程（S25A Q6(c)）；② 由参数区间求 f 的定义域、值域（J21 Q4(b)，S21 Q6(c)，O21 Q5(c)，O22 Q6(b)(c)，O25 Q3(b)，J26 Q5(d)）；③ 求点的坐标或参数值；④ 切线或法线再与曲线相交，求另一交点（O20 Q4(c)，S22 Q7(c)(d)，J25 Q9(b)，S26A Q6(c)） | 带整数常数的指定形式；值域写成关于 f 或 y 的不等式（写成 x 不给分）；每小问 1–4 分 | J21 Q4，S21 Q6，O22 Q6，O25 Q3，J26 Q5，S26A Q4(a) |
| 4.1 二项级数 | 21／21／53／148 | Find 32，State 6，Use 5，Show that 4 | 先提出常数，展开 (a + bx)ⁿ，n 为负数或分数，求前 3–4 项；求有效范围 \|x\| < a/b（7 次）；用展开式近似根式，给分数或指定位数（8 次：√5，√1.15，√3 两次，∛31，√7，∛6，√135）；由已知系数反求常数（O20 Q2，S21 Q1，S22 Q1，S24 Q8(a)，J25 Q3，J26 Q1）；对已有展开式做变换：x 换成 −x、x/5，两式相乘或相加，乘常数（S23 Q1，S25 Q8，S25A Q4，O25 Q1(c)，J26A Q1）；按 x² 或 x³ 展开（O21、J22、O22） | 系数化成最简分数；展开 4–5 分，范围 1 分，近似 2–3 分 | O20 Q2，O22 Q4，S23 Q1，J25 Q3，S25 Q8，J26 Q1，J26A Q1 |
| 5.1 隐函数与参数求导 | 21／37／66／283 | Find 49，Show that 13 | 隐函数求 dy/dx（用 x、y 表示，4–6 分），常含 aˣ（S23 Q2 的 2ˣ，O24 Q4 的 8ˣ，J25 Q2 的 10·2ˣ）、e^(xy) 或 e^(−2x)、乘积项；参数求导，常要化成 k·cosec t、k sin t 之类；在给定点求切线或法线；由条件求点或常数：驻点（S22 Q4，J24 Q3）、最北和最南的点（O22 Q11）、竖直切线（J23 Q5(b)）、已知斜率（O23 Q5(b)，O25 Q4(b)，O25 Q9(a)，J26A Q2）；取对数求导（O20 Q6） | 直线方程写成 ax + by + c = 0（整数，7 次）或 y = mx + c（7 次）；精确的斜率或坐标；每小问多为 3–6 分 | O21 Q1，J23 Q5，S24 Q3，O24 Q4，J25 Q9，S25 Q1，O25 Q9(a)，J26A Q2 |
| 5.2 建立微分方程、相关变化率 | 16／16／27／88（缺 O20、J21、S23、O25、J26A） | Find 16，Show that 10 | 全是几何情境：球（气球、冰球）、立方体、圆锥、圆柱、碗、正二十面体、弓形；先写几何公式，再用链式法则求某一时刻的变化率；由“与 r² 成反比”“流入减流出”建立微分方程（O21 Q9(a)，J22U Q7，O22 Q10(a)，S25 Q2，J26 Q8(a)） | 带单位的变化率，3 s.f.／2 s.f. 或精确值；求导、代入共 3–4 分 | S21 Q3，J22 Q4，O23 Q2，J24 Q4，S24 Q4，O24 Q5，S26A Q3 |
| 6.1 旋转体体积（绕 x 轴） | 21／21／29／136 | Find 17，Show that 10 | 直角坐标 16 题，参数方程 5 题（J21 Q9，J22U Q9，S23 Q8(d)，O23 Q8(d)，J26 Q9）；常先 “show V = k∫…”，再 “hence” 求精确值；由体积反求积分上限（O22 Q5）；情境：门把手、哑铃求密度、镇纸、花瓶水深（J22 Q7，S22 Q8，S25 Q9，S25A Q9）；组合体：圆柱减去曲线部分（S21 Q2），圆锥加曲线部分（S23 Q8(d)） | π(p + q ln 2)、a ln b、π(pπ³ + qπ + r) 等精确形式；每小问 3–7 分 | O20 Q3，J21 Q9，O22 Q5，J23 Q3，O24 Q7(b)，S25A Q9，S26A Q8 |
| 6.2 换元积分与分部积分 | 21／44／58／279 | Find 32，Show that 19，Hence find 4 | **分部**：x²e^(kx)、x² cos 2x 要用两次（S22 Q8(b)，S23 Q5(i)，O23 Q3(i)，J24 Q5(a)，J25 Q5(i)）；eˣ 乘三角函数，两次分部后移项（J21 Q7，J22U Q6，O22 Q7(ii)，S25 Q9(b)）；含 ln 的式子（O20 Q5，O21 Q8(a)，S25A Q1，J26 Q2）。**换元**：除 O20 Q7(i) 外都给出代换，常见 u = √(2x − 1)、u = eˣ − 3、x = 2 sin u、x = 4 sin θ、u = tan x、u = 3 + cos θ、u = √(x³ + 1) | a + b ln 2、a + ln b、a√3 + b 等精确形式，或 “show” 一个给定的原函数形式求 A、B；不定积分要写 + c；每小问 4–5 分为主 | O22 Q7，O23 Q3，O24 Q6，J25 Q7，S25 Q7，O25 Q6，J26A Q6 |
| 6.3 用部分分式积分 | 18／19／21／113（缺 O21、J22、J23） | Find 11，Show that 6，Hence show that 2 | 接着 2.1 做定积分，化成 ln k、p ln q + r、a + ln b、P ln 2 + Q ln 3；不定积分；由积分值反求下限 k（S23 Q3(c)）；嵌在微分方程、参数面积、体积里 | 精确的对数形式；最常见 6 分（8 次） | O22 Q2(b)，J24 Q2(b)，S25 Q4(b)，S25A Q7(c)，J26 Q4(b) |
| 6.4 可分离变量的微分方程 | 21／22／43／169 | Find 20，Show that 11，Hence find 5，Solve 3 | 几乎都是情境题的特解：细菌、水深、发动机温度、山羊数量、电流、游乐设施、洞穴水位、容器、气球、灌木、冷饮；多为 “solve to show” 给定形式并求常数（5–7 分）；之后求到达某值的时间（取整到秒或分，或 1 d.p.），求长期极限值（O20 Q9(b)，J21 Q10(d)，S21 Q8(b)，J23 Q7(b)，O23 Q7，S24 Q7(b)，O25 Q8(b)，J26A Q3(b)）；答案写成 y² = g(x)、yⁿ = f(t)（S21 Q8，J24 Q5(b)，S25 Q3，S25A Q3）；只求通解 2 次（J22 Q9(b)，J22U Q7(a)） | 给定形式与常数；时间、温度等带单位，按题目取整；后续小问多为 2 分 | O20 Q9，J21 Q10，S23 Q6，O23 Q7，O24 Q9，J25 Q4(ii)，S26A Q9 |
| 6.5 参数曲线下的面积（Issue 3 新增） | 8／8／12／59（S21，J22，J23，S24，O24，O25，J26A，S26A） | Show that 5，Find 5 | 先 “show area = k∫…dt”：写出 ∫y(dx/dt)dt，把 x 的上下限换成 t，用二倍角化简；再 “hence” 求精确面积；常与法线下方的三角形（J23 Q8(b)，S26A Q10(b)）、梯形（J26A Q7(c)）或矩形（S24 Q5(b)）组合 | 给定积分式（求 k、a、b），再求精确值；每小问 3–6 分，O25 Q9(b) 一小问 9 分 | S21 Q6(a)，J22 Q5，S24 Q5，O24 Q10，O25 Q9(b)，S26A Q10(b) |
| 7.1 二维与三维向量 | 1／1／1／2 | — | 从来不是考点本身；所有向量题都是三维，没有出过二维向量题 | — | S21 Q7(a)（附带） |
| 7.2 模与单位向量 | 12／12／17／53 | Find 14 | 单位向量只考过 1 次（S21 Q7(a)）；更多是用 ½\|a\|\|b\| sin θ 求三角形或平行四边形面积（J21 Q2(b)，S22 Q6(c)，O23 Q6(c)，S24 Q6(c)，S25A Q8(c)，O25 Q7(b)，J26A Q9(c)），以及已知 \|OA\| 列方程（S24 Q6(a)） | 最简根式或指定精度；多为 3 分 | S21 Q7(a)，S24 Q6，O25 Q7(b) |
| 7.3 向量加法、数乘及几何意义 | 7／7／8／21 | Find 7 | 点关于直线的对称点（O21 Q7(b)，S23 Q4(c)）、平行四边形的第四个顶点（J26A Q9(a)）、共线比例 c = 3b − 2a（S21 Q9(i)）、两点间的向量（O22 Q3(a)）、利用面积比确定点的位置（J25 Q8(d)） | 向量或坐标；2–3 分 | S21 Q9(i)，S23 Q4(c)，J26A Q9 |
| 7.4 位置向量 | 15／15／18／50 | Find 13 | AB = b − a，常是写直线方程的第一步 | 向量（不能写成坐标）；2 分为主 | O22 Q3(a)，J23 Q6(a)，S25A Q8(a) |
| 7.5 两点间距离 | 7／7／7／19 | Find 6 | 点到直线的最短距离（O21 Q7(a)(ii) 写成 √d）、\|PP′\|（S23 Q4(d)）、直线上与某点距离为 35 的点（J22U Q5(c)）、精确长度（O24 Q8(d)） | 最简根式；2–3 分 | O21 Q7，S23 Q4(d)，J22U Q5(c) |
| 7.6 直线的向量方程 | 21／21／36／130 | Find 27，Show that 4，Prove 2，Write down 2 | 过两点的直线（以 “r =” 开头，2 分）；两直线相交，求未知常数和交点（J24 Q6，O24 Q8，O25 Q5，J26 Q6，J26A Q5）；证明两直线异面或不相交（J21 Q8，J22 Q8(b)，O22 Q9）；直线上满足某条件的点（S24 Q6，J25 Q8，S26A Q7(b)） | r = a + λd；交点的坐标或位置向量；每小问 2–5 分 | J21 Q8，J22 Q8，O22 Q9，J24 Q6，O25 Q5，J26A Q5 |
| 7.7 数量积与夹角 | 21／23／31／116 | Find 30 | 两直线或两向量的夹角（角度取 1 或 2 位小数，或精确的 cos θ）；点在直线上的垂足，含原点到直线的垂足（O20 Q8(b)，S21 Q7(b)，O21 Q7(a)，J23 Q6(b)，S23 Q4(b)，J24 Q6(d)，J26 Q6(a)，S26A Q7(d)）；由垂直或 45° 夹角求未知数（S22 Q6(b)，S24 Q2(b)，S25 Q6(b)，S25A Q8(b)，J26A Q5） | 锐角，角度制；坐标、精确值；多为 3–5 分 | J22 Q8(c)，S23 Q4，J24 Q6，O24 Q8，S25 Q6(b)，S26A Q7 |

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据：21 份卷的索引检索，加 QP 文本检索（`work/wma14audit/scripts/` 中的检索脚本）。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 √2 无理与质数无穷多的原文证明 | 从未原题出现。考过的无理数证明是 ∛2（O21）、∛3（J23）、√7（S23），都先给出或先证 “n² 是 k 的倍数则 n 是 k 的倍数” 一类的引理 | 两个原文证明做成结构卡（假设、推导、矛盾、结论），重点练“引理 + 无理数”的组合 |
| 2.1 部分分式用于求导和级数展开 | 求导只有 O21 Q3(b)(c)，展开只有 J23 Q1(b) | 各一张卡即可 |
| 3.1 不要求画参数曲线 | 考纲明确排除；索引中唯一的 Sketch 是微分方程解的图像（O22 Q10(c)） | 不必练画参数曲线 |
| 4.1 有理函数先拆部分分式再展开 | 只有 J23 Q1(b)（ER：有效范围要取两个区间中较窄的那个） | 一张卡 |
| 6.1 π∫x² dy（绕 y 轴） | 考纲排除，从未出现 | 不做 |
| 6.2 单独的 ∫ln x dx；“换元、分部是链式法则、乘积法则的逆运算”的说明 | ∫ln x dx 没有单独考过，出现的都是 xⁿ ln x、ln x/x² 一类；“逆运算”从未作为问题出现 | ∫ln x dx 做一张推导卡；“逆运算”不必单独做卡 |
| 6.2 题目不给代换 | 只有 O20 Q7(i)（“a suitable substitution”），其余都给出代换 | 一张卡：u = 根号里的式子 |
| 公式册的 ∫sec x dx、∫cosec x dx | 21 份卷都没有用到 | 不必背推导，会查公式册即可 |
| 6.4 只求通解 | 只有 J22 Q9(b)、J22U Q7(a)；其余都要特解 | 重点练“先 + c，再代初值” |
| 7.1 二维向量 | 从未出题，所有向量题都是三维 | 不必单独做二维卡 |
| 7.2 单位向量 | 只考过 1 次（S21 Q7(a)） | 一张卡 |
| 7.6 两直线平行的判定 | 只作为“不平行”的理由出现在异面直线证明里（J21 Q8，O22 Q9），以及 S24 Q6(c) 的“过 O 且与 l₁ 平行” | 和异面直线的三步证明放在一起做卡 |
| 5.2 S23、O25、J26A、O20、J21 没有相关变化率题 | 21 份卷中 16 份有 | 仍是高频，照常练 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 O22、J23、S23、O23、J24 五份；没有标 ER 的条目来自 MS 的评分说明。part 1 的 MS 页码见 `WMA14.coverage.part1.md` “Recurring examiner warnings”，part 2 的出处见 `WMA14.coverage.part2.md` §5。下面引用的 MS 原文都在本次审核中核对过原文件。

1. **禁用计算器的题只写答案得 0 分**。O20 Q7(i)（MS：16 without working scores no marks）；O24 Q9(c)（没有过程 M0A0；不用 (b) 的解、只由微分方程得 cos(t/10) = 0，也是 M0A0）；O24 Q2（x² 的二次方程必须用非计算器方法解）。但 MS 允许在列出“三项二次方程、所有项移到一边”之后用计算器解它（O25 Q4(b)，O25 Q9(a)）。
2. **给定答案（A1\*）要每一步都写出来**。至少有一行中间步骤，倒推不得分：O20 Q4(a)(b)（“= 0 must be seen”），J21 Q7(b)，S21 Q6(a)(i)（dt 和交换上下限去掉负号都要写出），O22 Q11(a)（MS：只靠倒推最多得 B1；ER：这题是为 (b) 铺路的 show that，所有步骤都要写出），J24 Q7(a)（ER：没有写出 u 的积分和新上下限，丢最后两分），J23 Q2(a)（ER：最常丢的是结论 “so it is linear”）。
3. **反证法**：开头写出命题的否定（“for all k” 或只考虑负的 k 都是错误的假设，O23 Q4(a) ER）；每种情形都要做，例如两组因数对（O22 Q8 ER：多数人只做一种情形）和 3k + 1、3k + 2（J23 Q9 ER：40% 以上 0 分）；矛盾要有理由，只写 “no solutions” 不给分，要用 |sin x| ≤ 1 和 3x² + 2 ≥ 2 这样的事实（J24 Q8 ER，MS 写明草图不算证明）；结论要同时提到矛盾和原命题。无理数证明要在假设里写 “p/q in simplest form”，蕴含方向要对（O21 Q10(b) MS）。J25 Q6 MS：假设必须用文字写出，B0M1A1A1 这样的得分组合不存在。
4. **二项展开**：提出的常数要对，例如 4^(−½)，不是 4 或 4^½（O22 Q4 ER）；括号内项的符号要保留，例如 (1 − 4x)⁻³ 不能当作 x 或 4x 展开（J24 Q1 ER）；有效范围是 |x| < b/a（O23 Q1(b) ER：这一问答得很差）；两个级数组合时取较窄的区间（J23 Q1(b)(ii) ER）；近似值必须由展开式算出，按要求写成分数或指定位数，4 位小数的值 cao（O21 Q4(b) MS：1.7324，不是计算器的 1.7321）；MS 不接受直接写 nCr 而 n 不是整数的写法（S25A Q4(a)、O25 Q1(a) MS）。
5. **∫1/(ax + b) dx = (1/a) ln|ax + b|**，最常丢的是 1/a：O22 Q2(b) ER，S23 Q3(b) ER（写 ln(2x − 1) 的人和写对 ½ ln(2x − 1) 的人一样多），J24 Q2(b) ER。ln 的括号或绝对值要写（O22 MS）。
6. **换元积分**：dx 要整个换掉（“the dx CANNOT just be replaced by du”，S21 Q4 MS），常数和幂都不能丢（O22 Q7(i) MS：没有 4 不给 A 分）；用 u 的上下限，不要用 x 的上下限（O22 Q7(i) ER：用了 ln 7、ln 5 而不是 4、2）；题目要求换元就必须换元，用分部或部分分式最多 4/7（O23 Q3(ii) ER）。
7. **分部积分**：x²e^(kx) 类要用两次，符号和系数最容易错，e⁰ 当成 0 也常见（O23 Q3(i) ER）；eˣ 乘三角函数要把两次出现的同一积分移到一边合并，完全做对的人不多（O22 Q7(ii) ER）；不定积分要写 + c（O20 Q7(ii) MS：“The +c is required”；有些 MS 写 (+c)，即不强制，如 S22 Q8(b)）。
8. **旋转体体积**：y 要平方，π 要从一开始就写，不能最后补上；参数形式要用 π∫y²(dx/dt)dt，上下限换成 t 的值：J23 Q3 ER（没有平方是 0 分的主要原因），S23 Q8(d) ER（漏掉一部分体积；把 (t − 1/t)² 算成 t² − 1/t²；漏 dx/dt；t 的积分用了 x 的上下限），O23 Q8(d)(i) ER（漏 dx/dt；上限错写成 3π），S25A Q9(a) MS（2π × 144 得 B0）。
9. **微分方程**：先积分并写上 + c，再代初值；漏 + c 无法补救（S23 Q6 ER：“a critical error from which there was no recovery”；O23 Q7(d) ER；J24 Q5(b) ER）；变形时两边整体取倒数或平方，不能逐项取倒数，之后也不 isw（O21 Q2 MS）；比例关系要写出常数，例如 dr/dt = −k/r²（O22 Q10 ER）；情境中的单位要按题目处理：x 以千为单位时，答 4050 只而不是 4.05（O23 Q7 ER）。
10. **隐函数与参数求导**：dy/dx 只能从两项中提出（J25 Q2(a) MS）；aˣ 的导数是 aˣ ln a，xy 项用乘积法则，常数项求导后要消失（S23 Q2(b)、O23 Q5(a)、J24 Q3(a) ER）；竖直切线是分母为 0，不是分子（J23 Q5(b) ER）；代入的必须是题目给的点，代 (0, 0) 是 M0（J21 Q6(b) MS）；问法线不要求成切线（S23 Q8(c) ER）；点的坐标保持精确（O23 Q8(c) ER）。
11. **参数方程的值域**：两个参数端点和区间内的极值点都要检查（O22 Q6(c) ER：最大值在 t = 0，不在 t = π/3）；值域写成关于 f 或 y 的式子，写成 x 不给分（S21 Q6(c) MS：0 ≤ x ≤ 4 不接受）。
12. **向量**：直线方程以 “r =” 开头，写 “l =” 得 A0（S23 Q4(a) ER，J22 Q8(a) MS）；问向量就答向量，写坐标不给分（O22 Q3(a) MS，S21 Q7(a) MS）；夹角用方向向量，答锐角（J24 Q6(c) ER；O25 Q7(a) MS：用 AB·BC = −45 得到负的余弦，只给 M1dM1A0）；求垂足时用 “(到直线上一般点的向量)·(方向向量) = 0”，不能用 OC 代替 PC（S23 Q4(b) ER）；异面直线证明要写出不相交和不平行两部分，并给出“不平行”的理由（O22 Q9 MS 与 ER）；建议先画草图（S23 Q4 ER）。
13. **相关变化率**：先写几何公式，例如 S = 6x²、l = √(25 + r²)、r = (2/5)h，再用链式法则（O23 Q2 ER：常见 S = x²；J24 Q4 ER：把 l 当常数；J23 Q7(d) ER：没认出是链式法则，单位漏写）。
14. **精确值与精度**：要求精确就不能写小数（O20 Q3 MS：上限 2 ln 2，“Do not accept 1.386”；O20 Q4(c) MS：x = −40/49，“Do not accept decimals”）；按题目要求的形式给答案（J23 Q3 ER：要写 π ln 2，(π/2) ln 4 不符合 “a ln b, b prime”）；角度题用角度（J21 Q2 MS），积分里的上下限用弧度（J21 Q9(b) MS：用 π/3，不用 60°）。
