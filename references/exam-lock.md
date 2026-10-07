# 锁定考试：从板书精确到考试局、资格、单元与版本

制卡范围由“这场考试的这一份考纲”决定。板书里的课程名（“ALEVEL-高数”“英联邦学科”）只是弱线索；锁定要落到**考试局 + 资格 + 单元／试卷代码 + 考纲版本 + 目标考季**，并写出排除了哪些近似考试。结果写进牌组 JSON 的 `exam`（字段见 [deck-json.md](deck-json.md)）。

## 证据分级

| 级别 | 含义 | 例子 |
|---|---|---|
| A 直接证据 | 材料上印着的考试局与单元代码、封面、MS 的 Publications Code；用户或老师明说的考试与考季 | `WMA14/01A`、`9708/41/O/N/24`、“P4 mock，明年 1 月考” |
| B 强证据 | 版式指纹，加上**两条以上互相独立的排他知识点** | `(Total for Question n is m marks)` ＋ `r = a + λb` ＋ improper partial fractions |
| C 弱证据 | 课程名、机构标签、老师口头术语、单个非排他知识点 | “EDX-IAL”“高数” |

只有 A 级证据或 B 级证据能锁定；只有 C 级时继续取证。

## 步骤

1. **抽线索**：读全部页眉页脚、封面、题末分值写法、条码、文件名和课程标题，列出板书出现的全部知识点。`python scripts/exam_fingerprint.py board.pdf` 会对 PDF／图片做 OCR 并列出版式指纹与排他知识点提示；手写内容仍要人眼读。
2. **定考试局**：有 A 级证据即定；否则看版式指纹（下表）。
3. **定资格与单元**：把每个知识点映射到候选考纲的条目号与印刷页码。候选考纲覆盖全部知识点才保留；有两个以上知识点找不到对应条目（且不属于老师明显的拓展或先修）就排除。优先比较排他点。
4. **定版本**：先确定目标考季（板书日期、用户计划、老师说明；不知道时取下一个可报考季并记为假设）。CIE 看封面“Use this syllabus for exams in …”与 Version；Pearson 看 Issue 号、ISBN 与 Summary of changes（2013 旧 IAL 数学考纲也有 “Issue 3”，只看 Issue 号会混淆）。
5. **多候选仍并存**：先查用户 Google Drive、已有牌组和报名材料。候选差异不影响本批内容时，按更严格的一方制作并写明。差异会改变范围或深度时：开工前用户在场，就用选项问一次（“A) Pearson IAL WMA14，2027 年 1 月　B) CIE 9709 Paper 3，2027 年 6 月？”）；在要求一次做完的任务里，按证据最强的候选制作，`session_assumed` 或 `evidence` 写明假设，交付说明第一行写出另一候选会改变哪些卡。
6. **定报考结构**：这批内容会出现在哪些试卷、哪种卷型（9708 的 7.4／8.1 同时出现在 Paper 3 选择题与 Paper 4 essay；分段报考的学生还可能考 AS Paper 2 的 8＋12 分两问 essay）。写进 `exam.papers`，每种卷型分别标定（[coverage-ledger.md](coverage-ledger.md) §3）。
7. **题目溯源**：板书上的每道印刷题都去找官方出处——Drive 全文检索（`fullText contains '…题干里一段独特的话…'`）、本地真题 `pdftotext` 后 `grep`、Edexcel-Finder 一类的题干索引只作指针。找到就写 `board[i].source_paper`，并读该卷 MS 与 ER；排除过的考季也记下（“已排除 June 2025 /01、/01A、October 2025”），下次不重复找。
8. **记录**：`exam.identified_by` 写 `paper-code`／`exclusive-content`／`user`；`evidence` 写每条证据及其级别；用排他内容锁定时 `ruled_out` 写每个近似考试与排除它的证据。

## 版式指纹

| 考试局 | 指纹 |
|---|---|
| Pearson Edexcel（IAL 与 UK GCE） | 题末 `(Total for Question 9 is 12 marks)`；末页 `TOTAL FOR PAPER IS 75 MARKS`；封面 `Paper reference WMA14/01`、逐页条码 `*P74881A0132*`（P 号＋页码＋总页数）；区域卷 `/01A`；新式答题册 `Write the answer to Question 1 on these 2 pages`；阅卷扫描叠加的 `Q01B / Q01M / Q01A1` 分点栏 |
| Cambridge International | 页眉 `9708/41/O/N/24`（第二位数字为时区变体）；`© UCLES 2024`；`This document has 4 pages.`；分值 `[4]`，理科结构题常见 `[Total: 8]`；MS 页眉 `Cambridge International AS & A Level – Mark Scheme PUBLISHED` |
| AQA | 文件码 `AQA-73571-QP-JUN23`、`-MS-`、`-WRE-`（考试报告） |
| OCR | 组件 `H240/01`，题册与 Printed Answer Booklet 分离 |
| IB | `M23/5/MATHX/HP1/ENG/TZ1/XX/M`（考季／科目／级别卷号／时区／markscheme） |
| AP | “AP® … Free-Response Questions”，`© College Board` |

## 单元代码

- **Pearson IAL Mathematics（2018 考纲，Issue 3 – April 2019，ISBN 978 1 446 94981 8）**：P1–P4 = WMA11–WMA14；FP1–3 = WFM01–03；M1–3 = WME01–03；S1–3 = WST01–03；D1 = WDM11。每单元 1h30、75 分。P1–P4、M1、M2、S1、S2 有 1、6、10 月考季；FP、M3、S3 只有 1、6 月。（考纲印刷 pp.7–8、p.78）
- **Pearson IAL Economics（2018）**：WEC11 Markets in Action、WEC12 Macroeconomic Performance and Policy、WEC13 Business Behaviour、WEC14 Developments in the Global Economy。
- **CIE 9708 Economics（2026–2028 Version 2，December 2025）**：Paper 1 AS MCQ；Paper 2 AS Data Response and Essays（essay 分两问）；Paper 3 A Level MCQ；Paper 4 A Level Data Response and Essays（20 分 essay 不分小问）。（印刷 pp.35–36）
- **CIE 9709 Mathematics**：Paper 1 Pure 1、2 Pure 2、3 Pure 3、4 Mechanics、5 Probability & Statistics 1、6 Probability & Statistics 2；2028 年起换用 2028–2030 版。
- **Pearson UK**：9MA0（Paper 1/2 Pure、Paper 3 Statistics and Mechanics）、9FM0、9EC0。

## 已核实的排他知识点

| 知识点 | 在哪里考 | 能区分 |
|---|---|---|
| vector equation of a line `r = a + λb`、两直线 parallel／intersecting／skew | Pearson IAL P4 7.6（印刷 p.29）；CIE 9709 P3 3.7；UK 9FM0 | IAL P4 vs UK 9MA0（9MA0 不含）；不能区分 IAL P4 与 9709 P3 |
| Poisson 分布 | IAL S2 1.1–1.3（p.58）；9709 P6；UK 9FM0 | IAL S2 vs 9MA0 |
| population、census、sampling unit、sampling frame、statistic 及其 sampling distribution（枚举全部样本） | IAL S2 4.1–4.2（p.59） | 同局单元：出现 `σ²/n` 或 Central Limit Theorem 则属 S3 3.2、3.6（p.61） |
| binomial distribution | IAL 只在 S2（S1 只有 discrete uniform）；9709 P5；9MA0 | 同局单元判别 |
| permutations／combinations、geometric distribution | 9709 P5；IAL 全无 | CIE vs Pearson IAL |
| complex numbers | 9709 P3；IAL 只在 FP1／FP2 | 纯数卷出现即 CIE P3 或 Pearson FP |
| large data set | UK 9MA0 统计；IAL 全无 | UK vs IAL |
| property rights、pollution permits、nudge、regulation／deregulation | 9708 A Level 8.1.1（p.27） | 只区分同局单元：9708 A Level vs AS（AS 3.2 只有 subsidies、direct provision、information 等）；其他考试局的经济学考纲也有这些内容，不能用来区分考试局（`exam_fingerprint.py` 因此不把它算作考试局级排他点） |

搜索摘要得来的条目（9MA0 Topic 10、9709 条目号）在正式锁定前要读到考纲原文页码。

## 资料从哪里取

**先查技能自带的考试登记**（[exams/README.md](exams/README.md)）：已登记的考试有最新考纲条目与真题逐题索引，`python scripts/exam_index.py` 可按单元、考纲条目、关键词检索。登记是有日期的快照：用之前核对版本与考季，补查登记之后的新考季，缺口（以 `exam_index.py <单元> --gaps` 为准）照样去找；没有登记的考试从下面的检索顺序开始。

检索顺序：

1. **官方站点**：Pearson `qualifications.pearson.com`（spec、past papers、mark schemes、Examiners' report／PEF、exemplar responses with examiner commentary、SAM model answers）；Cambridge `cambridgeinternational.org/past-papers` 与 School Support Hub（syllabus、MS、Principal Examiner Report for Teachers、Example Candidate Responses、Specimen Paper Answers）；AQA `filestore.aqa.org.uk`；OCR；IB（Follett／Programme Resource Centre）；AP Central（sample responses、scoring commentary、chief reader report）。
2. **用户提供的文件**（上传的 PDF，或已连接的 Google Drive 等云盘）：按代码与 Publications Code 搜文件名和全文（如 `WST02`、`9708_s23_er`）。官方站点打不开时先问一句或直接搜用户已连接的云盘；不假设用户有哪些文件。
3. **官方 PDF 的公开镜像**（papacambridge、physicsandmathstutor、examsolutions 等），先做“三点一致”核验：文件名代码＝页眉页脚印刷代码＝封面科目与考季；再核版权行（`© UCLES 年份`／`© 年份 Pearson Education Ltd.`）与页数（CIE 写明页数，Pearson 条码末两位是总页数）。
4. **第三方总结**（复习网站、题库小程序、AI 摘要）只作为找原文的指针，不作考纲或评分证据；题库小程序版本可能重排或加水印，要回到原件。

网络环境拦截某些主机时，在 `research_gaps` 写明被拦主机，改走 Drive 或镜像，不把搜索摘要当作已读原文。处于保密期（AQA、OCR、Pearson 新考季）而在非官方渠道出现的材料，只用于理解评分口径，标注来源，不把原文搬到卡面。

## 真实范文从哪里来

| 考试局 | 真实考生作答 | 官方示范（不是真实考生） | 评分说明 |
|---|---|---|---|
| Cambridge | Example Candidate Responses（ECR，高中低档＋考官评语） | Specimen Paper Answers（SPA） | Principal Examiner Report for Teachers |
| Pearson | Exemplar responses with examiner commentary；Results Plus | SAM model answers | Examiners' report／Principal Examiner Feedback（PEF） |
| AQA／OCR | 教师资源中的 exemplar | — | Report on the examination／Examiners' report |
| AP | Sample responses＋scoring commentary | — | Chief reader report |

每份记录写清是真实考生还是官方撰写；同一题的三档作答只代表这一道题。
