from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HEADERS = {"Authorization": "Bearer あなたのアクセストークン"}

def query_llama(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()[0]["generated_text"]

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.form["message"]
    user_name = "ゆみたちゃん"  # 実際はセッションから取得
    prompt = f"あなたは『ちいかわ』というキャラです。ユーザーの名前は『{user_name}』です。短くかわいく返事して。むりって言われたら:stamp-muri:を返してね。\nユーザー「{user_name}」: {user_msg}\nちいかわ:"
    ai_reply = query_llama(prompt)
    return jsonify({"reply": ai_reply})

# index.htmlなどUI部分は省略
if __name__ == "__main__": app.run() 