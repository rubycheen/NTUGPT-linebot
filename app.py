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
url = 'https://dcde-140-112-90-16.ngrok-free.app/predict'
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

# Langchain 串接 OpenAI ，這裡 model 可以先選 gpt-3.5-turbo
# llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

# # 透過 ConversationBufferWindowMemory 快速打造一個具有「記憶力」的聊天機器人，可以記住至少五回。
# # 通常來說 5 回還蠻夠的
# memory = ConversationBufferWindowMemory(k=5)
# conversation = ConversationChain(
#     llm=llm,
#     memory=memory,
#     verbose=False
# )


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
    response = requests.post(url, json=data)
    # result = conversation.predict(input=event.message.text)  # 使用模型實例進行預測
    result = f"{response['answer']}\n參考資料：\n{response['urls']}"
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=))
        TextSendMessage(text=result.text))


if __name__ == "__main__":
    app.run()