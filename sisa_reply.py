import random 
import re


def check_special_words(user_message):
    if "タッパー" in user_message or "おかず" in user_message:
        return {"type": "image", "content": "images/sisa/sisa_stamp06.png"}
    if "郎" in user_message or "ラーメン" in user_message:
        return {"type": "image", "content": "images/sisa/sisa_stamp07.png"}
    if "自由" in user_message or "明日" in user_message:
        return {"type": "image", "content": "images/sisa/sisa_stamp08.png"}

    # ヒットしなければNone
    return None



def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "元気ですかー"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # 句読点や空白を除いた最後の1文字
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 3:
        return {"type": "text", "content": text + "!"}
    elif len(text) == 4:
        return {"type": "text", "content": text + "!"}
    
    # 通常パターン（ランダム返し）
    patterns = [
        {"type": "text", "content": "うれシーサー"},
        {"type": "image", "content": "images/sisa/sisa_stamp01.png"},
        {"type": "image", "content": "images/sisa/sisa_stamp02.png"},
        {"type": "image", "content": "images/sisa/sisa_stamp03.png"},
        {"type": "image", "content": "images/sisa/sisa_stamp04.png"},
        {"type": "image", "content": "images/sisa/sisa_stamp05.png"}, 
    ]
    return random.choice(patterns)
