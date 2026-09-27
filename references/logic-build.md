# 当前默认生成路径：混合内容导图

`python scripts/build_logic_deck.py input.json output_dir [--preview]` 调用 `build_map_deck.py`。依赖见 scripts/requirements.txt，语音还需 FFmpeg。当前模板不再继承旧 quiz 样式。先按 `exam-answer-first.md` 研究目标真题与可信人类作答，再设计教学与排版；程序能力不限制 AI 使用更好的表达。

批次：model_id、model_name、voice（省略即云希）、可选 narration_follow（真实音轨节点定位，单卡可覆盖）、academic、syllabus{url,edition}、cards，可加css。卡片：id、namespace、deck_id、deck、title、target、width、height、root、nodes、edges、reading_order、sources、audit；学科卡还需 scope 与 exam_use。学科批次另需 exam_task 与共享 answer_basis，卡片需 research_use（可覆盖 answer_basis）；新输入另含卡级 learning_unit 与批次 task_coverage，把局部教学与整题覆盖分开；不能填空话绕过校验。纯渲染工程样例的 academic:false 不是学科制卡的逃生开关。

exam_task 含非空文字：qualification（例如已确认的考试及阶段）、authority（考试局／主办方）、version（适用考纲年份／考试格式）、component（卷别／skill／task）、task_type（用户要做的题）。syllabus 对 IELTS 等没有学科考纲的考试记录实际官方格式／assessment criteria 来源与适用版本，不虚构 syllabus code。

answer_basis 可在批次共享，或个别卡需要不同来源时覆盖。先记录以下四项：question_refs（已读真题标识／位置与覆盖）、human_answer_refs（已读人类示范来源／作者及定位）、quality_review（评分／评语／官方要求如何支持其可用性及局限）、marking_refs（相应评分来源）。它们可引用批次 sources 的资料索引，记录真实阅读情况，不能只填“已检查”。同时记录 teaching_refs 与 difficulty_review；这六项均为生成前的非空检查项，但程序不能证明研究充分。其中前者定位读过的人类教学／典型错误材料，后者记录具体障碍、证据、采用的解释及承载节点。无需每张卡重写同一份研究。

每卡 research_use 简要说明共享研究怎样指导本卡的知识应用、选材、深度或重点；无需六项答题模板。仍兼容旧卡自己的 answer_basis.answer_moves；ai_additions 可按需记录，含 AI 原创完整答案时说明研究基础及核对，单卡可以只承担局部理解，整组应用要求另行映射，不能将局部完成伪称整题完成。最终有效研究和用途随卡保存到 Source 字段，制作元数据不挤进导图。

程序只检查其支持的记录结构，不自动验证教学依据或误区研究；新增的教学记录仍须实质审查。字段存在不证明来源真实或充分。实际阅读与研究充分性按 `exam-answer-first.md` 审查；证据不足不能假填字段。academic:false 只适用于真实非学科任务或明确工程样例，不能拿它绕过学科研究。

标题默认是 plain title，用于检索、元数据与无障碍说明；需要公式或术语强调时提供 title_html（与节点一样的被动 HTML／MathML）及 title_speech（自然语言朗读），避免把数学标记显示或念出来。标题与语音表达同一含义，不允许额外播放器。

nodes 每项有 id、x、y、width、html、speech，可选 style（root/branch/leaf/case/conclusion）。html 可含正文、table、MathML、SVG；节点内部组合不限单一形式。当前安全渲染器接受被动本地内容，若需动画或交互，显式扩展并测试，不退回文字。数学由作者提供 MathML，或用可信转换器将 LaTeX 转成 MathML；没有学科专用字符串替换词典。SVG需viewBox，准确性另用计算/标准模型核对。

edges 每条含 from、to、meaning；direction=down 可表示纵向连接，arrow=true 可加箭头。meaning用于制作者审查及图中title；若关系不能仅从位置与节点理解，必须把关系解释直接写在可见节点/图中，而非藏在tooltip。合并与交叉连接可用，不局限树形分类。

reading_order明确每个节点的整页讲解顺序，必须覆盖每节点一次；起点按理解路径选择，不强制根节点在先。speech是自然中文串联English术语的教学脚本，图和数表解释含义，不念排版代码。标题先读，后按reading_order；改布局须同步顺序。

输出单面HTML、cards.json、rendered.json、speech-manifest.json、apkg。模板字段FrontHTML/BackHTML仅为兼容名称，两者相同，qfmt/afmt均呈现BackHTML。制作端 `ccptAudit()` 输出节点边界、字号、重叠及组件计数；必须在真实目标窗口检查。该接口不自动评价讲解。

旧tree格式脚本为 `legacy_logic_deck.py --legacy-maintenance`，其余旧生成器同样需显式标记。assets/logic-example.json等为历史字段样例，不用于新任务。不要把旧JSON传给新生成器后忽略错误或静默丢字段。

原位更新沿用id/namespace/model与deck；测试牌组反而使用独立值。新包不可与既有namespace冲突。语音不可用先完成preview，未经用户同意不能静默改voice。

仅当用户另建审查测试组、目标voice不可用且未批准替换时，可用 `--text-only-test` 并在批次设置 `test_deck:true` 先交付图文审查。卡面显性显示语音待补、唯一播放器禁用，manifest标明available=false；这不是完整音频交付。验证器需显式 `--allow-text-only-test`，报告仍保留缺失。正式音频包不能绕过默认检查。

## 小范围教学与整组覆盖的数据

每卡 target 是本卡要讲透的小问题；learning_unit 含 starting_point（读者起点及本页如何提供必要背景）、boundary（本地范围与安排在别处的独立目标）、explanation_review（真实冷读发现、原因或对照解释怎样修复）。这三项是制作记录，不能替代可见的教学；卡面不必出现三个固定栏目。案例、问题数、分支数和表达方式不由字段限制。

批次 task_coverage 是数组，可支持多道已研究目标题。每项含 question（题目／指令与分值）、standard（适用最高评分要求）、worked_answer（已核对的制作端完整答案或定位）、reconstruction_review（从所交付整组重建的具体发现与连接检查）、status（partial 或 complete）、remaining（partial 时必须说明尚未覆盖的内容）。requirements 数组每项含 requirement、evidence、teaching，以及 locations；每个 location 为 card（本批卡 ID）与 nodes（该卡可见节点 ID 数组）。理解前提可以映射到其支撑的论证，并注明并非独立得分点。

局部小样可标 partial，不要求每张卡作答整题。标 complete 时应有实际的整组重建与连接检查，remaining 为空；程序不能验证作者的“完整”判断，仍按 full-credit-coverage.md 审阅。每张卡都应说明自己在该应用中的作用，不能为通过检查虚构得分。cards 顺序可表达首次教学次序，但 Anki 的复习顺序未必相同，卡内必须能够重新定向。

导出 Source 同时保存局部 learning_unit 和批次 task_coverage；学习正文不会被这些制作字段挤占。维护历史 per-card answer_coverage 时可显式传 --legacy-coverage-maintenance 保留旧结构，仅用于技术维护，不能用于新制卡或教学改版。新输入默认检查局部与整组两层；旧数据应实际重做范围与研究映射，而非只换字段名。

启用 narration_follow 后，生成器按标题和节点分别合成、解码实测再拼为一个整页 MP3。只有整页音频入包；rendered.json、speech-manifest.json 与 map-data 保存实际 cue。ccptAudit().narrationFollow 返回当前定位状态；preview 不提供未经合成的假时间点。所有教学节点始终可见，暂停不丢关注位置，结束和切卡清理。
