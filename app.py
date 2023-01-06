from flask import Flask, request, abort, url_for
from urllib.parse import parse_qsl, parse_qs
from linebot.models import events
from line_chatbot_api import *
from function.translate import *
from function.image import *
from function.setting import *
from function.audio import *
import re

# create flask server
app = Flask(__name__)

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

# handle msg
@handler.add(PostbackEvent)
def handle_postback(event):
    l_list=["zh-Hant","en","ja","ko"]
    postback_data = dict(parse_qsl(event.postback.data))
    print(postback_data.get('action'))
    for n in range(0,4):
        if postback_data.get('action')==f'{n}':
            f = open('./static/temp_language.txt', 'w')
            f.write(l_list[n]+"\n")
            f.close()
            set_out(event)
    for n in range(4,8):
        if postback_data.get('action')==f'{n}':
            f = open('./static/temp_language.txt', 'a')
            f.write(l_list[n-4])
            f.close()
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = '請在聊天室放上想翻的內容'))       
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type == "text":
        if event.message.text=='幫我翻成英文':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "輸入中文吧"))
            f = open('./static/temp_language.txt', 'w')
            f.write("zh-Hant\n")
            f.write("en")
            f.close()
        elif event.message.text=='英文好難==':
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "輸入英文吧"))
            f = open('./static/temp_language.txt', 'w')
            f.write("en\n")
            f.write("zh-Hant")
            f.close()
        elif event.message.text=='還有嗎':
            set_in(event)
        elif event.message.text=='電腦版':
            computer(event)
        else :
            recrive_text=event.message.text
            print(recrive_text)
            with open('./static/temp_language.txt', 'r') as f:
                line = f.readline().replace('\n','') #去掉換行
                l=[]
                while line:
                    l.append(line)
                    line = f.readline().replace('\n','') #去掉換行
            translate(event,recrive_text,l[0],l[1])
    elif event.message.type == "image":
        message_content = line_bot_api.get_message_content(event.message.id)
        with open('./static/images/temp_image.png', 'wb') as f:
            for chunk in message_content.iter_content():
                f.write(chunk)
        ul = url_for('static', filename='images/temp_image.png', _external=True)
        text = image(ul)
        print("==================")
        print(text)
        print("==================")
        with open('./static/temp_language.txt', 'r') as f:
            line = f.readline().replace('\n','') #去掉換行
            l=[]
            while line:
                l.append(line)
                line = f.readline().replace('\n','') #去掉換行
        translate(event,text,l[0],l[1])
    elif event.message.type == "audio":
        name_mp3 = './static/temp_recording.mp3'
        name_wav = './static/temp_recording.wav'
        message_content = line_bot_api.get_message_content(event.message.id)
        with open(name_mp3, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        
        os.system('ffmpeg -y -i ' + name_mp3 + ' ' + name_wav + ' -loglevel quiet')
        result = transcribe(name_wav)
        print('Transcribe:', result)
        with open('./static/temp_language.txt', 'r') as fd:
            line = fd.readline().replace('\n','') #去掉換行
            l=[]
            while line:
                l.append(line)
                line = fd.readline().replace('\n','') #去掉換行
        translate(event,result,l[0],l[1])

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)