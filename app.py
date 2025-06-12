from flask import Flask, render_template, request, redirect, url_for, session
from character_data import character_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 任意の文字列でOK

# 1. 名前入力画面
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('select'))
    return render_template('index.html')

# 2. キャラ選択画面
@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        session['character'] = request.form['character']
        return redirect(url_for('confirm'))
    return render_template('select.html')

# 3. 確認画面（画像＋名前）
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

# 仮の会話をはじめるよ
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # characterデータの取得（confirmと同じように！）
    character = session.get('character', 'ちいかわ')
    character_data = {
        'ちいかわ': {'images': ['images/chiikawa01.png', 'images/chiikawa02.png'], 'label': 'ちいかわ'},
        'ハチワレ': {'images': ['images/hachiware01.png','images/hachiware02.png'], 'label': 'ハチワレ'},
        'うさぎ': {'images': ['images/usagi01.png','images/usagi02.png'], 'label': 'うさぎ'}
    }
    data = character_data[character]

    if 'history' not in session:
        session['history'] = [
            {'sender': 'character', 'text': 'やあ、こんにちは！'}
        ]
    history = session['history']

    if request.method == 'POST':
        # 送信されたメッセージを受け取る
        user_message = request.form['message']
        # 履歴にユーザーの発言を追加
        history.append({'sender': 'user', 'text': user_message})
        # キャラの自動返事（まずは1パターン固定）
        history.append({'sender': 'character', 'text': 'うんうん、そうなんだね！'})
        # セッションに保存し直す
        session['history'] = history

    character = 'ちいかわ'
    images = 'images/chiikawa01.png'

    return render_template(
    'chat.html',
    history=history,
    character=data['label'],   # キャラ名
    images=data['images'],     # 画像リスト
    replies=data['replies']    # セリフリスト
)


if __name__ == '__main__':
    app.run(debug=True)

