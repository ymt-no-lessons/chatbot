import random
import re


import random
import re

def special_word(user_message):
    if "おやすみ" in user_message or "ねる" in user_message or "寝る" in user_message:
        return {"type": "image", "content": "images/hachiware/hachiware_stamp_sleep.png"}
    if "ありがとう" in user_message:
        return {"type": "text", "content": "どういたしましてッ！"}
    # …ここに増やしていく
    return None  # ヒットしなければNone


def reply(user_message):
    # 特別な言葉に対する返答
    result = special_word(user_message)
    if result:
        return result
    
    # 1. 【倒置法】に該当するかを判定
    m = re.match(r'(.+?)食べたい', user_message)
    if m:
        food = m.group(1).strip()
        return {"type": "text", "content": f"食べたいよね、{food}！"}
    m = re.match(r'(.+?)したい', user_message)
    if m:
        thing = m.group(1).strip()
        return {"type": "text", "content": f"したいよね、{thing}！"}
    m = re.match(r'(.+?)がない', user_message)
    if m:
        item = m.group(1).strip()
        return {"type": "text", "content": f"ないよ…{item}がッ！"}
    m = re.match(r'(.+?)したかった', user_message)
    if m:
        thing = m.group(1).strip()
        return {"type": "text", "content": f"したかったんだ…{thing}！"}
    m = re.match(r'(.+?)いたい', user_message)
    if m:
        body = m.group(1).strip()
        return {"type": "text", "content": f"いたいんだ、{body}ッ！"}

    # 2. 疑問文は「…ってコト？」で返す
    if user_message.endswith("？") or user_message.endswith("?"):
        base = user_message.rstrip("？?")
        return {"type": "text", "content": f"{base}…ってコト？"}

    # 3. たまに【スタンプ】で返す
    if random.random() < 0.2:  # 20%の確率でスタンプ返し
        stamp_images = [
            "images/hachiware/hachiware_stamp01.png",
            "images/hachiware/hachiware_stamp02.png",
            "images/hachiware/hachiware_stamp03.png",
        ]
        return {"type": "image", "content": random.choice(stamp_images)}

    # 4. それ以外は【あいづち】ランダム
    aizuchi = [
        "エヘヘ！",
        "エッ",
        "がんばってるね！",
        "なんとかなれーッ！",
        "うんうん…",
        "強くなりたいな…",
        "したいのッ？共有ッ！",
        "がんばって…",
        "images/hachiware/hachiware_stamp08.png",
        "images/hachiware/hachiware_stamp09.png"
    ]
    return {"type": "text", "content": random.choice(aizuchi)}
