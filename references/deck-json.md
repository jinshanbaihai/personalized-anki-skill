# 牌组数据（ccpt-6）与生成命令

## 命令

```bash
pip install -r scripts/requirements.txt          # genanki、edge-tts、latex2mathml；另需 ffmpeg/ffprobe
python scripts/build_cards.py deck.json out/ --preview         # 只出页面，检查内容与版式
node scripts/render_check.mjs out/ --phone --dark              # 真实 Chromium 截图 + ccptAudit 体检
python scripts/build_cards.py deck.json out/ --term-sampler    # 合成语音（晓晓/云扬，2× 或 1.5×）并打包 .apkg；另出术语试听
python scripts/build_cards.py deck.json out/ --audio-pending   # 语音服务不可达时先交付图文包，页面明示“语音待补”
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json   # 隔离 collection 导入、解码、重复导入保历史
```

`--audio-pending` 的包可以先导入学习；之后在能访问语音服务的机器上用同一份 deck.json 去掉该参数重跑、再导入，同 GUID 的 note 原位更新，复习历史保留。

## 顶层结构

```json
{
  "schema": "ccpt-6",
  "deck": {"name": "IAL Statistics 2::Sampling", "deck_id": 2026100611, "model_id": 2026100610,
           "model_name": "CCPT6 · 考纲知识卡", "namespace": "ccpt6-ial-wst02-sampling"},
  "style": {"theme": "lab", "voice": "xiaoxiao", "speed": "auto"},
  "speech_lexicon": {"ILATE": "I L A T E"},
  "exam": { ... },
  "research": [ ... ],
  "research_gaps": "",
  "board": [ ... ],
  "coverage": { ... },
  "cards": [ ... ]
}
```

- `deck_id`、`model_id` 取一次后固定；`namespace` + 卡 `id` 决定 GUID，原位更新时两者都不能改。
- `style.theme`：`editorial`（经济、商科、社科）、`paper`（纯数）、`lab`（统计、数据）、`blueprint`（物理、化学、工程）、`manuscript`（历史、文学、哲学）。单卡可用 `theme` 覆盖。
- `style.voice`：`xiaoxiao`（默认）或 `yunyang`，整副牌组一个声音；`style.speed`：`"auto"`（默认：逐卡按规则判定 2× 或 1.5×），或整副牌组固定 `2.0`／`1.5`（1.5 需写 `style.speed_reason`）。`speech_lexicon` 是读音替换表。规则见 [narration.md](narration.md)。
- 非考试材料设 `"academic": false`，可省略 `exam`、`research`、`coverage`；有考试目标时不能用它绕过取证。

## exam：锁定考试

```json
"exam": {
  "board": "Pearson Edexcel", "qualification": "International Advanced Level Mathematics", "code": "XMA01/YMA01",
  "units": ["WST02"], "spec_version": "Issue 3 (first teaching 2018)", "spec_url": "https://...",
  "identified_by": "exclusive-content",
  "evidence": ["板书标题 EDX-IAL", "题干版式 (Total for Question … marks)", "sampling distribution / statistic 属 S2 第 6 章"],
  "ruled_out": [{"candidate": "Edexcel 9MA0 Paper 3", "why_not": "9MA0 统计不含 sampling distribution of a statistic 的列举求法"}]
}
```

`identified_by`：`paper-code`（材料上直接有试卷代码）、`exclusive-content`（版式＋排他知识点；此时 `ruled_out` 必填）、`user`（用户明确告知）。方法见 [exam-lock.md](exam-lock.md)。

## research：实际读过的资料

每条 `{type, ref, read, used_for}`：`type` 取 `spec | qp | ms | er | exemplar | specimen | textbook | board | teacher | other`；`ref` 写文件名、年份季次、卷号题号与 URL；`read` 写实际读到的页码或范围；`used_for` 写它改变了哪些卡、哪句定义、哪一步。生成器要求至少有 `spec` 与 `ms`；没有 `er`／`exemplar`／`specimen` 时必须在 `research_gaps` 写明取不到什么、用什么替代。

## board：板书点

`[{id:"B07", where:"p3 左下", point:"proof by contradiction 三步", items:["P4-1.1"], note:"…"}]`。每个板书点要么映射到考点，要么在 `note` 说明为什么不进卡（老师口误已更正、离题、超纲）。

## coverage：范围账本

```json
"coverage": {
  "scope": "WST02 Chapter 6 Populations and samples（spec 6.1–6.4）",
  "status": "complete",
  "remaining": "",
  "items": [
    {"id": "S2-6.3", "spec": "6.3 Concept of a statistic and its sampling distribution", "class": "core",
     "point": "statistic 的定义与判断", "level": "MS：判断题需给理由 contains no unknown parameters；B1 定义关键词…"},
    {"id": "PRE-BIN", "spec": "S2 2.1 Binomial distribution", "class": "prerequisite", "point": "B(n,p) 的 P(X=0)",
     "reason": "求最小 n 的题需要"},
    {"id": "X-CLT", "spec": "S3", "class": "excluded", "point": "central limit theorem", "reason": "属 WST03，不在本卷"}
  ]
}
```

`class`：`core`（本卷考点，必须写 `level`：MS 要求的措辞、步骤、图或评价深度；已由其他牌组的卡讲透时写 `existing` 指明那张卡）、`prerequisite`（理解或解题必需的先修，写 `reason`）、`excluded`（教材或板书出现但不属于本卷，写 `reason`，任何卡不得覆盖）。`status: complete` 时每个 core／prerequisite 至少有一张卡；`partial` 时 `remaining` 写清还差什么。卡片用 `covers` 反向声明自己教哪些考点，生成器双向核对。方法见 [coverage-ledger.md](coverage-ledger.md)。

## cards：卡片

```json
{"id": "T03", "genre": "term", "title": "Sampling frame：可以抽到的个体名单",
 "covers": ["S2-6.2"], "sources": ["WST02 Jan 2019 Q1(a) MS"], "speed": 2.0,
 "blocks": [ {"type": "lead", "text": "…"}, {"type": "definition", "term": "Sampling frame", "text": "…", "keywords": ["…"]} ]}
```

- `genre`：`term` 术语、`derivation` 推导、`method` 方法、`formula` 公式、`chain` 因果、`map` 导图、`diagram` 图解、`compare` 辨析、`essay` 论述、`pitfall` 易错、`overview` 全景、`case` 案例。卡型怎样配块见 [card-genres.md](card-genres.md)。
- `speed` 可覆盖自动判定（`1.5` 必须同时写 `speed_reason`）；`theme`、`tag`（页眉考试标签）、`subdeck`、`title_speech`、`examples_waived`（术语卡没有自然非例时的理由）可选。声音只在 `style.voice` 设一次。
- 生成器按卡型检查最低结构：`term` 卡要有 definition、至少两个 idea units（keywords 或 unpack）、至少一个例子和一个写了理由的非例；`derivation` 卡要有 steps 与 finish。
- 卡片顺序就是首次学习顺序：先修与术语在前，推导与论述在后。

## 内容块（blocks）

| type | 字段 | 用途 |
|---|---|---|
| `lead` | text | 一句话主干，页面最醒目 |
| `definition` | term, text, keywords[], zh, gloss, everyday, accept[], reject[], source, label | 考试措辞的定义；`keywords` 必须逐字出现在 text 中并被高亮；`everyday` 写日常义 vs 考试义；`accept`／`reject` 写 MS 接受与拒收的说法 |
| `unpack` | items[{key, explain}], label | 逐词拆解定义或公式 |
| `examples` | yes[{text, why}], no[{text, why}] | 例子与反例 |
| `table` | head[], rows[[]], caption, label | 对比、分类、条件表 |
| `steps` | given, items[{subgoal, do, why, basis, mark, mark_note, trivial}], goal, marks_basis, label | 理科推导：每步“做什么＋为什么＋依据”；`subgoal` 把 2–4 步归成一组并显示组名；`mark` 用 MS 记号（M1、dM1、A1、A1*、B1、ft…），`mark_note` 写容忍与扣分；纯算术步可 `trivial: true`；`marks_basis` 说明得分标注来自哪份 MS 或“按同类题推断” |
| `chain` | items[{text, rel, cond, note, kind, ao, arrow, line} 或 {fork: [[…], […]]}], direction, label | 箭头因果链：`rel` 印在箭头上，`cond` 是挂在箭头下的条件旁注，`note` 是节点内的次要说明；`fork` 并列两条以上分支，分叉后的节点自动汇合（链不能以分叉开头，两个分叉之间要有节点）；`direction`: auto / row / column |
| `map` | root{text, rel, kind, ao, arrow, line, children[]}, layout, edge, fold, label | 深层导图；`kind` 见下；`layout`: auto / logic / outline；`edge`: curve / elbow（默认按主题）；`fold: false` 不折叠分支 |
| `figure` | svg, caption, points[] | 原创 SVG 图及逐点解读 |
| `pitfall` | items[{wrong, right, why, lost, source}] | 易错：老师批注、examiner report、MS 拒收说法；`lost` 写丢的分（A1） |
| `exam` | items[{text, mark}], label | 考法、command word、得分点 |
| `finish` | items[], label | 交卷前检查：exact、3 s.f.、指定形式、有效范围、`+c`、结论回指 |
| `sections` | items[{head, text, mark}], label | essay 段落骨架、分点论述 |
| `note` | text, label, tone(plain/key/aside/warn) | 补充说明 |
| `html` | html, speech | 特殊被动 HTML 的出口，必须自带 speech |

`map`／`chain` 的 `kind`：`root topic definition cause effect condition evaluation example step contrast policy limit note`，决定节点小标签、边框与底色；关系本身写在 `rel` 上，读者不靠颜色猜关系。`rel` 是短连接词（不超过约 8 个汉字），它决定连线：导致／所以／因此 → 正向箭头；因为／由于／取决于 → 反向箭头；仅当／如果／若 → 虚线；但是／然而 → 点线；例如 → 细线（规则与 `assets/ccpt6/layout.js` 的 `REL_RULES` 一致）；需要时用 `arrow`（forward/back/none）与 `line`（solid/dashed/dotted/thin）覆盖。长条件写成 condition 节点或 `cond` 旁注。

### 文字、数学与朗读

- 文字可含 `b strong em i u sub sup br span code mark small abbr s`；字面小于号写 `&lt;`。
- 数学写 LaTeX：行内 `$...$`，独立 `$$...$$`，构建时转成 MathML，离线显示，不依赖 MathJax。
- 每个公式后紧跟中文读法 `〔...〕`：`$\frac{9}{245}$〔245 分之 9〕`。没有读法的公式会让构建失败，除非整块另给 `speech`。
- 每块默认朗读其可见文字（步骤读作“第 1 步…为什么…依据…”，导图按一级分支分段）；需要改写口播时给该块 `speech`。朗读分段同时就是高亮与自动跟随滚动的单位。

## 输出

`out/<id>.html`（预览页）、`pages.json`、`speech-manifest.json`（每卡 voice、speed、atempo、分段朗读文本与实测 cue）、`report.json`（每卡速度与理由、S／M／m%／T／E／N／C 指标、时长、警告、覆盖统计）、`<牌组名>.apkg`，以及可选的 `term-sampler.mp3`。Note 字段：`StableID, Title, Page, Source, Narration`；Source 存 JSON（考试锁定、covers、来源），不显示在卡面。
