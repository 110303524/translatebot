from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage, 
    ImageSendMessage, 
    StickerSendMessage, 
    LocationSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    DatetimePickerAction,
    ConfirmTemplate
)

line_bot_api = LineBotApi('g2Xu3SbUavRYhHTPiFZFVtzavk+dyDsn+1i292ussoB/YEg+MuIC1nOMKVCsbp9bGNzYu7gL4mFNrR9Y7Z1/oW+9U3XAp7EcpQW9NXEjHJMN+hbNxyzO7y7A6qzDUU4xfpM0dV1P2j8rFdmM1+JJGwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2c3a7a529fe4cc2b048a516a8607f1d5')


