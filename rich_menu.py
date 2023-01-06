import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)

# ## 創建選單
# headers = {"Authorization":"Bearer g2Xu3SbUavRYhHTPiFZFVtzavk+dyDsn+1i292ussoB/YEg+MuIC1nOMKVCsbp9bGNzYu7gL4mFNrR9Y7Z1/oW+9U3XAp7EcpQW9NXEjHJMN+hbNxyzO7y7A6qzDUU4xfpM0dV1P2j8rFdmM1+JJGwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
# body = {
#     "size": {"width": 2500, "height": 1686},
#     "selected": "true",
#     "name": "Controller",
#     "chatBarText": "Controller",
#     "areas":[
#         {
#           "bounds": {"x": 0, "y": 0, "width": 1250, "height": 843},
#           "action": {"type": "message", "text": "幫我翻成英文"}
#         },
#         {
#           "bounds": {"x": 1250, "y": 0, "width": 1250, "height": 843},
#           "action": {"type": "message", "text": "英文好難=="}
#         },
#         {
#           "bounds": {"x": 0, "y": 843, "width": 1250, "height": 843},
#           "action": {"type": "message", "text": "還有嗎"}
#         },
#         {
#           "bounds": {"x": 1250, "y": 843, "width": 1250, "height": 843},
#           "action": {"type": "uri", "uri": "https://www.ncu.edu.tw"}
#         }
#     ]
#   }
# req_1= requests.request('POST', 'https://api.line.me/v2/bot/richmenu', headers=headers,data=json.dumps(body).encode('utf-8'))
# print(req_1.text)

## 設定選單圖片
line_bot_api = LineBotApi('g2Xu3SbUavRYhHTPiFZFVtzavk+dyDsn+1i292ussoB/YEg+MuIC1nOMKVCsbp9bGNzYu7gL4mFNrR9Y7Z1/oW+9U3XAp7EcpQW9NXEjHJMN+hbNxyzO7y7A6qzDUU4xfpM0dV1P2j8rFdmM1+JJGwdB04t89/1O/w1cDnyilFU=')
with open("./static/images/選單圖片.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-0d234cdc2c5e4f9608b0a40846b4b812", "image/jpeg", f)

##　啟用
headers = {"Authorization":"Bearer g2Xu3SbUavRYhHTPiFZFVtzavk+dyDsn+1i292ussoB/YEg+MuIC1nOMKVCsbp9bGNzYu7gL4mFNrR9Y7Z1/oW+9U3XAp7EcpQW9NXEjHJMN+hbNxyzO7y7A6qzDUU4xfpM0dV1P2j8rFdmM1+JJGwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
req_2 = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-0d234cdc2c5e4f9608b0a40846b4b812', headers=headers)
print(req_2.text)


