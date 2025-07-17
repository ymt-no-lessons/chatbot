from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HEADERS = {"Authorization": "Bearer あなたのアクセストークン"}

def query_llama(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()[0]["generated_text"]

@app.route("/chat")
def chat():
    return render_template("ask.html")

# index.htmlなどUI部分は省略
if __name__ == "__main__": app.run() 