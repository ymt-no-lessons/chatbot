import random


# 会話パターンごとに関数を定義するよ
def extract_head(user_message):
    if len(user_message) >= 2:
        return user_message[:2] + "…"
    return user_message[0] + "…"

def check_special_words(user_message):
    if "むり" in user_message:
        return "ム…"
    if "いや" in user_message:
        return "イヤ…？"
    if "かなしい" in user_message or "悲しい" in user_message:
        return "ワァ…"
    return None



def reply(user_message):
    # 「むり」が入ってたら専用スタンプを返す
    if "むり" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp_muri.png"}

    # 「すごい」が入ってたら専用スタンプを返す
    if "すごい" in user_message or "スゴイ" in user_message:
        return {"type": "image", "content": "images/chiikawa/chiikawa_stamp03.png"}

    # それ以外は通常パターン（テキストor汎用画像）をランダムで返す
    import random
    patterns = [
        {"type": "text", "content": "ワァ…"},
        {"type": "text", "content": user_message[:2] + "…"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp01.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp02.png"},
        {"type": "image", "content": "images/chiikawa/chiikawa_stamp03.png"},
    ]
    return random.choice(patterns)
