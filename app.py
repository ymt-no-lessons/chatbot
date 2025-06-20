from flask import Flask, render_template, request, redirect, url_for, session
from character_data import character_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 任意の文字列でOK

# 1. 名前入力画面を出すよ
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('select'))
    return render_template('index.html')

# 2. キャラ選択画面を出すよ
@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        session['character'] = request.form['character']
        return redirect(url_for('confirm'))
    return render_template('select.html')

# 3. 確認画面（画像＋名前）を出すよ
@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    username = session.get('username')
    character = session.get('character')
    character_data = {
        'ちいかわ': {'images': ['images/chiikawa01.png', 'images/chiikawa02.png'], 'label': 'ちいかわ'},
        'ハチワレ': {'images': ['images/hachiware01.png','images/hachiware02.png'], 'label': 'ハチワレ'},
        'うさぎ': {'images': ['images/usagi01.png','images/usagi02.png'], 'label': 'うさぎ'}
    }
    
    if not (username and character):
        return redirect(url_for('index'))  # データがなければ最初に戻る

    if request.method == 'POST':
        if request.form.get('action') == '決定':
            # チャット画面へリダイレクト！
            return redirect(url_for('chat'))
        elif request.form.get('action') == 'やり直す':
            return redirect(url_for('select'))


    data = character_data[character]
    return render_template('confirm.html', username=username, character=character, images=data['images'])


# キャラクターごとの会話を読み込むよ
from chiikawa_reply import reply as chiikawa_reply
from hachiware_reply import reply as hachiware_reply
from usagi_reply import reply as usagi_reply

# 会話をはじめるよ
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    character = session.get('character', 'ちいかわ')
    data = character_data[character]

    if 'history' not in session:
        session['history'] = [
            {'sender': 'character', 'text': 'やあ、こんにちは！'}
        ]
    history = session['history']

    if request.method == 'POST':
        user_message = request.form['message']
        history.append({'sender': 'user', 'text': user_message})

        # キャラごとにリプライ関数を呼ぶ
        if character == "ちいかわ":
            reply_text = chiikawa_reply(user_message)
        elif character == "ハチワレ":
            reply_text = hachiware_reply(user_message)
        elif character == "うさぎ":
            reply_text = usagi_reply(user_message)
        else:
            reply_text = "うまく返せない…"

        # リプライを履歴に追加
        history.append({
            'sender': 'character',
            'type': 'text',
            'content': reply_text
        })

    return render_template(
        'chat.html',
        history=history,
        character=data['label'],
        images=data['images'],
        replies=data['replies']
    )

if __name__ == '__main__':
    app.run(debug=True)

