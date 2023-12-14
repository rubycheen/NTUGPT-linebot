# from flask import Flask, request, abort
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import *
# import os
# from dotenv import load_dotenv
# load_dotenv()

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

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    app.run()