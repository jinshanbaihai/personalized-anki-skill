# 考试登记：已经调研好的考试

这里收录用户常考的考试的**最新考纲条目**和**新考纲实施以来全部可得真题的逐题索引**，目的是让同一考试的下一批板书不必重复例行调研。登记是**有日期的快照**，不是调研的替代品。

## 使用纪律（先读）

1. **登记只省例行调研，不免除调研纪律。** 锁定考试仍按 [../exam-lock.md](../exam-lock.md) 做；登记里的事实是起点，用之前核对：
   - 考纲版本与目标考季仍然适用（看 `versions.md` 与考纲封面；登记日期之后可能出了新版）；
   - 登记日期之后有没有新考季的真题、MS、考官报告（登记写明了截至哪一季）；
   - 登记里写明的缺口（缺 MS、缺考官报告、只有抽取文本的卷子）照样去找。
2. **登记外的一律完整调研**：别的考试局、别的科目、别的单元、陌生材料，按 SKILL.md 第 2–4 步从零开始。
3. **出处要回到原件**：索引条目的 `ms`、`er` 是要点摘录，做卡时要引用的措辞、步骤分与拒收说法回到原 MS／ER 核对；`sources` 写明了原件在哪（用户 Drive 标题、公开仓库路径或抽取文本）。只有抽取文本的条目（Edexcel-Finder 文本会丢失分式、根号与网络图）使用前先看原卷。
4. **新调研的结果回填登记**：同一考试做新卡时读到的新考季、新 MS／ER、新问法，按同样格式补进来（`python scripts/exam_index.py --check` 必须通过）。

## 收录范围

| 文件夹 | 考试 | 内容 |
|---|---|---|
| `cie-9708/` | Cambridge International AS & A Level Economics 9708，A Level（A2）阶段：主题 7–11，Paper 3 选择题与 Paper 4 数据题和论述题 | `syllabus-a-level.md` 考纲逐条（含 Paper 3／4 结构、AO、命令词，AS 主题 1–6 列编号）；`spec-items.json`；`9708-P3.questions.json`（2023 年 3 月至 2025 年 11 月全部 23 份卷、690 道选择题）、`9708-P4.questions.json`（同期全部 23 份卷、115 题）逐题索引；`syllabus-2029-changes.md` 2029 版考纲线索；`paper3-overview.md`、`paper4-overview.md` 按考纲条目汇总问法、频次、评分惯例与考官警告；`topic-notes.md` 专题深读笔记（consumer theory、外部性与政府干预） |
| `pearson-ial-maths/` | Pearson Edexcel IAL Mathematics／Further Mathematics／Pure Mathematics（2018 规范）全部 14 个单元：P1–P4（WMA11–14）、FP1–FP3（WFM01–03）、M1–M3（WME01–03）、S1–S3（WST01–03）、D1（WDM11） | `specification.md` 资格结构、单元组合、记号、公式表给出与须记的公式、计算器规则；`spec-items.*.json`；`units/<单元>.md` 每个单元的考纲逐条（印刷页码、指导栏、须记公式、与相邻单元的界线）与“真题需求概览”；`units/<单元>.questions.json` 逐题索引（14 个单元共 1,990 题，从各单元在 2018 规范下首考起到能取得的最新一季）；`units/WST02.notes.md`、`units/WMA14.notes.md` 专题深读笔记 |
| `versions.md`、`versions.json` | 两个考试的版本与日期 | 现行考纲与公式表版本、各单元在现行规范下的首考考季（沿用旧代码的 WFM／WME／WST 单元据此排除旧规范卷）、各考季开设的卷与变体、地区卷 /01A 的情况、已知的新版考纲 |

## 查询

```bash
python scripts/exam_index.py --list                          # 各单元题数与最新考季
python scripts/exam_index.py WMA14 --spec 4.1                # 考纲条目 4.1 的全部真题小问
python scripts/exam_index.py WST02 --grep "sampling frame"   # 在问法、终点要求、MS、考官报告要点里全文检索
python scripts/exam_index.py 9708/4 --spec 8.1.1 --since 2024-01
python scripts/exam_index.py WMA14 --coverage                # 每个考纲条目考过几次，哪些从未考过
python scripts/exam_index.py WMA14 --spec 6 --demands        # 生成 deck.json 的 demands 初稿（points、cards 由制作者填）
```

## 索引条目格式

每题一个对象：`id`、`unit`、`paper`（含变体，如 `WMA14/01A`、`9708/42`）、`series`（`YYYY-MM`）、`q`、`marks`、`parts`、`sources`。每个小问：`part`、`marks`、`spec`（考纲条目编号，必须存在于 `spec-items*.json`）、`command`、`ask`（问法转述）、`final_form`（终点要求）、`ms`（评分要点，如 “M1 … A1 cso”；选择题写 `key: B`）、`er`（考官报告要点）。转述为主，只在需要精确措辞时短引（不超过约 25 个英文词）；不含任何个人信息。

## 现状与缺口

截至 2026-10-06 的覆盖与缺口见 `versions.md` 与各单元 `.md` 的说明；要点：

- 来源：用户 Google Drive 中的官方原件、公开 GitHub 仓库中经核验的官方 PDF、Edexcel-Finder 题干文本。考试局官网与常见镜像在调研环境中被拦截。
- **最新考季**：Pearson 2025 年 10 月 /01A 之后、2026 年 1 月与 6 月的大部分卷子在考试局的受限区域，未取得；CIE 9708 的 2026 年 3 月与 6 月卷未取得。做卡时先补查这些考季。
- **考官报告**：Pearson 只有 2022-10 至 2024-01 各季；CIE 缺 2024-03、2024-11、2025-06、2025-11 的 Principal Examiner Report。
- **早期卷**：D1 等单元 2019–2022 部分考季只有抽取文本、没有 MS。
- CIE 官网页面已列出 2029 版考纲（`764392-2029-syllabus.pdf`）与一份 2026–2028 考纲更新说明，两者都未取得；2026–2028 Version 2 适用于 2028 年及以前的考季，2029 年起的考季先读新考纲（见 `cie-9708/syllabus-2029-changes.md`）。
