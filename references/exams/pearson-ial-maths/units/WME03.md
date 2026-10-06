# WME03 · M3 Mechanics 3：考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WME03.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WME03 --gaps` 输出为准（快照 2026-10-06）**。

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文术语保留原文。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6（M3 单元在 PDF 第 56–58 页）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019；文本版 `registry/src/fb/fb.txt`。力学部分全部在 FB p.13（PDF 第 19 页）。
- 导数点号、平方、分式都对照渲染页图核过：`registry/work/mech-spec/pg-56.png`、`pg-57.png`、`pg-58.png`、`fb-19.png`。纯文本抽取会丢掉 ẍ、θ̇ 上的点。
- 卷面信息取自本地真题封面 `registry/src/WME03/2025-06_01_qp.txt`（WME03/01，Thursday 12 June 2025）。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WME03/01**。另有区域卷 **WME03/01A**，考纲里没有这个代码。英国文化协会中国区 2026 年 1 月和 6 月以 WME03A 报名（10 月不开 M3）。**缺口**：本地没有 WME03/01A 的实卷或评分方案 | SPEC p.8、p.78 Appendix 1；versions.md §1.6 |
| 单元名称 | Unit M3: Mechanics 3 | SPEC p.50、p.67 |
| AS/A2 定位 | 单元页：“Optional unit for IAS Further Mathematics”，“Optional unit for IAL Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IA2**。权重：IAS 33⅓%，IAL 16⅔%。M3 **不能**计入 IAS 或 IAL Mathematics（两者的应用单元组合里都没有 M3） | SPEC p.50、p.67、p.8、p.10 |
| 资格结构 | 只用于 Further Mathematics：IAS/IAL Further Mathematics 的可选单元为 “FP2, FP3, M1, M2, M3, S1, S2, S3, D1” | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.50 |
| 题量（参考） | 2025 年 6 月 WME03/01 封面：“There are 7 questions”，总分 75。考纲不固定题量 | `registry/src/WME03/2025-06_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra manipulation、symbolic differentiation or integration 功能的计算器，也不得存有可调出的公式 | SPEC p.50；Appendix 6，p.86 |
| 卷面要求（试卷封面，不是考纲） | “Whenever a numerical value of g is required, take g = 9.8 m s⁻², and give your answer to either two significant figures or three significant figures.” 以及 “show sufficient working to make your methods clear” | 2025-06 WME03/01 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。FB p.13 的 M3 部分有 Motion in a circle、Centres of mass、Universal law of gravitation 三组；并写明 “Candidates sitting M3 may also require those formulae listed under Mechanics M2, and Pure Mathematics P1, P2, P3 and P4.” | SPEC p.50；FB p.13 |
| 开考季 | **January and June**。从 2020 年 6 月起 October 考季不开 M3 | SPEC p.8、p.70 |
| 2018 版首考 | **“First assessment: June 2020.”** 2020 年 6 月之前 2018 版不开 M3（p.70 表）。2020 年 6 月整季取消，实际第一次开考是 **2020 年 10 月**；2021 年 10 月也例外开考。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | SPEC p.50、p.70；versions.md §1.4–1.5 |
| 旧考纲同代码 | WME03 这个代码 2013 版旧考纲也用过，旧版最后一次是 **2020 年 1 月**，不算本考纲真题。p.1 说 Mechanics 各单元 “have not changed”，所以旧卷内容兼容，可作额外练习。Pearson 官网的 2020 年 1 月 WME03 在 2013 和 2018 两个文件夹里都有，按首考日期它属于旧考纲 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | “A knowledge of the specifications for P1, P2, P3, P4 and M1 and M2, and their prerequisites and associated formulae, is assumed and may be tested.” 注意 **FP1–FP3 都不是先修** | SPEC p.50 |
| 评估目标分配（75 分中） | AO1 20–25；**AO2 25–30**（M1、M2 都是 20–25）；AO3 10–15；AO4 5–10；AO5 5–10 | SPEC p.69 |
| 须背公式（不在 FB 里） | 考纲原文 “Formulae that students are expected to know … will **not** appear in the booklet”：The tension in an elastic string = **λx/l**；The energy stored in an elastic string = **λx²/(2l)**；For SHM：**ẍ = −ω²x**，**x = a cos ωt 或 x = a sin ωt**，**v² = ω²(a² − x²)**，**T = 2π/ω**。M1（p.44）、M2（p.47）的须背清单通过先修关系仍然适用。同处写明 “Questions will be set in SI units and other units in common usage.” | SPEC p.50 |
| 记号 | Appendix 7：4.14 ẋ, ẍ 表示对 t 的一阶、二阶导数（p.90） | SPEC p.90 |
| 单元概述 | “Further kinematics; elastic strings and springs; further dynamics; motion in a circle; statics of rigid bodies.” | SPEC p.50 |

---

## 2. 规格条目逐条（M3.3 Unit content）

### 主题 1 Further kinematics（p.51）

**1.1 Kinematics of a particle moving in a straight line when the acceleration is a function of the displacement (x), or time (t)**（p.51）
- 要求：直线运动中，加速度是位移 x 或时间 t 的函数时的运动学。指导栏：建立并求解下列形式的方程：**dv/dt = f(t)**，**v dv/dx = f(x)**，**dx/dt = f(x)** 或 **dx/dt = f(t)**，难度 “consistent with the level of calculus required in units P1, P2, P3 and P4”。
- 公式：a = v dv/dx 这一形式 FB 不给，指导栏点名要用。

### 主题 2 Elastic strings and springs（p.51）

**2.1 Elastic strings and springs. Hooke’s law**（p.51）
- 要求：弹性绳与弹簧；**Hooke’s law**。指导栏为空。
- 公式：弹性绳张力 = λx/l **须背**（p.50），FB 不给。

**2.2 Energy stored in an elastic string or spring**（p.51）
- 要求：弹性绳或弹簧储存的能量。指导栏：用 work-energy principle 解简单问题，涉及 **kinetic energy, potential energy and elastic energy**。
- 公式：弹性势能 = λx²/(2l) **须背**（p.50）；KE、PE 来自 M2 须背清单。

### 主题 3 Further dynamics（p.51）

**3.1 Newton’s laws of motion, for a particle moving in one dimension, when the applied force is variable**（p.51）
- 要求：质点在**一维**运动、所受力**可变**时的牛顿定律。指导栏：所得方程的求解难度与 P1–P4 的微积分一致；可能涉及万有引力定律，即 **inverse square law**。
- 公式：FB p.13 给出 Universal law of gravitation：Force = Gm₁m₂/d²。

**3.2 Simple harmonic motion**（p.51）
- 要求：简谐运动（SHM）。指导栏：
  - 可能要求证明质点在给定情形下做简谐运动，即证明 **ẍ = −ω²x**；
  - “Geometric or calculus methods of solution will be acceptable.”（几何法或微积分法都可以）；
  - 须熟悉标准公式，“which may be quoted without proof”（可不加证明直接引用）。
- 公式：ẍ = −ω²x、x = a cos ωt 或 a sin ωt、v² = ω²(a² − x²)、T = 2π/ω **须背**（p.50），FB 不给。

**3.3 Oscillations of a particle attached to the end of an elastic string or spring**（p.51）
- 要求：系在弹性绳或弹簧一端的质点的振动。
- 限制：“Oscillations will be in the direction of the string or spring **only**.”（只考沿绳或弹簧方向的振动。）

### 主题 4 Motion in a circle（p.51）

**4.1 Angular speed**（p.51）
- 要求：角速度（angular speed）。指导栏为空。
- 公式：FB p.13 给出 Transverse velocity：v = rθ̇。

**4.2 Radial acceleration in circular motion. The forms rω² and v²/r are required**（p.51）
- 要求：圆周运动的径向加速度，**rω² 和 v²/r 两种形式都要求**。
- 公式：FB p.13 给出 Radial acceleration：−rθ̇² = −v²/r；Transverse acceleration：v̇ = rθ̈。

**4.3 Uniform motion of a particle moving in a horizontal circle**（p.51）
- 要求：质点在水平圆上的匀速圆周运动。指导栏：可能出现 **‘conical pendulum’**、**an elastic string**、**motion on a banked surface** 以及其他情境的问题。

**4.4 Motion of a particle in a vertical circle**（p.51）
- 要求：质点在竖直圆上的运动。指导栏为空。

### 主题 5 Statics of rigid bodies（p.52）

**5.1 Centre of mass of uniform rigid bodies and simple composite bodies**（p.52）
- 要求：均匀刚体和简单复合体的质心。指导栏：“The use of integration and /or symmetry to determine the centre of mass of a uniform body **will be required**.”
- 公式：FB p.13 给出（均匀物体）：Solid hemisphere：距球心 3r/8；Hemispherical shell：距球心 r/2；Solid cone or pyramid of height h：在底面中心到顶点的连线上、距底面 h/4；Conical shell of height h：同一连线上距底面 h/3。M2 的三角形、圆弧、扇形结果也可用（FB 说明）。用积分求质心的一般公式 FB 不给。
- 对比：M2 2.2 指导栏写明 FB 结果 “may be quoted without proof”，M3 5.1 指导栏没有这句，而是写积分和/或对称 “will be required”。由此推断 M3 可能要求用积分推导质心位置，这一点要用真题评分方案核实。

**5.2 Simple cases of equilibrium of rigid bodies**（p.52）
- 要求：刚体平衡的简单情形。指导栏 “To include”：(i) **suspension of a body from a fixed point**（从定点悬挂）；(ii) **a rigid body placed on a horizontal or inclined plane**（放在水平面或斜面上的刚体）。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| 弹性绳张力 λx/l；弹性势能 λx²/(2l) | **须背**（考纲明列） | SPEC p.50 |
| SHM：ẍ = −ω²x；x = a cos ωt 或 a sin ωt；v² = ω²(a² − x²)；T = 2π/ω | **须背**（考纲明列） | SPEC p.50 |
| KE = ½mv²、PE = mgh；动量、冲量、匀加速五式 | **须背**（M2、M1 清单，经先修适用） | SPEC p.47、p.44 |
| 圆周运动：v = rθ̇；v̇ = rθ̈；−rθ̇² = −v²/r | FB 给出 | FB p.13 |
| 实心半球、半球壳、实心圆锥或棱锥、圆锥壳的质心 | FB 给出 | FB p.13 |
| 万有引力 Force = Gm₁m₂/d² | FB 给出 | FB p.13 |
| 三角形薄片、圆弧、扇形的质心 | FB 给出（M2 部分，M3 可用） | FB p.13 |
| a = v dv/dx、用积分求质心的公式（含旋转体）、圆锥摆等情境的受力方程 | FB **未给**，也不在须背清单里，但条目 1.1、4.3、5.1 要求使用 | SPEC pp.51–52；FB p.13（已核对没有） |
| P1–P4 的公式 | FB 给出，M3 可能用到 | FB p.13 的说明 |
| g 的取值 | 不是考纲内容；试卷封面规定 g = 9.8 m s⁻²，答案取 2 或 3 位有效数字 | 2025-06 QP 封面 |

---

## 4. 与相邻单元的界线

- **M2（先修，可直接考）**：M2 1.3 只到加速度是时间的函数（dx/dt = f(t)、dv/dt = g(t)）；M3 1.1 增加加速度是位移的函数（v dv/dx = f(x)、dx/dt = f(x)），3.1 增加变力。M2 2.2 求平面图形质心 “Use of integration is not required”；用积分求质心、三维物体质心在 M3 5.1。M2 2.3 是平面薄片的平衡，M3 5.2 是一般刚体放在水平面或斜面上、或悬挂的平衡。M2 3.1 的能量只有动能和重力势能，弹性势能在 M3 2.2。
- **M1（先修）**：M1 3.1 是匀加速直线运动；匀加速公式在变加速情形下不适用，这是 M3 1.1、3.1 与 M1 的分界。
- **P4（先修，可直接考）**：积分求旋转体体积在 P4 6.1（p.28，P4 指导栏写 “π∫y² dx is required, but not π∫x² dy”），分离变量的一阶微分方程在 P4 6.4（p.28），建立简单微分方程在 P4 5.2（p.27）。M3 1.1、3.1 的微积分以 P1–P4 为限。
- **FP2（不是 M3 的先修）**：二阶常系数线性微分方程在 FP2 5.1（p.38）。M3 3.2 允许 “Geometric or calculus methods”，SHM 标准公式可直接引用，所以 M3 不以 FP2 的二阶微分方程解法为前提。
- **FP3（不是 M3 的先修）**：弧长和旋转曲面面积在 FP3 4.6（p.42）。M3 FB 直接给出半球壳、圆锥壳的质心结果。
- **碰撞**：M3 没有碰撞条目；碰撞全部在 M1 4.3 和 M2 4.1–4.3。

---

## 5. 印刷问题与缺口
- 4.2 行在原版表格里排版错位：“Radial acceleration in circular” 在编号 4.2 的上一行，其余文字与 4.2 同行，属于同一条目。已对照渲染页确认。
- 5.1 指导栏印作 “integration and /or symmetry”（多一个空格），不影响含义。
- 缺口：本地没有 WME03/01A 实卷；Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 往届真题与审核记录（2026-10-06；构建溯源，不随包发布）

本节与第 7 节中的路径都相对于 `registry/`。审核脚本在 `work/wme03audit/scripts/`，改正清单在 `work/wme03audit/fixes.json`（每条写明原文、证据、改动类型），改动前的文件备份在 `work/wme03audit/backup/`，统计结果在 `work/wme03audit/stats.json`、`work/wme03audit/dump_by_spec.txt`。

**逐题索引（合并版）**：`pearson-ial-maths/units/WME03.questions.json`。由同目录 `WME03.questions.part1.json`（49 题：2020-10 至 2022-06 的 6 份正式卷，加 2022 年 1 月未启用卷 P71979A，id 后缀 `01U`）和 `part2.json`（42 题：2023-01 至 2025-06 的 6 份卷）合并而成。按 id 去重（没有重复），按考季 → 卷别（`01` 在 `01U` 前）→ 题号排序。改正同时写回两个 part 文件，合并文件与两个 part 文件逐条一致。合计 13 份卷、91 题、208 个小问、975 分。各卷来源、文件校验与缺口见 `WME03.coverage.part1.md`、`WME03.coverage.part2.md`。

- **格式校验**（构建时的合并校验脚本）：字段齐全，没有多余字段；每题各小问分值之和等于题目总分；每份卷 75 分、7 题，题号连续；spec id 全部在 `spec-items.mech.json` → WME03 中；series 全部符合 YYYY-MM；id 与 paper 一致；有 MS 的卷（13 份全有）每个小问都有 `ms`；有 ER 的卷每个小问都有 `er`，没有 ER 的卷 `er` 全空；引号内的原文都不超过 25 词。结果：0 个问题。
- **完整性**：对照了 `inventory/fm-mech.json`、`inventory/fm-mech-gaps.md`、`versions.json`（WME03 预期考季 2020-10 至 2026-06，共 14 季；2018 版首考是 2020 年 6 月，那一季取消，试卷改在 2020 年 10 月考；2020-01 及以前属于 2013 版，不收）、Edexcel-Finder 清单 `finder/finder-inventory.tsv`（2020-10 至 2025-01 的 11 份正式卷加未启用卷，P 号与题数都和索引一致）和第三方抓取的 Pearson 链接索引 `finder/gh/grademax_manifest/edexcel_2025.json`、`edexcel_2026.json`。**凡是拿得到 QP 文本的卷都已索引**：2020-10 至 2025-06 每个考季的 /01（12 份），加 2022 年 1 月未启用卷。没有收的：Finder 里的 Sample Assessment（S59765A，不是考季）；2014-01 至 2020-01 同代码的 2013 版旧卷。
  - `inventory/fm-mech.json` 和 `fm-mech-gaps.md` 仍把 2020-10 至 2022-06 的 QP 记为“只有 Finder 文本”、MS 记为缺失。这些 PDF 已在 part 1 从 GitHub `RayZ3R0/papernexus-finder@921bdf4f` 取得并核实（`WME03.coverage.part1.md` “New sources found in this pass”），清单本身尚未更新。
- **所有来源都拿不到的卷**：
  - **2026-01 WME03/01、2026-01 WME03/01A、2026-06 WME03/01、2026-06 WME03/01A**：QP、MS 都没有，不知道有没有 ER。这四份卷确实存在：grademax 的 2026 索引列出了 `wme03-01-que-20260122.pdf`、`wme03-01a-que-20260122.pdf`、`wme03-01-que-20260612.pdf`、`wme03-01a-que-20260612.pdf` 及各自的 rms 文件，都在 Pearson 的受限区。
  - 本次复查（2026-10-06）：Drive 上标题含 `WME03`、`wme03`、`Mechanics M3`、`MECH3` 且 2025-08-01 以后创建的文件，都是 2023-06 至 2025-06 已有文件的重复上传；标题含 `2601`、`2606`、`26_01`、`26_06`、`January 2026`、`June 2026` 的 PDF 只有 P4、P4A、S1、S1A。`git ls-remote` 显示 papernexus-finder 仍是 921bdf4f，Edexcel-Finder 仍是 e3db7034，都没有新数据。examsolutions S3 镜像对 `wme03-01-que-20260122.pdf` 返回 403。
  - **2025-06 WME03/01A 不存在的可能性大**：grademax 2025 索引里 M3 只有 /01。
  - **已收卷缺的 ER（8 份）**：2020-10、2021-01、2021-10、2022-01、2022-06、2024-06、2025-01、2025-06。2021-06 整季考试取消，本来就没有 ER；未启用卷没有人考，也没有 ER。本次又用 S3 镜像试了 2021-01、2022-06、2024-06、2025-01、2025-06 的官方文件名，都返回 403（已知存在的 `wme03-01-pef-20230302.pdf` 返回 200）。Drive 全文检索 `WME03` 加 `Examiners`／`Principal Examiner`，只找到 MS 和考纲。所以 ER 只有 2023-01、2023-06、2024-01 三份，覆盖 21 题、48 个小问。
- **准确性**：
  - 逐条对照 QP、MS、ER 原文（`work/wme03p1/clean/`、`work/wme03p2/clean/` 的文本层；分式、根号等看渲染图）复核了 29 题，13 份卷每份至少 1 题，题型分散：O20 Q6、Q7，J21 Q3，S21 Q7，O21 Q1、Q2、Q7，J22 Q3、Q4，J22U Q3，S22 Q2、Q4、Q5，J23 Q3、Q4、Q7，S23 Q2、Q4、Q5，J24 Q6、Q7，S24 Q2、Q4、Q7，J25 Q3、Q7，S25 Q1、Q5、Q6。核对内容包括：分值、spec 映射、命令词、`final_form`（每题按题意重新计算答案，与 MS 答案比对，全部一致）、MS 要点及页码、ER 内容及页码。
  - 发现的错误在 ER 字段，因此把三份 ER 的逐题评述（48 个有 ER 的小问）全部重读了一遍，没有发现别的错误。
  - 另用脚本对全部条目做了 6 项检查：
    - `markscheck.py`：各小问分值与 QP 印刷的 “(n)” 和 “Total for Question” 比对，0 处不符。命令词与印刷比对有 10 处提示，都是引导语写法（如 “Show that (a) …”、“Use … to show that”、“By differentiating …, prove”），不是错误。
    - `ms_checks.py`：所引 MS 页是否含该题评分行，有 4 处提示，都是 2022-01 Q3、Q7 的文本层丢了题号，翻页核对无误。`final_form` 中的数值是否出现在所引 MS 页，有 7 处提示，都是竖排分式被文本层拆开，看 MS 与渲染图核对无误。“or better”一类精度要求是否写进条目，有 1 处提示，那个 “1.7 or better” 属于同页的 Q5，已写在 J22 Q5(e)。
    - `er_checks.py`：ER 页码与“Question n”分节、小问提及位置的对照。提示项都逐条人工核对过。
    - `quotecheck.py`：60 处引号内的原文逐条在 MS／ER／QP 文本中查找。11 处不能逐字匹配，都是符号丢失或表格列交错造成的，按上下文核对无误。其中 O21 Q4(b) 的 MS 原文拼作 “aceleration”，条目引用时写成了正确拼法，未改。
- **发现并改正的错误（1 处；合并文件与 part 2 同步改）**：J23 Q4(a) 的 `er`。原条目写“保留 x = −5 的丢最后一分”，但 ER p.4 原文是 “Occasionally candidates included x = 4 in their solution and so forfeited the final mark”（已看渲染图 `work/wme03audit/img/er2301_q4.png` 确认）。按题意这应是指要舍去的根 −5（MS p.10：“If -5 is seen then it must be rejected”），但原条目把 ER 的字面说法换成了推断，没有交代。现改为如实引用 ER 原文，并注明它显然指 −5。
- **补充（3 处遗漏，不算错误）**：ER 总评页（p.3）点名了几个小问，原条目只引了逐题评述页。J23 Q4(b) 补上“有考生在 4(b) 用时过多，Q7 的评述也提到可能因此影响最后一题”（ER pp.3, 5）。S23 Q3(b)、Q4(b) 补上“这两问情境陌生、没有印刷答案，作答缺乏条理”（ER p.3）。S23 Q4(b) 另补 “Q4 是最不熟悉的情境，连高分考生也受挑战”（ER p.3）。
- **保留未改的判断**：
  - J21 Q3(a)(i)–(ii)（9 分）、S21 Q7(b)(i)–(ii)（8 分）按印刷合并计分；S24 Q1(a)(b) 照印刷分开，虽然 MS 写 “Mark parts (a) and (b) together”。
  - S25 Q1(a)（铰接杆的力矩，实属 M2 内容）标 5.2；S22 Q4(b) 因 MS 的 SHM 解法附带标了 3.3。
  - J25 Q3 MS 写 “accept 1.3√ag or better”（答案 √(3ag) ≈ 1.73√(ag)，疑为 1.7 的印刷错误），已看渲染图确认原文如此，条目照录并加了注。

## 7. 真题需求概览

**数据范围**：`WME03.questions.json` 的 13 份卷，即 2020-10 至 2025-06 每季的 /01（12 份正式卷），加 2022 年 1 月未启用卷（U），共 91 题、208 个小问、975 分。13 份卷都有 MS。ER 只有 J23、S23、J24 三份，覆盖 21 题、48 个小问。2026 年的四份卷拿不到，见第 6 节。下面的数字由 `work/wme03audit/scripts/stats.py` 从索引统计（结果在 `work/wme03audit/stats.json`、`dump_by_spec.txt`）。“问法、终点、评分”来自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节抽查过。未启用卷没有人考过，但出题风格与正式卷相同，所以计入统计；只看正式卷时，各条目的卷数见 7.2 表下的说明。

**引用写法**：J = January，S = June，O = October，后接两位年份；U = 2022 年 1 月未启用卷（J22U）；题号与小问照试卷印刷。“MS”“ER”指该卷的评分方案和考官报告，页码见索引条目的 `ms`、`er` 字段。

### 7.1 卷面结构

- **每卷 7 题、75 分**（13 份卷无一例外）。单题 5–17 分，8–11 分最常见。Q1 是 5–9 分的短题，最后一题 11–17 分。
- **小问**：一题 1 个小问的 14 题、2 个的 45 题、3 个的 25 题、4 个的 6 题、5 个的 1 题。小问分值：1 分 3 个、2 分 18 个、3 分 36 个、4 分 47 个、5 分 39 个、6 分 30 个、7 分 21 个、8 分 9 个、9 分 4 个、10 分 1 个。
- **命令词（208 个小问）**：Find 112，Show that 90，Prove 2，State 2，Describe 1，“Show that / Determine” 1（S21 Q7(b) 合并组）。**93 个小问（约 45%）以印刷结果结尾**，比 M1（约 12%）高得多，所以“把推导写到与印刷完全一致”是 M3 的核心技能。
- **按主条目统计的分值**（每个小问只算 `spec` 的第一个条目）：主题 1 变加速 78 分（8.0%），主题 2 弹性绳与弹簧 190 分（19.5%），主题 3 变力、SHM、弹性振动 224 分（23.0%），主题 4 圆周运动 295 分（30.3%），主题 5 刚体静力学 188 分（19.3%）。
- **每卷固定出现的题**：
  - **恰好一题水平圆周（4.3）、恰好一题竖直圆周（4.4）**，13 份卷都是如此；
  - **恰好一题变加速直线运动**（1.1 或 3.1），13 份卷都有，多在 Q1–Q5；
  - **至少一题质心，且每份卷都有一个用代数积分求质心的小问**（5.1，13/13）。J21、S21、J22、J23、S23、J24 六份卷有两题质心；
  - **至少一个 SHM 小问**（3.2，13/13）。O21、S22、S24 各有两题：一题纯运动学 SHM，一题弹性绳／弹簧上的 SHM；
  - 弹性绳／弹簧（2.1、2.2）每份卷都有。
- **题序**：最后一题是 SHM 或弹性振动的 7 份（S21、S22、J23、S23、S24、J25、S25），竖直圆周 3 份（O20、J22、J24），弹性能量 2 份（J21、J22U），质心 1 份（O21）。Q1 是质心积分的 5 份（J21、S21、J22、J23、S23）。
- **数值与精确**：大多数答案用 m、g、a、l、r 表示（精确式）；约 50 个小问要数值答案，用 g = 9.8 后取 2 或 3 位有效数字。有 5 题印了“不能只靠计算器”的警告（O21 Q2，S22 Q3，J23 Q4，S23 Q1，J25 Q1），积分或求导步骤必须写出。

### 7.2 每个考纲条目怎么考

“卷数／题数／小问／涉及分值（主）”：卷数含 J22U；一个小问可以带几个条目标签，所以各行相加大于 91 题、975 分；括号里是该条目作为第一标签时的分值。“典型分值”指带该标签的小问最常见的分值。

| 条目 | 卷数／题数／小问／涉及分值（主） | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 加速度是 x 或 t 的函数 | 13／13／24／116（78） | Find 16，Show that 8 | 几乎都是两问结构：(a) 用 v dv/dx 由 a = f(x)（J22U Q3，S24 Q3，S25 Q3）、v = f(x)（O21 Q2，S22 Q3，J23 Q4）或合力 F = f(x)（O20 Q5，S21 Q5，J22 Q3，这三题的 (a) 主标 3.1）求 v(x)，或求某处的加速度、力；(b) 再用 dx/dt = v 分离变量求时刻 t、v(t) 或 x(t)（O20 Q5(b)，S21 Q5(b)，O21 Q2(b)，S22 Q3(b)，J22U Q3(b)，J23 Q4(b)，S24 Q3(b)，S25 Q3(b)）。只有 J25 Q1 给 v 是 t 的分段函数：先求 a，再用连续性定 k、积分求 x | 精确式（v = 1 − 2x，v = e^(2−2t)，x = 88/3 + 8 ln 2）、印刷式，或 2–3 位有效数字；小问 4–7 分，5 分最多；一题 8–12 分 | S22 Q3，J23 Q4，S25 Q3，J25 Q1 |
| 2.1 弹性绳与弹簧，Hooke 定律 | 13／29／39／193（92） | Show that 22，Find 16，Describe 1 | ① 静平衡：珠子或质点挂在两固定点间的绳上（O20 Q2，J22 Q6(a)）；一个斜向或垂直于绳的力把绳拉离竖直（J23 Q2，S23 Q2，S24 Q1）；一根绳上挂两个质点（J22U Q1，J25 Q2）；竖直绳或弹簧的平衡位置（O20 Q6(a)，O21 Q3(a)，J24 Q6(a)）；两绳水平拉住（S21 Q7(a)，S22 Q7(a)）；与铰接杆的力矩结合（S25 Q1）。常以 “show that λ = …”“show that AE = …” 印出结果。② 作 SHM 证明、能量题、圆周题里的附带标签。③ “是否保持静止”：张力加重力分量与最大摩擦比较（J21 Q7(b)，S21 Q6(c)，J22U Q7(c)） | λ、长度写成 kmg、ka；印刷结果；单独的平衡题 3–4 分一问，一题 6–10 分 | J23 Q2，S24 Q1，J25 Q2 |
| 2.2 弹性势能、功能原理 | 13／15／19／105（98） | Find 11，Show that 8 | 能量方程，常含两个 EPE 项、GPE、KE，以及摩擦或阻力做的功：粗糙斜面或桌面（O20 Q3，J21 Q7(a)，S21 Q6，J22U Q7）；光滑斜面（S22 Q4，J24 Q2(a)）；竖直方向（O21 Q4(a)，S23 Q7(a)，J22 Q6(c)）；套在竖直杆上的环（J25 Q3）；竖直圆形金属线上的环（J23 Q6(a)）；恒定空气阻力 mg/5（S25 Q4(b)）；水平圆周中的 KE + EPE（J25 Q6(c)）。“最大速率”要先求加速度为零处的伸长（S22 Q4(b)，J22U Q7(b)，O21 Q4(b)） | 速率（精确根式或 2–3 位有效数字）、距离、印刷的 λ；7 分最常见 | S21 Q6，S22 Q4，J25 Q3，S25 Q4 |
| 3.1 一维变力，含平方反比 | 7／8／13／57（47），S22 以后只有 S23、J24 | Find 8，Show that 5 | 平方反比引力，都写成 gR²/x² 或 mgR²/(2x²)：先证 v² 的表达式，再求落地速率、到某速率时的高度、永不停止所需的最小 U（J21 Q2，S23 Q5，J24 Q1）。其他变力：2/x³（O20 Q5），sin 2x（S21 Q5），沿斜面的 (1/3)mx²（J22 Q3） | 印刷的 v² 式；√(kgR) 形式；距离从球心量起，要换算到离地高度（S23 Q5(b)） | J21 Q2，S23 Q5，J24 Q1 |
| 3.2 简谐运动 | 13／16／44／177（109） | Find 29，Show that 11，Prove 2，State 1 | ① 纯运动学 SHM：由周期和某时刻速率求振幅（O21 Q1）；由 x = 4 cos(πt/5) 证明 SHM，再求周期、振幅、最大速率、A 到 B 的时间（J22 Q5）；由每秒振动次数求最大速率与时间（S22 Q1）；潮汐（S24 Q4，答案要用 m h⁻¹ 和钟点）。② 弹性振动的后续小问：过某点的速率（v² = ω²(a² − x²)）、最大速率 aω、最大加速度 ω²a、到达指定位移或速率的时刻、一个周期内满足条件的总时长（S22 Q7(d)，J24 Q6(d)，S25 Q7(c)）、绳第一次变松的时刻（S23 Q7(c)）、走完给定总路程的时间（J22U Q6(c)，S24 Q7(c)） | 精确的单项式，如 (π/3)√(l/(3g))，或 2–3 位有效数字／“or better”；时间题 3–6 分；4 分最常见 | J22 Q5，J23 Q7，J24 Q6，S24 Q4，S25 Q7 |
| 3.3 弹性绳或弹簧末端质点的振动 | 12／14／26／123（68），只有 J22 没有 | Find 14，Show that 10，Prove 1 | 证明 SHM：在一般位置写 N2L，包含所有张力（Hooke 定律里伸长写成 e ± x）和重力，化成 ẍ = −ω²x 并写出 “SHM”，常连带印出周期。情形：竖直单绳（O20 Q6，S23 Q7）；竖直单弹簧（O21 Q3，J22U Q6，J25 Q7）；竖直两绳（J21 Q5，J24 Q6）；水平两绳或两弹簧（S21 Q7，S22 Q7，J23 Q7，S25 Q7）；水平单绳，对能量方程关于 x 求导（S24 Q7(b)）。“only SHM” 要证明绳始终不松（O20 Q6(b)）；初速度可以来自冲量（S21 Q7(b)） | ẍ = −ω²x 加结论，再加印刷的周期；4–8 分，4 分最多 | O20 Q6，S24 Q7，J25 Q7，S25 Q7 |
| 4.1 角速度 | 6／6／6／40（0） | Find 6 | 从未作主条目：由每秒转数或每转所需时间求 ω（O20 Q1，J21 Q3），求一圈的时间 2π/ω（O21 Q5(b)），求 ω（S21 Q2(b)），给定 ω 求力（S25 Q2） | — | O20 Q1，O21 Q5 |
| 4.2 径向加速度 rω² 与 v²/r | 13／22／23／153（0） | Find 13，Show that 10 | 从未作主条目。每份卷的水平圆和多数竖直圆都要写 mrω² 或 mv²/r；MS 要求加速度写成这两种形式之一，写 “a” 不得分（见 7.4 第 8 条） | — | S22 Q2，S23 Q4 |
| 4.3 水平圆周匀速运动 | 13／13／21／123（123） | Find 12，Show that 8，State 1 | 每卷恰好一题。① 圆锥摆的变体：质点在光滑桌面上、绳从桌面上方的点拉住（J22 Q2，J22U Q2，S25 Q2），两根绳（J23 Q5），环与竖直杆（O21 Q5），刚性臂（J21 Q3，S21 Q2），弹性绳（J25 Q6）；② 贴着表面：碗的光滑内表面（S22 Q2，S24 Q2），粗糙圆锥内表面（J24 Q4），带侧向摩擦的倾斜赛道（S23 Q4），转动圆筒的粗糙内壁（O20 Q1）。条件题要给不等式：N ≥ 0 给出 ω 的上限（J22 Q2），两绳张力为正给出 ω² 的范围（J23 Q5(c)），角度范围（J22U Q2），μ 的范围（O20 Q1） | 力、ω、v、长度用 m、g、a 表示；不等式；小问 2–9 分，一题 6–16 分 | J22 Q2，J23 Q5，S23 Q4，J24 Q4 |
| 4.4 竖直圆周运动 | 13／13／34／172（172），主条目分值最多 | Show that 24，Find 10 | 每卷恰好一题，多为三问：(a) 能量方程加径向方程，得到印刷的 T 或 v² 表达式；(b) 判断完整圆周（绳：顶点 T > 0，J21 Q6；杆：顶点 v² > 0，J22 Q7(b)）、最大与最小张力之比（S21 Q4，J22 Q7(c)）、离开球面 R = 0（S24 Q6，S25 Q5）、绳变松 T = 0（O20 Q7(c)，J22U Q5，S22 Q6，S23 Q6，J25 Q5(c)）；(c) 之后按抛体处理：最大高度（S22 Q6(c)，S23 Q6(c)），经过 O 所在水平线时的方向（S24 Q6(b)，S25 Q5(c)），是否落回碗里（J24 Q7(c)），绳何时再绷紧（J22U Q5(c)）。其他情境：撞桌边反弹（O20 Q7），钉子或桌边改变半径（O20 Q7(b)，J25 Q5），竖直圆形金属线上带弹性绳的环（J23 Q6） | 34 个小问中 24 个是印刷结果；精确根式；4 分或 7 分最常见 | S22 Q6，J24 Q7，S25 Q5 |
| 5.1 刚体与组合体的质心 | 13／19／36／174（138） | Show that 21，Find 15 | ① 每卷都有一个代数积分求质心的小问：FB 已给的结果也要“用代数积分证明”，如实心半球 3r/8（O20 Q4，J22U Q4，S22 Q5，S25 Q6）、实心圆锥 3h/4（O21 Q7，S24 Q5）；旋转体（J21 y = 1/x，S21 y = 3 − √x，J23 y = 1 + √x，J24 y = ¼x(3 − x)）；薄片的 ȳ（J22，S23，J25），半圆片 4r/(3π)（J24 Q5(a)）。② 组合体（加或减，壳体按面积算）：圆锥壳加半球壳（S21 Q1），圆柱壳加半球壳（J22 Q4），方纸板挖圆再加圆锥壳（J23 Q3），圆锥台（O21 Q7(b)），两圆锥相减（S23 Q3），圆锥挖去圆柱（S24 Q5(b)），半球挖去小半球（S25 Q6(b)），半圆片剪拼（J24 Q5(b)），圆柱加半球（J22U Q4(b)），半球加圆锥（S22 Q5(b)），半球加质点（O20 Q4(b)） | 主条目的 28 个小问中 20 个是印刷结果；5 分最常见 | J23 Q3，S24 Q5，S25 Q6 |
| 5.2 刚体平衡的简单情形 | 12／14／14／55（50），只有 S21 没有 | Find 13，Show that 1 | (i) 悬挂：自由悬挂求角度（J21 Q4(b) 得 50°，J24 Q5(c) 求 tan θ），两根竖直绳吊起求张力比（S23 Q3(b)），铰接加水平力（J25 Q4(b)），铰接杆由弹性绳拉住（S25 Q1(a)）；(ii) 放在平面上：斜面上将要翻倒（J22 Q4(b)，J23 Q3(b)，J24 Q3(b)，S24 Q5(c)），曲面着地平衡（“任意一点接触都能平衡”推出质心在球心：S22 Q5(b)，J22U Q4(c)；给定倾角：O20 Q4(b)，S25 Q6(c)；由平衡条件证明不等式：O21 Q7(c)） | tan 的精确值、角度（度）、参数 k；2–6 分，3 分最多 | J24 Q5(c)，S24 Q5(c)，S25 Q6(c) |

只看 12 份正式卷时：3.1 在 7 份卷出现，3.3 在 11 份，5.2 在 11 份，4.1 在 6 份，其余条目每份正式卷都有。

**终点形式**（按主条目，自动分类，仅供参考）：3.3 的 12 个主小问全部是印刷结果；4.4 有 24/34，5.1 有 20/28 是印刷结果；3.2 以精确式（17）和数值（12）为主；5.2 以精确的 tan 值和参数为主（7），另有 5 个数值；1.1 以精确式为主（8），印刷与数值各 4 个。

**`WME03.md` 第 2 节 5.1 的待核实点已有答案**：M3 确实要求用积分推导质心。13 份卷每份都有一个代数积分求质心的小问；FB 已给的实心半球、实心圆锥结果，也有 6 次以 “show, using algebraic integration” 的形式考查（O20、J22U、S22、S25 的半球，O21、S24 的圆锥）。

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据：13 份卷的索引检索，加 QP 文本关键词检索（`work/wme03p1/clean/`、`work/wme03p2/clean/` 的 QP 文本）。12 个条目每个都考过，最少的 3.1 也在 7 份卷出现；下面列的是条目里的具体要点。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 dv/dt = f(t)（直接给出加速度是 t 的函数） | 从未出现。唯一的时间函数题 J25 Q1 给的是 v(t)（分段），再求 a 和 x | M2 已练过 a = f(t)；一张“a = dv/dt，x = ∫v dt，分段时用连续性定常数”的卡即可 |
| 1.1 dx/dt = f(x) | 只作第二问出现（求 t），从未单独成题 | 和 v dv/dx 放在同一张流程卡里 |
| 3.1 FB 的万有引力公式 Gm₁m₂/d² | 3 次平方反比题都写成 gR²/x² 或 mgR²/(2x²)，从未用 G 或给出数值 | 一张卡：由“在表面 x = R 时加速度为 g”定出 k = gR² |
| 3.1 一维变力 | 只有 7 份卷出现；S22 以后只在 S23、J24 出现（都是引力） | 与 1.1 合并练 |
| 4.3 “conical pendulum” | QP 从未用这个词；单绳、质点悬空的标准圆锥摆没有单独出现，但变体每卷都有（桌面上、两绳、刚性臂、环） | 标准圆锥摆作基础卡，变体各做一张受力图卡 |
| 4.3 elastic string | 只有 J25 Q6 一次 | 一张卡：半径随伸长变化，张力用 Hooke 定律 |
| 4.3 banked surface | 只有 S23 Q4 一次（倾斜赛道）；J24 Q4 的粗糙圆锥内表面是同类 | 一张卡：有摩擦时要重新设 R，摩擦方向取决于“最大”还是“最小”速度 |
| 4.1、4.2 作主条目 | 从未，只作附带标签（各 6、23 个小问） | 嵌在 4.3、4.4 的卡里，不单独做计算卡 |
| 5.1 用积分推导壳体质心（半球壳 r/2、圆锥壳 h/3） | 从未要求推导；只作为 FB 结果用于组合体（S21 Q1，J22 Q4，J23 Q3） | 直接引用 FB；注意壳体按面积算质量 |
| 5.1 绕 y 轴旋转（π∫x² dy） | 从未出现，全部绕 x 轴；P4 指导栏也写 “π∫y² dx is required, but not π∫x² dy” | 不必练 |
| 5.2 先滑动还是先翻倒 | 从未要求比较。斜面题都写 “sufficiently rough to prevent … sliding”（J22 Q4，J23 Q3，J24 Q3）或只说 rough（S24 Q5） | 练“将翻倒 ⇔ 重力作用线过最低的边” |
| 3.3 振动方向 | 考纲限定只沿绳或弹簧方向振动，真题都遵守；不在同一直线上的弹性振动不会考 | 不必练 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 J23、S23、J24 三份；没有标 ER 的条目来自 MS 的评分说明。下面每条的出处都在本次审核中核对过原文（MS／ER 文本层，必要时看渲染图）。

1. **g 与精度**。每份 MS 的通用说明，以及 J23、S23、J24 三份 ER 的总评都写：用 g = 9.8 后答案给 2 或 3 位有效数字，g 的精确倍数通常接受。g = 9.81 在力学卷不接受（J24 Q2(b) ER）。S21 Q6(a)(b) MS 写 “2 or 3 sf as g has been used”；J21 Q3(a) 两个张力都要 2 或 3 位有效数字。题目要精确值时不能给小数：J22 Q7(c) k = 17/2（“Must be exact”），S22 Q5(b) k = √3，J23 Q3(b) 要精确分数，S24 Q5(c) tan α = 26/29。S25 Q7(b)(c) 要求答案写成单项式（single term）。
2. **变加速必须用微积分，suvat 不给分**。O20 Q3 MS：“answers using constant acceleration score no marks”；O21 Q4(b) MS：用匀加速公式 0/4；S22 Q6(a) MS：“M0 for v² = u² + 2as”；S25 Q3 MS 同样不给 suvat 分。积分前要把加速度写成 v dv/dx：J22 Q3(a) 的 DM1 要求这种形式；S24 Q3(a) MS：“M0 if acceleration is dv/dx or dv/dt”；J24 Q1(a) 从 ½v² = ∫… 起步，MS 最多给 M0M1A0*，ER 要求先列出 v 与 x 的微分方程再分离变量。J23 Q4(a) ER：最常见的概念错误是只把 v 对 x 求导。用能量法时功要用积分（S23 Q5(a) MS 与 ER）。
3. **积分常数、根的取舍、距离的起点**。+c 要用初始条件定出（J22 Q3(a) MS：“+c should be dealt with”）；开方要说明取正根，如 x > 0（J22U Q3(b) MS）；不合题意的根要舍去（J23 Q4(a) MS：“If -5 is seen then it must be rejected”）。平方反比题的距离从球心量起，要减去 R（S23 Q5(b) ER）。“explaining your reasoning” 要对 2gR²/x 项讨论 x → ∞（S23 Q5(c) MS 与 ER）。有计算器警告时，积分式必须写出（S23 Q1 MS：“the correct answer must come from integrated expressions”）。
4. **Show that：写出步骤，结果与印刷完全一致**。等式与印刷答案之间至少一行化简：J24 Q2(a) ER，S23 Q6(a) ER，S25 Q5(b) MS（“A line of working with terms collected must be seen”），S24 Q7(a) MS。结果要连同单位、所求量的名字一起写出：J23 Q1 ER（两问的印刷答案都带单位，只有 40% 拿满分），J24 Q6(a) MS 与 ER（“Must see AE =”），J24 Q5(b) ER（要写 “d = 4a/π”）。在错误推导后抄上印刷答案不得分：J23 Q3(a) ER，S23 Q7(a) ER，J24 Q6(b) ER。印刷答案之后的小问要照做，它们不一定更难：J23 Q3(b) ER，S23 Q7 ER。
5. **SHM 证明**。在一般位置写 N2L，所有力都要有；漏掉重力，即使最后“得到”印刷答案也不给分（J24 Q6(b) ER）。位移要从平衡位置量起（O20 Q6(b) MS）。最后要用 ẍ，不能用 a（O20 Q6(b) MS：“Must be ẍ now”；J25 Q7(a) MS：没用 ẍ 时最多 M1 DM1 A0 A0* DM1 A1*）。要写出 “SHM” 结论：很多考生把 ẍ = −ω²x 只当作求周期的中间步骤，因此丢分（J23 Q7(a) ER，S23 Q7(b) ER）；没有结论时 J25 Q7(a) MS 最多给 M1 DM1 A1 A0* DM1 A1*。由 ω 到印刷周期之间也要至少一行（S25 Q7(a)、J25 Q7(a) MS）。“only SHM” 要说明绳始终不松（O20 Q6(b) MS：振幅 2a/3 小于平衡伸长 4a/3）。题目要求对能量方程求导时，用 N2L 是 M0（S24 Q7(b) MS）。
6. **SHM 计时**。选 sin 还是 cos 要与 t = 0 的位置对应：O21 Q1(a) MS：“Use of v = ±aω sin ωt scores M0”（这等于假设 t = 0 在端点）。完整的方法通常要在周期的若干分之一上加或减：S23 Q7(c) ER，J23 Q7(d) ER（x = a sin ωt 也行，但很少有人做完），J24 Q6(d) ER（常留空）。先求对振幅，画简图有帮助（J24 Q6(c) ER）。速率和最大加速度写正值（J23 Q7(b)(c) MS 与 ER）。按题目要求的单位作答：S24 Q4(a) MS，速率 “must be in metres per hour”。
7. **弹性绳与能量**。自然长度要用对：J22U Q1 MS：“M0 if 11a is used for natural length”；S25 Q4(a) MS 允许按整根绳（自然长度 3a）或两根半绳（各 3a/2）算 EPE，但公式里的自然长度要与所取的绳对应。两根绳的伸长不同，不能设成同一个 e（J21 Q5(a) MS）；不同段的张力不能设为相等（J25 Q2 MS：“M0 if T_XP = T_PQ or T_PQ = T_QY”）。Hooke 定律里是伸长，不是绳长 AB（J23 Q2 MS）。EPE 写成 kx² 并用对伸长：S22 Q4(b) MS 用 l/4 作伸长是 M0。能量方程项要齐：J25 Q3 MS（2 个 EPE、2 个 KE、GPE），J23 Q6(a) ER（很多人没认出要用 EPE，用 Hooke 定律做不下去），S25 Q4(b) 还要加阻力做功。最大速率在加速度为零处（S22 Q4(b)，J22U Q7(b)，O21 Q4(b)）。平衡问题用 EPE 是 M0（S24 Q1(b) MS）；(a) 用了 Hooke 定律，(b) 也必须用（S25 Q1(b) MS：“If HL is seen in (a) it must be used in (b)”）。
8. **圆周运动的方程**。加速度写成 v²/r 或 rω²，不能写 “a”：J22 Q2 MS，S23 Q4(a) MS（“Allow rω² for acceleration but not 'a'”），S24 Q2(b) MS。半径要用圆的半径：S22 Q2 MS（用 r 代替 6r sin θ 只得 M1A1A0），J25 Q6(a) MS（“A0 if OP is the radius”），S25 Q2 MS（半径错算准确度错误）。反力要分解：S22 Q2 MS，“If R is not resolved then M0”。加摩擦后要重新设 R：S23 Q4(b) MS（“M0 if R from (a) is used”）与 ER。常见误解：R = mg cos α，以为垂直于斜面方向平衡（S23 Q4(a) ER）；摩擦写成 μmg cos θ（J24 Q4 ER）。写的是方程，不是表达式；F 不要同时代表摩擦和 ma（S23 Q4(a) ER）。圆周上某点要写运动方程，不能写平衡方程（J23 Q6(b) ER）。几何关系要用文字说明，不能只写没标位置的 θ（J23 Q5(a) ER）。
9. **条件写成不等式，并说明依据**。J22 Q2 MS：“Must see correct inequality stated, not N = 0 or N > 0”；J23 Q5(c) ER：要一开始就写 T_A > 0 且 T_B > 0，只解 T = 0 不够；J22U Q2 MS：角度范围 “Must come from an inequality”；O20 Q1 MS：F ≤ μR。完整圆周要给理由：绳在顶点 T > 0（J21 Q6(a)），杆在顶点 v² > 0（J22 Q7(b)），最大张力与断裂张力比较（J21 Q6(b)）。J24 Q7(b)：不等式成立的依据是 R ≥ 0，MS 规定不提 R 最多 M1A1M1A0*，ER 说写 v ≥ 0 不是有效依据。离开表面用 R = 0（S25 Q5(b) MS：“M0 if R is never zero”；S24 Q6(a)）；绳变松用 T = 0，用 V = 0 是 M0（J25 Q5(c) MS）。
10. **离开圆周后的抛体阶段**。最高点仍有水平速度分量，动能不会全部变成势能（S23 Q6(c) ER）；最大高度要加上绳变松处的高度（S23 Q6(c) ER）；用竖直分量，不是速率（S23 Q6(c) ER）；分量要从离开点的速率 v 算，用 (a) 的速率是 M0（S24 Q6(b) MS）。弦长 BC = 2r sin θ 而不是 2r，并要写出“落回碗里”的结论（J24 Q7(c) ER）；正确引用射程公式按特殊情况给 M1A1M1A1（J24 Q7(c) MS）。用 α 的小数值推出的印刷结果不给 A1*（S25 Q5(c) MS）。画大而清楚的图，标明水平和竖直方向（S23 Q6(c) ER，J24 Q7(c) ER）。
11. **质心**。薄片 ȳ 的公式 ∫½y² dx ÷ ∫y dx 要记住：S23 Q1 ER 说五分之一的考生记错或去求 x̄，只得 0 或 1 分。积分要先算出再相除，一步按计算器得出印刷答案不给分（J24 Q3(a) ER）；题目已给的体积或面积不必再积分（J24 Q3(a)、Q5(a) ER）。π 要么分子分母都有，要么都没有：S22 Q5(a)，S21 Q3(b)，O20 Q4(a)，J23 Q1(b)，J24 Q5(a)，J25 Q4(a)，S25 Q6(a) 的 MS。实心体不能当薄片：S25 Q6(a)(c) MS “M0 for a lamina”，(b) 当薄片最多 0100。壳体按面积，不按体积：J22 Q4(a) MS（“not using volumes”）。圆锥壳的斜高要用勾股定理：J23 Q3(a) MS（“A common error is to use 6a as slant height”）与 ER。约成简单的质量比（S23 Q3(a) ER：H : h : H − h）。结果要化到最简：J21 Q1(b) MS，分母留着 1 − 1/a 丢最后的 A1。漏掉 a 按特殊情况减分（J21 Q4(a) MS）。力矩要写成方程，不能只停留在表格或列向量里（J24 Q5(b) ER）。
12. **翻倒与悬挂的角度**。问 tan 就给 tan，不要只给角度：J24 Q5(c) ER，S24 Q5(c) MS（“A0 if they got straight to α”）。比值不要倒过来：S25 Q6(c) MS（A1ft 处 “Do not condone the reciprocal”），S23 Q3(b) ER（最常见的错误是比值上下颠倒）。距离从正确的点量起：J24 Q5(c) ER（要从 A 量，不是 B）。在图上标出角度才找得到三角形（J24 Q3(b) ER）；题目要度数时用弧度是 A0（J24 Q3(b) MS）。“曲面任意一点接触都能平衡”等价于质心在球心（S22 Q5(b)，J22U Q4(c)）。用临界情况的等式时，要说明不等号的方向（O21 Q7(c) MS）。
