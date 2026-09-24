# Personalized Anki Skill

> **逢山开路，遇水搭桥。** 从材料理解到可实际使用的 Anki 单面阅读卡，普通工程障碍由制作端解决。

这是供 GPT／AI 制卡使用的 **anki-ccpt-skill**。用户只在 Anki 学习，AI 承担研究、概念组织、准确绘图、讲解、语音与导入验证。

入口是 [SKILL.md](SKILL.md)。先识别学习用途，实际核对官方 syllabus 与 assessment objectives；具体考试用法必要时查官方题目和评分资料。卡片说明知识是什么、为什么，以及它如何帮助完成已核实的考试任务，不把关键词清单当成完整 analysis / evaluation。

每张卡以内置 Xmind 式思维导图组织完整关系，节点表达开放。先研究可靠教材的学科图示，再按范围与理解需要采用、简化或创造更合适的表达；具体情境、文字、图、表格与交互互相补足，不设固定组件配方。每次版式设计应用一次 `emilkowalski-skills`，不反复读取用户 Xmind 风格库。术语用 English，常规解释用中文，公式规范排版；内容优先级与解释篇幅服务学习目标。

首要目标是让初学者凭当前卡读懂对象、含义与原因；宁可充分展开，也不让读者自行补主语、条件、术语或因果。记忆点服务理解，不靠口诀、装饰或压字数替代教学。依据与验收见 [理解与记忆研究](references/comprehension-and-memory.md)。

制作后逐卡检验理解、用途、表达与实际运行；图形和技术检查通过不等于教学完成。具体视觉实施见 [Xmind + Emil 设计说明](references/xmind-emil-design.md)。

## 听讲与操作

打开即见完整内容，无需翻面。每卡只有一个播音入口，按阅读顺序覆盖整页学习内容；图像采用讲图式叙述。默认微软云逸 `zh-CN-YunyiMultilingualNeural`，离线音频随包交付，实际 1.5×。免费 Edge 未提供该 voice 时需可用且已授权的微软 Speech 接口，不静默换声。见 [语音实施](references/narration.md)。

**Space 播音 → Enter（Good）继续；1 = 下一学习日再看。** Space 同时控制暂停、继续和播完重播，切卡停止音频。桌面评分适配见 [single-face.md](references/single-face.md)，仅改网页 Space 监听不能替代 Anki 原生快捷键适配。

## 当前个人复习配置

复习规则仅在用户要求配置时应用，不因安装 skill 自动改 Anki。

- 保留原生 Enter = Good，希望明天再看时按 1 = Again。快刷的 Good 不等同于独立 recall，不据混杂记录声称拟合了个人记忆能力。
- learning 与 relearning 各用单一 `1d`：Again 当天不再出现，下一 Anki 学习日再来；之后 Good 返回正常 FSRS，Again 再等一天。按 Anki 换日时间，而非精确 24 小时。
- FSRS desired retention 当前为 `0.88`（2026-09-24 用户指定）：保留自适应增长，相同 memory state 下比此前 `0.85` 更早复习。它不是固定增长系数或固定间隔上限，也不能消除错误评分带来的偏差。
- 这是个人节奏的试用设置，不宣称普遍最优。官方通常建议 FSRS 使用小于一天的 learning steps；这里因明确的当日不重复偏好采用 `1d`。
- 不自动优化混杂旧记录、不批量重排已有到期日。提高 retention 会增加复习量。新卡日上限如需解除，检查 preset、子牌组、当日覆盖和 review limit；9999 是实践上近似不限，不是数学无限。

依据和维护方向见 [review-planning.md](references/review-planning.md) 与 [Anki 官方 Deck Options](https://docs.ankiweb.net/deck-options.html)。

## 安装与制作

将本仓库完整放入 AI 工具的技能目录，文件夹命名为 `anki-ccpt-skill`，保留 assets、scripts、references 的相对路径。提供教材或真题、考纲范围和现有卡片去重要求，由 AI 读取 SKILL.md 执行。此仓库不是需要导入 Anki 的牌组，也不是 Anki 插件。

现有可调整的生成起点是 [scripts/build_logic_deck.py](scripts/build_logic_deck.py)，示例在 [assets/logic-example.json](assets/logic-example.json)，用法见 [logic-build.md](references/logic-build.md)。Python 依赖列在 scripts/requirements.txt；语音处理另需 FFmpeg。旧生成器仅用于维护旧卡，新卡优先按当前 SKILL.md 的设计目的制作。

仓库只包含规则、通用模板、示例和制作脚本，不包含个人 Anki 数据库、学习记录、原始试卷或音频库。现有 LICENSE 保留。
