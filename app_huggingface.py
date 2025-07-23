import os
from flask import Flask, request, render_template, jsonify
import requests
from dotenv import load_dotenv
import logging # エラーログを見やすくするために追加するよ

app = Flask(__name__)

# ログの設定をするよ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# APIのURLとヘッダーは変わらないよ
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def query_llama(prompt):
    payload = {"inputs": prompt}
    try:
        # APIにリクエストを送るよ。タイムアウトも設定しておくと安心だね
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        logging.info(f"Hugging Face APIレスポンスステータスコード: {response.status_code}")
        logging.info(f"Hugging Face APIレスポンス内容: {response.text}")

        # ステータスコードが200番台以外だったらエラーとして処理するよ
        response.raise_for_status()

        result = response.json()

        # レスポンスの形式がリストの場合と辞書の場合に対応するよ
        if isinstance(result, list) and result:
            # リストの最初の要素から'generated_text'を取得するよ
            generated_text = result[0].get('generated_text')
            if generated_text:
                # プロンプトが返答に含まれている場合があるので、それを除去するよ
                # Llama-3はプロンプト全体を返すことが多いから、ここで整形するんだ
                # プロンプトの最後の部分から返答が始まることを期待して処理するよ
                # ちいかわ: の後から取得するイメージだね
                if "ちいかわ:" in generated_text:
                    return generated_text.split("ちいかわ:", 1)[1].strip()
                return generated_text.strip()
            else:
                logging.warning(f"レスポンスに 'generated_text' が見つからないよ: {result}")
                return "ごめんね、うまくお話できないみたい...。"
        elif isinstance(result, dict) and 'generated_text' in result:
            # 辞書形式で直接'generated_text'がある場合
            generated_text = result['generated_text']
            if "ちいかわ:" in generated_text:
                return generated_text.split("ちいかわ:", 1)[1].strip()
            return generated_text.strip()
        elif isinstance(result, dict) and 'error' in result:
            # エラーメッセージが返ってきた場合
            logging.error(f"Hugging Face APIエラー: {result['error']}")
            return f"エラー: {result['error']}"
        else:
            # 想定外のレスポンス形式の場合
            logging.error(f"Hugging Face APIから予期せぬレスポンスが返ってきたよ: {result}")
            return f"ごめんね、予期せぬエラーが出ちゃったみたい...。詳細: {str(result)}"
    except requests.exceptions.Timeout:
        logging.error("Hugging Face APIへのリクエストがタイムアウトしたよ。")
        return "ごめんね、ちいかわがちょっと考えすぎちゃったみたい。もう一度話しかけてみてね！"
    except requests.exceptions.RequestException as e:
        # requestsライブラリ関連のエラーをキャッチするよ
        logging.error(f"Hugging Face APIへのリクエスト中にエラーが発生したよ: {e}")
        return f"APIとの通信でエラーが出ちゃったみたい...。詳細: {e}"
    except Exception as e:
        # その他の予期せぬエラーをキャッチするよ
        logging.error(f"予期せぬエラーが発生したよ: {e}", exc_info=True)
        return f"ごめんね、予期せぬエラーが出ちゃったみたい...。詳細: {e}"

@app.route("/chat")
def chat():
    # ask.htmlをレンダリングするよ
    return render_template("ask.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.form.get("message")
    if not user_msg:
        return jsonify({"reply": "メッセージが空だよ！"}), 400

    # プロンプトを調整するよ。より明確にちいかわのキャラクター設定を伝えるんだ
    prompt = (
        "あなたは『ちいかわ』というキャラクターです。一人称は「ちいかわ」です。"
        "ユーザーの名前は『ゆみたちゃん』です。ゆみたちゃんに優しく、短く、可愛らしい言葉で返事してください。"
        "語尾に「〜だもん」や「〜だよ」などをつけてね。"
        "「むり」という言葉に対しては、絵文字の「:stamp-muri:」を返してね。他の絵文字も使っていいよ。"
        "ユーザーのメッセージ全体を理解し、それに対してちいかわらしく返事してください。\n"
        f"ユーザー: {user_msg}\nちいかわ:"
    )
    logging.info(f"生成されたプロンプト: {prompt}")
    ai_reply = query_llama(prompt)
    logging.info(f"AIの返信: {ai_reply}")
    return jsonify({"reply": ai_reply})

@app.route("/")
def index():
    # ルートURLにアクセスしたら、チャットページへのリンクを表示するよ
    return "<a href='/chat' class='text-blue-500 hover:underline'>ちいかわAIチャットを開く</a>"

if __name__ == "__main__":
    # デバッグモードでアプリを実行するよ
    app.run(debug=True)
