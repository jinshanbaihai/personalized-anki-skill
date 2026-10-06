# WME01 · M1 Mechanics 1：考纲摘要

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文术语保留原文。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6（M1 单元在 PDF 第 50–52 页）。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019；文本版 `registry/src/fb/fb.txt`。页码为印刷页码，力学部分全部在 FB p.13（PDF 第 19 页）。
- 不等号、分数、上标都对照渲染页图核过：`registry/work/mech-spec/pg-50.png`、`pg-51.png`、`pg-52.png`、`fb-19.png`。纯文本抽取会丢字符，例如 5.3 的 “F ≤ μR” 抽成了 “F  µR”。
- 卷面信息取自本地真题封面 `registry/src/WME01/2025-10_01_qp.txt`（WME01/01，Monday 13 October 2025）、`2025-10_01A_qp.txt`、`exemplar_01A_specimen.txt`。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WME01/01**。另有区域卷 **WME01/01A**，考纲里没有这个代码。已见实例：2025 年 10 月 WME01/01A 试卷（P87438A，Monday 13 October 2025），形式为单独的 “Question Paper” 加 “Answer book (sent separately)”；另有 2026 年 Pearson 发布的 WME01/01A Exemplar Answer Book（S87870A）。英国文化协会中国区 2025、2026 年 10 月以及 2026 年 1 月、6 月都以 WME01A 报名 | SPEC p.8、p.78 Appendix 1；versions.md §1.6；本地 QP 封面 |
| 单元名称 | Unit M1: Mechanics 1 | SPEC p.44、p.67 |
| AS/A2 定位 | 单元页：“Optional unit for IAS Mathematics and Further Mathematics”，“Optional unit for IAL Mathematics and Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IAS**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.44、p.67、p.8 |
| 资格结构 | IAS Mathematics：P1、P2 必考，再从 M1、S1、D1 中选一门。IAL Mathematics：P1–P4 必考，应用单元只能是以下组合之一：“M1 and S1 or M1 and D1 or M1 and M2 or S1 and D1 or S1 and S2”。IAS/IAL Further Mathematics：M1 属可选单元。一个单元成绩只能用于一份资格证书 | SPEC p.10 |
| 时长与分值 | 1 hour 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.44 |
| 题量（参考） | 2025 年 10 月 WME01/01 封面：“There are 7 questions”，总分 75。考纲不固定题量 | `registry/src/WME01/2025-10_01_qp.txt` |
| 计算器 | 允许使用。禁止带 symbolic algebra manipulation、symbolic differentiation or integration 功能的计算器，也不得存有可调出的公式 | SPEC p.44；Appendix 6，p.86 |
| 卷面要求（试卷封面，不是考纲） | “Whenever a numerical value of g is required, take g = 9.8 m s⁻², and give your answer to either 2 significant figures or 3 significant figures.” 以及 “show sufficient working to make your methods clear” | 2025-10 WME01/01 QP 封面 |
| 公式册 | 考试提供 FB（封面写 “Yellow”）。FB p.13 原话：“There are no formulae given for M1 in addition to those candidates are expected to know.” 以及 “Candidates sitting M1 may also require those formulae listed under Pure Mathematics P1 and P2.”（FB Issue 2 把这句从只写 P1 扩展为 P1 and P2，见 FB PDF p.3 变更说明） | SPEC p.44；FB p.13 |
| 开考季 | **January, June and October**。p.70 注：“From June 2020, all units will be assessed in January and June and just units P1, P2, P3, P4, M1, M2, S1 and S2 in October” | SPEC p.8、p.70 |
| 2018 版首考 | **“First assessment: June 2019.”** June 2020 之前可考的考季：2019 年 6 月、2019 年 10 月、2020 年 1 月（p.70 表）。2020 年 6 月整季取消。2021 年 6 月发布了试卷和评分方案，但考试取消，改用教师评估成绩，没有考官报告 | SPEC p.44、p.70；versions.md §1.4–1.5 |
| 旧考纲同代码 | WME01 这个代码 2013 版旧考纲也用过，旧版最后一次是 **2019 年 1 月**，不算本考纲真题。p.1 说 “The Further, Mechanics and Statistics units have not changed”，所以旧卷内容兼容，可作额外练习。Pearson 官网把 2019 年 6 月和 10 月的 WME01 放在 2013 文件夹里，但按首考日期它们属于 2018 版 | SPEC p.1；versions.md §1.4 |
| 先修知识（Prerequisites） | 原文：“A knowledge of P1 and P2 and associated formulae and of vectors in two dimensions.” 注意两点：① 与 M2、M3 不同，这里没有 “is assumed and may be tested” 的说法；② 二维向量在 P1、P2 里没有（向量是 P4 主题 7），所以这是单独列出的先修 | SPEC p.44；P4 7.1，p.28 |
| 评估目标分配（75 分中） | AO1 20–25；AO2 20–25；**AO3 15–20**；AO4 6–11；AO5 4–9。AO3 是建模（使用标准模型、解释结果、讨论假设），M1 的 AO3 比重与 S1、D1 并列最高 | SPEC p.68–69 |
| 须背公式（不在 FB 里） | 考纲原文 “Formulae that students are expected to know … will **not** appear in the booklet”：Momentum = mv；Impulse = mv − mu；constant acceleration 五式 v = u + at，s = ut + ½at²，s = vt − ½at²，v² = u² + 2as，s = ½(u + v)t。同处写明 “Questions will be set in SI units and other units in common usage.” | SPEC p.44 |
| 记号 | Appendix 7：第 9 节 Vectors（p.91）规定 i, j, k 为坐标轴方向的单位向量，\|a\| 为模，â 为 a 方向的单位向量；第 4.14 条 ẋ, ẍ 表示对 t 的一阶、二阶导数（p.90） | SPEC pp.90–91 |
| 单元概述 | “Mathematical models in mechanics; vectors in mechanics; kinematics of a particle moving in a straight line; dynamics of a particle moving in a straight line or plane; statics of a particle; moments.” | SPEC p.44 |

---

## 2. 规格条目逐条（M1.3 Unit content）

### 主题 1 Mathematical models in mechanics（p.45）

**1.1 The basic ideas of mathematical modelling as applied in Mechanics**（p.45）
- 要求：熟悉下列模型术语：**particle, lamina, rigid body, rod (light, uniform, non-uniform), inextensible string, smooth and rough surface, light smooth pulley, bead, wire, peg**。
- 还须熟悉使用这些模型时所作的假设（“the assumptions made in using these models”）。这和 AO3 的 “discussion of the assumptions made” 对应（p.68）。

### 主题 2 Vectors in mechanics（p.45）

**2.1 Magnitude and direction of a vector. Resultant of vectors may also be required**（p.45）
- 要求：求向量的大小和方向，也可能要求求合向量（resultant）。可能要求把向量分解（resolve）成两个分量，或用 vector diagram。题目可能用单位向量 **i 和 j** 表示。

**2.2 Application of vectors to displacements, velocities, accelerations and forces in a plane**（p.45）
- 要求：把向量用于平面内的位移、速度、加速度和力。考纲点名要求会用：**常速度**时 velocity = change of displacement / time；**常加速度**时 acceleration = change of velocity / time。
- 范围：只到这两种“常量”情形。位移是时间的一般函数、要求对向量求导或积分的情形属于 M2 1.3–1.4。

### 主题 3 Kinematics of a particle moving in a straight line（p.45）

**3.1 Motion in a straight line with constant acceleration**（p.45）
- 要求：直线匀加速运动。可能要求图像解法，包括 **displacement-time, velocity-time, speed-time and acceleration-time graphs**。“Knowledge and use of formulae for constant acceleration will be required.”
- 公式：五个匀加速公式**须背**（p.44），FB 不给。

### 主题 4 Dynamics of a particle moving in a straight line or plane（p.45）

**4.1 The concept of a force. Newton’s laws of motion**（p.45）
- 要求：力的概念与牛顿运动定律。指导栏：简单的常加速度问题，可以是标量形式，也可以是 **ai + bj** 形式的向量。
- 公式：牛顿第二定律 F = ma 不在 FB 里，也不在 p.44 须背清单里，但本条要求使用。

**4.2 Simple applications including the motion of two connected particles**（p.45）
- 要求：简单应用，考纲列出可能出现的三类：
  - (i) 两个相连质点沿直线运动或在重力作用下运动，且**每个质点所受的力都是常力**；可能涉及 **smooth fixed pulleys and/or pegs**；
  - (ii) 受力从一个固定值变为另一个固定值的运动，例：质点撞到地面（“a particle hitting the ground”）；
  - (iii) 沿光滑或粗糙斜面**直上或直下**的运动（“motion directly up or down a smooth or rough inclined plane”）。

**4.3 Momentum and impulse. The impulse-momentum principle. The principle of conservation of momentum applied to two particles colliding directly**（p.45）
- 要求：动量与冲量、冲量–动量原理、两个质点**正碰**（colliding directly）时的动量守恒。
- 排除：“Knowledge of Newton’s law of restitution is **not required**.” “Problems will be confined to those of a **one-dimensional** nature.”
- 公式：Momentum = mv，Impulse = mv − mu **须背**（p.44）。

**4.4 Coefficient of friction**（p.45）
- 要求：理解质点**运动时** **F = μR**。
- 注：考纲 4.4 和 5.3 标题都是 “Coefficient of friction”，靠指导栏区分：4.4 是运动中（等号），5.3 是平衡中（不等号）。

### 主题 5 Statics of a particle（p.46）

**5.1 Forces treated as vectors. Resolution of forces**（p.46）
- 要求：把力当作向量处理，会分解力。指导栏为空。

**5.2 Equilibrium of a particle under coplanar forces. Weight, normal reaction, tension and thrust, friction**（p.46）
- 要求：质点在共面力作用下的平衡；涉及的力为 **weight, normal reaction, tension and thrust, friction**。
- 限制：“Only simple cases of the application of the conditions for equilibrium to uncomplicated systems will be required.”

**5.3 Coefficient of friction**（p.46）
- 要求：理解**平衡**状态下 **F ≤ μR**（原文 “An understanding of F ≤ μR in a situation of equilibrium”）。已对照渲染页确认是 ≤。

### 主题 6 Moments（p.46）

**6.1 Moment of a force**（p.46）
- 要求：力矩。指导栏：作用在物体上的**共面平行力**（coplanar parallel forces）的简单问题，以及这种情形下的平衡条件。
- 范围：只到平行力。非平行共面力（如靠墙的梯子）属于 M2 5.2。

---

## 3. 公式：FB 已给 vs 须自己掌握

| 内容 | 状态 | 出处 |
|---|---|---|
| Momentum = mv；Impulse = mv − mu | **须背**（考纲明列） | SPEC p.44 |
| 匀加速五式 v = u + at，s = ut + ½at²，s = vt − ½at²，v² = u² + 2as，s = ½(u + v)t | **须背**（考纲明列） | SPEC p.44 |
| M1 专用公式 | FB **一条也不给**：“There are no formulae given for M1 in addition to those candidates are expected to know.” | FB p.13 |
| F = ma、W = mg、F = μR / F ≤ μR、力矩 = 力 × 垂直距离、velocity = change of displacement / time、acceleration = change of velocity / time | FB **未给**，也不在 p.44 须背清单里，但条目 2.2、4.1、4.4、5.3、6.1 要求使用，等于必须掌握 | SPEC pp.45–46；FB p.13（已核对没有） |
| P1、P2 的公式：P1 部分只有 Mensuration（球面积、圆锥侧面积）和 Cosine rule；P2 部分是等差/等比数列、对数、二项式、梯形法则 | FB 给出，M1 可能用到。正弦定理、二次方程求根公式、弧度制的弧长与扇形面积 FB 均未列 | FB p.3；FB p.13 的说明 |
| g 的取值 | 不是考纲内容；试卷封面规定 g = 9.8 m s⁻²，答案取 2 或 3 位有效数字 | 2025-10 QP 封面 |

---

## 4. 与相邻单元的界线

- **P1/P2（先修）**：M1 默认学过 P1、P2 及其公式（p.44）。M1 本身不涉及微积分：3.1 只到匀加速，变加速和对时间求导、积分在 M2 1.3–1.4。
- **P4（不是 M1 的先修）**：向量在 P4 主题 7（p.28–29），包括三维向量、position vectors、直线的向量方程、scalar product。M1 只要求二维向量（先修里单独写 “vectors in two dimensions”），题目用 i、j，见 2.1、4.1。
- **M2（以 M1 为先修，p.47）**：
  - 竖直平面内的匀加速运动、抛体（projectile）→ M2 1.1–1.2。M1 3.1 只到直线运动。
  - 位移是时间的函数、向量对时间求导和积分 → M2 1.3–1.4。M1 2.2 只到常速度、常加速度时的“变化量除以时间”。
  - 动量作为向量、向量形式的冲量–动量原理、**Newton’s law of restitution**、碰撞损失的机械能、连续碰撞 → M2 4.1–4.3。M1 4.3 明确排除恢复系数，并限于一维。
  - 动能、势能、功、功率、work-energy principle → M2 3.1。M1 没有能量条目。
  - 质心（离散质点组、平面图形、复合图形）和薄片平衡 → M2 2.1–2.3。M1 1.1 列有 non-uniform rod 这一模型，配合 6.1 的平行力矩平衡使用。
  - 非平行共面力作用下的刚体平衡（梯子靠墙等）→ M2 5.2。M1 6.1 限于平行力。
- **M3**：弹性绳与弹簧、变力、圆周运动、SHM 都在 M3，M1 不涉及。
- **S1、D1**：与 M1 没有内容重叠。资格结构上，IAL Mathematics 的应用单元组合里只有 “M1 and M2” 可以让学生考两门力学（p.10）。

---

## 5. 印刷问题与缺口
- 4.4 和 5.3 标题都印作 “Coefficient of friction”，内容只靠指导栏区分。`spec-items.mech.json` 里为这两条在标题后加了指导栏原文的括注以便区分。
- 纯文本抽取把 5.3 的 “≤” 丢成空格，以渲染页为准。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 往届真题与审核记录（2026-10-06）

本节与第 7 节中的路径都相对于 `registry/`。审核脚本在 `work/wme01audit/scripts/`，改正清单在 `work/wme01audit/fixes.json`（每条写明原值、证据、改动类型），改动前的文件备份在 `work/wme01audit/backup/`。

**逐题索引（合并版）**：`pearson-ial-maths/units/WME01.questions.json`，由同目录 `WME01.questions.part1.json`（79 题，2019-06 至 2022-10）与 `part2.json`（82 题，2023-01 至 2026-01，含 2025-10 /01A）合并，按 id 去重（没有重复），按考季 → 卷别（/01 在 /01A 前）→ 题号排序。改正同时写回两个 part 文件，合并文件与两个 part 文件逐条一致。各卷来源、文件校验与缺口见 `WME01.coverage.part1.md`、`WME01.coverage.part2.md`。

- **格式校验**（`merge_validate.py`）：161 题、422 小问、1575 分；字段齐全，无多余字段；每题各小问分值之和等于题目总分；每份卷 75 分，题号连续；spec id 全部在 `spec-items.mech.json` → WME01 中；series 全部符合 YYYY-MM；id 与 paper 一致；有 MS 的卷每个小问都有 `ms`，没有 MS 的卷 `ms` 全空；引号内的原文都不超过 25 词。结果 0 个问题。
- **完整性**：对照 `inventory/fm-mech.json`、`inventory/fm-mech-gaps.md`、`versions.json`（预期考季 2019-06 至 2026-06）、Edexcel-Finder 清单 `finder/finder-inventory.tsv`（2019-06 至 2025-01 每季的 P 号与题数都和索引一致；SAM 不是考季，不收），以及第三方抓取的 Pearson 官方链接索引 `finder/gh/grademax_maths_index.json`（2025-01 至 2026-06）。**凡是拿得到 QP 文本的卷都已索引**，共 21 份：2019-06 至 2026-01 每个考季的 /01（20 份）加 2025-10 /01A。2019-01 及以前同代码的卷属于 2013 版考纲，不收。
- **所有来源都拿不到的卷**：
  - **2026-06 WME01/01**：QP、MS、ER 都没有。
  - **2026-01 WME01/01A**、**2026-06 WME01/01A**：QP、MS、ER 都没有。
  - 这三份卷确实存在：grademax 索引列出了 `wme01-01-que-20260508.pdf`、`wme01-01a-que-20260110.pdf`、`wme01-01a-que-20260508.pdf` 及各自的 rms 文件，都在 Pearson 的受限区。本次在 Drive 上重新检索（标题含 `M1A`、`WME01A`、`wme01-01a`、`26_01`、`26_06`、`2601`、`2606`，以及 2026-01-15 以后创建、标题含 M1/WME01/Mechanics 的文件），只找到 P4、P4A、S1、S1A；两个 GitHub 仓库 `git ls-remote` 仍是 elite-igcse-math 05b0320d、papernexus-finder 921bdf4f，没有更新。
  - 已有卷缺的配套文件：2019-06、2019-10 没有 MS；（critic 2026-10-06：2019-06 MS 的 7 道题〔Q1、Q3–Q8，缺 Q2〕可从 GitHub `ShariarAlamDipto/grademax@9e09116` 的 `data/processed/Mechanics_1/markschemes/2019_Jun_P1_Q*.pdf` 取得，是带 PMT 戳的 Pearson MS 逐题裁切，内容与本索引 2019-06 各题吻合；已放在 `registry/src/WME01/2019-06_01_ms_crops/`，`ms` 字段尚未填写）2026-01 没有 MS（grademax 列出 `wme01-01-rms-20260305.pdf`，拿不到）；ER 只有 2022-10、2023-01、2023-06、2023-10、2024-01 五份，其余各季（2021-06 整季考试取消，本来就没有 ER）都没有。
  - **2025-06 WME01/01A 不存在**：grademax 索引里 2025 年 6 月只有 WMA11–WMA14、WFM02、WME02 有 /01A，WME01/01A 最早一份是 2025-10。`WME01.coverage.part2.md` §3 原来写“不知道是否存在”，已加审核注释。
- **准确性**：
  - 逐条对照 QP、MS、ER 原文（`work/wme01p1/clean/`、`work/wme01p2/clean/` 的文本层，必要时看 `src/WME01/*.txt` 原始抽取和渲染图）复核了 34 题，21 份卷每份至少 1 题，题型分散：S19 Q6、Q8，O19 Q3，J20 Q4，O20 Q6，J21 Q5，S21 Q4，O21 Q7，J22 Q3、Q8，S22 Q5，O22 Q3、Q7，J23 Q7，S23 Q2、Q6、Q8，O23 Q6、Q7，J24 Q4，S24 Q8，O24 Q1、Q5、Q6、Q7，J25 Q6，S25 Q2、Q8，O25 Q2，O25A Q6，J26 Q1、Q2、Q5、Q6、Q7。核对内容：分值、spec 映射、命令词、`final_form`（按题意重新计算答案，和 MS 答案比对；没有 MS 的 J26 各题全部重算并看了渲染图）、MS 要点、ER 内容及页码。
  - 另外用脚本对全部条目做了 6 项检查：每题各小问分值与 QP 印刷的 “(n)” 和 “Total for Question” 比对（`markscheck.py`，只有 3 处已声明的拆分）；367 个有 MS 的小问所引 MS 页是否含该题评分行（`ms_pagecheck.py`）；101 个有 ER 的小问所引 ER 页是否是该题、该小问的评述所在页，以及“最难／最差”一类排名语是否引了 ER 总评页（`er_sections.py`、`er_parts.py`）；`final_form` 中的数值答案是否出现在所引 MS 页（`answercheck.py`）；MS 中 “N or better” 一类精度要求是否写进条目（`orbetter.py`）；命令词与 QP 印刷是否一致（`cmdcheck.py`）。
- **发现并改正的错误（10 处，改了 11 个字段；合并文件和 part 文件同步改）**：
  1. **ER 页码（8 处，集中在“ER 引用”这一块，因此把全部 101 个 ER 小问按题、按小问重查了一遍，没有别的错）**：考官总评（各报告 p.3）里对题目难度的排名被只标成了该题评述页。O22 Q4(a)“全卷最差”、O22 Q5(a)“第二差”改为 ER pp.3–4；J23 Q7(a)、S23 Q7(a)、O23 Q5(a)、J24 Q4(i)“最难的一题”改为 ER pp.3, 5。O22 Q5(b)、(c) 的评述实际在 ER p.5，原标 p.4。`WME01.coverage.part1.md` 里引用 O22 Q5(c) ER 的两处页码也同步改为 p.5。
  2. **S23 Q2(b) 精度**：MS 原文是 “120° or better (118.0724…) OR 240 or better”，即 2 位有效数字的 120° 就给分。原条目写 “118° or better”，会让人以为 120° 不给分。`final_form` 和 `ms` 都已改正。
  3. **O23 Q6(c) 命令词**：QP 印的是 “(i) verify … (ii) find …”，4 分里 3 分给 (i) 的验证，命令词由 Show that 改为 Verify。
- **补充（2 处遗漏，不算错误）**：S24 Q7(d) 的 MS 接受 t = 0.42 或更精确；O24 Q3(c) 的 MS 对第一个 A1 接受 t = 2.7 或更精确，对 A1* 不接受。两条都补进了 `ms`。
- **格式统一（7 处）**：S19、O19、J20 中印作 “Hence find”“Hence show that” 的 3 个小问（S19 Q7(b)、O19 Q6(d)、J20 Q1(c)）命令词由 Find/Show that 改为原样；合并题号标签 “i-ii” 统一为 “i–ii”（J23 Q4、Q6，O23 Q1，J26 Q1）。
- **保留未改的差异**：part 1 在 `ms`/`er` 里用 en dash 写页码区间（pp.14–15），part 2 用连字符（pp.15-16）；两种写法脚本都能识别，没有统一。`final_form` 对没有 MS 的 J26 一律注明 “Indexer's own working”，本次重算全部吻合；J26 Q6(e) 题面“north-east”与计算矛盾（等分量时两分量为负，B 在 S 的西南），按原样保留并注明无法确定 MS 的处理。

## 7. 真题需求概览

**数据范围**：`WME01.questions.json` 的 21 份卷（2019-06 至 2026-01 每季的 /01，加 2025-10 /01A），共 161 题、422 小问、1575 分。18 份有 MS（S19、O19、J26 没有）；ER 只有 O22、J23、S23、O23、J24 五份，覆盖 39 题、101 个小问。S19 只有 Edexcel-Finder 文本（少数式子是重建的，见 `WME01.coverage.part1.md`）。缺的三份 2026 卷见第 6 节。下面的数字由 `work/wme01audit/scripts/stats.py` 从索引统计（结果在 `work/wme01audit/stats.json`、`stats.txt`）；“问法、终点、评分”来自索引的 `ask`、`final_form`、`ms`、`er` 字段，这些字段在第 6 节抽查过。

**引用写法**：J = January，S = June，O = October，后接两位年份；A = /01A；题号与小问照试卷印刷。“MS”“ER”指该卷的评分方案和考官报告；页码见索引条目的 `ms`、`er` 字段。

### 7.1 卷面结构

- 每卷 75 分、7 或 8 题（8 题 14 份，7 题 7 份）。单题 4–18 分，最常见 6–13 分。最后一题通常是分值最大的连接体或多阶段题，13–17 分（S19 Q8 16 分，J20 Q7 18 分，J21 Q8 17 分，S25 Q8 17 分，O25A Q7 17 分）。
- **按主条目统计的分值**（每个小问只算 `spec` 的第一个条目）：主题 1 建模 14 分（0.9%），主题 2 向量 321 分（20.4%），主题 3 直线运动学 352 分（22.3%），主题 4 动力学 497 分（31.6%），主题 5 质点静力学 223 分（14.2%），主题 6 力矩 168 分（10.7%）。
- **几乎每卷固定出现的四类题**：
  - 一题正碰／冲量（4.3，21 份卷都有）：13 份卷放在 Q1，5 份放在 Q2；
  - 一题梁、杆、板的力矩平衡（6.1，21 份卷都有），一般在 Q1–Q5；
  - 一题 i、j 向量（2.1 与 2.2，21 份卷都有），多在后半卷，Q8 是向量题的有 6 份；
  - 一题需要画图的运动学（3.1，21 份卷都有）。**除 O21 外，每份卷都有一个 Sketch 小问**（共 20 个，2–3 分）：速率–时间图 16 个（含 J20 Q5(a)、S21 Q8(a)、S22 Q7(a)、O24 Q4(c)、O25A Q7(a) 这类两车同轴的图），速度–时间图 2 个（S19 Q6(c)、O20 Q2(d)），加速度–时间图 2 个（O25 Q6(b)、J26 Q2(e)）。
- 命令词（422 个小问）：Find 320，Show that 47，Sketch 20，State 18，Write down 8，Determine 3，Hence find 2，Hence show that 1，Deduce 1，Describe 1，Verify 1。约八分之一的小问是要写出到印刷结果为止的完整推导。
- 小问分值：1 分 22 个，2 分 83 个，3 分 125 个，4 分 76 个，5 分 45 个，6 分 34 个，7 分 21 个，8 分及以上 16 个。22 个 1 分小问里 17 个是 State（建模说明 12 个，碰撞后的方向 4 个，摩擦方向 1 个），其余是 Write down 3 个、Find 2 个。

### 7.2 每个考纲条目怎么考

“卷数／题数／小问／涉及分值（主条目分值）”：一个小问可以带几个条目标签，所以各行相加大于 161 题、1575 分；括号里是该条目作为第一标签时的分值。“典型分值”指带该标签的小问最常见的分值。

| 条目 | 卷数／题数／小问／涉及分值（主） | 常见命令词 | 常见问法 | 终点形式与典型分值 | 代表题 |
|---|---|---|---|---|---|
| 1.1 建模术语与假设 | 15／21／26／68（14） | State 13，Find 11（作附带标签），Describe 1 | 1 分的“说明你怎样用了某个假设”：杆不弯（S19 Q3(b)，J20 Q2(b)）、均匀梁的重心在中点（S23 Q4(c)）、绳不可伸长所以加速度相同（S19 Q8(b)，S22 Q3(b)，O25 Q7(c)）、滑轮光滑所以两侧张力相等（O20 Q7(b)，O21 Q7(d)）、绳轻所以各段张力相同（J22 Q7(d)）、质点所以重力作用在一点（J22 Q3(c)）；“提出让模型更真实的改进”2 次（O19 Q6(e)，J21 Q8(c)）；比较几个模型（O21 Q3 三种刹车模型，S23 Q3 两个学生的下落模型） | 一句固定说法；1 分为主，改进题 1–2 分 | J20 Q2(b)，J22 Q7(d)，S23 Q4(c)，O25 Q7(c) |
| 2.1 向量的大小、方向、合成 | 21／39／68／264（95） | Find 60，Show that 7 | 速度或力的大小（精确根式，√101、5√13）；与 i、j 或另一向量的夹角；运动方向写成三位方位角；按大小和方位给出的两力求合力（余弦、正弦定理或分量：O19 Q7，J21 Q5，S24 Q2，J24 Q4，S25 Q4(a)）；合力平行于某向量 → 分量成比例，推出印刷的线性关系（S19 Q5(b)，O25 Q3(c)，O25A Q3(a)，J26 Q3(a)）或求参数（J20 Q6(c)，J25 Q1(b)） | 精确根式、角度取到整数度或按“N or better”、三位方位角；多为 2–5 分，4 分最多 | J21 Q5，J24 Q4，O25A Q3(a)，J26 Q6(b) |
| 2.2 平面内的位移、速度、加速度、力向量 | 20／30／83／305（226），只有 J20 没有 | Find 60，Show that 20 | ① 由两个位置求速度（位移变化÷时间），写 r = r₀ + tv（2 分）；② 写出相对位置向量 AB = b − a 并化成印刷形式（S19 Q7(a)，J21 Q6(c)，J22 Q8(b)，S22 Q8(b)，S23 Q8(c)，S24 Q7(c)，J26 Q6(c)，4–5 分）；③ 判断是否相撞：两个分量要给出同一个 t（O23 Q6(c)，S24 Q7(d)，J26 Q6(d)），或证明两船都经过同一点（J21 Q6(b)，O24 Q3(c)）；④ 最近距离（\|AB\|² 求导、配方或判别式：J21 Q6(d)，J22 Q8(c)，S23 Q8(d)，J24 Q7(c)）；⑤ 某方位时的距离（两分量相等或成比例：S22 Q8(d)，S24 Q7(e)，O21 Q8(c)(d)，J26 Q6(e)）；⑥ 距离等于某值的时刻（O19 Q8(c)，O21 Q4(b)，S22 Q8(e)，O22 Q8(c)）；⑦ 匀加速向量：a = Δv/Δt，求速度沿给定方向的时刻（O20 Q5(d)，S21 Q5(a)，J22 Q6(c)，J23 Q3(c)，S25 Q7） | i、j 形式的向量；时刻（小时、钟点、取到分钟）；精确距离；多为 2–5 分，最后的综合小问 6–8 分 | J22 Q8，S22 Q8，O23 Q6，S24 Q7，J26 Q6 |
| 3.1 直线匀加速运动 | 21／58／135／488（352），分值最多 | Find 99，Sketch 20，Show that 12 | ① 竖直上抛（从高处抛出、落地时间、落地速率、总路程、高于某点的时长：O20 Q2，J21 Q1，O21 Q6，J22 Q4，O22 Q5，J24 Q6，O24 Q7，S25 Q3，O25 Q4），反弹（S19 Q6，O19 Q2）；② 多阶段速率–时间图：画图后用面积求 T，常得到二次方程并要舍去一根（O19 Q6，J20 Q5，J21 Q7，S21 Q8，S22 Q7，J23 Q1，S23 Q5，O24 Q4，J25 Q2，O25A Q7，J26 Q2）；③ 直路上的 suvat（第 n 秒内的路程 S22 Q2(b)，S21 Q2 两段数据求加速度，J23 Q5，J24 Q3）；④ 加速度–时间图（给图求路程 O20 Q8、O23 Q2；画图 O25 Q6(b)、J26 Q2(e)）；⑤ 连接体断绳后的后续运动（O24 Q5(d)，J25 Q7(c)，S25 Q8(e)） | 用 g = 9.8 后给 2 或 3 位有效数字；舍去不合题意的根并说明；速率为正；草图标出关键数值；每小问 2–5 分 | J21 Q7，O22 Q5，J23 Q1，J24 Q6，O25A Q7 |
| 4.1 力与牛顿定律 | 19／44／59／274（86），J20、J21 两卷的动力学题只标了 4.2、4.4 | Find 49，Write down 5，Show that 5 | 向量形式 F = ma（J22 Q6(a)，O22 Q6，J25 Q1(a)，O25 Q3(a)，O25A Q3(b)，J26 Q3(b)，S21 Q3(b)，S23 Q2(c)）；升降机与箱体之间的反力（S21 Q4，O22 Q4，J23 Q7）；阻力模型（S23 Q3(b) 书本下落，O23 Q3(c) 锤钉入地，S24 Q5(b) 降落伞，S25 Q4(b) 驳船，J24 Q3(c) 货车牵引力）；绝大多数动力学小问的附带标签 | 加速度向量或大小、力（N）；多为 3–6 分 | O22 Q4，J23 Q7，S24 Q5(b) |
| 4.2 简单应用与两连接质点 | 20／28／58／272（184），J24 没有 | Find 45，Write down 6，Show that 4，State 2 | ① 定滑轮两侧悬挂（O20 Q7，O24 Q5，J25 Q7，S25 Q8）；② 一端在粗糙平面或桌面、一端悬挂（J20 Q7，J21 Q8，O21 Q7，J22 Q7，O22 Q7，O23 Q7，S24 Q8，O25 Q7，O25A Q5）；③ 汽车拖车、机车推车上坡（S19 Q4，O19 Q3，O20 Q6，S22 Q3，S23 Q7）；④ 叠放质点（S19 Q8，S24 Q3）；⑤ 断绳、着地后的第二阶段（S19 Q8(c)，J21 Q8(b)，S24 Q8(d)，O24 Q5(d)，J25 Q7(c)，S25 Q8(e)）。常先“写出 A、B 的运动方程”（2–4 分），再求 a、T、滑轮受力 | 用 m、g 表示（T = kmg，a = g/5 一类）或数值；单题 13–17 分，常是最后一题（6 份卷最后一题以 4.2 为主） | O21 Q7，O23 Q7，S24 Q8，S25 Q8 |
| 4.3 动量、冲量、正碰 | 21／24／47／144（139） | Find 41，State 4 | 动量守恒求碰后速率；冲量大小（有时要写单位 N s）；碰后方向（State，1 分）；方向未定时求两个值（S21 Q1(b)，O25 Q2(b)）；由冲量求速率（J21 Q2，S22 Q1，O25 Q2(a)，O25A Q1，J26 Q1）；松弛的绳突然拉紧（O19 Q1，S24 Q1）；碰后粘在一起（O22 Q1，O23 Q3）；与地面碰撞的冲量（O24 Q7(b)，S25 Q8(d)） | 用 u、mu 表示的正值；3 分小问最多（28 个） | J22 Q2，S23 Q1，O24 Q1，O25 Q2 |
| 4.4 运动中 F = μR | 17／21／31／174（88），O19、O20、S22、S23 没有 | Find 24，Show that 4，Determine 2 | 沿粗糙斜面上滑或下滑（S21 Q6，J23 Q8(a)，J24 Q8(b)，O24 Q6(b)，S25 Q6(a)）；粗糙水平面上减速，a = μg（O21 Q2(c)，J25 Q3(b)，S24 Q6(b)，J26 Q5）；由运动数据反求 μ（J20 Q7(d)，O21 Q2(c)，J25 Q3(b)，O25A Q5(b)）；连接体中的摩擦（见 4.2） | μ 写成 2 或 3 位有效数字的小数；加速度、时间、距离；多为 5–7 分 | J20 Q7(d)(e)，S21 Q6，S25 Q6(a) |
| 5.1 力的分解 | 21／47／68／336（31） | Find 59，Show that 9 | 作主条目时只有两类：两段绳对滑轮的合力（O21 Q7(c)，J22 Q7(c)，O23 Q7(b)，O25 Q7(d)，用 2T cos(θ/2) 或余弦定理）；两力合成后求大小或角度（S24 Q2，J24 Q4，S25 Q4(a)）。其余都是斜面、斜拉力题里的附带标签 | kmg 或数值；3–4 分 | O23 Q7(b)，J24 Q4，O25 Q7(d) |
| 5.2 共面力作用下的平衡 | 19／23／38／181（58），S19、S24 没有 | Find 30，Show that 5 | 绳上质点加一水平力或垂直于绳的力（J22 Q1，J24 Q1）；环套在粗糙杆或线上（J20 Q4，O21 Q5，O23 Q5）；晾衣绳（O25A Q6）；两绳拉船匀速前进（J23 Q6）；三个向量力平衡求 F3（S21 Q3(a)，S23 Q2(a)）；摩擦未达极限时求摩擦力的大小和方向（O21 Q5(a)，O22 Q3(a)，O23 Q5(a)(b)，J25 Q6(a)） | 张力、法向力、质量；多为 2–4 分 | J20 Q4，J24 Q1，O25A Q6 |
| 5.3 平衡中 F ≤ μR | 17／18／23／134（134），S19、S21、S24、O25A 没有 | Find 15，Show that 4，Determine 2，Deduce 1，Describe 1 | ① 极限平衡：粗糙斜面上加水平力、沿斜面的力或绳（O19 Q4，J22 Q5，O22 Q3(b)，J24 Q8(a)，O24 Q6(a)，J25 Q6(b)，S25 Q6(c)，J26 Q7(a)）；② 求力的最大值和最小值（O20 Q3(b)(c)，O23 Q5(c)）；③ 粗糙水平地面上斜拉（J21 Q3，S22 Q4，O25 Q5(a)）；④ “判断是否保持静止”（S22 Q4(a)，J23 Q8(c)，J25 Q6(c)）；⑤ 证明不等式 P ≤ 5W/8（S23 Q6）；⑥ μ ≥ 1 时会怎样并说明理由（O22 Q7(c)） | μ 或力的数值；不等式或比较后的结论；大题 6–9 分 | O22 Q3(b)，S23 Q6，O24 Q6(a)，J26 Q7 |
| 6.1 力矩 | 21／21／38／168（168） | Find 34，Show that 4 | 均匀或非均匀的梁、杆、板，搁在两个支点上或由两根竖绳吊着；“on the point of tilting”（O19 Q5(a)，J21 Q4，J22 Q3，S23 Q4(b)，J24 Q5(c)，S24 Q4(b)，O24 Q2(b)，J25 Q4(c)，S25 Q5，J26 Q4(b)）；给反力比求重心位置或距离（S21 Q7，O21 Q1，O23 Q1，J24 Q5(b)，O24 Q2(a)）；两反力或两张力相等（S19 Q3(c)，S21 Q7(b)，O25A Q2(b)）；求质量的取值范围（S22 Q5(c)）；绳的最大张力限制（O25 Q1(b)） | 质量、距离、反力；题目要求时给精确值（S23 Q4 的 p = 4/21、q = 2/3）；3 分小问最多（17 个） | J21 Q4，S22 Q5，S23 Q4，J24 Q5，O24 Q2 |

### 7.3 考纲写了、真题还没考过（或极少考）的点

依据：21 份卷的索引检索，加 QP 文本关键词检索（`work/wme01p1/clean/`、`work/wme01p2/clean/` 的 QP 文本和 S19 的 Finder 文本）。12 个条目每个都考过，最少的 1.1 也出现在 15 份卷里；下面列的是条目里的具体要点。

| 考纲要点 | 情况 | 制卡建议 |
|---|---|---|
| 1.1 lamina（薄片） | 21 份卷都没有出现；M1 的平衡题都是杆、梁、板当作 rod | 只需会这个术语的含义，不必做计算卡 |
| 1.1、4.2 peg（钉子） | 作为模型的 smooth peg 从未出现；O23 Q3 的 tent peg 是实物，不是模型钉 | 一张术语卡：光滑钉两侧张力相等，与光滑滑轮相同 |
| 1.1 bead、wire | 各只考过 1–2 次：O21 Q5 粗糙竖直线上的珠子，J20 Q4 粗糙水平线上的两个环 | 和“环套在杆上”（O23 Q5、J24 Q1）放在一起做卡 |
| 1.1 “说明怎样用了某假设” | 11 个小问，都是 1 分；另有 2 个“提出让模型更真实的改进”（O19 Q6(e) 2 分，J21 Q8(c) 1 分）；S21、J24、J25、S25、O25A、J26 六份卷完全没有 1.1 | 照 MS 接受的说法逐条做卡（见 7.4 第 10 条） |
| 3.1 displacement–time graph | 从未出现 | 一张识图卡（斜率 = 速度）即可 |
| 3.1 velocity–time 与 acceleration–time graph | 速度–时间图只有 S19 Q6(c)、O20 Q2(d) 两次要画，O25 Q6 给出图；加速度–时间图 4 次（O20 Q8、O23 Q2 给图，O25 Q6(b)、J26 Q2(e) 要画） | 重点仍是速率–时间图；加速度–时间图做一张“分段水平线、标数值”的卡 |
| 4.2(iii) 光滑斜面 | 只有 O25A Q5 的 Q 在光滑斜面上；其余斜面都是粗糙的 | 不必单独练光滑斜面 |
| 4.4 | O19、O20、S22、S23 四份卷没有运动中的摩擦 | 仍属高频（17 份卷） |
| 5.3 | S19、S21、S24、O25A 四份卷没有极限平衡；证明不等式型只有 S23 Q6 | 极限平衡照常练；不等式证明做一张结构卡 |
| 主题 1 作主条目 | 1575 分里只有 14 分 | 建模说明分值小但几乎送分，做成固定措辞卡 |

### 7.4 反复出现的评分惯例与考官提醒

ER 只有 O22、J23、S23、O23、J24 五份；没有标 ER 的条目来自 MS 的评分说明。下面每条的出处都在本次审核中核对过原文。

1. **g 与精度**。每份 MS 的通用说明都写：用 g = 9.8 后答案给 2 或 3 位有效数字；用 9.81 每题扣一次；过度精确每题扣一次，过早取近似每次都扣。由 9.8 算出的分数不给 A 分：O20 Q6(a)（32/125 is A0），J20 Q7(d)（5/8 is A0），O24 Q6(a)（392/19 A0，40g/19 可以），J25 Q7(b)（7/5 A0）。题目要精确值时不能写小数：S23 Q4(b)，ER 说取 0.67 的人丢了最后一分。中间用近似角也算过早近似：O22 Q3(a) ER（用 α ≈ 36.9° 被扣分），J23 Q8(b) ER（a 取整后再算速度，最后一分丢掉）。
2. **M 分的通用条件**。方程项数要对、量纲一致、该分解的力都要分解；分解时漏写或多写 g 只算准确度错误，漏掉质量、或力矩方程漏掉长度算方法错误（每份 MS 通用说明）。
3. **速率、冲量写正值，方向写清楚**。O22 Q1(a) ER：速率要求正值；O24 Q1(b) MS、S21 Q4 MS：答案 must be positive。方向措辞：O21 Q2(b) MS 写 “Direction changed is B0”；S22 Q1(b) MS 不接受 “motion of Q is unchanged”。
4. **冲量是同一质点动量之差**。质量与速度要配对（O25 Q2 MS：所有 M 分都要求 correct pairings of masses and velocities）；含 g 是 M0（J23 Q2(b) MS）；题目要求时写单位 N s（O22 Q1(b)，S23 Q1(c)，O23 Q3(b)）。
5. **多阶段运动不能用一条 suvat 贯穿**。J23 Q1(b) MS：整段用一个 suvat 公式是 M0；J23 Q5(c) ER：用 t = 14 代一个公式得 0 分；断绳、着地后要用新的加速度和新的初速度：O24 Q5(d) MS（s = 8 直接代是 M0），S25 Q8(e) MS，S23 Q7(c) ER（很多人沿用 0.75 m s⁻²）。不合题意的根要明确舍去：J21 Q7(c) MS。
6. **速率–时间图与速度–时间图**。竖直上抛的速率图是 V 形，不是速度图的一条直线；图末端不要画实线竖线（虚线可以）：O22 Q5(c) ER，另有 12 份 MS 写有 vertical line 的扣分说明（如 O23 Q2(b)、S24 Q5(d)、S25 Q3(c)、O24 Q4(c)）。关键数值都要标出（J23 Q1(a) ER：漏标 3T + 180）。
7. **摩擦**。只有极限平衡或运动时才能用 F = μR：O22 Q3(a) MS（用 F = 0.5R 是 M0），O23 Q5(a) ER。外力改变或撤去后要重新求 R：O24 Q6(b) MS（沿用 (a) 的 R、F 整问不给分），J25 Q6(c) MS（没有新的 R 是 M0），J23 Q8(c) ER。摩擦方向画反是 O22 Q3(b) ER 说的最常见错误。“是否保持静止”要写出不等式或差值再下结论，只写文字不给分：J25 Q6(c) MS；S23 Q6 ER：只在最后一行把等号改成 ≤ 不给最后一分。
8. **连接体：ma 里的质量要和所选物体对应**。S24 Q8 MS：ma 项用错质量，该方程 M0；J23 Q7 ER：整体方程用了升降机的质量 m，丢方法分；O23 Q7(a)(ii) ER：kma 或 kmg 漏 k。静止问题不要加 ma：J24 Q1 ER，J23 Q6 ER（匀速仍写了 ma）。
9. **力矩与“on the point of tilting”**。将要绕某点翻转就是另一支点（或绳）的力为零：J23 Q4 ER（置零的反力选错就一分不得），O22 Q2(a) ER，J24 Q5(c) ER（还要去掉题目说已经拿走的 55 kg）。不能假设两反力相等：S22 Q5 MS（M0）。反力比不要用反：J24 Q5(b) ER，O23 Q1 ER。
10. **建模说明按固定措辞给分**。光滑滑轮：两侧张力相等，写 “same for A and B”“same for both strings” 是 B0（O21 Q7(d) MS）；不可伸长：两个物体加速度相同，写 “the string has the same acceleration” 不给分（O25 Q7(c) MS）；质点：质量或重量集中（作用）在一点，必须提到质量或重量（J22 Q3(c) MS）；均匀：重心在中点；S23 Q4(c) ER 列出的常见错答是 “remains straight”“does not bend”“equal tensions”，以及只说重量作用在一点、没说是梁的中点。
11. **向量**。速度与速率要分清，问速率就给大小（J23 Q3(a) ER：只求出速度丢 2 分）。“平行于／沿某向量方向”要用分量成比例，不能令分量等于该向量（O22 Q6(a) ER；J25 Q1(b) 为此发了 Clarification Notice，把 “in the direction of” 改成 “parallel to”）。所有 MS 的通用说明都接受列向量，但题目要求 i、j 形式时，最终答案写成列向量要扣分：S23 Q8(a) ER，S25 Q2(a)(b) MS，O23 Q6(a)(b) MS，J22 Q8(b) MS。求方位要用相对向量 AB，不是 OA 和 OB（O22 Q8(c) ER），并取到要求的精度（J24 Q4(ii) ER：很多人停在 52° 或 38°）。中途改变航向要先求改向时刻的位置：O23 Q6(d) ER（两船都代 t = 2.5 最多 1/7）。
12. **合成与滑轮受力的向量三角形**。两力夹角 150° 时，三角形里的角是 30°；在正弦或余弦定理里用 150° 是错误的三角形，所有 M 分都没有（J24 Q4 MS 与 ER）。滑轮受力用 2T cos((90° − α)/2)、余弦定理配 90° + α，或水平竖直分量都可以；用 90° − α 是常见错误（O23 Q7(b) ER）。
13. **Show that**。必须写出完整推导，至少一行中间步骤，最后一行与印刷结果完全一致：O25 Q1(a) MS（要有 “x =” 和中间一行），S24 Q7(c) MS（AB 写在开头或结尾），O22 Q6(a) ER；验证型要明确写出 “X = 14.7 ⇒ F = 0” 这样的结论（O22 Q3(a) MS）。
14. **单位换算**。O23 Q3(c) ER：很多人把 12 cm 当成 12 m（MS 对此最多给 3/5）；O24 Q3(b)：速度由 km/h 换成 m/s；J23 Q1(b)：4.8 km、3 分钟要先换成 m 和 s（ER 说绝大多数人换对了）。
