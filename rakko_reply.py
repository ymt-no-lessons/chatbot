import random 
import re

# 会話パターンごとに関数を定義するよ
def extract_head(user_message):
    if len(user_message) >= 2:
        return user_message[:2] + "…"
    return user_message[0] + "…"

def check_special_words(user_message):
    if "ねえ" in user_message:
        return {"type": "text", "content": "どうした？"}

    if "かなしい" in user_message or "悲しい" in user_message:
        return {"type": "text", "content": "元気を出せッ"}

    if "すいか" in user_message:
        return {"type": "image", "content": "images/other/suikawari.png"}
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content": "images/other/water01.png"}
    # ヒットしなければNone
    return None


def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "リーチが長すぎるのかッ"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # 通常パターン（ランダム返し）
    patterns = [

        {"type": "image", "content": "images/rakko/rakko_stamp01.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp02.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp03.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp04.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp05.png"}, 
        {"type": "image", "content": "images/rakko/rakko_stamp07.png"},      

    ]
    return random.choice(patterns)
