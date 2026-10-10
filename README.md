# anki-ccpt-skill

把老师板书、课堂截图、讲评 PDF 做成**为考试背诵服务**的单面 Anki 知识卡：

1. 从内容锁定排他性的考试（考试局、资格、单元代码、考纲版本、考季）；
2. 读官方考纲、多年真题与 mark scheme、examiner report、真实考生范文，标定每个考点要掌握到什么程度；
3. 用范围账本保证考点不漏、不越界；
4. 术语卡逐词讲透定义，理科推导每一步写清做什么、为什么、依据和得分点，文科用箭头因果链和不限层级的导图；
5. 按学科选择有美感的版式主题（editorial／paper／lab／blueprint／manuscript），亮色与夜间模式都适配；
6. 晓晓或云扬配音，默认 2×、复杂卡 1.5×，可随时切换；Space 播音、Enter 继续、1 明天再看。
7. 板书优先：有老师板书原图时，板书上写了的直接用原图做卡面，按知识点裁切拼接（`scripts/board_images.py` 先给出编号区块），语音讲解并逐行框出正在讲的位置；只有板书没覆盖的才写补充卡并标明“补充 · 板书未写”；改造旧卡组同样适用；
8. 亮色模式干眼友好：页面与面板都不亮于 `#f6f1e7` 纸色，白底板书融进纸色、夜间反相。

从 [SKILL.md](SKILL.md) 开始。生成器入口 `scripts/build_cards.py`，数据格式见 [references/deck-json.md](references/deck-json.md)。

依赖：Python 3.10+（`pip install -r scripts/requirements.txt`）、ffmpeg／ffprobe；板书识别另需 poppler（pdftoppm、pdftotext、pdfimages）与 tesseract（含 `chi_sim`）；导入验证需要 `pip install -r scripts/requirements-validate.txt`；版式检查需要 Node 与 Playwright（Chromium，可用 `CHROMIUM_PATH` 指定）。缺了哪一项怎么办见 SKILL.md 的“运行环境”。

```bash
pip install -r scripts/requirements.txt
python scripts/board_images.py board.png out/regions/   # 板书优先：编号区块与总览页
python scripts/build_cards.py deck.json out/ --preview
node scripts/render_check.mjs out/ --phone --dark
python scripts/build_cards.py deck.json out/
python scripts/validate_package.py out/<牌组>.apkg
python scripts/package_skill.py dist/        # 上传给 Claude 的 anki-ccpt-skill.zip

# 只在源码仓库：
pip install -r scripts/requirements-dev.txt && python -m pytest scripts -q
```
