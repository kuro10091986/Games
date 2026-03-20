import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="小学校理科クイズ", layout="centered", page_icon="🔬")

# === 【完全版】理科クイズデータベース ===
# ご提示いただいた問題に基づき、正解と不正解選択肢を作成しました。
SCIENCE_QUIZ_DATA = [
    {
        "question": "発芽前の種子を横に切って切り口にヨウ素液をつけると何色になりますか？",
        "answer": "青紫色",
        "distractors": ["赤色", "無色", "黄色"]
    },
    {
        "question": "ヨウ素液は、デンプンがあると何色に変化しますか？",
        "answer": "青紫色",
        "distractors": ["赤色", "緑色", "黒色"]
    },
    {
        "question": "発芽後、しばらくしてしおれてきた子葉を横に切って切り口にヨウ素液をつけると色は変化しますか？",
        "answer": "変化しない",
        "distractors": ["青紫色になる", "赤色になる", "緑色になる"]
    },
    {
        "question": "植物が根から取り入れた水は主に葉から何になって空気中へ出て行きますか？",
        "answer": "水蒸気",
        "distractors": ["酸素", "二酸化炭素", "液体の水"]
    },
    {
        "question": "水分が葉から空気中へ出ていくことを何と言いますか？",
        "answer": "蒸散（じょうさん）",
        "distractors": ["光合成", "呼吸", "気化"]
    },
    {
        "question": "葉にデンプンができているかどうかを調べる薬品はなんですか？",
        "answer": "ヨウ素液",
        "distractors": ["石灰水", "BTB溶液", "リトマス紙"]
    },
    {
        "question": "私たちが吸い込んだ空気は何と言う体の部分に入りますか？",
        "answer": "肺（はい）",
        "distractors": ["胃（い）", "心臓（しんぞう）", "肝臓（かんぞう）"]
    },
    {
        "question": "石灰水を入れた袋に息を吹き込むと色はどうなりますか？",
        "answer": "白く濁る（にごる）",
        "distractors": ["赤くなる", "青くなる", "変化しない"]
    },
    {
        "question": "石灰水は何で白く濁りますか？",
        "answer": "二酸化炭素",
        "distractors": ["酸素", "窒素", "水素"]
    },
    {
        "question": "昆虫の体は、頭と腹と何の3つに分かれていますか？",
        "answer": "胸（むね）",
        "distractors": ["足（あし）", "羽（はね）", "背（せ）"]
    },
    {
        "question": "血液中の余分な水や不要なものを尿にする、体の部分はなんと言いますか？",
        "answer": "腎臓（じんぞう）",
        "distractors": ["肝臓（かんぞう）", "心臓（しんぞう）", "肺（はい）"]
    },
    {
        "question": "試験管の中にデンプンの液を入れ、さらに唾液（だえき）を入れました。10分後にヨウ素液を入れるとどうなりますか？",
        "answer": "変化しない（青紫色にならない）",
        "distractors": ["青紫色になる", "赤くなる", "緑色になる"]
    },
    {
        "question": "太陽はどこの空からどこの空へ動きますか？",
        "answer": "東の空から西の空へ",
        "distractors": ["西の空から東の空へ", "南の空から北の空へ", "北の空から南の空へ"]
    },
    {
        "question": "日本の天気はどこからどこへ変化しますか？",
        "answer": "西から東へ",
        "distractors": ["東から西へ", "南から北へ", "北から南へ"]
    },
    {
        "question": "星の明るさはどれも同じですか？違いますか？",
        "answer": "違う（等級がある）",
        "distractors": ["どれも同じ", "星座によって同じ", "季節によって同じ"]
    },
    {
        "question": "星座は時間とともに見える位置（くらい）は変わりますか？",
        "answer": "変わる",
        "distractors": ["変わらない", "季節によって変わらない", "場所によって変わらない"]
    },
    {
        "question": "星座は時間とともに並び方が変わりますか？",
        "answer": "変わらない",
        "distractors": ["変わる", "時間によって変わる", "場所によって変わる"]
    },
    {
        "question": "川の水量が増えると、川底の土はどうなりますか？",
        "answer": "流される（浸食・運搬される）",
        "distractors": ["積もる", "固まる", "変化しない"]
    },
    {
        "question": "丸くて小さい石が多いのは、川の上流・下流どちらですか？",
        "answer": "下流",
        "distractors": ["上流", "中流", "どちらも同じ"]
    },
    {
        "question": "川の流れは内側と外側のどちらが早いですか？",
        "answer": "外側",
        "distractors": ["内側", "どちらも同じ", "日によって違う"]
    },
    {
        "question": "火山灰の粒（つぶ）はどんな形をしていますか？",
        "answer": "角ばっている（ギザギザしている）",
        "distractors": ["丸い", "平ら", "形はない"]
    },
    {
        "question": "地震によって生じる大地のズレのことを何と言いますか？",
        "answer": "断層（だんそう）",
        "distractors": ["地割れ", "震源", "火山"]
    },
    {
        "question": "沸騰（ふっとう）しているときに、水の中から出てくる泡（あわ）の正体はなんですか？",
        "answer": "水蒸気",
        "distractors": ["空気", "酸素", "二酸化炭素"]
    },
    {
        "question": "空気の中で1番多い（体積比）のはなんですか？",
        "answer": "窒素（ちっそ）",
        "distractors": ["酸素", "二酸化炭素", "アルゴン"]
    },
    {
        "question": "水の温度を上げると、溶ける量が増えるのはミョウバン・食塩のどちらですか？",
        "answer": "ミョウバン",
        "distractors": ["食塩", "どちらも同じ", "どちらも増えない"]
    },
    {
        "question": "ものが一定の量の水に溶ける量には限りがあります。その量はものによって変わりますか、変わりませんか？",
        "answer": "変わる",
        "distractors": ["変わらない", "温度によって変わらない", "水の量によって変わらない"]
    },
    {
        "question": "赤いリトマス紙を青色にする水溶液の性質を何と言いますか？",
        "answer": "アルカリ性",
        "distractors": ["酸性", "中性", "どちらでもない"]
    },
    {
        "question": "リトマス紙の色が変化しない場合、水溶液は何性ですか？",
        "answer": "中性",
        "distractors": ["酸性", "アルカリ性", "酸性とアルカリ性の混合"]
    }
]

# === ゲームの状態管理 (セッションステート) ===
# 初回起動時のみ実行
if 's_score' not in st.session_state:
    st.session_state.s_score = 0
    st.session_state.s_total_count = 0
    # 未回答の問題リストをIDで管理
    st.session_state.s_remaining_ids = list(range(len(SCIENCE_QUIZ_DATA)))
    # 現在の問題ID（-1は問題がない状態）
    st.session_state.s_current_id = -1
    # 間違えた問題フラグ
    st.session_state.s_repeat_mode = False

# === 問題生成・更新関数 ===
def generate_question():
    """新しい問題、または同じ問題を再生成する。選択肢はシャッフルする。"""
    
    # どの問題を出すか決定
    if st.session_state.s_repeat_mode:
        # 間違えたので同じ問題IDを維持
        quiz_id = st.session_state.s_current_id
    else:
        # 正解したので、残りの問題から新しいIDをランダムに選ぶ
        if not st.session_state.s_remaining_ids:
            # 全問正解した
            st.session_state.s_current_id = -99
            st.session_state.s_options = []
            return
        quiz_id = random.choice(st.session_state.s_remaining_ids)
        st.session_state.s_current_id = quiz_id

    # 問題データの取得
    quiz_data = SCIENCE_QUIZ_DATA[quiz_id]
    
    # 選択肢の作成とシャッフル
    options = list(quiz_data["distractors"])
    options.append(quiz_data["answer"])
    random.shuffle(options)
    
    # セッション状態への保存
    st.session_state.s_question = quiz_data["question"]
    st.session_state.s_answer = quiz_data["answer"]
    st.session_state.s_options = options
    # 回答状態のリセット
    st.session_state.s_answered = False
    st.session_state.s_is_correct = False

# === メインUI ===
st.title("🔬 小学校理科クイズ")
st.markdown("間違えたら、正解するまで同じ問題を繰り返します。頑張りましょう！")
st.markdown("---")

# 最初の問題生成
if st.session_state.s_current_id == -1:
    generate_question()

# クイズ表示エリア
if st.session_state.s_current_id == -99:
    # 全問正解画面
    st.balloons()
    st.success("✨ おめでとうございます！ 全問正解です！")
    st.metric("最終スコア", f"{st.session_state.s_score} / {st.session_state.s_total_count}")
    
    if st.button("もう一度挑戦する", key="restart_science"):
        st.session_state.s_score = 0
        st.session_state.s_total_count = 0
        st.session_state.s_remaining_ids = list(range(len(SCIENCE_QUIZ_DATA)))
        st.session_state.s_current_id = -1
        st.session_state.s_repeat_mode = False
        st.rerun()

else:
    # 通常のクイズ画面
    # 問題テキスト
    st.subheader(f"問題: {st.session_state.s_question}")
    
    # 繰り返しモードの表示
    if st.session_state.s_repeat_mode and not st.session_state.s_answered:
        st.warning("⚠️ もう一度挑戦です！")

    # 選択肢 (フォームを使用して送信タイミングを制御)
    with st.form(key='science_answer_form', clear_on_submit=False):
        # index=Noneにして最初は何も選択されていない状態にする
        user_choice = st.radio("答えを選んでください", st.session_state.s_options, key="science_answer_radio", index=None)
        submit_button = st.form_submit_button(label='回答する')

        if submit_button:
            if user_choice is None:
                st.warning("選択肢を選んでから回答してください。")
            elif not st.session_state.s_answered:
                # 回答処理
                st.session_state.s_answered = True
                st.session_state.s_total_count += 1
                
                if user_choice == st.session_state.s_answer:
                    # 正解
                    st.session_state.s_is_correct = True
                    st.session_state.s_score += 1
                    
                    # この問題を「未回答問題リスト」から削除
                    if st.session_state.s_current_id in st.session_state.s_remaining_ids:
                        st.session_state.s_remaining_ids.remove(st.session_state.s_current_id)
                    
                    # 繰り返しモードを解除
                    st.session_state.s_repeat_mode = False
                else:
                    # 不正解
                    st.session_state.s_is_correct = False
                    # 次回同じ問題を繰り返す
                    st.session_state.s_repeat_mode = True
                
                # スコアを最新に反映するためにリラン
                st.rerun()

    # 回答後のフィードバックと「次の問題」ボタン
    if st.session_state.s_answered:
        if st.session_state.s_is_correct:
            st.success(f"✨ 正解！ 「{st.session_state.s_answer}」でした。")
            if st.button("次の問題へ", key="next_science"):
                generate_question()
                st.rerun()
        else:
            st.error(f"❌ 残念。正解は「{st.session_state.s_answer}」でした。")
            if st.button("もう一度同じ問題に挑戦", key="retry_science"):
                # 同じ問題IDで、選択肢を再シャッフルして生成
                generate_question()
                st.rerun()

    # スコア表示
    st.divider()
    st.write(f"**現在のスコア:** {st.session_state.s_score} / {st.session_state.s_total_count}")
    st.caption(f"全{len(SCIENCE_QUIZ_DATA)}問中、残り {len(st.session_state.s_remaining_ids)} 問です。")