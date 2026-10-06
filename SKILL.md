---
name: anki-ccpt-skill
description: 把老师板书、课堂截图、讲评 PDF、讲义做成为考试背诵服务的单面 Anki 知识卡。先从内容锁定排他性的考试（考试局、资格、单元代码、考纲版本），再读官方考纲、多年真题与 mark scheme、examiner report 和真实范文，标定“考什么、考到什么程度”，做到考点不漏、不越界；术语卡逐词讲透定义，理科推导每一步写清做什么与为什么并标得分点，文科用箭头因果链和不限层级的导图；按学科选用有美感的版式主题；晓晓或云扬配音，默认 2 倍速、复杂卡 1.5 倍速；Space 播音、Enter 继续、1 明天再看。内置 CIE 9708 A Level 与 Pearson IAL 数学全部单元的最新考纲条目和真题逐题索引。用于新制卡、整章补齐、错题讲评转卡、旧卡改造与制卡规则修改。
---

# 考试导向的 Anki 知识卡

## 目标

用户刷这些卡，是为了在**一场具体的考试**里拿分。读完一组卡，用户应当能：

- 按 mark scheme 认可的措辞写出每个术语的定义，并说清定义里每个词的作用；
- 把每类计算、证明、推导题完整走完，知道每一步为什么这样做、值哪一分、终点要写成什么样；
- 把文科论述的因果链与评价背下来，并在新题里调用；
- 不漏掉这场考试会考的任何考点，也不在考纲外的内容上花时间。

一切取舍以“读者理解透彻、记得住、考场用得上”为准，版式和流程服务这个目标。**讲透优先于简短**：卡的长短由讲透所需决定；内容多时拆成几张讲透的卡，不删理由来压缩篇幅。

## 工作流程

### 1. 读全输入

完整读入板书、讲评或讲义：每页每块的文字、公式、图、箭头、圈画、颜色批注和老师改写，建立板书点清单（`B01…`，写位置与内容）。长图与 PDF 用 `scripts/slice_board.py` 切成重叠切片逐片读；老师批注（“粗心”“过程不充分”“忘记最终要求”）照录，批改卷上的逐分记录（`Q01A2 0`）每个 0 分记成一个板书点并连到补救它的卡（M0 → 方法与完整推导卡，A0 → 易错卡与交卷前检查，B0 → 术语或结论句卡），这些都是易错卡的来源。板书通常清楚，以板书为准；但聊天软件常把长图压到几百像素宽，`slice_board.py` 会报告宽度不足 800 px 的图（扫描或导出的 PDF 按其中内嵌图片的像素判断，同样适用）：受影响的板书点标 `legibility: low`，用官方材料确认后写 `confirmed_by`，**不猜字**，不中途停下等用户，交付时请用户补原图。板书上的每道印刷题都去找官方出处（`source_paper`）。方法见 [coverage-ledger.md](references/coverage-ledger.md)。

**隐私**：讲评卷、批改卷和课堂截图上常有学生姓名、考生号、中心号、上课日期和总分。这些**一律不转录**进卡片、deck.json、研究记录、文件名或交付说明；批改卷只按“题号 + 分点 + 是否得分”中性记录（如“本卷批改记录：Q9(a) M1、A1 未得”），卡面不用“你”指称做卷人，不写个人总分。生成器会拦下“你的卷面／你丢”、总分写法、考生号和邮箱；姓名它认不出，要自己查。学习者明确要做只给自己看的个人化讲评时，才在 deck.json 写 `"personal": true`，这类卡组不外传。

### 2. 锁定考试

从内容判断是哪场考试，精确到**考试局 + 资格 + 单元／试卷代码 + 考纲版本 + 目标考季**（考季决定适用版本，不知道时写推定并标明），写出证据和被排除的近似考试。课程名只是弱线索，要靠印刷代码、版式指纹和排他知识点。`python scripts/exam_fingerprint.py 板书.pdf` 可先列出线索。同时确定这批内容出现在哪些试卷与卷型（`exam.papers`，如 9708 的选择题与 essay），各自标定。证据仍无法区分、且区分结果会改变卡片内容时：用户在场就用选项问一次；要求一次做完时按最强证据制作，并在交付说明第一行写出假设。方法、代码体系、排他知识点表与资料入口见 [exam-lock.md](references/exam-lock.md)。

**已登记的考试先查登记**：[references/exams/](references/exams/README.md) 收录了 CIE 9708 A Level（A2）与 Pearson IAL 数学全部单元（P1–P4、FP1–FP3、M1–M3、S1–S3、D1）的最新考纲条目（编号与印刷页码）和新考纲实施以来全部可得真题的逐题索引（对应考纲条目、分值、终点要求、MS 要点、考官报告要点、原件出处）。登记省掉的是例行调研，**不免除调研纪律**：先核对考纲版本与目标考季仍然适用，补查登记日期之后的新考季，缺口（以 `python scripts/exam_index.py <单元> --gaps` 的输出为准）照样去找；登记外的考试、单元或陌生材料，按本节与下一节完整调研。

### 3. 取证与标定掌握水平

- 读锁定版本的**考纲原文**，把本批范围的每一条拆成考点（定义、关系、方法、图、计算、评价角度），连指导栏一起读。
- 已登记的考试先跑 `python scripts/exam_index.py <单元> --gaps`：stderr 第一行是快照提示（快照日期、最新收录考季、未收录的预期考季数），stdout 列出应有而未收录的卷、没有 MS／考官报告的卷、只有抽取文本或只有 Drive 副本的原件。这些缺口与快照日期之后的新考季照样调研，仍缺的写进 `research_gaps`。再用 `python scripts/exam_index.py <单元> --spec <条目> --demands` 拉出真题需求清单初稿：`ms_source: registry summary` 的要点引用前回到原 MS 核对，`ms_source: not held` 的要自己找 MS。未登记的考试从零开始。
- 登记条目的 `sources` 依次是中性出处、公开地址（examsolutions S3 镜像、raw.githubusercontent.com，可直接下载）、Drive 标题与 id（id 只在构建登记的账号里有效，换账号按标题搜）、构建记录；`local:src/…` 等是构建溯源，不随包发布。取法见 [references/exams/README.md](references/exams/README.md)“原件怎么取”。
- 调研中找到登记里没有的题、MS 或考官报告：在仓库里工作就补进 `references/exams/`，跑 `--check` 与 `--completeness`；技能以上传的 zip 运行、没有仓库时，写进交付文件夹的 `registry-additions/<单元>.questions.json`（与 `units/<单元>.questions.json` 同格式，补全已有条目沿用原 `id`），用 `python scripts/exam_index.py --check-file registry-additions/<单元>.questions.json` 校验，并在交付说明里请用户把它合并进仓库、更新 `versions.json` 的 `gaps`、重新打包技能。
- 按考季倒序读真题，把考到本批内容的每个小问记进**真题需求清单**（`demands`：考季、题号、命令词、问什么、终点要求、MS 注释、对应考点与卡），读到连续三季没有新问法为止（`coverage.saturation`）。
- 每个考点读**至少两个不同考季**、问法不同的真题与对应 **mark scheme**；每个单元至少读一份 **examiner report**；essay 类科目找**真实考生的高中低档作答**（Cambridge ECR、Pearson exemplar responses），也可参考官方示范答案（标明不是真实考生）。
- 从这些材料读出每个考点的掌握水平：定义必含词与拒收说法、单独给分的步骤、终点要求、需要的图、essay 分析要展开到几环、评价写到什么程度。写进考点的 `level`，并在 `evidence` 挂上至少两条不同考季的 MS／ER 出处。**MS 认可的写法优先**：教材的等价说法只作补充，只有 MS 明确拒收的写法才标“不给分”。
- 检索顺序：官方站点 → 用户上传或已连接云盘里的官方文件 → 经核验的官方 PDF 镜像 → 第三方总结（只作指针）。读不到的写进 `research_gaps`，说明用什么替代。ECR、exemplar 这类手写答卷多是扫描图：用 `pdftoppm` 渲染后看图逐页读，在 `read` 里写明页码；“是图片、没有 OCR”不算取不到。
- 教材用考试局认可的教材核对讲法；大学教材只帮助制作者自己理解，不决定范围。

方法与 Pearson／Cambridge 的评分记号、定义采分、essay levels 见 [mark-scheme-calibration.md](references/mark-scheme-calibration.md)。

### 4. 建范围账本

板书点 → 考点 → 卡片三者连起来，每个考点标 `kind`（term／method／formula／diagram／chain／essay／command／fact），term 类考点必须有自己的术语卡；再建**术语台账**，把板书、MS 与题干里每个 English 学科词落到术语卡、就地释义或“已讲过”，命令词（Show that、Hence、Assess、Evaluate…）也做成卡。范围按粒度规则定：板书内容所在的**最小编号考纲条目整条补全**；同一大节的其余条目，真题曾与本批联考的，把联考时的问法纳入，条目本身标 `adjacent` 留给下一批并在交付时列出；做题必需的先修标 `prerequisite`；属于其他单元或超出考试的标 `excluded`，任何卡都不教。正向核对“每个考点、每条真题需求都有卡讲透”，反向核对“每张卡都属于考纲”，再用 2–3 道问法不同的真题只凭卡组作答来查漏。见 [coverage-ledger.md](references/coverage-ledger.md)。

### 5. 设计卡组

按考点选卡型，常用组合：

| 卡型 | 讲什么 | 主要块 |
|---|---|---|
| 术语 term | 一个术语的考试定义、逐词拆解、例与反例、易混辨析、考法 | definition, unpack, examples, table, exam |
| 推导 derivation／方法 method／公式 formula | 一道代表题或一个方法，每步“做什么、为什么、依据、得分点”，终点要求 | steps, finish, pitfall |
| 因果 chain | 一条完整的箭头因果链，箭头上写关系 | chain |
| 导图 map／全景 overview | 一个主题的多层结构，关系写在连线上，层级不设上限 | map |
| 图解 diagram | 原创标准图，逐点解读 | figure |
| 辨析 compare | 易混概念或方法并排 | table, examples |
| 论述 essay | essay 段落骨架、AO 分工、分档阶梯 | sections, map |
| 易错 pitfall | 老师批注、ER 与 MS 拒收说法、用户卷面丢分，标明来源种类 | pitfall |

**术语卡要舍得做**：每个考纲术语、每个 MS 要求精确措辞的概念都单独讲透（日常义 → 有出处的考试定义 → 逐词作用 → 正例与只缺一个属性的非例 → 考法），数学同样如此。**理科**每一步推理都写理由（目的、条件或原理，不复述做法），不跳代数小步；MS 的另一种做法并列并说明何时用；老师口诀标明“不是评分要求”并写出例外；页眉标明公式表是否给出。**文科**的展开要背，用箭头因果链与深层导图表达，不写长段文字；每个箭头的结果写成“哪个变量往哪边变”，评价节点写出条件。卡片顺序就是学习顺序：先修与术语在前，方法与推导居中，论述与全景在后。详见 [card-genres.md](references/card-genres.md)；语言、术语与数学排版见 [language-and-math.md](references/language-and-math.md)。

### 6. 写卡、生成与检查

把卡组写成 JSON（字段见 [deck-json.md](references/deck-json.md)），然后：

```bash
python scripts/build_cards.py deck.json out/ --preview      # 预览页
node scripts/render_check.mjs out/ --phone --dark           # 真实浏览器截图与版式体检
python scripts/build_cards.py deck.json out/                # 合成语音并打包 .apkg
python scripts/build_cards.py deck.json out/ --audio-pending # 语音服务不可达时：先打包图文，写出 deck.json 与 补语音.txt
pip install -r scripts/requirements-validate.txt            # 一次性：导入验证要用的 anki 后端
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json   # 语音待补的包也能验证；成品包加 --require-audio
```

生成器检查：考试已锁定、读过考纲与 MS（每种卷型都有来源）、考点与真题需求双向覆盖、术语定义有出处、每个公式有读法、推导每步有理由、关键词逐字出现在定义中、HTML 不吞字；另对复述式“为什么”、空泛箭头、缺条件的评价、过宽的导图、未解释的 English 词（`report.json` 给出全量术语台账）、`$…$` 之外的纯文本数学、难读符号与拼接错读给出警告；哪些必须改、哪些在交付说明里交代，见 [review-and-delivery.md](references/review-and-delivery.md) 的警告处理表。它不能证明内容讲对了，内容审查见下一步。

### 7. 审查与交付

先冷读与关键词复现测试，再交给独立审阅者找遗漏、误读、超纲和讲不透的地方，修改后复查；然后看截图、听语音、做导入验证与桌面操作测试。交付物是整个输出文件夹：`.apkg`、双击安装的 `ccpt_single_face.ankiaddon`、`deck.json`、`report.json`，语音待补时还有 `补语音.txt`；并告诉用户：插件在第一次复习 CCPT 卡时会自动把该牌组设为阅读预设（学习与重学步长 1 天，按 1 = 下一学习日再看），右下角提示一次，不想要可用“工具 → CCPT：撤销阅读预设”恢复；只用手机复习的用户要在牌组选项里手动把学习与重学步长设为 1d。交付时说明锁定的考试与证据（假设放第一行）、实际读过的资料与缺口、真题回查与冷读的记录、覆盖统计与留给下一批的相邻考点、板书看不清或更正处（请用户补原图）、语音状态，以及哪些检查真的做了（导入验证、截图、真实 Anki 里的按键）；交付文件不写学习者姓名、日期与总分。见 [review-and-delivery.md](references/review-and-delivery.md)。

## 版式与美感

每个学科用一套有明确艺术参照的主题，服务阅读：`editorial`（经济、商科、社科：报刊排印）、`paper`（纯数：数学教科书）、`lab`（统计：实验记录本）、`blueprint`（物理、化学：工程图纸）、`manuscript`（历史、文学、哲学：书籍与评点本朱批）；同一资格跨学科的子牌组可各用各的主题。每种卡型再有自己的版式母题：术语卡像词典条目，推导卡像批改过的答卷（页边线外是得分栏），因果链与导图画在点阵绘图纸上，论述卡像答题纸（段号落在红色页边线外），易错卡像红笔批改。每套都有亮色与 Anki 夜间模式配色并通过 WCAG 对比检查，随卡打包开源字体子集，中文不做伪斜体，老师批注统一用楷体红笔。页头固定显示卡型、考试标签、标题与播放器；长卡可滚动，语音朗读到哪里就高亮哪里，并在读者没有手动滚动时把它平滑带到视野内。导图在宽屏排成左→右逻辑图，放不下的分支在框内收成缩进大纲，手机上整体用缩进树，任何情况下文字都不缩小；关系词印在连线上并决定箭头方向与线型（导致→、←因为、仅当虚线、但是点线、例如细线）；因果链支持条件旁注与分叉汇合。见 [visual-themes.md](references/visual-themes.md)。

## 语音

每页一个播放器，讲解覆盖卡面全部内容，朗读到哪里就高亮哪里。一副牌组一个声音（单独学习的子牌组可以各自指定）：默认晓晓（`xiaoxiao`），男声选云扬（`yunyang`，Edge 中唯一的新闻播音定位男声）。得分点（M1、A1*、丢的分）、评分注意与表注都读出来，出处引用不读。默认 **2×**；生成器按可计算的规则只把真正复杂的卡降到 **1.5×** 并写出理由：多步带公式的推导、公式读法占比高、证明结构、跨步要记住多个数值这几类信号**至少两类同时成立**才算，单独一项、篇幅长或导图深都不算；播放时点速度按钮可临时在 2× 与 1.5× 之间切换。原速合成并全局缓存、修剪首尾静音、ffmpeg 一次加速、设计停顿、离线随卡；读音不对的术语用 `speech_lexicon` 修正，`--term-sampler` 出一分钟术语试听。语音服务不可达时预检立即说明原因，先交付图文包并明示“语音待补”，不静默换声音。见 [narration.md](references/narration.md)。

## 操作方式

单面卡：打开即见完整内容。**Space** 播放／暂停语音，**Enter** 记 Good 并继续，**1** 下一学习日再看。没有翻面、输入答案、选择题或“听完才能继续”。桌面端由 `scripts/single_face_addon.py` 实现，见 [review-and-delivery.md](references/review-and-delivery.md)。为满足“1 = 下一学习日再看”，插件第一次复习某牌组的 CCPT 卡、且其学习或重学步长短于 1 天时，自动改用 CCPT 阅读预设（只改步长为 1 天与 leech 只加标签），不弹窗，可从工具菜单撤销，撤销后不再自动改；其余复习安排只在用户要求时调整，见 [review-planning.md](references/review-planning.md)。

## 学习研究依据

术语的定义＋例反例、理科的 worked example 与逐步解释、文科的论证图与因果图、加速语音的理解边界、阅读卡 Good 的含义：证据与适用边界见 [learning-science.md](references/learning-science.md)。

## 运行环境

需要 Python 3.10+（`pip install -r scripts/requirements.txt`）。其余条件缺了也能交付，但要在交付说明里写明缺了什么：

| 条件 | 缺少时 |
|---|---|
| 能访问 `speech.platform.bing.com`（Edge 语音） | 预检以 `network_blocked` 停止；用 `--audio-pending` 交付图文包，同时写出 `deck.json` 与编号步骤的 `补语音.txt`，整个输出文件夹一起交付；学习者照着补，同一张卡原位更新 |
| ffmpeg／ffprobe | 构建以 `ffmpeg_missing`（退出码 4）停止并给出安装命令：Windows `winget install Gyan.FFmpeg`，macOS `brew install ffmpeg`，Linux `sudo apt install ffmpeg`；装不了就同上交付“语音待补” |
| poppler（`pdftoppm`／`pdftotext`／`pdfimages`） | `slice_board.py` 会改用 PyMuPDF（`pip install pymupdf`）；两者都没有时直接看图逐页读 PDF，长图仍记录行范围，并在交付说明写明 |
| tesseract（含 `chi_sim`） | `exam_fingerprint.py` 读不了图片：直接看切片，把转写的文字用 `-` 管道传给它；OCR 几乎为空时它也会提示这样做 |
| `anki` Python 包（`pip install -r scripts/requirements-validate.txt`，约 30 MB） | 跳过 `validate_package.py`，交付说明写“未做导入验证” |
| Node、Playwright 与 Chromium | 先 `which chromium chromium-browser google-chrome`，找到就设 `CHROMIUM_PATH`；仍没有时按 [review-and-delivery.md](references/review-and-delivery.md) §二 冷读可见文本、跑 `contrast_check.py`、请用户先打开一两张预览页，并写明未做截图检查 |
| 官方网站或用户的云盘 | 先用 `references/exams/` 的登记（原件链接见那里的“原件怎么取”）；仍缺的写进 `research_gaps`，不把搜索摘要当作已读原文 |

在 Claude 网页版或桌面版里使用时，把 `python scripts/package_skill.py` 生成的 `anki-ccpt-skill.zip` 上传为技能；沙盒通常不能联网合成语音，按上表交付“语音待补”包。每次对话都从用户给的材料重新开始：不假设这位用户与以前的对话是同一个人，接着做时请用户提供上次的 `deck.json` 或 `.apkg`。

## 维护本技能

以下只适用于**源码仓库**（上传的 zip 不含测试与 git 历史）：改规则时同步主文、references、生成器与测试；运行 `pip install -r scripts/requirements-dev.txt` 后 `python -m pytest scripts -q`（含 `exam_index.py --check` 与 `--completeness` 对全部考试登记的校验），再用一个真实小样做预览和截图检查；打包用 `python scripts/package_skill.py`，它只收 git 跟踪的文件，遇到未提交的文件、邮箱、云盘链接或密钥会拒绝打包。在上传的 zip 里补充考试登记后，至少运行 `python scripts/exam_index.py --check` 与 `--completeness`。新增考试登记时沿用 `references/exams/README.md` 的格式。修改规则不等于授权重写用户已有的全部卡片。旧版生成器（v5 导图卡、teaching、quiz 等）已从当前版本移除，需要时到源码仓库的 git 历史里取。
