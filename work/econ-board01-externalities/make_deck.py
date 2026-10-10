"""Builds work/econ-board01-externalities/deck.json: board cards for what the board shows; the rest stays on the old cards."""
import json, sys
from pathlib import Path

OUT = Path(sys.argv[1])
SRC = 'source/board.png'
OLD = '旧卡组（cie-alevel-a2-econ-from260917 · 板书01，已在 Anki 中）'
L2 = '图不准确最高 L2（9708/42 F/M 2024 Q2 MS pp10–11）'


def crop(box, where, points, speech='', spots=(), annotate=None):
    c = {'box': list(box), 'where': where, 'points': list(points)}
    if speech:
        c['speech'] = speech
    if spots:
        c['spots'] = [dict({'box': list(b), 'speech': s}, **({'step': True} if st else {})) for b, s, st in spots]
    if annotate:
        c['annotate'] = annotate
    return c


def kid(rel, text, kind='topic', *grand):
    n = {'rel': rel, 'text': text, 'kind': kind}
    if grand:
        n['children'] = [kid(*g) for g in grand]
    return n


def note(need, exam, text, *children):
    """The annotation beside a crop: why the board may be misread here, the exam requirement it serves, a small map."""
    return {'need': need, 'exam': exam, 'root': {'text': text, 'children': [kid(*c) for c in children]}}


def card(cid, title, covers, crops, notes=(), lead=None):
    blocks = []
    if lead:
        blocks.append({'type': 'lead', 'text': lead})
    blocks.append({'type': 'board', 'src': SRC, 'crops': crops})
    for label, text in notes:
        blocks.append({'type': 'note', 'tone': 'warn', 'label': label, 'text': text})
    return {'id': cid, 'genre': 'board', 'title': title, 'covers': covers, 'sources': ['本课板书 board.png'], 'blocks': blocks}


cards = [
 card('BD-I02', '负外部性：providing information 怎样减少有害消费', ['I02'], [
   crop((40, 312, 1262, 870), '板书开头：政策 3 providing information（提供信息）', ['BP03'],
        '看板书开头这一块：政府提供信息，用来减少 negative consumption 和 production externality。',
        [((50, 376, 1255, 614), '第一条路径针对消费者自己。很多有负消费外部性的商品同时是 demerit good，消费者因为 information failure 低估了对自己的危害；知道以后，感知到的净 benefit 下降，就会少买。', False),
         ((58, 630, 1192, 808), '第二条路径针对第三方损害。对有 negative production externality 的商品，信息提高消费者的 social responsibility，比如告诉他们保护环境对下一代有利，人们关心下一代，也会少用这些商品。', False),
         ((58, 816, 935, 870), '执行手段：广告牌、电视、广告平台和网络。注意，信息起作用要靠改变选择：行为改变时 demand 左移，quantity 下降；宣传本身不会降低每单位的 MSC，知道有污染也不等于一定愿意少买。', False)]),
   crop((35, 2575, 738, 2652), 'air travel 评分方案最后一条', ['BP11'],
        '评分方案也把 negative advertising 列为一种干预：需求下降，航班减少，可能达到 allocative efficiency。考试里要说清是信息改变了 demand 本身，这和税不同。')]),
 card('BD-I05', 'Information 的局限：要花钱，还要有说服力', ['I05'], [
   crop((60, 895, 1150, 1130), '板书：providing information（提供信息）的缺点', ['BP04'], '',
        [((60, 955, 252, 1003), '第一个缺点：贵，需要花钱。反复宣传占用预算，钱也可以用在别处，要和新增的社会 benefit 比较。', False),
         ((60, 1012, 1148, 1130), '第二个缺点：信息质量差就没有说服力，比如缺乏足够的证据，或者不够直观。信息发布不等于行为改变：海报可能被忽略，也可能被习惯抵消。', False)]),
   crop((60, 2864, 738, 2934), '评分方案 AO3 第三条', ['BP14'],
        '评分方案的评价也这样写：advertising 往往很贵，而且不一定有足够的说服力把消费带到正确水平。所以这类政策的效果是有条件的。')]),
 card('BD-I04', 'Nudge：信息怎样呈现，决定人们会不会接受', ['I04'], [
   crop((60, 1137, 1160, 1626), '板书：nudge theory（助推理论）与直观的例子', ['BP05'],
        '这里用到 A2 的 nudge theory：人们怎样回应信息，受信息呈现方式的影响。',
        [((60, 1137, 1158, 1314), '如果政府不用有说服力的方法，消费者不会配合。比如借节日贺卡、生日祝福顺带宣传保护环境，消费者更可能接受。', False),
         ((60, 1320, 1150, 1563), '信息要尽量直观。只说一瓶饮料有 30 克糖不够直观；在包装上画三大勺糖，一眼看出量很大，就更有说服力。', False),
         ((60, 1568, 905, 1626), '把器官病变的图印在烟盒上，也是用视觉冲击来影响选择。考试要分清：nudge 改变选择的呈现和环境，保留选择；它不是法律强制，也不是靠大幅改变价格。', False)])]),
 card('BD-ESSAY', '外部性 20 分 essay：三大板块怎么写', ['ESSAY-NEG'], [
   crop((35, 1648, 745, 1778), 'air travel 原题', ['BP06'],
        '这是 2023 年 2 至 3 月考季 9708 第 42 卷第 2 题：air travel 带来负外部性导致的 market failure，要求借助图评估政府干预能在多大程度上纠正。',
        annotate=note('skipped', '9708 F/M 2023 ER p9：本题按 negative consumption externality 分析，误用生产图影响分析档次',
                      '原题只说借助图，没说哪张图',
                      ('要画', 'negative consumption（负的消费外部性）图：MPB（边际私人收益）> MSB（边际社会收益）', 'definition'),
                      ('不是', 'production（生产外部性）图：MSC（边际社会成本）> MPC（边际私人成本）', 'contrast'))),
   crop((825, 1700, 1280, 2690), '老师的三大板块提示', ['BP06T'], '',
        [((825, 1700, 1280, 1815), '老师把外部性和市场失灵题分成三大板块。板块一：为什么外部性会带来市场失灵。', False),
         ((825, 1830, 1280, 2240), '写出 efficiency 和 market failure 的定义、外部性的定义、四条边际曲线的定义并画图；用图说明决策者只看 MPB 和 MPC，在两者相等处生产消费，这个点不是 MSB 等于 MSC 的点，所以没有实现 allocative efficiency；明确指出是生产过多还是过少。', False),
         ((825, 2290, 1280, 2370), '然后用题目里的例子说明这个商品具体有什么外部性。', False),
         ((825, 2450, 1280, 2690), '板块二：写两个政府干预政策，讲清各自的详细效果并画图，比如 tax 和 providing information。', False)]),
   crop((815, 2800, 1280, 2915), '老师：板块三', ['BP16'],
        '板块三是评价：老师的组织办法是每个政策写两个 limitations。',
        annotate=note('overstated', '9708 Paper 4 specimen rubric pp5–6：AO1 加 AO2 14 分、AO3 6 分；9708/42 M/J 2023 Q2 题目要求 two policies',
                      '老师：每个政策写两个 limitations（局限）',
                      ('这是', '课堂的组织办法，不是评分规则', 'note'),
                      ('AO3 看的是', '评价有发展、有依据、有判断', 'definition'),
                      ('如果', '题目给了政策数量，按题目写', 'condition'))),
   crop((815, 2980, 1280, 3362), '老师：conclusion', ['BP15'],
        '结论：政府干预有用，但不一定能彻底消除外部性；不同场合下不同政策更有效，要说明什么情况下 tax 更有效、什么情况下信息更有效。')]),
 card('BD-B01', 'Externality：评分方案的定义原句', ['B01'], [
   crop((35, 2183, 738, 2280), 'air travel 评分方案第二条', ['BP08'],
        '看评分方案原句：negative externalities 发生在一种商品的消费或生产给社会带来的 cost 大于个人承担的 cost 时，也叫负的 spill-over。关键是第三方：没有参与这笔交易的人受到了未计入价格的影响，所以 private 和 social 后果不同。'),
   crop((25, 7650, 800, 7756), '正外部性评分方案第二条', ['BP29A'],
        '正外部性对称：给社会带来的 benefit 大于个人得到的 benefit。要另作判断的是自己的后果：吸烟者自己的健康损失是 private cost，旁人被动吸烟的损失才是 external cost；商品有害，不足以单独证明有 externality。')]),
 card('BD-B03', 'Market failure（市场失灵）：MPB 等于 MPC 的点，不是 MSB 等于 MSC 的点', ['B03'], [
   crop((35, 2040, 738, 2184), 'air travel 评分方案第一条', ['BP07'],
        '评分方案第一条：这里的 market failure 指 allocative inefficiency，先定义 allocative efficiency，并联系到资源配置要使消费者满足最大，可用 AR 等于 MC 的图支持。'),
   crop((825, 1985, 1280, 2240), '老师：用图证明为什么有 market failure', ['BP07'],
        '老师的提示把它落到外部性上：未干预时交易在 MPB 等于 MPC 处，记为 Q m；社会最优看 MSB 与 MSC，若 MSB 大于 MSC，多一单位增加社会净收益，反之净损失。所以最优是 MSB 等于 MSC 的 Q 星，Q m 偏离 Q 星，就是 market failure。'),
   crop((35, 2390, 738, 2486), 'air travel 评分方案第五条', ['BP09'],
        '评分方案也要求图上同时标出没有考虑外部性的市场均衡点，以及考虑之后 allocatively efficient 的航班数量，再比较两者。')]),
 card('BD-T01', 'Indirect tax：评分方案说 demand 下降，图上应是沿 demand 减少', ['T01'], [
   crop((35, 80, 900, 136), '板书第一行', ['BP01'], '板书第一行只写了标题：indirect tax 可以减少负的消费和生产外部性。'),
   crop((35, 2483, 738, 2578), 'air travel 评分方案第六条', ['BP10'],
        '评分方案的说法是：税提高航空出行的成本，demand 下降，均衡航班数减少，达到 allocative efficiency。以卖方缴纳的 specific tax 为例，同一 quantity 需要更高的买方价格。这里的 demand 下降容易读错，看旁边的批注。',
        annotate=note('ambiguous', '9708/42 F/M 2023 Q2 MS pp9–10；' + L2,
                      '评分方案：tax 使 demand（需求）下降',
                      ('不是', 'demand 曲线左移', 'contrast'),
                      ('而是', '供给上移到 MPC（边际私人成本）+ t，价格上升', 'effect',
                       ('所以', 'quantity demanded（需求量）沿原 D 下降到 Q*', 'effect')),
                      ('对比', '让 D 本身左移的是 information（信息政策）', 'contrast')))]),
 card('BD-T05', '税率难设：不知道 Q* 处的 MEC，就难精确到达 Q*', ['T05'], [
   crop((60, 2772, 738, 2822), '评分方案 AO3 第一条', ['BP12'],
        '评价第一条：政府可以征税，但很难测准需要的税率。原因是损害不一定能直接标价，健康、环境和长期后果难以准确估值。低估 Q 星处的 MEC，有害活动仍然过多；高估又会把值得保留的活动也挤掉，造成新的 welfare loss。排放强度和地点不同，统一税率也未必合适。')]),
 card('BD-T04', '税的效果：价格上升，quantity 不一定马上大降', ['T04'], [
   crop((60, 2820, 738, 2868), '评分方案 AO3 第二条', ['BP13'],
        '评价第二条：税对价格和需求的影响有时要很长时间才见效。缺少替代品、成瘾或习惯会让 demand 较 inelastic，同样的涨价，quantity 减得少；替代交通更方便、消费者有时间调整后，响应才变强。税收收入多不等于外部性纠正得好，要看实际数量和社会损害的变化。')]),
 card('BD-J02', '结论：政府干预能减少低效，但要说出在什么条件下', ['J02'], [
   crop((60, 2932, 740, 3050), '评分方案 AO3 最后一条', ['BP15'],
        '评价的落点：政府干预能降低外部性造成的低效，但净效果不一定总是正的；哪种干预更有效，取决于商品或服务的性质。比较的是 net social welfare。'),
   crop((815, 2980, 1280, 3362), '老师：conclusion', ['BP15'], '',
        [((815, 3190, 1280, 3362), '举一个条件明确的判断：若危害急迫、可监测，而短期对价格反应很弱，单靠 tax 难以迅速减量，可执行的上限更及时；若不必立即完成、单位排放可测且企业减排成本差异大，税让低成本者多减排，可能更省资源。条件改变，结论也会改变。', False)])]),
 card('BD-B07', 'Positive consumption：MSB 高于 MPB，市场消费不足', ['B07'], [
   crop((195, 3180, 605, 3418), '板书：老师的红色草图', ['BP17'], '看老师的红色草图，向上的线是供给。',
        [((440, 3240, 600, 3350), '上面一条是 MSB，下面一条是 MPB：消费带来的益处超出本人，例如教育惠及更广泛的社会，这是 positive consumption externality。', False),
         ((270, 3350, 500, 3418), '市场按 MPB 与供给的交点停在 Q，社会最优在 MSB 与供给的交点 Q optimal，Q 停得太早。Q 到 Q optimal 之间仍有 MSB 大于 MSC，这段未实现的净收益就是 welfare loss。', False)],
        annotate=note('illegible', '9708 Paper 4 specimen MS pp9–10 的正消费外部性图；' + L2,
                      '向上那条线的标签看不清',
                      ('按模型应是', 'MPC（边际私人成本）= MSC（边际社会成本）：生产没有外部性', 'definition'),
                      ('考试时', '四条线都写清标签，不照抄草图', 'note')))]),
 card('BD-S01', 'Subsidy（补贴）：降低生产者面对的成本，把 Q 推向 Q*', ['S01', 'S02'], [
   crop((55, 3462, 1225, 4200), '板书：解决正外部性的政策 1 subsidy', ['BP18'],
        '这一块讲正外部性的第一个政策：subsidy。',
        [((55, 3640, 1225, 3695), '效果：政府在生产者每生产一单位时给一笔钱，企业需要靠售价覆盖的成本变低。准确说是有效供给变成 MPC 减 s，向下移动；原料和人力并没有因此变少。', False),
         ((60, 3725, 580, 3850), '只要每单位补贴等于 Q 星处的 external benefit，产量就增加到理想产量。', True),
         ((60, 3850, 580, 4040), '为什么产量增加：补贴降低均衡价格，让商品更 affordable，消费者买得更多。', True),
         ((585, 3720, 1215, 4190), '看图：MPC 等于 MSC 是原来的供给，补贴后的供给线下移；MSB 高于 MPB，两者在同一 quantity 的垂直差是每单位外部收益。补贴额设成 Q 星处的这段差，私人交易就从 Q actual 移到 Q optimal。', True),
         ((60, 4040, 580, 4160), '老师最后强调外部性被内部化：补贴把原本没进入私人决定的第三方收益，通过更低的有效成本反映到选择里。', False)],
        annotate=note('slip', '9708 Paper 4 specimen MS pp9–10：subsidy 降低生产成本、增加供给；' + L2,
                      '下移的供给线标成 MPC + subsidy',
                      ('笔误，应是', 'MPC（边际私人成本）− s：生产者面对的成本下降', 'definition'),
                      ('但是', '原来的 MSC（边际社会成本）不变：补贴是转移，不省资源', 'limit')))]),
 card('BD-S04', 'Subsidy 的局限 1：外部收益测不准', ['S04'], [
   crop((60, 4252, 1268, 4803), '板书：补贴的第 1 个局限', ['BP19'], '',
        [((60, 4252, 1230, 4553), '第一，每单位 external benefit 很难测准：很多外部收益发生在长期，比如教育提高劳动生产率，更受教育的劳动力能做出什么创新，现在难以预估，就像难以预估 AI 的发明。', False),
         ((60, 4560, 1225, 4682), '其次，external benefit 的金钱价值也难衡量，它们不是在市场上交易的商品，没有市场价格；疫苗让人均寿命提高一年，这一年值多少钱无法估算。', False),
         ((60, 4686, 1268, 4803), '所以补贴额若不等于每单位外部收益，产量就到不了最优产量，无法实现 allocative efficiency。不能把产量上升直接当成补贴已经最优。', True)],
        annotate=note('slip', '9708 Paper 4 specimen MS pp9–10 AO3：difficult to measure the precise value of the external benefit',
                      '板书：补贴后的产量到不了“实际产量”',
                      ('笔误，应是', '到不了最优产量 Q*', 'definition'),
                      ('若补少了', 'Q 仍低于 Q*：生产不足', 'effect'),
                      ('若补多了', 'Q 超过 Q*：多出的单位 MSC（边际社会成本）大于 MSB（边际社会收益）', 'effect')))]),
 card('BD-S05', 'Subsidy 的局限 2：成本与机会成本', ['S05'], [
   crop((65, 4833, 1190, 5072), '板书：补贴的第 2 个局限', ['BP20'], '',
        [((65, 4833, 1140, 4887), '第二，补贴花费大，并且有机会成本，要解释政府补贴这个商品放弃了什么。', False),
         ((65, 4895, 1190, 5011), '比如题目说补贴教育，机会成本就是这笔钱没有用来补贴医疗、建设基础设施或发放社会福利，后果可能是基础设施不足、穷人用不起医疗，这些方面也出现 welfare loss。', False),
         ((65, 5019, 760, 5072), '所以政府要判断钱花在哪里最能减少 welfare loss。注意，补贴付款本身是 transfer，支出大不自动等于 DWL 大；要比较纠正生产不足的净收益和放弃的替代用途。', False)])]),
 card('BD-S06', 'Subsidy 的局限 3：生产者可能依赖补贴', ['S06'], [
   crop((72, 5104, 1200, 5220), '板书：补贴的第 3 个局限', ['BP21'],
        '第三，producers may become dependent on subsidy：成本高的生产者缺乏动力降低成本、提高效率，补贴将来也很难取消。这是条件性的风险：绩效条件、竞争分配和可预期的退出安排可以保留改进的动力，有补贴不等于必然低效。')]),
 card('BD-S07', 'Subsidy 已发，quantity 为什么未必马上增加', ['S07'], [
   crop((55, 8627, 702, 8668), '正外部性评分方案 AO3 第二条', ['BP30'],
        '评分方案的评价写到：对价格和产出的影响有时要很长时间才见效。原因先看供给能否扩大：新学校、研发团队都需要设施、人才和建设时间。短期容量固定，补贴改善了激励，quantity 增幅仍可能很小。要比较短期与长期的真实 quantity 和社会 benefit，不能把发放预算当成效果已经实现。')]),
 card('BD-I03', '正面信息：为什么可能增加 merit good 的消费', ['I03'], [
   crop((60, 5328, 1135, 5690), '板书：解决正消费外部性的政策 2', ['BP22'], '',
        [((60, 5328, 1135, 5470), '政策 2 是 providing information。很多有正消费外部性的商品是 merit good，对消费者自己也有好处，却被低估。可信的说明让消费者认识到自己的 benefit，同一价格下愿意买更多，demand 右移，quantity 可能增加。', False),
         ((60, 5508, 515, 5690), '缺点：一是花钱；二是可能没有说服力，用 nudge theory 解释，和负外部性那里的信息政策一样。', False)],
        annotate=note('ambiguous', '9708 Paper 4 specimen MS pp9–10：advertising to increase demand；9708 M/J 2023 ER pp21–22：要连上 merit good、externality 与效率',
                      '板书：merit good（优值品）的好处被低估',
                      ('信息补的是', '消费者对自己 benefit（收益）的低估', 'definition',
                       ('所以', 'demand（需求）右移，Q 上升', 'effect')),
                      ('补不了', '给别人的 external benefit（外部收益）仍不进私人决定', 'limit',
                       ('所以', 'Q 未必升到 Q*', 'effect'))))]),
 card('BD-R02', 'Positive regulation（强制性规定）：要求消费，也要让人做得到', ['R02'], [
   crop((60, 5770, 1175, 6162), '板书：解决正消费外部性的政策 3', ['BP23'], '',
        [((60, 5770, 950, 5890), '政策 3 是 regulation：要求人们增加对这些商品的消费，比如义务教育，或强制接种疫苗、戴口罩。', False),
         ((60, 5922, 1175, 6162), '第一个局限：单靠规定无法增加穷人的消费，因为它没有让商品更 affordable，所以需要和 direct provision 等配套一起用。', False)],
        annotate=note('overstated', '9708 syllabus 8.1.1（regulation）；20 分题的评价要写清条件（9708 Paper 4 specimen rubric pp5–6）',
                      '板书：政府要先免费提供，才能要求增加消费',
                      ('说得过满', '免费不是唯一办法', 'limit'),
                      ('需要的是', '可负担、可获得：补贴、低价公办', 'condition'),
                      ('否则', '穷人做不到，规定难以执行', 'effect'))),
   crop((60, 6294, 1252, 6350), '板书：regulation 的第 3 个局限', ['BP25'],
        '第三个局限：强制性政策干预了人们的自由，带来 political pressure，政府有时迫于压力不使用 regulation。')]),
 card('BD-R03', 'Regulation（规定）的效果取决于执行', ['R03'], [
   crop((60, 6170, 1186, 6286), '板书：regulation 的第 2 个局限', ['BP24'], '',
        [((60, 6170, 1186, 6226), '第二个局限：可能因为 black market，或者政府缺乏 administrative power，规定没有被遵守。', False),
         ((60, 6232, 578, 6286), '比如有的农村地区仍有家庭不让适龄孩子上学。有法律不代表有遵守：监测薄弱、处罚轻，违规的预期代价低于合规成本，就会出现规避。加强执行本身也有成本，评价要把减少的外部损害和新增的实施成本放在一起比。', False)])]),
 card('BD-D01', 'Direct provision：政府直接增加供给', ['D01'], [
   crop((48, 6432, 1068, 6612), '板书：解决正外部性的政策 4', ['BP26'], '',
        [((48, 6432, 1000, 6550), '政策 4 是 direct provision：政府通过国企直接提供，比如公立学校、医院，或国有大学和科研机构做 R&D。', False),
         ((48, 6556, 1068, 6612), '效果是直接增加 market supply 和 output，也通过让商品便宜或免费来增加消费。但价格与容量要一起看：只降价而容量不增，可能形成排队；扩张超过 Q 星则造成浪费，公办本身不是最优供给的证明。', False)]),
   crop((25, 8333, 826, 8414), '正外部性评分方案最后一条', ['BP29'],
        '评分方案的写法：政府可以直接提供商品或服务，增加生产和供给，最终达到 allocatively efficient 的结果。')]),
 card('BD-D02', 'Direct provision（政府直接提供）的局限：花费大，也可能建错数量', ['D02'], [
   crop((48, 6650, 390, 6767), '板书：政府直接提供的局限 1', ['BP27'],
        '局限一：cost 和 opportunity cost。资金、土地和专业人员本可以用于其他项目。'),
   crop((48, 6897, 1212, 7075), '板书：政府直接提供的局限 3', ['BP27'], '',
        [((48, 6897, 1212, 6953), '局限三：外部收益的大小难以估算，政府不知道社会最优产量在哪里，可能过量提供。', False),
         ((48, 6959, 1190, 7075), '老师举的例子是在人口下降的地区修了过多学校和医院，后来被迫关门。比较的是额外的社会 benefit 和机会成本，不能只凭新建数量认定成功。', False)])],
   notes=[('未核实', '学校、医院关闭是课堂举例，2026-10-03 研究记录未核实，当作理解用的例子，不当作确定事实来写。')]),
 card('BD-D03', '国企为什么可能效率较低', ['D03'], [
   crop((48, 6773, 1054, 6889), '板书：政府直接提供的局限 2', ['BP28'], '',
        [((48, 6773, 1054, 6820), '局限二：由国企直接提供可能降低效率，要解释原因。', False),
         ((48, 6820, 1054, 6889), '一是不追求利润，缺乏控制成本的动力；二是竞争较弱，一个行业都是国企，也缺乏降低成本的动力。这可能造成 X-inefficiency：给定产出用了超过必要的投入。', False)]),
   crop((55, 8735, 702, 8778), '正外部性评分方案 AO3', ['BP30'],
        '评分方案的评价同样写到：direct provision 花费大，有时不如市场力量提供的有效率。要说成条件性风险：透明绩效、监督与恰当目标可以改善激励。')]),
 card('BD-POS-ESSAY', '正外部性 essay：机制本身和它在图上的样子都要讲', ['ESSAY-POS'], [
   crop((5, 7082, 915, 7182), '正外部性原题：specimen（样题）', ['BP29'],
        '这是 2023 年起使用的 Paper 4 specimen 第 2 题：借助图评估政府干预能否成功纠正正外部性造成的 market failure。它是样题，不是一场真实考试。'),
   crop((835, 8040, 1228, 8150), '老师的提示', ['BP29'],
        '老师的提示：既要解释机制本身，也要解释这个机制在外部性图上怎样体现。只写出价格下降、数量增加还不够，要接上为什么这让福利改善。'),
   crop((25, 8146, 826, 8334), '评分方案：subsidy（补贴）与 advertising（广告宣传）', ['BP29M'],
        '评分方案列的路径：补贴降低生产成本、增加供给、降低价格、提高均衡产量；广告提高需求、增加消费。',
        annotate=note('skipped', '9708 M/J 2023 ER pp21–22：只写价格、产量变化而不解释福利为何改善，分析不完整；9708 Paper 4 specimen MS pp9–10',
                      '评分方案：产量增加，就达到 allocative efficiency（配置效率）',
                      ('中间一步', 'Q 升到 MSB（边际社会收益）= MSC（边际社会成本）的 Q*', 'effect'),
                      ('所以', 'Q 与 Q* 之间的 welfare loss（福利损失）消失', 'effect'))),
   crop((55, 8778, 702, 8890), '评分方案 AO3 最后一条', ['BP30'],
        '评价落点与负外部性那题一样：干预能减少低效，但净效果不一定总为正，取决于商品或服务的性质。')]),
 card('BD-P01', 'Property rights（产权）：让损害有可主张的责任', ['P01'], [
   crop((45, 9058, 460, 9212), '板书：其它与市场失灵有关的政策', ['BP31'], '其它与 market failure 有关的政策，第一个是 property right。'),
   crop((45, 9372, 1192, 9580), '板书：property right 定义', ['BP31'], '',
        [((45, 9372, 1192, 9490), '定义：法律保护资产的私人所有权；资产被损害时，所有者有权向造成损害的一方索赔。责任让原本由第三方承担的影响进入私人决定。', False),
         ((45, 9522, 850, 9580), 'A2 考 property right，主要是看它怎样解决污染这类 negative externality。有产权还要能实施：边界、损害归因和执行都必须可行。', False)])]),
 card('BD-P02', 'Property rights：交易成本为零时，谈判能达到有效配置', ['P02'], [
   crop((45, 9217, 1190, 9333), '板书：经济学家的观点', ['BP32'],
        '经济学家认为有产权的世界资源配置效率更高：如果交易成本为零，消费者、生产者和第三方可以通过产权和谈判实现有效的资源配置。注意老师标出的前提：交易成本为零。'),
   crop((45, 9585, 1200, 9763), '板书：土地和河流的例子', ['BP32L'], '',
        [((45, 9585, 1100, 9640), '一块土地或河流如果没有产权，生产者污染它没有代价。板书说因为这块地不是私人的，这句要看旁边的批注。', False),
         ((45, 9645, 1200, 9763), '如果有产权，污染就有代价，会影响企业的行为，让它们少污染。设工厂减排一单位花 6 美元、居民因此得到 10 美元的 benefit：若工厂有排放权，居民付 8 美元买减排，双方各净得 2 美元。权利归谁影响谁付款，不能把效率与分配混为一谈。', False)],
        annotate=note('ambiguous', '9708/33 O/N 2017 Q16（key D）：产权让所有者保护资产、损害方承担责任；9708 syllabus 8.1.1',
                      '板书：没有产权，因为这块地不是私人的',
                      ('关键不在', '私有还是公有', 'contrast'),
                      ('而在', '有没有可执行的权利与损害责任', 'definition',
                       ('所以', '污染要付代价，排放减少', 'effect'))))]),
]

order = ['BD-I02', 'BD-I05', 'BD-I04', 'BD-ESSAY', 'BD-B01', 'BD-B03', 'BD-T01', 'BD-T05', 'BD-T04', 'BD-J02', 'BD-B07', 'BD-S01',
         'BD-S04', 'BD-S05', 'BD-S06', 'BD-S07', 'BD-I03', 'BD-R02', 'BD-R03', 'BD-D01', 'BD-D02', 'BD-D03', 'BD-POS-ESSAY', 'BD-P01', 'BD-P02']
by = {c['id']: c for c in cards}
cards = [by[i] for i in order]
cards[0]['blocks'][0]['masks'] = []

board = [
 {'id': 'BP01', 'where': '板书第一行', 'point': 'indirect tax 减少负的消费与生产外部性（标题）', 'items': ['T01']},
 {'id': 'BP02', 'where': '板书第二行', 'point': 'regulation 减少负外部性（标题）', 'items': [], 'note': '只有标题', 'not_shown': '板书只有标题，negative regulation 的机制由旧卡 R01 讲'},
 {'id': 'BP03', 'where': '约 3%–9% 处', 'point': '政策 3 providing information 的两条路径与执行手段', 'items': ['I02']},
 {'id': 'BP04', 'where': '约 9%–11% 处', 'point': 'information 的缺点：贵、质量差没有说服力', 'items': ['I05']},
 {'id': 'BP05', 'where': '约 11%–16% 处', 'point': 'nudge theory：呈现方式、直观的例子', 'items': ['I04']},
 {'id': 'BP06', 'where': '约 17% 处', 'point': 'air travel 原题', 'items': ['ESSAY-NEG'],
  'issue': 'skipped', 'issue_note': '原题只说借助图，没说是哪张图；考官报告要求 negative consumption 图'},
 {'id': 'BP06T', 'where': '约 17%–27% 处', 'point': '老师的三大板块提示', 'items': ['ESSAY-NEG']},
 {'id': 'BP07', 'where': '约 21%–23% 处', 'point': 'MS：market failure 与 allocative efficiency；老师：MPB=MPC 不是 MSB=MSC', 'items': ['B03']},
 {'id': 'BP08', 'where': '约 22% 处', 'point': 'MS：negative externalities 定义', 'items': ['B01']},
 {'id': 'BP09', 'where': '约 24% 处', 'point': 'MS：图上比较市场均衡与有效数量', 'items': ['B03']},
 {'id': 'BP10', 'where': '约 25% 处', 'point': 'MS：tax 提高成本，“demand 下降”', 'items': ['T01'],
  'issue': 'ambiguous', 'issue_note': '“decrease demand”易读成 D 左移；税是供给上移、需求量沿 D 减少'},
 {'id': 'BP11', 'where': '约 26% 处', 'point': 'MS：negative advertising', 'items': ['I02']},
 {'id': 'BP12', 'where': '约 28% 处', 'point': 'MS AO3：税率难以测准', 'items': ['T05']},
 {'id': 'BP13', 'where': '约 29% 处', 'point': 'MS AO3：税的影响需要时间', 'items': ['T04']},
 {'id': 'BP14', 'where': '约 29% 处', 'point': 'MS AO3：advertising 贵、不一定有说服力', 'items': ['I05']},
 {'id': 'BP15', 'where': '约 30%–34% 处', 'point': 'MS AO3 净效果与老师的 conclusion', 'items': ['J02']},
 {'id': 'BP16', 'where': '约 28%–29% 处', 'point': '老师：板块三 EV，每个政策两个 limitations', 'items': ['ESSAY-NEG'],
  'issue': 'overstated', 'issue_note': '“每个政策两个 limitations”是课堂组织办法，不是评分规则'},
 {'id': 'BP17', 'where': '约 32%–34% 处', 'point': '红色草图：MSB 高于 MPB，Q 小于 Q optimal', 'items': ['B07'], 'legibility': 'low', 'confirmed_by': '标准正消费外部性模型；2026-10-03 研究记录已标注该标签不清'},
 {'id': 'BP18', 'where': '约 35%–43% 处', 'point': '政策 1 subsidy：机制、四线图、内部化', 'items': ['S01', 'S02'],
  'issue': 'slip', 'issue_note': '下移的供给线标成 MPC + subsidy，应为 MPC − subsidy；“成本下降”不是真实 MSC 下降'},
 {'id': 'BP19', 'where': '约 43%–49% 处', 'point': 'subsidy 局限 1：外部收益难测', 'items': ['S04'],
  'issue': 'slip', 'issue_note': '“到不了实际产量”应为“到不了最优产量”'},
 {'id': 'BP20', 'where': '约 49%–51% 处', 'point': 'subsidy 局限 2：成本与机会成本', 'items': ['S05']},
 {'id': 'BP21', 'where': '约 52%–53% 处', 'point': 'subsidy 局限 3：生产者依赖', 'items': ['S06']},
 {'id': 'BP22', 'where': '约 54%–58% 处', 'point': '政策 2 positive information 及缺点', 'items': ['I03'],
  'issue': 'ambiguous', 'issue_note': '信息补的是私人 benefit 的低估，不是第三方的 external benefit'},
 {'id': 'BP23', 'where': '约 58%–62% 处', 'point': '政策 3 regulation 与局限 1（穷人负担）', 'items': ['R02'],
  'issue': 'overstated', 'issue_note': '“政府需要先免费提供才能要求增加消费”：可负担、可获得即可，免费不是唯一办法'},
 {'id': 'BP24', 'where': '约 63% 处', 'point': 'regulation 局限 2：black market、administrative power', 'items': ['R03']},
 {'id': 'BP25', 'where': '约 64% 处', 'point': 'regulation 局限 3：自由与 political pressure', 'items': ['R02']},
 {'id': 'BP26', 'where': '约 65%–67% 处', 'point': '政策 4 direct provision 及效果', 'items': ['D01']},
 {'id': 'BP27', 'where': '约 67%–72% 处', 'point': 'direct provision 局限 1、3：成本、过量提供', 'items': ['D02']},
 {'id': 'BP28', 'where': '约 69% 处', 'point': 'direct provision 局限 2：国企效率', 'items': ['D03']},
 {'id': 'BP29', 'where': '约 72%–85% 处', 'point': '正外部性 specimen 原题、老师提示、MS 的 direct provision 一条', 'items': ['ESSAY-POS', 'D01']},
 {'id': 'BP29M', 'where': '约 83%–85% 处', 'point': 'MS：subsidy 与 advertising 的作用路径', 'items': ['ESSAY-POS'],
  'issue': 'skipped', 'issue_note': '从“产量增加”直接跳到 allocative efficiency，缺“Q 升到 MSB = MSC 的 Q*”'},
 {'id': 'BP29A', 'where': '约 78% 处', 'point': 'MS：positive externalities 定义', 'items': ['B01']},
 {'id': 'BP30', 'where': '约 85%–90% 处', 'point': '正外部性 MS AO3', 'items': ['ESSAY-POS', 'S07', 'D03']},
 {'id': 'BP31', 'where': '约 92%–97% 处', 'point': 'property right 定义与 A2 的考法', 'items': ['P01']},
 {'id': 'BP32', 'where': '约 93%–95% 处', 'point': '经济学家：交易成本为零时，产权加谈判能有效配置', 'items': ['P02']},
 {'id': 'BP32L', 'where': '约 97%–99% 处', 'point': '土地、河流的例子：没有产权，污染没有代价', 'items': ['P02'],
  'issue': 'ambiguous', 'issue_note': '“因为这块地不是私人的”：问题在没有可执行的产权与责任，不在是否私有'},
 {'id': 'BP33', 'where': '底部', 'point': 'ClassIn 标记', 'items': [], 'note': '导出标记', 'not_shown': 'ClassIn 导出标记，不是教学内容'},
]

E_AIR = ['9708/42 F/M 2023 Q2 MS pp9–10', '9708 F/M 2023 ER p9']
E_POS = ['9708 Paper 4 specimen 2023 MS pp9–10', '9708 M/J 2023 ER pp21–22']
item = lambda i, spec, point, kind, level, ev, **kw: dict({'id': i, 'spec': spec, 'point': point, 'class': 'core', 'kind': kind, 'level': level, 'evidence': ev}, **kw)
old = lambda cid: {'existing': f'{OLD} {cid}'}
items = [
 item('B01', '7.4.1', 'externality 的定义（第三方、未计入价格）', 'term', 'MS 原句：cost／benefit to society greater than that incurred／received by individual；分清 private 与 external', E_AIR[:1] + E_POS[:1]),
 item('B02', '7.4.1', 'MPC、MEC、MSC 的边际定义', 'term', '同一 Q 比较；MSC＝MPC＋MEC', ['9708/32 O/N 2025 Q3 key C', '9708/32 F/M 2024 Q3 key B'], **old('B02')),
 item('B02b', '7.4.1', 'MPB、MEB、MSB 的边际定义', 'term', '正消费 MSB＞MPB；负消费 MSB＜MPB', ['9708/32 F/M 2024 Q3 key B', '9708/32 M/J 2023 Q6 ER p18'], **old('B02b')),
 item('B10', '7.4.1', 'total 与 marginal 的换算', 'method', '由 total 变化算 marginal，不用 total 当每单位税', ['9708/32 F/M 2024 Q3 key B', 'Varian Ch34'], **old('B10')),
 item('B11', '7.4.2', '多种外部性并存时先定 Q 再读差', 'diagram', '私人 Q 由 MPB=MPC；同一 Q 读对应两线之差', ['9708/32 O/N 2025 Q3 key C', '9708/32 F/M 2024 Q3 key B'], **old('B11')),
 item('B03', '7.3.5／7.4.2', 'Q*：MSB=MSC；市场停在 MPB=MPC', 'chain', 'MS：market failure＝allocative inefficiency；图比较市场均衡与有效数量', E_AIR + ['9708/32 O/N 2025 Q6 key A']),
 item('B04', '7.4.3', 'negative production 图', 'diagram', 'MSC＞MPC，生产过多，DWL', ['9708 F/M 2023 ER p9', '9708/42 O/N 2024 Q2 MS p10'], **old('B04')),
 item('B05', '7.4.3', 'negative consumption 图（air travel 要用）', 'diagram', 'MPB＞MSB，消费过多；ER 纠正误用生产图', E_AIR, **old('B05')),
 item('B06', '7.4.3', 'positive production 图', 'diagram', 'MSC＜MPC，生产不足', ['9708/32 M/J 2023 Q8 ER p18', '9708 Paper 4 specimen 2023 MS pp9–10'], **old('B06')),
 item('B07', '7.4.3', 'positive consumption 图', 'diagram', 'MSB＞MPB，MPC=MSC，Q＜Q*', E_POS + ['9708 SPA Paper 4 2023 Q2 pp9–11']),
 item('B08', '7.4.5', 'deadweight welfare loss', 'diagram', 'MSB 与 MSC 之差在 Qm 与 Q* 间的面积；付款矩形不是 DWL', ['9708/31 O/N 2020 Q13 key B', '9708 F/M 2023 ER p9'], **old('B08')),
 item('B09', '7.4.4', 'internalise：对齐激励而非污染归零', 'term', '最优可能仍有污染；比较边际值', ['9708/32 O/N 2025 Q6 key A', '9708/32 M/J 2019 Q17 key B'], **old('B09')),
 item('C01', '7.4.3', '四类 externality 的识别', 'fact', '行为来自生产或消费、对第三方是 cost 或 benefit', ['9708/32 F/M 2023 Q7 ER p6', '9708/32 M/J 2023 Q8 ER p18'], **old('C01')),
 item('C02', '7.4.3', '交通题按被分析的行为分类', 'fact', 'air travel 按 negative consumption 分析（ER）', E_AIR, **old('C02')),
 item('C03', '8.1.1', '场所限制减少外部伤害而不必同幅减消费', 'chain', '比较减少与转移的损害', ['9708/31 O/N 2020 Q14 key C', '9708/42 F/M 2024 Q2 MS pp10–11'], **old('C03')),
 item('I01', '1.6／7.4', 'merit/demerit 与 externality 的区别', 'term', '私人判断失误 vs 第三方影响', ['9708 O/N 2023 ER Paper 22 Q3', '9708 M/J 2023 ER pp21–22'], **old('I01')),
 item('I02', '8.1.1', '负面信息宣传的作用路径', 'chain', '信息改变 D 本身；条件：可信、改变选择', E_AIR),
 item('I03', '8.1.1', '正面信息与 merit good', 'chain', '私人 benefit 被低估；不保证到 Q*', E_POS),
 item('I04', '8.1.1', 'nudge：呈现与选择环境，保留选择', 'term', 'persuasion 而非 legal requirement', ['9708/32 O/N 2025 Q9 key D', 'BIT EAST 2014'], evidence_gap='nudge 只有一道 MCQ 直接考到；BIT EAST 报告作机制说明'),
 item('I05', '8.1.1', 'information policy 的局限', 'chain', 'MS AO3：costly、persuasive effect 不确定', E_AIR),
 item('T01', '8.1.1', 'indirect tax 的机制（沿 demand 减量）', 'chain', 'effective supply 上移，quantity demanded 沿 D 下降；MS 写法需改述', E_AIR),
 item('T07', '8.1.1', 'specific 与 ad valorem tax', 'term', '固定额 vs 比例，税楔金额', ['9708 syllabus 8.1.1 p27', '9708/42 F/M 2024 Q2 MS pp10–11'], **old('T07')),
 item('T02', '8.1.1', '负生产外部性：tax＝Q* 处 MEC', 'diagram', '把税对准 Q* 的 MEC', ['9708/32 M/J 2019 Q17 key B', '9708/42 O/N 2024 Q2 MS p10'], **old('T02')),
 item('T03', '8.1.1', '负消费外部性的税图', 'diagram', 'MPC＋t 与 MPB 交于 Q*', E_AIR, **old('T03')),
 item('T04', '8.1.1', '税的效果取决于响应与时间', 'chain', 'MS AO3：impact takes a long time；PED、替代品', E_AIR),
 item('T05', '8.1.1', '税率难设', 'chain', 'MS AO3：difficult to measure the precise level of taxation', E_AIR),
 item('T06', '8.1.1', '税的分配与规避', 'chain', 'transfer 与真实成本、低收入负担、规避', ['9708/32 F/M 2024 Q13 key D', '9708/42 F/M 2024 Q2 MS pp10–11'], **old('T06')),
 item('S01', '8.1.1', 'subsidy 降低有效成本', 'chain', '有效供给 MPC−s；真实 MSC 不变', E_POS + ['9708/32 O/N 2025 Q8 key B']),
 item('S02', '8.1.1', '正消费外部性的补贴图', 'diagram', 's＝Q* 处 MSB−MPB；标签 MPC−s', E_POS),
 item('S03', '8.1.1', '正生产外部性的补贴', 'diagram', 's＝Q* 处 MPC−MSC', ['9708/32 M/J 2023 Q8 ER p18', '9708 Paper 4 specimen 2023 MS pp9–10'], **old('S03')),
 item('S04', '8.1.1', '补贴局限：MEB 难测', 'chain', 'MS AO3：difficult to measure the precise value', E_POS),
 item('S05', '8.1.1', '补贴局限：机会成本', 'chain', 'MS AO3：funds might have been used for other purposes', E_POS + ['9708/32 F/M 2023 Q9 ER p6']),
 item('S06', '8.1.1', '补贴局限：依赖与低效', 'chain', '条件性风险', E_POS, evidence_gap='MS 未单列，来自老师板书与教材'),
 item('S07', '8.1.1', '补贴见效需要时间', 'chain', 'MS AO3：takes a long time to become effective', E_POS),
 item('R01', '8.1.1', 'negative regulation（标准、额度、禁令）', 'chain', '约束对象说清；针对危害', ['9708/42 F/M 2024 Q2 MS pp10–11', '9708/42 O/N 2024 Q2 MS p10'], **old('R01')),
 item('R02', '8.1.1', 'positive regulation 与配套', 'chain', '可负担、可获得；自由与政治可行性', E_POS),
 item('R03', '8.1.1', 'regulation 的执行与规避', 'chain', 'black market、监测与处罚', E_POS + ['9708/42 F/M 2024 Q2 MS pp10–11']),
 item('R04', '8.1.1', '统一减排标准未必最低成本', 'chain', '减排成本差异', ['9708/42 O/N 2024 Q2 MS p10', 'Varian Ch34'], **old('R04')),
 item('D01', '8.1.1', 'direct provision 的机制', 'chain', '增加供给与可获得性；免费不等于最优', E_POS + ['9708/32 F/M 2024 Q12 key D']),
 item('D01b', '1.6', '政府提供不等于 public good', 'term', 'non-rival、non-excludable 分开判断', ['9708/42 O/N 2023 MS Q1(d) p8', '9708/32 F/M 2024 Q12 key D'], **old('D01b')),
 item('D02', '8.1.1', 'direct provision 的配置风险', 'chain', '成本、机会成本、过量', E_POS),
 item('D03', '8.1.1', '公共提供的效率风险', 'chain', 'X-inefficiency 是条件性风险', E_POS),
 item('P01', '8.1.1', 'property rights 的定义与责任', 'term', '可执行的权利与索赔', ['9708/33 O/N 2017 Q16 key D', '9708 syllabus 8.1.1 p27']),
 item('P02', '8.1.1', '零交易成本下的谈判', 'chain', '补偿方向与效率／分配之分', ['9708/33 O/N 2017 Q16 key D', 'Varian Ch34 §34.4']),
 item('P03', '8.1.1', '交易成本与谈判障碍', 'chain', '多受害者、信息、执行', ['9708/33 O/N 2017 Q16 key D', 'Varian Ch34'], **old('P03')),
 item('E01', '8.1.1', 'tradable permits：cap 与交易', 'chain', 'cap 控制总量', ['9708/41 O/N 2024 Q2 MS p10', 'Varian Ch34'], **old('E01')),
 item('E02', '8.1.1', 'permit 价格与减排激励', 'chain', '低减排成本者多减排', ['9708/41 O/N 2024 Q2 MS p10', 'Varian Ch34'], **old('E02')),
 item('E03', '8.1.1', 'permits 的效果条件', 'chain', 'cap、监测、市场力量', ['9708/41 O/N 2024 Q2 MS p10', 'Varian Ch34'], **old('E03')),
 item('J01', '8.1.2', 'government failure 的判断基准', 'term', '与可行基准比较；正常行政支出不是失灵', ['9708/31 O/N 2023 Q11 key C', '9708/32 M/J 2019 Q15 key A'], **old('J01')),
 item('J02', '8.1.1–8.1.2', '条件性的政策判断', 'essay', 'MS AO3：net effect 不一定为正，取决于商品性质', E_AIR + E_POS[:1]),
 item('J03', '8.1.1', 'policy mix', 'chain', '不同工具对应不同障碍', ['9708/42 M/J 2023 Q2 MS pp10–11', '9708 M/J 2023 ER p24'], **old('J03')),
 item('J04', '8.1.1', '两个市场：税有害品或补贴替代品', 'chain', '说明市场之间的连接', ['9708/42 M/J 2023 Q2 MS pp10–11', '9708 M/J 2023 ER p24'], **old('J04')),
 item('J04b', '8.1.1', '补贴公共交通减少拥堵', 'chain', '替代性条件', ['9708/42 O/N 2025 Q2 MS pp12–13', '9708 M/J 2023 ER p24'], **old('J04b')),
 item('ESSAY-NEG', '7.4／8.1', '负外部性 20 分 essay 的结构', 'essay', 'AO1+AO2 14、AO3 6；图与正文解释；条件性结论', E_AIR),
 item('ESSAY-POS', '7.4／8.1', '正外部性 20 分 essay 的结构', 'essay', '机制要落到图上；AO3 发展评价', E_POS + ['9708 SPA Paper 4 2023 Q2 pp9–11']),
]
for it in items:
    if it.get('evidence_gap') is None:
        it.pop('evidence_gap', None)

research = [
 {'type': 'board', 'ref': 'board.png（1280×9866，SHA-256 a17f64f8…c9）', 'read': '2026-10-10 逐页读完 7 张编号总览页（0–9866 px）', 'used_for': '全部 25 张板书卡的卡面、裁切框与更正'},
 {'type': 'spec', 'ref': 'Cambridge 9708 syllabus 2026–2028 Version 2（2025-12）https://www.cambridgeinternational.org/Images/697423-2026-2028-syllabus.pdf', 'read': 'pp24、27–28、43（2026-10-03 制作记录；本次未重读）', 'used_for': '范围 7.3.5、7.4.1–7.4.5、8.1.1、8.1.2'},
 {'type': 'ms', 'ref': '9708/42 F/M 2023 Q2 mark scheme', 'read': 'pp9–10（板书原样贴入，本次随板书读过）', 'used_for': 'BD-ESSAY、BD-B01、BD-B03、BD-T01（“decrease demand”改述）、BD-T05、BD-T04、BD-J02', 'paper': '9708/4'},
 {'type': 'er', 'ref': '9708 F/M 2023 examiner report', 'read': 'pp6–7、9–11（2026-10-03 制作记录）', 'used_for': 'air travel 要用 negative consumption 图（BD-ESSAY 的批注）', 'paper': '9708/4'},
 {'type': 'ms', 'ref': '9708/42 F/M 2024 Q2 mark scheme', 'read': 'pp10–11（2026-10-03 研究记录《板书与考试证据》）', 'used_for': '批注里的“图不准确最高 L2”（BD-T01、BD-B07、BD-S01）', 'paper': '9708/4'},
 {'type': 'ms', 'ref': '9708 Paper 4 specimen 2023 mark scheme Q2', 'read': 'pp3–6、9–10（板书原样贴入，本次随板书读过）', 'used_for': 'BD-POS-ESSAY、BD-S07、BD-D01、BD-D03、BD-B01', 'paper': '9708/4'},
 {'type': 'exemplar', 'ref': '9708 Example Candidate Responses Paper 4（2023）Q2', 'read': 'script pp.15–21（high 16/20、middle 10/20、low 5/20；2026-10-03 制作记录）', 'used_for': '旁白里“只写价格效果不够，要接上福利”', 'paper': '9708/4'},
 {'type': 'specimen', 'ref': '9708 Specimen Paper Answers Paper 4（2023）Q2', 'read': 'pp9–11（2026-10-03 制作记录）', 'used_for': 'BD-POS-ESSAY 的机制讲法', 'paper': '9708/4'},
 {'type': 'ms', 'ref': '9708/32 F/M 2024 与 O/N 2025 选择题答案；9708/33 O/N 2017 Q16', 'read': 'QP 与 key（2026-10-03 制作记录）', 'used_for': 'BD-I04（persuasion 而非强制）、BD-S04、BD-P01', 'paper': '9708/3'},
 {'type': 'er', 'ref': '9708 M/J 2023 examiner report', 'read': 'pp18、21–22、24（2026-10-03 制作记录）', 'used_for': '“做出价格效果还不是解释福利改善”（BD-POS-ESSAY、BD-I03 的批注）', 'paper': ['9708/3', '9708/4']},
 {'type': 'textbook', 'ref': 'Varian, Intermediate Microeconomics 8e Ch16、33、34、36', 'read': '2026-10-03 制作记录所列页', 'used_for': 'BD-P02 的谈判数例、BD-S05 transfer 与机会成本之分'},
 {'type': 'other', 'ref': '旧卡组研究记录《板书与考试证据.md》（2026-10-03）', 'read': '2026-10-10 全文重读', 'used_for': '10 处批注的问题点：MPC + subsidy 方向、实际产量笔误、红色草图标签、免费提供说得过满、信息补私人低估、MS 的 decrease demand、air travel 用哪张图、两个 limitations 的地位、价格效果与福利之分、不是私人的≠没有产权'},
 {'type': 'other', 'ref': '旧卡组制作源 cards.json（53 张，已核对内容复评）', 'read': '2026-10-10 全部 53 张的朗读文本', 'used_for': '板书卡旁白沿用已复评的讲解；29 张板书未覆盖的卡保留原卡（existing）'},
]

deck = {
 'schema': 'ccpt-6',
 'deck': {'name': 'Economics::板书01 Externalities（板书卡）', 'deck_id': 2026101011, 'model_id': 2026101010,
          'model_name': 'CCPT6 · 考纲知识卡', 'namespace': 'ccpt6-9708-board01-externalities-board'},
 'style': {'theme': 'editorial', 'voice': 'xiaoxiao', 'speed': 'auto'},
 'speech_lexicon': {'MPB': 'M P B', 'MPC': 'M P C', 'MSB': 'M S B', 'MSC': 'M S C', 'MEB': 'M E B', 'MEC': 'M E C', 'DWL': 'D W L', 'AO3': 'A O 3', 'R&D': 'R and D'},
 'exam': {'board': 'Cambridge International', 'qualification': 'Cambridge International AS & A Level Economics', 'code': '9708',
          'units': ['9708/3', '9708/4'], 'spec_version': '2026–2028 syllabus, Version 2 (December 2025)',
          'spec_url': 'https://www.cambridgeinternational.org/Images/697423-2026-2028-syllabus.pdf', 'session': 'May/June 2027', 'session_assumed': True,
          'identified_by': 'exclusive-content',
          'evidence': ['板书贴入的评分方案用 Table A AO1/AO2 14 分、Table B AO3 6 分，是 9708 Paper 4 essay 的评分格式',
                       '题干原文定位为 9708/42 F/M 2023 Q2 与 9708 Paper 4 specimen 2023 Q2（2026-10-03 研究记录）',
                       'property rights、nudge、tradable permits 同属 9708 A Level 8.1.1'],
          'ruled_out': [{'candidate': 'Cambridge IGCSE Economics 0455', 'why_not': 'IGCSE 不考 MPB/MSB 四线图与 20 分 AO3 essay'},
                        {'candidate': 'Pearson Edexcel IAL Economics', 'why_not': 'IAL 的评分记号不是 Table A/B 的 AO1+AO2 14／AO3 6'}],
          'papers': [{'code': '9708/3', 'format': 'mcq'}, {'code': '9708/4', 'format': 'essay'}]},
 'research': research,
 'research_gaps': '2024、2025 年的 examiner report 下载多站返回 HTML/403，未取得逐题讲解。本次改造只重读了板书原图与旧卡制作源；考纲、MS、ER、范文的实读范围引用 2026-10-03 的制作记录。',
 'board': board,
 'demands': [
  {'id': 'D1', 'series': 'Feb/Mar 2023', 'q': '9708/42 Q2', 'command': 'Assess', 'ask': 'air travel 负外部性：借助图评估政府能在多大程度上纠正', 'points': ['ESSAY-NEG', 'B01', 'B03', 'B05', 'T01', 'T04', 'T05', 'I02', 'I05', 'J02'],
   'cards': ['BD-ESSAY', 'BD-B01', 'BD-B03', 'BD-T01', 'BD-T04', 'BD-T05', 'BD-I02', 'BD-I05', 'BD-J02']},
  {'id': 'D2', 'series': 'Specimen 2023', 'q': '9708/04 Q2', 'command': 'Assess', 'ask': '正外部性：借助图评估干预能否成功纠正', 'points': ['ESSAY-POS', 'B01', 'B07', 'S01', 'S02', 'S04', 'S05', 'S07', 'I03', 'D01', 'D02', 'D03'],
   'cards': ['BD-POS-ESSAY', 'BD-B01', 'BD-B07', 'BD-S01', 'BD-S04', 'BD-S05', 'BD-S07', 'BD-I03', 'BD-D01', 'BD-D02', 'BD-D03']},
  {'id': 'D3', 'series': 'May/June 2023', 'q': '9708/42 Q2', 'command': 'Assess', 'ask': '两项政策鼓励电动车', 'points': ['J04', 'S01', 'T01', 'J02'], 'cards': ['BD-S01', 'BD-T01', 'BD-J02']},
  {'id': 'D4', 'series': 'Feb/Mar 2024', 'q': '9708/42 Q2', 'command': 'Assess', 'ask': 'climate change：价格机制干预', 'points': ['T01', 'T05', 'R01', 'J02'], 'cards': ['BD-T01', 'BD-T05', 'BD-J02']},
  {'id': 'D5', 'series': 'Oct/Nov 2024', 'q': '9708/41 Q2', 'command': 'Assess', 'ask': '两项政策降低负外部性是否改善配置效率', 'points': ['E01', 'T01', 'I02', 'J02'], 'cards': ['BD-T01', 'BD-I02', 'BD-J02']},
  {'id': 'D6', 'series': 'Oct/Nov 2025', 'q': '9708/42 Q2', 'command': 'Assess', 'ask': 'congestion：补贴或提供替代公共交通', 'points': ['J04b', 'S01', 'D01'], 'cards': ['BD-S01', 'BD-D01']},
  {'id': 'D7', 'series': 'Feb/Mar 2024', 'q': '9708/32 Q3', 'ask': '由 total WTP 与 total EB 求新增产量的 MSB', 'points': ['B10', 'B02b'], 'cards': [], 'not_carded': '板书未覆盖，由旧卡 B10、B02b 承担'},
  {'id': 'D8', 'series': 'Oct/Nov 2025', 'q': '9708/32 Q9', 'ask': 'nudge 的本质特征', 'points': ['I04'], 'cards': ['BD-I04']},
  {'id': 'D9', 'series': 'Oct/Nov 2025', 'q': '9708/32 Q8', 'ask': '补贴可能改善 allocative efficiency', 'points': ['S01', 'S04'], 'cards': ['BD-S01', 'BD-S04']},
  {'id': 'D10', 'series': 'Feb/Mar 2024', 'q': '9708/32 Q12', 'ask': '公共垃圾收集的理由', 'points': ['D01', 'D01b'], 'cards': ['BD-D01']},
  {'id': 'D11', 'series': 'Oct/Nov 2017', 'q': '9708/33 Q16', 'ask': 'property rights 的作用', 'points': ['P01', 'P02'], 'cards': ['BD-P01', 'BD-P02']},
  {'id': 'D12', 'series': 'Oct/Nov 2025', 'q': '9708/32 Q6', 'ask': 'optimal output 依 MSB=MSC，不是污染为零', 'points': ['B03', 'B09'], 'cards': ['BD-B03']},
 ],
 'coverage': {
  'scope': '板书01 Externalities：外部性与政府干预（9708 7.3.5、7.4.1–7.4.5、8.1.1、8.1.2 的相关部分）；本包只含板书写了的知识点，其余由旧卡组承担',
  'status': 'complete', 'remaining': '',
  'saturation': '沿用 2026-10-03 制作记录：essay 6 场加 1 份 specimen、选择题 20 道（2017–2025）；最近三个考季（2024 F/M、2024 O/N、2025 O/N）没有出现新的问法类型',
  'backcheck': [
   {'paper': '9708/42', 'series': '2023-03', 'q': '2', 'result': 'pass', 'fixed_by': [],
    'note': '定义（BD-B01）、market failure 论证（BD-B03）、tax 与信息两项政策（BD-T01、BD-I02）、AO3（BD-T05、BD-T04、BD-I05、BD-J02）；负消费外部性图由旧卡 B05 承担'},
   {'paper': '9708/04', 'series': 'specimen-2023', 'q': '2', 'result': 'pass', 'fixed_by': [],
    'note': '图（BD-B07、BD-S01）、补贴／信息／直接提供三条机制、各政策局限与结论（BD-S04–S07、BD-I03、BD-D01–D03、BD-POS-ESSAY）'}],
  'coldread': [],
  'items': items},
 'terms_known': [{'term': 'subsidy', 'taught_in': ['BD-S01']}, {'term': 'nudge', 'taught_in': ['BD-I04']}, {'term': 'property rights', 'taught_in': ['BD-P01']}, {'term': 'regulation', 'taught_in': ['BD-R02', 'BD-R03']}, {'term': 'direct provision', 'taught_in': ['BD-D01']}, {'term': 'market failure', 'taught_in': ['BD-B03']}],
 'ignore_words': [],
 'cards': cards,
}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(cards), 'cards', len(items), 'items')
