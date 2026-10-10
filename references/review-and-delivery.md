# 审查、交付与原生操作

## 一、内容审查（先于版式）

1. **冷读每张卡**（关掉语音）：读完能否说出主干与理由？哪一句会让基础不稳的读者停下来？定义里的每个词是否讲过作用？推导是否有跳步？因果链的每个箭头是否成立？发现问题就补解释或拆卡。
2. **关键词复现测试**：只看卡组，写出 MS 要求的定义关键词、推导得分步骤、结论句、essay 的 AO1/AO2/AO3 骨架。写不出的就是缺口。
3. **双向核对**：按 [coverage-ledger.md](coverage-ledger.md) 回扫考纲原文、板书点与真题需求清单（每条 demand 都能指出准备它的卡）；生成器的 `coverage` 报告只能证明连线没断，考点清单本身是否漏项要人读原文判断。
4. **独立评审**：内容成形后，交给没有参与制作的审阅者（子 agent），给它考纲条目、MS 摘录、板书和卡片预览，要求：找遗漏、误读、超纲、讲不透的地方，并对每条给出可执行的改法。采纳后让审阅者复查改动部分与整组连接；旧版通过不代表新版通过。没有子 agent 时，作者分开做冷读、反例检查和范围回扫，并如实说明。
5. **数值核算**：所有计算、概率、系数、图中数值用工具复算一遍。
6. **真题回查留痕**：上面第 2 步与 coverage-ledger 的“只凭卡组作答 2–3 道问法不同的真题”都要记进 deck.json：`coverage.backcheck`（每道题的 paper、series、q、结果 pass／gap、补救的卡）与 `coverage.coldread`（冷读关键词测试里写不出的词与补救的卡）。`status: complete` 至少要有两道不同考季的回查；交付说明引用这些记录，不只说“已回查”。
7. **隐私复查**：全文搜一遍姓名、考生号、中心号、日期、邮箱、总分与“你的卷面／你丢”式写法（生成器会拦下常见写法，但拦不住姓名）。批改卷只按“题号 + 分点 + 是否得分”记录。板书卡逐张看 `out/media/ccpt6-board-*.png`：区块里出现的姓名、日期、学号、班级用 `masks` 涂掉后重建（生成器认不出图里的字）。
8. **板书卡复查**（有板书卡时）：每张卡的区块是否正好覆盖这个知识点（没漏掉老师补在别处的红笔、没混进别的知识点）；行框是否框在正在讲的那一行；语音是否讲了为什么与得分点，而不只是念板书；板书没写、考试要的内容是否有紧随其后的补充卡。

**警告怎么处理**（`report.json` 的 `deck_warnings` 与每张卡的 `warnings`）：

| 类别 | 警告 | 处理 |
|---|---|---|
| must-fix | 空泛箭头（没写哪个变量往哪边变）、含代数的 trivial 步、推导步缺“为什么”、卡面上 `$…$` 之外的纯文本数学、`speech_lint` 报出的难读符号与拼接错读 | 交付前改掉；改不了的逐条写理由 |
| explain-in-delivery | 同节相邻的 `adjacent` 考点、超过三成判为 1.5×（附 `style.speed_review` 与逐卡原因）、术语台账（给出真实总数与前几项的处理）、豁免字段（`*_waived`） | 交付说明里如实列出 |
| 参考 | 关系词不在规则表、导图分支偏宽、长节点 | 看截图后决定 |

## 二、版式与渲染

```bash
python scripts/build_cards.py deck.json out/ --preview
node scripts/render_check.mjs out/ --phone --dark
```

找不到浏览器时先试 `which chromium chromium-browser google-chrome`，找到就用 `CHROMIUM_PATH=<路径> node scripts/render_check.mjs …`（Playwright 不在全局路径时再设 `NODE_PATH`）。`render_check` 在真实 Chromium 中打开每页，桌面 1280×800、手机 390×844、亮／暗两种模式截图到 `out/check/`，并用 `ccptAudit()` 检查：正文不小于 15px、界面小字不小于 12px、数学上下标不小于 9.5px、没有横向滚动、手机上没有被横向截断的公式、没有被截断的块、导图节点不重叠、每页恰好一个播放器、无脚本错误。`ccptAudit()` 另查板书图片是否都加载（`brokenImages`）、显示比例是否低于原像素的 0.45（`boardScale`，手写字会太小：裁窄或拆块）。程序通过后仍要**看截图**：层级是否一眼可辨，图是否清楚，长卡在正常字号下是否读起来顺；板书卡看亮、暗两种截图里白底是否融进纸色、红蓝笔迹是否仍可分辨。读着累的卡要重新分卡，不靠缩小字号。

**没有 Node 或 Chromium 时**（常见于 Claude 网页版的沙盒）：① 冷读 `out/pages.json` 里每页的可见文本，专找重复注释（“优点（优点）”）、残留标签、未翻译的长英文句和表格里挤成一列的内容；② 跑 `python scripts/contrast_check.py` 检查配色；③ 把一两张代表页（一张导图或因果链、一张推导）的 `out/<id>.html` 交给用户先打开看一眼；④ 交付说明写明“未做截图检查”。

## 三、语音

```bash
python scripts/speech_backend.py --check --voice xiaoxiao     # 服务与声音是否可用
python scripts/speech_backend.py --probe /tmp/probe.mp3       # 实际合成一段
python scripts/build_cards.py deck.json out/                  # 合成全部语音并打包
```

缺 ffmpeg 时构建以 `ffmpeg_missing` 停止并给出安装命令（不是语音服务的问题）。检查：音频可解码；成品时长与“修剪后原速 ÷ 速度”一致（生成器自动校验）；段间没有超过设计停顿的空白；听一遍 `term-sampler.mp3` 确认 English 术语与缩写读音，读错就改 `speech_lexicon`；公式读法表达含义；讲图时先说看哪里；Space 暂停续播、结束重播、切卡停止；点速度按钮可在 2×／1.5× 之间切换且音高不变；1.5× 卡都有理由。`node scripts/render_check.mjs out/ --play` 在 Chromium 中实际按 Space 播放、检查高亮与切速。规则见 [narration.md](narration.md)。语音服务不可达时用 `--audio-pending` 先交付图文包（页面明示“语音待补”，播放器禁用）；交付文件夹里会写出 `deck.json` 和按步骤编号的 `补语音.txt`（安装 Python、依赖与 ffmpeg，检查语音服务，带 `--term-sampler` 重建，导入后原位补上语音），**整个文件夹一起交付**。不静默换声音。

## 四、打包与导入验证

```bash
pip install -r scripts/requirements-validate.txt                          # 一次性：anki 后端，约 30 MB
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json   # 语音待补的包会被识别并报告 audio_pending_cards
python scripts/validate_package.py out/<牌组>.apkg --require-audio            # 成品包：每页都必须带可解码的语音
```

装不上 anki 时跳过这一步，交付说明写“未做导入验证”。在临时空 collection 中导入，检查每张卡单页、一个播放器、媒体可解码、无缺失媒体；再做一次真实评分后重复导入，确认卡片身份、排程与 revlog 不变。这一步不等于桌面操作测试。

## 五、单面卡的桌面操作

用户只看一页完整内容，没有题目面、翻面、输入答案或选择题。**Space** 播放／暂停／继续／重播语音，不评分；**Enter** 记 Good 并进入下一张；**1** 记 Again，下一个 Anki 学习日再看。

实现：question 与 answer 模板显示同一页；每次构建都在输出目录写出 `ccpt_single_face.ankiaddon`（也可 `python scripts/package_addon.py 目录/`），用户双击即安装（重启 Anki）。插件只对模板含 `data-ccpt-single` 的卡生效：首次显示后自动切到可评分状态，接管 Space／Enter／1，长按不连发，其他卡与编辑器不受影响；学习步长按下文在首次复习时自动设置一次；复习中从不弹对话框。插件通过公开钩子 `gui_hooks.state_shortcuts_will_change` 改写 reviewer 的 Space／Enter／1；需要 Anki 2.1.50 或更新（manifest `min_point_version`），接口缺失时只提示、不接管按键。牌组设了“不自动播放音频”时 Anki 会要求点击才能出声，插件只对 CCPT 卡解除这一限制（CCPT 音频从不自动播放），所以 Space 照常播音；页面里只处理 Space，Enter 与 1 交给宿主（浏览器预览窗等不受影响）。已核对 Anki 26.09.3（aqt 26.9.3）源码中这些接口与钩子均存在；26.x 的作答键来自可配置的 `get_answer_key`，插件在 `1` 被改键时会补回。Anki 升级后先在测试 profile 复核。

**“1 = 下一学习日再看”依赖牌组的学习步长**：Anki 默认步长（1m、10m）下，按 1 的卡和 Enter 的新卡会在当天几分钟后再出现。所以插件第一次显示某个牌组的 CCPT 卡、而它的学习或重学步长短于 1 天（或为空）时，自动给这个牌组的“家族”（共用同一预设的最高上级牌组，及共用该预设的子牌组）换上“CCPT 阅读（原预设名）”：克隆原预设（已有同名阅读预设则沿用，不重复克隆），只把新卡与遗忘卡的步长改成 1 天、leech 只加标签，其余设置（每日数量、FSRS、retention）不变；有自己预设的子牌组、只含非 CCPT 卡的牌组和筛选牌组不改。随后重建队列，屏幕上这张卡也按新步长评分；右下角提示改了什么、如何撤销，不弹对话框（评分用的 Enter 不会误点）。撤销：工具 → “CCPT：撤销阅读预设”，恢复插件记录的原预设，此后插件不再自动修改这些牌组（包括之后加在其下的子牌组）。决定按 Anki 用户（profile）与牌组记在插件配置里（工具 → 插件 → 配置），重启、重装插件都保留；`auto_reading_preset` 设为 false 则不自动改，每次启动只提示一次。两台电脑同步同一个集合时，这些决定各自记在本机，一台上撤销后另一台可能再次应用，需要时在另一台也撤销一次。工具菜单“CCPT：牌组使用阅读预设（1 = 隔天再看）”是后备：它找出所有含 CCPT 卡（标签 ccpt6 或单面模板）的牌组，与当前选中的牌组无关，列出名单确认后应用；撤销过的牌组也可由此重新启用。FSRS 关闭时 Enter 的新卡隔天出现；开启 FSRS 时 Enter 的新卡间隔由 FSRS 决定（不会是当天），按 1 仍是下一学习日。AnkiMobile／AnkiDroid 不加载桌面插件：卡片仍是同一张完整页面，点页面上的播放键听讲解（2×／1.5× 键同样可用），先点 Show Answer 再点 Good／Again（AnkiDroid 可在设置里把手势或音量键映射到这两个按钮）；预设在桌面改过一次即随同步生效；只用手机、从不在桌面复习的用户要在牌组选项里手动把学习步长与重学步长都设为 `1d`（leech 选“仅标记”）。交付时把这些告诉用户。

实测项：打开卡即见完整内容；Space 只控制语音；Enter 一次 Good；1 一次 Again 且 due = 下一学习日；切卡停止旧音频。评分测试在测试 profile 或测试后立即撤销，并核对原卡状态与 revlog，不污染学习历史。插件的自动测试（源码仓库的 `scripts/test_addon.py`）用模拟的 aqt 调用 Space／Enter／1 的快捷键回调，并在真实 anki 集合上核对按 1 与 Enter 后 due = 下一天、不是几分钟后；它没有在真实 Anki 窗口里按键，桌面按键仍需在测试 profile 里实测一次，没测时交付说明照实写。

## 六、原位更新与新旧卡

- GUID = `namespace` + 卡 `id`。更新已有卡时两者都不能改；新卡用新的 `id`。拆分旧卡时，旧卡承接最接近的一个目标，拆出的部分用新 `id`。
- 先读取实际集合中的 note GUID、StableID、note／card ID、notetype 与牌组，再决定映射；不凭旧作者文件猜。
- 旧版本 skill 生成的卡（v5 导图卡，字段 FrontHTML／BackHTML）要改用 ccpt-6 时：先导入一个 ccpt-6 包让新 notetype 存在，在 Anki 浏览器里选中旧卡 → Change Note Type → ccpt-6（BackHTML → Page，StableID → StableID，Source → Source），复习历史随卡保留；再用同一 GUID 的 deck.json 生成新包导入覆盖内容。整个流程先在集合备份或测试 profile 中走一遍。
- 共享 notetype 的模板改动影响该类型全部卡，改前确认不会破坏未改的旧卡。
- 只操作用户授权的牌组；调度设置按 [review-planning.md](review-planning.md)，只在用户要求时改。例外：插件按“1 = 下一学习日再看”的设计，在首次复习时把 CCPT 牌组的学习与重学步长设为 1 天：只改含 CCPT 卡的牌组家族，记录原预设，提示一次，可从工具菜单撤销，撤销后不再自动改。

## 七、交付说明

告诉用户：

- 锁定的考试与证据；有假设时（考季、另一候选考试）放在第一行，并说明另一种情况会改变哪些卡。
- 实际读过的考纲、MS、ER、范文与真题考季（以及取不到的）；真题需求清单的条数与饱和依据。
- 考点总数、卡数与覆盖状态；同节相邻、留给下一批的考点（`adjacent`）逐条列出，用户说一句即可续做。
- 板书中看不清（`legibility: low`）或更正的位置：看不清的请用户补发原始导出（例如 ClassIn 原图），补来后原位更新。板书卡的原图宽度不足 800 px 时（报告逐卡警告）同样请用户补发原图。
- 有板书卡时：哪些知识点做成了板书卡、哪些补了文字卡及原因；`not_shown` 的板书点逐条列出；`board/` 里的板书副本只含卡片用到的区块、遮挡已涂上；请用户在真实客户端的夜间模式看一张板书卡（Anki 桌面、AnkiDroid、AnkiMobile 都应显示为深底浅字）。
- 语音状态：已合成，或待补（照 `补语音.txt` 的步骤补；补完后可选听一遍 `term-sampler.mp3`，读错的词告诉 Claude）。
- 交付物是**整个输出文件夹**：`.apkg`、`ccpt_single_face.ankiaddon`、`deck.json`、`report.json`，语音待补时还有 `补语音.txt`。`deck.json` 是续做与补语音的依据：在新的对话里接着做时，把它（或上次的 .apkg）和交付说明一起交给 Claude，新对话不会记得上一次的内容。
- 实测范围：导入验证做了没有、截图检查做了没有、桌面按键（Space／Enter／1）是在真实 Anki 里试过还是只在测试里模拟过，如实写。
- 隐私：交付文件（含 deck.json、交付说明）不写学习者姓名、考生号、日期与总分；批改卷只记题号和分点。学习者想知道总分时在对话里说，不写进文件。
- 首次使用：双击安装 `ccpt_single_face.ankiaddon`、重启 Anki、导入 `.apkg`；第一次复习时插件会自动把 CCPT 牌组设为阅读预设并在右下角提示（不想要：工具 → CCPT：撤销阅读预设）；只用手机的用户请在牌组选项里把学习与重学步长设为 1d。导入后先在真实客户端看一张导图卡和一张推导卡，确认字体、公式与图都正常。
- 工程检查、制作者判断和用户实际体验分开说，不把程序通过说成学会了。
