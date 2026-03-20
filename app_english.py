import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="小学校英語：高度学習モード", layout="centered", page_icon="🔤")

# === 【全100問】英語クイズ完全データベース ===
ENGLISH_QUIZ_DATA = [
    # --- あいさつ・日常の表現 ---
    {"question": "おはようございます", "answer": "Good morning.", "distractors": ["Good evening.", "Hello.", "Goodbye."]},
    {"question": "こんにちは", "answer": "Hello. / Hi.", "distractors": ["Good night.", "See you.", "Welcome."]},
    {"question": "こんばんは", "answer": "Good evening.", "distractors": ["Good morning.", "I’m sorry.", "Please."]},
    {"question": "さようなら", "answer": "Goodbye. / Bye.", "distractors": ["Nice to meet you.", "Hello.", "Welcome."]},
    {"question": "おやすみなさい", "answer": "Good night.", "distractors": ["Good evening.", "Goodbye.", "Thank you."]},
    {"question": "ありがとう", "answer": "Thank you.", "distractors": ["I’m sorry.", "You’re welcome.", "Please."]},
    {"question": "はじめまして", "answer": "Nice to meet you.", "distractors": ["How are you?", "Welcome.", "See you."]},
    {"question": "お元気ですか？", "answer": "How are you?", "distractors": ["What is this?", "What time is it?", "Who are you?"]},
    {"question": "元気です、ありがとう。", "answer": "I’m fine, thank you.", "distractors": ["You’re welcome.", "I’m sorry.", "Nice to meet you."]},
    {"question": "失礼します／すみません（呼びかけ）", "answer": "Excuse me.", "distractors": ["I’m sorry.", "Please.", "Thank you."]},
    {"question": "ごめんなさい", "answer": "I’m sorry.", "distractors": ["Excuse me.", "You’re welcome.", "Hello."]},
    {"question": "どういたしまして", "answer": "You’re welcome.", "distractors": ["Thank you.", "I’m fine.", "Please."]},
    {"question": "お願いします", "answer": "Please.", "distractors": ["Excuse me.", "Sorry.", "Welcome."]},
    {"question": "またね／ではまた", "answer": "See you.", "distractors": ["Nice to meet you.", "Hello.", "Good night."]},
    {"question": "ようこそ", "answer": "Welcome.", "distractors": ["Goodbye.", "Hi.", "See you."]},

    # --- 数・時間 ---
    {"question": "1", "answer": "one", "distractors": ["two", "ten", "on"]},
    {"question": "2", "answer": "two", "distractors": ["too", "ten", "three"]},
    {"question": "3", "answer": "three", "distractors": ["tree", "thirty", "thirteen"]},
    {"question": "4", "answer": "four", "distractors": ["for", "five", "forty"]},
    {"question": "5", "answer": "five", "distractors": ["fire", "four", "fifteen"]},
    {"question": "6", "answer": "six", "distractors": ["sex", "seven", "sixteen"]},
    {"question": "7", "answer": "seven", "distractors": ["seventeen", "six", "eleven"]},
    {"question": "8", "answer": "eight", "distractors": ["eighty", "eat", "eighteen"]},
    {"question": "9", "answer": "nine", "distractors": ["nice", "night", "nineteen"]},
    {"question": "10", "answer": "ten", "distractors": ["tenn", "two", "twelve"]},
    {"question": "11", "answer": "eleven", "distractors": ["seven", "twelve", "eleventy"]},
    {"question": "12", "answer": "twelve", "distractors": ["twenty", "eleven", "two"]},
    {"question": "13", "answer": "thirteen", "distractors": ["thirty", "three", "third"]},
    {"question": "15", "answer": "fifteen", "distractors": ["fifty", "five", "fifth"]},
    {"question": "20", "answer": "twenty", "distractors": ["twelve", "two", "thirty"]},
    {"question": "何時ですか？", "answer": "What time is it?", "distractors": ["What is this?", "How are you?", "What o'clock?"]},
    {"question": "時刻（～時）", "answer": "o'clock", "distractors": ["clock", "time", "hour"]},

    # --- 曜日・月・季節 ---
    {"question": "日曜日", "answer": "Sunday", "distractors": ["Monday", "Saturday", "Sun"]},
    {"question": "月曜日", "answer": "Monday", "distractors": ["Sunday", "Tuesday", "Month"]},
    {"question": "火曜日", "answer": "Tuesday", "distractors": ["Thursday", "Wednesday", "Tuesday."]},
    {"question": "水曜日", "answer": "Wednesday", "distractors": ["Thursday", "Tuesday", "Friday"]},
    {"question": "木曜日", "answer": "Thursday", "distractors": ["Tuesday", "Tuesday", "Friday"]},
    {"question": "金曜日", "answer": "Friday", "distractors": ["Saturday", "Thursday", "Monday"]},
    {"question": "土曜日", "answer": "Saturday", "distractors": ["Sunday", "Friday", "Saturday."]},
    {"question": "1月", "answer": "January", "distractors": ["February", "June", "July"]},
    {"question": "2月", "answer": "February", "distractors": ["January", "March", "Friday"]},
    {"question": "3月", "answer": "March", "distractors": ["May", "April", "March."]},
    {"question": "4月", "answer": "April", "distractors": ["August", "Apple", "Autumn"]},
    {"question": "5月", "answer": "May", "distractors": ["March", "June", "Monday"]},
    {"question": "6月", "answer": "June", "distractors": ["July", "January", "June."]},
    {"question": "7月", "answer": "July", "distractors": ["June", "January", "July."]},
    {"question": "8月", "answer": "August", "distractors": ["Autumn", "April", "August."]},
    {"question": "9月", "answer": "September", "distractors": ["October", "November", "Sunday"]},
    {"question": "10月", "answer": "October", "distractors": ["October.", "September", "December"]},
    {"question": "11月", "answer": "November", "distractors": ["December", "November.", "October"]},
    {"question": "12月", "answer": "December", "distractors": ["December.", "November", "January"]},
    {"question": "春", "answer": "spring", "distractors": ["summer", "fall", "winter"]},
    {"question": "夏", "answer": "summer", "distractors": ["spring", "winter", "sunny"]},
    {"question": "秋", "answer": "fall / autumn", "distractors": ["spring", "winter", "apple"]},
    {"question": "冬", "answer": "winter", "distractors": ["water", "summer", "spring"]},

    # --- 学校・文房具・教科 ---
    {"question": "学校", "answer": "school", "distractors": ["station", "hospital", "park"]},
    {"question": "ペン", "answer": "pen", "distractors": ["pencil", "pan", "pin"]},
    {"question": "鉛筆", "answer": "pencil", "distractors": ["pen", "eraser", "notebook"]},
    {"question": "消しゴム", "answer": "eraser", "distractors": ["ruler", "brush", "pencil"]},
    {"question": "ノート", "answer": "notebook", "distractors": ["book", "note", "paper"]},
    {"question": "本", "answer": "book", "distractors": ["notebook", "bag", "look"]},
    {"question": "定規（ものさし）", "answer": "ruler", "distractors": ["eraser", "ruler.", "roller"]},
    {"question": "かばん", "answer": "bag", "distractors": ["bug", "box", "chair"]},
    {"question": "机", "answer": "desk", "distractors": ["chair", "table", "disk"]},
    {"question": "いす", "answer": "chair", "distractors": ["desk", "table", "hair"]},
    {"question": "国語", "answer": "Japanese", "distractors": ["English", "Japan", "Social studies"]},
    {"question": "算数／数学", "answer": "math", "distractors": ["science", "music", "maths"]},
    {"question": "理科", "answer": "science", "distractors": ["math", "art", "social studies"]},
    {"question": "社会", "answer": "social studies", "distractors": ["science", "history", "geography"]},
    {"question": "音楽", "answer": "music", "distractors": ["math", "art", "English"]},
    {"question": "体育", "answer": "P.E.", "distractors": ["Art", "Science", "P.E"]},
    {"question": "英語", "answer": "English", "distractors": ["Japanese", "England", "Music"]},
    {"question": "図工／美術", "answer": "art", "distractors": ["music", "math", "P.E."]},

    # --- 食べ物・動物・スポーツ ---
    {"question": "りんご", "answer": "apple", "distractors": ["orange", "banana", "April"]},
    {"question": "オレンジ", "answer": "orange", "distractors": ["apple", "lemon", "orange."]},
    {"question": "バナナ", "answer": "banana", "distractors": ["banana.", "apple", "orange"]},
    {"question": "牛乳", "answer": "milk", "distractors": ["water", "juice", "egg"]},
    {"question": "卵", "answer": "egg", "distractors": ["egg.", "milk", "bread"]},
    {"question": "水", "answer": "water", "distractors": ["milk", "waiter", "winter"]},
    {"question": "パン", "answer": "bread", "distractors": ["pan", "bread.", "egg"]},
    {"question": "犬", "answer": "dog", "distractors": ["cat", "bird", "rabbit"]},
    {"question": "猫", "answer": "cat", "distractors": ["dog", "rat", "cap"]},
    {"question": "鳥", "answer": "bird", "distractors": ["bad", "bed", "panda"]},
    {"question": "ウサギ", "answer": "rabbit", "distractors": ["rabbit.", "panda", "lion"]},
    {"question": "パンダ", "answer": "panda", "distractors": ["rabbit", "lion", "panda."]},
    {"question": "ライオン", "answer": "lion", "distractors": ["lion.", "tiger", "bear"]},
    {"question": "野球", "answer": "baseball", "distractors": ["soccer", "tennis", "basket"]},
    {"question": "サッカー", "answer": "soccer", "distractors": ["baseball", "soccer.", "tennis"]},
    {"question": "テニス", "answer": "tennis", "distractors": ["tennis.", "soccer", "table tennis"]},
    {"question": "バスケットボール", "answer": "basketball", "distractors": ["baseball", "soccer", "volleyball"]},

    # --- 基本の文とルール ---
    {"question": "私は～です（I のあとの単語）", "answer": "am", "distractors": ["are", "is", "be"]},
    {"question": "あなたは～です（You のあとの単語）", "answer": "are", "distractors": ["am", "is", "be"]},
    {"question": "私は～が好きです（文）", "answer": "I like ...", "distractors": ["I have ...", "I play ...", "I am ..."]},
    {"question": "私は～を飼っています／持っています（文）", "answer": "I have ...", "distractors": ["I like ...", "I play ...", "I am ..."]},
    {"question": "私は～を弾きます／します（文）", "answer": "I play ...", "distractors": ["I have ...", "I like ...", "I go ..."]},
    {"question": "これは何ですか？", "answer": "What is this?", "distractors": ["What is your name?", "What time is it?", "Who is this?"]},
    {"question": "あなたの名前は何ですか？", "answer": "What is your name?", "distractors": ["What is this?", "How are you?", "Who are you?"]},
    {"question": "文の最後にうつ「.」の名前", "answer": "ピリオド (period)", "distractors": ["クエスチョンマーク", "カンマ", "ビックリマーク"]},
    {"question": "疑問文の最後にうつ「?」の名前", "answer": "クエスチョンマーク (question mark)", "distractors": ["ピリオド", "カンマ", "ビックリマーク"]},
    {"question": "「～へ行きましょう」と誘う時の言葉", "answer": "Let's (go to ...)", "distractors": ["Please", "Hello", "Welcome"]}
]

# --- 状態管理の初期化 ---
if 'eng_remaining_ids' not in st.session_state:
    st.session_state.update({
        'eng_remaining_ids': list(range(len(ENGLISH_QUIZ_DATA))),
        'eng_wrong_pool': [],      # 復習用プール
        'eng_step_counter': 0,     
        'eng_next_interval': random.randint(3, 5),
        'eng_current_id': -1,
        'eng_answered': False
    })

def generate_next_question():
    """高度な出題アルゴリズム（割り込み復習型）"""
    st.session_state.eng_step_counter += 1
    
    # 復習を出すタイミングかどうか判定
    is_review_time = (st.session_state.eng_wrong_pool and 
                      st.session_state.eng_step_counter >= st.session_state.eng_next_interval)

    if is_review_time:
        quiz_id = random.choice(st.session_state.eng_wrong_pool)
        # 次の復習までの距離を設定
        st.session_state.eng_next_interval = st.session_state.eng_step_counter + random.randint(3, 5)
    elif st.session_state.eng_remaining_ids:
        quiz_id = random.choice(st.session_state.eng_remaining_ids)
    elif st.session_state.eng_wrong_pool:
        quiz_id = random.choice(st.session_state.eng_wrong_pool)
    else:
        st.session_state.eng_current_id = -99
        return

    quiz_data = ENGLISH_QUIZ_DATA[quiz_id]
    options = list(quiz_data["distractors"]) + [quiz_data["answer"]]
    random.shuffle(options)
    
    st.session_state.update({
        'eng_current_id': quiz_id,
        'eng_q_txt': quiz_data["question"],
        'eng_q_ans': quiz_data["answer"],
        'eng_q_opts': options,
        'eng_answered': False
    })

# 初回起動
if st.session_state.eng_current_id == -1:
    generate_next_question()

st.title("🔤 英語：高度学習モード")
st.caption("目の前の一問に集中！間違えた問題は忘れた頃に再登場します。")

if st.session_state.eng_current_id == -99:
    st.balloons()
    st.success("✨ Excellent! すべての英語課題をクリアしました！")
    if st.button("Try again (最初から挑戦)"):
        for key in list(st.session_state.keys()):
            if key.startswith('eng_'): del st.session_state[key]
        st.rerun()
else:
    st.subheader(f"問題: {st.session_state.eng_q_txt}")
    
    with st.form(key='eng_answer_form'):
        user_choice = st.radio("正しい英語を選んでください", st.session_state.eng_q_opts, index=None)
        submitted = st.form_submit_button("回答する (Answer)")

        if submitted:
            if user_choice:
                st.session_state.eng_answered = True
                
                if user_choice == st.session_state.eng_q_ans:
                    st.success(f"⭕ Correct! 「{st.session_state.eng_q_ans}」")
                    # 正解したら各リストから完全に削除
                    if st.session_state.eng_current_id in st.session_state.eng_remaining_ids:
                        st.session_state.eng_remaining_ids.remove(st.session_state.eng_current_id)
                    if st.session_state.eng_current_id in st.session_state.eng_wrong_pool:
                        st.session_state.eng_wrong_pool.remove(st.session_state.eng_current_id)
                else:
                    st.error(f"❌ Oops! 正解は「{st.session_state.eng_q_ans}」でした。")
                    # 間違えたら復習プールに追加
                    if st.session_state.eng_current_id not in st.session_state.eng_wrong_pool:
                        st.session_state.eng_wrong_pool.append(st.session_state.eng_current_id)
                st.rerun()
            else:
                st.warning("選択してください。")

    if st.session_state.eng_answered:
        if st.button("Next question (次の問題へ)"):
            generate_next_question()
            st.rerun()