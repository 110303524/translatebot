from urllib.parse import parse_qsl, parse_qs
from line_chatbot_api import *

def set_in(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
            title='輸入語言?',
            text='請在下方點選翻譯前的語言',
            actions=[
                PostbackAction(
                    label="中文",
                    display_text="我想把中文",
                    data='action=0'
                ),
                PostbackAction(
                    label="英文",
                    display_text="我想把英文",
                    data='action=1'
                ),
                PostbackAction(
                    label="日文",
                    display_text="我想把日文",
                    data='action=2'
                ),
                PostbackAction(
                    label="韓文",
                    display_text="我想把韓文",
                    data='action=3'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def set_out(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
            title='輸出語言?',
            text='請在下方點選翻譯後的語言',
            actions=[
                PostbackAction(
                    label="中文",
                    display_text="翻成中文",
                    data='action=4'
                ),
                PostbackAction(
                    label="英文",
                    display_text="翻成英文",
                    data='action=5'
                ),
                PostbackAction(
                    label="日文",
                    display_text="翻成日文",
                    data='action=6'
                ),
                PostbackAction(
                    label="韓文",
                    display_text="翻成韓文",
                    data='action=7'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def computer(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
            title='選單',
            text='請在下方點選模式',
            actions=[
                MessageAction(
                    label="中翻英",
                    text="幫我翻成英文",
                ),
                MessageAction(
                    label="英翻中",
                    text="英文好難==",
                ),
                MessageAction(
                    label="更多語言",
                    text="還有嗎",
                ),
                MessageAction(
                    label="前往官網",
                    text="幫我翻成英文",
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)