# 牌组数据（ccpt-6）与生成命令

## 命令

```bash
pip install -r scripts/requirements.txt          # genanki、edge-tts、latex2mathml；另需 ffmpeg/ffprobe
python scripts/build_cards.py deck.json out/ --preview         # 只出页面，检查内容与版式
node scripts/render_check.mjs out/ --phone --dark              # 真实 Chromium 截图 + ccptAudit 体检
python scripts/build_cards.py deck.json out/ --term-sampler    # 合成语音（晓晓/云扬，2× 或 1.5×）并打包 .apkg；另出术语试听
python scripts/build_cards.py deck.json out/ --audio-pending   # 语音服务不可达时先交付图文包，页面明示“语音待补”
python scripts/build_cards.py deck.json --check-research       # 卡还没写时：先查考试锁定、research、考点与真题需求计划
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json   # 隔离 collection 导入、解码、重复导入保历史（需 requirements-validate.txt）
```

`--audio-pending` 的包可以先导入学习；输出目录里同时写出 `deck.json`、按步骤编号的 `补语音.txt` 和补语音要用的 `skill/` 程序副本（scripts 与 assets，约 6 MB）（每次打包都会写出 `deck.json`，新对话续做时把它交给 Claude）。之后在能访问语音服务的机器上照 `补语音.txt` 用这份 deck.json 去掉该参数重跑、再导入，同 GUID 的 note 原位更新（Anki 默认“较新时更新”），复习历史保留。Note 字段 `StableID, Title, Page, Source, Narration` 永远不改，改了旧卡就无法原位更新（测试锁定）。

## 顶层结构

```json
{
  "schema": "ccpt-6",
  "deck": {"name": "IAL Statistics 2::Sampling", "deck_id": 2026100611, "model_id": 2026100610,
           "model_name": "CCPT6 · 考纲知识卡", "namespace": "ccpt6-ial-wst02-sampling"},
  "style": {"theme": "lab", "voice": "xiaoxiao", "speed": "auto"},
  "speech_lexicon": {"ILATE": "I L A T E"},
  "exam": { ... },
  "terms_known": [{"term": "sampling frame", "taught_in": ["T03"]}],
  "ignore_words": ["respectively"],
  "research": [ ... ],
  "research_gaps": "",
  "board": [ ... ],
  "demands": [ ... ],
  "coverage": { ... },
  "cards": [ ... ]
}
```

- `deck_id`、`model_id` 取一次后固定；`namespace` + 卡 `id` 决定 GUID，原位更新时两者都不能改。
- `style.theme`：`editorial`（经济、商科、社科）、`paper`（纯数）、`lab`（统计、数据）、`blueprint`（物理、化学、工程）、`manuscript`（历史、文学、哲学）。同一资格跨学科时用 `style.theme_by_subdeck`（如 `{"S2": "lab", "P4": "paper"}`）；单卡可用 `theme` 覆盖。
- `style.voice`：`xiaoxiao`（默认）或 `yunyang`；`style.voice_by_subdeck` 只用于**单独学习**的子牌组（如 `{"Essay": "yunyang"}`），因为从父牌组一起复习时声音会逐卡交替；`--term-sampler` 按每种声音各出一份试听；`style.speed`：`"auto"`（默认：逐卡按规则判定 2× 或 1.5×），或整副牌组固定 `2.0`／`1.5`（1.5 需写 `style.speed_reason`）。`speech_lexicon` 是读音替换表。规则见 [narration.md](narration.md)。
- `style.speed_review`：一副卡组超过三成判为 1.5× 时打包前必填（`--preview` 只警告），写为什么这副卡确实这么密（会印进报告，也要写进交付说明）。`style.legacy_voice: true` 才允许云希（只用于维护旧卡）。`deck.tag` 可指定页眉考试标签（默认由考试代码与单元生成，如“9708 · P3 · P4”）。
- `personal`：默认不写（false）。生成器拒绝“你的卷面／你丢”式写法、考生号与中心号、邮箱，以及卷面总分（如“总分 49/75”）；只有学习者明确要一副只给自己看的个人化讲评时才写 `"personal": true`，这类卡组不外传。单条误拦（例如概率 13/125 旁边恰好有“试卷”二字）把报错里的路径写进 `privacy_reviewed`（如 `["cards[3].blocks[1].text"]`），其余照常检查。姓名生成器认不出，制作者自己保证不写。
- 非考试材料设 `"academic": false`，可省略 `exam`、`research`、`coverage`；有 `exam` 或任何卡写了 `covers` 时生成器拒绝 `academic: false`，不能用它绕过取证。

## exam：锁定考试

```json
"exam": {
  "board": "Pearson Edexcel", "qualification": "International Advanced Level Mathematics", "code": "XMA01/YMA01",
  "units": ["WST02"], "spec_version": "Issue 3 (April 2019)", "spec_url": "https://...", "session": "January 2027",
  "identified_by": "exclusive-content",
  "evidence": ["板书标题 EDX-IAL", "题干版式 (Total for Question … marks)", "sampling frame、statistic、sampling distribution 属 S2 考纲 4.1–4.2"],
  "ruled_out": [{"candidate": "Edexcel 9MA0 Paper 3", "why_not": "9MA0 统计不含 sampling distribution of a statistic 的列举求法"}],
  "papers": [{"code": "WST02", "format": "structured"}]
}
```

`identified_by`：`paper-code`（材料上直接有试卷代码）、`exclusive-content`（版式＋排他知识点；此时 `ruled_out` 必填）、`user`（用户明确告知）。`session` 是目标考季，它决定适用的考纲版本；不知道时写推定的下一个考季并加 `"session_assumed": true`。`papers`（考试牌组必填）列出考这批内容的每份试卷与卷型（`mcq`／`structured`／`data-response`／`essay`／`practical`／`oral`），每份都要有一条 `research` 记录写 `"paper": "<code>"`，或在 `research_gaps` 说明缺口。方法见 [exam-lock.md](exam-lock.md)。

## research：实际读过的资料

每条 `{type, ref, read, used_for, paper?, via?}`：`type` 取 `spec | qp | ms | er | exemplar | specimen | textbook | board | teacher | other`；`ref` 写文件名、年份季次、卷号题号与 URL；`read` 写实际读到的页码或范围；`used_for` 写它改变了哪些卡、哪句定义、哪一步。`via`：`original`（读的是原件）或 `registry`（读的是技能自带考试登记里的摘要，`ref` 写卷号与考季；要引用的措辞仍回原件核对）。生成器要求有 `spec` 与 `ms`；任何地方都找不到 MS 时，只允许 `coverage.status: "partial"` 并在 `research_gaps` 说明（交付说明第一行也要写）。没有 `er`／`exemplar`／`specimen` 时必须在 `research_gaps` 写明取不到什么、用什么替代。卷型含 essay 或 data-response 时，`exemplar`／`specimen` 记录的 `read` 要写明读了哪几页（如 `script pp.15–21 read`）：扫描答卷渲染成图片后看图读，“是图片／无 OCR”不算取不到，否则报告给出警告。

## board：板书点

`[{id:"B07", where:"p3 左下", point:"proof by contradiction 三步", items:["P4-1.1"], note:"…", source_paper:"WMA14 Jan 2026 Q7", legibility:"ok"}]`。每个板书点要么映射到考点，要么在 `note` 说明为什么不进卡（老师口误已更正、离题、超纲）。卡组里有板书卡（`genre: "board"`）时，每个不是丢分记录的板书点还要出现在某个 crop 的 `points` 里，或写 `not_shown` 说明为什么不上卡（章节标题、题外话、已更正的笔误）。`source_paper` 写印刷题的官方出处（找不到写“未找到官方出处”）；批改卷上丢的分（如 `Q01A2 0`，也可写 `Q9(a)M1`、`Q9(a)(ii)A1` 这类带小问的 id）也记成板书点，写 `lost`（“A1”）与 `cards`（补救它的卡）或 `not_carded`；只记题号、分点与是否得分，不写姓名、日期和总分。可选 `score`（这一分点得了几分），`score` 大于 0 时不需要 `lost`：M0 → 方法卡与完整推导卡，A0 → 易错卡与 finish 检查项，B0 → 术语或结论句卡；看不清的板书点写 `"legibility": "low"` 和 `confirmed_by`（用哪份官方材料确认了内容），不猜字。卡组不是从板书做的（例如只按考纲某节制作）时，`board` 可为空，但要写 `board_waived` 说明。

## demands：真题需求清单

`[{id:"D07", series:"June 2024", q:"Q3(a)", command:"Explain", ask:"…", final_form:"…", marks:"B1", ms_notes:"…", points:["S2-4.1b"], cards:["T-frame"]}]`。考到本批内容的每个真题小问一条；`points` 指向考点，`cards` 指向准备它的卡（暂不做卡写 `not_carded`）。`coverage.saturation` 写读了哪些考季、为何停止（连续三季没有新问法）。没有任何 demand 的 core 考点会列进报告。方法见 [coverage-ledger.md](coverage-ledger.md) §3。

## coverage：范围账本

```json
"coverage": {
  "scope": "WST02 考纲 4.1–4.2 Population, census and sample; statistic and its sampling distribution",
  "status": "complete",
  "remaining": "",
  "saturation": "按考季倒序读 WST02 June 2026 → Jan 2023 共 9 季；最后 3 季没有新问法",
  "backcheck": [{"paper": "WST02/01", "series": "2024-06", "q": "3", "result": "pass", "fixed_by": []},
                {"paper": "WST02/01", "series": "2023-01", "q": "5(b)", "result": "gap", "fixed_by": ["M-sampdist"], "note": "缺“列出全部样本”这一步的 B1"}],
  "coldread": [{"card": "T03", "missing": ["all"], "fixed_by": ["T03"]}],
  "items": [
    {"id": "S2-4.2a", "spec": "4.2 Concepts of a statistic and its sampling distribution", "class": "core", "kind": "term",
     "point": "statistic 的定义与判断", "level": "MS：判断需给理由 contains no unknown parameters／based only on the sample；“because it is known”不给分",
     "evidence": ["WST02 Jan 2025 Q2(i) MS p.8", "WST02 Jun 2023 ER p.4"]},
    {"id": "PRE-BIN", "spec": "S2 2.1 Binomial distribution", "class": "prerequisite", "point": "B(n,p) 的 P(X=0)",
     "reason": "求最小 n 的题需要"},
    {"id": "S2-4.3", "spec": "4.3 Hypothesis tests", "class": "adjacent", "point": "critical region", "reason": "同属第 4 节、下一批；June 2024 Q3 与 sampling 联考，联考时的问法已纳入 S2-4.1b"},
    {"id": "X-CLT", "spec": "S3", "class": "excluded", "point": "central limit theorem", "reason": "属 WST03，不在本卷"}
  ]
}
```

`class`：`core`（本卷考点，必须写 `level`：MS 要求的措辞、步骤、图或评价深度；`kind`：`term`／`method`／`formula`／`diagram`／`chain`／`essay`／`command`／`fact`，`term` 类考点必须有自己的术语卡；`evidence`：至少两条不同考季的 MS 或 ER 出处，取不到就写 `evidence_gap`；已由其他牌组的卡讲透时写 `existing` 指明那张卡）、`prerequisite`（理解或解题必需的先修，写 `reason`）、`adjacent`（同一考纲大节、留给下一批，写 `reason`；卡片不能覆盖它，报告会列出）、`excluded`（教材或板书出现但不属于本卷，写 `reason`，任何卡不得覆盖）。`status: complete` 时每个 core／prerequisite 至少有一张卡；`partial` 时 `remaining` 写清还差什么。卡片用 `covers` 反向声明自己教哪些考点，生成器双向核对。`backcheck` 记录“只凭卡组作答真题”的结果（`result` 为 `pass` 或 `gap`，`gap` 必须写 `fixed_by`）；`status: complete` 至少要有两条不同考季的回查。`coldread` 记录冷读关键词测试里写不出的词（`missing`）和补上它们的卡。`--preview` 时缺回查只警告，打包时必须有。方法见 [coverage-ledger.md](coverage-ledger.md) 与 [review-and-delivery.md](review-and-delivery.md) §一。

## cards：卡片

```json
{"id": "T03", "genre": "term", "title": "Sampling frame：可以抽到的个体名单",
 "covers": ["S2-4.1b"], "sources": ["WST02 June 2024 Q3(a) MS p.8"], "speed": 2.0,
 "blocks": [ {"type": "lead", "text": "…"}, {"type": "definition", "term": "Sampling frame", "text": "…", "keywords": ["…"]} ]}
```

- `genre`：`term` 术语、`derivation` 推导、`method` 方法、`formula` 公式、`chain` 因果、`map` 导图、`diagram` 图解、`compare` 辨析、`essay` 论述、`pitfall` 易错、`overview` 全景、`case` 案例、`board` 板书（学习者自己的 ClassIn 板书按知识点裁切，见下文 board 块）。卡型怎样配块见 [card-genres.md](card-genres.md)。
- 牌组级 `terms_known` 写成 `{term, taught_in: [卡 id]}`：只列本牌组里确实有卡讲透的词（`taught_in` 指向那张卡）；功能词写进 `ignore_words`；别处讲过、这里只是用到的词在卡上就地释义（`<abbr title="…">词</abbr>（中文）` 或“词（中文）”，缩写同样可以写成 `MS（评分方案）`）。旧的纯字符串写法仍能用，但报告会提醒改写。生成器把卡上出现、却没有术语卡、就地释义或 `terms_known` 解释的 English 词（单词与词组，复数归到单数）**全量**列进 `report.json` 的 `term_ledger`（总数在 `term_ledger_total`，与考点或真题文本相关的排在前面）；8 个词以上、旁边没有中文的英文句子列进 `untranslated`。交付说明引用真实总数。
- `speed` 可覆盖自动判定（`1.5` 必须同时写 `speed_reason`）；`theme`、`tag`（页眉考试标签）、`subdeck`、`title_speech`、`examples_waived`（术语卡没有自然非例时的理由）、`formula_booklet`（`given` 公式表已给／`memorise` 须背／`derive` 须会推导，显示在页眉）可选。声音只在 `style.voice` 或 `style.voice_by_subdeck` 设定。
- `links`：相关卡的 id（例如论述卡连到它的因果链卡与导图卡）。`exam_waived`：术语卡确实没有考法可写时的理由。
- 生成器按卡型检查最低结构：`term` 卡要有 definition、至少一个例子和一个写了理由的非例；考试牌组的 `term` 卡还要有 definition `source`、至少两项的 unpack、exam 块（或 `exam_waived`）；`derivation` 卡要有 steps 与 finish；`method` 卡要有 steps；`formula` 卡要有 unpack 或 steps，考试牌组还要写 `formula_booklet`（推导、方法卡缺它会警告）；`case` 卡要有 chain、map 或 sections 把案例连回理论；`chain` 卡要有 chain 块，`map`／`overview` 卡要有 map 块，`essay` 卡要有 sections，并有 chain／map 块或 `links`；`board` 卡要有 board 块。term／command 类考点可以由术语卡或展示了定义的板书卡讲透，chain 类考点可以由 chain／map 块或展示了箭头的板书卡讲透。
- 卡片顺序就是首次学习顺序：先修与术语在前，推导与论述在后。

## 内容块（blocks）

| type | 字段 | 用途 |
|---|---|---|
| `lead` | text | 一句话主干，页面最醒目 |
| `definition` | term, text, keywords[], zh, gloss, everyday, accept[], reject[], source, label | 考试措辞的定义；`keywords` 必须逐字出现在 text 中并被高亮；`everyday` 写日常义 vs 考试义；`accept`／`reject` 写 MS 接受与拒收的说法 |
| `unpack` | items[{key, explain}], label | 逐词拆解定义或公式 |
| `examples` | yes[{text, why}], no[{text, why}] | 例子与反例 |
| `table` | head[], rows[[]], caption, label | 对比、分类、条件表 |
| `steps` | given, items[{subgoal, do, why, basis, mark, mark_note, trivial}], goal, marks_basis, label, when | 理科推导：每步“做什么＋为什么＋依据”；`subgoal` 把 2–4 步归成一组并显示组名；`mark` 用 MS 记号（M1、dM1、ddM1、A1、A1*、A1ft、A1cso、B1、B1ft、C1、SC1，可写“M1 A1”或“M1A1”），朗读时读成“这一步记 M 1”；`mark_note` 写容忍与扣分并朗读为“评分注意”；只有 `mark_note` 的步骤也算有解释；纯算术步可 `trivial: true`；`marks_basis` 说明得分标注来自哪份 MS（登记里已有真 MS 时不能再写“按同类题推断”）；MS 的另一种做法再用一个 steps 块，`label` 写“另一种做法”、`when` 写何时选它 |
| `chain` | items[{text, rel, cond, note, kind, ao, arrow, line} 或 {fork: [[…], […]]}], direction, label | 箭头因果链：`rel` 印在箭头上，`cond` 是挂在箭头下的条件旁注，`note` 是节点内的次要说明；`fork` 并列两条以上分支，分叉后的节点自动汇合（链不能以分叉开头，两个分叉之间要有节点）；`direction`: auto / row / column |
| `map` | root{text, rel, kind, ao, arrow, line, children[]}, layout, edge, fold, label | 深层导图；`kind` 见下；`layout`: auto / logic / outline；`edge`: curve / elbow（默认按主题）；`fold: false` 不折叠分支 |
| `figure` | svg, caption, points[] | 原创 SVG 图及逐点解读 |
| `pitfall` | items[{wrong, right, why, lost, source, source_type}] | 易错：老师批注、examiner report、MS 拒收说法、用户卷面；`lost` 写丢的分（A1）；`source_type`：er／ms／ecr／specimen／teacher／user-script／textbook／author，卡面印出种类 |
| `exam` | items[{text, mark}], label | 考法、command word、得分点 |
| `finish` | items[], label | 交卷前检查：exact、3 s.f.、指定形式、有效范围、`+c`、结论回指 |
| `sections` | items[{head, text, mark}], label | essay 段落骨架、分点论述 |
| `note` | text, label, tone(plain/key/aside/warn/heuristic), exceptions[] | 补充说明；`heuristic` 是老师口诀（ILATE 等），必须写 `exceptions`，卡面注明不是评分要求 |
| `html` | html, speech | 特殊被动 HTML 的出口，必须自带 speech |
| `board` | src, crops[{box, speech, where, points[], spots[{box, speech, step}], alt, tone}], masks[], tone, label | 板书卡：`src` 是板书原图（相对 deck.json 的路径；PDF 先用 `pdftoppm -r 200 -png` 转成 PNG）；`crops` 按阅读顺序列出这个知识点需要的区块，`box` 是原图像素 `[x0, y0, x1, y1]`（取自 `board_images.py` 的 `regions.json`）；每块要有 `speech` 或带 speech 的 `spots`；`spots` 是块内的行框，读到它时框出来，推导步写 `step: true`（计入语速规则的推导步数）；`points` 写这块展示的板书点；`where` 是印在块上方的小字位置；`masks` 是要涂掉的框（姓名、日期、学号），对同一原图的所有区块生效；`tone`：`auto`（默认，按底色判断）／`light`（白底，亮色融进纸色、夜间反相）／`dark`（黑板绿板，原样显示）／`keep`（照片，原样显示） |

`map`／`chain` 的 `kind`：`root topic definition cause effect condition evaluation example step contrast policy limit note`，决定节点小标签、边框与底色；关系本身写在 `rel` 上，读者不靠颜色猜关系。`rel` 是短连接词（不超过约 8 个汉字），它决定连线：导致／所以／因此 → 正向箭头；因为／由于／取决于 → 反向箭头；仅当／如果／若 → 虚线；但是／然而 → 点线；例如 → 细线（规则与 `assets/ccpt6/layout.js` 的 `REL_RULES` 一致）；需要时用 `arrow`（forward/back/none）与 `line`（solid/dashed/dotted/thin）覆盖。长条件写成 condition 节点或 `cond` 旁注。

### 板书块示例

```json
{"id": "BD03", "genre": "board", "title": "用总面积为 1 求 k，再求概率", "covers": ["CRV-k"], "sources": ["本课板书"],
 "blocks": [{"type": "board", "src": "board.png", "masks": [[40, 20, 600, 100]], "crops": [
   {"box": [56, 996, 684, 1238], "where": "板书约 56% 处", "points": ["B05"], "speech": "这道例题把定义里的第二个条件变成方程来求 k。",
    "spots": [{"box": [60, 1062, 680, 1120], "speech": "用总面积为 1：k x 从 0 积到 2，得到 2k 等于 1。这一步是方法分 M 1。", "step": true},
              {"box": [60, 1120, 680, 1178], "speech": "解出 k 等于二分之一，这是 A 1。", "step": true}]},
   {"box": [68, 1560, 700, 1630], "where": "板书约 87% 处", "points": ["B07"], "speech": "老师的红笔批注：漏写范围 0 到 2 会扣 A 1。"}]}]}
```

朗读顺序：标题 → 每块的 `speech` → 这块的各个 `spots`（逐个框出）→ 下一块。`speech` 是纯朗读文本，不写 LaTeX；公式按含义读出来。

### 文字、数学与朗读

- 文字可含 `b strong em i u sub sup br span code mark small abbr s`；字面小于号写 `&lt;`。
- 数学写 LaTeX：行内 `$...$`，独立 `$$...$$`，构建时转成 MathML，离线显示，不依赖 MathJax。
- 每个公式后紧跟中文读法 `〔...〕`：`$\frac{9}{245}$〔245 分之 9〕`。没有读法的公式会让构建失败，除非整块另给 `speech`。
- 每块默认朗读其可见文字（步骤读作“第 1 步…为什么…依据…这一步记 M 1…评分注意…”，导图每个节点一段）；得分点、丢的分、表注都读，出处（`source`、`marks_basis`）不读；需要改写口播时给该块 `speech`。朗读分段同时就是高亮与自动跟随滚动的单位。
- 金额写 `\$2`：卡面显示 $2，朗读为“2 美元”（未转义的成对 `$` 会被当作公式）。比较符号前后留空格（`x < 2`）即可直接写，读作“小于”；紧贴字母的 `MSB<MSC` 会被当成标签而拒绝，写成 `MSB &lt; MSC` 或公式。
- 长等式链（两个以上 `=`、`<`、`≤` 等）在行内公式里会自动在关系符号前留出换行点，手机上折行而不是被横向截断。

## 输出

`out/<id>.html`（预览页）、`out/media/ccpt6-board-<哈希>.png`（板书区块，随包打包）、`out/board/`（非预览构建时写出：每张板书原图只保留卡片用到的区块、遮挡已涂上，`deck.json` 的 `src` 改指这里，交付文件夹因此能独立重建）、`ccpt_single_face.ankiaddon`（双击安装的桌面插件）、`pages.json`、`speech-manifest.json`（每卡 voice、speed、atempo、分段朗读文本与实测 cue）、`report.json`（每卡速度、理由与 `metrics.signals`、S／M／m%／T／E／N／C 指标、时长、`plain_math` 纯文本数学处数、警告；全量 `term_ledger` 与 `term_ledger_total`、`untranslated`、`waivers`、`speed` 汇总、`backcheck`／`coldread`、覆盖统计）、`deck.json`（打包时的卡组数据，续做与补语音用）、`<牌组名>.apkg`，以及可选的 `term-sampler.mp3`。Note 字段：`StableID, Title, Page, Source, Narration`；Source 存 JSON（考试锁定、covers、来源），不显示在卡面。
