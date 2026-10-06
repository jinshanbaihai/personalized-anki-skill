# 知识阅读卡的生成与数据

`python scripts/build_logic_deck.py input.json output_dir [--preview]` 调用 `build_map_deck.py`。按 `textbook-research.md` 从板书或其他输入识别知识与范围，完整研读相关教材章节和模型，提炼关系；按 `syllabus-coverage.md` 用 syllabus、essay、MCQ、mark schemes、实际可得的人类作答及教师提示查漏。研究与内部样卡可交替：已核实的局部关系可以先做 preview 检查阅读负担，研究记录必须如实标出未读和未核实部分；正式定稿前完成相关整章、整模型研究与覆盖复查。生成器只验证可追溯结构，不证明实际阅读、教学准确或覆盖无遗漏。

依赖见 `scripts/requirements.txt`，语音另需 FFmpeg。`assets/map-example.json` 是明确的非学科渲染 fixture；完整新 metadata 的可运行 synthetic fixture 见 `scripts/test_learning_units.py`，不能将测试内容冒充正式教学研究。旧 quiz/tree 生成器不是新任务入口。

## 批次与卡片

批次包含 model_id、model_name、cards；voice 省略时使用云希。可选 css 与 narration_follow（是否按真实音轨定位节点，单卡可覆盖）。按考纲制作的学科批次设 `academic:true`，还需 syllabus、exam_task、research_basis、knowledge_coverage；完整主题交付另需 assessment_checks。明确无考试目标的教材阅读或工程 fixture 可不启用 academic，无需编造考试材料；知识来源与教学审查仍必需。已有考试目标时不能借此绕过范围与研究要求。

syllabus 记录 url 与 edition。exam_task 含 qualification、authority、version、component、task_type 五个非空文本，确认实际考试、阶段、年份与题型；它限定研究范围，不要求每张知识卡取自一道题。非学科考纲型考试记录实际官方内容与 assessment criteria，不能虚构 syllabus code。

每卡含 id、namespace、deck_id、deck、title、target、width、height、root、nodes、edges、reading_order、sources、audit。学科卡另含 scope、research_use、learning_unit。sources 是非空定位文本数组，定位本卡知识解释所用教材页段、模型图或其他材料；可引用共享索引，但不能只有“来源可靠”。scope 写实际知识边界，research_use 简要说明研究如何影响本卡内容与解释。target 是本卡要读懂和记住的知识关系，不是必须回答的考题。

learning_unit 含 starting_point（本卡提供的最少重新定向信息）、boundary（局部关系与安排在别处的独立内容）、explanation_review（实际发现的缺口、删冗余和保留机制的理由）。它们是制作记录，不变成卡面固定栏目，也不要求每卡重新从零讲整章。

audit 保存实际内容和显示审查发现。程序只检查存在，制作者仍须审阅记录是否具体、卡面是否确实修复；“已检查、通过”不是实质验收。

## 研究记录 research_basis

批次共享以下非空文本；可以引用有可定位内容的研究索引，不为每张卡重复全文：

| 字段 | 记录内容 |
|---|---|
| input_trace | 板书、课堂资料或其他输入的页／区域与识别到的知识，待辨认处与范围判断；没有板书时如实说明本次教材或用户主题输入 |
| textbook_refs | 书名、作者、版次、完整章与相关页段、模型图定位；避免不同版次页码混用 |
| reading_record | 实际连续阅读的章首到章尾范围、完整模型段落与图注，读到的结构与尚未取得内容；不能用搜索摘要充数 |
| model_synthesis | 自己提炼的对象、假设、约束、机制、变化与边界及其关系；纯概念主题记录对应概念结构，不硬造数学模型 |
| source_review | 来源质量、模型约定、冲突处理与超纲部分怎样隔离；研究范围与卡片范围分别说明 |
| syllabus_refs | 适用官方 syllabus 版次、条目和页码，知识边界依据 |
| question_refs | 实际研读的 essay 与 MCQ 标识、定位、问法覆盖；未读或不可得处明确说明，URL 清单不等于已读 |
| marking_refs | 相配 mark scheme、评分等级与 AO 要求及实际使用位置，区分必需内容和可替代的 indicative content |
| examiner_refs | 实际读过的 examiner report／教师提示与位置、对内容的具体影响；不可得时记录限制与补证路径，不编造共识 |
| human_response_refs | 实际可得的完整人类作答及评分依据；材料缺失时明确限制和替代证据，不能用 AI 答案冒充，也不因此禁止已获充分教材和官方依据的基础卡 |

这些字段用于让研究可追查；非空文字不代表真实、充分或已经读完。正式研究仍按 `textbook-research.md` 审核。教材的完整阅读与模型提炼不授权把整章高级内容塞进卡片。

## 知识范围 knowledge_coverage

批次对象含 scope_id（范围稳定标识）、scope（与 syllabus 对应的本批范围）、status（partial 或 complete）、remaining（未覆盖内容）、required_core、items。status 描述本批声明范围；complete 的 remaining 必须为空，partial 必须明确剩余内容，不能用改名缩小范围掩盖用户要求尚未完成。

required_core 是研究阶段对板书、教材与 syllabus 逐项回扫后先形成的核心知识 ID 清单。items 必须保留这份清单中的每一项且分类为 core，不能通过删掉整行、改成 prerequisite／excluded 来伪装完成；尚未教的项留在 partial 清单中。它用于发现“已识别但制卡漏掉”的知识，不是第二份完整论述。不能从最终卡片倒生成 required_core 再宣称两表一致；清单本身是否遗漏，还须人工对原板书、原 syllabus 和教材关系完整回扫。

清单可以纠错。发现误识板书、混用考纲或错误纳入知识时，在既有 source_review 中记清原项、改后的范围、具体依据，以及重新回扫原材料和独立复核的结果，再同步修改 required_core 与 items。无需另建历史状态表；不能用“范围调整”掩盖用户仍要求完成的知识。程序继续检查两者一致，实质纠错是否成立由来源与独立复核判断。

items 是按 syllabus 条目拆出的知识要求数组；每项含：

- id：批次内唯一知识标识；syllabus_item：具体 syllabus 条目及分解位置；knowledge：需掌握的命题或关系；evidence：定位依据。
- classification：core（范围内核心知识）、prerequisite（理解所必需但非独立考纲要求）、excluded（教材出现但本批不应教学的内容）。
- reason：prerequisite 和 excluded 必填，说明必要性或排除理由；core 可补选材说明，不能凭分类名称宣布“在考纲内”。
- locations：`[{"card":"卡ID","nodes":["可见节点ID"]}]`。已教内容指向实际卡面；complete 时每个 core／prerequisite 都必须有位置。partial 可保留尚未教学项的空 locations，并在 remaining 说明缺口。excluded 的 locations 必须为空，避免一边标超纲一边出卡。

所有交付卡都须归属于 core 或有理由的 prerequisite；不要求每张卡绑定题目、完整范文或独立得分点。至少识别一个 core 条目；局部交付可以先教必要基础并把尚未交付的 core 留作空映射，不能只列排除项宣称主题完整。该结构能发现丢失已识别核心、缺映射、悬空引用和显式未完成，却不能自动发现研究清单一开始就漏了整条 syllabus、错误纳入超纲内容或节点只写了标签；两方向实质审查见 `syllabus-coverage.md`。

## 已有卡片的只读复用

先核对已有卡，准确且充分的知识可以计入覆盖；不必为它重写新作者 schema、重新生成音频或重新导入旧 note。批次可另列 existing_cards，每项如下：

```json
{
  "id": "existing-budget-income",
  "snapshot_path": "snapshots/budget-income.json",
  "sha256": "该快照文件原始字节的 SHA256，小写 64 位",
  "identity": {"collection": "实际 Anki profile 或 collection 标识", "note_id": 1001, "card_id": 1002, "model_id": 1003},
  "content_review": "实际核对的命题、条件、范围和解释是否充分，以及与本批知识要求的对应；不能只写通过"
}
```

这是格式示意，ID、哈希、说明必须替换为真实采集值。snapshot_path 默认相对于输入 JSON 所在目录解析，也接受绝对路径。id 是本批引用别名，不能与新增 cards 的 id 冲突；同一旧 card 不能换别名重复登记。knowledge_coverage 和 assessment_checks 的 locations 都可引用这一别名及快照节点 ID，包括完全由已有卡支撑的一次应用检查。

快照文件格式：

```json
{
  "identity": {"collection": "实际 Anki profile 或 collection 标识", "note_id": 1001, "card_id": 1002, "model_id": 1003},
  "capture_source": "实际采集位置与方法、对应卡面及复核材料位置",
  "captured_at": "实际采集时间及时区",
  "html": "<main><section id=\"income\">从旧卡实际可见页面采集的知识解释</section></main>",
  "nodes": [{"id": "income-change", "locator": "id:income"}]
}
```

采集的是实际呈现后的可见内容，而非未运行的 Anki 模板；先查看渲染结果与计算后的可见性，再保存需要核对的内容，去掉隐藏子树、脚本、样式表和模板。保留图表及必要上下文供人工比对，不凭空补写旧卡。节点 locator 支持 `id:元素ID`、`data-node:节点值`，或旧卡没有元素 ID 时的 `text:完整可见引文`；目标必须唯一、可见且包含知识文字。纯图节点应定位到与图合在一起的解释或图注，同时人工核对原图；文字匹配不能验证图形正确。不能把标题标签当作充分解释。

构建时核对文件存在、字节哈希、collection／note／card／model 身份一致，以及每个引用节点实际存在、非空且未被标为隐藏。没有快照、仅声明“existing”或只填外部路径不能计入覆盖。哈希一致只表示快照未换，不能证明内容准确或当前 Anki 仍相同；content_review 仍须实际阅读，旧卡发生改变后重新采集和复核。只核了保存快照时，报告明确说“已核对保存快照”，不能声称已检查实时 Anki。

existing_cards 仅参与覆盖校验，生成器只为 cards 内的本批新／授权改动卡生成 HTML、音频和 note。Source 保存旧卡身份、采集方法和时间、快照哈希、内容审查及引用节点的可见文字摘录，便于日后追查；不把不可复现的外部路径当唯一证据，也不把整个旧牌组塞进每张卡。原快照和相关复核图保存在本批研究材料中。

## 整组考试应用检查 assessment_checks

数组中的每项含 question_refs、marking_refs、application_review 三个非空文本及 locations。记录代表性 essay／MCQ 的具体来源、对应评分依据，以及从已教知识重建分析、识别条件、评价或作出判断时发现的具体结果与缺口。locations 指向支撑检查的卡与可见节点；无需覆盖每张基础卡，也不能将其全包装成评分点。

完整主题（knowledge_coverage.status 为 complete）至少有一项实际应用检查；局部／阶段性交付可以暂不填，不能因此声称整主题或考试覆盖完成。发现尚未补齐的知识缺口，就回改内容或标 partial。软件验证不判断样题选择是否充分，几题成功也不是未来所有题无遗漏的保证。

## 页面与音频

标题默认 plain text，用于检索和无障碍说明；有公式或强调时提供 title_html（被动 HTML／MathML）及 title_speech（同义自然朗读），不额外添加播放器。

nodes 每项含 id、x、y、width、html、speech，可选 style（root/branch/leaf/case/conclusion）。html 可混合正文、table、MathML、SVG；形态服务关系，不固定图文比例或节点数。被动本地内容由当前 renderer 支持；必要交互须扩展并验证，不能删知识来适应旧组件。数学使用 MathML 或可信转换，不用学科词典粗替换。SVG 需 viewBox，图形正确性另用计算或标准模型核对。

文字中的小于号写为 `&lt;` 或规范 MathML。裸写 `MSB<MSC` 可能被浏览器当作标签，连后面的解释一起吞掉；生成器会拒绝非标准 HTML／SVG／MathML 标签，并检查可能吞句的开标签与必须成对的元素；HTML 合法省略结束标签仍可使用。这个检查保护内容完整性，不代替实际冷读和渲染审查，也不自动判断每个标准元素在当前浏览器的显示支持。

edges 含 from、to、meaning；direction=down 支持纵向连接，arrow=true 可加箭头。meaning 是制作审查记录及图中 title；读者理解所需的关系必须在卡面可见，不能藏进 tooltip。分流、合并和交叉关系可以存在，不强制树形分类。

reading_order 必须包含每个节点且恰好一次；按阅读逻辑选择起点，不强制根节点先读。speech 自然串联中文和 English 术语，辅助卡面阅读；图和数表解释含义，不念排版代码或无用读数。先设计轻量而充分的可见知识，再写对应语音，不能用音频补卡面缺失。

启用 narration_follow 后，标题和节点分段合成，经解码实测后拼成唯一整页 MP3，记录真实 cue；只有整页音频入包。所有教学节点始终可见，布局不追逐高亮；暂停保持位置，结束和切卡清理。preview 不生成猜测时间点。

## 输出、维护与验证

输出单面 HTML、cards.json、rendered.json、speech-manifest.json、apkg。FrontHTML/BackHTML 是兼容字段名，两者内容相同；qfmt/afmt 都显示 BackHTML。Source 保存本卡知识来源、研究应用、learning_unit 及共享研究／知识覆盖／应用检查，制作 metadata 不占卡面。Anki 字段仍按 HTML 存储，Source 的 `<`、`>`、`&` 使用 JSON 自身的 Unicode 转义；`json.loads` 必须恢复完全相同的对象，不能整体 HTML 转义破坏旧读取端。

`ccptAudit()` 报告实际窗口的节点边界、文字字号、缩放、溢出、重叠及组件数。渲染结果仍须看截图；大画布缩到窗口并不证明读起来轻松，过密需重写和拆分。单面播放器、媒体打包、原位身份与历史保护继续按 `acceptance.md`、`single-face.md` 和 `native-delivery.md` 验证。

原位更新先读取实际 note GUID、StableID、note/card ID、model 和 deck，再决定对应的新单元；旧作者文件中的同名牌组 ID 不一定等于当前原生 ID。已有 GUID 直接保留，不凭猜测重算 namespace。原卡承接最接近的一个目标，拆出的新关系另建稳定身份；隔离测试组使用独立值。

共享 notetype 的模板修改会影响未改旧卡。若同一 model 中仍有旧 renderer，先在只读备份的隔离 collection 中验证两套样式与脚本的兼容分派，不能直接覆盖旧 CSS／JS，也不能因全局选择器相互污染而只做简单追加。以真实拟导入包导入两次，核对旧卡全部身份、排程与 revlog、未改 note 字段、notetype 未意外克隆；同时比较未改旧页与新页的实际呈现和切卡清理，再执行正式原生导入。不得另开 backend 写正在运行的 live collection。

语音失败先完成 preview 并诊断，不静默换 voice。仅在授权的图文测试组可用 `--text-only-test` 与 `test_deck:true`；页面显性标明音频待补，播放器禁用，manifest 的 available=false；正式音频包不能绕过默认检查。

`--preview` 不合成语音；匹配的本地音频须能实际解码才可播放。没有可用音频时页面显示“图文预览，未生成语音”，禁用播放器与其 Space 操作，不请求不存在的音频文件。已有真实可用音频的 preview 保持播放、暂停和继续；运行时媒体失败应显示失败原因，不能回显“已暂停”误导用户。preview 始终不生成 apkg。

历史 answer_basis 与 per-card answer_coverage／shared task_coverage 仅通过 `--legacy-coverage-maintenance` 进行明确的技术维护；新制卡和内容改版必须使用本页知识结构。旧 tree／quiz 维护另用对应生成器的 `--legacy-maintenance`。不能静默丢弃旧字段后冒称已完成内容迁移；本规则不要求为纯样式或音频修复重写既有知识。
