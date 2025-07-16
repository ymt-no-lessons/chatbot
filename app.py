from flask import Flask, render_template, request, redirect, url_for, session, send_file
from character_data import character_data
import random
from datetime import datetime
import os
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 1. 名前入力画面
@app.route('/', methods=['GET', 'POST'])
def index():
    # 履歴が残っていたら続きますか？画面へ
    if 'history' in session:
        return render_template('resume_confirm.html')
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['user_icon'] = request.form['icon']
        return redirect(url_for('select'))
    return render_template('index.html')

# 2. キャラ選択画面
@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        session['character'] = request.form['character']
        return redirect(url_for('confirm'))
    return render_template('select.html')

# 3. 確認画面
@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    username = session.get('username')
    character = session.get('character')
    data = character_data[character]
    if not (username and character):
        return redirect(url_for('index'))
    if request.method == 'POST':
        if request.form.get('action') == '決定':
            return redirect(url_for('chat'))
        elif request.form.get('action') == 'やり直す':
            return redirect(url_for('select'))
    return render_template('confirm.html', username=username, character=character, images=data['images'])

# キャラクターごとの会話を読み込むよ
from chiikawa_reply import reply as chiikawa_reply
from hachiware_reply import reply as hachiware_reply
from usagi_reply import reply as usagi_reply
from kurimanju_reply import reply as kurimanju_reply
from rakko_reply import reply as rakko_reply
from sisa_reply import reply as sisa_reply
from momonga_reply import reply as momonga_reply

# 会話画面
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    character = session.get('character')
    if not character:
        # キャラ未設定ならトップへリダイレクトでもいい
        return redirect(url_for('select'))
    data = character_data[character]

    # セッション初期化
    if 'history' not in session:
        session['history'] = [{
            'sender': 'character',
            'type': 'text',
            'content': data.get('greeting', 'こんにちは！')
        }]
        session['chat_over'] = False

    history = session['history']
    chat_over = session.get('chat_over', False)

    # ユーザーの発言回数
    user_turns = sum(1 for m in history if m['sender'] == 'user')

    if request.method == 'POST' and not chat_over:
        user_message = request.form['message']
        history.append({'sender': 'user', 'type': 'text', 'content': user_message})

        # キャラごとのreply
        if character == "ちいかわ":
            reply_data = chiikawa_reply(user_message)
        elif character == "ハチワレ":
            reply_data = hachiware_reply(user_message)
        elif character == "うさぎ":
            reply_data = usagi_reply(user_message)
        elif character == "くりまんじゅう":
            reply_data = kurimanju_reply(user_message)
        elif character == "ラッコ":
            reply_data = rakko_reply(user_message)
        elif character == "シーサー":
            reply_data = sisa_reply(user_message)
        elif character =="モモンガ":
            reply_data = momonga_reply(user_message)
        else:
            reply_data = {'type': 'text', 'content': "うまく返せない…"}

        if not isinstance(reply_data, dict):
            reply_data = {'type': 'text', 'content': reply_data}

        history.append({'sender': 'character', **reply_data})

        # 10回で終了
        user_turns = sum(1 for m in history if m['sender'] == 'user')
        if user_turns >= 10:
            # 終了メッセージ&画像（キャラ分岐サンプル）
            today = datetime.now().weekday()
            username = session.get('username', '')

            bye_message = data.get('bye_message', "今日はここまでだよ、バイバイ！")
            bye_image = data.get('bye_image', "images/chiikawa/chiikawa_stamp_bye.png")

            # サンプル：土曜・ユーザー名・通常
            if username == 'ゆみた' and 'bye_special' in data and 'ymt' in data['bye_special']:
                bye_message = data['bye_special']['ymt']['message']
                bye_image = data['bye_special']['ymt']['image']
            elif today == 6 and 'bye_special' in data and 'sunday' in data['bye_special']:
                bye_message = data['bye_special']['sunday']['message']
                bye_image = data['bye_special']['sunday']['image']
            elif today == 5 and 'bye_special' in data and 'saturday' in data['bye_special']:
                bye_message = data['bye_special']['saturday']['message']
                bye_image = data['bye_special']['saturday']['image']

            history.append({'sender': 'character', 'type': 'text', 'content': bye_message})
            history.append({'sender': 'character', 'type': 'image', 'content': bye_image})
            session['chat_over'] = True

        session['history'] = history
        return redirect(url_for('chat'))

    chat_over = session.get('chat_over', False)
    return render_template(
        'chat.html',
        history=history,
        character=data['label'],
        images=data['images'],
        chat_over=chat_over
    )


# 履歴ダウンロード
@app.route('/download_history', methods=['GET', 'POST'])
def download_history():
    history = session.get('history', [])
    if request.method == 'POST':
        # 履歴をテキスト化
        lines = []
        for msg in history:
            sender = "あなた" if msg['sender'] == "user" else "キャラ"
            content = msg.get('content') or msg.get('text')
            if msg.get('type') == 'image':
                line = f"{sender}: [スタンプ: {content}]"
            else:
                line = f"{sender}: {content}"
            lines.append(line)
        text_data = "\n".join(lines)
        file_data = io.BytesIO()
        file_data.write(text_data.encode('utf-8'))
        file_data.seek(0)
        session.clear()
        return send_file(
            file_data,
            mimetype='text/plain',
            as_attachment=True,
            download_name='chat_history.txt'
        )
    return render_template('download_done.html')

# リロード（完全リセット）
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect(url_for('index'))

# リロードするか確認画面
@app.route('/reset_confirm', methods=['GET', 'POST'])
def reset_confirm():
    if request.method == 'POST':
        print(request.form)  # ← 追加してみて！

        action = request.form['action']
        if action == 'はい':
            return redirect(url_for('download_history'))
        else:
            session.clear()
            return redirect(url_for('index'))
    return render_template('reset_confirm.html')

# 履歴が残っていた場合の確認
@app.route('/resume_confirm', methods=['POST'])
def resume_confirm():
    action = request.form['action']
    if action == 'はい':
        return redirect(url_for('chat'))
    else:
        session.clear()
        return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)