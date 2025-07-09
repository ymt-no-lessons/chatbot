import random 
import re

# 会話パターンごとに関数を定義するよ
def extract_head(user_message):
    if len(user_message) >= 2:
        return user_message[:2] + "…"
    return user_message[0] + "…"

def check_special_words(user_message):
    if "かなしい" in user_message or "悲しい" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp08.png"}
    if "がんばって" in user_message or "頑張って" in user_message or "がんばれ" in user_message or "頑張れ" in user_message:
        return {"type": "image", "content": "images/kurimanju/kurimanju_stamp06.png"}

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
    
    # 句読点や空白を除いた最後の1文字
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:
        return {"type": "text", "content": text + "…"}
    elif len(text) == 2:
        return {"type": "text", "content": text + "…"}
    
    # 通常パターン（ランダム返し）
    patterns = [
        {"type": "text", "content": "ハァー…"},
        {"type": "text", "content": extract_head(user_message)},  # ←ここ！
        {"type": "text", "content": user_message[:2] + "…"},
        {"type": "text", "content": user_message[-1] + "…"},
        {"type": "text", "content": user_message[-2:] + "…"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp01.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp02.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp03.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp04.png"},
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp05.png"}, 
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp07.png"},      
        {"type": "image", "content": "images/kurimanju/kurimanju_stamp10.png"},
    ]
    return random.choice(patterns)
