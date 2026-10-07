# 考试登记：已经调研好的考试

这里收录已经调研过的考试的**最新考纲条目**和**新考纲实施以来全部可得真题的逐题索引**，目的是让同一考试的下一批板书不必重复例行调研。登记是**有日期的快照**（2026-10-06），不是调研的替代品。

## 使用纪律（先读）

1. **登记只省例行调研，不免除调研纪律。** 锁定考试仍按 [../exam-lock.md](../exam-lock.md) 做；登记里的事实是起点，用之前核对：
   - 考纲版本与目标考季仍然适用（看 `versions.md` 与考纲封面；登记日期之后可能出了新版）；
   - 登记日期之后有没有新考季的真题、MS、考官报告；
   - **缺口以 `python scripts/exam_index.py <单元> --gaps` 的输出为准**：它按 `versions.json` 的考季规则算出该单元应有而未收录的卷、未收录 MS／考官报告的卷、只有抽取文本的卷、只有 Drive 副本的原件，这些照样去找。每次查询都在 stderr 打印一行快照提示：快照日期、该单元最新收录的考季、未收录的预期考季数、返回的小问里缺 MS／ER 要点的数目。
2. **登记外的一律完整调研**：别的考试局、别的科目、别的单元、陌生材料，按 SKILL.md 第 2–4 步从零开始。
3. **出处要回到原件**：索引条目的 `ms`、`er` 是要点摘录，做卡时要引用的措辞、步骤分与拒收说法回到原 MS／ER 核对。`sources` 先写中性出处（考试局／卷号／考季／文件类型），再写公开地址（examsolutions S3 镜像或 raw.githubusercontent.com），再写 Drive 标题与 id，最后是构建时的记录；取原件的方法见下文“原件怎么取”。只有抽取文本的条目（Edexcel-Finder 文本会丢失分式、根号与网络图）使用前先看原卷。
4. **新调研的结果回填登记**：同一考试做新卡时读到的新考季、新 MS／ER、新问法，按同样格式补进来。
   - **在仓库里工作时**：补进 `units/<单元>.questions.json`（或 `cie-9708/9708-P3.questions.json` 等），运行 `python scripts/exam_index.py --check` 与 `python scripts/exam_index.py --completeness`，都必须通过；补上的缺口从 `versions.json` 的 `gaps` 里删去，否则 `--completeness` 会报 `STALE`。
   - **技能以上传的 zip 运行、手边没有仓库时**：把新找到的题写进交付文件夹的 `registry-additions/<单元>.questions.json`（格式与 `units/<单元>.questions.json` 相同；补全已有条目时沿用原 `id`），用 `python scripts/exam_index.py --check-file registry-additions/<单元>.questions.json` 校验到 `ok`。交付说明里告诉用户：把这些条目合并进仓库的 `references/exams/`，运行 `--check` 与 `--completeness`（并更新 `versions.json` 的 `gaps`），再重新打包技能。

## 收录范围

| 文件夹 | 考试 | 内容 |
|---|---|---|
| `cie-9708/` | Cambridge International AS & A Level Economics 9708，A Level（A2）阶段：主题 7–11，Paper 3 选择题与 Paper 4 数据题和论述题 | `syllabus-a-level.md` 考纲逐条（含 Paper 3／4 结构、AO、命令词，AS 主题 1–6 列编号）；`spec-items.json`；`9708-P3.questions.json`（2023 年 3 月至 2025 年 11 月全部 23 份卷、690 条，其中 M/J 2023–2025 的 9708/33 与 9708/31 是同一份卷，90 条标 `same_as`）、`9708-P4.questions.json`（同期全部 23 份卷、115 条，M/J 2023–2025 的 9708/43 与 9708/41 同卷，15 条标 `same_as`）逐题索引；`syllabus-2029-changes.md` 2029 版考纲线索；`paper3-overview.md`、`paper4-overview.md` 按考纲条目汇总问法、频次、评分惯例与考官警告；`topic-notes.md` 专题深读笔记（consumer theory、外部性与政府干预） |
| `pearson-ial-maths/` | Pearson Edexcel IAL Mathematics／Further Mathematics／Pure Mathematics（2018 规范）全部 14 个单元：P1–P4（WMA11–14）、FP1–FP3（WFM01–03）、M1–M3（WME01–03）、S1–S3（WST01–03）、D1（WDM11） | `specification.md` 资格结构、单元组合、记号、公式表给出与须记的公式、计算器规则；`spec-items.*.json`；`units/<单元>.md` 每个单元的考纲逐条（印刷页码、指导栏、须记公式、与相邻单元的界线）与“真题需求概览”；`units/<单元>.questions.json` 逐题索引（14 个单元共 1,990 题，从各单元在 2018 规范下首考起到能取得的最新一季）；`units/WST02.notes.md`、`units/WMA14.notes.md` 专题深读笔记 |
| `versions.md`、`versions.json` | 两个考试的版本与日期 | 现行考纲与公式表版本、各单元在现行规范下的首考考季（沿用旧代码的 WFM／WME／WST 单元据此排除旧规范卷）、各考季开设的卷与变体、地区卷 /01A 的情况、已知的新版考纲；`versions.json` 另有机器可读的 `expected_papers`（各单元应有哪些卷）与 `gaps`（已知并接受的缺口及原因） |

各 `.md` 里出现的 `registry/…`、`work/…`、`src/…`、`inventory/…`、`scratchpad/…`、`finder/…`、`research/…`、`*.coverage.part*.md`、`*.questions.part*.json`、审核脚本名与 `CRITIC.md` 都是**构建溯源（不随包发布）**：构建登记时沙箱里的工作文件，技能包里没有，只说明某个结论是怎么核出来的。

## 查询

```bash
python scripts/exam_index.py --list                          # 各单元题数与最新考季
python scripts/exam_index.py WMA14 --spec 4.1                # 考纲条目 4.1 的全部真题小问
python scripts/exam_index.py WST02 --grep "sampling frame"   # 在问法、终点要求、MS、考官报告要点里全文检索
python scripts/exam_index.py 9708/4 --spec 8.1.1 --since 2024-01
python scripts/exam_index.py 9708 --spec 7.4                 # "9708" = 9708/3 与 9708/4
python scripts/exam_index.py WMA14 --coverage                # 每个考纲条目考过几次，哪些从未考过
python scripts/exam_index.py WMA14 --spec 6 --demands        # 生成 deck.json 的 demands 初稿（points、cards 由制作者填）
python scripts/exam_index.py WST02 --gaps                    # 该单元的缺口（按规则算出，标注 versions.json 里记的原因）
python scripts/exam_index.py --completeness                  # 全部单元：算出的缺口都要在 versions.json gaps 里有原因
python scripts/exam_index.py --check                         # 校验全部登记（测试也跑）
python scripts/exam_index.py --check-file registry-additions/WST02.questions.json
```

- 单元代码不分大小写；Pearson 单元也可以写短名（P4、S2、FP1……）；`9708` 同时查 9708/3 与 9708/4。未知单元或未知考纲条目以非零状态退出，并列出最接近的名字。
- 考纲印刷编号重号的两个条目可按应有编号查：WST01 的 `5.1#2`（正态分布）查 `6.1`，WFM02 的 `7.1#2`（极坐标面积）查 `7.2`；`--spec 5.1` 不会匹配 `5.1#2`。
- 与另一变体同卷的条目（`same_as`）默认不出现在查询与 `--coverage` 里，保留的条目在 `papers` 里列出两个卷号；`--all-variants` 把它们也列出来。
- 输出一律 UTF-8；控制台不支持的字符被替换，不会报错退出。

## 索引条目格式

每题一个对象：`id`、`unit`、`paper`（含变体，如 `WMA14/01A`、`9708/42`）、`series`（`YYYY-MM`）、`q`、`marks`、`parts`、`sources`；同卷复用时另有 `papers`（保留条目，列出全部卷号）或 `same_as`（重复条目，指向保留条目的 `id`）。每个小问：`part`、`marks`、`spec`（考纲条目编号，必须存在于 `spec-items*.json`）、`command`、`ask`（问法转述）、`final_form`（终点要求）、`ms`（评分要点，如 “M1 … A1 cso”；选择题写 `key: B`）、`er`（考官报告要点）。转述为主，只在需要精确措辞时短引（不超过约 25 个英文词）；不含任何个人信息。

`sources` 的 `qp`、`ms`、`er` 各是一段文字，用 ` | ` 分段：中性出处 → 公开地址 → Drive 定位 → 构建记录（页码、封面核对、本地副本路径）。非空的每一段出处至少含一个可解析的定位（`drive:`、`github:`、`finder:` 或 `https://`），`--check` 会检查；`ms`、`er` 可以为空（没取得），空着的由 `--gaps` 计数。

### 原件怎么取（Resolving sources）

| `sources` 里的写法 | 怎么取 |
|---|---|
| `https://examsolutions.s3.eu-west-2.amazonaws.com/exam+papers/maths/IAL/<文件>`（“S3 mirror” 或 “examsolutions S3 mirror of Pearson `<文件>`”） | 直接下载。examsolutions 的公开 S3 镜像，文件名就是 Pearson 官方文件名；地址 = 基址 `https://examsolutions.s3.eu-west-2.amazonaws.com/exam+papers/maths/IAL/` + 文件名 |
| `github:owner/repo@sha path`（也有 `owner/repo@sha:path`、`owner/repo/path (commit sha)` 的写法） | `https://raw.githubusercontent.com/owner/repo/<sha>/<URL 编码的 path>`；条目里已经写好完整 commit 的 raw 地址，固定在该 commit，仓库以后变了也不受影响 |
| `finder:<路径>.json`（Edexcel-Finder） | `anonymouslyanonymous1/Edexcel-Finder` 在所注 commit（`e3db703420c90046e31b197a504d1ea119e7e771`）的原始 JSON：`https://raw.githubusercontent.com/anonymouslyanonymous1/Edexcel-Finder/<commit>/static/Data/<URL 编码的路径>`。内容是逐页抽取的小写题干文本，不是 PDF |
| `drive:"标题" (id X)`、`drive:标题 (Drive id X; …)`、`drive copy "标题" (id X)` | 有 Google Drive 连接器时按 id 打开，或按标题搜索。**id 只在构建登记的那个账号里有效**；标题是官方或常见文件名，在别的 Drive 或网上也能搜到 |
| `local:src/…`、`registry/…`、`work/…`、`scratchpad/…`、`inventory/…`、`*.coverage.part*`、`CRITIC.md` | 构建溯源，不随包发布；只说明构建时读的是哪个副本。取原件用同一段里的公开地址或 Drive 定位 |

只有 Drive 定位、没有公开地址的原件，在 `versions.json` 的 `gaps` 里记为 `qp-drive-only`／`ms-drive-only`／`er-drive-only`（原因 `drive_only`）。

### `--demands` 输出字段

| 字段 | 含义 |
|---|---|
| `id` | 条目 `id` 加小问号，如 `WMA14-2024-06-01-Q3b` |
| `series` | 考季 `YYYY-MM` |
| `paper` | 卷号；同卷复用时写成 `9708/31 = 9708/33` |
| `q` | 题号与小问，如 `Q3b` |
| `command`、`ask`、`final_form` | 命令词、问法转述、终点要求（同索引小问字段） |
| `marks` | MS 的给分代码串（如 `M1 A1`），能从 MS 要点读出且合计等于分值时才写；否则写分值数字（文本） |
| `marks_total` | 小问分值（整数） |
| `ms_notes` | 索引里的 MS 要点；登记没有该卷 MS 时写 `MS not held in registry (snapshot 2026-10-06)` |
| `ms_source` | `registry summary`：`ms_notes` 是登记的转述，引用前回到原 MS 核对；`not held`：登记没有 MS，要自己去找 |
| `er_notes` | 考官报告要点；登记有该卷报告但报告没有评这一问时写 `ER held; no comment on this part`；没有报告时写 `ER not held in registry (snapshot …)` |
| `spec` | 小问对应的考纲条目编号（`spec-items*.json` 的键） |
| `points`、`cards` | 空列表，由制作者填考点 id 与卡 id（见 [../coverage-ledger.md](../coverage-ledger.md) §3） |
| `source` | 该题的 `sources`（`qp`、`ms`、`er` 三段出处），按上表取原件 |

## 现状与缺口

截至 2026-10-06：

- **来源**：构建登记时可得的 Drive 原件（Pearson、Cambridge 官方 PDF）、公开 GitHub 仓库中经核验的官方 PDF（`Upppllld/OpenPastPapers`、`RayZ3R0/papernexus-finder`、`EslamAhmedGaber/elite-igcse-math` 等，固定在 commit）、examsolutions 的公开 S3 镜像（Pearson 官方文件名）、Edexcel-Finder 题干文本。条目里写出的 575 个公开地址在 2026-10-06 逐个用 `curl -sI` 复测，全部返回 200。
- **访问**：构建登记的沙箱里，考试局官网（qualifications.pearson.com、cambridgeinternational.org）与 papacambridge、pastpapers.co、xtremepape、physicsandmathstutor 一类镜像都被拦截（2026-10-06 复测：代理 CONNECT 返回 403）；examsolutions 的 S3 镜像与 raw.githubusercontent.com 可以访问。
- **缺口**：一律以 `python scripts/exam_index.py <单元> --gaps` 与 `--completeness` 的输出为准；`versions.json` 的 `gaps` 给每个缺口记了原因（`pearson_secure`：2025 年 10 月起 Pearson 把 QP／MS 放在需中心登录的安全区；`not_reached`：已发布但构建时取不到；`not_published`：本来就没有，如 2021 年 6 月的考官报告；`cie_2026_not_reached`、`cie_er_not_reached`、`variant_er_unconfirmed`、`text_only`、`partial`、`drive_only`；各原因的全文在 `gaps.reasons`）。缺口种类：`paper`（应有而未收录的卷）、`ms`／`er`（已收录的卷没有 MS／考官报告）、`ms-partial`／`er-partial`（只有部分题有）、`qp-text`（题卷只有抽取文本）、`qp-drive-only`／`ms-drive-only`／`er-drive-only`（只有 Drive 副本）。做卡时先补查最新考季。
- CIE 官网页面已列出 2029 版考纲（`764392-2029-syllabus.pdf`）与一份 2026–2028 考纲更新说明，两者都未取得；2026–2028 Version 2 适用于 2028 年及以前的考季，2029 年起的考季先读新考纲（见 `cie-9708/syllabus-2029-changes.md`）。
