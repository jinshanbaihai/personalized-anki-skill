# WME02 · M2 Mechanics 2：考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WME02.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WME02 --gaps` 输出为准（快照 2026-10-06）**。

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文术语保留原文。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6（M2 单元在 PDF 第 53–55 页）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019；文本版 `registry/src/fb/fb.txt`。力学部分全部在 FB p.13（PDF 第 19 页）。
- 不等号、分数指数、上标都对照渲染页图核过：`registry/work/mech-spec/pg-53.png`、`pg-54.png`、`pg-55.png`、`zoom54-54.png`（1.4 的例子）、`fb-19.png`。纯文本抽取会丢字符，例如 4.2 的 “0 ≤ e ≤ 1” 抽成了 “0  e 1”。
- 卷面信息取自本地真题封面 `registry/src/WME02/2025-10_01_qp.txt`（WME02/01，Thursday 23 October 2025）和 `2025-06_01A_qp.txt`（WME02/01A）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WME02/01**。另有区域卷 **WME02/01A**，考纲里没有这个代码。已见实例：2025 年 6 月 WME02/01A 试卷（P79507A，Monday 2 June 2025，7 题，75 分）。英国文化协会中国区 2025、2026 年 10 月以及 2026 年 1 月、6 月都以 WME02A 报名 | SPEC p.8、p.78 Appendix 1；versions.md §1.6；本地 QP 封面 |
| 单元名称 | Unit M2: Mechanics 2 | SPEC p.47、p.67 |
| AS/A2 定位 | 单元页：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Mathematics and Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔%。注意 M2 **不能**计入 IAS Mathematics（IAS Mathematics 的可选单元只有 M1、S1、D1） | SPEC p.47、p.67、p.8、p.10 |
| 资格结构 | IAL Mathematics 里，M2 只能以 “M1 and M2” 这一组合出现。IAS/IAL Further Mathematics：M2 属可选单元 | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.47 |
| 题量（参考） | 2025 年 10 月 WME02/01 封面：“There are 7 questions”，总分 75。考纲不固定题量 | `registry/src/WME02/2025-10_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra manipulation、symbolic differentiation or integration 功能的计算器，也不得存有可调出的公式 | SPEC p.47；Appendix 6，p.86 |
| 卷面要求（试卷封面，不是考纲） | “Whenever a numerical value of g is required, take g = 9.8 m s⁻², and give your answer to either 2 significant figures or 3 significant figures.” 以及 “show sufficient working to make your methods clear” | 2025-10 WME02/01 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。FB p.13 的 M2 部分只有 **Centres of mass**（三角形薄片、圆弧、扇形）三条；并写明 “Candidates sitting M2 may also require those formulae listed under Pure Mathematics P1, P2, P3 and P4.” | SPEC p.47；FB p.13 |
| 开考季 | **January, June and October**。p.70 注：从 2020 年 6 月起，October 考季只开 P1–P4、M1、M2、S1、S2 | SPEC p.8、p.70 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月之前 2018 版不开 M2（p.70 表）。2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.47、p.70；versions.md §1.4–1.5 |
| 旧考纲同代码 | WME02 这个代码 2013 版旧考纲也用过，旧版最后一次是 **2020 年 1 月**，不算本考纲真题。p.1 说 Mechanics 各单元 “have not changed”，所以旧卷内容兼容，可作额外练习。Pearson 官网把 2020 年 1 月的 WME02 放在 2018 文件夹里，但按首考日期它属于旧考纲 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specifications for P1, P2, P3, P4 and M1, and their prerequisites and associated formulae, is assumed and may be tested.” | SPEC p.47 |
| 评估目标分配（75 分中） | AO1 20–25；AO2 20–25；AO3 10–15；**AO4 7–12**；AO5 5–10 | SPEC p.69 |
| 须背公式（不在 FB 里） | 考纲原文 “Formulae that students are expected to know … will **not** appear in the booklet”：**Kinetic energy = ½mv²**；**Potential energy = mgh**。M1 页的须背清单（动量、冲量、匀加速五式，p.44）通过先修关系仍然适用。同处写明 “Questions will be set in SI units and other units in common usage.” | SPEC p.47、p.44 |
| 记号 | Appendix 7：4.14 ẋ, ẍ 表示对 t 的一阶、二阶导数（p.90）；第 9 节 Vectors 规定 i, j, k、\|a\|、â 等（p.91）。1.4 的例子用 ṙ、r̈ | SPEC pp.90–91、p.48 |
| 单元概述 | “Kinematics of a particle moving in a straight line or plane; centres of mass; work and energy; collisions; statics of rigid bodies.” | SPEC p.47 |

---

## 2. 规格条目逐条（M2.3 Unit content）

### 主题 1 Kinematics of a particle moving in a straight line or plane（p.48）

**1.1 Motion in a vertical plane with constant acceleration, e.g. under gravity**（p.48）
- 要求：竖直平面内的匀加速运动，例如只受重力作用。指导栏为空。

**1.2 Simple cases of motion of a projectile**（p.48）
- 要求：简单的抛体运动（projectile）。指导栏为空。
- 公式：FB 不给任何抛体公式，须由匀加速公式（M1 须背清单）分水平、竖直两个方向自行建立。

**1.3 Velocity and acceleration when the displacement is a function of time**（p.48）
- 要求：位移是时间的函数时求速度和加速度。指导栏：建立并求解形如 **dx/dt = f(t)** 或 **dv/dt = g(t)** 的方程，难度 “consistent with the level of calculus in P1, P2 P3 and P4”。
- 范围：加速度是时间的函数。加速度是位移的函数（v dv/dx = f(x)）属于 M3 1.1。

**1.4 Differentiation and integration of a vector with respect to time**（p.48）
- 要求：对时间求向量的导数和积分。考纲例子：已知 **r = t²i + t^{3/2}j**，求某一时刻的 **ṙ 和 r̈**（已对照放大渲染图确认指数是 3/2）。

### 主题 2 Centres of mass（p.48）

**2.1 Centre of mass of a discrete mass distribution in one and two dimensions**（p.48）
- 要求：一维和二维离散质点组的质心。指导栏为空。
- 公式：质心坐标公式（Σmx/Σm 之类）FB 不给，也不在须背清单里。

**2.2 Centre of mass of uniform plane figures, and simple cases of composite plane figures**（p.48）
- 要求：均匀平面图形和简单复合平面图形的质心。
- 指导栏：适当时可以利用对称轴（“The use of an axis of symmetry will be acceptable where appropriate”）；“**Use of integration is not required.**”；图形可以包括公式册里提到的形状；“Results given in the formulae book may be quoted without proof.”
- 公式：FB p.13 给出三条（均匀物体）：Triangular lamina：沿中线距顶点 2/3；Circular arc（半径 r、圆心角 2α）：距圆心 r sin α / α；Sector of circle（半径 r、圆心角 2α）：距圆心 2r sin α / (3α)。

**2.3 Simple cases of equilibrium of a plane lamina**（p.48）
- 要求：平面薄片（lamina）平衡的简单情形。考纲列出三种情形：(i) **suspended from a fixed point**（从定点悬挂）；(ii) **free to rotate about a fixed horizontal axis**（可绕固定水平轴转动）；(iii) **put on an inclined plane**（放在斜面上）。

### 主题 3 Work and energy（p.48）

**3.1 Kinetic and potential energy, work and power. The work-energy principle. The principle of conservation of mechanical energy**（p.48）
- 要求：动能、势能、功、功率；功能原理（work-energy principle）；机械能守恒原理。指导栏：可能出现在**恒定阻力**（constant resistance）下运动、和/或沿斜面上下运动的问题。
- 公式：KE = ½mv²、PE = mgh **须背**（p.47）。功、功率的公式（如功率 = 力 × 速度）FB 不给，也不在须背清单里，但本条要求使用。

### 主题 4 Collisions（p.49）

**4.1 Momentum as a vector. The impulse-momentum principle in vector form. Conservation of linear momentum**（p.49）
- 要求：动量作为向量；向量形式的冲量–动量原理；线动量守恒。指导栏为空。

**4.2 Direct impact of elastic particles. Newton’s law of restitution. Loss of mechanical energy due to impact**（p.49）
- 要求：弹性质点的正碰（direct impact）；**Newton’s law of restitution**；碰撞造成的机械能损失。
- 指导栏：须知道并会用不等式 **0 ≤ e ≤ 1**（e 为 coefficient of restitution）。已对照渲染页确认是 ≤。
- 公式：恢复定律的表达式 FB 不给，也不在须背清单里。

**4.3 Successive impacts of up to three particles or two particles and a smooth plane surface**（p.49）
- 要求：最多三个质点之间，或两个质点与一个光滑平面之间的**连续碰撞**（successive impacts）。
- 排除：“Collision with a plane surface will **not** involve oblique impact.”（与平面的碰撞不涉及斜碰。）

### 主题 5 Statics of rigid bodies（p.49）

**5.1 Moment of a force**（p.49）
- 要求：力矩。指导栏为空。

**5.2 Equilibrium of rigid bodies**（p.49）
- 要求：刚体平衡。指导栏：涉及**平行和非平行**共面力（parallel and non-parallel coplanar forces）的问题；可能包括 **rods or ladders** 靠在光滑或粗糙的竖直墙上、立在光滑或粗糙的地面上。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| Kinetic energy = ½mv²；Potential energy = mgh | **须背**（考纲明列） | SPEC p.47 |
| Momentum = mv；Impulse = mv − mu；匀加速五式 | **须背**（M1 清单，经先修适用） | SPEC p.44、p.47 |
| 三角形薄片、圆弧、扇形的质心位置 | FB 给出，可不加证明直接引用（2.2 指导栏） | FB p.13；SPEC p.48 |
| 抛体运动各式、离散质点组质心公式、功 = 力 × 沿力方向的位移、功率、恢复定律、向量形式的冲量 | FB **未给**，也不在须背清单里，但条目 1.2、2.1、3.1、4.1、4.2 要求使用，等于必须掌握 | SPEC pp.48–49；FB p.13（已核对没有） |
| P1–P4 的公式（三角恒等式、求导、积分表等） | FB 给出，M2 可能用到 | FB p.13 的说明 |
| g 的取值 | 不是考纲内容；试卷封面规定 g = 9.8 m s⁻²，答案取 2 或 3 位有效数字 | 2025-10 QP 封面 |

---

## 4. 与相邻单元的界线

- **M1（先修，可直接考）**：M1 的内容是 M2 的基础（p.47）。M1 只到直线匀加速、一维动量（不含恢复系数）、平行力的力矩、质点平衡。M2 把它们推广为：平面运动与抛体（1.1–1.2）、变加速（1.3–1.4）、向量动量与恢复定律（4.1–4.3）、非平行力下的刚体平衡（5.2），并新增质心（2.x）和功与能（3.1）。
- **P1–P4（先修，可直接考）**：1.3 的微积分以 P1–P4 为限（p.48 指导栏）。P3 的求导、积分（e^{kx}、三角函数、链式法则等，P3 4.1–4.2、5.1–5.2，pp.24–25）和 P4 的积分方法（P4 6.2–6.3，p.28）都在范围内。向量：1.4 的考纲例子只用 i、j；三维向量和 scalar product 在 P4 主题 7（pp.28–29）。
- **M3（以 M2 为先修，p.50）**：
  - 加速度是**位移**的函数、v dv/dx = f(x)、变力作用下的牛顿定律（含万有引力反平方律）→ M3 1.1、3.1。M2 1.3 只到加速度是时间的函数。
  - 用**积分**求质心、三维均匀刚体（实心半球、圆锥等）的质心 → M3 5.1。M2 2.2 明确 “Use of integration is not required”，2.1 也只到一维和二维。
  - 刚体放在水平面或斜面上的平衡 → M3 5.2；M2 2.3 限于平面薄片。
  - 弹性势能 → M3 2.2；M2 3.1 只有动能、重力势能。
  - 竖直圆周运动 → M3 4.4；M2 1.1 的竖直平面运动是匀加速运动。
- **斜碰**：M2 4.3 明确排除与平面的斜碰；M3 没有碰撞条目，所以 IAL 2018 版 M1–M3 里都不考 oblique impact。

---

## 5. 印刷问题与缺口
- “Assessment information” 一节的编号印作 **M2.1**（p.47），与上一节 “M2.1 Unit description” 重号，应为 M2.2。已对照渲染页确认是考纲原文如此。
- 1.3 指导栏印作 “P1, P2 P3 and P4”，少一个逗号，不影响含义。
- 纯文本抽取把 4.2 的 “≤” 丢成空格、把 1.4 的分数指数拆散，以渲染页为准。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 逐题索引与审核（2026-10-06；构建溯源，不随包发布）

**索引文件**：同目录 `WME02.questions.json`。它由 `WME02.questions.part1.json`（2020-10 至 2022-10，55 题）和 `WME02.questions.part2.json`（2023-01 至 2025-10，73 题）合并而成，按 id 去重（没有重复），再按考季、卷号（/01 在 /01A 前）、题号排序。构建记录见 `WME02.coverage.part1.md`、`WME02.coverage.part2.md`。

审核脚本和输出都在 `registry/work/wme02audit/`：
- 脚本：`completeness.py`、`show.py`、`ersec.py`、`qpblocks.py`、`markscheck.py`、`cmdcheck.py`、`quotecheck.py`、`er_pagecheck.py`、`ms_pagecheck.py`、`codesum.py`、`acccheck.py`、`formcheck.py`、`apply_fixes.py`、`stats.py`、`stats2.py`、`shapes.py`。
- 输出：`validate.txt`、`completeness.txt`、`checks.txt`、`stats.txt`、`stats2.txt`、`byitem.txt`（按主条目列出全部小问）。`shapes_rough.txt` 是关键词粗筛，有误报，第 7 节的题型计数以 `byitem.txt` 人工核对为准。
- 改动清单：`fixes.json`（33 条）；改动前的三个文件备份在 `backup/`。

**收录范围**：17 份卷，128 题，297 个小问，1275 分。

| 考季 | 卷 | 题数 | QP、MS 来源 | ER |
|---|---|---|---|---|
| 2020-10（封面 Thursday 21 May 2020，10 月实考） | /01 | 8 | GitHub `RayZ3R0/papernexus-finder`（PMT 戳记的 Pearson PDF），本地 `src/WME02/` | 缺 |
| 2021-01 | /01 | 8 | 同上 | 缺 |
| 2021-06（考试取消，只发布了试卷和 MS） | /01 | 8 | 同上 | 本季没有 ER |
| 2021-10 | /01 | 8 | 同上 | 缺 |
| 2022-01 | /01 | 7 | 同上 | 缺 |
| 2022-06 | /01 | 8 | 同上 | 缺 |
| 2022-10 | /01 | 8 | examsolutions S3 镜像（papernexus 有同一文本） | 有 |
| 2023-01 | /01 | 8 | S3 镜像 | 有 |
| 2023-06 | /01 | 7 | S3 镜像 | 有 |
| 2023-10 | /01 | 7 | S3 镜像；Drive 有 MS 重存版（`src/WME02/alt/`） | 有 |
| 2024-01 | /01 | 8 | S3 镜像；Drive 有同一 QP 和 MS 重存版 | 有 |
| 2024-06 | /01 | 7 | Drive | 缺 |
| 2024-10 | /01 | 7 | Drive | 缺 |
| 2025-01 | /01 | 8 | Drive | 缺 |
| 2025-06 | /01 | 7 | Drive | 缺 |
| 2025-06 | /01A | 7 | Drive（P79507A，第一份 M2 区域卷） | 缺 |
| 2025-10 | /01 | 7 | Drive | 缺 |

**格式校验**（构建时的合并校验脚本，结果 0 个问题）
- 每条记录字段齐全；各小问分值之和等于题目总分；每卷 75 分，题号连续。
- 所有 spec id 都在 `spec-items.mech.json` → `WME02` 中；series 都是 YYYY-MM，且月份只有 01、06、10；id 与考季、卷号、题号一致。
- 引号内的文字都不超过 25 词。297 个小问都有 MS 要点；`er` 恰好在有 ER 的 5 季（38 题、94 个小问）填写。
- `markscheck.py` 从 QP 文本逐题读出印刷的 "(n)" 和 "Total"，128 题的小问分值顺序和总分全部一致。

**自动比对**（输出见 `checks.txt`）
- **命令词**（`cmdcheck.py`）：剩下 17 处标记都不是错误。它们是共用题干的 "Find"（O21 Q3、J24 Q1 的 "Find (a) … (b) …"）、"Using this model, find" 记为 Find，以及把 work-energy 指令写在题干里的 S24 Q4(b)(c)、S25 Q4(c)。
- **引文**（`quotecheck.py`）：9 处加引号的短语里，4 处是 QP 上的分式给定结果（如 "d = 5a/2"），文本层是叠排分式，人工核对无误；其余逐字找到。
- **MS 页码与数值**（`ms_pagecheck.py`）：每个小问都引了 MS 页，页面都存在且含该题的评分行。`final_form` 中 221 个小数逐个在所引 MS 页上查找，找不到的 6 个都核对过：1.27、57.7 是 MS 中 1.268…、57.662… 的舍入；0.131、694.4 出自 ER；0.682 rad 对应 MS 的 "0.68(2)"；47.5 即 MS 的 95/2。
- **ER 页码**（`er_pagecheck.py`）：94 个 `er` 字段逐条比对所引 ER 页。标记的 26 处全部人工看过，4 处是评论跨页而只引了一页（改正 6–9），其余是转述用词不同。
- **评分代码求和**（`codesum.py`）：把 `ms` 中的 B1、M1、A1、DM1、A2ft 等代码按小问求和。改正前 8 处差异中 7 处是说明里的 "M1A0A0" 一类特例，1 处是真错（改正 5）。改正后 S24 Q6(a) 因并列写出两种配对仍被计多，属同类误报。
- **精度阈值**（`acccheck.py`）：MS 中的 "X or better" 与索引逐题比对。标记 5 处，1 处是真错（改正 3），其余属于同页的相邻题或中间值。
- **答案形式**（`formcheck.py`）：QP 要求 "exact"、"n significant figures"、"in terms of i and j" 的小问，`final_form` 都写明了；唯一的标记是误报。

**完整性**
- **预期考季**：据 `versions.json` 和 `src/expected_series.json`，2018 考纲下 WME02 预期 18 季：2020-10 起每年 1、6、10 月，到 2026-06 为止。2020-06 整季取消。
- **收录情况**：有 QP 文本的 16 季 17 份卷全部收录，没有漏卷。`inventory/fm-mech.json` 的 17 个 WME02 卷和 `finder/finder-inventory.tsv` 中 14 季 2018 考纲卷都在索引内。
- **不收**：finder 中的 SAM（S59764A）是样卷，不是真题，与其他单元的做法一致；2014-01 至 2020-01 的 16 份同代码卷属于 2013 旧考纲（M2 内容未变，可作额外练习）。
- **所有来源都拿不到的卷**：2025-10 WME02/01A；2026-01 WME02/01 与 /01A；2026-06 WME02/01 与 /01A。QP、MS、ER 全缺。证据和检索记录见 `WME02.coverage.part2.md` 的 "Papers missing"。2026-10-06 审核时再查 Drive（标题含 WME02，全部分页；以及 2025-10-15 以后修改、标题含 WME02/Mechanics M2/MS_M2/M2A 的文件），只找到已收录的 2023–2025 文件。
- **缺 ER**：2020-10、2021-01、2021-10、2022-01、2022-06、2024-06、2024-10、2025-01、2025-06（/01 与 /01A，WebSearch 显示 /01A 有单独的 ER）、2025-10。2021-06 本来没有 ER。有 ER 的只有 O22、J23、S23、O23、J24 五季。

**准确性抽查**
- **抽查范围**：对照 QP、MS、ER 原文逐条复核 43 题，覆盖全部 17 份卷和全部 12 个有题的条目（1.1 没有题）：
  - 2020–2021：O20 Q2、Q4、Q6、Q7；J21 Q6、Q8；S21 Q1–Q8（全卷）；O21 Q1、Q3、Q8；
  - 2022：J22 Q5、Q7；S22 Q2、Q6；O22 Q1、Q8；
  - 2023：J23 Q6、Q7；S23 Q3；O23 Q7；
  - 2024：J24 Q2、Q6；S24 Q2、Q3、Q6；O24 Q5、Q7；
  - 2025：J25 Q3、Q8；S25 Q3、Q6；S25A Q1、Q2、Q7；O25 Q4、Q7。
  - S21 先抽了 Q2、Q4、Q6，Q2 和 Q6 各有一处错误，于是把 S21 全卷 8 题逐题复核，又查出 Q3(a) 一处遗漏。
  - 另外，全部 94 个 `er` 字段都与 ER 原文对照过页码（见上文"ER 页码"）。
- **核对内容**：分值、spec 映射、命令词、终点形式、MS 要点、ER 要点。不看 MS 独立重算了 30 余个终点值，全部与 `final_form` 一致，例如 O21 Q3 的 56 和 42、S23 Q3 的 16y/9 与 9y/8、O23 Q7 的 e = 7/10 与 f ≤ 5/16、O24 Q7 第二次碰撞冲量 60mu/49、J25 Q8 的 k = 1/6、S25 Q3 的 (3π − 1)/(3π + 5)、S25A Q2 的 k = (92 + 15π)/48、S25A Q7 的 0.16u 与 0.18u、O25 Q4 的 k = (48 − 12π)/(8 + 3π)、O25 Q7 的 7.54、27.3、2.04，以及 S22 Q6、S23 Q4、J24 Q7、S25 Q5、O25 Q6 的动能损失（用 ½·m₁m₂/(m₁ + m₂)·(1 − e²)·(相对速度)² 核对）。

**改正**（合并文件和对应 part 文件同步修改，清单见 `work/wme02audit/fixes.json`）
1. **错误（7 个，改 9 个字段）**
   - F1–F2 S21 Q6(c)：`final_form` 原写 "√(16g/13) ≈ 3.47"，暗示精确式得分；MS p.15 要求代入 g，只收 3.47 或 3.5。
   - F3–F4 S21 Q2(b)：原写 "52.1i + 212.5j or better"，MS p.9 的门槛是 "52i + 210j or better"。
   - F5 S24 Q6(a)：`ms` 列了 B1、B1、M1A1、B1、M1、A1*，共 7 分，题目只有 6 分。MS p.13 是 B1（F = R/3）加一组"分解 + 力矩"（S = F 配 M(A) 或 M(G)，R = mg 配 M(B)），再 M1A1*。
   - F6–F9 ER 页码：O22 Q1(b)、O23 Q2(a)、J24 Q1(b) 的评论续到下一页，改为 "ER pp.3–4"；J24 Q4(a) 改为 "ER pp.4–5"。
2. **遗漏（1 处）**：F10 S21 Q3(a) 补上 MS p.10 的规定：求出到 BC 的距离 (236 − 6π)a/(3(28 − π)) 而不是到 AD 的距离，给 4/5。
3. **引文（1 处）**：F11 S23 Q4(a) 引号内 "fudged" 不是原文，改为 ER p.5 的 "fudge"。
4. **标签约定统一（11 处）**：part 1 和 part 2 的副标签规则不一致，导致按条目统计时两段不可比。统一为 part 2 的规则：
   - 正碰小问只有在给出或要求冲量、或只用动量守恒（不用恢复定律）时才加 4.1；只用 CLM + 恢复定律的记 4.2。改 O20 Q7(a)、S21 Q8(a)、J22 Q4(a)、O22 Q7(a)（F13–F16）。
   - 碰墙或第三个质点的小问记 4.3，有冲量时加 4.1，不再加 4.2；只有问动能损失时保留 4.2（O21 Q6(b)）。改 O20 Q7(b)、J21 Q8(b)、S21 Q8(b)、J22 Q4(b)、S22 Q2(a)、O22 Q7(b)（F17–F22）。
   - 附加质点后悬挂的薄片，按 part 2 记 ["2.3", "5.1"]，2.1 只留给纯质点组。改 O20 Q4(b)（F12）。
5. **格式统一（11 处）**：part 1 把 "Use the work-energy principle to find" 记成 "Use"，改为全句，共 7 处（F23–F29）；J23 Q8(b) 改为 QP 原句 "Use the principle of conservation of mechanical energy to find"（F30）；"By considering energy, find" 是限定方法的指令，从 "Find" 改为全句，共 3 处（J21 Q7(a)、O21 Q8(a)、S23 Q7(a)，F31–F33）。
6. **错误分布**：S21 有 3 处（2 处终点精度、1 处遗漏），已对 S21 全卷复核；ER 页码问题已用脚本扫过全部 94 个 `er` 字段；标签和命令词问题已对全部 297 个小问按条目、按命令词逐一列出检查。其余错误分散，没有再集中在某一卷。

**保留未改的差异**（coverage 文件是构建记录，没有改动，以本节和索引为准）
- `WME02.coverage.part1.md` 的 "Spec coverage" 表中，2.1、4.1、4.2 的 "Parts tagged" 是统一标签前的数字。
- `inventory/fm-mech.json` 和 `fm-mech-gaps.md` 仍把 2020-10 至 2022-06 的 QP 记为"只有 Finder 文本"、MS 记为缺失；part 1 已从 papernexus 补齐 PDF。
- S25A Q7(d) 的 MS 一处写 "a third collision"，一处写 "a second collision"；索引按题意记为 P、Q 再次相碰（coverage part 2 已说明）。同一小问的 MS 注释把 B1 写成"Q 的速度"，评分行是 P 的速度 0.16u，索引按评分行记录。

## 7. 真题需求概览

**数据范围**
- 本节统计第 6 节收录的 17 份卷：O20、J21、S21、O21、J22、S22、O22、J23、S23、O23、J24、S24、O24、J25、S25、S25A、O25。共 128 题、297 个小问、1275 分。
- 17 份卷都有 MS；有 ER 的只有 O22、J23、S23、O23、J24 五份。
- 拿不到的卷见第 6 节"完整性"。

**统计方法**
- 数字由 `work/wme02audit/scripts/stats.py`、`stats2.py` 从索引算出，结果存于 `stats.txt`、`stats2.txt`。题型计数由 `byitem.txt` 人工归类。
- "问法、终点、评分"取自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节抽查过。

**引用写法**
- J = January，S = June，O = October，后接两位年份；S25A 是 2025 年 6 月的 WME02/01A 区域卷。
- S21 的考试取消了，但试卷和 MS 已发布。O20 用的是原定 2020 年 6 月的试卷。
- 题号和小问按试卷印刷。MS、ER 页码见索引条目 `ms`、`er` 字段末尾的 "(MS p.n)"、"(ER p.n)"，下文只在需要时注出。

### 7.1 卷面结构

**题量与分值**
- 每卷 75 分。8 题的 9 份（O20、J21、S21、O21、S22、O22、J23、J24、J25），7 题的 8 份（J22、S23、O23、S24、O24、S25、S25A、O25）。S24 以后只有 J25 是 8 题。
- 单题 5–17 分。最常见 10 分（23 题），其次 12 分（18 题）、9 分（17 题）、8 分（16 题）、11 分（14 题）。最大的是 S25A Q7（17 分，三质点碰撞）。
- 每题 1–4 个小问，2 个小问最常见（56 题），单问题 21 题。

**命令词**（297 个小问）

| 命令词 | 次数 |
|---|---|
| Find | 213 |
| Show that | 58 |
| Use the work-energy principle to find | 17 |
| By considering energy, find | 3 |
| Use the principle of conservation of mechanical energy to find | 1 |
| Hence find、Verify、Determine、State、Explain | 各 1 |

- M2 一直以 "Find" 为主。"Determine" 只出现在 S25A Q7(d)（"Determine, with clear reasoning, whether …"）。
- 给定结果的小问（Show that、Verify）59 个，共 244 分，约占 19%。
- 限定方法的小问 21 个：work-energy 17，by considering energy 3，conservation of mechanical energy 1。不用指定方法不给分（见 7.4 第 4 条）。

**各主题分值**（按每个小问的第一个 spec 计）

| 主题 | 分值 | 占比 | 每卷分值范围 |
|---|---|---|---|
| 1 运动学（抛体、变加速） | 341 | 27% | 14–25 |
| 4 碰撞与冲量 | 322 | 25% | 15–25 |
| 3 功、能、功率 | 253 | 20% | 9–21 |
| 5 刚体静力学 | 181 | 14% | 9–15 |
| 2 质心 | 178 | 14% | 5–15 |

**每卷固定出现的题型**
- **17/17 份卷都有**：
  - 抛体题（1.2）。
  - 用微积分的运动学题：向量型 1.4 有 13 份，标量型 1.3 有 O21、J24、S24、S25A 四份，S25 两种都有。
  - 组合薄片或线框质心的 show-that（2.2）。
  - 功能或功率题（3.1）。
  - 冲量题（4.1）。S24 改为二维碰撞的向量动量（Q1），S25 把冲量接在 r(t) 之后（Q2）。
  - 正碰题（4.2）。
  - 杆、梯子、梁的平衡题（5.1/5.2），每题 9–12 分；第一问多是取矩求出或证明张力、反力（17 题中 12 题是 show-that）。
- **16/17**：车辆或骑车人的功率题（P = Fv），只有 S24 没有。其中拖车题 6 份：J22 Q2、S23 Q6、J24 Q5、O24 Q3、J25 Q2、O25 Q1。
- **15/17**：
  - 碰后接墙或第三个质点（4.3），缺 J23、S23。
  - 薄片自由悬挂或绕轴转动（2.3），缺 S21、S25A；这两卷改为两根竖直绳吊薄片（S21 Q3(b)、S25A Q2(b)，记 5.1）。
- **10/17**：粗糙斜面上克服摩擦力做功，再用功能原理（O20 Q6、S21 Q6、O21 Q1、S22 Q8、O22 Q8、J23 Q5、J24 Q3、S24 Q4、J25 Q1、O25 Q7）。其中 O20、S22、O22、O25 的质点离开斜面后接平抛。
- **10/17**：第二次碰撞（判断是否发生、范围、时间、位置或冲量）：J21 Q8、S21 Q8、J22 Q4、O22 Q7、O23 Q7、J24 Q7、S24 Q5、O24 Q7、J25 Q8、S25A Q7。

**题面限制语**
- "Solutions relying (entirely) on calculator technology are not acceptable" 和 "show all stages of your working"：从 S23 起出现，共 8 题，全部是微积分运动学题：S23 Q2、S24 Q2、O24 Q1、J25 Q3、S25 Q1、S25 Q2、S25A Q1、O25 Q3。
- 题中给出质心公式：O21 Q7（扇形，"may use, without proof"）、J22 Q6 与 S25 Q3（半圆弧 2r/π）、S25A Q2（扇形）、O25 Q4（半圆薄片 4r/3π）。其余用公式册（三角形、圆弧、扇形）。
- g 改用 10：只有 S25 Q7（"modelled as being 10 m s⁻²"）。其余一律 g = 9.8，代入 g 后的答案给 2 或 3 位有效数字。
- i、j 在竖直平面内的向量抛体：9 份卷（O20 Q8、S21 Q7、O22 Q8、S23 Q7、O23 Q4、J24 Q8、S24 Q7、J25 Q4、S25A Q3）。

### 7.2 每个考纲条目怎么考

- "卷数／题数／小问／涉及分值"按标签出现的任何位置统计。一个小问可以带几个标签，所以各行相加会超过 128 题、1275 分。
- 括号内的"主"表示该条目作为第一个标签时的小问数和分值。

| 条目 | 卷数／题数／小问／涉及分值 | 常见命令词（主） | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 竖直平面内的匀加速运动 | 0（主 0） | — | 从未单独考。竖直平面内的重力运动都以抛体出现，记在 1.2；竖直上抛、自由下落没有单独成题 | — | — |
| 1.2 抛体 | 17／17／45／182（主 42／172） | Find 38，Show that 4 | **求初速度或其分量**：由某时刻的速度反推（O20 Q8(a)，J25 Q4(a)），show u = 14（S24 Q7(a)）。**射程、飞行时间、最大高度**（S21 Q7(a)，J22 Q7(d)，O22 Q8(c)，J24 Q8(a)，S25A Q3）。**速度满足某条件的时间区间或高度**：先由速率求竖直分量 ±v_y，再求两个时刻之差（O20 Q8(b)，J21 Q7(c)，S21 Q7(b)，O21 Q8(c)，J24 Q8(b)，S24 Q7(b)）。**速度方向与初速度、给定向量或斜面垂直**（O20 Q8(c)，S21 Q7(c)，S23 Q7(d)，O23 Q4(d)，J24 Q8(c)，S25 Q7(b)）。**落地或某时刻的方向角**（O22 Q8(d)，S23 Q7(b)，O23 Q4(c)）。**推导轨迹方程或射程公式**，6 分（J22 Q7(a)，J23 Q8(a)，O24 Q5(a)）。**越过竿的 θ 范围**（J22 Q7(b)）。**离开斜面后的平抛**（O20 Q6(b)，S22 Q8(c)，O22 Q8(c)，O25 Q7(c)(d)） | 2 或 3 位有效数字（33/42）；角度要写明在水平线上方还是下方；向量答案写成 i、j；2–6 分，平均 4.1 | O20 Q8，S21 Q7，J22 Q7，O23 Q4，J24 Q8，S24 Q7 |
| 1.3 位移是时间的函数（标量） | 5／5／15／47（主 15／47） | Find 11，Show that 3，Verify 1 | **给出 x(t)**（多项式或分数次幂）：求静止时刻（O21 Q3(a)，J24 Q1(a)，S25A Q1(a) 验证 t = 2）；求区间内总路程，必须在转向处分段（O21 Q3(b)，J24 Q1(b)，S25 Q1(c)，S25A Q1(b)）；求加速度大小（J24 Q1(c)，S25A Q1(c)）。**给出 a(t)**：积分并用初值定常数，证 k = 4 和 s 的给定形式（S25 Q1）。**分段连续的速度**：用连续性证 k = 4 并说明舍根，再分段积分求位移，7 分（S24 Q2） | t 的精确值；路程和加速度大小必须为正；2–7 分 | O21 Q3，J24 Q1，S24 Q2，S25 Q1，S25A Q1 |
| 1.4 向量对时间求导和积分 | 13／13／31／122（主 31／122） | Find 29，Show that 2 | **求导**：由 r 求 v、a，或由 v 求 a，再 F = ma（O20 Q5(a)，S21 Q2(a)，J22 Q3(a)，S22 Q1(a)，J23 Q4(b)，O23 Q1(b)，O24 Q1(b)，J25 Q3(b)，O25 Q3(a)）。**积分**：由 v 求 r，用给定位置定常数（J21 Q5(c)，S21 Q2(b)，J22 Q3(b)，O22 Q4(b)，J23 Q4(c)，S23 Q2(a)，O24 Q1(a)，O25 Q3(b)）。**"moving in the direction of / parallel to"**：令一个分量为 0，或令两分量成比例（11 份卷，例如 S22 Q1(b)，S23 Q2(b)，O24 Q1(c)，O25 Q3(c)）。**瞬时静止**要两个分量同时为 0（O20 Q5(b)）。**证明永不回到原点**（J25 Q3(c)）。**r(t) 后接冲量**（S25 Q2） | 问 velocity、acceleration、force 时答 i、j 向量（17/31），问 speed、magnitude 时答正标量；要求 exact 时写根式（S23 Q2(c) √325，O25 Q3(c) 3√34）；只取定义域内的 t（"T = 2 only"）；2–7 分 | J21 Q5，J22 Q3，O22 Q4，S23 Q2，O24 Q1，J25 Q3，O25 Q3 |
| 2.1 离散质点组的质心 | 1／1／2／6（主 2／6） | Show that 1，Find 1 | 只考过一次：三个质点坐标给定，证 x̄，再由质心在直线 x + 2y = 3 上求 k（O22 Q1）。其余附加质点的题都用力矩处理，不求组合质心 | 给定式；k = 23/20；2–4 分 | O22 Q1 |
| 2.2 均匀平面图形与组合图形的质心 | 17／18／31／154（主 18／86） | Show that 16，Find 1，Hence find 1 | **几乎每卷一道约 5 分的 show-that**：矩形或正方形挖去三角形、正方形、圆（O20，S21，J23，J25）；L 形（O22）；加扇形并由质心在边上证 a = √3d（O21）；半圆从一边移到另一边（S25A）；加半圆再挖半圆（O25）；梯形，要自己推梯形质心（O24）；折叠薄片（S23 三角形，J24 矩形）；不同面密度（S22，O23，J25）；内切圆孔，再求 k 的范围（S24 Q3(a)(b)）；线框（J21 杆架，J22 与 S25 含半圆弧） | 给定答案要写成题面形式，以 "d =" 或题中字母结尾，至少一步化简（O23 Q2(a)，J24 Q4(a)，O25 Q4(a)）；3–5 分（J21 Q4 整题 9 分） | S23 Q3(a)，O23 Q2(a)，J24 Q4(a)，S24 Q3(a)，O24 Q4(a)，S25 Q3(a) |
| 2.3 平面薄片的平衡 | 15／16／19／95（主 18／86） | Find 18 | **自由悬挂求角**：悬点与质心的连线竖直，用 tan 求某边与竖直线的夹角（J21 Q4，O21 Q7(b) 用弧度，J22 Q6(b)，S22 Q7(b)，J23 Q3(b) 取整度数，S24 Q3(c)，O24 Q4(b)，O25 Q4(b)）。**给定角，反求尺寸或参数**（O20 Q4(b)，O22 Q6(b)，S23 Q3(b)）。**求精确的 tan**（O23 Q2(b)，J25 Q6(b)，S25 Q3(b)）。**绕光滑水平轴转动，用外力或附加质点使某边竖直或水平**：对转轴取矩（J21 Q2，O23 Q2(c)，J24 Q4(b)，S24 Q3(d)，O25 Q4(c)）。考纲列的第 (iii) 种"放在斜面上"从未考 | 角度 2 或 3 位有效数字，或按题意取整；精确 tan；力、质量用 W、M、g 表示；3–7 分 | J23 Q3(b)，O23 Q2，S24 Q3(c)(d)，O24 Q4(b)，O25 Q4(b)(c) |
| 3.1 动能、势能、功、功率；功能原理；机械能守恒 | 17／36／66／292（主 59／253） | Find 35，Use the work-energy principle to find 17，By considering energy, find 3，Show that 3，Use the principle of conservation of mechanical energy to find 1 | **功率 P = Fv**（16 份卷）：平路、上坡、下坡中的两种工况联立求 P 和 R（O20 Q2，J21 Q3，O21 Q2，S22 Q4）；求恒定速度、某速度时的加速度或减速度、某时刻的功率（S21 Q1，O22 Q2，J23 Q1，O23 Q5，S25 Q4，S25A Q4）；拖车与车之间的拉力（J22 Q2，S23 Q6，J24 Q5，O24 Q3，J25 Q2，O25 Q1）；拖杆断开后用功能原理求拖车滑行距离（J22 Q2(b)，S23 Q6(c)，O24 Q3(b)）。**粗糙斜面**（10 份卷）：先求克服摩擦力的功，再用功能原理求初速度、距离或返回时的速度（S21 Q6 连滑轮，J23 Q5，J24 Q3，S24 Q4，O25 Q7）。**抛体的能量**：由能量求落地速度或高度（J21 Q7(a)，O21 Q8(a)，J23 Q8(b)，S23 Q7(a)，S25 Q7(a) 用 g = 10）。**骑车人的总功**（O23 Q5(b)，S25A Q4(c)） | 2 或 3 位有效数字（47/59）；功用 J 或 kJ，功率注意 kW 与 W；减速度写成正数（J24 Q5(a)）；2–9 分，平均 4.3 | O20 Q2，J22 Q2，S23 Q6，J24 Q3，O24 Q3，S25 Q4，O25 Q7 |
| 4.1 向量动量；向量形式的冲量–动量原理；动量守恒 | 17／28／39／168（主 30／126） | Find 26，Show that 4 | **I = m(v − u) 的向量形式**：已知冲量求速度、速率（J22 Q1(a)，J24 Q2(a)）。**冲量大小或末速率给定，速度含参数**：得二次方程，两个解都要（O20 Q1，J21 Q1，O21 Q4，S22 Q3，O22 Q3，O24 Q2，J25 Q5，S25A Q5，O25 Q2）；给定动能增量（J23 Q2，O24 Q2）。**夹角**：冲量与初速度之间，或前后速度之间，用 tan 之差、点积或余弦定理（J22 Q1(b)，S23 Q1(b)，J24 Q2(b)，J25 Q5(c)，O25 Q2(b)）。**冲量与速度成给定角**：动量三角形配余弦定理（S21 Q4，O23 Q3）。**一维碰撞中的冲量**：由冲量反求速度或 e（J23 Q7(b)，S23 Q4(a)(b)，O24 Q7(b)，S25 Q5(c)，S25A Q7(c)）。**二维碰撞的向量动量守恒**（S24 Q1） | 冲量写成 i、j 形式（J25 Q5(b) 不收列向量）；两个解都要；大小为正；角度 3 位有效数字；1–8 分 | O20 Q1，J23 Q2，O23 Q3，J24 Q2，S24 Q1，J25 Q5，S25A Q5 |
| 4.2 正碰；牛顿恢复定律；碰撞的机械能损失 | 17／17／31／149（主 25／129） | Find 18，Show that 7 | **CLM + 恢复定律，证碰后速度的 e 表达式**（S21 Q8(a)，J22 Q4(a)，O22 Q7(a)，S25 Q5(a)，S25A Q7(a)，O25 Q6(a)）。**求 e**：由动能增量（O20 Q7(a)）、由冲量（J21 Q8(a)，O21 Q6(a)），或由已求出的速度（S23 Q4(c)，O23 Q7(b)）；反过来已知 e 求碰后速度（J25 Q8(a)）。**由方向条件求 e 或参数的范围**（J23 Q7(c)，J24 Q7(a)，S24 Q5(a)，O24 Q7(a)，S25A Q7(b)）。**动能损失**（S22 Q6(b)，S23 Q4(d)，J24 Q7(b)，S25 Q5(b)，O25 Q6(b)）；碰后动能为碰前一半，得二次方程（O23 Q7(a)）。**求质量比 k**（S22 Q6(a)，J25 Q8(b)） | 分数，或含 u、e、m 的式子；范围两端都要，严格与非严格不等号写对（0 ≤ e ≤ 1）；速率为正；动能损失保留 m 和 u²；3–9 分，平均 5.2 | J22 Q4，O22 Q7，J24 Q7，O24 Q7，S25 Q5，O25 Q6 |
| 4.3 连续碰撞（至多三个质点，或两个质点与光滑平面） | 15／15／17／67（主 17／67） | Find 15，Show that 1，Determine 1 | **碰墙求 f**：由墙后速度条件（O20 Q7(b)，S25 Q5(d)），或由墙给的冲量（O25 Q6(c)）；求墙给的冲量（O23 Q7(d)）。**是否发生第二次碰撞**：比较两速度，得 f 或 e 的范围（J22 Q4(b)，O23 Q7(c)，J24 Q7(c)，S24 Q5(b)）。**第二次碰撞的位置或时间**（J21 Q8(b)，O22 Q7(b)，J25 Q8(c)）。**第二次碰撞中的冲量**（O24 Q7(c)）。**三个质点**（S21 Q8(b) 证会再碰，S25A Q7(d) Determine）。**两墙之间往返的时间**（S22 Q2） | 范围、分数，或含 d、u 的式子；判断题要写出速度比较和结论；1–6 分 | J21 Q8(b)，O23 Q7(c)(d)，J24 Q7(c)，J25 Q8(c)，S25A Q7(d) |
| 5.1 力矩 | 17／24／25／99（主 16／57） | Show that 12，Find 4 | 几乎都是刚体题的第一问：对铰链、地面接触点或悬点取矩，证明绳的张力、支杆推力、钉或横杆或半球的法向反力等于给定值（O21 Q5(a)，J22 Q5(b)，S22 Q5(a)，O22 Q5(b)，J23 Q6(a)，O23 Q6(a)，J24 Q6(a)，O24 Q6(a)，J25 Q7(a)，S25 Q6(a)，S25A Q6(a)，O25 Q5(b)）。求张力或墙的反力（S21 Q5(a)，S23 Q5(a)）。两根竖直绳吊薄片，求拉力关系（S21 Q3(b)，S25A Q2(b)） | 给定答案要写出三角值的代入（J24 Q6(a)，J25 Q7(a)）和 "S =" 等字母（S25 Q6(a)）；3–5 分 | J23 Q6(a)，J24 Q6(a)，J25 Q7(a)，S25 Q6(a)，O25 Q5(b) |
| 5.2 刚体平衡 | 17／19／40／181（主 24／124） | Find 17，Show that 5，State 1，Explain 1 | **铰链或接触点 A 处的合力**：只求大小（S21 Q5(b)，J23 Q6(b)，O23 Q6(b)，J24 Q6(b)），大小和方向（J22 Q5(c)，O22 Q5(c) 要精确值），只求方向（J25 Q7(b)）。**极限平衡求 μ**（O21 Q5(b) 在墙上，S22 Q5(b)，S23 Q5(b)，O24 Q6(b)，O25 Q5(c)），或求角（O20 Q3 精确 tan θ，S24 Q6(a)，S25 Q6(c) 得 tan θ 的二次方程）。**梯子**：人爬到何处将滑动（J21 Q6(b)）；外加水平力的最大值（S24 Q6(b)）。**半球几何**：杆与半球相切，得 5–12–13 一类三角形（J22 Q5(a)，O22 Q5(a)，O25 Q5(a)）。**建模假设**（J21 Q6(c)，1 分） | 精确值或 2、3 位有效数字；μ 常是分数；角度要写明从哪条线量起；6 分的小问最多，平均 5.2 分 | O20 Q3，J22 Q5，S23 Q5，J24 Q6，S24 Q6，J25 Q7，O25 Q5 |

**刚体题的支承方式**（17 题，每卷一题）
- 地面粗糙、墙或钉光滑：J21 Q6（梯子）、S24 Q6、J24 Q6（钉）、O24 Q6（钉）、S25 Q6（横杆）。
- 地面与墙都粗糙：O20 Q3、S23 Q5。
- 靠在固定光滑半球上：J22 Q5、O22 Q5（另一端铰接在地面）、O25 Q5。
- 铰接在墙上，用绳或轻杆拉住：S21 Q5、J23 Q6（轻杆，推力）、O23 Q6、J25 Q7。
- 一端靠粗糙墙，用绳拉住：O21 Q5、S25A Q6；一端在粗糙地面，用垂直于杆的绳拉住：S22 Q5。

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据是 17 份卷的索引检索。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 竖直平面内的匀加速运动（非抛体） | 从未单独考 | 并入抛体卡（竖直方向的 suvat） |
| 1.3 由 dx/dt = f(t) 或 dv/dt = g(t) 积分 | 只有 S25 Q1（由 a(t) 积分两次）和 S24 Q2(c)（由 v(t) 分段积分）；其余 1.3 题都是给出 x(t) 求导 | 一张"积分、每次用初值定常数"卡 |
| 1.4 向量中的指数函数 | 从未出现；三角函数只有 J22 Q3（sin 3t、cos t）；分数次幂和根式较多（O22、O23、J25、S25） | 用 P3/P4 的求导积分卡，配一张链式法则卡 |
| 2.1 离散质点组 | 只考过 O22 Q1 | 一张 Σmx/Σm 卡（公式册不给） |
| 2.3 (iii) 薄片放在斜面上 | 从未考 | 一张判据卡：重力作用线是否落在支撑面内 |
| 2.2 梯形质心 | 公式册不给，O24 Q4(a) 要自己推；S23 Q3(a) 用梯形但未说明质心位置的得 0/5 | 推导卡：拆成矩形加三角形 |
| 3.1 阻力与速度成正比 | 只有 S21 Q1（20V N） | 一张卡：F − kv 代入 P/v 得二次方程 |
| 3.1 指定"机械能守恒"作答 | J23 Q8(b)、S25 Q7(a) 两次 | 与功能原理卡对照：无摩擦时才可用 |
| 4.1 二维碰撞中的向量动量守恒 | 只有 S24 Q1 | 一张卡：两质点的冲量大小相等、方向相反 |
| 4.3 三个质点的连续碰撞 | 只有 S21 Q8、S25A Q7；其余都是两个质点加一面墙 | 一张流程卡 |
| 4.3 质点在两面墙之间往返 | 只有 S22 Q2 | 一张卡（每次碰墙速度乘 e） |
| 5.2 平行力 | 只在两根竖直绳吊薄片中出现（S21 Q3(b)、S25A Q2(b)） | 一张卡 |
| 斜碰 | 考纲排除（4.3 指导栏），17 份卷中没有出现 | 不做 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 O22、J23、S23、O23、J24 五份；没有标 ER 的条目都来自 MS 的评分说明。

1. **g = 9.8，答案 2 或 3 位有效数字**
   - 每份 ER 都重复这条规则：O22 ER p.3，J23 ER p.3，S23 ER p.3，O23 ER p.3，J24 ER p.3。O23 ER 原话：更精确的答案 "will be penalised, including fractions"。
   - 用 9.81 每题扣一次（O23 ER p.3，J24 ER p.3；各份 MS 的通则，S22 Q4 因此封顶 7/8）。
   - 代入 g = 9.8 之后保留精确分数或根式会丢最后的 A：S21 Q1 的 (49 + 22√14)/5，S21 Q7(a) 的 144/g，O21 Q8(a) 的 80/7，S22 Q4 的 1164，O22 Q8(c) 的 (5 + √67)/7，S23 Q6(b) 的 73/160（ER p.6），S23 Q7(a) 的 9√5（ER p.6），O23 Q4(a) 的 20/49，J24 Q8(a)(b) 的 40/7、56/g、30/49、6/g，S24 Q7(b) 的 10/7，O25 Q7(a) 的 10g/13。
   - g 的倍数有时可以接受：S21 Q6(a)(b)，O20 Q6(a) 的 "21g"；但 S21 Q6(c) 要求代入 g，S22 Q8(a) 不收 g 的倍数。
   - 不要过早取近似：S23 Q5(b) 的 μ = 0.131（ER p.6）。J25 Q1 MS 写明 "Do not ISW"。
2. **答题目问的量：大小还是向量，速率还是速度，减速度为正**
   - J24 ER p.3：失分多因为 "leaving the final answer as a negative value … or leaving an answer as a vector when the magnitude was required"，例子是 J24 Q1(c)、Q2(a)、Q5(a)。
   - 要向量却漏写 j（O23 Q1(a)，ER p.3）；要向量就写成 i、j 形式（S21 Q7(c)，S22 Q1(a)，S24 Q1(b)；J25 Q5(b) 列向量得 B0）。
   - 问速率时写成 2.5i 得 A0（J25 Q3(a)）。冲量大小、速率、距离、加速度大小都必须为正（J23 Q7(b)，O23 Q7(d)，O22 Q7(a)，S21 Q8(a)，S25A Q1(b)(c)）。
   - 把速率当向量代入冲量式是 O22 Q3 最常见的错误：ER 原话 "it is not correct to equate a scalar quantity to a vector quantity"，MS 对这类答卷封顶 3/6。
3. **给定答案（A1*）：步骤写全，终点与题面一字不差**
   - 通则：O22 ER p.3，S23 ER p.3，O23 ER p.3，J24 ER p.3。
   - 写出 x̄ 却从未提到题目要的 d：J24 Q4(a)（ER pp.4–5），O23 Q2(a)（ER pp.3–4）；O25 Q4(a) MS 要求写 "d ="，S25 Q6(a)(b) 要求写 "S ="、"V ="。
   - 三角值的代入必须看得到：J24 Q6(a) 要见到 cos θ 的值（ER p.5），J25 Q7(a) 每个力矩项都要有三角比，不给 benefit of doubt。
   - 硬凑给定答案不得 A1*：S23 Q4(a) 的 "fudge"（ER p.5），O23 Q7(a) 的 "wishful thinking"（ER p.6），O22 Q5(b) 的 "fiddle"（ER p.4）。
   - 只写 "t = 2，v = 0" 而无过程得 A0（S25A Q1(a)）；S25 Q1(a) 必须看到 1.5 和 13.5 的代入；J23 Q8(a) 要说明 1/cos²α = 1 + tan²α（ER p.5）；J22 Q7(a) 最后一步要解释。
4. **"Use the work-energy principle" 就必须用功能原理**
   - 用 suvat 或牛顿第二定律不给分：O20 Q6(b)，S22 Q8(b)，J23 Q5(b)(c)（ER p.4），S23 Q6(c)、Q7(a)（ER p.6），O24 Q3(b)，S25 Q7(a)。
   - 常见漏项与重复：漏掉克服阻力的功（S23 Q6(c)，O23 Q5(b)）；把重力势能增量和克服重力的功各算一次（J23 Q5(b)，S23 Q6(c)，J24 Q3(a)）；漏掉斜面顶端的动能或摩擦功（O22 Q8(b)）；拖车单独运动时用了整车或货车的质量（S23 Q6(c)）；下滑时把摩擦力和重力分量写成同向（J24 Q3(b)）；漏乘距离（J24 Q3(a)）。
5. **功率题**
   - 30 kW 写成 30（J23 Q1(a)，ER p.3）；减速度当成加速度（J23 Q1(b)）；12600 作为 kW 的最终答案得 4/5（J22 Q2(a)）。
   - 把功率当力用得 M0（O25 Q1）；两种工况的牵引力不能取同一个值（S22 Q4 下坡方程沿用平路的牵引力得 M0）；整体质量写错，如 600 kg（J24 Q5(a)，ER p.5）；求拉力时用错阻力（J24 Q5(b)）；重力分量漏 g（S23 Q6(b)）。
6. **碰撞**
   - 先画图标方向：前后方向读错是主要失分（J23 Q7(a)，O23 Q7(a)，J24 Q7(a)，ER 各页）；假设反向却得到负"速率"（O22 Q7(a)）。MS 要求质量与速度正确配对（S25A Q7）。
   - 恢复定律按"分离速度 = e × 接近速度"记，不要背带符号的公式（S23 Q4(c)，ER p.5）。
   - 动能损失写 ½m(u² − v²)，不是 ½m(v − u)²；两个质点都要算，质量用对；答案保留 m 和 u²（S23 Q4(d)，J24 Q7(b)，J23 通则 ER p.3）。
   - 范围题：两端都要，严格与非严格写对（J24 Q7(a)(c)，O23 Q7(c)，O24 Q7(a)）；要说明 Q 会反弹（f > 0，O23 Q7(c)）；J23 Q7(c) 要用上 v ≠ u；J22 Q4(b) 下限可省，写了就要严格。
   - 第二次碰撞的判断要写出速度比较；只列两个速度就下结论得 M0A0（S25A Q7(d)）。
   - 双重符号错误碰巧得到正确答案，封顶 4/6（J21 Q8(a)）。
7. **向量冲量**
   - 减法顺序要对（J24 Q2(a)，ER p.4）；0.25 × 8 漏括号写成 8，一次丢 4 分（O23 Q3，ER p.4）。
   - 动量三角形配余弦定理效率高（O23 Q3）；夹角要找对两条向量（J24 Q2(b)，S23 Q1(b)）。
   - 问冲量大小时不要停在向量（S23 Q1(a)）；动能变化条件用速率平方，22 J 不是末动能（J23 Q2，ER p.3）；两个解都要找（J23 Q2）。
   - S21 Q4：把末速度当成与初速度或冲量平行是方法错误，不按误读处理。
8. **质心与悬挂**
   - 分割要简单，复杂分割最容易错：S23 Q3(a) 是 "by far, the least successful question"（ER p.4）；J24 Q4(a)（ER pp.4–5）；O22 Q6(a)（ER p.5）。
   - 没有说明的梯形质心得 0/5（S23 Q3(a)）；不同密度要计入（O23 Q2(a)）；线框当成薄片最多 B0B0M1A0A0（S25 Q3(a)）；a 全部漏写按误读或特例处理（J21 Q4）。
   - 先写 tan θ 再写 θ（O23 Q2(b)，ER p.4）；给题目要的角（47，不是 43），要整数度就给整数度（J23 Q3(b)，MS "do not ISW"）。
   - 薄片由外力撑住时对转轴取矩，用垂直距离，不要分解力（O23 Q2(c)，ER p.4）；对 A 取矩要计入 S 处的力（J24 Q4(b)，ER p.5）；不必求竖直距离或组合质心（J24 Q4(b)）。
9. **刚体平衡**
   - 墙的摩擦力要画对方向（S23 Q5(a)，ER p.5；O20 Q3 方向错得 A0）；墙的反力垂直于墙，不是垂直于梁（S23 Q5(a)）。
   - 钉的反力垂直于杆，不是竖直（J24 Q6(a)，ER p.5）。
   - 铰链力的两个分量都要计入，沿杆分解时尤其容易漏（J23 Q6(b)，O23 Q6(b)，J24 Q6(b)，ER 各页）；绳在墙上的端点 D 没有反力（O23 Q6(b)）。
   - sin、cos 混淆碰巧抵消仍然扣分（O23 Q6(a)，ER p.5）。
   - S24 Q6(a)：一次分解只能配对应的力矩方程，只分解不取矩只得 SC B1。
   - 要 k 不要 kW（O22 Q5(c)，ER p.3）；要精确值时只给小数得 A0（O22 Q5(c)，O20 Q3）。
10. **微积分运动学**
    - 求总路程要在转向处分段（J24 Q1(b)，ER pp.3–4；O21 Q3(b)，S25 Q1(c)，S25A Q1(b)）。
    - 求导，不要除以 t（J24 Q1(a)，ER p.3）；"show all stages" 的题要手算二次方程（J24 Q1(a)）。
    - 变加速度不能用 suvat（J23 Q4，ER p.4；S23 Q2，ER p.4；O24 Q1 用 suvat 得 M0）。
    - 先求积分常数再代值（O24 Q1(a)，S23 Q2(a)，O22 Q4(b)，ER p.4）；要令 v 的分量而不是 r 的分量（O23 Q1(a)，ER p.3）；方向比例中的 −2 放对边（S23 Q2(b)，ER p.4）。
    - 题目要 exact 就给精确值（S23 Q2(c)，ER p.4）。
11. **抛体**
    - 速度与初速度方向垂直时，水平分量不变，竖直分量为负；用点积，最好画图（S23 Q7(d)，ER p.7；J24 Q8(c)，ER p.6）。
    - 区间题要的是区间长度；不要把速率代进 suvat（J24 Q8(b)，ER p.6）。
    - "vertical distance between" 不是两点间直线距离；题目要求 2 位有效数字就照做（O23 Q4(b)，ER p.4）；落地时间用 2T（O23 Q4(c)）。
    - 方向角要写明从哪里量起（S23 Q7(b)，ER p.6）；位移要从抛出高度起算（S23 Q7(d)）。
    - "By considering energy" 的小问用 suvat 不给分（S23 Q7(a)，ER p.6）。
12. **书写**
    - 说明每个方程代表什么，画带标注的图：O22 ER p.3，J23 ER p.3，S23 ER p.3，O23 ER p.3，J24 ER p.3。
    - 改错时重写，不要在原处涂改（J23 Q3(a)，ER p.4）；写不下时用附加纸并注明位置（O22、S23、O23 ER 通则）。
