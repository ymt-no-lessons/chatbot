import os
from flask import Flask, request, render_template, jsonify
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def query_llama(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        print("レスポンス内容:", response.text)
        print("HTTPステータスコード:", response.status_code)
        result = response.json()
        if isinstance(result, list):
            return result[0].get('generated_text', str(result))
        elif isinstance(result, dict) and 'generated_text' in result:
            return result['generated_text']
        elif isinstance(result, dict) and 'error' in result:
            return f"エラー: {result['error']}"
        else:
            return str(result)
    except Exception as e:
        return f"APIエラー: {e}"

@app.route("/chat")
def chat():
    return render_template("ask.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.form.get("message")
    prompt = (
        "あなたは『ちいかわ』というキャラです。"
        "ユーザーの名前は『ゆみたちゃん』です。"
        "やさしく短く返事してください。"
        "「むり」と言われたら :stamp-muri: を返してね。\n"
        f"ユーザー: {user_msg}\nちいかわ:"
    )
    ai_reply = query_llama(prompt)
    return jsonify({"reply": ai_reply})

@app.route("/")
def index():
    return "<a href='/chat'>ちいかわAIチャットを開く</a>"

if __name__ == "__main__":
    app.run(debug=True)
