import random
import re

def check_special_words(user_message):
    if "ちょうだい" in user_message or "欲しい" in user_message or "ほしい" in user_message  or "返せ" in user_message or "返して" in user_message:
        return {"type": "image", "content": "images/momonga/momonga_stamp01.png"}
    if "うまみ" in user_message or "うま味" in user_message or "旨味" in user_message:
        return {"type": "image", "content": "images/momonga/momonga_stamp_umami.png"}    
    # …ここに増やしていく
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content": "images/momonga/momonga_stamp05.png"}
    if "風呂" in user_message or "洗う" in user_message or "臭い" in user_message:
        return {"type": "image", "content": "images/momonga/momonga_stamp07.png"}  
    if "歯" in user_message or "矯正" in user_message:
        return {"type": "image", "content": "images/momonga/momonga_stamp09.png"}  

    # ヒットしなければNone
    return None

def reply(user_message):
    # まずspecialワードの判定をする！
    special = check_special_words(user_message)
    if special:
        return special

    # たまに【スタンプ】で返す
    if random.random() < 0.4:  # 40%の確率でスタンプ返し
        stamp_images = [
            {"type": "image", "content": "images/momonga/momonga_stamp02.png"},
            {"type": "image", "content": "images/momonga/momonga_stamp03.png"},
            {"type": "image", "content": "images/momonga/momonga_stamp04.png"},
        ]
        return random.choice(stamp_images)

    # 4. それ以外は【あいづち】ランダム
    aizuchi = [
        "ホォ～ン！",
        "ほめろッ",
        {"type": "image", "content": "images/momonga/momonga_stamp06.png"},
        {"type": "image", "content": "images/momonga/momonga_stamp08.png"},
        {"type": "image", "content": "images/momonga/momonga_stamp10.png"},
    ]
    return random.choice(aizuchi)
