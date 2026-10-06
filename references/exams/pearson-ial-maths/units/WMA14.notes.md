# Pearson Edexcel IAL WMA14（Pure Mathematics P4）：专题深读笔记

> 全卷逐题索引见同目录 `WMA14.questions.json`，考纲条目与真题需求概览见 `WMA14.md`；这里是一批板书制卡时逐题深读的标定证据。

可复核资料池，按 [exam-lock.md](../../../exam-lock.md) 与 [mark-scheme-calibration.md](../../../mark-scheme-calibration.md) 的流程整理。同一考试的新卡先查这里，再补读缺的部分。本文件不含任何学生个人信息。最近核验：2026-10-06。

## 考试身份

| 字段 | 值 |
|---|---|
| 考试局 | Pearson Edexcel |
| 资格 | International Advanced Level in Mathematics / Pure Mathematics（2018 specification）；IAL 代码 YMA01 / YPM01，IAS 代码 XMA01 / XPM01 |
| 单元 | WMA14 Pure Mathematics P4（IAL 第二年的纯数单元，接在 WMA13 P3 之后） |
| 卷别 | WMA14/01（全球卷）与 WMA14/01A（区域卷，独立答题册，版式与分值相同）；1 h 30 min，75 分，全部为结构题；随卷提供 formulae booklet；‘Inexact answers should be given to three significant figures unless otherwise stated’ |
| 考季 | January、June、October 三季；2026 Oct/Nov 季英国文化教育协会中国考点信息表列 WMA14A：28 October 2026 16:00 |
| 规格版本 | Issue 3，April 2019，ISBN 978 1 446 94981 8；first teaching September 2018；Unit P4 first assessment June 2020 |
| 官方规格地址 | https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf（研究时 Pearson 域名被网络策略拦截，读的是 Drive 上字节一致的副本：2,438,609 字节） |

区分要点：UK 9MA0 的纯数卷是 100 分 2 小时、没有 /01A；Cambridge 9709 P3 用 [n] 分值和 © UCLES；P4 的 partial fractions、rational-n binomial、parametric/implicit differentiation、3D vector lines、separable DE 都不在 WMA13 P3 或 WFM01 FP1。

## 考纲与公式表

| ID | 来源 | 实际读取位置 | 使用范围 |
|---|---|---|---|
| SPEC | IAL Maths/Further/Pure Maths Specification Issue 3 | Issue 3 changes 页；印刷 pp.21–25（Unit P3：P3.2 须记公式、P3.3 1.1–6.2）；pp.26–29（Unit P4 全文：P4.2 Assessment information，P4.3 1.1–7.7 与 Guidance） | P4 范围；P1–P3 作先修（P4 Assessment information：‘A knowledge of the specifications for P1, P2 and P3, their prerequisites and associated formulae, is assumed and may be tested.’）；须记的点积公式 |
| FB | Mathematical Formulae and Statistical Tables，Issue 2（January 2021，P59773RA） | 印刷 pp.3–5（Pure Mathematics P1–P4 全部条目） | given / memorise 判定 |

P4 考纲七节：1 Proof（1.1 proof by contradiction，含 √2 无理、素数无穷）；2 Algebra and functions（2.1 partial fractions，分母为 distinct/repeated linear，分子次数可等于或高于分母）；3 Coordinate geometry（3.1 parametric ↔ Cartesian）；4 Sequences and series（4.1 rational-n binomial、|x| < b/a、结合 partial fractions）；5 Differentiation（5.1 parametric 与 implicit、切线法线；5.2 connected rates 与建立一阶 DE）；6 Integration（6.1 体积 π∫y² dx，含参数式；6.2 换元与分部，含 ∫ln x、两次分部；6.3 partial fractions 积分；6.4 分离变量 DE 与模型；6.5 parametric area，Issue 3 新增）；7 Vectors（7.1–7.7：3D、模与单位向量、位置向量、距离、r = a + λb、相交/平行/skew、scalar product 求角与垂直）。

规格内明确排除或未列：π∫x² dy（只考绕 x 轴）；(x² + a) 型分母的 partial fractions；参数曲线作图；反三角函数积分；t 公式；vector product。

### formula booklet 判定

| 公式 | 判定 | 依据 |
|---|---|---|
| (1 + x)^n 级数（|x| < 1, n ∈ ℝ） | given | FB p.5（P4 段）；P2 段 p.3 是正整数 n |
| 分部积分 ∫u (dv/dx) dx = uv − ∫v (du/dx) dx | given | FB p.5 |
| tan kx、sec x、cot x、cosec x 的导数，商法则 | given | FB p.4（P3 段） |
| ∫sec² kx、∫tan x = ln|sec x|、∫cot x = ln|sin x|、∫cosec x、∫sec x | given | FB pp.4–5 |
| sin(A ± B)、cos(A ± B)、tan(A ± B) | given | FB p.4 |
| double angle、sec² = 1 + tan²、cosec² = 1 + cot² | memorise | SPEC P3 Assessment information（p.21）‘Formulae that students are expected to know are given below and will not appear in the booklet’ |
| ∫e^{kx}、∫1/x、∫sin kx、∫cos kx；∫f′(x)/f(x)、∫f′(x)[f(x)]ⁿ | memorise | SPEC P3.2（p.22）与 P3 5.x |
| a·b = a₁b₁ + a₂b₂ + a₃b₃，cos θ = a·b/(|a||b|) | memorise | SPEC P4.2（p.26）、7.7 Guidance（p.29） |
| V = π∫y² dx 与参数式 π∫y² (dx/dt) dt；A = ∫y (dx/dt) dt；dy/dx = (dy/dt)/(dx/dt) | memorise | FB 未给；SPEC 6.1、6.5、5.1 |

## 题卷、评分方案与考官报告

页码为印刷页；无印刷页码处用 PDF 页序。全部原件取自用户 Google Drive（Pearson 域名在研究环境中被拦）。

### 题卷（QP，倒序）

| 季 | 卷 | 出版代码 | 读取 |
|---|---|---|---|
| June 2026 | /01A | P84806A | 全卷 pp.1–7；答题册封面 |
| January 2026 | /01A | P87595A | 全卷；指数丢失处渲染 pp.2–3 |
| January 2026 | /01 | P81324A | 全卷；渲染 pp.2、6 |
| October 2025 | /01 | — | 全卷 |
| June 2025 | /01A | P78911A | 全卷 |
| June 2025 | /01 | — | 全卷 |
| January 2025 | /01 | P76196A | 全卷 |
| October 2024 | /01 | — | 全卷 |
| June 2024 | /01 | — | 全卷 |
| January 2024 | /01 | P74881A | 全卷 |
| October 2023 | /01 | — | 全卷 |
| June 2023 | /01 | — | 全卷 |
| January 2023 | /01 | — | 全卷 |

### 评分方案（MS）

| ID | 卷 | 实际读取位置 | 可复用的规则 |
|---|---|---|---|
| MS-O25 | Oct 2025 /01 | pp.3–6 通则；Q1 pp.8–10；Q3 pp.13–14；Q4 p.15；Q5 p.16；Q6 p.19；Q8 p.24；Q9 p.26；Q10 p.30 | M/A/B、dM、cao、cso、isw、awrt、oe、ft 定义；binomial B1（提出常数因子并算出）M1（第 3 或第 4 项结构）A1 A1；validity ‘|x| < 2/5 oe’；消参 M1 M1 dM1 A1 B1；反证结论 |
| MS-J25A | Jun 2025 /01A | Q2 pp.10–11 | connected rates：‘now being marked as M1dM1A1 not B1M1A1’；dx/dt = dx/dV × dV/dt |
| MS-J25 | Jun 2025 /01 | Q2 p.9；Q5 p.14；Q9 pp.21–22 | 体积 B1 ‘A correct expression for the volume including limits and dx’、M1 展开平方三项、dM1 cos2x 恒等式、A1；重复分部 |
| MS-J25W | Jan 2025 /01 | Q3 pp.10–11；Q4 pp.11–13；Q5(ii) p.17；Q6 pp.19–20 | binomial 漏乘常数 ‘condoning the omission of their 3’ 只保 M；PF 积分 ‘Moduli are not required, brackets will suffice’；反证假设 ‘Must be in words’ |
| MS-O24 | Oct 2024 /01 | Q1 p.7；Q2 pp.9–10；Q4 p.13；Q6 p.17；Q7 pp.18–19；Q8 p.20；Q9 p.23；Q10 p.24 | ‘8^{1/3} must be evaluated’；反证 ‘If the roots are just stated then M0A0A0 follows’；换元末 A1 ‘Correct expression in the required form including the + c’；improper PF ‘Just stating the values of A and B is insufficient’；Q10(a) ‘On EPEN this is M1M1A1 but we are marking this as B1M1A1’ |
| MS-J24 | Jun 2024 /01 | Q1 p.7；Q2 p.8；Q3 p.9；Q7 p.17；Q8(b) pp.19–20 | 分部 M1 ‘in the correct direction’；implicit normal ‘If the form y = mx + c is used then the method must proceed as far as c = …’；判别式须写出数值 |
| MS-J24W | Jan 2024 /01 | Q2 pp.8–9；Q6 pp.16–17；Q7 pp.19–20；Q8 p.21 | PF M1 A1 M1 A1；角度 M1 M1 A1 awrt；体积 ‘Makes the connection with part (a)’；‘Do not accept “this equation has no solutions” without proof as to why … A sketch is not a proof’ |
| MS-O23 | Oct 2023 /01 | p.6；Q1 pp.7–8；Q4 p.17；Q7(d) pp.27–28；Q8 p.29 | binomial 4 分 B1 M1 A1 A1，末 A1 ‘cao … must be simplified … Do not isw’；validity 拒收单边与未化简；反证结论 ‘but not just “contradiction”’ |
| MS-J23 | Jun 2023 /01 | Q3 pp.11–12；Q4 pp.13–14；Q6 pp.17–18；Q7 p.19；Q8(d) p.20 | ‘Allow brackets instead of moduli’；‘r =’ 必写，‘l = …’ A0；垂足 M1 dM1 ddM1 A1；DE B1 分离、M1、A1 含 k 与另一常数、M1 M1 M1、A1；√7 无理证明四分点 |
| MS-J23W | Jan 2023 /01 | Q1 p.7；Q7 p.20；Q8 pp.22–24；Q9 p.25 | 参数 normal B1 M1 A1 dM1 A1*；面积 M1 A1 dM1 A1 M1 A1；‘If the t’s become x’s … M0’ |

### 考官报告（ER / Principal Examiner Feedback）

| ID | 卷 | 实际读取位置 | 有价值的证据 |
|---|---|---|---|
| ER-J24W | Jan 2024 /01 | 全文 pp.1–12 | binomial 代错整体项、漏常数；第二个 ln 未除系数；体积不会平方；分部第二次符号；位置向量当方向向量；取钝角或只给 2 s.f.；show that 漏步骤；‘no solutions’ 不给理由；矛盾后不回指原命题；dx/dt 除反；切线当法线 |

其余各季的 WMA14 ER 在 Drive 中未取得。真实考生作答：IAL 数学没有公开 exemplar（WMA11 01A 的 exemplar 文件是空白答题册）；可用的真实作答是用户自己的阅卷答卷与 ER 的转述。

### 第三方指针（不作评分依据）

Edexcel-Finder（GitHub，第三方从官方 QP 抽取的题干 JSON，October 2020–January 2025 共 16 份）：只用来确认原题出处和找到更早季的问法，例如 skew lines（January 2021、October 2022）、unit vector（June 2021）、‘no greatest odd integer’（January 2021）。这些季的 MS 未取得。

## 已核的评分规则（跨季一致）

1. 记号：M＝方法分（方法须正确且用于本题）；A＝准确分（依赖相应 M）；B＝独立分；dM＝依赖前一个 M；cao＝correct answer only；cso＝correct solution only（推导中不能有错）；ft＝follow through；isw＝ignore subsequent working；awrt＝answers which round to；oe＝or equivalent；A1*＝给定答案（show that）。
2. **ePEN 标签不等于 MS 记号**：答卷上 Q01B、Q04bM2 等是阅卷系统的栏位名，字母可能与 MS 不同（Oct 2024 Q10(a)：‘On EPEN this is M1M1A1 but we are marking this as B1M1A1’；Jun 2025 /01A Q2：‘now being marked as M1dM1A1 not B1M1A1’）。拿到考生 ePEN 记录时，按栏位顺序对应 MS 步骤，不要从字母推断分类。
3. Show that（A1*/cso）：每一步要看得到；给定结果不能从结论倒推。
4. Hence：必须用前一问的结果，另起炉灶通常不给分。
5. 精确值与形式：‘exact’ 不能给小数；‘in the form …’ 要写成题目形式并给出常数（换元题的形式含 + c）。
6. 二项式末项 cao 且须化简，不 isw。
7. 反证法：假设用文字写出且否定正确；推出矛盾要给理由（判别式数值、平方非负等）；结论回指原命题；只写 ‘contradiction’ 不够。
8. 向量直线方程须写 ‘r =’。
9. 不定积分 moduli 可用括号代替；+ c 是否要求看具体题（换元的 ‘required form’ 要求，Jun 2023 Q3(b) 不要求）。

## 区域卷 /01A 说明

- 题型、分值、版式与 /01 相同；答题册独立（板书答卷页印 ‘Write the answer to Question n on these k pages’）。
- /01A 的 MS 只读到 June 2025 一份；June 2026 /01A 的 MS 与 ER 均未取得。该卷各小问的得分点结构只能由 ePEN 栏位＋同类题 MS 推断（标“按同类题推断”）。
- January 2026 两份 QP 无 MS。

## 需求覆盖统计（13 季 263 条 demands）

最常考：implicit 求导 21/13 季；parametric 求导 12/12；切线与法线 21/12；partial fractions 积分 17/13；connected rates 16/10；向量垂直应用 16/12；换元 15/13；消参 15/12；binomial 14/12；分离变量 DE 13/13；体积 13/10；分部 12/12；反证结构 12/12；参数面积 10/7。命令词：Show that 50 次（13 季），Hence 32 次（11 季），exact 21 次。2023–2026 未出现：skew lines、unit vector、素数无穷证明。

## 缺口

1. June 2026 /01A MS 与 ER；January 2026 /01A 与 /01 MS。
2. WMA14 ER 只取得 January 2024 一份。
3. 2020–2022 各季 MS（skew lines、unit vector、整数性质证明的评分措辞）。
4. IAL 数学没有公开的真实考生 exemplar。
