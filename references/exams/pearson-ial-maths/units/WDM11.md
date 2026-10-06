# WDM11 · D1 Decision Mathematics 1：考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `WDM11.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py WDM11 --gaps` 输出为准（快照 2026-10-06）**。

核对日期：2026-10-06。条目编号、措辞和页码以考纲原文为准，本文件的中文是转述，英文关键词照抄考纲。

**来源**
- **SPEC**：Pearson Edexcel International Advanced Subsidiary/Advanced Level in Mathematics, Further Mathematics and Pure Mathematics – Specification – **Issue 3 – April 2019**，ISBN 978 1 446 94981 8。本地文件 `scratchpad/research/dl/ial-maths-spec.pdf`，md5 06d01a11b53e1e03d25a0df0a265510d，与 `registry/versions.md` §1.1 是同一文件。页码一律写印刷页码，印刷页 = PDF 页 − 6。D1 在印刷 pp.63–66（PDF pp.69–72），其中 p.66 是 Glossary for D1。
- **FB**：Mathematical Formulae and Statistical Tables，**Issue 2 – January 2021**。本地文件 `scratchpad/boards/B-S2/src/ial_formulae_booklet.pdf`，md5 a1c61b665dcae1af155e289c78b74019。D1 只涉及 FB p.1 的一句说明。
- 版面与符号对照渲染页图核过（`registry/work/stat-spec/pg-69.png`–`pg-72.png`）。版面文本：`registry/work/stat-spec/lay_p069.txt`–`lay_p072.txt`。
- 试卷封面只用来补充考场要求，不是考纲：`registry/src/WDM11/2025-06_01_qp.txt`（WDM11/01，Thursday 15 May 2025，P76408A）；`registry/src/WDM11/2025-09_01A_specimen.txt`（WDM11/01A Exemplar Paper，S87873A）。
- 新旧 D1 的题面对比：Edexcel-Finder 题面数据 `registry/finder/repo/static/Data/`（提交 e3db703，见 `registry/finder/commit.txt`），只用于 §4 的一条说明。

---

## 1. 单元事实

| 项目 | 内容 | 出处 |
|---|---|---|
| 单元代码 | **WDM11/01**。另有区域卷 **WDM11/01A**，考纲里没有这个代码。英国文化协会中国区 2026 年 1 月和 6 月以 WDM11A 报名。Pearson 出过一份 WDM11/01A “Exemplar Paper”（S87873A，12 页）和配套答题册；脚本比对显示，它的题目与 2025 年 6 月 WDM11/01 几乎相同（较长的文本行 96% 重合），不要当作另一份真题 | SPEC p.9、p.78；versions.md §1.6；`inventory/stat-gaps.md`；本次比对 |
| 单元名称 | Unit D1: Decision Mathematics 1；p.67 表中写作 “D1: Decision Mathematics 1” | SPEC p.63、p.67 |
| AS/A2 定位 | 单元页原文：“Optional unit for IAS Mathematics and Further Mathematics”，“Optional unit for IAL Mathematics and Further Mathematics”。p.67 “IAS or IA2” 一栏为 **IAS**。权重：IAS 33⅓%，IAL 16⅔% | SPEC p.63、p.67、p.9 |
| 资格结构 | IAS Mathematics：P1、P2 必考，再从 M1、S1、D1 中选一门。IAL Mathematics：含 D1 的选修组合是 “M1 and D1” 和 “S1 and D1”。IAS/IAL Further Mathematics 都可选 D1 | SPEC p.10 |
| 时长与分值 | 1 hour and 30 minutes，**75 marks**，“Students must answer all questions” | SPEC p.63 |
| 题量（参考） | 2025 年 6 月卷封面写 “There are 8 questions”，总分 75。考纲没有固定题量 | `registry/src/WDM11/2025-06_01_qp.txt` |
| 答题册（试卷封面，不是考纲） | D1 在**单独的答题册**上作答。/01 封面：“You must have: Decision Mathematics Answer Book (enclosed), calculator”，并要求 “Answer the questions in the D1 answer book provided”。/01A 封面：“Answer book (sent separately).” 两种封面都**没有**要求带公式册 | 2025-06 /01 QP 封面；/01A Exemplar 封面 |
| 计算器 | 允许使用，规则见 Appendix 6 | SPEC p.63；p.86 |
| 卷面要求（试卷封面） | “show sufficient working to make your methods clear”；非精确答案默认保留 3 位有效数字 | 2025-06 QP 封面 |
| 公式册 | 考纲写 FB “will be provided for use in the assessments”，但 FB p.1 写明 “No formulae are required for the unit Decision Mathematics D1.”，FB 里没有 D1 部分 | SPEC p.63；FB p.1 |
| 开考季 | **January and June**。从 2020 年 6 月起 October 考季不开 D1。2020 年 6 月以前，D1 在 2019 年 6 月、2020 年 1 月开考 | SPEC p.9、p.70；versions.md §1.4 |
| 特殊考季 | 2020 年 6 月整季取消。2020 年 10 月和 2021 年 10 月例外地开考了 D1。2021 年 6 月发布了试卷和评分方案，但考试取消，没有考官报告 | versions.md §1.5 |
| 2018 版首考 | **“First assessment: June 2019.”** 实际第一次开考就是 2019 年 6 月 | SPEC p.63；versions.md §1.4 |
| 与旧考纲的关系 | WDM11 是新代码，旧考纲的 D1 是 **WDM01**。p.1 原话：“Decision Mathematics 1 has been updated”（Statistics、Mechanics、Further 各单元则 “have not changed”）。考纲没有列出改了什么；题面检索显示内容确实不同，见 §4 | SPEC p.1；versions.md §1.4 |
| 先修知识 | D1 单元页**没有** “Prerequisites” 条目。代之以 “1. Preamble”，见下一行 | SPEC p.63 |
| Preamble（考纲原意） | ① 须熟悉 Glossary for D1 中定义的术语；② “Students should show clearly how an algorithm has been applied.”；③ “Matrix representation will be required but matrix manipulation is not required.”；④ 要能给情境建模并解释，“including cross-checking between models and reality” | SPEC p.63 |
| 评估目标分配（75 分中） | AO1 20–25；AO2 20–25；**AO3 15–20**；AO4 5–10；AO5 5–10 | SPEC p.69 |
| 须背公式 | D1 **没有**须背公式清单。原文：“Students are expected to know any other formulae that might be required and which are not included in the booklet” | SPEC p.63 |
| 单元概述 | “Algorithms; algorithms on graphs; algorithms on graphs II; critical path analysis; linear programming.” | SPEC p.63 |

---

## 2. 规格条目逐条（D1.3 Unit content）

### 主题 1 Algorithms（p.64）

**1.1 The general ideas of algorithms and the implementation of an algorithm given by a flow chart or text**（p.64）
- 要求：算法的一般概念；执行以流程图或文字给出的算法。
- 排除：“The order of an algorithm is not expected.”
- 规定：“Whenever finding the middle item of any list, the method defined in the glossary must be used.”（找列表中间项一律按 Glossary 的规则，见 §3。）

**1.2 Students should be familiar with bin packing, bubble sort, quick sort, binary search**（p.64）
- 要求：熟悉 **bin packing**、**bubble sort**、**quick sort**、**binary search**。
- 规定：“When using the quick sort algorithm, the pivot should be chosen as the middle item of the list.”
- 说明：考纲没有点名装箱算法的具体变体（如 first-fit），也没有写装箱下界的求法；试卷会考（例如 2025 年 6 月 Q1 要求 first-fit bin-packing 和 lower bound），要从真题和评分方案确认。

### 主题 2 Algorithms on graphs（p.64）

**2.1 The minimum spanning tree (minimum connector) problem. Prim’s and Kruskal’s algorithm**（p.64）
- 要求：最小生成树（minimum connector）问题；**Prim’s** 和 **Kruskal’s** 算法。
- 要求：“Matrix representation for Prim’s algorithm is expected.” 会根据给定矩阵画网络，也会写出网络对应的矩阵。

**2.2 Dijkstra’s algorithm for finding the shortest path**（p.64）
- 要求：用 **Dijkstra’s algorithm** 求最短路径。指导栏为空。

### 主题 3 Algorithms on graphs II（p.64）

**3.1 Algorithm for finding the shortest route around a network, travelling along every edge at least once and ending at the start vertex. The network will have up to four odd nodes**（p.64）
- 要求：求经过每条边至少一次并回到起点的最短路线，“Also known as the ‘Chinese postman’ problem”。网络最多有 **4 个奇顶点**。要用观察法考虑奇顶点的**所有可能配对**（“use inspection to consider all possible pairings of odd nodes”）。
- 排除：“(The application of Floyd’s algorithm to the odd nodes is not required.)”

**3.2 The practical and classical Travelling Salesman problems. The classical problem for complete graphs satisfying the triangle inequality**（p.64）
- 要求：practical 与 classical 两种 **Travelling Salesman** 问题（定义见 Glossary）；classical 问题针对满足 triangle inequality 的完全图。
- 包括：“The use of short cuts to improve upper bound is included.”

**3.3 Determination of upper and lower bounds using minimum spanning tree methods**（p.64）
- 要求：用最小生成树方法求旅行商问题的上界和下界。
- 包括：“The conversion of a network into a complete network of shortest ‘distances’ is included.”
- 说明：考纲没有写下界的具体做法（删去一个顶点后求剩余部分的最小生成树等），要从评分方案确认。

**3.4 The nearest neighbour algorithm**（p.64）
- 要求：**nearest neighbour algorithm**。指导栏为空。

### 主题 4 Critical path analysis（p.65）

**4.1 Modelling of a project by an activity network, from a precedence table**（p.65）
- 要求：由 precedence table 建立项目的 activity network。“Activity on arc will be used.” “The use of dummies is included.”
- 规定：“In a precedence network, precedence tables will only show immediate predecessors.”

**4.2 Completion of the precedence table for a given activity network**（p.65）
- 要求：由给定的 activity network 补全 precedence table。指导栏为空。

**4.3 Algorithm for finding the critical path. Earliest and latest event times. Earliest and latest start and finish times for activities**（p.65）
- 要求：求关键路径的算法；事件的最早、最晚时间；活动的最早、最晚开始与结束时间。指导栏为空。

**4.4 Total float. Gantt (cascade) charts. Scheduling**（p.65）
- 要求：**total float**（定义见 Glossary）；**Gantt (cascade) charts**；**scheduling**。指导栏为空。

### 主题 5 Linear programming（p.65）

**5.1 Formulation of problems as linear programs**（p.65）
- 要求：把问题表述为线性规划。指导栏为空。

**5.2 Graphical solution of two variable problems using ruler and vertex methods**（p.65）
- 要求：两变量问题的图解法，用 **ruler** 法和 **vertex** 法。指导栏为空。考纲**没有** simplex 方法（全文检索无此词）。

**5.3 Consideration of problems where solutions must have integer values**（p.65）
- 要求：考虑解必须取整数的问题。指导栏为空。

---

## 3. Glossary for D1（p.66）

Preamble 要求熟悉这些术语（p.63）。以下按原文转述，粗体为考纲原词。

- **middle item**：N 个元素的列表中，N 为奇数时中间项位置是 [½(N + 1)]，N 为偶数时是 [½(N + 2)]。考纲的例子：N = 9 时是第 5 个，N = 6 时是第 4 个。
- **graph**：由点（**vertices** 或 **nodes**）和连接它们的线（**edges** 或 **arcs**）组成。**subgraph**：每个顶点和每条边都属于 G 的图。
- **weighted graph** 或 **network**：每条边带一个数（通常叫 **weight**）的图。
- **degree** 或 **valency**：与该顶点相连的边数。度数为奇（偶）的顶点叫 **odd**（**even**）顶点。
- **path**：一串边，前一条边的终点是后一条边的起点，且 “no vertex appears more than once”。
- **cycle**（**circuit**）：闭合的 path，最后一条边的终点是第一条边的起点。
- **connected**：两顶点之间有 path 则相连；所有顶点两两相连的图是 connected graph。
- **directed edges**、**digraph**：边带方向的图。
- **tree**：无 cycle 的连通图。**spanning tree**：包含 G 全部顶点的子图，且是一棵树。
- **minimum spanning tree (MST)**：总长度尽可能小的 spanning tree，“sometimes called a minimum connector”。
- **complete graph**：n 个顶点中每个顶点都与其余所有顶点相连。
- **travelling salesman problem**：“find a route of minimum length which visits every vertex in an undirected network”。**classical** 问题中每个顶点只访问一次；**practical** 问题中顶点可以重复访问。
- **triangular inequality**：对三个顶点 A、B、C，length AB ≤ length AC + length CB，其中 AB 是最长的边。（条目 3.2 写作 “triangle inequality”，Glossary 写作 “triangular inequality”，是同一概念。）
- **walk**：一串边，前一条边的终点是后一条边的起点（不要求顶点不重复）。**tour**：访问每个顶点并回到起点的 walk。
- **total float**：活动 (i, j) 的 F(i, j) = lⱼ − eᵢ − duration(i, j)，其中 eᵢ 是事件 i 的最早时间，lⱼ 是事件 j 的最晚时间。除 middle item 的位置式外，这是 Glossary 里唯一的公式；FB 不给。

---

## 4. 与相邻单元的界线

- **P1**：线性规划的可行域要画不等式区域。P1 1.7–1.9（p.14）是一元一次、二次不等式的图像表示与求解；D1 单元页没有把 P1 列为先修。
- **FP1**：D1 要求 matrix representation（如 Prim’s 算法的矩阵形式），但 “matrix manipulation is not required”。矩阵运算在 FP1 主题 5–6。
- **没有 D2**：2018 版共 14 个单元，决策数学只有 D1（SPEC pp.7–9）。
- **旧考纲 WDM01 不能当兼容练习**（与 S1–S3 不同）。考纲只说 D1 “has been updated”。用 Edexcel-Finder 题面做关键词检索（这是题面证据，不是考纲对比）：
  - 2018 版 WDM11 的 13 份题面（2019 年 6 月至 2025 年 1 月）**全部**出现 “nearest neighbour” 和 “lower bound”，**没有一份**出现 “matching”；
  - Finder 里标为 WDM01 的 12 份旧卷（2014 年 1 月至 2020 年 10 月）**全部**出现 “matching”，**没有一份**出现 “nearest neighbour” 或 “travelling salesman”。
  - 由此推断：旧 D1 有匹配（matchings）而没有旅行商问题，新 D1 正好相反（推断，Medium）。用旧卷练习时要跳过匹配题。
  - 同一 Finder 文件夹里还混有英国 6689 D1 旧卷，统计时已排除。
- **术语**：3.1 的题型考纲只叫 “Chinese postman”，没有用 “route inspection” 这个名字；试卷会用这个名字（Finder 的 13 份 WDM11 题面中，2022 年 6 月和 2023 年 1 月两份出现 “route inspection”）。

---

## 5. 印刷问题与缺口

- **公式册说法不一致**：考纲 p.63 说考试提供 FB；FB p.1 说 D1 不需要任何公式；2025 年 6 月 WDM11/01 封面的 “You must have” 只列答题册和计算器。以试卷封面为准，D1 考试实际上不依赖公式册。
- **术语写法不一致**：条目 3.2 写 “triangle inequality”，Glossary 写 “triangular inequality”（p.64、p.66）。
- **Glossary 的 middle item 记号**：[½(N + 1)] 中的方括号考纲没有解释；N 为奇数时 ½(N + 1) 本身就是整数，括号不影响结果。
- 缺口：考纲没有写装箱算法的变体、装箱下界、旅行商下界的具体做法、Gantt 图和调度的作答格式，都要从评分方案和考官报告确认。
- 缺口：2013 版 WDM01 考纲本环境没有取得，新旧差异只能用题面关键词推断（§4）。
- 缺口：Pearson 官网无法访问（403），无法确认 Issue 3 之后是否另有勘误页。versions.md §1.2 用 WebSearch 查过，没有发现新版考纲。

---

## 6. 逐题索引与审核（2026-10-06；构建溯源，不随包发布）

**索引文件**：同目录 `WDM11.questions.json`。它由 `WDM11.questions.part1.json`（2019-06 至 2022-06，8 份卷，56 题）和 `WDM11.questions.part2.json`（2023-01 至 2025-06，6 份卷，44 题）合并而成，按 id 去重（没有重复 id），再按考季、题号排序。构建记录见 `WDM11.coverage.part1.md`、`WDM11.coverage.part2.md`；这两个文件是构建记录，本次没有改，和本节不一致的地方以本节和索引为准。

审核脚本和输出都在 `registry/work/wdm11audit/`：
- 脚本：`completeness.py`（与清单比对）、`markseq.py`（小问分值与印刷的 "(n)" 序列逐题比对）、`cmdcheck.py`（命令词）、`speckw.py`（按算法关键词检查 spec 映射）、`pagecheck.py`（所引 MS 页、ER 页是否落在该题范围内）、`algo_check.py`（装箱、排序、LCM、整数解重算）、`show.py`、`fq.py`、`sec.py`、`apply_fixes.py`、`stats.py`。
- 输出：`validate.txt`、`completeness.txt`、`pagecheck.txt`、`algo_check.txt`、`stats.txt`、`byitem.txt`（按主条目列出全部小问）。
- 改动清单：`fixes.json`（14 处字段改动）；改动前的两个 part 文件和本文件备份在 `backup/`。渲染核对图在 `img/`。

**收录范围**：14 份卷，100 题，356 个小问，1050 分。

| 考季 | 卷 | 题数 | 题目来源 | MS | ER |
|---|---|---|---|---|---|
| 2019-06（2018 考纲首考） | /01 | 6 | **只有 Edexcel-Finder 文本**（P61648A） | 缺 | 缺 |
| 2020-01 | /01 | 7 | 只有 Finder 文本（P60708A） | 缺 | 缺 |
| 2020-10（封面 Tuesday 19 May 2020，原定 2020 年 6 月的卷，10 月实考） | /01 | 8 | 只有 Finder 文本（P62510A） | 缺 | 缺 |
| 2021-01 | /01 | 7 | 只有 Finder 文本（P66161A） | 缺 | 缺 |
| 2021-06（考试取消，只发布了试卷和 MS） | /01 | 7 | 只有 Finder 文本（P66639A） | 缺 | 本季没有 ER |
| 2021-10 | /01 | 7 | 只有 Finder 文本（P69351A） | 缺 | 缺 |
| 2022-01 | /01 | 7 | 只有 Finder 文本（P71980RA） | 缺 | 缺 |
| 2022-06 | /01 | 7 | 只有 Finder 文本（P72458A） | 缺 | 缺 |
| 2023-01 | /01 | 6 | examsolutions S3 镜像（Pearson 原文件名，题目按更正后的 H→G 版） | 有 | 有 |
| 2023-06 | /01 | 8 | S3 镜像；Drive 有同尺寸副本 | 有 | 有 |
| 2024-01 | /01 | 7 | S3 镜像；Drive 有 QP、答题册 | 有 | 有 |
| 2024-06 | /01 | 7 | Drive | 有 | 缺 |
| 2025-01 | /01 | 8 | Drive | 有（只有 **Final** 版） | 缺 |
| 2025-06 | /01 | 8 | Drive | 有 | 缺 |

D1 只在 1 月、6 月开考（2020-10、2021-10 是例外），没有 2022-10 及以后的 10 月卷。WDM11/01A 区域卷到 2025-06 为止只有 Exemplar（与 2025-06 /01 逐题相同，不单列，见 `WDM11.coverage.part2.md` §4）。

**格式校验**（构建时的合并校验脚本，改动后 0 个问题，`validate.txt`）
- 每条记录字段齐全；各小问分值之和等于题目总分；每卷 75 分，题号连续；id 与考季、卷号、题号一致；series 都是 YYYY-MM。
- 所有 spec id 都在 `spec-items.stat.json` → `WDM11` 中。合并时有 3 个小问的 spec 是空列表（part 1 把只考 Glossary 术语的小问留空），已按 part 2 的做法补上（见下"改正" F1–F3）。
- 引号内文字都不超过 25 词。有 MS 的 6 份卷全部 156 个小问都有 MS 要点；`er` 恰好在有 ER 的 3 季（J23、S23、J24，21 题、77 个小问）填写。2019-06 至 2022-06 的 8 份卷没有 MS，`ms`、`er` 为空，`final_form` 只写题目要求的形式，没有自行计算答案。

**自动比对**
- **小问分值**（`markseq.py`）：100 题的小问分值顺序和题目总分，全部与印刷的 "(n)" 和 "(Total …)" 一致。part 1 用 Finder 文本（2022-01 的 Finder 文件前 19 页是答题册，已跳过），part 2 用 QP 文本。有 7 题印刷序列前面多出的数字是活动网络里括号中的工期（如 "A(8)"）或 INT(8)，已核对。
- **命令词**（`cmdcheck.py`）：351 个带标号的小问，69 处与"标号后第一个词"不同，逐条看过都不是错误，原因是题干以 "Starting at A, use …"、"Using …, apply …"、"Hence determine …" 之类开头。S25 Q3 的小问标号按试卷印刷为 (i)(a)、(i)(b)、(ii)。
- **spec 映射**（`speckw.py`）：按 Dijkstra、Prim/Kruskal、nearest neighbour、route inspection、dummy、float/cascade/schedule、formulate、objective line 等关键词检查，只剩 3 处，都是合理的判断：S22 Q3(f)（比较上界，记 3.3）、J23 Q4(a)（由网络补先序表，记 4.2）、S24 Q6(b)（读给定的 cascade chart 定关键活动，记 4.3）。
- **MS/ER 页码**（`pagecheck.py`）：268 处 MS 页码、86 处 ER 页码。21 处被脚本标记，都是 2025-06 MS 的版式（题号单独一行、注释页只写 "Notes"）或 J23 Q5(a) 引了 ER 引言页 p.3（引言确实点名 Question 5 (a)(b) 的术语问题）。逐页看过，所引页都是该题的评分行或注释。

**完整性**（`completeness.txt`）
- **预期考季**：据 `versions.json` 和 `src/expected_series.json`，到 2026-06 共 16 季：2019-06、2020-01、2020-10、2021-01、2021-06、2021-10、2022-01、2022-06、2023-01 至 2026-06 每年 1、6 月。
- **收录情况**：有 QP 文本的 14 季 14 份卷全部收录，没有漏卷。`inventory/stat.json` 的 WDM11 条目、`finder/finder-inventory.tsv` 的 13 份 2018 考纲卷（2019-06 至 2025-01）、`src/WDM11/` 和 `src/WDM11/alt/` 的全部 QP 文本都在索引内。
- **不收**：Finder 中标为 WDM01 的旧 D1 卷（2013 考纲，内容不同，见 §4）；Exemplar 区域卷与 2025-06 /01 相同。
- **所有来源都拿不到的卷**：
  - 2026-01 WDM11/01、WDM11/01A；2026-06 WDM11/01、WDM11/01A（QP、MS、ER 全缺）。英国文化协会中国区这两季都有 WDM11A 报名，所以 /01A 卷应当存在。
  - 2025-06 是否有 /01A 卷不明。（critic 2026-10-06：grademax 的 Pearson 链接索引 `finder/gh/grademax_maths_index.json` 里 2025 年 6 月只有 WMA11–WMA14、WFM02、WME02 有 /01A，本单元没有，所以这份卷很可能没有出过；属中等可信的指针，不是缺口。）
- **缺 MS**：2019-06 至 2022-06 共 8 份（Pearson 文件名见 `inventory/stat-gaps.md`）。2025-01 只有 Final 版。
- **缺 ER**：2019-06 至 2022-06（2021-06 本来没有 ER），以及 2024-06、2025-01、2025-06。
- **本次补查**（2026-10-06）：
  - Drive：标题含 WDM11/Decision/D1、全文含 WDM11 或 Decision Mathematics，限 2026-01-15 以后修改的文件，只找到已收录的文件。另有一个未登记的 `01 Maths.zip`（id 1Ku2k-NFUx1mfmn2U1csv-DtLLd82Nvj4），下载核对是 UKMT 初级、高级数学挑战赛 2019–2023 的题目和解答，与 D1 无关，已删除本地副本。
  - WebSearch 找到 PMT 的 D1 MS（如 `Edexcel-IAL/Decision/D1/MS/January 2021 MS.pdf`、`October 2021 MS.pdf`、`January 2020 MS.pdf`）和 Maths Genie 的 2022-01 页面，但 curl（CONNECT 被拒）和 WebFetch（EGRESS_BLOCKED）都打不开。
  - 其余来源（papernexus 的 d1 目录只有 2024-06、29 个仓库树、S3 镜像）part 1、part 2 已查过，没有重复。

**准确性抽查**
- **抽查范围**：对照原文逐条复核 33 题，覆盖全部 14 份卷和全部 15 个条目。
  - part 1（只有 Finder 文本，没有 MS）抽 9 题，每份卷至少 1 题：S19 Q4、J20 Q7、O20 Q3、J21 Q4、S21 Q3、O21 Q6、J22 Q4、S22 Q6、S22 Q7。核对题意、分值、spec、终点形式和丢失的不等号说明。9 题没有发现错误。
  - part 2 抽 24 题：J23 Q1、Q6；S23 Q3、Q7、Q8；J24 Q2、Q3、Q6、Q7；S24 Q1、Q3、Q6；J25 Q4、Q5、Q7、Q8；S25 全部 8 题（S25 Q7(e) 查出一处表述不准，于是把 S25 剩下的 Q2、Q4、Q6 也逐题核对）。每题对照 QP 文本、所引 MS 页和 ER 页；从 MS 渲染图读取的值（S24 Q6(d) 2 ≤ x ≤ 6、S24 Q7(b)、J25 Q8 图 4）重新看图核对。
  - 另外不看 MS 独立重算了 part 2 中能算的终点值：J23 Q1 两条 NN 路线 345、342 与下界 327；S23 Q7 的 Prim 顺序、MST 201、NN 248、x = 34 与区间 [235, 246]；J24 Q2 的 Prim 顺序、MST 205、NN 289、x = 31；J24 Q6 的 72 ≤ n ≤ 74 与 n = 72；J24 Q7 的约束化简、三个顶点和 £12 560；S23 Q8 的约束化简与 24；J25 Q4(b) 的关键活动；J25 Q5、S25 Q5 的百分比约束；S25 Q3 的快速排序首轴、二分查找轴序列和 15 < x < 19；S25 Q8 的顶点、a = 11、b = 13 与 1/2 < k < 2/3；J24 Q5 的 k = 240；S23 Q4 的顶点与 k ≥ 2/3；以及 J23 Q3、S23 Q2、S24 Q1、J25 Q1、S25 Q1 的全部装箱和冒泡结果、J25 Q3 的 LCM 13 860；S25 Q2 的 Prim 顺序、MST 540、NN 路线 PRSTUVQP 880 与下界 720（`algo_check.txt`）。
- **结果**：抽查的 33 题里，分值、spec、命令词、MS 要点和 ER 要点都与原文一致；终点形式有 1 处表述不准（S25 Q7(e)，见 F11）。问题没有集中在某一块：S25 全卷 8 题已全部核对，没有发现第二处。全索引的分值、命令词、spec 关键词和页码已用上面的脚本扫过。
- **发现一处评分方案本身的问题**：J25 Q8(c) 要求最小整数解。MS（Final 版）给 (3, 11)，并接受 39 作为证据。但 (4, 10) 满足全部四个约束（落在 x + 2y = 24 上，题目说边界属于可行域），P = 2x + 3y = 38 < 39；对可行域内整数点穷举，最小值正是 (4, 10)（`algo_check.txt`）。索引保留 MS 的答案，并在 `final_form`、`ms` 中加了审核标记。手头只有 Final 版，没有核对 Pearson 发布的 Results 版是否已更正。

**改正**（合并文件和对应 part 文件同步修改，清单见 `work/wdm11audit/fixes.json`）
1. **不一致（3 个小问，改 6 个字段）**：F1–F3。part 1 把只考 Glossary 术语的 3 个小问的 spec 留空，part 2 把同类术语映射到最接近的条目。统一按 part 2 的做法：O21 Q1(a)（解释 path）、J22 Q2(a)（写出一条 path）→ `2.1`；J22 Q2(b)（判断是否 tour）→ `3.2`。`ask` 里的 "no spec item id" 同步改写。
2. **不一致（5 个小问）**：F4–F8。part 2 在 LP 答案是物品件数时把 `5.3` 记为次要条目，part 1 只在 S21 Q7(d) 这样做。补上：S19 Q5(f)、(g)（衬衫件数）、J20 Q7(e)（培训天数）、O20 Q8(b)（甜甜圈个数）、J22 Q7(e)（容器个数）。
3. **评分方案问题标记（1 个小问，2 个字段）**：F9–F10，即上面的 J25 Q8(c)。
4. **表述不准（1 个小问）**：F11 S25 Q7(e)。原写“在 13 < t < 14 时 D、C、E、F、G 必须同时进行，或在 16 < t < 17 时 D、E、F、G、H 必须同时进行”。MS p.18 的论证是：D、C、F、G 必在第一个区间进行，D、F、G、H 必在第二个区间进行，而 E 有浮动时间，只需在两个区间之一进行，所以共需 5 人；满分要写出两个区间（MS p.19）。已按此改写。

---

## 7. 真题需求概览

**数据范围**
- 本节统计第 6 节收录的 14 份卷：S19、J20、O20、J21、S21、O21、J22、S22、J23、S23、J24、S24、J25、S25。共 100 题、356 个小问、1050 分。
- 有 MS 的只有 J23 起的 6 份卷（44 题、156 个小问）；有 ER 的只有 J23、S23、J24 三份。S19 至 S22 的 8 份卷只有 Finder 题目文本，所以下文的"评分惯例"全部来自 2023–2025 的 MS 和 ER。
- 拿不到的卷见第 6 节"完整性"。

**统计方法**
- 数字由 `work/wdm11audit/scripts/stats.py` 从索引算出，结果存于 `stats.txt`；按主条目列出的全部小问在 `byitem.txt`。题型计数是对 `byitem.txt` 逐条人工归类得出的。
- 一个小问按它的第一个 spec（主条目）计分；"出现卷数"按任意位置的 spec 计。

**引用写法**
- J = January，S = June，O = October，后接两位年份。O20 用的是原定 2020 年 6 月的试卷；S21 的考试取消，但试卷和 MS 已发布。
- 题号和小问按试卷印刷。MS、ER 页码是本地 PDF 的页码（`src/WDM11/<series>_01_ms.pdf`、`_er.pdf`），也写在索引条目 `ms`、`er` 字段末尾。

### 7.1 卷面结构

**题量与分值**
- 每卷 75 分、90 分钟，在单独的答题册上作答（网络图、事件时间框、甘特图网格、LP 坐标纸都预印在答题册里）。
- 6 题的 2 份（S19、J23），7 题的 8 份（J20、J21、S21、O21、J22、S22、J24、S24），8 题的 4 份（O20、S23、J25、S25）。
- 单题 4–18 分，最常见 10 分（15 题），其次 7 分、13 分（各 12 题）、9 分（10 题）。每题 1–8 个小问，3 个最常见（28 题）。
- 小问分值：2 分最多（109 个），其次 3 分（76）、4 分（61）、1 分（57）。5 分以上的小问几乎都是画活动网络（5 分）、Dijkstra（6–7 分）、带配对表的 route inspection（4–6 分）、LP 建模（5–8 分）。

**每卷必考的题型**（14 份卷都有）
- 排序或装箱（1.2）；最小生成树（2.1，Prim 或 Kruskal）；Dijkstra（2.2）；route inspection（3.1）；旅行商问题的 nearest neighbour 上界（3.4）和删点下界（3.3）；关键路径（4.3）；线性规划（5.1 建模、5.2 图解，至少各占一部分）。
- 活动网络作图（4.1）11 份有（O21、J23、S25 没有）；浮动时间、甘特图、排程或工人数（4.4）13 份有（只有 S19 没有）。

**各主题分值**（按主条目计）

| 主题 | 分值 | 占比 |
|---|---|---|
| 1 Algorithms（1.1–1.2） | 176 | 16.8% |
| 2 Algorithms on graphs（2.1–2.2） | 180 | 17.1% |
| 3 Algorithms on graphs II（3.1–3.4） | 209 | 19.9% |
| 4 Critical path analysis（4.1–4.4） | 239 | 22.8% |
| 5 Linear programming（5.1–5.3） | 246 | 23.4% |

**命令词**（356 个小问，按每个小问的第一个动词计）

| 命令词 | 次数 | 主要用在 |
|---|---|---|
| Use | 79 | 指定算法（Dijkstra、Prim、Kruskal、NN、FF/FFD、quick sort、binary search、objective line） |
| Determine | 52 | 反推未知量（x、k、n、工期）、区间、起终点、工人数 |
| State | 43 | 关键活动、MST 权重、更好的上界、区间、经过次数 |
| Find | 29 | 删点下界、配对表与重复边、顶点坐标 |
| Calculate | 28 | 工人数下界、浮动时间、延误上限、费用 |
| Draw | 23 | 活动网络、甘特图、MST、约束直线 |
| Complete | 19 | 事件时间框、先序表、追踪表、局部网络 |
| Write down | 16 | 区间、路线、目标函数 |
| Explain | 13 | 术语（path、dummy）、约束的含义、为什么某式取极值 |
| Formulate | 10 | LP 建模 |
| Apply、Carry out、Perform | 7、4、3 | FF/FFD 装箱、冒泡或快速排序 |
| Represent、Schedule、Show、Obtain、Show that | 5、4、4、3、3 | 画约束、排程图、展示 NN 两条路线或二分查找、求界、给定结果 |
| 其他（Add、Interpret、Rewrite、Define、Express、Describe、Construct、Eliminate、Form） | 各 1–2 | |

### 7.2 每个考纲条目怎么考

| 条目 | 主条目小问 | 分值 | 出现卷数（任意位置） | 常见命令词 | 典型分值 |
|---|---|---|---|---|---|
| 1.1 算法（流程图或文字） | 6 | 17 | 4 | Complete、Explain | 追踪表 4 分 + 解释 1–2 分 |
| 1.2 装箱、冒泡、快速排序、二分查找 | 54 | 159 | 14 | Use、Apply、Determine、Calculate | 2–4 分 |
| 2.1 最小生成树（Prim、Kruskal） | 37 | 83 | 14 | Use、Draw、State | 算法 2–3 分，画树或权重 1 分 |
| 2.2 Dijkstra | 20 | 97 | 14 | Use | 主问 6 分（12 次）或 7 分（2 次），追加问 2 分 |
| 3.1 Route inspection | 35 | 107 | 14 | Determine、Find、State | 配对表 4–6 分，追加问 1–3 分 |
| 3.2 实用与经典 TSP | 6 | 9 | 7 | Explain、Interpret | 1–2 分 |
| 3.3 TSP 上下界 | 31 | 59 | 14 | Find、State、Write down | 下界 2–3 分，区间与比较 1–2 分 |
| 3.4 Nearest neighbour | 14 | 34 | 14 | Use | 2–3 分 |
| 4.1 活动网络作图 | 13 | 56 | 11 | Draw | 5 分（10 次） |
| 4.2 由网络补先序表 | 3 | 7 | 3 | Complete | 2–3 分 |
| 4.3 关键路径、事件时间 | 34 | 86 | 14 | State、Complete | 事件时间 4 分，关键活动 1–2 分 |
| 4.4 浮动、甘特图、排程 | 34 | 90 | 13 | Calculate、Draw、Determine、Schedule | 甘特图或排程 3–4 分，工人数 1–2 分 |
| 5.1 LP 建模 | 31 | 113 | 14 | Formulate、Write down、Show that | 完整建模 5–8 分，单条约束 1–3 分 |
| 5.2 图解（直尺法、顶点法） | 36 | 130 | 14 | Determine、Use、Represent | 画约束 4 分，求最优 2–5 分 |
| 5.3 整数解 | 2 | 3 | 11 | Write down、State | 1–2 分；多数作为次要条目出现 |

**1.1 算法的一般概念**
- 只考过 3 次未见过的算法：S21 Q3（求方程正根的迭代流程图，结果给 5 位小数）、S23 Q3（用 INT 逐位取余的文字算法）、J25 Q3（用 INT 的流程图，输出最小公倍数）。另有 O20 Q2(a) 要求用文字描述冒泡排序的一轮和停止条件。
- 形式固定：先填追踪表（4 分），再说明输出与输入的关系（1–2 分），答案要具体："the digits of N in reverse order"、"lowest common multiple"（S23 Q3(b)、J25 Q3(b)）。

**1.2 装箱、排序、查找**（14 份卷都有，每卷 6–17 分）
- 按卷计：快速排序 11 份，FFD 12 份，FF 11 份（O21、J24 是给出 FF 结果反推），冒泡排序 8 份（J20、O20、J21、S21、S22、J23、S23、S25），装箱下界计算 6 份（S19、S21、O21、J22、S22、S25），二分查找 4 份（J21、J22、S24、S25）。
- 典型组合：下界 → FF → 排序 → FFD，或"排序 → 二分查找"。
- 常见变式：
  - 已知装箱结果，反推箱子容量 n 的范围或值（O21 Q7、J24 Q6）；
  - 给出排序中途的列表，反推未知数的范围（J20 Q4(d)、S25 Q3(ii)）、已进行的最多轮数（O20 Q2(b)），或判断哪个数是第一轮的轴（S23 Q2(a)）；
  - 冒泡一轮的比较次数和交换次数（J21 Q3(b)、J23 Q3(b)）；
  - 解释 FFD 结果为什么最优（S24 Q1(d)：下界 3.01 → 4 箱）。
- 终点形式：每箱内容；每一轮后的列表（快速排序要标出轴）；二分查找要写出每次的轴、丢弃的部分和结论（找到或不在表中）。

**2.1 最小生成树**（14 份卷都有）
- Prim 12 次，其中 7 次在距离表（矩阵）上做（O21、S22、S23、J24、S24、J25、S25）；Kruskal 5 次，全在 2019–2022（S19、J20、O20、J22、S22），**2023 年以后没有考过 Kruskal**。
- 常与旅行商问题连用：Prim 求 MST → 上界 = 2 × MST（O21、S22、S23、J25、S25）→ 删点求下界。
- 其他问法：由距离表画网络（O20 Q1(a)，唯一一次考"矩阵表示"的逆向）；MST 唯一时求某边权重的区间（J23 Q5(e)：21 < x < 25）；由 Prim 选边顺序推出关于 x、y 的不等式（S21 Q7）；Dijkstra 路线恰好经过所有顶点时它就是 MST（S24 Q3(b)）。
- 图论术语也记在这里：path（O21 Q1(a)、J22 Q2(a)、J23 Q5(b)）、tree 和 MST 的定义（J20 Q2(a)）、度数和为偶数（J23 Q5(a)）。

**2.2 Dijkstra**（14 份卷都有，每卷 6–10 分）
- 主问几乎总是"求 A 到 J（或 H）的最短路径并写出长度"，6 分，在答题册的预印框里写顺序号、最终值和工作值。
- 追加问（2 分）：经过某点的路线（J21 Q5(b)、S21 Q5(c)、O21 Q1(c)、J23 Q2(b)）；关闭道路后多出多少时间（S25 Q4(b)）；从哪个点开始跑一次就能同时得到两条最短路（S21 Q5(a)）。
- 带未知数的变式：边长含 x（O20 Q7、S22 Q6）。用 Dijkstra 补全最短距离表，为旅行商问题服务（J22 Q6(a)）。

**3.1 Route inspection**（14 份卷都有，每卷 4–10 分）
- 起终点相同（S19、O20、O21、J22(a)、S22、J23、J25）和起终点不同（J20、J21、S21、J22(b)、S23、J24、S24、S25）两种都常考。起终点不同时，要先改奇点集合（去掉或加入起终点）再配对。
- 追加问：
  - 允许在任意点结束或任选起终点，问在哪里结束、新长度或差值（S19 Q3(g)、J21 Q5(e)–(f)、O21 Q5(c)、J23 Q2(d)、J24 Q3(c)、J25 Q2(c)）；
  - 某顶点在路线中出现几次（J20 Q6(c)、J21 Q5(d)、O21 Q5(b)、S23 Q6(c)）；
  - 给出路线总长反推边长 x 或其范围（O20 Q7(b)、S22 Q6(b)、(d)）；
  - 新增一条路后的变化（S22 Q6(d)、S25 Q6(b)）；两种方案比较（J20 Q6(d)、J22 Q5(c)、S23 Q6(d)–(e)）。
- 终点形式：三种配对各写总和 → 最小者 → 重复的边逐条写出 → 总长 = 网络总权 + 最小配对和。

**3.2 实用与经典旅行商问题**（7 份卷出现，共 9 分）
- 解释两者区别 2 次（J21 Q4(a)、J25 Q6(a)）；把表上的路线"按实际经过的城镇"写出 2 次（S21 Q4(c)、S22 Q3(h)）；用 shortcut 改进上界 1 次（O20 Q3(a)）；判断某 walk 是否为 tour 1 次（J22 Q2(b)）。

**3.3 上界与下界**（14 份卷都有）
- 删点下界每卷都考（2–3 分）：残余 MST 的权 + 被删点的两条最短边。
- 上界：2 × MST（5 次）、比较两个 NN 上界选更好的（J21 Q4(c)、S22 Q3(f)、S23 Q7(d)、J24 Q2(d)、J25 Q6(e)），比较两个下界（J21 Q4(e)）。
- "能确信包含最优值的最小区间" 8 次（S19、J21、O21、J22、J23、S23、J25，另 J23 Q5(e) 是 MST 题里的区间）。
- 带未知数：已知下界反求 x（S23 Q7(e)、J24 Q2(e)），或用 x 的给定范围比较上界（S23 Q7(d)）。
- 补全最短距离表（把网络变成完全网络）2 次：S21 Q4(a)、J22 Q6(a)。

**3.4 Nearest neighbour**（14 份卷都有，2–4 分）
- 几乎都是"从某点出发用 NN 求上界，写出路线和长度"。两次要求"说明有两条 NN 路线"（O21 Q3(d)、J23 Q1(a)，在某步出现等距）。终点是回到起点的闭合路线加总长。

**4.1 活动网络作图**（11 份卷，几乎都是 5 分）
- 由先序表画 activity on arc 网络，要求"最少虚活动"或"恰好 n 个虚活动"（S19、J22 要求恰好 4 个）。有 MS 的 4 次中，S23、J24、S24 是 4 个虚活动，J25 是 5 个；S24 Q6、J25 Q4 都需要一个区分同起止活动的 uniqueness dummy。
- 解释某个虚活动的作用 2 次（S19 Q4(a)、J25 Q7(a)）；补全局部网络 1 次（J21 Q6(a)）。

**4.2 由网络补先序表**：只考过 3 次（O21 Q4(a)、J23 Q4(a)、S25 Q7(a)），2–3 分，按行分组给分。

**4.3 关键路径**（14 份卷都有）
- 补全事件时间框 11 次（9 次是 4 分；S22 Q2(b) 3 分，S24 Q2(a) 连同完成时间 5 分），随后写关键活动或关键路径（1–2 分）。
- 推理题：已知某活动关键或关键路径唯一，问哪些必须、可能或不可能关键（S19 Q6(b)、J20 Q5(b)、O20 Q4(b)、S21 Q6(b)、J24 Q4(b)、J25 Q4(b)）；所有活动等长时的关键路径（S19 Q6(c)、O20 Q4(c)、S21 Q6(c)）；某活动缩短或延长后的影响（S19 Q4(d)–(e)、O20 Q5(d)、O21 Q4(e)）。
- 带未知工期：由浮动关系或路径长度反求工期（J20 Q3(a)、J22 Q4(a)、S22 Q2(a)、O21 Q4(b)、S23 Q5(b)）。
- 考纲写的"活动的最早、最晚开始与结束时间"从没有单独作为问题出现，题目都用事件时间和浮动时间问。

**4.4 浮动、甘特图、排程**（13 份卷）
- 工人数下界 = 总工期 ÷ 项目时长、向上取整：计算型 8 次（O20、J21、O21、J23、S23、J24、S24、S25）。
- 画甘特（cascade）图 7 次（J20、S21、J22、S22、J24、J25、S25），之后都接"用图说明至少要几名工人，写出时刻和活动"（2–3 分）。
- 画排程图 6 次（O20、J21、O21、J23、S23、S24），要求用最少工人在最短时间完成；下界不一定够用（S23：下界 3，排程要 4 人）。
- 浮动时间或最大可延误天数 1–2 分（J23 Q4(d)、S23 Q1(b)、J24 Q1(b)、J25 Q7(d)），已知浮动上限反求工期范围（S24 Q6(d)）。读给定排程图写完成时间、关键活动和浮动（S22 Q5(b)）。

**5.1 LP 建模**（14 份卷都有）
- 主流题型：三个变量的文字情境，条件含"至少/至多百分之几"、"每 a 个 X 至少 b 个 Y"、时间或材料"可做 p 个 X 或 q 个 Y"、预算；要求写目标（必须写 maximise/minimise）和化简成整数系数的不等式（5–8 分）。只有 J21 Q2、O21 Q2 是两个变量。
- 随后给出一个等式条件（"恰好 n 件"、"比例 5 : 2"、"20% 是某类"）消去 z，变成两变量问题（S19、J20、O20、J22、J23、S23、J24、S24、S25）。常带"解释为什么最大化 P 等价于最小化某式"（J22 Q7(b)、J24 Q7(b)）或 "Show that" 某条约束（J25 Q5(b)、S25 Q5(b)、(d)）。
- 反向题：从图上的可行域写出全部不等式（O20 Q6(a)、J21 Q7(a)、S22 Q7(a)、S23 Q4(a)、S24 Q7(a)、J25 Q8(a)、S25 Q8(a)），常要先由两个顶点求第三条直线方程。

**5.2 图解**（14 份卷都有）
- 画约束并标出可行域 R（4 分）7 次。
- 求最优：目标线法 6 次（S19、J20、O21、J22、J23，J24 Q5 读给定的目标线）；point testing/vertex method 2 次（S23 Q4(c)、J24 Q7(d)）。两种方法不能混用（见 7.4）。
- 求精确顶点坐标（S23 Q4(b)、J24 Q7(d)、S25 Q8(b)），答案常是分数。
- 参数题很多：目标函数含 k 或 a，求使最优顶点不变（或指定最大、最小顶点）的范围（O20 Q6(b)、O21 Q6(c)、S23 Q4(d)、S25 Q8(c)），或使最小值至少为最大值一半的范围（S24 Q7(b)），由已知最大最小值反求目标函数或系数（J21 Q7(b)、J24 Q5、J25 Q8(b)、S25 Q8(b)），新约束不改变可行域的最大 k（S22 Q7(b)）。
- 终点要写回情境：几件 X、几件 Y、（被消去的）几件 Z、费用或利润。

**5.3 整数解**
- 明确考整数的只有 2 次：S21 Q7(d)（由图写出所有整数点）、J25 Q8(c)（最小整数解）。另有 9 个小问的答案是物品件数，索引把 5.3 记为次要条目（S19 Q5(f)–(g)、J20 Q7(e)、O20 Q8(b)、J22 Q7(e)、J23 Q6(d)、S23 Q8(b)、J24 Q7(d)、S24 Q5(b)、S25 Q5(e)）。
- **注意 J25 Q8(c)**：MS（Final 版）给 (3, 11)，但 (4, 10) 也在可行域内且目标值更小（38 < 39），见第 6 节。

### 7.3 考纲写了、真题还没考过（或极少考）的点

- **没有一个条目完全没考过**：15 个条目都至少做过一次主条目。
- **从未出现**：
  - 3.2 的三角不等式（triangle inequality）；
  - 写出网络的矩阵表示（只考过反方向：O20 Q1(a) 由距离表画网络）；
  - 4.3 的"活动最早、最晚开始与结束时间"作为单独问题；
  - Glossary 中的 subgraph、connected、digraph、walk 的定义题。
- **极少出现**：
  - Kruskal：2019–2022 共 5 次，2023–2025 一次也没有（全用 Prim）；
  - 1.1 未见过的算法：3 次（S21、S23、J25）；
  - 3.2 实用与经典 TSP：J21、J25 各一次解释，O20 一次 shortcut；
  - 4.2 补先序表：3 次；
  - 5.3 明确的整数解：2 次；
  - 二分查找：4 次。
- **考纲排除、不必准备**：算法的阶（order of an algorithm）、对奇点用 Floyd 算法、矩阵运算、simplex（D1 无此内容）。

### 7.4 反复出现的评分惯例与考官提醒

以下 MS 页码都指 2023–2025 的 6 份 MS，ER 只有 J23、S23、J24。2019–2022 没有 MS，不能核对那几年的评分细则。

**全卷通用**
1. **没有过程基本没分。** D1 是"a methods-based examination"，只写答案"rarely gains any credit"（ER J23 p.3、S23 p.3）。工人数或箱数下界只写结果不给分：S25 Q1(a)、Q7(c)（MS pp.5、19）、S24 Q2(b)（MS p.9）、J24 Q1(c)（MS p.7）、S23 Q1(c)（MS p.7）、J23 Q4(e)（MS p.13）。浮动时间要写出所用的三个数（J23 Q4(d)、S23 Q1(b)、J24 Q1(b)）。
2. **按题目要求的方法和顺序做。** 按相反顺序排序：快速排序按误读处理，最多 2/4（J24 Q6(b)，MS p.15；S24 Q1(b)；J25 Q1(b)）；冒泡排序方向反了 3 分丢 2 分（ER S23 p.4）。题目要求排程却画甘特图、或反过来，该部分不得分（ER S23 p.3；J24 Q1(d)，MS p.7）。要求点测试却用目标线法 M0（J24 Q7(d)，MS p.17）；要求目标线法却不画线，没有分（ER J23 p.6）。
3. **问"with a reason"就要写理由。** 只写数值不得分：S24 Q3(b) 只写 74 是 M0（MS p.10）；J24 Q2(d) 要说明 289 < 291（ER J24 p.4）。
4. **术语要准确。** 把 cycle 写成 "circle" 扣分（J23 Q5(b)，MS p.15、ER p.5）；解释 path 时要指出重复的顶点（J23 Q5(b)）；path 不必经过所有顶点（ER J23 p.5）。
5. **卷面**：不用彩色笔和荧光笔，图用深色铅笔（ER J23 p.3、S23 p.3）；最后一题常来不及做（ER J24 p.3、S23 p.7）。

**排序、装箱、查找**
6. 快速排序的轴取中间项（按 Glossary 的 middle item），取首项或末项是 M0；每轮只取一个轴只得 M1；满分要写出最后一轮（"fifth pass"）（S24 Q1(b)、J25 Q1(b)、S25 Q3(i)(a)，MS pp.5–6、6–7、10–11；ER J23 p.4）。
7. 冒泡排序要写出最后一轮没有交换的那一轮，"stop"、"sort complete"不够（S23 Q2(b)，MS p.8、ER p.4）。比较次数与交换次数要标明（J23 Q3(b)：不标明时按先比较、后交换读；只写 "6 then 10" 给 SC B1 B0，MS p.11）。
8. 二分查找要丢掉轴本身，保留轴只得 M1（S25 Q3(i)(b)，MS pp.9–10；S24 Q1(e)，MS pp.5–7）；最后要写结论"不在表中"。
9. FFD 写成按递增顺序的 first-fit 不得分（J23 Q3(d)、S24 Q1(c)、J25 Q1(c)）；FF 的方法分要求前若干项放对，写累计和只在 M 分上宽容（J25 Q1(a)、S25 Q1(b)）。反推箱子容量要写出"哪个数放不进哪个箱"的理由（J24 Q6，MS p.14；ER J24 p.5）。

**图算法**
10. **Prim**：要按选取顺序列出边，只写顶点顺序或矩阵上方的编号拿不到最后一分；出现明确的"拒绝"只给 M1；从别的点开始最多 M1（S23 Q7(a)，MS p.15；J24 Q2(a)，MS p.8；S25 Q2(a)，MS p.7）。权重有重复时只写权重不算（J23 Q5(c)）。不要在最后加一条"回到 A"的边，也不要按 NN 的顺序选边（ER S23 p.6）。
11. **Dijkstra**：工作值要按标号顺序写（如"at D the working values must be 39 37 35"，J24 Q3(a)，MS p.10）；标号必须严格递增，重复标号扣一次；路线要从起点写到终点，"J to A"不行（J23 Q2(a)、S23 Q6(a)）。不要划掉正确的工作值；常见遗漏是最后几个点的工作值（ER J23 pp.3–4、S23 p.6）。
12. **Route inspection**：三种配对各写全并算出总和，"明显更大"的也要写（ER J23 p.4）；重复的边逐条写成边，"BF"、"B(CD)F"、"AE via B and C"都不行（J24 Q3(b)，MS p.10；J23 Q2(c)，MS p.9）。起终点不同时奇点集合要改；用错集合按误读处理（J24 Q3(b) 最多 3/5；S24 Q4(d) 最多 2/4；S25 Q6(a) 最多 M1 A1）。选终点时要明确说出"不含起点的奇点之间最短的是哪一对"（J23 Q2(d)、J25 Q2(c)；ER J24 p.4）。

**旅行商问题**
13. NN 路线必须回到起点并写成路线；只给长度、漏掉最后一步都会丢分（ER J23 p.3、S23 pp.6–7、J24 p.4）。不要把 NN 长度乘 2（S25 Q2(c)，MS p.7；ER S23 p.7）。2 × MST 之后再做别的计算不按 isw 处理（S25 Q2(b)）。
14. 删点下界：先写残余 MST 的权，再加被删点的两条最短边；从 NN 回路中去掉该点是错的，最多 1/3（ER J23 p.3）。有未知数时要说明为什么最短的两条是这两条（J24 Q2(e)，MS p.8；ER J24 p.4）。
15. 区间要写成不等式，"327 – 342"是 B0；下界可以用严格不等号（J23 Q1(c)，MS p.6）。上界一侧错用严格不等号会丢最后一分（ER S23 p.7）。比较上界时要用题目给的 x 的范围（S23 Q7(d)，MS p.15；ER S23 p.7）。

**关键路径**
16. 活动网络必须 activity on arc，activity on node 是 M0（J25 Q4(a)，MS p.11；ER S23 p.5、J24 p.4）。每条活动和虚活动都要画箭头，虚活动没有箭头只得 M1；只能有一个终点；多余但正确的虚活动只扣最后一分（S24 Q6(a)，MS p.15）。建议最后重画一份干净的网络（ER J24 p.5）。
17. 事件时间：上框从左到右递增、下框从右到左递减，允许一个 "rogue value" 拿 M 分（各卷 MS）。晚时间小于早时间是不可能的（ER J24 p.3）。关键活动要写全且不能多写（J23 Q4(c)、S24 Q6(b)）。
18. 甘特图要画浮动时间（建议涂阴影，虚线难辨认，ER J24 p.3）；排程图每人一行，活动不能超过项目结束时间（ER S23 p.3）。
19. **工人数论证**：必须给出严格落在区间内的时刻和那一刻同时进行的活动，例如 "At time 9.5, activities G, C, E and I must all be happening"（S24 Q6(c)，MS p.15）。写 "12 – 13"、"between 12 and 13" 或等于端点的时刻是 A0，附加一句错误陈述也是 A0（J24 Q1(e)、J25 Q7(f)、S25 Q7(e)，MS pp.7、16、19）。有两个关键区间时满分要两个都写（S25 Q7(e)）。

**线性规划**
20. 目标要写 "maximise" 或 "minimise"（"max/min" 可以，"maximum/minimum" 不行）（J23 Q6(a)、J25 Q5(a)、S25 Q5(a)；ER J24 p.6、J23 p.6）。目标函数不能随意放大：J25 Q5(a) 用英镑写 1.5x + 2y + 1.8z 或用便士写 150x + 200y + 180z 都可以，但乘以 10 写成 15x + 20y + 18z 是 B0（MS p.12）。
21. 约束化简成整数系数；百分比、比例条件最容易写反（ER S23 pp.7–8、J24 pp.5–6）。"恰好"类条件要保留为等式再消元（S23 Q8，ER pp.7–8）；把不等式当等式解，即使得到正确数字也不给分（S23 Q8(b)，MS p.18）。"Show that" 中把等式改成不等式只得 M1 A0（S25 Q5(b)）。
22. 直线用尺子画，从坐标轴画到坐标轴（误差一小格），可行域要标 R，不能只靠阴影（J23 Q6(c)，MS p.17；ER J23 p.6、J24 p.6）。目标线不能太短（J23 Q6(d)，MS p.17）。
23. point testing 要把每个顶点都代入（ER S23 p.5）。题目要求精确坐标时，42.3 或 42.33 不行，42.3 循环可以（J24 Q7(d)，MS p.17）；S23 Q4(b) 写 6.666… 也不行。
24. 从图写约束时，全部写成严格不等号：S25 Q8(a) 给 SC B1 B0（MS p.22）；J25 Q8(a) 只在第一分上宽容（MS p.18）。
25. 最终答案要回到情境，写出每种物品的数量（包括消去的 z）："x = 60, y = 20 is A0"（S25 Q5(e)，MS p.15；ER J24 p.6）。用 k 的不等式比较梯度时容易弄错负号和方向，代入两个顶点比较目标值更稳妥（ER S23 p.5）。
