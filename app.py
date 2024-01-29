from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

import os
import openai
import requests

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

app = Flask(__name__)
url = 'https://9fad-140-112-90-16.ngrok-free.app/predict'
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    data = {'prompt': event.message.text}
    response = requests.post(url, json=data).text

    answer = response.split('"answer":"')[1].split('"')[0]
    urls = ''
    for idx in range(4, len(response.split('"answer":"')[1].split('"')), 2):
        urls+=response.split('"answer":"')[1].split('"')[idx]+'\n'
    result = answer+'\n參考網頁:\n\n'+ urls

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))


if __name__ == "__main__":
    app.run()