# 当前默认生成路径：混合内容导图

`python scripts/build_logic_deck.py input.json output_dir [--preview]` 调用 `build_map_deck.py`。依赖见 scripts/requirements.txt，语音还需 FFmpeg。当前模板不再继承旧 quiz 样式。先按 `exam-answer-first.md` 研究目标真题与可信人类作答，再设计教学与排版；程序能力不限制 AI 使用更好的表达。

批次：model_id、model_name、voice（省略即云希）、academic、syllabus{url,edition}、cards，可加css。卡片：id、namespace、deck_id、deck、title、target、width、height、root、nodes、edges、reading_order、sources、audit；学科卡还需 scope 与 exam_use。学科批次另需 exam_task，卡片需 answer_basis；旧输入要补真实研究后迁移，不能填空话绕过校验。纯渲染工程样例的 academic:false 不是学科制卡的逃生开关。

exam_task 含非空文字：qualification（例如已确认的考试及阶段）、authority（考试局／主办方）、version（适用考纲年份／考试格式）、component（卷别／skill／task）、task_type（用户要做的题）。syllabus 对 IELTS 等没有学科考纲的考试记录实际官方格式／assessment criteria 来源与适用版本，不虚构 syllabus code。

answer_basis 含非空文字：question_refs（实际题目标识和位置）、human_answer_refs（人类示范作者／发布者、来源及定位，可引用本批 sources 条目）、quality_review（结合分数／评语／官方要求说明可学和不可照搬之处）、marking_refs（匹配的评分来源）、answer_moves（本卡教的是哪段答题思路）、ai_additions（基于范文研究的新答案、改述、基础解释或假设案例，确实没有则说明）。此记录随卡保存到 Source 字段，不必把制作元数据挤进导图。卡面仍须有清楚的真实任务 hook 与作答用途。

程序只检查关键记录存在，不证明它们真实或充分。必须实际阅读并核对页码、作者、题目匹配与支持关系；人类示范不足的卡保留草稿，不能假填字段后导入。

nodes 每项有 id、x、y、width、html、speech，可选 style（root/branch/leaf/case/conclusion）。html 可含正文、table、MathML、SVG；节点内部组合不限单一形式。当前安全渲染器接受被动本地内容，若需动画或交互，显式扩展并测试，不退回文字。数学由作者提供 MathML，或用可信转换器将 LaTeX 转成 MathML；没有学科专用字符串替换词典。SVG需viewBox，准确性另用计算/标准模型核对。

edges 每条含 from、to、meaning；direction=down 可表示纵向连接，arrow=true 可加箭头。meaning用于制作者审查及图中title；若关系不能仅从位置与节点理解，必须把关系解释直接写在可见节点/图中，而非藏在tooltip。合并与交叉连接可用，不局限树形分类。

reading_order明确每个节点的整页讲解顺序，必须覆盖每节点一次且先根节点。speech是自然中文串联English术语的教学脚本，图和数表解释含义，不念排版代码。标题先读，后按reading_order；改布局须同步顺序。

输出单面HTML、cards.json、rendered.json、speech-manifest.json、apkg。模板字段FrontHTML/BackHTML仅为兼容名称，两者相同，qfmt/afmt均呈现BackHTML。制作端 `ccptAudit()` 输出节点边界、字号、重叠及组件计数；必须在真实目标窗口检查。该接口不自动评价讲解。

旧tree格式脚本为 `legacy_logic_deck.py --legacy-maintenance`，其余旧生成器同样需显式标记。assets/logic-example.json等为历史字段样例，不用于新任务。不要把旧JSON传给新生成器后忽略错误或静默丢字段。

原位更新沿用id/namespace/model与deck；测试牌组反而使用独立值。新包不可与既有namespace冲突。语音不可用先完成preview，未经用户同意不能静默改voice。

仅当用户另建审查测试组、目标voice不可用且未批准替换时，可用 `--text-only-test` 并在批次设置 `test_deck:true` 先交付图文审查。卡面显性显示语音待补、唯一播放器禁用，manifest标明available=false；这不是完整音频交付。验证器需显式 `--allow-text-only-test`，报告仍保留缺失。正式音频包不能绕过默认检查。
