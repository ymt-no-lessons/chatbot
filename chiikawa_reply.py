import random
import re

# 会話パターンごとに関数を定義するよ
def extract_head(user_message):
    if len(user_message) >= 2:
        return user_message[:2] + "…"
    return user_message[0] + "…"

def check_special_words(user_message):
    if "ねえ" in user_message:
        return "ン…"
    if "いや" in user_message:
        return "イヤ…？"
    if "かなしい" in user_message or "悲しい" in user_message:
        return "ワァ…"
    if "悪夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_nightmare.png"}

def reply(user_message):
    # 特定ワード（むり、すごい）が入っていたら即返し！
    if "いや" in user_message or "イヤ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_iya.png"}

    if "えらい" in user_message or "えらいっ" in user_message or "えらいね" in user_message or "えらい！" in user_message or "えらいよ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp09.png"}
    
    if "がんばって" in user_message or "頑張って" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp06.png"}

    # 句読点や空白を除いた最後の1文字で返したい特別パターン
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:  # たとえば1文字入力ならこれで返す、など
        return {"type": "text", "content": text[-1] + "…"}

    # 句読点や空白を除いた最後の2文字で返したい特別パターン
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:  # たとえば2文字入力ならこれで返す、など
        return {"type": "text", "content": text[-2] + "…"}
    
    # ここまで何もヒットしなかった場合、patternsからランダムで返す
    patterns = [
        {"type": "text", "content": "ワァ…"},
        {"type": "text", "content": user_message[:2] + "…"},
        {"type": "text", "content": user_message[-1] + "…"},   # 語尾1文字
        {"type": "text", "content": user_message[-2:] + "…"},  # 語尾2文字
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp01.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp02.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp03.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp04.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp05.png"}      
    ]
    return random.choice(patterns)
