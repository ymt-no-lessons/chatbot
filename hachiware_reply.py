import random
import re

# 会話パターンごとに関数を定義するよ
def check_special_words(user_message):
    if "むり" in user_message or "悲しい" in user_message:
        return "なんとかなれーッ！"
    return None

def reply(user_message):
    # 特定ワード（むり、すごい）が入っていたら即返し！
    if "えらい" in user_message or "えらいっ" in user_message or "えらいね" in user_message or "えらい！" in user_message or "えらいよ" in user_message:
        return {"type": "image", "content": "images/hachiware/hachiware_stamp04.png"}

    # 句読点や空白を除いた最後の1文字で返したい特別パターン
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:  # たとえば1文字入力ならこれで返す、など
        return {"type": "text", "content": text[-1] + "…"}

    # 句読点や空白を除いた最後の2文字で返したい特別パターン
    text = re.sub(r'[\s。、！!？?]+$', '', user_message)
    if len(text) == 1:  # たとえば2文字入力ならこれで返す、など
        return {"type": "text", "content": text[-2] + "…"}
    
    # ここまで何もヒットしなかった場合、patternsからランダムで返す
    patterns = [
        {"type": "text", "content": "全然わかんないッ！"},
        {"type": "text", "content": user_message[:2] + "…"},
        {"type": "text", "content": user_message[-1] + "…"},   # 語尾1文字
        {"type": "text", "content": user_message[-2:] + "…"},  # 語尾2文字
        {"type": "image", "content": "images/hachiware/hachiware_stamp01.png"},
        {"type": "image", "content": "images/hachiware/hachiware_stamp02.png"},
        {"type": "image", "content": "images/hachiware/hachiware_stamp03.png"},
    ]
    return random.choice(patterns)
