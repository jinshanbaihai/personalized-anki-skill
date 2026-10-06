# CIE 9708: the 2029 syllabus, change check

Checked 2026-10-06. Baseline: `syllabus-a-level.md` (digest of the 2026–2028 syllabus, Version 2, December 2025; "SYL V2" below). Page numbers "p." are printed pages of SYL V2, which equal PDF pages.

## 0. Result

**The 2029 syllabus PDF could not be obtained, so no change list can be given.** Its existence, file name and size are confirmed from a saved copy of the official 9708 page. Its cover, version, content, assessment and command words were not read.

- Do not assume that the 2029 syllabus repeats SYL V2. Nothing read here says whether it changes anything.
- For exams in 2026, 2027 and 2028, SYL V2 applies (SYL p.1: "Use this syllabus for exams in 2026, 2027 and 2028.").
- Before making cards for a candidate who sits 9708 in 2029, obtain `764392-2029-syllabus.pdf` and run the comparison in §3.

## 1. Evidence that the 2029 syllabus exists

| # | Fact | Source | Confidence |
|---|---|---|---|
| E1 | The official programme page lists five syllabus documents. Their link labels and paths are: "2023-2025 Syllabus (PDF, 645KB)" `/Images/595463-2023-2025-syllabus.pdf`; "2023-2025 Syllabus update (PDF, 139KB)" `/Images/633788-2023-2025-syllabus-update.pdf`; "2026 - 2028 Syllabus (PDF, 599KB)" `/Images/697423-2026-2028-syllabus.pdf`; "2026 - 2028 Syllabus update (PDF, 110KB)" `/Images/748950-2026-2028-syllabus-update.pdf`; **"2029 Syllabus (PDF, 649KB)" `/Images/764392-2029-syllabus.pdf`** | Saved copy of `cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-economics-9708/` (page title "Cambridge International AS & A Level Economics (9708)"). Drive `official-course.html`, ID 12FL6bWGTRBsnMfWoG3sNesbp8KE5ehuA, 538,798 bytes, uploaded 2026-10-02. Its sha256 `d8083fd5…eee2f7` matches the entry for that URL in the Drive manifest `fresh-downloads.json` (same folder). Local copy: `src/9708-SYL/official-page_2026-10-02.html` | High (official page; snapshot no later than 2026-10-02) |
| E2 | The page states: "The syllabus year refers to the year in which the examination will be taken." So "2029 Syllabus" is the syllabus for exams in 2029. The label names one year only, unlike "2026 - 2028". Whether the document also covers 2030 or later is unknown until its cover is read | Same page | High for the rule. The years on the cover are not verified |
| E3 | The page's "Syllabus updates / Summary of the changes" block describes the **2023** revision and refers readers to the 2023–2025 syllabus. That revision: six AS and five A Level topics, a new "International economic issues" topic, content moved between AS and A Level, fewer AOs, a new Section C in Papers 2 and 4, two-hour Papers 2 and 4. The block says it applies "for examination from June 2023 onwards". It says nothing about 2029 | Same page | High |
| E4 | WebSearch summaries (2026-10-06, eight queries in English and Chinese) repeat the E3 text as if it were the "2029 changes". **That attribution is wrong**: the page ties that text to 2023. No search result quoted any content of the 2029 PDF | WebSearch | — |
| E5 | The 2029 file differs from the 2026–2028 file. The local 2026–2028 PDF is 613,490 bytes, which is 599.1 KiB and matches the label "599KB". So the labels are KiB of the real files, and the 2029 PDF is about 649 KiB (≈ 664,600 bytes), some 50 KiB larger. File size says nothing about content: layout or accessibility changes could account for it | E1; `src/9708-SYL/2026-2028_syllabus.pdf` | High that it is a different file |
| E6 | The local 2026–2028 PDF is the current official file. Its sha256 `0f02e7ef…a7db0d8` equals the hash recorded for `Images/697423-2026-2028-syllabus.pdf` in the Drive manifest (E1). It also equals the `source_sha256` in the public repo `Mrmanwonder/Axon-Site@45a84e836e4f` (`curriculum/syllabi/sources.json`, entry 9708 "2026-2028") | Hash comparison | High |
| E7 | SYL V2 does not mention 2029. Its change page lists one V2 change only: "The weblink on page 38 has been updated." (p.43). p.38 tells teachers to "Check you are using the syllabus for the year the candidate is taking the exam." | `src/9708-SYL/2026-2028_syllabus.txt` | High |
| E8 | Cambridge appears to have published single-year "2029" syllabuses for several subjects in the same document-number range. Search-result titles: `763395-2029-syllabus.pdf` (IGCSE Computer Science 0265), `764165-2029-syllabus.pdf` (O Level Biology 5090), `764167-2029-syllabus.pdf` (O Level Combined Science 5129), `764368-2029-syllabus.pdf` (IGCSE (9–1) Physics 0972), plus `764163` and `764365`. Document numbers rise over time (2028–2030 syllabuses are 744xxx; the 9708 V2-era update is 748950). So 764392 was probably issued in 2026, after V2 (December 2025). Why these syllabuses cover a single year is not stated anywhere read here. A one-year bridge before a redeveloped syllabus is one possible reading, but it is **unverified** | WebSearch result titles (*pointer*) | Low to medium |
| E9 | The "2026 - 2028 Syllabus update" (748950, 110 KB) was not read. Its content is unknown. It may be the notice that goes with V2 (inference from the document number) | E1 | — |

## 2. Where the PDF was looked for (2026-10-06)

| Route | Result |
|---|---|
| `www.cambridgeinternational.org`, `www.cie.org.uk` (curl; WebFetch) | Blocked by the egress proxy (curl: no connection; WebFetch: EGRESS_BLOCKED) |
| Web archives: `web.archive.org`, `archive.org/wayback`, `archive.today` | Blocked (no connection, or 403) |
| Mirrors: syllabus.papacambridge.com, pastpapers.papacambridge.com, pastpapers.co, gceguide.cc, dynamicpapers.com, bestexamhelp.com, xtrapapers.co, savemyexams.com | Blocked |
| WebSearch (eight queries, English and Chinese, including the exact file name `764392-2029-syllabus`) | Confirms that "2029 Syllabus (PDF, 649KB)" is listed. No copy, no text, no change summary |
| GitHub code search: `"764392-2029-syllabus"`, `"748950-2026-2028-syllabus-update"`, `"2029 Syllabus" "9708"`, `"2029-syllabus.pdf" 9708/economics` | 0 hits for both file names. The other hits list 9708 only up to 2026–2028: `KanzaAkram/syllabus-ib-edexcel-ocr-aqa-` download report; `RokctAI/factory`, `Mrmanwonder/Axon-Site`, `CNTWDev/AIStudy`, `funteck123/divergencie-web` |
| GitHub repositories about 9708 updated since June 2026 (`sl080/Alevel-9708-Revision`, `vishal108bw-cloud/cie9708-economics`, `lisaelfishawi/a-level-economics-9708`, `renxudong117/economics-0455-9708-self-study`, `randomizerselection/oehler-huang-library`); file lists read from blobless clones | No 2029 syllabus. Where a syllabus version is named, it is 2026–2028 |
| Hugging Face dataset search ("cambridge syllabus", "9708 economics", "cambridge past papers") | Nothing |
| User's Google Drive: title and full-text searches for `2029`, `764392`, `748950`, "Use this syllabus for exams in 2029", "for examination in 2029" | Only the saved official page (E1). No 2029 PDF, no 2026–2028 update document |

## 3. Comparison to run when the PDF is available

When the user uploads `https://www.cambridgeinternational.org/Images/764392-2029-syllabus.pdf` (Drive, any name; or `registry/src/9708-SYL/2029_syllabus.pdf`):

1. **Verify the cover and version.** Check the years line ("Use this syllabus for exams in …"), the version and publication date in the "Important: Changes to this syllabus" box (SYL V2 has this on p.3), and the "Changes to this syllabus" page (SYL V2 p.43). Record the md5 and sha256.
2. **Extract the text page by page** with `pdftotext -layout` into `cie-9708/work/syl2029/pNN.txt`. Then run `cie-9708/work/scripts/parse_syl.py` on it. That script reads pages 15–34 only, so adjust the range if the pagination differs.
3. **Diff against the baseline below.** Record every change here with its 2029 page and the SYL V2 page.

| Area | SYL V2 baseline (page) | What to compare |
|---|---|---|
| Years, series | Exams in 2026, 2027, 2028; June and November series, plus March in India (p.1, p.38) | Years covered; series |
| Content overview, assessment overview | pp.9–11 | Topic list; paper list |
| Assessment objectives and weightings | AO1/AO2/AO3 (p.13). A Level weighting 35/40/25. Paper 3 47/40/13; Paper 4 33/37/30 (p.14) | Wording and weightings |
| Topic 7 The price system and the microeconomy | 47 items: 7.1 (5), 7.2 (4), 7.3 (6), 7.4 (7) on p.24; 7.5 (10) p.25; 7.6 (5) pp.25–26; 7.7 (5) p.26; 7.8 (5) p.27 | Item ids, stems and bullets against `spec-items.json` (key `9708`, level `A2`) |
| Topic 8 Government microeconomic intervention | 17 items: 8.1 (2) pp.27–28; 8.2 (5) and 8.3 (10) on p.28 | Same |
| Topic 9 The macroeconomy | 24 items: 9.1 (3) p.29; 9.2 (6) and 9.3 (7) p.30; 9.4 (8) p.31 | Same |
| Topic 10 Government macroeconomic intervention | 9 items: 10.1 (1) and 10.2 (5) p.31; 10.3 (3) p.32 | Same |
| Topic 11 International economic issues | 25 items: 11.1 (3) and 11.2 (5) p.32; 11.3 (4) and 11.4 (3) p.33; 11.5 (7) and 11.6 (3) p.34 | Same |
| AS content assumed | p.15; and p.36 "The AS Level content will not be the direct focus of questions on Paper 3." (same sentence for Paper 4) | Whether the rule still holds |
| Paper 3 | 1 h 15 min; 30 marks; 30 four-option MCQs; 17% of A Level (p.11, p.36) | Duration, marks, number of items, weighting |
| Paper 4 | 2 h; 60 marks; 33% of A Level. Section A: one compulsory data response question, 20 marks, four parts. Sections B (mainly micro) and C (mainly macro): one 20-mark essay each from a choice of two, not divided into parts (p.11, p.36) | Structure, choice, marks, essay format |
| Command words | 17 words on p.37: Analyse, Assess, Calculate, Comment, Compare, Consider, Define, Demonstrate, Describe, Discuss, Evaluate, Explain, Give, Identify, Justify, Outline, State | Additions, removals, changed definitions |
| Other | Calculators allowed; no formulae given (p.35); administrative-zone variants (p.39) | Any change |

4. **Then update** `syllabus-a-level.md` (§1, gap G2), `../versions.md` §2.2 and `../versions.json`. Change `spec-items.json` only if 2029 candidates are in scope; if so, add 2029 items under a separate version marker rather than overwriting the V2 items.

## 4. Consequences for card making

- **Exam in 2026–2028:** use SYL V2 and the existing registry.
- **Exam in 2029:** the registry's syllabus layer is unverified for that year. Tell the user that the 2029 syllabus exists (E1) but has not been read, and ask for the PDF before relying on topic codes, AOs, paper formats or command words.
- Exam-lock rule: a candidate's exam year selects the syllabus file. "No significant changes" (SYL V2 p.3) describes V2 against V1 of the 2026–2028 syllabus. It says nothing about 2029.

## Appendix. March and June 2026 Paper 3/4 materials (searched in the same pass)

**Staged.** Three page images of the **M/J 2026 9708/41 mark scheme**:

| File | Content |
|---|---|
| `src/9708-P4/2026-06_41_ms_pages/2026-06_41_ms_p05.png` | Section A, Q1(a) [4], 1(b) [4], 1(c) [6]: Japan extract; business-cycle evidence, commercial banks and the 2% inflation target, yen depreciation and the trade balance |
| `src/9708-P4/2026-06_41_ms_pages/2026-06_41_ms_p10.png` | Section C, Q4 [20], first page: essay on fiscal policy, the multiplier and a negative output gap. Indicative AO1/AO2 content |
| `src/9708-P4/2026-06_41_ms_pages/2026-06_41_ms_p11.png` | Q4 continued: further AO1/AO2 points, AO3 evaluation points, and the mark split "AO1 Knowledge and understanding and AO2 Analysis 14", "AO3 Evaluation 6" |

- **Provenance.** `randomizerselection/oehler-huang-library@029e00ef6d7f` (a teacher's lesson library):
  - `apps/library/a-level/lessons/9-2-3-business-cycle/assets/9708-s26-41-q1a-ms.png`
  - `apps/library/a-level/lessons/9-2-1-growth-output-gaps/assets/9708-s26-41-q4-ms-10.png` and `…-q4-ms-11.png`
- **Verification.** The images are PapaCambridge-stamped renders of whole MS pages. Each carries the header "9708/41 … Mark Scheme … May/June 2026 PUBLISHED" and the footer "© Cambridge University Press & Assessment 2026 … Page 5 / 10 / 11 of 14". md5 prefixes: d3cb7544, 1f7e7d8f, e561157e. OCR text is beside each image (`.txt`, tesseract; check against the image before quoting).
- **Watch-out.** p.10 contains the line "AO1 and AO2 out of 8 marks. AO3 out of 4 marks." This conflicts with the 14/6 split on p.11 and with the 20-mark essay scheme used since 2023. Treat 14/6 as correct. The teacher repo's `growth-output-gaps/README.md` flags the same inconsistency.

**Not found anywhere reachable** (Drive title and full-text search for `9708_m26`, `9708_s26`, `9708/4x/M/J/26`, `9708/32/F/M/26`, "Economics June 2026" and similar; GitHub code and repository search; blocked mirrors as in §2):
- every F/M 2026 (9708/32, 9708/42) and M/J 2026 (9708/31–34, 9708/41–44) question paper;
- every mark scheme except the three pages above;
- the March 2026 and June 2026 examiner reports.

**Pointers to existence (not usable as sources):**
- The teacher repo cites, and transcribes in lesson slides, these items. Its audit file lists sha256 hashes of local `9708_s26_qp_31`, `9708_s26_ms_31`, `9708_m26_qp_32` and `9708_m26_ms_32` PDFs.
  - M/J 2026: 9708/31 Q15, Q16, Q21; 9708/32 Q15; 9708/34 Q18; 9708/41 Q1(a), Q4; 9708/44 Q1(d) (8 marks).
  - F/M 2026: 9708/32 Q15, Q16.
  - Keys as the repo states them, to check against the MSs once they are held: s26/31 Q15 C, Q21 A; s26/34 Q18 B; m26/32 Q15 D, Q16 C.
- `nikhilsingh-official/cambridgeparser@e7be381a1cd5` (`src/constants/gradeThresholds.ts`, scraped from PapaCambridge) lists published 2026 grade thresholds for 9708 Paper 1 only (`9708_m26_12`; `9708_s26_11` to `_14`). So the 2026 threshold documents exist. Paper 3/4 rows are not in that file.
