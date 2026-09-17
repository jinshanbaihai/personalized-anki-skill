# Personalized Anki Skill

> **逢山开路，遇水搭桥。** 从材料理解到可实际使用的 Anki 单面阅读卡，普通工程障碍由制作端解决。

这是供 GPT／AI 制卡使用的 **anki-ccpt-skill**。用户只在 Anki 学习，AI 承担研究、概念组织、准确绘图、讲解、语音与导入验证。

入口是 [SKILL.md](SKILL.md)。制卡直接使用内置的 Xmind 式导图规则，不反复读取用户样例库；每次设计任务读取并应用一次 `emilkowalski-skills`，整批卡片复用，具体流程见 [Xmind + Emil 设计说明](references/xmind-emil-design.md)。以概念导图卡呈现定义与关系，以讲图卡解释空间、变化与原理；足够完整的中文解释配合 English 学科概念（包括 price 等常见词在学科中的用法，覆盖标题、分支、图标签与语音），让当前概念的完整关系尽可能在一页看清。它提供设计方向，不把所有学科锁进一种模板；不默认生成四选一。

## 听讲与操作

打开即见完整内容，无需翻面。每卡只有一个播音入口，按阅读顺序覆盖整页学习内容；图像采用讲图式叙述。默认微软语音，离线音频随包交付，实际 1.75×。

**Space 播音 → Enter（Good）继续；1 = 下一学习日再看。** Space 同时控制暂停、继续和播完重播，切卡停止音频。桌面评分适配见 [single-face.md](references/single-face.md)，仅改网页 Space 监听不能替代 Anki 原生快捷键适配。

## 当前个人复习配置

复习规则仅在用户要求配置时应用，不因安装 skill 自动改 Anki。

- 保留原生 Enter = Good，希望明天再看时按 1 = Again。快刷的 Good 不等同于独立 recall，不据混杂记录声称拟合了个人记忆能力。
- learning 与 relearning 各用单一 `1d`：Again 当天不再出现，下一 Anki 学习日再来；之后 Good 返回正常 FSRS，Again 再等一天。按 Anki 换日时间，而非精确 24 小时。
- FSRS desired retention 暂用 `0.95`：保留间隔随熟悉程度增长，同时比默认 `0.90` 更早安排复习。它不是固定增长系数或固定间隔上限，也不能消除错误评分带来的偏差。
- 这是个人节奏的试用设置，不宣称普遍最优。官方通常建议 FSRS 使用小于一天的 learning steps；这里因明确的当日不重复偏好采用 `1d`。
- 不自动优化混杂旧记录、不批量重排已有到期日。提高 retention 会增加复习量。新卡日上限如需解除，检查 preset、子牌组、当日覆盖和 review limit；9999 是实践上近似不限，不是数学无限。

依据和维护方向见 [review-planning.md](references/review-planning.md) 与 [Anki 官方 Deck Options](https://docs.ankiweb.net/deck-options.html)。

## 安装与制作

将本仓库完整放入 AI 工具的技能目录，文件夹命名为 `anki-ccpt-skill`，保留 assets、scripts、references 的相对路径。提供教材或真题、考纲范围和现有卡片去重要求，由 AI 读取 SKILL.md 执行。此仓库不是需要导入 Anki 的牌组，也不是 Anki 插件。

当前推荐生成入口是 [scripts/build_logic_deck.py](scripts/build_logic_deck.py)，示例在 [assets/logic-example.json](assets/logic-example.json)，用法见 [logic-build.md](references/logic-build.md)。Python 依赖列在 scripts/requirements.txt；语音处理另需 FFmpeg。旧生成器仅用于维护旧卡，新卡优先按当前 SKILL.md 的设计目的制作。

仓库只包含规则、通用模板、示例和制作脚本，不包含个人 Anki 数据库、学习记录、原始试卷或音频库。现有 LICENSE 保留。
