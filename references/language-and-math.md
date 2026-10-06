# 语言、术语与数学排版

## 中文讲解，English 术语

中文负责叙述、连接与解释；**凡在本学科中承担概念、量、关系、过程或判断标准的词，用考试使用的 English**。判断标准是它在当前语境里的作用，不是词有多难：price、quantity demanded、income、sample、frame、unit、force、mass 这类看似日常的词，作为学科概念时同样用 English。

- 同一概念全卡组只用一个 English 名称（quantity demanded 不随手缩成 demand；net benefit 不混成 profit），标题、导图节点、图中标签、公式说明和语音一致。
- 术语第一次出现时用中文讲清它指什么；缩写先给全称（MSC = marginal social cost），之后再用缩写。不默认每次出现都加括号翻译。
- 定义本身用考试原文（English），旁边用中文讲解整句意思；考试要写的是 English 定义。
- 术语以锁定考纲、MS 与官方教材用词为准，不生造英文词组，也不为了“更英文”引入超纲概念。
- 完整短句仍按中文语法组织，不写成中英词语随机拼接的句子。

示例：“下一单位的 willingness to pay 高于 price，所以继续购买能增加 net benefit。”

## 数学与公式

- 一律写 LaTeX，构建时转成 MathML，卡面显示真正的分式、上下标、根号、向量和矩阵：`$\frac{MU_x}{P_x}=\frac{MU_y}{P_y}$`，不写 `MUx/Px`、`MU/price` 这类纯文本。
- 变量用本学科通行符号；公式旁用中文交代每个符号的含义与对应的 English 术语（“$P_x$ 表示 good X 的 price”）。
- 每个公式后写中文读法 `〔…〕`，语音按含义读（“X 的 marginal utility 除以 X 的 price”“245 分之 9”“1 加 4x 的三分之一次方”），不念排版代码，不逐个字母拆读。
- 读法示例（读“含义＋结构”）：

  | 卡面 LaTeX | 〔读法〕 |
  |---|---|
  | `(8+32x)^{\frac13}` | 8 加 32x，这个整体的三分之一次方 |
  | `\frac{9}{245}` | 245 分之 9 |
  | `X\sim B(n,\frac{9}{245})` | X 服从二项分布，参数是 n 和 245 分之 9 |
  | `P(X\ge 1)>0.95` | X 大于等于 1 的概率大于 0.95 |
  | `\frac{dV}{dt}=\frac{dV}{dx}\times\frac{dx}{dt}` | dV dt 等于 dV dx 乘以 dx dt |
  | `\pi\int y^2\,dx` | pi 乘以，y 平方对 x 的积分 |
  | `\mathbf r=\mathbf a+\lambda\mathbf b` | 向量 r 等于向量 a，加上 lambda 倍的向量 b |
  | `\sin^2 x` | sin x 的平方 |
  | `\binom{n}{r}` | n choose r，也就是组合数 |

  式子很长时先说一句“这一步把…化成…”，再读式子。希腊字母用英文名；读音不确定的缩写放进 `speech_lexicon`（见 [narration.md](narration.md)）。
- 数值计算、展开系数、概率、最小 n 等结果在写卡前用工具实际算一遍（Python、Wolfram），把核算方式记进 `research` 或卡的 `sources`。
- 比较符号前后留空格（`x < 2`）可直接写，显示为 <、读作“小于”；紧贴字母的 `MSB<MSC` 会被浏览器当成标签，生成器拒绝，写成 `MSB &lt; MSC` 或公式。
- 金额写 `\$2`：卡面显示 $2，朗读为“2 美元”；未转义的成对 `$` 会被当作公式。
- 行内长等式链（两个以上关系符号）会在关系符号前自动留出换行点，手机上折行；`\bar{x}` 自动排成横跨字母的横线，`\ln x`、`\sin x` 自动留出函数名后的细空格，`({-}\frac23)` 的负号贴紧数字。

## 强调与颜色

- 强调用来找重点：MS 必含词用 `definition.keywords` 高亮，关键结论用 `<b>`；不给所有 English 词都上色。
- 关系靠文字和箭头表达（`rel`、`chain`），颜色只是辅助；去掉颜色后关系仍可读。
- 正文与背景对比至少 4.5:1，大字至少 3:1（WCAG 2.2，1.4.3）；主题配色已按此设计，自定义 `css` 时保持。
