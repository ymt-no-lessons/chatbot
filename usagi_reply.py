import random
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):

    if "いや" in user_message:
        return "イヤ…？"
    if "かなしい" in user_message or "悲しい" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp01.png"}
    if "旅" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp02.png"}
    if "usaketsu" in user_message or "うさけつ" in user_message or "ウサケツ" in user_message:
        return {"type": "image", "content": "images/usagi/usagi_stamp03.png"}
    if "悪夢" in user_message or "アクム" in user_message or "あくむ" in user_message:
        return {"type": "image", "content": "images/usagi/nightmare.png"}

def reply(user_message):
    # patternsからランダムで返す
    patterns = [
        {"type": "text", "content": "ワァ…"},
        {"type": "image", "content": "images/usagi/usagi_stamp06.png"},
        {"type": "image", "content": "images/usagi/usagi_stamp07.png"}      
    ]
    return random.choice(patterns)
