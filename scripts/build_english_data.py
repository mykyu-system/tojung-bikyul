import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'Mykyu-system_TOJEONG_100_FINAL.json'
OUT = ROOT / 'data/en'
OUT.mkdir(parents=True, exist_ok=True)

raw = json.loads(SRC.read_text(encoding='utf-8'))

NAMES = {
    '각골난망': 'Never Forgetting Kindness', '견인지로': 'Perseverance Opens the Way',
    '계명성효': 'Diligence and Loyalty', '고진감래': 'Sweetness After Hardship',
    '과유불급': 'Moderation', '구사일생': 'Narrow Escape', '금상첨화': 'Adding Beauty to Good Fortune',
    '금옥만당': 'Abundant Wealth', '금의환향': 'Returning in Glory', '난형난제': 'Evenly Matched',
    '다다익선': 'The More the Better', '대기만성': 'Greatness Takes Time', '대동단결': 'Unity',
    '동고동락': 'Sharing Joy and Sorrow', '동귀어진': 'Shared Fate', '동병상련': 'Shared Hardship',
    '동분서주': 'Busy Pursuit', '동상이몽': 'Different Motives', '등고자비': 'Step by Step',
    '등용문': 'Gateway to Success', '마부위침': 'Persistence', '막상막하': 'Evenly Matched',
    '만사형통': 'Everything Goes Smoothly', '만시지탄': 'Regret of Delay',
    '망양보뢰': 'Repair Before It Is Too Late', '맹모삼천': 'A Good Environment Matters',
    '명경지수': 'Clear Mind', '명월청풍': 'Clear Moon and Gentle Wind', '무위자연': 'Natural Flow',
    '문경지교': 'Deep Friendship', '반포지효': 'Filial Devotion', '배수진': 'Last Stand',
    '백년대계': 'Long-Term Plan', '백년해로': 'Lifelong Harmony', '백발백중': 'High Accuracy',
    '백년하청': 'Uncertain Waiting', '부귀영화': 'Prosperity and Honor',
    '부화뇌동': 'Following Others Blindly', '불로장생': 'Longevity',
    '불치하문': 'Willingness to Learn', '비룡재천': 'Dragon Rising to Heaven',
    '사면초가': 'Surrounded by Difficulties', '사상누각': 'Unstable Foundation',
    '사필귀정': 'Justice Prevails', '산고수장': 'Enduring Strength',
    '삼고초려': 'Persistent Effort', '삼인성호': 'Rumor Gains Power',
    '상부상조': 'Mutual Support', '새옹지마': 'Fortune Can Change', '선견지명': 'Foresight',
    '설상가상': 'One Difficulty After Another', '수어지교': 'Close Harmony',
    '수원목본': 'Strong Roots', '수적석천': 'Persistence Wears Down Obstacles',
    '수적천석': 'Persistence', '순풍만리': 'Smooth Sailing', '순풍순수': 'Favorable Flow',
    '승승장구': 'Continuous Success', '안분지족': 'Contentment', '안하무인': 'Arrogance',
    '양호유환': 'Hidden Trouble', '어변성룡': 'Transformation and Rise',
    '역지사지': 'Consider the Other Side', '오매불망': 'Deep Longing',
    '온고지신': 'Learn from the Past', '와신상담': 'Determined Endurance',
    '용두사미': 'Strong Start, Weak Finish', '용비어천': 'Ascending Dragon',
    '우공이산': 'Persistent Effort Moves Mountains', '우후죽순': 'Rapid Growth',
    '운개일출': 'Clouds Clear, Sun Appears', '운중신룡': 'Dragon in the Clouds',
    '월명천심': 'Bright Moon, Clear Heart', '유비무환': 'Preparedness Prevents Trouble',
    '유종지미': 'Good Finish', '유지경성': 'Steady Persistence Succeeds',
    '이심전심': 'Understanding Without Words', '일거양득': 'Two Gains at Once',
    '일사천리': 'Rapid Progress', '일석이조': 'Two Gains at Once',
    '일출동산': 'Sunrise Over the East', '일취월장': 'Rapid Improvement',
    '입신양명': 'Achievement and Recognition', '자업자득': 'You Reap What You Sow',
    '자포자기': 'Giving Up on Oneself', '전화위복': 'Adversity Turns to Opportunity',
    '절차탁마': 'Refinement Through Effort', '점입가경': 'Improving Gradually',
    '조삼모사': 'Short-Term Thinking', '좌정관천': 'Limited Perspective',
    '준비': 'Preparation', '지피지기': 'Know Yourself and Others',
    '진퇴양난': 'Difficult Choice', '천고마비': 'A Season of Abundance',
    '천생연분': 'Natural Match', '천재일우': 'Rare Opportunity',
    '천지개태': 'Renewal and Opening', '천하태평': 'Peace and Ease',
    '청운지지': 'High Ambition', '청출어람': 'Surpassing the Teacher',
    '초목우로': 'Nourishment and Growth', '춘풍득의': 'Spring Breeze and Success',
    '타산지석': 'Learn from Others', '풍전등화': 'Precarious Situation',
    '한천빙해': 'Cold and Frozen Conditions', '호가호위': 'Borrowed Authority',
    '호연지기': 'Moral Courage', '혼정신성': 'Family Care and Duty',
    '화개만천': 'Good Fortune Spreads', '화기애애': 'Harmony and Warmth',
    '화룡점정': 'Finishing Touch', '화이부동': 'Harmony Without Conformity'
}

GRADES = {'대길': 'Excellent', '길': 'Favorable', '평길': 'Balanced', '주의': 'Caution', '신중': 'Prudent'}

UPPER = {
    1: ('Heaven', 'clear initiative and responsible leadership', 'disciplined expansion', 'visible ownership', 'direct, considerate communication', 'a sustainable pace that prevents burnout'),
    2: ('Lake', 'open exchange and well-chosen alliances', 'value created through negotiation', 'collaboration and client trust', 'warmth without vague promises', 'regular recovery and emotional balance'),
    3: ('Fire', 'clarity, visibility, and accurate judgment', 'transparent numbers and informed choices', 'recognition earned through precision', 'honest expression without drama', 'protecting sleep and mental focus'),
    4: ('Thunder', 'timely movement and constructive beginnings', 'quick action with a firm spending limit', 'decisive starts and practical experiments', 'speaking early before tension builds', 'managing surges of energy carefully'),
    5: ('Wind', 'adaptability and steady influence', 'flexible planning and diversified income', 'persuasion, learning, and gradual reach', 'listening closely and adjusting gently', 'consistent routines and good circulation'),
    6: ('Water', 'depth, patience, and careful risk reading', 'liquidity, reserves, and downside control', 'specialized work done with discretion', 'trust built through calm consistency', 'rest, hydration, and measured intensity'),
    7: ('Mountain', 'restraint, boundaries, and durable foundations', 'saving first and committing selectively', 'expertise, concentration, and firm standards', 'respectful distance and dependable support', 'posture, mobility, and restorative rest'),
    8: ('Earth', 'support, patience, and practical stewardship', 'steady accumulation and useful assets', 'reliable execution behind the scenes', 'care expressed through consistent actions', 'simple habits, nourishment, and grounding')
}

MIDDLE = {
    1: ('Opening', 'choosing one clear opening before expanding'),
    2: ('Alignment', 'bringing people, timing, and resources into alignment'),
    3: ('Execution', 'turning preparation into visible, measurable work'),
    4: ('Adjustment', 'reviewing feedback and correcting course early'),
    5: ('Consolidation', 'strengthening what already works before adding more'),
    6: ('Reflection', 'reducing noise and waiting for the right signal')
}

LOWER = {
    1: ('Initiation', 'act once the facts are clear', 'rushing the first move'),
    2: ('Cooperation', 'coordinate expectations before committing', 'assuming that others understood'),
    3: ('Completion', 'finish, document, and close the loop', 'leaving details unresolved')
}

MONTHS = [
    ('January', 'set foundations and clear unfinished work', 'reset the budget and recurring costs', 'starting too many priorities'),
    ('February', 'build dependable alliances and test mutual expectations', 'review shared expenses and negotiated terms', 'mistaking friendliness for agreement'),
    ('March', 'make the first visible move on a prepared plan', 'direct money toward tools that improve execution', 'acting before the numbers are confirmed'),
    ('April', 'review results and correct course without losing momentum', 'check contracts, fees, and payment timing', 'defending an old plan after conditions change'),
    ('May', 'pursue growth while protecting quality and capacity', 'capture gains without expanding fixed costs too quickly', 'overestimating available time or cash'),
    ('June', 'turn steady effort into measurable progress', 'collect what is owed and strengthen cash flow', 'letting a busy schedule hide weak margins'),
    ('July', 'simplify commitments and protect energy', 'favor reserves and essential spending', 'forcing progress during a low-energy stretch'),
    ('August', 'negotiate, reconnect, and widen practical options', 'compare offers and improve terms before signing', 'accepting attractive conditions without reading details'),
    ('September', 'separate durable opportunities from distractions', 'prioritize dependable returns over excitement', 'following other people’s urgency'),
    ('October', 'complete high-value work and secure the result', 'lock in gains and settle important accounts', 'confusing momentum with unlimited capacity'),
    ('November', 'consolidate, document, and reduce exposure', 'organize taxes, records, debt, and reserves', 'postponing an uncomfortable but necessary review'),
    ('December', 'close the year cleanly and prepare the next cycle', 'finish the year with a realistic balance sheet', 'making emotional year-end commitments')
]

DETAILS = {
    'investment': ('For investing', 'position size, evidence, and an exit rule', 'Set the maximum acceptable loss before entry and increase exposure only after the thesis is confirmed'),
    'job_change': ('For a job change', 'role clarity, stability, and the real cost of transition', 'Compare the daily work, decision authority, and six-month outlook rather than relying on the title alone'),
    'promotion_exam': ('For promotion or exams', 'consistent preparation and visible proof of competence', 'Turn the goal into a weekly schedule and keep evidence of completed work'),
    'real_estate': ('For property decisions', 'location, financing, maintenance, and resale conditions', 'Inspect the downside case as carefully as the hoped-for return'),
    'document_contract': ('For documents and contracts', 'dates, obligations, exceptions, and written confirmation', 'Record every material promise and verify the final version before signing'),
    'children_family': ('For family matters', 'reliable support without taking over another person’s choices', 'Offer a stable framework, then leave room for each person to carry an appropriate share'),
    'social': ('For social connections', 'quality of trust rather than number of contacts', 'Give more time to reciprocal relationships and less to repeated ambiguity'),
    'accident': ('For safety', 'fatigue, haste, traffic, tools, and preventable distractions', 'Slow down at transitions, especially when attention is divided or the schedule is compressed'),
    'travel_move': ('For travel or relocation', 'timing, backup plans, documents, and realistic costs', 'Confirm the route, paperwork, budget, and fallback before the point of no return')
}

HEALTH_GUARD = {
    1: 'overexertion after a fast start',
    2: 'stress carried from unspoken expectations',
    3: 'fatigue created by unfinished obligations'
}


def score_tone(score):
    if score >= 90:
        return 'strong momentum supports decisive but accountable action'
    if score >= 82:
        return 'conditions are favorable when opportunity is matched with preparation'
    if score >= 74:
        return 'steady progress is available through sequencing and consistency'
    if score >= 66:
        return 'selective action and careful review matter more than speed'
    return 'restraint, recovery, and risk control should come first'


def month_tone(score):
    if score >= 86:
        return 'The monthly current is strong, so a well-prepared move can be advanced with confidence'
    if score >= 80:
        return 'The monthly current is supportive, especially for practical work already in motion'
    if score >= 74:
        return 'The monthly current is workable, but progress will depend on pacing and follow-through'
    if score >= 68:
        return 'The monthly current is mixed, so protect the downside before seeking expansion'
    return 'The monthly current is quiet; preserve resources and avoid forcing a result'


def differentiated_month_score(source_score, overall_score, upper, middle, lower, month):
    seasonal = [0, 1, 2, -1, 3, 1, -2, 2, 0, 3, -1, 1]
    resonance = (upper * 11 + middle * 7 + lower * 5 + month * upper + (13 - month) * middle + month * month * lower) % 15 - 7
    anchored = round((int(source_score) * 2 + int(overall_score)) / 3)
    return max(48, min(96, anchored + seasonal[month - 1] + resonance))


def build_reading(g, index):
    upper, middle, lower = (int(part) for part in g['code'].split('-'))
    u = UPPER[upper]
    m = MIDDLE[middle]
    l = LOWER[lower]
    name = NAMES.get(g['name'], f'Reading {index:03d}')
    marker = f"{u[0]}–{m[0]}–{l[0]} pattern"
    score = int(g['overall_score'])
    tone = score_tone(score)

    result = {
        'code': g['code'],
        'name': name,
        'interpretation_type': 'traditional_structure_modern_english_v2',
        'disclaimer': 'This modern English interpretation is based on the traditional 144-reading structure and is intended for cultural reflection and entertainment, not medical, legal, or financial decision-making.',
        'overall_score': score,
        'summary': f"{name} frames 2026 as a year of {u[1]}. In this reading, the {marker} favors {m[1]} and asks you to {l[1]}. With an overall score of {score}, {tone}.",
        'money': f"Financially, {name} emphasizes {u[2]}. Under the {marker}, improve one dependable source of value, keep commitments proportional to cash flow, and let {l[0].lower()} govern any increase in risk.",
        'career': f"In work and career, {name} highlights {u[3]}. The {m[0].lower()} phase rewards {m[1]}; make responsibilities visible and {l[1]} when an opportunity becomes concrete.",
        'relationship': f"In relationships, {name} calls for {u[4]}. The {marker} grows stronger when expectations are spoken plainly, room is left for response, and you {l[1]} rather than guessing.",
        'health': f"For wellbeing, {name} points toward {u[5]}. Let the {m[0].lower()} phase shape your routine, and pay attention to {HEALTH_GUARD[lower]}, especially when fatigue begins to rise.",
        'keywords': [name, u[0], m[0], l[0]],
        'grade': GRADES.get(g.get('grade'), 'Balanced')
    }

    detailed = {}
    for key, (opener, focus, guidance) in DETAILS.items():
        detailed[key] = f"{opener}, {name} directs attention to {focus}. {guidance}. Within the {marker}, {l[1]} and avoid {l[2]} when the stakes increase."
    detailed['final'] = f"Final judgment: {name} carries a {score}/100 annual tone. {tone.capitalize()}. Follow the {marker} by focusing on {u[1]}, {m[1]}, and the discipline to {l[1]}."
    result['detailed'] = detailed

    months = []
    summaries = []
    for source_month in g.get('months', []):
        month_number = int(source_month['month'])
        month_name, flow_focus, money_focus, caution_focus = MONTHS[month_number - 1]
        monthly_score = differentiated_month_score(source_month['score'], score, upper, middle, lower, month_number)
        flow = f"In {month_name}, {name} supports efforts to {flow_focus}. {month_tone(monthly_score)}; use {u[1]} while {m[1]}."
        money = f"For {month_name} finances, {money_focus}. At {monthly_score}/100, the {marker} rewards {u[2]}; let {l[0].lower()} guide the decision."
        caution = f"{month_name}’s main watchpoint is {caution_focus}. Within the {marker}, guard against {l[2]} so the momentum of {name} remains practical and controlled."
        months.append({'month': month_number, 'score': monthly_score, 'flow': flow, 'money': money, 'caution': caution})
        summaries.append({'month': month_number, 'score': monthly_score, 'headline': flow, 'money': money, 'caution': caution})
    result['months'] = months
    result['monthly_summary'] = summaries
    return result


readings = [build_reading(g, i) for i, g in enumerate(raw['gwae'], 1)]
if len(readings) != 144 or len({g['code'] for g in readings}) != 144:
    raise RuntimeError('The source must contain exactly 144 unique reading codes.')
if any(len(g['months']) != 12 for g in readings):
    raise RuntimeError('Every reading must contain exactly 12 monthly results.')

for i in range(8):
    target = OUT / f'gua-{i + 1:02d}.json'
    target.write_text(json.dumps(readings[i * 18:(i + 1) * 18], ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

stems = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
branches = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai']
cycle = [stems[i % 10] + '-' + branches[i % 12] for i in range(60)]
kr_stems = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
kr_branches = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']
kr_cycle = [kr_stems[i % 10] + kr_branches[i % 12] for i in range(60)]
refs = {}
for i, key in enumerate(kr_cycle):
    value = raw['calculation']['jogyeonpyo'][key]
    refs[cycle[i]] = {'yearNumber': value['태세수'], 'monthNumber': value['월건수'], 'dayNumber': value['일진수']}

for number, (start, end) in enumerate([(1900, 1929), (1930, 1959), (1960, 1989), (1990, 2019), (2020, 2050)], 1):
    solar = {k: {kk: vv for kk, vv in v.items() if kk != 'dayGanji'} for k, v in raw['calculation']['solar_to_lunar'].items() if start <= int(k[:4]) <= end}
    lunar = {k: v for k, v in raw['calculation']['lunar_to_solar'].items() if start <= int(k[:4]) <= end}
    month_days = {k: v for k, v in raw['calculation']['month_days'].items() if start <= int(k[:4]) <= end}
    target = OUT / f'calendar-{number:02d}.json'
    target.write_text(json.dumps({'solarToLunar': solar, 'lunarToSolar': lunar, 'monthDays': month_days}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

manifest = {
    'version': '2.0.0-verified',
    'language': 'en',
    'name': 'Mykyu-system Personal Fortune',
    'description': 'Verified English 144-reading fortune data and calendar calculation data.',
    'supportedYears': [1900, 2050],
    'readingYear': 2026,
    'guaFiles': [f'gua-{i:02d}.json' for i in range(1, 9)],
    'calendarFiles': [f'calendar-{i:02d}.json' for i in range(1, 6)],
    'sexagenaryCycle': cycle,
    'cycleReference': refs,
    'validationExamples': raw['calculation'].get('validation_examples', []),
    'disclaimer': 'Traditional cultural fortune content for reflection and entertainment, not a scientific prediction.'
}
(OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
