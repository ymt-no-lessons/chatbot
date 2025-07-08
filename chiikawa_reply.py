import random 
import re

# 会話パターンごとに関数を定義するよ
def extract_head(user_message):
    if len(user_message) >= 2:
        return user_message[:2] + "…"
    return user_message[0] + "…"

def check_special_words(user_message):
    if "ねえ" in user_message:
        return {"type": "text", "content": "ン…"}
    if "いや" in user_message or "イヤ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_iya.png"}
    if "かなしい" in user_message or "悲しい" in user_message:
        return {"type": "text", "content": "ワァ…"}
    if "悪夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_nightmare.png"}
    if "がんばって" in user_message or "頑張って" in user_message or "がんばれ" in user_message or "頑張れ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp06.png"}
    if "えらい" in user_message or "えらいっ" in user_message or "えらいね" in user_message or "えらい！" in user_message or "えらいよ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp09.png"}
    if "黒い流れ星" in user_message or "ループ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_loop.png"}
    
    return None

def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "エッ…"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # 句読点や空白を除いた最後の1文字
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:
        return {"type": "text", "content": text + "…"}
    elif len(text) == 2:
        return {"type": "text", "content": text + "…"}
    
    # 通常パターン（ランダム返し）
    patterns = [
        {"type": "text", "content": "ワァ…"},
        {"type": "text", "content": extract_head(user_message)},  # ←ここ！
        {"type": "text", "content": user_message[:2] + "…"},
        {"type": "text", "content": user_message[-1] + "…"},
        {"type": "text", "content": user_message[-2:] + "…"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp01.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp02.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp03.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp04.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp05.png"}, 
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp07.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp08.png"}, 
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp09.png"},       
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp10.png"}
    ]
    return random.choice(patterns)
