import random 
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):
    if "神" in user_message or "福" in user_message or "信" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp07.png"}
    if "つまみ" in user_message or "肴" in user_message or "自由" in user_message or "市場" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp08.png"}
    if "酒" in user_message or "アルコール" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp09.png"}
    if "禁" in user_message or "免許" in user_message or "だめ" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp10.png"}    
    if "月" in user_message or "夜" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp11.png"}
    if "粉チーズ" in user_message or "しょうゆ" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp12.png"}
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content": "images/other/water01.png"}
    # ヒットしなければNone
    return None

def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "ハァーー…"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # 通常パターン（ランダム返し）
    patterns = [

        {"type": "image", "content": "images/kurimanju/kurimanju_stamp01.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp02.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp03.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp04.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp05.png"}, 
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp06.png"},      
    ]
    return random.choice(patterns)
