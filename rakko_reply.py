import random
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):
    if "ねえ" in user_message:
        return {"type": "text", "content": "どうした？"}
    if "かなしい" in user_message or "悲しい" in user_message or "つらい" in user_message:
        return {"type": "text", "content": "元気を出せッ"}
    if "スイーツ" in user_message or "菓子" in user_message or "おやつ" in user_message or "甘" in user_message:
        return {"type": "image", "content": "images/rakko/rakko_stamp10.png"}    
    if "すいか" in user_message:
        return {"type": "image", "content": "images/other/suikawari.png"}
    if "水" in user_message or "暑" in user_message or "熱中症" in user_message:
        return {"type": "image", "content":}
    if "特訓" in user_message or "討伐" in user_message or "ランカー" "images/other/water01.png"  or "戦" in user_message in user_message:
        return {"type": "text", "content": "強くなりたいと思ったんだ"}
    if "記念" in user_message or "公園" in user_message or "きねん"  or "こうえん" in user_message in user_message:
        return {"type": "image", "content": "images/rakko/rakko_stamp11.png"}
    if "懐か" in user_message or "なつかし" in user_message:
        return {"type": "image", "content": "images/rakko/rakko_stamp12.png"}
    if "昔" in user_message  or "むかし" in user_message or "思い出"  or "過去" in user_message in user_message:
        return {"type": "image", "content": "images/rakko/rakko_stamp12.png"}
    # ヒットしなければNone
    return None

def reply(user_message):
    # 空メッセージ対策
    if not user_message:
        return {"type": "text", "content": "驕っていたのかもしれないッ"}
    
    # specialワードで返答
    special = check_special_words(user_message)
    if special:
        return special
    
    # 通常パターン（ランダム返し）
    if random.random() < 0.4:  # 40%の確率でスタンプ返し
        stamp_images = [
        {"type": "image", "content": "images/rakko/rakko_stamp01.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp02.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp03.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp04.png"},
        {"type": "image", "content": "images/rakko/rakko_stamp05.png"}, 
        {"type": "image", "content": "images/rakko/rakko_stamp07.png"},      
    ]
    return random.choice(patterns)
