import random
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):
    if "旅" in user_message or "外出" in user_message or "お出かけ" in user_message or "おでかけ" in user_message or "トラベル" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp02.png"}
    if "かなしい" in user_message or "悲しい" in user_message:
        return "ハァ～？"
    if "けつ" in user_message or "ケツ" in user_message or "しり" in user_message :
        return {"type": "image", "content": "images/usagi/usagi_stamp03.png"}
    if "悪夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/usagi/nightmare.png"}

def reply(user_message):
    # patternsからランダムで返す
    patterns = [
        {"type": "text", "content": "フゥ～ン"},
        {"type": "text", "content": "イィィィヤァァアァッハー!!!"},        {"type": "text", "content": "ウ～ラ～ヤハヤハ"},
        {"type": "image", "content": "images/usagi/usagi_stamp02.png"},     
        {"type": "image", "content": "images/usagi/usagi_stamp06.png"},
        {"type": "image", "content": "images/usagi/usagi_stamp07.png"},

    ]
    return random.choice(patterns)
