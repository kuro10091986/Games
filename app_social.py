import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="小学校社会：一問一答マスター", layout="centered", page_icon="🗾")

# === 【全50問】社会科クイズデータベース ===
SOCIAL_QUIZ_DATA = [
    # --- 地理：日本の国土・気候・産業 ---
    {"question": "日本のまわりにある3つの大きな海（三大洋）のうち、東側に広がる海は何ですか？", "answer": "太平洋", "distractors": ["日本海", "大西洋", "インド洋"]},
    {"question": "日本の位置を緯度と経度で表すと、北緯と何経の範囲にありますか？", "answer": "東経", "distractors": ["西経", "南緯", "赤道"]},
    {"question": "日本の領土の最も東にある島は何ですか？", "answer": "南鳥島（みなみとりしま）", "distractors": ["沖ノ鳥島", "択捉島", "与那国島"]},
    {"question": "日本の領土の最も南にある島は何ですか？", "answer": "沖ノ鳥島（おきのとりしま）", "distractors": ["南鳥島", "石垣島", "宮古島"]},
    {"question": "日本の川は外国に比べて「長さ」と「流れ」にどのような特徴がありますか？", "answer": "長さは短く、流れは急である", "distractors": ["長さは長く、流れは緩やか", "長さは短く、流れは緩やか", "長さは長く、流れは急である"]},
    {"question": "夏から秋に雨が多く、冬は晴れの日が多いのは、日本海側と太平洋側のどちらの気候ですか？", "answer": "太平洋側の気候", "distractors": ["日本海側の気候", "瀬戸内の気候", "北海道の気候"]},
    {"question": "一年中あたたかく、雨が多い気候を利用して、さとうきびなどの栽培がさかんな県はどこですか？", "answer": "沖縄県", "distractors": ["鹿児島県", "高知県", "宮崎県"]},
    {"question": "米があまるようになったため、水田を減らして生産をおさえる政策を何といいますか？", "answer": "生産調整（減反）", "distractors": ["地租改正", "農地改革", "二毛作"]},
    {"question": "寒い時期にビニールハウスなどを使い、野菜を早く育てる栽培方法を何といいますか？", "answer": "促成栽培（そくせいさいばい）", "distractors": ["抑制栽培", "有機栽培", "高冷地農業"]},
    {"question": "国内で消費される食料のうち、国内で生産されたものの割合を何といいますか？", "answer": "食料自給率", "distractors": ["食料輸入率", "国内総生産", "地産地消率"]},
    {"question": "稚魚（ちぎょ）を施設で大きくなるまで育ててからとる漁業を何といいますか？", "answer": "養殖漁業（ようしょくぎょぎょう）", "distractors": ["栽培漁業", "遠洋漁業", "沖合漁業"]},
    {"question": "太平洋沿岸に工業地帯や地域がつらなっている地域を何といいますか？", "answer": "太平洋ベルト", "distractors": ["工業専用地域", "臨海工業地帯", "京浜工業地帯"]},
    {"question": "自動車産業が非常にさかんな、愛知県を中心とした工業地帯は何ですか？", "answer": "中京工業地帯", "distractors": ["阪神工業地帯", "北九州工業地帯", "瀬戸内工業地域"]},
    {"question": "従業員が300人未満の、小規模な工場のことを何といいますか？", "answer": "中小工場（中小企業）", "distractors": ["大企業", "家内工業", "国営工場"]},
    {"question": "八代海沿岸で発生した、水のよごれが原因の公害病は何ですか？", "answer": "水俣病（みなまたびょう）", "distractors": ["イタイイタイ病", "四日市ぜんそく", "新潟水俣病"]},

    # --- 歴史：縄文時代～江戸時代 ---
    {"question": "縄のような文様がついた、縄文時代に使われていた土器を何といいますか？", "answer": "縄文土器", "distractors": ["弥生土器", "埴輪", "青磁"]},
    {"question": "弥生時代に30ほどの国をしたがえた、邪馬台国の女王はだれですか？", "answer": "卑弥呼（ひみこ）", "distractors": ["推古天皇", "持統天皇", "北条政子"]},
    {"question": "王や豪族をほうむるためにつくられた、巨大な墓を何といいますか？", "answer": "古墳（こふん）", "distractors": ["寺院", "ピラミッド", "貝塚"]},
    {"question": "聖徳太子が定めた、役人の心構えを示したきまりを何といいますか？", "answer": "十七条の憲法", "distractors": ["大宝律令", "御成敗式目", "武家諸法度"]},
    {"question": "710年に、唐（中国）にならって奈良につくられた都を何といいますか？", "answer": "平城京", "distractors": ["平安京", "藤原京", "難波京"]},
    {"question": "11世紀初めに摂政となり、藤原氏の全盛期をきずいた人物はだれですか？", "answer": "藤原道長", "distractors": ["藤原頼通", "藤原不比等", "平清盛"]},
    {"question": "「枕草子」を書いた、平安時代の女性作家はだれですか？", "answer": "清少納言", "distractors": ["紫式部", "和泉式部", "樋口一葉"]},
    {"question": "1192年に征夷大将軍になり、鎌倉幕府を開いたのはだれですか？", "answer": "源頼朝（みなもとのよりとも）", "distractors": ["源義経", "足利尊氏", "北条時宗"]},
    {"question": "鎌倉時代、日本をしたがえようと二度にわたり攻めてきた国を何といいますか？", "answer": "元（げん）", "distractors": ["唐", "宋", "明"]},
    {"question": "足利義満が京都に建てた、金色の建物（北山文化）を何といいますか？", "answer": "金閣", "distractors": ["銀閣", "法隆寺", "東大寺"]},
    {"question": "室町時代に中国にわたって、すみ絵（水墨画）を学んだ人物はだれですか？", "answer": "雪舟（せっしゅう）", "distractors": ["運慶", "葛飾北斎", "狩野永徳"]},
    {"question": "1549年に来日し、キリスト教を伝えた宣教師はだれですか？", "answer": "ザビエル", "distractors": ["ペリー", "マルコ・ポーロ", "ルイス・フロイス"]},
    {"question": "室町幕府をほろぼしたが、家臣の明智光秀にそむかれ本能寺で自害した人物は？", "answer": "織田信長", "distractors": ["豊臣秀吉", "徳川家康", "今川義元"]},
    {"question": "刀狩や検地を行い、全国統一をなしとげた人物はだれですか？", "answer": "豊臣秀吉", "distractors": ["織田信長", "足利義昭", "上杉謙信"]},
    {"question": "1603年に江戸幕府を開いた人物はだれですか？", "answer": "徳川家康", "distractors": ["徳川家光", "徳川吉宗", "徳川慶喜"]},
    {"question": "徳川家光が定めた、大名が1年おきに江戸と領地を往復する制度は何ですか？", "answer": "参勤交代", "distractors": ["鎖国", "武家諸法度", "目安箱"]},
    {"question": "キリスト教の禁止を強め、外国との交流を制限した状態を何といいますか？", "answer": "鎖国（さこく）", "distractors": ["開国", "参勤交代", "文明開化"]},
    {"question": "オランダ語の書物からヨーロッパの知識を学ぶ学問を何といいますか？", "answer": "蘭学（らんがく）", "distractors": ["国学", "儒学", "仏教"]},
    {"question": "葛飾北斎や歌川広重などがえがいた、版画の絵を何といいますか？", "answer": "浮世絵（うきよえ）", "distractors": ["水墨画", "大和絵", "油絵"]},

    # --- 歴史：明治時代～現代 ---
    {"question": "江戸時代の終わりに浦賀へ来航し、日本に開国を求めたアメリカの使者は？", "answer": "ペリー", "distractors": ["ハリス", "マッカーサー", "ザビエル"]},
    {"question": "1867年に江戸幕府の15代将軍が政権を朝廷に返したことを何といいますか？", "answer": "大政奉還（たいせいほうかん）", "distractors": ["版籍奉還", "廃藩置県", "明治維新"]},
    {"question": "「学問のすゝめ」を書き、人間の平等や学問の大切さを説いた人物はだれですか？", "answer": "福沢諭吉", "distractors": ["夏目漱石", "野口英世", "新渡戸稲造"]},
    {"question": "初代の内閣総理大臣になり、憲法づくりに取り組んだ人物はだれですか？", "answer": "伊藤博文", "distractors": ["板垣退助", "大隈重信", "桂太郎"]},
    {"question": "西洋風のくらしや文化が広まった、明治時代の様子を何といいますか？", "answer": "文明開化", "distractors": ["富国強兵", "殖産興業", "鎖国"]},
    {"question": "1904年、韓国や満州をめぐる対立から始まった日本とロシアの戦争は？", "answer": "日露戦争", "distractors": ["日清戦争", "第一次世界大戦", "太平洋戦争"]},
    {"question": "1941年に始まった、アメリカやイギリスなどとの戦争を何といいますか？", "answer": "太平洋戦争", "distractors": ["日露戦争", "日中戦争", "ベトナム戦争"]},
    {"question": "1946年に公布された、現在の日本の憲法を何といいますか？", "answer": "日本国憲法", "distractors": ["大日本帝国憲法", "十七条の憲法", "平和憲法"]},

    # --- 公民：政治と世界 ---
    {"question": "日本国憲法の三つの基本原則は、国民主権、基本的人権の尊重と、あと一つは何ですか？", "answer": "平和主義", "distractors": ["軍備増強", "天皇主権", "中央集権"]},
    {"question": "日本国憲法では、天皇は国や国民のまとまりの何と定められていますか？", "answer": "象徴（しょうちょう）", "distractors": ["首長", "統治者", "神"]},
    {"question": "法律をつくったり、予算を決めたりする国の機関を何といいますか？", "answer": "国会（立法権）", "distractors": ["内閣", "裁判所", "市役所"]},
    {"question": "内閣の代表で、国会によって選ばれる人を何といいますか？", "answer": "内閣総理大臣", "distractors": ["大統領", "衆議院議長", "外務大臣"]},
    {"question": "国民が裁判に参加し、有罪か無罪かを判断する制度を何といいますか？", "answer": "裁判員制度", "distractors": ["陪審制", "司法試験", "検察制度"]},
    {"question": "核兵器を「もたない、つくらない、もちこませない」という原則を何といいますか？", "answer": "非核三原則", "distractors": ["核拡散防止", "平和条約", "安全保障"]},
    {"question": "世界の平和と安全を守るために1945年に発足した国際組織は何ですか？", "answer": "国際連合", "distractors": ["国際連盟", "EU", "NATO"]},
    {"question": "開発と環境のバランスをとり、未来に豊かな生活を残せる社会を何といいますか？", "answer": "持続可能な社会（SDGs関連）", "distractors": ["高度経済成長", "情報化社会", "格差社会"]}
]

# --- ゲームエンジン部分 ---
if 'soc_score' not in st.session_state:
    st.session_state.update({
        'soc_score': 0, 'soc_total_count': 0, 'soc_current_id': -1,
        'soc_remaining_ids': list(range(len(SOCIAL_QUIZ_DATA))),
        'soc_repeat_mode': False, 'soc_answered': False
    })

def generate_question():
    if st.session_state.soc_repeat_mode:
        quiz_id = st.session_state.soc_current_id
    else:
        if not st.session_state.soc_remaining_ids:
            st.session_state.soc_current_id = -99
            return
        quiz_id = random.choice(st.session_state.soc_remaining_ids)
        st.session_state.soc_current_id = quiz_id

    quiz_data = SOCIAL_QUIZ_DATA[quiz_id]
    options = list(quiz_data["distractors"]) + [quiz_data["answer"]]
    random.shuffle(options)
    st.session_state.update({
        'soc_question': quiz_data["question"], 'soc_answer': quiz_data["answer"],
        'soc_options': options, 'soc_answered': False, 'soc_is_correct': False
    })

if st.session_state.soc_current_id == -1:
    generate_question()

st.title("🗾 社会科：一問一答マスター")
st.caption(f"地理・歴史・公民 全{len(SOCIAL_QUIZ_DATA)}問")

if st.session_state.soc_current_id == -99:
    st.balloons()
    st.success("✨ 全問正解！素晴らしい知識です。")
    st.metric("最終スコア", f"{st.session_state.soc_score} / {st.session_state.soc_total_count}")
    if st.button("もう一度挑戦する"):
        st.session_state.update({'soc_score': 0, 'soc_total_count': 0, 'soc_remaining_ids': list(range(len(SOCIAL_QUIZ_DATA))), 'soc_current_id': -1, 'soc_repeat_mode': False})
        st.rerun()
else:
    st.subheader(f"問題: {st.session_state.soc_question}")
    
    with st.form(key='soc_form'):
        user_choice = st.radio("答えを選んでください", st.session_state.soc_options, index=None)
        if st.form_submit_button("回答する"):
            if user_choice:
                st.session_state.soc_answered = True
                st.session_state.soc_total_count += 1
                if user_choice == st.session_state.soc_answer:
                    st.session_state.soc_is_correct = True
                    if st.session_state.soc_current_id in st.session_state.soc_remaining_ids:
                        st.session_state.soc_remaining_ids.remove(st.session_state.soc_current_id)
                    st.session_state.soc_repeat_mode = False
                else:
                    st.session_state.soc_is_correct = False
                    st.session_state.soc_repeat_mode = True
                st.rerun()
            else:
                st.warning("選択肢を選んでください。")

    if st.session_state.soc_answered:
        if st.session_state.soc_is_correct:
            st.success(f"⭕ 正解！「{st.session_state.soc_answer}」")
            if st.button("次の問題へ"):
                generate_question()
                st.rerun()
        else:
            st.error(f"❌ 残念！正解は「{st.session_state.soc_answer}」でした。")
            if st.button("もう一度挑戦（正解するまで進めません！）"):
                generate_question()
                st.rerun()

    st.divider()
    st.write(f"スコア: {st.session_state.soc_score} / {st.session_state.soc_total_count} (残り: {len(st.session_state.soc_remaining_ids)}問)")