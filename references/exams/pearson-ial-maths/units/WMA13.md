# WMA13 Pure Mathematics 3（P3）考纲条目登记

**来源**：Pearson Edexcel IAL Mathematics, Further Mathematics and Pure Mathematics Specification，**Issue 3 – April 2019**（ISBN 978 1 446 94981 8；本地 `research/dl/ial-maths-spec.pdf`，md5 06d01a11…；与 `registry/versions.md` §1.1 一致）。P3 位于印刷页 **pp.21–25**（PDF 页 = 印刷页 + 6）。公式册 *Mathematical Formulae and Statistical Tables* **Issue 2 – January 2021**（P59773RA；Pure Mathematics P3 一节在公式册印刷 **pp.4–5**）。条目编号与页码已用脚本逐页核对，含公式的格子另用渲染图核对（如 5.1 的 1/xⁿ、2.3 的 r cos(θ ± a)）。登记日期 2026-10-06。

共用部分见 `../specification.md`。

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WMA13/01**（区域卷 WMA13/01A，已见 June 2025 与 October 2025） | p.78；`versions.md` §1.6 |
| 名称 | Unit P3: Pure Mathematics 3 | p.21 |
| 角色 | **IA2 单元**（p.67）。Compulsory unit for IAL Mathematics and Pure Mathematics；IAS 权重 N/A（不能用于 IAS 资格）；不计入 Further Mathematics。IAL Mathematics 的 A* 要求 P3 + P4 合计 UMS ≥ 180/200（p.74） | p.21；p.7；p.74 |
| 权重 | IAS N/A，IAL 16⅔% | p.7 |
| 时长与分值 | 1 h 30 min，75 分，answer all questions；可用计算器；提供公式册 | p.21（P3.2） |
| 考季 | January、June、October | p.7；p.70 |
| 2018 考纲首考 | **January 2020**（实际首考同） | p.21；p.7；`versions.md` §1.4 |
| 先修 | “A knowledge of the specifications for P1 and P2, their prerequisites and associated formulae, is assumed and may be tested.” | p.21 |
| AO 分值区间 | AO1 25–30，AO2 25–30，AO3 5–10，AO4 5–10，AO5 5–10 | p.69 |
| 单元描述 | Algebra and functions; trigonometry; exponentials and logarithms; differentiation; integration; numerical methods | p.21 |

## 2. 公式：须记住 vs 公式册给出

**考纲列为须记住**（P3.2，pp.21–22）：
- Trigonometry：cos²A + sin²A ≡ 1；sec²A ≡ 1 + tan²A；cosec²A ≡ 1 + cot²A；sin 2A ≡ 2 sin A cos A；cos 2A ≡ cos²A − sin²A；tan 2A ≡ 2 tan A/(1 − tan²A)
- Differentiation：sin kx → k cos kx；cos kx → −k sin kx；e^kx → k e^kx；ln x → 1/x；f(x) + g(x) → f′(x) + g′(x)；f(x)g(x) → f′(x)g(x) + f(x)g′(x)（product rule）；f(g(x)) → f′(g(x))g′(x)（chain rule）；aˣ → aˣ ln a
- Integration：∫cos kx dx = (1/k) sin kx + c；∫sin kx dx = −(1/k) cos kx + c；∫e^kx dx = (1/k)e^kx + c；∫(1/x) dx = ln|x| + c，x ≠ 0；∫(f′(x) + g′(x)) dx = f(x) + g(x) + c；∫f′(g(x))g′(x) dx = f(g(x)) + c；∫aˣ dx = aˣ/ln a + c（此行即 Issue 3 更正的一项，见 PDF p.3）
- 加上 P1、P2 的须记公式。

**公式册 P3 节给出**（公式册 pp.4–5；“Candidates sitting Pure Mathematics P3 may also require those formulae listed under Pure Mathematics P1 and P2.”）：
- Logarithms and exponentials：e^(x ln a) = aˣ
- Trigonometric identities：sin(A ± B) ≡ sin A cos B ± cos A sin B；cos(A ± B) ≡ cos A cos B ∓ sin A sin B；tan(A ± B) ≡ (tan A ± tan B)/(1 ∓ tan A tan B)，(A ± B ≠ (k + ½)π)；以及 sin A + sin B、sin A − sin B、cos A + cos B、cos A − cos B 四个 sum-to-product 公式
- Differentiation：tan kx → k sec²kx；sec x → sec x tan x；cot x → −cosec²x；cosec x → −cosec x cot x；quotient rule f(x)/g(x) → (f′(x)g(x) − f(x)g′(x))/(g(x))²
- Integration (+ constant)：sec²kx → (1/k) tan kx；tan x → ln|sec x|；cot x → ln|sin x|

注意：
- **倍角公式要背**（不在公式册）；**复角公式在公式册**。
- **quotient rule 在公式册**，product rule 与 chain rule 要背。
- sec x、cosec x、cot x 的导数在公式册里，但 4.2 写明 “Differentiation of cosec x, cot x and sec x are required”，即要会推导或使用。
- 公式册 P3 节印了四个 sum-to-product（factor formulae），P3 考纲 2.3 的条目文字没有提到它们；本登记不判断它们是否会被单独考查（未用真题核实，记为缺口）。

## 3. 考纲条目（P3.3 Unit content）

### 1. Algebra and functions

**1.1 Simplification of rational expressions including factorising and cancelling, and algebraic division** — p.23
- 要求：有理式化简（因式分解后约分）与代数除法；“Denominators of rational expressions will be **linear or quadratic**”，例 1/(ax + b)、(ax + b)/(px² + qx + r)、(x³ + 1)/(x² − 1)。

**1.2 Definition of a function. Domain and range of functions. Composition of functions. Inverse functions and their graphs** — p.23
- 要求：函数是从 ℝ（或 ℝ 的子集）到 ℝ 的 **one-one 或 many-one mapping**；使用记号 f : x ↦ 与 f(x)；“Students should know that **fg will mean ‘do g first, then f’**”；知道若 f⁻¹ 存在，则 f⁻¹f(x) = ff⁻¹(x) = x；domain、range、composite、inverse 及反函数图像。

**1.3 The modulus function** — p.23
- 要求：能画 y = |ax + b|，以及给出 y = f(x) 图像时画 y = |f(x)| 与 y = f(|x|)；例：画 y = |2x − 1| 并用图像解方程 |2x − 1| = x + 5 或不等式 |2x − 1| > x + 5。

**1.4 Combinations of the transformations y = f(x) as represented by y = af(x), y = f(x) + a, y = f(x + a), y = f(ax)** — p.23
- 要求：给出 y = f(x) 的图像，画 y = 2f(3x)、y = f(−x) + 1 等；画 y = 3 + sin 2x、y = −cos(x + π/4) 等。
- 排除：“**The graph of y = f(ax + b) will not be required.**”

### 2. Trigonometry

**2.1 Knowledge of secant, cosecant and cotangent and of arcsin, arccos and arctan. Their relationships to sine, cosine and tangent. Understanding of their graphs and appropriate restricted domains** — p.23
- 要求：sec、cosec、cot 与 arcsin、arccos、arctan 的定义、与 sin/cos/tan 的关系、图像与反三角函数的 restricted domains；“Angles measured in both **degrees and radians**.”
- 范围：反三角函数的求导与积分属 FP3 3.2、4.2（p.41–42）。

**2.2 Knowledge and use of sec²θ = 1 + tan²θ and cosec²θ = 1 + cot²θ** — p.23
- 公式：两式须记住（p.21）。

**2.3 Knowledge and use of double angle formulae; use of formulae for sin(A ± B), cos(A ± B) and tan(A ± B) and of expressions for a cos θ + b sin θ in the equivalent forms of r cos(θ ± a) or r sin(θ ± a)** — p.24
- 要求：To include application to **half angles**；能在给定区间解 a cos θ + b sin θ = c，能证明 cos x cos 2x + sin x sin 2x ≡ cos x 这类恒等式。（考纲把 R 形式中的角写作 a，不是 α。）
- 排除：“Knowledge of the **t (tan ½θ) formulae** will not be required.”
- 公式：倍角公式须记住（p.21）；复角公式在公式册（p.4）。

### 3. Exponentials and logarithms（考纲小标题印作 “Exponential and logarithms”）

**3.1 The function eˣ and its graph** — p.24
- 要求：To include the graph of y = e^(ax + b) + c。

**3.2 The function ln x and its graph; ln x as the inverse function of eˣ** — p.24
- 要求：“Solution of equations of the form e^(ax + b) = p and ln(ax + b) = q is expected.”

**3.3 Use logarithmic graphs to estimate parameters in relationships of the form y = axⁿ and y = kbˣ** — p.24
- 要求：画 log y 对 log x 得直线，intercept 为 log a、gradient 为 n；画 log y 对 x 得直线，intercept 为 log k、gradient 为 log b。

### 4. Differentiation

**4.1 Differentiation of e^kx, ln kx, sin kx, cos kx, tan kx and their sums and differences** — p.24
- 公式：sin kx、cos kx、e^kx、ln x 的导数须记住（p.22）；tan kx 的导数在公式册（p.4）。

**4.2 Differentiation using the product rule, the quotient rule and the chain rule** — p.24
- 要求：“Differentiation of **cosec x, cot x and sec x** are required.”；对由标准函数经乘积、商、复合得到的函数熟练求导，例 2x⁴ sin x、e^(3x)/x、cos x²、tan²2x。
- 公式：product rule、chain rule 须记住（p.22）；quotient rule 在公式册（p.4）。

**4.3 The use of dy/dx = 1/(dx/dy)** — p.24
- 要求：例：x = sin 3y 时求 dy/dx。
- 范围：一般的 implicit differentiation 属 **P4 5.1**。

**4.4 Understand and use exponential growth and decay** — p.24
- 要求：熟悉 ‘initial’、‘meaning when’ t = 0 等术语；可能要讨论 t 很大时的行为，或判断模型预测的取值范围是否合理；“Consideration of a **second improved model** may be required.”；“Knowledge and use of the result d/dx(aˣ) = aˣ ln a is expected.”
- 公式：d/dx(aˣ) = aˣ ln a 须记住（p.22）；e^(x ln a) = aˣ 在公式册（p.4）。
- 范围：建立并解微分方程属 **P4 5.2、6.4**。

### 5. Integration

**5.1 Integration of e^kx, 1/xⁿ, sin kx, cos kx and their sums and differences** — p.25
- 要求：To include integration of standard functions such as sin 3x、e^5x、1/(2x)。（条目原文印作 1/xⁿ；guidance 的例子 1/(2x) 即 n = 1 的情形，结果为 ln。）
- 公式：∫cos kx、∫sin kx、∫e^kx、∫1/x = ln|x| + c 须记住（p.22）。

**5.2 Integration by recognition of known derivatives to include integrals of the form ∫f′(x)/f(x) dx = ln(f(x)) + c and ∫f′(x)[f(x)]ⁿ dx = [f(x)]ⁿ⁺¹/(n + 1) + c** — p.25
- 要求：例如积分 tan x、sec²2x；“Students are expected to be able to use **trigonometric identities to integrate**, for example, sin²x, tan²x, cos²3x.”
- 公式：∫tan x = ln|sec x|、∫sec²kx、∫cot x 在公式册（p.5）；∫f′(g(x))g′(x) dx = f(g(x)) + c 须记住（p.22）。
- 被引用：P4 6.3 的 guidance 指回本条（“see P3 section 5.2”），如 ∫x/(x² + 5) dx、∫2/(2x − 1)⁴ dx。
- 范围：P3 没有 substitution、by parts、partial fractions 积分，也没有旋转体体积与微分方程（这些属 **P4 6**）；P2 的定积分与面积（P2 8.1–8.2）作为先修可与 P3 的新函数结合出题。

### 6. Numerical methods

**6.1 Location of roots of f(x) = 0 by considering changes of sign of f(x) in an interval of x in which f(x) is continuous** — p.25
- 要求：在 f(x) 连续的区间内用变号确定根的位置（guidance 空白）。

**6.2 Approximate solution of equations using simple iterative methods, including recurrence relations of the form xₙ₊₁ = f(xₙ)** — p.25
- 要求：“Solution of equations by use of iterative procedures, **for which leads will be given**.”（迭代式会在题中给出或给出引导。）

## 4. 与相邻单元的界线

| 内容 | P3 做到哪里 | 属于哪个单元（考纲出处） |
|---|---|---|
| 有理式 | 化简、约分、代数除法，分母为一次或二次（1.1） | 部分分式分解 → **P4 2.1**（p.27）；P2 只除以 (ax ± b)（P2 2.1） |
| 图像变换 | 组合变换、modulus 图像（1.3–1.4）；y = f(ax + b) 不要求 | 单一变换在 **P1 1.12**；含 modulus 的代数不等式 → **FP2 1.1**（p.37） |
| 三角 | 六个三角函数、反三角函数、Pythagorean 恒等式、复角、倍角、半角、R 形式（2.1–2.3）；t 公式不要求 | 基本恒等式与简单方程在 **P2 6**；反三角函数的求导 → **FP3 3.2**，其积分 → **FP3 4.2**（pp.41–42）；三角换元积分 → **FP3 4.3**；De Moivre、cos nθ 用幂表示 → **FP2 3.2**（p.37） |
| 指数与对数 | eˣ、ln x、对数作图估参数、指数增长衰减（3.1–3.3、4.4） | 指数律与 aˣ = b 在 **P2 5**；hyperbolic functions → **FP3 1**（p.41） |
| 求导 | 标准函数、product／quotient／chain、dy/dx = 1/(dx/dy)（4.1–4.3） | implicit 与 parametric differentiation、connected rates of change → **P4 5.1–5.2**（p.27）；三阶及更高阶导数、Maclaurin → **FP2 6**（p.38） |
| 积分 | 标准函数、识别导数形式、用三角恒等式变形后积分（5.1–5.2） | 换元、分部、部分分式积分、旋转体体积、可分离变量微分方程、参数曲线下面积 → **P4 6.1–6.5**（p.28）；hyperbolic 与 reduction formulae → **FP3 4**（p.42） |
| 数值方法 | 变号定位根、给出引导的迭代 xₙ₊₁ = f(xₙ)（6.1–6.2） | 梯形法在 **P2 8.3**；interval bisection、linear interpolation、Newton-Raphson → **FP1 3.1**（p.33）。FP1 只以 P1、P2 为先修，所以把“用变号定位根”作为额外先修单独列出（p.30） |
| 被其他单元依赖 | — | P4、FP2、FP3、M2、M3 的先修都包括 P3（pp.26、36、40、47、50）；S2 公式册注明可能用到 P1–P4 公式（公式册 p.18） |

## 5. 往届真题

2018 考纲下 WMA13 的试卷、MS、ER 收集情况见 `../../inventory/pure.json` 与 `../../inventory/pure-gaps.md`。逐题索引见同目录 `WMA13.questions.json`（19 份卷、178 题，2020-01 至 2025-10，含 2025-06、2025-10 的 /01A），来源与缺口说明见 `WMA13.coverage.part1.md`、`WMA13.coverage.part2.md`；真题需求概览见第 6 节。注意：`pure-gaps.md` 把 2020-01 至 2021-10 的 QP／MS 记为缺失，后来已在 GitHub `RayZ3R0/papernexus-finder` 找到并核实（见 `WMA13.coverage.part1.md`“New sources found in this pass”）。

## 6. 真题需求概览

**数据与口径**。依据同目录 `WMA13.questions.json`（2026-10-06 由 `WMA13.questions.part1.json` + `part2.json` 合并并审计，审计记录见 6.5）：19 份卷 = WMA13/01 的 17 个考季（2020-01 至 2025-10；2020-06 取消，那份卷按 Pearson 归档记作 2020-10）+ 2025-06 /01A + 2025-10 /01A，共 178 题、500 小问、1425 分。19 份卷都有 QP 和 MS；ER 只有 5 份（2022-10、2023-01、2023-06、2023-10、2024-01），所以“考生怎么丢分”只能从这 5 份报告里取，其余卷只能看 MS 写明的评分规则。2026-01、2026-06（/01 与 /01A）在所有可达来源里都没找到，不在统计内（见 `WMA13.coverage.part2.md` §3）。

引用写法：`2023-01 Q5(b)` 指 2023 年 1 月 WMA13/01 第 5 题 (b)；`2025-06A` 指 /01A 卷；`MS 2022-06 Q8(a)`、`ER 2024-01 Q2(a)` 指该卷的评分方案或考官报告中对应题的部分。一个小问可以挂多个条目，各条目分别计数。“主考”= 该小问 spec 列表排第一的条目；“涉及分值”= 挂了该条目的小问分值之和（多条目小问重复计）；“主考分值占比”= 只按主考条目计、合计 1425 分的占比；“卷”= 19 份卷中出现该条目的份数。

### 6.1 卷面结构

- 每卷 8–10 题、75 分、全部必答；单题 3–14 分（中位 8），小问 1–7 分（中位 3；2 分 156 问、3 分 141 问、4 分 101 问）。最后一题 7–14 分：19 份中 9 份是三角（2.x），8 份是求导或指数模型（4.x），另 2 份是代数除法加积分（2020-10 Q9，14 分）和模函数（2025-06 Q10）；最大的单题是 2020-10 Q9 与 2024-10 Q9（各 14 分）。
- 命令词（全部 500 小问）：Find 236，Show that 88（另有 Prove 9、Show 4），Hence find 30，State 24，Solve 21，Hence solve 16，Sketch 15，Express 13，Write／Write down 14，Calculate 7，Interpret 4。“Show that／Prove”约占五分之一，几乎都是给定答案（A1\*）。
- 主考分值占比：2.3 13.0%，4.2 12.8%，1.2 10.3%，1.3 10.3%，4.4 7.2%，4.3 6.2%，5.2 5.9%，3.3 5.6%，4.1 5.4%，6.2 4.6%，2.1 4.1%，1.1 3.6%，2.2 2.4%，5.1 2.4%，1.4 2.2%，6.1 2.0%，3.2 1.5%，3.1 0.4%。前四项（三角变形、求导法则、函数、模函数）合占约 46%。
- 19 份卷每份都有：一道函数题（1.2：反函数、复合、值域）；至少一问模函数（1.3）；一道复角／倍角／R 形式题（2.3）；一道情境模型（18 份是指数模型或对数线性模型，挂 4.4、3.2、3.3；2022-10 的情境题是含 ln 的利润模型 Q5，4.4 只出现在 Q4(b) 的 10ʸ 求导）；一道迭代题（6.2）；至少一处乘积／商／链式法则（4.2）。
- 不许依赖计算器的要求逐年增多。QP 中 “calculator technology” 出现的处数（题首 banner 或小问括注）：2020-01 为 0，2020-10 为 1（当时写作 graphical or numerical methods），2021-01 至 2022-01 每卷 1–2 处，2022-06 起每卷 3–8 处；题首整题 banner（In this question you must show all stages of your working）2022-06 起每卷 2–6 题，2025-10 最多（6 题）。这类题的评分规则见 6.4 第 1 条。
- 第 1 题没有固定题型：函数、变换或模函数 6 次（2023-01、2024-01、2024-06、2025-06、2025-06A、2025-10），求导 3 次（2021-06、2022-01、2022-06），变号定根 3 次（2023-06、2023-10、2025-01），有理式化简后接反函数或积分 2 次（2021-10、2022-10），积分 2 次（2021-01、2025-10A），三角方程 2 次（2020-10、2024-10），指数模型 1 次（2020-01）。

### 6.2 各条目怎么考

**1.1 Rational expressions, algebraic division**（17/19 卷；18 题 22 小问，主考 14；涉及 86 分；小问中位 4，范围 2–6）
- 命令词：Find 10，Show that 9，Write 3。
- 考法：(a) 两个分式通分、分解因式后约分，show 成给定的最简式，再接反函数或求导：2021-01 Q3(a)、2021-10 Q1(a)、2024-01 Q4(a)、2025-06 Q4(a)。(b) 代数除法写成 Ax + B + C/(x − a)、Ax² + Bx + C + D/(x + 3)²、Ax + B + (Cx + D)/(x² + 4) 等，紧接着积分（5.2）或求切线：2020-01 Q8(ii)、2020-10 Q9(a)、2021-06 Q3(ii)(a)、2022-10 Q1(a)、2023-01 Q4(a)、2024-06 Q2(a)、2024-10 Q9(c)、2025-01 Q4(a)、2025-06A Q4(a)、2025-10A Q3(a)。
- 答案形式：给定的最简式（要看到用于约分的因式）；整数常数 A、B、C；“show D = 0” 一类的给定值。

**1.2 Functions: domain, range, composite, inverse**（19/19；31 题 67 小问，主考 62；涉及 163 分；中位 2，范围 1–4）
- 命令词：Find 45，Hence find 6，State 5，Solve 4，Sketch 2。
- 考法：反函数 f⁻¹（约 26 小问，常另给 1 分要定义域，如 2021-01 Q3(c)、2022-10 Q2(b)(ii)）；复合函数求值或解方程 fg(a)、ff(6)、gf(a) = 7（约 21 小问：2023-10 Q2(a)(c)、2024-10 Q6(c) 解 gg(x) = 126、2022-06 Q2(c) 解 f(1/a) = g(a + 3)）；值域（约 19 小问），包括 R 形式函数的值域（2020-01 Q9(c)、2021-06 Q9(c)）和由驻点求值域（2022-06 Q6(d)、2024-10 Q7(c)、2025-01 Q9(c)）；f⁻¹(x) = f(x)（2020-01 Q2(c)、2025-06 Q1(d)）；在同一坐标系画 f⁻¹（2021-06 Q4(c)、2023-06 Q4(b)）。函数题多排在卷首：2023-01 Q1、2025-06 Q1、2025-10 Q1、2020-01 Q2、2022-06 Q2、2022-10 Q2、2023-10 Q2。
- 答案形式：f⁻¹(x) = …（以 x 为自变量）连同定义域；值域用 f(x)、y 或区间记号，端点开闭要对；精确值。

**1.3 The modulus function**（19/19；21 题 59 小问，主考 50；涉及 163 分；中位 2，范围 1–6）
- 命令词：Find 30，State 9，Solve 9，Sketch 7，Write down 2。
- 考法：每卷至少一问，16 份卷是 y = a|bx + c| + d 或 y = a − |bx − c| 型（例外：2023-10 Q9 的 |2 − 4 ln(x + 1)|、2024-10 Q3 的 2x² − 10x 取 f(|x|) 与 |f(x)|、2025-06A Q8 的分式 |g(x)|）。套路是：顶点和截距（1–2 分）→ 解方程或不等式（与直线相交，3–5 分）→ 交点个数对应参数 k 的范围（2020-01 Q6(c)、2020-10 Q4(c)、2022-06 Q5(c)、2025-06 Q10(c)、2025-06A Q8(d)、2025-10A Q6(d)）。常带参数 a、k，要“用 a、k 表示”（2021-01 Q4、2021-06 Q6、2022-06 Q5、2023-01 Q6、2024-01 Q8、2025-01 Q7、2025-06 Q10）。y = |f(x)| 与 f(|x|)：画 |f(x)| 2022-01 Q7(c)、2025-06A Q8(c)；解 f(|x|) = 0 或 48（2023-06 Q6(d)、2024-10 Q3(a)）；解 |f(x)| ≥ (5/2)x（2024-10 Q3(b)）。与三次曲线、对数函数合题：2025-10 Q8、2023-10 Q9。
- 答案形式：坐标（截距要写成坐标或 y = …）；参数的最简式；不等式解集写成一条完整的陈述（见 6.4 第 6 条）。

**1.4 Combined transformations**（12/19；16 题 22 小问，主考 17；涉及 47 分；中位 2，范围 1–6）
- 命令词：Find 11，Sketch 5，Describe 2，State 2。
- 考法：给一点求它在 y = 2f(3x) + 8、3f(x − 1)、f(x − 2) + 8 下的像（1–2 分：2024-01 Q1(a)(b)、2024-06 Q1(c)、2024-10 Q7(d)、2025-01 Q6(c)、2025-06A Q1(a)(b)）；由变换后的顶点反求 a、b（2020-10 Q4(d)、2021-10 Q2(d)）；画一般曲线的 y = 3f(2x)、y = f(−x) − 1（只有 2021-01 Q2）；描述 cos θ 变成 R cos(θ + α) 的伸缩与平移（只有 2020-01 Q9(b)）；R 形式函数变换后的最值点（2022-10 Q8(c)(d)）；变换后的值域（与 1.2 同挂）。
- 答案形式：坐标；a、b 的值；草图要标截距与转折点。

**2.1 sec, cosec, cot; arcsin, arccos, arctan**（18/19；31 题 44 小问，主考 19；涉及 153 分；中位 4，范围 1–6）
- 命令词：Show that 14，Hence solve 8，Find 6，Prove 4，Solve 4。
- 考法：含 sec、cosec、cot 的恒等式证明与方程（2022-01 Q2、2022-06 Q7、2023-01 Q5、2023-10 Q8、2025-01 Q8(i)、2025-06A Q7、2025-10A Q5）；求导后出现的 arctan／tan 形式，引出迭代（2020-01 Q7(b) arccos、2021-01 Q6(b)、2021-06 Q1(a)、2025-06 Q7(a)）；精确值 arcsin／arccos（2023-10 Q10(a)、2025-01 Q10(c) b = ½arccos(√5/3)、2025-06 Q9(a)）；画 y = arcsin(x/2)（2021-10 Q8(a)，唯一一次作图）。
- 答案形式：给定恒等式；角度 1 d.p. 或弧度 3 s.f.、区间内全部解；精确的反三角表达式。

**2.2 sec²θ = 1 + tan²θ, cosec²θ = 1 + cot²θ**（11/19；12 题 13 小问，主考 7；涉及 58 分；中位 4，范围 3–6）
- 命令词：Hence solve 5，Show that 4，Solve 3，Prove 1。
- 考法：用这两个恒等式把方程化成 tan、sec、cot 或 cosec 的二次方程再解：2021-01 Q7(b)、2021-06 Q2(b)、2022-01 Q9(i)、2023-06 Q9(b)、2023-10 Q8(b)、2024-10 Q1、2025-06 Q8(b)、2025-06A Q7(c)；证明题中把 sec² 化成 1 + tan²（2020-01 Q5(a)、2022-06 Q7(a)、2023-10 Q8(a)）；x = f(y) 求导时把 sec² 换成 x 的式子（2021-01 Q10(b)、2023-01 Q7(a)）。
- 答案形式：区间内全部解（角度 1 d.p. 或弧度 3 s.f.）；二次方程的另一个根若无解（如 sec θ = 2/3）要舍去或可忽略（2024-10 Q1）。
- 口径：只用到 sin² + cos² = 1 的小问不挂 2.2（审计时改正了 6 处，见 6.5）。

**2.3 Double angle, compound angle, R 形式**（19/19；40 题 84 小问，主考 59；涉及 275 分，最多；中位 3，范围 1–6）
- 命令词：Show that 16，Hence solve 14，Find 14，Express 10，Prove 8，Hence find 4。
- 考法：(a) R 形式：Express as R cos(x ± α) 或 R sin(x ± α)（10/19 卷：2020-01 Q9、2020-10 Q7、2021-06 Q9、2022-10 Q8、2023-01 Q2、2024-06 Q4、2025-06 Q2、2025-06A Q5、2025-10 Q4、2025-10A Q8），随后求由它构成的函数的最值及取最值的 x（如 g(x) = 3 − 7f(2x)、15/(41 + 16 sin x − 30 cos x)、18/(f(3x) + 4√3)），或情境模型（海鸟高度 2020-10 Q7、摩天轮 2025-10A Q8）；另有 2 次在解方程时自己想到用 R 方法（2022-06 Q9(b)、2024-01 Q9(b)）。(b) 证明恒等式再 hence solve：三倍角与四倍角（sin 3x 2020-10 Q5、2024-10 Q5；tan 3x 2025-06 Q8；sin 4θ 2025-06A Q7）、倍角化简（2021-06 Q2、2022-01 Q9(ii)、2022-10 Q9、2024-01 Q9、2025-10 Q9）。(c) 复角：2021-10 Q4、2023-10 Q3(a)（由 cos(A + B) 证 cos 2A）、2024-06 Q7、2025-01 Q8(ii)（认出 tan(2x − 70°)）。(d) 为积分做准备：sin³x、cos²3x、sin²3x、(1 + 2cos 2x)²、(2cos x − sin x)²（见 5.1）。
- 答案形式：R 要精确（√41、5、25），α 按题给精度（弧度 3–4 s.f. 或 d.p.，角度 1–2 d.p.）；区间内全部解，不多不少；给定恒等式。
- 未考：公式册印的四个 sum-to-product（factor）公式在 19 份卷中都没有用到；t (tan ½θ) 公式按考纲不要求，只在 MS 里作为可选解法出现（2022-06 Q9(b)）。

**3.1 eˣ and its graph**（11/19；15 题 20 小问，主考只有 2；涉及 34 分；中位 2，范围 1–3）
- 考法：几乎都是附属标签：模型中 e⁰ = 1 求初值、t → ∞ 时 e^(−kt) → 0 求极限。作为主考只有 2020-10 Q6(a)（解 5e^(x − 1) + 3 = 18，写成 ln k）和 2025-01 Q5(b)（画 H = 280e^(−0.05t) + 24 并写出渐近线，唯一一次要求考生画 e 的图像）。

**3.2 ln x; ln x as the inverse of eˣ**（19/19；36 题 51 小问，主考 11；涉及 158 分；中位 3，范围 1–5）
- 命令词：Find 37，Show that 6，State 3。
- 考法：多数与 4.4 同挂：模型中“何时达到某值”要解 e^(ax + b) = p（2020-01 Q1(b)、2021-06 Q8(c)、2022-01 Q4(b)、2023-06 Q7(c)、2024-01 Q3(b)、2025-01 Q5(c)、2025-06A Q9(c)）；含 ln 的函数：f(x) = 2 + 5 ln x 的反函数（2024-06 Q5、2024-01 Q4(c)、2025-06A Q8(b)）；y = |2 − 4 ln(x + 1)| 的渐近线、截距和不等式（2023-10 Q9）；6√x ln(4x) 与 x 轴的交点（2025-01 Q9(a)）；log₁₀ 反解（2022-10 Q4(a)）；对数不等式定参数（2023-10 Q5(c)、2025-10 Q6(ii)）。
- 答案形式：精确的 ln 形式（ln k、p ln q）或按题给 d.p.／s.f.。考生从未被要求自己画 ln x 的图像。

**3.3 Log graphs for y = axⁿ and y = kbˣ**（16/19；16 题 32 小问，全部主考；涉及 80 分；中位 3，范围 1–4）
- 命令词：Find 16，Show that 5，Interpret 3，Express／Write 4。
- 考法：两类。(a) log y 对 x（y = abᵗ）：2020-10 Q2、2021-01 Q8、2021-06 Q5、2022-01 Q8、2022-06 Q4、2023-01 Q3、2023-10 Q6、2024-01 Q3、2024-06 Q3(ii)（底 3）、2024-10 Q4、2025-01 Q2、2025-10 Q3。(b) log y 对 log x（y = axⁿ）：2020-01 Q3、2021-10 Q7、2023-06 Q2（底 6）、2024-06 Q3(i)（要画 log 图并标截距）、2025-06 Q3。已知条件是直线过两点、斜率和截距，或直接给出 log₁₀S = 4.5 − 0.006t。后续：写出直线方程 → 写成 V = abᵗ（a、b 按题给精度）→ 用模型求值或解释常数（初值、每年比例）→ 情境中求时间。2022-10 与两份 /01A 卷没有这类题。
- 答案形式：方程（不是只给数值）；a、b 按 s.f.／d.p.；解释要带情境（“the initial percentage …”）。

**4.1 Derivatives of eᵏˣ, ln kx, sin kx, cos kx, tan kx**（17/19；40 题 46 小问，主考 24；涉及 166 分；中位 4，范围 1–7）
- 命令词：Find 24，Show that 15，Hence find 4。
- 考法：多与 4.2 同挂。单独主考时：模型的变化率（2023-06 Q7(b)、2024-01 Q5(c)、2025-01 Q5(d) 证 dH/dt = a + bH）；求驻点（2022-06 Q8(a)、2023-10 Q5(b)、2025-10 Q7 求 k 的范围）；最大斜率（2021-10 Q6(ii)(b)）；x = 3 cos 2y 的 dx/dy（2025-01 Q10(a)）；y = ln(1 − cos 2x) 化成 k cot x（2025-10A Q4(a)）。
- 答案形式：最简式；给定形式中的常数；精确坐标。

**4.2 Product, quotient and chain rules**（19/19；51 题 70 小问，主考 54；涉及 243 分；中位 4，范围 1–7）
- 命令词：Find 33，Show that 25（另 Show 3、Prove 1），Hence find 6。
- 考法：(a) 驻点的 x 满足给定方程（常化成 arctan 或 tan 形式，接着迭代）：2020-01 Q4(ii)、2021-01 Q6(b)、2021-06 Q1(a)、2022-06 Q9(a)、2024-06 Q8(b)、2025-06 Q7(a)、2025-10A Q2(a)。(b) 证明 f′(x) 等于给定的因式形式：2022-06 Q6(a)、2023-06 Q8(a)、2023-10 Q7(b)、2024-10 Q7(a)、2025-06A Q6(a)。(c) 增减性：用 f′ 的符号证明单调（2021-10 Q1(c)、2022-01 Q6(a)、2024-01 Q4(b)、2024-06 Q5(b)），或求递增区间（2020-01 Q4(i)(b)、2025-01 Q3）。(d) 切线、法线及其围成的面积（P2 内容，挂 4.2）：2020-10 Q9(b)、2022-06 Q1(b)、2024-01 Q7(c)、2024-06 Q6(a)、2024-10 Q9(b)、2025-10A Q3(b)。
- 答案形式：simplest form；给定形式中的常数；ax + by + c = 0 整系数；精确坐标。

**4.3 dy/dx = 1/(dx/dy)**（14/19；14 题 24 小问，全部主考；涉及 88 分；中位 4，范围 2–6）
- 命令词：Find 13，Show that 9。
- 考法：曲线写成 x = g(y)：sec²2y（2021-01 Q10）、ln sin y（2020-10 Q8(ii)）、sin²2y（2021-06 Q7）、2 sin y（2021-10 Q8）、ye^(2y)（2022-01 Q10）、10ʸ（2022-10 Q4）、tan（2023-01 Q7）、y 的分式（2023-06 Q10、2025-06A Q3）、sin²4y（2023-10 Q10）、sin²y（2024-06 Q9）、y 的二次式（2024-10 Q2）、cos 2y（2025-01 Q10）、sin(3y + π/4)（2025-06 Q9）。一般是先 show dy/dx 等于只含 x 的给定式（9 小问），再求切线、法线、平行于 y 轴的切线（dx/dy = 0：2023-06 Q10(b)、2024-10 Q2(b)）、三角形面积（2024-06 Q9(c)）、dy/dx 的最小值（2023-10 Q10(d)）或参数范围（2022-01 Q10(b)）。
- 答案形式：只含 x 的式子（题目要求时）；精确值；竖直切线写成方程 x = …。

**4.4 Exponential growth and decay**（19/19；28 题 69 小问，主考 47；涉及 152 分；中位 2，范围 1–5）
- 命令词：Find 39，Show that 6，Hence find 6，Interpret 4，State 4，Calculate 3，Explain 2。
- 考法：每卷一道情境模型，常见三类：logistic 型 ae^(kt)/(b + e^(kt))（蟾蜍 2020-01 Q1、鱼 2021-06 Q8、水草 2022-01 Q4、果蝇 2023-01 Q10、松鼠 2025-10 Q5、蜜蜂 2025-10A Q7）；冷却型 A + Be^(−kt)（烤箱 2021-01 Q5、房间 2024-01 Q5、金属 2025-01 Q5、处理器 2025-06 Q6）；增长／衰减与其他（细菌 2023-06 Q7、药量 2022-01 Q8 与 2025-06A Q9、金矿 2021-10 Q3、手机销量 2023-10 Q4、马的心率 2024-10 Q8、高尔夫球 2024-06 Q8、短跑 2022-06 Q8、利润 2022-10 Q5）。小问固定套路：初值（1 分）→ 极限或上限（1 分，并说明为何达不到某值）→ 何时达到某值（ln）→ 某时刻的变化率（必须求导）→ 由导数为 0 求最值 → 解释常数。aˣ 的导数 aˣ ln a 考过 5 次（2021-06 Q5(b)、2022-01 Q8(c)、2022-10 Q4(b)、2024-10 Q4(c)、2025-10 Q3(c)）。
- 答案形式：带单位与情境；按题给 d.p.／s.f.；“nearest whole number”、“years and months”（2021-06 Q8(c)、2021-10 Q3(a)(ii)）。
- 未考：考纲 guidance 提到的 “second improved model” 在 19 份卷中从未出现。

**5.1 Integration of eᵏˣ, 1/xⁿ, sin kx, cos kx**（11/19；13 题 13 小问，主考 9；涉及 52 分；中位 4，范围 2–5）
- 命令词：Find 6，Hence find 5，Show that 2。
- 考法：先用三角恒等式改写再积分：sin³x（2020-10 Q5(b)）、(1 + 2cos 2x)²（2021-10 Q10(b)）、(2cos x − sin x)²（2023-01 Q8）、5 − 4cos²3x（2023-10 Q3(b)）、sin²3x（2025-06 Q5(i)）；拆分成幂函数和（2021-01 Q1）、(t + 1)/t（2025-10A Q1(ii)）；模型中积分 e 项（2022-06 Q8(b)）。
- 答案形式：精确值（含 π、√）；不定积分要 simplest form 和 + c。

**5.2 Integration by recognition (f′/f, f′fⁿ)**（18/19；20 题 27 小问，主考 25；涉及 93 分；中位 4，范围 2–6）
- 命令词：Find 19，Hence find 4，Show that 2。
- 考法：(ax + b)ⁿ（2021-06 Q3(i)、2021-10 Q5(i)、2022-01 Q3(i)、2025-10A Q1(i)(a)）；f′/f → ln（2021-01 Q9(i)、2022-01 Q3(ii)、2022-06 Q3、2025-10 Q6(ii)、2025-10A Q1(i)(b)）；f′fⁿ（2021-01 Q9(ii)、2021-10 Q5(ii)、2023-06 Q3(ii)(b)、2025-06 Q5(ii)）；接在代数除法之后的定积分，答案写成 p + q ln r（2020-10 Q9(c)、2021-06 Q3(ii)(b)、2022-10 Q1(b)、2024-06 Q2(b)、2024-10 Q9(d)、2025-01 Q4(b)、2025-06A Q4(b)）；曲线、法线与 x 轴围成的面积（2024-06 Q6(b)、2024-10 Q9(d)）；由定积分的值反求常数 k（2022-06 Q3(b)、2025-10 Q6(ii)）；cosec x cot x（2023-06 Q9(c)）。
- 答案形式：按题给形式的精确值（p + ln q、α + β ln 3）；对数要合并；不定积分 + c 与括号。
- 未考：公式册 P3 节的 ∫tan x、∫sec²kx、∫cot x 从未直接出现。

**6.1 Locating roots by sign change**（14/19；14 题 14 小问，全部主考；涉及 29 分；每问 2–3 分）
- 命令词：全部是 Show that。
- 考法：两种。(a) 根在 [a, b] 内（10 次，如 2020-01 Q7(a)、2023-06 Q1(a)、2024-01 Q2(a)、2025-01 Q1(a)）；(b) 根等于给定的 3 或 4 位小数：取包住它的窄区间（2020-10 Q6(b)、2021-01 Q6(d)、2025-06 Q7(c)、2025-10A Q2(c)）。
- 答案形式：两端函数值（至少 1 s.f.）、变号、连续、结论（窄区间版本见 6.4 第 3 条）。

**6.2 Iteration xₙ₊₁ = f(xₙ)**（19/19；19 题 33 小问，主考 30；涉及 76 分；中位 2，范围 1–4）
- 命令词：Find 22，Show that 9。
- 考法：每卷一题。先 show f(x) = 0 可改写成 x = g(x)（9 次，如 2022-10 Q5(c)、2023-01 Q9(d)、2024-01 Q2(b)、2025-10 Q2(b)），再由 x₁ 算 x₂、x₃ 或 x₆，最后“by repeated iteration”给出根。迭代式常含 arctan、arccos、ln、e 或根号；根常有情境含义（盈利所需月数 2022-10 Q5(e)、球的水平距离 2024-06 Q8(c)、跑完全程的时间 2022-06 Q8(c)）。
- 答案形式：按题给 d.p.（多为 3 或 4 位，2020-10 Q6(c) 要 6 位）；x₂ 一般 awrt，后面的项常是 cao。

### 6.3 尚未考过或极少考的考纲内容

18 个条目都考过，每个条目至少出现在 11 份卷里（最少的是 2.2、3.1、5.1，各 11 份；1.4 为 12 份）。以下是条目内部从未考过或只考过一两次的点：

- **sum-to-product（factor）公式**（公式册 P3 节）：0/19。
- **sec、cosec、cot 的图像**：从未要求作图；反三角函数只画过一次（2021-10 Q8(a) y = arcsin(x/2)）。
- **ln x 的图像**：考生从未被要求作图；eˣ 型图像只画过一次（2025-01 Q5(b)）。
- **y = f(|x|) 的作图**：只考过解方程（2023-06 Q6(d)、2024-10 Q3(a)），没画过。
- **一般曲线的组合变换作图**：只有 2021-01 Q2；用文字描述伸缩与平移只有 2020-01 Q9(b)。其余变换题都只求点的像。
- **∫tan x、∫sec²kx、∫cot x**（公式册给出）：0/19；用三角恒等式积分 tan²x 也从未出现（sin²、cos²、sin³ 出现过）。
- **4.4 “second improved model”**：0/19。
- **半角**：只以 cos(x/2)、tan(x/2) 作函数的自变量出现（2021-06 Q1、2025-10A Q2），没有专门的半角恒等式题。
- **x 的负整数幂（n ≥ 2）的积分**：只有 2021-01 Q1（x⁻³ 项）；其余负幂积分都是 (ax + b)⁻ⁿ 形式（2020-01 Q8(ii)、2021-06 Q3(i)、2021-10 Q5(i)、2023-01 Q4(b)），按“识别导数”计入 5.2。

### 6.4 反复出现的评分惯例与考官提醒

以下来自 19 份 MS 和 5 份 ER，引用格式为“MS／ER 卷 题号”。只在引号内是原文短引。

1. **不许依赖计算器的题，必须写出过程，只写答案得 0 分或特殊分。** MS 2022-06 Q8(a)：“awrt 6.97 and awrt 11.9 with no calculus scores 0 marks”；MS 2024-10 Q8(c)：从导数直接写 T = 1.158 只得 1,1,0,0,0；MS 2023-06 Q10(b)：题目要求用 (a)，没有令 dx/dy = 0 的过程得 0/4；MS 2025-10 Q8(d)：完全没有过程的正确答案不得分；MS 2025-01 Q1(c)：迭代只写 0.1622…（计算器解出的值）判 M0A0A0。ER 2023-01 Q5(b) 与 ER 2024-01 通则（8(c)）都批评了无视 banner 直接用计算器。
2. **Show that、Prove 与给定答案（A1\*）。** 要写出关键的中间行，并有结论，不能直接跳到印好的答案：MS 2021-06 Q1(a) 要看到 tan(x/2) = 4/x 这一步；MS 2022-06 Q9(a) 只用商法则分子 vu′ − uv′ 的，最高 M1A0dM1A0；MS 2025-06 Q4(a) 约分用到的因式必须在分式里写出来；MS 2024-06 Q9(b) 要先写出未化简的 sin y、cos y 关于 x 的表达式。ER 2023-01 Q5(a)：show that 题 “all steps should be demonstrated”；ER 2023-10 Q3(a)：直接引用倍角公式去证倍角公式属循环论证，不得分。
3. **变号定根要写“连续”。** 两端的值、变号、连续、结论缺一不可。ER 2022-10 Q5(b)：漏写 continuity 是最常见的错误，“the case for the past few series”；ER 2024-01 Q2(a)：“Despite it being highlighted in every appropriate series”仍常丢这一分，还出现“the interval is continuous”这类错误说法；ER 2023-06 Q1(a)、ER 2023-10 Q1(a) 同样提醒。例外：证明根等于某个给定小数时（窄区间），MS 不要求提连续性，用反复迭代代替变号得 0 分（MS 2025-10A Q2(c)、MS 2025-06 Q7(c)）。
4. **迭代值按题给小数位数写，后面的项不是 awrt。** MS 2020-01 Q7(b)：x₅ = 0.8110，“0.811 is A0”；MS 2021-06 Q1(b)：x₆ = 2.155，“this is not awrt”；ER 2022-10 Q5(d)：有考生把 t₆ 写成 6.13。用角度制算出 x₂ ≈ 127 仍可得第一个 M 分（MS 2021-06 Q1(b)）。
5. **反函数要带定义域；值域写成 f(x) 或 y 的范围。** ER 2023-10 Q2(b)：定义域最常漏写，或误写成 x ≠ 4；ER 2023-01 Q1(c) 同样；MS 2025-01 Q6(a)：多写排除值即 B0。值域写成 x 的范围要扣分：MS 2022-01 Q6(c)(ii) 写 5 < x < 22 只得 B1B0；端点开闭要对：MS 2024-06 Q5(d) 上界必须是严格不等号；ER 2023-10 Q7(a) 漏掉 0 或开闭写错。
6. **模函数：两种情形都要解，舍去不合条件的根，答案写成一条完整陈述。** MS 2024-10 Q3(b)：“x ≤ 15/4 and x ≥ 25/4”、“25/4 ≤ x ≤ 15/4”判错，两段要“brought together on a single line”；ER 2022-10 Q7(d)：多给的解丢最后两分，x = 24 未舍；ER 2023-10 Q9(c)：忽略 x > −1 的限制，最后一分只有约十分之一的人拿到；MS 2022-10 Q7(a)(ii)：只写 −17 不写成 (0, −17) 或 y = −17 判 B0。
7. **R 形式：R 精确，α 按题给精度；最值要看整个表达式。** MS 2020-01 Q9(a)：R = √41，“Do not allow decimals for this mark”；ER 2023-01 Q2(b)：最常见的错误答案是 3 − 7√5，正确做法是让 cos(2x − α) = −1；ER 2024-01 Q9(b)：把 5 sin(2x − 0.927) 写成 5 sin(2x + 0.927)。
8. **三角方程：区间内全部解、不多不少、单位一致。** ER 2023-01 Q5(b)：最常见的丢分是漏掉负根；ER 2023-10 Q8(b)：多写了 180°；ER 2023-06 Q9(b)：π/4 只写成 0.785（题目要求精确时丢分）；MS 2025-06A Q7(c)：区间内有多余的解则扣最后的 A 分。
9. **情境指数模型：变化率要求导，单位与数量级要对。** ER 2023-06 Q7(b)：把 t = 5 代入 N 或算平均变化率，均不得分；ER 2024-01 Q5(c)：典型错误答案 17.89（直接代入）；ER 2023-10 Q4(c)：dN/dt 仍以千为单位，4.73 要写成 4730；ER 2023-10 Q6(c)：q 要解释成每年的比例变化，这是全卷得分率最低的一分。初值与极限的说法：MS 2020-01 Q1(c) 要说明“上限是 450”并下结论，只写“the limit is 450”判 B0。
10. **对数图像题：用题目的底，写出指数律的一步。** MS 2021-10 Q7(b)：用 ln 判 B0，未写出加法律也判 B0；MS 2021-01 Q8(a)：log P = log a × t log b、10^0.68 + 10^0.09t 都算错误过程；MS 2024-06 Q3(ii)：写 3⁴ + 3^(2t) 判 M0；MS 2025-10 Q3(b)：最后要写出方程，不能只给 a、b 的值。
11. **积分：+ c、ln 的括号、题目要求的形式；“hence”要用上一问。** MS 2025-06A Q4(b)：“+ 2 ln 2 is A0”（要求 α + ln β 的形式）；MS 2022-06 Q3：(a) 漏了系数会封顶 (b) 的分；MS 2023-06 Q3(ii)(b)：只写答案得 0 分；ER 2023-06 Q9(c)：没有认出公式册里的 cosec x cot x 结果；ER 2023-10 Q3(b)：不用 (a) 的恒等式直接硬算。
12. **求导法则要对，化简要彻底。** MS 2021-06 Q1(a)：写出的乘积法则必须正确；ER 2024-01 Q7(a)：把分母 9(3x − k) 展开后求导常出错；ER 2023-10 Q5(a)：对 ln(x² + k) 求导时不用链式法则；ER 2023-01 Q9(a)：有人把 e^(x²) 当成 e^(2x) 处理，较弱的考生链式求导漏项；MS 2023-06 Q10(a)：公因子 3 必须约去才给最后的 A 分。
13. **x = f(y) 型：整个导数取倒数，答案化成只含 x。** MS 2025-01 Q10(b)：题目写 hence，用 arccos 求导公式直接得出答案不给分；ER 2023-06 Q10(b)：平行于 y 轴的切线要写成方程 x = …，只给坐标丢分。
14. **精确值与过早取整。** MS 通则：要求精确值时 “marks will normally be lost if the candidate resorts to using rounded decimals”（如 MS 2025-10 通则）；MS 2024-01 Q7(b)：k = 7/3、11/3 可写成循环小数，但 2.33、3.67 不行；ER 2023-06 Q7(a)：k 要 4 s.f.，写 0.173 而非 0.1733 丢分。

### 6.5 审计记录（2026-10-06）

- **合并与校验**：`work/wma13audit/scripts/merge_validate.py` 合并两个 part 文件（178 题，无重复 id），按 series → paper → 题号排序写出 `WMA13.questions.json`。校验项：字段齐全、无多余字段；series 为 YYYY-MM；paper 为 WMA13/01 或 WMA13/01A；id 与 series、paper、题号一致；每题小问分值之和 = 题目总分；每卷 75 分、题号连续；每个 spec id 都在 `spec-items.pure.json` → `WMA13` 中；有 ms／er 文字的题有对应来源。结果 0 错误。另用 `markcheck.py` 逐题核对 QP 印刷的 “Total … marks” 与各小问 “(n)”（小问只拆分印刷分组、不跨组）：178/178 一致。`numcheck.py` 核对 ms 与 final_form 中的小数答案都出现在 MS／QP 原文里，13 处不在原文的值逐一复算（如 0.24/8、135/16 = 8.4375、cos θ = −1/3 → 109.5°、250.5°），都正确。MS／ER 页码引用 350 处，全部在对应 PDF 页数之内；43 个 `local:src/WMA13/…` 来源文件都存在，且 series、paper、类型与条目一致。
- **完整性**：对照 `inventory/pure.json`、`inventory/finder.json`（Edexcel-Finder 2020-01 至 2025-01 的 15 份 + SAM）、`inventory/pure-coverage.json`、`versions.json`（预期考季 2020-01 至 2026-06）和 `pure-gaps.md`：凡有 QP 文本的卷（19 份）都已索引；SAM 不是考季，不收。所有来源都缺的卷：2026-01 WMA13/01 与 /01A、2026-06 WMA13/01 与 /01A（QP、MS、ER 都没有；本轮再次查了 Drive：标题含 P3／WMA13 或全文含 WMA13/01 且创建于 2026-01-10 之后的文件，标题含 26_01、26_06、2601、2606 的文件，只找到 WMA14、WST01 的 2026 卷；GitHub `EslamAhmedGaber/elite-igcse-math` HEAD 仍为 05b0320，没有 WMA13）。/01A 是否在 2026-01、2026-06 开考未核实（中国考点时间表列出了全部 14 个单元的 A 代码，见 `versions.json` → `regional_01A`）。ER 缺 14 份：2020-01 至 2022-06（2021-06 本来就没有报告）以及 2024-06 至 2025-10 的全部卷。
- **抽查**：逐条对照 QP、MS（及 ER）原文复核 22 题，覆盖 19 份卷中的每一份：2020-01 Q4、2020-10 Q9、2021-01 Q8、2021-06 Q1、2021-10 Q3、2021-10 Q7、2022-01 Q6、2022-06 Q9、2022-10 Q7、2023-01 Q5、2023-06 Q10、2023-10 Q2、2024-01 Q7、2024-06 Q3、2024-06 Q9、2024-10 Q8、2025-01 Q6、2025-01 Q10、2025-06 Q4、2025-06A Q7、2025-10 Q5、2025-10A Q2。分值、小问拆分、命令词和 MS 要点都与原文一致；发现的问题集中在 part 2 的 spec 标注上，于是对全部 500 小问做了 spec 规则扫描，并逐行复读了 part 2（2023-01 至 2025-10）全部 287 小问的 spec 标签。
- **改正 12 处**（明细与理由见 `work/wma13audit/fixes.json`，用 `apply_fixes.py` 已写回两个 part 文件后重新合并）：
  - spec 误挂 2.2（实际只用 sin² + cos² = 1）6 处：2023-10 Q3(a)、2023-10 Q10(c)、2024-01 Q6(b)、2024-06 Q9(b)、2025-01 Q10(b)、2025-06A Q7(b)。
  - 2023-06 Q9(c)：∫cosec x cot x 属“识别已知导数”，5.1 → 5.2。
  - 2025-10 Q3(c)：d/dt(1.12ᵗ) = 1.12ᵗ ln 1.12 属 4.4，[3.1, 3.2, 4.1] → [4.4, 3.2]（与 part 1 的同类题一致）。
  - 2021-10 Q7(b)：ask 中 “M = prᵍ” 的上标 g 改为 pr^q。
  - 2024-01 Q7(a)：ask 补上定义域 x > k/3 和 “in terms of k”。
  - 2023-06 Q10(b)：final_form 补上答案形式 x = −4/3、x = 4（必须写成方程、精确）。
  - 2025-01 Q10(b)：ms 补上 MS 的说明：题目写 hence，用 arccos 求导公式直接作答不给分。
- **重建注意**：part 2 由 `work/wma13p2/papers/p_*.py` 经 `build.py`／`finalize.py` 生成，part 1 由 `work/wma13p1/scripts/p_<series>.py` 生成。若重新生成 part 文件，要再运行 `python3 -I work/wma13audit/scripts/apply_fixes.py pearson-ial-maths/units work/wma13audit/fixes.json`（已改过的会显示 already），然后运行 `merge_validate.py … --write`。
- **体例差异（未改）**：part 1 的 ask／ms 用 Unicode 数学符号（π、², ≠）并在 ms 末尾注 MS 页码；part 2 用 ASCII 写法（pi、^2、!=），只在 er 末尾注 ER 页码。检索时两种写法都要考虑。
