import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="小学校理科：一問一答マスター", layout="centered", page_icon="🔬")

# === 【全50問以上】理科クイズ完全データベース ===
# 新しく追加された50問を中心に、これまでの内容をすべて統合しました。
SCIENCE_QUIZ_DATA = [
    # --- 植物のつくりとはたらき ---
    {"question": "種子の中のでんぷんが、発芽や成長に使われることを調べるために使う薬品は何ですか？", "answer": "ヨウ素液", "distractors": ["石灰水", "ベネジクト液", "塩酸"]},
    {"question": "ヨウ素液はでんぷんに反応すると、何色に変化しますか？", "answer": "青むらさき色", "distractors": ["赤色", "緑色", "黄色"]},
    {"question": "植物のからだの中の水が、水蒸気となって葉などから出ていくことを何といいますか？", "answer": "蒸散（じょうさん）", "distractors": ["光合成", "呼吸", "気化"]},
    {"question": "植物の成長に必要な3つの主な条件は、「水」「日光」とあと一つは何ですか？", "answer": "肥料", "distractors": ["土", "空気", "温度"]},
    {"question": "葉に日光が当たるとでんぷんができることを調べる際、日光を当てない葉を包むものは何ですか？", "answer": "アルミニウムはく", "distractors": ["ラップ", "黒い紙", "ビニール袋"]},
    {"question": "実ができるために、花粉がめしべの先に付くことを何といいますか？", "answer": "受粉（じゅふん）", "distractors": ["受精", "光合成", "発芽"]},
    
    # --- 動物のからだとメダカのたんじょう ---
    {"question": "メダカのたまご（卵）と、おすが出した何が結びつくと子メダカになりますか？", "answer": "精子（せいし）", "distractors": ["花粉", "胞子", "栄養"]},
    {"question": "卵と精子が結びつくことを何といいますか？", "answer": "受精（じゅせい）", "distractors": ["受粉", "ふ化", "脱皮"]},
    {"question": "血液を全身に送り出すポンプの役割をしているからだの部分は何ですか？", "answer": "心臓（しんぞう）", "distractors": ["肺", "胃", "肝臓"]},
    {"question": "血液中の余分な水や不要なものをこしとって尿にする、からだの部分は何ですか？", "answer": "じん臓", "distractors": ["肝臓", "心臓", "小腸"]},
    {"question": "ヒトが酸素を取り入れ、二酸化炭素を出すことを何といいますか？", "answer": "呼吸（こきゅう）", "distractors": ["消化", "循環", "排出"]},
    {"question": "呼吸に関わる器官で、気管の先にある左右一対の大きな袋状のものは何ですか？", "answer": "肺（はい）", "distractors": ["心臓", "胃", "ぼうこう"]},
    {"question": "食べたものを吸収されやすい形に変えるはたらきを何といいますか？", "answer": "消化（しょうか）", "distractors": ["吸収", "呼吸", "燃焼"]},
    {"question": "だ液には、食べ物の中の何を別のものに変えるはたらきがありますか？", "answer": "でんぷん", "distractors": ["たんぱく質", "脂肪", "ビタミン"]},
    {"question": "消化された養分の大部分は、どこから吸収されますか？", "answer": "小腸（しょうちょう）", "distractors": ["大腸", "胃", "食道"]},
    {"question": "昆虫のからだは、頭、胸、腹の3つの部分と、何本のあしでできていますか？", "answer": "6本", "distractors": ["4本", "8本", "2本"]},

    # --- 月と太陽・天気の変化 ---
    {"question": "太陽や月は、時刻とともにどの方角からどの方角へ動いて見えますか？", "answer": "東から南を通って西へ", "distractors": ["西から南を通って東へ", "南から北へ", "北から東を通って南へ"]},
    {"question": "太陽が真南にきたときのことを何といいますか？", "answer": "南中（なんちゅう）", "distractors": ["日の出", "日の入り", "夏至"]},
    {"question": "月の形は毎日変わります。右側が細く光る月を何といいますか？", "answer": "三日月", "distractors": ["満月", "半月", "新月"]},
    {"question": "気温をはかるとき、温度計は地面からどのくらいの高さにしますか？", "answer": "1.2〜1.5m", "distractors": ["0m", "5m", "10m"]},
    {"question": "気温を正しくはかるには、日光が「当たる」ところと「当たらない」ところのどちらではかりますか？", "answer": "当たらないところ", "distractors": ["当たるところ", "室内", "地下"]},
    {"question": "日本付近の天気は、およそどの方角からどの方角へ変化することが多いですか？", "answer": "西から東へ", "distractors": ["東から西へ", "南から北へ", "北から南へ"]},
    {"question": "雲の量が多いとき、天気はどうなりますか？", "answer": "くもり または 雨", "distractors": ["快晴", "晴れ", "雪"]},

    # --- 大地のつくりと変化 ---
    {"question": "川の流れの外側と内側では、どちらの流れが速いですか？", "answer": "外側", "distractors": ["内側", "どちらも同じ", "日によって違う"]},
    {"question": "川の流れで「川岸がけずられる」のは、カーブの外側と内側のどちらですか？", "answer": "外側", "distractors": ["内側", "底の方", "真ん中"]},
    {"question": "川の「丸くて小さい石」が多いのは、川の上流と下流のどちらですか？", "answer": "下流", "distractors": ["上流", "中流", "山の上"]},
    {"question": "流れる水が「土を運ぶはたらき」を何といいますか？", "answer": "運搬（うんぱん）", "distractors": ["浸食", "堆積", "蒸発"]},
    {"question": "れき（小石）・砂・どろのうち、最もはやく沈むものはどれですか？", "answer": "れき", "distractors": ["砂", "どろ", "すべて同じ"]},
    {"question": "地層の中に含まれる、大昔の生物の死がいやあとを何といいますか？", "answer": "化石", "distractors": ["断層", "火山灰", "宝石"]},
    {"question": "地震によって生じる、大地のズレを何といいますか？", "answer": "断層（だんそう）", "distractors": ["地割れ", "噴火口", "震源"]},
    {"question": "火山灰のつぶを顕微鏡でみると、砂のつぶに比べてどんな形をしていますか？", "answer": "角ばっている", "distractors": ["丸い", "平ら", "形がない"]},

    # --- 水のすがた・ものの燃え方 ---
    {"question": "水を熱して沸騰しているときに出てくる「あわ」の正体は何ですか？", "answer": "水蒸気", "distractors": ["空気", "酸素", "二酸化炭素"]},
    {"question": "水が沸騰している間、温度はどのように変化しますか？", "answer": "変わらない（約100℃のまま）", "distractors": ["上がり続ける", "下がり続ける", "上下する"]},
    {"question": "水蒸気が冷やされて、目に見える「湯気」になるのは、何体になったときですか？", "answer": "液体", "distractors": ["固体", "気体", "プラズマ"]},
    {"question": "空気をあたためると、体積はどうなりますか？", "answer": "大きくなる", "distractors": ["小さくなる", "変わらない", "なくなる"]},
    {"question": "ものが燃えるとき、空気中のどの気体が使われますか？", "answer": "酸素", "distractors": ["窒素", "二酸化炭素", "水素"]},
    {"question": "ものが燃えたあと、空気中の何の気体が増えますか？", "answer": "二酸化炭素", "distractors": ["酸素", "窒素", "ヘリウム"]},
    {"question": "二酸化炭素を通すと白くにごる液体は何ですか？", "answer": "石灰水", "distractors": ["ヨウ素液", "食塩水", "アンモニア水"]},
    {"question": "空気の成分のうち、最も割合が多い気体は何ですか？", "answer": "窒素（ちっ素）", "distractors": ["酸素", "二酸化炭素", "アルゴン"]},
    {"question": "ろうそくの火を消すには、空気（酸素）をどのようにすればよいですか？", "answer": "断ち切る（少なくする）", "distractors": ["増やす", "あたためる", "かきまぜる"]},

    # --- 水よう液の性質 ---
    {"question": "ものが水にとけて、全体が透明になった液体を何といいますか？", "answer": "水よう液", "distractors": ["どろ水", "混合物", "溶媒"]},
    {"question": "水の温度を上げると、とける量が非常に増えるのは、食塩とミョウバンのどちらですか？", "answer": "ミョウバン", "distractors": ["食塩", "どちらも同じ", "どちらも増えない"]},
    {"question": "とけているものを取り出すために、液体をこす道具を何といいますか？", "answer": "ろ紙", "distractors": ["リトマス紙", "pH試験紙", "折り紙"]},
    {"question": "青色のリトマス紙を赤色に変える水よう液は何性ですか？", "answer": "酸性", "distractors": ["アルカリ性", "中性", "油性"]},
    {"question": "赤色のリトマス紙を青色に変える水よう液は何性ですか？", "answer": "アルカリ性", "distractors": ["酸性", "中性", "水性"]},
    {"question": "リトマス紙の色をどちらも変えない水よう液は何性ですか？", "answer": "中性", "distractors": ["酸性", "アルカリ性", "両性"]},

    # --- てこと電気 ---
    {"question": "てこで、おもりに力がはたらく点を何といいますか？", "answer": "作用点", "distractors": ["支点", "力点", "終点"]},
    {"question": "重いものを小さな力で持ち上げるには、支点から「力点」までの距離をどうすればよいですか？", "answer": "長く（大きく）する", "distractors": ["短くする", "変えない", "支点に近づける"]},
    {"question": "乾電池2個を、電流が強くなるようにつなぐ方法を何といいますか？", "answer": "直列つなぎ", "distractors": ["並列つなぎ", "交差つなぎ", "交互つなぎ"]},
    {"question": "コイルに鉄心を入れ、電流を流したときだけ磁石になるものを何といいますか？", "answer": "電磁石", "distractors": ["永久磁石", "コンパス", "発電機"]}
]

# --- 以下、ゲームエンジン部分（前回の仕様を維持） ---
if 's_score' not in st.session_state:
    st.session_state.update({
        's_score': 0, 's_total_count': 0, 's_current_id': -1,
        's_remaining_ids': list(range(len(SCIENCE_QUIZ_DATA))),
        's_repeat_mode': False, 's_answered': False
    })

def generate_question():
    if st.session_state.s_repeat_mode:
        quiz_id = st.session_state.s_current_id
    else:
        if not st.session_state.s_remaining_ids:
            st.session_state.s_current_id = -99
            return
        quiz_id = random.choice(st.session_state.s_remaining_ids)
        st.session_state.s_current_id = quiz_id

    quiz_data = SCIENCE_QUIZ_DATA[quiz_id]
    options = list(quiz_data["distractors"]) + [quiz_data["answer"]]
    random.shuffle(options)
    st.session_state.update({
        's_question': quiz_data["question"], 's_answer': quiz_data["answer"],
        's_options': options, 's_answered': False, 's_is_correct': False
    })

if st.session_state.s_current_id == -1:
    generate_question()

st.title("🔬 理科：一問一答マスター")
st.caption(f"全{len(SCIENCE_QUIZ_DATA)}問：間違えたら正解するまで再挑戦！")

if st.session_state.s_current_id == -99:
    st.balloons()
    st.success("✨ 全問正解！おめでとうございます！")
    st.metric("最終スコア", f"{st.session_state.s_score} / {st.session_state.s_total_count}")
    if st.button("最初から解き直す"):
        st.session_state.update({'s_score': 0, 's_total_count': 0, 's_remaining_ids': list(range(len(SCIENCE_QUIZ_DATA))), 's_current_id': -1, 's_repeat_mode': False})
        st.rerun()
else:
    st.subheader(f"問題: {st.session_state.s_question}")
    if st.session_state.s_repeat_mode and not st.session_state.s_answered:
        st.warning("⚠️ 正解するまで次の問題へ進めません！")

    with st.form(key='sci_form'):
        user_choice = st.radio("答えを選択してください", st.session_state.s_options, index=None)
        if st.form_submit_button("回答する"):
            if user_choice:
                st.session_state.s_answered = True
                st.session_state.s_total_count += 1
                if user_choice == st.session_state.s_answer:
                    st.session_state.s_is_correct = True
                    if st.session_state.s_current_id in st.session_state.s_remaining_ids:
                        st.session_state.s_remaining_ids.remove(st.session_state.s_current_id)
                    st.session_state.s_repeat_mode = False
                else:
                    st.session_state.s_is_correct = False
                    st.session_state.s_repeat_mode = True
                st.rerun()
            else:
                st.warning("選択してください。")

    if st.session_state.s_answered:
        if st.session_state.s_is_correct:
            st.success(f"⭕ 正解！「{st.session_state.s_answer}」")
            if st.button("次の問題へ"):
                generate_question()
                st.rerun()
        else:
            st.error(f"❌ 残念！正解は「{st.session_state.s_answer}」でした。")
            if st.button("もう一度挑戦"):
                generate_question()
                st.rerun()

    st.divider()
    st.write(f"スコア: {st.session_state.s_score} / {st.session_state.s_total_count} (残り: {len(st.session_state.s_remaining_ids)}問)")