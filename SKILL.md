---
name: anki-ccpt-skill
description: 把老师板书、课堂截图、讲评 PDF、讲义做成为考试背诵服务的单面 Anki 知识卡。先从内容锁定排他性的考试（考试局、资格、单元代码、考纲版本），再读官方考纲、多年真题与 mark scheme、examiner report 和真实范文，标定“考什么、考到什么程度”，做到考点不漏、不越界；术语卡逐词讲透定义，理科推导每一步写清做什么与为什么并标得分点，文科用箭头因果链和不限层级的导图；按学科选用有美感的版式主题；晓晓或云扬配音，默认 2 倍速、复杂卡 1.5 倍速；Space 播音、Enter 继续、1 明天再看。用于新制卡、整章补齐、错题讲评转卡、旧卡改造与制卡规则修改。
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

完整读入板书、讲评或讲义：每页每块的文字、公式、图、箭头、圈画、颜色批注和老师改写，建立板书点清单（`B01…`，写位置与内容）。长图与 PDF 用 `scripts/slice_board.py` 切成重叠切片逐片读；老师批注（“粗心”“过程不充分”“忘记最终要求”）照录，它们是易错卡的来源。板书通常清楚，以板书为准；只在真正模糊处查证补齐并标注依据。方法见 [coverage-ledger.md](references/coverage-ledger.md)。

### 2. 锁定考试

从内容判断是哪场考试，精确到**考试局 + 资格 + 单元／试卷代码 + 考纲版本 + 目标考季**，写出证据和被排除的近似考试。课程名只是弱线索，要靠印刷代码、版式指纹和排他知识点。`python scripts/exam_fingerprint.py 板书.pdf` 可先列出线索。只有在证据仍无法区分、且区分结果会改变卡片内容时，才用选项问用户一次。方法、代码体系、排他知识点表与资料入口见 [exam-lock.md](references/exam-lock.md)。

### 3. 取证与标定掌握水平

- 读锁定版本的**考纲原文**，把本批范围的每一条拆成考点（定义、关系、方法、图、计算、评价角度），连指导栏一起读。
- 每个考点读**至少两个不同考季**、问法不同的真题与对应 **mark scheme**；每个单元至少读一份 **examiner report**；essay 类科目找**真实考生的高中低档作答**（Cambridge ECR、Pearson exemplar responses），也可参考官方示范答案（标明不是真实考生）。
- 从这些材料读出每个考点的掌握水平：定义必含词与拒收说法、单独给分的步骤、终点要求、需要的图、essay 分析要展开到几环、评价写到什么程度。写进考点的 `level`。
- 检索顺序：官方站点 → 用户 Google Drive 中的官方文件 → 经核验的官方 PDF 镜像 → 第三方总结（只作指针）。读不到的写进 `research_gaps`，说明用什么替代。
- 教材用考试局认可的教材核对讲法；大学教材只帮助制作者自己理解，不决定范围。

方法与 Pearson／Cambridge 的评分记号、定义采分、essay levels 见 [mark-scheme-calibration.md](references/mark-scheme-calibration.md)。

### 4. 建范围账本

板书点 → 考点 → 卡片三者连起来：板书讲到的考纲小节**整节补全**；做题必需的先修标 `prerequisite`；属于其他单元或超出考试的标 `excluded`，任何卡都不教。正向核对“每个考点都有卡讲透”，反向核对“每张卡都属于考纲”，再用 2–3 道问法不同的真题只凭卡组作答来查漏。见 [coverage-ledger.md](references/coverage-ledger.md)。

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
| 易错 pitfall | 老师批注、ER 与 MS 拒收说法 | pitfall |

**术语卡要舍得做**：每个考纲术语、每个 MS 要求精确措辞的概念都单独讲透，数学同样如此。**理科**每一步推理都写理由，不跳代数小步。**文科**的展开要背，用箭头因果链与深层导图表达，不写长段文字。卡片顺序就是学习顺序：先修与术语在前，方法与推导居中，论述与全景在后。详见 [card-genres.md](references/card-genres.md)；语言、术语与数学排版见 [language-and-math.md](references/language-and-math.md)。

### 6. 写卡、生成与检查

把卡组写成 JSON（字段见 [deck-json.md](references/deck-json.md)），然后：

```bash
python scripts/build_cards.py deck.json out/ --preview      # 预览页
node scripts/render_check.mjs out/ --phone --dark           # 真实浏览器截图与版式体检
python scripts/build_cards.py deck.json out/                # 合成语音并打包 .apkg
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json
```

生成器检查：考试已锁定、读过考纲与 MS、考点双向覆盖、每个公式有读法、推导每步有理由、关键词逐字出现在定义中、HTML 不吞字。它不能证明内容讲对了，内容审查见下一步。

### 7. 审查与交付

先冷读与关键词复现测试，再交给独立审阅者找遗漏、误读、超纲和讲不透的地方，修改后复查；然后看截图、听语音、做导入验证与桌面操作测试。交付时说明锁定的考试与证据、实际读过的资料与缺口、覆盖统计、板书模糊或更正处、语音状态。见 [review-and-delivery.md](references/review-and-delivery.md)。

## 版式与美感

每个学科用一套有明确艺术参照的主题，服务阅读：`editorial`（经济、商科、社科：报刊排印）、`paper`（纯数：数学教科书）、`lab`（统计：实验记录本）、`blueprint`（物理、化学：工程图纸）、`manuscript`（历史、文学、哲学：书籍与评点本朱批）。每套都有亮色与 Anki 夜间模式配色并通过 WCAG 对比检查，随卡打包开源字体子集，中文不做伪斜体，老师批注统一用楷体红笔。页头固定显示卡型、考试标签、标题与播放器；长卡可滚动，语音朗读到哪里就高亮哪里，并在读者没有手动滚动时把它平滑带到视野内。导图在宽屏排成左→右逻辑图，放不下的分支在框内收成缩进大纲，手机上整体用缩进树，任何情况下文字都不缩小；关系词印在连线上并决定箭头方向与线型（导致→、←因为、仅当虚线、但是点线、例如细线）；因果链支持条件旁注与分叉汇合。见 [visual-themes.md](references/visual-themes.md)。

## 语音

每页一个播放器，讲解覆盖卡面全部内容，朗读到哪里就高亮哪里。整副牌组一个声音：默认晓晓（`xiaoxiao`），男声选云扬（`yunyang`，Edge 中唯一的新闻播音定位男声）。默认 **2×**；生成器按可计算的规则只把真正复杂的卡（多步带公式的推导、公式读法占比高、证明结构、需同时记住多个数值）降到 **1.5×** 并写出理由，篇幅长或导图深不算复杂；播放时点速度按钮可临时在 2× 与 1.5× 之间切换。原速合成并全局缓存、修剪首尾静音、ffmpeg 一次加速、设计停顿、离线随卡；读音不对的术语用 `speech_lexicon` 修正，`--term-sampler` 出一分钟术语试听。语音服务不可达时预检立即说明原因，先交付图文包并明示“语音待补”，不静默换声音。见 [narration.md](references/narration.md)。

## 操作方式

单面卡：打开即见完整内容。**Space** 播放／暂停语音，**Enter** 记 Good 并继续，**1** 下一学习日再看。没有翻面、输入答案、选择题或“听完才能继续”。桌面端由 `scripts/single_face_addon.py` 实现，见 [review-and-delivery.md](references/review-and-delivery.md)；复习安排只在用户要求时调整，见 [review-planning.md](references/review-planning.md)。

## 学习研究依据

术语的定义＋例反例、理科的 worked example 与逐步解释、文科的论证图与因果图、加速语音的理解边界、阅读卡 Good 的含义：证据与适用边界见 [learning-science.md](references/learning-science.md)。

## 维护本技能

改规则时同步主文、references、生成器、样例与测试；运行 `python -m pytest scripts -q` 与一个真实小样的预览和截图检查。修改规则不等于授权重写用户已有的全部卡片。旧版生成器（v5 导图卡、teaching、quiz 等）已从当前版本移除，需要维护旧格式时从 git 历史 `4c66000` 取用。
