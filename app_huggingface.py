import os
from flask import Flask, request, render_template, jsonify
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# .env読み込み
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"  # ←ここ大事
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def query_llama(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        result = response.json()
        # モデルによって返却形式が違う場合があるので注意
        if isinstance(result, list):
            # モデルによってはこう返ってくる
            return result[0]['generated_text']
        elif isinstance(result, dict) and 'generated_text' in result:
            return result['generated_text']
        elif isinstance(result, dict) and 'error' in result:
            return f"エラー: {result['error']}"
        else:
            # 万一フォーマット違い
            return str(result)
    except Exception as e:
        return f"APIエラー: {e}"

# チャット画面
@app.route("/chat")
def chat():
    return render_template("ask.html")

# AIへの質問
@app.route("/ask", methods=["POST"])
def ask():
    # JS側から「application/x-www-form-urlencoded」なら
    user_msg = request.form.get("message")
    # AIへのプロンプトを構築
    # 必要に応じて名前やキャラを変更
    prompt = (
        "あなたは『ちいかわ』というキャラです。"
        "ユーザーの名前は『ゆみたちゃん』です。"
        "やさしく短く返事してください。"
        "「むり」と言われたら :stamp-muri: を返してね。\n"
        f"ユーザー: {user_msg}\nちいかわ:"
    )
    ai_reply = query_llama(prompt)
    return jsonify({"reply": ai_reply})

# 最低限のトップページも追加（必要に応じてカスタム）
@app.route("/")
def index():
    return "<a href='/chat'>ちいかわAIチャットを開く</a>"

if __name__ == "__main__":
    # 本番環境では「debug=False」に！
    app.run(debug=True)
