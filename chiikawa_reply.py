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
    if "夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_nightmare.png"}
    if "がんばって" in user_message or "頑張って" in user_message or "がんば" in user_message or "頑張" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp06.png"}
    if "口" in user_message or "出して" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp08.png"}
    if "えらい" in user_message or "エライ" in user_message or "すごい" in user_message or "良いね" in user_message or "イイネ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp09.png"}
    if "黒" in user_message or "流れ星" in user_message or "ループ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_loop.png"}
    if "試験" in user_message or "テスト" in user_message or "しけん" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_test.png"}
    if "５" in user_message or "5" in user_message or "くさ" in user_message or "草" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_aun.png"}
    if "すいか" in user_message:
        return {"type": "image", "content": "images/other/suikawari.png"}
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content": "images/other/water01.png"}
    # ヒットしなければNone
    return None

    # ア、ウン画像で返答の特定ワードもこっちに書くやりかた
def reply_aun_stamp():
    stamp_images = [
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp_aun.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp_aun2.png"},
    ]
    return random.choice(stamp_images)


def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "エッ…"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # ア、ウン画像で返答の特定ワードもこっちに書くやりかたをこっちで返す
    if any(word in user_message for word in ["合格", "おめでとう", "受かった"]):
        return reply_aun_stamp()   # 引数いらない！
    
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
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp01.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp02.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp03.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp04.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp05.png"}, 
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp07.png"},      
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp10.png"},
    ]
    return random.choice(patterns)
