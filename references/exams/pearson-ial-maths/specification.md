# Pearson Edexcel IAL Mathematics / Further Mathematics / Pure Mathematics（2018）规格书共用部分

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用`units/<单元>.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py <单元> --gaps` 输出为准（快照 2026-10-06）**。

单元条目见 `units/<代码>.md`（纯数 P1–P4 由本次写入：`units/WMA11.md`–`units/WMA14.md`）；考纲条目目录见 `spec-items.*.json`；版本与考季核查见 `../versions.md`。登记日期 2026-10-06。

## 0. 来源与核验

| 代号 | 文件 | 版本标识 | 本地路径与校验 |
|---|---|---|---|
| SPEC | *Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics Specification* | **Issue 3 – April 2019**（每页页脚）；ISBN **978 1 446 94981 8**；First teaching September 2018；First examination from January 2019；First certification August 2019（IAS）、August 2020（IAL） | `scratchpad/research/dl/ial-maths-spec.pdf`，99 页，md5 `06d01a11b53e1e03d25a0df0a265510d`；逐页文本 `registry/work/pure-spec/clean/pNNN.txt`（PDF 页号）。**印刷页 = PDF 页 − 6** |
| FB | *Mathematical Formulae and Statistical Tables*（试卷封面称 “Yellow”） | **Issue 2 – January 2021**；First examination from January 2019；P59773RA；ISBN 978 1 4469 4983 2 | `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，34 页，md5 `a1c61b665dcae1af155e289c78b74019`；文本 `registry/src/fb/fb.txt`。印刷页 = PDF 页 − 6（例：P1–P2 节印刷 p.3 = PDF p.9） |

- 与 `../versions.md` §1.1–1.3 一致：Issue 3 是当前版本，没有找到更新的 IAL 数学考纲或公式册（该文件 §1.2 记录的是否定性检索结果，Pearson 官网本环境无法访问）。
- **不要与 2013 旧考纲混淆**：旧 IAL 数学考纲也叫 “Issue 3”。核对 ISBN 978 1 446 94981 8 与首考 January 2019。
- **Issue 3 相对 Issue 2 的改动**（SPEC PDF p.3）：(1) P3 “Notation and formulae” 的积分表中 ∫aˣ dx 改为 aˣ/ln a + c（印刷 p.22）；(2) P4 新增 6.5 “Use integration to find the area under a curve given its parametric equations”，并注明不要求画参数曲线（印刷 p.28）。
- **FB Issue 2 的改动**（FB PDF p.3）：删去 FP1 节 “In FP1, θ will be a multiple of 45°”；更正 FP3 椭圆标准式为 x²/a² + y²/b² = 1；更正 FP3 积分表第 6–9 行（arcosh、arsinh、artanh 形式）；M1 节注明可能用到 P1 **和 P2** 公式；S1 节新增可能用到 P1、P2 公式；更正 S1 的 r 公式；S3 节注明可能用到 S1、S2 及 P1–P4 公式；更正 S3 两样本均值差的抽样分布；随机数表间距调整。
- 本文件的页码均为印刷页（“p.”）；公式册页码写作“FB p.”。

## 1. 资格结构（Qualification at a glance，pp.6–10）

- 一份考纲包含三个资格：IAS/IAL in **Mathematics**、**Further Mathematics**、**Pure Mathematics**。均为 **modular** qualifications（p.1）；课程可按单元分阶段教学与考试，也可作为 linear course 在最后一次考完（p.6）。
- “A variety of 14 equally weighted units”（p.1）；IAS 由 3 个单元组成，IAL 由 6 个单元组成（p.10；p.67）。
- 旧考纲沿革（p.1）：Decision Mathematics 1 已更新；“The Further, Mechanics and Statistics units have not changed.” 纯数改为四个 Pure Mathematics 单元（P1–P4，新代码 WMA11–14）。FP、M、S 沿用旧代码，旧考纲试卷不计入 2018 考纲范围，界线见 `../versions.md` §1.4。

### 1.1 单元总表（pp.7–9；IAS／IA2 归属见 p.67；单元起始页见 p.11）

| 单元 | 代码 | IAS/IA2 | 考季 | 考纲首考 | IAS 权重 | IAL 权重 | 内容概要（考纲原词） | 单元起始页 |
|---|---|---|---|---|---|---|---|---|
| P1 | WMA11/01 | IAS | Jan, Jun, Oct | January 2019 | 33⅓% | 16⅔% | Algebra and functions; coordinate geometry; trigonometry; differentiation; integration | p.12 |
| P2 | WMA12/01 | IAS | Jan, Jun, Oct | June 2019 | 33⅓% | 16⅔% | Proof; algebra and functions; coordinate geometry; sequences and series; exponentials and logarithms; trigonometry; differentiation; integration | p.17 |
| P3 | WMA13/01 | IA2 | Jan, Jun, Oct | January 2020 | N/A | 16⅔% | Algebra and functions; trigonometry; exponentials and logarithms; differentiation; integration; numerical methods | p.21 |
| P4 | WMA14/01 | IA2 | Jan, Jun, Oct | June 2020 | N/A | 16⅔% | Proof; algebra and functions; coordinate geometry; binomial expansion; differentiation; integration; vectors | p.26 |
| FP1 | WFM01/01 | IAS | Jan, Jun | June 2019 | 33⅓% | 16⅔% | Complex numbers; roots of quadratic equations; numerical solution of equations; coordinate systems; matrix algebra; transformations using matrices; series; proof | p.30 |
| FP2 | WFM02/01 | IA2 | Jan, Jun | June 2020 | 33⅓% | 16⅔% | Inequalities; series; further complex numbers; first and second order differential equations; Maclaurin and Taylor series; polar coordinates | p.36 |
| FP3 | WFM03/01 | IA2 | Jan, Jun | June 2020 | 33⅓% | 16⅔% | Hyperbolic functions; further coordinate systems; differentiation; integration; vectors; further matrix algebra | p.40 |
| M1 | WME01/01 | IAS | Jan, Jun, Oct | June 2019 | 33⅓% | 16⅔% | Mathematical models in mechanics; vectors in mechanics; kinematics; dynamics; statics of a particle; moments | p.44 |
| M2 | WME02/01 | IA2 | Jan, Jun, Oct | June 2020 | 33⅓% | 16⅔% | Kinematics in a line or plane; centres of mass; work and energy; collisions; statics of rigid bodies | p.47 |
| M3 | WME03/01 | IA2 | Jan, Jun | June 2020 | 33⅓% | 16⅔% | Further kinematics; elastic strings and springs; further dynamics; motion in a circle; statics of rigid bodies | p.50 |
| S1 | WST01/01 | IAS | Jan, Jun, Oct | June 2019 | 33⅓% | 16⅔% | Mathematical models; representation and summary of data; probability; correlation and regression; discrete random variables and distributions; the Normal distribution | p.53 |
| S2 | WST02/01 | IA2 | Jan, Jun, Oct | June 2020 | 33⅓% | 16⅔% | Binomial and Poisson distributions; continuous random variables and distributions; samples; hypothesis tests | p.57 |
| S3 | WST03/01 | IA2 | Jan, Jun | June 2020 | 33⅓% | 16⅔% | Combinations of random variables; sampling; estimation, confidence intervals and tests; goodness of fit and contingency tables; regression and correlation | p.60 |
| D1 | WDM11/01 | IAS | Jan, Jun | June 2019 | 33⅓% | 16⅔% | Algorithms; algorithms on graphs; algorithms on graphs II; critical path analysis; linear programming | p.63 |

- IA2 单元中 FP2、FP3、M2、M3、S2、S3 的 IAS 权重仍写 33⅓%，因为它们可作 IAS Further Mathematics 的选修单元（p.10）；P3、P4 的 IAS 权重为 N/A（p.7）。
- 考季（p.70）：June 2020 之前各单元的开考季见 `../versions.md` §1.4；从 June 2020 起，**all** units 每年 January 与 June 开考，October 则 “**just** units P1, P2, P3, P4, M1, M2, S1 and S2”，“for the lifetime of the qualifications”。 资格颁发同样从 June 2020 起每年 1、6、10 月。
- 实际考季的例外（June 2020 全球取消、October 2020 与 October 2021 全部 14 个单元开考、June 2021 有卷无 ER 等）与区域卷 /01A、June 2024 的 /01R：见 `../versions.md` §1.5–1.6 与 `../inventory/pure-gaps.md`。考纲本身只列 `/01`（p.78）。

### 1.2 各资格的单元组合（p.10）

| 资格 | 必修 | 选修 |
|---|---|---|
| IAS Mathematics（3 个单元） | P1, P2 | M1, S1, D1 中选 1 |
| IAS Further Mathematics（3 个单元） | FP1 | FP2, FP3, M1, M2, M3, S1, S2, S3, D1 中选 2 |
| IAS Pure Mathematics（3 个单元） | P1, P2, FP1 | — |
| IAL Mathematics（6 个单元） | P1, P2, P3, P4 | M1 and S1 / M1 and D1 / M1 and M2 / S1 and D1 / S1 and S2 五组中选 1 组 |
| IAL Further Mathematics（6 个单元） | FP1，以及 FP2 或 FP3 之一 | 其余从 FP2, FP3, M1, M2, M3, S1, S2, S3, D1 中选 |
| IAL Pure Mathematics（6 个单元） | P1, P2, P3, P4, FP1 | FP2 或 FP3 |

（“选 1”“选 2”是按“IAS 共 3 个单元、IAL 共 6 个单元”从表中推出的数目，表本身只列单元名。）

## 2. Cash-in、成绩与重考（pp.71–75，p.78）

- **代码**（Appendix 1，p.78）：单元代码 = 单元的 entry code（WMA11/01 … WDM11/01）；**cash-in code** 用来把单元成绩汇总为资格成绩：IAS — Mathematics **XMA01**、Further Mathematics **XFM01**、Pure Mathematics **XPM01**；IAL — Mathematics **YMA01**、Further Mathematics **YFM01**、Pure Mathematics **YPM01**。entry 细节见 Pearson Information Manual（未读，缺口）。
- **一个单元只能用于一个资格**：“once a unit result has been used to cash in for a qualification, it cannot be re-used to cash in for another qualification”；同时拿 IAL Mathematics 与 IAL Further Mathematics 的学生要用 **12 个不同单元**的成绩（p.10）。
- **重考**：任何单元都可重考，不论是否已 cash in；多次重考取最好成绩（p.71）。
- **等级**（p.73）：IAS 五级 A–E；IAL 六级 A*–E；低于最低标准为 U；单元成绩单独报告。
- **UMS**（pp.73–74）：

| 层级 | 满分 UMS | A | B | C | D | E | U |
|---|---|---|---|---|---|---|---|
| 单元 | 100 | 80 | 70 | 60 | 50 | 40 | — |
| IAS（XMA01 / XFM01 / XPM01） | 300 | 240 | 210 | 180 | 150 | 120 | 0–119 |
| IAL（YMA01 / YFM01 / YPM01） | 600 | 480 | 420 | 360 | 300 | 240 | 0–239 |

- **A\* 规则**（p.74）：
  - IAL **Mathematics**：总成绩 A（≥ 480/600）**且** P3 + P4 合计 ≥ **180/200** UMS。
  - IAL **Further Mathematics**：总成绩 A **且** 最好的三个 IA2 单元（纯数或应用单元均可）合计 ≥ **270/300**。
  - IAL **Pure Mathematics**：总成绩 A **且** 其 IA2 单元合计 ≥ **270/300**。
- 首次颁发（p.70 表）：IAS Mathematics June 2019 起；IAS Further Mathematics 与 IAS Pure Mathematics June 2019 起（October 2019 无）；三种 IAL 资格 June 2020 起。
- 先修与升学（p.75）：资格本身 “no prior learning or other requirements”；最适合已有 Level 2 资格如 International GCSE in Mathematics 的学生。
- 考试语言（p.71）：只有英语，所有作答必须用英语。

## 3. 每个单元的考试形式（p.7；各单元 X.2 Assessment information）

- 每个单元：**externally assessed**；书面考试 **1 hour 30 minutes**；**75 marks**；**Students must answer all questions**（无选做题）；可用计算器（Appendix 6）；提供公式册 *Mathematical Formulae and Statistical Tables*；学生须理解 Appendix 7 的记号；题目使用 SI 单位及常用单位。
- 试卷封面说明（以 WMA14/01 January 2024 QP 为例，本地 `research/dl/wma14-jan24-qp.pdf` 封面）：须带公式册（Yellow）与计算器；“You should show sufficient working to make your methods clear. Answers without working may not gain full credit.”；“Inexact answers should be given to three significant figures unless otherwise stated.”；每题分值印在括号内。
- 样卷：Sample Assessment Materials（SAMs）为单独文件（p.67；本次未读）。

## 4. 使用考纲的规则（Using this specification，p.2）

制卡划定范围时直接用得上：
- **Compulsory content**：至少要教完内容栏的全部要点。
- “**The word ‘including’ in content specifies the detail of what must be covered.**” —— 条目里 including 后面列的是必须覆盖的细节。
- **Examples** 只作说明，“for illustrative purposes only”，可用别的例子；考试 “are not limited to the examples given”。
- Depth and breadth：要用到内容的全部范围与全部 AO。

## 5. Assessment objectives（p.68）与各单元 AO 分值（p.69）

| AO | 内容（意译，关键词保留原文） | IAS / IA2 / IAL 最低权重 |
|---|---|---|
| AO1 | Recall, select and use 数学事实、概念与技巧，用于各种情境 | 30% / 30% / 30% |
| AO2 | 构造 **rigorous mathematical arguments and proofs**：精确陈述、逻辑推导与推断、代数式变形，包括为处理以非结构形式给出的较大问题而构造的长论证 | 30% / 30% / 30% |
| AO3 | 回忆、选择并使用 **standard mathematical models** 表示现实情境；理解给出的模型表示；用原情境解释模型结果，包括讨论 **assumptions** 与模型的 **refinement** | 10% / 10% / 10% |
| AO4 | 理解把常见现实情境翻译成数学的做法；用计算结果作预测或评论情境；必要时批判性地阅读较长的数学论证或应用实例 | 5% / 5% / 5% |
| AO5 | 准确高效地使用 **calculator technology** 与允许的资源（formulae booklets、statistical tables）；知道何时不该用这类技术及其局限；“Give answers to appropriate accuracy.” | 5% / 5% / 5% |

各单元 AO 分值区间（满分 75，p.69）：

| 单元 | AO1 | AO2 | AO3 | AO4 | AO5 |
|---|---|---|---|---|---|
| P1 | 30–35 | 25–30 | 5–15 | 5–10 | 1–5 |
| P2 | 25–30 | 25–30 | 5–10 | 5–10 | 5–10 |
| P3 | 25–30 | 25–30 | 5–10 | 5–10 | 5–10 |
| P4 | 25–30 | 25–30 | 5–10 | 5–10 | 5–10 |
| FP1 | 25–30 | 25–30 | 0–5 | 5–10 | 5–10 |
| FP2 | 25–30 | 25–30 | 0–5 | 7–12 | 5–10 |
| FP3 | 25–30 | 25–30 | 0–5 | 7–12 | 5–10 |
| M1 | 20–25 | 20–25 | 15–20 | 6–11 | 4–9 |
| M2 | 20–25 | 20–25 | 10–15 | 7–12 | 5–10 |
| M3 | 20–25 | 25–30 | 10–15 | 5–10 | 5–10 |
| S1 | 20–25 | 20–25 | 15–20 | 5–10 | 5–10 |
| S2 | 25–30 | 20–25 | 10–15 | 5–10 | 5–10 |
| S3 | 25–30 | 20–25 | 10–15 | 5–10 | 5–10 |
| D1 | 20–25 | 20–25 | 15–20 | 5–10 | 5–10 |

## 6. 计算器规则（Appendix 6，p.86）

- 学生应有至少具备以下键的计算器：+、−、×、÷、π、x²、√x、1/x、xʸ、ln x、eˣ、x!、sine／cosine／tangent 及其反函数（度、度的小数、弧度），以及 memory。
- “Calculators with a facility for **symbolic algebra, differentiation and/or integration are not permitted**.”
- 计算器必须：桌面大小；电池或太阳能供电；没有印有说明或公式的盖子、外壳。考生自己负责电源、工作状态、清除存储内容。
- 计算器不得：设计或改装为提供语言翻译、符号代数运算、符号微分或积分、与其他机器或互联网通信；考试中向其他考生借用（监考可以给学生一台）；存有可调出的信息（databanks、dictionaries、mathematical formulae、text）。
- 更多规定见 JCQ *Instructions for conducting examinations* 与 *Information for candidates for written examinations*（未读）。
- 试卷封面的同义表述（WMA14/01 January 2024 QP）：“Calculators must not have the facility for symbolic algebra manipulation, differentiation and integration, or have retrievable mathematical formulae stored in them.”
- 题干限制（不是考纲条文，而是试卷用语）：许多纯数题印有 “**Solutions relying entirely on calculator technology are not acceptable.**”，此时必须写出代数过程。本地已提取文本的纯数试卷中含这句话的份数：WMA11 9/21、WMA12 17/21、WMA13 14/14、WMA14 10/14（`registry/src/WMA1x/*qp*.txt`，按文本检索计数，扫描件可能漏计）。
- 评分通则（WMA14 January 2024 MS PDF p.6，General Principles for Pure Mathematics Marking）：用学过的公式时建议先写出公式；要求 exact 或明显需要用 surd 时改用四舍五入的小数通常失分；“in your head” 能完成的步骤可不写过程。

## 7. 记号（Appendix 7: Notation，pp.87–92）

“The following notation will be used in the examinations.”（p.87）。原表编号照录，含原文的编号瑕疵。

**1 Set notation（pp.87–88）**：1.1 ∈ is an element of；1.2 ∉；1.3 {x₁, x₂, …}；1.4 {x : …} the set of all x such that；1.5 n(A) 集合 A 的元素个数；1.6 ∅ empty set；1.7 ε universal set；1.8 A′ complement；1.9 ℕ = {1, 2, 3, …}（**不含 0**）；1.10 ℤ = {0, ±1, ±2, …}；1.11 ℤ⁺ = {1, 2, 3, …}；1.12 ℤₙ integers modulo n；1.13 ℚ = {p/q : p ∈ ℤ, q ∈ ℤ⁺}；1.14 ℚ⁺ = {x ∈ ℚ : x > 0}；1.15 ℚ₀⁺ = {x ∈ ℚ : x ≥ 0}；1.16 ℝ；1.17 ℝ⁺ = {x ∈ ℝ : x > 0}；1.18 ℝ₀⁺ = {x ∈ ℝ : x ≥ 0}；1.19 ℂ；1.20 (x, y) ordered pair；1.21 A × B cartesian product；1.22 ⊆ subset；1.22（重号）⊂ proper subset；1.23 ∪；1.24 ∩；1.25 [a, b] closed interval {a ≤ x ≤ b}；1.26 [a, b) {a ≤ x < b}；1.27 (a, b] {a < x ≤ b}；1.28 (a, b) open interval {a < x < b}（1.26–1.28 各印有第二种写法，渲染后显示为 “[a, b]”，疑为反向方括号写法排版丢失，以第一种写法为准）；1.29 yRx related by R；1.30 y ∼ x equivalent。

**2 Miscellaneous symbols（p.88）**：= ；≠；≡ is identical to or is congruent to；≈；≅ isomorphic；∝ proportional to；<；≤（印作 ⩽）、≯ is less than or equal to, is not greater than；>；≥（印作 ⩾）、≮；∞；p ∧ q；p ∨ q（p or q or both）；~p not p；p ⇒ q（if p then q）；p ⇐ q；p ⇔ q（equivalent）；∃ there exists；∀ for all。

**3 Operations（p.89）**：a + b；a − b；a × b, ab, a.b；a ÷ b, a/b；Σᵢ₌₁ⁿ aᵢ；Πᵢ₌₁ⁿ aᵢ；√a the **positive** square root of a；|a| modulus；n!；binomial coefficient (n r) = n!/(r!(n − r)!) for n ∈ ℤ⁺，= n(n − 1)…(n − r + 1)/r! for n ∈ ℚ。

**4 Functions（pp.89–90）**：f(x)；f : A → B；f : x ↦ y；f⁻¹；g∘f, gf，(g∘f)(x) = gf(x) = g(f(x))；lim_{x→a} f(x)；Δx, δx increment；dy/dx；dⁿy/dxⁿ；f′(x), f″(x), …, f⁽ⁿ⁾(x)；∫y dx indefinite integral；∫ₐᵇ y dx definite integral；∂V/∂x partial derivative；ẋ, ẍ derivatives with respect to t。

**5 Exponential and logarithmic functions（p.90）**：e；eˣ, exp x；logₐx；ln x, logₑx；lg x, log₁₀x。

**6 Circular and hyperbolic functions（p.90）**：sin, cos, tan, cosec, sec, cot；arcsin, arccos, arctan, arccosec, arcsec, arccot；sinh, cosh, tanh, cosech, sech, coth；arsinh, arcosh, artanh, arcosech, arsech, arcoth。

**7 Complex numbers（p.90）**：i, j（√−1）；z = x + iy；Re z；Im z；|z| = √(x² + y²)；arg z = θ，原文范围印作 −π < x ≤ π（变量应为 θ）；z* = x − iy。

**8 Matrices（p.91）**：M；M⁻¹；Mᵀ；det M or |M|。

**9 Vectors（p.91）**：a（粗体）；AB→；â unit vector；i, j, k；|a|, a magnitude；|AB→|, AB；a.b scalar product；a × b vector product。

**10 Probability and statistics（pp.91–92）**：A, B, C events；A ∪ B；A ∩ B；P(A)；A′；P(A | B)；X, Y, R random variables；x, y, r values；x₁, x₂, … observations；f₁, f₂, … frequencies（编号跳过 10.10）；p(x) = P(X = x)；p₁, p₂, …；f(x), g(x) pdf；F(x), G(x) cdf P(X ≤ x)；E(X)；E[g(X)]；Var(X)；G(t) probability generating function；B(n, p)；N(μ, σ²)；μ；σ²；σ；x̄, m sample mean；s², σ̂² unbiased estimate of population variance，s² = (1/(n − 1))Σ(xᵢ − x̄)²；ϕ、Φ standard normal pdf and cdf；ρ population product moment correlation coefficient；r sample PMCC；Cov(X, Y)。

对纯数卡片最要紧的约定：ℕ 从 1 开始；√a 指正平方根；fg 表示 f(g(x))（P3 1.2 另写明 “do g first, then f”）；≡ 用于恒等式（P2、P3 的恒等式都写成 ≡）；a.b 既是乘号也是 scalar product。

## 8. 公式：公式册给出 vs 考生须记住（逐单元）

**通则**：
- 公式册按单元排列；考生可能要用先前单元引入的公式（原文举例：考 P3、P4 的考生可能要用 P1、P2 首次引入的公式）。 力学、统计单元也可能要用纯数单元的公式。“No formulae are required for the unit Decision Mathematics D1.”（FB p.1 Introduction）
- 各单元 X.2 “Notation and formulae” 一栏列出“Formulae that students are expected to know … will not appear in the booklet”。P4、FP1、S2 还加一句 “This is a list of formulae that students are expected to remember and which will not be included in formulae booklets.”
- 先修单元的须记公式同样要记（各单元 Prerequisites：“… and associated formulae, is assumed and may be tested”）。

| 单元 | 考纲列为须记住（不印在公式册） | 公式册给出（FB 页） | 公式册的交叉引用 |
|---|---|---|---|
| **P1** | 求根公式；sine rule；area = ½ab sin C；arc length = rθ；sector area = ½r²θ；d/dx xⁿ = nxⁿ⁻¹；∫xⁿ dx = xⁿ⁺¹/(n + 1) + c，n ≠ −1（pp.12–13） | Mensuration：球面积 4πr²、圆锥侧面积 πr × slant height；Cosine rule（FB p.3） | — |
| **P2** | 三条对数律；sin²A + cos²A ≡ 1；tan θ ≡ sin θ/cos θ；area under a curve = ∫ₐᵇ y dx（y ≥ 0）（p.17） | 等差 uₙ、Sₙ；等比 uₙ、Sₙ、S∞（|r| < 1）；换底公式；(a + b)ⁿ（n ∈ ℕ）与 ⁿCᵣ；(1 + x)ⁿ（|x| < 1，n ∈ ℝ）；trapezium rule（FB p.3） | — |
| **P3** | sec²A ≡ 1 + tan²A，cosec²A ≡ 1 + cot²A，sin 2A，cos 2A，tan 2A；sin kx、cos kx、e^kx、ln x、aˣ 的导数，sum rule、product rule、chain rule；cos kx、sin kx、e^kx、1/x、f′ + g′、f′(g(x))g′(x)、aˣ 的积分（pp.21–22） | e^(x ln a) = aˣ；sin/cos/tan(A ± B)；四个 sum-to-product；tan kx、sec x、cot x、cosec x 的导数；quotient rule；sec²kx、tan x、cot x 的积分（FB pp.4–5） | 可能用到 P1、P2 公式 |
| **P4** | scalar product (x, y, z)·(a, b, c) = xa + yb + zc（p.26）。另：7.5 的距离公式与 7.7 的 cos∠AOB = a.b/(|a||b|) 在 guidance 中写为须知道（p.29） | (1 + x)ⁿ（|x| < 1，n ∈ ℝ）；cosec x 与 sec x 的积分；integration by parts（FB p.5） | 可能用到 P1–P3 公式 |
| **FP1** | α + β = −b/a，αβ = c/a；Σr = ½n(n + 1)（p.31）。FP1.2 另列先修：用变号定位根、绕原点旋转任意角、三次与四次多项式除以二次式（p.30） | Summations；Numerical solution of equations；Conics；Matrix transformations（FB p.6） | 可能用到 P1、P2 公式 |
| **FP2** | 无清单：FP2.2 第 2 项只写 “Notation”（p.36） | Area of a sector；Complex numbers；Maclaurin's and Taylor's Series（FB p.7） | 可能用到 FP1 与 P1–P4 公式 |
| **FP3** | 无清单：FP3.2 第 3 项只写 “Notation”（p.40） | Vectors；Hyperbolic functions；Conics；Differentiation；Integration；Arc length；Surface area of revolution（FB pp.8–11） | 可能用到 FP1 与 P1–P4 公式 |
| **M1** | Momentum = mv；Impulse = mv − mu；匀加速五式 v = u + at，s = ut + ½at²，s = vt − ½at²，v² = u² + 2as，s = ½(u + v)t（p.44） | “There are no formulae given for M1 in addition to those candidates are expected to know.”（FB p.13） | 可能用到 P1、P2 公式（Issue 2 更正） |
| **M2** | Kinetic energy = ½mv²；Potential energy = mgh（p.47） | Centres of mass（FB p.13） | 可能用到 P1–P4 公式 |
| **M3** | 弹性绳张力 λx/l；弹性势能 λx²/(2l)；SHM：ẍ = −ω²x，x = a cos ωt 或 a sin ωt，v² = ω²(a² − x²)，T = 2π/ω（p.50） | Motion in a circle；Centres of mass；Universal law of gravitation（FB p.13） | 可能用到 M2 与 P1–P4 公式 |
| **S1** | 均值 x̄ = Σx/n 或 Σfx/Σf；标准差 = √(variance)；IQR = Q₃ − Q₁；P(A′) = 1 − P(A)；独立事件 P(B \| A) = P(B)、P(A \| B) = P(A)、P(A ∩ B) = P(A)P(B)；E(aX + b) = aE(X) + b；Var(aX + b) = a²Var(X)；离散 cdf F(x₀) = P(X ≤ x₀) = Σ_{x ≤ x₀} p(x)；Z = (X − μ)/σ，X ∼ N(μ, σ²)（pp.53–54） | Probability；Discrete distributions；Continuous distributions；Correlation and regression；Normal distribution function 表；Percentage points of the Normal distribution（FB pp.14–17） | 可能用到 P1、P2 公式（Issue 2 新增） |
| **S2** | 连续随机变量：P(a < X ≤ b) = ∫ₐᵇ f(x) dx；f(x) = dF(x)/dx（p.57） | Discrete distributions；Continuous distributions；Binomial cumulative distribution function 表；Poisson cumulative distribution function 表（FB pp.18–24） | 可能用到 S1 与 P1–P4 公式 |
| **S3** | aX ± bY ∼ N(aμₓ ± bμᵧ, a²σₓ² + b²σᵧ²)，X、Y 独立且各自服从正态（p.60） | Expectation algebra；Sampling distributions；Correlation and regression；Non-parametric tests；Percentage points of the χ² distribution；Critical values for correlation coefficients；Random numbers（FB pp.25–28） | 可能用到 S1、S2 与 P1–P4 公式（Issue 2 更正） |
| **D1** | “Students are expected to know any other formulae that might be required and which are not included in the booklet”（p.63）；另须熟悉 D1 Glossary 的术语，清楚写出算法如何应用（Preamble，p.63） | 无（FB p.1：D1 不需要公式） | — |

FP、M、S、D 各单元的完整须记清单与条目登记由各自的单元文件负责；上表只摘录考纲 X.2 栏与公式册目录及各节标题；FP、M、S 各节的具体公式未在本文件逐条转录。

## 9. 术语表摘录（Appendix 5: Glossary，p.85）

- **Assessment objectives**：资格要求学生达到的目标，各有侧重，可单独或组合考查。
- **External assessment**：在同一全球区域同一时间、同一地点举行的考试。
- **Linear** 与 **Modular**：前者全部考试集中在课程末；后者由可在课程中途考的单元组成，最终等级由单元成绩合成（本资格为 modular）。
- **Raw marks**：考生实际得分；合成总成绩时需转换。
- **Uniform Mark Scale (UMS)**：把各单元原始分换算到统一尺度，使原始满分不同但权重相同的单元可比。

## 10. 缺口

1. Pearson 官网（qualifications.pearson.com）本环境无法访问：Information Manual（entry 与 aggregation 细节）、SAMs、Pearson 关于 IAL 数学是否改版的新闻均未读。当前版本判断依赖 `../versions.md` §1.2 的否定性检索结果。
2. 公式册 FP1–S3 各节只核对了节标题，没有逐条转录公式（这部分由各单元文件负责核对）。
3. 公式册 P3 节的四个 sum-to-product 公式在 P3 考纲条目中没有被点名；是否单独命题未用真题核实。
4. Appendix 7 的 1.26–1.28 第二种区间写法在 PDF 中渲染为 “[a, b]”，原意无法从本文件确认。
