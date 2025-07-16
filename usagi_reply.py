import random
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):
    if "旅" in user_message or "外出" in user_message or "お出かけ" in user_message or "おでかけ" in user_message or "トラベル" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp02.png"}
    if "かなしい" in user_message or "悲しい" in user_message:
        return "ハァ～？"
    if "けつ" in user_message or "ケツ" in user_message or "しり" in user_message or "尻" in user_message :
        return {"type": "image", "content": "images/usagi/usagi_stamp03.png"}
    if "夢" in user_message or "悪夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/usagi/nightmare.png"}
    if "天気" in user_message or "てんき" in user_message or "てるてる" in user_message or "坊主" in user_message or "ぼうず" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp08.png"}
    if "雨" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp_urayahabouzu.png"}
    if "すいか" in user_message:
        return {"type": "image", "content": "images/other/suikawari.png"}
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content": "images/other/water01.png"}
    # ヒットしなければNone
    return None

def reply(user_message):
    # まずspecialワードの判定をする！
    special = check_special_words(user_message)
    if special:
        return special

    # patternsからランダムで返す
    patterns = [
        {"type": "text", "content": "フゥ～ン"},
        {"type": "text", "content": "イィィィヤァァアァッハー!!!"},
        {"type": "text", "content": "ウ～ラ～ヤハヤハ"},
        {"type": "image", "content": "images/usagi/usagi_stamp03.png"}, 
        {"type": "image", "content": "images/usagi/usagi_stamp04.png"},
        {"type": "image", "content": "images/usagi/usagi_stamp05.png"},    
        {"type": "image", "content": "images/usagi/usagi_stamp06.png"},
        {"type": "image", "content": "images/usagi/usagi_stamp07.png"},

    ]
    return random.choice(patterns)
