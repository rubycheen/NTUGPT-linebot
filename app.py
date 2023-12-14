# from flask import Flask, request, abort
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import *
# import os
# # from dotenv import lo_dotenv
# # load_dotenv()

# app = Flask(__name__)

# # print(os.environ['CHANNEL_ACCESS_TOKEN'])
# # print(os.environ['CHANNEL_SECRET'])

# # line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
# # handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
# line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
# handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
# html = '''
# <!doctype html>
# <html>
#   <head>
#     <link rel="shortcut icon" href="/favicon.ico">
#     <title>Hello world!</title>
#   </head>
#   <body>
#     <p>Hello world!</p>
#   </body>
# </html>
# '''

# @app.route('/', methods=['GET'])
# def index():
#     return html

# @app.route("/callback", methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)
#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(event.reply_token, message)

# import os
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 12345))
#     app.run(host='0.0.0.0', port=port)

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

import os


app = Flask(__name__)

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()