from flask import Flask, render_template, request, redirect, url_for, session 
from character_data import character_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 任意の文字列でOK

# 名前入力 or 前回履歴の確認
@app.route('/', methods=['GET', 'POST'])
def index():
    # 履歴が残っていたら「続きますか？」画面へ
    if 'history' in session:
        return render_template('resume_confirm.html')
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['user_icon'] = request.form['icon']
        return redirect(url_for('select'))
    return render_template('index.html')

@app.route('/resume_confirm', methods=['POST'])
def resume_confirm():
    action = request.form['action']
    if action == 'はい':
        return redirect(url_for('chat'))
    else:
        session.clear()
        return redirect(url_for('index'))

@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        session['character'] = request.form['character']
        return redirect(url_for('confirm'))
    return render_template('select.html')

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    username = session.get('username')
    character = session.get('character')
    if not (username and character):
        return redirect(url_for('index'))  # データがなければ最初に戻る

    data = character_data[character]
    if request.method == 'POST':
        if request.form.get('action') == '決定':
            return redirect(url_for('chat'))
        elif request.form.get('action') == 'やり直す':
            return redirect(url_for('select'))
    return render_template('confirm.html', username=username, character=character, images=data['images'])

# 会話をはじめるよ
from chiikawa_reply import reply as chiikawa_reply
from hachiware_reply import reply as hachiware_reply
from usagi_reply import reply as usagi_reply

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    character = session.get('character', 'ちいかわ')
    data = character_data[character]

    if 'history' not in session:
        session['history'] = [
            {'sender': 'character', 'type': 'text', 'content': data['greeting']}
        ]

    history = session['history']

    if request.method == 'POST':
        user_message = request.form['message']
        history.append({'sender': 'user', 'type': 'text', 'content': user_message})

        if character == "ちいかわ":
            reply_text = chiikawa_reply(user_message)
        elif character == "ハチワレ":
            reply_text = hachiware_reply(user_message)
        elif character == "うさぎ":
            reply_text = usagi_reply(user_message)
        else:
            reply_text = "うまく返せない…"

        if isinstance(reply_text, dict):
            reply_data = reply_text
        else:
            reply_data = {'type': 'text', 'content': reply_text}

        history.append({'sender': 'character', **reply_data})
        session['history'] = history
        return redirect(url_for('chat'))

    return render_template(
        'chat.html',
        history=history,
        character=data['label'],
        images=data['images'],
    )

@app.route('/reset_confirm', methods=['GET', 'POST'])
def reset_confirm():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'はい':
            return redirect(url_for('download_history'))
        else:
            session.clear()
            return redirect(url_for('index'))
    return render_template('reset_confirm.html')

@app.route('/download_history', methods=['GET', 'POST'])
def download_history():
    history = session.get('history', [])
    # ダウンロード処理（略：適宜実装）
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('index'))
    return render_template('download_done.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
