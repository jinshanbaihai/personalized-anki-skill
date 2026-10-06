# CIE 9708 Economics：A Level（A2）考纲摘要

> **构建溯源，不随包发布**：本文件反引号里的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`boards/…` 路径，`*.coverage.part*.md`、`*.questions.part*.json` 等分卷文件，以及审核脚本和它们的输出文件，都是构建登记时沙箱里的工作文件，技能包里没有，只说明结论是怎么核出来的。要看原件，用同目录 `9708-P3.questions.json`、`9708-P4.questions.json` 各条的 `sources`（公开地址或 Drive 定位，见 [README](../README.md) “原件怎么取”）。文中写到的缺口是构建时的记录，**缺口以 `python scripts/exam_index.py 9708 --gaps` 输出为准（快照 2026-10-06）**。

登记日期 2026-10-06。用途：给 9708 A Level 阶段（Paper 3、Paper 4；考纲 topics 7–11）制卡时，先用本文件确认考纲版本、卷型、评分方式和条目编号，再去真题索引查各条目的考法。机读条目目录在同目录的 `spec-items.json`（键 `9708`；AS 131 条，level `AS`；A Level 122 条，level `A2`）。版本与考季的完整核查记录见 `../versions.md` §2。

## 0. 来源

| 代号 | 文件 | 本文件用到的位置 | 本地路径、Drive 与校验 |
|---|---|---|---|
| SYL | *Cambridge International AS & A Level Economics 9708 syllabus for examination in 2026, 2027 and 2028*，**Version 2**（December 2025），44 页 | 逐页抽成文本后通读；用到 pp.1–3、5、9–39、43–44 | `scratchpad/research/dl/cie9708-2026-2028.pdf`，与 `registry/src/9708-SYL/2026-2028_syllabus.pdf` 相同（md5 `36981a13a95397a443c80fb22ad394d0`）；PDF 创建于 2025-12-08。Drive `697423-2026-2028-syllabus.pdf`（ID 1coC6Yup6p2Hv_pzwqYMj3eCtA4TCynWf，613,490 字节；`versions.md` 记录其 md5 与本地相同）。另有 Drive 副本 `9708_2026_2028_syllabus.pdf`（ID 1lvsRe3nUKFz9kZ5jsr_jg8D72xJSiDXL），字节数相同，md5 未核。逐页文本：`registry/cie-9708/work/syl/pNN.txt`（`pdftotext -layout`）；解析结果：`work/syl_parsed.json`（脚本 `work/scripts/parse_syl.py`） |
| MS-P4 | 17 份 Paper 4 mark scheme：F/M 2023 /42 至 O/N 2025 /44，另加 2023 specimen MS（9708/04） | 通用评分原则、Table A／Table B、Section A 各小问分值、按题加的封顶规则 | `registry/src/9708-P4/<series>_<comp>_ms.txt`（核对脚本 `work/scripts/p4_scan.py`）。引文取自 9708/41 M/J 2024 MS（`research/dl/9708_s24_ms_41.pdf`）：Generic Marking Principles p.2，Social Science-Specific Marking Principles p.3，levels 指引与 AO p.4，Table A p.5，Table B p.6，Section A p.7 |
| QP 封面 | Paper 3：9708/32 F/M 2023、9708/34 O/N 2025；Paper 4：9708/42 M/J 2023、9708/44 O/N 2025 | p.1 的 INSTRUCTIONS 与 INFORMATION | `registry/src/9708-P3/2023-03_32_qp.txt`、`2025-11_34_qp.txt`；`registry/src/9708-P4/2023-06_42_qp.txt`、`2025-11_44_qp.txt` |
| ER-M23 | March 2023 Principal Examiner Report for Teachers，Paper 9708/42 "General comments" | 2023 年改制说明 | `registry/src/9708-ER/2023-03_all_er.txt`（Drive ID 1sdqiivYrg8dRLPPo7v-dalnWusr_EGEx） |

- **页码**：一律写考纲印刷页（"p."）。本考纲印刷页 = PDF 页：pp.4–43 每页页脚的页码与 PDF 页序逐一核对过。
- **引文**：考纲原文（条目、command words、AO）照录英文；MS 与 ER 只引短语，其余用中文转述。

## 1. 版本与适用范围

| 事实 | 内容 | 出处 |
|---|---|---|
| 适用年份 | "Use this syllabus for exams in 2026, 2027 and 2028." | SYL p.1 |
| 版本 | Version 2，"published December 2025"；"There are no significant changes which affect teaching." V2 列出的唯一改动："The weblink on page 38 has been updated." | SYL p.3 方框；p.43 |
| Version 1 | 未读。版权行为 "© Cambridge University Press & Assessment September 2023"，据此推断 V1 发布于 2023 年 9 月（推断） | SYL p.2、p.44 |
| 考季 | "Exams are available in the June and November series. Exams are also available in the March series in India." | SYL p.1；p.38 |
| 用对年份 | "Check you are using the syllabus for the year the candidate is taking the exam." | SYL p.38 |
| 与 2023 年起考试的衔接 | "Any textbooks endorsed to support the syllabus for examination from 2023 are still suitable for use with this syllabus." | SYL p.3、p.43 |
| 试卷变体 | 按 administrative zone 出不同试卷，每个 zone 有自己的时间表。Paper 3／4 各考季的变体号（31–34、41–44）见 `../versions.md` §2.4 | SYL p.39 |

**2023 年改制：现行内容的首考。** F/M 2023（仅限印度）是首考，M/J 2023 是首个全球考季（`versions.md` §2.3）。ER-M23 的 Paper 42 部分写明：

- "the March 2023 paper was based on the new 9708 A Level Economics syllabus"；
- Section A 数据题的结构与评分没有变；
- essay 由 2023 年前的六题任选两题，改为 Section B 两道微观题选一、Section C 两道宏观题选一；
- "Essays are now marked out of 20, instead of being marked out of 25."；
- "Generic marked levels cover 0 to 14 marks and 6 marks are available for evaluation."

所以 2022 年及以前的 Paper 4 essay（满分 25、六选二、旧 levels）不属于本考纲，评分方式不能迁移。用作内容补充时要标明。

**适用判断（本登记的做法）。** 制卡时，2026–2028 年的考试按 SYL V2；F/M 2023 至 O/N 2025 的真题按同一内容框架使用，条目一律用 SYL V2 的编号。依据是 p.3 与 p.43 的两句官方说明（"no significant changes which affect teaching"，以及为 2023 年起考试认证的教材仍然适用）。这是推断：2023–2025 版考纲原文没有读到，条目编号与措辞没有逐条比对过（缺口 G1）。

**更早与更晚的版本（均未读）：**

- **2023–2025 版**：WebSearch 结果给出 `cambridgeinternational.org/Images/595463-2023-2025-syllabus.pdf`（结果标题 "Version 2 Syllabus"）与 `cie.org.uk/Images/633788-2023-2025-syllabus-update.pdf`（结果标题 "2023 2025 syllabus update"）。两个主机及 sbac.edu 上的公开副本都被出口代理拦截（2026-10-06，curl 与 WebFetch），构建登记时可得的 Drive 原件里也没有（标题与全文检索）。
- **2029 版**：WebSearch 摘要两次称官方 9708 页面列有 "2029 Syllabus"（649 KB），只是指针。文件号、适用年份和内容都不知道（缺口 G2）。为 2029 年及以后的考试制卡前，必须先读到它。
- **2022 及以前**：例如 `Images/557232-2022-syllabus.pdf`（指针），不属于本登记。

## 2. A Level 阶段的考试结构

### 2.1 报考路线、成绩与 AS 内容的地位

| 路线（SYL p.12） | Paper 1 | Paper 2 | Paper 3 | Paper 4 |
|---|---|---|---|---|
| 1 AS Level only（同一考季考完全部 AS 卷） | yes | yes | no | no |
| 2 A Level 分两年：第 1 年 AS | yes | yes | no | no |
| 2 A Level 分两年：第 2 年 "Complete the A Level" | no | no | yes | yes |
| 3 A Level（同一考季考完全部四卷） | yes | yes | yes | yes |

- 分段报考时，AS 成绩按 Cambridge Handbook 的规则与时限 carry forward（p.12、p.39）。AS 路线成绩为 a–e，A Level 路线为 A*–E（p.12）。
- p.15："The AS Level content is assumed knowledge for A Level Paper 3 and Paper 4."
- p.36（Paper 3 与 Paper 4 各写一遍）："The AS Level content will not be the direct focus of questions on Paper 3."（Paper 4 同句）。所以 A2 卡组要把 AS 概念当作先修来用，但出题焦点在 topics 7–11。
- 按路线 2 分段报考的学生，第二年只考 Paper 3 与 Paper 4。

### 2.2 两张 A Level 试卷总览（SYL p.11、p.14、p.35–36）

| 项目 | Paper 3 A Level Multiple Choice | Paper 4 A Level Data Response and Essays |
|---|---|---|
| 时长 | 1 hour 15 minutes | 2 hours |
| 分值 | 30 marks：30 道选择题，每题四个选项 A–D，答对 1 分 | 60 marks：Section A 20 + Section B 20 + Section C 20 |
| 占 A Level | 17% | 33% |
| AO1／AO2／AO3 占本卷 | 47%／40%／13% | 33%／37%／30% |
| 题目依据 | "based on the A Level subject content; knowledge of material from the AS Level subject content is assumed" | 同左 |
| 评分 | 只看选项对错 | Section A 按点给分；Section B、C 用 levels-based mark scheme |

- 整个 A Level 的 AO 权重：AO1 35%、AO2 40%、AO3 25%（与 AS 相同）（p.14）。Paper 1 与 Paper 2 各占 A Level 的 17% 和 33%（p.11）。
- p.35："Calculators may be used for all papers." "Formulae are not given in the question papers." 所以 PED、乘数、MRP、集中度等公式都必须背。

### 2.3 Paper 3（选择题）

- **试卷指示**（QP 封面，F/M 2023 /32 与 O/N 2025 /34 相同）："There are thirty questions on this paper. Answer all questions." 每题有 A、B、C、D 四个选项，用 soft pencil 填在答题卡上，可用计算器，草稿写在试卷上。"Each correct answer will score one mark." 试卷共 12 页。
- **MS**：只有每题的答案字母，没有评分说明（核对的 14 份 Paper 3 MS 都不含 point-based 原则）。选项为什么对、为什么错，只能从 Principal Examiner Report 找。
- **AO3 份额（推算）**：30 分的 13% ≈ 4 分，即大约 4 道题考评价。这是从权重算出的近似值，不是官方题数。

### 2.4 Paper 4（数据题与 essay）

**试卷指示**（QP 封面，M/J 2023 /42 与 O/N 2025 /44 措辞相同）："Answer three questions in total: Section A: answer Question 1. Section B: answer one question. Section C: answer one question." "You may answer with reference to any economy you have studied where relevant to the question." 答在随卷的 answer booklet 上，可用计算器。

**Section A：数据题（20 分，必答）。** SYL p.36 的要求：

- "one compulsory data response question (20 marks)"；
- 材料是 "source material containing data in written, numerical and/or diagrammatic form"，考生 "should answer the question using relevant and appropriate information from the source material to support their answer"；
- "Section A has four parts. Answers to part questions should show evidence of evaluation (AO3), where appropriate."

从 17 份 MS 读出的实际拆分（脚本逐份核对，每份小问分值合计都是 20）：

| 考季／卷 | 小问分值 | 最后一问的开头（MS 题干） |
|---|---|---|
| F/M 2023 /42 | (a)3 (b)5 (c)6 (d)6 | Assess whether … |
| M/J 2023 /42 | (a)2 (b)4 (c)6 (d)8 | Evaluate, using the article, … |
| O/N 2023 /42 | (a)3 (b)6 (c)6 (d)5 | Assess whether … |
| F/M 2024 /42 | (a)5 (b)4 (c)(i)3 (c)(ii)8 | Consider whether … |
| M/J 2024 /41 | (a)3 (b)3 (c)6 (d)8 | Use one example … to assess … |
| M/J 2024 /42 | (a)3 (b)3 (c)6 (d)8 | Evaluate … |
| O/N 2024 /41 | (a)4 (b)4 (c)4 (d)8 | Use the information to assess … |
| O/N 2024 /42 | (a)2 (b)4 (c)6 (d)8 | Evaluate the likely impact … |
| F/M 2025 /42 | (a)2 (b)5 (c)6 (d)7 | Consider the effects … |
| M/J 2025 /41 | (a)3 (b)6 (c)3 (d)8 | Assess whether the article provides sufficient evidence … |
| M/J 2025 /42 | (a)2 (b)4 (c)4 (d)10 | With the help of a marginal social cost and benefit diagram discuss whether … |
| M/J 2025 /43 | (a)3 (b)6 (c)3 (d)8 | 与 /41 的 Section A 开头和分值相同（未全文比对） |
| M/J 2025 /44 | (a)3 (b)3 (c)6 (d)8 | With reference to the article, assess whether … |
| O/N 2025 /41 | (a)2 (b)5 (c)6 (d)7 | Consider if the article contains sufficient information … |
| O/N 2025 /42 | (a)3 (b)4 (c)6 (d)7 | Use the article to evaluate … |
| O/N 2025 /43 | (a)5 (b)(i)2 (b)(ii)5 (c)8 | … explain … and assess whether there is enough evidence … |
| O/N 2025 /44 | (a)4 (b)(i)2 (b)(ii)1 (b)(iii)5 (c)8 | Consider whether … |

规律（由上表归纳）：

- 前面的小问 1–6 分，考定义、解释、读数据或画图；最后一问 5–10 分（多为 7–8 分），一律是带评价的命令（Assess、Evaluate、Consider whether、discuss whether），常要求判断材料证据是否充分。
- "four parts" 是考纲说法。实际有 3 个字母小问再分 (i)(ii)(iii) 的情况（F/M 2024、O/N 2025 /43、/44）。

Section A 按点给分。MS p.3 的 "Social Science-Specific Marking Principles (for point-based marking)" 列出以下原则（转述；17 份 Paper 4 MS 都有这一节）：

- 措辞不同但意思清楚相同的答案给分，"unless the mark scheme requires a specific term"；MS 没写到但正确的例子或答案也给分。
- 只写出 key term 不给分，"unless that is all that is required"，要看出考生懂这个词。自相矛盾、两头都押的答案不给分；重复已得分的点（包括 "mirror statements"）不再给分。
- 拼写不扣分，但术语拼写必须能和易混的其他术语清楚区分。
- MS 里 `/` 或 "or" 分隔同一得分点的不同写法；`;`、bullet 或 `(1)` 分隔不同得分点；括号内容只是给阅卷人的说明，不写也能得分。
- 计算题：除非题目和 MS 注明需要过程，只写正确答案也得全分；用 MS 以外的正确方法，到达同等步骤给同等分；"own figure rule"：沿用前面算错的数字，只要方法正确完整，后续仍给全分。
- 个别小问有图形封顶。例：O/N 2025 /41 的 1(b) 写明 "Maximum 3 marks if no diagram"。

**Section B（微观）与 Section C（宏观）：essay。** SYL p.36 的要求：

- 每节两题选一，每题 20 分，"focusing mainly on microeconomics"／"macroeconomics"；
- "Section B and C questions are not divided into parts. Answers should show evidence of evaluation (AO3)."；
- "Candidates are encouraged to use clearly labelled diagrams to illustrate their answers, where appropriate."；
- 考纲提醒考生熟悉 "the assessment criteria in the levels-based mark scheme for Sections B and C"。考纲本身不印 levels 表，下表取自 MS。

**每篇 essay 的评分（17 份 Paper 4 MS 与 2023 specimen MS 完全相同）。** MS 在每题下写 "AO1 and AO2 out of 14 marks. AO3 out of 6 marks."：

| 表 | Level | 分数 | 描述要点（转述，引号内为原文短语） |
|---|---|---|---|
| Table A：AO1 Knowledge and understanding + AO2 Analysis（满分 14） | 3 | 11–14 | 相关概念的知识与理解 "detailed"，并有解释和适当例子；切中题目要求，"fully develops these explanations"；分析 "developed and detailed"，需要时准确使用图形与公式 "and these are fully explained"；组织清楚、有逻辑 |
| | 2 | 6–10 | 部分相关概念，解释与例子 "limited, over-generalised or contain inaccuracies"；只回应题目 "general theme"，"limited development"；分析大体准确但 "little detail"；图形与公式 "partially accurate or not fully explained" |
| | 1 | 1–5 | 少量相关知识点，"significant errors or omissions"；与题目关系不大；分析 "largely descriptive"；图形与公式可能有严重错误或缺失 |
| | 0 | 0 | No creditable response |
| Table B：AO3 Evaluation（满分 6） | 2 | 4–6 | "Provides a justified conclusion or judgement that addresses the specific requirements of the question"；评价 "developed, reasoned and well-supported" |
| | 1 | 1–3 | 结论或判断 "vague or general"；评价 "simple"，没有展开、缺少支撑 |
| | 0 | 0 | No creditable response |

阅卷方法（MS p.4 "Guidance on using levels-based mark schemes"，转述）：

- 先选最贴合的 level（best fit），再定分：作答 "convincingly" 符合该 level 的描述给最高分，"adequately" 符合给中间分，"just meets" 给最低分。
- 每题 MS 列出 "Indicative content"（"Responses may include"），这是有效思路的举例，不是必须写全的清单。

**按题加的封顶规则（每题都要读该题 MS）。** 2024–2025 年的 MS 常见以下几类：

- **缺图封顶**："Up to Level 2 only if no diagram."（M/J 2024 /41 Q3，用 indifference curve 分析 normal good 与 Giffen good）；"No diagram Max L2 8 marks."（M/J 2025 /42）；同类写法见 O/N 2024 /41、M/J 2025 /41、/43、/44，O/N 2025 /41、/43。
- **缺少规定的分析内容封顶**：例如 M/J 2025 /42 的一道劳动市场题写明，没有分析 productivity 提高的最高 L2 10 分，只分析完全或不完全劳动市场其中一种的最高 L2 8 分。
- **图的类型不对**：O/N 2025 /43 有一题写 "No diagram Max L3" 并注明 "Micro diagram not acceptable"，即宏观题用微观图不算。
- 这些封顶写的是 Table A 的 level（L2 = 6–10，L3 = 11–14），位置在 AO1/AO2 的 indicative content 下；AO3 的 6 分按 Table B 另评。MS 没有说缺图是否同时限制 AO3。

**Paper 4 的 AO3 分布（推算）。** 考纲给 Paper 4 的 AO3 权重是 30%，即约 18 分。两篇 essay 共 12 分 AO3（MS），所以 Section A 约有 6 分落在评价上，与"最后一问总带评价命令"一致。这是按权重推算的近似值，MS 没有逐小问标 AO。

**essay 的命令词。** 脚本粗略统计了 14 份 Paper 4 QP 的 56 道 essay：以 Evaluate 为主，其次是 Assess 与 Consider；Discuss、Justify 各有个别出现。脚本按题末 400 字符窗口计数，一题可能被重复计入。

### 2.5 Assessment objectives（SYL p.13，原文）

- **AO1 Knowledge and understanding**
  - Show knowledge of syllabus content, recalling facts, formulae and definitions.
  - Demonstrate understanding of syllabus content, giving appropriate explanations and examples.
  - Apply knowledge and understanding to economic information using written, numerical and diagrammatic forms.
- **AO2 Analysis**
  - Examine economic issues and relationships, using relevant economic concepts, theories and information.
  - Select, interpret and organise economic information in written, numerical and diagrammatic form.
  - Use economic information to recognise patterns, relationships, causes and effects.
  - Explain the impacts and consequences of changes in economic variables.
- **AO3 Evaluation**
  - Recognise assumptions and limitations of economic information and models.
  - Assess economic information and the strengths and weaknesses of arguments.
  - Recognise that some economic decisions involve consideration of factors such as priorities and value judgements.
  - Communicate reasoned judgements, conclusions and decisions, based on the arguments.

## 3. Command words（SYL p.37）

考纲原话："The use of the command word will relate to the subject context." 英文释义照录原文；中文是本登记的译述，不是官方译文。

| Command word | What it means（原文） | 中文 |
|---|---|---|
| Analyse | examine in detail to show meaning, identify elements and the relationship between them | 详细考察，说明含义，找出各组成要素及其相互关系 |
| Assess | make an informed judgement | 作出有依据的判断 |
| Calculate | work out from given facts, figures or information | 根据所给事实、数字或信息算出结果 |
| Comment | give an informed opinion | 给出有依据的看法 |
| Compare | identify/comment on similarities and/or differences | 指出或评论相同点和（或）不同点 |
| Consider | review and respond to given information | 审视所给信息并作出回应 |
| Define | give precise meaning | 给出精确含义 |
| Demonstrate | show how or give an example | 说明如何，或举例 |
| Describe | state the points of a topic / give characteristics and main features | 陈述要点，或给出特征与主要特点 |
| Discuss | write about issue(s) or topic(s) in depth in a structured way | 有条理地深入论述问题或主题 |
| Evaluate | judge or calculate the quality, importance, amount, or value of something | 判断或计算某事物的质量、重要性、数量或价值 |
| Explain | set out purposes or reasons / make the relationships between things clear / say why and/or how and support with relevant evidence | 说明目的或原因；理清事物之间的关系；说明为什么、怎样，并用相关证据支持 |
| Give | produce an answer from a given source or recall/memory | 从所给材料或记忆中给出答案 |
| Identify | name/select/recognise | 说出名称、选出或辨认 |
| Justify | support a case with evidence/argument | 用证据或论证支持一个观点 |
| Outline | set out the main points | 列出要点 |
| State | express in clear terms | 用清楚的措辞表述 |

**表外命令词。** Paper 4 Section A 还出现过 **Distinguish (between)**，它不在 p.37 的表里。例子：M/J 2024 /41 1(b)（absolute vs relative poverty，3 分）、F/M 2024 /42 1(c)(i)、O/N 2025 /43 1(b)(i)（equity vs equality）。M/J 2024 /41 的 MS 对两个概念各按定义要点给分。题干里也常见 "With the help of a diagram"、"With reference to the article"、"Use the information to …" 这类限定，它们规定了必须使用的工具或证据。

## 4. Key concepts（SYL p.5）

考纲为全科列出七个 key concepts，A Level 各主题的导语会点名其中几个（见 §5 各主题）：

- **Scarcity and choice**：资源稀缺而欲望无限，必须在竞争性用途间选择，选择有机会成本。
- **The margin and decision-making**：消费者、厂商、政府在边际上决策（例如厂商生产到额外一单位的收益等于其成本）；决策也可能基于事实、理论、有效性、优先次序与价值判断。
- **Equilibrium and disequilibrium**：单个市场与整体经济不断进出均衡，持续改变资源配置。
- **Time**：短期与长期条件不同，主体的反应依时间框架而异；有些决策是用现在的成本换未来的收益。
- **Efficiency and inefficiency**：市场与整体经济在使用稀缺资源时可以在不同方面有效或无效。
- **The role of government and the issues of equality and equity**：不受管制市场中的自由，与通过政府管制实现的更大社会平等与公平之间存在取舍。
- **Progress and development**：社会可以用货币衡量进步，也可以在生活水平、包容性与可持续性等更规范的意义上发展。

## 5. A Level 条目（topics 7–11，印刷 pp.24–34，原文逐字）

每条写出考纲编号、学习结果原文（英文逐字，含全部 bullet 与括注）和印刷页。〔 〕标签是本登记按原文措辞自动加的检索提示，不是考纲内容：〔计算〕＝原文含 calculation／calculate／formula(e)；〔图／模型〕＝原文点名曲线、矩阵、乘数或方程式模型；〔不要求〕＝原文写明 not required。条目跨页时写出 bullet 所在页。机读版见 `spec-items.json`（title 为条目主干，不含 bullet）。

### 7 The price system and the microeconomy (A Level)（p.24 起）

- 主题说明（p.24）：研究消费者与厂商的动机和行为，市场与参与者的效率、由此产生的市场失灵；原文："Both perfectly competitive and imperfect market structures will be analysed and appraised."
- Key concepts（原文）：scarcity and choice; the margin and decision-making; equilibrium and disequilibrium; efficiency and inefficiency; time

#### 7.1 Utility（p.24）

- **7.1.1** definition and calculation of total utility and marginal utility — p.24 〔计算〕
- **7.1.2** diminishing marginal utility — p.24
- **7.1.3** equi-marginal principle — p.24
- **7.1.4** derivation of an individual demand curve — p.24 〔图／模型〕
- **7.1.5** limitations of marginal utility theory and its assumptions of rational behaviour — p.24

#### 7.2 Indifference curves and budget lines（p.24）

- **7.2.1** meaning of an indifference curve and a budget line — p.24 〔图／模型〕
- **7.2.2** causes of a shift in the budget line — p.24
- **7.2.3** income, substitution and price effects for normal, inferior and Giffen goods — p.24
- **7.2.4** limitations of the model of indifference curves — p.24 〔图／模型〕

#### 7.3 Efficiency and market failure（p.24）

- **7.3.1** definitions of productive efficiency and allocative efficiency — p.24
- **7.3.2** conditions for productive efficiency and allocative efficiency — p.24
- **7.3.3** Pareto optimality — p.24
- **7.3.4** definition of dynamic efficiency — p.24
- **7.3.5** definition of market failure — p.24
- **7.3.6** reasons for market failure — p.24

#### 7.4 Private costs and benefits, externalities and social costs and benefits（p.24）

- **7.4.1** definition and calculation of social costs (SC) as the sum of private costs (PC) and external costs (EC), including marginal social costs (MSC), marginal private costs (MPC) and marginal external costs (MEC) — p.24 〔计算〕
- **7.4.2** definition and calculation of social benefits (SB) as the sum of private benefits (PB) and external benefits (EB), including marginal social benefits (MSB), marginal private benefits (MPB) and marginal external benefits (MEB) — p.24 〔计算〕
- **7.4.3** definition of positive externality and negative externality — p.24
- **7.4.4** positive and negative externalities of both consumption and production — p.24
- **7.4.5** deadweight welfare losses arising from positive and negative externalities — p.24
- **7.4.6** asymmetric information and moral hazard — p.24
- **7.4.7** use of costs and benefits in analysing decisions (knowledge of net present value is not required) — p.24 〔不要求〕

#### 7.5 Types of cost, revenue and profit, short-run and long-run production（p.25）

- **7.5.1** short-run production function: — p.25 〔计算〕
  - fixed and variable factors of production
  - definition and calculation of total product, average product and marginal product
  - law of diminishing returns (law of variable proportions)
- **7.5.2** short-run cost function: — p.25 〔计算〕〔图／模型〕
  - definition and calculation of fixed costs (FC) and variable costs (VC)
  - definition and calculation of total, average and marginal costs (TC, AC, MC), including average total cost (ATC), total and average fixed costs (TFC, AFC) and total and average variable costs (TVC, AVC)
  - explanation of shape of short-run average cost and marginal cost curves
- **7.5.3** long-run production function: — p.25
  - no fixed factors of production
  - returns to scale
- **7.5.4** long-run cost function: — p.25 〔图／模型〕
  - explanation of shape of long-run average cost curve
  - concept of minimum efficient scale
- **7.5.5** relationship between economies of scale and decreasing average costs — p.25
- **7.5.6** internal and external economies of scale — p.25
- **7.5.7** internal and external diseconomies of scale — p.25
- **7.5.8** definition and calculation of revenue: total, average and marginal revenue (TR, AR, MR) — p.25 〔计算〕
- **7.5.9** definition of normal, subnormal and supernormal profit — p.25
- **7.5.10** calculation of supernormal and subnormal profit — p.25 〔计算〕

#### 7.6 Different market structures（p.25）

- **7.6.1** perfect competition and imperfect competition: monopoly, monopolistic competition, oligopoly, natural monopoly — p.25
- **7.6.2** structure of the listed markets as explained by number of buyers and sellers, product differentiation, degree of freedom of entry and availability of information — p.25
- **7.6.3** barriers to entry and exit: — p.25
  - legal barriers
  - market barriers
  - cost barriers
  - physical barriers
- **7.6.4** performance of firms in different market structures: — p.26 〔图／模型〕
  - revenues and revenue curves
  - output in the short run and the long run
  - profits in the short run and the long run
  - shutdown price in the short run and the long run
  - derivation of a firm’s supply curve in a perfectly competitive market
  - efficiency and X-inefficiency in the short run and the long run
  - contestable markets: features and implications
  - price competition and non-price competition
  - collusion and the Prisoner’s Dilemma in oligopolistic markets, including a two-player pay-off matrix
- **7.6.5** definition and calculation of the concentration ratio — p.26 〔计算〕

#### 7.7 Growth and survival of firms（p.26）

- **7.7.1** reasons for different sizes of firms — p.26
- **7.7.2** internal growth of firms: organic growth and diversification — p.26
- **7.7.3** external growth of firms – integration (mergers and takeovers): — p.26
  - methods of integration:
    - horizontal
    - vertical (forwards and backwards)
    - conglomerate
  - reasons for integration
  - consequences of integration
- **7.7.4** cartels: — p.26
  - conditions for an effective cartel
  - consequences of a cartel
- **7.7.5** principal–agent problem arising from differing objectives of shareholders/owners and managers — p.26

#### 7.8 Differing objectives and policies of firms（p.27）

- **7.8.1** traditional profit-maximising objective of firms — p.27
- **7.8.2** an understanding of other objectives of firms: — p.27
  - survival
  - profit satisficing
  - sales maximisation
  - revenue maximisation
- **7.8.3** price discrimination – first, second and third degree: — p.27
  - conditions for effective price discrimination
  - consequences of price discrimination
- **7.8.4** other pricing policies: — p.27
  - limit pricing
  - predatory pricing
  - price leadership
- **7.8.5** relationship between price elasticity of demand and a firm’s revenue: — p.27 〔图／模型〕
  - in a normal downward sloping demand curve
  - in a kinked demand curve

### 8 Government microeconomic intervention (A Level)（p.27 起）

- 主题说明（p.27）：评价政府应对不同形式市场失灵的政策选项及其利弊，government failure 的成因与对效率的影响；收入与财富分配（equality、equity、efficiency、poverty）；完全竞争与不完全竞争条件下的劳动市场及政府干预。
- Key concepts（原文）：the margin and decision-making; equilibrium and disequilibrium; efficiency and inefficiency; time; the role of government and the issues of equality and equity

#### 8.1 Government policies to achieve efficient resource allocation and correct market failure（p.27）

- **8.1.1** application and effectiveness of measures to tackle different forms of market failure: — p.27
  - specific and ad valorem indirect taxes
  - subsidies
  - price controls
  - production quotas
  - prohibitions and licences
  - regulation and deregulation
  - direct provision
  - pollution permits
  - property rights
  - nationalisation and privatisation
  - provision of information
  - behavioural insights and ‘nudge’ theory
- **8.1.2** government failure in microeconomic intervention: — p.28
  - definition of government failure
  - causes of government failure
  - consequences of government failure

#### 8.2 Equity and redistribution of income and wealth（p.28）

- **8.2.1** difference between equity and equality — p.28
- **8.2.2** difference between equity and efficiency — p.28
- **8.2.3** distinction between absolute poverty and relative poverty — p.28
- **8.2.4** the poverty trap — p.28
- **8.2.5** policies towards equity and equality, for example: — p.28
  - negative income tax
  - universal benefits and means-tested benefits
  - universal basic income

#### 8.3 Labour market forces and government intervention（p.28）

- **8.3.1** demand for labour as a derived demand — p.28
- **8.3.2** factors affecting demand for labour in a firm or an occupation — p.28
- **8.3.3** causes of shifts in and movement along the demand curve for labour in a firm or an occupation — p.28 〔图／模型〕
- **8.3.4** marginal revenue product (MRP) theory: — p.28 〔计算〕
  - definition and calculation of marginal revenue product
  - derivation of an individual firm’s demand for labour using marginal revenue product
- **8.3.5** factors affecting the supply of labour to a firm or to an occupation: — p.28
  - wage and non-wage factors
- **8.3.6** causes of shifts in and movement along the supply curve of labour to a firm or an occupation — p.28 〔图／模型〕
- **8.3.7** wage determination in perfect markets: — p.28
  - equilibrium wage rate and employment in a labour market
- **8.3.8** wage determination in imperfect markets: — p.28
  - influence of trade unions on wage determination and employment in a labour market
  - influence of government on wage determination and employment in a labour market using a national minimum wage
  - influence of monopsony employers on wage determination and employment in a labour market
- **8.3.9** determination of wage differentials by labour market forces — p.28
- **8.3.10** transfer earnings and economic rent: — p.28
  - definition of transfer earnings
  - definition of economic rent
  - factors affecting transfer earnings and economic rent in an occupation

### 9 The macroeconomy (A Level)（p.29 起）

- 主题说明（p.29）：AD 的决定因素、multiplier process、money and banking；经济的周期性及其对主要宏观指标（economic growth, low unemployment, price stability and balance of payments stability）的影响；增长的 sustainability 与 inclusivity。
- Key concepts（原文）：the margin and decision-making; time; equilibrium and disequilibrium; progress and development

#### 9.1 The circular flow of income（p.29）

- **9.1.1** the multiplier process: — p.29 〔计算〕〔图／模型〕
  - definition of the multiplier
  - formulae for and calculation of multiplier in a closed and open economy, with and without a government sector
  - calculation of:
    - average and marginal propensities to save (aps and mps)
    - average and marginal propensities to consume (apc and mpc)
    - average and marginal propensities to import (apm and mpm)
    - average and marginal rates of tax (art and mrt)
  - national income determination using AD and income approach with the multiplier process
  - calculation of effect of changing AD on national income using the multiplier
- **9.1.2** components of Aggregate Demand (AD) and their determinants: — p.29
  - consumption function: autonomous and induced consumer expenditure
  - savings function: autonomous and induced savings
  - autonomous and induced investment; the accelerator
  - government spending
  - net exports (exports minus imports)
- **9.1.3** full employment level of national income and equilibrium level of national income: — p.29
  - inflationary and deflationary gaps

#### 9.2 Economic growth and sustainability（p.30）

- **9.2.1** actual growth versus potential growth in national output — p.30
- **9.2.2** positive and negative output gaps — p.30
- **9.2.3** business (trade) cycle: — p.30
  - phases of the cycle
  - causes of the cycle
  - role of automatic stabilisers
- **9.2.4** policies to promote economic growth and their effectiveness — p.30
- **9.2.5** inclusive economic growth: — p.30
  - definition of inclusive economic growth
  - impact of economic growth on equity and equality
  - policies to promote inclusive growth
- **9.2.6** sustainable economic growth: — p.30
  - definition of sustainable economic growth
  - using and conserving resources
  - impact of economic growth on the environment and climate change
  - policies to mitigate the impact of economic growth on the environment and climate change

#### 9.3 Employment/unemployment（p.30）

- **9.3.1** definition of full employment — p.30
- **9.3.2** equilibrium and disequilibrium unemployment (including hysteresis) — p.30
- **9.3.3** voluntary and involuntary unemployment — p.30
- **9.3.4** natural rate of unemployment: — p.30
  - definition
  - determinants
  - policy implications
- **9.3.5** patterns and trends in (un)employment — p.30
- **9.3.6** mobility of labour: — p.30
  - forms of labour mobility: geographical and occupational
  - factors affecting labour mobility
- **9.3.7** policies to reduce unemployment and their effectiveness — p.30

#### 9.4 Money and banking（p.31）

- **9.4.1** definition, functions and characteristics of money — p.31
- **9.4.2** definition of money supply — p.31
- **9.4.3** quantity theory of money (MV = PT) — p.31 〔图／模型〕
- **9.4.4** functions of commercial banks: — p.31
  - providing deposit accounts (demand deposit account, savings account)
  - lending money (overdrafts, loans)
  - holding or providing cash, securities, loans, deposits, equity
  - reserve ratio and capital ratio
  - objectives of commercial banks: liquidity, security, profitability
- **9.4.5** causes of changes in the money supply in an open economy: — p.31 〔图／模型〕
  - commercial banks as sources of credit creation and the bank credit multiplier
  - role of a central bank
  - government deficit financing
  - quantitative easing
  - changes in the balance of payments
- **9.4.6** policies to reduce inflation and their effectiveness — p.31
- **9.4.7** demand for money: liquidity preference theory — p.31
- **9.4.8** interest rate determination: loanable funds theory and Keynesian theory — p.31

### 10 Government macroeconomic intervention (A Level)（p.31 起）

- 主题说明（p.31）：政府管理宏观经济、实现所选目标时遇到的困难；原文点名 "Important trade-offs like the Phillips curve" 及其他 policy conflicts；评价不同宏观政策对不同目标的有效性；macroeconomic government failure。
- Key concepts（原文）：scarcity and choice; the margin and decision-making; equilibrium and disequilibrium; efficiency and inefficiency; time; progress and development

#### 10.1 Government macroeconomic policy objectives（p.31）

- **10.1.1** objectives in terms of inflation, balance of payments, unemployment, growth, development, sustainability and redistribution of income and wealth — p.31

#### 10.2 Links between macroeconomic problems and their interrelatedness（p.31）

- **10.2.1** relationship between the internal value of money and the external value of money — p.31
- **10.2.2** relationship between the balance of payments and inflation — p.31
- **10.2.3** relationship between growth and inflation — p.31
- **10.2.4** relationship between growth and the balance of payments — p.31
- **10.2.5** relationship between inflation and unemployment: — p.31 〔图／模型〕
  - traditional Phillips curve
  - expectations-augmented Phillips curve (short- and long-run Phillips curve)

#### 10.3 Effectiveness of policy options to meet all macroeconomic objectives（p.32）

- **10.3.1** effectiveness of different policies in relation to different macroeconomic objectives: — p.32 〔图／模型〕
  - fiscal policy including Laffer curve analysis
  - monetary policy
  - supply-side policy including market-based and interventionist policies
  - exchange rate policy
  - international trade policy
- **10.3.2** problems and conflicts arising from the outcome of these policies — p.32
- **10.3.3** existence of government failure in macroeconomic policies — p.32

### 11 International economic issues (A Level)（p.32 起）

- 主题说明（p.32）：完整的 balance of payments；fixed and managed exchange rate systems 的优缺点；经济发展过程、不同发展水平国家的特征、高收入与低收入国家的关系；living standards、international aid、multinational companies、external debt、globalisation。
- Key concepts（原文）：progress and development; scarcity and choice; time

#### 11.1 Policies to correct disequilibrium in the balance of payments（p.32）

- **11.1.1** components of the balance of payments accounts: current account, financial account and capital account — p.32
- **11.1.2** effect of fiscal, monetary, supply-side, protectionist and exchange rate policies on the balance of payments — p.32
- **11.1.3** difference between expenditure-switching and expenditure-reducing policies — p.32

#### 11.2 Exchange rates（p.32）

- **11.2.1** measurement of exchange rates: — p.32
  - distinction between nominal and real exchange rates
  - trade-weighted exchange rates
- **11.2.2** determination of exchange rates under fixed and managed systems — p.32
- **11.2.3** distinction between revaluation and devaluation of a fixed exchange rate — p.32
- **11.2.4** changes in the exchange rate under different exchange rate systems — p.32
- **11.2.5** the effects of changing exchange rates on the external economy using Marshall-Lerner and J curve analysis — p.32 〔图／模型〕

#### 11.3 Economic development（p.33）

- **11.3.1** classification of economies in terms of their level of development — p.33
- **11.3.2** classification of economies in terms of their level of national income — p.33
- **11.3.3** indicators of living standards and economic development: — p.33 〔图／模型〕
  - monetary indicators including real per capita national income statistics (GDP, GNI, NNI) and purchasing power parity
  - issues of comparison using monetary indicators
  - non-monetary indicators
  - composite indicators:
    - Human Development Index (HDI)
    - Measure of Economic Welfare (MEW)
    - Multidimensional Poverty Index (MPI)
  - the Kuznets curve
- **11.3.4** comparison of economic growth rates and living standards: — p.33
  - over time
  - between countries

#### 11.4 Characteristics of countries at different levels of development（p.33）

- **11.4.1** population growth and structure: — p.33
  - measurement and causes of changes in birth rate, death rate, infant mortality and net migration
  - optimum population
  - level of urbanisation
- **11.4.2** income distribution: — p.33 〔计算〕〔图／模型〕
  - calculation of Gini coefficient and Lorenz curve analysis
- **11.4.3** economic structure: — p.33
  - employment composition: primary, secondary and tertiary sectors
  - pattern of trade at different levels of development

#### 11.5 Relationship between countries at different levels of development（p.34）

- **11.5.1** international aid: — p.34
  - forms of aid
  - reasons for giving aid
  - effects of aid
  - importance of aid
- **11.5.2** trade and investment — p.34
- **11.5.3** role of multinational companies (MNCs): — p.34
  - definition of MNC
  - activities of MNCs
  - consequences of MNCs
- **11.5.4** Foreign Direct Investment (FDI): — p.34
  - definition of FDI
  - consequences of FDI
- **11.5.5** external debt: — p.34
  - causes of debt
  - consequences of debt
- **11.5.6** role of the International Monetary Fund (IMF) — p.34
- **11.5.7** role of the World Bank — p.34

#### 11.6 Globalisation（p.34）

- **11.6.1** meaning of globalisation and its causes and consequences — p.34
- **11.6.2** distinction between a free trade area, a customs union, a monetary union and full economic union — p.34
- **11.6.3** trade creation and trade diversion — p.34

## 6. AS 条目简表（topics 1–6，印刷 pp.15–23；A Level 默认已掌握）

考纲 p.15："The AS Level content is assumed knowledge for A Level Paper 3 and Paper 4." 下面只列编号与条目主干（原文），bullet 省略；原文中带 "not required" 的限定照录在方括号里，因为它们决定 AS 与 A Level 的分界（见 §7）。

**1 Basic economic ideas and resource allocation (AS Level)**（p.15 起）

- **1.1 Scarcity, choice and opportunity cost**（p.15）：1.1.1 fundamental economic problem of scarcity；1.1.2 need to make choices at all levels (individuals, firms, governments)；1.1.3 nature and definition of opportunity cost, arising from choices；1.1.4 basic questions of resource allocation
- **1.2 Economic methodology**（p.15）：1.2.1 economics as a social science；1.2.2 positive and normative statements (the distinction between facts and value judgements)；1.2.3 meaning of the term ceteris paribus；1.2.4 importance of the time period (short run, long run, very long run)
- **1.3 Factors of production**（p.16）：1.3.1 nature and definition of factors of production: land, labour, capital and enterprise；1.3.2 difference between human capital and physical capital；1.3.3 rewards to the factors of production；1.3.4 division of labour and specialisation；1.3.5 role of the entrepreneur in contemporary economies: risk and organisation of the other factors of production
- **1.4 Resource allocation in different economic systems**（p.16）：1.4.1 decision-making in market, planned and mixed economies；1.4.2 resource allocation in these economic systems
- **1.5 Production possibility curves**（p.16）：1.5.1 nature and meaning of a production possibility curve (PPC)；1.5.2 shape of the PPC: constant and increasing opportunity costs；1.5.3 causes and consequences of shifts in a PPC；1.5.4 significance of a position within a PPC
- **1.6 Classification of goods and services**（p.16）：1.6.1 nature and definition of free goods and private goods (economic goods)；1.6.2 nature and definition of public goods；1.6.3 nature and definition of merit goods: under-consumption as a result of imperfect information in the market；1.6.4 nature and definition of demerit goods: over-consumption as a result of imperfect information in the market

**2 The price system and the microeconomy (AS Level)**（p.17 起）

- **2.1 Demand and supply curves**（p.17）：2.1.1 effective demand；2.1.2 individual and market demand and supply；2.1.3 determinants of demand；2.1.4 determinants of supply；2.1.5 causes of a shift in the demand curve (D)；2.1.6 causes of a shift in the supply curve (S)；2.1.7 distinction between the shift in the demand or supply curve and the movement along these curves
- **2.2 Price elasticity, income elasticity and cross elasticity of demand**（p.17）：2.2.1 definition of price elasticity, income elasticity and cross elasticity of demand (PED, YED, XED)；2.2.2 formulae for and calculation of price elasticity, income elasticity and cross elasticity of demand；2.2.3 significance of relative percentage changes, the size and sign of the coefficient of；2.2.4 descriptions of elasticity values: perfectly elastic, (highly) elastic, unitary elasticity, (highly) inelastic, perfectly inelastic；2.2.5 variation in price elasticity of demand along the length of a straight-line demand curve；2.2.6 factors affecting；2.2.7 relationship between price elasticity of demand and total expenditure on a product；2.2.8 implications for decision-making of price elasticity, income elasticity and cross elasticity of demand
- **2.3 Price elasticity of supply**（p.18）：2.3.1 definition of price elasticity of supply (PES)；2.3.2 formula for and calculation of price elasticity of supply；2.3.3 significance of relative percentage changes, the size and sign of the coefficient of price elasticity of supply；2.3.4 factors affecting price elasticity of supply；2.3.5 implications for speed and ease with which firms react to changed market conditions
- **2.4 The interaction of demand and supply**（p.18）：2.4.1 definition of market equilibrium and disequilibrium；2.4.2 effects of shifts in demand and supply curves on equilibrium price and quantity；2.4.3 relationships between different markets；2.4.4 functions of price in resource allocation; rationing, signalling (transmission of preferences) and incentivising
- **2.5 Consumer and producer surplus**（p.18）：2.5.1 meaning and significance of consumer surplus；2.5.2 meaning and significance of producer surplus；2.5.3 causes of changes in consumer and producer surplus；2.5.4 significance of price elasticity of demand and of supply in determining the extent of these changes

**3 Government microeconomy intervention (AS Level)**（p.18 起）

- **3.1 Reasons for government intervention in markets**（p.18）：3.1.1 addressing the non-provision of public goods；3.1.2 addressing the over-consumption of demerit goods and the under-consumption of merit goods；3.1.3 controlling prices in markets
- **3.2 Methods and effects of government intervention in markets**（p.19）：3.2.1 impact and incidence of specific indirect taxes；3.2.2 impact and incidence of subsidies；3.2.3 direct provision of goods and services；3.2.4 maximum and minimum prices；3.2.5 buffer stock schemes；3.2.6 provision of information
- **3.3 Addressing income and wealth inequality**（p.19）：3.3.1 difference between income as a flow concept and wealth as a stock concept；3.3.2 measuring income and wealth inequality [Gini coefficient (calculation not required)]；3.3.3 economic reasons for inequality of income and wealth；3.3.4 policies to redistribute income and wealth

**4 The Macroeconomy (AS Level)**（p.19 起）

- **4.1 National income statistics**（p.19）：4.1.1 meaning of national income；4.1.2 measurement of national income；4.1.3 adjustment of measures from market prices to basic prices；4.1.4 adjustment of measures from gross values to net values
- **4.2 Introduction to the circular flow of income**（p.20）：4.2.1 circular flow of income in a closed economy and an open economy: the flow of income between households, firms and government and the international economy；4.2.2 injections and leakages (multiplier not required)；4.2.3 equilibrium and disequilibrium (marginal and average propensities not required)
- **4.3 Aggregate Demand and Aggregate Supply analysis**（p.20）：4.3.1 definition of Aggregate Demand (AD)；4.3.2 components of AD and their meanings: AD = C + I + G + (X – M)；4.3.3 determinants of AD (detailed knowledge of the components of AD is not required)；4.3.4 shape of the AD curve (downward sloping)；4.3.5 causes of a shift in the AD curve；4.3.6 definition of Aggregate Supply (AS)；4.3.7 determinants of AS；4.3.8 shape of the AS curve in the short run (SRAS, upward sloping line or sweeping curve) and the long run (LRAS, either a vertical line or in three sections – highly elastic, upward sloping, vertical)；4.3.9 causes of a shift in the AS curve in the short run (SRAS) and in the long run (LRAS)；4.3.10 distinction between a movement along and a shift in AD and AS；4.3.11 establishment of equilibrium in the AD/AS model and the determination of the level of real output, the price level and employment；4.3.12 effects of shifts in the AD curve and the AS curve on the level of real output, the price level and employment
- **4.4 Economic growth**（p.20）：4.4.1 meaning of economic growth；4.4.2 measurement of economic growth；4.4.3 distinction between growth in nominal GDP and real GDP；4.4.4 causes of economic growth；4.4.5 consequences of economic growth
- **4.5 Unemployment**（p.20）：4.5.1 meaning of unemployment；4.5.2 measures of unemployment, with reference to possible difficulties in measurement；4.5.3 causes and types of unemployment: frictional, structural, cyclical, seasonal and technological；4.5.4 consequences of unemployment
- **4.6 Price stability**（p.21）：4.6.1 definition of inflation, deflation and disinflation；4.6.2 measurement of changes in the price level；4.6.3 distinction between money values (nominal) and real data；4.6.4 causes of inflation: cost-push and demand-pull inflation；4.6.5 consequences of inflation

**5 Government macroeconomic intervention (AS Level)**（p.21 起）

- **5.1 Government macroeconomic policy objectives**（p.21）：5.1.1 use of government policy to achieve macroeconomic objectives: price stability, low unemployment, economic growth (policy conflicts and trade-offs are not required)
- **5.2 Fiscal policy**（p.21）：5.2.1 meaning of government budget；5.2.2 distinction between a government budget deficit and a government budget surplus；5.2.3 meaning and significance of the national debt；5.2.4 taxation；5.2.5 government spending；5.2.6 distinction between expansionary and contractionary fiscal policy；5.2.7 AD/AS analysis of the impact of expansionary and contractionary fiscal policy on the equilibrium level of national income and the level of real output, the price level and employment
- **5.3 Monetary policy**（p.22）：5.3.1 definition of monetary policy；5.3.2 tools of monetary policy: interest rates, money supply and credit regulations；5.3.3 distinction between expansionary and contractionary monetary policy；5.3.4 AD/AS analysis of the impact of expansionary and contractionary monetary policy on the equilibrium national income and the level of real output, the price level and employment
- **5.4 Supply-side policy**（p.22）：5.4.1 meaning of supply-side policy, in terms of its effect on LRAS curves；5.4.2 objectives of supply-side policy: increasing productivity and productive capacity；5.4.3 tools of supply-side policy, for example training, infrastructure development, support for technological improvement；5.4.4 AD/AS analysis of the impact of supply-side policy on the equilibrium national income and the level of real output, the price level and employment

**6 International economic issues (AS Level)**（p.22 起）

- **6.1 The reasons for international trade**（p.22）：6.1.1 distinction between absolute and comparative advantage；6.1.2 benefits of specialisation and free trade (trade liberalisation), including the trading possibility curve；6.1.3 exports, imports and the terms of trade；6.1.4 limitations of the theories of absolute and comparative advantage
- **6.2 Protectionism**（p.22）：6.2.1 meaning of protectionism in the context of international trade；6.2.2 different tools of protection and their impact；6.2.3 arguments for and against protectionism
- **6.3 Current account of the balance of payments**（p.23）：6.3.1 components of the current account of the balance of payments；6.3.2 calculation of；6.3.3 causes of imbalances in the current account of the balance of payments；6.3.4 consequences of imbalances in the current account of the balance of payments for the domestic and external economy
- **6.4 Exchange rates**（p.23）：6.4.1 definition of exchange rate；6.4.2 determination of a floating exchange rate；6.4.3 distinction between depreciation and appreciation of a floating exchange rate；6.4.4 causes of changes in a floating exchange rate: demand and supply of the currency；6.4.5 AD/AS analysis of the impact of exchange rate changes on the domestic economy’s equilibrium national income and the level of real output, the price level and employment
- **6.5 Policies to correct imbalances in the current account of the balance of payments**（p.23）：6.5.1 government policy objective of stability of the current account；6.5.2 effect of fiscal, monetary, supply-side and protectionist policies on the current account

## 7. AS 与 A Level 的分界

同一话题在 AS 与 A Level 各有条目时，A Level 卷（Paper 3／4）会在 AS 的基础上加深。下表全部取自考纲原文的条目措辞，用于判断某个知识点属于"先修（AS）"还是"本阶段（A2）"。

| 话题 | AS（Paper 1／2 的直接考点；A2 的先修） | A Level（Paper 3／4） |
|---|---|---|
| 需求与消费者 | 2.1 demand and supply curves；2.2 PED／YED／XED（p.17） | 7.1 utility、equi-marginal principle、"derivation of an individual demand curve"；7.2 indifference curves、budget line、income／substitution／price effects for normal, inferior and Giffen goods（p.24） |
| 效率 | 2.5 consumer and producer surplus（p.18） | 7.3 productive／allocative／dynamic efficiency、Pareto optimality、market failure（p.24）；7.4.5 deadweight welfare losses |
| 信息问题 | 1.6.3／1.6.4 merit／demerit goods："imperfect information in the market"（p.16） | 7.4.6 asymmetric information and moral hazard（p.24） |
| 外部性 | AS 没有单独的 externality 条目；3.1.2 只写 demerit／merit goods 的过度与不足消费（p.18） | 7.4.1–7.4.5 SC = PC + EC、MSC／MPC／MEC、MSB／MPB／MEB、positive／negative externalities of consumption and production（p.24） |
| 成本、收益与市场结构 | AS 没有；1.3.4 只有 division of labour and specialisation（p.16） | 7.5 costs, revenue, profit；7.6 market structures；7.7 growth of firms；7.8 objectives and pricing（pp.25–27） |
| 微观干预工具 | 3.2 specific indirect taxes、subsidies、direct provision、maximum and minimum prices、buffer stock schemes、provision of information（p.19） | 8.1.1 把 AS 的工具（taxes、subsidies、direct provision、price controls、provision of information）放到市场失灵情境下评价有效性，并另加 ad valorem taxes、production quotas、prohibitions and licences、regulation and deregulation、pollution permits、property rights、nationalisation and privatisation、"behavioural insights and ‘nudge’ theory"；8.1.2 government failure（pp.27–28） |
| 不平等的测量 | 3.3.2 "Gini coefficient (calculation not required)"（p.19） | 11.4.2 "calculation of Gini coefficient and Lorenz curve analysis"（p.33） |
| 再分配政策 | 3.3.4 minimum wage、transfer payments、progressive income taxes, inheritance and capital taxes、state provision（p.19） | 8.2.5 negative income tax、universal and means-tested benefits、universal basic income；8.2.3 absolute／relative poverty；8.2.4 poverty trap（p.28） |
| 劳动市场 | 1.3.3 rewards to the factors of production（p.16）；2.4.3 derived demand（p.18） | 8.3 MRP theory、wage determination in perfect and imperfect markets（trade unions、national minimum wage、monopsony）、wage differentials、transfer earnings and economic rent（p.28） |
| 循环流与乘数 | 4.2.2 "injections and leakages (multiplier not required)"；4.2.3 "(marginal and average propensities not required)"（p.20） | 9.1.1 multiplier 的公式与计算、aps／mps、apc／mpc、apm／mpm、art／mrt；9.1.3 inflationary and deflationary gaps（p.29） |
| AD 的组成 | 4.3.3 "determinants of AD (detailed knowledge of the components of AD is not required)"（p.20） | 9.1.2 consumption function、savings function、autonomous and induced investment、"the accelerator"（p.29） |
| 增长 | 4.4 meaning, measurement, causes, consequences（p.20） | 9.2 actual vs potential growth、output gaps、business (trade) cycle、automatic stabilisers、inclusive and sustainable growth（p.30） |
| 失业 | 4.5 measures, types（frictional, structural, cyclical, seasonal, technological）, consequences（p.20） | 9.3 full employment、equilibrium／disequilibrium unemployment（hysteresis）、voluntary／involuntary、natural rate、labour mobility、policies（p.30） |
| 通胀与货币 | 4.6 inflation, CPI, cost-push／demand-pull（p.21）；5.3 monetary policy tools（p.22） | 9.4 money and banking、"quantity theory of money (MV = PT)"、credit creation、quantitative easing、liquidity preference、loanable funds；9.4.6 policies to reduce inflation（p.31） |
| 宏观目标与冲突 | 5.1.1 price stability、low unemployment、economic growth，"(policy conflicts and trade-offs are not required)"（p.21） | 10.1.1 另加 balance of payments、development、sustainability、redistribution；10.2 目标之间的关系与 Phillips curve；10.3.2 policy conflicts；10.3.3 macro government failure（pp.31–32） |
| 宏观政策 | 5.2–5.4 fiscal、monetary、supply-side policy 的 AD/AS 分析（pp.21–22） | 10.3.1 effectiveness：fiscal policy "including Laffer curve analysis"、monetary、supply-side "including market-based and interventionist policies"、exchange rate policy、international trade policy（p.32） |
| 国际收支 | 6.3 只有 current account；6.5.2 fiscal、monetary、supply-side、protectionist policies 对 current account 的影响（p.23） | 11.1.1 current, financial and capital accounts；11.1.2 加上 exchange rate policies；11.1.3 expenditure-switching vs expenditure-reducing（p.32） |
| 汇率 | 6.4 只有 floating exchange rate：决定、depreciation／appreciation、AD/AS 影响（p.23） | 11.2 nominal vs real、trade-weighted、fixed and managed systems、revaluation／devaluation、Marshall-Lerner and J curve（p.32） |
| 贸易 | 6.1 absolute／comparative advantage、terms of trade；6.2 protectionism（p.22） | 11.5.2 trade and investment；11.6 globalisation、free trade area／customs union／monetary union／full economic union、trade creation and trade diversion（p.34） |
| 发展 | AS 没有 | 11.3 development indicators（HDI、MEW、MPI、Kuznets curve）；11.4 population, income distribution, economic structure；11.5 aid, MNCs, FDI, external debt, IMF, World Bank（pp.33–34） |

**A Level 部分唯一的明文排除：** 7.4.7 "knowledge of net present value is not required"（p.24）。

## 8. 缺口与待查

| 编号 | 缺口 | 影响 | 下一步 |
|---|---|---|---|
| G1 | 2023–2025 版考纲（`595463-2023-2025-syllabus.pdf`）与 `633788-2023-2025-syllabus-update.pdf` 未读；条目编号与措辞没有逐条对比 | F/M 2023–O/N 2025 的真题按 SYL V2 编号映射，依据只是官方"no significant changes which affect teaching"等两句说明 | Drive 或可达镜像出现该文件时，逐条对比 topics 7–11，并在本文件记录差异 |
| G2 | "2029 Syllabus"只有搜索摘要，文件号与内容未知 | 2029 年及以后考试的范围不能用本文件 | 为 2029 年考试制卡前先取得并通读该文件 |
| G3 | Version 1（2023 年 9 月，推断）未读 | 只影响版本沿革；V2 声明只改了 p.38 的网址 | 不急 |
| G4 | 考纲不印 Paper 4 的 levels 表；本文件的 Table A／B 取自 MS | 已核 17 份 Paper 4 MS（F/M 2023–O/N 2025）与 2023 specimen MS，完全相同 | 新考季 MS 出来后复核一次 |
| G5 | Paper 3 与 Section A 的 AO 逐题分配不公开；§2.3、§2.4 的 AO3 份额是按权重推算的近似值 | 只能作为分配复习时间的参考 | 无官方来源可补 |
| G6 | F/M 2026、M/J 2026 及以后考季的 QP／MS 本环境不可达（`versions.md` §2.5） | 考法统计只到 O/N 2025 | 定期在 Drive 检索 `9708_m26`、`9708_s26`、`9708_w26`；缺卷以 `python scripts/exam_index.py 9708 --gaps` 为准 |
