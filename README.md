# anki-ccpt-skill

把老师板书、课堂截图、讲评 PDF 做成**为考试背诵服务**的单面 Anki 知识卡：

1. 从内容锁定排他性的考试（考试局、资格、单元代码、考纲版本、考季）；
2. 读官方考纲、多年真题与 mark scheme、examiner report、真实考生范文，标定每个考点要掌握到什么程度；
3. 用范围账本保证考点不漏、不越界；
4. 术语卡逐词讲透定义，理科推导每一步写清做什么、为什么、依据和得分点，文科用箭头因果链和不限层级的导图；
5. 按学科选择有美感的版式主题（editorial／paper／lab／blueprint／manuscript），亮色与夜间模式都适配；
6. 晓晓或云扬配音，默认 2×、复杂卡 1.5×，可随时切换；Space 播音、Enter 继续、1 明天再看。

从 [SKILL.md](SKILL.md) 开始。生成器入口 `scripts/build_cards.py`，数据格式见 [references/deck-json.md](references/deck-json.md)。

```bash
pip install -r scripts/requirements.txt     # 另需 ffmpeg；版式检查需要 Node + Playwright
python scripts/build_cards.py deck.json out/ --preview
node scripts/render_check.mjs out/ --phone --dark
python scripts/build_cards.py deck.json out/
python -m pytest scripts -q
```
