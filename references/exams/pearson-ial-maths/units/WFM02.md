# WFM02 · FP2 Further Pure Mathematics 2：考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WFM02.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WFM02 --gaps` 输出为准（快照 2026-10-06）**。

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述。

**来源**
- **SPEC**：Pearson Edexcel IAS/IAL Mathematics, Further Mathematics and Pure Mathematics Specification，**Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。页码为印刷页码。
- 不等号、上标、积分限都已对照渲染页图核过（`registry/work/fm-spec/pg-43.png`、`pg-44.png`、`pg-45.png`、`fb-13.png`）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WFM02/01**。另有区域卷 **WFM02/01A**，考纲里没有这个代码；目前见到最早的一份是 2025 年 6 月的 WFM02/01A 试卷。英国文化协会中国区 2026 年 1 月和 6 月以 WFM02A 报名 | SPEC p.8、p.78；versions.md §1.6 |
| 单元名称 | Unit FP2: Further Pure Mathematics 2。p.67 的表里写作 “FP2: Further Mathematics 2” | SPEC p.36、p.67 |
| AS/A2 定位 | 单元页：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Further Mathematics and Pure Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔%，所以也可以计入 IAS Further Mathematics | SPEC p.36、p.67、p.8 |
| 资格结构 | IAL Further Mathematics 的必考单元是 “FP1 and either FP2 or FP3”。IAL Pure Mathematics 是 P1–P4 加 FP1 必考，再从 FP2、FP3 中选一门 | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.36 |
| 题量（参考） | 2025 年 6 月卷封面：“There are 9 questions”，总分 75。考纲不固定题量 | `registry/src/WFM02/2025-06_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra、symbolic differentiation or integration 功能的计算器，也不得存有可调出的公式 | SPEC p.36；Appendix 6，p.86 |
| 公式册 | 考试提供 FB。FP2 部分在 FB p.7；考生还可能要用 “Further Pure Mathematics FP1, and Pure Mathematics P1, P2, P3 and P4” 的公式 | SPEC p.36；FB p.7 |
| 开考季 | **January and June**。从 2020 年 6 月起，October 考季不开 FP2 | SPEC p.8、p.70 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**。2021 年 10 月也例外开考。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.36；versions.md §1.4–1.5 |
| 旧考纲同代码 | 2013 版旧考纲也用 WFM02 这个代码，最后一次是 **2019 年 6 月**，不算本考纲真题。p.1 说 Further 各单元内容 “have not changed”，所以旧卷可作兼容练习 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specifications for P1, P2, P3, P4 and FP1, their prerequisites and associated formulae, is assumed and may be tested.”注意 **FP3 不是先修** | SPEC p.36 |
| 评估目标分配（75 分中） | AO1 25–30；AO2 25–30；AO3 0–5；**AO4 7–12**（FP1 是 5–10）；AO5 5–10 | SPEC p.69 |
| 须背公式清单 | FP2 单元页只写 “2. Notation”（编号印错，应为 3），**没有**列出须背公式。FP1 页那张须背清单（p.31）通过先修关系仍然适用 | SPEC p.36 |
| 记号 | 见 Appendix 7：复数记号在 p.90，arg z 主值范围为 −π < θ ≤ π（原文把 θ 误印成 x） | SPEC p.90 |
| 单元概述 | “Inequalities; series; further complex numbers; first order differential equations; second order differential equations; Maclaurin and Taylor series; Polar coordinates.” | SPEC p.36 |

---

## 2. 规格条目逐条（FP2.3 Unit content）

### 主题 1 Inequalities（p.37）

**1.1 The manipulation and solution of algebraic inequalities and inequations, including those involving the modulus sign**（p.37）
- 要求：处理和求解代数不等式（含 **modulus sign**，即绝对值）。考纲例子：1/(x − a) > x/(x − b)，以及 |x² − 1| > 2(x + 1)。
- 公式：FB 不给相关内容。

### 主题 2 Series（p.37）

**2.1 Summation of simple finite series using the method of differences**（p.37）
- 要求：用 **method of differences**（差分法，也叫裂项相消）求有限级数的和。考纲例子：Σ_{r=1}^{n} 1/(r(r+1))，先用 partial fractions 写成 1/r − 1/(r+1) 再求和。
- 公式：FB 不给。部分分式属于 P4 2.1。

### 主题 3 Further complex numbers（p.37）

**3.1 Euler's relation e^{iθ} = cos θ + i sin θ**（p.37）
- 要求：掌握 Euler 关系式。考纲要求熟悉（“should be familiar with”）cos θ = ½(e^{iθ} + e^{−iθ}) 和 sin θ = (1/2i)(e^{iθ} − e^{−iθ})。
- 公式：FB p.7 只给 e^{iθ} = cos θ + i sin θ；cos θ、sin θ 的指数形式 **FB 不给**。

**3.2 De Moivre's theorem and its application to trigonometric identities and to roots of a complex number**（p.37）
- 要求：
  - 用 **De Moivre's theorem** 把 cos nθ、sin mθ 写成 sin θ、cos θ 的幂；
  - 反过来，把 sin θ、cos θ 的幂写成倍角形式（multiple angles）；
  - 求复数的根；
  - 会证明 De Moivre's theorem 对**任意整数 n** 成立（“prove De Moivre's theorem for any integer n”）。
- 公式：FB p.7 给出 {r(cos θ + i sin θ)}ⁿ = rⁿ(cos nθ + i sin nθ)，以及 zⁿ = 1 的根 z = e^{2πki/n}（k = 0, 1, …, n − 1）。

**3.3 Loci and regions in the Argand diagram**（p.37）
- 要求：Argand diagram 上的轨迹与区域。
  - 轨迹：|z − a| = b；|z − a| = k|z − b|；arg(z − a) = β；arg((z − a)/(z − b)) = β；
  - 区域：|z − a| ≤ |z − b|；|z − a| ≤ b。
- 公式：FB 不给。

**3.4 Elementary transformations from the z-plane to the w-plane**（p.37）
- 要求：从 z 平面到 w 平面的初等变换。可能出 w = z² 和 w = (az + b)/(cz + d)，其中 a, b, c, d ∈ ℂ（“may be set”）。
- 公式：FB 不给。

### 主题 4 First order differential equations（p.38）

**4.1 Further solution of first order differential equations with separable variables**（p.38）
- 要求：进一步求解可分离变量的一阶微分方程。题目可能要求自己列方程（“The formation of the differential equation may be required”）。要求求 **particular solutions**，并画出解曲线族中的若干条（“sketch members of the family of solution curves”）。

**4.2 First order linear differential equations of the form dy/dx + Py = Q where P and Q are functions of x**（p.38）
- 要求：求解一阶线性微分方程 dy/dx + Py = Q（P、Q 是 x 的函数）。
- 公式：积分因子 **e^{∫P dx}** “may be quoted without proof”，即可直接写出、无需证明，但 **FB 不给**，须记住。

**4.3 Differential equations reducible to the above types by means of a given substitution**（p.38）
- 要求：用**题目给定的代换**，把方程化成上面两种类型再求解。指导栏为空。

### 主题 5 Second order differential equations（p.38）

**5.1 The linear second order differential equation a d²y/dx² + b dy/dx + cy = f(x) where a, b and c are real constants and the particular integral can be found by inspection or trial**（p.38）
- 要求：求解常系数线性二阶微分方程。
  - **auxiliary equation**（辅助方程）的根可以是不等实根、相等实根或复根。
  - f(x) 的形式限于：k e^{px}；A + Bx；p + qx + cx²；m cos ωx + n sin ωx。
  - 须熟悉 **'complementary function'** 和 **'particular integral'** 这两个术语。
  - 会解 d²y/dx² + 4y = sin 2x 这类方程。按：此例的右端 sin 2x 恰好是互补函数中的一项；这是本文件的数学说明，不是考纲原文。
- 公式：辅助方程和互补函数的形式 FB 都不给。

**5.2 Differential equations reducible to the above types by means of a given substitution**（p.38）
- 要求：用给定代换把方程化成 5.1 的类型。指导栏为空。

### 主题 6 Maclaurin and Taylor series（p.38）

**6.1 Third and higher order derivatives**（p.38）：三阶及更高阶导数。指导栏为空。

**6.2 Derivation and use of Maclaurin series**（p.38）
- 要求：推导并使用 Maclaurin 级数。可能要求推导 eˣ、sin x、cos x、ln(1 + x) “and other simple functions” 的展开式。
- 公式：FB p.7 给出 Maclaurin 通式，以及 eˣ、ln(1+x)（−1 < x ≤ 1）、sin x、cos x、arctan x（−1 ≤ x ≤ 1）的展开式和收敛范围。注意：考纲写 “derivation … may be required”，所以题目可能要求从通式推导出这些展开式，而不是直接引用。

**6.3 Derivation and use of Taylor series**（p.38）
- 要求：推导并使用 Taylor 级数。考纲例子：把 sin x 按 (x − π) 的升幂展开到 (x − π)³ 项（含该项）。
- 公式：FB p.7 给出 Taylor 级数的两种形式：f(x) 在 x = a 处的展开，和 f(a + x) 的展开。

**6.4 Use of Taylor series method for series solutions of differential equations**（p.38）
- 要求：用 Taylor 级数法求微分方程的级数解。考纲例子：求 d²y/dx² + x dy/dx + y = 0 的解，按 x 的幂写到 x⁴ 项，初始条件 x = 0 时 y = 1、dy/dx = 0。

### 主题 7 Polar coordinates（p.39）

**7.1 Polar coordinates (r, θ), r ≥ 0**（p.39）
- 要求：极坐标 (r, θ)，约定 **r ≥ 0**。可能要求画出这些曲线：θ = α；r = p sec(α − θ)；r = a；r = 2a cos θ；r = kθ；r = a(1 ± cos θ)；r = a(3 + 2 cos θ)；r = a cos 2θ；r² = a² cos 2θ。
- 公式：极坐标与直角坐标的互化式 x = r cos θ、y = r sin θ，**FB 不给**。

**7.1（第二个，JSON 键为 “7.1#2”）Use of the formula ½∫_α^β r² dθ for area**（p.39）
- 编号说明：Issue 3 原文这一行也印作 “7.1”，已对照渲染页图确认，并非抽取错误。逻辑上应是 7.2；JSON 里用键 “7.1#2” 区分两个 7.1，并记别名 7.2：查询写 `python scripts/exam_index.py WFM02 --spec 7.2`，`--spec 7.1` 只匹配第一个 7.1。
- 要求：用 ½∫_α^β r² dθ 求极坐标曲线围成的面积。本行指导栏写的是：“The ability to find **tangents parallel to, or at right angles to, the initial line** is expected”，即还要会求与初始线平行或垂直的切线。
- 公式：FB p.7 “Area of a sector” 给出 A = ½∫r² dθ。求切线所需的关系式 FB 不给。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| ½∫r² dθ（极坐标面积） | FB 给出 | FB p.7 |
| e^{iθ} = cos θ + i sin θ；De Moivre；zⁿ = 1 的根 | FB 给出 | FB p.7 |
| Maclaurin、Taylor 通式；eˣ、ln(1+x)、sin x、cos x、arctan x 展开式及收敛范围 | FB 给出。但 6.2 可能要求推导 | FB p.7；SPEC p.38 |
| cos θ = ½(e^{iθ}+e^{−iθ})，sin θ = (1/2i)(e^{iθ}−e^{−iθ}) | FB **未给**，考纲要求熟悉 | SPEC p.37 |
| 积分因子 e^{∫P dx} | FB **未给**，可不加证明地写出 | SPEC p.38 |
| 辅助方程、互补函数的三种形式、特解的试探形式 | FB **未给** | SPEC p.38 |
| x = r cos θ，y = r sin θ；与初始线平行或垂直的切线条件 | FB **未给** | SPEC p.39 |
| FP1、P1–P4 的公式（Σr²、Σr³、二项式级数、三角恒等式、P3/P4 积分表等） | FB 给出，FP2 可能用到 | FB pp.3–6 |

---

## 4. 与相邻单元的界线

- **P1/P3（不等式与绝对值）**：一次、二次不等式的求解和图示在 P1 1.7–1.9（p.14）。绝对值函数的图像，以及借助图像解 |2x − 1| > x + 5 这类方程和不等式，在 P3 1.3（p.23）。FP2 1.1 往上扩展到分式不等式和含二次式的绝对值不等式。
- **P4（部分分式、微分方程、二项式级数）**：
  - 部分分式在 P4 2.1（p.27），FP2 2.1 差分法要用到；
  - 列简单微分方程在 P4 5.2（p.27），可分离变量一阶微分方程的通解和特解在 P4 6.4（p.28）。FP2 4.1 是 “Further solution”，新增画解曲线族，并接着学 4.2 积分因子法和 4.3 代换法；
  - 有理指数的二项式级数在 P4 4.1（p.27），属于 P4；Maclaurin 和 Taylor 级数属于 FP2 主题 6。
- **FP1（先修）**：
  - 复数的定义、模和辐角、四则运算、Argand 图表示、多项式方程的根都在 FP1 主题 1。FP1 1.2 不要求 arg(z₁z₂) = arg z₁ + arg z₂；FP2 的 De Moivre 和轨迹题实际上要用到辐角的运算；
  - Σr、Σr²、Σr³ 的标准求和在 FP1 7.1，并明确不考差分法；差分法属于 FP2 2.1；
  - 数学归纳法在 FP1 8.1。FP2 3.2 要求证明 De Moivre 定理对任意整数 n 成立；考纲没有规定用什么方法证明。
- **FP3（不是 FP2 的先修，两者平行）**：双曲函数在 FP3 主题 1，FP2 不能默认学生会；FP3 也不默认学生学过 FP2。弧长和旋转曲面面积在 FP3 4.6，并写明 “Equations in polar form will not be set”，所以极坐标只在 FP2 中考。积分技巧（hyperbolic/trig substitution、reduction formulae）在 FP3 主题 4。
- **M3**：M3 的变力运动和 SHM 写明求解 “consistent with the level of calculus in units P1, P2, P3 and P4”（p.51），不依赖 FP2 的二阶微分方程方法。

---

## 5. 印刷问题与缺口
- 主题 7 有两个条目都编号为 “7.1”（p.39），已对照页图确认。registry 中第二个记作 “7.1#2”。
- 第二个 7.1 讲面积，但它的指导栏讲的是切线，即这一行的指导栏与条目标题内容不对应，以原文为准。
- 单元页的 “2. Notation” 编号重复（前面已有 “2. Examination”）。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误。

---

## 6. 真题需求概览

**数据基础**：`WFM02.questions.json`（2026-10-06 由 `WFM02.questions.part1.json` 与 `part2.json` 合并；按 series → 同季 /01 在 /01A 之前 → 题号排序）。共 13 份卷：2020-10、2021-01、2021-06、2021-10、2022-01、2022-06、2023-01、2023-06、2024-01、2024-06、2025-01、2025-06 /01、2025-06 /01A。合计 109 题、245 小问、975 分，每卷 75 分。13 份卷都有 QP 和 MS；考官报告（ER）只拿到 2023-01、2023-06、2024-01 三份，覆盖 25 题。各卷来源和文件校验见 `WFM02.coverage.part1.md`、`WFM02.coverage.part2.md`。

**统计口径**：
- "考 n/13 卷"：该条目出现在小问 `spec` 列表任一位置的卷数。
- "主条目分值"：只把小问分值记到 `spec` 列表的第一个 id 上。
- 引用写法：`2023-06 Q2(a)` 指 2023 年 6 月 WFM02/01 第 2 题 (a)；`2025-06A` 指 2025 年 6 月 WFM02/01A。MS、ER 页码都是 `sources` 所列 PDF 的页码。

**仍缺的卷与报告**（详见 `WFM02.coverage.part2.md` §3）：
- **整卷缺失**：2026-01 WFM02/01 与 /01A，2026-06 WFM02/01 与 /01A。grademax 清单列出了它们的 Pearson 文件名，但 QP、MS、ER 都拿不到。
- **只缺 ER**：2020-10、2021-01、2021-10、2022-01、2022-06、2024-06、2025-01、2025-06 /01、2025-06 /01A。2021-06 考试取消，本来就没有报告。
- 2026-10-06 复查 Drive：标题含 WFM02/FP2，标题含 2601/2606 + Further/F2/FM，全文 WFM02 + Examiners。没有找到新文件。

**审计记录（2026-10-06，脚本与备份在 `registry/work/wfm02audit/`）**：
- **结构**：109 条字段齐全；各小问分值之和等于题目总分；spec id 都在 `spec-items.fm.json` → WFM02 中；series 格式都是 YYYY-MM；每卷 75 分，题号连续。没有问题。
- **分值**：按 QP 的 "Total for Question n" 和 "(Total n marks)" 切题，109 题的总分与印刷值全部一致。小问分值也与印刷值一致，只有两类例外，都是有意按 MS 处理：
  - 4 题按 MS 拆分：2023-01 Q9(a)、2024-01 Q2(a)、2025-01 Q7(a)、2025-06A Q1(b)；
  - 4 题按 MS 合并为 "i–ii"：2020-10 Q5、2021-06 Q2、2022-06 Q3、2024-06 Q6。
- **指令词**：245 个 `command` 的每个词都能在对应 QP 题块中找到。
- **答案**：用 sympy 复算了约 130 个可计算的 `final_form`，全部一致。复算内容包括：
  - 部分分式与差分求和；
  - 不等式解集（逐点扫描）；
  - 复数根；
  - 通解、特解代回原方程；
  - 级数系数；
  - 极坐标切点与面积；
  - 变换像的圆心与半径。
- **人工逐条对照 QP、MS、ER 原文**，共 23 题：2020-10 Q5，2021-01 Q7，2021-06 Q1、Q8，2021-10 Q8，2022-01 Q3、Q8，2022-06 Q8，2023-01 Q4、Q9，2023-06 Q2、Q8，2024-01 Q6、Q7、Q8，2024-06 Q6、Q10，2025-01 Q7、Q8，2025-06 Q6、Q8，2025-06A Q4、Q8。另外核对了：
  - 三份报告覆盖的全部 25 题的 `er` 字段，其中 7 题已在上面的人工对照中核过；
  - 17 处 MS 特殊规则（SC、max、"scores 0"）；
  - 307 处 MS/ER 页码引用。
- **结论**：分值、spec、答案和 MS 要点没有实质错误。
- **修改**：只改了 2 处 ER 措辞，都是让表述更精确，不是纠错。记录在 `work/wfm02audit/fixes.json`：
  - 2023-06 Q2(a)：原写 "Hardest question"，没有页码。ER p.10 确实称 Q2 为 "the hardest"。现补上页码，并加入 ER p.4 的统计：这是唯一一道平均分低于一半（约 4.5/10）、众数不是满分的题。
  - 2023-06 Q7(b)：原写 "few could integrate (ln x)/x"。ER p.9 的原意是：只有少数人做对；多数人用分部积分，卡在第二步；只有少数人看出这是 reverse chain rule。

### 6.1 每卷结构

- 每卷 8–10 题：8 题的 9 份，9 题的 3 份，10 题的 1 份。每题 3–16 分。
- 七个主题每卷都考。各卷分值（按主条目汇总）：

| 主题 | 20-10 | 21-01 | 21-06 | 21-10 | 22-01 | 22-06 | 23-01 | 23-06 | 24-01 | 24-06 | 25-01 | 25-06 | 25-06A | 合计 | 每卷平均 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 不等式 | 9 | 7 | 7 | 8 | 11 | 8 | 6 | 7 | 5 | 6 | 7 | 10 | 6 | 97 | 7.5 |
| 2 级数（差分法） | 9 | 6 | 8 | 9 | 11 | 5 | 6 | 7 | 7 | 8 | 9 | 10 | 8 | 103 | 7.9 |
| 3 复数 | 15 | 19 | 17 | 19 | 15 | 22 | 16 | 17 | 18 | 19 | 24 | 21 | 20 | 242 | 18.6 |
| 4 一阶微分方程 | 8 | 9 | 11 | 9 | 14 | 7 | 9 | 11 | 13 | 9 | 6 | 11 | 8 | 125 | 9.6 |
| 5 二阶微分方程 | 14 | 12 | 13 | 11 | 6 | 12 | 13 | 11 | 14 | 10 | 11 | 10 | 13 | 150 | 11.5 |
| 6 Maclaurin/Taylor | 7 | 9 | 9 | 8 | 8 | 8 | 15 | 9 | 9 | 14 | 8 | 5 | 8 | 117 | 9.0 |
| 7 极坐标 | 13 | 13 | 10 | 11 | 10 | 13 | 10 | 13 | 9 | 9 | 10 | 8 | 12 | 141 | 10.8 |

- 每卷固定会有下面几类题，顺序不定：
  - 一道 "Use algebra" 不等式；
  - 一道差分法求和；
  - 一道 de Moivre；
  - 一道 Argand 轨迹题或 z→w 变换题，有时两者都有；
  - 一道一阶线性微分方程，多数要先做给定代换；
  - 一道二阶常系数微分方程（CF + PI + PS），6 份卷要先做代换；
  - 一道高阶导数 + Taylor/Maclaurin；
  - 一道极坐标题：切线 + 面积，或交点 + 面积。

### 6.2 逐条目考频与考法

| 条目 | 考卷数 | 小问（主/全部） | 主条目分值 | 常见指令词 | 典型最终形式 | 单个小问分值 |
|---|---|---|---|---|---|---|
| 1.1 不等式 | 13/13 | 21/22 | 97 | Use algebra (to obtain/determine/find)、Using algebra, solve、Hence (or otherwise) determine | 区间并集；端点常为精确根式；严格/非严格要分清 | 1–9 |
| 2.1 差分法 | 13/13 | 34/34 | 103 | Express (in partial fractions)、Show that、Hence (use the method of differences to) show/find | 指定形式的闭式并给出常数；精确分数；n 的值 | 1–7 |
| 3.1 Euler | 6/13 | 2/7 | 5 | Express、Show that | re^{iθ}，−π < θ ≤ π | 2–3 |
| 3.2 de Moivre | 13/13 | 32/33 | 119 | Show that / Use de Moivre's theorem to show、Hence solve/determine、Solve | 给定恒等式；re^{iθ} 形式的全部根；3 d.p./3 s.f.；精确积分值 | 1–6 |
| 3.3 轨迹与区域 | 12/13 | 12/20 | 32 | Determine、Sketch、Shade | 草图/阴影区域；直线方程（整数系数）；精确复数；\|w\| 的范围；arg 取 3 s.f. | 1–5 |
| 3.4 z→w 变换 | 12/13 | 16/17 | 86 | Determine、Find、Show that、Sketch | 像圆的圆心与精确半径；像直线方程；用 arg 表示的区域 | 2–8 |
| 4.1 可分离变量 | 1/13 | 2/2 | 9 | Solve、Sketch | v = f(x)；解曲线草图并标渐近线 | 4–5 |
| 4.2 积分因子法 | 12/13 | 17/18 | 79 | Determine、Obtain、Solve、Hence find | y = f(x) 或 y² = f(x)；过定点的特解 | 2–8 |
| 4.3 一阶给定代换 | 8/13 | 12/17 | 37 | Show that（给定结果）、Hence obtain | 给定方程；还原代换（1–2 分） | 1–5 |
| 5.1 二阶常系数 | 13/13 | 23/23 | 114 | Determine、Find、Solve | 带 "y =" 的通解 = CF + PI；特解；后续求值 | 2–8 |
| 5.2 二阶给定代换 | 6/13 | 13/16 | 36 | Show that、Hence show/determine/obtain | 给定方程；用原变量写出通解 | 1–6 |
| 6.1 高阶导数 | 13/13 | 13/15 | 55 | Show that、Determine | 含整数常数的给定形式；数值 | 3–7 |
| 6.2 Maclaurin | 3/13 | 6/6 | 13 | Hence determine、Write down、Use、Show that | 到 x³ 的级数，系数化简 | 1–3 |
| 6.3 Taylor | 8/13 | 6/10 | 20 | Hence (or otherwise) determine、Use、Hence show | (x − a) 的升幂级数；近似值（4 s.f.） | 2–7 |
| 6.4 微分方程级数解 | 8/13 | 9/10 | 29 | Determine、Find、Obtain、Express | x 或 (x − a) 的级数解 | 1–6 |
| 7.1 极坐标 | 12/13 | 5/16 | 10 | Determine、Write down、Sketch | 点的极坐标；精确参数 k | 1–3 |
| 7.1#2 面积与切线 | 13/13 | 22/22 | 131 | Use (algebraic integration)、Use calculus (to determine)、Show that、Find | 精确极坐标（"no others"）；指定形式的精确面积 | 4–9 |

**1.1 不等式**（每卷 5–11 分，几乎都是整题）
- **有理分式不等式**：2021-10 Q2，2022-06 Q2(a)，2023-06 Q3，2024-01 Q1，2024-06 Q5，2025-06A Q1。2023-06 Q3(a) 先要求推出 (x + 4)(x − 1)(px² + qx + r) ≤ 0 这一中间式，再解 (b)。
- **含绝对值**：
  - 整个式子外套绝对值：2020-10 Q3（分式），2021-01 Q3、2021-06 Q5（二次式）；
  - 绝对值在分母：2023-01 Q5，2022-06 Q2(b)；
  - 曲线中含 |x|：2022-01 Q3，2025-06 Q8。
- **"先交点后不等式" 两步式**：2022-01 Q3，2025-01 Q2，2025-06 Q8，2025-06A Q1。
- **加绝对值的 follow-up**（1–4 分）：2022-06 Q2(b)，2025-01 Q2(c)，2025-06 Q8(b)，2025-06A Q1(b)(ii)。
- 精确端点常见，例如 2 ± √15（2024-06 Q5）、(13 + √201)/2（2025-06 Q8）。

**2.1 差分法**（每卷 5–11 分）
- 固定三段：
  - (a) 部分分式或给定恒等式，1–4 分；
  - (b) "Hence/using the method of differences show Σ = 给定形式"，求常数，3–7 分；
  - (c) 后续一问。
- 被求和项的类型：
  - 有理式：8 份卷；
  - 根式有理化：2023-06 Q1，2024-01 Q3；
  - arctan 差公式：2022-01 Q6，含求无穷和的极限；
  - log₃：2025-06A Q5；
  - 多项式恒等式 n⁵ − (n − 1)⁵ 推出 Σr⁴：2021-10 Q9。
- (c) 的变式：
  - 改上下限求数值和：2020-10 Q2(c)，2023-06 Q1(c)，2024-06 Q3(c)；
  - 求常数 k：2024-01 Q3(c)；
  - 列二次不等式求最小 n：2025-06 Q5(c)；
  - 解出 n：2025-06A Q5(c)。

**3.1 Euler 公式**：单独计分只有两次，即 2021-01 Q8(a)（z = e^{iθ}）和 2025-06 Q1(a)（化为 re^{iθ}）。其余都作为 3.2 的附带要求，即根写成 re^{iθ}：2020-10 Q4(b)，2021-10 Q1，2022-01 Q1(b)，2024-01 Q2(b)，2025-06 Q1(b)。

**3.2 de Moivre**（每卷 4–14 分）
- **倍角恒等式（3–6 分）+ "Hence" 解方程**：恒等式见 2021-06 Q7（tan 4θ）、2022-06 Q8（sin 5θ）、2023-01 Q7（cos 5x）、2024-06 Q9（cos 6θ）、2025-01 Q7（sin/cos/tan 5θ）、2025-06 Q9（sin 5θ）。后一问是：
  - 解多项式或三角方程，答案取 3 d.p./3 s.f.；
  - 求精确值：2025-06 Q9(b)；
  - 求定积分：2022-06 Q8(c)。
- **zⁿ + z⁻ⁿ = 2cos nθ → 降幂 → 积分**：2021-01 Q8 求 ∫，2025-06A Q8 求旋转体体积。
- **复数的 n 次根**（4–5 分）：2020-10 Q4，2021-10 Q1，2022-01 Q1，2025-06 Q1(b)；平方根写成 a + ib：2024-01 Q2(c)。
- **模辐角形式的乘方与除法**：2023-06 Q2(a)，2024-01 Q2(b)。

**3.3 轨迹与区域**
- **主考 3.3 的小问**：
  - Apollonius 圆 + 半直线交点：2021-10 Q6；
  - 垂直平分线：2023-01 Q6(a)、2024-06 Q1；
  - 扇形区域 + 最小 arg：2023-06 Q2(b)(c)；
  - 从精确网格图读出 a、b、c，再求 |w| 的范围和最小 arg：2025-06A Q4；
  - 由像圆方程读出圆心半径：2023-06 Q5(b)；画 |z| = 1：2025-06 Q3(a)。
- 其余 8 次是 3.4 变换题里的附带要求，例如判断像区域在圆内还是圆外。

**3.4 变换**（每卷 3–13 分，只有 2025-06A 没考）
- 全部是 w = (az + b)/(cz + d) 型。
- 像的类型：
  - 圆 → 圆：2020-10 Q5，2021-06 Q2，2022-06 Q3；
  - 直线 → 圆：2022-01 Q7(b)，2023-01 Q6(b)，2023-06 Q5，2024-01 Q7，2024-06 Q6；
  - 直线 → 直线：2021-10 Q3，2022-01 Q7(a)，2025-01 Q8(a)；
  - 圆 → 直线：2025-01 Q8(b)，2025-06 Q3(b)；
  - 区域的像：2024-01 Q7(b)，2025-01 Q8(c)；
  - 不动点：2021-01 Q1。

**4.1–4.3 一阶微分方程**
- **4.2**：12 份卷考了，只有 2022-01 没考。两种来路：
  - 直接用积分因子：2020-10 Q6，2021-10 Q4，2022-06 Q4，2025-01 Q1，2025-06A Q2；
  - 先按给定代换化成线性方程：y² = 1/z、v = y⁻²、y = 1/z、z = y⁻²、y² = w sin 2x、y² = 1/t、z = 1/y²，见 2021-01、2021-06、2023-01、2023-06、2024-01、2024-06、2025-06。
- **4.3** 的固定写法："Show that the substitution … transforms (I) into (II)"，给定结果，3–5 分；最后 "Hence obtain" 还原代换，1–2 分。
- **4.1** 只出现一次：2022-01 Q8 用 v = y − 2x 化成可分离变量方程，(d) 画过 (−1, −1) 的解曲线。

**5.1–5.2 二阶微分方程**（每卷 6–14 分）
- **通解与特解**：通解 5–8 分；特解 4–5 分。
- **后续求值**：2023-06 Q4(c) 求 x = −2 时的值；2024-01 Q6(c) 求第一个转折点，取 3 s.f.；2025-06A Q7(c) 求 x = 1/8 时的值。
- **辅助方程根的类型**：
  - 两个不同实根：7 次；
  - 重根：2023-01 Q9、2023-06 Q4；
  - 共轭复根：2021-01 Q6、2024-01 Q6、2025-01 Q6；
  - 纯虚根：2022-06 Q7。
- **右端形式**：
  - 多项式：7 次；
  - 指数：5 次，其中与 CF 重叠的有 2022-01 Q2 和 2025-06 Q4（后者题目直接给出 PI 的形式 λxe^{3x}）；
  - 三角：只有 2021-01 Q6，且不与 CF 重叠。
- **5.2 的代换**：x = e^u（2020-10、2025-06A），x = t²（2021-10），y = xv（2022-06），x = t^{1/2}（2023-01），t = ln x（2024-06）。最后一问 "Hence … general solution of (I)" 通常只有 1 分（B1ft）。

**6.1–6.4 级数**（每卷 5–15 分）
- **6.1 求高阶导数**，每卷都有，多为 "Show that d³y/dx³ = …（求整数常数）"，3–7 分。来源有两种：
  - 显函数：tan²x、√(4 + ln x)、ln(5 + 3x)、sec x、tan(3x/2)、eˣ sin x、arcsin 2x；
  - 由微分方程隐式求导：2020-10，2021-01，2021-06，2022-06，2023-01 Q4，2024-06 Q2，2025-01 Q3，2025-06 Q2。
- **6.4 级数解**：在 x = 0 处展开 4 次；在 x = a ≠ 0 处展开 4 次（2023-01、2024-06、2025-01、2025-06）。
- **6.3 Taylor**：在 π/3、1、π/6 处展开；另有用级数求近似值，例如 sec(7π/24) 取 4 s.f.（2023-06 Q6(c)），tan(3π/8) 写成给定形式（2024-01 Q4(b)）。
- **6.2 Maclaurin**：只考过 3 次，都是复合函数：ln(5 + 3x)（2023-01 Q1），eˣ sin x（2024-06 Q7），arcsin 2x 以及它与 e^{3x} 的乘积（2025-06A Q3）。

**7.1 / 7.1#2 极坐标**（每卷 8–13 分）
- **切线**：9 份卷考了，4–6 分。
  - 与初始线平行：2020-10、2021-06、2022-06、2023-01、2023-06 Q8(b)、2025-01；
  - 与初始线垂直：2021-01、2021-10、2025-06A。
- **面积**：13/13 卷，6–9 分，都要求精确值并写成指定形式。区域的拆法：
  - 扇形减三角形（弓形）：2020-10、2022-06；
  - 加梯形：2021-10、2023-06；
  - 加三角形：2023-01、2024-06；
  - 两曲线之间：2022-01（玫瑰线减圆）、2025-06（两圆）、2025-06A（圆减曲线）；
  - 单一扇形区域：2021-01、2021-06、2024-01、2025-01。
- **被积式**：除 (a + b cos θ)² 外，还出现 tan θ 或 tan(θ/2) 的平方，要用 sec² − 1 处理，见 2024-01 Q5、2025-01 Q5(b)、2025-06A Q6(b)。
- **7.1 主考**：写出点坐标（2023-06 Q8(a)），精确 R（2021-01 Q7(b)），交点与直线参数（2024-06 Q10(a)、2025-06 Q7(a)），在极坐标网格上作图（2022-01 Q4(a)）。

### 6.3 至今没考过或只考过一次的要求

下面这些要求考纲里有，但 13 份卷里没考过或只考过一次。做卡时仍要覆盖，但可以把它们标成"考纲要求、真题未见"。

- **3.2 证明 de Moivre 定理对任意整数 n 成立**：没考过。2021-01 Q8(a) 和 2025-06A Q8(a) 只要求由 de Moivre 推出 zⁿ + z⁻ⁿ = 2cos nθ。
- **3.1 sin θ 的指数形式**，即 zⁿ − z⁻ⁿ = 2i sin nθ 方向：没作为题目要求出现过，只在 2022-06 Q8(a) MS 的另解里出现。
- **3.3 轨迹 arg((z − a)/(z − b)) = β**：没考过。区域 |z − a| ≤ |z − b| 考过（2024-06 Q1(b)、2025-06A Q4）。
- **3.4 变换 w = z²**：没考过，所有变换都是分式线性型。
- **4.1 由情境建立微分方程**、**画解曲线族中的若干条**：没考过。4.1 只在 2022-01 Q8 出现一次，画的是一条特解曲线。
- **5.1 三角右端与 CF 重叠的情形**（考纲例题 d²y/dx² + 4y = sin 2x）：没考过。三角右端只有 2021-01 Q6 一次。
- **6.2 推导 eˣ、sin x、cos x、ln(1 + x) 的标准展开**：没单独考过。实际考的都是复合函数。
- **7.1 画考纲列出的标准曲线**（r = kθ、r² = a² cos 2θ、r = a(3 + 2cos θ)、r = p sec(α − θ) 等）：没要求画过。题目都直接给出图。唯一的作图题是 2022-01 Q4(a) 的 r = 4 − 1.5 cos 6θ，加上 r = 1。
- **只考过 1–3 次的条目**：4.1（1 份卷）、6.2（3 份卷）。3.1 单独计分只有 2 次。

### 6.4 评分方案（MS）的固定惯例

1. **"Use algebra" 必须有代数过程。**
   - 只画图、只用计算器得 0 分，或只能拿临界值的 B 分："No algebra implies no marks"（2020-10 Q3，MS p.10）；纯图像解得 0/7（2021-06 Q5，p.16）；草图加临界值、没有代数，只给 B 分（2022-06 Q2(a)，p.8）。
   - 2025-06 Q8(a) 解出四次方程时允许用计算器，但必须先用代数推出这个方程（MS pp.19–20）。
2. **不等式的写法。**
   - 区间之间用 "and"/"or"/逗号或 ∪ 连接；用 ∩ 扣一个 A（2020-10 Q3，p.10；2021-10 Q2，p.9）。
   - 开区间用方括号得 A0（2025-06 Q8(a)，p.20）。
   - 分母或 |x| 产生的临界值单独给 B1：2022-01 Q3(b)（0 和 ±4，pp.10–11）；2024-06 Q5（−2 和 3，p.12）。
   - 把错误情形下得到的根 (−13 − √201)/2 当作端点，得 M0（2025-06 Q8(a)，p.20）。
3. **差分法要写出相消过程，并从题目给的下限开始。**
   - 开头至少写 3 行、结尾至少写 2 行（2020-10 Q2(b)，p.9；2021-06 Q1(b)，p.9）。
   - 必须从 r = 5 开始，从 r = 1 开始是 M0，除非完整地算出 f(n) − f(4)（2022-06 Q1(b)，p.7）。
   - 部分分式要写成完整形式，否则 (a) 得 M0（2025-06 Q5(a)，MS p.14）。
4. **"Hence" 必须真的用到前一问。**
   - 只写答案得 0 分（2022-06 Q8(b)，p.18）。
   - 不用 (b) 而用计算器解得 0 分（2025-01 Q7(c)，p.21）。
   - 直接解关于 x² 的三次方程得 0 分（2024-06 Q9(b)，p.18）。
   - 没有列出二次不等式就试值，得 0 分（2025-06 Q5(c)，p.15）。
   - 不用 (a) 的方法最多 1 分（2025-06A Q8(b)，p.20）。
5. **给定结果（A1*）要有中间步骤。**
   - 代换后至少写一行，再到结果（2023-01 Q9(b)，p.25；2025-06 Q6(a)，p.16）。
   - 不能直接跳到 cos(2π/3) + i sin(2π/3)（2023-06 Q2(a)，p.9）。
   - 要展开 (1 − sin²θ)²，并写出等式两边（2022-06 Q8(a)，p.18）。
6. **复数根。**
   - 必须给出全部 n 个根，形式和辐角范围按题目要求，且 "no others"。
   - 要 re^{iθ} 却写成 r(cos θ + i sin θ)，扣最后的 A 分；用角度当作 misread，按 M1M1B1A0A0 给分（2020-10 Q4(b)，p.11）。
   - 漏写或错用 2kπ，最多 M1A0A0（2025-06 Q1(b)，p.8）。
7. **微分方程的答案格式。**
   - 通解必须写成 "y = …"（自变量是 t 时写 "x = …"），并用原变量表示：2023-06 Q4(a)（ER p.6）；2024-01 Q6(a)，p.14；2025-01 Q6(a)，p.18 要求 "Must have y = … and be in terms of x only"。2025-01 Q6(b) 的特解则接受不写 "y ="（p.19）。
   - 常数必须带上，而且在后续变形中处理正确：2020-10 Q6，p.13；2025-01 Q1(b) 中 "y = tan x sec²x + c → c = …" 记 M0（p.8）。
   - 特解要用含两个常数的 CF 加上 PI（2024-01 Q6(b)，p.15）。
8. **PI 的试探形式。**
   - 不需要乘 t 时却用了 λte^{−3t}：最多 B0M1dM0A0（2024-01 Q6(a)，p.14）。
   - 右端是 t 时，PI 只设 at 得 M0（2023-01 Q9(c)，p.26）。
   - 多项式右端只设 λu 得 M0（2020-10 Q8(b)，p.18）。
9. **级数答案前要不要写 "y ="，各卷标准不一。**
   - 要求写：2020-10 Q1(c)，p.8；2021-01 Q5(b)，p.15；2021-10 Q5(b)，p.12；2022-06 Q5(b)，p.12；2025-01 Q3(b)，p.11（"f(x) = … is A0"）。
   - 不要求：2022-01 Q5(b)，p.15；2023-01 Q4(b)，p.13；2024-01 Q4(a)，p.11；2024-06 Q2(b)，p.15（condone missing）；2025-06 Q2，p.9。
   - 2023-06 Q6(b) 本次不扣，ER p.8 提醒以后可能恢复。
   - 所以做卡时一律要求写 "y ="。
10. **极坐标。**
    - 与初始线平行的切线要对 r sin θ 求导，垂直的要对 r cos θ 求导。2025-01 Q5(a) 中用 r cos θ 该问得 0 分（p.17）。
    - 坐标要 "and no others"（2021-10 Q8(a)，p.15；2023-06 Q8(b)，p.18）。
    - 面积公式中的 ½ 必须出现，才能拿最后的 dM1（2024-06 Q10(b)，p.21）。
11. **变换题。**
    - 先把 z 用 w 表示，再代入轨迹方程。
    - 圆心和半径必须从正确的圆方程得出（2020-10 Q5，p.12）。
    - 圆心写成含 i 的形式得 A0（2021-10 Q6(a)，p.13）。
    - 判断区域的像，要用一个测试点决定取哪一侧（2025-01 Q8(c)，pp.24–25）。

### 6.5 考官报告的警示（只有 2023-01、2023-06、2024-01 三份）

- **复数**
  - 处理分母 cos θ − i sin θ 时，要先处理负号再用 de Moivre；相除时辐角要相减，常见错误是相加。经错误过程得到给定答案不给分（2023-06 Q2(a)，ER p.4）。
  - 求根时常漏掉第二个根，或给出共轭对；在乘方中多加 +2kπ（2024-01 Q2(b)(c)，pp.3–4）。
  - 解出 sin²θ 后忘了开方（2023-01 Q7(b)，p.6）。
- **轨迹与变换**
  - 区域图中的半直线要从圆心出发，不能用实轴；圆要明显经过原点（2023-06 Q2(b)，p.5）。
  - 取实部、虚部时丢掉分母（2024-01 Q7(a)，p.7；2023-06 Q5(a)，p.7）。
  - 不会判断区域的像是圆内还是圆外（2024-01 Q7(b)，p.7）。
- **不等式**
  - 漏掉分母或绝对值产生的临界值：−2（2024-01 Q1，p.3）；−8，同时只讨论了绝对值的一种情形（2023-01 Q5，p.5）。
  - 端点 −4 和 1 被误取为闭区间；选成"两边加中间"的错误区域（2023-06 Q3(b)，p.6）。
- **差分法**
  - 公因子 1/8 过早乘进各分式（2023-01 Q2(b)，p.4）；丢掉 ½，或记错 Σr（2024-01 Q3(c)，p.4）。
  - 改下限时误用 (a) 的结果（2023-06 Q1(c)，pp.3–4）。
- **一阶微分方程**
  - 把 e^{−∫1/x dx} 算成 −x（2023-01 Q3(b)，p.4）。
  - ∫sec x tan x dx 记不住（2024-01 Q8(c)，pp.7–8）；∫(ln x)/x dx 只有少数人做对（2023-06 Q7(b)，p.9）。
  - 最后漏写常数（2023-06 Q7(b)，p.9；2024-01 Q8(c)，p.8）。
  - "using (a)" 必须看得出来（2024-01 Q8(b)，p.7）。
- **二阶微分方程**
  - PI 设成 at 而不是 at + b，丢 3 分（2023-01 Q9(c)，p.7）。
  - 没必要地设 λte^{−3t}（2024-01 Q6(a)，p.6）。
  - PI 中常数算错，连丢 3 个 A（2023-06 Q4(a)，p.6）。
  - 写成 "GS =" 而不是 "y ="（2023-06 Q4(a)，p.6）。
  - 求 d²y/dx² 时漏掉 dt/dx（2023-01 Q9(a)(ii)，pp.6–7）。
- **级数**
  - 链式法则出错：ln(5 + 3x) 求导得 1/(5 + 3x)（2023-01 Q1(a)，p.3）；漏掉 sec 或 tan 的幂（2023-06 Q6(a)，p.8）；把 tan² 写成 tan（2024-01 Q4(a)，p.5）。
  - 用 3 代替 3!；展开成 x 的幂而不是 (x − a) 的幂（2024-01 Q4(a)，p.5）。
  - 求 sec(7π/24) 时误把 x − π/3 设为 7π/24（2023-06 Q6(c)，p.8）。
  - 不写出求导值和 Taylor 公式，有丢方法分的风险（2023-06 Q6(b)，p.8；2024-01 Q4(a)，p.5）。
- **极坐标**
  - r 算成 3 而不是 9；不用微积分直接猜出 π/3（2023-06 Q8(b)，p.10）。
  - 区域拆错，导致积分限取错（2023-06 Q8(c)，pp.10–11；2023-01 Q8(b)，p.6）。
  - 平方 r 时丢中间项；把 tan²θ 写成 1 − sec²θ，或用分部积分；减去 −20 时符号出错（2024-01 Q5，p.5）。
