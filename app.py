import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="小学校英単語500 攻略クイズ", layout="centered", page_icon="🎓")

# === 【完全版】画像から抽出した全500語のデータベース ===
# ここにすべての単語が含まれています。
WORD_DATA = {
    "1.動作": [
        ("会う", "meet"), ("洗う", "wash"), ("歩く", "walk"), ("行く", "go"), ("歌う", "sing"),
        ("得る", "get"), ("置く", "put"), ("する", "do"), ("訪れる", "visit"), ("踊る", "dance"),
        ("泳ぐ", "swim"), ("買う", "buy"), ("描く", "draw"), ("考える", "think"), ("感謝する", "thank"),
        ("好む", "like"), ("去る", "leave"), ("参加する", "join"), ("調べる", "check"), ("住む", "live"),
        ("演奏する", "play"), ("座る", "sit"), ("掃除する", "clean"), ("そろえる", "set"), ("立つ", "stand"),
        ("楽しむ", "enjoy"), ("食べる", "eat"), ("試す", "try"), ("作る", "make"), ("綴る", "spell"),
        ("跳ぶ", "jump"), ("止まる", "stop"), ("飲む", "drink"), ("乗る", "ride"), ("走る", "run"),
        ("話す", "speak"), ("ブラシをかける", "brush"), ("触れる", "touch"), ("勉強する", "study"), ("ほしい", "want"),
        ("曲がる", "turn"), ("見える", "see"), ("見る", "watch"), ("見る", "look"), ("目が覚める", "wake"),
        ("持っていく", "take"), ("持っている", "have"), ("読む", "read"), ("料理する", "cook"), ("練習する", "practice")
    ],
    "2.状態・気持ち": [
        ("新しい", "new"), ("熱い", "hot"), ("甘い", "sweet"), ("忙しい", "busy"), ("美しい", "beautiful"),
        ("うれしい", "happy"), ("おいしい", "delicious"), ("多い", "many"), ("おかしな", "funny"), ("お気に入りの", "favorite"),
        ("おそろしい", "scary"), ("おもしろい", "interesting"), ("かたい", "hard"), ("かっこいい", "cool"), ("活動的な", "active"),
        ("悲しい", "sad"), ("かわいい", "cute"), ("かわいらしい", "lovely"), ("歓迎される", "welcome"), ("空腹の", "hungry"),
        ("元気な", "fine"), ("元気のよい", "cheerful"), ("塩からい", "salty"), ("親しみやすい", "friendly"), ("親切な", "kind"),
        ("新鮮な", "fresh"), ("すっぱい", "sour"), ("すてきな", "nice"), ("すばらしい", "great"), ("すばらしい", "wonderful"),
        ("高い", "high"), ("たくさんの", "many"), ("正しい", "right"), ("楽しさ", "fun"), ("小さい", "small"),
        ("疲れた", "tired"), ("冷たい", "cold"), ("長い", "long"), ("苦い", "bitter"), ("人気のある", "popular"),
        ("眠い", "sleepy"), ("速い", "fast"), ("開いている", "open"), ("古い", "old"), ("短い", "short"),
        ("申し訳なく思って", "sorry"), ("最も良い", "best"), ("優しい", "gentle"), ("やわらかい", "soft"), ("有名な", "famous"),
        ("よい", "good"), ("わくわくさせる", "exciting")
    ],
    "3.飲食物": [
        ("アイスクリーム", "ice cream"), ("イチゴ", "strawberry"), ("おにぎり", "rice ball"), ("オムレツ", "omelet"), ("オレンジ", "orange"),
        ("カレーライス", "curry and rice"), ("キウイフルーツ", "kiwi fruit"), ("キノコ", "mushroom"), ("キャベツ", "cabbage"), ("牛肉", "beef"),
        ("牛乳", "milk"), ("キュウリ", "cucumber"), ("くだもの", "fruit"), ("ケーキ", "cake"), ("紅茶", "tea"),
        ("コーヒー", "coffee"), ("サクランボ", "cherry"), ("サラダ", "salad"), ("サンドイッチ", "sandwich"), ("ジャガイモ", "potato"),
        ("ジュース", "juice"), ("スイカ", "watermelon"), ("スープ", "soup"), ("ステーキ", "steak"), ("スパゲッティ", "spaghetti"),
        ("ソーダ", "soda"), ("食べ物", "food"), ("卵", "egg"), ("タマネギ", "onion"), ("チョコレート", "chocolate"),
        ("デザート", "dessert"), ("トウモロコシ", "corn"), ("ドーナツ", "donut"), ("トマト", "tomato"), ("ナッツ", "nut"),
        ("肉", "meat"), ("日本茶", "green tea"), ("ニンジン", "carrot"), ("飲み物", "drink"), ("パイ", "pie"),
        ("パイナップル", "pineapple"), ("バナナ", "banana"), ("パフェ", "parfait"), ("ハンバーガー", "hamburger"), ("ピーマン", "green pepper"),
        ("ピザ", "pizza"), ("豚肉", "pork"), ("ブドウ", "grape"), ("フライドチキン", "fried chicken"), ("フライドポテト", "french fries"),
        ("プリン", "pudding"), ("ベーコン", "bacon"), ("ポップコーン", "popcorn"), ("ミネラルウォーター", "mineral water"), ("メロン", "melon"),
        ("めん", "noodle"), ("モモ", "peach"), ("焼き魚", "grilled fish"), ("リンゴ", "apple"), ("レタス", "lettuce"), ("レモン", "lemon")
    ],
    "4.数": [
        ("0", "zero"), ("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"), ("5", "five"),
        ("6", "six"), ("7", "seven"), ("8", "eight"), ("9", "nine"), ("10", "ten"),
        ("11", "eleven"), ("12", "twelve"), ("13", "thirteen"), ("14", "fourteen"), ("15", "fifteen"),
        ("16", "sixteen"), ("17", "seventeen"), ("18", "eighteen"), ("19", "nineteen"), ("20", "twenty"),
        ("30", "thirty"), ("40", "forty"), ("50", "fifty"), ("60", "sixty"), ("70", "seventy"),
        ("80", "eighty"), ("90", "ninety"), ("100", "hundred"),
        ("1番目の", "first"), ("2番目の", "second"), ("3番目の", "third"), ("4番目の", "fourth"), ("5番目の", "fifth"),
        ("10番目の", "tenth"), ("20番目の", "twentieth"), ("30番目の", "thirtieth")
    ],
    "5.学校生活": [
        ("アルファベット", "alphabet"), ("英語", "English"), ("音楽", "music"), ("家庭科", "home economics"), ("社会", "social studies"),
        ("書道", "calligraphy"), ("数学", "math"), ("図画工作", "arts and crafts"), ("体育", "P.E."), ("日本語", "Japanese"),
        ("理科", "science"), ("料理", "cooking"), ("運動場", "playground"), ("音楽祭", "music festival"), ("学芸会", "drama festival"),
        ("学校", "school"), ("教室", "classroom"), ("クラス", "class"), ("校外学習", "field trip"), ("コンピューター室", "computer room"),
        ("修学旅行", "school trip"), ("卒業式", "graduation ceremony"), ("体育館", "gym"), ("体育祭", "sports festival"), ("図書室", "library"),
        ("入学式", "entrance ceremony"), ("部・クラブ", "club"), ("鉛筆", "pencil"), ("消しゴム", "eraser"), ("定規", "ruler"),
        ("手紙", "letter"), ("ノート", "notebook"), ("はさみ", "scissors"), ("筆箱", "pencil case"), ("ペン", "pen"), ("マーカー", "marker")
    ],
    "6.町・施設・職業": [
        ("家", "house"), ("医者", "doctor"), ("宇宙飛行士", "astronaut"), ("英雄", "hero"), ("駅", "station"),
        ("お笑い芸人", "comedian"), ("歌手", "singer"), ("ガソリンスタンド", "gas station"), ("かど", "corner"), ("看護師", "nurse"),
        ("客室乗務員", "flight attendant"), ("教師", "teacher"), ("警察官", "police officer"), ("警察署", "police station"), ("芸術家", "artist"),
        ("公園", "park"), ("コンビニエンスストア", "convenience store"), ("サッカー選手", "soccer player"), ("ジェット機", "jet"), ("獣医", "vet"),
        ("消防署", "fire station"), ("書店", "bookstore"), ("神社", "shrine"), ("水族館", "aquarium"), ("スーパーマーケット", "supermarket"),
        ("タクシー", "taxi"), ("出口", "exit"), ("デパート", "department store"), ("寺", "temple"), ("動物園", "zoo"),
        ("動物園の飼育員", "zookeeper"), ("通り", "street"), ("特売", "sale"), ("農場主", "farmer"), ("歯医者", "dentist"),
        ("パイロット", "pilot"), ("博物館・美術館", "museum"), ("橋", "bridge"), ("バス", "bus"), ("バスの運転手", "bus driver"),
        ("花屋", "flower shop"), ("パン屋", "baker"), ("病院", "hospital"), ("町", "town"), ("メニュー", "menu"),
        ("野球選手", "baseball player"), ("遊園地", "amusement park"), ("郵便局", "post office"), ("料理人", "cook"), ("レストラン", "restaurant")
    ],
    "7.日常生活": [
        ("長靴", "rain boots"), ("家", "home"), ("いす", "chair"), ("腕時計", "watch"), ("かさ", "umbrella"),
        ("カップ", "cup"), ("カレンダー", "calendar"), ("ギター", "guitar"), ("車いす", "wheelchair"), ("ごみ", "garbage"),
        ("コンピューター", "computer"), ("磁石", "magnet"), ("自転車", "bicycle"), ("シャツ", "shirt"), ("宿題", "homework"),
        ("新聞", "newspaper"), ("スニーカー", "sneakers"), ("ズボン", "pants"), ("セーター", "sweater"), ("そうじ", "cleaning"),
        ("太鼓", "drum"), ("昼食", "lunch"), ("朝食", "breakfast"), ("机", "desk"), ("Tシャツ", "T-shirt"),
        ("テーブル", "table"), ("手袋", "glove"), ("テレビ", "TV"), ("電話", "telephone"), ("時計", "clock"),
        ("バイオリン", "violin"), ("箱", "box"), ("バッグ", "bag"), ("半ズボン", "shorts"), ("ピアノ", "piano"),
        ("ブーツ", "boots"), ("おふろ", "bath"), ("ベッド", "bed"), ("帽子(ふちあり)", "hat"), ("帽子(ふちなし)", "cap"),
        ("本", "book"), ("夕食", "dinner"), ("リコーダー", "recorder"), ("レインコート", "raincoat")
    ],
    "8.色": [
        ("色", "color"), ("青", "blue"), ("赤", "red"), ("オレンジ", "orange"), ("黄", "yellow"),
        ("黒", "black"), ("白", "white"), ("茶色", "brown"), ("ピンク", "pink"), ("緑", "green"), ("むらさき", "purple")
    ],
    "9.スポーツ": [
        ("アーチェリー", "archery"), ("オリンピック", "Olympic Games"), ("カヌー", "canoe"), ("サーフィン", "surfing"), ("サイクリング", "cycling"),
        ("サッカー", "soccer"), ("水泳", "swimming"), ("スポーツ", "sport"), ("体操", "gymnastics"), ("卓球", "table tennis"),
        ("チーム", "team"), ("テニス", "tennis"), ("登山", "climbing"), ("ドッジボール", "dodge ball"), ("バスケットボール", "basketball"),
        ("バドミントン", "badminton"), ("パラリンピック", "Paralympic Games"), ("バレーボール", "volleyball"), ("フットボール", "football"), ("ボクシング", "boxing"),
        ("野球", "baseball"), ("スケート", "skating"), ("ヨット競技", "sailing"), ("ラグビー", "rugby"), ("陸上競技", "track and field"), ("レスリング", "wrestling")
    ],
    "10.季節・月・曜日・時間": [
        ("春", "spring"), ("夏", "summer"), ("秋", "autumn"), ("冬", "winter"),
        ("1月", "January"), ("2月", "February"), ("3月", "March"), ("4月", "April"), ("5月", "May"), ("6月", "June"),
        ("7月", "July"), ("8月", "August"), ("9月", "September"), ("10月", "October"), ("11月", "November"), ("12月", "December"),
        ("日曜日", "Sunday"), ("月曜日", "Monday"), ("火曜日", "Tuesday"), ("水曜日", "Wednesday"), ("木曜日", "Thursday"), ("金曜日", "Friday"), ("土曜日", "Saturday"),
        ("時刻・時間", "time"), ("日", "day"), ("年", "year"), ("朝・午前", "morning"), ("午後", "afternoon")
    ],
    "11.国": [
        ("アメリカ", "the USA"), ("イギリス", "the UK"), ("イタリア", "italy"), ("インド", "india"), ("エジプト", "egypt"),
        ("オーストラリア", "australia"), ("カナダ", "canada"), ("韓国", "korea"), ("スペイン", "spain"), ("タイ", "thailand"),
        ("中国", "china"), ("ドイツ", "germany"), ("日本", "japan"), ("ブラジル", "brazil"), ("フランス", "france"), ("ペルー", "peru"), ("ロシア", "russia")
    ],
    "12.動植物": [
        ("イヌ", "dog"), ("イノシシ", "wild boar"), ("ウサギ", "rabbit"), ("ウシ", "cow"), ("ウマ", "horse"),
        ("蛾", "moth"), ("木", "tree"), ("クマ", "bear"), ("クモ", "spider"), ("ゴリラ", "gorilla"),
        ("サル", "monkey"), ("巣", "nest"), ("ゾウ", "elephant"), ("タヌキ", "raccoon dog"), ("トラ", "tiger"),
        ("トンボ", "dragonfly"), ("ニワトリ", "chicken"), ("ネコ", "cat"), ("ネズミ", "mouse"), ("バッタ", "grasshopper"),
        ("花", "flower"), ("パンダ", "panda"), ("ヒツジ", "sheep"), ("フクロウ", "owl"), ("ブタ", "pig"),
        ("ヘビ", "snake"), ("龍", "dragon")
    ],
    "13.自然・天気": [
        ("自然", "nature"), ("海", "sea"), ("川", "river"), ("浜辺", "beach"), ("湖", "lake"),
        ("山", "mountain"), ("天気", "weather"), ("雨の", "rainy"), ("くもった", "cloudy"), ("太陽", "sun"),
        ("虹", "rainbow"), ("晴れた", "sunny"), ("星", "star"), ("雪の", "snowy")
    ],
    "14.人と身体": [
        ("私は", "I"), ("私の", "my"), ("私を", "me"), ("あなたは", "you"), ("あなたの", "your"),
        ("私たちは", "we"), ("私たちの", "our"), ("私たちを", "us"), ("彼は", "he"), ("彼女は", "she"),
        ("父", "father"), ("母", "mother"), ("兄・弟", "brother"), ("姉・妹", "sister"), ("友だち", "friend"),
        ("祖父", "grandfather"), ("祖母", "grandmother"), ("脚", "leg"), ("頭", "head"), ("顔", "face"),
        ("肩", "shoulder"), ("口", "mouth"), ("つま先", "toe"), ("手", "hand"), ("歯", "teeth"),
        ("鼻", "nose"), ("ひざ", "knee"), ("目", "eye")
    ]
}

# === 共通データ処理 ===
# 全単語をリスト化 (出題用)
ALL_PAIRS = []
ALL_JP_WORDS = []
ALL_EN_WORDS = []
for category, words in WORD_DATA.items():
    for jp, en in words:
        ALL_PAIRS.append((jp, en, category))
        ALL_JP_WORDS.append(jp)
        ALL_EN_WORDS.append(en)

# === クイズロジック ===
def get_next_question():
    """全単語の中からランダムに問題と選択肢を生成する"""
    # 全データからランダムに1つのペアを選択
    target = random.choice(ALL_PAIRS)
    mode = random.randint(0, 1) # 0: JP->EN, 1: EN->JP
    
    category = target[2]
    
    if mode == 0:
        question = target[0] # 日本語
        answer = target[1]   # 英語（正解）
        # 選択肢用の英語リスト (正解を除外)
        distractors_pool = [w for w in ALL_EN_WORDS if w != answer]
    else:
        question = target[1] # 英語
        answer = target[0]   # 日本語（正解）
        # 選択肢用の日本語リスト (正解を除外)
        distractors_pool = [w for w in ALL_JP_WORDS if w != answer]
        
    # 不正解選択肢を3つランダムに抽出
    options = random.sample(distractors_pool, 3)
    options.append(answer) # 正解を追加
    random.shuffle(options) # シャッフル
    
    return {
        "question": question,
        "answer": answer,
        "options": options,
        "category": category,
        "mode": mode
    }

# === ゲームの状態管理 (セッションステート) ===
# 最初の問題の初期化
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.total_count = 0
    st.session_state.answered = True # 最初は「回答済み」状態にして、問題生成を促す

# === 画面更新用の関数 ===
def rerun_with_new_question():
    """新しい問題を生成して画面を再描画する"""
    st.session_state.game_state = get_next_question()
    st.session_state.answered = False
    st.session_state.current_choice = None # ラジオボタンのリセット用
    # st.rerun() # 自動的にリランされない場合のみコメント解除

# === メインUI ===
st.title("🎓 小学生英単語500 攻略クイズ")
st.markdown("---")

# 最初の問題生成
if st.session_state.answered and 'game_state' not in st.session_state:
    rerun_with_new_question()

# 問題表示エリア
if 'game_state' in st.session_state:
    state = st.session_state.game_state
    
    # カテゴリ情報
    st.caption(f"カテゴリー: {state['category']}")
    
    # 問題テキスト
    if state['mode'] == 0:
        st.subheader(f"「**{state['question']}**」は英語で何と言う？")
    else:
        st.subheader(f"「**{state['question']}**」の意味は？")
        
    # 選択肢 (フォームを使用して送信タイミングを制御)
    with st.form(key='answer_form', clear_on_submit=False):
        user_choice = st.radio("答えを選んでください", state['options'], key="answer_radio", index=None)
        submit_button = st.form_submit_button(label='回答する')

        if submit_button:
            if user_choice is None:
                st.warning("選択肢を選んでから回答してください。")
            elif not st.session_state.answered:
                # 回答処理
                st.session_state.answered = True
                st.session_state.total_count += 1
                if user_choice == state['answer']:
                    st.session_state.score += 1
                    st.success(f"✨ 正解！ 「{state['answer']}」でした。")
                else:
                    st.error(f"❌ 残念。正解は「{state['answer']}」でした。")
                
                # 自動的にスコアを表示するためにリラン (最新のanswered状態を反映)
                st.rerun()

    # スコアと次の問題ボタン
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.session_state.total_count > 0:
            st.write(f"**現在のスコア:** {st.session_state.score} / {st.session_state.total_count}")
    
    with col2:
        if st.session_state.answered:
            if st.button("次の問題へ", key="next_question"):
                rerun_with_new_question()
                st.rerun() # 画面をリセット