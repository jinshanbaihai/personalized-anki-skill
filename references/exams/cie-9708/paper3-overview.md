# 9708 Paper 3（A Level Multiple Choice）：真题需求概览

逐题索引（合并版）：`9708-P3.questions.json`（同一文件夹）。最初由 `9708-P3.questions.part1.json` 与 `part2.json` 合并（15 份卷，2026-10-06 审核），同日又并入补建的 `9708-P3.questions.gap2023.json` 与 `gap2024.json`（8 份卷），去重、排序后共 690 条。最初 15 份卷的来源与建索引时的检查见 `9708-P3.coverage.part1.md`、`9708-P3.coverage.part2.md`；补建的 8 份卷的来源写在各条的 `sources` 里，检查记录见第 7 节。考纲条目与印刷页码见 `syllabus-a-level.md` 与 `spec-items.json`。本文件的统计都由脚本从合并后的索引算出（`work/p3audit/scripts/`：`stats.py`、`render_table.py`、`overview_stats.py`、`build_overview.py`），问法与结论的文字是人工归纳（`desc.py`），引用的 key 都已对过 MS。

## 真题需求概览

### 1. 数据范围与引用写法

- **索引了 23 份卷、690 条（每题一条）**，即 2023-03 至 2025-11 的全部 Paper 3 卷（Feb/March 只有 /32）：M23/32；S23/31、/32、/33；W23/31、/32、/33；M24/32；S24/31、/32、/33；W24/31、/32、/33；M25/32；S25/31、/32、/33、/34；W25/31、/32、/33、/34。
- **同一份题的三对卷**：S23/33 = S23/31、S24/33 = S24/31、S25/33 = S25/31（MS key 相同，题面与页码逐题一致；索引里两卷各有 30 条，`spec`、`ask`、`ms` 相同）。W23、W24、W25 的 /31 与 /33 是不同的题。所以下面按 **20 份不同的卷、600 道不同的题** 统计。
- 每题 1 分。23 份卷都有 MS（只有答案字母）。有 Principal Examiner Report（PER）逐题评论的考季：M23、S23（/31、/32、/33）、W23（/31、/32、/33）、S24（/31、/32、/33）、M25。M24、W24、S25、W25 没有 PER（没有取得，见第 7 节），这些卷的 `er` 为空。
- **没有进索引**：2026 年的 M26/32 与 S26/31–34。它们已经公布（有间接证据），但这里拿不到，见第 7 节。所以本文件的统计止于 W25。
- **引用写法**：M = Feb/March，S = May/June，W = Oct/Nov，后接两位年份、斜杠与卷号，如 `S25/31 Q14` 即 9708/31 May/June 2025 第 14 题，对应索引 id `9708/3-2025-06-31-Q14`。PER 页码是本地 PDF 页（`src/9708-ER/<series>_all_er.pdf`）。
- **条目标签**：索引 `spec` 的第一个 id 是主考点，其余是次要考点。下表“主／全／卷”= 以该条目为主考点的题数／打了该条目标签的题数／涉及的卷数（共 20 份）。

### 2. 卷面结构

- QP 封面（M23/32 与 W25/32 相同）："There are thirty questions on this paper. Answer all questions."，1 小时 15 分钟，可用计算器，"Each correct answer will score one mark."。考纲 p.35：不给公式（乘数、MRP、集中度、Gini 等要自己记）。
- **题序跟着考纲走**：topic 7 集中在 Q1–Q14（中位 Q5；另有 W24/32 Q18 一题），topic 8 在 Q7–Q25（中位 Q12），topic 9 在 Q13–Q26（中位 Q18；另有 M23/32 Q30 一题），topic 10 在 Q15–Q26（中位 Q22），topic 11 在 Q9–Q30（中位 Q27）。
- **每卷各 topic 题数**（按主考点；AS 指主考点落在 AS 条目的题；“= /33”表示同考季 /33 是同一份题，只算一次）：

  | 卷 | T7 | T8 | T9 | T10 | T11 | AS |
  |---|---|---|---|---|---|---|
  | M23/32 | 10 | 6 | 6 | 3 | 5 | 0 |
  | S23/31（= /33） | 11 | 5 | 5 | 3 | 5 | 1 |
  | S23/32 | 13 | 3 | 5 | 4 | 5 | 0 |
  | W23/31 | 10 | 6 | 6 | 3 | 4 | 1 |
  | W23/32 | 9 | 5 | 6 | 3 | 7 | 0 |
  | W23/33 | 10 | 5 | 5 | 3 | 6 | 1 |
  | M24/32 | 10 | 5 | 5 | 5 | 5 | 0 |
  | S24/31（= /33） | 10 | 6 | 4 | 3 | 7 | 0 |
  | S24/32 | 10 | 5 | 6 | 3 | 5 | 1 |
  | W24/31 | 11 | 4 | 6 | 2 | 6 | 1 |
  | W24/32 | 11 | 5 | 3 | 4 | 7 | 0 |
  | W24/33 | 10 | 5 | 4 | 5 | 6 | 0 |
  | M25/32 | 7 | 7 | 6 | 2 | 8 | 0 |
  | S25/31（= /33） | 7 | 7 | 5 | 5 | 5 | 1 |
  | S25/32 | 7 | 7 | 6 | 3 | 6 | 1 |
  | S25/34 | 6 | 5 | 7 | 4 | 7 | 1 |
  | W25/31 | 7 | 5 | 7 | 2 | 8 | 1 |
  | W25/32 | 8 | 3 | 6 | 3 | 9 | 1 |
  | W25/33 | 7 | 5 | 8 | 3 | 7 | 0 |
  | W25/34 | 7 | 7 | 7 | 4 | 5 | 0 |
  | 合计（600） | 181 | 106 | 113 | 67 | 123 | 10 |

  2023–2024 的 12 份卷 topic 7 每卷 9–13 题、topic 11 每卷 4–7 题；2025 年的 8 份卷 topic 7 降到 6–8 题，topic 11 升到 5–9 题。20 份卷合计：topic 7 181 题（30%），topic 8 106，topic 9 113，topic 10 67，topic 11 123，AS 10。
- **题型**（自动分型，按题面文字；一题可属多类）：只用文字的 363 题；带图 114 题（其中“四个图选一个”5 题）；选项是 yes/no、increase/decrease 组合行的 95 题；需要计算的约 45 题；给数据表的 37 题；题干含 not／NOT／least 的 75 题（最后一问里 NOT/not 约 46 题、least 约 18 题）。
- **问法**：Paper 3 没有 Cambridge 的命令词（Define、Explain、Assess…），题干只有几种句式。按 592 道能从 QP 文本取出题干的题的最后一问粗略计数：“What is most likely …”约 84 题，“What is (a) …”／“What is meant by …”定义题约 60 题，“effect／impact／result of …”约 74 题，“Which statement … is correct／NOT correct”约 26 题，“Which combination／row …”约 34 题，“What can be concluded …”约 17 题，“Which area …”约 6 题（可重叠）。所以卡片要练的是：认出定义、在图上定位、判断方向组合、排除“只对一半”的选项，以及注意 NOT／least。

### 3. 逐条目考频与考法（A Level topics 7–11）

“题型”列是打了该条目标签的全部题的自动分型计数；“key 反映的结论”是从 key 反推出的、MS 认可的那条结论（Paper 3 MS 只有字母，原因来自 PER 或我们按题面推出，括号里给出处）。“代表题”优先列有 PER 逐题评论的题，再按考季从新到旧。

#### Topic 7 The price system and the microeconomy（考纲 pp.24–27）

| 条目 | 主／全／卷 | 题型 | 常见问法 | key 反映的结论 | 代表题 |
|---|---|---|---|---|---|
| 7.1.1 definition and calculation of total utility and marginal utility（p.24） | 4／7／7 | 文字 1、图 4、组合行 3、表格数据 1 | 由总效用表或总效用曲线求某一单位的 MU、找 MU = 0 的点；比较两人第 n 单位的 MU；MU 与平均效用的关系 | MU(n) = TU(n) − TU(n−1)；TU 最高点处 MU = 0（W24/31 Q1）；MU 高于平均效用时平均效用上升（S24/31 Q1）；曲线是 TU 不是 MU（W23/32 Q1 的 ER） | W23/32 Q1，S24/32 Q1，W24/31 Q1，S24/31 Q1 |
| 7.1.2 diminishing marginal utility（p.24） | 4／8／8 | 文字 2、组合行 4、图 4、表格数据 1 | MU 为正但递减时 TU 怎么变；MU 降到零以下后 TU 怎么变；沿无差异曲线移动时两种商品的 MU 怎么变 | MU 为正递减：TU 仍上升但增幅变小；MU 为负：TU 下降，峰值在 MU = 0 处（S23/31 Q1，W23/33 Q1）；多消费的那种 MU 下降 | M24/32 Q1，W23/31 Q1，W23/33 Q1，S23/31 Q1 |
| 7.1.3 equi-marginal principle（p.24） | 7／8／8 | 文字 3、组合行 4、计算 3、表格数据 2 | 给 MU 表与价格求效用最大化组合；等边际原则的定义与等价写法（MUY × PZ = MUZ × PY）；偏好或价格变化后多买哪种 | 各商品 MU/P 相等（花在每种商品上的最后一元带来的效用相同）且收入花完；表给的是 MU 还是 TU 要先看清 | M23/32 Q2，W25/31 Q4，S25/31 Q1，W24/32 Q1 |
| 7.1.5 limitations of marginal utility theory and its assumptions of rational behaviour（p.24） | 1／1／1 | 组合行 1 | rational consumer 需要哪些假设（行列 yes/no） | 完全信息、无成瘾行为、选择不受他人影响 | M23/32 Q1 |
| 7.2.1 meaning of an indifference curve and a budget line（p.24） | 12／13／13 | 文字 4、图 8、组合行 4、NOT／least 3、计算 2 | 无差异曲线表示什么、为何凸向原点、哪句不对（会相交）；预算线截距与斜率、与无差异曲线的切点；收入或价格变化后新截距的计算 | 同一曲线上满足程度相同；凸向原点 = MRS 递减（W23/33 Q2）；无差异曲线不相交（W24/33 Q2）；最优点在切点；斜率 = Px/Py；截距 = 收入/价格 | S24/31 Q2，W25/32 Q2，S25/31 Q3，W24/31 Q2 |
| 7.2.2 causes of a shift in the budget line（p.24） | 2／5／5 | 文字 2、组合行 2、计算 1、NOT／least 1、图 1 | 预算线平移或转动的原因；什么不会影响预算线（NOT） | 收入变化 → 平移；一种价格变化 → 绕另一截距转动；偏好不影响预算线 | W23/31 Q2，S25/32 Q1 |
| 7.2.3 income, substitution and price effects for normal, inferior and Giffen goods（p.24） | 2／2／2 | 文字 1、组合行 1、图 1 | 图上把价格效应拆成替代效应与收入效应并判断正负；劣等品需求曲线为何仍向下倾斜 | 收入效应 = 两条平行预算线之间的移动；劣等品：替代效应大于反向的收入效应 | M23/32 Q3，M25/32 Q5 |
| 7.2.4 limitations of the model of indifference curves（p.24） | 2／3／3 | 文字 1、图 2、NOT／least 1、组合行 1 | 无差异曲线分析的哪条假设不对（NOT）；理论中哪个特征最接近现实 | 模型假设收入有限、消费者始终追求满足最大化，“目标可能改变”不是模型假设（S23/31 Q3）；最贴近现实的是收入有限（W24/32 Q2） | W24/32 Q2，S23/31 Q3 |
| 7.3.1 definitions of productive efficiency and allocative efficiency（p.24） | 5／6／6 | 文字 4、组合行 1、计算 1 | 某结构或某企业达到哪几种效率（生产／配置／动态 yes/no 行）；配置效率何时达到；为何追求效率 | 配置：P = MC；生产：最低 AC；无管制独家供应商通常只有动态效率可能 | S23/32 Q9，W25/33 Q1，S25/32 Q2，W24/32 Q18 |
| 7.3.2 conditions for productive efficiency and allocative efficiency（p.24） | 3／12／9 | 文字 4、图 4、计算 4、组合行 3、NOT／least 1 | MC < P 时如何改进；自然垄断图上哪组价格产量有配置效率；什么有助于配置效率 | 增加产量、降低价格到 P = MC；自然垄断在 P = MC 处配置有效但不在最低 AC | W25/32 Q8，S25/31 Q2，M23/32 Q10 |
| 7.3.3 Pareto optimality（p.24） | 4／4／4 | 文字 3、计算 1、组合行 1 | 什么能带来 Pareto 最优；由分配变化判断是否 Pareto 改进；什么证据说明已到 Pareto 最优 | 至少一人变好且没有人变坏（S23/31 Q2 的 PER：误选者没注意到有人变差）；W25/34 Q6 的 key 为 full employment | S23/31 Q2，W25/31 Q5，W25/34 Q6，W23/33 Q10 |
| 7.3.4 definition of dynamic efficiency（p.24） | 5／6／6 | 文字 3、组合行 2、图 1、NOT／least 1 | 什么有助于动态效率；动态效率在图上怎么体现；哪种结构最不可能有动态效率；垄断把超额利润再投资的效果 | 降低留存利润税、投资新技术；AC 曲线随时间下移；完全竞争最不可能 | M25/32 Q7，M24/32 Q7，W23/31 Q8，S23/31 Q4 |
| 7.3.5 definition of market failure（p.24） | 1／1／1 | 文字 | 哪一项是 market failure 的例子 | 社会需要的物品供给不足（M25/32 Q2） | M25/32 Q2 |
| 7.3.6 reasons for market failure（p.24） | 2／5／5 | 文字 5、NOT／least 2 | 缺乏产权为何造成低效；牙医过度治疗属于哪类失灵；汽车尾气的应对 | 资源对使用者零成本而被耗尽（S25/34 Q3）；牙医过度治疗 = 信息不对称 | W23/32 Q3，S25/34 Q3 |
| 7.4.1 definition and calculation of social costs (SC) as the sum of private costs (P…（p.24） | 7／10／7 | 文字 7、图 2、组合行 1、计算 1 | 内部化外部成本后企业的总成本；哪项是外部成本；成本变化如何移动 MPC 与 MEC；读图求 MEC 或净社会收益面积；哪组变化使净社会成本上升 | SC = PC + EC；MEC = MSC 与 MPC 的竖直距离；道路拥堵是外部成本（S23/31 Q9）；净社会收益 = 需求曲线下面积 − MSC 下面积（S23/31 Q10 的 PER） | S23/31 Q10，W25/32 Q3，S24/31 Q6，W23/31 Q10 |
| 7.4.2 definition and calculation of social benefits (SB) as the sum of private benef…（p.24） | 3／6／6 | 文字 3、计算 1、表格数据 1、组合行 1 | SB、PB、EB 的恒等式选哪个；哪项是私人收益；由支付意愿与外部收益表求 MSB | SB = PB + EB；MSB = MPB + MEB；改骑摩托的人自己省下的时间是私人收益（W23/33 Q8） | S23/32 Q6，M24/32 Q3，W23/33 Q8 |
| 7.4.3 definition of positive externality and negative externality（p.24） | 3／5／5 | 文字 4、组合行 1、图 1 | 四曲线图上判断外部性类型与福利最大产量；某项行为（接种疫苗、强制戴头盔）为什么有正外部性 | 福利最大在 MSC = MSB；MSC < MPC 为正生产外部性；正外部性 = 第三方得到的收益（疾病不再传播、医疗压力减轻） | S24/31 Q3，W25/34 Q4，W24/32 Q4 |
| 7.4.4 positive and negative externalities of both consumption and production（p.24） | 4／16／15 | 文字 10、图 5、组合行 3、NOT／least 2、计算 2 | 判别外部性属于生产还是消费、正还是负；图上选纠正方向；demerit／外部收益组合与低消费 | 先判类型再选图；消费的正外部性 → 消费不足 | M23/32 Q7，S25/34 Q2，M25/32 Q6，S23/32 Q8 |
| 7.4.5 deadweight welfare losses arising from positive and negative externalities（p.24） | 3／8／8 | 图 8、组合行 4、计算 1 | 在外部性图上指认 DWL 三角形；纠正后 DWL 变化；需求移动后 DWL 增减；MSC 高于 MPC 时怎样才达到配置效率 | DWL 在市场产量与社会最优产量之间、MSC 与 MSB 之间；负生产外部性 → 减少消费、提高价格（W24/32 Q8） | S24/32 Q7，W25/31 Q6，W24/32 Q8 |
| 7.4.6 asymmetric information and moral hazard（p.24） | 7／7／6 | 文字 6、NOT／least 3、图 1 | moral hazard 的定义、何时发生、哪一项不是（NOT）；信息不对称导致过度治疗；低估 MPC 的后果 | 投保或受保护后承担更大风险；过度消费 = 高估净收益 | W25/32 Q1，S25/31 Q4，W23/32 Q8，S23/32 Q1 |
| 7.4.7 use of costs and benefits in analysing decisions（p.24） | 7／7／7 | 文字 7、NOT／least 1 | CBA 中哪项是外部成本；净社会收益为正为何仍可能不建；为何难以量化；什么条件使 CBA 不准；什么准则决定最优产量 | 外部成本 = 第三方承担；预算约束与机会成本；无形收益难以货币化；外部成本收益占比越高越不准（W23/33 Q9） | W23/31 Q9，S23/32 Q12，W25/32 Q6，S25/34 Q4 |
| 7.5.1 short-run production function（p.25） | 3／5／4 | 表格数据 3、计算 1、组合行 1、图 1 | 由总产量表求 MP、判断边际收益递减从第几个工人开始；生产函数定义填空 | MP = ΔTP／ΔL，MP 开始下降处即边际收益递减（W24/31 Q14：第 3 个工人，10 → 9）；生产函数 = 各投入组合可得的最大产量 | W24/31 Q14，M24/32 Q4，S23/32 Q14 |
| 7.5.2 short-run cost function（p.25） | 9／13／10 | 文字 4、图 5、组合行 3、表格数据 2、NOT／least 1、计算 1 | 短期哪种成本持续下降；MC 低于 AVC 时能得出什么；MC、ATC、AFC 随产量的变化；MC > ATC 的产量；由价格、销量、TFC 与正常利润求 AVC；SRAC／LRAC 图上扩产后单位成本降多少 | AFC 持续下降；MC < AVC → AVC 下降，不论 MC 本身升降（S23/31 Q7 的 PER）；MC 穿过 ATC 最低点；正常利润 → TR = TC | S23/31 Q7，W25/33 Q4，M25/32 Q1，W24/31 Q7 |
| 7.5.3 long-run production function（p.25） | 1／3／3 | 图 2、NOT／least 1、组合行 1、表格数据 1 | LRAC 下降段的原因（另作次要标签：生产函数填空、LRAC 与 SRAC 包络图） | 长期所有投入可变：LRAC 下降 = 规模报酬递增（W24/31 Q4） | W24/31 Q4 |
| 7.5.4 long-run cost function（p.25） | 4／9／7 | 文字 1、图 7、NOT／least 2、组合行 2、选图 1 | LRAC 与多条 SRAC 的包络图上哪句不对（NOT）；S 形 LRTC 上 LRATC 最低点在哪；一路下降与一路上升的 LRAC 各表示什么；技术改进后 ATC、供给与 PPC 的变化 | 原点射线与 LRTC 的切点；收益递减属于短期成本曲线；技术改进：ATC 下移、供给右移、PPC 外移（W23/33 Q5） | W23/31 Q4，W25/33 Q7，W24/32 Q3，W23/33 Q5 |
| 7.5.5 relationship between economies of scale and decreasing average costs（p.25） | 1／7／7 | 文字 1、组合行 4、图 3、NOT／least 1 | 两家航空公司合并后沿 LRAC 下移的原因 | 规模经济使平均成本下降 | W25/31 Q2 |
| 7.5.6 internal and external economies of scale（p.25） | 2／4／4 | 文字 3、图 1 | 哪一项是内部或外部规模经济 | 内部：企业自身扩大规模带来的单位成本下降；外部：行业在当地集聚带来的好处，如本地学院的相关培训（W24/33 Q8） | S25/31 Q5，W24/33 Q8 |
| 7.5.7 internal and external diseconomies of scale（p.25） | 1／1／1 | 选图 1、图 1 | 四个成本图中哪一个表示规模不经济 | LRAC 上升段 | S25/32 Q5 |
| 7.5.9 definition of normal, subnormal and supernormal profit（p.25） | 2／6／5 | 图 4、计算 3、组合行 2 | 垄断图上只有正常利润的产量；固定成本上升对利润最大化企业的价格、产量与利润的影响 | AR = AC；固定成本不影响 MC、MR → 价格、产量不变，利润下降（W24/32 Q6） | S25/31 Q6，W24/32 Q6 |
| 7.5.10 calculation of supernormal and subnormal profit（p.25） | 1／1／1 | 计算 1、表格数据 1 | 由 MR、AR、MC、ATC 表求利润最大化产量上的超额利润总额 | 先找 MC = MR 的产量，再算 (AR − ATC) × Q（W24/33 Q4：(85 − 75) × 3 = 30） | W24/33 Q4 |
| 7.6.1 perfect competition and imperfect competition: monopoly, monopolistic competit…（p.25） | 5／9／9 | 文字 7、NOT／least 2、计算 2、图 2、选图 1 | 识别市场结构（并购后一家占 80%）；各结构的特征（垄断竞争无进入壁垒；自然垄断）；哪个行业企业最不能自行定价；高固定成本、低边际成本、MES 很大的结构 | price taker = 完全竞争；MES 相对市场需求很大 → natural monopoly，进入壁垒高、一家主导（S24/31 Q10） | W23/32 Q4，W25/32 Q4，W24/31 Q8，S24/31 Q10 |
| 7.6.3 barriers to entry and exit（p.25） | 4／6／5 | 文字 5、组合行 1、NOT／least 1 | 专利保护属于哪类进入壁垒；哪组成本条件最能阻止进入；可竞争市场的必要假设；现实中退出为何有成本 | 法律壁垒；高沉没成本、高 MES；可竞争 = 可自由进出（S24/31 Q7）；退出时收不回的固定成本即沉没成本（W24/33 Q6） | W24/33 Q6，S24/31 Q7，W23/31 Q7，S23/32 Q10 |
| 7.6.4 performance of firms in different market structures（p.26） | 12／20／15 | 文字 9、组合行 6、图 6、NOT／least 3、计算 3、选图 1 | 长期垄断竞争的效率与利润（含四图选一）；短期与长期停业条件；非勾结寡头的定价行为；哪些结构可竞争；两家企业合作或独立的收益表（命名概念）；需求移动后 TR 与 DWL 面积 | 长期：AR 切 AC，正常利润、无配置效率；短期只须 TR ≥ TVC，长期须覆盖全部成本（S23/31 Q6 的 PER）；非勾结寡头：一家涨价他家不跟（S24/31 Q5）；囚徒困境 | S23/31 Q6，M23/32 Q6，S24/31 Q5，W25/33 Q5 |
| 7.6.5 definition and calculation of the concentration ratio（p.26） | 3／4／4 | 文字 3、表格数据 1 | 由前几家企业份额判断市场结构或集中度的变化；四企业集中度 25% 的含义 | 集中度 = 最大 n 家企业的市场份额之和；集中度高 → 寡头 | S25/34 Q6，W24/32 Q5，W24/33 Q10 |
| 7.7.1 reasons for different sizes of firms（p.26） | 2／2／2 | 文字 1、组合行 1、NOT／least 1 | 什么使小企业更难生存；大小企业配对陈述 | 潜在竞争者面前没有有效的进入壁垒（S24/32 Q8） | S25/31 Q7，S24/32 Q8 |
| 7.7.3 external growth of firms – integration (mergers and takeovers)（p.26） | 12／15／13 | 文字 10、组合行 4、NOT／least 2、图 1 | 横向、前向纵向、后向纵向整合的识别（情境题）；合并后 AR、LRAC 与需求弹性的变化；同行合并最不令人信服的理由 | 同行业同阶段合并 = 横向；收购供应商（咖啡农场、芯片设计公司）= 后向纵向整合；收购主要对手后 PED 下降、LRAC 下降（S23/31 Q8） | S24/31 Q9，W25/34 Q3，S25/32 Q7，W24/31 Q5 |
| 7.7.4 cartels（p.26） | 3／5／5 | 文字 5、NOT／least 1 | 什么阻止卡特尔形成或勾结；限产或定价的生产者协议叫什么 | 进入壁垒低（M25/32 Q3）、需求不稳定（W25/34 Q1）会阻止勾结；限产定价协议 = cartel（W24/33 Q9） | W25/34 Q1，M25/32 Q3，W24/33 Q9 |
| 7.7.5 principal–agent problem arising from differing objectives of shareholders/owne…（p.26） | 6／7／7 | 文字 6、NOT／least 1、计算 1 | 哪一项不是委托代理问题（NOT）；所有权与控制权分离的结果；什么能缓解、什么会加剧 | 所有权与控制权分离、目标不一致；利润挂钩报酬或经理持股可缓解，取消持股会加剧（W23/33 Q3） | S23/31 Q11，M23/32 Q8，W25/31 Q1，W24/31 Q9 |
| 7.8.1 traditional profit-maximising objective of firms（p.27） | 3／7／7 | 计算 4、图 4、表格数据 2、组合行 1 | 由 TC／TR 表识别企业目标；哪种策略不属于非利润最大化目标；从 MC = MR 增产到 MR 仍为正时利润与 TR 的变化 | 长期定在 MC = MR 就是利润最大化（S24/31 Q8）；增产到 MR 仍为正：利润下降、TR 上升 | W25/31 Q3，S24/31 Q8，S24/32 Q6 |
| 7.8.2 an understanding of other objectives of firms（p.27） | 11／14／12 | 文字 3、计算 9、图 8、NOT／least 1、表格数据 1 | 图上定位收益最大化、销量最大化、利润最大化产量；改换目标后 TR 增加对应哪块面积；MR = 0 对应什么目标；按情境识别 profit satisficing | 利润最大：MC = MR；收益最大：MR = 0；销量最大（正常利润约束）：AR = AC；ΔTR = MR 下方面积；只求让所有者满意的利润 = satisficing（W24/31 Q6） | M25/32 Q4，W25/31 Q7，W24/31 Q6，S24/31 Q4 |
| 7.8.3 price discrimination – first, second and third degree（p.27） | 5／5／5 | 文字 5、NOT／least 1 | 有效价格歧视的必要条件；哪一项不是必要条件（NOT）；情境识别（航空公司、长途汽车越临近出发越贵） | 能分割市场、不能转售、各市场 PED 不同；产品缺乏弹性本身不够 | W23/31 Q6，W24/32 Q7，S23/32 Q3 |
| 7.8.4 other pricing policies（p.27） | 2／3／3 | 文字 | 哪种结构能出现价格领导；为阻止进入而设低价叫什么 | 寡头；limit pricing | W25/33 Q2，S25/34 Q5 |
| 7.8.5 relationship between price elasticity of demand and a firm’s revenue（p.27） | 1／1／1 | 组合行 1 | 哪种对手反应造成拗折需求曲线 | 涨价不跟、降价跟 | W23/31 Q5 |

#### Topic 8 Government microeconomic intervention（考纲 pp.27–28）

| 条目 | 主／全／卷 | 题型 | 常见问法 | key 反映的结论 | 代表题 |
|---|---|---|---|---|---|
| 8.1.1 application and effectiveness of measures to tackle different forms of market …（p.27） | 34／46／20 | 文字 38、NOT／least 6、图 5、计算 4、表格数据 1、选图 1、组合行 1 | 全卷最高频。政策选择与效果：间接税、补贴、最高价、管制、可交易许可证、产权、直接提供、国有化／私有化、nudge；哪项不用市场力量或不属于 regulation（NOT）；税收收入低于预测的原因；许可证相对税的优点；2025 年起 nudge 几乎每卷一题 | 按失灵类型选政策（公共物品 → 政府直接提供，S23/31 Q12）；需求缺乏弹性时税对数量作用小；许可证使污染总量确定；把垄断价格管制在 AR = MC 处可达配置效率（W24/33 Q11）；nudge 的本质是 persuasion（W25/32 Q9），不靠禁令或价格 | S23/31 Q13，M23/32 Q15，W25/31 Q9，S25/31 Q8 |
| 8.1.2 government failure in microeconomic intervention（p.28） | 10／12／10 | 文字 11、NOT／least 3、组合行 1 | 哪一项是或不是 government failure；哪项政策最可能导致政府失灵；最高价、禁烟、修路等政策的意外后果；PED 与执法开支组合 | 政府干预使配置更差（意外后果、执法不足）；对垃圾按量征税可能引发非法倾倒（S24/31 Q11 的 PER）；最高价低于市场价 → 短缺 | M25/32 Q8，S24/31 Q11，W23/31 Q11，S23/31 Q17 |
| 8.2.1 difference between equity and equality（p.28） | 2／3／3 | 文字 | 哪项体现 equality 而非 equity；何时收入分配更平等 | 同等对待所有人 = equality；按需要区别对待 = equity | M25/32 Q9，W25/34 Q9 |
| 8.2.3 distinction between absolute poverty and relative poverty（p.28） | 1／1／1 | 文字 | 什么最可能使相对贫困增加 | 取消全国最低工资（W23/33 Q13） | W23/33 Q13 |
| 8.2.4 the poverty trap（p.28） | 6／6／6 | 文字 4、组合行 2 | 什么造成贫困陷阱；免税额与 means-tested 福利份额怎样组合会加重；如何降低 | 多挣一元导致更多福利被扣（S24/31 Q13 的 PER：许多考生不认识这个术语）；降低免税额、提高 means-tested 份额会加重（W24/33 Q15） | S24/31 Q13，W25/31 Q10，S25/31 Q11，W24/33 Q15 |
| 8.2.5 policies towards equity and equality, for example（p.28） | 9／18／12 | 文字 13、组合行 3、图 2、NOT／least 2 | 再分配政策组合（累进所得税、间接税、福利）；UBI 的效果；短期内降低不平等的政策；政策与优缺点配对；可支配收入计算 | UBI 降低工作激励但提高平等；销售税在花费可支配收入时才交；短期降低不平等：最低工资（W24/32 Q15） | W23/32 Q12，M23/32 Q16，S23/32 Q15，W25/32 Q10 |
| 8.3.2 factors affecting demand for labour in a firm or an occupation（p.28） | 1／3／3 | 文字 2、组合行 1 | 提高劳动边际生产率的政策（教育、资本品税收减免 yes/no 行）；什么使劳动需求右移 | 两项都提高劳动生产率（W23/33 Q12 的 PER：44% 只选了教育） | W23/33 Q12 |
| 8.3.3 causes of shifts in and movement along the demand curve for labour in a firm o…（p.28） | 6／7／7 | 文字 4、图 2、组合行 1 | 什么使劳动需求或 MRP 曲线移动；生产率提高对需求、供给与工资的影响 | 产品需求上升或劳动生产率上升（新机器）→ MRP 右移；最终产品价格下降 → MRP 左移（W24/32 Q13） | W25/33 Q9，W24/32 Q13，S24/31 Q14，M24/32 Q14 |
| 8.3.4 marginal revenue product (MRP) theory（p.28） | 5／10／8 | 文字 3、计算 3、图 3、表格数据 1、组合行 1 | MRP 怎么算、劳动需求曲线怎么来；利润最大化的雇佣条件；AP、MP 曲线与工资线决定雇佣量 | MRP = MPP × MR（S23/33 Q15 的 PER：选项分布像在猜）；雇到 MRP = 雇佣的边际成本（S24/32 Q14） | M25/32 Q13，W24/31 Q15，S24/32 Q14，M24/32 Q15 |
| 8.3.5 factors affecting the supply of labour to a firm or to an occupation（p.28） | 4／7／6 | 文字 4、图 1、表格数据 1、组合行 1、NOT／least 1 | 哪一项不是劳动供给因素（NOT）；向后弯曲供给曲线的定义；净优势；两职业表格比较 | 劳动生产率影响需求不影响供给 | S25/32 Q13，S24/32 Q13，W23/32 Q11，M23/32 Q13 |
| 8.3.6 causes of shifts in and movement along the supply curve of labour to a firm or…（p.28） | 5／6／5 | 文字 2、图 2、组合行 2 | 两条供给曲线斜率不同的原因；企业自办培训、女性劳动供给减少、劳动力扩大的影响 | 所需技能越专门、培训越长，供给越缺乏弹性（M23/32 Q12）；劳动力扩大 → 平均工资增速下降（W24/31 Q13） | W23/31 Q13，W25/34 Q10，W24/31 Q13，M23/32 Q12 |
| 8.3.7 wage determination in perfect markets（p.28） | 1／5／5 | 组合行 2、图 2、计算 1、表格数据 1 | 完全竞争劳动市场中给 MRP 与 MCL 求雇佣量；工会提高工资对竞争企业就业的影响 | 雇到 MRP = MCL 为止（W24/32 Q14：MRP = MCL = 30，雇 3 人）；竞争市场工资高于均衡 → 就业减少 | W24/32 Q14 |
| 8.3.8 wage determination in imperfect markets（p.28） | 14／17／15 | 文字 7、图 8、计算 1、组合行 1、表格数据 1、NOT／least 1 | 竞争市场与买方垄断市场的最低工资效应；工会提高工资对竞争企业与买方垄断者就业的影响；工会何时能提高工资而不减少就业；降低实际工资的政策 | 竞争市场：就业下降，降幅由 MRP 曲线决定；买方垄断：就业可增、失业减少、DWL 缩小；经济整体就业上升时工会议价力强（S25/34 Q12）；公共部门加薪低于通胀可降实际工资（M25/32 Q12） | W25/31 Q12，S25/31 Q12，M25/32 Q12，W24/32 Q12 |
| 8.3.10 transfer earnings and economic rent（p.28） | 8／8／8 | 文字 1、图 7、组合行 1、NOT／least 1 | 在劳动市场图上指认经济租与转移收入面积；完全弹性与完全无弹性供给的极端情形；供给弹性变化后两者的增减；数值例（教师）；最低工资后经济租增加的面积 | 经济租 = 工资线以下、供给曲线以上；完全弹性 → 全为转移收入；完全无弹性 → 全为经济租；供给变得更有弹性 → 转移收入增加、经济租减少（W24/33 Q14） | W25/34 Q14，S25/31 Q14，M25/32 Q14，W24/33 Q14 |

#### Topic 9 The macroeconomy（考纲 pp.29–31）

| 条目 | 主／全／卷 | 题型 | 常见问法 | key 反映的结论 | 代表题 |
|---|---|---|---|---|---|
| 9.1.1 the multiplier process（p.29） | 12／16／14 | 文字 10、计算 5、表格数据 1、组合行 1、图 1 | 乘数大小计算；乘数模型的必要假设；所需投资增量；哪组变化使乘数最大；开放经济后什么下降；乘数定义；债券融资赤字的效果 | k = 1/(MPS + MRT + MPM) = 1/(1 − MPC)（无政府无外贸）；所需注入 = 缺口／k；Keynes 模型假设 APS 随收入上升（S24/31 Q19，该卷最差题，四成选了充分就业） | S24/31 Q19，W25/31 Q22，S25/31 Q15，M25/32 Q24 |
| 9.1.2 components of Aggregate Demand (AD) and their determinants（p.29） | 15／18／11 | 文字 14、组合行 2、计算 1、图 1 | accelerator 的表述、假设与解释对象；C = a + bY 中 a、b 的变化；由收入与消费数据求 APC、MPC；AMD 与 45° 线；通胀时维持生活水平意味着什么上升 | 投资取决于产出变化率（增速下降 → 投资下降，W23/33 Q21）；b = MPC；MPC = ΔC／ΔY（W24/31 Q19：100／200 = 0.5） | S23/32 Q18，S25/32 Q16，M25/32 Q15，W24/31 Q19 |
| 9.1.3 full employment level of national income and equilibrium level of national inc…（p.29） | 8／10／10 | 文字 2、图 7、计算 2 | 在 45° 线图或注入－漏出图上指认通胀／通缩缺口；用消费函数算通胀缺口；什么导致通胀缺口；什么使国民收入下降 | 缺口在充分就业收入处量；M25/32 Q19 是该卷最差题；削减国防开支使收入下降，减少储蓄或降低 MPM 反而提高收入（W23/33 Q20 的 PER） | M25/32 Q19，S24/32 Q20，W23/33 Q20，W25/34 Q15 |
| 9.2.1 actual growth versus potential growth in national output（p.30） | 5／6／6 | 文字 4、图 2 | PPC 上从曲线内到曲线上的移动原因；什么一定表示长期增长；什么阻碍实际 GDP 更快增长；负的实际增长带来什么 | 曲线内到曲线上 = 实际增长（利用闲置资源）；外移 = 潜在增长；LRAS 垂直段；负增长 → 失业率上升（W24/33 Q22） | W25/31 Q20，M25/32 Q16，W24/33 Q22，W23/32 Q18 |
| 9.2.2 positive and negative output gaps（p.30） | 3／6／5 | 文字 5、图 1 | 正／负产出缺口时增长率、物价、失业的伴随变化 | 正缺口：实际产出高于潜在，通胀压力 | W25/32 Q17，W25/34 Q16，S25/31 Q17 |
| 9.2.3 business (trade) cycle（p.30） | 4／7／6 | 文字 3、组合行 3、图 1 | 读图找最长衰退期；自动稳定器的税与福利组合；预算赤字随周期变化 | 累进所得税 + means-tested benefits = 自动稳定（S25/32 Q17） | W25/33 Q13，S25/32 Q17，S25/32 Q18，M23/32 Q17 |
| 9.2.5 inclusive economic growth（p.30） | 1／1／1 | 文字 1、NOT／least 1 | 哪项政策最不可能促进 inclusive growth（least） | 削弱工会力量的立法（W25/34 Q18） | W25/34 Q18 |
| 9.2.6 sustainable economic growth（p.30） | 7／8／5 | 文字 8、NOT／least 3 | 可持续增长的来源与政策；监管型与市场型气候政策；促增长不一定促发展的政策 | 不损害后代满足需要的能力；开采不可再生资源 | M23/32 Q19，S25/34 Q16，W23/31 Q19，S23/31 Q18 |
| 9.3.2 equilibrium and disequilibrium unemployment (including hysteresis)（p.30） | 5／7／7 | 文字 7、NOT／least 2 | hysteresis 失业的定义与成因；哪个不是结构性失业；需求永久转移的后果；复苏后失业仍上升的解释哪项不对（NOT） | 长期失业导致技能与工作经验丧失；居家办公使市中心店铺关门 → 结构性失业（W23/33 Q18）；挑选合适工作的人属摩擦性（S23/31 Q19） | S23/31 Q19，W25/32 Q14，S25/31 Q16，W23/33 Q18 |
| 9.3.3 voluntary and involuntary unemployment（p.30） | 2／2／2 | 文字 1、组合行 1、NOT／least 1 | 哪类失业可算 voluntary；两个陈述分别属于自愿还是非自愿失业 | frictional（S23/32 Q22）；福利与税收造成的不工作 = 自愿，积极求职却找不到 = 非自愿（W24/33 Q17） | S23/32 Q22，W24/33 Q17 |
| 9.3.4 natural rate of unemployment（p.30） | 7／8／8 | 文字 8、NOT／least 2 | 自然失业率高低的原因；降低政策；福利与自然率（NOT／least） | 工会力量、福利、培训与流动性：参加培训、劳动流动性提高 → 自然率下降（W24/31 Q18，W24/32 Q17） | S24/32 Q18，W25/33 Q15，S25/34 Q17，W24/31 Q18 |
| 9.3.5 patterns and trends in (un)employment（p.30） | 1／6／6 | 文字 2、NOT／least 2、表格数据 2、计算 2、组合行 1 | 比较两国青年与总体失业率表能得出什么；劳动力包括哪些人；由人口、劳动力、就业、失业数求失业率 | 只下表格能支持的结论（S24/31 Q18）；劳动力 = 就业 + 失业，不含经济上不活跃者；失业率 = 失业 ÷ 劳动力（W24/31 Q20：25%） | S24/31 Q18 |
| 9.3.6 mobility of labour（p.30） | 7／8／8 | 文字 6、组合行 1、图 1 | 提高职业流动性的政策或因素；失业与职位空缺同时上升的原因；移民对增长与工资的影响；移民积分表 | 教育与再培训；失业与空缺同时上升 → 职业流动性下降（W24/31 Q17） | W25/31 Q18，S25/31 Q18，M25/32 Q18，W24/31 Q17 |
| 9.3.7 policies to reduce unemployment and their effectiveness（p.30） | 7／12／10 | 文字 9、组合行 2、NOT／least 1、表格数据 1 | 政策与失业类型配对（就业中心 → frictional；培训 → structural；需求侧 → cyclical）；表格比较两国扩张 AD 的结果 | 先判失业类型再选政策 | S23/31 Q21，W25/31 Q16，S24/32 Q25，M24/32 Q17 |
| 9.4.1 definition, functions and characteristics of money（p.31） | 4／4／4 | 文字 | 货币的职能与特征的区分；情境题问是哪一种职能 | 职能：交换媒介、计价单位、价值储藏、延期支付标准；可分、耐久是特征（W23/33 Q17）；分期付款 = 延期支付标准（W24/32 Q16）；比价 = 计价单位（W24/33 Q16） | W24/31 Q16，W24/32 Q16，W24/33 Q16，W23/33 Q17 |
| 9.4.3 quantity theory of money (MV = PT)（p.31） | 4／4／4 | 文字 3、组合行 1、NOT／least 1 | MV = PT 下哪组变化价格不变；什么降低 V；哪句正确或不正确 | M 与 T 同比例增加、V 不变 → P 不变 | W25/31 Q14，S25/31 Q20，S25/34 Q19，M25/32 Q17 |
| 9.4.4 functions of commercial banks（p.31） | 3／3／3 | 文字 2、组合行 1、NOT／least 1 | 中央银行与商业银行职能配对；哪项不是商业银行职能（NOT）；商业银行什么行为引发金融危机 | 中央银行不以利润最大化为目标，商业银行是（M23/32 Q18）；担保要求不足、承担过度风险（S24/31 Q16） | M23/32 Q18，S24/31 Q16，S24/32 Q16 |
| 9.4.5 causes of changes in the money supply in an open economy（p.31） | 4／9／8 | 文字 4、组合行 4、图 2、选图 1、NOT／least 1 | QE 的传导填空与利率图；什么减少国内货币供给；QE 何时最不致失稳 | QE：买资产 → MS 右移 → 利率下降；深度衰退时最安全 | W25/32 Q13，W25/32 Q16，W25/34 Q24，S25/32 Q19 |
| 9.4.6 policies to reduce inflation and their effectiveness（p.31） | 5／8／6 | 文字 7、组合行 1 | 进口价格引起的通胀用什么政策；长期抗通胀手段；紧缩货币在哪种汇率制度下更有效；高利率如何反而推高通胀 | 进口价格推动的通胀：本币升值或重估（M24/32 Q20、Q26）；长期手段：供给侧（W25/33 Q20）；紧缩货币在浮动汇率、AD 对利率敏感时最有效（W25/33 Q22）；高利率提高企业借贷成本 → 成本推动（W24/31 Q23） | W25/33 Q20，W24/31 Q23，M24/32 Q20 |
| 9.4.7 demand for money: liquidity preference theory（p.31） | 8／9／7 | 文字 4、图 4、组合行 1 | 什么减少货币需求；流动性陷阱的特征与位置；LP 曲线右移原因；Keynes 理论中利息的意义 | 利息 = 放弃流动性的报酬；陷阱 = LP 水平段，低利率低通胀低增长；收入或物价上升 → LP 右移 | S24/32 Q21，W25/31 Q17，S25/34 Q18，M24/32 Q16 |
| 9.4.8 interest rate determination: loanable funds theory and Keynesian theory（p.31） | 1／7／6 | 文字 4、图 3、选图 1 | 哪一项属于 Keynesian 分析 | 流动性陷阱、利率由货币供求决定 | W25/31 Q15 |

#### Topic 10 Government macroeconomic intervention（考纲 pp.31–32）

| 条目 | 主／全／卷 | 题型 | 常见问法 | key 反映的结论 | 代表题 |
|---|---|---|---|---|---|
| 10.1.1 objectives in terms of inflation, balance of payments, unemployment, growth, d…（p.31） | 9／9／7 | 文字 8、NOT／least 3、计算 1、表格数据 1 | 政策行为对应的目标（加 VAT → 减赤字；加息 → 控通胀）；哪项是或不是宏观目标；读表选最接近全部目标的国家；增长提高后最可能同时实现的目标；封闭经济没有哪个目标 | 宏观目标针对整个经济：增长、低通胀、低失业、国际收支、发展与可持续；Pareto 最优、垄断管制不是（W24/31 Q21，W23/33 Q26）；封闭经济无国际收支目标 | W23/33 Q25，S25/31 Q22，W24/31 Q21，M24/32 Q21 |
| 10.2.1 relationship between the internal value of money and the external value of money（p.31） | 6／11／8 | 文字 4、组合行 7 | 贬值、降息、QE、国内物价上涨对货币内部价值与外部价值的影响（组合行） | 内部价值 = 购买力（物价），外部价值 = 汇率 | S25/31 Q24，M25/32 Q20，M24/32 Q25，S23/32 Q26 |
| 10.2.2 relationship between the balance of payments and inflation（p.31） | 3／8／8 | 文字 4、组合行 4、表格数据 1 | 国内通胀上升对国际收支的影响；国际收支赤字何时带来最大需求拉动压力 | 通胀上升 → 出口竞争力下降、经常账户恶化 | S23/31 Q24，S25/34 Q22，S24/32 Q23 |
| 10.2.3 relationship between growth and inflation（p.31） | 1／2／2 | 文字 1、组合行 1 | 哪项政策提高增长而不引起通胀 | 增加供给的措施，如对生产者补贴（M25/32 Q21） | M25/32 Q21 |
| 10.2.4 relationship between growth and the balance of payments（p.31） | 1／3／3 | 文字 1、表格数据 1、组合行 1 | 固定汇率下贸易差额恶化后失业与物价的变化 | AD 下降：失业升、物价降 | W25/31 Q19 |
| 10.2.5 relationship between inflation and unemployment（p.31） | 13／15／13 | 文字 5、表格数据 5、图 4、组合行 2 | 表格中哪一年或哪几国符合（或最不符合）Phillips 权衡；预期增广 Phillips 曲线上的移动路径；短期 Phillips 曲线右移原因；为何只在短期成立；Phillips 曲线的纵轴 | 失业下降伴随通胀上升；AD 上升：沿 SRPC 失业下降，再回到自然率、通胀更高（S24/31 Q21，W24/31 Q22）；通胀预期上升 → SRPC 右移，所以权衡只在短期成立（W24/33 Q21） | W25/32 Q23，S25/31 Q23，W24/31 Q22，S24/31 Q20 |
| 10.3.1 effectiveness of different policies in relation to different macroeconomic obj…（p.32） | 24／37／16 | 文字 25、组合行 8、NOT／least 6、图 5、表格数据 2 | 政策组合的有效性（衰退、通缩、滞胀、三重问题）；Laffer 曲线（三次）；降息在衰退中为何可能无效、何时有效；货币政策时滞；扩张财政何时无效；加强市场力量的政策 | 按问题来源选政策（能源价格推动的滞胀：削减间接税，S24/31 Q22）；企业信心低时降息无效（W24/33 Q18），投资对利率有弹性时有效（W24/33 Q23）；Laffer：超过峰值税率后再提高税率反使税收下降 | S24/32 Q22，W25/32 Q15，S25/34 Q20，W24/32 Q20 |
| 10.3.2 problems and conflicts arising from the outcome of these policies（p.32） | 10／21／13 | 文字 16、组合行 3、表格数据 2、NOT／least 2、图 1 | 政策冲突与副作用：挤出效应命名；加息的其他后果；通胀目标调整原因；增加直接税的结果组合；哪对目标可同时实现 | 增长与通胀、失业与通胀、增长与经常账户之间的冲突 | W25/31 Q21，S25/31 Q19，M24/32 Q23，S23/32 Q23 |

#### Topic 11 International economic issues（考纲 pp.32–34）

| 条目 | 主／全／卷 | 题型 | 常见问法 | key 反映的结论 | 代表题 |
|---|---|---|---|---|---|
| 11.1.1 components of the balance of payments accounts: current account, financial acc…（p.32） | 6／9／7 | 文字 7、NOT／least 3、组合行 2 | 经常账户与金融账户各含什么（FDI、股息、利息归哪个账户）；哪一项不在经常账户（NOT）；经常账户转为赤字的原因 | 服务贸易、初次收入（利息利润股息）、二次收入在经常账户；FDI、证券投资、官方储备在金融账户（W24/31 Q26，W24/32 Q26，M25/32 Q25） | W25/31 Q25，M25/32 Q22，W24/31 Q26，M24/32 Q27 |
| 11.1.2 effect of fiscal, monetary, supply-side, protectionist and exchange rate polic…（p.32） | 5／11／9 | 文字 6、图 2、组合行 2、计算 1 | 各类政策对经常账户的作用；固定汇率下加息对两个账户；长期解决持续赤字的办法 | 固定汇率下加息：需求下降改善经常账户，资本流入改善金融账户（W25/31 Q29） | M23/32 Q24，W25/31 Q29，S25/32 Q27 |
| 11.1.3 difference between expenditure-switching and expenditure-reducing policies（p.32） | 7／7／7 | 文字 6、NOT／least 1、计算 1 | 支出转换与支出削减政策的识别（汇率下调、关税 = 转换；加所得税 = 削减）；何时支出削减优于支出转换（PED 与 MPM 表） | 进出口 PED 低、MPM 高时用支出削减 | S24/32 Q26，S25/34 Q26，W24/31 Q25，M23/32 Q29 |
| 11.2.1 measurement of exchange rates（p.32） | 1／1／1 | 文字 | trade-weighted exchange rate 的定义 | 按贸易权重的一篮子汇率 | W25/32 Q25 |
| 11.2.2 determination of exchange rates under fixed and managed systems（p.32） | 2／4／3 | 文字 3、组合行 1 | 窄幅可变区间的汇率制度叫什么；固定汇率下有顺差时维持汇率的政策 | managed float（M24/32 Q28）；顺差压力下用扩张性货币政策（W25/34 Q29） | W25/34 Q29，M24/32 Q28 |
| 11.2.3 distinction between revaluation and devaluation of a fixed exchange rate（p.32） | 2／5／5 | 文字 | 官方调低货币相对约定汇率叫什么；浮动汇率下跌与固定汇率上调的术语 | devaluation；浮动下跌 = depreciation，固定上调 = revaluation（W24/32 Q27） | W25/33 Q25，W24/32 Q27 |
| 11.2.4 changes in the exchange rate under different exchange rate systems（p.32） | 4／8／6 | 文字 6、组合行 2、NOT／least 1 | 什么不会使货币升值（NOT）；从低估的固定汇率转为浮动时哪个目标受益；低收入经济贬值对三个目标的影响；欧元区国家改用浮动汇率 | 国内通胀上升不会使货币升值（M25/32 Q23） | W25/31 Q30，S25/32 Q26，S25/34 Q29，M25/32 Q23 |
| 11.2.5 the effects of changing exchange rates on the external economy using Marshall-…（p.32） | 10／11／8 | 文字 3、组合行 4、图 3、计算 3、表格数据 2 | J 曲线与 Marshall–Lerner：给短期、长期弹性表选组合；升值时的反 J；AD/AS 图上升值后的新均衡；贬值对成本推动与需求拉动通胀；J 曲线初期恶化的原因 | 短期 PEDx + PEDm < 1，长期 > 1；贬值初期买方认识价格变化需要时间，经常账户先恶化（S23/32 Q28） | W25/31 Q23，S25/31 Q27，S24/31 Q26，W23/32 Q24 |
| 11.3.1 classification of economies in terms of their level of development（p.33） | 4／10／7 | 文字 8、NOT／least 3、组合行 2 | 按特征判断谁最发达；增长 vs 发展的区别（central to growth but not development）；新兴经济体特征（NOT）；阻碍发展的因素 | 发展包含增长以外的福利、分配与可持续 | S23/32 Q29，W25/32 Q30，S25/31 Q30，S23/32 Q30 |
| 11.3.2 classification of economies in terms of their level of national income（p.33） | 3／5／5 | 文字 1、组合行 2、表格数据 2、计算 1 | 低收入国家常见特征（组合行） | 死亡率高、生产率低、储蓄率低；第一产业依赖高、Gini 高、人均实际收入低（W23/33 Q27） | S25/34 Q28，W23/32 Q25，W23/33 Q27 |
| 11.3.3 indicators of living standards and economic development（p.33） | 27／27／18 | 文字 13、图 6、组合行 5、NOT／least 5、表格数据 4、选图 1 | 出现次数全卷第二（topic 11 第一）。HDI 组成（不含婴儿死亡率；HDI 与 MPI 共有的是受教育年限；HDI 比人均收入多调整了预期寿命）；MEW 对 GDP 的调整；MPI 指标（NOT）；Kuznets 曲线（命名、坐标轴、转折点推断、哪图不是）；PPP 定义；实际人均收入计算；读表判断增长、发展与生活水平 | MEW：环境成本收益、闲暇价值、无酬工作都要调整；实际人均增长 ≈ 名义增长 − 通胀 − 人口增长（W24/33 Q27：5 − 4 − 2 ≈ −1%） | W23/31 Q27，M23/32 Q26，S24/31 Q28，S23/31 Q27 |
| 11.4.1 population growth and structure（p.33） | 7／11／10 | 文字 5、NOT／least 3、组合行 2、表格数据 2、图 2 | 三地出生率、死亡率、婴儿死亡率或城市化表；最优人口；人口老龄化、劳动力缩小的对策；发展中国家变发达后预期寿命 | 读表只下表格能支持的结论；资本存量增加使最优人口变大，出生率上升不会（S24/31 Q29 的 PER） | S24/31 Q29，M25/32 Q27，W24/33 Q25，M24/32 Q30 |
| 11.4.2 income distribution（p.33） | 14／19／15 | 文字 7、图 8、组合行 2、表格数据 2、计算 1、NOT／least 1 | Lorenz 曲线面积求 Gini；哪条曲线最平等；Gini 怎样变化表示更平等；Lorenz 曲线外移最不可能的原因（least）；收入与财富分布变化 | Gini = 平等线与 Lorenz 曲线之间面积 ÷ 平等线以下总面积；越接近 0 越平等；所得税更累进不会使 Lorenz 曲线外移（W24/32 Q29） | W25/32 Q28，S25/32 Q25，W24/32 Q24，S24/31 Q30 |
| 11.4.3 economic structure（p.33） | 1／6／6 | 文字 4、组合行 1、计算 1、表格数据 1、NOT／least 1 | 由三次产业就业份额判断哪国最可能是高收入国家（其余多作低收入、发展特征题的次要标签） | 第一产业份额最小、第三产业份额最大的那国（W24/33 Q30） | W24/33 Q30 |
| 11.5.1 international aid（p.34） | 6／6／6 | 文字 6、NOT／least 2 | 援助的分类（多边、捆绑）；哪类援助附带限制条件；援助对发展作用有限的证据；援助增加后最不可能改善什么；长期效益最大的援助 | 捆绑援助（必须购买援助国商品）附带限制（W24/31 Q28）；赠款用于生产性资本（农机）长期效益大 | M25/32 Q30，W25/32 Q26，S25/34 Q30，W24/31 Q28 |
| 11.5.3 role of multinational companies (MNCs)（p.34） | 4／7／7 | 文字 4、组合行 2、NOT／least 2、计算 1 | MNC 的定义；MNC 增多最可能的后果；MNC 迁入发展中国家短期对就业、投资与经常账户的影响；建厂对低收入国家哪项不是好处（NOT） | 在多国经营的企业；就业与投资上升、经常账户不一定改善（S23/31 Q26）；挤压本地小企业不是好处 | W25/31 Q26，W25/34 Q28，S24/31 Q27，S23/31 Q26 |
| 11.5.4 Foreign Direct Investment (FDI)（p.34） | 6／9／8 | 文字 5、组合行 2、NOT／least 2、图 1、计算 1 | FDI 后再进口机器原料对经常账户与金融账户的影响；FDI 与 GDP 增长关系的读图；低工资、廉价土地何时吸引不到 FDI；哪种对 FDI 的批评最不成立 | 金融账户改善、经常账户恶化；基础设施不足时吸引不到（W23/33 Q30） | W25/34 Q30，W24/32 Q28，S24/32 Q28，W23/33 Q23 |
| 11.5.6 role of the International Monetary Fund (IMF)（p.34） | 3／4／4 | 文字 4、NOT／least 2 | IMF 的职能；哪项不是 IMF 职能（NOT）；IMF 贷款条件与幼稚产业论的冲突 | 为国际收支困难国家提供短期援助（W23/33 Q28 的 PER：42% 误选无息基建贷款）；不为基建项目出资；条件要求贸易自由化、私有化、削减开支 | W23/33 Q28，S25/31 Q28，S25/32 Q29 |
| 11.5.7 role of the World Bank（p.34） | 2／3／3 | 文字 3、NOT／least 2 | 哪项是 World Bank 而非 IMF 的角色；World Bank 的主要职能 | 为发展项目（基建）提供低息贷款 | M25/32 Q29，W25/31 Q28 |
| 11.6.1 meaning of globalisation and its causes and consequences（p.34） | 5／5／4 | 文字 4、NOT／least 2、组合行 1 | 全球化的可能结果；哪项不是全球化的威胁（NOT）；高低收入国家贸易中双方都受益的情形；全球增长没有伴随什么（NOT）；苏伊士运河堵塞说明的后果 | 国际相互依存加深；贸易增加、生活水平提高 | W23/32 Q26，W24/31 Q30，S24/31 Q23 |
| 11.6.2 distinction between a free trade area, a customs union, a monetary union and f…（p.34） | 2／3／3 | 文字 2、图 1 | monetary union 发生什么；哪项不是 customs union 的特征（NOT） | 货币联盟 = 共同货币；关税同盟 = 共同对外关税，无共同货币 | W25/31 Q27，W25/33 Q24 |
| 11.6.3 trade creation and trade diversion（p.34） | 2／2／2 | 图 2 | 关税取消后贸易创造的净收益面积；关税同盟前后进口来源与数量 | 净收益 = w + y（S25/31 Q29） | S25/31 Q29，S25/32 Q30 |

### 4. 至今没考过的条目，以及只作次要标签出现的条目

在 20 份不同的卷里，下面 4 个 A Level 条目一次都没有作为主考点或次要考点出现：

- 7.1.4 derivation of an individual demand curve（p.24）
- 8.2.2 difference between equity and efficiency（p.28）
- 9.3.1 definition of full employment（p.30）
- 10.3.3 existence of government failure in macroeconomic policies（p.32）

注意：这只代表 2023-03 至 2025-11 的 Paper 3；Paper 4 可能考过（见同文件夹的 Paper 4 索引），2026 年的卷没有进索引。只按最初 15 份卷统计时还列在这里的 7.5.10、8.2.3、9.4.1、11.5.2，在补进的 8 份卷里都出现了（9.4.1 在 W23/33 与 W24 三份卷各有一道主考点题）。

下面 10 个条目只作为次要标签出现过（没有一道题以它为主考点），做卡时把它们当作和主考点一起被问的“搭配知识”：

- 7.5.8 definition and calculation of revenue: total, average and marginal revenue (TR…（p.25）：S23/31 Q5，S24/31 Q4，S24/32 Q6，W24/33 Q7，M25/32 Q4，W25/31 Q3，W25/33 Q5，W25/34 Q7
- 7.6.2 structure of the listed markets as explained by number of buyers and sellers, …（p.25）：S24/32 Q5，S24/32 Q9，W24/31 Q8，S25/32 Q6，S25/34 Q6
- 7.7.2 internal growth of firms: organic growth and diversification（p.26）：M24/32 Q9，S25/31 Q7
- 8.3.1 demand for labour as a derived demand（p.28）：S23/31 Q15，M24/32 Q14，S24/31 Q14
- 8.3.9 determination of wage differentials by labour market forces（p.28）：M23/32 Q13，W25/34 Q10
- 9.2.4 policies to promote economic growth and their effectiveness（p.30）：M23/32 Q19，S23/31 Q25，W23/33 Q12，W23/33 Q19，S24/32 Q22，W25/31 Q18
- 9.4.2 definition of money supply（p.31）：W25/32 Q13
- 11.3.4 comparison of economic growth rates and living standards（p.33）：S23/31 Q29，W23/32 Q29，M24/32 Q19，W24/33 Q27
- 11.5.2 trade and investment（p.34）：W24/31 Q30
- 11.5.5 external debt（p.34）：S23/32 Q19

### 5. 评分方案（MS）惯例

- **MS 只有答案字母**：每份 Paper 3 MS 共 3 页，第 2–3 页是 “Question | Answer | Marks” 表，每题一个字母、1 分，"Maximum Mark: 30"；第 1 页写 "Mark schemes should be read in conjunction with the question paper and the Principal Examiner Report for Teachers."（23 份 MS 全部如此，例：`src/9708-P3/2025-11_33_ms.txt`）。第 2 页到 Q28，Q29–Q30 在第 3 页（23 份都是这样；`ms` 字段里的 “MS p.” 照此）。没有 accept／reject、没有部分分，选项为什么对只能从 PER 找。
- **PER 答案表与 MS 一致**：两种来源都有的 11 份卷（M23/32，S23/31、/32、/33，W23/31、/32、/33，S24/31、/32、/33，M25/32）逐字母比对一致。`inventory/9708-mcq-keys.json` 收了全部 23 个 key 串。
- **同一考季的不同卷号一般是不同的题**：例外是 S23、S24、S25 的 /33 = /31（见第 1 节）。PER 对 S24/31 与 /33 的两节评论逐字相同；S23 的两节各评论了不同的题，都评论了 Q6，解释相同、百分比不同（/31 30%、/33 23%）。
- **由 key 反推出的固定结论**（Paper 3 一再按这些判对错，做卡时可以当作“MS 认可的说法”）：
  1. 效用最大化：各商品 MU/P 相等且收入花完，等价写法 MUY × PZ = MUZ × PY（M23/32 Q2，W25/32 Q5，W24/32 Q1，W24/33 Q1）。
  2. 收入效应是两条平行预算线之间的移动；从 E1 到 E2 的整段移动是价格效应（M23/32 Q3，PER 2023-03 pp.6–7）。
  3. 三个产量：利润最大 MC = MR；收益最大 MR = 0；销量最大（受正常利润约束）AR = AC（M23/32 Q5，S23/31 Q5，S24/31 Q4，M24/32 Q6，W24/33 Q7，M25/32 Q4，W25/31 Q7，W25/32 Q7，W25/34 Q7）。从 MC = MR 增产到 MR = 0，TR 增加的是 MR 下方那块面积（M25/32 Q4）。
  4. 停业条件：短期 TR 至少覆盖 TVC，长期须覆盖全部成本（S23/32 Q4；S23/31 Q6 与 PER 2023-06 pp.16–17）。MC 低于 AVC 时 AVC 一定在下降，不论 MC 本身升还是降（S23/31 Q7 的 PER）。
  5. 长期垄断竞争：只有正常利润，且没有配置效率（M23/32 Q6，W23/32 Q5，W24/33 Q5）。
  6. 配置效率 P = MC；自然垄断在 AR = MC 处配置有效但不是生产有效（S25/31 Q2）；把垄断价格管制在 AR = MC 处可达配置效率（W24/33 Q11）。
  7. SB = PB + EB，即 social benefit − external benefit = private benefit（S23/32 Q6）；SC = PC + EC；净社会收益 = 需求曲线下面积 − MSC 下面积（S23/31 Q10 的 PER）。
  8. 经济租与转移收入：完全弹性的供给下工资总额全是转移收入，完全无弹性时全是经济租（S25/31 Q14，S25/32 Q14）；供给变得更有弹性 → 转移收入增加、经济租减少（W24/33 Q14）；数值例中经济租 = 实得工资 − 留在本职的最低工资（M25/32 Q14）。
  9. 买方垄断市场设定有效最低工资可以提高就业、减少失业、缩小 DWL（S25/32 Q12，W25/31 Q12，W24/32 Q12：设在最后一名工人的 MRP 以下）；竞争市场的最低工资或工会加薪使就业减少（M23/32 Q11，S25/31 Q12，W24/33 Q12）。
  10. 乘数 = 1／(MPS + MRT + MPM)（W23/32 Q17：0.2 + 0.2 + 0.1 → 2）；封闭无政府经济 = 1／(1 − MPC)（S25/31 Q15，W25/34 Q17）；MPC = ΔC／ΔY（W24/31 Q19）。
  11. 通胀缺口在充分就业收入处、计划支出高出 45° 线的距离（M25/32 Q19：Y = 800 时 C + I = 840，缺口 40）；均衡收入低于充分就业收入时是通缩缺口（S23/31 Q20，W24/32 Q19）。
  12. J 曲线：短期进出口需求价格弹性之和 < 1，长期 > 1；贬值后经常账户先恶化后改善（S24/31 Q26）；升值时形状倒过来（S25/31 Q27，S25/34 Q27，W25/32 Q29）。
  13. 实际人均收入变化 ≈ 名义增长 − 通胀 − 人口增长（M24/32 Q19：2 − 3 − 1 = −2%；W24/33 Q27：5 − 4 − 2 ≈ −1%）。
  14. HDI 不含婴儿死亡率（S25/31 Q26）；HDI 比人均收入多考虑出生时预期寿命（W24/31 Q27）；HDI 与 MPI 共用受教育年限（W25/33 Q28）；MEW 对 GDP 加减环境成本收益、闲暇价值和无酬劳动三项（W23/31 Q27）。
  15. Gini = 平等线与 Lorenz 曲线之间的面积 ÷ 平等线以下的总面积（W23/31 Q29，S23/31 Q30，W24/33 Q29）；Gini 越低越平等（S24/31 Q30，W24/32 Q24）。
  16. 流动性陷阱：LP 曲线水平段，利率低、通胀低、增长低（S24/32 Q21，W25/31 Q17）。
  17. 先 FDI 买下企业、再进口机器原料：金融账户改善，经常账户恶化（S24/32 Q28）；FDI 记在金融账户，利息利润股息记在经常账户（W24/31 Q26，W24/32 Q26）。
  18. 为基础设施项目提供资金的是 World Bank 而不是 IMF（M25/32 Q29，S25/31 Q28）；IMF 为国际收支困难的国家提供短期援助（W23/33 Q28）。
  19. 货币的职能是交换媒介、计价单位、价值储藏、延期支付标准；可分、耐久是特征（W23/33 Q17）；分期付款 = 延期支付标准（W24/32 Q16），比价 = 计价单位（W24/33 Q16）。
  20. 失业率 = 失业人数 ÷ 劳动力（W24/31 Q20：300 000 ÷ 1 200 000 = 25%）；劳动力含失业者与自雇者，不含经济上不活跃者（S23/31 Q28）。
  21. 支出转换：汇率下调、关税（S24/31 Q25，W24/31 Q25，W24/32 Q25）；支出削减：提高所得税等压缩总需求（W24/33 Q26）。
  22. 预期增广 Phillips 曲线：AD 上升 → 沿短期曲线失业下降、通胀上升 → 回到自然率、通胀更高（S24/31 Q21，W24/31 Q22）；权衡只在短期成立，因为通胀预期会上升（W24/33 Q21）。

### 6. 考官报告（PER）的警示

有 PER 的是 M23、S23（三卷）、W23（三卷）、S24（三卷）、M25。各卷“最多人答对”的题只列题号（已写进对应题的 `er`），下表只列有逐题评论的题。百分比是选各选项的考生比例；“条目”取索引 `spec` 的前两个 id。

| 题 | 条目 | 正确率与主要干扰项 | PER 的解释（意译） | 出处 |
|---|---|---|---|---|
| M23/32 Q2 | 7.1.3 | 32%；A 19%、C 24%、D 25% | 表给的是各单位的 MU 不是 TU；令 MU/P 相等：2 单位 S、1 单位 T（24/6 = 32/8 = 4） | PER 2023-03 p.6 |
| M23/32 Q3 | 7.2.3 | 46%；A 38% | 选 A 的人把 E1→E2 整段当成收入效应；收入效应是两条平行预算线之间的移动（本题为负） | PER 2023-03 pp.6–7 |
| M23/32 Q6 | 7.6.4、7.3.2 | 37%；C 40% | 知道长期垄断竞争没有超额利润，但长期利润最大化点不是配置有效 | PER 2023-03 p.7 |
| M23/32 Q16 | 8.2.5、3.3.4 | 40%；A 35% | 把所得税和销售税都扣掉、又漏了现金福利；销售税是花可支配收入时才交，正确为 55% + 5% = 60% | PER 2023-03 p.7 |
| M23/32 Q26 | 11.3.3 | 37%；B 29%、D 26% | 选 D 的人没看到题问的是“增长指标里不含”的项；实际人均收入本来就在增长指标里 | PER 2023-03 p.7 |
| S23/31 Q2（= S23/33 Q2） | 7.3.3 | /31 38%；D 42% | Pareto improvement 要求至少一人变好且没有人变坏；选 D 的人看到消费者 1、2 变好，没注意到消费者 3 变差了 | PER 2023-06 p.16 |
| S23/31 Q6；S23/33 Q6 | 7.6.4、7.5.2 | /31 30%、C 40%；/33 23%、C 51% | 垄断竞争企业短期须覆盖可变成本，长期须覆盖全部成本；W、Z 连可变成本都不够，短期就停；X、Y 只在长期退出 | PER 2023-06 pp.16–17、p.19 |
| S23/31 Q7（= S23/33 Q7） | 7.5.2 | /31 38%；D 37% | MC 低于 AVC 时 AVC 一定下降，不论 MC 在升还是降；MC = AVC 时 AVC 停止下降 | PER 2023-06 p.17 |
| S23/31 Q10（= S23/33 Q10） | 7.4.1、7.4.5 | /31 32%；A 21%、C 19%、D 28% | 收益看需求曲线下的面积（x + z + w），社会成本看 MSC 下的面积（y + z + w），产量 OQ 处净社会收益 = x − y | PER 2023-06 p.17 |
| S23/33 Q15（= S23/31 Q15） | 8.3.4、8.3.1 | /33 20%；A 23%、B 26%、C 31% | 劳动需求曲线就是 MRP 曲线，MRP = 边际物质产品 × 边际收益；选项分布像是在猜 | PER 2023-06 pp.19–20 |
| S23/32 Q4 | 7.6.4、7.5.2 | 31%；B 41% | 长期须覆盖全部成本（AR ≥ ATC）；选 B 的人答的是短期（只须覆盖 AVC） | PER 2023-06 p.18 |
| S23/32 Q9 | 7.3.1、7.3.4 | 43%；A 28% | 大型独家供应商追求利润，有能力引入新工艺降低长期成本，即动态效率；不会在生产或配置有效的产量上生产 | PER 2023-06 p.18 |
| W23/31 Q4 | 7.5.4、7.5.2 | 25%；A 26%、B 27%、C 22% | 像在猜，也有人没看到题问 NOT correct；收益递减对应短期成本曲线上升段 | PER 2023-11 p.17 |
| W23/31 Q6 | 7.8.3 | 32%；B 44% | 价格歧视的分析涉及不同消费者的 PED 差异，但“产品缺乏弹性”本身不能让企业有效地价格歧视 | PER 2023-11 pp.17–18 |
| W23/31 Q27 | 11.3.3 | 31%；C 35% | MEW 要对环境成本收益、闲暇价值、无酬家务（打扫、育儿）三项都做调整 | PER 2023-11 p.18 |
| W23/32 Q1 | 7.1.1 | 37%；D 35% | 图里是总效用曲线不是边际效用曲线；第 4 块时两曲线相差 30 是 TU 的差，第 4 块的 MU 分别是 +5 和 −5 | PER 2023-11 p.19 |
| W23/32 Q4 | 7.6.1、7.7.3 | 37%；A 25%、D 24% | 两家大企业占 80% 是寡头，合并后成为垄断，其余 20% 的结构不变 | PER 2023-11 pp.19–20 |
| W23/32 Q12 | 8.2.5 | 37%；B 45% | UBI 定期发给每个人，没有收入审查、不论是否工作，所以会降低工作激励 | PER 2023-11 p.20 |
| W23/33 Q12 | 8.3.2、9.2.4 | 54%；C 44% | 改善教育提高劳动技能与生产率；资本品税收减免鼓励投资，也提高劳动生产率（C 只选了教育） | PER 2023-11 p.21 |
| W23/33 Q20 | 9.1.3、9.1.2 | 51%；A 18%、B 14%、C 17% | 削减国防开支减少政府支出、降低国民收入；减少储蓄、提高 APC、降低 MPM 都会提高收入 | PER 2023-11 p.21 |
| W23/33 Q25 | 10.1.1 | 53%；A 38% | 政策的主要目标：增长、低通胀、低失业、国际收支为正；D 在增长、通胀、国际收支上都优于 A，A 只在失业上占优 | PER 2023-11 pp.21–22 |
| W23/33 Q28 | 11.5.6 | 43%；D 42% | IMF 贷款要求调整政策：贸易自由化、私有化、削减社会支出和政府支出以平衡预算；C（国际收支短期援助）符合 | PER 2023-11 p.22 |
| S24/31 Q11（= S24/33 Q11） | 8.1.2、8.1.1 | 不到 1/3；其余三项各约 1/5 到 1/4 | 按垃圾量征税可能催生影子经济（非法倾倒），这是政府失灵；奖励、宣传、补助都是鼓励正面行为，而不是惩罚负面行为 | PER 2024-06 p.18（/33：p.22，同文） |
| S24/31 Q13（= S24/33 Q13） | 8.2.4 | 三个错误选项各超过 1/5 | 很多人不认识 poverty trap：它指收入增加时失去福利，多挣一元反而被扣更多 | PER 2024-06 p.19（/33：p.23） |
| S24/31 Q19（= S24/33 Q19） | 9.1.1、9.1.2 | 28%（该卷最差）；C 超过 40%、D 约 1/6 | Keynes 模型假设收入越高、储蓄所占比例越大；充分就业是古典或货币主义模型的假设；模型对开放或封闭经济都适用 | PER 2024-06 p.19（/33：p.23） |
| S24/31 Q29（= S24/33 Q29） | 11.4.1 | 超过 1/3；近一半选出生率上升 | 出生率上升使人口增加，但不改变最优人口（使人均 GDP 最大的人口）；资本等其他要素增加才使最优人口变大 | PER 2024-06 p.19（/33：p.23） |
| S24/32 Q18 | 9.3.4、9.3.7 | 27%（该卷最差）；A 超过一半、D 约 1/8 | 失业救济不会迫使企业加薪；A（便于解雇高成本工人）、D（政府支出增加、税收随之上升）都是救济可能的效果；可能没看到粗体 NOT | PER 2024-06 p.20 |
| S24/32 Q20 | 9.1.3、9.2.2 | 略过半数；各错误选项都有不少人选 | PPC、LRAS、实际与趋势 GDP 三图都显示低于充分产出 → 通缩缺口；有闲置产能时增长不必先推高物价；LRAS 水平段上供给侧政策无效 | PER 2024-06 p.21 |
| S24/32 Q21 | 9.4.7 | 29%；B 最多，A、D 各约 15% | 流动性陷阱：利率极低、投机者预期债券价格下跌，最可能出现在增长与通胀都低时；很多考生不熟悉这些条件 | PER 2024-06 p.21 |
| M25/32 Q4 | 7.8.2、7.8.1 | 不到 1/5；超过 3/4 选 C 或 D | Y + Z 是总成本的增加、Z 是利润的减少；考生不懂 MR 与 TR 的关系，或把 TR 与利润混淆 | PER 2025-03 p.6 |
| M25/32 Q19 | 9.1.3、9.1.1 | 全卷最差；B、C 最多 | 忽略了 C = 100 + 0.8Y 里的 100，算出 $160m（B）或加上 I 后 $260m（C） | PER 2025-03 pp.6–7 |
| M25/32 Q29 | 11.5.7、11.5.6 | 不到 1/5；正确的 D 最少人选 | 其余三项 World Bank 与 IMF 都做；"Candidates need to have a better knowledge of this part of the syllabus." | PER 2025-03 p.7 |

**PER 的总体评语**：

- 平均分：W23/31 1055 人、16.4／30；W23/32 4118 人、16.6／30；W23/33 171 人、22.7／30（PER 2023-11 pp.17、19、21）。
- S23/31：答对率 75% 以上的有 Q9、11、13、17、19、21、24、27、28，低于 40% 的是 Q2、6、7、10；S23/33 同一份题，60% 以上的 10 题，低于 25% 的是 Q6、Q15（PER 2023-06 pp.16、19）。
- S24/31（= /33）：15% 的考生答对 24 题以上；微观题略好于宏观题；Q2、3、5、9、28 答对率 80% 以上，Q11、Q19 不到三分之一（PER 2024-06 p.18）。S24/32："Candidates performed significantly better on the microeconomic questions compared to the macroeconomic ones."，Q18、Q21 答对率不到 30%（p.20）。
- M25/32："Candidates performed significantly better on the microeconomic questions compared to the macroeconomic ones."（PER 2025-03 p.6）
- 反复出现的失分原因：没看到 NOT（W23/31 Q4、M23/32 Q26、S24/32 Q18）；把 TU 当 MU、把 TR 当利润（W23/32 Q1、M25/32 Q4）；短期与长期条件混淆（S23/32 Q4、S23/31 Q6）；只记住一半条件（“缺乏弹性”就能价格歧视，W23/31 Q6；长期无超额利润就以为有配置效率，M23/32 Q6；只选教育、漏了资本品税收减免，W23/33 Q12）；不认识术语（poverty trap、optimum population，S24/31 Q13、Q29）；Keynes 与古典假设混淆（S24/31 Q19）；计算漏掉自主消费（M25/32 Q19）；国际机构职能分不清（M25/32 Q29、W23/33 Q28）。做选择题辨析卡时，这些干扰项就是现成的“错误说法”。

### 7. 来源状态与审核

**Paper 3 来源（2026-10-06）**

| 考季 | 卷 | QP 与 MS | PER |
|---|---|---|---|
| 2023-03 | 32 | 有 | 有（`src/9708-ER/2023-03_all_er.pdf` pp.6–7） |
| 2023-06 | 31、32、33 | 有（/31、/33 的 QP 与 MS，以及 /32 的 MS，来自 `Upppllld/OpenPastPapers@6db0095`） | 有（/31 pp.16–17，/32 pp.18–19，/33 pp.19–20） |
| 2023-11 | 31、32、33 | 有（/33 来自 OpenPastPapers） | 有（/31 pp.17–18，/32 pp.19–20，/33 pp.21–22） |
| 2024-03 | 32 | 有 | **没有** |
| 2024-06 | 31、32、33 | 有（/31、/33 来自 OpenPastPapers） | 有（Drive `s24-er.pdf`，本地 `src/9708-ER/2024-06_all_er.pdf`：/31 pp.18–19，/32 pp.20–21，/33 pp.22–23） |
| 2024-11 | 31、32、33 | 有（都来自 OpenPastPapers） | **没有** |
| 2025-03 | 32 | 有 | 有（pp.6–7） |
| 2025-06 | 31、32、33、34 | 有 | **没有** |
| 2025-11 | 31、32、33、34 | 有 | **没有** |
| 2026-03 | 32 | 没有（已公布，拿不到） | 没有 |
| 2026-06 | 31–34 | 没有（已公布，拿不到；变体是否齐全未核实） | 没有 |

- OpenPastPapers 的文件都核对过封面卷号、考季与逐页页脚（如 `9708/31/O/N/24`），MS 页眉写明卷号与考季；本地副本在 `src/9708-P3/<series>_<卷>_{qp,ms}.pdf`（+ `.txt`）。
- Drive 上名为 `9708_s24_er.pdf`、`9708_w24_er.pdf`、`9708_s25_er.pdf` 的文件不是报告，而是存下来的 PapaCambridge 网页（`src/9708-ER/check/*.NOT_PDF`）。2024-03、2024-11、2025-06、2025-11 的 PER 在 Drive 与 OpenPastPapers 都没有。
- 2026 年的卷：pastpapers.co 的页面（搜索结果）和公开仓库 `randomizerselection/oehler-huang-library` 里的一份来源审计文件（记录了某教师本地的 `9708_s26_qp_31.pdf`、`9708_m26_qp_32.pdf` 等的 sha256）说明已经公布；Drive、OpenPastPapers（止于 O/N 2025）与 GitHub 代码搜索都找不到文件本身。做卡时要先看有没有比 W25 更新的考季。
- Paper 3 的 specimen QP／MS 没有找到。
- 首轮复查（2026-10-06）只查了 Drive（按标题、页脚代码全文检索）与 Hugging Face，结论“所有来源都查过”不成立：它漏了 finder 轮已记入 `inventory/github-candidates.json` 的 `Upppllld/OpenPastPapers`。critic 轮从那里取得 8 份卷，随后补建索引（见下）。

**第一次审核（2026-10-06，最初 15 份卷、450 条）**

- 合并：part1 180 条 + part2 270 条，无重复 id，按考季、卷号、题号排序。脚本校验：字段齐全，每条 1 分且小问分值之和等于总分，全部 spec id 都在 `spec-items.json`，series 格式 YYYY-MM，每卷题号 1–30 齐全，0 错误。
- key：450 条的 key 与 MS 文本（14 份）和 `inventory/9708-mcq-keys.json`（含 S23/32 的 PER 答案表）逐条比对，0 不符；`ms` 字段里的 MS 页码 450 条全对；QP 页码在能自动定位题号的 410 条里全对（1 条是脚本误把图中标签当题号）。
- 选项转述：281 条能从 QP 文本解析出四个选项的题，把 `ms` 里的 keyed option 转述与 key 字母对应的选项做词重叠比对，0 实质不符（2 条报警是表格题与词形差异）。
- 人工复核 49 条，覆盖全部 15 份卷（每份至少 2 条；其中 9 道图形题用 8 张页面渲染图核对；S25/33 的 Q14、Q27 对过 S25/33 自己的 OCR 文本）：题意、key、条目映射、keyed option 转述都与原文一致，只发现 5 条映射问题。清单见 `work/p3audit/audit_log.json`。
- PER 覆盖：M23、S23/32、W23/31、W23/32、M25 的“最多人答对”题号和逐题评论都已进入对应题的 `er` 字段，逐一对过 PER 原文，没有遗漏或错号。之后 critic 按 PER 2024-06 的 Paper 32 节（pp.20–21）补了 S24/32 的 `er`（Q1、7、10、22、26、29 为正确率 80% 以上的题，Q18、Q20、Q21 有逐题评论）。
- 改动（5 条，都是条目映射；`work/p3audit/fixes.json`）：W23/32 Q25、S25/34 Q28 问的是 low-income countries 的特征，补上漏标的 11.3.2 并设为主考点；M24/32 Q19（实际人均收入计算）主考点由 AS 4.4.3 改为 11.3.3，与 W25/33 Q26 一致；S25/31 Q25 与 S25/33 Q25（关税使受保护行业生产无效率）补 A Level 关联 7.3.1。

**补卷合并与复核（2026-10-06，新增 8 份卷、240 条）**

- 合并：`gap2023.json`（S23/31、S23/33、W23/33，90 条）与 `gap2024.json`（S24/31、S24/33、W24/31、W24/32、W24/33，150 条）并入合并版，与已有 450 条无重复 id，按考季、卷号、题号排序，共 690 条（`work/p3audit/scripts/merge_gaps.py`；合并前的文件存于 `work/p3gap/`）。原有 450 条没有改动。
- 校验：`merge_validate.py` 0 错误（23 份卷，每份题号 1–30 齐全）；把 `spec-items.json` 与两份合并索引放进 `references/exams/cie-9708/` 结构，调用 `scripts/exam_index.py` 的 `check()`：P3 690 条、P4 115 条，0 problems（`check_packaged.py`）。
- key：690 条与 23 份 MS 文本和 key 清单逐条比对，0 不符（`keycheck.py`）。key 清单补了 S24/31、S24/33、W24/31–33 五个 key 串，S24/31、S24/33、S24/32 的 MS 与 PER 答案表逐字母一致；S23/31、S23/33、W23/33 原来只有 PER 答案表，现在也对过 MS。
- 页码：新增 240 条的 QP 页码全对；MS 页码有 6 条错（S23/31、S23/33、W23/33 的 Q29、Q30 在 MS 第 3 页，原写 p.2），已改。
- 选项转述与条目关键词扫描：`optcheck.py` 对新增条目只报 S23/31（= /33）Q1 一处，是转述里带了解释造成的误报；`specscan.py` 对新增条目报 12 处，逐条看过都是题干或选项里的词触发的，映射不需要因此改动。
- 人工复核 17 条新增条目，覆盖全部 8 份卷：S23/31 Q6、Q10，S23/33 Q15，W23/33 Q12、Q27、Q28，S24/31 Q4、Q11、Q19，S24/33 Q22，W24/31 Q20、Q26，W24/32 Q8、Q16、Q18，W24/33 Q18、Q27（W24/31 Q26 的 ✓/✗ 表与 S24/31 Q4 的图用页面渲染图核对，`work/p3gap/img/`）。题意、key、keyed option 转述与 PER 引文都与原文一致。条目映射改 2 条（`work/p3audit/fixes.json`，与第一次审核的同类改动一致）：W23/33 Q27（低收入经济的特征）补 11.3.2 并设为主考点；W24/33 Q27（实际人均收入计算）主考点由 11.3.4 改为 11.3.3。
- 同题卷：S23/33 与 S24/33 的 30 条在 `spec`、`ask`、`ms` 上与 /31 完全相同（MS 页码也相同）。
- 统计：本文件第 1–6 节按合并后的索引重算（20 份不同的卷、600 道不同的题），`desc.py` 为新出现主考点的 9 个条目补写了说明，并按新题更新了 58 个条目的问法与结论。
