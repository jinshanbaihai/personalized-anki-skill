# 用 mark scheme、考官报告和真实作答标定“掌握到什么程度”

考纲只说考什么；**掌握水平**要从评分材料里读出来：定义必须出现哪几个词、推导哪一步单独给分、哪种写法会被判 0、essay 要展开到第几环因果、评价要写到什么程度。每个 core 考点的 `level` 字段（[coverage-ledger.md](coverage-ledger.md)）就写这件事。

## 读多少材料

- 每个 core 考点至少找到 **2 个不同考季**、问法不同的真题，连同对应 MS 一起读；高频考点读到问法不再出新。定义题、计算题、证明题、essay 题分别找。
- 每个单元至少读 1 份 examiner report（Pearson 叫 Examiners' report／PEF，Cambridge 叫 Principal Examiner Report for Teachers），重点读与本批考点相关的题段。
- essay 类科目找**同一题的高中低档真实作答**（Cambridge ECR、Pearson exemplar responses），看档位之间差在哪里。
- 每种卷型分别标定：同一考点在选择题（考辨析细节与干扰项）、结构题、essay 里的掌握要求不同。选择题用考官报告的逐题说明（哪个干扰项最常被选、为什么）做辨析卡。
- **用户自己的卷面**也是标定材料：讲评 PDF 里的逐分记录（`Q01B 1｜Q01M 1｜Q01A1 1｜Q01A2 0`）直接显示这位考生在哪类分上丢分，A 分为 0 的点优先做易错卡（`source_type: "user-script"`）。
- 数学的“真实考生作答”通常只有两种来源：考官报告里转述的考生写法，和用户自己被批改过的卷子；Pearson 是否为 IAL 数学发布带评语的 exemplar 要查，查不到就写进 `research_gaps`。
- 读不到时在 `research_gaps` 写明，并写用什么替代（同类题、同考试局其他单元的 ER、教材）。

## Pearson（IAL／GCE 数学、统计）MS 记号

| 记号 | 含义 | 对卡片的意义 |
|---|---|---|
| M1 | Method：知道方法并开始应用；代入有小错仍可得 | 推导卡标出“方法从哪一步开始算数” |
| dM1／ddM1 | 依赖前一个（两个）M 分 | 前一步方法错，后面方法分一起丢 |
| A1 | Accuracy：只有对应 M 已得才可得；默认 cao（只认正确答案） | 粗心丢的通常是 A 分 |
| A1ft／B1ft | follow through：沿用前面错误结果仍可得 | 说明哪一步可以“错一处、不连坐” |
| A1*／cso／ag | 答案印在题上（show that），整段无误才得 | show that 题必须写出每个中间等式 |
| B1 | 不依赖方法的独立分（陈述、定义、常数因子、结论） | 定义、结论句单独成卡 |
| awrt／3 s.f. | 四舍五入到…；默认非精确答案 3 位有效数字 | 写进“交卷前检查” |
| isw／oe／SC | 忽略后续多写／等价写法可接受／特殊情况封顶 | SC 常揭示典型误解（如不放回误作放回） |

Pure 通则（WMA14 MS p.6）：先写公式再代入；要求 exact 时用小数会丢分；“in your head”能算的可不写过程；`Solutions relying entirely on calculator technology are not acceptable` 的题必须写代数过程。

**老师批注与官方扣分类型的对应**

| 批注 | 通常对应 | 证据 |
|---|---|---|
| 粗心 | A 分（cao）；符号、提出的常数因子、`+c`、有效数字 | WMA14 Jan 2024 ER pp.3、6、7 |
| 过程不充分、答案不严谨 | show that 的 A1*cso；“no solutions”不说明理由；结论不回指原命题 | WMA14 Jan 2024 MS pp.20–21，ER pp.8–9 |
| 忘记答案的最终要求 | exact、3 s.f.、指定形式、锐角、有效范围、`n = 51` 而非 `n ≥ 51`、结论用语境词 | WMA14 Jan 2025 MS p.6；WST02 Jun 2023 ER p.3；WST02 Jun 2024 MS pp.8–9 |

## Pearson 统计定义题：背到哪个词

MS 用三种写法告诉你要背什么：**粗体或下划线关键词**、`oe` 接受清单、明确的 B0 拒收说法。

| 术语 | 必含 | 也接受 | 不给分 | 出处 |
|---|---|---|---|---|
| sampling frame | **list**（register／database）＋**all**＋个体名称 | “database of all members” | 部分名单（“a list of 50 members”）；列的不是个体（“list of all stocktaking systems”） | WST02 Jun 2024 Q3 p.8；Oct 2025 Q1 p.6；Jun 2023 ER p.4（“all”常漏） |
| sampling unit | 个体本身（“the shops”“individual members”） | shop／store／member | 个体的属性（“member's opinions”“the number of shops”） | 同上 |
| statistic | 只由样本观测计算＋不含未知参数 | based solely on observations；contains no unknown parameters；calculated from the sample | “because it is known” | WST02 Jan 2025 Q2 p.8；Jun 2023 ER p.4（会背定义却认不出哪项是 statistic） |
| sampling distribution | all possible samples＋all values of the statistic＋probabilities | “the probability distribution of a statistic” | — | WST02 Oct 2025 Q3(a) p.9 |
| census 与 sample 优缺点 | 优：quicker／cheaper／easier to process；缺：may be biased／not representative／less accurate | — | 单说 “a sample is more uncertain” | WST02 Jun 2024 Q3(c) |

所以术语卡要同时教：标准句、必含词、也给分的说法、不给分的说法，以及一组“这是不是 statistic”的辨认例。

## Cambridge 的定义与 essay 评分

**定义**：Cambridge 接受换词，但按“要素”给分，并且“DO NOT credit answers simply for using a key term”。例：recession = GDP＋负增长＋连续两个季度，三个要素各 1 分（9708/42 F/M 2023 MS p.8）。考纲本身就是定义锚：7.4.1 SC = PC + EC（MSC = MPC + MEC）、7.4.3 positive／negative externality、1.6.3 merit goods = 因 imperfect information 而 under-consumption、8.1.2 government failure。ER 点名的浅层回答：merit good 说成“对人有益”，negative externality 不提 third party。定义卡把要素拆成编号槽位，一个槽位一个得分点。

**Paper 4 essay（20 分）**：AO1＋AO2 共 14 分（Level 3 = 11–14：知识详细、分析充分展开、图和公式准确且在正文中解释），AO3 共 6 分（Level 2 = 4–6：有理由、有支持的评价，给出针对题意的 justified conclusion）。整篇 best fit。

ER 给出的硬门槛：

- 题目要求配图时，缺图或图未正确标注，AO1／AO2 封顶 Level 2（9708 June 2023 ER p.21）。
- 先判断是 consumption 还是 production externality，图要与之对应（9708/42 F/M 2023 ER p.9）。
- 只有一环因果的“部分展开”分析通常停在 Level 2（同上 p.8）；只罗列政策不讨论各自有效程度拿不到高分。
- 评价要质疑题干说法本身；单纯分析影响不算评价（同上 p.10）。

**同一题三档真实作答的差距**（ECR 2023 Paper 42 Q2，16／10／5 分）：低档把税画成 minimum price、定义没写出 private 与 social 的差；中档图缺坐标标签、评价不展开；高档图标注完整并在正文引用，但第二个政策分析不足仍被扣分。由此得到卡片的目标线：**高档已做到的＋高档被扣分的缺口**，也就是 Level 3 上沿。超过这条线的大学层次推导只留在研究记录。

**Indicative content**（“Responses may include … Accept all valid responses”）是可接受路径，进覆盖账本用于查漏，不是每篇必写清单。**MS 认可的写法优先**：卡面先给 MS 的说法，教材里的等价画法用一句“另一种画法”补充；只有 MS 明确拒收（B0、reject 列表、ER 点名扣分）的写法才放进 `reject`。例：9708/42 F/M 2023 MS 写 “a tax … will decrease demand”。对消费征收的税既可画成需求（MPB）向下移动到 MPB − t，也可画成供给向上移动、在价格上形成楔子；两种画法数量结果相同，卡面以 MS 的写法为主，另一种作补充，不暗示 MS 写错。

## 把评分材料变成卡片内容

1. **推导卡**：每步写“做什么、为什么、依据”，右侧 `mark` 用 MS 记号；`mark_note` 写容忍与扣分（“漏乘提出的 2：M1 仍得，A1 全丢”）。题目来自老师 mock 而非官方卷时，`marks_basis` 写“按 WMA14 同类题 MS 推断（Jan 2025 Q3）”。卡末用 `finish` 块写终点要求：exact／3 s.f.／指定形式／有效范围／`+c`／结论回指。
2. **术语卡**：`definition` 的 `text` 用考纲或 MS 原句，`keywords` 标 MS 粗体词，`accept` 与 `reject` 写 MS 的接受与拒收清单；配 `examples` 做辨认；`exam` 块写怎么问、几分。
3. **易错卡**：每条写错误写法、正确写法、为什么错、丢哪一分（`lost`）与来源；来源分清 ER、MS 注释、老师批注，老师批注不冒称 ER。
4. **essay 卡**：AO1 知识点做术语卡与图卡；AO2 做箭头因果链（每个箭头一个得分环节，节点可标 `ao`）；AO3 评价写全“条件 → 后果 → 对结论的影响 → 判断”；另做一张分档阶梯卡（L1 只点名、L2 一环因果、L3 多环因果＋图在正文中被解释），描述取 levels 原句的中文释义，例句自写并标“示例”。
5. **冷读验收**：只看卡组，能否写出 MS 要求的终点句与关键词（sampling frame 的 “list of all …”、反证法的 “contradiction … so n is odd”、essay 的 justified conclusion）。写不出就是缺口。
